const fs = require('fs'), crypto = require('crypto');
const basePath = 'sources/inventories/tokens.inventory.json';
const base=JSON.parse(fs.readFileSync(basePath)), live=JSON.parse(fs.readFileSync('implementations/figma/conversation.v0.1.0.tokens-readback.json'));
const extPaths=['specs/tokens/ai-design-system.six-family-color.v0.1.0.json','drafts/foundations/ai-design-system.dot-background-colors.v0.1.0.json'];
const extensions=extPaths.flatMap(p=>JSON.parse(fs.readFileSync(p)).variables.map(v=>({...v,source:p})));
const primitive=base.collections.find(c=>c.name==='primitive');
const semantic=base.collections.find(c=>c.name==='semantic');
const byId=new Map(base.collections.flatMap(c=>c.variables).map(v=>[v.id,v]));
const byPrim=new Map(live.primitives.map(v=>[v.id,v]));
let errors=[],comparisons=0;
for(const v of live.variables){
 const e=extensions.find(x=>x.name===v.name)||semantic.variables.find(x=>x.name===v.name);
 if(!e){errors.push(v.name+': no normative definition');continue;}
 if(e.description!==v.description)errors.push(v.name+': description');
 if(JSON.stringify([...e.scopes].sort())!==JSON.stringify([...v.scopes].sort()))errors.push(v.name+': scopes');
 for(const [modeId,a] of Object.entries(v.valuesByMode)){
 const mode=['Contable','Administrativo','Servicios','Personas'][Number(modeId.split(':')[1])];
 const canonicalMode=semantic.modes.find(m=>m.name===mode)?.modeId;
 const expected=e.valuesByMode[e.source?modeId:canonicalMode]; const actual=byPrim.get(a.id);
 const expectedPrim=expected&&(expected.name?primitive.variables.find(p=>p.name===expected.name):byId.get(expected.id));
 if(!actual||!expectedPrim||actual.name!==expectedPrim.name){errors.push(v.name+'/'+mode+': alias');continue;}
 const av=Object.values(actual.values)[0],ev=Object.values(expectedPrim.valuesByMode)[0];
 if(JSON.stringify(av)!==JSON.stringify(ev))errors.push(v.name+'/'+mode+': primitive value');
 comparisons++;
 }
}
console.log(JSON.stringify({status:errors.length?'FAIL':'PASS',canonicalSha256:crypto.createHash('sha256').update(fs.readFileSync(basePath)).digest('hex'),semanticDefinitions:live.variables.length,primitiveDefinitions:live.primitives.length,aliasComparisons:comparisons,extensionSources:extPaths,errors},null,2));
