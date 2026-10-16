#!/usr/bin/env python3
"""Review the v0.1.1 TextStyle catalogue and variable evidence without Figma writes.

This is style-definition QA only. It never upgrades component-consumer status,
rewrites historical reports, or infers a successful migration from valid styles.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import sys
import unittest

import typography_qa as qa


SCRIPT = "implementations/figma/typography_consumer_foundation_qa.py"
VARIABLES = "sources/figma-snapshots/typography/variables.after.json"
INVENTORY = "sources/inventories/tokens.inventory.json"
AVATAR = "drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json"
OUTPUT = "implementations/figma/typography.v0.1.1.styles.qa.json"
SCOPES = {"fontFamily": "FONT_FAMILY", "fontStyle": "FONT_STYLE", "fontSize": "FONT_SIZE",
          "lineHeight": "LINE_HEIGHT", "letterSpacing": "LETTER_SPACING"}
MODE_NAMES = {"Contable", "Administrativo", "Servicios", "Personas"}


class VariableUniverse:
    """Resolve each mode by its declared name; never choose an arbitrary value."""
    def __init__(self, collections, variables, named_aliases=False):
        self.collections = {c["id"]: c for c in collections}
        self.variables = {v["id"]: v for v in variables}
        if len(self.collections) != len(collections) or len(self.variables) != len(variables):
            raise ValueError("Duplicate collection or variable identity")
        self.by_name = {}
        self.named_aliases = named_aliases
        for variable in variables:
            collection = self.collections[variable["variableCollectionId"]]
            key = (collection["name"], variable["name"])
            if key in self.by_name:
                raise ValueError("Duplicate variable name within collection")
            self.by_name[key] = variable

    def resolve(self, variable, mode_name):
        seen, chain = set(), []
        while True:
            if variable["id"] in seen:
                raise ValueError("Variable alias cycle")
            seen.add(variable["id"])
            collection = self.collections[variable["variableCollectionId"]]
            modes = collection["modes"]
            selected = [m for m in modes if m["name"] == mode_name]
            if len(selected) != 1:
                if len(modes) != 1:
                    raise ValueError("Missing or ambiguous collection mode")
                selected = modes
            value = variable["valuesByMode"][selected[0]["modeId"]]
            chain.append({"id": variable["id"], "name": variable["name"], "collection": collection["name"]})
            if not isinstance(value, dict) or value.get("type") != "VARIABLE_ALIAS":
                return value, chain
            if "id" in value:
                variable = self.variables[value["id"]]
            elif self.named_aliases and "name" in value:
                # Canonical extension aliases name an existing primitive. Its
                # target's destination ID is evidence, not the historical ID.
                variable = self.by_name[("primitive", value["name"])]
            else:
                raise ValueError("Alias lacks a resolvable identity")


def canonical_universe(inventory, extension):
    collections = [{k: v for k, v in c.items() if k != "variables"} for c in inventory["collections"]]
    variables = [{**v, "variableCollectionId": c["id"]} for c in inventory["collections"] for v in c["variables"]]
    collection = extension["collection"]
    collection_id = "canonical-avatar-extension"
    collections.append({"id": collection_id, "name": collection["name"],
                        "modes": [{"modeId": mid, "name": name} for mid, name in collection["modes"].items()]})
    variables.extend({**v, "id": "canonical-avatar:" + v["name"], "variableCollectionId": collection_id}
                     for v in extension["variables"])
    return VariableUniverse(collections, variables, named_aliases=True)


def equal_value(actual, expected):
    if isinstance(actual, str) and isinstance(expected, str):
        return actual.casefold() == expected.casefold()
    return qa.numeric_equal(actual, expected)


def verify_binding(review, sid, spec, record, field, token, observed, canonical):
    location = {"styleLogicalId": sid, "field": field, "token": token}
    actual = observed.by_name.get(("semantic", token))
    reference = canonical.by_name.get(("semantic", token))
    if actual is None or reference is None:
        review.issue("MISSING_CANONICAL_VARIABLE", "Missing observed or canonical semantic token", **location)
        return None
    if field not in SCOPES:
        review.issue("UNSUPPORTED_TOKEN_FIELD", "Token reference does not name a supported TextStyle field", **location)
        return None
    alias = {"type": "VARIABLE_ALIAS", "id": actual["id"]}
    if record.get("boundVariables", {}).get(field) != alias:
        review.issue("STYLE_BINDING_ID", "Style does not bind the exact observed semantic variable", **location,
                     expected=alias, actual=record.get("boundVariables", {}).get(field))
    if SCOPES[field] not in actual.get("scopes", []) or SCOPES[field] not in reference.get("scopes", []):
        review.issue("VARIABLE_SCOPE", "Observed or canonical variable lacks the required scope", **location)
    expected_type = "STRING" if field in {"fontFamily", "fontStyle"} else "FLOAT"
    if actual["resolvedType"] != expected_type or reference["resolvedType"] != expected_type:
        review.issue("VARIABLE_TYPE", "Observed or canonical variable has the wrong type", **location)
    modes = observed.collections[actual["variableCollectionId"]]["modes"]
    if (len(modes) != 4 or {m["name"] for m in modes} != MODE_NAMES
            or len({m["modeId"] for m in modes}) != 4
            or {m["modeId"] for m in modes} != set(actual["valuesByMode"])):
        review.issue("VARIABLE_MODES", "Expected all four uniquely identified semantic modes", **location)
    wanted = spec[field]
    if isinstance(wanted, dict):
        if wanted.get("unit") != "PIXELS":
            review.issue("BOUND_METRIC_UNIT", "A bound metric must declare PIXELS", **location)
            return None
        wanted = wanted["value"]
    resolutions = {}
    for mode in modes:
        try:
            value, chain = observed.resolve(actual, mode["name"])
            approved_value, approved_chain = canonical.resolve(reference, mode["name"])
        except (KeyError, TypeError, ValueError) as error:
            review.issue("VARIABLE_RESOLUTION", str(error), **location, mode=mode["name"])
            continue
        review.counts["modeResolutions"] += 1
        if not equal_value(value, wanted) or not equal_value(value, approved_value):
            review.issue("VARIABLE_VALUE", "Actual mode value differs from style or canonical token", **location,
                         mode=mode["name"], expected=wanted, canonical=approved_value, actual=value)
        if [(x["collection"], x["name"]) for x in chain] != [(x["collection"], x["name"]) for x in approved_chain]:
            review.issue("ALIAS_IDENTITY", "Alias chain changes semantic identity despite possible numeric equality",
                         **location, mode=mode["name"], actual=chain, canonical=approved_chain)
        resolutions[mode["modeId"]] = {"modeName": mode["name"], "value": value, "chain": chain}
    return {"token": token, "variableId": actual["id"], "scope": SCOPES[field], "modes": resolutions}


def run(args):
    review = qa.Review(args.repo_root)
    for source in (SCRIPT, qa.SCRIPT, qa.CONTRACT, qa.FORMATTING_AMENDMENT):
        review.read_bytes(source)
    inputs = [review.load(path) for path in (args.catalog, args.styles_state, args.styles_readback,
                                            args.variables, INVENTORY, AVATAR)]
    proofs = []
    if all(value is not None for value in inputs):
        catalog, state, readback, variables, inventory, avatar = inputs
        styles = {s["id"]: s for s in catalog["styles"]}
        style_map = state.get("styleMap", {})
        records = readback if isinstance(readback, list) else readback["styles"]
        actual_styles = {r["id"]: r for r in records}
        if (catalog.get("version") != "0.1.1" or len(styles) != 79 or len(catalog["styles"]) != 79
                or set(style_map) != set(styles) or len(set(style_map.values())) != 79 or not all(style_map.values())):
            review.issue("STYLE_MAP_COVERAGE", "Require 79 unique canonical logical and real IDs from v0.1.1")
        if len(actual_styles) != len(records):
            review.issue("DUPLICATE_READBACK_ID", "Repeated TextStyle ID in readback")
        if set(actual_styles) != set(style_map.values()):
            review.issue("STYLE_READBACK_COVERAGE", "Readback must contain exactly the 79 mapped TextStyle IDs",
                         missing=sorted(set(style_map.values()) - set(actual_styles)),
                         added=sorted(set(actual_styles) - set(style_map.values())))
        if state.get("errors"):
            review.issue("STYLE_STATE_ERRORS", "Style state records implementation errors", errors=state["errors"])
        review.validate_derivatives(styles)
        review.validate_formatting_derivatives(styles)
        observed = VariableUniverse(variables["collections"], variables["variables"])
        canonical = canonical_universe(inventory, avatar)
        for sid, spec in styles.items():
            record = actual_styles.get(style_map.get(sid))
            if record is None:
                review.issue("MISSING_STYLE", "Canonical style missing from final readback", styleLogicalId=sid)
                continue
            review.counts["styles"] += 1
            differences = qa.recipe_errors(record, spec)
            differences += [field for field in ("name", "description") if record.get(field) != spec[field]]
            if differences:
                review.issue("STYLE_DEFINITION", "Readback differs from canonical TextStyle", styleLogicalId=sid, fields=differences)
            if set(record.get("boundVariables", {})) != set(spec["tokenRefs"]):
                review.issue("STYLE_BINDING_FIELDS", "Style binding fields differ from canonical tokenRefs", styleLogicalId=sid)
            proof = {"styleLogicalId": sid, "styleId": record["id"], "bindings": {}}
            for field, token in spec["tokenRefs"].items():
                review.counts["bindings"] += 1
                binding = verify_binding(review, sid, spec, record, field, token, observed, canonical)
                if binding is not None:
                    proof["bindings"][field] = binding
            proofs.append(proof)
        for key, expected in {"styles": 79, "bindings": 322, "modeResolutions": 1288}.items():
            if review.counts[key] != expected:
                review.issue("STYLE_QA_COVERAGE", "Validated coverage differs from the complete 79-style catalogue",
                             field=key, expected=expected, actual=review.counts[key])
    base = review.report()
    return {"schema_version": 1, "id": "QA-TYPOGRAPHY-STYLES-001", "version": "0.1.1",
            "result": base["result"], "execution": "LOCAL_SAVED_EVIDENCE_REVIEW", "figmaWrites": "NOT_RUN",
            "scope": "79 canonical TextStyles, exact IDs and definitions, 322 bindings and 1288 four-mode resolutions; excludes component migration",
            "componentMigration": "NOT_VALIDATED_BY_THIS_REPORT", "userAudit": "PENDING",
            "counts": {key: review.counts[key] for key in ("styles", "bindings", "modeResolutions", "derivedStyles", "formattingDerivedStyles")},
            "failureCount": base["failureCount"],
            "blockedCount": base["blockedCount"], "findings": base["findings"], "validatedStyles": proofs,
            "sources": base["sources"], "sourcesDigest": base["sourcesDigest"],
            "limits": ["Variable identities and mode resolution use the saved variable snapshot identified by source hash.",
                       "No consumer, instance scale, geometry, clipping or visual validation is inferred from style-definition PASS."]}


class RegressionTests(unittest.TestCase):
    def fixture(self):
        modes = [{"modeId": str(i), "name": name} for i, name in enumerate(sorted(MODE_NAMES))]
        collections = [{"id": "semantic", "name": "semantic", "modes": modes},
                       {"id": "primitive", "name": "primitive", "modes": [{"modeId": "value", "name": "Value"}]}]
        primitive = {"id": "p", "name": "font/size/14", "variableCollectionId": "primitive", "valuesByMode": {"value": 14}}
        semantic = {"id": "s", "name": "font/size/md", "variableCollectionId": "semantic", "resolvedType": "FLOAT",
                    "scopes": ["FONT_SIZE"], "valuesByMode": {m["modeId"]: {"type": "VARIABLE_ALIAS", "id": "p"} for m in modes}}
        return collections, [semantic, primitive]

    def test_full_four_mode_alias_proof_and_wrong_identity(self):
        collections, variables = self.fixture()
        observed = VariableUniverse(collections, variables)
        canonical = VariableUniverse(copy.deepcopy(collections), copy.deepcopy(variables))
        review = qa.Review(Path.cwd())
        args = (review, "body", {"fontSize": 14}, {"boundVariables": {"fontSize": {"type": "VARIABLE_ALIAS", "id": "s"}}},
                "fontSize", "font/size/md", observed, canonical)
        verify_binding(*args)
        self.assertEqual(review.findings, [])
        self.assertEqual(review.counts["modeResolutions"], 4)
        variables[1]["name"] = "font/size/different-role-same-value"
        review.findings.clear()
        verify_binding(*args)
        self.assertEqual({f["code"] for f in review.findings}, {"ALIAS_IDENTITY"})

    def test_alias_cycle_and_ambiguous_mode_cannot_pass(self):
        collections, variables = self.fixture()
        variables[1]["valuesByMode"]["value"] = {"type": "VARIABLE_ALIAS", "id": "s"}
        with self.assertRaisesRegex(ValueError, "cycle"):
            VariableUniverse(collections, variables).resolve(variables[0], "Contable")
        collections, variables = self.fixture()
        with self.assertRaisesRegex(ValueError, "mode"):
            VariableUniverse(collections, variables).resolve(variables[0], "Unknown mode")

    def test_mode_specific_value_and_scope_are_checked(self):
        collections, variables = self.fixture()
        canonical = VariableUniverse(copy.deepcopy(collections), copy.deepcopy(variables))
        variables[0]["valuesByMode"]["0"] = 15
        variables[0]["scopes"] = []
        review = qa.Review(Path.cwd())
        verify_binding(review, "body", {"fontSize": 14}, {"boundVariables": {"fontSize": {"type": "VARIABLE_ALIAS", "id": "s"}}},
                       "fontSize", "font/size/md", VariableUniverse(collections, variables), canonical)
        self.assertTrue({"VARIABLE_VALUE", "VARIABLE_SCOPE", "ALIAS_IDENTITY"}.issubset({f["code"] for f in review.findings}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--catalog", default=qa.CURRENT_CATALOG)
    parser.add_argument("--styles-state", default=qa.CURRENT_STYLES_STATE)
    parser.add_argument("--styles-readback", default=qa.CURRENT_STYLES_READBACK)
    parser.add_argument("--variables", default=VARIABLES)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(RegressionTests))
        return 0 if result.wasSuccessful() else 1
    try:
        report = run(args)
    except (KeyError, TypeError, ValueError, IndexError, OSError) as error:
        report = {"schema_version": 1, "id": "QA-TYPOGRAPHY-STYLES-001", "version": "0.1.1", "result": "FAIL",
                  "componentMigration": "NOT_VALIDATED_BY_THIS_REPORT", "figmaWrites": "NOT_RUN", "counts": {},
                  "findings": [{"code": "INVALID_EVIDENCE", "message": str(error)}]}
    output = args.output or args.repo_root / OUTPUT
    target = output.resolve()
    if "v0.1.0" in target.name or target in {args.repo_root.resolve() / qa.CURRENT_OUTPUT,
                                            args.repo_root.resolve() / qa.RESTORATION_OUTPUT}:
        parser.error("Style QA cannot overwrite historical, consumer-migration or restoration reports")
    for source in report.get("sources", {}):
        if target == (args.repo_root / source).resolve():
            parser.error("Style QA output cannot overwrite an input source")
    data = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    if not output.exists() or output.read_text(encoding="utf-8") != data:
        output.write_text(data, encoding="utf-8")
    print(json.dumps({"output": str(output), "result": report["result"], "counts": report["counts"],
                      "findings": len(report["findings"])}, ensure_ascii=False))
    return 0 if report["result"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
