// Read-only API evidence. CFG and PART_INDEX are literal inputs. Never derives IDs from suffixes.
figma.skipInvisibleInstanceChildren=false;
const page=await figma.getNodeByIdAsync(CFG.pageId);
if(page?.type!=='PAGE')throw Error('Missing exact page');
await figma.setCurrentPageAsync(page);
// Materialize real descendants before addressing virtual instance-text IDs.
const liveTexts=new Map(page.findAllWithCriteria({types:['TEXT','TEXT_PATH']}).map(n=>[n.id,n]));
const clean=x=>JSON.parse(JSON.stringify(x,(_,v)=>typeof v==='symbol'?'MIXED':v));
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const fields=['fontName','fontWeight','fontSize','lineHeight','letterSpacing','textStyleId','textStyleOverrides','boundVariables','textDecoration','textCase','fills','hyperlink','paragraphSpacing','paragraphIndent'];
const nodes={},textRecords={},routes=[],issues=[],recipeKeys=new Map(),recipes=[],mainCache=new Map(),routeSeen=new Set(),textSeen=new Set();
const intern=x=>{const k=JSON.stringify(x);if(recipeKeys.has(k))return recipeKeys.get(k);const i=recipes.length;recipeKeys.set(k,i);recipes.push(x);return i;};
async function mainOf(n){if(!mainCache.has(n.id))mainCache.set(n.id,await n.getMainComponentAsync());return mainCache.get(n.id);}
async function remember(n){if(!n||n.type==='DOCUMENT'||nodes[n.id])return;const row={id:n.id,type:n.type,name:n.name,parentId:n.parent?.id||null};nodes[n.id]=row;
 if(n.type!=='PAGE'){row.visible=n.visible;row.componentPropertyReferences=clean(n.componentPropertyReferences);}
 if(n.type==='INSTANCE'){const m=await mainOf(n);row.mainComponentId=m?.id||null;row.scaleFactor=n.scaleFactor;row.overrides=clean(n.overrides);if(m)await remember(m);}
}
function pathBetween(root,leaf){const steps=[];let n=leaf;while(n&&n.id!==root.id){const p=n.parent;if(!p||!('children'in p))return null;const index=p.children.findIndex(c=>c.id===n.id);if(index<0)return null;steps.push(index);n=p;}return n?steps.reverse():null;}
const pending=CFG.targets.map(t=>({id:t.nodeId,node:liveTexts.get(t.nodeId)}));
for(let qi=0;qi<pending.length;qi++){
 if(pending.length>2000)throw Error('Unbounded counterpart traversal');
 const {id,node:t}=pending[qi];if(textSeen.has(id))continue;textSeen.add(id);
 if(!t||!['TEXT','TEXT_PATH'].includes(t.type)){issues.push({code:'MISSING_TEXT',nodeId:id});continue;}
 await remember(t);
 const segments=t.characters.length?t.getStyledTextSegments(fields):[{start:0,end:0,...Object.fromEntries(fields.map(k=>[k,t[k]]))}];
 textRecords[id]={width:t.width,height:t.height,textAutoResize:t.textAutoResize,characters:t.characters,segments:segments.map(s=>[s.start,s.end,intern(clean(Object.fromEntries(fields.map(k=>[k,s[k]]))))]),ancestorIds:[],terminalPrincipal:true};
 for(let p=t.parent;p&&p.type!=='DOCUMENT';p=p.parent){
  await remember(p);textRecords[id].ancestorIds.push(p.id);if(p.type!=='INSTANCE')continue;textRecords[id].terminalPrincipal=false;
  const key=t.id+'@'+p.id;if(routeSeen.has(key))continue;routeSeen.add(key);
  const path=pathBetween(p,t),m=await mainOf(p);const route={textId:t.id,instanceId:p.id,mainId:m?.id||null,path,pairs:[],status:'OBSERVED'};routes.push(route);
  if(!m||!path){route.status='UNRESOLVED';issues.push({code:'MISSING_MAIN_OR_REAL_CHILD_PATH',textId:t.id,instanceId:p.id});continue;}
  let a=p,b=m;
  for(const index of path){
   const ai='children'in a?a.children[index]:null,bi='children'in b?b.children[index]:null;
   if(!ai||!bi){route.status='UNRESOLVED';issues.push({code:'COUNTERPART_PATH_MISSING',textId:t.id,instanceId:p.id,index,instanceParentId:a.id,mainParentId:b.id});break;}
   await remember(ai);await remember(bi);
   route.pairs.push({index,instanceChildId:ai.id,mainChildId:bi.id,typeMatches:ai.type===bi.type,nameMatches:ai.name===bi.name,propertyReferencesMatch:equal(clean(ai.componentPropertyReferences),clean(bi.componentPropertyReferences))});
   if(ai.type!==bi.type){route.status='UNRESOLVED';issues.push({code:'COUNTERPART_TYPE_MISMATCH',textId:t.id,instanceId:p.id});break;}
   a=ai;b=bi;
  }
  if(route.status==='OBSERVED'&&['TEXT','TEXT_PATH'].includes(b.type)){route.counterpartTextId=b.id;pending.push({id:b.id,node:b});}
  else if(route.status==='OBSERVED'){route.status='UNRESOLVED';issues.push({code:'COUNTERPART_NOT_TEXT',textId:t.id,instanceId:p.id});}
 }
}
const counts={targetTexts:CFG.targets.length,capturedTargets:CFG.targets.filter(t=>textRecords[t.nodeId]).length,allTexts:Object.keys(textRecords).length,apiNodes:Object.keys(nodes).length,mainRoutes:routes.length,blankTargetRanges:0,nonblankTargetRanges:0,unresolvedRoutes:routes.filter(r=>r.status!=='OBSERVED').length};
for(const t of CFG.targets)for(const s of textRecords[t.nodeId]?.segments||[])counts[recipes[s[2]].textStyleId===''?'blankTargetRanges':'nonblankTargetRanges']++;
// Lossless dictionary transport for core evidence; componentProperties/preferredValues are deliberately omitted.
const ids=[],idIndex=new Map(),strings=[],stringIndex=new Map(),objects=[],objectIndex=new Map();
const ix=(v,arr,map)=>{if(v===null||v===undefined)return null;const key=typeof v==='object'?JSON.stringify(v):v;if(map.has(key))return map.get(key);const i=arr.length;arr.push(v);map.set(key,i);return i;};
const ID=v=>ix(v,ids,idIndex),STR=v=>ix(v,strings,stringIndex),OBJ=v=>ix(v,objects,objectIndex);
const nodeRows=Object.values(nodes).map(n=>[ID(n.id),STR(n.type),STR(n.name),ID(n.parentId),n.visible??null,OBJ(n.componentPropertyReferences),ID(n.mainComponentId),n.scaleFactor??null,OBJ(n.overrides)]);
const textRows=Object.entries(textRecords).map(([id,t])=>[ID(id),t.width,t.height,STR(t.textAutoResize),STR(t.characters),t.segments,t.ancestorIds.map(ID),t.terminalPrincipal]);
const routeRows=routes.map(r=>[ID(r.textId),ID(r.instanceId),ID(r.mainId),r.path,r.pairs.map(p=>[p.index,ID(p.instanceChildId),ID(p.mainChildId),p.typeMatches,p.nameMatches,p.propertyReferencesMatch]),STR(r.status),ID(r.counterpartTextId)]);
const payload=JSON.stringify({schema_version:2,kind:'SCALED_INHERITANCE_API_SUPPLEMENT',page:{id:page.id,name:page.name},mappingSha256:CFG.mappingSha256,policy:'OBSERVED only; actual parents/children/getMainComponentAsync. No suffix reconstruction or scale product. ComponentProperties/preferredValues omitted; full direct instance overrides and text recipes retained.',targetIds:CFG.targets.map(t=>ID(t.nodeId)),counts,columns:{nodes:['id','typeString','nameString','parentId','visible','referencesObject','mainId','scaleFactor','overridesObject'],texts:['id','width','height','textAutoResizeString','charactersString','segments','ancestorIds','terminalPrincipal'],routes:['textId','instanceId','mainId','path','pairs','statusString','counterpartTextId'],pairs:['index','instanceChildId','mainChildId','typeMatches','nameMatches','propertyReferencesMatch']},ids,strings,objects,nodes:nodeRows,texts:textRows,recipes,routes:routeRows,issues});
const fingerprint=s=>{let a=2166136261,b=5381;for(let i=0;i<s.length;i++){const c=s.charCodeAt(i);a=Math.imul(a^c,16777619)>>>0;b=(Math.imul(b,33)^c)>>>0;}return a.toString(36)+'.'+b.toString(36);};
const parts=Math.ceil(payload.length/14500);if(!Number.isInteger(PART_INDEX)||PART_INDEX<0||PART_INDEX>=parts)throw Error('Invalid part index');
return{captureVersion:'inheritance-api-v3',page:{id:page.id,name:page.name},counts,parts,part:PART_INDEX,payloadLength:payload.length,payloadFingerprint:fingerprint(payload),payload:payload.slice(PART_INDEX*14500,(PART_INDEX+1)*14500)};
