// LINEAR-PROGRESS-BAR-001 · runner injects the read-only source variant snapshot.
figma.skipInvisibleInstanceChildren=false;
const sourceSpecs=__PROGRESS_VARIANTS_JSON__.variants;
if(!Array.isArray(sourceSpecs)||sourceSpecs.length!==48||new Set(sourceSpecs.map(s=>`${s.type}/${s.size}/${s.percentage}`)).size!==48)throw new Error("Source variant matrix mismatch");
if(figma.root.children.some(p=>p.name==="Linear Progress Bars"))throw new Error("Target page exists; inspect before retry");
const tokenSpecs={
  track:["VariableID:219:122","color/background/progress/track","FRAME_FILL"],
  primary:["VariableID:219:123","color/background/progress/primary","FRAME_FILL"],
  warning:["VariableID:219:124","color/background/progress/warning","FRAME_FILL"],
  positive:["VariableID:219:125","color/background/progress/positive","FRAME_FILL"],
  danger:["VariableID:219:126","color/background/progress/danger","FRAME_FILL"],
  text:["VariableID:13:27","color/text/primary","TEXT_FILL"],
  secondary:["VariableID:13:28","color/text/secondary","TEXT_FILL"],
  family:["VariableID:10:2","font/family/base","FONT_FAMILY"],
  regular:["VariableID:10:3","font/weight/regular","FONT_STYLE"],
  size12:["VariableID:10:8","font/size/xs","FONT_SIZE"],
  size14:["VariableID:10:9","font/size/sm","FONT_SIZE"],
  size24:["VariableID:12:2","font/size/xl","FONT_SIZE"],
  line16:["VariableID:12:7","font/line-height/xs","LINE_HEIGHT"],
  line20:["VariableID:12:8","font/line-height/sm","LINE_HEIGHT"],
  line24:["VariableID:12:9","font/line-height/md","LINE_HEIGHT"],
  tracking:["VariableID:12:16","font/letter-spacing/normal","LETTER_SPACING"],
  gap4:["VariableID:12:29","spacing/xs","GAP"],
  radius:["VariableID:13:11","radius/full","CORNER_RADIUS"]
};
const v={};for(const [k,[id,name,scope]] of Object.entries(tokenSpecs)){const t=await figma.variables.getVariableByIdAsync(id);if(!t||t.name!==name||t.variableCollectionId!=="VariableCollectionId:6:2"||!t.scopes.includes(scope))throw new Error("Token mismatch "+k);v[k]=t;}
await figma.loadFontAsync({family:"Manrope",style:"Regular"});
const page=figma.createPage();page.name="Linear Progress Bars";await figma.setCurrentPageAsync(page);
const created=[page.id],components=[];
function solid(token){return figma.variables.setBoundVariableForPaint({type:"SOLID",color:{r:1,g:1,b:1}},"color",token);}
function textNode(parent,name,chars,size,line,color,propertyKey,showKey){const t=figma.createText();t.name=name;t.fontName={family:"Manrope",style:"Regular"};t.characters=chars;t.fontSize=size;t.lineHeight={unit:"PIXELS",value:line};t.letterSpacing={unit:"PIXELS",value:0};t.textAutoResize="WIDTH_AND_HEIGHT";t.fills=[solid(color)];
  t.setBoundVariable("fontFamily",v.family);t.setBoundVariable("fontStyle",v.regular);t.setBoundVariable("fontSize",size===24?v.size24:size===14?v.size14:v.size12);t.setBoundVariable("lineHeight",line===24?v.line24:line===20?v.line20:v.line16);t.setBoundVariable("letterSpacing",v.tracking);
  parent.appendChild(t);if(propertyKey||showKey)t.componentPropertyReferences={...(propertyKey?{characters:propertyKey}:{}),...(showKey?{visible:showKey}:{})};created.push(t.id);return t;}
function frame(parent,name,w,h,mode,gap){const f=figma.createFrame();f.name=name;f.resize(w,h);f.fills=[];f.strokes=[];f.layoutMode=mode;if(mode!=="NONE"){f.primaryAxisSizingMode="FIXED";f.counterAxisSizingMode="FIXED";f.primaryAxisAlignItems="MIN";f.counterAxisAlignItems="CENTER";f.itemSpacing=gap;if(gap===4)f.setBoundVariable("itemSpacing",v.gap4);}parent.appendChild(f);created.push(f.id);return f;}
function rounded(n){n.cornerRadius=9999;for(const key of ["topLeftRadius","topRightRadius","bottomLeftRadius","bottomRightRadius"])n.setBoundVariable(key,v.radius);}
const title=textNode(page,"Page title","Linear Progress Bars",24,24,v.text,null,null);title.x=80;title.y=64;
for(const source of sourceSpecs){
  const size=source.size==="middle"?"Medium":source.size==="small"?"Small":"Large";
  const type=source.type[0].toUpperCase()+source.type.slice(1);
  const rowH=size==="Small"?16:20,trackH=source.trackHeight,compH=size==="Small"?44:size==="Medium"?52:56;
  const c=figma.createComponent();c.name=`Type=${type}, Size=${size}, Progress=${source.percentage}`;c.resize(246,compH);c.fills=[];c.strokes=[];
  c.layoutMode="VERTICAL";c.primaryAxisSizingMode="FIXED";c.counterAxisSizingMode="FIXED";c.primaryAxisAlignItems="MIN";c.counterAxisAlignItems="MIN";c.itemSpacing=4;c.setBoundVariable("itemSpacing",v.gap4);
  page.appendChild(c);created.push(c.id);
  const labelKey=c.addComponentProperty("Label","TEXT","Label");const helperKey=c.addComponentProperty("Helper text","TEXT","Optional helper text");
  const showLabelKey=c.addComponentProperty("Show label","BOOLEAN",true);const showPctKey=c.addComponentProperty("Show percentage","BOOLEAN",true);const showHelperKey=c.addComponentProperty("Show helper text","BOOLEAN",true);
  const row=frame(c,"Label and percentage",246,rowH,"HORIZONTAL",0);row.primaryAxisAlignItems="SPACE_BETWEEN";row.componentPropertyReferences={visible:showLabelKey};
  textNode(row,"Label","Label",size==="Small"?12:14,rowH,v.text,labelKey,null);
  textNode(row,"Percentage",source.percentage,size==="Small"?12:14,rowH,v.text,null,showPctKey);
  const track=frame(c,"Track",246,trackH,"NONE",0);track.fills=[solid(v.track)];track.clipsContent=true;rounded(track);
  const bar=figma.createFrame();bar.name="Progress bar";bar.resize(source.fillWidth,trackH);bar.fills=[solid(v[source.type])];bar.strokes=[];rounded(bar);track.appendChild(bar);created.push(bar.id);
  textNode(c,"Helper text","Optional helper text",12,16,v.secondary,helperKey,showHelperKey);
  components.push(c);
}
const set=figma.combineAsVariants(components,page);set.name="Linear Progress Bar";
set.description="Progreso lineal en cuatro tonos, tres tamaños y cuatro valores fijos de ejemplo. El porcentaje visible coincide con el ancho de la barra. Valor dinámico y accesibilidad programática requieren producto/frontend.";
set.descriptionMarkdown=set.description;set.x=80;set.y=144;created.push(set.id);
for(const c of set.children){const p=c.variantProperties;const source=sourceSpecs.find(s=>s.type===p.Type.toLowerCase()&&s.size===(p.Size==="Medium"?"middle":p.Size.toLowerCase())&&s.percentage===p.Progress);if(!source)throw new Error("Unexpected variant "+c.name);c.x=source.x;c.y=source.y;}
set.resizeWithoutConstraints(1034,1402);
return {pageId:page.id,setId:set.id,variants:set.children.map(c=>({id:c.id,name:c.name,wh:[c.width,c.height]})),createdNodeIds:created};
