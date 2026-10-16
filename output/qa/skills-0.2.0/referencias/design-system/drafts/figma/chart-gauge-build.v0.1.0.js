// CHARTS-001 phase B · runner substitutes __SOURCE_VECTOR_PATHS_JSON__ with the
// exact array from sources/figma-snapshots/chart-donut.vector-paths.json.
figma.skipInvisibleInstanceChildren = false;
const sourcePaths = __SOURCE_VECTOR_PATHS_JSON__.variants;
if (!Array.isArray(sourcePaths) || sourcePaths.length !== 3 || sourcePaths.some(x => x.vectors?.length !== 2)) throw new Error("Source vector snapshot mismatch");
const page = await figma.getNodeByIdAsync("210:122");
if (!page || page.type !== "PAGE" || page.name !== "Charts") throw new Error("Charts page mismatch");
if (page.children.some(x => x.name === "Semi-donut Gauge")) throw new Error("Gauge exists; inspect before retry");
const tokenSpecs={track:["VariableID:208:124","color/shape/chart/track","SHAPE_FILL"],progress:["VariableID:208:123","color/shape/chart/progress","SHAPE_FILL"],text:["VariableID:13:27","color/text/primary","TEXT_FILL"],family:["VariableID:10:2","font/family/base","FONT_FAMILY"],semibold:["VariableID:10:5","font/weight/semibold","FONT_STYLE"],size:["VariableID:12:3","font/size/2xl","FONT_SIZE"],line:["VariableID:12:9","font/line-height/md","LINE_HEIGHT"],tracking:["VariableID:12:16","font/letter-spacing/normal","LETTER_SPACING"]};
const v={};for(const [k,[id,name,scope]] of Object.entries(tokenSpecs)){const t=await figma.variables.getVariableByIdAsync(id);if(!t||t.name!==name||t.variableCollectionId!=="VariableCollectionId:6:2"||!t.scopes.includes(scope))throw new Error("Token mismatch "+k);v[k]=t;}
await figma.loadFontAsync({family:"Manrope",style:"SemiBold"});
await figma.setCurrentPageAsync(page);
function solid(variable){return figma.variables.setBoundVariableForPaint({type:"SOLID",color:{r:1,g:1,b:1}},"color",variable);}
const components=[],created=[];
for(const sample of sourcePaths){
  const percent=sample.name.split("=")[1];
  const c=figma.createComponent();c.name="Progress="+percent;c.resize(283,142);c.fills=[];c.strokes=[];c.clipsContent=false;page.appendChild(c);created.push(c.id);
  for(const source of sample.vectors){
    if(source.paths.length!==1||source.paths[0].windingRule!=="NONZERO")throw new Error("Unexpected path structure "+source.id);
    const n=figma.createVector();n.name=source.name;n.vectorPaths=source.paths.map(p=>({windingRule:p.windingRule,data:p.data}));
    n.resize(source.width,source.height);n.x=source.x;n.y=source.y;n.fills=[solid(source.name==="Total"?v.track:v.progress)];n.strokes=[];c.appendChild(n);created.push(n.id);
  }
  const t=figma.createText();t.name="Percent";t.fontName={family:"Manrope",style:"SemiBold"};t.characters=percent;t.fontSize=32;
  t.lineHeight={unit:"PIXELS",value:24};t.letterSpacing={unit:"PIXELS",value:0};t.textAlignHorizontal="CENTER";t.textAlignVertical="CENTER";t.textAutoResize="NONE";
  t.resize(105,66);t.x=89;t.y=percent==="50%"?76.5:76;t.fills=[solid(v.text)];
  t.setBoundVariable("fontFamily",v.family);t.setBoundVariable("fontStyle",v.semibold);t.setBoundVariable("fontSize",v.size);t.setBoundVariable("lineHeight",v.line);t.setBoundVariable("letterSpacing",v.tracking);
  c.appendChild(t);created.push(t.id);components.push(c);
}
const set=figma.combineAsVariants(components,page);set.name="Semi-donut Gauge";
set.description="Indicador semicircular con tres valores de ejemplo fijos. El porcentaje y el arco están sincronizados por variante; el consumidor define métrica, rango y alternativa accesible.";
set.descriptionMarkdown=set.description;set.x=840;set.y=170;created.push(set.id);
set.children.forEach(c=>{const p=c.variantProperties.Progress;c.x=20;c.y=20+["75%","50%","25%"].indexOf(p)*162;});
set.resizeWithoutConstraints(323,510);
return {pageId:page.id,setId:set.id,variants:set.children.map(c=>({id:c.id,name:c.name,wh:[c.width,c.height],vectors:c.children.filter(x=>x.type==="VECTOR").map(n=>({id:n.id,name:n.name,paths:n.vectorPaths.length,wh:[n.width,n.height],xy:[n.x,n.y]}))})),createdNodeIds:created};
