"""Run-local recovery of Graphify's size-before-data-classification failure.
No package or source is modified. The upstream parser is replayed only for the
failed, hash-verified data files, with an 8 MiB process-local bound. Its ordinary
`skipped=data json` outcome is required. The original ast.json stays unchanged.
"""
from pathlib import Path
import hashlib, inspect, json, sys
import graphify.extractors.json_config as extractor
from graphify.cache import load_cached
RUN = Path(__file__).resolve().parent
ROOT = RUN.parents[2]
read = lambda p: json.loads(p.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
ast = read(RUN/'ast.json')
plan = read(RUN/'source-plan.json')
old = read(RUN/'before/graph.json')
expected = plan.get('source_sha256', {})
if not expected:
    expected = read(RUN/'source-plan.json')['source_sha256']
failed = list(ast.get('failed_sources', []))
assert failed, 'No failed sources to recover'
source = inspect.getsource(extractor.extract_json)
needle = '_JSON_MAX_BYTES = 1_048_576'
assert source.count(needle) == 1
runtime_source = source.replace(needle, '_JSON_MAX_BYTES = 8_388_608')
namespace = dict(vars(extractor))
exec(compile(runtime_source, '<run-local bounded JSON extractor>', 'exec'), namespace)
rows=[]
for raw in failed:
    path = Path(raw); relative = path.relative_to(ROOT).as_posix()
    assert path.suffix == '.json'
    assert sha(path) == expected[relative], ('Source changed', relative)
    assert 1_048_576 < path.stat().st_size <= 8_388_608
    content = read(path)
    assert isinstance(content, dict), ('Unexpected root type', relative)
    assert not (set(content) & extractor._CONFIG_JSON_KEYS), ('Config keys found', relative)
    assert path.name.casefold() not in extractor._CONFIG_JSON_NAMES
    before = [n for n in old['nodes'] if n.get('source_file') in (raw,relative) and n.get('sha256') == sha(path)]
    assert before, ('Prior same-hash artifact missing', relative)
    cache = load_cached(path, ROOT, cache_root=ROOT)
    result = namespace['extract_json'](path)
    assert result == {'nodes': [], 'edges': [], 'skipped': 'data json (not a config/manifest)'}, (relative,result)
    rows.append({'source_file': raw, 'sha256': sha(path), 'bytes': path.stat().st_size,
                 'root_keys': list(content), 'prior_same_hash_artifacts': [n['id'] for n in before],
                 'upstream_cache_hit': cache is not None, 'result': result})
recovered = dict(ast)
recovered['failed_sources'] = [p for p in failed if p not in {r['source_file'] for r in rows}]
assert not recovered['failed_sources']
assert {r['source_file'] for r in rows} <= set(ast['extracted_sources'])
audit = {'status':'PASS', 'scope':'Bounded structural classification of the ten oversized data JSON files; not semantic extraction or product validation',
         'method':'Replay the unmodified upstream JSON extraction algorithm in an isolated namespace with the sole byte-limit substitution 1 MiB -> 8 MiB, restricted to hash-verified failure paths. Require ordinary upstream data-JSON skip. Do not edit installed package, canonical sources, or original ast.json.',
         'upstream_extractor_sha256':sha(Path(inspect.getsourcefile(extractor))),
         'upstream_function_sha256':hashlib.sha256(source.encode()).hexdigest(),
         'runtime_function_sha256':hashlib.sha256(runtime_source.encode()).hexdigest(),
         'original_ast_sha256':sha(RUN/'ast.json'), 'original_failed_sources':failed,
         'recovered_sources':rows, 'remaining_failed_sources':recovered['failed_sources'],
         'supplement_required':True,
         'supplement_scope':'File identity, source hash, top-level data keys/recorded status and exact local reference strings; no claim of field-by-field semantic extraction.',
         'token_usage':'UNAVAILABLE'}
recovered['recovery_audit'] = str(RUN/'large-data-json-recovery.json')
(RUN/'ast-recovered.json').write_text(json.dumps(recovered, ensure_ascii=False, indent=2)+'\n')
audit['recovered_ast_sha256'] = sha(RUN/'ast-recovered.json')
(RUN/'large-data-json-recovery.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'status':'PASS','classified_files':len(rows),'cache_hits':sum(r['upstream_cache_hit'] for r in rows),'remaining_failed_sources':len(recovered['failed_sources']),'original_ast_preserved':True,'outputs':['ast-recovered.json','large-data-json-recovery.json']}))
