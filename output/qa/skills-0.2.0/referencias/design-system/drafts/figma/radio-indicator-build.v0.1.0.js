// RADIO-BUTTON-001 phase 3a. Run only after the two semantic fill variables exist.
figma.skipInvisibleInstanceChildren = false;

if (figma.root.children.some(p => p.name === "Radio Buttons")) {
  throw new Error("Radio Buttons page already exists; inspect before retrying");
}
const ids = {
  selected: ["VariableID:140:122", "color/background/control-selected"],
  selectedHover: ["VariableID:140:123", "color/background/control-selected-hover"],
  background: ["VariableID:13:35", "color/background/default"],
  disabled: ["VariableID:13:38", "color/background/disabled"],
  borderControl: ["VariableID:123:122", "color/border/control"],
  borderHover: ["VariableID:13:19", "color/border/hover"],
  borderBrand: ["VariableID:13:16", "color/border/brand"],
  borderDisabled: ["VariableID:13:17", "color/border/disabled"],
  focusOuter: ["VariableID:136:122", "color/focus/effect-outer"],
  focusInner: ["VariableID:136:123", "color/focus/effect-inner"],
  stroke: ["VariableID:13:3", "stroke/md"]
};
const vars = {};
for (const [key, [id, name]] of Object.entries(ids)) {
  const v = await figma.variables.getVariableByIdAsync(id);
  if (!v || v.name !== name || v.variableCollectionId !== "VariableCollectionId:6:2") {
    throw new Error("Semantic variable mismatch: " + key);
  }
  vars[key] = v;
}
if (typeof figma.variables.setBoundVariableForEffect !== "function") {
  throw new Error("Effect variable binding unavailable");
}

function solid(v) {
  return figma.variables.setBoundVariableForPaint(
    { type: "SOLID", color: { r: 1, g: 1, b: 1 } }, "color", v
  );
}
function focusEffect(variable, spread) {
  return figma.variables.setBoundVariableForEffect({
    type: "DROP_SHADOW", visible: true, radius: 0,
    color: { r: 1, g: 1, b: 1, a: 1 }, offset: { x: 0, y: 0 },
    spread, blendMode: "NORMAL", showShadowBehindNode: false
  }, "color", variable);
}

const page = figma.createPage();
page.name = "Radio Buttons";
await figma.setCurrentPageAsync(page);
const created = [page.id];

const style = figma.createEffectStyle();
style.name = "Focus/Selection Outset";
style.description = "Anillo exterior 4 px e interior 2 px para controles de selección; ambos colores ligados a variables semánticas EFFECT_COLOR.";
style.effects = [focusEffect(vars.focusOuter, 4), focusEffect(vars.focusInner, 2)];

const components = [];
const details = [];
for (const selected of ["True", "False"]) {
  for (const state of ["Default", "Hover", "Focus", "Disabled"]) {
    const component = figma.createComponent();
    component.name = "Selected=" + selected + ", State=" + state;
    component.resize(24, 24);
    component.fills = [];
    component.strokes = [];
    component.clipsContent = false;
    page.appendChild(component);
    created.push(component.id);

    const outer = figma.createEllipse();
    outer.name = selected === "True" ? "Selected disc" : "Unselected ring";
    outer.resize(18, 18);
    outer.strokes = [];
    if (selected === "True") {
      outer.fills = [solid(vars[state === "Hover" ? "selectedHover" : state === "Disabled" ? "disabled" : "selected"])];
    } else {
      outer.fills = [solid(vars.background)];
      const borderKey = state === "Default" ? "borderControl" : state === "Hover" ? "borderHover" : state === "Focus" ? "borderBrand" : "borderDisabled";
      outer.strokes = [solid(vars[borderKey])];
      outer.strokeAlign = "INSIDE";
      outer.strokeWeight = 2;
      outer.setBoundVariable("strokeWeight", vars.stroke);
    }
    component.appendChild(outer);
    outer.x = 3;
    outer.y = 3;
    if (state === "Focus") outer.effectStyleId = style.id;
    created.push(outer.id);

    let innerId = null;
    if (selected === "True") {
      const inner = figma.createEllipse();
      inner.name = "Selected center";
      inner.resize(8, 8);
      inner.fills = [solid(vars.background)];
      inner.strokes = [];
      component.appendChild(inner);
      inner.x = 8;
      inner.y = 8;
      innerId = inner.id;
      created.push(inner.id);
    }
    components.push(component);
    details.push({ id: component.id, selected, state, outerId: outer.id, innerId });
  }
}
const set = figma.combineAsVariants(components, page);
set.name = "Radio Indicator";
set.description = "Indicador visual local de Radio Button: Selected True/False × State Default/Hover/Focus/Disabled. Rellenos, bordes y foco vinculados a variables semánticas de AI Design System.";
set.descriptionMarkdown = set.description;
set.x = 80;
set.y = 160;
for (const child of set.children) {
  const p = child.variantProperties;
  const col = ["Default", "Hover", "Focus", "Disabled"].indexOf(p.State);
  const row = ["True", "False"].indexOf(p.Selected);
  if (col < 0 || row < 0) throw new Error("Unexpected indicator variant");
  child.x = 48 + col * 104;
  child.y = 48 + row * 88;
}
set.resizeWithoutConstraints(432, 208);
created.push(set.id);
return { pageId: page.id, indicatorSetId: set.id, focusStyleId: style.id, variants: details, createdNodeIds: created };
