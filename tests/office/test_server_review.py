"""Independent persistence and evidence-origin regressions; no sockets or model."""
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch

import test_office as fixtures

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import evolution_office_server as server


class IndependentServerTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.OfficeTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.runtime = server.OfficeRuntime(self.fixture.root, codex="must-not-execute")
        self.addCleanup(self.runtime.shutdown)

    def test_explicit_private_channels_never_enter_public_updates(self):
        job = {"id": "privacy-filter-001", "updates": []}
        with patch.object(self.runtime, "persist"):
            for container in ("item", "event"):
                for field in ("channel", "phase"):
                    for value in ("analysis", "reasoning"):
                        event = {"type": "item.completed", "item": {"id": f"{container}-{field}-{value}", "type": "agent_message", "text": "PRIVATE_REASONING"}}
                        (event["item"] if container == "item" else event)[field] = value
                        self.runtime.consume(job, event)
            self.runtime.consume(job, {"type": "item.completed", "item": {"id": "public", "type": "agent_message", "channel": "commentary", "text": "Hallazgo público"}})
            self.runtime.consume(job, {"type": "item.started", "item": {"id": "tool", "type": "mcp_tool_call", "arguments": "PRIVATE_ARGUMENTS", "result": "PRIVATE_RESULT"}})
        encoded = json.dumps(self.runtime.public(job), ensure_ascii=False)
        self.assertNotIn("PRIVATE_", encoded)
        self.assertIn("Hallazgo público", encoded)
        self.assertEqual(len([u for u in job["updates"] if u["kind"] == "message"]), 1)

    def test_evidence_html_cannot_execute_in_composer_origin(self):
        path = self.fixture.root / "qa/untrusted.html"
        path.write_text('<script>fetch("/api/session").then(r=>r.json())</script>')
        self.fixture.record(self.fixture.payload(evidence=["qa/untrusted.html"]))
        handler = server.Handler.__new__(server.Handler)
        handler.path = "/qa/untrusted.html"
        handler.server = Mock(runtime=self.runtime)
        handler.trusted = lambda: True
        headers = {}
        handler.send_response = Mock()
        handler.send_header = lambda key, value: headers.__setitem__(key, value)
        handler.end_headers = Mock()
        handler.wfile = io.BytesIO()
        handler.do_GET()
        active_html = headers.get("Content-Type", "").startswith("text/html")
        isolated = "sandbox" in headers.get("Content-Security-Policy", "") and "allow-same-origin" not in headers.get("Content-Security-Policy", "")
        download = headers.get("Content-Disposition", "").startswith("attachment")
        self.assertTrue(not active_html or isolated or download,
                        "Evidence HTML executes beside the token endpoint, bypassing cross-origin checks")

    def test_initial_persistence_failure_does_not_leave_runtime_busy(self):
        with patch.object(self.runtime, "persist", side_effect=OSError("disk full")), patch.object(server.subprocess, "Popen") as popen:
            try:
                self.runtime.submit("disk-first-001", "Do not lose this request")
            except OSError:
                pass
        self.assertIsNone(self.runtime.active, "Failed acceptance permanently occupies the only worker")
        popen.assert_not_called()
        job = self.runtime.jobs.get("disk-first-001")
        self.assertTrue(job is None or job["status"] == "failed")
        with patch.object(server.subprocess, "Popen", side_effect=OSError("runner unavailable")) as popen:
            retry, created = self.runtime.submit("disk-first-001", "Do not lose this request")
        popen.assert_called_once()
        self.assertTrue(created)
        self.assertEqual(retry["status"], "failed")
        self.assertIsNone(self.runtime.active)

    def test_startup_failure_and_error_write_failure_still_release_worker(self):
        proc = Mock()
        real_persist = self.runtime.persist
        def persist(job):
            if job["status"] != "received":
                raise OSError("disk full after spawn")
            return real_persist(job)
        original = server.private_write
        def write(path, value):
            if path.name == "result.json":
                raise OSError("disk full storing startup failure")
            return original(path, value)
        with patch.object(server.subprocess, "Popen", return_value=proc), patch.object(self.runtime, "terminate") as terminate, patch.object(self.runtime, "persist", side_effect=persist), patch.object(server, "private_write", side_effect=write):
            try:
                self.runtime.submit("disk-spawn-001", "Request")
            except OSError:
                pass
        self.assertIsNone(self.runtime.active, "Startup error handler left worker busy")
        self.assertFalse(self.runtime.processes)
        terminate.assert_called_once_with(proc)
        self.assertEqual(self.runtime.jobs["disk-spawn-001"]["status"], "failed")

    def test_final_result_write_failure_releases_worker_and_reports_failure(self):
        job = {"id": "disk-result-001", "request_id": "disk-result-001", "status": "running",
               "message": "Request", "result": None, "error": None}
        folder = self.runtime.folder / job["id"]
        folder.mkdir()
        job["event_id"] = self.runtime.event(job)
        self.runtime.jobs[job["id"]] = job
        self.runtime.active = job["id"]
        proc = Mock(returncode=0)
        proc.communicate.return_value = (json.dumps({"type": "item.completed", "item": {"type": "agent_message", "text": "Answer"}}), "")
        self.runtime.processes[job["id"]] = proc
        self.addCleanup(self.runtime.processes.clear)
        with patch.object(server, "private_write", side_effect=OSError("disk full")), patch.object(self.runtime, "stream", return_value=("", "", ["Answer"], None)):
            try:
                self.runtime.run(job, proc, "prompt fixture")
            except OSError:
                pass
        self.assertIsNone(self.runtime.active, "Finalization disk failure permanently occupies worker")
        self.assertFalse(self.runtime.processes)
        self.assertEqual(job["status"], "failed", "Undurable result was reported completed")
        self.assertTrue(job["error"])


if __name__ == "__main__":
    unittest.main()
