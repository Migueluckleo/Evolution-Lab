const fs = require('fs');
const crypto = require('crypto');
const assert = require('assert/strict');
const read = p => JSON.parse(fs.readFileSync(p,'utf8'));
const final = read('qa/implementations/fuentes.v0.1.0.final.json');
const initial = read('qa/implementations/fuentes.v0.1.0.slots.json');
const before = read('implementations/figma/fuentes.v0.1.0.dot-before.json');
const pre = read('implementations/figma/fuentes.v0.1.0.preflight.json');
const ext = read('sources/inventories/ai-design-system.fuentes-hover.v0.1.0.json');
const base = read('sources/inventories/tokens.inventory.json');
const hash = crypto.createHash('sha256').update(fs.readFileSync('sources/inventories/tokens.inventory.json')).digest('hex');
assert.equal(hash,ext.canonical_base_sha256);
assert.equal(final.uniquePage,1);
assert.equal(final.structural.failed.length,0);
assert.equal(final.issues.length,0);
assert.equal(final.reactions.length,0);
assert.equal(final.paints.length,22);
for (const m of final.masters) {
 assert.equal(m.height,90); assert.ok(Math.abs(m.width-167.6666717529297)<0.01);
 assert.equal(m.minWidth,150);assert.equal(m.maxWidth,168);assert.equal(m.radius,8);
 assert.deepEqual(m.padding,[8,8,8,8]);assert.equal(m.gap,8);assert.equal(m.strokeWeight,1);
 assert.equal(m.strokeAlign,'INSIDE');assert.equal(m.strokesIncludedInLayout,true);
 assert.deepEqual(m.explicitVariableModes,{});
}
for (let i=0;i<4;i++) {
 const f=final.fixtures[i]; assert.equal(f.slot.children.length,[0,1,2,4][i]);
 assert.equal(f.slot.violations.length,0);assert.equal(f.slot.layoutWrap,'WRAP');
 for (const c of f.slot.children) assert.ok(c.width<=f.slot.width);
}
const long=final.fixtures[4];assert.equal(long.width,150);assert.equal(long.main,'848:26');
assert.ok(long.height>90);assert.ok(long.slot.children.some(c=>c.height>16));
for(const c of long.slot.children)assert.ok(c.width<=long.slot.width);
for(const t of initial.tests.filter(t=>t.pass!==undefined))assert.equal(t.pass,true,t.test);
assert.deepEqual(final.dotMain.fills,before.fills);assert.deepEqual(final.dotMain.strokes,before.strokes);
assert.equal(final.dotMain.width,before.width);assert.equal(final.dotMain.height,before.height);
const ev=ext.variables[0], fv=final.hoverVariable;
assert.equal(fv.name,ev.name);assert.equal(fv.description,ev.description);assert.deepEqual(fv.scopes,ev.scopes);
const primitives=new Map(pre.primitives.map(v=>[v.id,v]));
const canonical=base.collections.flatMap(c=>c.variables);
for(const [i,mode] of ['Contable','Administrativo','Servicios','Personas'].entries()) {
 const alias=fv.valuesByMode['6:'+i];assert.equal(alias.type,'VARIABLE_ALIAS');
 const dest=primitives.get(alias.id), expected=ev.aliasesByMode[mode];
 assert.equal(dest.name,expected.primitiveName);
 const src=canonical.find(v=>v.id===expected.primitiveId);assert.equal(src.name,expected.primitiveName);
 const srcValue=Object.values(src.valuesByMode)[0];assert.deepEqual(dest.valuesByMode['6:4'],srcValue);
 assert.equal(Object.values(final.themes[i].modes)[0],'6:'+i);
 for(const ch of ['r','g','b'])assert.ok(Math.abs(final.themes[i].fill[0].color[ch]-srcValue[ch])<1e-6);
}
console.log(JSON.stringify({status:'PASS',scope:'Saved Figma readback, structural Slots, token aliases, main Dot preservation, canonical hash',paintBindings:22,variants:2,themes:4,canonicalHash:hash,accessibility:'LIMITATIONS_DOCUMENTED',remotePublication:'NOT_PERFORMED'},null,2));
