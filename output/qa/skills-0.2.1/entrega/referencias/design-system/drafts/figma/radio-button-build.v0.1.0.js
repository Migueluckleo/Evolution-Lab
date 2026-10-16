// RADIO-BUTTON-001 phase 3b. Public wrapper and documentation on the existing page.
figma.skipInvisibleInstanceChildren = false;
const page = await figma.getNodeByIdAsync("142:122");
const indicatorSet = await figma.getNodeByIdAsync("142:144");
if (!page || page.type !== "PAGE" || page.name !== "Radio Buttons") throw new Error("Radio page mismatch");
if (!indicatorSet || indicatorSet.type !== "COMPONENT_SET" || indicatorSet.name !== "Radio Indicator" || indicatorSet.children.length !== 8) throw new Error("Indicator set mismatch");
if (page.children.some(n => n.name === "Radio Button")) throw new Error("Public set exists; inspect before retrying");

const ids = {
  family: ["VariableID:10:2", "font/family/base"],
  weight: ["VariableID:10:3", "font/weight/regular"],
  size: ["VariableID:10:9", "font/size/sm"],
  lineHeight: ["VariableID:12:8", "font/line-height/sm"],
  tracking: ["VariableID:12:16", "font/letter-spacing/normal"],
  gap: ["VariableID:12:30", "spacing/sm"],
  textPrimary: ["VariableID:13:27", "color/text/primary"],
  textDisabled: ["VariableID:13:30", "color/text/disabled"],
  docWeight: ["VariableID:10:5", "font/weight/semibold"],
  docSize: ["VariableID:10:11", "font/size/lg"],
  docLineHeight: ["VariableID:12:9", "font/line-height/md"]
};
const vars = {};
for (const [key, [id, name]] of Object.entries(ids)) {
  const v = await figma.variables.getVariableByIdAsync(id);
  if (!v || v.name !== name || v.variableCollectionId !== "VariableCollectionId:6:2") throw new Error("Variable mismatch " + key);
  vars[key] = v;
}
await figma.loadFontAsync({ family: "Manrope", style: "Regular" });
await figma.loadFontAsync({ family: "Manrope", style: "SemiBold" });
await figma.setCurrentPageAsync(page);

function solid(v) {
  return figma.variables.setBoundVariableForPaint({ type: "SOLID", color: { r: 0, g: 0, b: 0 } }, "color", v);
}
function bindLabel(n, state) {
  n.fontName = { family: "Manrope", style: "Regular" };
  n.fontSize = 14;
  n.lineHeight = { unit: "PIXELS", value: 20 };
  n.letterSpacing = { unit: "PIXELS", value: 0 };
  n.fills = [solid(state === "Disabled" ? vars.textDisabled : vars.textPrimary)];
  n.setBoundVariable("fontFamily", vars.family);
  n.setBoundVariable("fontStyle", vars.weight);
  n.setBoundVariable("fontSize", vars.size);
  n.setBoundVariable("lineHeight", vars.lineHeight);
  n.setBoundVariable("letterSpacing", vars.tracking);
  n.textAutoResize = "WIDTH_AND_HEIGHT";
}

const sourceByKey = new Map(indicatorSet.children.map(c => [c.variantProperties.Selected + "/" + c.variantProperties.State, c]));
const components = [];
const variantDetails = [];
const created = [];
for (const selected of ["True", "False"]) {
  for (const state of ["Default", "Hover", "Focus", "Disabled"]) {
    const indicator = sourceByKey.get(selected + "/" + state);
    if (!indicator) throw new Error("Missing indicator " + selected + "/" + state);
    const component = figma.createComponent();
    component.name = "Selected=" + selected + ", State=" + state;
    component.resize(24, 24);
    component.layoutMode = "HORIZONTAL";
    component.primaryAxisAlignItems = "CENTER";
    component.counterAxisAlignItems = "CENTER";
    component.itemSpacing = 8;
    component.paddingTop = 0;
    component.paddingRight = 0;
    component.paddingBottom = 0;
    component.paddingLeft = 0;
    component.fills = [];
    component.strokes = [];
    component.clipsContent = false;
    component.setBoundVariable("itemSpacing", vars.gap);
    page.appendChild(component);
    created.push(component.id);

    const leftKey = component.addComponentProperty("Left label", "TEXT", "Field Label");
    const rightKey = component.addComponentProperty("Right label", "TEXT", "Field Label");
    const showLeftKey = component.addComponentProperty("Show left label", "BOOLEAN", false);
    const showRightKey = component.addComponentProperty("Show right label", "BOOLEAN", false);

    const left = figma.createText();
    left.name = "Left label";
    bindLabel(left, state);
    left.characters = "Field Label";
    component.appendChild(left);
    left.visible = false;
    left.componentPropertyReferences = { characters: leftKey, visible: showLeftKey };
    created.push(left.id);

    const instance = indicator.createInstance();
    instance.name = "Radio Indicator";
    component.appendChild(instance);
    created.push(instance.id);

    const right = figma.createText();
    right.name = "Right label";
    bindLabel(right, state);
    right.characters = "Field Label";
    component.appendChild(right);
    right.visible = false;
    right.componentPropertyReferences = { characters: rightKey, visible: showRightKey };
    created.push(right.id);

    component.layoutSizingHorizontal = "HUG";
    component.layoutSizingVertical = "HUG";
    components.push(component);
    variantDetails.push({ id: component.id, selected, state, leftId: left.id, indicatorId: instance.id, indicatorMainId: indicator.id, rightId: right.id, propertyKeys: [leftKey, rightKey, showLeftKey, showRightKey] });
  }
}
const set = figma.combineAsVariants(components, page);
set.name = "Radio Button";
set.description = "Opción visual de selección única. Selected True/False y State Default/Hover/Focus/Disabled; etiquetas izquierda y derecha editables, ocultas por defecto. Requiere grupo semántico y nombre accesible en implementación de producto.";
set.descriptionMarkdown = set.description;
set.x = 80;
set.y = 480;
for (const child of set.children) {
  const p = child.variantProperties;
  const col = ["Default", "Hover", "Focus", "Disabled"].indexOf(p.State);
  const row = ["True", "False"].indexOf(p.Selected);
  if (col < 0 || row < 0) throw new Error("Unexpected wrapper variant");
  child.x = 48 + col * 104;
  child.y = 48 + row * 88;
}
set.resizeWithoutConstraints(432, 208);
created.push(set.id);

const title = figma.createText();
title.name = "Page title";
title.fontName = { family: "Manrope", style: "SemiBold" };
title.characters = "Radio Buttons";
title.fontSize = 20;
title.lineHeight = { unit: "PIXELS", value: 24 };
title.fills = [solid(vars.textPrimary)];
title.setBoundVariable("fontFamily", vars.family);
title.setBoundVariable("fontStyle", vars.docWeight);
title.setBoundVariable("fontSize", vars.docSize);
title.setBoundVariable("lineHeight", vars.docLineHeight);
page.appendChild(title);
title.x = 80;
title.y = 80;
created.push(title.id);

const note = figma.createText();
note.name = "Usage note";
bindLabel(note, "Default");
note.characters = "Selecciona una opción de un grupo mutuamente excluyente. En uso real, cada opción necesita etiqueta clara y nombre accesible; aquí las etiquetas están ocultas por defecto. Auditoría humana pendiente.";
note.textAutoResize = "HEIGHT";
note.resize(700, 60);
page.appendChild(note);
note.x = 80;
note.y = 760;
created.push(note.id);

return { pageId: page.id, publicSetId: set.id, variants: variantDetails, createdNodeIds: created };
