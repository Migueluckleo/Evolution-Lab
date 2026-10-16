#!/usr/bin/env python3
"""Join complete v0.1.1 audit responses locally; reject mixed or missing captures.

Input files are the direct JSON objects returned by typography.v0.1.1.audit.js.
The transport fingerprint is noncryptographic. Output manifests contain SHA256
of exact input bytes and of the assembled census. No Figma calls or mutations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import unittest


def base36(number):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = ""
    while number:
        number, remainder = divmod(number, 36)
        result = digits[remainder] + result
    return result or "0"


def fingerprint(text):
    a, b = 2166136261, 5381
    for character in text:
        point = ord(character)
        value = point if point <= 0xffff else 0xd800 + ((point - 0x10000) >> 10)
        a = ((a ^ value) * 16777619) & 0xffffffff
        b = ((b * 33) ^ value) & 0xffffffff
    return base36(a) + "." + base36(b)


def assemble(records):
    if not records:
        raise ValueError("No capture parts")
    reference = records[0]
    metadata = ("captureVersion", "page", "nodes", "recipes", "parts", "payloadLength", "payloadFingerprint", "structureIncluded")
    if reference.get("captureVersion") != "0.1.1" or any(field not in reference for field in metadata):
        raise ValueError("Expected complete v0.1.1 transport metadata")
    count = reference["parts"]
    if type(count) is not int or count < 1:
        raise ValueError("Invalid part count")
    by_index = {}
    for record in records:
        if any(record.get(field) != reference[field] for field in metadata):
            raise ValueError("Capture metadata or fingerprint differs between parts")
        index = record.get("part")
        if type(index) is not int or not 0 <= index < count or index in by_index:
            raise ValueError("Invalid or duplicate part index")
        if not isinstance(record.get("payload"), str):
            raise ValueError("Capture payload is not a string")
        by_index[index] = record["payload"]
    if set(by_index) != set(range(count)):
        raise ValueError("Capture has missing parts")
    joined = "".join(by_index[i] for i in range(count))
    # JavaScript slices UTF16 strings, potentially splitting a surrogate pair.
    payload = joined.encode("utf-16-le", "surrogatepass").decode("utf-16-le")
    if len(payload.encode("utf-16-le")) // 2 != reference["payloadLength"] or fingerprint(payload) != reference["payloadFingerprint"]:
        raise ValueError("Assembled payload does not match capture length/fingerprint")
    census = json.loads(payload)
    if (census.get("schema_version") != 2 or census.get("page") != reference["page"]
            or len(census.get("nodes", [])) != reference["nodes"] or len(census.get("recipes", [])) != reference["recipes"]
            or ("structuralEvidence" in census) != reference["structureIncluded"]):
        raise ValueError("Assembled census does not match transport metadata")
    return payload, census


class RegressionTests(unittest.TestCase):
    def fixture(self):
        payload = json.dumps({"schema_version": 2, "page": {"id": "p", "name": "Texto🧾"},
                              "nodes": [], "recipes": []}, ensure_ascii=False, separators=(",", ":"))
        pieces = [payload[:30], payload[30:]]
        metadata = {"captureVersion": "0.1.1", "page": {"id": "p", "name": "Texto🧾"}, "nodes": 0,
                    "recipes": 0, "parts": 2, "payloadLength": len(payload.encode("utf-16-le")) // 2,
                    "payloadFingerprint": fingerprint(payload), "structureIncluded": False}
        return payload, [{**metadata, "part": index, "payload": piece} for index, piece in enumerate(pieces)]

    def test_complete_reordered_parts(self):
        payload, records = self.fixture()
        self.assertEqual(assemble(list(reversed(records)))[0], payload)

    def test_javascript_unicode_fingerprint_and_split_surrogate_pair(self):
        self.assertEqual(fingerprint('A🧾é\n"\\'), "1kne8vv.13sd6jr")
        payload, records = self.fixture()
        raw = payload.encode("utf-16-le")
        split = raw.index("🧾".encode("utf-16-le")) + 2
        records[0]["payload"] = raw[:split].decode("utf-16-le", "surrogatepass")
        records[1]["payload"] = raw[split:].decode("utf-16-le", "surrogatepass")
        self.assertEqual(assemble(records)[0], payload)

    def test_missing_duplicate_mixed_or_modified_parts_fail(self):
        _, records = self.fixture()
        for bad in (records[:1], records + records[:1],
                    [records[0], {**records[1], "payloadFingerprint": "changed"}],
                    [records[0], {**records[1], "payload": records[1]["payload"] + " "}]):
            with self.assertRaises(ValueError):
                assemble(bad)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("parts", nargs="*", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(RegressionTests))
        return 0 if result.wasSuccessful() else 1
    if not args.parts or args.output is None:
        parser.error("Provide capture part JSON files and --output")
    if not args.output.name.startswith("census.after.v0.1.1.") or args.output.suffix != ".json":
        parser.error("Output must be a new census.after.v0.1.1.<page>.json file")
    sources = {str(path.resolve()): hashlib.sha256(path.read_bytes()).hexdigest() for path in args.parts}
    try:
        payload, census = assemble([json.loads(path.read_text(encoding="utf-8")) for path in args.parts])
    except (ValueError, KeyError, TypeError, UnicodeError) as error:
        parser.error(str(error))
    # Preserve exact assembled JSON bytes; no reformatting or fabricated fields.
    data = payload.encode("utf-8")
    if args.output.exists() and args.output.read_bytes() != data:
        parser.error("Capture output already exists with different bytes; choose an explicit new capture path")
    manifest = {"schema_version": 1, "page": census["page"], "sources": sources,
                "output": str(args.output.resolve()), "sha256": hashlib.sha256(data).hexdigest(),
                "transportFingerprint": "Verified noncryptographic fingerprint; not an authenticity proof"}
    if args.manifest:
        manifest_data = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        if args.manifest.resolve() in {args.output.resolve(), *(path.resolve() for path in args.parts)}:
            parser.error("Manifest cannot overwrite a capture input or output")
        if args.manifest.exists() and args.manifest.read_bytes() != manifest_data:
            parser.error("Manifest already exists with different bytes")
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_bytes(manifest_data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(data)
    print(json.dumps({"output": str(args.output), "page": census["page"], "nodes": len(census["nodes"]),
                      "parts": len(args.parts), "sha256": manifest["sha256"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
