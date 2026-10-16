// BREADCRUMBS-001, phase P3.c. Requires page and Breadcrumb item set from P3.a-b.
figma.skipInvisibleInstanceChildren = false;
const page = await figma.getNodeByIdAsync("190:188");
const itemSet = await figma.getNodeByIdAsync("190:210");
if (!page || page.type !== "PAGE" || page.name !== "Breadcrumbs") throw new Error("Breadcrumbs page mismatch");
if (!itemSet || itemSet.type !== "COMPONENT_SET" || itemSet.name !== "Breadcrumb item" || itemSet.parent?.id !== page.id || itemSet.children.length !== 6) throw new Error("Breadcrumb item set mismatch");
if (page.children.some(n => n.name === "Breadcrumbs" && n.type === "COMPONENT_SET")) throw new Error("Breadcrumbs composition already exists; inspect before retry");
const previousMain = itemSet.children.find(n => n.name === "State=Default, Current=false");
const currentMain = itemSet.children.find(n => n.name === "State=Default, Current=true");
if (!previousMain || !currentMain || previousMain.type !== "COMPONENT" || currentMain.type !== "COMPONENT") throw new Error("Required item variants missing");
const tokenSpecs = {
  iconPrimary: ["VariableID:13:20", "color/icon/primary", "SHAPE_FILL"],
  textPrimary: ["VariableID:13:27", "color/text/primary", "TEXT_FILL"],
  family: ["VariableID:10:2", "font/family/base", "FONT_FAMILY"],
  regular: ["VariableID:10:3", "font/weight/regular", "FONT_STYLE"],
  noteSize: ["VariableID:10:9", "font/size/sm", "FONT_SIZE"],
  noteLine: ["VariableID:12:8", "font/line-height/sm", "LINE_HEIGHT"],
  tracking: ["VariableID:12:16", "font/letter-spacing/normal", "LETTER_SPACING"],
  gapInner: ["VariableID:12:29", "spacing/xs", "GAP"],
  gapOuter: ["VariableID:12:30", "spacing/sm", "GAP"],
  iconSize: ["VariableID:12:23", "size/xl", "WIDTH_HEIGHT"]
};
const v = {};
for (const [k, [id, name, scope]] of Object.entries(tokenSpecs)) {
  const x = await figma.variables.getVariableByIdAsync(id);
  if (!x || x.name !== name || x.variableCollectionId !== "VariableCollectionId:6:2" || !x.scopes.includes(scope)) throw new Error("variable mismatch " + k);
  v[k] = x;
}
const fonts = await figma.listAvailableFontsAsync();
if (!fonts.some(f => f.fontName.family === "Manrope" && f.fontName.style === "Regular")) throw new Error("Manrope Regular unavailable");
await figma.loadFontAsync({ family: "Manrope", style: "Regular" });
const arrowKey = "395e4dcf16b8451c0b295bb7402a9319d1b4a9f2";
const arrowMain = await figma.importComponentByKeyAsync(arrowKey);
if (!arrowMain || arrowMain.type !== "COMPONENT" || arrowMain.key !== arrowKey) throw new Error("ArrowLeft import mismatch");
await figma.setCurrentPageAsync(page);
const created = [], mutated = [], components = [], details = [];
function solid(variable) { return figma.variables.setBoundVariableForPaint({ type: "SOLID", color: { r: 1, g: 1, b: 1 } }, "color", variable); }
for (const level of [2, 3, 4, 5]) {
  const width = 242 + 120 * (level - 2);
  const innerWidth = width - 32;
  const comp = figma.createComponent();
  comp.name = "Level=" + level;
  comp.resize(width, 24);
  comp.layoutMode = "HORIZONTAL";
  comp.primaryAxisSizingMode = "FIXED";
  comp.counterAxisSizingMode = "FIXED";
  comp.primaryAxisAlignItems = "MIN";
  comp.counterAxisAlignItems = "CENTER";
  comp.itemSpacing = 8;
  comp.setBoundVariable("itemSpacing", v.gapOuter);
  comp.fills = [];
  comp.strokes = [];
  page.appendChild(comp);
  created.push(comp.id);
  const arrow = arrowMain.createInstance();
  arrow.name = "ArrowLeft";
  arrow.resize(24, 24);
  arrow.setBoundVariable("width", v.iconSize);
  arrow.setBoundVariable("height", v.iconSize);
  comp.appendChild(arrow);
  created.push(arrow.id);
  const vectors = arrow.findAll(n => n.type === "VECTOR");
  if (!vectors.length) throw new Error("ArrowLeft has no vector");
  for (const vector of vectors) { vector.fills = [solid(v.iconPrimary)]; mutated.push(vector.id); }
  const items = figma.createAutoLayout("HORIZONTAL");
  items.name = "Items";
  items.resize(innerWidth, 24);
  items.primaryAxisSizingMode = "FIXED";
  items.counterAxisSizingMode = "FIXED";
  items.primaryAxisAlignItems = "MIN";
  items.counterAxisAlignItems = "CENTER";
  items.itemSpacing = 4;
  items.setBoundVariable("itemSpacing", v.gapInner);
  items.fills = [];
  items.strokes = [];
  comp.appendChild(items);
  created.push(items.id);
  const itemIds = [];
  for (let i = 1; i <= level; i++) {
    const inst = (i === level ? currentMain : previousMain).createInstance();
    inst.name = "Breadcrumb " + i;
    items.appendChild(inst);
    if (i === level) inst.resize(90, 24);
    created.push(inst.id);
    itemIds.push(inst.id);
  }
  components.push(comp);
  details.push({ id: comp.id, level, size: [comp.width, comp.height], arrowId: arrow.id, itemIds, frameId: items.id, innerWidth });
}
const set = figma.combineAsVariants(components, page);
set.name = "Breadcrumbs";
set.description = "Ruta jerárquica visual de dos a cinco segmentos. Compone instancias reales de Breadcrumb item y una instancia ArrowLeft. El producto define destinos, navegación, página actual y truncamiento.";
set.descriptionMarkdown = set.description;
set.x = 360; set.y = 160;
for (const child of set.children) {
  const level = Number(child.variantProperties.Level);
  if (![2,3,4,5].includes(level)) throw new Error("Unexpected Breadcrumbs level");
  child.x = 24; child.y = 24 + 74 * (level - 2);
}
set.resizeWithoutConstraints(650, 296);
created.push(set.id);
const note = figma.createText();
note.name = "Usage and accessibility note";
note.fontName = { family: "Manrope", style: "Regular" };
note.characters = "Los niveles son muestras visuales. Define enlaces, destinos, página actual, foco y acortamiento en producto. En este destino, los iconos compactos usan 24 px tokenizados y las etiquetas activas usan Manrope local. Auditoría humana pendiente.";
note.fontSize = 14;
note.lineHeight = { unit: "PIXELS", value: 20 };
note.letterSpacing = { unit: "PIXELS", value: 0 };
note.fills = [solid(v.textPrimary)];
note.resize(850, 100);
note.textAutoResize = "HEIGHT";
note.setBoundVariable("fontFamily", v.family);
note.setBoundVariable("fontStyle", v.regular);
note.setBoundVariable("fontSize", v.noteSize);
note.setBoundVariable("lineHeight", v.noteLine);
note.setBoundVariable("letterSpacing", v.tracking);
page.appendChild(note); note.x = 80; note.y = 680;
created.push(note.id);
return { pageId: page.id, itemSetId: itemSet.id, compositionSetId: set.id, arrowMainId: arrowMain.id, variants: details, createdNodeIds: created, mutatedNodeIds: mutated, setSize: [set.width,set.height] };
