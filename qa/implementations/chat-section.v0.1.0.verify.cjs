const fs=require('fs'),crypto=require('crypto');
const read=p=>JSON.parse(fs.readFileSync(p));
const base=read('sources/inventories/tokens.inventory.json'),pre=read('implementations/figma/chat-section.v0.1.0.preflight.json'),qa=read('qa/implementations/chat-section.v0.1.0.final.json'),cleanup=read('qa/implementations/chat-section.v0.1.0.cleanup.json');
const identities=read('specs/tokens/ai-design-system.character-identity.v0.1.0.json');
const paths=['specs/tokens/ai-design-system.six-family-color.v0.1.0.json','drafts/foundations/ai-design-system.dot-background-colors.v0.1.0.json'];
const exts=paths.flatMap(p=>read(p).variables.map(v=>({...v,source:p}))),sem=base.collections.find(c=>c.name==='semantic'),prim=base.collections.find(c=>c.name==='primitive'),byId=new Map(base.collections.flatMap(c=>c.variables).map(v=>[v.id,v]));
const vars=[...pre.variables,...cleanup.dependencyVariables],prims=new Map([...pre.primitives,...cleanup.primitives].map(v=>[v.id,v]));
let errors=[],aliases=0;
for(const v of vars){const e=exts.find(x=>x.name===v.name)||sem.variables.find(x=>x.name===v.name);if(!e){errors.push(v.name+' undefined');continue;}
for(const k of ['description','resolvedType'])if(e[k]!==v[k])errors.push(v.name+': '+k);
if(JSON.stringify([...e.scopes].sort())!==JSON.stringify([...v.scopes].sort()))errors.push(v.name+': scopes');
for(const [id,a]of Object.entries(v.valuesByMode)){const mode=['Contable','Administrativo','Servicios','Personas'][Number(id.split(':')[1])];const mid=sem.modes.find(m=>m.name===mode)?.modeId;const alias=e.valuesByMode[e.source?id:mid],ep=alias?.name?prim.variables.find(v=>v.name===alias.name):byId.get(alias?.id),ap=prims.get(a.id);if(!ap||!ep||ap.name!==ep.name||JSON.stringify(Object.values(ap.valuesByMode)[0])!==JSON.stringify(Object.values(ep.valuesByMode)[0]))errors.push(v.name+'/'+mode);aliases++;}}
for(const v of qa.identities){const e=identities.variables.find(x=>x.name===v.name);if(!e||JSON.stringify(Object.values(v.valuesByMode)[0])!==JSON.stringify(e.valuesByMode.Value)||v.description!==e.description||JSON.stringify(v.scopes)!==JSON.stringify(e.scopes))errors.push(v.name+' identity');}
const lum=c=>[c.r,c.g,c.b].map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((a,v,i)=>a+v*[.2126,.7152,.0722][i],0);
const val=(name,mode)=>Object.values(prims.get(vars.find(v=>v.name===name).valuesByMode[mode].id).valuesByMode)[0];
const contrast=[];for(const [i,theme]of ['Contable','Administrativo','Servicios','Personas'].entries())for(const [foreground,background]of [['color/text/brand','color/background/default'],['color/text/brand','color/surface/brand'],['color/text/brand','color/interactive/secondary/hover'],['color/text/tertiary','color/background/default']]){const a=lum(val(foreground,'6:'+i)),b=lum(val(background,'6:'+i));contrast.push({theme,foreground,background,ratio:Number(((Math.max(a,b)+.05)/(Math.min(a,b)+.05)).toFixed(3)),note:'Observed palette; not a WCAG certification'});}
console.log(JSON.stringify({status:errors.length?'FAIL':'PASS',semanticDefinitions:vars.length,aliasComparisons:aliases,identityTokens:qa.identities.length,canonicalSha256:crypto.createHash('sha256').update(fs.readFileSync('sources/inventories/tokens.inventory.json')).digest('hex'),contrast,errors},null,2));if(errors.length)process.exitCode=1;
