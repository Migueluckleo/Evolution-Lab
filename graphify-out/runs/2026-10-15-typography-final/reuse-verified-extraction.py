"""Reuse only extraction whose complete source bytes match the final plan."""
from pathlib import Path
import hashlib,json,shutil,sys
from graphify.extract import _get_extractor

root=Path.cwd().resolve()
old=root/'graphify-out/runs/2026-10-15-typography'
new=root/'graphify-out/runs/2026-10-15-typography-final'
read=lambda p:json.loads(p.read_text())
dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
sys.path.insert(0,str(root/'scripts'))
import ds_graph,ds_core
config=read(root/'config/ds-project.json')
ds_graph.assert_source_plan(new,config)
ds_graph.assert_live_baseline(new)
oa,na=read(old/'source-plan.json'),read(new/'source-plan.json')
op,np=read(old/'semantic-plan.json'),read(new/'semantic-plan.json')
assert op['chunks']==np['chunks']
reused=[]
for i in range(4,61):
    for name in np['chunks'][i]:
        rel=Path(name).relative_to(root).as_posix()
        assert op['source_sha256'][rel]==np['source_sha256'][rel]==sha(Path(name))
    target=new/f'chunk-{i:02d}.json'
    assert not target.exists()
    shutil.copy2(old/target.name,target)
    reused.append({'chunk':target.name,'sha256':sha(target),'source_files':np['chunks'][i]})
od,nd=read(old/'detection.json'),read(new/'detection.json')
oc,nc=set(od['files']['code']),set(nd['files']['code'])
assert oc<=nc
for name in oc:
    rel=Path(name).relative_to(root).as_posix()
    assert oa['source_sha256'][rel]==na['source_sha256'][rel]==sha(Path(name))
ast=read(old/'ast.json');assert not ast['failed_sources']
assert {str((root/p).resolve()) for p in ast['extracted_sources']}==oc
added=[]
for name in sorted(nc-oc):
    path=Path(name);assert path.suffix=='.json' and path.stat().st_size<1048576
    json.loads(path.read_text())
    result=_get_extractor(path)(path)
    assert result.get('skipped','').startswith('data json') and not result.get('error')
    assert not result.get('nodes') and not result.get('edges')
    ast['extracted_sources'].append(name)
    added.append({'source_file':name,'sha256':sha(path),'result':result})
assert len(added)==1
ast['extraction_reuse']={'from_run':old.name,'basis':'All 938 source SHA-256 values match final bytes; one new JSON classified by the installed extractor. See extraction-reuse.json.'}
assert not (new/'ast.json').exists()
dump(new/'ast.json',ast)
for name in ['large-data-json-retry.json','official-update-preservation.json']:
    shutil.copy2(old/name,new/name)
dump(new/'ast-preparation.json',{'status':'AST_READY','expected_code_files':len(nc),'extracted_sources':len(ast['extracted_sources']),'failed_sources':[],
    'nodes':len(ast['nodes']),'edges':len(ast['edges']),'reused_sources':len(oc),'fresh_sources':len(added),
    'original_run':old.name,'retry_record':'large-data-json-retry.json','scope':'AST/data classification; structural supplement and semantic gate remain required.'})
dump(new/'extraction-reuse.json',{'status':'PASS','previous_run':old.name,'image_chunks':reused,'code_sources_reused':len(oc),'new_code_sources':added,
    'original_ast_sha256':sha(old/'ast.json'),'final_ast_sha256':sha(new/'ast.json'),
    'large_json_retry':'large-data-json-retry.json','official_update':'official-update-preservation.json','source_files_unchanged':True})
ds_graph.assert_source_plan(new,config)
ds_graph.assert_live_baseline(new)
print(json.dumps({'status':'PASS','images':len(reused),'code_reused':len(oc),'code_added':len(added)}))
