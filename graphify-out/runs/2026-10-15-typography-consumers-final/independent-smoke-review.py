"""Review three completed read-only CLI smokes against their current source evidence."""
import hashlib
import json
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RUN = Path(__file__).resolve().parent
EXPECTED = '2f1f6a8c4813923b7f14b6382eb76dffb0b04e707938943d55490410a63ccd63'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads(p.read_text())
graphpath = ROOT/'graphify-out/graph.json'
assert sha(graphpath) == EXPECTED
graph = read(graphpath)
nodes = {n['id']: n for n in graph['nodes']}
links = graph.get('links', graph.get('edges', []))
plan = read(RUN/'independent-smoke-plan.json')
freeze = read(RUN/'source-plan.json')['source_sha256']
checked_sources = {}
def source(path):
    path = Path(path)
    if not path.is_absolute(): path = ROOT/path
    rel = str(path.relative_to(ROOT))
    actual = sha(path)
    assert actual == freeze[rel], ('Source drift', rel)
    checked_sources[rel] = actual
    return path
def data(path): return read(source(path))

adj = defaultdict(list)
for e in links:
    adj[e['source']].append((e['target'],e))
    adj[e['target']].append((e['source'],e))
def navigation(a,b):
    """Undirected navigation only: preserve actual edge endpoints/direction in output."""
    assert a in nodes and b in nodes
    q=deque([a]);previous={a:None}
    while q:
        c=q.popleft()
        if c==b:break
        for target,edge in adj[c]:
            if target not in previous:previous[target]=(c,edge);q.append(target)
    assert b in previous, ('No navigation path',a,b)
    out=[];c=b
    while previous[c]:
        old,e=previous[c]
        out.append({'from':old,'to':c,'edge':{k:e[k] for k in ('source','target','relation','confidence','confidence_score','source_file','source_location') if k in e}})
        c=old
    return {'source':a,'target':b,'mode':'UNDIRECTED_NAVIGATION_NOT_CAUSAL_PROOF','steps':list(reversed(out))}

amendment='specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md'
amendment_text=source(amendment).read_text()
catalog=data('specs/tokens/ai-design-system.typography.v0.1.2.json')
global_qa=data('qa/implementations/typography/consumption-v0.1.1/consumer-final.global.v0.1.2.json')
overlay=data('qa/implementations/typography/consumption-v0.1.1/consumer-final.native-inheritance.v0.1.2.json')
historical=data('qa/implementations/typography/consumption-v0.1.1/consumer-final.v0.1.1.strict.json')
counts=global_qa['counts']
assert catalog['version']=='0.1.2' and len(catalog['styles'])==79
assert global_qa['result']==overlay['result']=='PASS' and historical['result']=='FAIL'
assert (counts['resolvedRanges'],counts['directStyleRanges'],counts['inheritedNativeScaleRanges'],counts['unresolvedRanges'])==(3353,3250,103,0)
assert counts['nativeLocalEmptyRanges']==counts['uiIntervalsWithoutStyle']==overlay['counts']['localEmptyStyleIds']==103
assert counts['afterPages']==34 and counts['documentationNodes']==150 and counts['preservationHashesEqual']==3501
assert any('Table atomic whole-page' in s for s in global_qa['limits'])
native_id='specs_typography_native_inheritance_amendment_v0_1_2_typography_native_inheritance_001'
coverage_id='qa_implementations_typography_v0_1_2_review_coverage'
assert nodes[native_id]['catalog_styles']==79 and nodes[native_id]['version']=='0.1.2'
assert '3250direct+103provennative' in nodes[coverage_id]['summary']
assert '103' in amendment_text and 'NAT-01' in amendment_text

manifest=data('qa/skills/release-0.2.1/manifest-summary.json')
installed=data('qa/skills/release-0.2.1/installed-check.json')
release_text=source('qa/skills/release-0.2.1/README.md').read_text()
registry_text=source('registry/skills.md').read_text()
protocol_text=source('protocols/08-SKILLS-AND-RELEASES.md').read_text()
assert manifest['version']==installed['version']=='0.2.1' and installed['status']=='CURRENT'
assert manifest['families']==43 and manifest['ds_sources']==2131
assert set(manifest['packages'])=={'contpaqi-figma-screens','contpaqi-po-prototypes'}
release_id='registry_skills_consumer_skills_release_0_2_1'
assert nodes[release_id]['families']==manifest['families'] and nodes[release_id]['ds_digest']==manifest['ds_digest']
assert nodes[release_id]['figma_prototype']=='NOT_RUN' and 'NOT_RUN' in release_text
assert 'registry_skills_document' in nodes
family_coverage='specs_typography_consumption_amendment_v0_1_0_exact_family_and_range_coverage'
family_targets={other for other,e in adj[family_coverage] if nodes[other].get('source_file','').startswith('specs/components/') and '.typography.amendment.v0.1.0.md' in nodes[other].get('source_file','')}
assert len(family_targets)==43, len(family_targets)
for skill in ('contpaqi-figma-screens','contpaqi-po-prototypes'):
    assert skill in source('skills/'+skill+'/SKILL.md').read_text()

countdir='qa/implementations/typography/consumption-v0.1.1/inheritance-count-four-thirds/'
count_text=source(countdir+'README.md').read_text()
evaluation=data(countdir+'evaluation.json')
cleanup=data(countdir+'cleanup.result.json')
assert len(evaluation['checks'])==12 and all(evaluation['checks'].values())
assert evaluation['status']=='CAUSAL_INHERITANCE_SUPPORTED_FOR_THIS_PILOT'
assert cleanup['status']=='CLEANUP_COMPLETE' and cleanup['errors']==[] and len(cleanup['removedNodeIds'])==27
observations={o['phase']:o for o in evaluation['observations']}
a,b,restored=(observations[k] for k in ('A','B','RESTORED_A'))
for k in ('instanceRecipe','mainHash','instanceHash','geometryHash'):assert a[k]==restored[k]
assert a['instanceRecipe']['fontSize']==5.333333492279053 and b['instanceRecipe']['fontSize']==26.666667938232422
assert all(o['instanceRecipe']['textStyleId']=='' for o in observations.values())
assert '155:136/texto155:137' in count_text
for artifact in evaluation['artifacts']:
    assert sha(source(countdir+artifact['file']))==artifact['sha256']

artifact_native='specs_typography_native_inheritance_amendment_v0_1_2_artifact_md'
artifact_catalog='specs_tokens_ai_design_system_typography_v0_1_2_artifact_json'
artifact_global='qa_implementations_typography_consumption_v0_1_1_consumer_final_global_v0_1_2_artifact_json'
count_causal='qa_implementations_typography_consumption_v0_1_1_inheritance_count_four_thirds_readme_causal'
count_restored='qa_implementations_typography_consumption_v0_1_1_inheritance_count_four_thirds_readme_restoration'
paths=[
 [navigation(artifact_native,artifact_catalog),navigation(artifact_native,artifact_global)],
 [navigation(release_id,'skills_contpaqi_figma_screens_skill_contpaqi_figma_screens'),navigation(release_id,'skills_contpaqi_po_prototypes_skill_contpaqi_po_prototypes'),navigation(release_id,'protocols_08_skills_and_releases_artifact_md'),navigation(release_id,family_coverage)],
 [navigation(count_causal,count_restored)]]
answers=[
 {'result':'PASS_SOURCE_CROSS_CHECK','catalogStyles':79,'uiRanges':3353,'directStyleRanges':3250,'inheritedNativeScaleRanges':103,'observedEmptyLocalStyleIds':103,'historicalStrictResult':'FAIL_RETAINED','limits':['Table atomic whole-page response missing; final text QA does not reconstruct it.','150 editorial nodes preserved; user audit PENDING.','Native exception applies only to proven scoped entries.']},
 {'result':'PASS_SOURCE_CROSS_CHECK','version':'0.2.1','packages':list(manifest['packages']),'sourceFiles':2131,'familySpecCoverageEdges':43,'dsDigest':manifest['ds_digest'],'installedStatus':'CURRENT','newFigmaScreenExecution':'NOT_RUN','humanAudit':'PENDING'},
 {'result':'PASS_SOURCE_CROSS_CHECK','scope':'One Count4/3 pilot; all103 proven separately.','checksPassed':12,'restoration':'A and RESTORED_A recipes/geometry/main/instance hashes exactly equal.','originalGuardsPreserved':True,'localStyleId':'EMPTY_OBSERVED_THROUGHOUT','cleanup':'CLEANUP_COMPLETE','removedTemporaryNodeIds':27}]
queries=[]
for q,answer,nav in zip(plan['queries'],answers,paths):
    execution=read(RUN/('smoke-'+q['id']+'.execution.json'))
    assert execution['exitCode']==0 and execution['stderrBytes']==0
    stdout=RUN/execution['stdout'];raw=stdout.read_text();pathfile=RUN/('smoke-'+q['id']+'.path.txt')
    assert 'Shortest path (' in pathfile.read_text()
    anchors=[]
    for expected in q['verified_node_anchors']:
        node=nodes[expected['id']];source(node['source_file'])
        anchors.append(node)
    queries.append({'id':q['id'],'expandedTokens':q['expanded_tokens'],'commandArgs':q['command_args'],'execution':execution,
                    'cliTruncated':'[!] TRUNCATED' in raw,'cliCompleteOverBudget':'Complete answer over budget' in raw,
                    'outputSha256':sha(stdout),'pathOutput':pathfile.name,'pathOutputSha256':sha(pathfile),
                    'exactPublishedNodeAnchors':anchors,'sourceCrossCheck':answer,'verifiedNavigationPaths':nav})
assert sha(graphpath)==EXPECTED
report={'schema_version':1,'status':'PASS_SCOPED_INDEPENDENT_SMOKES','graphSha256Before':EXPECTED,'graphSha256After':sha(graphpath),
        'graphCounts':{'nodes':len(nodes),'edges':len(links)},'queries':queries,'checkedSources':checked_sources,
        'allCheckedSourcesMatchFrozenPlan':True,'sourceWrites':'NOT_RUN','graphWrites':'NOT_RUN','saveResult':'NOT_RUN','reflect':'NOT_RUN',
        'limitations':['First two broad BFS outputs were truncated; preserved raw outputs and exact-node/path checks resolve scope.','Third CLI includes unrelated lexical matches and exceeded requested budget to retain all found edges.','Navigation paths are undirected and preserve original edge directions; they do not imply causal or normative priority.','This smoke validates retrieval and source consistency, not a fresh Figma/browser execution.']}
(RUN/'independent-smoke-queries.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':report['status'],'queries':len(queries),'checkedSources':len(checked_sources),'navigationPaths':sum(map(len,paths)),'graphUnchanged':True}))
