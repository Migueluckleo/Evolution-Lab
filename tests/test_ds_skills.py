"""Release and installation regressions with tiny local fixtures; no DS builds."""
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import ds_skills as skills


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.names = ["contpaqi-figma-screens", "contpaqi-po-prototypes"]
        self.config = {"skills": self.names, "output": "output/skills", "initial_version": "0.1.0",
                       "authority": "DERIVED_NOT_AUTHORITY"}
        (self.root / "specs").mkdir()
        (self.root / "specs/example.md").write_text("# Fuente ñ\nEstado: DRAFT\n")
        for name in self.names:
            p = self.root / "skills" / name
            p.mkdir(parents=True)
            (p / "SKILL.md").write_text("---\nname: " + name + "\ndescription: Fixture.\n---\n")
        self.mock_inputs = patch.object(skills, "inputs", side_effect=lambda root=skills.ROOT: self.state())
        self.mock_inputs.start()

    def tearDown(self):
        self.mock_inputs.stop()
        self.tmp.cleanup()

    def state(self):
        files = {p.relative_to(self.root).as_posix(): skills.digest(p.read_bytes())
                 for p in sorted((self.root / "specs").glob("*.md"))}
        templates = {name: {"SKILL.md": skills.digest((self.root / "skills" / name / "SKILL.md").read_bytes())}
                     for name in self.names}
        fingerprint = {"files": files, "templates": templates, "config": self.config}
        return {"root": self.root, "config": self.config, "files": files, "templates": templates,
                "components": [], "excluded_links": [], "ds_digest": skills.digest(skills.compact(files)),
                "input_digest": skills.digest(skills.compact(fingerprint)), "fingerprint": fingerprint}

    def release(self, version="0.1.0"):
        return self.root / "output/skills" / version

    def all_bytes(self, directory):
        return {p.relative_to(directory).as_posix(): p.read_bytes() for p in directory.rglob("*") if p.is_file()}

    def test_snapshot_byte_identity_zip_portability_and_digest(self):
        skills.sync(self.root)
        for name in self.names:
            package = self.release() / name
            manifest = json.loads((package / "assets/snapshot-manifest.json").read_text())
            original = (self.root / "specs/example.md").read_bytes()
            self.assertEqual((package / "assets/design-system/specs/example.md").read_bytes(), original)
            expected = json.dumps(manifest["files"], sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
            self.assertEqual(manifest["ds_digest"], hashlib.sha256(expected).hexdigest())
            with zipfile.ZipFile(self.release() / f"{name}-0.1.0.zip") as archive:
                self.assertTrue(all(n.startswith(name + "/") for n in archive.namelist()))
                self.assertTrue(all(i.date_time == (1980, 1, 1, 0, 0, 0) for i in archive.infolist()))
                self.assertEqual(archive.read(name + "/assets/design-system/specs/example.md"), original)
        self.assertEqual(skills.check(self.root)["status"], "CURRENT")

    def test_unchanged_inputs_do_not_bump_rewrite_or_touch_mtimes(self):
        skills.sync(self.root)
        directory = self.root / "output/skills"
        before = {str(p): (p.read_bytes(), p.stat().st_mtime_ns) for p in directory.rglob("*") if p.is_file()}
        result = skills.sync(self.root, bump="major")
        after = {str(p): (p.read_bytes(), p.stat().st_mtime_ns) for p in directory.rglob("*") if p.is_file()}
        self.assertEqual(result["operation"], "UNCHANGED")
        self.assertEqual(before, after)

    def test_change_addition_and_deletion_each_make_snapshot_stale(self):
        skills.sync(self.root)
        history = self.all_bytes(self.release())
        (self.root / "specs/example.md").write_text("Changed\n")
        self.assertEqual(skills.check(self.root)["status"], "STALE")
        self.assertEqual(skills.sync(self.root)["version"], "0.1.1")
        (self.root / "specs/added.md").write_text("Additional contract\n")
        self.assertEqual(skills.check(self.root)["status"], "STALE")
        self.assertEqual(skills.sync(self.root, bump="minor")["version"], "0.2.0")
        (self.root / "specs/added.md").unlink()
        self.assertEqual(skills.check(self.root)["status"], "STALE")
        self.assertEqual(skills.sync(self.root, bump="major")["version"], "1.0.0")
        self.assertEqual(history, self.all_bytes(self.release()))

    def test_skill_template_change_invalidates_both_packages(self):
        skills.sync(self.root)
        (self.root / "skills" / self.names[0] / "SKILL.md").write_text("Changed instructions\n")
        self.assertEqual(skills.check(self.root)["status"], "STALE")
        skills.sync(self.root)
        for name in self.names:
            release = json.loads((self.release("0.1.1") / name / "assets/release.json").read_text())
            self.assertEqual(release["version"], "0.1.1")

    def test_version_collision_preserves_existing_release(self):
        self.release().mkdir(parents=True)
        (self.release() / "do-not-touch").write_text("preserve")
        with self.assertRaisesRegex(ValueError, "collision"):
            skills.sync(self.root)
        self.assertEqual((self.release() / "do-not-touch").read_text(), "preserve")

    def test_tampering_or_extra_files_never_pass_or_silently_repair(self):
        skills.sync(self.root)
        target = self.release() / self.names[0] / "SKILL.md"
        target.write_text("Tampered")
        self.assertEqual(skills.check(self.root)["status"], "STALE")
        with self.assertRaisesRegex(ValueError, "damaged"):
            skills.sync(self.root)
        self.assertEqual(target.read_text(), "Tampered")
        target.write_bytes((self.root / "skills" / self.names[0] / "SKILL.md").read_bytes())
        (self.release() / "unexpected").write_text("extra")
        self.assertEqual(skills.check(self.root)["status"], "STALE")

    def test_zip_is_reproducible_independent_of_input_dictionary_order(self):
        a = skills.zip_bytes("skill", {"b.txt": b"B", "a.txt": "ñ".encode()})
        b = skills.zip_bytes("skill", {"a.txt": "ñ".encode(), "b.txt": b"B"})
        self.assertEqual(a, b)

    def test_path_escape_and_symlink_are_rejected(self):
        for path in ["../escape", "/absolute", "a/../../escape", "a\\b"]:
            with self.assertRaises(ValueError):
                skills.safe(self.root, path)
        (self.root / "link").symlink_to(self.root / "specs", target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            skills.safe(self.root, "link/example.md")

    def test_explicit_selection_detects_new_files_and_excludes_secrets(self):
        (self.root / "specs/.env").write_text("DO_NOT_PACKAGE")
        cfg = {"include": ["specs/**"], "exclude": [], "link_dependency_roots": ["specs"],
               "excluded_link_reason": "outside snapshot"}
        paths, _ = skills.source_selection(self.root, cfg, {})
        self.assertEqual(paths, ["specs/example.md"])
        (self.root / "specs/new.md").write_text("new")
        paths, _ = skills.source_selection(self.root, cfg, {})
        self.assertIn("specs/new.md", paths)

    def test_missing_dependency_fails_and_external_reference_is_recorded(self):
        cfg = {"include": ["specs/**"], "exclude": [], "link_dependency_roots": ["specs"],
               "excluded_link_reason": "outside snapshot"}
        (self.root / "specs/example.md").write_text("[missing](missing.md)\n")
        with self.assertRaisesRegex(ValueError, "Missing snapshot dependency"):
            skills.source_selection(self.root, cfg, {})
        (self.root / "specs/example.md").write_text("[maintenance](../scripts/missing.py)\n")
        _, exclusions = skills.source_selection(self.root, cfg, {})
        self.assertEqual(exclusions[0]["reason"], "outside snapshot")

    def test_install_upgrade_is_explicit_and_preserves_unrelated_skills(self):
        dest = self.root / "installed"
        old = dest / "contpaqi-poc-builder"
        old.mkdir(parents=True)
        (old / "SKILL.md").write_text("OLD")
        skills.sync(self.root)
        self.assertEqual(skills.install(self.root, dest)["operation"], "INSTALLED")
        self.assertEqual(skills.install(self.root, dest)["operation"], "UNCHANGED")
        (self.root / "specs/example.md").write_text("Updated")
        skills.sync(self.root)
        self.assertEqual(skills.install(self.root, dest, verify_only=True)["status"], "STALE")
        skills.install(self.root, dest)
        self.assertEqual((old / "SKILL.md").read_text(), "OLD")
        for name in self.names:
            receipt = json.loads((dest / name / skills.INSTALL_RECEIPT).read_text())
            self.assertEqual(receipt["version"], "0.1.1")

    def test_install_refuses_user_changes_or_unmanaged_targets(self):
        dest = self.root / "installed"
        skills.sync(self.root)
        skills.install(self.root, dest)
        target = dest / self.names[0] / "SKILL.md"
        target.write_text("USER EDIT")
        with self.assertRaisesRegex(ValueError, "local edits"):
            skills.install(self.root, dest)
        self.assertEqual(target.read_text(), "USER EDIT")
        unmanaged = self.root / "unmanaged" / self.names[0]
        unmanaged.mkdir(parents=True)
        (unmanaged / "SKILL.md").write_text("ORIGINAL")
        with self.assertRaisesRegex(ValueError, "no managed receipt"):
            skills.install(self.root, unmanaged.parent)

    def test_install_rolls_back_both_skills_after_partial_failure(self):
        dest = self.root / "installed"
        skills.sync(self.root)
        skills.install(self.root, dest)
        before = self.all_bytes(dest)
        (self.root / "specs/example.md").write_text("Updated")
        skills.sync(self.root)
        real_replace = skills.os.replace
        def fail_second_publication(source, target):
            if str(source).endswith("staged/" + self.names[1]):
                raise OSError("simulated disk failure")
            return real_replace(source, target)
        with patch.object(skills.os, "replace", side_effect=fail_second_publication):
            with self.assertRaisesRegex(OSError, "simulated"):
                skills.install(self.root, dest)
        self.assertEqual(self.all_bytes(dest), before)


class HandoffTypographyTests(unittest.TestCase):
    """Synthetic handoff fixtures; no browser, Figma, build or release writes."""

    catalog_path = "specs/tokens/ai-design-system.typography.v0.1.2.json"
    contract_path = "specs/foundations/typography.contract.v0.1.0.md"
    format_path = "specs/foundations/typography.formatting.amendment.v0.1.1.md"
    consumption_path = "specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md"
    native_path = "specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md"
    native_evidence_path = "qa/implementations/typography/consumption-v0.1.1/consumer-final.native-inheritance.v0.1.2.json"
    family_base = "specs/components/button.contract.v0.2.0.md"
    family_amendment = "specs/components/button.typography.amendment.v0.1.0.md"
    style_ids = ["ui-action-label-medium-underline", "ui-action-label-small-underline",
                 "ui-action-label-normal-underline", "ui-upload-action-feedback-underline"]

    def setUp(self):
        self.node = os.environ.get("NODE_BINARY") or shutil.which("node")
        if not self.node:
            self.skipTest("Node is required to execute the handoff generator")
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.script = Path(__file__).resolve().parents[1] / "skills/contpaqi-po-prototypes/assets/starter/scripts/handoff.mjs"
        self.snapshot = self.root / "references/design-system"
        self.files = {}
        fixtures = {self.catalog_path: {"styles": [{"id": sid, "name": sid,
                     "category": "complementary", "textDecoration": "UNDERLINE"} for sid in self.style_ids]},
                    "specs/tokens/ai-design-system.typography.v0.1.0.json": {"styles": []},
                    "implementations/web/src/generated/tokens.manifest.json": {"tokens": []}}
        for name in [self.contract_path, self.format_path, self.consumption_path, self.native_path,
                     self.family_base, self.family_amendment]:
            fixtures[name] = "# Synthetic normative fixture\n"
        for name, value in fixtures.items():
            target = self.snapshot / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(value if isinstance(value, str) else json.dumps(value))
            self.files[name] = hashlib.sha256(target.read_bytes()).hexdigest()
        digest = hashlib.sha256(json.dumps(self.files, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        self.write_json("references/snapshot-manifest.json", {"files": self.files, "ds_digest": digest,
            "package_version": "0.0.0-fixture", "components": [{"id": "BUTTON-001", "exports": ["Button"],
            "contract": self.family_base, "amendments": [self.family_amendment]}]})
        self.write_json("references/release.json", {"ds_digest": digest, "version": "0.0.0-fixture",
            "skill_name": "contpaqi-po-prototypes", "companion_skill": "contpaqi-figma-screens"})
        self.viewport = {"width": 1440, "height": 900}
        self.brief = {"title": "Synthetic test", "objective": "Exercise source identity only", "theme": "Contable",
            "viewports": [self.viewport], "screens": [{"id": "main", "name": "Fixture", "entry": "start",
            "layout": "fixture", "content": "fixture", "states": [{"id": "initial", "name": "Fixture",
            "actions": [], "expect": [{"selector": "p", "visible": True}], "nodes": ["fixture"]}]}],
            "components": [{"instanceId": "fixture", "componentId": "BUTTON-001", "exportName": "Button",
            "placement": "fixture", "kind": "ds", "props": {}, "tokens": [], "omissions": [],
            "slots": [{"name": "fixture", "status": "NOT_APPLICABLE", "content": "Synthetic fixture"}]}],
            "transitions": [], "decisions": [], "limitations": ["Synthetic test, not browser or Figma evidence"],
            "checks": [], "figmaTarget": None}
        self.write_json("brief.json", self.brief)
        html = b"<!doctype html><p>Synthetic fixture</p>"
        (self.root / "render.html").write_bytes(html)
        self.html_hash = hashlib.sha256(html).hexdigest()
        self.write_json("render.manifest.json", {"sha256": self.html_hash})

    def write_json(self, relative, value):
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(value))

    def capture_fixture(self, style_ids=None):
        self.write_json("capture/report.json", {"status": "PASS", "html_sha256": self.html_hash,
            "brief_sha256": hashlib.sha256((self.root / "brief.json").read_bytes()).hexdigest(),
            "states": [{"screen_id": "main", "state_id": "initial", "viewport": self.viewport, "status": "PASS",
            "nodes": [{"id": "fixture", "visible": True, "text": "Synthetic text", "computed_style": {},
            "bounding_box": {}, "text_runs": [{"text": "Synthetic text", "kind": "text",
            "typography_style_id": sid, "computed_style": {"textDecorationLine": "underline"}}
            for sid in (self.style_ids if style_ids is None else style_ids)]}]}]})

    def run_handoff(self):
        return subprocess.run([self.node, str(self.script)], cwd=self.root, capture_output=True, text=True)

    def result(self):
        return json.loads((self.root / "entrega/referencias/handoff.json").read_text())

    def test_active_catalog_and_amendments_embedded_with_hashes(self):
        self.capture_fixture()
        result = self.run_handoff()
        self.assertEqual(result.returncode, 0, result.stderr)
        handoff = self.result()
        self.assertEqual({s["id"] for s in handoff["typography"]["styles"]}, set(self.style_ids))
        expected = [self.catalog_path, self.contract_path, self.format_path, self.consumption_path, self.native_path,
                    self.family_base, self.family_amendment]
        sources = {s["path"]: s["sha256"] for s in handoff["sources"]}
        for source in expected:
            self.assertEqual(sources[source], self.files[source])
        self.assertNotIn("specs/tokens/ai-design-system.typography.v0.1.0.json", sources)
        md = (self.root / "entrega/replicar-en-figma.md").read_text()
        portable = json.loads(re.search(r"```json\n(.*?)\n```", md, re.S)[1])
        self.assertEqual(portable["typography"], handoff["typography"])
        self.assertEqual(portable["sources"], handoff["sources"])
        self.assertEqual(handoff["typography"]["status"], "IDENTIFIED")
        self.assertTrue(handoff["typography"]["metric_validation"].startswith("NOT_PERFORMED"))

    def test_uncaptured_handoff_keeps_sources_without_claiming_measurements(self):
        result = self.run_handoff()
        self.assertEqual(result.returncode, 0, result.stderr)
        handoff = self.result()
        self.assertEqual(handoff["typography"]["status"], "NOT_RUN")
        self.assertEqual(handoff["typography"]["styles"], [])
        self.assertEqual(handoff["capture"]["status"], "NOT_RUN")
        self.assertEqual(handoff["typography"]["catalog"]["path"], self.catalog_path)
        self.assertEqual({s["path"] for s in handoff["typography"]["amendments"]},
                         {self.format_path, self.consumption_path, self.native_path})

    def test_changed_format_source_is_rejected(self):
        (self.snapshot / self.format_path).write_text("Changed fixture\n")
        result = self.run_handoff()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Fuente alterada: " + self.format_path, result.stderr)
        self.assertFalse((self.root / "entrega").exists())

    def test_missing_consumption_source_is_rejected(self):
        (self.snapshot / self.consumption_path).unlink()
        result = self.run_handoff()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(self.consumption_path, result.stderr)
        self.assertFalse((self.root / "entrega").exists())

    def add_fixture_source(self, relative, value):
        target = self.snapshot / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(value))
        self.files[relative] = hashlib.sha256(target.read_bytes()).hexdigest()
        manifest = json.loads((self.root / "references/snapshot-manifest.json").read_text())
        manifest["files"] = self.files
        manifest["ds_digest"] = hashlib.sha256(json.dumps(self.files, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        self.write_json("references/snapshot-manifest.json", manifest)
        release = json.loads((self.root / "references/release.json").read_text())
        release["ds_digest"] = manifest["ds_digest"]
        self.write_json("references/release.json", release)

    def native_fixture(self, with_evidence=True):
        style_id = "ui-checkbox-label-scaled-five-sixths"
        catalog = json.loads((self.snapshot / self.catalog_path).read_text())
        catalog["styles"].append({"id": style_id, "name": style_id, "category": "complementary",
            "derivedFrom": {"baseStyleId": "ui-body-compact", "scaleFactor": 0.8333333134651184}})
        self.add_fixture_source(self.catalog_path, catalog)
        if with_evidence:
            self.add_fixture_source(self.native_evidence_path, {"status": "VALIDATION_PENDING"})
        self.capture_fixture([style_id])
        return style_id

    def test_native_recipe_keeps_metric_identity_and_pending_evidence(self):
        style_id = self.native_fixture()
        for report in ({"status": "VALIDATION_PENDING"}, {"result": "PASS"}):
            with self.subTest(report=report):
                self.add_fixture_source(self.native_evidence_path, report)
                result = self.run_handoff()
                self.assertEqual(result.returncode, 0, result.stderr)
                handoff = self.result()
                style = handoff["typography"]["styles"][0]
                self.assertEqual(style["id"], style_id)
                self.assertEqual(style["derived_from"]["baseStyleId"], "ui-body-compact")
                native = handoff["typography"]["native_inheritance"]
                self.assertEqual(native["source_report_status"], next(iter(report.values())))
                self.assertEqual(native["destination_validation"], "NOT_RUN")
                self.assertEqual(native["source"]["sha256"], self.files[self.native_evidence_path])
                portable = json.loads(re.search(r"```json\n(.*?)\n```", (self.root / "entrega/replicar-en-figma.md").read_text(), re.S)[1])
                self.assertEqual(portable["typography"], handoff["typography"])

    def test_native_recipe_without_evidence_is_rejected(self):
        self.native_fixture(with_evidence=False)
        result = self.run_handoff()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(self.native_evidence_path, result.stderr)
        self.assertFalse((self.root / "entrega").exists())

    def test_native_family_requires_evidence_even_without_capture(self):
        manifest = json.loads((self.root / "references/snapshot-manifest.json").read_text())
        manifest["components"][0]["amendments"].append(self.native_path)
        self.write_json("references/snapshot-manifest.json", manifest)
        result = self.run_handoff()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(self.native_evidence_path, result.stderr)
        self.assertFalse((self.root / "entrega").exists())

    def test_altered_native_evidence_is_rejected(self):
        self.native_fixture()
        (self.snapshot / self.native_evidence_path).write_text('{"status":"PASS"}')
        result = self.run_handoff()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Fuente alterada: " + self.native_evidence_path, result.stderr)
        self.assertFalse((self.root / "entrega").exists())

    def test_unknown_captured_style_is_rejected(self):
        self.capture_fixture(["unknown-style"])
        result = self.run_handoff()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Identidad tipográfica capturada fuera del catálogo: unknown-style", result.stderr)
        self.assertFalse((self.root / "entrega").exists())


if __name__ == "__main__":
    unittest.main()
