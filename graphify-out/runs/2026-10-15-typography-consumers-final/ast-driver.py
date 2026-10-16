#!/usr/bin/env python3
"""Prepare AST after `scripts/ds graph prepare`; preserve all live graph outputs.

Does not extract semantics, publish a graph, or certify CURRENT. Run with the
interpreter recorded in graphify-out/.graphify_python. --restore-only recovers
the nine saved outputs after an interrupted official update.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys

sys.dont_write_bytecode = True


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def stop_child(process):
    if process is not None and process.poll() is None:
        os.killpg(process.pid, signal.SIGTERM)
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--run", required=True)
    parser.add_argument("--restore-only", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    live = root / "graphify-out"
    recorded = Path((live / ".graphify_python").read_text().strip()).resolve()
    if Path(sys.executable).resolve() != recorded:
        raise ValueError("Use the interpreter recorded in graphify-out/.graphify_python")
    os.chdir(root)
    sys.path.insert(0, str(root / "scripts"))
    import ds_core
    import ds_graph
    if ds_core.ROOT.resolve() != root:
        raise ValueError("Project scripts resolved outside requested root")
    config = ds_core.read_json(root / "config/ds-project.json")
    ds_graph.runtime_gate(config)
    run = ds_graph.run_path(args.run)
    names = [*ds_graph.OUTPUTS, "ds-closure.json"]
    if len(names) != 9 or len(set(names)) != 9:
        raise ValueError("Expected exactly the nine reviewed graph outputs")
    backup = run / "official-update-before"
    record = run / "official-update-before.json"

    def restore():
        saved = ds_core.read_json(record)
        if saved.get("root") != str(root) or saved.get("run") != args.run or set(saved["sha256"]) != set(names):
            raise ValueError("Backup metadata belongs to another root/run/output set")
        for name, digest in saved["sha256"].items():
            if digest is not None and sha(backup / name) != digest:
                raise ValueError("Backup damaged; refusing partial restore: " + name)
        for name, digest in saved["sha256"].items():
            target = live / name
            if digest is None:
                target.unlink(missing_ok=True)
            else:
                temporary = live / (name + ".ds-skills-restore-tmp")
                shutil.copy2(backup / name, temporary)
                os.replace(temporary, target)
        actual = {name: sha(live / name) for name in names}
        if actual != saved["sha256"]:
            raise RuntimeError("Restored output hashes differ from saved baseline")
        ds_graph.assert_live_baseline(run)
        return actual

    if args.restore_only:
        print(json.dumps({"status": "RESTORED", "preserved_outputs": restore()}, indent=2))
        return 0
    for name in ("source-plan.json", "detection.json", "semantic-plan.json", "before/graph.json"):
        if not (run / name).is_file():
            raise ValueError("Run graph prepare first; missing " + name)
    if (run / "closure.json").exists() or (run / "ast.json").exists() or backup.exists() or record.exists():
        raise ValueError("Run already has AST, closure or update backup; preserve it instead of overwriting")
    ds_graph.assert_source_plan(run, config)
    ds_graph.assert_live_baseline(run)
    baseline = {name: sha(live / name) for name in names}
    backup.mkdir()
    for name, digest in baseline.items():
        if digest is not None:
            shutil.copy2(live / name, backup / name)
    write_json(record, {"root": str(root), "run": args.run, "sha256": baseline})
    if any(digest is not None and sha(backup / name) != digest for name, digest in baseline.items()):
        raise ValueError("Backup verification failed; official update was not started")

    def interrupted(signum, _frame):
        raise InterruptedError("Interrupted by signal " + str(signum))

    for signum in (signal.SIGTERM, signal.SIGHUP):
        signal.signal(signum, interrupted)
    process = None
    code = None
    after_official = None
    try:
        environment = os.environ.copy()
        environment["GRAPHIFY_OUT"] = "graphify-out"
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        with (run / "official-update.log").open("x") as log:
            process = subprocess.Popen(
                [sys.executable, "-B", "-m", "graphify", "update", "."],
                cwd=root, env=environment, stdout=log, stderr=subprocess.STDOUT,
                start_new_session=True,
            )
            code = process.wait()
        after_official = {name: sha(live / name) for name in names}
    finally:
        stop_child(process)
        restored = restore()
        write_json(run / "official-update-preservation.json", {
            "official_update_exit_code": code,
            "official_output_sha256_before_restore": after_official,
            "preserved_outputs": restored,
            "status": "RESTORED",
            "scope": "Nine live outputs preserved; official update is AST-only and does not certify CURRENT",
        })
    if code != 0:
        raise RuntimeError("Official update failed; live outputs restored; inspect official-update.log")
    ds_graph.assert_source_plan(run, config)
    import ds_graph_engine as engine
    engine.initialize(run)
    try:
        with (run / "ast-run.log").open("x") as log, contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
            engine.ast()
    finally:
        ds_graph.assert_live_baseline(run)
    ds_graph.assert_source_plan(run, config)
    ast = ds_core.read_json(run / "ast.json")
    expected = set(ds_core.read_json(run / "detection.json")["files"].get("code", []))
    extracted = {str((root / path).resolve()) for path in ast.get("extracted_sources", [])}
    missing = sorted(expected - extracted)
    summary = {
        "status": "AST_READY" if not ast.get("failed_sources") and not missing else "BLOCKED",
        "run": args.run, "nodes": len(ast.get("nodes", [])), "edges": len(ast.get("edges", [])),
        "expected_code_files": len(expected), "extracted_sources": len(extracted),
        "failed_sources": ast.get("failed_sources", []), "missing_sources": missing,
        "scope": "AST only; semantic chunks and scripts/ds graph close remain required",
    }
    write_json(run / "ast-preparation.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["status"] == "AST_READY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
