// Reproducible local evidence validation; generated manifest is not normative.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const root=path.resolve(__dirname,'../..');
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const json=p=>JSON.parse(read(p));
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex');
const families=['buttons','icon-button','breadcrumbs','metric-card','charts','linear-progress-bar'];
const errors=[],counts=[];
for(const f of families){const b=json(`qa/implementations/${f}.color.v0.1.0.before.json`),a=json(`qa/implementations/${f}.color.v0.1.0.after.json`),s=json(`qa/implementations/${f}.color.v0.1.0.source.json`);
 for(let i=0;i<a.roots.length;i++)for(const k of ['geometry','api','properties'])if(a.roots[i][k]!==b.roots[i][k])errors.push(`${f}:${k}`);
 for(const g of a.groups){const scope=g.field==='strokes'?'STROKE_COLOR':g.kind==='TEXT'?'TEXT_FILL':['FRAME','COMPONENT','INSTANCE'].includes(g.kind)?'FRAME_FILL':'SHAPE_FILL';if(!g.variableId||g.remote||!g.scopes.includes(scope))errors.push(`${f}:${g.variable}:scope/binding`);}
 const hist=d=>{const o={};for(const g of d.groups){const k=JSON.stringify([g.kind,g.field,g.colors.length===1?Array(4).fill(g.colors[0]):g.colors]);o[k]=(o[k]||0)+g.consumers.length;}return o;};
 const hs=hist(s),ha=hist(a);
 if(f==='charts'){
  const k=(kind,colors)=>JSON.stringify([kind,'fills',colors]);
  delete hs[k('RECTANGLE',Array(4).fill('D9D9D9'))];hs[k('RECTANGLE',Array(4).fill('E2E8F0'))]=4;
  for(const [kind,colors,n]of [['TEXT',Array(4).fill('0F172A'),6],['RECTANGLE',['3255F7','037255','FF5300','8300F8'],1],['RECTANGLE',['EFF3FF','ECFDF5','FFF7EC','F5F0FF'],1],['RECTANGLE',['BFCEFE','93D3BF','FFD8C8','E0CAFC'],4]])hs[k(kind,colors)]=(hs[k(kind,colors)]||0)+n;
 }
 for(const k of new Set([...Object.keys(hs),...Object.keys(ha)]))if(hs[k]!==ha[k])errors.push(`${f}:palette:${k}`);
 counts.push({family:f,paints:a.groups.reduce((n,g)=>n+g.consumers.length,0),definitions:a.roots.reduce((n,r)=>n+r.definitions.length,0)});
}
const canonical=json('qa/implementations/six-families.color.v0.1.0.canonical-after.json');
errors.push(...canonical.flatMap(x=>x.errors));
const data=json('specs/tokens/ai-design-system.six-family-color.v0.1.0.json');
if(data.variables.length!==12)errors.push('expected12roles');
if(hash('sources/inventories/tokens.inventory.json')!==data.baseInventory.sha256)errors.push('historical inventory changed');
const promoted=families.filter(f=>f!=='buttons').map(f=>`specs/${f}.contract.v0.1.0.md`);
const docs=[...promoted,'specs/components/six-family-color.amendment.v0.1.0.md','qa/implementations/six-families.color.v0.1.0.review.md'];
for(const p of docs)for(const m of read(p).matchAll(/\]\(([^)]+)\)/g)){const q=m[1].split('#')[0];if(!q||/^[a-z]+:\/\//.test(q))continue;if(!fs.existsSync(path.resolve(root,path.dirname(p),q)))errors.push(`broken link:${p}:${q}`);}
const files=new Set([...docs,'sources/inventories/tokens.inventory.json','specs/tokens/ai-design-system.six-family-color.v0.1.0.json']);
for(const dir of ['qa/implementations','implementations/figma'])for(const name of fs.readdirSync(path.join(root,dir)))if(/(?:six-famil|buttons\.color|icon-button\.color|breadcrumbs\.color|metric-card\.color|charts\.color|linear-progress-bar\.color)/.test(name)&&!name.endsWith('manifest.json'))files.add(`${dir}/${name}`);
const out={date:'2026-10-05',status:errors.length?'FAIL':'PASS',counts,errors,files:[...files].sort().map(p=>({path:p,sha256:hash(p)}))};
fs.writeFileSync(path.join(__dirname,'six-families.color.v0.1.0.manifest.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({status:out.status,counts,errors,manifestFiles:files.size}));
process.exitCode=errors.length?1:0;
