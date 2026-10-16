const fs = require('node:fs');
const crypto = require('node:crypto');
const bytes = fs.readFileSync('sources/inventories/tokens.inventory.json');
const digest = crypto.createHash('sha256').update(bytes).digest('hex');
const inventory = JSON.parse(bytes);
const semantic = inventory.collections.find(c => c.name === 'semantic');
const all = inventory.collections.flatMap(c => c.variables);
const actual = JSON.parse(fs.readFileSync('sources/figma-snapshots/select.target-tokens.v0.1.0.json'));
const errors = [];
if (digest !== 'cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474') errors.push('Inventory digest changed');
function equal(a,b) {
  if (typeof a === 'number' && typeof b === 'number') return Math.abs(a-b) < 0.000001;
  if (a && b && typeof a === 'object' && typeof b === 'object') return Object.keys(a).every(k=>equal(a[k],b[k])) && Object.keys(b).every(k=>k in a);
  return a === b;
}
for (const v of actual.variables) {
  const ref = semantic.variables.find(x=>x.name===v.name);
  if (!ref) { errors.push(`${v.name}: missing canonical semantic token`); continue; }
  if (v.type!==ref.resolvedType || !equal(v.scopes,ref.scopes) || v.description!==ref.description) errors.push(`${v.name}: metadata mismatch`);
  if (v.values.length !== semantic.modes.length) errors.push(`${v.name}: mode count`);
  for (let i=0;i<semantic.modes.length;i++) {
    let value=ref.valuesByMode[semantic.modes[i].modeId]; const chain=[];
    while (value && value.type==='VARIABLE_ALIAS') {
      const primitive=all.find(p=>p.id===value.id);
      if (!primitive) throw new Error(`Missing canonical alias ${value.id}`);
      chain.push(primitive.name); value=Object.values(primitive.valuesByMode)[0];
    }
    if (!equal(chain,v.values[i].chain.map(x=>x.name)) || !equal(value,v.values[i].value)) errors.push(`${v.name}: alias/value mismatch ${semantic.modes[i].name}`);
  }
}
console.log(JSON.stringify({status:errors.length?'FAIL':'PASS',digest,roles:actual.variables.length,modeChecks:actual.variables.length*4,errors},null,2));
process.exitCode=errors.length?1:0;
