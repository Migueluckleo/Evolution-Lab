#!/usr/bin/env python3
"""Bounded local retry for large data JSON after the preserved official AST run.

Never changes corpus bytes, installed extractor code, semantics or live graph.
Unknown failures remain blocking. Original failed AST/preparation are preserved.
"""
import argparse
import hashlib
import inspect
import json
from pathlib import Path
import shutil
import sys


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run', required=True)
    a = p.parse_args()
    root = Path.cwd().resolve()
    recorded = Path((root/'graphify-out/.graphify_python').read_text().strip()).resolve()
    if Path(sys.executable).resolve() != recorded:
        raise ValueError('Use the recorded Graphify interpreter')
    sys.path.insert(0, str(root/'scripts'))
    import ds_core, ds_graph
    import graphify.extractors.json_config as module
    run = ds_graph.run_path(a.run)
    config = ds_core.read_json(root/'config/ds-project.json')
    ds_graph.assert_source_plan(run, config)
    ds_graph.assert_live_baseline(run)
    ast_path = run/'ast.json'
    ast = ds_core.read_json(ast_path)
    preparation = ds_core.read_json(run/'ast-preparation.json')
    if preparation.get('missing_sources'):
        raise ValueError('AST source coverage is incomplete; bounded retry does not cover missing files')
    failures = ast.get('failed_sources', [])
    if not failures:
        print(json.dumps({'status': 'NO_RETRY_NEEDED'}))
        return
    original = inspect.getsource(module.extract_json)
    needle = '_JSON_MAX_BYTES = 1_048_576'
    if original.count(needle) != 1:
        raise ValueError('Installed extractor no longer matches reviewed bounded retry')
    namespace = dict(vars(module))
    exec(compile(original.replace(needle, '_JSON_MAX_BYTES = 8_388_608'), '<bounded-local-json-retry>', 'exec'), namespace)
    retry = namespace['extract_json']
    rows = []
    detected = set(ds_core.read_json(run/'detection.json')['files']['code'])
    for name in failures:
        source = Path(name).resolve()
        if not source.is_relative_to(root) or str(source) not in detected or source.suffix != '.json':
            raise ValueError('Failure is not an exact detected JSON: '+name)
        before = source.read_bytes()
        if not 1_048_576 < len(before) <= 8_388_608:
            raise ValueError('Unknown failure or file beyond reviewed8MiB bound: '+name)
        data = json.loads(before)
        result = retry(source)
        if (not result.get('skipped', '').startswith('data json') or result.get('error')
                or result.get('nodes') or result.get('edges') or source.read_bytes() != before):
            raise ValueError('Retry was not an unchanged, explicit data-JSON classification: '+name)
        rows.append({'source_file': str(source), 'sha256': hashlib.sha256(before).hexdigest(),
                     'bytes': len(before), 'root_type': type(data).__name__,
                     'top_level_keys': list(data) if isinstance(data, dict) else None,
                     'extractor_result': result, 'structural_supplement_required': True})
    if inspect.getsource(module.extract_json) != original:
        raise ValueError('Installed extractor source changed')
    ds_graph.assert_source_plan(run, config)
    ds_graph.assert_live_baseline(run)
    for source, backup in ((ast_path, run/'ast.initial-failed.json'),
                           (run/'ast-preparation.json', run/'ast-preparation.initial-failed.json')):
        if backup.exists():
            raise ValueError('Historical failure backup already exists; do not overwrite')
        shutil.copy2(source, backup)
    report = {'status': 'RETRY_COMPLETE', 'source_files_unchanged': True,
              'installed_extractor_unchanged': True,
              'installed_extractor_sha256': hashlib.sha256(Path(inspect.getfile(module)).read_bytes()).hexdigest(),
              'initial_bound': 1_048_576, 'retry_bound': 8_388_608, 'rows': rows,
              'scope': 'AST config classification only; all files still require project structural coverage. Not semantic QA.'}
    ds_core.dump(run/'large-data-json-retry.json', report)
    ast['failed_sources'] = []
    ast['extraction_retries'] = ['large-data-json-retry.json']
    ds_core.dump(ast_path, ast)
    preparation.update(status='AST_READY', failed_sources=[], extraction_retries=['large-data-json-retry.json'])
    ds_core.dump(run/'ast-preparation.json', preparation)
    ds_graph.assert_source_plan(run, config)
    ds_graph.assert_live_baseline(run)
    print(json.dumps({'status': 'AST_READY', 'bounded_retries': len(rows), 'remaining_failed_sources': 0,
                      'structural_supplement_still_required': True}))


if __name__ == '__main__':
    main()
