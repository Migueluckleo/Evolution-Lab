import argparse,hashlib,json
from pathlib import Path
R=Path('/Users/miguel.leo/Desktop/CONTPAQi-designSystem-Optimizado');H=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('page_id',choices=['444:122','518:122','737:303']);p.add_argument('--part',type=int,default=0);a=p.parse_args()
m=R/'implementations/figma/typography.v0.1.1.mapping.json'; data=json.loads(m.read_text());targets=[]
for n in data['nodes']:
 if n['pageId']!=a.page_id:continue
 seg=[s for s in n['segments'] if s.get('instanceScale',1)!=1]
 if not seg:continue
 targets.append({'nodeId':n['nodeId'],'segments':[{'start':s['start'],'end':s['end'],'mappedStyleLogicalId':s['styleLogicalId'],'baseStyleLogicalId':s['scaleEvidence']['baseStyleLogicalId'],'principalTextNodeId':s['scaleEvidence']['principalTextNodeId'],'principalComponentId':s['scaleEvidence']['principalComponentId'],'instanceScale':s['instanceScale']} for s in seg]})
cfg={'pageId':a.page_id,'mappingSha256':hashlib.sha256(m.read_bytes()).hexdigest(),'targets':targets}
out=H/(a.page_id.replace(':','-')+f'-part-{a.part:03}.js');script='const CFG='+json.dumps(cfg,separators=(',',':'))+';\nconst PART_INDEX='+str(a.part)+';\n'+(H/'audit.js').read_text()
if out.exists() and out.read_text()!=script:raise SystemExit('Existing request differs; preserve historical script')
out.write_text(script);print(json.dumps({'script':str(out),'targets':len(targets),'part':a.part,'figmaCalls':'NOT_RUN'}))
