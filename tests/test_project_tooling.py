import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import ds_core as core
import ds_graph as graph


def record(path, version, status="APPROVED", **extra):
    return {"id": "EXAMPLE-001", "path": path, "kind": "base", "metadata":
            {"contract_id": "EXAMPLE-001", "status": status, "version": version, **extra}}


class ResolutionTests(unittest.TestCase):
    def test_latest_version_never_wins_without_evidence(self):
        rows = [record("old.md", "1.0"), record("new.md", "9.0")]
        self.assertEqual(len(core.resolve_bases(rows)), 2)

    def test_explicit_supersession_beats_version_order(self):
        old = record("old.md", "9.0")
        new = record("new.md", "1.0", supersedes="old.md")
        self.assertEqual(core.resolve_bases([old, new]), [new])

    def test_draft_does_not_replace_approved(self):
        old = record("old.md", "1.0")
        draft = record("new.md", "2.0", status="DRAFT", supersedes="old.md")
        self.assertEqual(core.resolve_bases([old, draft]), [old])

    def test_partial_amendment_does_not_replace_base(self):
        old = record("old.md", "1.0")
        amendment = record("amendment.md", "1.1", supersedes="old.md")
        amendment["kind"] = "amendment"
        self.assertEqual(core.resolve_bases([old, amendment]), [old])

    def test_base_version_preserves_composition_without_duplicate_active_base(self):
        old = record("old.md", "1.0")
        new = record("new.md", "2.0", base_version="1.0")
        self.assertEqual(core.resolve_bases([old, new]), [new])


class DocumentTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for name in ("specs", "registry", "sources"):
            (self.root / name).mkdir()
        (self.root / "AGENTS.md").write_text("**Paquete de protocolos:** 0.2.4\n")
        (self.root / "README.md").write_text("**Versión operativa integrada:** 0.2.4\n")
        (self.root / "CHANGELOG.md").write_text("## 0.2.4\n")
        self.config = {"protocol_package": "0.2.4", "historical_link_exceptions": [], "protected_data": {}}

    def tearDown(self):
        self.tmp.cleanup()

    def check(self, paths, parsed=None):
        return core.documentation_check(parsed or {}, paths, {"issues": []}, self.config, self.root)

    def test_duplicate_json_keys_fail(self):
        (self.root / "x.json").write_text('{"x":1,"x":2}')
        self.assertEqual(self.check(["x.json"])["status"], "FAIL")

    def test_malformed_and_duplicate_yaml_fail(self):
        (self.root / "bad.yaml").write_text("a: [unterminated")
        (self.root / "duplicate.yaml").write_text("a: 1\na: 2\n")
        parsed = core.yaml_documents(["bad.yaml", "duplicate.yaml"], self.root)
        self.assertTrue(parsed["bad.yaml"]["errors"])
        self.assertTrue(parsed["duplicate.yaml"]["errors"])

    def test_unsafe_yaml_tag_rejected(self):
        (self.root / "x.yaml").write_text("--- !ruby/object:Object {}\n")
        self.assertTrue(core.yaml_documents(["x.yaml"], self.root)["x.yaml"]["errors"])

    def test_historical_link_exception_pinned_to_exact_bytes(self):
        path = self.root / "historic.md"
        path.write_text("[old](missing.md)\n")
        self.config["historical_link_exceptions"] = [{
            "source": "historic.md", "target": "missing.md", "line": 1, "source_sha256": core.sha(path)}]
        result = self.check(["historic.md"])
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["findings"][0]["severity"], "HISTORICAL")
        path.write_text("[old](missing.md)\nChanged\n")
        self.assertEqual(self.check(["historic.md"])["status"], "FAIL")

    def test_code_examples_are_not_links_but_reference_definitions_are_checked(self):
        tick = chr(96) * 3
        path = self.root / "example.md"
        path.write_text(tick + "\n[demo](missing.md)\n" + tick + "\n[ref]: actual-missing.md\n")
        result = self.check(["example.md"])
        links = [f["message"] for f in result["findings"] if f["control"] == "DOC-LINK"]
        self.assertEqual(links, ["actual-missing.md"])

    def test_protected_data_change_fails(self):
        path = self.root / "sources/tokens.json"
        path.write_text('{"v":1}')
        self.config["protected_data"] = {"sources/tokens.json": {"sha256": core.sha(path)}}
        path.write_text('{"v":2}')
        self.assertEqual(self.check(["sources/tokens.json"])["status"], "FAIL")

    def test_data_reference_resolves_relative_to_own_document(self):
        path = "specs/test.md"
        (self.root / path).write_text("# test\n")
        (self.root / "specs/local.json").write_text("{}")
        meta = {"contract_id": "TEST-001", "status": "DRAFT", "version": "1.0", "data_refs": ["local.json"]}
        parsed = {path: {"value": meta, "errors": []}}
        self.assertEqual(self.check([path], parsed)["status"], "PASS")

    def test_read_only_checks_preserve_bytes(self):
        (self.root / "x.json").write_text("{}")
        before = {str(p): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.check(["x.json"])
        after = {str(p): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_prose_metadata_reads_authority_without_promoting_qa(self):
        path = "specs/example.contract.md"
        (self.root / path).write_text("# EXAMPLE-001 · Example · v0.1.0\n\nEstado: DELEGATED_FOR_BUILD. "
                                      "Auditoría humana PENDING. QA PASS.\nPágina semántica **Examples**.\n")
        value = core.yaml_documents([path], self.root)[path]["value"]
        self.assertEqual(value["status"], "DELEGATED_FOR_BUILD")
        self.assertEqual(value["user_audit"], "PENDING")
        self.assertEqual(value["figma_page_name"], "Examples")
        self.assertNotIn("implementation_status", value)

    def test_prose_qa_alone_never_supplies_approval(self):
        path = "specs/example.contract.md"
        (self.root / path).write_text("# EXAMPLE-001 · Example · v0.1.0\n\nQA PASS. APPROVED example text.\n")
        parsed = core.yaml_documents([path], self.root)
        self.assertNotIn("status", parsed[path]["value"])
        self.assertEqual(self.check([path], parsed)["status"], "FAIL")


class GraphGateTests(unittest.TestCase):
    def test_skill_css_is_indexed_without_allowing_paths_outside_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            css = root / "skills/demo/assets/globals.css"
            css.parent.mkdir(parents=True)
            css.write_text("body { color: var(--ds-text); }")
            config = {"exclude_roots": [], "exclude_prefixes": [],
                      "supplemental_design_data": [], "supplemental_documents": [],
                      "supplemental_skill_sources": ["skills/demo/assets/globals.css"]}
            def detected(_):
                return {"files": {"code": [], "document": [], "image": [], "paper": []}}
            with patch("graphify.detect.detect", side_effect=detected):
                result = core.corpus(root, config)
                self.assertEqual(result["files"]["document"], [str(css.resolve())])
                config["supplemental_skill_sources"] = ["skills/../outside.css"]
                with self.assertRaisesRegex(ValueError, "Unsupported supplemental skill"):
                    core.corpus(root, config)

    def test_new_source_after_prepare_cannot_receive_old_semantic_stamp(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp)
            core.dump(run / "source-plan.json", {"source_sha256": {"old.md": "a"}, "config_sha256": "c"})
            with patch.object(graph, "plan", return_value=({"source_sha256": {"old.md": "a", "new.md": "b"}, "config_sha256": "c"}, {})):
                with self.assertRaisesRegex(ValueError, "Fuentes cambiaron"):
                    graph.assert_source_plan(run, {})

    def test_concurrent_graph_change_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "run"
            live = Path(tmp) / "live"
            (run / "before").mkdir(parents=True)
            live.mkdir()
            (run / "before/graph.json").write_text("old")
            (live / "graph.json").write_text("newer")
            with patch.object(graph, "LIVE", live):
                with self.assertRaisesRegex(ValueError, "Live graph changed"):
                    graph.assert_live_baseline(run)
            self.assertEqual((live / "graph.json").read_text(), "newer")

    def test_missing_semantic_chunk_fails_without_touching_prior_graph(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp)
            (run / "before").mkdir()
            core.dump(run / "before/graph.json", {"nodes": [], "links": []})
            core.dump(run / "semantic-plan.json", {"chunks": [["/project/new.md"]]})
            before = (run / "before/graph.json").read_bytes()
            with self.assertRaisesRegex(ValueError, "Semántica pendiente"):
                graph.validate_fragments(run)
            self.assertEqual(before, (run / "before/graph.json").read_bytes())

    def test_semantic_placeholder_cannot_claim_coverage(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp)
            (run / "before").mkdir()
            core.dump(run / "before/graph.json", {"nodes": [], "links": []})
            core.dump(run / "semantic-plan.json", {"chunks": [["/project/new.md"]]})
            core.dump(run / "chunk-00.json", {"nodes": [], "edges": []})
            with self.assertRaisesRegex(ValueError, "coverage"):
                graph.validate_fragments(run)

    def test_publish_rolls_back_partial_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            run, live = root / "run", root / "live"
            (run / "before").mkdir(parents=True)
            (run / "staged").mkdir()
            live.mkdir()
            for filename in graph.OUTPUTS:
                (run / "before" / filename).write_text("original")
                (live / filename).write_text("original")
                (run / "staged" / filename).write_text("new")
            real_replace = graph.os.replace
            calls = []
            def fail_second(a, b):
                calls.append(b)
                if len(calls) == 2:
                    raise OSError("Simulated interruption")
                return real_replace(a, b)
            with patch.object(graph.os, "replace", side_effect=fail_second):
                with self.assertRaises(OSError):
                    graph.publish(run, {"status": "CURRENT"}, live)
            self.assertTrue(all((live / name).read_text() == "original" for name in graph.OUTPUTS))
            self.assertFalse((live / "ds-closure.json").exists())

    def test_ast_stamp_never_satisfies_document_semantics(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "config").mkdir()
            (root / "graphify-out").mkdir()
            (root / "config/ds-project.json").write_text("{}")
            doc = root / "new.md"
            doc.write_text("Changed meaning")
            md5 = hashlib.md5(doc.read_bytes()).hexdigest()
            core.dump(root / "graphify-out/manifest.json",
                      {"new.md": {"ast_hash": md5, "semantic_hash": "old"}})
            detection = {"files": {"document": [str(doc)], "code": [], "image": [], "paper": []}}
            with patch.object(graph, "ROOT", root), patch.object(graph, "LIVE", root / "graphify-out"), \
                 patch.object(graph, "runtime_gate"), \
                 patch.object(graph, "relative", side_effect=lambda p: core.relative(p, root)), \
                 patch.object(graph, "paths_of", return_value=["new.md"]):
                delta, _ = graph.plan({}, detection)
            self.assertEqual(delta["semantic_required"], ["new.md"])


if __name__ == "__main__":
    unittest.main()
