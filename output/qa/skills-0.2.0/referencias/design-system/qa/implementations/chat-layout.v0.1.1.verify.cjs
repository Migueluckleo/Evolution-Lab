const fs = require('fs');
const crypto = require('crypto');
const read = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const base = read('sources/inventories/tokens.inventory.json');
const geo = read('qa/implementations/chat-layout.v0.1.1.observed.json');
const details = read('qa/implementations/chat-layout.v0.1.1.structure.json');
const checks = read('qa/implementations/chat-layout.v0.1.1.instances-and-spacing.json');
const errors = [], rows = new Map(geo.rows.map(r => [r[0], Object.fromEntries(geo.keys.map((k,i)=>[k,r[i]]))]));
const expect = (id,key,value) => { if(rows.get(id)?.[key] !== value) errors.push(`${id}.${key}`); };
for(const id of ['783:25','783:117']) expect(id,'maxWidth',816);
for(const id of ['783:24','783:116']) expect(id,'minWidth',574);
expect('783:24','layoutSizingVertical','HUG');
expect('783:116','layoutSizingVertical','FIXED');
expect('783:116','minHeight',null);
expect('783:126','overflowDirection','VERTICAL');
expect('783:126','clipsContent',false);
expect('797:316','layoutSizingVertical','FIXED');
expect('797:381','layoutSizingVertical','FILL');
expect('797:381','minHeight',null);
for(const id of ['784:103','784:163']) if(checks.nodes.find(n=>n.id===id)?.minWidth!==358) errors.push(id+' override');
if(details.count!==478 || details.pending!==0 || details.slots.length!==40 || details.slots.some(s=>s.limitViolations.length)) errors.push('Traversal/Slots');
const sem=base.collections.find(c=>c.name==='semantic');
const byId=new Map(base.collections.flatMap(c=>c.variables).map(v=>[v.id,v]));
const prim=new Map(checks.primitives.map(v=>[v.id,v]));
let aliases=0;
for(const v of checks.variables){
  const e=sem.variables.find(x=>x.name===v.name);
  if(!e){errors.push(v.name+' absent');continue;}
  for(const field of ['resolvedType','description','scopes']) if(JSON.stringify(e[field])!==JSON.stringify(v[field])) errors.push(v.name+'.'+field);
  for(const [mid,a]of Object.entries(v.valuesByMode)){
    const theme=['Contable','Administrativo','Servicios','Personas'][Number(mid.split(':')[1])];
    const sm=sem.modes.find(m=>m.name===theme);
    const ep=byId.get(e.valuesByMode[sm.modeId].id), ap=prim.get(a.id);
    if(!ap || ep.name!==ap.name || JSON.stringify(Object.values(ep.valuesByMode)[0])!==JSON.stringify(Object.values(ap.valuesByMode)[0])) errors.push(v.name+'/'+theme);
    aliases++;
  }
}
const canonicalSha256=crypto.createHash('sha256').update(fs.readFileSync('sources/inventories/tokens.inventory.json')).digest('hex');
if(canonicalSha256!=='cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474') errors.push('Canonical hash');
console.log(JSON.stringify({date:'2026-10-09',status:errors.length?'FAIL':'PASS',scope:'Read-only evidence consistency and five spacing definitions; not interactive overflow QA',layoutRows:geo.rows.length,traversedNodes:details.count,slots:details.slots.length,spacingDefinitions:checks.variables.length,aliases,canonicalSha256,errors},null,2));
if(errors.length)process.exitCode=1;
