"""Server contract tests. Uses a local fake executable, never an AI model."""
import http.client
import json
from pathlib import Path
import sys
import tempfile
import threading
import time
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import evolution_office_server as server


class ComposerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "office").mkdir()
        (self.root / "office/config.json").write_text(json.dumps({"agents": [{"id": "eva"}, {"id": "user"}], "objectives": [{"id": "construction"}]}))
        (self.root / "office/dashboard.html").write_text('<html>__OFFICE_DATA__</html>')
        self.fake = self.root / "fake-codex"
        self.fake.write_text('#!' + sys.executable + '\n' + '''import json,sys,time
from pathlib import Path
prompt=sys.stdin.read()
Path("received-args.json").write_text(json.dumps(sys.argv[1:]))
if "WAIT_TEST" in prompt: time.sleep(0.4)
if "TIMEOUT_TEST" in prompt: time.sleep(20)
if "FAIL_TEST" in prompt:
    print("credential=DO_NOT_EXPOSE",file=sys.stderr)
    sys.exit(3)
print(json.dumps({"type":"item.completed","item":{"type":"agent_message","text":"Resultado real del ejecutable de prueba"}}))
''')
        self.fake.chmod(0o700)
        self.runtime = server.OfficeRuntime(self.root, self.fake, timeout=60)
        self.http = server.make_server(self.runtime, 0)
        self.thread = threading.Thread(target=self.http.serve_forever, daemon=True)
        self.thread.start()
        self.host = '127.0.0.1:' + str(self.http.server_port)

    def tearDown(self):
        self.http.shutdown()
        self.runtime.shutdown()
        self.http.server_close()
        self.thread.join(2)
        self.temp.cleanup()

    def call(self, method, path, payload=None, headers=None):
        conn = http.client.HTTPConnection('127.0.0.1', self.http.server_port, timeout=5)
        h = {'Host': self.host}
        if method == 'POST':
            h.update({'Origin': 'http://' + self.host, 'Content-Type': 'application/json', 'X-Office-Token': self.runtime.token})
        if headers:
            h.update(headers)
        body = json.dumps(payload) if payload is not None else None
        conn.request(method, path, body=body, headers=h)
        response = conn.getresponse()
        data = response.read().decode()
        status = response.status
        conn.close()
        try:
            data = json.loads(data)
        except ValueError:
            pass
        return status, data

    def wait(self, job_id):
        end = time.monotonic() + 65
        while time.monotonic() < end:
            job = self.runtime.jobs[job_id]
            if job['status'] in {'completed', 'failed'} and self.runtime.active is None:
                return job
            time.sleep(.02)
        self.fail('fake execution did not finish')

    def test_success_records_request_response_and_safe_arguments(self):
        status, data = self.call('POST', '/api/messages', {'request_id': 'success-0001', 'message': 'hola $(touch injected)'})
        self.assertEqual(status, 202)
        job = self.wait(data['job']['id'])
        self.assertEqual(job['status'], 'completed', job)
        events = [json.loads(x) for x in (self.root / 'office/events.jsonl').read_text().splitlines()]
        self.assertEqual([(x['from'], x['to'], x['status']) for x in events], [('user', 'eva', 'DISPATCHED'), ('eva', 'user', 'RECORDED')])
        self.assertEqual(events[1]['reply_to'], events[0]['id'])
        self.assertFalse((self.root / 'injected').exists())
        self.assertEqual(json.loads((self.root / 'received-args.json').read_text()), ['exec', '--json', '--approve-for-me', '-C', str(self.root.resolve()), '-'])
        self.assertTrue((self.root / events[1]['evidence'][0]).is_file())

    def test_idempotency_and_busy(self):
        payload = {'request_id': 'waiting-0001', 'message': 'WAIT_TEST'}
        self.assertEqual(self.call('POST', '/api/messages', payload)[0], 202)
        self.assertEqual(self.call('POST', '/api/messages', payload)[0], 200)
        self.assertEqual(self.call('POST', '/api/messages', {**payload, 'message': 'changed'})[0], 409)
        self.assertEqual(self.call('POST', '/api/messages', {**payload, 'request_id': 'waiting-0002'})[0], 409)
        self.wait('waiting-0001')
        self.assertEqual(len((self.root / 'office/events.jsonl').read_text().splitlines()), 2)

    def test_host_origin_token_and_job_auth(self):
        payload = {'request_id': 'denied-0001', 'message': 'hello'}
        for headers in ({'Host': 'attacker.test'}, {'Origin': 'https://attacker.test'}, {'X-Office-Token': ''}, {'Sec-Fetch-Site': 'cross-site'}):
            self.assertEqual(self.call('POST', '/api/messages', payload, headers)[0], 403)
        self.assertEqual(self.call('GET', '/api/jobs/unknown-job')[0], 403)
        status, session = self.call('GET', '/api/session')
        self.assertEqual(status, 200)
        self.assertEqual(session['token'], self.runtime.token)
        self.assertIsNone(session['active_job'])
        self.assertEqual(self.call('GET', '/api/session', headers={'Host': 'localhost:' + str(self.http.server_port)})[0], 200)
        self.assertEqual(len(self.runtime.jobs), 0)

    def test_input_limits_and_shapes(self):
        for payload in ({'request_id': '../escape', 'message': 'hello'}, {'request_id': 'invalid-0001', 'message': ''}, {'request_id': 'invalid-0001', 'message': 'x' * 8001}, [], {'request_id': 'invalid-0001', 'message': 'hi', 'extra': True}):
            self.assertEqual(self.call('POST', '/api/messages', payload)[0], 400)
        self.assertEqual(self.call('POST', '/api/messages', {'request_id': 'oversize-001', 'message': 'x' * 40000})[0], 413)

    def test_failure_is_not_success_and_logs_are_not_served(self):
        self.call('POST', '/api/messages', {'request_id': 'failure-0001', 'message': 'FAIL_TEST'})
        job = self.wait('failure-0001')
        self.assertEqual(job['status'], 'failed')
        status, body = self.call('GET', '/api/jobs/failure-0001', headers={'X-Office-Token': self.runtime.token})
        self.assertEqual(status, 200)
        self.assertNotIn('DO_NOT_EXPOSE', json.dumps(body))
        self.assertEqual(self.call('GET', '/output/office-runtime/jobs/failure-0001/logs.json')[0], 404)
        events = [json.loads(x) for x in (self.root / 'office/events.jsonl').read_text().splitlines()]
        self.assertEqual(events[-1]['status'], 'FAIL')

    def test_timeout_stops_process(self):
        self.runtime.timeout = .1
        self.call('POST', '/api/messages', {'request_id': 'timeout-0001', 'message': 'TIMEOUT_TEST'})
        job = self.wait('timeout-0001')
        self.assertEqual(job['status'], 'failed')
        self.assertIn('tiempo', job['error'])
        self.assertFalse(self.runtime.processes)

    def test_allowlist_blocks_files_and_symlinks(self):
        (self.root / 'secret.txt').write_text('secret')
        (self.root / 'office/dist').mkdir(exist_ok=True)
        (self.root / 'office/dist/index.html').symlink_to(self.root / 'secret.txt')
        for route in ('/', '/secret.txt', '/.git/config', '/%2e%2e/secret.txt'):
            self.assertEqual(self.call('GET', route)[0], 404)

    def test_single_runtime_and_restart_idempotency(self):
        with self.assertRaises(RuntimeError):
            server.OfficeRuntime(self.root, self.fake)
        self.call('POST', '/api/messages', {'request_id': 'restart-0001', 'message': 'hello'})
        self.wait('restart-0001')
        self.runtime.shutdown()
        replacement = server.OfficeRuntime(self.root, self.fake)
        try:
            job, created = replacement.submit('restart-0001', 'hello')
            self.assertFalse(created)
            self.assertEqual(job['status'], 'completed', job)
        finally:
            replacement.shutdown()


if __name__ == '__main__':
    unittest.main()
