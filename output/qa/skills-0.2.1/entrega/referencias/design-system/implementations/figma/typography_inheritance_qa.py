#!/usr/bin/env python3
"""Validate the closed103 native-inheritance evidence set without Figma writes.

This evidence checker does not edit/replace historical mapping or direct-ID QA.
It verifies raw transport, actual API relations, recipes/bindings and three causal
pilots. A PASS proves this evidence scope; adoption requires the named amendment.
"""
from __future__ import annotations
import argparse, copy, hashlib, json, re, sys, unittest, tempfile
from collections import Counter
from pathlib import Path
import typography_qa as qa
ROOT=Path(__file__).resolve().parents[2]
SUPPLEMENT='qa/implementations/typography/continuation-2026-10-15/typography-inheritance-supplement-v3'
QA='qa/implementations/typography/consumption-v0.1.1'
PILOTS={'5/6':('inheritance-checkbox-five-sixths','446:167','ui-body-compact','subheading-1-semibold'),'2/3':('inheritance-checkbox-two-thirds','446:207','ui-body-compact','subheading-1-semibold'),'4/3':('inheritance-count-four-thirds','I522:408;183:164','micro-count-small','ui-metric-value-small')}
TYPOGRAPHY_FIELDS={'fontName','fontFamily','fontStyle','fontWeight','fontSize','lineHeight','letterSpacing','textStyleId','textStyleOverrides','textDecoration','textCase','paragraphSpacing','paragraphIndent'}
SLOT_MAIN='456:440';SLOT_INSTANCE='I467:1052;456:440';SLOT_REF={'slotContentId':'Options#466:0'}

def load(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def need(condition,message):
    if not condition: raise ValueError(message)
def fingerprint(text):
    a,b=2166136261,5381
    encoded=text.encode('utf-16-le','surrogatepass')
    for i in range(0,len(encoded),2):
        c=int.from_bytes(encoded[i:i+2],'little');a=((a^c)*16777619)&0xffffffff;b=((b*33)^c)&0xffffffff
    def base36(n):
        s='';alphabet='0123456789abcdefghijklmnopqrstuvwxyz'
        while n:n,r=divmod(n,36);s=alphabet[r]+s
        return s or '0'
    return base36(a)+'.'+base36(b)

def assemble(directory,page):
    files=sorted(directory.glob(page+'-part-*.result.json'));need(bool(files),'Missing raw parts '+page)
    rows=[load(p) for p in files];first=rows[0]
    need(first['captureVersion']=='inheritance-api-v3','Require materialized-object audit v3')
    need([r['part'] for r in rows]==list(range(first['parts'])),'Incomplete/duplicate raw parts '+page)
    for r in rows:
        need(all(r[k]==first[k] for k in ['captureVersion','page','counts','parts','payloadLength','payloadFingerprint']),'Mixed capture cut '+page)
        need(len(r['payload'].encode('utf-16-le'))//2<=14500,'Oversized part')
    text=''.join(r['payload'] for r in rows)
    need(len(text.encode('utf-16-le'))//2==first['payloadLength'] and fingerprint(text)==first['payloadFingerprint'],'Transport fingerprint mismatch')
    data=json.loads(text);need(data==load(directory/(page+'.assembled.json')),'Assembled JSON differs from verified raw transport')
    return data,files+[directory/(page+'.assembled.json')]

def decode(data):
    need(data['schema_version']==2,'Unexpected supplement schema')
    ids,strings,objects=data['ids'],data['strings'],data['objects']
    def val(values,i):return None if i is None else values[i]
    nodes={}
    for r in data['nodes']:
        need(len(r)==9,'Unexpected node columns')
        n={'id':val(ids,r[0]),'type':val(strings,r[1]),'name':val(strings,r[2]),'parentId':val(ids,r[3]),'visible':r[4],'refs':val(objects,r[5]),'mainId':val(ids,r[6]),'scale':r[7],'overrides':val(objects,r[8])}
        need(n['id'] not in nodes,'Duplicate API node');nodes[n['id']]=n
    texts={}
    for r in data['texts']:
        need(len(r)==8,'Unexpected text columns')
        texts[ids[r[0]]]={'width':r[1],'height':r[2],'textAutoResize':strings[r[3]],'characters':strings[r[4]],'segments':[(a,b,data['recipes'][i]) for a,b,i in r[5]],'ancestors':[ids[i] for i in r[6]],'terminal':r[7]}
    routes=[]
    for r in data['routes']:
        need(len(r)==7,'Unexpected route columns')
        routes.append({'textId':val(ids,r[0]),'instanceId':val(ids,r[1]),'mainId':val(ids,r[2]),'path':r[3],'pairs':[{'index':p[0],'instanceChildId':ids[p[1]],'mainChildId':ids[p[2]],'typeMatches':p[3],'nameMatches':p[4],'refsMatch':p[5]} for p in r[4]],'status':strings[r[5]],'counterpartTextId':val(ids,r[6])})
    return {'nodes':nodes,'texts':texts,'routes':routes,'targetIds':[ids[i] for i in data['targetIds']],'issues':data['issues'],'counts':data['counts'],'page':data['page']}

def slot_boundary(route,nodes):
    for pair in route['pairs']:
        a,b=nodes[pair['instanceChildId']],nodes[pair['mainChildId']]
        if a['type']=='SLOT' or b['type']=='SLOT':
            need(a['type']==b['type']=='SLOT' and a['refs']==b['refs']==SLOT_REF,'Unproven Slot boundary')
            need(b['id']==SLOT_MAIN and pair['typeMatches'] and pair['refsMatch'],'Unknown Slot main/reference')
            return {'instanceSlotId':a['id'],'mainSlotId':b['id'],'slotContentId':SLOT_REF['slotContentId'],'policy':'Local Slot children are not identified with same-index main children; nearest interior main is authoritative.'}
    return None

def validate_structure(decoded):
    nodes,texts,routes=decoded['nodes'],decoded['texts'],decoded['routes'];classified=[]
    by_pair={(r['textId'],r['instanceId']):r for r in routes};need(len(by_pair)==len(routes),'Duplicate route')
    for tid,text in texts.items():
        parent=nodes[tid]['parentId'];instance_ancestors=[]
        for aid in text['ancestors']:
            need(aid==parent and aid in nodes,'Incomplete actual ancestor chain '+tid)
            node=nodes[aid];parent=node['parentId']
            if node['type']=='INSTANCE':instance_ancestors.append(aid);need((tid,aid) in by_pair,'Missing main route '+tid+'@'+aid)
        need(nodes[text['ancestors'][-1]]['type']=='PAGE','Ancestor chain did not reach PAGE')
        need(text['terminal']==(not instance_ancestors),'Incorrect terminal-principal label')
    for n in nodes.values():
        if n['type']!='INSTANCE':continue
        need(n['mainId'] in nodes and nodes[n['mainId']]['type']=='COMPONENT','Missing actual main record')
        need(isinstance(n['overrides'],list),'Missing direct override list')
        for override in n['overrides']:
            bad=TYPOGRAPHY_FIELDS.intersection(override['overriddenFields'])
            if 'boundVariables' in override['overriddenFields'] and override['id'] in texts:bad.add('boundVariables_on_text')
            need(not bad,'Typographic instance override '+n['id']+' -> '+override['id']+' '+','.join(sorted(bad)))
    for r in routes:
        need(nodes[r['instanceId']]['mainId']==r['mainId'],'Route main differs from API main')
        need(r['textId'] in texts and r['instanceId'] in texts[r['textId']]['ancestors'],'Route is not an actual ancestor')
        boundary=slot_boundary(r,nodes)
        if r['status']!='OBSERVED':
            need(r['status']=='UNRESOLVED' and boundary is not None,'Unresolved non-Slot main route')
            need(r['instanceId']=='467:1052' and r['mainId']=='456:421' and boundary['instanceSlotId']==SLOT_INSTANCE,'Missing path outside reviewed local Slot instance')
            matching=[i for i in decoded['issues'] if i.get('textId')==r['textId'] and i.get('instanceId')==r['instanceId']]
            need(len(matching)==1,'Missing/ambiguous raw Slot issue');issue=matching[0]
            need(issue['code']=='COUNTERPART_PATH_MISSING' and issue['instanceParentId']==SLOT_INSTANCE and issue['mainParentId']==SLOT_MAIN and issue['index'] in (5,6,7),'Unrecognized Slot path issue')
            need(r['path'][1]==issue['index'] and len(r['pairs'])==1,'Missing path does not occur immediately inside native Slot')
        elif not boundary:
            need(all(p['typeMatches'] and p['nameMatches'] and p['refsMatch'] for p in r['pairs']),'Non-Slot counterpart differs')
            need(r['counterpartTextId'] in texts,'Missing counterpart text recipe')
        if boundary:classified.append({'textId':r['textId'],'ancestorInstanceId':r['instanceId'],'rawStatus':r['status'],'classification':'NATIVE_SLOT_COMPOSITION_BOUNDARY',**boundary})
    need(len(decoded['issues'])==sum(r['status']!='OBSERVED' for r in routes),'Unclassified capture issue')
    return classified

def validate_target(node,decoded,styles,ids,style_bindings):
    nodes,texts,routes=decoded['nodes'],decoded['texts'],decoded['routes'];tid=node['nodeId'];text=texts[tid]
    ancestry=[i for i in text['ancestors'] if nodes[i]['type']=='INSTANCE'];need(ancestry,'No instance ancestor')
    nearest=ancestry[0];r=[r for r in routes if r['textId']==tid and r['instanceId']==nearest];need(len(r)==1,'Nearest route absent/ambiguous');r=r[0]
    need(r['status']=='OBSERVED' and not slot_boundary(r,nodes),'Nearest text route must reach a real main without crossing local Slot')
    need(all(p['typeMatches'] and p['nameMatches'] and p['refsMatch'] for p in r['pairs']),'Nearest real child route differs')
    out=[]
    for start,end,recipe,assignment,_ in qa.align_ranges(text['segments'],[(s['start'],s['end'],s) for s in node['segments']],[(s['start'],s['end'],s) for s in node['segments']]):
        evidence=assignment['scaleEvidence'];principal=evidence['principalTextNodeId'];base=evidence['baseStyleLogicalId'];factor=assignment['instanceScale']
        need(r['mainId']==evidence['principalComponentId'] and r['counterpartTextId']==principal,'Nearest actual principal differs from mapped evidence '+tid)
        need(texts[principal]['terminal'],'Principal still contains unresolved instance ancestry')
        need(nodes[nearest]['scale']==factor,'Actual native scale differs')
        need(recipe.get('textStyleId')=='','This exception is for the observed local-empty scope only')
        need(not qa.recipe_errors(recipe,styles[base],factor),'Resolved native recipe differs '+tid)
        need(not qa.recipe_errors(recipe,styles[assignment['styleLogicalId']],1),'Materialized derived recipe differs '+tid)
        need(recipe.get('textStyleOverrides')==assignment['beforeTextStyleOverrides']==[],'Unexpected semantic text overrides')
        need(recipe.get('boundVariables')==assignment['beforeBoundVariables'],'Changed instance text bindings')
        need(all(recipe.get(k)==v for k,v in assignment['preserveFormatting'].items()),'Changed preserved formatting')
        principal_ranges=texts[principal]['segments'];need(len(principal_ranges)==1,'Principal unexpectedly mixed')
        pr=principal_ranges[0][2];need(pr.get('textStyleId')==ids[base],'Principal lacks exact canonical base TextStyle ID')
        need(not qa.recipe_errors(pr,styles[base]) and pr.get('textStyleOverrides')==[],'Principal recipe/semantic override drift')
        need(pr.get('boundVariables')==style_bindings[ids[base]],'Principal token bindings differ from canonical style readback')
        out.append({'nodeId':tid,'start':start,'end':end,'pageId':node['pageId'],'sourceInstanceId':nearest,'principalComponentId':r['mainId'],'principalTextNodeId':principal,'baseStyleLogicalId':base,'principalTextStyleId':ids[base],'materializedStyleLogicalId':assignment['styleLogicalId'],'nativeScale':factor,'recipeScale':1,'localTextStyleId':recipe['textStyleId'],'actualChildPath':r['path'],'ancestorInstanceIds':ancestry,'principalBoundVariables':pr['boundVariables'],'instanceBoundVariables':recipe['boundVariables'],'status':'API_CHAIN_AND_RECIPE_PASS'})
    return out

def check_pilot(directory,ratio,source_id,base_id,other_id,styles,style_ids):
    data={n:load(directory/(n+'.result.json')) for n in ['read-a','set-b','read-b','restore-a','read-restored','cleanup']}
    a,b,r=[data[n] for n in ['read-a','read-b','read-restored']];ao,bo,ro=[d['observation'] for d in [a,b,r]];factor=qa.f32(int(ratio.split('/')[0])/int(ratio.split('/')[1]));checks={}
    checks['three_independent_readbacks']=all(d['status']=='READBACK_CAPTURED' and d['issues']==[] and d['createdNodeIds']==[] and d['mutatedNodeIds']==[] for d in [a,b,r]) and len({d['capturedAt'] for d in [a,b,r]})==3
    checks['original_guards_preserved']=ao['sourceGuard']==bo['sourceGuard']==ro['sourceGuard']==a['state']['baseline']['sourceGuard']
    checks['all_observation_fields_restored']=ao==ro
    checks['scale_and_main_links_stable']=ao['scale']==bo['scale']==ro['scale']==factor and ao['relationships']==bo['relationships']==ro['relationships'] and a['state']['sourceInstanceId']==source_id
    checks['controls_unchanged']=all(ao[k]==bo[k]==ro[k] for k in ['mainControl','instanceControl','instanceOverrides','propertyDefinitionsHash','copiedPropertyDefinitionsHash'])
    checks['principal_ids_exact']=ao['mainActor'][0]['textStyleId']==ro['mainActor'][0]['textStyleId']==style_ids[base_id] and bo['mainActor'][0]['textStyleId']==style_ids[other_id]
    checks['instance_ids_blank_throughout']=all(o['instanceActor'][0]['textStyleId']=='' for o in [ao,bo,ro])
    for phase,o,logical in [('A',ao,base_id),('B',bo,other_id),('RESTORED_A',ro,base_id)]:
        checks[phase+'_instance_recipe_matches_causal_style']=not qa.recipe_errors(o['instanceActor'][0],styles[logical],factor) and not qa.recipe_errors(o['mainActor'][0],styles[logical])
    writes=[(directory/(n+'.js')).read_text() for n in ['set-b','restore-a']]
    checks['write_scripts_only_actor_range_setter']=all(s.count('await c.actor.setRangeTextStyleIdAsync(')==1 and len(re.findall(r'\.setRangeTextStyleIdAsync\(',s))==1 and not re.search(r'\.(?:fontSize|lineHeight|letterSpacing|fontName|textStyleId)\s*=(?!=)',s) for s in writes)
    c=data['cleanup'];checks['cleanup_complete']=c['status']=='CLEANUP_COMPLETE' and c['errors']==[] and all(i in c['removedNodeIds'] for i in a['state']['createdRootIds'])
    need(all(checks.values()),'Causal pilot failed '+ratio+': '+','.join(k for k,v in checks.items() if not v))
    return {'ratio':ratio,'status':'CAUSAL_INHERITANCE_SUPPORTED_FOR_THIS_PILOT','sourceInstanceId':source_id,'checks':checks,'directory':str(directory.relative_to(ROOT))}

def run(root=ROOT):
    sources={};findings=[];result={'schema_version':1,'status':'BLOCKED','evidenceOnly':True,'approval':'NOT_CONFERRED','counts':{},'sources':sources,'findings':findings,'ranges':[],'slotBoundaries':[],'rawIssues':[],'pilots':[]}
    def tracked(path):
        p=root/path;sources[str(path)]=sha(p);return load(p)
    try:
        mapping=tracked(qa.CURRENT_MAPPING);catalog=tracked(qa.CURRENT_CATALOG);state=tracked(qa.CURRENT_STYLES_STATE)
        styles={s['id']:s for s in catalog['styles']};ids=state['styleMap'];style_readback=tracked(QA+'/styles.initial-description-readback.json');style_bindings={s['id']:s['boundVariables'] for s in style_readback['styles']};expected={n['nodeId']:n for n in mapping['nodes'] if any(s.get('instanceScale',1)!=1 for s in n['segments'])};need(len(expected)==103,'Scope no longer103')
        directory=root/SUPPLEMENT;captured=set();route_count=0
        for page in ['444-122','518-122','737-303']:
            raw,paths=assemble(directory,page)
            for p in paths:sources[str(p.relative_to(root))]=sha(p)
            need(raw['mappingSha256']==sources[qa.CURRENT_MAPPING],'Supplement belongs to another mapping')
            decoded=decode(raw);need(raw['counts']['capturedTargets']==raw['counts']['targetTexts'],'Incomplete targets')
            expected_page={n for n in expected if expected[n]['pageId']==raw['page']['id']};need(set(decoded['targetIds'])==expected_page,'Missing or extra page targets')
            result['slotBoundaries']+=validate_structure(decoded);result['rawIssues']+=decoded['issues'];route_count+=len(decoded['routes'])
            for nid in decoded['targetIds']:
                need(nid not in captured,'Target captured twice');captured.add(nid);result['ranges']+=validate_target(expected[nid],decoded,styles,ids,style_bindings)
        need(captured==set(expected) and len(result['ranges'])==103,'Incomplete103 range proof')
        need(len(result['rawIssues'])==6,'Reviewed Slot boundary issue count changed')
        for ratio,(name,source,base,other) in PILOTS.items():
            path=root/QA/name
            for phase in ['read-a','set-b','read-b','restore-a','read-restored','cleanup']:
                for suffix in ['.result.json','.js']:
                    p=path/(phase+suffix);sources[str(p.relative_to(root))]=sha(p)
            result['pilots'].append(check_pilot(path,ratio,source,base,other,styles,ids))
        for path in ['specs/composition-slots.amendment.v0.1.0.md',SUPPLEMENT+'/audit.js',SUPPLEMENT+'/test.cjs','implementations/figma/typography_inheritance_qa.py',qa.SCRIPT]:sources[path]=sha(root/path)
        factors=Counter(str(r['nativeScale']) for r in result['ranges']);need(factors==Counter({str(qa.f32(2/3)):14,str(qa.f32(5/6)):76,str(qa.f32(4/3)):13}),'Scale scopes changed')
        result['counts']={'targetNodes':len(captured),'ranges':len(result['ranges']),'pages':3,'actualMainRoutes':route_count,'nativeLocalEmptyRanges':103,'directLocalStyleIds':0,'terminalPrincipals':len({r['principalTextNodeId'] for r in result['ranges']}),'principalComponents':len({r['principalComponentId'] for r in result['ranges']}),'rawSlotMissingPathIssuesPreserved':6,'slotBoundaryRoutes':len(result['slotBoundaries']),'causalPilots':3,'causalChecks':36,'typographicInstanceOverrides':0,'byNativeScale':dict(factors)}
        result['status']='PASS'
    except (KeyError,ValueError,TypeError,IndexError,OSError) as error:findings.append({'code':'INHERITANCE_EVIDENCE','status':'FAIL','message':str(error)})
    result['limits']=['A PASS is scoped to103 observed ranges and3 causal experiments; local IDs remain empty.','Final consumer overlay must additionally verify current34-page selection, direct3250/editorial150 preservation, canonical79 catalogue and the explicitly active amendment.','The6 raw missing outer-main paths remain recorded; only native Slot Options content boundaries are classified, never fabricated same-index counterparts.']
    return result

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw,_=assemble(ROOT/SUPPLEMENT,'444-122');cls.data=decode(raw)
        cls.mapping=load(ROOT/qa.CURRENT_MAPPING);cls.styles={s['id']:s for s in load(ROOT/qa.CURRENT_CATALOG)['styles']};cls.ids=load(ROOT/qa.CURRENT_STYLES_STATE)['styleMap'];cls.node=next(n for n in cls.mapping['nodes'] if n['nodeId']==cls.data['targetIds'][0]);cls.bindings={s['id']:s['boundVariables'] for s in load(ROOT/QA/'styles.initial-description-readback.json')['styles']}
    def test_real_scope(self):self.assertTrue(validate_structure(copy.deepcopy(self.data)));self.assertEqual(len(validate_target(self.node,self.data,self.styles,self.ids,self.bindings)),1)
    def test_wrong_nearest_main_rejected(self):
        d=copy.deepcopy(self.data);r=next(r for r in d['routes'] if r['textId']==self.node['nodeId']);r['mainId']='wrong'
        with self.assertRaises(ValueError):validate_target(self.node,d,self.styles,self.ids,self.bindings)
    def test_typographic_override_rejected(self):
        d=copy.deepcopy(self.data);n=next(n for n in d['nodes'].values() if n['type']=='INSTANCE');n['overrides'].append({'id':self.node['nodeId'],'overriddenFields':['fontSize']})
        with self.assertRaises(ValueError):validate_structure(d)
    def test_frame_name_does_not_prove_slot(self):
        d=copy.deepcopy(self.data);d['nodes'][SLOT_INSTANCE]['type']='FRAME'
        with self.assertRaises(ValueError):validate_structure(d)
    def test_extra_binding_rejected(self):
        d=copy.deepcopy(self.data);d['texts'][self.node['nodeId']]['segments'][0][2]['boundVariables']['fontSize']={'id':'new','type':'VARIABLE_ALIAS'}
        with self.assertRaises(ValueError):validate_target(self.node,d,self.styles,self.ids,self.bindings)
    def test_missing_transport_part_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            d=Path(temp);source=ROOT/SUPPLEMENT/'444-122-part-000.result.json';(d/source.name).write_bytes(source.read_bytes())
            with self.assertRaises(ValueError):assemble(d,'444-122')
    def test_principal_binding_identity_rejected(self):
        d=copy.deepcopy(self.data);p=self.node['segments'][0]['scaleEvidence']['principalTextNodeId'];d['texts'][p]['segments'][0][2]['boundVariables']['fontFamily']['id']='same-value-wrong-variable'
        with self.assertRaises(ValueError):validate_target(self.node,d,self.styles,self.ids,self.bindings)
    def test_blank_principal_rejected(self):
        d=copy.deepcopy(self.data);p=self.node['segments'][0]['scaleEvidence']['principalTextNodeId'];d['texts'][p]['segments'][0][2]['textStyleId']=''
        with self.assertRaises(ValueError):validate_target(self.node,d,self.styles,self.ids,self.bindings)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--self-test',action='store_true');a=p.parse_args()
    if a.self_test:
        test=unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests));sys.exit(0 if test.wasSuccessful() else 1)
    result=run()
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','counts','findings']},ensure_ascii=False));sys.exit(0 if result['status']=='PASS' else 2)
