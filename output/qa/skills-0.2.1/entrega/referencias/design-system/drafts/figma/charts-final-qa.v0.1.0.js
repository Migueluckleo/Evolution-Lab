// CHARTS-001 · read-only final implementation audit.
figma.skipInvisibleInstanceChildren=false;
const page=await figma.getNodeByIdAsync("210:122");
if(!page||page.type!=="PAGE")throw new Error("Charts page missing");
const semantic=(await figma.variables.getLocalVariablesAsync()).filter(v=>v.variableCollectionId==="VariableCollectionId:6:2");
const byId=new Map(semantic.map(v=>[v.id,v]));
const sets=["Chart Legend Label","Chart Cell","Progress Chart Item","Semi-donut Gauge"];
const mains={};for(const name of sets){const n=page.children.find(c=>c.name===name&&c.type==="COMPONENT_SET");if(!n)throw new Error("Missing set "+name);mains[name]=n;}
const header=page.children.find(c=>c.name==="Chart Header"&&c.type==="COMPONENT");if(!header)throw new Error("Missing Chart Header");
const all=page.findAll(n=>true);const paints=[],texts=[],instances=[],vectors=[],reactions=[],exceptions=[];
function kind(n){if(n.type==="TEXT")return "text";if(n.type==="VECTOR"||n.type==="RECTANGLE"||n.type==="ELLIPSE")return "shape";if(n.type==="FRAME"||n.type==="COMPONENT"||n.type==="INSTANCE")return "background";return "other";}
for(const n of all){
  if(n.type==="INSTANCE")instances.push({id:n.id,name:n.name,mainId:(await n.getMainComponentAsync())?.id,properties:n.componentProperties});
  if(n.type==="VECTOR")vectors.push({id:n.id,name:n.name,pathCount:n.vectorPaths.length,paths:n.vectorPaths.map(p=>p.data)});
  if(n.reactions?.length)reactions.push({id:n.id,count:n.reactions.length});
  if(n.type==="TEXT"){
    const bv=n.boundVariables||{};const fields=["fontFamily","fontStyle","fontSize","lineHeight","letterSpacing"];
    texts.push({id:n.id,name:n.name,chars:n.characters,wh:[n.width,n.height],font:n.fontName,size:n.fontSize,refs:n.componentPropertyReferences||{},bindings:Object.fromEntries(fields.map(k=>[k,Array.isArray(bv[k])?bv[k][0]?.id||null:bv[k]?.id||null]))});
  }
  for(const prop of ["fills","strokes"]){
    const list=n[prop];if(!Array.isArray(list))continue;
    for(const p of list){if(p.type!=="SOLID"||p.visible===false)continue;const id=p.boundVariables?.color?.id||null;const v=id?byId.get(id):null;
      const role=v?.name||null;const consumer=prop==="strokes"?"border":kind(n);
      const scope=prop==="strokes"?"STROKE_COLOR":n.type==="TEXT"?"TEXT_FILL":n.type==="FRAME"||n.type==="COMPONENT"||n.type==="INSTANCE"?"FRAME_FILL":"SHAPE_FILL";
      const category=role?.split("/")[1];
      const semanticOk=consumer==="border"?category==="border":consumer==="text"?category==="text":consumer==="background"?category==="background":consumer==="shape"?category==="shape":false;
      const scopeOk=!!v&&v.scopes.includes(scope);
      paints.push({id:n.id,nodeType:n.type,name:n.name,prop,role,variableId:id,scope,semanticOk,scopeOk});
      if(!id||!v||!semanticOk||!scopeOk)exceptions.push({id:n.id,name:n.name,prop,role,scope,semanticOk,scopeOk});
    }
  }
}
const mainCount=Object.values(mains).reduce((sum,s)=>sum+s.children.length,0)+1;
const sourceVariants=__SOURCE_VECTOR_PATHS_JSON__.variants;
const gauge=mains["Semi-donut Gauge"];
const gaugeVectors=gauge.findAll(n=>n.type==="VECTOR");
function numericTokens(s){return s.match(/[+-]?(?:\d+\.?\d*|\.\d+)(?:e[+-]?\d+)?/gi)?.map(Number)||[];}
function commandSkeleton(s){return s.replace(/[+-]?(?:\d+\.?\d*|\.\d+)(?:e[+-]?\d+)?/gi,"#");}
const pathChecks=gaugeVectors.map(n=>{const src=sourceVariants.find(v=>v.name===n.parent.name)?.vectors.find(x=>x.name===n.name);const a=src?.paths[0]?.data||"",b=n.vectorPaths[0]?.data||"";const aa=numericTokens(a),bb=numericTokens(b);return {id:n.id,name:n.name,sourceId:src?.id,byteEqual:a===b,commandEqual:commandSkeleton(a)===commandSkeleton(b),numericCountEqual:aa.length===bb.length,maxNumericDelta:aa.length===bb.length?Math.max(...aa.map((x,i)=>Math.abs(x-bb[i]))):null};});
return {page:{id:page.id,name:page.name,duplicateCount:figma.root.children.filter(p=>p.name==="Charts").length},sets:Object.fromEntries(Object.entries(mains).map(([name,s])=>[name,{id:s.id,count:s.children.length,properties:s.componentPropertyDefinitions,children:s.children.map(c=>({id:c.id,name:c.name,wh:[c.width,c.height],properties:c.variantProperties}))}])),header:{id:header.id,wh:[header.width,header.height],properties:header.componentPropertyDefinitions},mainCount,instanceCount:instances.length,instanceMainIds:[...new Set(instances.map(i=>i.mainId))],instanceTexts:instances.map(i=>i.properties["Text#210:8"]?.value),vectors:{count:vectors.length,gaugeCount:gaugeVectors.length,pathChecks},texts:{count:texts.length,incomplete:texts.filter(t=>Object.values(t.bindings).some(x=>!x))},paints:{count:paints.length,exceptions,roleCounts:paints.reduce((a,p)=>(a[p.role||"NONE"]=(a[p.role||"NONE"]||0)+1,a),{})},reactions};
