// ICON-BUTTON-001 · build only after source/target contract QA and background-role readback PASS.
figma.skipInvisibleInstanceChildren = false;
if (figma.root.children.some(p => p.name === "Icon Buttons")) throw new Error("Icon Buttons page already exists");
const dotIds = { Small: "155:136", Medium: "155:134", Large: "155:132" };
const dots = {};
for (const [size, id] of Object.entries(dotIds)) {
  const n = await figma.getNodeByIdAsync(id);
  if (!n || n.type !== "COMPONENT" || n.name !== "Type=Count, Size=" + size || n.parent?.id !== "155:144") throw new Error("Dot Count dependency mismatch " + size);
  dots[size] = n;
}
const ids = {
  hoverBg: ["VariableID:180:122", "color/interactive/icon-button/hover-bg", "FRAME_FILL"],
  activeBg: ["VariableID:180:123", "color/interactive/icon-button/active-bg", "FRAME_FILL"],
  disabledBg: ["VariableID:13:65", "color/interactive/disabled/bg", "FRAME_FILL"],
  focusBg: ["VariableID:13:35", "color/background/default", "FRAME_FILL"],
  borderSubtle: ["VariableID:13:14", "color/border/subtle", "STROKE_COLOR"],
  borderDisabled: ["VariableID:13:17", "color/border/disabled", "STROKE_COLOR"],
  borderHover: ["VariableID:13:19", "color/border/hover", "STROKE_COLOR"],
  borderFocus: ["VariableID:13:71", "color/focus/ring", "STROKE_COLOR"],
  iconPrimary: ["VariableID:13:20", "color/icon/primary", "SHAPE_FILL"],
  iconDisabled: ["VariableID:13:24", "color/icon/disabled", "SHAPE_FILL"],
  iconOnBrand: ["VariableID:13:23", "color/icon/on-brand", "SHAPE_FILL"],
  textPrimary: ["VariableID:13:27", "color/text/primary", "TEXT_FILL"],
  family: ["VariableID:10:2", "font/family/base", "FONT_FAMILY"],
  regular: ["VariableID:10:3", "font/weight/regular", "FONT_STYLE"],
  semibold: ["VariableID:10:5", "font/weight/semibold", "FONT_STYLE"],
  docSize: ["VariableID:10:11", "font/size/lg", "FONT_SIZE"],
  noteSize: ["VariableID:10:9", "font/size/sm", "FONT_SIZE"],
  docLine: ["VariableID:12:9", "font/line-height/md", "LINE_HEIGHT"],
  noteLine: ["VariableID:12:8", "font/line-height/sm", "LINE_HEIGHT"],
  tracking: ["VariableID:12:16", "font/letter-spacing/normal", "LETTER_SPACING"],
  gapNone: ["VariableID:12:18", "spacing/none", "GAP"],
  paddingSmall: ["VariableID:12:29", "spacing/xs", "GAP"],
  paddingMedium: ["VariableID:12:30", "spacing/sm", "GAP"],
  radius: ["VariableID:13:6", "radius/md", "CORNER_RADIUS"],
  stroke: ["VariableID:12:41", "stroke/xs", "STROKE_FLOAT"],
  body24: ["VariableID:12:23", "size/xl", "WIDTH_HEIGHT"],
  body48: ["VariableID:12:26", "size/4xl", "WIDTH_HEIGHT"],
  body56: ["VariableID:12:27", "size/5xl", "WIDTH_HEIGHT"],
  icon16: ["VariableID:12:22", "size/lg", "WIDTH_HEIGHT"],
  icon24: ["VariableID:12:23", "size/xl", "WIDTH_HEIGHT"],
  icon32: ["VariableID:12:24", "size/2xl", "WIDTH_HEIGHT"]
};
const v = {};
for (const [k, [id, name, scope]] of Object.entries(ids)) {
  const x = await figma.variables.getVariableByIdAsync(id);
  if (!x || x.name !== name || x.variableCollectionId !== "VariableCollectionId:6:2" || !x.scopes.includes(scope)) throw new Error("variable mismatch " + k);
  v[k] = x;
}
await figma.loadFontAsync({ family: "Manrope", style: "Regular" });
await figma.loadFontAsync({ family: "Manrope", style: "SemiBold" });
const bellMain = await figma.importComponentByKeyAsync("ef703d88cfc6792cdd17351c4cc923a019b91855");
if (!bellMain || bellMain.type !== "COMPONENT" || bellMain.key !== "ef703d88cfc6792cdd17351c4cc923a019b91855") throw new Error("Bell Phosphor import mismatch");
const page = figma.createPage();
page.name = "Icon Buttons";
await figma.setCurrentPageAsync(page);
const created = [page.id], mutated = [], components = [], details = [];
function solid(variable) { return figma.variables.setBoundVariableForPaint({ type: "SOLID", color: { r: 1, g: 1, b: 1 } }, "color", variable); }
const sizeSpecs = {
  Small: { body: 24, icon: 16, dot: 8, pad: 4, bodyToken: v.body24, iconToken: v.icon16, padToken: v.paddingSmall, dotMain: dots.Small, dotX: 12, dotY: 12 },
  Medium: { body: 48, icon: 24, dot: 12, pad: 8, bodyToken: v.body48, iconToken: v.icon24, padToken: v.paddingMedium, dotMain: dots.Medium, dotX: 24, dotY: 18 },
  Large: { body: 56, icon: 32, dot: 16, pad: 8, bodyToken: v.body56, iconToken: v.icon32, padToken: v.paddingMedium, dotMain: dots.Large, dotX: 28, dotY: 20 }
};
for (const style of ["Ghost", "Outline"]) {
  for (const state of ["Default", "Disabled", "Hover", "Focus", "Active"]) {
    for (const size of ["Small", "Medium", "Large"]) {
      const s = sizeSpecs[size];
      const comp = figma.createComponent();
      comp.name = "Style=" + style + ", Size=" + size + ", State=" + state;
      comp.resize(s.body, s.body);
      comp.layoutMode = "HORIZONTAL";
      comp.primaryAxisSizingMode = "FIXED";
      comp.counterAxisSizingMode = "FIXED";
      comp.primaryAxisAlignItems = "CENTER";
      comp.counterAxisAlignItems = "CENTER";
      comp.paddingTop = s.pad; comp.paddingRight = s.pad; comp.paddingBottom = s.pad; comp.paddingLeft = s.pad;
      comp.itemSpacing = 0;
      for (const side of ["Top", "Right", "Bottom", "Left"]) comp.setBoundVariable("padding" + side, s.padToken);
      comp.setBoundVariable("itemSpacing", v.gapNone);
      comp.setBoundVariable("width", s.bodyToken);
      comp.setBoundVariable("height", s.bodyToken);
      comp.cornerRadius = 8;
      for (const corner of ["topLeftRadius", "topRightRadius", "bottomRightRadius", "bottomLeftRadius"]) comp.setBoundVariable(corner, v.radius);
      comp.strokes = [];
      comp.fills = [];
      comp.clipsContent = false;
      if (state === "Hover") comp.fills = [solid(v.hoverBg)];
      if (state === "Active") comp.fills = [solid(v.activeBg)];
      if (state === "Focus") comp.fills = [solid(v.focusBg)];
      if (style === "Outline" && state === "Disabled") comp.fills = [solid(v.disabledBg)];
      let strokeVar = null;
      if (state === "Focus") strokeVar = v.borderFocus;
      else if (style === "Outline") strokeVar = state === "Disabled" ? v.borderDisabled : state === "Hover" ? v.borderHover : v.borderSubtle;
      if (strokeVar) {
        comp.strokes = [solid(strokeVar)];
        comp.strokeWeight = 1;
        comp.strokeAlign = "INSIDE";
        for (const side of ["Top", "Right", "Bottom", "Left"]) comp.setBoundVariable("stroke" + side + "Weight", v.stroke);
      }
      page.appendChild(comp);
      created.push(comp.id);
      const iconKey = comp.addComponentProperty("Icon", "INSTANCE_SWAP", bellMain.id);
      const showCountKey = comp.addComponentProperty("Show count", "BOOLEAN", true);
      const bell = bellMain.createInstance();
      bell.name = "Bell icon";
      bell.resize(s.icon, s.icon);
      bell.setBoundVariable("width", s.iconToken);
      bell.setBoundVariable("height", s.iconToken);
      comp.appendChild(bell);
      bell.componentPropertyReferences = { mainComponent: iconKey };
      created.push(bell.id);
      const iconColor = state === "Disabled" ? v.iconDisabled : state === "Active" ? v.iconOnBrand : v.iconPrimary;
      const vectors = bell.findAll(n => n.type === "VECTOR");
      if (!vectors.length) throw new Error("Bell has no vector");
      for (const vector of vectors) { vector.fills = [solid(iconColor)]; mutated.push(vector.id); }
      const dot = s.dotMain.createInstance();
      dot.name = "Count indicator";
      comp.appendChild(dot);
      dot.layoutPositioning = "ABSOLUTE";
      dot.x = s.dotX; dot.y = s.dotY;
      dot.componentPropertyReferences = { visible: showCountKey };
      created.push(dot.id);
      components.push(comp);
      details.push({ id: comp.id, style, size, state, bellId: bell.id, bellVectorIds: vectors.map(n => n.id), dotId: dot.id, iconKey, showCountKey, box: [comp.width, comp.height], dotPosition: [dot.x, dot.y] });
    }
  }
}
const set = figma.combineAsVariants(components, page);
set.name = "Icon Button";
set.description = "Acción iconográfica visual en Ghost u Outline, tres tamaños y cinco estados. El Bell es reemplazable y el Count opcional es una instancia de Dot. El producto debe definir acción, nombre accesible, foco por teclado y comunicación del conteo.";
set.descriptionMarkdown = set.description;
set.x = 80; set.y = 160;
const stateRows = { Default: 0, Disabled: 2, Hover: 4, Focus: 6, Active: 8 };
const colX = { Small: 32, Medium: 112, Large: 204 };
const offsetY = { Small: 32, Medium: 24, Large: 21 };
for (const child of set.children) {
  const p = child.variantProperties;
  if (!(p.State in stateRows) || !(p.Size in colX) || !["Ghost", "Outline"].includes(p.Style)) throw new Error("Unexpected Icon Button variant");
  const row = stateRows[p.State] + (p.Style === "Outline" ? 1 : 0);
  child.x = colX[p.Size]; child.y = offsetY[p.Size] + row * 96;
}
set.resizeWithoutConstraints(289, 960);
created.push(set.id);
const title = figma.createText();
title.name = "Page title";
title.fontName = { family: "Manrope", style: "SemiBold" };
title.characters = "Icon Buttons";
title.fontSize = 20;
title.lineHeight = { unit: "PIXELS", value: 24 };
title.letterSpacing = { unit: "PIXELS", value: 0 };
title.fills = [solid(v.textPrimary)];
title.setBoundVariable("fontFamily", v.family);
title.setBoundVariable("fontStyle", v.semibold);
title.setBoundVariable("fontSize", v.docSize);
title.setBoundVariable("lineHeight", v.docLine);
title.setBoundVariable("letterSpacing", v.tracking);
page.appendChild(title); title.x = 80; title.y = 80;
created.push(title.id);
const note = figma.createText();
note.name = "Usage and accessibility note";
note.fontName = { family: "Manrope", style: "Regular" };
note.characters = "Bell y Count son ejemplos. Define nombre accesible y acción en producto; Small 24 px y Count Small 4 px no son por sí solos suficientes para uso táctil o lectura de un dato. Auditoría humana pendiente.";
note.fontSize = 14;
note.lineHeight = { unit: "PIXELS", value: 20 };
note.letterSpacing = { unit: "PIXELS", value: 0 };
note.fills = [solid(v.textPrimary)];
note.resize(750, 80); note.textAutoResize = "HEIGHT";
note.setBoundVariable("fontFamily", v.family);
note.setBoundVariable("fontStyle", v.regular);
note.setBoundVariable("fontSize", v.noteSize);
note.setBoundVariable("lineHeight", v.noteLine);
note.setBoundVariable("letterSpacing", v.tracking);
page.appendChild(note); note.x = 80; note.y = 1210;
created.push(note.id);
return { pageId: page.id, setId: set.id, importedBellMainId: bellMain.id, variants: details, createdNodeIds: created, mutatedNodeIds: mutated, setBounds: [set.width, set.height] };
