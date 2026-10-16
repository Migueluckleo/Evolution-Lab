#!/usr/bin/env python3
"""Verify the retained archive; optionally restore to a disposable directory.

Never deletes project files, edits the Git index, or restores over the workspace.
"""
import argparse
import hashlib
import json
import subprocess
import tarfile
import tempfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "qa/tooling/retention.2026-10-13.manifest.json"


def digest(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def safe_path(name):
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or path.as_posix() != name:
        raise ValueError("Unsafe or noncanonical archive path: " + name)
    if not name.startswith("graphify-out/"):
        raise ValueError("Outside the authorized derivative scope: " + name)
    return path


def verify(working=False, restore_test=False, index_removed=False):
    manifest = json.loads(MANIFEST.read_text())
    records = manifest["files"]
    expected = {item["path"]: item for item in records}
    if len(expected) != len(records):
        raise ValueError("Repeated manifest path")
    archive_info = manifest["archive"]
    archive = ROOT / safe_path(archive_info["path"])
    if archive.stat().st_size != archive_info["bytes"] or digest(archive) != archive_info["sha256"]:
        raise ValueError("Recovery archive digest/size mismatch")
    seen = set()
    with tempfile.TemporaryDirectory(prefix="ds-retention-verify-") as directory:
        with tarfile.open(archive, "r:gz") as stream:
            for member in stream:
                path = safe_path(member.name)
                if not member.isfile() or member.name not in expected or member.name in seen:
                    raise ValueError("Unexpected, unsafe or repeated member: " + member.name)
                item = expected[member.name]
                with stream.extractfile(member) as source:
                    data = source.read()
                if member.size != item["bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"]:
                    raise ValueError("Member digest/size mismatch: " + member.name)
                if restore_test:
                    restored = Path(directory) / path
                    restored.parent.mkdir(parents=True, exist_ok=True)
                    restored.write_bytes(data)
                    if digest(restored) != item["sha256"]:
                        raise ValueError("Restore readback mismatch: " + member.name)
                if working:
                    local = ROOT / path
                    if local.is_symlink() or not local.is_file() or digest(local) != item["sha256"]:
                        raise ValueError("Local bytes changed since snapshot: " + member.name)
                seen.add(member.name)
    if seen != set(expected):
        raise ValueError("Archive coverage mismatch")
    if index_removed:
        tracked = set(subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0"))
        if tracked & seen:
            raise ValueError("Selected derivatives remain in the Git index")
    return {"status": "PASS", "archive_files": len(seen),
            "archive_sha256": archive_info["sha256"], "restore_readback": restore_test,
            "local_bytes_match_snapshot": working, "index_removed": index_removed}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--working", action="store_true", help="Compare local files to the initial snapshot; cache regeneration can change them.")
    parser.add_argument("--restore-test", action="store_true", help="Restore and read back in a temporary directory, then remove only that directory.")
    parser.add_argument("--index-removed", action="store_true", help="Check that selected paths are absent from the current Git index.")
    args = parser.parse_args()
    try:
        print(json.dumps(verify(args.working, args.restore_test, args.index_removed), indent=2))
    except (OSError, ValueError, tarfile.TarError, subprocess.CalledProcessError) as error:
        parser.exit(1, "FAIL: " + str(error) + "\n")
