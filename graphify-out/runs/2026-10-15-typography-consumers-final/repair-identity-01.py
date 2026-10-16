import copy, hashlib, json, re, shutil, sys
from pathlib import Path
ROOT=Path('/Users/miguel.leo/Desktop/CONTPAQi-designSystem-Optimizado')
RUN=ROOT/'graphify-out/runs/2026-10-15-typography-consumers-final'
read=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
write=lambda p,d:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
old='registry_skills_versioned_consumer_skill_release_registry'
stable='registry_skills_document'
path=RUN/'chunk-01.json'; part=read(path); before=read(RUN/'before/graph.json'); combined=read(RUN/'combined-raw.json')
assert sum(n['id']==stable and n.get('source_file')=='registry/skills.md' and n.get('file_type')=='document' for n in before['nodes'])==1
assert sum(n['id']==old and n.get('source_file')==str(ROOT/'registry/skills.md') and n.get('file_type')=='document' for n in part['nodes'])==1
assert (ROOT/'registry/skills.md').read_text().splitlines()[0]=='# Releases de skills del DS'
archive=RUN/'identity-repair-attempt-01';archive.mkdir(exist_ok=True)
for name in ['chunk-01.json','chunk-01-15-17.validation.json','combined-raw.json','extract-docs-01.py']:
 assert not (archive/name).exists(),name
 shutil.copy2(RUN/name,archive/name)
# The same document is freshly extracted, but retains its established external identity.
for n in part['nodes']:
 if n['id']==old:n['id']=stable
for e in part['edges']:
 for key in ['source','target']:
  if e[key]==old:e[key]=stable
for h in part.get('hyperedges',[]):h['nodes']=[stable if i==old else i for i in h['nodes']]
part['nodes'].sort(key=lambda n:n['id'])
part['edges'].sort(key=lambda e:(e['source_file'],e['source'],e['target'],e['relation'],str(e.get('source_location'))))
write(path,part)
helper=RUN/'extract-docs-01.py';text=helper.read_text()
needle=" ident=norm(str(Path(p).with_suffix('')))+'_'+norm(label)\n"
assert text.count(needle)==1
text=text.replace(needle,needle+" # Preserve the established document identity referenced by retained external semantics.\n if p=='registry/skills.md' and label=='Versioned consumer skill release registry':ident='registry_skills_document'\n")
helper.write_text(text)
# Reconstruct the exact previously assembled union with the one-to-one identity change in memory.
fixed=copy.deepcopy(combined)
for n in fixed['nodes']:
 if n['id']==old:n['id']=stable
for e in fixed['edges']:
 for key in ['source','target']:
  if e[key]==old:e[key]=stable
for h in fixed.get('hyperedges',[]):h['nodes']=[stable if i==old else i for i in h['nodes']]
ids={n['id'] for n in fixed['nodes']}
assert len(ids)==len(fixed['nodes'])
missing=[e for e in fixed['edges'] if e['source'] not in ids or e['target'] not in ids]
hmissing=[h for h in fixed.get('hyperedges',[]) if not set(h['nodes'])<=ids]
assert not missing and not hmissing,(missing,hmissing)
# Inventory every prior endpoint from the replaced 22 sources. Any prior ID still used
# in the assembled union must exist; retired isolated concepts are not fabricated aliases.
files=read(RUN/'chunk-01.files.json');relative={str(Path(f).relative_to(ROOT)) for f in files}
prior={n['id'] for n in before['nodes'] if n.get('source_file') in relative}
used={i for e in fixed['edges'] for i in [e['source'],e['target']]}|{i for h in fixed.get('hyperedges',[]) for i in h['nodes']}
referenced_prior=prior&used
assert not referenced_prior-ids
retired=sorted(prior-ids)
plan=read(RUN/'source-plan.json')['source_sha256']
assert all(sha(Path(f))==plan[str(Path(f).relative_to(ROOT))] for f in files)
seed=read(RUN/'seed-01.json')
assert all(n in part['nodes'] for n in seed['nodes']) and all(e in part['edges'] for e in seed['edges'])
sys.path.insert(0,str(ROOT/'scripts'))
from ds_graph import validate_fragments
validate_fragments(RUN)
validation=read(RUN/'chunk-01-15-17.validation.json')
validation['chunks']['1']['sha256']=sha(path)
validation['full_assembled_union_endpoint_integrity']='PASS after stable identity replacement; no edge removal'
validation['identity_repair_evidence']='chunk-01.identity-repair.json'
write(RUN/'chunk-01-15-17.validation.json',validation)
combined_ids={n['id'] for n in combined['nodes']}
proof={
 'status':'PASS','scope':'Fragment identity and in-memory full assembled union only; no live graph publication',
 'identity':{'replaced':old,'preserved':stable,'source_file':str(ROOT/'registry/skills.md'),'source_location':'L1','evidence':'Both the before graph and the current source identify the same Releases de skills del DS document. Current attributes remain freshly extracted; only its stable ID is preserved.'},
 'failed_attempt':{'root_report':'root-close-attempt-01.json','preserved_directory':str(archive.relative_to(RUN)),'chunk_sha256':sha(archive/'chunk-01.json'),'combined_sha256':sha(archive/'combined-raw.json'),'missing_endpoints_before':[e for e in combined['edges'] if e['source'] not in combined_ids or e['target'] not in combined_ids]},
 'chunk':{'sha256':sha(path),'nodes':len(part['nodes']),'edges':len(part['edges']),'hyperedges':len(part.get('hyperedges',[])),'sources':len(files),'prompt_sha256':sha(RUN/'chunk-01.prompt.txt')},
 'full_union':{'nodes':len(fixed['nodes']),'edges':len(fixed['edges']),'hyperedges':len(fixed.get('hyperedges',[])),'missing_edge_endpoints':missing,'missing_hyperedge_endpoints':hmissing,'edges_removed':0},
 'prior_endpoint_audit':{'sources':len(relative),'prior_node_ids':len(prior),'prior_ids_still_referenced':len(referenced_prior),'missing_still_referenced':sorted(referenced_prior-ids),'retired_unreferenced_ids':retired},
 'checks':{'all_fragments_validation':'PASS','all22_source_hashes':'PASS','seed_exact_preservation':'PASS','current_source_title_and_prior_document_identity':'PASS'},
 'source_sha256':{f:sha(Path(f)) for f in files},'usage_status':'UNAVAILABLE'}
write(RUN/'chunk-01.identity-repair.json',proof)
print(json.dumps({k:proof[k] for k in ['status','chunk','full_union','prior_endpoint_audit']},ensure_ascii=False,indent=2))
