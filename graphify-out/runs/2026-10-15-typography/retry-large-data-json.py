"""Retry six known local data JSON files using a bounded 8 MiB read in memory.

Preserves the installed extractor, source files and failed run evidence. The
upstream 1 MiB config probe errors before classifying large data JSON. This run
uses exactly the installed extractor with only its local read bound changed,
then requires its explicit data-JSON skip. Project structural extraction still
indexes these data files and their actual references before graph publication.
"""
from pathlib import Path
import hashlib
import inspect
import json
import shutil
import sys
import graphify.extractors.json_config as module

root = Path.cwd().resolve()
run = root / 'graphify-out/runs/2026-10-15-typography'
ast_path = run / 'ast.json'
ast = json.loads(ast_path.read_text())
assert len(ast['failed_sources']) == 6
original = inspect.getsource(module.extract_json)
needle = '_JSON_MAX_BYTES = 1_048_576'
assert original.count(needle) == 1
namespace = dict(vars(module))
exec(compile(original.replace(needle, '_JSON_MAX_BYTES = 8_388_608'), '<bounded-local-json-retry>', 'exec'), namespace)
retry = namespace['extract_json']
rows = []
for name in ast['failed_sources']:
    path = Path(name).resolve()
    assert path.is_relative_to(root) and path.suffix == '.json'
    before = path.read_bytes()
    assert 1_048_576 < len(before) <= 8_388_608
    parsed = json.loads(before)
    result = retry(path)
    assert result.get('skipped', '').startswith('data json'), result
    assert not result.get('error') and not result.get('nodes') and not result.get('edges')
    assert path.read_bytes() == before
    rows.append({'source_file': str(path), 'sha256': hashlib.sha256(before).hexdigest(),
                 'bytes': len(before), 'root_type': type(parsed).__name__,
                 'top_level_keys': list(parsed) if isinstance(parsed, dict) else None,
                 'extractor_result': result,
                 'structural_supplement_required': True})
assert inspect.getsource(module.extract_json) == original
for source, backup in [(ast_path, run/'ast.initial-failed.json'),
                       (run/'ast-preparation.json', run/'ast-preparation.initial-failed.json')]:
    assert not backup.exists()
    shutil.copy2(source, backup)
report = {'status': 'RETRY_COMPLETE', 'source_files_unchanged': True,
          'installed_extractor_unchanged': True,
          'installed_extractor_sha256': hashlib.sha256(Path(inspect.getfile(module)).read_bytes()).hexdigest(),
          'initial_failure': 'json file too large to index', 'initial_bound': 1_048_576,
          'retry_bound': 8_388_608, 'rows': rows,
          'scope': 'AST config classification only; explicit data identities and references still require project structural supplement. Not a semantic PASS.'}
(run/'large-data-json-retry.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
ast['failed_sources'] = []
ast['extraction_retries'] = ['large-data-json-retry.json']
ast_path.write_text(json.dumps(ast, ensure_ascii=False, indent=2)+'\n')
preparation = json.loads((run/'ast-preparation.json').read_text())
preparation.update(status='AST_READY', failed_sources=[], extraction_retries=['large-data-json-retry.json'])
(run/'ast-preparation.json').write_text(json.dumps(preparation, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'status':'AST_READY', 'bounded_retries':len(rows), 'remaining_failed_sources':0,
                  'source_files_unchanged':True,'installed_extractor_unchanged':True}))
