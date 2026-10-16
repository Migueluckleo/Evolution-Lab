// CHARTS-001 phase C: Progress Chart Item and Chart Header using local Legend Label instances.
figma.skipInvisibleInstanceChildren=false;
const page=await figma.getNodeByIdAsync("210:122");
const legendSet=await figma.getNodeByIdAsync("210:145");
const legendMain=await figma.getNodeByIdAsync("210:129");
if(!page||page.type!=="PAGE"||page.name!=="Charts"||!legendSet||legendSet.name!=="Chart Legend Label"||!legendMain||legendMain.parent?.id!==legendSet.id)throw new Error("Chart dependency mismatch");
if(page.children.some(x=>["Progress Chart Item","Chart Header"].includes(x.name)))throw new Error("Chart component exists; inspect before retry");
const tokenSpecs={
  text:["VariableID:13:27","color/text/primary","TEXT_FILL"],
  track:["VariableID:13:37","color/background/muted","FRAME_FILL"],
  progress:["VariableID:208:123","color/shape/chart/progress","SHAPE_FILL"],
  legendTrack:["VariableID:208:124","color/shape/chart/track","SHAPE_FILL"],
  series1:["VariableID:208:126","color/shape/chart/series-1","SHAPE_FILL"],
  series2:["VariableID:208:127","color/shape/chart/series-2","SHAPE_FILL"],
  series3:["VariableID:208:128","color/shape/chart/series-3","SHAPE_FILL"],
  family:["VariableID:10:2","font/family/base","FONT_FAMILY"],
  regular:["VariableID:10:3","font/weight/regular","FONT_STYLE"],
  fsXs:["VariableID:10:8","font/size/xs","FONT_SIZE"],
  fsLg:["VariableID:10:11","font/size/lg","FONT_SIZE"],
  lhXs:["VariableID:12:7","font/line-height/xs","LINE_HEIGHT"],
  lhSm:["VariableID:12:8","font/line-height/sm","LINE_HEIGHT"],
  tracking:["VariableID:12:16","font/letter-spacing/normal","LETTER_SPACING"],
  gapNone:["VariableID:12:18","spacing/none","GAP"],
  gapSm:["VariableID:12:30","spacing/sm","GAP"],
  gapLg:["VariableID:12:32","spacing/lg","GAP"],
  gapXl:["VariableID:12:33","spacing/xl","GAP"],
  radiusNone:["VariableID:12:39","radius/none","CORNER_RADIUS"],
  radiusXs:["VariableID:13:4","radius/xs","CORNER_RADIUS"],
  radiusSm:["VariableID:13:5","radius/sm","CORNER_RADIUS"]
};
const v={};for(const [k,[id,name,scope]] of Object.entries(tokenSpecs)){const t=await figma.variables.getVariableByIdAsync(id);if(!t||t.name!==name||t.variableCollectionId!=="VariableCollectionId:6:2"||!t.scopes.includes(scope))throw new Error("Token mismatch "+k);v[k]=t;}
await figma.loadFontAsync({family:"Manrope",style:"Regular"});await figma.setCurrentPageAsync(page);
function solid(token){return figma.variables.setBoundVariableForPaint({type:"SOLID",color:{r:1,g:1,b:1}},"color",token);}
const created=[],mutated=[];
function frame(parent,name,w,h,mode,gap,gapToken){const f=figma.createFrame();f.name=name;f.resize(w,h);f.fills=[];f.strokes=[];f.layoutMode=mode;f.primaryAxisSizingMode="FIXED";f.counterAxisSizingMode="FIXED";f.primaryAxisAlignItems="MIN";f.counterAxisAlignItems="CENTER";f.itemSpacing=gap;if(gapToken)f.setBoundVariable("itemSpacing",gapToken);parent.appendChild(f);created.push(f.id);return f;}
function textNode(parent,name,chars,size,line,fs,lh,propKey){const t=figma.createText();t.name=name;t.fontName={family:"Manrope",style:"Regular"};t.characters=chars;t.fontSize=size;t.lineHeight={unit:"PIXELS",value:line};t.letterSpacing={unit:"PIXELS",value:0};t.textAutoResize="WIDTH_AND_HEIGHT";t.fills=[solid(v.text)];
  t.setBoundVariable("fontFamily",v.family);t.setBoundVariable("fontStyle",v.regular);t.setBoundVariable("fontSize",fs);t.setBoundVariable("lineHeight",lh);t.setBoundVariable("letterSpacing",v.tracking);parent.appendChild(t);if(propKey)t.componentPropertyReferences={characters:propKey};created.push(t.id);return t;}
function bindCorners(n,token,value){n.cornerRadius=value;for(const key of ["topLeftRadius","topRightRadius","bottomLeftRadius","bottomRightRadius"])n.setBoundVariable(key,token);}
function legendInstance(parent,label,swatchToken,show,w,align){const i=legendMain.createInstance();i.name="Chart Legend Label";i.resize(w,16);i.setProperties({"Text#210:8":label,"Show swatch#210:9":show});i.primaryAxisAlignItems=align;parent.appendChild(i);created.push(i.id);
  const shape=i.findOne(n=>n.type==="RECTANGLE"&&n.name==="Series shape");if(!shape)throw new Error("Legend swatch missing");shape.fills=[solid(swatchToken)];mutated.push(shape.id);return i;}
const progressVariants=[];
for(const kind of ["Top","Detail"]){const detail=kind==="Detail";const c=figma.createComponent();c.name="Type="+kind;c.resize(639,detail?104:30);c.fills=[];c.strokes=[];
  c.layoutMode="VERTICAL";c.primaryAxisSizingMode="FIXED";c.counterAxisSizingMode="FIXED";c.primaryAxisAlignItems="MIN";c.counterAxisAlignItems="MIN";c.itemSpacing=detail?16:6;
  if(detail)c.setBoundVariable("itemSpacing",v.gapLg);
  page.appendChild(c);created.push(c.id);const labelKey=c.addComponentProperty("Label","TEXT","Text example");const valueKey=c.addComponentProperty("Value","TEXT","$100k");
  const head=frame(c,"Header",639,16,"HORIZONTAL",0,v.gapNone);head.primaryAxisAlignItems="SPACE_BETWEEN";
  textNode(head,"Label","Text example",12,16,v.fsXs,v.lhXs,labelKey);
  textNode(head,"Value","$100k",12,16,v.fsXs,v.lhXs,valueKey);
  const parent=detail?frame(c,"Body",639,72,"VERTICAL",8,v.gapSm):c;
  const track=frame(parent,"Bar",639,detail?24:8,"HORIZONTAL",0,v.gapNone);track.fills=[solid(v.track)];track.clipsContent=true;bindCorners(track,detail?v.radiusSm:v.radiusXs,detail?4:2);
  const fill=figma.createRectangle();fill.name="Progress";fill.resize(detail?247:580,detail?24:8);fill.fills=[solid(v.progress)];fill.strokes=[];bindCorners(fill,v.radiusNone,0);track.appendChild(fill);created.push(fill.id);
  if(detail)for(let row=0;row<2;row++){const line=frame(parent,"Legend "+(row+1),639,16,"HORIZONTAL",0,v.gapNone);
    legendInstance(line,"Progress",row===0?v.progress:v.legendTrack,true,213,"MIN");
    legendInstance(line,"80%",row===0?v.progress:v.legendTrack,false,213,"CENTER");
    legendInstance(line,"80k",row===0?v.progress:v.legendTrack,false,213,"MAX");
  }
  progressVariants.push(c);
}
const progressSet=figma.combineAsVariants(progressVariants,page);progressSet.name="Progress Chart Item";
progressSet.description="Dos anatomías de progreso con geometría y textos de muestra fijos. Las barras no calculan porcentajes; las leyendas reutilizan Chart Legend Label.";
progressSet.descriptionMarkdown=progressSet.description;progressSet.x=80;progressSet.y=824;created.push(progressSet.id);
progressSet.children.forEach(c=>{c.x=20;c.y=c.variantProperties.Type==="Top"?24:94;});progressSet.resizeWithoutConstraints(679,222);
const h=figma.createComponent();h.name="Chart Header";h.resize(638,48);h.fills=[];h.strokes=[];h.layoutMode="HORIZONTAL";h.primaryAxisSizingMode="FIXED";h.counterAxisSizingMode="FIXED";h.primaryAxisAlignItems="MIN";h.counterAxisAlignItems="MAX";h.itemSpacing=24;h.setBoundVariable("itemSpacing",v.gapXl);page.appendChild(h);h.x=840;h.y=824;created.push(h.id);
const titleKey=h.addComponentProperty("Title","TEXT","Title chart");const descKey=h.addComponentProperty("Description","TEXT","Description");const showLegendKey=h.addComponentProperty("Show legend","BOOLEAN",true);const showDescKey=h.addComponentProperty("Show description","BOOLEAN",true);
const left=frame(h,"Title and description",412,48,"VERTICAL",8,v.gapSm);left.counterAxisAlignItems="MIN";
textNode(left,"Title","Title chart",20,20,v.fsLg,v.lhSm,titleKey);
const desc=textNode(left,"Description","Description",12,20,v.fsXs,v.lhSm,descKey);desc.componentPropertyReferences={characters:descKey,visible:showDescKey};
const indicators=frame(h,"Indicators",202,16,"HORIZONTAL",0,v.gapNone);indicators.componentPropertyReferences={visible:showLegendKey};
legendInstance(indicators,"Value 1",v.series1,true,66,"MIN");legendInstance(indicators,"Value 2",v.series2,true,68,"MIN");legendInstance(indicators,"Value 3",v.series3,true,68,"MIN");
h.description="Encabezado de gráfico con título, descripción y tres series visibles. Los textos de serie se editan en las instancias locales de Chart Legend Label; los datos reales y su accesibilidad pertenecen al consumidor.";
h.descriptionMarkdown=h.description;
return {pageId:page.id,progressSetId:progressSet.id,progressVariants:progressSet.children.map(c=>({id:c.id,name:c.name})),headerId:h.id,legendInstances:progressSet.findAll(n=>n.type==="INSTANCE").length+h.findAll(n=>n.type==="INSTANCE").length,createdNodeIds:created,mutatedNodeIds:mutated};
