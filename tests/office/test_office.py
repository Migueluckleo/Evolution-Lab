"""Office ledger and inert-dashboard regressions. Every write uses a temporary root."""
import concurrent.futures
from contextlib import redirect_stderr
import importlib.util
import io
import json
from html.parser import HTMLParser
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("evolution_office", ROOT / "scripts/evolution_office.py")
office = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(office)


class Scripts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.current = None
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag == "script":
            self.current = {"attrs": dict(attrs), "data": ""}
            self.blocks.append(self.current)

    def handle_endtag(self, tag):
        if tag == "script":
            self.current = None

    def handle_data(self, data):
        if self.current is not None:
            self.current["data"] += data


class OfficeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name).resolve()
        self.root = self.base / "repo"
        (self.root / "office").mkdir(parents=True)
        for name in ("config.json", "dashboard.html"):
            shutil.copyfile(ROOT / "office" / name, self.root / "office" / name)
        (self.root / "qa").mkdir()
        (self.root / "qa/proof.md").write_text("Independent evidence fixture")
        self.config = json.loads((self.root / "office/config.json").read_text())

    def payload(self, kind="note", **changes):
        event = dict(kind=kind, **{"from": "eva", "to": "vera"},
                     message="Verify the artifact", why="Independent QA", scope="Fixture only",
                     deliverable="Evidence report", objective="maintenance",
                     status="DISPATCHED" if kind == "request" else "RECORDED", evidence=[])
        event.update(changes)
        return event

    def record(self, payload):
        return office.record(payload, self.root)

    def request(self):
        return self.record(self.payload("request"))

    def response(self, request, **changes):
        event = self.payload("response", **{"from": "vera", "to": "eva"},
                             reply_to=request, status="PASS", evidence=["qa/proof.md"])
        event.update(changes)
        return event

    def test_append_preserves_prior_events_and_hash_chain(self):
        first = self.record(self.payload(id="first"))
        before = (self.root / "office/events.jsonl").read_bytes()
        second = self.record(self.payload(id="second"))
        self.assertTrue((self.root / "office/events.jsonl").read_bytes().startswith(before))
        _, events = office.load(self.root)
        self.assertEqual([e["id"] for e in events], [first, second])
        self.assertIsNone(events[0]["previous"])
        self.assertEqual(events[1]["previous"], events[0]["sha256"])
        self.assertEqual(events[1]["sha256"], office.digest(events[1]))
        self.assertTrue((self.root / "office/dist/index.html").is_file())

    def test_parallel_appends_are_not_lost(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            ids = list(pool.map(lambda i: self.record(self.payload(id=f"event-{i}")), range(12)))
        _, events = office.load(self.root)
        self.assertEqual(len(events), 12)
        self.assertEqual({e["id"] for e in events}, set(ids))

    def test_mutating_historical_message_breaks_validation(self):
        self.record(self.payload())
        _, events = office.load(self.root)
        events[0]["message"] = "Changed after recording"
        with self.assertRaisesRegex(ValueError, "cadena"):
            office.validate(self.config, events, self.root)

    def test_duplicate_id_does_not_modify_ledger(self):
        self.record(self.payload(id="same"))
        before = (self.root / "office/events.jsonl").read_bytes()
        with self.assertRaisesRegex(ValueError, "duplicada"):
            self.record(self.payload(id="same"))
        self.assertEqual((self.root / "office/events.jsonl").read_bytes(), before)

    def test_response_links_request_and_reverses_participants(self):
        request = self.request()
        self.record(self.response(request))
        config, events = office.load(self.root)
        self.assertEqual(office.validate(config, events, self.root), {request})
        self.assertEqual(events[1]["reply_to"], events[0]["id"])

    def test_wrong_participants_or_objective_do_not_answer(self):
        request = self.request()
        for changes in ({"from": "atlas"}, {"to": "atlas"}, {"objective": "efficiency"}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.record(self.response(request, **changes))
        self.assertEqual(len(office.load(self.root)[1]), 1)

    def test_missing_request_and_second_response_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "solicitud pendiente"):
            self.record(self.response("unknown"))
        request = self.request()
        self.record(self.response(request))
        with self.assertRaisesRegex(ValueError, "solicitud pendiente"):
            self.record(self.response(request))
        self.assertEqual(len(office.load(self.root)[1]), 2)

    def test_completed_response_requires_existing_evidence(self):
        request = self.request()
        for status in ("PASS", "COMPLETED"):
            with self.subTest(status=status), self.assertRaisesRegex(ValueError, "evidencia"):
                self.record(self.response(request, status=status, evidence=[]))

    def test_completed_response_with_local_evidence_is_valid(self):
        request = self.request()
        reply = self.record(self.response(request, status="COMPLETED", evidence=["qa/proof.md"]))
        config, events = office.load(self.root)
        self.assertEqual(events[-1]["id"], reply)
        self.assertEqual(events[-1]["status"], "COMPLETED")
        self.assertEqual(events[-1]["evidence"], ["qa/proof.md"])
        self.assertEqual(office.validate(config, events, self.root), {request})

    def test_decisions_and_notes_cannot_claim_completion_without_evidence(self):
        for kind in ("decision", "note"):
            for status in ("PASS", "COMPLETED"):
                with self.subTest(kind=kind, status=status), self.assertRaisesRegex(ValueError, "evidencia"):
                    self.record(self.payload(kind, status=status))
        self.assertFalse((self.root / "office/events.jsonl").exists())

    def test_render_failure_does_not_hide_a_committed_event(self):
        self.record(self.payload(id="before"))
        ledger = self.root / "office/events.jsonl"
        before = ledger.read_bytes()
        (self.root / "office/dashboard.html").unlink()
        try:
            event_id = self.record(self.payload(id="after"))
        except OSError:
            self.assertEqual(ledger.read_bytes(), before,
                             "record raised without returning the ID, but committed an event")
        else:
            self.assertEqual(event_id, "after")
            self.assertIn(event_id, {event["id"] for event in office.load(self.root)[1]})

    def test_invalid_template_prevents_append(self):
        self.record(self.payload(id="before"))
        ledger = self.root / "office/events.jsonl"
        before = ledger.read_bytes()
        (self.root / "office/dashboard.html").write_text("<html>No data placeholder</html>")
        with self.assertRaises(ValueError):
            self.record(self.payload(id="after"))
        self.assertEqual(ledger.read_bytes(), before)

    def test_panel_write_failure_returns_committed_id_and_render_recovers(self):
        original = office.atomic_write
        def fail_panel(path, text):
            if path == self.root / "office/dist/index.html":
                raise OSError("simulated panel disk error")
            return original(path, text)
        warning = io.StringIO()
        with patch.object(office, "atomic_write", side_effect=fail_panel), redirect_stderr(warning):
            event_id = self.record(self.payload(id="persisted"))
        self.assertEqual(event_id, "persisted")
        self.assertIn("persisted", warning.getvalue())
        self.assertIn("no repitas record", warning.getvalue())
        self.assertEqual(len(office.load(self.root)[1]), 1)
        self.assertEqual(office.render(self.root), 1)
        parsed = Scripts(); parsed.feed((self.root / "office/dist/index.html").read_text())
        self.assertEqual(json.loads(parsed.blocks[0]["data"])["events"][0]["id"], event_id)

    def test_cli_record_file_check_and_render(self):
        (self.root / "scripts").mkdir()
        script = self.root / "scripts/evolution_office.py"
        shutil.copyfile(ROOT / "scripts/evolution_office.py", script)
        payload_file = self.root / "payload.json"
        payload_file.write_text(json.dumps(self.payload("request", id="cli-request")))
        result = subprocess.run([sys.executable, str(script), "record", "--file", str(payload_file)],
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("cli-request", result.stdout)
        payload_file.write_text(json.dumps(self.response("cli-request", id="cli-response", status="COMPLETED")))
        result = subprocess.run([sys.executable, str(script), "record", "--file", str(payload_file)],
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        for command in ("check", "render"):
            result = subprocess.run([sys.executable, str(script), command], capture_output=True,
                                    text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(office.load(self.root)[1]), 2)

    def read_state(self):
        return json.loads((self.root / "office/dist/state.json").read_text())

    def read_embedded_state(self):
        parsed = Scripts()
        parsed.feed((self.root / "office/dist/index.html").read_text())
        return json.loads(parsed.blocks[0]["data"])

    def test_state_matches_html_and_revision_tracks_events_and_config(self):
        office.render(self.root)
        first = self.read_state()
        self.assertEqual(first, self.read_embedded_state())
        office.render(self.root)
        self.assertEqual(first["revision"], self.read_state()["revision"])
        self.record(self.payload(id="new-event"))
        second = self.read_state()
        self.assertNotEqual(first["revision"], second["revision"])
        self.assertEqual(second, self.read_embedded_state())
        self.assertEqual(second["events"][-1]["id"], "new-event")
        config_path = self.root / "office/config.json"
        config = json.loads(config_path.read_text())
        config["mission"] += " revised"
        config_path.write_text(json.dumps(config))
        office.render(self.root)
        self.assertNotEqual(second["revision"], self.read_state()["revision"])
        self.assertEqual(self.read_state(), self.read_embedded_state())

    def test_state_write_failure_returns_committed_id_and_render_recovers(self):
        office.render(self.root)
        before = self.read_state()
        original = office.atomic_write
        def fail_state(path, text):
            if path == self.root / "office/dist/state.json":
                raise OSError("simulated state disk error")
            return original(path, text)
        warning = io.StringIO()
        with patch.object(office, "atomic_write", side_effect=fail_state), redirect_stderr(warning):
            event_id = self.record(self.payload(id="state-persisted"))
        self.assertEqual(event_id, "state-persisted")
        self.assertIn(event_id, warning.getvalue())
        self.assertIn("no repitas record", warning.getvalue())
        self.assertEqual(self.read_state(), before)
        self.assertEqual(self.read_embedded_state()["events"][-1]["id"], event_id)
        self.assertEqual(len(office.load(self.root)[1]), 1)
        self.assertEqual(office.render(self.root), 1)
        self.assertEqual(self.read_state(), self.read_embedded_state())
        self.assertEqual(self.read_state()["events"][-1]["id"], event_id)

    def test_render_cannot_overwrite_a_concurrent_newer_record(self):
        self.record(self.payload(id="before"))
        original = office.load
        loaded, release, started = threading.Event(), threading.Event(), threading.Event()
        def paused_load(root):
            result = original(root)
            if threading.current_thread().name.startswith("renderer"):
                loaded.set()
                if not release.wait(5):
                    raise RuntimeError("Test synchronization timed out")
            return result
        def append():
            started.set()
            return self.record(self.payload(id="newer"))
        with patch.object(office, "load", side_effect=paused_load):
            with concurrent.futures.ThreadPoolExecutor(max_workers=1, thread_name_prefix="renderer") as render_pool, concurrent.futures.ThreadPoolExecutor(max_workers=1, thread_name_prefix="writer") as record_pool:
                render_job = render_pool.submit(office.render, self.root)
                try:
                    self.assertTrue(loaded.wait(5))
                    record_job = record_pool.submit(append)
                    self.assertTrue(started.wait(5))
                    # A correctly serialized writer waits; an unlocked render lets it commit first.
                    try:
                        record_job.result(timeout=0.2)
                    except concurrent.futures.TimeoutError:
                        pass
                finally:
                    release.set()
                render_job.result(timeout=5)
                record_job.result(timeout=5)
        ids = [e["id"] for e in office.load(self.root)[1]]
        self.assertEqual(ids, ["before", "newer"])
        self.assertEqual([e["id"] for e in self.read_state()["events"]], ids)
        self.assertEqual(self.read_state(), self.read_embedded_state())

    def test_outside_absolute_traversal_and_symlink_evidence_are_rejected(self):
        outside = self.base / "outside.md"
        outside.write_text("Not part of the repository")
        (self.root / "qa/outside-link.md").symlink_to(outside)
        for evidence in ([str(outside)], ["../outside.md"], ["qa/outside-link.md"]):
            with self.subTest(evidence=evidence), self.assertRaisesRegex(ValueError, "fuera del repositorio"):
                self.record(self.payload(evidence=evidence))
        self.assertFalse((self.root / "office/events.jsonl").exists())

    def test_missing_file_or_directory_is_not_evidence(self):
        for evidence in (["qa/missing.md"], ["qa"]):
            with self.subTest(evidence=evidence), self.assertRaises(ValueError):
                self.record(self.payload(evidence=evidence))

    def test_request_requires_real_dispatch_status_and_no_reply_to(self):
        for event in (self.payload("request", status="RECORDED"), self.payload(reply_to="other")):
            with self.assertRaises(ValueError):
                self.record(event)

    def rendered_attack(self):
        attack = '</script><script>globalThis.pwned=true</script><img src=x onerror="pwned=true">&'
        self.record(self.payload(message=attack, why=attack, scope=attack, deliverable=attack,
                                 tool_ref=attack, evidence=["qa/proof.md"]))
        config = json.loads((self.root / "office/config.json").read_text())
        config["mission"] = attack
        config["agents"][0]["name"] = attack
        (self.root / "office/config.json").write_text(json.dumps(config))
        office.render(self.root)
        document = (self.root / "office/dist/index.html").read_text()
        parser = Scripts()
        parser.feed(document)
        return attack, document, parser

    def test_embedded_json_cannot_escape_script_element(self):
        attack, document, parsed = self.rendered_attack()
        self.assertEqual(len(parsed.blocks), 2)
        self.assertNotIn("img", parsed.tags)
        self.assertNotIn(attack, document)
        embedded = json.loads(parsed.blocks[0]["data"])
        self.assertEqual(embedded["events"][0]["message"], attack)
        self.assertEqual(embedded["config"]["mission"], attack)
        self.assertEqual(parsed.blocks[0]["attrs"]["type"], "application/json")

    def test_dashboard_uses_text_nodes_for_untrusted_values(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("Node required for isolated dashboard JavaScript execution")
        attack, _, parsed = self.rendered_attack()
        harness = r"""
const vm=require('node:vm'), fs=require('node:fs');
const input=JSON.parse(fs.readFileSync(0,'utf8')), all=[];
class Element {
  constructor(tag){this.tag=tag;this.children=[];this.dataset={};this.style={setProperty(){}};this.value='';this._text='';this.scrollTop=0;this.scrollHeight=0;this.clientHeight=0;all.push(this)}
  set textContent(value){this._text=String(value)} get textContent(){return this._text}
  set innerHTML(value){throw Error('Untrusted HTML sink used')}
  append(...items){this.children.push(...items)} replaceChildren(...items){this.children=items}
  querySelector(tag){return this.summary??=new Element(tag)}
  setAttribute(){}
}
const byId={};
const document={getElementById(id){return byId[id]??=new Element(id)},createElement(tag){return new Element(tag)},querySelectorAll(){return all.filter(e=>e.className==='person')}};
document.getElementById('data').textContent=input.json;
const context={document,location:{protocol:'file:'},fetch(){throw Error('Unexpected network')},setTimeout(){throw Error('Unexpected polling for local file')},setInterval(){throw Error('Unexpected live polling')}};
vm.createContext(context);vm.runInContext(input.script,context,{timeout:1000});
if(context.pwned)throw Error('Injected script executed');
if(!all.some(e=>e.textContent===input.attack))throw Error('Message was not rendered as text');
if(document.getElementById('feed').children.length!==1)throw Error('Incorrect event count');
console.log('PASS: payload remains text; no HTML sink or network');
"""
        result = subprocess.run([node, "-e", harness], input=json.dumps({"json": parsed.blocks[0]["data"],
                                "script": parsed.blocks[1]["data"], "attack": attack}),
                                capture_output=True, text=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_dashboard_distinguishes_recorded_messages_http_and_local_file(self):
        office.render(self.root)
        document = (self.root / "office/dist/index.html").read_text()
        for wording in ("Perfiles de IA que trabajan bajo demanda", "intercambios reales resumidos", "Actualización automática · mensajes registrados", "Sin conexión · último corte guardado", "Archivo local · corte del"):
            self.assertIn(wording, document)
        parsed = Scripts(); parsed.feed(document)
        self.assertIn("generated", json.loads(parsed.blocks[0]["data"]))

    def test_http_sync_updates_quotes_and_preserves_last_cut_on_disconnect(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("Node required for isolated HTTP synchronization")
        request = self.request()
        initial = self.read_state()
        attack = '</script><img src=x onerror="globalThis.pwned=true">'
        self.record(self.response(request, message=attack))
        updated = self.read_state()
        parsed = Scripts(); parsed.feed((self.root / "office/dist/index.html").read_text())
        harness = r"""
const vm=require('node:vm'),fs=require('node:fs');
const input=JSON.parse(fs.readFileSync(0,'utf8')),all=[],timers=[];
class Element {
 constructor(tag){this.tag=tag;this.children=[];this.dataset={};this.style={setProperty(){}};this.value='';this._text='';this.scrollTop=0;this.scrollHeight=0;this.clientHeight=0;all.push(this)}
 set textContent(v){this._text=String(v)} get textContent(){return this._text}
 set innerHTML(v){throw Error('HTML sink used')}
 append(...v){this.children.push(...v)} replaceChildren(...v){this.children=v}
 querySelector(tag){return this.summary??=new Element(tag)} setAttribute(){}
}
const ids={},document={hidden:false,getElementById(id){return ids[id]??=new Element(id)},createElement(tag){return new Element(tag)}};
document.getElementById('data').textContent=JSON.stringify(input.initial);
let calls=0,mode='ok',next=input.updated;
const context={document,location:{protocol:'http:'},AbortController,
 setTimeout(fn,delay){timers.push({fn,delay});return timers.length},clearTimeout(){},
 async fetch(url,options){calls++;if(url!=='./state.json'||options.cache!=='no-store')throw Error('Unexpected request');
   if(mode==='offline')throw Error('Disconnected');if(mode==='bad')return {ok:false};
   return {ok:true,json:async()=>next};}};
vm.createContext(context);
function assert(ok,message){if(!ok)throw Error(message)}
(async()=>{
 vm.runInContext(input.script,context,{timeout:1000});await new Promise(setImmediate);
 assert(calls===1,'HTTP did not fetch initial update');
 assert(ids.feed.children.length===2,'Response not added');
 const first=ids.feed.children[0],second=ids.feed.children[1];
 assert(all.some(e=>e.className==='reply'&&e.textContent.includes('Verify the artifact')),'Response lacks quoted request');
 assert(all.some(e=>e.tag==='p'&&e.textContent===input.attack),'Fetched message not rendered as text');
 assert(!context.pwned,'Fetched script executed');
 assert(ids.connection.textContent.includes('mensajes registrados'),'Connection label is inaccurate');
 await vm.runInContext('sync()',context);
 assert(ids.feed.children[0]===first&&ids.feed.children[1]===second,'Same revision needlessly rebuilt messages');
 mode='offline';await vm.runInContext('sync()',context);
 assert(ids.connection.textContent.includes('Sin conexión'),'Disconnect is hidden');
 assert(ids.feed.children[1]===second,'Disconnect discarded last messages');
 mode='bad';await vm.runInContext('sync()',context);
 assert(ids.connection.textContent.includes('Sin conexión'),'HTTP error is hidden');
 document.hidden=true;const before=calls;await vm.runInContext('sync()',context);
 assert(calls===before,'Hidden page polled');
 document.hidden=false;mode='ok';await vm.runInContext('sync()',context);
 assert(ids.connection.textContent.includes('mensajes registrados'),'Reconnect failed');
 assert(timers.some(t=>t.delay===3000),'Polling cadence missing');
 console.log('PASS: updates, inert fetched text, correlation, no redundant rebuild, disconnect, visibility, recovery');
})().catch(e=>{console.error(e);process.exitCode=1});
"""
        result = subprocess.run([node, "-e", harness], input=json.dumps({"initial": initial,
                                "updated": updated, "script": parsed.blocks[1]["data"], "attack": attack}),
                                capture_output=True, text=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
