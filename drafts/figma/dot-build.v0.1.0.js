// DOT-001 · source-faithful visual reconstruction with semantic fill roles.
if (figma.root.children.some(p => p.name === "Dots")) throw new Error("Dots page already exists");
const ids = {
  active: ["VariableID:154:122", "color/background/status-active"],
  busy: ["VariableID:154:123", "color/background/status-busy"],
  inactive: ["VariableID:154:124", "color/background/status-inactive"],
  count: ["VariableID:154:125", "color/background/notification-count"],
  border: ["VariableID:13:18", "color/border/on-brand"],
  text: ["VariableID:13:33", "color/text/on-brand"],
  textPrimary: ["VariableID:13:27", "color/text/primary"],
  family: ["VariableID:10:2", "font/family/base"],
  bold: ["VariableID:10:6", "font/weight/bold"],
  regular: ["VariableID:10:3", "font/weight/regular"],
  docSize: ["VariableID:10:11", "font/size/lg"],
  docLine: ["VariableID:12:9", "font/line-height/md"],
  noteSize: ["VariableID:10:9", "font/size/sm"],
  noteLine: ["VariableID:12:8", "font/line-height/sm"],
  radius: ["VariableID:13:11", "radius/full"],
  stroke: ["VariableID:12:41", "stroke/xs"],
  size8: ["VariableID:12:20", "size/sm"],
  size12: ["VariableID:12:21", "size/md"],
  size16: ["VariableID:12:22", "size/lg"]
};
const v = {};
for (const [key, [id, name]] of Object.entries(ids)) {
  const x = await figma.variables.getVariableByIdAsync(id);
  if (!x || x.name !== name || x.variableCollectionId !== "VariableCollectionId:6:2") throw new Error("variable mismatch " + key);
  v[key] = x;
}
await figma.loadFontAsync({ family: "Manrope", style: "Bold" });
await figma.loadFontAsync({ family: "Manrope", style: "Regular" });
await figma.loadFontAsync({ family: "Manrope", style: "SemiBold" });
function solid(x) { return figma.variables.setBoundVariableForPaint({ type: "SOLID", color: { r: 1, g: 1, b: 1 } }, "color", x); }
const specs = { Small: { h: 8, sizeToken: v.size8, font: 4 }, Medium: { h: 12, sizeToken: v.size12, font: 8 }, Large: { h: 16, sizeToken: v.size16, font: 8 } };
const page = figma.createPage();
page.name = "Dots";
await figma.setCurrentPageAsync(page);
const created = [page.id], components = [], details = [];
for (const type of ["Active", "Busy", "Inactive", "Count", "Overflow"]) {
  for (const size of ["Large", "Medium", "Small"]) {
    const spec = specs[size];
    const width = type === "Overflow" ? size === "Small" ? 12 : 23 : spec.h;
    const comp = figma.createComponent();
    comp.name = "Type=" + type + ", Size=" + size;
    comp.resize(width, spec.h);
    comp.fills = [solid(v[type === "Active" ? "active" : type === "Busy" ? "busy" : type === "Inactive" ? "inactive" : "count"])];
    comp.strokes = [solid(v.border)];
    comp.strokeAlign = "OUTSIDE";
    comp.strokeWeight = 1;
    comp.cornerRadius = 9999;
    comp.layoutMode = "NONE";
    comp.clipsContent = false;
    for (const side of ["Top", "Right", "Bottom", "Left"]) comp.setBoundVariable("stroke" + side + "Weight", v.stroke);
    for (const corner of ["topLeftRadius", "topRightRadius", "bottomRightRadius", "bottomLeftRadius"]) comp.setBoundVariable(corner, v.radius);
    comp.setBoundVariable("height", spec.sizeToken);
    if (width !== 23) comp.setBoundVariable("width", type === "Overflow" && size === "Small" ? v.size12 : spec.sizeToken);
    page.appendChild(comp);
    created.push(comp.id);

    let textId = null, propertyKey = null;
    if (type === "Count" || type === "Overflow") {
      const value = type === "Count" ? "1" : "99+";
      propertyKey = comp.addComponentProperty(type === "Count" ? "Count" : "Overflow label", "TEXT", value);
      const t = figma.createText();
      t.name = type === "Count" ? "Count label" : "Overflow label";
      t.fontName = { family: "Manrope", style: "Bold" };
      t.characters = value;
      t.fontSize = spec.font;
      t.letterSpacing = { unit: "PERCENT", value: -2 };
      t.lineHeight = size === "Medium" ? { unit: "AUTO" } : { unit: "PERCENT", value: 160 };
      t.fills = [solid(v.text)];
      t.setBoundVariable("fontFamily", v.family);
      t.setBoundVariable("fontStyle", v.bold);
      t.textAutoResize = "WIDTH_AND_HEIGHT";
      comp.appendChild(t);
      t.x = (width - t.width) / 2;
      t.y = (spec.h - t.height) / 2;
      t.componentPropertyReferences = { characters: propertyKey };
      textId = t.id;
      created.push(t.id);
    }
    components.push(comp);
    details.push({ id: comp.id, type, size, wh: [width, spec.h], textId, propertyKey });
  }
}
const set = figma.combineAsVariants(components, page);
set.name = "Dot";
set.description = "Indicador visual compacto de presencia o conteo. Tipos Active, Busy, Inactive, Count y Overflow en tres tamaños. Los valores numéricos son ejemplos editables; Small tiene tipografía diminuta heredada y no sustituye un texto accesible de producto.";
set.descriptionMarkdown = set.description;
set.x = 80;
set.y = 160;
for (const child of set.children) {
  const p = child.variantProperties;
  const col = ["Large", "Medium", "Small"].indexOf(p.Size);
  const row = ["Active", "Busy", "Inactive", "Count", "Overflow"].indexOf(p.Type);
  if (col < 0 || row < 0) throw new Error("Unexpected Dot variant");
  child.x = 50 + col * 112;
  child.y = 48 + row * 74;
}
set.resizeWithoutConstraints(360, 420);
created.push(set.id);

const title = figma.createText();
title.name = "Page title";
title.fontName = { family: "Manrope", style: "SemiBold" };
title.characters = "Dots";
title.fontSize = 20;
title.lineHeight = { unit: "PIXELS", value: 24 };
title.fills = [solid(v.textPrimary)];
title.setBoundVariable("fontFamily", v.family);
title.setBoundVariable("fontStyle", await figma.variables.getVariableByIdAsync("VariableID:10:5"));
title.setBoundVariable("fontSize", v.docSize);
title.setBoundVariable("lineHeight", v.docLine);
page.appendChild(title);
title.x = 80;
title.y = 80;
created.push(title.id);
const note = figma.createText();
note.name = "Usage and accessibility note";
note.fontName = { family: "Manrope", style: "Regular" };
note.characters = "Active, Busy e Inactive indican presencia; Count y Overflow muestran ejemplos editables. El texto numérico Small de origen es demasiado pequeño para comunicar un conteo esencial: acompáñalo de una alternativa accesible. Auditoría humana pendiente.";
note.fontSize = 14;
note.lineHeight = { unit: "PIXELS", value: 20 };
note.fills = [solid(v.textPrimary)];
note.setBoundVariable("fontFamily", v.family);
note.setBoundVariable("fontStyle", v.regular);
note.setBoundVariable("fontSize", v.noteSize);
note.setBoundVariable("lineHeight", v.noteLine);
note.textAutoResize = "HEIGHT";
note.resize(700, 80);
page.appendChild(note);
note.x = 80;
note.y = 640;
created.push(note.id);
return { pageId: page.id, setId: set.id, variants: details, createdNodeIds: created };
