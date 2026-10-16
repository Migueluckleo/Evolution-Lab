"""Streaming regressions; local fake subprocesses only, no model or live server."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import unittest
from unittest.mock import patch

import test_server as fixtures
import evolution_office_server as server


class StreamingTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ComposerTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.runtime = self.fixture.runtime
        self.root = self.fixture.root
        self.fake = self.fixture.fake

    def program(self, code):
        self.fake.write_text('#!' + sys.executable + '\n' + code)

    def post(self, ident='streaming-0001'):
        status, body = self.fixture.call('POST', '/api/messages', {'request_id': ident, 'message': 'request'})
        self.assertEqual(status, 202)
        return body['job']['id']

    def observe(self, predicate, timeout=30):
        end = time.monotonic() + timeout
        while time.monotonic() < end:
            if predicate():
                return
            time.sleep(.02)
        self.fail('Expected streaming state did not arrive')

    def test_chunked_unicode_progress_during_running_and_reload(self):
        self.program('''import sys,json,os,time
from pathlib import Path
sys.stdin.read()
e={"type":"item.completed","item":{"id":"visible-1","type":"agent_message","text":"Encontré documentación útil: diseño ☀️"}}
b=(json.dumps(e,ensure_ascii=False)+"\\n").encode()
cut=b.index("☀".encode())+1
os.write(1,b[:cut]);time.sleep(.05);os.write(1,b[cut:])
# Reasoning and raw tool output must never enter public progress.
print(json.dumps({"type":"item.completed","item":{"id":"private-1","type":"reasoning","text":"PRIVATE_REASONING"}}),flush=True)
print(json.dumps({"type":"item.started","item":{"id":"command-1","type":"command_execution","command":"SECRET_ARGUMENT","aggregated_output":"SECRET_OUTPUT"}}),flush=True)
# Duplicate event must not add another bubble.
os.write(1,b)
end=time.monotonic()+30
while not Path("release-test").exists() and time.monotonic()<end: time.sleep(.02)
print(json.dumps({"type":"item.completed","item":{"id":"final-1","type":"agent_message","text":"Entrega final"}}),flush=True)
''')
        job_id = self.post()
        self.observe(lambda: len(self.runtime.jobs[job_id].get('updates', [])) >= 2)
        job = self.runtime.jobs[job_id]
        self.assertEqual(job['status'], 'running')
        public = self.runtime.public(job)
        visible = [x for x in public['updates'] if x['kind'] == 'message']
        self.assertEqual(len(visible), 1)
        self.assertEqual(visible[0]['message'], 'Encontré documentación útil: diseño ☀️')
        self.assertNotIn('PRIVATE_REASONING', json.dumps(public))
        self.assertNotIn('SECRET_ARGUMENT', json.dumps(public))
        self.assertNotIn('SECRET_OUTPUT', json.dumps(public))
        persisted = json.loads((self.runtime.folder / job_id / 'job.json').read_text())
        self.assertEqual(persisted['updates'], public['updates'])
        status, session = self.fixture.call('GET', '/api/session')
        self.assertEqual(status, 200)
        self.assertEqual(session['last_job']['id'], job_id)
        self.assertEqual(session['active_job']['updates'], public['updates'])
        self.assertTrue(session['server_now'])
        (self.root / 'release-test').write_text('go')
        final = self.fixture.wait(job_id)
        self.assertEqual(final['result'], 'Entrega final', final)
        events = [json.loads(x) for x in (self.root / 'office/events.jsonl').read_text().splitlines()]
        self.assertEqual(len([x for x in events if x['kind'] == 'response']), 1)
        self.assertEqual(events[-1]['status'], 'RECORDED')

    def test_timeout_keeps_public_progress_and_drains_both_logs(self):
        self.runtime.timeout = 2
        self.program('''import sys,json,time,os
from pathlib import Path
Path("runner-ready").write_text("ready")
sys.stdin.read()
print(json.dumps({"type":"item.completed","item":{"id":"progress","type":"agent_message","text":"Resultado parcial"}}),flush=True)
os.write(2,b"PRIVATE_STDERR"*10000)
time.sleep(20)
''')
        # Start the interpreter before timing streaming, so OS launch latency cannot
        # turn a "preserve existing progress" check into a "no output yet" check.
        proc = subprocess.Popen([str(self.fake)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", start_new_session=True, cwd=self.root)
        self.addCleanup(lambda: self.runtime.terminate(proc) if proc.poll() is None else None)
        self.observe(lambda: (self.root / "runner-ready").exists())
        job_id = 'timeout-stream-01'
        job = {"id": job_id, "request_id": job_id, "status": "running", "message": "request", "result": None, "error": None, "updates": []}
        (self.runtime.folder / job_id).mkdir()
        job['event_id'] = self.runtime.event(job)
        self.runtime.jobs[job_id] = job
        self.runtime.processes[job_id] = proc
        self.runtime.active = job_id
        self.runtime.run(job, proc, 'request')
        final = self.runtime.jobs[job_id]
        self.assertEqual(final['status'], 'failed', final)
        self.assertIn('tiempo', final['error'])
        self.assertTrue(any(x['message'] == 'Resultado parcial' for x in final['updates']))
        logs = json.loads((self.runtime.folder / job_id / 'logs.json').read_text())
        self.assertIn('Resultado parcial', logs['stdout'])
        self.assertEqual(logs['stderr'], 'PRIVATE_STDERR' * 10000)
        self.assertNotIn('PRIVATE_STDERR', json.dumps(self.runtime.public(final)))
        self.assertFalse(self.runtime.processes)

    def test_known_delegation_shape_no_names_from_prompt_and_dedup(self):
        job = {'id': 'consume-shapes-01', 'updates': []}
        with patch.object(self.runtime, 'persist'):
            event = {'type': 'item.completed', 'item': {'id': 'collab-1', 'type': 'collab_agent_tool_call', 'tool': 'send_message', 'receiver_thread_ids': ['real-thread-123'], 'prompt': 'SECRET_PROMPT', 'agents_states': {'fake-name': 'PRIVATE_RESULT'}}}
            self.runtime.consume(job, event)
            self.runtime.consume(job, event)
            self.runtime.consume(job, {'type': 'item.completed', 'item': {'id': 'hidden', 'type': 'agent_message', 'channel': 'analysis', 'text': 'PRIVATE_REASONING'}})
            self.runtime.consume(job, {'type': 'item.started', 'item': {'id': 'unknown', 'type': 'collab_agent_tool_call', 'tool': 'unrecognized', 'receiver_thread_ids': ['should-not-map']}})
        self.assertEqual(len(job['updates']), 2)
        self.assertEqual(job['updates'][0]['kind'], 'delegation')
        self.assertEqual(job['updates'][0]['actor'], 'eva')
        self.assertEqual(job['updates'][0]['tool_ref']['receiver_thread_ids'], ['real-thread-123'])
        self.assertEqual(job['updates'][1]['kind'], 'activity')
        self.assertNotIn('tool_ref', job['updates'][1])
        self.assertNotIn('SECRET_PROMPT', json.dumps(job))
        self.assertNotIn('PRIVATE_RESULT', json.dumps(job))
        self.assertNotIn('PRIVATE_REASONING', json.dumps(job))

    def test_wait_error_does_not_drop_messages_or_leave_worker_busy(self):
        self.program('''import sys,json
sys.stdin.read()
print(json.dumps({"type":"item.completed","item":{"id":"progress","type":"agent_message","text":"Avance conservado"}}),flush=True)
''')
        original_wait = subprocess.Popen.wait
        def wait(proc, *args, **kwargs):
            result = original_wait(proc, *args, **kwargs)
            if getattr(proc, '_stream_wait_failed', False):
                return result
            proc._stream_wait_failed = True
            raise OSError('PRIVATE_WAIT_ERROR')
        with patch.object(subprocess.Popen, 'wait', wait):
            job_id = self.post('wait-error-0001')
            final = self.fixture.wait(job_id)
        self.assertEqual(final['status'], 'failed', final)
        self.assertTrue(any(x['message'] == 'Avance conservado' for x in final['updates']))
        self.assertNotIn('PRIVATE_WAIT_ERROR', json.dumps(self.runtime.public(final)))
        self.assertFalse(self.runtime.processes)


if __name__ == '__main__':
    unittest.main()
