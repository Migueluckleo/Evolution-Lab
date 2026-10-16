// Read-only paint audit. Adapted from buttons.local-bindings.v0.2.2.snapshot.js.
// Caller supplies PAGE_ID and ROOT_IDS. All descendants, including hidden content, are inspected.
function fingerprint(value){const s=JSON.stringify(value);let h=2166136261;for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return (h>>>0).toString(16)+':'+s.length;}
figma.skipInvisibleInstanceChildren=false;
await figma.setCurrentPageAsync(await figma.getNodeByIdAsync(PAGE_ID));
const vars={},colls={},groups={},roots=[],errors=[];
async function variable(id){if(!vars[id]){const v=await figma.variables.getVariableByIdAsync(id);if(!v)throw Error('Missing variable '+id);vars[id]=v;}return vars[id];}
async function resolve(id,mode,seen=[]){if(seen.includes(id))throw Error('Alias cycle '+id);const v=await variable(id);if(!colls[v.variableCollectionId])colls[v.variableCollectionId]=await figma.variables.getVariableCollectionByIdAsync(v.variableCollectionId);const c=colls[v.variableCollectionId];const m=c.modes.find(x=>x.name===mode)||c.modes.find(x=>x.modeId===c.defaultModeId)||c.modes[0];const a=v.valuesByMode[m.modeId];return a&&a.type==='VARIABLE_ALIAS'?resolve(a.id,mode,[...seen,id]):a;}
const rgb=x=>x&&typeof x.r==='number'?['r','g','b'].map(k=>Math.round(x[k]*255).toString(16).padStart(2,'0')).join('').toUpperCase():x;
for(const id of ROOT_IDS){const root=await figma.getNodeByIdAsync(id);if(!root)throw Error('Missing root '+id);const nodes=[root,...root.findAll(()=>true)];const geometry=[],api=[];
 for(const n of nodes){geometry.push([n.id,n.name,n.type,n.parent.id,...['x','y','width','height','visible','opacity','layoutMode','itemSpacing','paddingTop','paddingBottom','paddingLeft','paddingRight'].map(k=>k in n?n[k]:null)]);api.push([n.id,...['componentPropertyReferences','componentProperties','variantProperties','reactions'].map(k=>k in n?n[k]:null)]);
  if(n===root&&n.type==='COMPONENT_SET')continue;
  let visible=true;let p=n;while(p&&p.type!=='PAGE'){if('visible'in p&&!p.visible)visible=false;p=p.parent;}
  for(const field of ['fills','strokes']){if(!(field in n)||!Array.isArray(n[field]))continue;for(let index=0;index<n[field].length;index++){const paint=n[field][index];if(paint.type!=='SOLID'||paint.visible===false||paint.opacity===0)continue;const vid=paint.boundVariables?.color?.id;const v=vid?await variable(vid):null;const colors=vid?await Promise.all(['Contable','Administrativo','Servicios','Personas'].map(async m=>rgb(await resolve(vid,m)))):[rgb(paint.color)];const key=JSON.stringify([n.type,n.type==='COMPONENT'?'variant':n.name,field,v?.name||null,colors,visible,paint.opacity??1]);if(!groups[key])groups[key]={kind:n.type,name:n.name,field,variableId:vid||null,variable:v?.name||null,scopes:v?.scopes||[],remote:v?.remote||false,colors,visible,opacity:paint.opacity??1,consumers:[]};groups[key].consumers.push([n.id,index]);}
  }
 }
 roots.push({id:root.id,name:root.name,nodeCount:nodes.length,geometry:fingerprint(geometry),api:fingerprint(api),definitions:root.type==='COMPONENT_SET'?root.children.map(n=>[n.id,n.name,n.width,n.height]):[[root.id,root.name,root.width,root.height]],properties:fingerprint(root.componentPropertyDefinitions)});
}
return {pageId:PAGE_ID,roots,groups:Object.values(groups),variables:Object.values(vars).map(v=>({id:v.id,name:v.name,collection:v.variableCollectionId,remote:v.remote})),errors};
