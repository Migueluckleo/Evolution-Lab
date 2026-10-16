// CHECKBOX-001 · build only after source contract QA and Radio color extension QA.
figma.skipInvisibleInstanceChildren = false;
if (figma.root.children.some(p => p.name === "Checkboxes")) throw new Error("Checkboxes page already exists");
const checkMain = await figma.getNodeByIdAsync("148:125");
const minusMain = await figma.getNodeByIdAsync("148:156");
if (!checkMain || checkMain.key !== "b0e1ef9e3dcc90870bbf7ef05b8ee937890eb31d") throw new Error("Check import mismatch");
if (!minusMain || minusMain.key !== "10ad6c579ecb00c883f839281ca2ad812962a324") throw new Error("Minus import mismatch");
const styles = await figma.getLocalEffectStylesAsync();
const focusStyle = styles.find(s => s.id === "S:dea3da42f15a5819697eb5bd5c53429d8ebf7180,");
if (!focusStyle || focusStyle.name !== "Focus/Selection Outset" || focusStyle.effects.length !== 2) throw new Error("Shared focus style mismatch");

const ids = {
  selected: ["VariableID:140:122", "color/background/control-selected"],
  selectedHover: ["VariableID:140:123", "color/background/control-selected-hover"],
  bgDisabled: ["VariableID:13:38", "color/background/disabled"],
  borderControl: ["VariableID:123:122", "color/border/control"],
  borderHover: ["VariableID:13:19", "color/border/hover"],
  borderDisabled: ["VariableID:13:17", "color/border/disabled"],
  iconOnBrand: ["VariableID:13:23", "color/icon/on-brand"],
  textPrimary: ["VariableID:13:27", "color/text/primary"],
  textDisabled: ["VariableID:13:30", "color/text/disabled"],
  family: ["VariableID:10:2", "font/family/base"],
  weight: ["VariableID:10:3", "font/weight/regular"],
  size: ["VariableID:10:9", "font/size/sm"],
  lineHeight: ["VariableID:12:8", "font/line-height/sm"],
  tracking: ["VariableID:12:16", "font/letter-spacing/normal"],
  gap: ["VariableID:12:30", "spacing/sm"],
  radius: ["VariableID:13:5", "radius/sm"],
  stroke: ["VariableID:13:3", "stroke/md"],
  iconSize: ["VariableID:12:21", "size/md"],
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

function solid(v) {
  return figma.variables.setBoundVariableForPaint({ type: "SOLID", color: { r: 1, g: 1, b: 1 } }, "color", v);
}
function bindText(n, disabled) {
  n.fontName = { family: "Manrope", style: "Regular" };
  n.fontSize = 14;
  n.lineHeight = { unit: "PIXELS", value: 20 };
  n.letterSpacing = { unit: "PIXELS", value: 0 };
  n.fills = [solid(disabled ? vars.textDisabled : vars.textPrimary)];
  n.setBoundVariable("fontFamily", vars.family);
  n.setBoundVariable("fontStyle", vars.weight);
  n.setBoundVariable("fontSize", vars.size);
  n.setBoundVariable("lineHeight", vars.lineHeight);
  n.setBoundVariable("letterSpacing", vars.tracking);
  n.textAutoResize = "WIDTH_AND_HEIGHT";
}

const page = figma.createPage();
page.name = "Checkboxes";
await figma.setCurrentPageAsync(page);
const created = [page.id];
const components = [];
const details = [];
for (const selection of ["Selected", "Indeterminate", "Unselected"]) {
  for (const state of ["Default", "Hover", "Focus", "Disabled"]) {
    const comp = figma.createComponent();
    comp.name = "Selection=" + selection + ", State=" + state;
    comp.resize(24, 24);
    comp.layoutMode = "HORIZONTAL";
    comp.primaryAxisAlignItems = "CENTER";
    comp.counterAxisAlignItems = "CENTER";
    comp.itemSpacing = 8;
    comp.paddingTop = 0;
    comp.paddingRight = 0;
    comp.paddingBottom = 0;
    comp.paddingLeft = 0;
    comp.fills = [];
    comp.strokes = [];
    comp.clipsContent = false;
    comp.setBoundVariable("itemSpacing", vars.gap);
    page.appendChild(comp);
    created.push(comp.id);

    const leftTextKey = comp.addComponentProperty("Left label", "TEXT", "Field Label");
    const rightTextKey = comp.addComponentProperty("Right label", "TEXT", "Field Label");
    const leftVisibleKey = comp.addComponentProperty("Show left label", "BOOLEAN", false);
    const rightVisibleKey = comp.addComponentProperty("Show right label", "BOOLEAN", false);
    const left = figma.createText();
    left.name = "Left label";
    bindText(left, state === "Disabled");
    left.characters = "Field Label";
    comp.appendChild(left);
    left.visible = false;
    left.componentPropertyReferences = { characters: leftTextKey, visible: leftVisibleKey };
    created.push(left.id);

    const content = figma.createFrame();
    content.name = "Checkbox indicator";
    content.resize(24, 24);
    content.layoutMode = "NONE";
    content.fills = [];
    content.strokes = [];
    content.clipsContent = false;
    comp.appendChild(content);
    created.push(content.id);
    const box = figma.createRectangle();
    box.name = selection === "Unselected" ? "Unselected outline" : "Selected box";
    box.resize(18, 18);
    box.cornerRadius = 4;
    for (const corner of ["topLeftRadius", "topRightRadius", "bottomRightRadius", "bottomLeftRadius"]) box.setBoundVariable(corner, vars.radius);
    box.strokes = [];
    if (selection === "Unselected") {
      box.fills = [];
      box.strokes = [solid(vars[state === "Hover" ? "borderHover" : state === "Disabled" ? "borderDisabled" : "borderControl"])];
      box.strokeWeight = 2;
      box.strokeAlign = state === "Focus" ? "OUTSIDE" : "INSIDE";
      box.setBoundVariable("strokeWeight", vars.stroke);
    } else {
      box.fills = [solid(vars[state === "Hover" ? "selectedHover" : state === "Disabled" ? "bgDisabled" : "selected"])];
    }
    content.appendChild(box);
    box.x = 3;
    box.y = 3;
    if (state === "Focus") box.effectStyleId = focusStyle.id;
    created.push(box.id);

    let iconId = null;
    let vectorIds = [];
    if (selection !== "Unselected") {
      const main = selection === "Selected" ? checkMain : minusMain;
      const icon = main.createInstance();
      icon.name = selection === "Selected" ? "Check" : "Minus";
      icon.resize(12, 12);
      icon.setBoundVariable("width", vars.iconSize);
      icon.setBoundVariable("height", vars.iconSize);
      content.appendChild(icon);
      icon.x = 6;
      icon.y = 6;
      for (const vector of icon.findAll(n => n.type === "VECTOR")) {
        vector.fills = [solid(vars.iconOnBrand)];
        vectorIds.push(vector.id);
        created.push(vector.id);
      }
      if (!vectorIds.length) throw new Error("Imported icon has no vector in " + selection + "/" + state);
      iconId = icon.id;
      created.push(icon.id);
    }

    const right = figma.createText();
    right.name = "Right label";
    bindText(right, state === "Disabled");
    right.characters = "Field Label";
    comp.appendChild(right);
    right.visible = false;
    right.componentPropertyReferences = { characters: rightTextKey, visible: rightVisibleKey };
    created.push(right.id);
    comp.layoutSizingHorizontal = "HUG";
    comp.layoutSizingVertical = "HUG";
    components.push(comp);
    details.push({ id: comp.id, selection, state, leftId: left.id, indicatorId: content.id, boxId: box.id, iconId, vectorIds, rightId: right.id });
  }
}
const set = figma.combineAsVariants(components, page);
set.name = "Checkbox";
set.description = "Control visual Selected, Indeterminate o Unselected con estados Default, Hover, Focus y Disabled. Etiquetas opcionales editables y ocultas por defecto. La selección funcional, el grupo y el nombre accesible deben definirse en producto.";
set.descriptionMarkdown = set.description;
set.x = 80;
set.y = 160;
for (const child of set.children) {
  const p = child.variantProperties;
  const col = ["Default", "Hover", "Focus", "Disabled"].indexOf(p.State);
  const row = ["Selected", "Indeterminate", "Unselected"].indexOf(p.Selection);
  if (col < 0 || row < 0) throw new Error("Unexpected Checkbox variant");
  child.x = 48 + col * 104;
  child.y = 48 + row * 88;
}
set.resizeWithoutConstraints(432, 296);
created.push(set.id);

const title = figma.createText();
title.name = "Page title";
title.fontName = { family: "Manrope", style: "SemiBold" };
title.characters = "Checkboxes";
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
bindText(note, false);
note.characters = "Permite seleccionar una o más opciones de un grupo. Selected, Indeterminate y Unselected son apariencias visuales; cada uso real necesita etiqueta clara y nombre accesible. Auditoría humana pendiente.";
note.textAutoResize = "HEIGHT";
note.resize(700, 60);
page.appendChild(note);
note.x = 80;
note.y = 520;
created.push(note.id);
return { pageId: page.id, setId: set.id, focusStyleId: focusStyle.id, variants: details, createdNodeIds: created };
