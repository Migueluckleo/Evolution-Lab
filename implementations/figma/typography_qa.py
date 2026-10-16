#!/usr/bin/env python3
"""Independently validate saved typography migration evidence; never call Figma.

No epsilon, rounding-to-pass, positional segment matching or guessed style IDs.
The output is deterministic for its input bytes. Missing evidence cannot PASS.
"""
from __future__ import annotations

import argparse
from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import struct
import sys
import tempfile
import unittest


CATALOG = "specs/tokens/ai-design-system.typography.v0.1.0.json"
MAPPING = "implementations/figma/typography.v0.1.0.mapping.json"
STYLES_STATE = "implementations/figma/typography.v0.1.0.catalog.state.json"
CONTRACT = "specs/foundations/typography.contract.v0.1.0.md"
STYLES_READBACK = "implementations/figma/typography.v0.1.0.styles.readback.json"
INSTANCE_SCALES = "implementations/figma/typography.v0.1.0.instance-scales.readback.json"
OUTPUT = "implementations/figma/typography.v0.1.0.qa.json"
RESTORATION_OUTPUT = "implementations/figma/typography.v0.1.0.restoration.qa.json"
BEFORE_GLOB = "sources/figma-snapshots/typography/census.before.*.json"
AFTER_GLOB = "sources/figma-snapshots/typography/census.after.*.json"
# Keep the exported historical constants for the v0.1.0 foundation verifier.
# CLI migration defaults advance together without retargeting its saved reports.
CURRENT_VERSION = "0.1.1"
CURRENT_CATALOG = "specs/tokens/ai-design-system.typography.v0.1.1.json"
CURRENT_MAPPING = "implementations/figma/typography.v0.1.1.mapping.json"
CURRENT_STYLES_STATE = "implementations/figma/typography.v0.1.1.catalog.state.json"
CURRENT_STYLES_READBACK = "implementations/figma/typography.v0.1.1.styles.readback.json"
CURRENT_INSTANCE_SCALES = "implementations/figma/typography.v0.1.1.instance-scales.readback.json"
CURRENT_OUTPUT = "implementations/figma/typography.v0.1.1.qa.json"
CURRENT_AFTER_GLOB = "sources/figma-snapshots/typography/census.after.v0.1.1.*.json"
FORMATTING_AMENDMENT = "specs/foundations/typography.formatting.amendment.v0.1.1.md"
DISCOVERY = "sources/figma-snapshots/typography.discovery.2026-10-15.json"
VARIABLE_FILES = (
    "sources/figma-snapshots/typography/variables.before.json",
    "sources/figma-snapshots/typography/metric-variables.before.json",
)
SCRIPT = "implementations/figma/typography_qa.py"
EXPECTED = {"pages": 34, "nodes": 3501, "uiNodes": 3351,
            "uiSegments": 3353, "documentationNodes": 150,
            "documentationSegments": 150, "scaledSegments": 103,
            "catalogStyles": 75}
FIELDS = ("fontFamily", "fontStyle", "fontSize", "lineHeight", "letterSpacing")
METRIC_FIELDS = set(FIELDS) | {"fontName", "fontWeight"}
FORMATTING = ("fills", "hyperlink", "textDecoration", "textCase",
              "paragraphSpacing", "paragraphIndent")
NODE_PRESERVE = ("name", "pageId", "ownerComponentId", "effectiveVisible",
                 "width", "height", "charactersHash", "textAutoResize")
WEIGHTS = {"Regular": 400, "Medium": 500, "SemiBold": 600, "Bold": 700}


def f32(value):
    return struct.unpack("!f", struct.pack("!f", value))[0]


def numeric_equal(actual, expected, ratio=False):
    if not isinstance(actual, (int, float)) or isinstance(actual, bool):
        return False
    return (actual == expected or actual == f32(expected)
            or (ratio and actual == f32(expected / 100) * 100))


def metric_equal(actual, expected, scale=1, line_height=False):
    if not isinstance(actual, dict) or not isinstance(expected, dict):
        return False
    if (not line_height and actual.get("value") == expected.get("value") == 0
            and actual.get("unit") in {"PIXELS", "PERCENT"}
            and expected.get("unit") in {"PIXELS", "PERCENT"}):
        return True
    if actual.get("unit") != expected.get("unit"):
        return False
    if expected["unit"] == "AUTO":
        return True
    value = expected["value"] * (scale if expected["unit"] == "PIXELS" else 1)
    return numeric_equal(actual.get("value"), value,
                         ratio=line_height and expected["unit"] == "PERCENT")


def recipe_errors(recipe, style, scale=1, check_decoration=True):
    """Compare resolved fields, independently from the migration generator."""
    errors = []
    font = recipe.get("fontName", {})
    for actual, expected, label in ((font.get("family"), style["fontFamily"], "fontFamily"),
                                    (font.get("style"), style["fontStyle"], "fontStyle")):
        if actual != expected:
            errors.append(label)
    axes = font.get("variationSettings", {})
    if set(axes) - {"wght"} or axes.get("wght", style["fontWeight"]) != style["fontWeight"]:
        errors.append("variationSettings")
    if recipe.get("fontWeight", axes.get("wght", WEIGHTS.get(font.get("style")))) != style["fontWeight"]:
        errors.append("fontWeight")
    if not numeric_equal(recipe.get("fontSize"), style["fontSize"] * scale):
        errors.append("fontSize")
    for field in ("lineHeight", "letterSpacing"):
        if not metric_equal(recipe.get(field), style[field], scale, field == "lineHeight"):
            errors.append(field)
    if check_decoration and recipe.get("textDecoration") != style.get("textDecoration", "NONE"):
        errors.append("textDecoration")
    return errors


def preserved_recipe_equal(before, after, ignore_fields=()):
    """Only the equivalent named Manrope wght axis may change representation."""
    omitted = set(ignore_fields) | {"fontName"}
    if {k: v for k, v in before.items() if k not in omitted} != {
            k: v for k, v in after.items() if k not in omitted}:
        return False
    old, new = before.get("fontName"), after.get("fontName")
    if old == new:
        return True
    if not isinstance(old, dict) or not isinstance(new, dict):
        return False
    if {k: v for k, v in old.items() if k != "variationSettings"} != {
            k: v for k, v in new.items() if k != "variationSettings"}:
        return False
    weight = WEIGHTS.get(old.get("style"))
    return old.get("family") == "Manrope" and weight is not None and all(
        name.get("variationSettings", {}) in ({}, {"wght": weight}) for name in (old, new))


def validate_ranges(ranges):
    """Require complete, nonoverlapping intervals independent of array order."""
    if not ranges:
        raise ValueError("Text node has no ranges")
    ordered = sorted(ranges, key=lambda r: (r[0], r[1]))
    if len(ordered) == 1 and ordered[0][0:2] == (0, 0):
        return ordered
    end = 0
    for start, stop, _ in ordered:
        if not isinstance(start, int) or not isinstance(stop, int) or start != end or stop <= start:
            raise ValueError("Ranges have gap, overlap, invalid bounds or duplicate empty range")
        end = stop
    return ordered


def align_ranges(before, after, assignments):
    """Partition the union of boundaries; accept semantically equivalent merges/splits."""
    sequences = [validate_ranges(items) for items in (before, after, assignments)]
    ends = [items[-1][1] for items in sequences]
    if len(set(ends)) != 1:
        raise ValueError("Range extents differ")
    if ends[0] == 0:
        return [(0, 0, *(items[0][2] for items in sequences))]
    boundaries = sorted({p for items in sequences for a, b, _ in items for p in (a, b)})
    positions = [0, 0, 0]
    result = []
    for start, end in zip(boundaries, boundaries[1:]):
        values = []
        for i, items in enumerate(sequences):
            while items[positions[i]][1] <= start:
                positions[i] += 1
            a, b, value = items[positions[i]]
            if a > start or b < end:
                raise ValueError("Uncovered interval")
            values.append(value)
        result.append((start, end, *values))
    return result


class Review:
    def __init__(self, root):
        self.root = root.resolve()
        self.findings = []
        self.sources = {}
        self.counts = Counter()
        self.mode = "migration"
        self.editorial_binding_rule = False
        self.version = CURRENT_VERSION
        self.expected = EXPECTED.copy()
        self.expected["catalogStyles"] = 79

    def issue(self, code, message, status="FAIL", **location):
        self.findings.append({"code": code, "status": status, "message": message, **location})

    def path(self, path):
        path = Path(path)
        resolved = (path if path.is_absolute() else self.root / path).resolve()
        if not resolved.is_relative_to(self.root):
            raise ValueError(f"Evidence path escapes repository: {path}")
        return resolved

    def read_bytes(self, path, required=True):
        file = self.path(path)
        if not file.is_file():
            if required:
                self.issue("MISSING_EVIDENCE", "Required evidence file is missing", "BLOCKED",
                           source=file.relative_to(self.root).as_posix())
            return None
        data = file.read_bytes()
        self.sources[file.relative_to(self.root).as_posix()] = hashlib.sha256(data).hexdigest()
        return data

    def load(self, path, required=True):
        data = self.read_bytes(path, required)
        return json.loads(data) if data is not None else None

    def census(self, pattern, phase):
        pages, nodes = {}, {}
        files = sorted(self.root.glob(pattern))
        if pattern == AFTER_GLOB:
            # Historical wildcard predates versioned final captures. Never mix
            # its 34 restored pages with the separate v0.1.1 migration cut.
            files = [p for p in files if not p.name.startswith("census.after.v")]
        for file in files:
            data = self.load(file)
            try:
                if data.get("schema_version") != 2:
                    raise ValueError("Expected census schema_version 2")
                page = data["page"]
                if page["id"] in pages:
                    raise ValueError("Duplicate page ID")
                columns = data["columns"]
                required = {"idParts", "nameIndex", "effectiveVisible", "width", "height", "segments",
                            "preservationHash", "ownerComponentId", "textAutoResize", "charactersHash"}
                if len(set(columns)) != len(columns) or not required.issubset(columns):
                    raise ValueError("Missing or duplicate columns")
                pages[page["id"]] = {"page": page, "components": data["components"]}
                component_ids = [c["id"] for c in data["components"]]
                if len(set(component_ids)) != len(component_ids):
                    raise ValueError("Duplicate component IDs")
                for raw in data["nodes"]:
                    if len(raw) != len(columns):
                        raise ValueError("Row length differs from columns")
                    row = dict(zip(columns, raw))
                    if any(not isinstance(i, int) or i < 0 or i >= len(data["paths"]) for i in row["idParts"]):
                        raise ValueError("Invalid idParts reference")
                    node_id = ";".join(data["paths"][i] for i in row["idParts"])
                    if not node_id or node_id in nodes:
                        raise ValueError("Empty or duplicate text node ID")
                    if not 0 <= row["nameIndex"] < len(data["names"]):
                        raise ValueError("Invalid nameIndex")
                    ranges = []
                    for start, end, ri in row["segments"]:
                        if not isinstance(ri, int) or not 0 <= ri < len(data["recipes"]):
                            raise ValueError("Invalid recipeIndex")
                        ranges.append((start, end, data["recipes"][ri]))
                    validate_ranges(ranges)
                    nodes[node_id] = {**row, "nodeId": node_id, "pageId": page["id"],
                                      "name": data["names"][row["nameIndex"]], "ranges": ranges,
                                      "recipes": data["recipes"],
                                      "source": file.relative_to(self.root).as_posix()}
            except (KeyError, TypeError, ValueError, IndexError) as error:
                self.issue("CENSUS_SCHEMA", str(error), phase=phase,
                           source=file.relative_to(self.root).as_posix())
        self.counts[f"{phase}Pages"] = len(pages)
        self.counts[f"{phase}Nodes"] = len(nodes)
        return pages, nodes

    def validate_sources(self, refs):
        for ref in refs:
            data = self.read_bytes(ref["path"])
            if data is not None and self.sources[ref["path"]] != ref["sha256"]:
                self.issue("SOURCE_HASH_MISMATCH", "Mapping input changed since mapping was derived",
                           source=ref["path"])

    def run_restoration(self, args):
        """Restoration is judged against original evidence, never the new style map."""
        self.mode = "restoration"
        self.version = "0.1.0"
        self.read_bytes(SCRIPT)
        discovery = self.load(DISCOVERY)
        before_pages, before_nodes = self.census(args.before_glob, "before")
        after_pages, after_nodes = self.census(args.after_glob, "after")
        shared_files = set(self.root.glob(args.before_glob)) & set(self.root.glob(args.after_glob))
        if shared_files:
            self.issue("RESTORATION_EVIDENCE_PHASES", "Before and restored evidence must be separate captures",
                       sources=sorted(p.relative_to(self.root).as_posix() for p in shared_files))
        if discovery is None:
            return self.report()
        discovery_ids = {p["id"] for p in discovery["pages"]}
        if set(before_pages) != discovery_ids or len(before_pages) != EXPECTED["pages"]:
            self.issue("BEFORE_PAGE_COVERAGE", "Original census differs from 34-page discovery")
        if len(before_nodes) != EXPECTED["nodes"]:
            self.issue("BEFORE_NODE_COVERAGE", "Original census differs from 3501-node baseline")
        if not after_pages:
            self.issue("AFTER_NOT_AVAILABLE", "Restoration after census has not been provided", "BLOCKED")
            return self.report()
        if set(after_pages) != set(before_pages):
            self.issue("PAGE_COVERAGE", "Original/restored page sets differ",
                       missing=sorted(set(before_pages) - set(after_pages)), added=sorted(set(after_pages) - set(before_pages)))
        for pid in sorted(set(before_pages) & set(after_pages)):
            before, after = before_pages[pid], after_pages[pid]
            if before["page"] != after["page"]:
                self.issue("PAGE_CHANGED", "Original page identity/name changed", pageId=pid)
            if sorted(before["components"], key=lambda x: x["id"]) != sorted(after["components"], key=lambda x: x["id"]):
                self.issue("COMPONENT_STRUCTURE", "Original component IDs/names/types/parents changed", pageId=pid)
        if set(before_nodes) != set(after_nodes):
            self.issue("NODE_COVERAGE", "Original/restored text IDs differ",
                       missing=sorted(set(before_nodes) - set(after_nodes)), added=sorted(set(after_nodes) - set(before_nodes)))
        for nid in sorted(set(before_nodes) & set(after_nodes)):
            self.compare_restored_node(before_nodes[nid], after_nodes[nid])
        for key in ("uiNodes", "uiSegments", "documentationNodes", "documentationSegments"):
            if self.counts[key] != EXPECTED[key]:
                self.issue("SCOPE_COUNT", "Restoration scope count differs from original baseline",
                           field=key, expected=EXPECTED[key], actual=self.counts[key])
        return self.report()

    def compare_restored_node(self, before, after):
        nid = before["nodeId"]
        location = {"nodeId": nid, "pageId": before["pageId"]}
        prefix = "ui" if before["ownerComponentId"] or nid.startswith("I") else "documentation"
        self.counts[prefix + "Nodes"] += 1
        self.counts[prefix + "Segments"] += len(before["ranges"])
        self.counts[prefix + "AfterSegments"] += len(after["ranges"])
        for field in NODE_PRESERVE:
            if before[field] != after[field]:
                self.issue("RESTORATION_NODE_PROPERTY", "Original text node property was not restored",
                           **location, field=field, before=before[field], after=after[field])
        old_bounds = sorted((a, b) for a, b, _ in before["ranges"])
        new_bounds = sorted((a, b) for a, b, _ in after["ranges"])
        if old_bounds != new_bounds:
            self.counts["nodesWithChangedSegmentation"] += 1
        if before["preservationHash"] != after["preservationHash"]:
            self.issue("RESTORATION_PRESERVATION_HASH", "Opaque original properties are not proven restored",
                       "BLOCKED" if old_bounds != new_bounds else "FAIL", **location,
                       before=before["preservationHash"], after=after["preservationHash"],
                       segmentationChanged=old_bounds != new_bounds)
        else:
            self.counts["preservationHashesEqual"] += 1
        try:
            aligned = align_ranges(before["ranges"], after["ranges"], before["ranges"])
        except ValueError as error:
            self.issue("RESTORATION_RANGE_COVERAGE", str(error), **location)
            return
        for start, end, old, new, _ in aligned:
            loc = {**location, "start": start, "end": end}
            self.counts["comparedIntervals"] += 1
            for field in sorted(set(old) | set(new)):
                original, restored = old.get(field), new.get(field)
                if field == "fontSize":
                    equal = numeric_equal(restored, original) if isinstance(original, (int, float)) else original == restored
                elif field in {"lineHeight", "letterSpacing"}:
                    equal = metric_equal(restored, original, line_height=field == "lineHeight")
                elif field == "textStyleOverrides" and isinstance(original, list) and isinstance(restored, list):
                    equal = sorted(original) == sorted(restored)
                else:
                    equal = original == restored
                if not equal:
                    self.issue("RESTORATION_RECIPE", "Original range property was not restored", **loc,
                               field=field, before=original, after=restored)
                elif original != restored:
                    self.counts["acceptedRepresentationDifferences"] += 1
                if field == "textStyleId" and equal:
                    self.counts["originalStyleIdsRestored"] += 1
                if field == "boundVariables" and equal:
                    self.counts["originalBindingsRestored"] += 1

    def run(self, args):
        catalog = self.load(args.catalog)
        mapping = self.load(args.mapping)
        state = self.load(args.styles_state)
        discovery = self.load(DISCOVERY)
        self.read_bytes(SCRIPT)
        # §5 permits additive canonical bindings on an original reused style,
        # not arbitrary editorial changes or a blanket exception by node ID.
        self.editorial_binding_rule = self.read_bytes(CONTRACT) is not None
        if any(d is None for d in (catalog, mapping, state, discovery)):
            return self.report()
        styles = {s["id"]: s for s in catalog["styles"]}
        self.version = catalog.get("version")
        count_by_version = {"0.1.0": 75, "0.1.1": 79}
        self.expected["catalogStyles"] = count_by_version.get(self.version)
        if (len(styles) != len(catalog["styles"])
                or len(styles) != self.expected["catalogStyles"]):
            self.issue("CATALOG_IDS", "Canonical catalogue must have the reviewed count of unique IDs for its version",
                       version=self.version, expected=self.expected["catalogStyles"], actual=len(styles))
        if mapping.get("version") != self.version:
            self.issue("CATALOG_MAPPING_VERSION", "Catalogue and mapping versions differ")
        self.counts["catalogStyles"] = len(styles)
        self.validate_derivatives(styles)
        if self.version == "0.1.1":
            self.read_bytes(FORMATTING_AMENDMENT)
            self.validate_formatting_derivatives(styles)
        self.validate_sources(mapping["sources"])
        if mapping.get("blocked") or mapping.get("status") != "READY_FOR_APPLICATION":
            self.issue("MAPPING_NOT_READY", "Mapping has blocked or unprepared assignments")
        for key, value in self.expected.items():
            if mapping["summary"].get(key) != value:
                self.issue("MAPPING_SCOPE", "Mapping scope differs from reviewed baseline",
                           field=key, expected=value, actual=mapping["summary"].get(key))
        style_map = state.get("styleMap", {})
        if set(style_map) != set(styles) or len(set(style_map.values())) != len(styles) or not all(style_map.values()):
            self.issue("STYLE_MAP", "Style map must assign a unique real ID to each canonical style")
        if state.get("errors"):
            self.issue("STYLE_STATE_ERRORS", "Style implementation reports errors", errors=state["errors"])
        variables = {}
        for path in VARIABLE_FILES:
            for var in self.load(path) or []:
                if var.get("scopes") and (var.get("collectionId") == "VariableCollectionId:6:2"
                                         or var["name"].startswith(("font/line-height/", "font/letter-spacing/"))):
                    variables[var["name"]] = var
        expected_bindings = {}
        for sid, style in styles.items():
            expected_bindings[sid] = {}
            for field, token in style["tokenRefs"].items():
                if token not in variables:
                    self.issue("MISSING_VARIABLE", "Missing local variable identity", styleLogicalId=sid, token=token)
                else:
                    expected_bindings[sid][field] = {"type": "VARIABLE_ALIAS", "id": variables[token]["id"]}
        readback = self.load(args.styles_readback)
        style_readback = {}
        if readback is not None:
            records = readback if isinstance(readback, list) else readback.get("styles", [])
            style_readback = {r["id"]: r for r in records}
            if len(style_readback) != len(records):
                self.issue("DUPLICATE_READBACK_ID", "Duplicate IDs in style readback")
            for sid, style in styles.items():
                record = style_readback.get(style_map.get(sid))
                if record is None:
                    self.issue("STYLE_NOT_READ", "Canonical style absent from final readback", styleLogicalId=sid)
                    continue
                self.counts["stylesRead"] += 1
                differences = recipe_errors(record, style)
                for field in ("name", "description"):
                    if record.get(field) != style[field]:
                        differences.append(field)
                if differences:
                    self.issue("STYLE_DEFINITION", "Final style differs from canonical definition",
                               styleLogicalId=sid, fields=differences)
                actual_bindings = record.get("boundVariables", {})
                for field, binding in expected_bindings[sid].items():
                    if actual_bindings.get(field) != binding:
                        self.issue("STYLE_BINDING", "Style semantic binding differs", styleLogicalId=sid,
                                   field=field, expected=binding, actual=actual_bindings.get(field))
                    self.counts["styleBindingsChecked"] += 1
                for field in set(actual_bindings) - set(expected_bindings[sid]):
                    self.issue("UNDECLARED_STYLE_BINDING", "Style has undeclared binding", styleLogicalId=sid, field=field)
        before_pages, before_nodes = self.census(args.before_glob, "before")
        after_pages, after_nodes = self.census(args.after_glob, "after")
        discovery_ids = {p["id"] for p in discovery["pages"]}
        if set(before_pages) != discovery_ids or len(before_pages) != EXPECTED["pages"]:
            self.issue("BEFORE_PAGE_COVERAGE", "Before census differs from 34-page discovery")
        if not after_pages:
            self.issue("AFTER_NOT_AVAILABLE", "After census has not been provided", "BLOCKED")
            return self.report()
        scale_readback = self.load(args.instance_scales)
        if scale_readback is not None:
            self.validate_instance_scales(scale_readback, mapping["nodes"])
        if set(after_pages) != set(before_pages):
            self.issue("PAGE_COVERAGE", "Before/after page sets differ", missing=sorted(set(before_pages) - set(after_pages)),
                       added=sorted(set(after_pages) - set(before_pages)))
        for pid in sorted(set(before_pages) & set(after_pages)):
            before, after = before_pages[pid], after_pages[pid]
            if before["page"] != after["page"]:
                self.issue("PAGE_CHANGED", "Page identity/name changed", pageId=pid)
            if sorted(before["components"], key=lambda x: x["id"]) != sorted(after["components"], key=lambda x: x["id"]):
                self.issue("COMPONENT_STRUCTURE", "Component IDs/names/types/parents changed", pageId=pid)
        assignments = {n["nodeId"]: n for n in mapping["nodes"]}
        if len(assignments) != len(mapping["nodes"]) or set(assignments) != set(before_nodes):
            self.issue("MAPPING_NODE_COVERAGE", "Mapping IDs differ from before census")
        if set(before_nodes) != set(after_nodes):
            self.issue("NODE_COVERAGE", "Before/after text IDs differ",
                       missing=sorted(set(before_nodes) - set(after_nodes)), added=sorted(set(after_nodes) - set(before_nodes)))
        for nid in sorted(set(before_nodes) & set(after_nodes) & set(assignments)):
            self.compare_node(before_nodes[nid], after_nodes[nid], assignments[nid], styles,
                              style_map, expected_bindings, style_readback)
        for key in ("uiNodes", "uiSegments", "documentationNodes", "documentationSegments", "scaledSegments"):
            if self.counts[key] != EXPECTED[key]:
                self.issue("SCOPE_COUNT", "Validated scope count differs from reviewed baseline",
                           field=key, expected=EXPECTED[key], actual=self.counts[key])
        return self.report()

    def validate_instance_scales(self, evidence, assignments):
        rows = evidence if isinstance(evidence, list) else evidence.get("nodes")
        if not isinstance(rows, list) or any(
                not isinstance(row, dict) or not isinstance(row.get("nodeId"), str)
                or not row["nodeId"] or not isinstance(row.get("instanceScale"), (int, float))
                or isinstance(row["instanceScale"], bool) or not 0 < row["instanceScale"] < float("inf")
                for row in rows):
            self.issue("INSTANCE_SCALE_SCHEMA", "Each observed scale needs a text node ID and a finite positive numeric scale")
            return {}
        observed = {row["nodeId"]: row for row in rows}
        expected = {n["nodeId"] for n in assignments
                    if any(s.get("instanceScale", 1) != 1 for s in n["segments"])}
        self.counts["instanceScaleNodesRead"] = len(observed)
        if len(observed) != len(rows) or set(observed) != expected:
            self.issue("INSTANCE_SCALE_COVERAGE", "Final instance-scale evidence differs from mapped scaled nodes",
                       expected=len(expected), actual=len(observed), duplicateRows=len(rows) - len(observed),
                       missing=sorted(expected - set(observed)), added=sorted(set(observed) - expected))
        for assignment in assignments:
            row = observed.get(assignment["nodeId"])
            for segment in assignment["segments"]:
                scale = segment.get("instanceScale", 1)
                if scale == 1 or row is None:
                    continue
                if row["instanceScale"] != scale:
                    self.issue("INSTANCE_SCALE_CHANGED", "Final effective instance scale changed",
                               nodeId=assignment["nodeId"], start=segment["start"], end=segment["end"],
                               expected=scale, actual=row["instanceScale"])
                else:
                    self.counts["instanceScalesChecked"] += 1
        return observed

    def allows_editorial_binding_additions(self, old, new, styles, style_map, bindings, readback):
        if not self.editorial_binding_rule:
            return False
        if not preserved_recipe_equal(old, new, ("boundVariables",)):
            return False
        original = old.get("boundVariables")
        current = new.get("boundVariables")
        if not isinstance(original, dict) or not isinstance(current, dict):
            return False
        if not set(original).issubset(current) or any(current[k] != v for k, v in original.items()):
            return False
        real_id = old.get("textStyleId")
        logical_ids = [sid for sid, rid in style_map.items() if rid == real_id]
        if not real_id or len(logical_ids) != 1:
            return False
        sid = logical_ids[0]
        record = readback.get(real_id)
        if sid not in styles or record is None or recipe_errors(new, styles[sid]) or recipe_errors(record, styles[sid]):
            return False
        additions = set(current) - set(original)
        canonical = bindings.get(sid, {})
        observed = record.get("boundVariables", {})
        return bool(additions) and all(
            field in canonical and current[field] == canonical[field] == observed.get(field)
            for field in additions)

    def validate_formatting_derivatives(self, styles):
        for style in styles.values():
            if style.get("textDecoration") not in {"NONE", "UNDERLINE"}:
                self.issue("CANONICAL_DECORATION", "Every v0.1.1 recipe must explicitly declare its decoration",
                           styleLogicalId=style["id"])
        derivatives = [s for s in styles.values() if s.get("derivedFormattingFrom")]
        if len(derivatives) != 4:
            self.issue("FORMATTING_DERIVATIVE_COUNT", "Exactly four preserved underline recipes are required")
        for style in derivatives:
            origin = style["derivedFormattingFrom"]
            base = styles.get(origin.get("baseStyleId"))
            if (base is None or origin.get("overrides") != {"textDecoration": "UNDERLINE"}
                    or style.get("textDecoration") != "UNDERLINE" or base.get("textDecoration") != "NONE"
                    or not origin.get("reason") or style.get("category") != "complementary"
                    or not style.get("compatibilityOnly")):
                self.issue("FORMATTING_DERIVATIVE_SCOPE", "Underline recipe lacks its original base, declaration or compatibility scope",
                           styleLogicalId=style["id"])
                continue
            for field in (*FIELDS, "fontWeight", "tokenRefs"):
                if style.get(field) != base.get(field):
                    self.issue("FORMATTING_DERIVATIVE_METRIC", "Underline recipe changes its base metrics or semantic bindings",
                               styleLogicalId=style["id"], field=field)
        self.counts["formattingDerivedStyles"] = len(derivatives)

    def validate_derivatives(self, styles):
        derivatives = [s for s in styles.values() if s.get("derivedFrom")]
        if len(derivatives) != 3:
            self.issue("DERIVED_CATALOG_COUNT", "Exactly three evidence-based scaled derivatives are required")
        for style in derivatives:
            origin = style["derivedFrom"]
            base = styles.get(origin.get("baseStyleId"))
            ratio = origin.get("scaleRatio", {})
            if (base is None or not ratio.get("denominator")
                    or origin.get("numericEncoding") != "FLOAT32_BASE_TIMES_FLOAT32_SCALE"):
                self.issue("DERIVATION_METADATA", "Derivative lacks its base, ratio or numeric encoding", styleLogicalId=style["id"])
                continue
            scale = f32(ratio["numerator"] / ratio["denominator"])
            if origin.get("scaleFactor") != scale:
                self.issue("DERIVATION_SCALE", "Derivative scale factor differs from encoded ratio", styleLogicalId=style["id"])
            if style["fontSize"] != f32(base["fontSize"] * scale):
                self.issue("DERIVATION_SIZE", "Derivative size differs from encoded base times scale", styleLogicalId=style["id"])
            for field in ("fontFamily", "fontStyle", "fontWeight"):
                if style[field] != base[field]:
                    self.issue("DERIVATION_FONT", "Derivative changes base font", styleLogicalId=style["id"], field=field)
            for field in ("lineHeight", "letterSpacing"):
                expected = copy.deepcopy(base[field])
                if expected["unit"] == "PIXELS":
                    expected["value"] = f32(expected["value"] * scale)
                if style[field] != expected:
                    self.issue("DERIVATION_METRIC", "Derivative metric differs from encoded base times scale", styleLogicalId=style["id"], field=field)
            if not style.get("compatibilityOnly") or style.get("category") != "complementary":
                self.issue("DERIVATION_SCOPE", "Scaled derivative is not restricted to compatibility", styleLogicalId=style["id"])
        self.counts["derivedStyles"] = len(derivatives)

    def compare_node(self, before, after, assigned, styles, style_map, bindings, readback):
        nid = before["nodeId"]
        location = {"nodeId": nid, "pageId": before["pageId"]}
        is_ui = bool(before["ownerComponentId"]) or nid.startswith("I")
        prefix = "ui" if is_ui else "documentation"
        self.counts[prefix + "Nodes"] += 1
        self.counts[prefix + "Segments"] += len(before["ranges"])
        self.counts[prefix + "AfterSegments"] += len(after["ranges"])
        if assigned["scope"] != ("UI" if is_ui else "DOCUMENTATION"):
            self.issue("MAPPING_SCOPE_CHANGED", "Mapping does not preserve derived UI/editorial scope", **location)
        for field in NODE_PRESERVE:
            if before[field] != after[field]:
                self.issue("NODE_PRESERVATION", "Text node property changed", **location,
                           field=field, before=before[field], after=after[field])
        old_bounds = sorted((a, b) for a, b, _ in before["ranges"])
        new_bounds = sorted((a, b) for a, b, _ in after["ranges"])
        if old_bounds != new_bounds:
            self.counts["nodesWithChangedSegmentation"] += 1
        if before["preservationHash"] != after["preservationHash"]:
            # The hash includes per-segment fills/hyperlinks as well as opaque
            # ancestry/alignment/props. Equal interval semantics cannot prove
            # the opaque fields when segmentation changes: require more evidence.
            status = "BLOCKED" if old_bounds != new_bounds else "FAIL"
            self.issue("PRESERVATION_HASH", "Opaque preservation fields are not proven unchanged",
                       status, **location, before=before["preservationHash"], after=after["preservationHash"],
                       segmentationChanged=old_bounds != new_bounds)
        else:
            self.counts["preservationHashesEqual"] += 1
        expected_ranges = []
        for segment in assigned["segments"]:
            expected_ranges.append((segment["start"], segment["end"], segment))
            if is_ui and segment.get("instanceScale", segment.get("expectedScale", 1)) != 1:
                self.counts["scaledSegments"] += 1
            if not is_ui:
                continue
            sid = segment.get("styleLogicalId")
            if str(segment.get("applicationStatus", "")).startswith("UNRESOLVED"):
                self.issue("ASSIGNMENT_APPLICATION_UNRESOLVED", "Logical recipe is mapped but its Figma application remains unresolved",
                           "BLOCKED", **location, start=segment["start"], end=segment["end"],
                           applicationStatus=segment["applicationStatus"])
            if segment.get("status") != "MAPPED" or sid not in styles:
                self.issue("ASSIGNMENT_NOT_MAPPED", "UI assignment has no canonical style", **location)
                continue
            recipe_scale = segment.get("recipeScale", segment.get("expectedScale", 1))
            instance_scale = segment.get("instanceScale", segment.get("expectedScale", 1))
            if segment.get("expectedScale", recipe_scale) != recipe_scale:
                self.issue("SCALE_ALIAS", "expectedScale must alias recipeScale, not instanceScale", **location)
            if instance_scale != 1:
                evidence = segment.get("scaleEvidence", {})
                derived = styles[sid].get("derivedFrom", {})
                if (instance_scale not in {f32(2 / 3), f32(5 / 6), f32(4 / 3)}
                        or evidence.get("factor") != instance_scale
                        or derived.get("scaleFactor") != instance_scale or recipe_scale != 1
                        or evidence.get("styleLogicalId") not in {sid, derived.get("baseStyleId")}
                        or nid.split(";")[-1] != evidence.get("principalTextNodeId")):
                    self.issue("SCALE_EVIDENCE", "Scaled assignment lacks its exact principal/factor evidence", **location)
        try:
            aligned = align_ranges(before["ranges"], after["ranges"], expected_ranges)
        except ValueError as error:
            self.issue("RANGE_COVERAGE", str(error), **location)
            return
        for start, end, old, new, segment in aligned:
            loc = {**location, "start": start, "end": end}
            self.counts["comparedIntervals"] += 1
            for phase, recipe in (("before", old), ("after", new)):
                overrides = recipe.get("textStyleOverrides")
                if not isinstance(overrides, list) or any(not isinstance(field, str) for field in overrides):
                    self.issue("RANGE_EVIDENCE", "Explicit textStyleOverrides array is required; missing evidence is not an empty override list",
                               **loc, phase=phase, field="textStyleOverrides")
            if not is_ui:
                if not preserved_recipe_equal(old, new):
                    if self.allows_editorial_binding_additions(old, new, styles, style_map, bindings, readback):
                        self.counts["editorialRangesWithCanonicalBindingAdditions"] += 1
                    else:
                        self.issue("EDITORIAL_RECIPE", "Historical editorial recipe changed beyond canonical additive bindings allowed by contract §5", **loc)
                continue
            sid = segment.get("styleLogicalId")
            if sid not in styles:
                continue
            style = styles[sid]
            scale = segment.get("recipeScale", segment.get("expectedScale", 1))
            for label, recipe in (("before", old), ("after", new)):
                # v0.1.0 kept decoration as a separate range property. v0.1.1
                # explicitly owns it in the catalogue, including the NONE cases.
                differences = recipe_errors(recipe, style, scale, check_decoration="textDecoration" in style)
                if differences:
                    self.issue("RESOLVED_METRICS", "Resolved typography differs from exact mapped recipe",
                               **loc, phase=label, styleLogicalId=sid, scale=scale, fields=differences)
            expected_id = style_map.get(sid)
            actual_id = new.get("textStyleId")
            if not actual_id:
                self.counts["uiIntervalsWithoutStyle"] += 1
            if actual_id not in set(style_map.values()):
                self.counts["uiIntervalsWithForeignStyle"] += 1
            if actual_id != expected_id:
                self.issue("CONSUMER_STYLE_ID", "UI range does not consume its mapped real TextStyle ID",
                           **loc, styleLogicalId=sid, expected=expected_id, actual=actual_id)
            overrides = new.get("textStyleOverrides")
            shared_fields = METRIC_FIELDS | ({"textDecoration"} if "textDecoration" in style else set())
            metric_overrides = {field for field in overrides if isinstance(field, str)} & shared_fields if isinstance(overrides, list) else set()
            if metric_overrides:
                self.issue("METRIC_OVERRIDE", "UI range overrides shared typographic fields", **loc,
                           fields=sorted(metric_overrides), scale=scale)
            for field in FORMATTING:
                if old.get(field) != new.get(field):
                    self.issue("RANGE_FORMATTING", "Non-typographic range property changed", **loc, field=field,
                               before=old.get(field), after=new.get(field))
            style_bindings = readback.get(expected_id, {}).get("boundVariables", {})
            effective = {**style_bindings, **new.get("boundVariables", {})}
            for field in (set(effective) & METRIC_FIELDS) - set(old.get("boundVariables", {})) - set(bindings[sid]):
                self.issue("UNDECLARED_CONSUMER_BINDING", "New metric binding is neither original nor declared by the canonical style",
                           **loc, field=field, actual=effective[field])
            # Existing semantic identity must survive either on range or style.
            for field, old_binding in old.get("boundVariables", {}).items():
                if effective.get(field) != old_binding:
                    self.issue("LOST_SEMANTIC_BINDING", "Original binding not retained by range/style",
                               **loc, field=field, expected=old_binding, actual=effective.get(field),
                               status="BLOCKED" if expected_id not in readback else "FAIL")
            for field, binding in bindings[sid].items():
                if effective.get(field) != binding:
                    self.issue("CONSUMER_BINDING", "Effective range/style binding differs from canonical style",
                               **loc, field=field, expected=binding, actual=effective.get(field),
                               status="BLOCKED" if expected_id not in readback else "FAIL")
            self.counts["uiIntervalsChecked"] += 1

    def report(self):
        for key in ("uiIntervalsWithoutStyle", "uiIntervalsWithForeignStyle", "nodesWithChangedSegmentation"):
            self.counts.setdefault(key, 0)
        failures = sum(f["status"] == "FAIL" for f in self.findings)
        blocked = sum(f["status"] == "BLOCKED" for f in self.findings)
        status = "FAIL" if failures else "BLOCKED" if blocked else "PASS"
        files = dict(sorted(self.sources.items()))
        digest = hashlib.sha256(json.dumps(files, sort_keys=True, ensure_ascii=False,
                                          separators=(",", ":")).encode("utf-8")).hexdigest()
        findings = sorted(self.findings, key=lambda f: json.dumps(f, sort_keys=True, ensure_ascii=False))
        report = {"schema_version": 1, "id": "QA-TYPOGRAPHY-MIGRATION-001", "version": self.version,
                "result": status, "execution": "LOCAL_SAVED_EVIDENCE_REVIEW",
                "figmaWrites": "NOT_RUN", "userAudit": "PENDING",
                "scope": "Canonical styles and complete baseline text/range migration; no visual screenshot claim",
                "expected": self.expected, "counts": dict(sorted(self.counts.items())),
                "failureCount": failures, "blockedCount": blocked, "findings": findings,
                "sources": files, "sourcesDigest": digest,
                "limits": ["Census charactersHash/preservationHash are captured noncryptographic fingerprints, not raw values.",
                           "Same preservationHash is evidence of captured properties; it is not a collision-proof identity proof.",
                           "Audit captures text width/height, not every frame position or a rendered clipping review.",
                           "Page/component structure is compared; separate visual QA remains required.",
                           "Editorial scope is the 150 baseline nodes; new documentation is outside this baseline."]}
        if self.mode == "restoration":
            report.update({"id": "QA-TYPOGRAPHY-RESTORATION-001", "mode": "restoration",
                           "migrationValidation": "BLOCKED",
                           "scope": "Restore original baseline text/range metrics, content, opaque preservation properties, bounds, IDs and bindings on 34 pages; does not validate consumption of the new catalogue.",
                           "expected": {k: EXPECTED[k] for k in ("pages", "nodes", "uiNodes", "uiSegments", "documentationNodes", "documentationSegments")},
                           "policy": {"styleIds": "Require original ID, including original empty ID; style renaming with the same ID does not change the census recipe.",
                                      "bindings": "Require original range binding identities; no new catalogue map or inheritance substitute.",
                                      "normalizations": "Only exact numeric equality, documented float32 encoding and exact zero tracking PIXELS/PERCENT equivalence; no epsilon.",
                                      "separateOutput": "This report must not replace the blocked migration QA."}})
            # Empty style IDs were valid in the original baseline and are not
            # restoration defects. Do not publish migration-oriented counters.
            for key in ("uiIntervalsWithoutStyle", "uiIntervalsWithForeignStyle"):
                report["counts"].pop(key, None)
        return report


class RegressionTests(unittest.TestCase):
    def test_historical_style_map_covers_75_catalogue_ids(self):
        root = Path(__file__).resolve().parents[2]
        catalog = json.loads((root / CATALOG).read_text(encoding="utf-8"))
        state = json.loads((root / STYLES_STATE).read_text(encoding="utf-8"))
        expected = {style["id"] for style in catalog["styles"]}
        self.assertEqual(len(expected), 75)
        self.assertEqual(set(state["styleMap"]), expected)
        self.assertEqual(len(set(state["styleMap"].values())), 75)
        self.assertTrue(all(state["styleMap"].values()))

    def test_cli_defaults_select_one_current_version_without_changing_historical_exports(self):
        args = argument_parser().parse_args([])
        for path in (args.catalog, args.mapping, args.styles_state, args.styles_readback, args.instance_scales):
            self.assertIn(f"v{CURRENT_VERSION}.", path)
        self.assertEqual(args.styles_state, CURRENT_STYLES_STATE)
        self.assertIn(".catalog.state.json", args.styles_state)
        self.assertIn("v0.1.0.", CATALOG)
        self.assertIn("v0.1.0.", STYLES_READBACK)

    def test_historical_census_never_includes_new_versioned_capture(self):
        with tempfile.TemporaryDirectory(prefix="typography-checker-test-") as directory:
            root = Path(directory)
            snapshot = root / "sources/figma-snapshots/typography"
            snapshot.mkdir(parents=True)
            data = {"schema_version": 2, "page": {"id": "page-1", "name": "Original"},
                    "columns": ["idParts", "nameIndex", "effectiveVisible", "width", "height", "segments",
                                "preservationHash", "ownerComponentId", "textAutoResize", "charactersHash"],
                    "components": [], "nodes": [], "paths": [], "names": [], "recipes": []}
            (snapshot / "census.after.1-1.json").write_text(json.dumps(data), encoding="utf-8")
            data["page"]["name"] = "Final capture"
            (snapshot / "census.after.v0.1.1.1-1.json").write_text(json.dumps(data), encoding="utf-8")
            historical = Review(root)
            pages, _ = historical.census(AFTER_GLOB, "after")
            self.assertEqual(historical.findings, [])
            self.assertEqual(pages["page-1"]["page"]["name"], "Original")
            final = Review(root)
            pages, _ = final.census(CURRENT_AFTER_GLOB, "after")
            self.assertEqual(final.findings, [])
            self.assertEqual(pages["page-1"]["page"]["name"], "Final capture")

    def fixture(self, editorial=False):
        style = {"fontFamily": "Manrope", "fontStyle": "Regular", "fontWeight": 400,
                 "fontSize": 14, "lineHeight": {"unit": "PIXELS", "value": 20},
                 "letterSpacing": {"unit": "PIXELS", "value": 0}}
        binding = {"type": "VARIABLE_ALIAS", "id": "semantic-font-family"}
        recipe = {"fontName": {"family": "Manrope", "style": "Regular"}, "fontWeight": 400,
                  "fontSize": 14, "lineHeight": style["lineHeight"], "letterSpacing": style["letterSpacing"],
                  "textStyleId": "style-real", "boundVariables": {"fontFamily": binding},
                  "textStyleOverrides": [], "fills": [], "hyperlink": None, "textDecoration": "NONE"}
        before = {"nodeId": "text-1", "pageId": "page-1", "name": "Label", "ownerComponentId": "" if editorial else "component-1",
                  "effectiveVisible": 1, "width": 80, "height": 20, "charactersHash": "characters",
                  "textAutoResize": "WIDTH_AND_HEIGHT", "preservationHash": "preserved",
                  "ranges": [(0, 4, recipe)]}
        assignment = {"scope": "DOCUMENTATION" if editorial else "UI", "segments": [
            {"start": 0, "end": 4, "styleLogicalId": "body", "status": "MAPPED", "expectedScale": 1}]}
        return before, assignment, {"body": style}, {"body": "style-real"}, {"body": {"fontFamily": binding}}, {
            "style-real": {"boundVariables": {"fontFamily": binding}}}

    def compare_fixture(self, mutate, editorial=False):
        before, assigned, styles, ids, bindings, readback = self.fixture(editorial)
        after = copy.deepcopy(before)
        mutate(after)
        review = Review(Path.cwd())
        review.compare_node(before, after, assigned, styles, ids, bindings, readback)
        return review

    def test_inherited_binding_valid_but_wrong_id_or_lost_alias_fails(self):
        review = self.compare_fixture(lambda n: n["ranges"][0][2].update(boundVariables={}))
        self.assertEqual(review.findings, [])
        review = self.compare_fixture(lambda n: n["ranges"][0][2].update(textStyleId="foreign-style"))
        self.assertIn("CONSUMER_STYLE_ID", {f["code"] for f in review.findings})
        review = self.compare_fixture(lambda n: n["ranges"][0][2].update(
            boundVariables={"fontFamily": {"type": "VARIABLE_ALIAS", "id": "equal-value-but-wrong-identity"}}))
        self.assertIn("LOST_SEMANTIC_BINDING", {f["code"] for f in review.findings})

    def test_geometry_editorial_and_metric_override_fail(self):
        review = self.compare_fixture(lambda n: n.update(width=81))
        self.assertIn("NODE_PRESERVATION", {f["code"] for f in review.findings})
        review = self.compare_fixture(lambda n: n["ranges"][0][2].update(textStyleId="new-style"), editorial=True)
        self.assertIn("EDITORIAL_RECIPE", {f["code"] for f in review.findings})
        review = self.compare_fixture(lambda n: n["ranges"][0][2].update(textStyleOverrides=["fontSize"]))
        self.assertIn("METRIC_OVERRIDE", {f["code"] for f in review.findings})

    def test_override_evidence_cannot_be_missing_null_or_malformed(self):
        for invalid in (None, "", {}, ["fontSize", None]):
            with self.subTest(overrides=invalid):
                review = self.compare_fixture(lambda n: n["ranges"][0][2].update(textStyleOverrides=invalid))
                self.assertIn("RANGE_EVIDENCE", {f["code"] for f in review.findings})
        review = self.compare_fixture(lambda n: n["ranges"][0][2].pop("textStyleOverrides"))
        self.assertIn("RANGE_EVIDENCE", {f["code"] for f in review.findings})
        before, assigned, styles, ids, bindings, readback = self.fixture()
        after = copy.deepcopy(before)
        before["ranges"][0][2].pop("textStyleOverrides")
        review = Review(Path.cwd())
        review.compare_node(before, after, assigned, styles, ids, bindings, readback)
        self.assertEqual([(f["code"], f["phase"]) for f in review.findings], [("RANGE_EVIDENCE", "before")])

    def test_new_metric_binding_rejected_but_original_binding_preserved(self):
        alias = {"type": "VARIABLE_ALIAS", "id": "undeclared-metric-alias"}
        review = self.compare_fixture(lambda n: n["ranges"][0][2]["boundVariables"].update(lineHeight=alias))
        self.assertIn("UNDECLARED_CONSUMER_BINDING", {f["code"] for f in review.findings})
        before, assigned, styles, ids, bindings, readback = self.fixture()
        readback["style-real"]["boundVariables"]["lineHeight"] = alias
        review = Review(Path.cwd())
        review.compare_node(before, copy.deepcopy(before), assigned, styles, ids, bindings, readback)
        self.assertIn("UNDECLARED_CONSUMER_BINDING", {f["code"] for f in review.findings})
        before["ranges"][0][2]["boundVariables"]["lineHeight"] = alias
        review = Review(Path.cwd())
        review.compare_node(before, copy.deepcopy(before), assigned, styles, ids, bindings, readback)
        self.assertEqual(review.findings, [])

    def test_unresolved_application_cannot_pass_even_with_matching_fixture_values(self):
        before, assigned, styles, ids, bindings, readback = self.fixture()
        assigned["segments"][0]["applicationStatus"] = "UNRESOLVED_SCALED_LINK"
        review = Review(Path.cwd())
        review.compare_node(before, copy.deepcopy(before), assigned, styles, ids, bindings, readback)
        self.assertEqual([(f["code"], f["status"]) for f in review.findings],
                         [("ASSIGNMENT_APPLICATION_UNRESOLVED", "BLOCKED")])

    def test_editorial_exception_requires_same_recipe_and_proven_additive_binding(self):
        before, assigned, styles, ids, bindings, _ = self.fixture(editorial=True)
        after = copy.deepcopy(before)
        readback = {"style-real": copy.deepcopy(after["ranges"][0][2])}
        before["ranges"][0][2]["boundVariables"] = {}
        review = Review(Path.cwd())
        review.editorial_binding_rule = True
        review.compare_node(before, after, assigned, styles, ids, bindings, readback)
        self.assertEqual(review.findings, [])
        self.assertEqual(review.counts["editorialRangesWithCanonicalBindingAdditions"], 1)
        for change in (
            lambda recipe: recipe.update(textStyleId="foreign"),
            lambda recipe: recipe.update(fontSize=15),
            lambda recipe: recipe.update(textDecoration="UNDERLINE"),
            lambda recipe: recipe["boundVariables"].update(fontFamily={"type": "VARIABLE_ALIAS", "id": "wrong-alias"}),
            lambda recipe: recipe["boundVariables"].update(lineHeight={"type": "VARIABLE_ALIAS", "id": "undeclared-alias"}),
        ):
            changed = copy.deepcopy(after)
            change(changed["ranges"][0][2])
            review = Review(Path.cwd())
            review.editorial_binding_rule = True
            review.compare_node(before, changed, assigned, styles, ids, bindings, readback)
            self.assertIn("EDITORIAL_RECIPE", {f["code"] for f in review.findings})
        for enabled, records in ((False, readback), (True, {})):
            review = Review(Path.cwd())
            review.editorial_binding_rule = enabled
            review.compare_node(before, after, assigned, styles, ids, bindings, records)
            self.assertIn("EDITORIAL_RECIPE", {f["code"] for f in review.findings})
        # Removing an original alias is not an additive foundation update.
        review = Review(Path.cwd())
        review.editorial_binding_rule = True
        review.compare_node(after, before, assigned, styles, ids, bindings, readback)
        self.assertIn("EDITORIAL_RECIPE", {f["code"] for f in review.findings})

    def test_instance_scale_evidence_requires_all_103_exact_observations(self):
        scale = f32(2 / 3)
        assignments = [{"nodeId": f"text-{i}", "segments": [
            {"start": 0, "end": 1, "instanceScale": scale}]} for i in range(103)]
        rows = [{"nodeId": a["nodeId"], "instanceScale": scale} for a in assignments]
        review = Review(Path.cwd())
        review.validate_instance_scales({"nodes": rows}, assignments)
        self.assertEqual(review.findings, [])
        self.assertEqual(review.counts["instanceScalesChecked"], 103)
        for invalid in (rows[:-1], rows + [rows[0]], rows + [{"nodeId": "foreign", "instanceScale": scale}]):
            review = Review(Path.cwd())
            review.validate_instance_scales(invalid, assignments)
            self.assertIn("INSTANCE_SCALE_COVERAGE", {f["code"] for f in review.findings})
        changed = copy.deepcopy(rows)
        changed[0]["instanceScale"] = scale + 0.000001
        review = Review(Path.cwd())
        review.validate_instance_scales(changed, assignments)
        self.assertEqual([f["code"] for f in review.findings], ["INSTANCE_SCALE_CHANGED"])
        self.assertEqual(review.counts["instanceScalesChecked"], 102)
        for value in (None, True, "0.6666667", 0, float("inf"), float("nan")):
            changed[0]["instanceScale"] = value
            review = Review(Path.cwd())
            review.validate_instance_scales(changed, assignments)
            self.assertEqual([f["code"] for f in review.findings], ["INSTANCE_SCALE_SCHEMA"])

    def test_changed_segmentation_does_not_hide_opaque_hash_change(self):
        def split(node):
            recipe = node["ranges"][0][2]
            node["ranges"] = [(2, 4, recipe), (0, 2, recipe)]
            node["preservationHash"] = "different-segment-sensitive-hash"
        review = self.compare_fixture(split)
        self.assertEqual([(f["code"], f["status"]) for f in review.findings], [("PRESERVATION_HASH", "BLOCKED")])

    def test_merge_split_and_reorder(self):
        before = [(0, 3, "a"), (3, 8, "b")]
        after = [(5, 8, "z"), (0, 5, "y")]
        mapped = [(0, 8, "style")]
        self.assertEqual(align_ranges(before, after, mapped), [
            (0, 3, "a", "y", "style"), (3, 5, "b", "y", "style"),
            (5, 8, "b", "z", "style")])

    def test_missing_and_overlapping_ranges_rejected(self):
        for bad in [[(0, 2, None), (3, 5, None)], [(0, 4, None), (3, 5, None)]]:
            with self.assertRaises(ValueError):
                align_ranges(bad, [(0, 5, None)], [(0, 5, None)])
        with self.assertRaises(ValueError):
            align_ranges([(0, 4, None)], [(0, 5, None)], [(0, 4, None)])

    def test_float32_not_epsilon(self):
        self.assertTrue(numeric_equal(f32(1.33) * 100, 133, True))
        self.assertFalse(numeric_equal(133.000001, 133, True))
        self.assertTrue(metric_equal({"unit": "PIXELS", "value": 0}, {"unit": "PERCENT", "value": 0}))
        self.assertFalse(metric_equal({"unit": "PIXELS", "value": -2}, {"unit": "PERCENT", "value": -2}))

    def test_scaled_recipe_and_wrong_weight(self):
        style = {"fontFamily": "Manrope", "fontStyle": "Regular", "fontWeight": 400,
                 "fontSize": 14, "lineHeight": {"unit": "PIXELS", "value": 20},
                 "letterSpacing": {"unit": "PIXELS", "value": 0}}
        scale = f32(5 / 6)
        recipe = {"fontName": {"family": "Manrope", "style": "Regular"}, "fontWeight": 400,
                  "fontSize": f32(14 * scale), "lineHeight": {"unit": "PIXELS", "value": f32(20 * scale)},
                  "letterSpacing": {"unit": "PIXELS", "value": 0}, "textDecoration": "NONE"}
        self.assertEqual(recipe_errors(recipe, style, scale), [])
        self.assertIn("fontSize", recipe_errors(recipe, style))
        changed = copy.deepcopy(recipe)
        changed["fontWeight"] = 600
        self.assertIn("fontWeight", recipe_errors(changed, style, scale))

    def test_canonical_decoration_and_equivalent_manrope_weight_axis(self):
        before, _, styles, *_ = self.fixture()
        recipe = copy.deepcopy(before["ranges"][0][2])
        style = styles["body"]
        self.assertEqual(recipe_errors(recipe, style), [])
        recipe["fontName"]["variationSettings"] = {"wght": 400}
        self.assertEqual(recipe_errors(recipe, style), [])
        self.assertTrue(preserved_recipe_equal(before["ranges"][0][2], recipe))
        for axes in ({"wght": 500}, {"wght": 400, "wdth": 100}):
            recipe["fontName"]["variationSettings"] = axes
            self.assertIn("variationSettings", recipe_errors(recipe, style))
            self.assertFalse(preserved_recipe_equal(before["ranges"][0][2], recipe))
        recipe["fontName"] = {"family": "Another font", "style": "Regular", "variationSettings": {"wght": 400}}
        self.assertIn("fontFamily", recipe_errors(recipe, style))
        self.assertFalse(preserved_recipe_equal(before["ranges"][0][2], recipe))
        recipe = copy.deepcopy(before["ranges"][0][2])
        recipe["textDecoration"] = "UNDERLINE"
        self.assertIn("textDecoration", recipe_errors(recipe, style))
        style["textDecoration"] = "UNDERLINE"
        self.assertEqual(recipe_errors(recipe, style), [])
        recipe.pop("textDecoration")
        self.assertIn("textDecoration", recipe_errors(recipe, style))

    def test_underline_derivatives_change_no_metrics_or_bindings(self):
        _, _, base_styles, *_ = self.fixture()
        base = {**base_styles["body"], "id": "base", "textDecoration": "NONE", "tokenRefs": {"fontFamily": "font/family/base"}}
        styles = {"base": base}
        for i in range(4):
            style = copy.deepcopy(base)
            style.update(id=f"underline-{i}", textDecoration="UNDERLINE", category="complementary", compatibilityOnly=True,
                         derivedFormattingFrom={"baseStyleId": "base", "overrides": {"textDecoration": "UNDERLINE"},
                                                "reason": "Preserve observed underline in this test fixture"})
            styles[style["id"]] = style
        review = Review(Path.cwd())
        review.validate_formatting_derivatives(styles)
        self.assertEqual(review.findings, [])
        styles["underline-0"]["fontSize"] = 15
        review.validate_formatting_derivatives(styles)
        self.assertIn("FORMATTING_DERIVATIVE_METRIC", {f["code"] for f in review.findings})

    def test_materialized_derivatives_are_not_scaled_twice(self):
        base = {"id": "base", "fontFamily": "Manrope", "fontStyle": "Regular", "fontWeight": 400,
                "fontSize": 14, "lineHeight": {"unit": "PIXELS", "value": 20},
                "letterSpacing": {"unit": "PERCENT", "value": -2}}
        styles = {"base": base}
        for numerator, denominator in ((2, 3), (5, 6), (4, 3)):
            style = copy.deepcopy(base)
            scale = f32(numerator / denominator)
            style.update(id=f"derived-{numerator}-{denominator}", category="complementary", compatibilityOnly=True,
                         fontSize=f32(base["fontSize"] * scale),
                         lineHeight={"unit": "PIXELS", "value": f32(20 * scale)},
                         derivedFrom={"baseStyleId": "base", "scaleFactor": scale,
                                      "scaleRatio": {"numerator": numerator, "denominator": denominator},
                                      "numericEncoding": "FLOAT32_BASE_TIMES_FLOAT32_SCALE"})
            styles[style["id"]] = style
        review = Review(Path.cwd())
        review.validate_derivatives(styles)
        self.assertEqual(review.findings, [])
        styles["derived-2-3"]["fontSize"] = f32(styles["derived-2-3"]["fontSize"] * f32(2 / 3))
        review.validate_derivatives(styles)
        self.assertIn("DERIVATION_SIZE", {f["code"] for f in review.findings})

    def test_restoration_accepts_original_empty_style_without_new_catalogue(self):
        before, *_ = self.fixture()
        before["ranges"][0][2]["textStyleId"] = ""
        after = copy.deepcopy(before)
        review = Review(Path.cwd())
        review.mode = "restoration"
        review.compare_restored_node(before, after)
        self.assertEqual(review.findings, [])
        self.assertEqual(review.counts["originalStyleIdsRestored"], 1)
        self.assertEqual(review.report()["migrationValidation"], "BLOCKED")

    def test_restoration_rejects_new_id_alias_and_geometry(self):
        before, *_ = self.fixture()
        after = copy.deepcopy(before)
        after["ranges"][0][2]["textStyleId"] = "new-catalogue-style"
        after["ranges"][0][2]["boundVariables"] = {}
        after["width"] = 81
        review = Review(Path.cwd())
        review.compare_restored_node(before, after)
        self.assertEqual({f.get("field") for f in review.findings}, {"textStyleId", "boundVariables", "width"})

    def test_restoration_aligns_split_ranges_but_requires_opaque_preservation(self):
        before, *_ = self.fixture()
        after = copy.deepcopy(before)
        recipe = after["ranges"][0][2]
        after["ranges"] = [(2, 4, recipe), (0, 2, recipe)]
        review = Review(Path.cwd())
        review.compare_restored_node(before, after)
        self.assertEqual(review.findings, [])
        after["preservationHash"] = "opaque-difference"
        review.compare_restored_node(before, after)
        self.assertEqual([(f["code"], f["status"]) for f in review.findings], [("RESTORATION_PRESERVATION_HASH", "BLOCKED")])


def argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--catalog", default=CURRENT_CATALOG)
    parser.add_argument("--mapping", default=CURRENT_MAPPING)
    parser.add_argument("--styles-state", default=CURRENT_STYLES_STATE)
    parser.add_argument("--styles-readback", default=CURRENT_STYLES_READBACK)
    parser.add_argument("--instance-scales", "--instance-scale", default=CURRENT_INSTANCE_SCALES)
    parser.add_argument("--before-glob", default=BEFORE_GLOB)
    parser.add_argument("--after-glob", help="Default: current version's final capture; historical restored capture with --restoration")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--restoration", action="store_true", help="Compare with original census; write a separate restoration report, never the migration result")
    return parser


def main():
    parser = argument_parser()
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(RegressionTests))
        return 0 if result.wasSuccessful() else 1
    args.after_glob = args.after_glob or (AFTER_GLOB if args.restoration else CURRENT_AFTER_GLOB)
    review = Review(args.repo_root)
    try:
        result = review.run_restoration(args) if args.restoration else review.run(args)
    except (KeyError, TypeError, ValueError, IndexError, OSError) as error:
        review.issue("INVALID_EVIDENCE", str(error))
        result = review.report()
    output = args.output or args.repo_root / (RESTORATION_OUTPUT if args.restoration else CURRENT_OUTPUT)
    if args.restoration and output.resolve() in {(args.repo_root / OUTPUT).resolve(), (args.repo_root / CURRENT_OUTPUT).resolve()}:
        parser.error("Restoration output must not overwrite the migration QA report")
    serialized = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if not output.exists() or output.read_text(encoding="utf-8") != serialized:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(serialized, encoding="utf-8")
    print(json.dumps({"output": str(output), "result": result["result"], "counts": result["counts"],
                      "failureCount": result["failureCount"], "blockedCount": result["blockedCount"]}, ensure_ascii=False))
    return 0 if result["result"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
