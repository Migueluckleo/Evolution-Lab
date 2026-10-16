// CHARTS-001 phase A: create the exclusive page, Chart Legend Label and Chart Cell.
figma.skipInvisibleInstanceChildren = false;
if (figma.root.children.some(p => p.name === "Charts")) throw new Error("Charts page exists; inspect before retry");
const tokenSpecs = {
  text: ["VariableID:13:27", "color/text/primary", "TEXT_FILL"],
  border: ["VariableID:13:12", "color/border/accent", "STROKE_COLOR"],
  bar: ["VariableID:208:122", "color/background/chart/bar", "FRAME_FILL"],
  neutral: ["VariableID:208:125", "color/shape/chart/legend-neutral", "SHAPE_FILL"],
  family: ["VariableID:10:2", "font/family/base", "FONT_FAMILY"],
  regular: ["VariableID:10:3", "font/weight/regular", "FONT_STYLE"],
  semibold: ["VariableID:10:5", "font/weight/semibold", "FONT_STYLE"],
  xs: ["VariableID:10:8", "font/size/xs", "FONT_SIZE"],
  md: ["VariableID:10:10", "font/size/md", "FONT_SIZE"],
  xl: ["VariableID:12:2", "font/size/xl", "FONT_SIZE"],
  lhXs: ["VariableID:12:7", "font/line-height/xs", "LINE_HEIGHT"],
  lhMd: ["VariableID:12:9", "font/line-height/md", "LINE_HEIGHT"],
  tracking: ["VariableID:12:16", "font/letter-spacing/normal", "LETTER_SPACING"],
  spNone: ["VariableID:12:18", "spacing/none", "GAP"],
  spXs: ["VariableID:12:29", "spacing/xs", "GAP"],
  spSm: ["VariableID:12:30", "spacing/sm", "GAP"],
  radiusNone: ["VariableID:12:39", "radius/none", "CORNER_RADIUS"],
  radiusSm: ["VariableID:13:5", "radius/sm", "CORNER_RADIUS"],
  stroke: ["VariableID:12:41", "stroke/xs", "STROKE_FLOAT"]
};
const v = {};
for (const [key, [id, name, scope]] of Object.entries(tokenSpecs)) {
  const t = await figma.variables.getVariableByIdAsync(id);
  if (!t || t.name !== name || t.variableCollectionId !== "VariableCollectionId:6:2" || !t.scopes.includes(scope)) throw new Error("Token mismatch " + key);
  v[key] = t;
}
const fonts = await figma.listAvailableFontsAsync();
for (const style of ["Regular", "SemiBold"]) {
  if (!fonts.some(f => f.fontName.family === "Manrope" && f.fontName.style === style)) throw new Error("Manrope " + style + " unavailable");
  await figma.loadFontAsync({ family: "Manrope", style });
}
const page = figma.createPage(); page.name = "Charts"; await figma.setCurrentPageAsync(page);
const created = [page.id], legendVariants = [], cellVariants = [];
function solid(variable) { return figma.variables.setBoundVariableForPaint({ type: "SOLID", color: { r: 1, g: 1, b: 1 } }, "color", variable); }
function bindText(t, chars, size, height, style, fs, lh) {
  t.fontName = { family: "Manrope", style }; t.characters = chars; t.fontSize = size;
  t.lineHeight = { unit: "PIXELS", value: height }; t.letterSpacing = { unit: "PIXELS", value: 0 };
  t.fills = [solid(v.text)]; t.setBoundVariable("fontFamily", v.family);
  t.setBoundVariable("fontStyle", style === "Regular" ? v.regular : v.semibold);
  t.setBoundVariable("fontSize", fs); t.setBoundVariable("lineHeight", lh);
  t.setBoundVariable("letterSpacing", v.tracking);
}
function docText(name, chars, x, y) {
  const t = figma.createText(); t.name = name; bindText(t, chars, 24, 24, "Regular", v.xl, v.lhMd);
  t.textAutoResize = "WIDTH_AND_HEIGHT"; page.appendChild(t); t.x = x; t.y = y; created.push(t.id); return t;
}
docText("Page title", "Charts", 80, 64);
docText("Section · Legend labels", "Chart Legend Label", 80, 128);
docText("Section · Chart cells", "Chart Cell", 80, 344);
docText("Section · Progress", "Progress Chart Item", 80, 782);
docText("Section · Gauge", "Semi-donut Gauge", 840, 128);
docText("Section · Header", "Chart Header", 840, 782);
for (const weight of ["Regular", "SemiBold"]) for (const sizeName of ["Small", "Medium"]) {
  const isMedium = sizeName === "Medium";
  const c = figma.createComponent(); c.name = `Weight=${weight}, Text size=${sizeName}`; c.resize(76,16);
  c.layoutMode = "HORIZONTAL"; c.primaryAxisSizingMode = "FIXED"; c.counterAxisSizingMode = "FIXED";
  c.primaryAxisAlignItems = "MIN"; c.counterAxisAlignItems = "CENTER";
  c.itemSpacing = 4; c.setBoundVariable("itemSpacing", v.spXs);
  c.paddingTop = c.paddingBottom = 0; c.paddingLeft = c.paddingRight = 4;
  c.setBoundVariable("paddingTop", v.spNone); c.setBoundVariable("paddingBottom", v.spNone);
  c.setBoundVariable("paddingLeft", v.spXs); c.setBoundVariable("paddingRight", v.spXs);
  c.fills = []; c.strokes = []; page.appendChild(c); created.push(c.id);
  const textKey = c.addComponentProperty("Text", "TEXT", "000");
  const showKey = c.addComponentProperty("Show swatch", "BOOLEAN", true);
  const dot = figma.createFrame(); dot.name = "Swatch"; dot.resize(16,16); dot.fills=[]; dot.strokes=[];
  c.appendChild(dot); dot.componentPropertyReferences = { visible: showKey }; created.push(dot.id);
  const shape = figma.createRectangle(); shape.name="Series shape"; shape.resize(16,10); shape.x=0; shape.y=3;
  shape.fills=[solid(v.neutral)]; shape.strokes=[]; dot.appendChild(shape); created.push(shape.id);
  const t = figma.createText(); t.name="Text"; bindText(t,"000",isMedium?16:12,16,weight,isMedium?v.md:v.xs,v.lhXs);
  t.textAutoResize="WIDTH_AND_HEIGHT"; c.appendChild(t); t.componentPropertyReferences={ characters:textKey }; created.push(t.id);
  legendVariants.push(c);
}
const legendSet = figma.combineAsVariants(legendVariants,page); legendSet.name="Chart Legend Label";
legendSet.description="Etiqueta y swatch de serie para leyendas de Charts; cuatro combinaciones de peso y tamaño, texto y swatch editables. La semántica de datos corresponde al consumidor.";
legendSet.descriptionMarkdown=legendSet.description; legendSet.x=80; legendSet.y=170; created.push(legendSet.id);
legendSet.children.forEach(c=>{const p=c.variantProperties; c.x=p["Text size"]==="Small"?20:116; c.y=p.Weight==="Regular"?36:86;});
legendSet.resizeWithoutConstraints(212,138);
const cells=[{has:false,pos:"-",seg:"-"}];
for (const pos of ["first","middle","last"]) for (const seg of ["solo","upper","middle","lower"]) cells.push({has:true,pos,seg});
for (const spec of cells) {
  const c=figma.createComponent(); c.name=`Has content=${spec.has}, Position=${spec.pos}, Segment=${spec.seg}`;
  c.resize(26,35); c.fills=[]; c.strokes=[solid(v.border)]; c.strokeWeight=1;
  c.setBoundVariable("strokeWeight",v.stroke); c.dashPattern=[2,2]; c.clipsContent=false;
  c.layoutMode="HORIZONTAL"; c.primaryAxisSizingMode="FIXED"; c.counterAxisSizingMode="FIXED";
  c.primaryAxisAlignItems="MIN"; c.counterAxisAlignItems="CENTER";
  c.itemSpacing=0; c.setBoundVariable("itemSpacing",v.spNone);
  c.paddingTop=0; c.paddingBottom=0; c.setBoundVariable("paddingTop",v.spNone); c.setBoundVariable("paddingBottom",v.spNone);
  const left=spec.pos==="middle"?6:spec.pos==="last"?4:8;
  const right=spec.pos==="middle"?6:spec.pos==="last"?8:4;
  c.paddingLeft=left; c.paddingRight=right;
  if(left===4||left===8)c.setBoundVariable("paddingLeft",left===4?v.spXs:v.spSm);
  if(right===4||right===8)c.setBoundVariable("paddingRight",right===4?v.spXs:v.spSm);
  page.appendChild(c); created.push(c.id);
  if(spec.has) {
    const bar=figma.createFrame(); bar.name="BarCell"; bar.resize(14,35); bar.fills=[solid(v.bar)]; bar.strokes=[];
    bar.topLeftRadius=(spec.seg==="solo"||spec.seg==="upper")?4:0;
    bar.topRightRadius=bar.topLeftRadius;
    bar.bottomLeftRadius=(spec.seg==="solo"||spec.seg==="lower")?4:0;
    bar.bottomRightRadius=bar.bottomLeftRadius;
    for(const corner of ["topLeftRadius","topRightRadius","bottomLeftRadius","bottomRightRadius"]) bar.setBoundVariable(corner,bar[corner]===4?v.radiusSm:v.radiusNone);
    c.appendChild(bar); created.push(bar.id);
  }
  cellVariants.push(c);
}
const cellSet=figma.combineAsVariants(cellVariants,page); cellSet.name="Chart Cell";
cellSet.description="Celda visual de gráfico: una combinación vacía y doce barras por posición y segmento. El consumidor aporta valor y alternativa textual; no hay interacción.";
cellSet.descriptionMarkdown=cellSet.description; cellSet.x=80; cellSet.y=388; created.push(cellSet.id);
cellSet.children.forEach(c=>{const p=c.variantProperties; const col=p["Has content"]==="false"?0:["first","middle","last"].indexOf(p.Position)+1; const row=p["Has content"]==="false"?0:["solo","upper","middle","lower"].indexOf(p.Segment); c.x=20+col*62; c.y=28+row*76;});
cellSet.resizeWithoutConstraints(290,360);
return {pageId:page.id,legendSetId:legendSet.id,cellSetId:cellSet.id,legendVariants:legendSet.children.map(c=>({id:c.id,name:c.name})),cellVariants:cellSet.children.map(c=>({id:c.id,name:c.name})),createdNodeIds:created};
