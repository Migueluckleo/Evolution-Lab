#!/usr/bin/env python3
"""Reuse43 already-read Specs only after a real frozen Graphify prepare.

No graph update/close, aliases, source edits or semantic fabrication. All
preflight checks finish before writing any seed. Existing different outputs
are never overwritten. --check-only computes the proposed partition read-only.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path('/Users/miguel.leo/Desktop/CONTPAQi-designSystem-Optimizado')
SPEC = ROOT/'.codex/skills/graphify/references/extraction-spec.md'
EXPECTED_SPEC_SHA = '32d7decad42d58129c6694ea4e4ce1f72a531bc5161827d2095787e9448735e9'
MANIFEST = Path('/tmp/typography-stable-specs-semantic.json')
TYPE_SET = {'code', 'document', 'paper', 'image', 'rationale', 'concept'}
RELATIONS = {'calls','implements','references','cites','conceptually_related_to','shares_data_with','semantically_similar_to','rationale_for'}
INFERRED = {.95, .85, .75, .65, .55}


def need(value, message):
    if not value:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2)+'\n').encode()


def repo_path(path):
    p = Path(path)
    need(p.is_absolute() and str(p.resolve()) == path and p.is_relative_to(ROOT), 'Not exact absolute repository source: '+path)
    return p.relative_to(ROOT).as_posix()


def stem(path):
    return re.sub('[^a-z0-9_]', '_', str(Path(repo_path(path)).with_suffix('')).lower())+'_'


def confidence(row, hyper=False):
    c, value = row.get('confidence'), row.get('confidence_score')
    need(not isinstance(value, bool), 'Boolean confidence score')
    need((c == 'EXTRACTED' and value == 1.0) or (c == 'INFERRED' and value in INFERRED)
         or (not hyper and c == 'AMBIGUOUS' and isinstance(value, (int,float)) and .1 <= value <= .3), 'Invalid confidence')


def expanded_prompt(template, files, number):
    return (template.replace('CHUNK_NUM', str(number)).replace('TOTAL_CHUNKS', '2')
            .replace('\nFILE_LIST\n', '\n'+'\n'.join(files)+'\n')
            .replace('DEEP_MODE (if --mode deep)', 'DEEP_MODE=false (standard mode)'))


def prepare_reuse(run_name):
    need(re.fullmatch('[a-z0-9][a-z0-9-]{0,79}', run_name), 'Invalid run name')
    run = ROOT/'graphify-out/runs'/run_name
    need(run.exists() and run.resolve() == run, 'A real non-symlink prepared run is required')
    required = [run/'source-plan.json', run/'semantic-plan.json', run/'before/graph.json']
    need(all(p.is_file() for p in required), 'prepare has not created its freeze, semantic plan and graph backup')
    source_plan, semantic_plan, prior = map(load, required)
    need(not list(run.glob('delta-*.json')), 'Unplanned semantic delta exists')
    need(sha(SPEC) == EXPECTED_SPEC_SHA == semantic_plan['prompt_sha256'], 'Extraction spec hash differs from prepared/extracted prompt')
    need(source_plan['source_sha256'][SPEC.relative_to(ROOT).as_posix()] == EXPECTED_SPEC_SHA, 'Extraction spec absent/mismatched in source freeze')
    need(sha(ROOT/'config/ds-project.json') == source_plan['config_sha256'], 'Configuration changed after prepare')
    # Check every source in the prepared freeze, including non-Spec evidence.
    drift = [p for p,h in source_plan['source_sha256'].items() if not (ROOT/p).is_file() or sha(ROOT/p) != h]
    need(not drift, 'Sources changed after prepare: '+str(drift[:10]))
    for filename in ['graph.json','graph.html','GRAPH_REPORT.md','manifest.json','.graphify_health.json',
                     '.graphify_labels.json','.graphify_labels.json.sig','cost.json','ds-closure.json']:
        backup, live = run/'before'/filename, ROOT/'graphify-out'/filename
        need(backup.exists() == live.exists() and (not backup.exists() or sha(backup) == sha(live)), 'Live graph changed after prepare: '+filename)
    chunks = semantic_plan['chunks']
    all_files = [p for group in chunks for p in group]
    need(len(all_files) == len(set(all_files)), 'Duplicate files across prepared chunks')
    for i, files in enumerate(chunks):
        need(load(run/f'chunk-{i:02d}.files.json') == files, 'Chunk list differs from prepared semantic plan')
        for p in files:
            relative = repo_path(p)
            need(relative in source_plan['semantic_required'], 'Chunk source is outside semantic delta')
            need(semantic_plan['source_sha256'][relative] == source_plan['source_sha256'][relative], 'Semantic/source freeze hash mismatch')
    need(set(map(repo_path, all_files)) == set(source_plan['semantic_required']), 'Semantic chunks do not exactly cover frozen delta')
    prior_ids = {n['id']: n for n in prior['nodes']}
    need(len(prior_ids) == len(prior['nodes']), 'Prior graph has duplicate IDs')
    manifest = load(MANIFEST)
    stable = manifest['files']
    need(len(stable) == len(set(stable)) == len(manifest['sha256']) == 43, 'Stable manifest must contain43 exact sources')
    need(set(stable) <= set(all_files), 'All43 reused sources must belong to this prepared semantic delta')
    template = SPEC.read_text().split('```', 2)[1].strip()+'\n'
    fragments, file_sets, proof_records, copied = [], [], [], {MANIFEST.name: MANIFEST.read_bytes()}
    for number in (1,2):
        fragment_path = Path(f'/tmp/typography-stable-semantic-{number}.json')
        evidence_path = Path(f'/tmp/typography-stable-semantic-{number}.evidence.json')
        prompt_path = Path(f'/tmp/typography-stable-semantic-prompt-{number}.txt')
        data, evidence = load(fragment_path), load(evidence_path)
        if number == 1:
            files, before, after = evidence['filesReadInFull'], evidence['before'], evidence['after']
            prompt_hashes = [evidence['prompt_sha256']]
            need(evidence['sourceBytesUnchanged'] is True and evidence['status'] == 'PASS', 'First extraction evidence is incomplete')
            before_path = Path('/tmp/typography-stable-semantic-1.before.json')
            historical_before = load(before_path)
            need(historical_before['files'] == before and historical_before['prompt_sha256'] == prompt_hashes[0], 'First pre-extraction ledger differs')
            recorded_external = set(evidence['verifiedExternalEndpoints'])
        else:
            files, before, after = evidence['files'], evidence['source_sha256_before'], evidence['source_sha256_after']
            prompt_hashes = [evidence['prompt_sha256_before'], evidence['prompt_sha256_after']]
            need(evidence['sources_unchanged'] is True and evidence['matches_manifest'] is True
                 and evidence['status'] == 'EXTRACTED_NOT_PUBLISHED' and evidence['read_completely'] == files,
                 'Second extraction evidence is incomplete')
            need(evidence['extraction_spec_sha256'] == EXPECTED_SPEC_SHA and evidence['deep_mode'] is False, 'Second extraction spec/mode changed')
            before_path = Path('/tmp/typography-stable-semantic-2.hashes-before.json')
            historical_before = load(before_path)
            # Preserve the original before ledger; its schema is checked below
            # against the source entries instead of replacing it with new hashes.
            before_map = historical_before.get('source_sha256', historical_before.get('sources', historical_before.get('sha256', historical_before)))
            need(all(before_map.get(p) == h for p,h in before.items()), 'Second pre-extraction ledger differs')
            recorded_external = set(evidence['external_existing_endpoint_ids'])
        expected_files = stable[:22] if number == 1 else stable[22:]
        need(files == expected_files and before == after and set(before) == set(files), 'Original fragment file/hash coverage differs')
        need(sha(fragment_path) == evidence['output_sha256'], 'Extracted fragment bytes changed')
        need(all(h == sha(prompt_path) for h in prompt_hashes), 'Original prompt bytes changed')
        need(prompt_path.read_text() == expanded_prompt(template, files, number), 'Original prompt does not exactly render current extraction-spec with original files/mode')
        for p,h in before.items():
            relative = repo_path(p)
            need(h == manifest['sha256'][p] == sha(Path(p)) == source_plan['source_sha256'][relative]
                 == semantic_plan['source_sha256'][relative], 'Source hash differs from before/after/manifest/freeze: '+p)
        need(data.get('input_tokens') == data.get('output_tokens') == 0 and data.get('usage_status') == 'UNAVAILABLE', 'Unverified token accounting')
        need(all(isinstance(data.get(k), list) for k in ('nodes','edges','hyperedges')), 'Fragment schema missing arrays')
        need(len(data['hyperedges']) <= 3, 'Original fragment exceeds hyperedge limit')
        represented = set()
        for node in data['nodes']:
            need(node.get('source_file') in files and node.get('file_type') in TYPE_SET, 'Invalid node source or type')
            need(bool(node.get('label')) and re.fullmatch('[a-z0-9_]+',node.get('id',''))
                 and node['id'].startswith(stem(node['source_file'])), 'Invalid/non-deterministic full-path node identity')
            if not node.get('reference_only'):represented.add(node['source_file'])
            for field in ('source_url','captured_at','author','contributor'):
                need(field in node, 'Missing provenance field '+field)
        need(represented == set(files), 'Fragment does not contain semantic entities for all assigned sources')
        for edge in data['edges']:
            need(edge.get('source_file') in files and edge.get('relation') in RELATIONS, 'Edge source/relation outside schema')
            confidence(edge)
        for hyperedge in data['hyperedges']:
            need(hyperedge.get('source_file') in files and hyperedge.get('relation') in {'participate_in','implement','form'}
                 and re.fullmatch('[a-z0-9_]+',hyperedge.get('id','')) and len(set(hyperedge.get('nodes',[]))) >= 3, 'Invalid hyperedge')
            confidence(hyperedge, True)
        fragments.append(data);file_sets.append(set(files))
        proof_records.append({'fragment':fragment_path.name,'sha256':sha(fragment_path),'evidence':evidence_path.name,
                              'evidenceSha256':sha(evidence_path),'prompt':prompt_path.name,'promptSha256':sha(prompt_path),
                              'files':files,'recordedExternalEndpoints':sorted(recorded_external)})
        for path in (fragment_path,evidence_path,prompt_path,before_path):copied[path.name]=path.read_bytes()
    need(not file_sets[0] & file_sets[1] and file_sets[0] | file_sets[1] == set(stable), 'Fragment union is not exact43')
    all_nodes = [n for d in fragments for n in d['nodes']]
    new_ids = {n['id']:n for n in all_nodes}
    need(len(new_ids) == len(all_nodes), 'Duplicate IDs between original fragments')
    hypers = [h for d in fragments for h in d['hyperedges']]
    need(len({h['id'] for h in hypers}) == len(hypers), 'Duplicate hyperedge IDs')
    allowed = set(new_ids) | set(prior_ids)
    external_used = set()
    for d in fragments:
        for endpoints in ([e['source'],e['target']] for e in d['edges']):
            need(set(endpoints) <= allowed, 'Cross-edge endpoint absent from both real fragments and prior graph')
            external_used |= set(endpoints) - set(new_ids)
        for h in d['hyperedges']:
            need(set(h['nodes']) <= allowed, 'Hyperedge endpoint absent from fragments/prior graph')
            external_used |= set(h['nodes']) - set(new_ids)
    need(external_used == set().union(*(set(p['recordedExternalEndpoints']) for p in proof_records)), 'External endpoint proof coverage differs')
    for nid in external_used:
        source = prior_ids[nid].get('source_file')
        need(source, 'External endpoint lacks source identity')
        path = Path(source);relative = path.relative_to(ROOT).as_posix() if path.is_absolute() else source
        need(relative in source_plan['source_sha256'], 'External prior endpoint source deleted/excluded from frozen corpus')
    for nid in set(new_ids) & set(prior_ids):
        source = prior_ids[nid].get('source_file','')
        need((ROOT/source).resolve() == Path(new_ids[nid]['source_file']), 'New ID collides with a different existing entity source')

    writes = {run/'stable-semantic-reuse'/name:raw for name,raw in copied.items()}
    writes[run/'stable-semantic-reuse'/Path(__file__).name] = Path(__file__).read_bytes()
    rows=[]
    all_edges=[e for d in fragments for e in d['edges']]
    for i, assigned in enumerate(chunks):
        selected = set(assigned) & set(stable)
        seed = {k:[row for d in fragments for row in d[k] if row['source_file'] in selected]
                for k in ('nodes','edges','hyperedges')}
        need(len(seed['hyperedges']) <= 3, f'Chunk {i:02d} would contain {len(seed["hyperedges"])} hyperedges; none discarded')
        represented = {n['source_file'] for n in seed['nodes'] if not n.get('reference_only')}
        need(represented == selected, 'Repartition lost source coverage')
        remaining = [p for p in assigned if p not in selected]
        seed.update(input_tokens=0,output_tokens=0,usage_status='UNAVAILABLE')
        writes[run/f'seed-{i:02d}.json'] = encoded(seed)
        writes[run/f'chunk-{i:02d}.remaining.files.json'] = encoded(remaining)
        if not remaining:
            writes[run/f'chunk-{i:02d}.json'] = encoded(seed)
        rows.append({'chunk':i,'seed':f'seed-{i:02d}.json','remainingList':f'chunk-{i:02d}.remaining.files.json',
                     'status':'COMPLETE_FROM_VERIFIED_EXTRACTION' if not remaining else 'SEED_ONLY_INCOMPLETE',
                     'reusedFiles':len(selected),'remainingFiles':len(remaining),
                     'nodes':len(seed['nodes']),'edges':len(seed['edges']),'hyperedges':len(seed['hyperedges']),
                     'seedSha256':hashlib.sha256(encoded(seed)).hexdigest()})
    need(sum(r['reusedFiles'] for r in rows)==43 and sum(r['nodes'] for r in rows)==len(all_nodes)
         and sum(r['edges'] for r in rows)==len(all_edges) and sum(r['hyperedges'] for r in rows)==len(hypers), 'Repartition changed original graph content counts')
    report={'schema_version':1,'status':'VERIFIED_SEEDS_PREPARED','graphStatus':'NOT_PUBLISHED',
            'run':run_name,'sourcePlanSha256':sha(run/'source-plan.json'),'semanticPlanSha256':sha(run/'semantic-plan.json'),
            'extractionSpecSha256':sha(SPEC),'manifestSha256':sha(MANIFEST),'helperSha256':sha(Path(__file__)),
            'priorGraphSha256':sha(run/'before/graph.json'),'originalExtractions':proof_records,
            'counts':{'sourceFiles':43,'nodes':len(all_nodes),'edges':len(all_edges),'hyperedges':len(hypers),
                      'externalPriorEndpoints':len(external_used),'completeChunks':sum(r['remainingFiles']==0 for r in rows),
                      'incompleteChunks':sum(r['remainingFiles']>0 for r in rows)},'chunks':rows,
            'rule':'Repartition unchanged real extraction by exact source_file; every seed with remaining sources is incomplete and cannot substitute for chunk-NN.json.',
            'copiedEvidenceSha256':{str(p.relative_to(run)):hashlib.sha256(raw).hexdigest() for p,raw in writes.items() if p.parent.name=='stable-semantic-reuse'},
            'usage_status':'UNAVAILABLE','input_tokens':0,'output_tokens':0}
    writes[run/'stable-semantic-reuse.json'] = encoded(report)
    for p,raw in writes.items():
        need(not p.exists() or p.read_bytes()==raw, 'Refuse to replace a different existing output: '+str(p))
    # Incomplete finals might already be separately completed; leave them alone.
    return writes,report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',required=True)
    parser.add_argument('--check-only',action='store_true')
    args=parser.parse_args()
    try:
        writes,report=prepare_reuse(args.run)
        if not args.check_only:
            for path,raw in writes.items():
                if path.exists():continue
                path.parent.mkdir(parents=True,exist_ok=True)
                with path.open('xb') as stream:stream.write(raw)
        print(json.dumps({'status':'CHECK_ONLY' if args.check_only else report['status'],'counts':report['counts'],
                          'chunks':report['chunks'],'graphWrites':'NOT_RUN'},ensure_ascii=False))
        return 0
    except (ValueError,KeyError,TypeError,OSError,IndexError) as error:
        print(json.dumps({'status':'BLOCKED','error':str(error),'graphWrites':'NOT_RUN'},ensure_ascii=False),file=sys.stderr)
        return 2


if __name__=='__main__':
    sys.exit(main())
