// INLINE-NOTIFICATION-001 · run only after contract QA PASS and target preflight.
figma.skipInvisibleInstanceChildren = false;
if (figma.root.children.some(p => p.name === "Inline Notifications")) throw new Error("Inline Notifications page already exists");
const expected = {
  bgLight: ["VariableID:13:35", "color/background/default", "FRAME_FILL"],
  bgSuccess: ["VariableID:13:41", "color/feedback/positive/bg", "FRAME_FILL"],
  bgDanger: ["VariableID:13:49", "color/feedback/danger/bg", "FRAME_FILL"],
  bgWarning: ["VariableID:13:45", "color/feedback/warning/bg", "FRAME_FILL"],
  bgInfo: ["VariableID:13:53", "color/feedback/information/bg", "FRAME_FILL"],
  iconPrimary: ["VariableID:13:20", "color/icon/primary", "SHAPE_FILL"],
  iconSuccess: ["VariableID:13:44", "color/feedback/positive/icon", "SHAPE_FILL"],
  iconDanger: ["VariableID:13:52", "color/feedback/danger/icon", "SHAPE_FILL"],
  iconWarning: ["VariableID:13:48", "color/feedback/warning/icon", "SHAPE_FILL"],
  iconInfo: ["VariableID:13:56", "color/feedback/information/icon", "SHAPE_FILL"],
  textPrimary: ["VariableID:13:27", "color/text/primary", "TEXT_FILL"],
  textSecondary: ["VariableID:13:28", "color/text/secondary", "TEXT_FILL"],
  family: ["VariableID:10:2", "font/family/base", "FONT_FAMILY"],
  regular: ["VariableID:10:3", "font/weight/regular", "FONT_STYLE"],
  semibold: ["VariableID:10:5", "font/weight/semibold", "FONT_STYLE"],
  font16: ["VariableID:10:10", "font/size/md", "FONT_SIZE"],
  font14: ["VariableID:10:9", "font/size/sm", "FONT_SIZE"],
  font20: ["VariableID:10:11", "font/size/lg", "FONT_SIZE"],
  line24: ["VariableID:12:9", "font/line-height/md", "LINE_HEIGHT"],
  line20: ["VariableID:12:8", "font/line-height/sm", "LINE_HEIGHT"],
  tracking: ["VariableID:12:16", "font/letter-spacing/normal", "LETTER_SPACING"],
  gap4: ["VariableID:12:29", "spacing/xs", "GAP"],
  gap16: ["VariableID:12:32", "spacing/lg", "GAP"],
  padding24: ["VariableID:12:33", "spacing/xl", "GAP"],
  radius8: ["VariableID:13:6", "radius/md", "CORNER_RADIUS"],
  size16: ["VariableID:12:22", "size/lg", "WIDTH_HEIGHT"],
  size24: ["VariableID:12:23", "size/xl", "WIDTH_HEIGHT"]
};
const v = {};
for (const [k, [id, name, scope]] of Object.entries(expected)) {
  const x = await figma.variables.getVariableByIdAsync(id);
  if (!x || x.name !== name || x.variableCollectionId !== "VariableCollectionId:6:2" || !x.scopes.includes(scope)) throw new Error("variable mismatch " + k);
  v[k] = x;
}
if (Object.values(v.iconWarning.valuesByMode).some(a => a.type !== "VARIABLE_ALIAS" || a.id !== "VariableID:8:109")) throw new Error("Warning icon alias mismatch");
await figma.loadFontAsync({ family: "Manrope", style: "Regular" });
await figma.loadFontAsync({ family: "Manrope", style: "SemiBold" });
const keys = {
  Light: "27962798645349b2b27ba120b6bb1db551e4c8a3",
  Success: "c05dcb9e418a4827e9999640903ed093e850fdc0",
  Danger: "a553df531f5cbc790fbf9481e2d13c0a39c6d540",
  Warning: "75ba7898c02f2522c78786982ea96e00a557bec0",
  Info: "4b8a12b3aa942823e8f1ecea2a3b8af2759cd7cc",
  Close: "ad6c943c212c2ceb4f59e3b435e6781f43657387"
};
const iconMains = {};
for (const [name, key] of Object.entries(keys)) {
  const x = await figma.importComponentByKeyAsync(key);
  if (!x || x.key !== key || x.type !== "COMPONENT") throw new Error("Phosphor import mismatch " + name);
  iconMains[name] = x;
}
const page = figma.createPage();
page.name = "Inline Notifications";
await figma.setCurrentPageAsync(page);
const created = [page.id], mutated = [], comps = [], details = [];
function solid(variable) { return figma.variables.setBoundVariableForPaint({ type: "SOLID", color: { r: 1, g: 1, b: 1 } }, "color", variable); }
function makeIcon(main, name, size, colorVar, sizeVar, parent, propertyKey) {
  const icon = main.createInstance();
  icon.name = name;
  icon.resize(size, size);
  icon.setBoundVariable("width", sizeVar);
  icon.setBoundVariable("height", sizeVar);
  parent.appendChild(icon);
  if (propertyKey) icon.componentPropertyReferences = { visible: propertyKey };
  created.push(icon.id);
  const vectors = icon.findAll(n => n.type === "VECTOR");
  if (!vectors.length) throw new Error("Icon has no vectors " + name);
  for (const vector of vectors) { vector.fills = [solid(colorVar)]; mutated.push(vector.id); }
  return { id: icon.id, vectors: vectors.map(n => n.id), key: main.key };
}
function makeText(name, characters, size, colorVar, sizeVar, parent, charactersKey, visibleKey) {
  const t = figma.createText();
  t.name = name;
  t.fontName = { family: "Manrope", style: "Regular" };
  t.fontSize = size;
  t.lineHeight = { unit: "PIXELS", value: 24 };
  t.letterSpacing = { unit: "PIXELS", value: 0 };
  t.characters = characters;
  t.fills = [solid(colorVar)];
  t.resize(482, name === "Title" ? 24 : 48);
  t.textAutoResize = "HEIGHT";
  parent.appendChild(t);
  t.layoutSizingHorizontal = "FILL";
  t.setBoundVariable("fontFamily", v.family);
  t.setBoundVariable("fontStyle", v.regular);
  t.setBoundVariable("fontSize", sizeVar);
  t.setBoundVariable("lineHeight", v.line24);
  t.setBoundVariable("letterSpacing", v.tracking);
  t.componentPropertyReferences = { characters: charactersKey, visible: visibleKey };
  created.push(t.id);
  return t;
}
const spec = {
  Light: { bg: v.bgLight, icon: v.iconPrimary },
  Success: { bg: v.bgSuccess, icon: v.iconSuccess },
  Danger: { bg: v.bgDanger, icon: v.iconDanger },
  Warning: { bg: v.bgWarning, icon: v.iconWarning },
  Info: { bg: v.bgInfo, icon: v.iconInfo }
};
const body = "Mensaje breve sobre el estado actual del proceso.\nInformación adicional para la persona usuaria.";
for (const type of ["Light", "Success", "Danger", "Warning", "Info"]) {
  const comp = figma.createComponent();
  comp.name = "Type=" + type;
  comp.resize(602, 108);
  comp.layoutMode = "HORIZONTAL";
  comp.primaryAxisSizingMode = "FIXED";
  comp.counterAxisSizingMode = "AUTO";
  comp.primaryAxisAlignItems = "MIN";
  comp.counterAxisAlignItems = "MIN";
  comp.paddingTop = 16; comp.paddingBottom = 16;
  comp.paddingLeft = 24; comp.paddingRight = 24;
  comp.itemSpacing = 16;
  comp.setBoundVariable("paddingTop", v.gap16);
  comp.setBoundVariable("paddingBottom", v.gap16);
  comp.setBoundVariable("paddingLeft", v.padding24);
  comp.setBoundVariable("paddingRight", v.padding24);
  comp.setBoundVariable("itemSpacing", v.gap16);
  comp.fills = [solid(spec[type].bg)];
  comp.strokes = [];
  comp.cornerRadius = 8;
  for (const corner of ["topLeftRadius", "topRightRadius", "bottomRightRadius", "bottomLeftRadius"]) comp.setBoundVariable(corner, v.radius8);
  page.appendChild(comp);
  created.push(comp.id);
  const titleKey = comp.addComponentProperty("Title", "TEXT", "Título");
  const descKey = comp.addComponentProperty("Description", "TEXT", body);
  const showTitleKey = comp.addComponentProperty("Show title", "BOOLEAN", true);
  const showDescKey = comp.addComponentProperty("Show description", "BOOLEAN", true);
  const showIconKey = comp.addComponentProperty("Show icon", "BOOLEAN", true);
  const showDismissKey = comp.addComponentProperty("Show dismiss", "BOOLEAN", true);
  const leading = makeIcon(iconMains[type], "Status icon", 24, spec[type].icon, v.size24, comp, showIconKey);
  const column = figma.createAutoLayout("VERTICAL");
  column.name = "Text content";
  column.resize(482, 76);
  column.primaryAxisSizingMode = "AUTO";
  column.counterAxisSizingMode = "FIXED";
  column.itemSpacing = 4;
  column.setBoundVariable("itemSpacing", v.gap4);
  column.fills = []; column.strokes = [];
  comp.appendChild(column);
  column.layoutSizingHorizontal = "FILL";
  column.layoutSizingVertical = "HUG";
  created.push(column.id);
  const title = makeText("Title", "Título", 16, v.textPrimary, v.font16, column, titleKey, showTitleKey);
  const description = makeText("Description", body, 14, v.textSecondary, v.font14, column, descKey, showDescKey);
  const close = makeIcon(iconMains.Close, "Dismiss icon", 16, v.iconPrimary, v.size16, comp, showDismissKey);
  comps.push(comp);
  details.push({ id: comp.id, type, leading, columnId: column.id, titleId: title.id, descriptionId: description.id, close, keys: { titleKey, descKey, showTitleKey, showDescKey, showIconKey, showDismissKey } });
}
const set = figma.combineAsVariants(comps, page);
set.name = "Inline Notification";
set.description = "Mensaje contextual de cinco tratamientos visuales. Title y Description son editables; Show icon y Show dismiss solo controlan apariencia. Close no ejecuta cierre por sí mismo. No simular enlaces sin destino; el producto define severidad, anuncio accesible y acción.";
set.descriptionMarkdown = set.description;
set.x = 80; set.y = 160;
for (const child of set.children) {
  const row = ["Light", "Success", "Danger", "Warning", "Info"].indexOf(child.variantProperties.Type);
  if (row < 0) throw new Error("Unexpected variant Type");
  child.x = 24; child.y = 40 + row * 148;
}
set.resizeWithoutConstraints(650, 780);
created.push(set.id);
const pageTitle = figma.createText();
pageTitle.name = "Page title";
pageTitle.fontName = { family: "Manrope", style: "SemiBold" };
pageTitle.characters = "Inline Notifications";
pageTitle.fontSize = 20;
pageTitle.lineHeight = { unit: "PIXELS", value: 24 };
pageTitle.letterSpacing = { unit: "PIXELS", value: 0 };
pageTitle.fills = [solid(v.textPrimary)];
pageTitle.setBoundVariable("fontFamily", v.family);
pageTitle.setBoundVariable("fontStyle", v.semibold);
pageTitle.setBoundVariable("fontSize", v.font20);
pageTitle.setBoundVariable("lineHeight", v.line24);
pageTitle.setBoundVariable("letterSpacing", v.tracking);
page.appendChild(pageTitle); pageTitle.x = 80; pageTitle.y = 80;
created.push(pageTitle.id);
const note = figma.createText();
note.name = "Usage and accessibility note";
note.fontName = { family: "Manrope", style: "Regular" };
note.characters = "Cinco tratamientos visuales con contenido editable. El icono Close no cierra por sí mismo; el producto debe definir acción, anuncio accesible y tamaño táctil. Auditoría humana pendiente.";
note.fontSize = 14;
note.lineHeight = { unit: "PIXELS", value: 20 };
note.letterSpacing = { unit: "PIXELS", value: 0 };
note.fills = [solid(v.textPrimary)];
note.resize(800, 60); note.textAutoResize = "HEIGHT";
note.setBoundVariable("fontFamily", v.family);
note.setBoundVariable("fontStyle", v.regular);
note.setBoundVariable("fontSize", v.font14);
note.setBoundVariable("lineHeight", v.line20);
note.setBoundVariable("letterSpacing", v.tracking);
page.appendChild(note); note.x = 80; note.y = 990;
created.push(note.id);
return { pageId: page.id, setId: set.id, importedIconIds: Object.fromEntries(Object.entries(iconMains).map(([name,x])=>[name,x.id])), variants: details, createdNodeIds: created, mutatedNodeIds: mutated, setBounds: { width: set.width, height: set.height }, variantBounds: set.children.map(n=>({ name:n.name, width:n.width, height:n.height, x:n.x, y:n.y })) };
