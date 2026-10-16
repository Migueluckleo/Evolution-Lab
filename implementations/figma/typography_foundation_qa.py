#!/usr/bin/env python3
"""Verify canonical TextStyles and explicitly allowed additive foundation bindings.

Never writes Figma, the strict restoration report, or the blocked migration report.
The supplemental preservation PASS is not a claim of literal restoration.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

import typography_qa as qa


STATE = "implementations/figma/typography.v0.1.0.catalog.state.json"
VARIABLES = "sources/figma-snapshots/typography/variables.after.json"
INVENTORY = "sources/inventories/tokens.inventory.json"
AVATAR = "drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json"
STYLE_OUTPUT = "implementations/figma/typography.v0.1.0.styles.qa.json"
PRESERVATION_OUTPUT = "implementations/figma/typography.v0.1.0.preservation.qa.json"
SCOPES = {"fontFamily": "FONT_FAMILY", "fontStyle": "FONT_STYLE", "fontSize": "FONT_SIZE",
          "lineHeight": "LINE_HEIGHT", "letterSpacing": "LETTER_SPACING"}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(root, path, data):
    target = root / path
    if target.resolve() in {(root / qa.OUTPUT).resolve(), (root / qa.RESTORATION_OUTPUT).resolve()}:
        raise ValueError("Cannot overwrite migration or strict restoration report")
    content = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if not target.exists() or target.read_text(encoding="utf-8") != content:
        target.write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    root = args.repo_root.resolve()
    sources = {}

    def load(path):
        sources[path] = sha(root / path)
        return json.loads((root / path).read_text(encoding="utf-8"))

    sources["implementations/figma/typography_foundation_qa.py"] = sha(Path(__file__))
    sources[qa.SCRIPT] = sha(root / qa.SCRIPT)
    catalog = load(qa.CATALOG)
    state = load(STATE)
    readback = load(qa.STYLES_READBACK)["styles"]
    observed = load(VARIABLES)
    inventory = load(INVENTORY)
    avatar = load(AVATAR)
    styles = {s["id"]: s for s in catalog["styles"]}
    real_styles = {s["id"]: s for s in readback}
    style_map = state["styleMap"]
    logical_by_real = {value: key for key, value in style_map.items()}
    variables = {v["id"]: v for v in observed["variables"]}
    collections = {c["id"]: c for c in observed["collections"]}
    semantic = {v["name"]: v for v in variables.values()
                if collections[v["variableCollectionId"]]["name"] == "semantic"}
    canon_by_id = {v["id"]: v for c in inventory["collections"] for v in c["variables"]}
    canonical = {v["name"]: v for c in inventory["collections"] if c["name"] == "semantic" for v in c["variables"]}
    canonical.update({v["name"]: v for v in avatar["variables"]})
    canon_primitive = {v["name"]: v for c in inventory["collections"] if c["name"] == "primitive" for v in c["variables"]}
    failures, validated, binding_count, mode_count = [], [], 0, 0

    def issue(code, **detail):
        failures.append({"code": code, **detail})

    def resolve_actual(variable, mode):
        seen, chain = set(), []
        while True:
            if variable["id"] in seen:
                raise ValueError("Variable alias cycle")
            seen.add(variable["id"])
            chain.append({"id": variable["id"], "name": variable["name"]})
            values = variable["valuesByMode"]
            selected_mode = mode if mode in values else next(iter(values)) if len(values) == 1 else None
            if selected_mode is None:
                raise ValueError("Ambiguous target collection mode")
            value = values[selected_mode]
            if not isinstance(value, dict) or value.get("type") != "VARIABLE_ALIAS":
                return value, chain
            variable = variables[value["id"]]

    def canonical_terminal_names(variable):
        names = set()
        for value in variable["valuesByMode"].values():
            seen = set()
            while isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS":
                target = canon_by_id[value["id"]] if "id" in value else canon_primitive[value["name"]]
                if target["name"] in seen:
                    raise ValueError("Canonical alias cycle")
                seen.add(target["name"])
                names.add(target["name"])
                value = next(iter(target["valuesByMode"].values()))
        return names

    if len(styles) != 75 or len(style_map) != 75 or set(styles) != set(style_map) or len(logical_by_real) != 75:
        issue("STYLE_MAP_COVERAGE")
    if len(real_styles) != len(readback):
        issue("DUPLICATE_READBACK_ID")
    for sid, spec in styles.items():
        record = real_styles.get(style_map.get(sid))
        if record is None:
            issue("MISSING_STYLE", styleLogicalId=sid)
            continue
        differences = qa.recipe_errors(record, spec)
        differences += [field for field in ("name", "description") if record.get(field) != spec[field]]
        if differences:
            issue("STYLE_DEFINITION", styleLogicalId=sid, fields=differences)
        if set(record.get("boundVariables", {})) != set(spec["tokenRefs"]):
            issue("STYLE_BINDING_FIELDS", styleLogicalId=sid)
        proof = {"styleLogicalId": sid, "styleId": record["id"], "bindings": {}}
        for field, token in spec["tokenRefs"].items():
            binding_count += 1
            var = semantic.get(token)
            if var is None or token not in canonical:
                issue("MISSING_CANONICAL_VARIABLE", styleLogicalId=sid, field=field, token=token)
                continue
            alias = {"type": "VARIABLE_ALIAS", "id": var["id"]}
            if record.get("boundVariables", {}).get(field) != alias:
                issue("STYLE_BINDING_ID", styleLogicalId=sid, field=field, expected=alias)
            if SCOPES[field] not in var["scopes"] or SCOPES[field] not in canonical[token]["scopes"]:
                issue("VARIABLE_SCOPE", styleLogicalId=sid, field=field, token=token)
            expected_type = "STRING" if field in {"fontFamily", "fontStyle"} else "FLOAT"
            if var["resolvedType"] != expected_type:
                issue("VARIABLE_TYPE", token=token)
            modes = collections[var["variableCollectionId"]]["modes"]
            if len(modes) != 4 or {m["modeId"] for m in modes} != set(var["valuesByMode"]):
                issue("VARIABLE_MODES", token=token)
            wanted = spec[field]
            if isinstance(wanted, dict):
                if wanted.get("unit") != "PIXELS":
                    issue("BOUND_METRIC_UNIT", styleLogicalId=sid, field=field)
                wanted = wanted["value"]
            resolved = {}
            for mode in modes:
                mode_count += 1
                value, chain = resolve_actual(var, mode["modeId"])
                good = value.lower() == wanted.lower() if isinstance(value, str) and isinstance(wanted, str) else qa.numeric_equal(value, wanted)
                if not good:
                    issue("VARIABLE_VALUE", styleLogicalId=sid, field=field, mode=mode["name"], expected=wanted, actual=value)
                if {x["name"] for x in chain[1:]} != canonical_terminal_names(canonical[token]):
                    issue("ALIAS_IDENTITY", styleLogicalId=sid, field=field, mode=mode["name"], chain=chain)
                resolved[mode["modeId"]] = {"modeName": mode["name"], "value": value, "chain": chain}
            proof["bindings"][field] = {"token": token, "variableId": var["id"], "scope": SCOPES[field], "modes": resolved}
        validated.append(proof)
    style_report = {"schema_version": 1, "id": "QA-TYPOGRAPHY-STYLES-001", "result": "FAIL" if failures else "PASS",
                    "scope": "75 canonical TextStyle definitions and 304 semantic bindings, including actual four-mode alias resolution; excludes component migration.",
                    "componentMigration": "BLOCKED", "userAudit": "PENDING", "figmaWrites": "NOT_RUN",
                    "counts": {"styles": len(validated), "bindings": binding_count, "modeResolutions": mode_count},
                    "findings": failures.copy(), "validatedStyles": validated, "sources": dict(sorted(sources.items()))}
    write(root, STYLE_OUTPUT, style_report)

    # Recompute strict restoration in memory; preserve its persisted FAIL bytes.
    strict_bytes_before = (root / qa.RESTORATION_OUTPUT).read_bytes()
    strict_saved = load(qa.RESTORATION_OUTPUT)
    review = qa.Review(root)
    strict_now = review.run_restoration(SimpleNamespace(before_glob=qa.BEFORE_GLOB, after_glob=qa.AFTER_GLOB))
    sources.update(review.sources)
    if strict_now["findings"] != strict_saved["findings"]:
        issue("STRICT_REPORT_STALE", message="Strict findings changed; preserve and re-review the new baseline before allowing deltas")
    for path, digest in strict_saved["sources"].items():
        if "census.before." in path or "census.after." in path:
            if sources.get(path) != digest:
                issue("STRICT_CAPTURE_CHANGED", source=path)
    _, before = review.census(qa.BEFORE_GLOB, "before")
    _, after = review.census(qa.AFTER_GLOB, "after")
    proof_by_sid = {p["styleLogicalId"]: p for p in validated}
    allowed = []
    for finding in strict_now["findings"]:
        if finding["code"] != "RESTORATION_RECIPE" or finding.get("field") != "boundVariables":
            issue("NON_ALLOWED_RESTORATION_DIFFERENCE", finding=finding)
            continue
        old, new = finding["before"], finding["after"]
        if not set(old).issubset(new) or any(new[k] != v for k, v in old.items()):
            issue("BINDING_REMOVED_OR_REPLACED", finding=finding)
            continue
        nid, start, end = finding["nodeId"], finding["start"], finding["end"]
        old_recipe = next(r for a, b, r in before[nid]["ranges"] if a <= start and b >= end)
        new_recipe = next(r for a, b, r in after[nid]["ranges"] if a <= start and b >= end)
        real_id = old_recipe.get("textStyleId")
        logical_id = logical_by_real.get(real_id)
        if not real_id or new_recipe.get("textStyleId") != real_id or logical_id not in proof_by_sid:
            issue("ADDITION_WITHOUT_ORIGINAL_CANONICAL_STYLE", nodeId=nid, start=start, end=end)
            continue
        additions = sorted(set(new) - set(old))
        valid = True
        for field in additions:
            field_proof = proof_by_sid[logical_id]["bindings"].get(field)
            expected_alias = {"type": "VARIABLE_ALIAS", "id": field_proof["variableId"]} if field_proof else None
            if new[field] != expected_alias or real_styles[real_id].get("boundVariables", {}).get(field) != new[field]:
                issue("NON_CANONICAL_BINDING_ADDITION", nodeId=nid, start=start, end=end, field=field, actual=new[field])
                valid = False
        if valid:
            allowed.append({"nodeId": nid, "pageId": finding["pageId"], "start": start, "end": end,
                            "originalStyleId": real_id, "styleLogicalId": logical_id, "addedFields": additions})
    if (root / qa.RESTORATION_OUTPUT).read_bytes() != strict_bytes_before:
        raise RuntimeError("Strict restoration report was modified unexpectedly")
    preservation = {"schema_version": 1, "id": "QA-TYPOGRAPHY-PRESERVATION-001", "result": "FAIL" if failures else "PASS",
                    "scope": "Original metrics, content, captured properties, bounds, IDs, formatting and existing bindings preserved; only verified additive canonical bindings on original reused TextStyles are allowed.",
                    "literalRestoration": "FAIL", "componentMigration": "BLOCKED", "userAudit": "PENDING", "figmaWrites": "NOT_RUN",
                    "authorization": "Current typography task authorizes canonical foundation TextStyles and semantic bindings; this supplemental check does not redefine literal restoration or validate full component migration.",
                    "strictRestoration": {"path": qa.RESTORATION_OUTPUT, "sha256": sources[qa.RESTORATION_OUTPUT],
                                          "result": strict_saved["result"], "differenceCount": strict_saved["failureCount"]},
                    "styleValidation": {"path": STYLE_OUTPUT, "sha256": sha(root / STYLE_OUTPUT), "result": style_report["result"]},
                    "counts": {**strict_now["counts"], "allowedBindingRanges": len(allowed),
                               "allowedBindingNodes": len({x["nodeId"] for x in allowed}),
                               "reusedStylesWithAdditions": len({x["originalStyleId"] for x in allowed}),
                               "addedBindingReferences": sum(len(x["addedFields"]) for x in allowed)},
                    "allowedCanonicalStyleBindings": allowed, "findings": failures,
                    "limits": strict_now["limits"], "sources": dict(sorted(sources.items()))}
    write(root, PRESERVATION_OUTPUT, preservation)
    print(json.dumps({"styles": {"result": style_report["result"], **style_report["counts"]},
                      "preservation": {"result": preservation["result"], "allowedRanges": len(allowed),
                                       "findings": len(failures)}, "strictRestorationUnchanged": True}))
    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())
