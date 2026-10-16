// BREADCRUMBS-001, phase P3.a-b. Run only after source/contract QA PASS.
figma.skipInvisibleInstanceChildren = false;
if (figma.root.children.some(p => p.name === "Breadcrumbs")) throw new Error("Breadcrumbs page already exists; inspect before retry");
const tokenSpecs = {
  textTertiary: ["VariableID:13:29", "color/text/tertiary", "TEXT_FILL"],
  textDisabled: ["VariableID:13:30", "color/text/disabled", "TEXT_FILL"],
  textBrand: ["VariableID:13:32", "color/text/brand", "TEXT_FILL"],
  textBrandStrong: ["VariableID:13:34", "color/text/brand/strong", "TEXT_FILL"],
  textPrimary: ["VariableID:13:27", "color/text/primary", "TEXT_FILL"],
  iconBrand: ["VariableID:13:25", "color/icon/brand", "SHAPE_FILL"],
  iconSecondary: ["VariableID:13:21", "color/icon/secondary", "SHAPE_FILL"],
  iconTertiary: ["VariableID:13:22", "color/icon/tertiary", "SHAPE_FILL"],
  family: ["VariableID:10:2", "font/family/base", "FONT_FAMILY"],
  regular: ["VariableID:10:3", "font/weight/regular", "FONT_STYLE"],
  semibold: ["VariableID:10:5", "font/weight/semibold", "FONT_STYLE"],
  textSize: ["VariableID:10:10", "font/size/md", "FONT_SIZE"],
  titleSize: ["VariableID:10:11", "font/size/lg", "FONT_SIZE"],
  noteSize: ["VariableID:10:9", "font/size/sm", "FONT_SIZE"],
  line: ["VariableID:12:9", "font/line-height/md", "LINE_HEIGHT"],
  noteLine: ["VariableID:12:8", "font/line-height/sm", "LINE_HEIGHT"],
  tracking: ["VariableID:12:15", "font/letter-spacing/tight", "LETTER_SPACING"],
  noteTracking: ["VariableID:12:16", "font/letter-spacing/normal", "LETTER_SPACING"],
  gap: ["VariableID:12:29", "spacing/xs", "GAP"],
  iconSize: ["VariableID:12:23", "size/xl", "WIDTH_HEIGHT"]
};
const v = {};
for (const [k, [id, name, scope]] of Object.entries(tokenSpecs)) {
  const x = await figma.variables.getVariableByIdAsync(id);
  if (!x || x.name !== name || x.variableCollectionId !== "VariableCollectionId:6:2" || !x.scopes.includes(scope)) throw new Error("variable mismatch " + k);
  v[k] = x;
}
const fonts = await figma.listAvailableFontsAsync();
for (const style of ["Regular", "SemiBold"]) {
  if (!fonts.some(f => f.fontName.family === "Manrope" && f.fontName.style === style)) throw new Error("Manrope " + style + " unavailable");
  await figma.loadFontAsync({ family: "Manrope", style });
}
const iconKeys = {
  House: "aac149e12fc8ed2da22bd95d2cef764a2b407ad7",
  CaretRight: "e2fc671298e81c590f5a4a5272d9c97709515666"
};
const icons = {};
for (const [name, key] of Object.entries(iconKeys)) {
  const main = await figma.importComponentByKeyAsync(key);
  if (!main || main.type !== "COMPONENT" || main.key !== key) throw new Error("Phosphor import mismatch " + name);
  icons[name] = main;
}
const page = figma.createPage();
page.name = "Breadcrumbs";
await figma.setCurrentPageAsync(page);
const created = [page.id], mutated = [], components = [], details = [];
function solid(variable) { return figma.variables.setBoundVariableForPaint({ type: "SOLID", color: { r: 1, g: 1, b: 1 } }, "color", variable); }
function addIcon(parent, kind, color) {
  const inst = icons[kind].createInstance();
  inst.name = kind;
  inst.resize(24, 24);
  inst.setBoundVariable("width", v.iconSize);
  inst.setBoundVariable("height", v.iconSize);
  parent.appendChild(inst);
  created.push(inst.id);
  const vectors = inst.findAll(n => n.type === "VECTOR");
  if (!vectors.length) throw new Error(kind + " has no vector");
  for (const vector of vectors) { vector.fills = [solid(color)]; mutated.push(vector.id); }
  return inst;
}
function addText(parent, label, color, semibold, editable) {
  const t = figma.createText();
  t.name = label === "..." ? "Shortened label" : "Label";
  t.fontName = { family: "Manrope", style: semibold ? "SemiBold" : "Regular" };
  t.characters = label;
  t.fontSize = 16;
  t.lineHeight = { unit: "PIXELS", value: 24 };
  t.letterSpacing = { unit: "PIXELS", value: 0 };
  t.textAutoResize = "NONE";
  t.resize(label === "..." ? 14 : 88, 24);
  t.fills = [solid(color)];
  t.setBoundVariable("fontFamily", v.family);
  t.setBoundVariable("fontStyle", semibold ? v.semibold : v.regular);
  t.setBoundVariable("fontSize", v.textSize);
  t.setBoundVariable("lineHeight", v.line);
  t.setBoundVariable("letterSpacing", v.tracking);
  parent.appendChild(t);
  created.push(t.id);
  if (editable) {
    const key = parent.addComponentProperty("Label", "TEXT", "Breadcrumb");
    t.componentPropertyReferences = { characters: key };
  }
  return t;
}
const specs = [
  { state: "Default", current: "false", width: 116, height: 24, x: 23, y: 25, label: "Breadcrumb", textVar: v.textTertiary, caretVar: v.iconSecondary },
  { state: "Icon", current: "false", width: 52, height: 24, x: 55, y: 394, house: true, caretVar: v.iconSecondary },
  { state: "Shortened", current: "false", width: 42, height: 24, x: 62.5, y: 98, label: "...", textVar: v.textTertiary, caretVar: v.iconSecondary },
  { state: "Disabled", current: "false", width: 116, height: 24, x: 23, y: 172, label: "Breadcrumb", textVar: v.textDisabled, caretVar: v.iconTertiary },
  { state: "Default", current: "true", width: 88, height: 24, x: 36, y: 246, label: "Breadcrumb", textVar: v.textBrand },
  { state: "Hover", current: "false", width: 88, height: 24, x: 36, y: 320, label: "Breadcrumb", textVar: v.textBrandStrong }
];
for (const s of specs) {
  const comp = figma.createComponent();
  comp.name = "State=" + s.state + ", Current=" + s.current;
  comp.resize(s.width, s.height);
  comp.layoutMode = "HORIZONTAL";
  comp.primaryAxisSizingMode = "FIXED";
  comp.counterAxisSizingMode = "FIXED";
  comp.primaryAxisAlignItems = "MIN";
  comp.counterAxisAlignItems = "CENTER";
  comp.itemSpacing = 4;
  comp.setBoundVariable("itemSpacing", v.gap);
  comp.fills = [];
  comp.strokes = [];
  page.appendChild(comp);
  created.push(comp.id);
  if (s.house) addIcon(comp, "House", v.iconBrand);
  else if (s.label) addText(comp, s.label, s.textVar, s.state === "Shortened", s.state !== "Shortened");
  if (s.caretVar) addIcon(comp, "CaretRight", s.caretVar);
  components.push(comp);
  details.push({ id: comp.id, state: s.state, current: s.current, size: [s.width, s.height] });
}
const set = figma.combineAsVariants(components, page);
set.name = "Breadcrumb item";
set.description = "Segmento visual de ruta jerárquica. Seis combinaciones observadas; Label editable cuando hay texto normal. House y CaretRight son iconos Phosphor. Navegación, truncamiento y accesibilidad se definen en producto.";
set.descriptionMarkdown = set.description;
set.x = 80; set.y = 160;
for (const child of set.children) {
  const p = child.variantProperties;
  const s = specs.find(x => x.state === p.State && x.current === p.Current);
  if (!s) throw new Error("Unexpected Breadcrumb item variant");
  child.x = s.x; child.y = s.y;
}
set.resizeWithoutConstraints(162, 438);
created.push(set.id);
const title = figma.createText();
title.name = "Page title";
title.fontName = { family: "Manrope", style: "SemiBold" };
title.characters = "Breadcrumbs";
title.fontSize = 20;
title.lineHeight = { unit: "PIXELS", value: 24 };
title.letterSpacing = { unit: "PIXELS", value: 0 };
title.fills = [solid(v.textPrimary)];
title.setBoundVariable("fontFamily", v.family);
title.setBoundVariable("fontStyle", v.semibold);
title.setBoundVariable("fontSize", v.titleSize);
title.setBoundVariable("lineHeight", v.line);
title.setBoundVariable("letterSpacing", v.noteTracking);
page.appendChild(title); title.x = 80; title.y = 80;
created.push(title.id);
return { pageId: page.id, setId: set.id, iconMainIds: Object.fromEntries(Object.entries(icons).map(([k,n]) => [k,n.id])), variants: details, createdNodeIds: created, mutatedNodeIds: mutated, setSize: [set.width,set.height] };
