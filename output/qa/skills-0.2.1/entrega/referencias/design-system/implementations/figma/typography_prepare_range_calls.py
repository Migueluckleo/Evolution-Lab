"""Prepare strictly guarded page batches; never writes to Figma itself."""
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def pack_expected(nodes):
    """Lossless interned ID segments/ranges, with shared path prefixes."""
    logical = sorted({s['styleLogicalId'] for n in nodes for s in n['segments']})
    indexes = {name: i for i, name in enumerate(logical)}
    rows, previous, paths, ranges = [], [], [], []
    path_index, range_index = {}, {}
    for node in nodes:
        parts = []
        for part in node['nodeId'].split(';'):
            if part not in path_index:
                path_index[part] = len(paths)
                paths.append(part)
            parts.append(path_index[part])
        recipe = [[s['start'], s['end'], indexes[s['styleLogicalId']]] for s in node['segments']]
        recipe_key = compact(recipe)
        if recipe_key not in range_index:
            range_index[recipe_key] = len(ranges)
            ranges.append(recipe)
        prefix = 0
        while prefix < min(len(previous), len(parts)) and previous[prefix] == parts[prefix]:
            prefix += 1
        rows.append([prefix, *parts[prefix:], range_index[recipe_key]])
        previous = parts
    return {'logical': logical, 'paths': paths, 'ranges': ranges, 'rows': rows}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--page-id', action='append', help='Generate only these pages')
    ap.add_argument('--guard-metadata', type=Path, help='External global preflight provenance; attached verbatim, never treated as global postflight proof')
    a = ap.parse_args()
    m=json.loads((ROOT/'implementations/figma/typography.v0.1.1.mapping.json').read_text())
    c=json.loads((ROOT/'specs/tokens/ai-design-system.typography.v0.1.1.json').read_text())
    state=json.loads((ROOT/'implementations/figma/typography.v0.1.1.catalog.state.json').read_text())
    tpl=(ROOT/'implementations/figma/typography.v0.1.1.apply-ranges.js').read_text()
    qa=json.loads((ROOT/'implementations/figma/typography.v0.1.1.styles.qa.json').read_text())
    if qa['result'] != 'PASS':
        raise ValueError('Canonical style/binding QA must be PASS')
    validated={s['styleLogicalId']:s for s in qa['validatedStyles']}
    global_manifest=json.loads(a.guard_metadata.read_text()) if a.guard_metadata else None
    provenance={
        'mappingSha256':hashlib.sha256((ROOT/'implementations/figma/typography.v0.1.1.mapping.json').read_bytes()).hexdigest(),
        'catalogSha256':hashlib.sha256((ROOT/'specs/tokens/ai-design-system.typography.v0.1.1.json').read_bytes()).hexdigest(),
        'styleQaSha256':hashlib.sha256((ROOT/'implementations/figma/typography.v0.1.1.styles.qa.json').read_bytes()).hexdigest(),
        'guardPolicy':'STRICT_PAGE_PRESERVATION_NO_INHERITED_GEOMETRY_EXCEPTION',
        'globalPreflight':{'path':str(a.guard_metadata),'sha256':hashlib.sha256(a.guard_metadata.read_bytes()).hexdigest(),
                           'counts':{key:global_manifest[key] for key in ('pages','nodes','texts') if key in global_manifest}} if a.guard_metadata else None,
        'globalPostflight':'REQUIRED_NOT_EXECUTED_BY_PREPARER',
    }
    a.output.mkdir(parents=True,exist_ok=True)
    manifest=[]
    for page in m['pages']:
        pid=page.get('pageId',page.get('id'))
        if a.page_id and pid not in a.page_id:
            continue
        ns=[n for n in m['nodes'] if n['pageId']==pid and n['scope']=='UI' and not any(s.get('instanceScale',1)!=1 for s in n['segments'])]
        packed_nodes=sorted(ns,key=lambda n:n['nodeId'])
        packed=pack_expected(packed_nodes)
        packed_index={n['nodeId']:i for i,n in enumerate(packed_nodes)}
        ids=set(packed['logical'])
        styles={}
        for s in c['styles']:
            if s['id'] not in ids:
                continue
            record=validated[s['id']]
            if record['styleId'] != state['styleMap'][s['id']]:
                raise ValueError('Style QA ID differs from current mapping: '+s['id'])
            styles[s['id']]={k:s[k] for k in ['fontFamily','fontStyle','fontWeight','fontSize','lineHeight','letterSpacing','textDecoration']} | {
                'figmaId':record['styleId'],
                'bindings':{field:{'type':'VARIABLE_ALIAS','id':binding['variableId']} for field,binding in record['bindings'].items()},
            }
        # Every batch carries the full page allowlist. Batch size does not narrow
        # the preservation guard or serve as a workaround for an approval denial.
        for j in range(0,len(ns),180):
            entries=[[packed_index[n['nodeId']],n['before']['width'],n['before']['height'],n['before']['preservationHash']] for n in ns[j:j+180]]
            replacements={'PAGE_ID':pid,'PAGE_EXPECTATIONS':packed,'PAGE_GUARD_METADATA':provenance,'ENTRIES':entries,'STYLES':styles}
            code=tpl
            for token,value in replacements.items():
                code=code.replace(token,compact(value))
            name=pid.replace(':','-')+('.'+str(j//180) if len(ns)>180 else '')
            if len(code.encode())>48000:raise ValueError('Oversized tool script: '+name)
            (a.output/(name+'.js')).write_text(code)
            manifest.append({'name':name,'pageId':pid,'nodes':len(entries),'pageMappedUI':len(ns),'pageGuard':'ALL_NODES_AND_TEXTS','bytes':len(code.encode()),'sha256':hashlib.sha256(code.encode()).hexdigest()})
    (a.output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'scripts':len(manifest),'nodes':sum(x['nodes']for x in manifest)}))
if __name__=='__main__':main()
