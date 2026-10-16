const fs=require('fs'),crypto=require('crypto');
const base=JSON.parse(fs.readFileSync('sources/inventories/tokens.inventory.json'));
const live=JSON.parse(fs.readFileSync('implementations/figma/chat-section.v0.1.0.preflight.json'));
const sem=base.collections.find(c=>c.name==='semantic'), byId=new Map(base.collections.flatMap(c=>c.variables).map(v=>[v.id,v]));
const prim=new Map(live.primitives.map(v=>[v.id,v]));const errors=[];let aliases=0;
for(const v of live.variables){const e=sem.variables.find(x=>x.name===v.name);if(!e){errors.push(v.name+': missing canonical');continue;}
for(const k of ['description','resolvedType'])if(v[k]!==e[k])errors.push(v.name+': '+k);
if(JSON.stringify([...e.scopes].sort())!==JSON.stringify([...v.scopes].sort()))errors.push(v.name+': scopes');
for(const [id,a]of Object.entries(v.valuesByMode)){const mode=['Contable','Administrativo','Servicios','Personas'][Number(id.split(':')[1])];const m=sem.modes.find(x=>x.name===mode);const expected=byId.get(e.valuesByMode[m.modeId].id),actual=prim.get(a.id);if(!actual||!expected||actual.name!==expected.name||JSON.stringify(Object.values(actual.valuesByMode)[0])!==JSON.stringify(Object.values(expected.valuesByMode)[0]))errors.push(v.name+'/'+mode+': alias/value');aliases++;}}
console.log(JSON.stringify({status:errors.length?'FAIL':'PASS',semanticDefinitions:live.variables.length,aliasComparisons:aliases,canonicalSha256:crypto.createHash('sha256').update(fs.readFileSync('sources/inventories/tokens.inventory.json')).digest('hex'),errors},null,2));
if(errors.length)process.exitCode=1;
