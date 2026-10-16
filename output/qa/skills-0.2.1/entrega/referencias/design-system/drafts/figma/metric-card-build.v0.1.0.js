// METRIC-CARD-001 · create eight observed variants on the exclusive Metric Cards page.
figma.skipInvisibleInstanceChildren = false;
if (figma.root.children.some(p => p.name === "Metric Cards")) throw new Error("Metric Cards page exists; inspect before retry");
const tokenSpecs = {
  bgDefault: ["VariableID:13:35", "color/background/default", "FRAME_FILL"],
  bgSubtle: ["VariableID:13:36", "color/background/subtle", "FRAME_FILL"],
  borderSubtle: ["VariableID:13:14", "color/border/subtle", "STROKE_COLOR"],
  textPrimary: ["VariableID:13:27", "color/text/primary", "TEXT_FILL"],
  textSecondary: ["VariableID:13:28", "color/text/secondary", "TEXT_FILL"],
  textTrend: ["VariableID:200:122", "color/text/metric/trend", "TEXT_FILL"],
  iconBrand: ["VariableID:200:123", "color/icon/metric/brand", "SHAPE_FILL"],
  family: ["VariableID:10:2", "font/family/base", "FONT_FAMILY"],
  regular: ["VariableID:10:3", "font/weight/regular", "FONT_STYLE"],
  tracking: ["VariableID:12:16", "font/letter-spacing/normal", "LETTER_SPACING"],
  fsXs: ["VariableID:10:8", "font/size/xs", "FONT_SIZE"],
  fsSm: ["VariableID:10:9", "font/size/sm", "FONT_SIZE"],
  fsMd: ["VariableID:10:10", "font/size/md", "FONT_SIZE"],
  fsLg: ["VariableID:10:11", "font/size/lg", "FONT_SIZE"],
  fsXl: ["VariableID:12:2", "font/size/xl", "FONT_SIZE"],
  fs2xl: ["VariableID:12:3", "font/size/2xl", "FONT_SIZE"],
  lhXs: ["VariableID:12:7", "font/line-height/xs", "LINE_HEIGHT"],
  lhSm: ["VariableID:12:8", "font/line-height/sm", "LINE_HEIGHT"],
  lhMd: ["VariableID:12:9", "font/line-height/md", "LINE_HEIGHT"],
  lhXl: ["VariableID:12:11", "font/line-height/xl", "LINE_HEIGHT"],
  spXs: ["VariableID:12:29", "spacing/xs", "GAP"],
  spSm: ["VariableID:12:30", "spacing/sm", "GAP"],
  spLg: ["VariableID:12:32", "spacing/lg", "GAP"],
  spXl: ["VariableID:12:33", "spacing/xl", "GAP"],
  radSm: ["VariableID:13:5", "radius/sm", "CORNER_RADIUS"],
  radXl: ["VariableID:13:8", "radius/xl", "CORNER_RADIUS"],
  szLg: ["VariableID:12:22", "size/lg", "WIDTH_HEIGHT"],
  szXl: ["VariableID:12:23", "size/xl", "WIDTH_HEIGHT"],
  sz2xl: ["VariableID:12:24", "size/2xl", "WIDTH_HEIGHT"],
  sz4xl: ["VariableID:12:26", "size/4xl", "WIDTH_HEIGHT"],
  sz6xl: ["VariableID:12:28", "size/6xl", "WIDTH_HEIGHT"],
  strokeXs: ["VariableID:12:41", "stroke/xs", "STROKE_FLOAT"]
};
const v = {};
for (const [k, [id, name, scope]] of Object.entries(tokenSpecs)) {
  const t = await figma.variables.getVariableByIdAsync(id);
  if (!t || t.name !== name || t.variableCollectionId !== "VariableCollectionId:6:2" || !t.scopes.includes(scope)) throw new Error("Token mismatch " + k);
  v[k] = t;
}
const fonts = await figma.listAvailableFontsAsync();
if (!fonts.some(f => f.fontName.family === "Manrope" && f.fontName.style === "Regular")) throw new Error("Manrope Regular unavailable");
await figma.loadFontAsync({ family: "Manrope", style: "Regular" });
const iconKeys = { CurrencyCircleDollar: "441865351ce8a0390c7544fee2348dd8ae895f51", ArrowUpRight: "8f20fac8635901c6627e086c16fdf197d5134b7f" };
const icons = {};
for (const [name, key] of Object.entries(iconKeys)) {
  const main = await figma.importComponentByKeyAsync(key);
  if (!main || main.key !== key) throw new Error("Icon import mismatch " + name);
  icons[name] = main;
}
const page = figma.createPage(); page.name = "Metric Cards"; await figma.setCurrentPageAsync(page);
const created = [page.id], mutated = [], components = [], details = [];
function solid(t) { return figma.variables.setBoundVariableForPaint({ type: "SOLID", color: { r: 1, g: 1, b: 1 } }, "color", t); }
function box(parent, name, w, h, direction, gap, gapVar) {
  const f = figma.createFrame(); f.name = name; f.resize(w, h); f.layoutMode = direction;
  f.primaryAxisSizingMode = "FIXED"; f.counterAxisSizingMode = "FIXED";
  f.primaryAxisAlignItems = "MIN"; f.counterAxisAlignItems = "CENTER";
  f.itemSpacing = gap; if (gapVar) f.setBoundVariable("itemSpacing", gapVar);
  f.fills = []; f.strokes = []; parent.appendChild(f); created.push(f.id); return f;
}
function textNode(parent, name, chars, size, height, width, fsVar, lhVar, color, propKey, visibleKey) {
  const t = figma.createText(); t.name = name; t.fontName = { family: "Manrope", style: "Regular" };
  t.characters = chars; t.fontSize = size; t.lineHeight = { unit: "PIXELS", value: height };
  t.letterSpacing = { unit: "PIXELS", value: 0 }; t.textAutoResize = "NONE"; t.resize(width, height);
  t.fills = [solid(color)]; t.setBoundVariable("fontFamily", v.family); t.setBoundVariable("fontStyle", v.regular);
  t.setBoundVariable("fontSize", fsVar); t.setBoundVariable("lineHeight", lhVar); t.setBoundVariable("letterSpacing", v.tracking);
  parent.appendChild(t); created.push(t.id);
  if (propKey || visibleKey) t.componentPropertyReferences = { ...(propKey ? { characters: propKey } : {}), ...(visibleKey ? { visible: visibleKey } : {}) };
  return t;
}
function icon(parent, name, size, sizeVar, propertyRefs) {
  const inst = icons[name].createInstance(); inst.name = name; inst.resize(size, size);
  inst.setBoundVariable("width", sizeVar); inst.setBoundVariable("height", sizeVar);
  parent.appendChild(inst); created.push(inst.id);
  for (const vector of inst.findAll(n => n.type === "VECTOR")) {
    if (vector.fills?.some(p => p.visible !== false) || vector.strokes?.some(p => p.visible !== false)) {
      if (vector.fills?.some(p => p.visible !== false)) vector.fills = [solid(v.iconBrand)];
      if (vector.strokes?.some(p => p.visible !== false)) vector.strokes = [solid(v.iconBrand)];
      mutated.push(vector.id);
    }
  }
  if (propertyRefs) inst.componentPropertyReferences = propertyRefs;
  return inst;
}
function radius(node, t) { node.cornerRadius = 16; for (const side of ["topLeftRadius","topRightRadius","bottomLeftRadius","bottomRightRadius"]) node.setBoundVariable(side, t); }
function padding(node, px, t) { node.paddingTop = node.paddingRight = node.paddingBottom = node.paddingLeft = px; for (const side of ["paddingTop","paddingRight","paddingBottom","paddingLeft"]) node.setBoundVariable(side, t); }
const specs = [
  { type: "Vertical Metric", size: "Large", id: "587:2747", w: 289, h: 256, x: 24, y: 24, contentW: 241, headerH: 64, contentH: 128 },
  { type: "Vertical Metric", size: "Small", id: "2838:2255", w: 200, h: 216, x: 469, y: 24, contentW: 168, headerH: 56, contentH: 112 },
  { type: "Horizontal Metric", size: "Large", id: "587:2748", w: 311, h: 192, x: 24, y: 328, contentW: 263, headerH: 64, contentH: 64 },
  { type: "Horizontal Metric", size: "Small", id: "2847:243", w: 232, h: 160, x: 469, y: 328, contentW: 200, headerH: 48, contentH: 64 },
  { type: "One Metric V1", size: "Large", id: "587:2749", w: 337, h: 156, x: 24, y: 568, contentW: 193, contentH: 108 },
  { type: "One Metric V1", size: "Small", id: "2847:258", w: 257, h: 116, x: 469, y: 568, contentW: 145, contentH: 84 },
  { type: "One Metric V2", size: "Large", id: "587:2750", w: 397, h: 144, x: 24, y: 767, contentW: 189, contentH: 96 },
  { type: "One Metric V2", size: "Small", id: "2847:266", w: 313, h: 112, x: 469, y: 767, contentW: 145, contentH: 80 }
];
for (const s of specs) {
  const lg = s.size === "Large", dual = s.type === "Vertical Metric" || s.type === "Horizontal Metric", vertical = s.type === "Vertical Metric", v2 = s.type === "One Metric V2";
  const p = lg ? 24 : 16, padVar = lg ? v.spXl : v.spLg, iconSize = v2 ? (lg ? 64 : 48) : (lg ? 32 : 24), iconVar = v2 ? (lg ? v.sz6xl : v.sz4xl) : (lg ? v.sz2xl : v.szXl), navSize = lg ? 32 : 24, navVar = lg ? v.sz2xl : v.szXl;
  const comp = figma.createComponent(); comp.name = "Type=" + s.type + ", Size=" + s.size; comp.resize(s.w, s.h);
  comp.layoutMode = dual ? "VERTICAL" : "HORIZONTAL"; comp.primaryAxisSizingMode = "FIXED"; comp.counterAxisSizingMode = "FIXED";
  comp.primaryAxisAlignItems = "MIN"; comp.counterAxisAlignItems = "CENTER"; comp.itemSpacing = 16; comp.setBoundVariable("itemSpacing", v.spLg);
  padding(comp, p, padVar); radius(comp, v.radXl);
  if (v2) { comp.fills = []; comp.strokes = [solid(v.borderSubtle)]; comp.strokeWeight = 1; comp.setBoundVariable("strokeWeight", v.strokeXs); }
  else { comp.fills = [solid(v.bgSubtle)]; comp.strokes = []; }
  page.appendChild(comp); created.push(comp.id);
  const titleKey = comp.addComponentProperty("Title", "TEXT", "Title");
  const showIconKey = comp.addComponentProperty("Show icon", "BOOLEAN", true);
  const iconKey = comp.addComponentProperty("Icon", "INSTANCE_SWAP", icons.CurrencyCircleDollar.id);
  const showActionKey = comp.addComponentProperty("Show action", "BOOLEAN", true);
  const showDetailKey = comp.addComponentProperty("Show detail", "BOOLEAN", true);
  let descriptionKey = null, amountKeys = null, valueKey = null, trendKey = null;
  if (dual) {
    descriptionKey = comp.addComponentProperty("Description", "TEXT", "Description");
    const sampleValue = vertical ? "$123,456.00" : "$123,320.00";
    amountKeys = [1,2].map(i => ({label: comp.addComponentProperty("Amount " + i + " label", "TEXT", "Amount " + i), value: comp.addComponentProperty("Amount " + i + " value", "TEXT", sampleValue)}));
  } else {
    valueKey = comp.addComponentProperty("Value", "TEXT", "$123,320.00");
    trendKey = comp.addComponentProperty("Trend", "TEXT", "+5.2%");
  }
  function addCategoryIcon(parent) { return icon(parent, "CurrencyCircleDollar", iconSize, iconVar, { visible: showIconKey, mainComponent: iconKey }); }
  function addNavigate(parent) {
    const nav = box(parent, "Navigate", navSize, navSize, "HORIZONTAL", 0, null);
    nav.primaryAxisAlignItems = "CENTER"; nav.counterAxisAlignItems = "CENTER"; padding(nav, 4, v.spXs); radius(nav, v.radSm);
    nav.fills = [solid(v2 ? v.bgSubtle : v.bgDefault)]; nav.componentPropertyReferences = { visible: showActionKey };
    icon(nav, "ArrowUpRight", lg ? 24 : 16, lg ? v.szXl : v.szLg, null);
    return nav;
  }
  if (dual) {
    const header = box(comp, "Header", s.contentW, s.headerH, "VERTICAL", 8, v.spSm);
    const titleRow = box(header, "Title row", s.contentW, lg ? 32 : 24, "HORIZONTAL", 16, v.spLg);
    addCategoryIcon(titleRow);
    const titleW = vertical ? (lg ? 145 : 88) : (lg ? 167 : 120);
    textNode(titleRow, "Title", "Title", lg ? 24 : 16, lg ? 24 : (vertical ? 16 : 24), titleW, lg ? v.fsXl : v.fsMd, lg ? v.lhMd : (vertical ? v.lhXs : v.lhMd), v.textPrimary, titleKey, null);
    addNavigate(titleRow);
    textNode(header, "Description", "Description", lg ? 14 : 12, vertical || lg ? 24 : 16, s.contentW, lg ? v.fsSm : v.fsXs, vertical || lg ? v.lhMd : v.lhXs, v.textSecondary, descriptionKey, showDetailKey);
    const content = box(comp, "Content", s.contentW, s.contentH, "VERTICAL", 16, v.spLg);
    for (const i of [0,1]) {
      const label = "Amount " + (i+1), value = vertical ? "$123,456.00" : "$123,320.00";
      if (vertical) {
        const amount = box(content, label, s.contentW, lg ? 56 : 48, "VERTICAL", 8, v.spSm);
        textNode(amount, "Label", label, lg ? 16 : 14, 16, s.contentW, lg ? v.fsMd : v.fsSm, v.lhXs, v.textPrimary, amountKeys[i].label, null);
        textNode(amount, "Value", value, lg ? 32 : 24, lg ? 32 : 24, s.contentW, lg ? v.fs2xl : v.fsXl, lg ? v.lhXl : v.lhMd, v.textPrimary, amountKeys[i].value, null);
      } else {
        const row = box(content, label, s.contentW, 24, "HORIZONTAL", lg ? 8 : 16, lg ? v.spSm : v.spLg); row.primaryAxisAlignItems = "SPACE_BETWEEN";
        textNode(row, "Label", label, lg ? 16 : 14, 20, lg ? 72 : 64, lg ? v.fsMd : v.fsSm, v.lhSm, v.textPrimary, amountKeys[i].label, null);
        textNode(row, "Value", value, lg ? 24 : 20, 24, lg ? 150 : 120, lg ? v.fsXl : v.fsLg, v.lhMd, v.textPrimary, amountKeys[i].value, null);
      }
    }
  } else {
    if (v2) {
      const tile = box(comp, "Icon tile", lg ? 96 : 80, lg ? 96 : 80, "HORIZONTAL", 0, null);
      tile.primaryAxisAlignItems = "CENTER"; tile.counterAxisAlignItems = "CENTER";
      padding(tile, lg ? 16 : 8, lg ? v.spLg : v.spSm); radius(tile, v.radXl); tile.fills = [solid(v.bgSubtle)];
      addCategoryIcon(tile);
    } else addCategoryIcon(comp);
    const content = box(comp, "Content", s.contentW, s.contentH, "VERTICAL", v2 ? (lg ? 8 : 4) : (lg ? 16 : 8), v2 ? (lg ? v.spSm : v.spXs) : (lg ? v.spLg : v.spSm));
    const titleSize = lg ? 24 : (v2 ? 16 : 20);
    textNode(content, "Title", "Title", titleSize, 24, s.contentW, lg ? v.fsXl : (v2 ? v.fsMd : v.fsLg), v.lhMd, v.textPrimary, titleKey, null);
    textNode(content, "Value", "$123,320.00", lg ? 32 : 24, lg ? 32 : 24, s.contentW, lg ? v.fs2xl : v.fsXl, lg ? v.lhXl : v.lhMd, v.textPrimary, valueKey, null);
    textNode(content, "Trend", "+5.2%", lg ? 16 : 14, v2 ? 24 : 20, s.contentW, lg ? v.fsMd : v.fsSm, v2 ? v.lhMd : v.lhSm, v.textTrend, trendKey, showDetailKey);
    addNavigate(comp);
  }
  components.push(comp); details.push({ id: comp.id, sourceId: s.id, type: s.type, size: s.size, box: [s.w,s.h] });
}
const set = figma.combineAsVariants(components, page); set.name = "Metric Card";
set.description = "Tarjeta de métricas en cuatro disposiciones y dos tamaños. Importes, etiquetas, título y tendencia editables como ejemplos. Navegación y actualización de datos requieren definición de producto.";
set.descriptionMarkdown = set.description; set.x = 80; set.y = 160;
for (const child of set.children) {
  const p = child.variantProperties; const s = specs.find(x => x.type === p.Type && x.size === p.Size);
  if (!s) throw new Error("Unexpected Metric Card variant " + child.name);
  child.x = s.x; child.y = s.y;
}
set.resizeWithoutConstraints(806, 935); created.push(set.id);
const title = figma.createText(); title.name = "Page title"; title.fontName = { family: "Manrope", style: "Regular" };
title.characters = "Metric Cards"; title.fontSize = 24; title.lineHeight = { unit: "PIXELS", value: 24 }; title.letterSpacing = { unit: "PIXELS", value: 0 };
title.fills = [solid(v.textPrimary)]; title.setBoundVariable("fontFamily", v.family); title.setBoundVariable("fontStyle", v.regular); title.setBoundVariable("fontSize", v.fsXl); title.setBoundVariable("lineHeight", v.lhMd); title.setBoundVariable("letterSpacing", v.tracking);
page.appendChild(title); title.x = 80; title.y = 80; created.push(title.id);
return { pageId: page.id, setId: set.id, iconMainIds: Object.fromEntries(Object.entries(icons).map(([k,n]) => [k,n.id])), variants: details, createdNodeIds: created, mutatedNodeIds: mutated, setSize: [set.width,set.height] };
