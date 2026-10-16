const fs=require('fs'),crypto=require('crypto'),path=require('path'),cp=require('child_process');
const run='graphify-out/runs/2026-10-09-fuentes/';
const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const v=read(run+'verification.json'),m=read(run+'manifest-check.json'),g=read('graphify-out/graph.json'),b=read(run+'before/graph.json');
const edges=g.links||g.edges,adj=new Map(g.nodes.map(n=>[n.id,new Set()]));
for(const e of edges){adj.get(e.source).add(e.target);adj.get(e.target).add(e.source);}
const artifact=p=>g.nodes.find(n=>n.source_file===p&&n.sha256)?.id;
function route(a,b){const s=artifact(a),t=artifact(b);if(!s||!t)return [];const q=[[s]],seen=new Set([s]);for(const p of q){const n=p.at(-1);if(n===t)return p;for(const z of adj.get(n))if(!seen.has(z)){seen.add(z);q.push([...p,z]);}}return [];}
const contract='specs/components/fuentes.contract.v0.1.0.md';
const targets=['specs/foundations/fuentes-hover.contract.v0.1.0.md','sources/inventories/ai-design-system.fuentes-hover.v0.1.0.json','sources/inventories/tokens.inventory.json','drafts/contracts/fuentes.source.component-contract.md','drafts/contracts/fuentes.source.component-contract.yaml','qa/implementations/fuentes.v0.1.0.final.json','qa/implementations/fuentes.v0.1.0.slots.json','qa/implementations/fuentes.v0.1.0.contrast.json','qa/implementations/fuentes.v0.1.0.review.md','implementations/figma/fuentes.v0.1.0.state.json','registry/SESSION-HANDOFF-2026-10-09-FUENTES.md'];
const paths=targets.map(to=>({from:contract,to,path:route(contract,to)}));
const qa=JSON.parse(cp.execFileSync(process.execPath,['qa/implementations/fuentes.v0.1.0.verify.cjs'],{encoding:'utf8'}));
const errors=[];
if(v.status!=='PASS'||m.status!=='PASS'||qa.status!=='PASS')errors.push('Prior gate failed');
if(paths.some(p=>!p.path.length))errors.push('Missing Fuentes lineage');
for(const [p,h]of Object.entries(v.output_sha256))if(hash('graphify-out/'+p)!==h)errors.push('Export drift '+p);
for(const p of [contract,...targets])if(!fs.existsSync(p))errors.push('Missing source '+p);
// Only structural artifact hashes identify the containing file. Semantic
// evidence may quote the hash of a referenced historical snapshot instead.
for(const n of g.nodes)if(n.sha256&&n.extraction_scope==='file identity, explicit references; semantic entities indexed separately'&&fs.existsSync(n.source_file)&&hash(n.source_file)!==n.sha256)errors.push('Source hash drift '+n.source_file);
const extNode=g.nodes.find(n=>n.source_file==='sources/inventories/ai-design-system.fuentes-hover.v0.1.0.json'&&n.aliasesByMode);
if(!extNode||Object.keys(extNode.aliasesByMode).length!==4)errors.push('Missing four brand aliases in graph');
if(extNode){const neighbors=[...adj.get(extNode.id)].map(id=>g.nodes.find(n=>n.id===id));for(const brand of ['blue','green','orange','purple'])if(!neighbors.some(n=>n.label==='color/'+brand+'/100'))errors.push('Missing primitive link '+brand);}
for(const p of [contract,'specs/foundations/fuentes-hover.contract.v0.1.0.md']){const text=fs.readFileSync(p,'utf8');for(const hit of text.matchAll(/\[[^\]]*\]\(([^)]+)\)/g))if(!/^\w+:/.test(hit[1])&&!fs.existsSync(path.resolve(path.dirname(p),hit[1].split('#')[0])))errors.push('Broken spec link '+hit[1]);}
const out={date:new Date().toISOString(),status:errors.length?'FAILED':'CURRENT',errors,graph:{nodes:g.nodes.length,edges:edges.length,nodeDelta:g.nodes.length-b.nodes.length,edgeDelta:edges.length-(b.links||b.edges).length,corpusFiles:v.corpus_files},scopedPaths:paths,qaReadback:qa,sourceSha256:Object.fromEntries([contract,...targets].map(p=>[p,hash(p)])),outputSha256:v.output_sha256,sourceLinkLimitations:v.source_link_limitations.length,scope:'Full derived corpus freshness, Fuentes contract/token/QA lineage; not human approval, remote publication or whole-library Figma revalidation'};
fs.writeFileSync(run+'closure.json',JSON.stringify(out,null,2));console.log(JSON.stringify({status:out.status,errors,graph:out.graph,paths:paths.length,sourceLinkLimitations:out.sourceLinkLimitations}));if(errors.length)process.exitCode=1;
