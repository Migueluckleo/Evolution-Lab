const fs = require('fs');
const crypto = require('crypto');
const inventoryPath = 'sources/inventories/tokens.inventory.json';
const bytes = fs.readFileSync(inventoryPath);
if (crypto.createHash('sha256').update(bytes).digest('hex') !== 'cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474') throw Error('Canonical JSON changed');
const inv = JSON.parse(bytes);
const sem = inv.collections.find(c => c.name === 'semantic');
const byId = new Map(inv.collections.flatMap(c => c.variables).map(v => [v.id,v]));
const actual = JSON.parse(fs.readFileSync('qa/implementations/select.v0.1.0.tokens.json'));
const modes = ['52:2','2849:0','2849:1','2849:2'];
const close = (a,b) => typeof a === 'number' && typeof b === 'number' ? Math.abs(a-b)<1e-6 : a && b && typeof a==='object' && typeof b==='object' ? Object.keys(a).every(k=>close(a[k],b[k])) && Object.keys(a).length===Object.keys(b).length : a===b;
let checks=0; const extension=[];
for(const v of actual.variables){
 const canonical=sem.variables.find(x=>x.name===v.name);
 if(!canonical){extension.push(v.name);continue;}
 if(v.type!==canonical.resolvedType || v.description!==canonical.description || JSON.stringify(v.scopes)!==JSON.stringify(canonical.scopes)) throw Error('metadata mismatch '+v.name);
 for(let i=0;i<4;i++){
  const expected=canonical.valuesByMode[modes[i]];
  const primitive=byId.get(expected.id);
  const got=v.values.find(x=>x.mode==='6:'+i);
  if(!primitive || got.alias!==primitive.name || !close(got.value,Object.values(primitive.valuesByMode)[0])) throw Error('alias/value mismatch '+v.name+' mode '+i);
  checks++;
 }
}
const baseExtension=JSON.parse(fs.readFileSync('drafts/foundations/ai-design-system.control-colors.v0.1.0.json'));
const amendment=JSON.parse(fs.readFileSync('drafts/foundations/ai-design-system.control-colors.v0.1.1.json'));
const control=actual.variables.find(v=>v.name===amendment.variableName);
const base=baseExtension.variables.find(v=>v.name===amendment.variableName);
if(control.id!==amendment.targetId || control.description!==base.description || control.type!==amendment.resolvedType || JSON.stringify(control.scopes)!==JSON.stringify(amendment.scopes)) throw Error('Extension metadata mismatch');
for(const got of control.values){
 const expected=amendment.valuesByMode[got.mode];
 const primitive=inv.collections.find(c=>c.name==='primitive').variables.find(v=>v.name===expected.name);
 if(got.alias!==expected.name || !close(got.value,Object.values(primitive.valuesByMode)[0])) throw Error('Extension alias/value mismatch');
}
const lum=hex=>{const c=hex.match(/../g).map(h=>parseInt(h,16)/255).map(x=>x<=0.04045?x/12.92:((x+0.055)/1.055)**2.4);return c[0]*0.2126+c[1]*0.7152+c[2]*0.0722;};
const contrast=(a,b)=>(Math.max(lum(a),lum(b))+0.05)/(Math.min(lum(a),lum(b))+0.05);
console.log(JSON.stringify({canonicalChecks:checks,extensionChecks:4,totalVariableModeChecks:checks+4,variables:actual.variables.length,nonConsumingPaints:actual.issues.filter(x=>x.paint.visible===false).length,contrast:{primaryOnWhite:contrast('0f172a','ffffff'),tertiaryOnWhite:contrast('64748b','ffffff'),borderOnWhite:contrast('94a3b8','ffffff')},pass:true},null,2));
