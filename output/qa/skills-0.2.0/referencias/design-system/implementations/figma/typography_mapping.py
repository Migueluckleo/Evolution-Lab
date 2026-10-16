#!/usr/bin/env python3
"""Derive typography migration assignments from saved evidence; never call Figma.

The output is a plan, not implementation QA. Unknown UI recipes are BLOCKED.
Only explicit Figma float32 encodings and zero-unit equivalence are accepted.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
from pathlib import Path
import struct


CATALOG = "specs/tokens/ai-design-system.typography.v0.1.0.json"
CENSUS_GLOB = "sources/figma-snapshots/typography/census.before.*.json"
DISCOVERY = "sources/figma-snapshots/typography.discovery.2026-10-15.json"
CHECKBOX_SCALE = "sources/figma-snapshots/typography/scaled-instance-evidence.json"
COUNT_SCALE = "sources/figma-snapshots/typography/header-scaled-instance-evidence.json"
OUTPUT = "implementations/figma/typography.v0.1.0.mapping.json"
GENERATOR = "implementations/figma/typography_mapping.py"
WEIGHTS = {"Regular": 400, "Medium": 500, "SemiBold": 600, "Bold": 700}
PRESERVE = [
    "characters", "fills and semantic color bindings", "hyperlink",
    "textDecoration", "textCase", "paragraphSpacing", "paragraphIndent",
    "alignment", "textAutoResize", "visibility", "layout and text bounds",
    "component properties", "instance scale", "unrelated instance overrides",
]


def f32(value):
    return struct.unpack("!f", struct.pack("!f", value))[0]


def read_json(root, path):
    return json.loads((root / path).read_text(encoding="utf-8"))


def source_ref(root, path, role):
    return {"path": path, "sha256": hashlib.sha256((root / path).read_bytes()).hexdigest(), "role": role}


def numeric_match(actual, expected, field, notes, percent_ratio=False):
    """No tolerance matching: only exact values or documented float32 encoding."""
    if actual == expected:
        return True
    if actual == f32(expected):
        notes.append({"field": field, "kind": "FLOAT32", "observed": actual, "canonical": expected})
        return True
    if percent_ratio and actual == f32(expected / 100) * 100:
        notes.append({"field": field, "kind": "PERCENT_RATIO_FLOAT32", "observed": actual, "canonical": expected})
        return True
    return False


def unit_match(actual, expected, field, scale, notes):
    if not isinstance(actual, dict) or not isinstance(expected, dict):
        return False
    if (field == "letterSpacing" and actual.get("value") == expected.get("value") == 0
            and actual.get("unit") in {"PIXELS", "PERCENT"}
            and expected.get("unit") in {"PIXELS", "PERCENT"}):
        if actual["unit"] != expected["unit"]:
            notes.append({"field": field, "kind": "EXACT_ZERO_UNIT_CONVERSION", "observed": actual, "canonical": expected})
        return True
    if actual.get("unit") != expected.get("unit"):
        return False
    if expected["unit"] == "AUTO":
        return True
    target = expected["value"] * (scale if expected["unit"] == "PIXELS" else 1)
    return numeric_match(actual.get("value"), target, field, notes,
                         percent_ratio=field == "lineHeight" and expected["unit"] == "PERCENT")


def match_recipe(recipe, style, scale=1):
    notes = []
    font = recipe.get("fontName", {})
    if font.get("family") != style["fontFamily"] or font.get("style") != style["fontStyle"]:
        return None
    axes = font.get("variationSettings", {})
    if set(axes) - {"wght"} or ("wght" in axes and axes["wght"] != style["fontWeight"]):
        return None
    if recipe.get("fontWeight", WEIGHTS.get(font.get("style"))) != style["fontWeight"]:
        return None
    if not numeric_match(recipe.get("fontSize"), style["fontSize"] * scale, "fontSize", notes):
        return None
    for field in ("lineHeight", "letterSpacing"):
        if not unit_match(recipe.get(field), style[field], field, scale, notes):
            return None
    # These are not reasons to create a new metric style. Preserve the original
    # formatting explicitly; reject unknown paragraph/case policies in UI.
    if recipe.get("paragraphSpacing", 0) != 0 or recipe.get("paragraphIndent", 0) != 0:
        return None
    if recipe.get("textCase", "ORIGINAL") != "ORIGINAL":
        return None
    if recipe.get("textDecoration", "NONE") not in {"NONE", "UNDERLINE"}:
        return None
    return notes


def decode_page(path, data):
    if data.get("schema_version") != 2:
        raise ValueError(f"Unsupported census schema: {path}")
    columns = data["columns"]
    result = []
    for raw in data["nodes"]:
        row = dict(zip(columns, raw))
        node_id = ";".join(data["paths"][part] for part in row["idParts"])
        result.append({
            "nodeId": node_id, "pageId": data["page"]["id"], "pageName": data["page"]["name"],
            "name": data["names"][row["nameIndex"]], "source": path,
            "ownerComponentId": row["ownerComponentId"] or None,
            "effectiveVisible": row["effectiveVisible"],
            "before": {key: row[key] for key in ("width", "height", "preservationHash", "charactersHash", "textAutoResize")},
            "rawSegments": row["segments"], "recipes": data["recipes"],
        })
    return result


def scale_rules(root, by_id):
    evidence = read_json(root, CHECKBOX_SCALE)
    rules = []
    for numerator, denominator in ((2, 3), (5, 6)):
        expected = f32(numerator / denominator)
        samples = [sample for sample in evidence
                   if any(a.get("scaleFactor") == expected for a in sample["ancestors"])]
        if not samples:
            raise ValueError(f"Missing API evidence for Checkbox scale {numerator}/{denominator}")
        rules.append({"baseStyleLogicalId": "ui-body-compact", "factor": expected,
                      "ratio": f"{numerator}/{denominator}", "source": CHECKBOX_SCALE,
                      "sampleNodeIds": [s["id"] for s in samples], "mainPageName": "Checkboxes"})
    count = read_json(root, COUNT_SCALE)
    expected = f32(4 / 3)
    if not any(a.get("scaleFactor") == expected and a.get("main") == "155:136" for a in count["ancestors"]):
        raise ValueError("Missing API evidence for Count Small scale4/3")
    rules.append({"baseStyleLogicalId": "micro-count-small", "factor": expected, "ratio": "4/3",
                  "source": COUNT_SCALE, "sampleNodeIds": [count["nodeId"]], "mainPageName": "Dots"})
    for rule in rules:
        candidates = [style for style in by_id.values()
                      if style.get("derivedFrom", {}).get("baseStyleId") == rule["baseStyleLogicalId"]
                      and style["derivedFrom"].get("scaleFactor") == rule["factor"]]
        if len(candidates) != 1:
            raise ValueError(f"Missing or ambiguous materialized style: {rule['ratio']}")
        derived = candidates[0]
        base = by_id[rule["baseStyleLogicalId"]]
        meta = derived["derivedFrom"]
        numerator, denominator = map(int, rule["ratio"].split("/"))
        if meta.get("scaleRatio") != {"numerator": numerator, "denominator": denominator}:
            raise ValueError(f"Derived ratio mismatch: {derived['id']}")
        if meta.get("numericEncoding") != "FLOAT32_BASE_TIMES_FLOAT32_SCALE":
            raise ValueError(f"Unknown derivation encoding: {derived['id']}")
        for field in ("fontFamily", "fontStyle", "fontWeight"):
            if derived[field] != base[field]:
                raise ValueError(f"Derived font identity mismatch: {derived['id']}/{field}")
        if derived["fontSize"] != f32(base["fontSize"] * rule["factor"]):
            raise ValueError(f"Derived font size mismatch: {derived['id']}")
        for field in ("lineHeight", "letterSpacing"):
            expected_metric = dict(base[field])
            if expected_metric["unit"] == "PIXELS":
                expected_metric["value"] = f32(expected_metric["value"] * rule["factor"])
            if derived[field] != expected_metric:
                raise ValueError(f"Derived metric mismatch: {derived['id']}/{field}")
        if "fontSize" in derived.get("tokenRefs", {}) or "lineHeight" in derived.get("tokenRefs", {}):
            raise ValueError(f"Derived metric binding would undo scaling: {derived['id']}")
        rule["styleLogicalId"] = derived["id"]
    return rules


def generate(root):
    catalog = read_json(root, CATALOG)
    styles = catalog["styles"]
    by_id = {s["id"]: s for s in styles}
    if len(by_id) != len(styles):
        raise ValueError("Duplicate canonical style IDs")
    sources = [source_ref(root, CATALOG, "canonical style recipes"),
               source_ref(root, DISCOVERY, "observed old style IDs and recipes"),
               source_ref(root, CHECKBOX_SCALE, "observed Checkbox instance scale"),
               source_ref(root, COUNT_SCALE, "observed Count Small instance scale"),
               source_ref(root, GENERATOR, "deterministic mapping generator")]
    nodes = []
    pages = []
    for file in sorted(root.glob(CENSUS_GLOB)):
        path = file.relative_to(root).as_posix()
        data = read_json(root, path)
        decoded = decode_page(path, data)
        nodes.extend(decoded)
        pages.append({"pageId": data["page"]["id"], "name": data["page"]["name"],
                      "source": path, "nodeCount": len(decoded),
                      "segmentCount": sum(len(n["rawSegments"]) for n in decoded)})
        sources.append(source_ref(root, path, "before census, all text nodes and ranges"))
    by_node = {n["nodeId"]: n for n in nodes}
    if len(by_node) != len(nodes):
        raise ValueError("Duplicate census node IDs")
    rules = scale_rules(root, by_id)
    output_nodes, blocked = [], []
    counts = collections.Counter()
    for node in nodes:
        is_instance = node["nodeId"].startswith("I")
        scope = "UI" if node["ownerComponentId"] or is_instance else "DOCUMENTATION"
        record = {k: v for k, v in node.items() if k not in {"rawSegments", "recipes"}}
        record.update({"scope": scope, "fate": "INSTANCE" if is_instance else "MAIN_DIRECT", "segments": []})
        counts["nodes"] += 1
        counts["uiNodes" if scope == "UI" else "documentationNodes"] += 1
        counts["instanceNodes" if is_instance else "directNodes"] += 1
        for start, end, recipe_index in node["rawSegments"]:
            recipe = node["recipes"][recipe_index]
            segment = {"start": start, "end": end, "recipeIndex": recipe_index,
                       "oldStyleId": recipe.get("textStyleId"), "styleLogicalId": None,
                       "expectedScale": 1, "recipeScale": 1, "instanceScale": 1, "normalizations": [],
                       "preserveFormatting": {field: recipe.get(field) for field in
                          ("textDecoration", "textCase", "paragraphSpacing", "paragraphIndent", "hyperlink")},
                       "beforeBoundVariables": recipe.get("boundVariables", {}),
                       "beforeTextStyleOverrides": recipe.get("textStyleOverrides")}
            counts["segments"] += 1
            if scope == "DOCUMENTATION":
                segment.update({"status": "NOT_APPLICABLE", "action": "PRESERVE_LEGACY_DOCUMENTATION",
                                "reason": "Historical editorial text outside component scope; no typography or geometry edit."})
                counts["documentationSegments"] += 1
            else:
                counts["uiSegments"] += 1
                matches = []
                for style in styles:
                    if "derivedFrom" in style:
                        continue  # Only the documented scaled consumers may use these styles.
                    notes = match_recipe(recipe, style)
                    if notes is not None:
                        matches.append((style["id"], 1, notes, None))
                # Fractional text keeps its existing instance scale, while the
                # applied derived style already contains resolved metrics.
                # Its recipeScale is1, not another application of instanceScale.
                if not matches and is_instance:
                    principal = by_node.get(node["nodeId"].split(";")[-1])
                    for rule in rules:
                        style = by_id[rule["baseStyleLogicalId"]]
                        derived = by_id[rule["styleLogicalId"]]
                        notes = match_recipe(recipe, derived, 1)
                        if notes is None or not principal or principal["pageName"] != rule["mainPageName"]:
                            continue
                        if node["nodeId"] not in derived.get("consumerScope", {}).get("instanceTextNodeIds", []):
                            continue
                        if match_recipe(recipe, style, rule["factor"]) is None:
                            continue
                        principal_recipes = [principal["recipes"][r] for _, _, r in principal["rawSegments"]]
                        if not principal_recipes or not all(match_recipe(r, style) is not None for r in principal_recipes):
                            continue
                        scale = {**rule, "principalTextNodeId": principal["nodeId"],
                                 "principalComponentId": principal["ownerComponentId"],
                                 "instanceScale": rule["factor"], "recipeScale": 1,
                                 "method": "Preserve one effective instance scale; derived style metrics are already materialized. Never multiply ancestor scales or multiply the derived recipe again.",
                                 "evidenceScope": "API representative scale, matching principal, exact float32 resolved recipe and enumerated consumer scope; final linked-style readback remains required."}
                        matches.append((derived["id"], 1, notes, scale))
                if len(matches) != 1:
                    segment.update({"status": "BLOCKED", "action": "NO_WRITE",
                                    "reason": "NO_EXACT_CATALOG_MATCH" if not matches else "AMBIGUOUS_CATALOG_MATCH",
                                    "candidateStyleIds": [m[0] for m in matches]})
                    blocked.append({"nodeId": node["nodeId"], "pageId": node["pageId"],
                                    "start": start, "end": end, "recipeIndex": recipe_index,
                                    "reason": segment["reason"], "observedRecipe": recipe})
                    counts["blockedSegments"] += 1
                else:
                    style_id, scale, notes, scale_evidence = matches[0]
                    segment.update({"status": "MAPPED", "styleLogicalId": style_id,
                                    "expectedScale": scale, "recipeScale": scale,
                                    "instanceScale": scale_evidence["factor"] if scale_evidence else 1,
                                    "normalizations": notes,
                                    "action": "APPLY_MATERIALIZED_DERIVED_STYLE" if scale_evidence else "APPLY_CATALOG_STYLE"})
                    if scale_evidence:
                        segment["scaleEvidence"] = scale_evidence
                        counts["scaledSegments"] += 1
                    counts["mappedUiSegments"] += 1
            record["segments"].append(segment)
        output_nodes.append(record)
    reuse = []
    for old in read_json(root, DISCOVERY)["styles"]:
        candidates = [s["id"] for s in styles if match_recipe(old, s) is not None]
        reuse.append({"figma_style_id": old["id"], "figma_style_key": old["key"], "old_name": old["name"],
                      "style_id": candidates[0] if len(candidates) == 1 else None,
                      "action": "REUSE_AND_RENAME_AFTER_CONSUMER_CHECK" if len(candidates) == 1 else "BLOCKED",
                      "source": DISCOVERY,
                      "precondition": "Read actual style and all consumers; preserve semantic bindings. Migrate duplicate old IDs before considering removal; never delete by name."})
    counts.update({"pages": len(pages), "catalogStyles": len(styles), "oldStyleReuseCandidates": len(reuse)})
    counts.setdefault("blockedSegments", 0)
    return {
        "schema_version": 1, "id": "FOUNDATIONS-TYPOGRAPHY-001", "version": catalog["version"],
        "fileKey": "tj3WIBEZDGLVs7MJWKCwgf", "provenance": "DERIVED",
        "status": "BLOCKED" if blocked else "READY_FOR_APPLICATION",
        "implementationValidation": "NOT_PERFORMED_BY_THIS_MAPPING",
        "generator": GENERATOR, "sources": sources, "summary": dict(sorted(counts.items())),
        "policies": {
            "uiScope": "ownerComponentId nonempty OR nodeId starts with I; includes instances outside component masters.",
            "documentationScope": "No owner and non-instance in legacy census: NOT_APPLICABLE; preserve existing typography and geometry.",
            "newTypographyDocumentation": "Uses the18 base styles; it was created after this before-census and is validated separately, not fabricated as baseline nodes.",
            "normalization": "Only exact zero PIXELS/PERCENT equivalence, float32 numeric encoding, and percent line-height f32(value/100)*100; no nearest-style matching.",
            "decoration": "Underline remains a semantic range property; preserve it after style assignment rather than creating duplicate metric styles.",
            "scaling": "For the103 scoped fractional ranges, apply the explicit materialized derived style with recipeScale=1 while preserving instanceScale. expectedScale is the compatibility alias of recipeScale, never instanceScale. Do not multiply ancestor scaleFactor values, scale the derived recipe again, or replace the style with a free fractional font-size override.",
            "application": "Logical IDs only. Resolve real TextStyle IDs from the later verified implementation state; no guessed IDs.",
            "preserve": PRESERVE,
            "bindings": "Preserve semantic identity of node/range bindings; style application must not silently replace specific aliases by numerically equal tokens.",
        },
        "pages": pages, "nodes": output_nodes,
        "existing_style_reuse_candidates": reuse, "blocked": blocked,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path, help="Defaults to the persistent mapping inside repo-root")
    args = parser.parse_args()
    root = args.repo_root.resolve()
    result = generate(root)
    output = args.output or root / OUTPUT
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "status": result["status"], **result["summary"]}, ensure_ascii=False))
    return 2 if result["status"] == "BLOCKED" else 0


if __name__ == "__main__":
    raise SystemExit(main())
