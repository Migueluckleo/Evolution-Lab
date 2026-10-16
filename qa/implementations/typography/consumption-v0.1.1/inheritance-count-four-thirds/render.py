#!/usr/bin/env python3
"""Prepare literal-ID Figma pilot scripts locally; never calls Figma."""
import argparse,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=Path('/Users/miguel.leo/Desktop/CONTPAQi-designSystem-Optimizado')
p=argparse.ArgumentParser();p.add_argument('operation',choices=['setup','read-a','set-b','read-b','restore-a','read-restored','cleanup']);p.add_argument('--evidence',type=Path);p.add_argument('--output',type=Path);p.add_argument('--run-tag',default='20261015-count-four-thirds-native-inheritance-03');a=p.parse_args()
state=None
if a.evidence:
 evidence=json.loads(a.evidence.read_text())
 if 'content' in evidence: raise SystemExit('Persist direct returned JSON, not an MCP wrapper')
 state=evidence.get('state')
 if a.operation=='cleanup' and not state:state={'recovery':evidence['recovery']}
 if not state:raise SystemExit('No returned state; do not guess IDs')
if a.operation!='setup' and not state:raise SystemExit('Require --evidence from successful setup, or recovery for cleanup')
catalog={s['id']:s for s in json.loads((ROOT/'specs/tokens/ai-design-system.typography.v0.1.1.json').read_text())['styles']}
ids=json.loads((ROOT/'implementations/figma/typography.v0.1.1.catalog.state.json').read_text())['styleMap']
styles={}
for key,logical in [('A','micro-count-small'),('B','ui-metric-value-small')]:
 s=catalog[logical];styles[key]={'logicalId':logical,'id':ids[logical], 'fontName':{'family':s['fontFamily'],'style':s['fontStyle']}, **{k:s[k] for k in ['fontWeight','fontSize','lineHeight','letterSpacing','textDecoration']}}
# Exact Figma readback encoding of percentage160 (Float32 ratio times100), observed in79-style QA.
import struct
f32=lambda v:struct.unpack('f',struct.pack('f',v))[0]
styles['A']['lineHeight']['value']=f32(styles['A']['lineHeight']['value']/100)*100
run=state.get('runTag',a.run_tag) if state else a.run_tag
cfg={'runTag':run,'sourceRootId':'522:408','sourceInstanceId':'I522:408;183:164','sourceMainId':'155:136','sourceActorId':'155:137','sourceControlId':'155:135','rootNames':{'owner':'TEMP typography inheritance owner '+run,'instance':'TEMP typography inheritance instance '+run},'styles':styles,'readPhase':{'read-a':'A','read-b':'B','read-restored':'RESTORED_A'}.get(a.operation),'writeTarget':'B' if a.operation=='set-b' else 'A'}
operation={'read-a':'read','read-b':'read','read-restored':'read','set-b':'set','restore-a':'set'}.get(a.operation,a.operation)
script='const CFG='+json.dumps(cfg,ensure_ascii=False,separators=(',',':'))+';\nconst STATE='+json.dumps(state,ensure_ascii=False,separators=(',',':'))+';\n'+(HERE/'common.js').read_text()+'\n'+(HERE/(operation+'.operation.js')).read_text()
out=a.output or HERE/(a.operation+'.js');out.write_text(script)
print(json.dumps({'script':str(out),'operation':a.operation,'figmaCalls':'NOT_RUN','literalIdsFrom':str(a.evidence) if a.evidence else 'runtime API source discovery','status':'LOCAL_TEMPLATE_ONLY'}))
