const PAGE_ID="783:6";const PART_INDEX=1;
const INCLUDE_STRUCTURE=false;const STRUCTURE_NODE_IDS=[];
// Read-only. Substitute PAGE_ID and PART_INDEX. Optional INCLUDE_STRUCTURE and
// STRUCTURE_NODE_IDS collect raw geometry/ancestor scales without interpreting
// them as effective instanceScale. Keep writes frozen across all part reads.
const page=await figma.getNodeByIdAsync(PAGE_ID);await figma.setCurrentPageAsync(page);figma.skipInvisibleInstanceChildren=false;
const clean=x=>JSON.parse(JSON.stringify(x,(_,v)=>typeof v==='symbol'?'MIXED':v));
const fields=['fontName','fontSize','fontWeight','lineHeight','letterSpacing','textStyleId','textStyleOverrides','boundVariables','textCase','textDecoration','fills','hyperlink','paragraphSpacing','paragraphIndent'];
const recipes=[], keys=new Map(), names=[], ni=new Map(), paths=[], pi=new Map();
const intern=(s,a,m)=>{if(m.has(s))return m.get(s);let i=a.length;a.push(s);m.set(s,i);return i;};
const hash=x=>{let a=2166136261,b=5381;for(const c of JSON.stringify(x)){let t=c.charCodeAt(0);a=Math.imul(a^t,16777619)>>>0;b=(Math.imul(b,33)^t)>>>0;}return a.toString(36)+'.'+b.toString(36);};
const texts=page.findAllWithCriteria({types:['TEXT','TEXT_PATH']});
const nodes=texts.map(n=>{
 let ancestors=[],p=n.parent,vis=n.visible,owner=null;
 while(p&&p.type!=='DOCUMENT'){if(p.type==='COMPONENT'&&!owner)owner=p.id;if('visible' in p&&!p.visible)vis=false;ancestors.push(p.id);p=p.parent;}
 const segs=n.characters.length?n.getStyledTextSegments(fields):[{start:0,end:0,...Object.fromEntries(fields.map(k=>[k,n[k]]))}];
 const r=segs.map(s=>{const rec=clean(Object.fromEntries(fields.map(k=>[k,s[k]])));const k=JSON.stringify(rec);let idx=keys.get(k);if(idx===undefined){idx=recipes.length;keys.set(k,idx);recipes.push(rec);}return [s.start,s.end,idx];});
 // This preservation algorithm and its input object are byte-identical to the
 // historical audit. New evidence remains outside that fingerprint.
 const preserve=clean({characters:n.characters,textCase:n.textCase,textDecoration:n.textDecoration,fills:segs.map(s=>s.fills),hyperlinks:segs.map(s=>s.hyperlink),paragraphSpacing:n.paragraphSpacing,paragraphIndent:n.paragraphIndent,props:n.componentPropertyReferences,ancestors,visible:n.visible,textAutoResize:n.textAutoResize,textAlignHorizontal:n.textAlignHorizontal,textAlignVertical:n.textAlignVertical});
 return [n.id.split(';').map(x=>intern(x,paths,pi)),intern(n.name,names,ni),vis?1:0,n.width,n.height,r,hash(preserve),owner||'',n.textAutoResize,hash(n.characters)];
});
const components=page.findAllWithCriteria({types:['COMPONENT','COMPONENT_SET']}).map(n=>({id:n.id,name:n.name,type:n.type,parentId:n.parent.id}));
const includeStructure=typeof INCLUDE_STRUCTURE!=='undefined'&&INCLUDE_STRUCTURE===true;
const structureIds=typeof STRUCTURE_NODE_IDS!=='undefined'?new Set(STRUCTURE_NODE_IDS):null;
const structure=includeStructure?texts.filter(n=>!structureIds||structureIds.has(n.id)).map(n=>{
 let ancestors=[],p=n.parent;
 while(p&&p.type!=='DOCUMENT'){
  ancestors.push(clean({id:p.id,type:p.type,parentId:p.parent?.id,
   visible:p.type==='PAGE'?null:p.visible,width:p.type==='PAGE'?null:p.width,height:p.type==='PAGE'?null:p.height,
   scaleFactor:p.type==='INSTANCE'?p.scaleFactor:null,
   relativeTransform:p.type==='PAGE'?null:p.relativeTransform,absoluteTransform:p.type==='PAGE'?null:p.absoluteTransform}));
  p=p.parent;
 }
 return clean({nodeId:n.id,parentId:n.parent?.id,x:n.x,y:n.y,width:n.width,height:n.height,
  relativeTransform:n.relativeTransform,absoluteTransform:n.absoluteTransform,absoluteBoundingBox:n.absoluteBoundingBox,
  hasMissingFont:n.hasMissingFont,componentPropertyReferences:n.componentPropertyReferences,ancestors});
}):undefined;
const payload=JSON.stringify({schema_version:2,page:{id:page.id,name:page.name},columns:['idParts','nameIndex','effectiveVisible','width','height','segments','preservationHash','ownerComponentId','textAutoResize','charactersHash'],paths,names,recipes,nodes,components,
 ...(includeStructure?{structuralEvidence:{policy:'Raw ancestor scaleFactor values; no product or effective instanceScale inferred.',nodes:structure}}:{})});
const fingerprint=s=>{let a=2166136261,b=5381;for(const c of s){const t=c.charCodeAt(0);a=Math.imul(a^t,16777619)>>>0;b=(Math.imul(b,33)^t)>>>0;}return a.toString(36)+'.'+b.toString(36);};
const part=PART_INDEX;
if(!Number.isInteger(part)||part<0||part>=Math.ceil(payload.length/14500))throw new Error('Invalid capture part index');
return {captureVersion:'0.1.1',page:{id:page.id,name:page.name},nodes:nodes.length,recipes:recipes.length,
 parts:Math.ceil(payload.length/14500),part,payloadLength:payload.length,payloadFingerprint:fingerprint(payload),
 structureIncluded:includeStructure,payload:payload.slice(part*14500,(part+1)*14500)};
