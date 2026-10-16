#!/usr/bin/env python3
"""Plan, collect and summarize a complete saved Figma typography capture locally.

No Figma calls. Capture summaries report observations, never migration PASS.
Each generated request returns one <=14500 UTF16-character payload part. Stop
Figma writes before the first request and keep that cut stable across all pages.
"""
from __future__ import annotations

import argparse
from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import typography_qa as qa
import typography_capture_parts as parts


AUDIT = "implementations/figma/typography.v0.1.1.audit.js"
SCRIPT = "implementations/figma/typography_capture_collect.py"
PART_SCRIPT = "implementations/figma/typography_capture_parts.py"


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def write_once(path, data):
    path = Path(path)
    if path.exists():
        if path.read_bytes() != data:
            raise ValueError(f"Existing file has different bytes: {path}; use a new capture directory")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def slug(page_id):
    if not page_id or any(c not in "0123456789:" for c in page_id):
        raise ValueError("Unexpected page ID")
    return page_id.replace(":", "-")


def make_plan(root):
    mapping, catalog, state = (read(root / path) for path in (qa.CURRENT_MAPPING, qa.CURRENT_CATALOG, qa.CURRENT_STYLES_STATE))
    discovery = read(root / qa.DISCOVERY)
    if len(catalog["styles"]) != 79 or set(state["styleMap"]) != {s["id"] for s in catalog["styles"]}:
        raise ValueError("Require current79 catalogue and style map")
    pages = []
    for page in sorted(discovery["pages"], key=lambda p: p["name"]):
        nodes = [n for n in mapping["nodes"] if n["pageId"] == page["id"]]
        ui = [n for n in nodes if n["scope"] == "UI"]
        scaled = [n for n in ui if any(s.get("instanceScale", 1) != 1 for s in n["segments"])]
        pages.append({"id": page["id"], "name": page["name"], "expectedNodes": len(nodes),
                      "expectedUiNodes": len(ui), "expectedUiRanges": sum(len(n["segments"]) for n in ui),
                      "scaledNodeIds": [n["nodeId"] for n in scaled],
                      "scaledRanges": sum(s.get("instanceScale", 1) != 1 for n in ui for s in n["segments"]),
                      "outputName": "census.after.v0.1.1." + slug(page["id"]) + ".json"})
    expected = {"pages": len(pages), "nodes": sum(p["expectedNodes"] for p in pages),
                "uiNodes": sum(p["expectedUiNodes"] for p in pages),
                "uiRanges": sum(p["expectedUiRanges"] for p in pages),
                "scaledNodes": sum(len(p["scaledNodeIds"]) for p in pages),
                "scaledRanges": sum(p["scaledRanges"] for p in pages)}
    if expected != {"pages": 34, "nodes": 3501, "uiNodes": 3351, "uiRanges": 3353, "scaledNodes": 103, "scaledRanges": 103}:
        raise ValueError("Capture plan differs from reviewed34-page/103-scaled scope")
    sources = [qa.CURRENT_MAPPING, qa.CURRENT_CATALOG, qa.CURRENT_STYLES_STATE, qa.DISCOVERY, AUDIT, SCRIPT, PART_SCRIPT, qa.SCRIPT]
    return {"schema_version": 1, "version": "0.1.1", "repoRoot": str(root.resolve()), "fileKey": mapping["fileKey"],
            "expected": expected, "sources": {path: sha(root / path) for path in sources}, "pages": pages,
            "policy": {"figmaWrites": "NOT_PERFORMED_BY_COLLECTOR", "freeze": "All Figma writes must stop before first capture part through last part",
                       "pageCalls": "Capture part0 first, then each missing index; one14500-character payload per call",
                       "scale": "Collect raw ancestor geometry; never infer effective instanceScale by multiplying ancestors",
                       "result": "Coverage summary is not consumer QA or approval"}}


def load_plan(directory):
    plan = read(directory / "plan.json")
    root = Path(plan["repoRoot"])
    changed = [name for name, digest in plan["sources"].items() if not (root / name).is_file() or sha(root / name) != digest]
    if changed:
        raise ValueError("Plan inputs changed; create a new capture plan: " + ", ".join(changed))
    return plan, root


def page_parts(directory, page):
    files = sorted((directory / "parts" / slug(page["id"])).glob("part-*.json"))
    return files, [read(path) for path in files]


def validate_headers(records, page):
    if not records:
        return [0]
    reference = records[0]
    if reference.get("page") != {"id": page["id"], "name": page["name"]}:
        raise ValueError("Capture page identity differs from plan")
    if reference.get("captureVersion") != "0.1.1" or reference.get("structureIncluded") != bool(page["scaledNodeIds"]):
        raise ValueError("Capture version or required scaled structure differs from plan")
    count = reference.get("parts")
    if type(count) is not int or count < 1:
        raise ValueError("Invalid capture part count")
    indices = []
    metadata = ("captureVersion", "page", "nodes", "recipes", "parts", "payloadLength", "payloadFingerprint", "structureIncluded")
    for record in records:
        if any(field not in record or record[field] != reference.get(field) for field in metadata):
            raise ValueError("Mixed capture metadata/fingerprints")
        index = record.get("part")
        if type(index) is not int or not 0 <= index < count or index in indices:
            raise ValueError("Invalid or duplicated capture part")
        if not isinstance(record.get("payload"), str) or len(record["payload"].encode("utf-16-le", "surrogatepass")) // 2 > 14500:
            raise ValueError("Capture part exceeds14500 UTF16 characters or has invalid payload")
        indices.append(index)
    return sorted(set(range(count)) - set(indices))


def decode_census(census):
    columns = census["columns"]
    if len(set(columns)) != len(columns):
        raise ValueError("Duplicate census columns")
    nodes = {}
    for raw in census["nodes"]:
        if len(raw) != len(columns):
            raise ValueError("Census row length differs from columns")
        row = dict(zip(columns, raw))
        node_id = ";".join(census["paths"][i] for i in row["idParts"])
        if node_id in nodes:
            raise ValueError("Repeated census node ID")
        row["nodeId"] = node_id
        row["name"] = census["names"][row["nameIndex"]]
        row["ranges"] = qa.validate_ranges([(a, b, census["recipes"][i]) for a, b, i in row["segments"]])
        nodes[node_id] = row
    return nodes


def summarize_page(census, assignments, styles, style_map):
    nodes = decode_census(census)
    expected = {n["nodeId"]: n for n in assignments}
    result = {"pageId": census["page"]["id"], "pageName": census["page"]["name"], "counts": Counter(),
              "missingNodeIds": sorted(set(expected) - set(nodes)), "extraNodeIds": sorted(set(nodes) - set(expected)),
              "discrepancies": [], "scaledRanges": [], "validation": "NOT_VALIDATED_BY_THIS_SUMMARY"}
    counts = result["counts"]
    counts["observedNodes"] = len(nodes)
    structure = {n["nodeId"]: n for n in census.get("structuralEvidence", {}).get("nodes", [])}
    logical_by_real = {rid: sid for sid, rid in style_map.items()}
    for node_id in sorted(set(expected) & set(nodes)):
        mapped, observed = expected[node_id], nodes[node_id]
        if mapped["scope"] != "UI":
            counts["editorialNodes"] += 1
            continue
        counts["uiNodes"] += 1
        counts["hiddenUiNodes"] += int(not observed["effectiveVisible"])
        assigned = [(s["start"], s["end"], s) for s in mapped["segments"]]
        try:
            aligned = qa.align_ranges(observed["ranges"], observed["ranges"], assigned)
        except ValueError as error:
            result["discrepancies"].append({"nodeId": node_id, "error": "RANGE_COVERAGE", "message": str(error)})
            continue
        for start, end, recipe, _, segment in aligned:
            sid = segment["styleLogicalId"]
            actual_id = recipe.get("textStyleId")
            expected_id = style_map[sid]
            if "textStyleId" not in recipe or not isinstance(actual_id, str):
                classification = "missingStyleIdEvidence"
            elif actual_id == "":
                classification = "emptyStyleId"
            elif actual_id == expected_id:
                classification = "exactStyleId"
            elif actual_id in logical_by_real:
                classification = "otherCanonicalStyleId"
            else:
                classification = "foreignStyleId"
            differences = qa.recipe_errors(recipe, styles[sid], segment.get("recipeScale", 1))
            overrides = recipe.get("textStyleOverrides")
            override_evidence = isinstance(overrides, list) and all(isinstance(x, str) for x in overrides)
            shared_overrides = sorted(set(overrides) & (qa.METRIC_FIELDS | {"textDecoration"})) if override_evidence else None
            counts["uiIntervals"] += 1
            counts[classification] += 1
            counts["metricMismatchIntervals"] += bool(differences)
            counts["missingOverrideEvidenceIntervals"] += not override_evidence
            counts["sharedOverrideIntervals"] += bool(shared_overrides)
            detail = {"nodeId": node_id, "name": observed["name"], "start": start, "end": end,
                      "visible": bool(observed["effectiveVisible"]), "classification": classification,
                      "expectedStyleLogicalId": sid, "expectedTextStyleId": expected_id,
                      "actualTextStyleId": actual_id, "actualStyleLogicalId": logical_by_real.get(actual_id),
                      "metricDifferences": differences, "sharedOverrides": shared_overrides}
            if classification != "exactStyleId" or differences or shared_overrides or not override_evidence:
                result["discrepancies"].append(detail)
            if segment.get("instanceScale", 1) != 1:
                counts["scaledIntervals"] += 1
                counts["scaledEmptyStyleId"] += classification == "emptyStyleId"
                counts["scaledExactStyleId"] += classification == "exactStyleId"
                counts["scaledMetricMismatchIntervals"] += bool(differences)
                captured = structure.get(node_id)
                counts["scaledStructureNodes"] += captured is not None
                result["scaledRanges"].append({**detail, "expectedInstanceScale": segment["instanceScale"],
                    "recipeScale": segment.get("recipeScale", 1), "applicationStatus": segment.get("applicationStatus"),
                    "resolvedRecipe": {k: recipe.get(k) for k in ("fontName", "fontSize", "lineHeight", "letterSpacing", "textDecoration")},
                    "structureEvidence": captured, "effectiveInstanceScale": "NOT_INFERRED"})
    counts.setdefault("exactStyleId", 0)
    counts.setdefault("emptyStyleId", 0)
    result["counts"] = dict(sorted(counts.items()))
    return result


def inspect_capture(directory, plan, root):
    mapping = read(root / qa.CURRENT_MAPPING)
    styles = {s["id"]: s for s in read(root / qa.CURRENT_CATALOG)["styles"]}
    style_map = read(root / qa.CURRENT_STYLES_STATE)["styleMap"]
    result = {"schema_version": 1, "version": "0.1.1", "captureStatus": "NOT_RUN",
              "validation": "NOT_VALIDATED_BY_THIS_SUMMARY", "planSha256": sha(directory / "plan.json"),
              "expected": plan["expected"], "pages": [], "requests": [], "totals": Counter(), "errors": []}
    payloads = {}
    for page in plan["pages"]:
        files, records = page_parts(directory, page)
        row = {"pageId": page["id"], "pageName": page["name"], "captureStatus": "NOT_RUN" if not records else "PARTIAL",
               "partsReceived": len(records), "expectedUiNodes": page["expectedUiNodes"], "expectedUiRanges": page["expectedUiRanges"]}
        try:
            missing = validate_headers(records, page)
            row["missingParts"] = missing
            if missing:
                result["requests"].extend({"pageId": page["id"], "pageName": page["name"], "part": i,
                                           "includeStructure": bool(page["scaledNodeIds"])} for i in missing)
            else:
                payload, census = parts.assemble(records)
                summary = summarize_page(census, [n for n in mapping["nodes"] if n["pageId"] == page["id"]], styles, style_map)
                row.update(summary)
                row["captureStatus"] = "CAPTURE_COMPLETE"
                row["sha256"] = hashlib.sha256(payload.encode("utf-8")).hexdigest()
                row["partSources"] = {str(path): sha(path) for path in files}
                payloads[page["id"]] = payload
                result["totals"].update(summary["counts"])
                if summary["missingNodeIds"] or summary["extraNodeIds"]:
                    result["errors"].append({"pageId": page["id"], "error": "NODE_COVERAGE"})
                if any(d.get("error") == "RANGE_COVERAGE" for d in summary["discrepancies"]):
                    result["errors"].append({"pageId": page["id"], "error": "RANGE_COVERAGE"})
                observed_structure = [n["nodeId"] for n in census.get("structuralEvidence", {}).get("nodes", [])]
                if (set(observed_structure) != set(page["scaledNodeIds"])
                        or len(set(observed_structure)) != len(observed_structure)):
                    result["errors"].append({"pageId": page["id"], "error": "SCALED_STRUCTURE_COVERAGE",
                                             "missing": sorted(set(page["scaledNodeIds"]) - set(observed_structure)),
                                             "extra": sorted(set(observed_structure) - set(page["scaledNodeIds"]))})
        except (KeyError, IndexError, ValueError, TypeError) as error:
            row.update(captureStatus="INVALID", error=str(error))
            result["errors"].append({"pageId": page["id"], "error": str(error)})
        result["pages"].append(row)
    completed = sum(p["captureStatus"] == "CAPTURE_COMPLETE" for p in result["pages"])
    result["totals"]["pagesComplete"] = completed
    result["totals"] = dict(sorted(result["totals"].items()))
    result["captureStatus"] = "CAPTURE_COMPLETE" if completed == len(plan["pages"]) and not result["errors"] else "PARTIAL" if completed or any(p["partsReceived"] for p in result["pages"]) else "NOT_RUN"
    return result, payloads


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("plan", "record", "status", "requests", "export"), nargs="?")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--capture-dir", type=Path)
    parser.add_argument("--response", type=Path, nargs="+")
    parser.add_argument("--limit", type=int, default=2, help="Number of independent one-part request files to emit; never concatenate tool payloads")
    parser.add_argument("--output", type=Path, help="Optional complete JSON summary output")
    parser.add_argument("--output-dir", type=Path, help="Explicit census destination for export")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        tests = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(RegressionTests))
        return 0 if tests.wasSuccessful() else 1
    if args.operation is None or args.capture_dir is None:
        parser.error("Require an operation and --capture-dir")
    directory = args.capture_dir.resolve()
    try:
        if args.operation == "plan":
            plan = make_plan(args.repo_root.resolve())
            write_once(directory / "plan.json", encoded(plan))
            print(json.dumps({"plan": str(directory / "plan.json"), "expected": plan["expected"], "figmaCalls": "NOT_RUN"}))
            return 0
        plan, root = load_plan(directory)
        if args.operation == "record":
            if not args.response:
                raise ValueError("record requires direct JSON response files via --response")
            pending = {}
            pages = {p["id"]: p for p in plan["pages"]}
            for source in args.response:
                record = read(source)
                page = pages[record["page"]["id"]]
                _, existing = page_parts(directory, page)
                destination = directory / "parts" / slug(page["id"]) / f"part-{record['part']:03d}.json"
                if destination.exists() and destination.read_bytes() != source.read_bytes():
                    raise ValueError("Part already exists with different bytes; capture must not mix cuts")
                siblings = [item for item in existing if item["part"] != record["part"]]
                siblings += [read(p) for p in pending.values() if read(p)["page"]["id"] == page["id"]]
                validate_headers(siblings + [record], page)
                pending[destination] = source
            for destination, source in pending.items():
                write_once(destination, source.read_bytes())
        summary, payloads = inspect_capture(directory, plan, root)
        if args.operation == "requests":
            if args.limit < 1:
                raise ValueError("Request limit must be positive")
            pages = {p["id"]: p for p in plan["pages"]}
            requests = []
            for request in summary["requests"][:args.limit]:
                page = pages[request["pageId"]]
                header = "const PAGE_ID=" + json.dumps(page["id"]) + ";const PART_INDEX=" + str(request["part"]) + ";\n"
                header += "const INCLUDE_STRUCTURE=" + json.dumps(bool(page["scaledNodeIds"])) + ";const STRUCTURE_NODE_IDS=" + json.dumps(page["scaledNodeIds"]) + ";\n"
                target = directory / "requests" / (slug(page["id"]) + f"-part-{request['part']:03d}.js")
                write_once(target, (header + (root / AUDIT).read_text(encoding="utf-8")).encode("utf-8"))
                requests.append({**request, "script": str(target)})
            print(json.dumps({"captureStatus": summary["captureStatus"], "requests": requests, "figmaCalls": "NOT_RUN"}, ensure_ascii=False))
        elif args.operation == "export":
            if args.output_dir is None or summary["captureStatus"] != "CAPTURE_COMPLETE":
                raise ValueError("export requires --output-dir and a complete34-page capture")
            targets = [(args.output_dir / p["outputName"], payloads[p["id"]].encode("utf-8")) for p in plan["pages"]]
            for target, data in targets:
                if target.exists() and target.read_bytes() != data:
                    raise ValueError("Final census already exists with different bytes: " + str(target))
            for target, data in targets:
                write_once(target, data)
            print(json.dumps({"exported": len(targets), "outputDir": str(args.output_dir), "validation": summary["validation"]}))
        else:
            print(json.dumps({"captureStatus": summary["captureStatus"], "totals": summary["totals"], "errors": summary["errors"],
                              "pages": [{k: p[k] for k in ("pageId", "pageName", "captureStatus", "partsReceived", "counts", "missingParts") if k in p} for p in summary["pages"]]}, ensure_ascii=False))
        if args.output:
            # Summaries are derived and may progress; raw parts/censuses are immutable.
            protected = {(root / source).resolve() for source in plan["sources"]} | {(directory / "plan.json").resolve()}
            if (args.output.resolve() in protected or args.output.resolve().is_relative_to(directory / "parts")
                    or args.output.name.startswith("census.") or "v0.1.0" in args.output.name):
                raise ValueError("Summary cannot overwrite plan, canonical inputs, historical QA or raw captures")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(encoded(summary))
        return 2 if summary["errors"] else 0
    except (KeyError, IndexError, TypeError, ValueError, OSError) as error:
        parser.error(str(error))


class RegressionTests(unittest.TestCase):
    def fixture(self):
        style = {"fontFamily": "Manrope", "fontStyle": "Regular", "fontWeight": 400, "fontSize": 14,
                 "lineHeight": {"unit": "PIXELS", "value": 20}, "letterSpacing": {"unit": "PIXELS", "value": 0}, "textDecoration": "NONE"}
        recipe = {"fontName": {"family": "Manrope", "style": "Regular"}, "fontSize": 14, "fontWeight": 400,
                  "lineHeight": style["lineHeight"], "letterSpacing": style["letterSpacing"], "textDecoration": "NONE",
                  "textStyleId": "real-style", "textStyleOverrides": []}
        census = {"schema_version": 2, "page": {"id": "1:1", "name": "Test"},
                  "columns": ["idParts", "nameIndex", "effectiveVisible", "segments"], "paths": ["2:1"], "names": ["Label"],
                  "recipes": [recipe], "nodes": [[[0], 0, 0, [[0, 4, 0]]]]}
        assigned = [{"nodeId": "2:1", "scope": "UI", "segments": [{"start": 0, "end": 4, "styleLogicalId": "body", "instanceScale": 1, "recipeScale": 1}]}]
        return census, assigned, {"body": style}, {"body": "real-style", "other": "other-real"}

    def test_empty_exact_other_and_missing_ids_are_distinct(self):
        for value, expected in (("", "emptyStyleId"), ("real-style", "exactStyleId"), ("other-real", "otherCanonicalStyleId"), ("foreign", "foreignStyleId")):
            census, assignments, styles, ids = self.fixture()
            census["recipes"][0]["textStyleId"] = value
            result = summarize_page(census, assignments, styles, ids)
            self.assertEqual(result["counts"][expected], 1)
            self.assertEqual(result["validation"], "NOT_VALIDATED_BY_THIS_SUMMARY")
        census, assignments, styles, ids = self.fixture()
        census["recipes"][0].pop("textStyleId")
        self.assertEqual(summarize_page(census, assignments, styles, ids)["counts"]["missingStyleIdEvidence"], 1)

    def test_scaled_empty_id_with_preserved_metrics_never_infers_link_or_scale(self):
        census, assignments, styles, ids = self.fixture()
        assignments[0]["segments"][0]["instanceScale"] = qa.f32(2 / 3)
        assignments[0]["segments"][0]["applicationStatus"] = "UNRESOLVED_SCALED_LINK"
        census["recipes"][0]["textStyleId"] = ""
        result = summarize_page(census, assignments, styles, ids)
        row = result["scaledRanges"][0]
        self.assertEqual(row["metricDifferences"], [])
        self.assertEqual(row["classification"], "emptyStyleId")
        self.assertEqual(row["effectiveInstanceScale"], "NOT_INFERRED")
        self.assertIsNone(row["structureEvidence"])

    def test_partial_parts_and_immutable_files(self):
        _, records = parts.RegressionTests().fixture()
        page = {"id": "p", "name": "Texto🧾", "scaledNodeIds": []}
        self.assertEqual(validate_headers(records[:1], page), [1])
        with self.assertRaises(ValueError):
            validate_headers([records[0], {**records[1], "payloadFingerprint": "different"}], page)
        with tempfile.TemporaryDirectory(prefix="typography-collector-test-") as directory:
            target = Path(directory) / "immutable.json"
            write_once(target, b"original")
            write_once(target, b"original")
            with self.assertRaises(ValueError):
                write_once(target, b"changed")
            self.assertEqual(target.read_bytes(), b"original")

    def test_split_ranges_and_metric_differences_remain_visible(self):
        census, assignments, styles, ids = self.fixture()
        changed = copy.deepcopy(census["recipes"][0]); changed["fontSize"] = 15
        census["recipes"].append(changed)
        census["nodes"][0][-1] = [[0, 2, 0], [2, 4, 1]]
        result = summarize_page(census, assignments, styles, ids)
        self.assertEqual(result["counts"]["uiIntervals"], 2)
        self.assertEqual(result["counts"]["metricMismatchIntervals"], 1)


if __name__ == "__main__":
    raise SystemExit(main())
