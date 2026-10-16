"""Prepare 66 explicitly diagnosed contextual Button corrections; never call Figma.

This opt-in adapter leaves the strict shared template byte-for-byte intact.
Geometry exceptions require an explicit, evidenced before/after ledger. They
are checked as exact tuples, not as a tolerance or blanket ancestor exemption.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

from typography_prepare_range_calls import ROOT, compact, pack_expected

TEMPLATE = ROOT / 'implementations/figma/typography.v0.1.1.apply-ranges.js'
TEMPLATE_SHA = 'bd54eb1525325d744c040c7e4c410e40f980d06cf8d8bbb875ad19c0befb319a'
PAGE = '394:122'
IDS = ('I420:232;26:104', 'I420:249;26:104', 'I420:266;26:104',
       'I420:283;26:299', 'I420:299;26:104', 'I420:313;26:104')
SOURCE = 'ui-action-label-small'
TARGET = 'ui-label-compact-bold'
REPORTS = {
    PAGE: ('apply.394-122.1.range-indexed.json', 6),
    '565:122': ('apply.565-122.whole-page.detail.json', 36),
    '639:128': ('apply.639-128.whole-page.detail.json', 16),
    '765:6': ('apply.765-6.whole-page.detail.json', 8),
}
GEOMETRY_FIELDS = {'x', 'width', 'relativeTransform', 'absoluteTransform',
                   'absoluteBoundingBox', 'absoluteRenderBounds'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Pinned template anchor is not unique: ' + old[:80])
    return text.replace(old, new, 1)


def recovery_template():
    """Return a reviewed adapter of the pinned complete-page guard."""
    if sha(TEMPLATE) != TEMPLATE_SHA:
        raise ValueError('Strict template changed; independently review this adapter before use')
    text = TEMPLATE.read_text()
    text = replace_once(text, 'const clean=x=>', '''const recovery=RECOVERY_RULES;
const recoveryById=new Map(recovery.rows.map(r=>[r.id,r])),recoveryIds=new Set(recoveryById.keys()),geometryById=new Map(recovery.geometry.map(g=>[g.id,g]));
const clean=x=>''')
    text = replace_once(text, 'const errors=[],nodes=[];', '''const errors=[],nodes=[];
const rawProp=(row,key)=>{const v=row.props[key];return v&&typeof v==='object'&&Object.keys(v).length===1&&'valueRef'in v?JSON.parse(valueStrings[v.valueRef]):v;};
const geometryPhase=(row,g,phase)=>Object.entries(g.fields).every(([key,v])=>equal(rawProp(row,key),v[phase]));
const geometryCandidate=n=>n.id==='I420:299;26:104';
if(page.id!==recovery.pageId||expected.length!==recovery.rows.length||entries.length!==recovery.rows.length||recoveryIds.size!==entries.length||entries.some(e=>!recoveryIds.has(e.id)||e.segments.length!==1||e.segments[0].logical!==recoveryById.get(e.id).target))errors.push(['RECOVERY_SCOPE']);
for(const g of recovery.geometry){const row=before.get(g.id),n=await figma.getNodeByIdAsync(g.id);if(!row||!n||!geometryCandidate(n)||!geometryPhase(row,g,'before')&&!geometryPhase(row,g,'after'))errors.push([g.id,'RECOVERY_GEOMETRY_PREFLIGHT']);}
const sourceRecipe=(id,a)=>a.textStyleId===styles[recoveryById.get(id).source].figmaId&&matches(a,styles[recoveryById.get(id).source]);
const restoredRecipe=(id,a)=>a.textStyleId===styles[recoveryById.get(id).target].figmaId&&matches(a,styles[recoveryById.get(id).target]);
const recoveryDimensions=(n,e)=>n.height===e.h&&(n.width===e.w||n.id==='I420:299;26:104'&&n.width===e.w+1&&geometryById.has(n.id));
const recoveryBindings=(id,actual)=>Object.entries(actual||{}).every(([key,v])=>{
 if(!metricBindings.has(key))return true; // Retained exactly by the full-page guard, including fills.
 const target=styles[recoveryById.get(id).target].bindings[key];
 return target!==undefined&&(equal(v,target)||Array.isArray(v)&&v.length&&v.every(a=>equal(a,target)));
});''')
    old = "if(n.width!==e.w||n.height!==e.h||preserve(n)!==e.hash)errors.push([e.id,'PREFLIGHT_PRESERVATION']);for(const s of e.segments){const segs=n.getStyledTextSegments(fields,s.start,s.end);if(!segs.length||segs.some(a=>!matches(a,styles[s.logical])))errors.push([e.id,'PREFLIGHT_RECIPE',s.logical]);}"
    new = "if(!recoveryDimensions(n,e)||preserve(n)!==e.hash)errors.push([e.id,'PREFLIGHT_PRESERVATION']);for(const s of e.segments){const segs=n.getStyledTextSegments(fields,s.start,s.end);if(!segs.length||segs.some(a=>!sourceRecipe(n.id,a)&&!restoredRecipe(n.id,a)||!recoveryBindings(n.id,a.boundVariables))||!recoveryBindings(n.id,n.boundVariables))errors.push([e.id,'PREFLIGHT_RECIPE_OR_BINDING',s.logical]);}"
    text = replace_once(text, old, new)
    text = replace_once(text, 'for(const [id,a]of before){', '''const recoveryCoreEqual=(a,b)=>{
 const g=geometryById.get(a.id);
 if(!g)return exactCaptured({...a,segments:undefined,boundVariables:undefined},{...b,segments:undefined,boundVariables:undefined});
 if(!geometryPhase(a,g,'before')&&!geometryPhase(a,g,'after')||!geometryPhase(b,g,'after'))return false;
 const ac={...a,props:{...a.props},segments:undefined,boundVariables:undefined},bc={...b,props:{...b.props},segments:undefined,boundVariables:undefined};
 for(const key of Object.keys(g.fields)){delete ac.props[key];delete bc.props[key];}
 return exactCaptured(ac,bc);
};
const recoveryRecipeEqual=(id,old,now)=>{
 if(!recoveryIds.has(id)||!sourceRecipe(id,old)||!restoredRecipe(id,now))return exactCaptured(recipe(old),recipe(now));
 const a=recipe(old),b=recipe(now);delete a.letterSpacing;delete b.letterSpacing;
 return exactCaptured(a,b);
};
for(const [id,a]of before){''')
    text = replace_once(text, "if(!exactCaptured({...a,segments:undefined,boundVariables:undefined},{...b,segments:undefined,boundVariables:undefined}))", "if(!recoveryCoreEqual(a,b))")
    text = replace_once(text, "if(!exactCaptured(recipe(old),recipe(now)))", "if(!recoveryRecipeEqual(id,old,now))")
    text = replace_once(text, "checked:entries.length,mutatedNodeIds:mutated", "checked:entries.length,recovery:{scope:'EXPLICIT_DIAGNOSED_CONTEXTUAL_LABELS',rows:recovery.rows,geometryLedgerIds:recovery.geometry.map(g=>g.id),ledgerEvidence:recovery.evidence},mutatedNodeIds:mutated")
    return '// Opt-in contextual recovery. No other page exception.\n' + text


def validate_geometry(fields):
    """Only the diagnosed one-pixel horizontal restoration may be described."""
    if not fields or set(fields) - GEOMETRY_FIELDS:
        raise ValueError('Unsupported recovery geometry field')
    for key, pair in fields.items():
        if set(pair) != {'before', 'after'}:
            raise ValueError('Geometry requires an exact before/after pair')
        a, b = pair['before'], pair['after']
        if key in {'x', 'width'}:
            deltas = [b-a]
            if key == 'width' and b-a != -1:
                raise ValueError('Only the diagnosed width reduction of exactly one pixel is allowed')
        elif key.endswith('Transform'):
            if len(a) != 2 or len(b) != 2 or any(len(r) != 3 for r in a+b):
                raise ValueError('Invalid transform shape')
            if a[0][:2] != b[0][:2] or a[1] != b[1]:
                raise ValueError('Only transform translation X may change')
            deltas = [b[0][2]-a[0][2]]
        else:
            if not isinstance(a, dict) or not isinstance(b, dict) or set(a) != {'x','y','width','height'} or set(a) != set(b) or a['y'] != b['y'] or a['height'] != b['height']:
                raise ValueError('Bounds may only restore X/width')
            deltas = [b['x']-a['x'], b['width']-a['width']]
            if deltas[1] not in (0, -1):
                raise ValueError('Bounds width may only shrink by one pixel')
        if not any(deltas) or any(not isinstance(d, (int,float)) or isinstance(d,bool) or not math.isfinite(d) or abs(d) > 1 for d in deltas):
            raise ValueError('Geometry delta must be nonzero and at most one pixel horizontally')


def verify_evidence(records):
    if not records:
        raise ValueError('Missing measured geometry evidence')
    for item in records:
        path = ROOT / item['path']
        if not item.get('locator') or sha(path) != item['sha256']:
            raise ValueError('Evidence locator/hash does not match: ' + str(path))


def unwrap(path):
    value = json.loads(path.read_text())
    return json.loads(value['content'][0]['text']) if 'content' in value else value


def prepare(ledger_path, output):
    ledger = json.loads(ledger_path.read_text())
    if ledger.get('schema_version') != 1 or ledger.get('pageId') != PAGE or ledger.get('ids') != list(IDS):
        raise ValueError('Ledger must describe exactly the six diagnosed FileUpload labels, in fixed order')
    if len(ledger.get('geometry', [])) != 1 or ledger['geometry'][0]['id'] != IDS[4]:
        raise ValueError('Only the measured Success label has a geometry exception')
    verify_evidence(ledger.get('evidence'))
    for g in ledger['geometry']:
        validate_geometry(g['fields'])
    label = next((g for g in ledger['geometry'] if g['id'] == IDS[4]), None)
    if not label or label['fields'].get('width') != {'before':122,'after':121}:
        raise ValueError('Missing exact 122→121 label restoration')
    mapping_path = ROOT / 'implementations/figma/typography.v0.1.1.mapping.json'
    catalog_path = ROOT / 'specs/tokens/ai-design-system.typography.v0.1.1.json'
    qa_path = ROOT / 'implementations/figma/typography.v0.1.1.styles.qa.json'
    state_path = ROOT / 'implementations/figma/typography.v0.1.1.catalog.state.json'
    m, c, q, state = [json.loads(p.read_text()) for p in (mapping_path,catalog_path,qa_path,state_path)]
    if q['result'] != 'PASS':
        raise ValueError('Canonical style/binding QA must be PASS')
    validated = {s['styleLogicalId']:s for s in q['validatedStyles']}
    indexed_nodes = {n['nodeId']:n for n in m['nodes']}
    profiles = {}
    evidence_root = ROOT / 'qa/implementations/typography/consumption-v0.1.1'
    for page_id, (filename, count) in REPORTS.items():
        report_path = evidence_root / filename
        report = unwrap(report_path)
        if report['status'] != 'PREFLIGHT_FAILED_NO_WRITE' or report['mutatedNodeIds']:
            raise ValueError('Expected the recorded no-write preflight result')
        rows = []
        for error in report['errors']:
            if error[1] == 'PREFLIGHT_PRESERVATION' and error[0] == IDS[4] and page_id == PAGE:
                continue
            if error[1] != 'PREFLIGHT_RECIPE':
                raise ValueError('Unknown preflight error; do not broaden this recovery')
            node = indexed_nodes[error[0]]
            principal_id = node['nodeId'].split(';')[-1]
            principal = indexed_nodes[principal_id]
            if (node['pageId'] != page_id or node['fate'] != 'INSTANCE' or node['scope'] != 'UI'
                or len(node['segments']) != 1 or node['segments'][0]['styleLogicalId'] != error[2]
                or node['segments'][0].get('instanceScale',1) != 1
                or principal['pageId'] != '0:1' or principal['fate'] != 'MAIN_DIRECT'
                or len(principal['segments']) != 1):
                raise ValueError('Explicit contextual identity/source differs from the canonical mapping')
            rows.append({'id':node['nodeId'],'source':principal['segments'][0]['styleLogicalId'],
                         'target':error[2],'principalTextId':principal_id})
        if len(rows) != count or len({r['id'] for r in rows}) != count:
            raise ValueError('The fixed contextual count changed')
        if page_id == PAGE and [r['id'] for r in rows] != list(IDS):
            raise ValueError('The six FileUpload identities changed')
        profiles[page_id] = {'rows':rows,'evidence':[{'path':str(report_path.relative_to(ROOT)),
            'sha256':sha(report_path),'locator':'errors: exact diagnosed no-write identities and target recipes'}]}
    styles = {}
    needed = {r[k] for p in profiles.values() for r in p['rows'] for k in ('source','target')}
    for s in c['styles']:
        if s['id'] in needed:
            row = validated[s['id']]
            if row['styleId'] != state['styleMap'][s['id']]:
                raise ValueError('Style QA and current IDs disagree')
            styles[s['id']] = {k:s[k] for k in ('fontFamily','fontStyle','fontWeight','fontSize','lineHeight','letterSpacing','textDecoration')} | {'figmaId':row['styleId'], 'bindings':{k:{'type':'VARIABLE_ALIAS','id':v['variableId']} for k,v in row['bindings'].items()}}
    for profile in profiles.values():
        for row in profile['rows']:
            source, target = styles[row['source']], styles[row['target']]
            if source['letterSpacing'] != {'unit':'PERCENT','value':0.1} or target['letterSpacing'] != {'unit':'PIXELS','value':0} or any(source[k] != target[k] for k in ('fontFamily','fontStyle','fontWeight','fontSize','lineHeight','textDecoration')):
                raise ValueError('Only the exact existing 0.1%→0 tracking correction is supported')
    output.mkdir(parents=True,exist_ok=True)
    manifest = []
    for page_id, profile in profiles.items():
        ordered = [indexed_nodes[row['id']] for row in profile['rows']]
        needed = {row[k] for row in profile['rows'] for k in ('source','target')}
        geometry = ledger['geometry'] if page_id == PAGE else []
        evidence = profile['evidence'] + (ledger['evidence'] if page_id == PAGE else [])
        replacements = {'PAGE_ID':page_id,'PAGE_EXPECTATIONS':pack_expected(ordered),
            'STYLES':{k:v for k,v in styles.items() if k in needed},
            'ENTRIES':[[i,n['before']['width'],n['before']['height'],n['before']['preservationHash']] for i,n in enumerate(ordered)],
            'RECOVERY_RULES':{'pageId':page_id,'rows':profile['rows'],'geometry':geometry,'evidence':evidence},
            'PAGE_GUARD_METADATA':{'guardPolicy':'EXACT_66_DIAGNOSED_CONTEXTUAL_LABELS_ONLY','strictTemplateSha256':TEMPLATE_SHA,'mappingSha256':sha(mapping_path),'catalogSha256':sha(catalog_path),'styleQaSha256':sha(qa_path),'recoveryLedger':{'path':str(ledger_path),'sha256':sha(ledger_path)},'globalPostflight':'REQUIRED_NOT_EXECUTED_BY_PREPARER'}}
        code = recovery_template()
        for token, value in replacements.items():
            code = code.replace(token, compact(value))
        if len(code.encode()) > 48000:
            raise ValueError('Recovery script exceeds tool input budget')
        destination = output / (page_id.replace(':','-')+'.js')
        destination.write_text(code)
        manifest.append({'name':destination.stem,'pageId':page_id,'bytes':len(code.encode()),'sha256':sha(destination),'nodes':len(ordered),'geometryIds':[g['id'] for g in geometry]})
    (output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (output/'explicit-allowlist.json').write_text(json.dumps(profiles,indent=2)+'\n')
    return {'scripts':manifest,'nodes':sum(row['nodes'] for row in manifest)}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--ledger',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a = p.parse_args()
    print(json.dumps(prepare(a.ledger,a.output),ensure_ascii=False))
