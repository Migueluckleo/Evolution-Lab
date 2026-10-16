
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
 const preserve=clean({characters:n.characters,textCase:n.textCase,textDecoration:n.textDecoration,fills:segs.map(s=>s.fills),hyperlinks:segs.map(s=>s.hyperlink),paragraphSpacing:n.paragraphSpacing,paragraphIndent:n.paragraphIndent,props:n.componentPropertyReferences,ancestors,visible:n.visible,textAutoResize:n.textAutoResize,textAlignHorizontal:n.textAlignHorizontal,textAlignVertical:n.textAlignVertical});
 return [n.id.split(';').map(x=>intern(x,paths,pi)),intern(n.name,names,ni),vis?1:0,n.width,n.height,r,hash(preserve),owner||'',n.textAutoResize,hash(n.characters)];
});
const components=page.findAllWithCriteria({types:['COMPONENT','COMPONENT_SET']}).map(n=>({id:n.id,name:n.name,type:n.type,parentId:n.parent.id}));
const payload=JSON.stringify({schema_version:2,page:{id:page.id,name:page.name},columns:['idParts','nameIndex','effectiveVisible','width','height','segments','preservationHash','ownerComponentId','textAutoResize','charactersHash'],paths,names,recipes,nodes,components});
const part=PART_INDEX;
return {page:{id:page.id,name:page.name},nodes:nodes.length,recipes:recipes.length,parts:Math.ceil(payload.length/14500),part,payload:payload.slice(part*14500,(part+1)*14500)};

