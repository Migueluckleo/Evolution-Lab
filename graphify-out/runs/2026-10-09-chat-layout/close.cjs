const fs=require('fs'),crypto=require('crypto'),path=require('path'),cp=require('child_process');
const run='graphify-out/runs/2026-10-09-chat-layout/';
const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const v=read(run+'verification.json'),m=read(run+'manifest-check.json'),g=read('graphify-out/graph.json'),b=read(run+'before/graph.json');
const edges=g.links||g.edges,adj=new Map(g.nodes.map(n=>[n.id,new Set()]));
for(const e of edges){adj.get(e.source).add(e.target);adj.get(e.target).add(e.source);}
const artifact=p=>g.nodes.find(n=>n.source_file===p&&n.sha256)?.id;
function route(a,b){const s=artifact(a),t=artifact(b);if(!s||!t)return [];const q=[[s]],seen=new Set([s]);for(const p of q){const n=p.at(-1);if(n===t)return p;for(const z of adj.get(n))if(!seen.has(z)){seen.add(z);q.push([...p,z]);}}return [];}
const amendment='specs/components/chat.layout.amendment.v0.1.1.md';
const targets=['specs/chat-section.contract.v0.1.0.md','specs/chat-toolbar.contract.v0.1.0.md','qa/implementations/chat-layout.v0.1.1.observed.json','qa/implementations/chat-layout.v0.1.1.structure.json','qa/implementations/chat-layout.v0.1.1.instances-and-spacing.json','qa/implementations/chat-layout.v0.1.1.review.md','implementations/figma/chat-layout.v0.1.1.state.json','registry/SESSION-HANDOFF-2026-10-09-CHAT-LAYOUT.md','sources/inventories/tokens.inventory.json'];
const paths=targets.map(to=>({from:amendment,to,path:route(amendment,to)}));
const qa=JSON.parse(cp.execFileSync(process.execPath,['qa/implementations/chat-layout.v0.1.1.verify.cjs'],{encoding:'utf8'}));
const errors=[];
if(v.status!=='PASS'||m.status!=='PASS'||qa.status!=='PASS')errors.push('Prior gate failed');
if(paths.some(p=>!p.path.length))errors.push('Missing Chat lineage');
for(const [p,h]of Object.entries(v.output_sha256))if(hash('graphify-out/'+p)!==h)errors.push('Export drift '+p);
for(const p of [amendment,...targets])if(!fs.existsSync(p))errors.push('Missing source '+p);
const text=fs.readFileSync(amendment,'utf8');
for(const hit of text.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)){if(!/^\w+:/.test(hit[1])&&!fs.existsSync(path.resolve(path.dirname(amendment),hit[1].split('#')[0])))errors.push('Broken amendment link '+hit[1]);}
const out={date:new Date().toISOString(),status:errors.length?'FAILED':'CURRENT',errors,graph:{nodes:g.nodes.length,edges:edges.length,nodeDelta:g.nodes.length-b.nodes.length,edgeDelta:edges.length-(b.links||b.edges).length,corpusFiles:v.corpus_files},scopedPaths:paths,qaReadback:qa,sourceSha256:Object.fromEntries([amendment,...targets].map(p=>[p,hash(p)])),outputSha256:v.output_sha256,sourceLinkLimitations:v.source_link_limitations.length,scope:'Derived graph freshness and documentation/read-only configuration QA; not interactive scroll, human approval or Figma mutation'};
fs.writeFileSync(run+'closure.json',JSON.stringify(out,null,2));console.log(JSON.stringify({status:out.status,errors,graph:out.graph,paths:paths.length,sourceLinkLimitations:out.sourceLinkLimitations}));if(errors.length)process.exitCode=1;
