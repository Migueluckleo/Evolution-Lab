// TOGGLE-001 · one-page Figma construction, adapted from the library skill's
// createComponentWithVariants and bindVariablesToComponent helpers.
figma.skipInvisibleInstanceChildren = false;

const expectedPages = ["Buttons", "Chips", "Tooltips", "Badges"];
const currentPages = figma.root.children.map(p => p.name);
if (currentPages.includes("Toggles")) throw new Error("Toggles page already exists");
if (expectedPages.some(name => !currentPages.includes(name))) throw new Error("Expected destination pages missing");

const ids = {
  family: ["VariableID:10:2", "font/family/base"],
  weight: ["VariableID:10:3", "font/weight/regular"],
  size: ["VariableID:10:9", "font/size/sm"],
  lineHeight: ["VariableID:12:7", "font/line-height/xs"],
  letterSpacing: ["VariableID:12:16", "font/letter-spacing/normal"],
  gap: ["VariableID:12:30", "spacing/sm"],
  stroke: ["VariableID:12:41", "stroke/xs"],
  radius: ["VariableID:13:11", "radius/full"],
  borderDefault: ["VariableID:13:13", "color/border/default"],
  borderStrong: ["VariableID:13:15", "color/border/strong"],
  borderBrand: ["VariableID:13:16", "color/border/brand"],
  borderDisabled: ["VariableID:13:17", "color/border/disabled"],
  borderHover: ["VariableID:13:19", "color/border/hover"],
  iconOnBrand: ["VariableID:13:23", "color/icon/on-brand"],
  textPrimary: ["VariableID:13:27", "color/text/primary"],
  textTertiary: ["VariableID:13:29", "color/text/tertiary"],
  textDisabled: ["VariableID:13:30", "color/text/disabled"],
  bgDefault: ["VariableID:13:35", "color/background/default"],
  bgMuted: ["VariableID:13:37", "color/background/muted"],
  bgDisabled: ["VariableID:13:38", "color/background/disabled"],
  primaryDefault: ["VariableID:13:57", "color/interactive/primary/default"],
  primaryHover: ["VariableID:13:58", "color/interactive/primary/hover"],
  interactiveDisabled: ["VariableID:13:65", "color/interactive/disabled/bg"],
  focusRing: ["VariableID:13:71", "color/focus/ring"],
  docWeight: ["VariableID:10:5", "font/weight/semibold"],
  docSize: ["VariableID:10:11", "font/size/lg"],
  docLineHeight: ["VariableID:12:9", "font/line-height/md"]
};
const vars = {};
for (const [key, [id, name]] of Object.entries(ids)) {
  const v = await figma.variables.getVariableByIdAsync(id);
  if (!v || v.name !== name || v.variableCollectionId !== "VariableCollectionId:6:2") {
    throw new Error("Missing or mismatched semantic variable " + key);
  }
  if (Object.keys(v.valuesByMode).length !== 4) throw new Error("Mode count mismatch for " + key);
  vars[key] = v;
}
if (typeof figma.variables.setBoundVariableForEffect !== "function") throw new Error("Effect binding unavailable");
await figma.loadFontAsync({ family: "Manrope", style: "Regular" });
await figma.loadFontAsync({ family: "Manrope", style: "SemiBold" });

const page = figma.createPage();
page.name = "Toggles";
await figma.setCurrentPageAsync(page);
const created = [page.id];

function solid(variable) {
  return figma.variables.setBoundVariableForPaint(
    { type: "SOLID", color: { r: 0.5, g: 0.5, b: 0.5 } },
    "color",
    variable
  );
}
function bindText(node, fillVar) {
  node.fontName = { family: "Manrope", style: "Regular" };
  node.fontSize = 14;
  node.lineHeight = { unit: "PIXELS", value: 16 };
  node.letterSpacing = { unit: "PIXELS", value: 0 };
  node.fills = [solid(fillVar)];
  node.setBoundVariable("fontFamily", vars.family);
  node.setBoundVariable("fontStyle", vars.weight);
  node.setBoundVariable("fontSize", vars.size);
  node.setBoundVariable("lineHeight", vars.lineHeight);
  node.setBoundVariable("letterSpacing", vars.letterSpacing);
}
function innerEffects() {
  return [
    { type: "INNER_SHADOW", visible: true, radius: 4.1666665, color: { r: 0, g: 0, b: 0, a: 0.1 }, offset: { x: 1.6666666, y: 1.6666666 }, spread: 0, blendMode: "NORMAL" },
    { type: "INNER_SHADOW", visible: true, radius: 1.6666666, color: { r: 0, g: 0, b: 0, a: 0.5 }, offset: { x: 0, y: 0.4166667 }, spread: 0, blendMode: "NORMAL" },
    { type: "INNER_SHADOW", visible: true, radius: 0, color: { r: 0, g: 0, b: 0, a: 0.25 }, offset: { x: 0, y: 0.8333333 }, spread: 0, blendMode: "NORMAL" }
  ];
}
function focusEffects(isOn) {
  const ring = figma.variables.setBoundVariableForEffect(
    { type: "DROP_SHADOW", visible: true, radius: 0, color: { r: 0.11372549, g: 0.12941177, b: 0.6901961, a: 1 }, offset: { x: 0, y: 0 }, spread: 3.3333333, blendMode: "NORMAL", showShadowBehindNode: false },
    "color",
    vars.focusRing
  );
  const gap = figma.variables.setBoundVariableForEffect(
    { type: "DROP_SHADOW", visible: true, radius: 0, color: { r: 1, g: 1, b: 1, a: 1 }, offset: { x: 0, y: 0 }, spread: 1.6666666, blendMode: "NORMAL", showShadowBehindNode: false },
    "color",
    vars.bgDefault
  );
  return isOn ? [ring, gap] : [ring, gap, ...innerEffects()];
}

const map = {
  "On/Default": ["primaryDefault", "borderBrand", "bgDefault", "textPrimary"],
  "On/Hover": ["primaryHover", "borderHover", "bgDefault", "textPrimary"],
  "On/Focus": ["primaryDefault", "borderBrand", "bgDefault", "textPrimary"],
  "On/Disabled": ["interactiveDisabled", "borderDisabled", "bgMuted", "textDisabled"],
  "Off/Default": ["bgMuted", "borderStrong", "bgDefault", "textPrimary"],
  "Off/Hover": ["textTertiary", "borderDefault", "bgDefault", "textPrimary"],
  "Off/Focus": ["bgMuted", "borderStrong", "bgDefault", "textPrimary"],
  "Off/Disabled": ["bgDisabled", "borderDisabled", "iconOnBrand", "textDisabled"]
};
const components = [];
const variantDetails = [];
for (const toggle of ["On", "Off"]) {
  for (const state of ["Default", "Hover", "Focus", "Disabled"]) {
    const key = toggle + "/" + state;
    const [trackRole, borderRole, thumbRole, labelRole] = map[key];
    const comp = figma.createComponent();
    comp.name = "Toggle=" + toggle + ", State=" + state;
    comp.fills = [];
    comp.strokes = [];
    comp.resize(40, 20);
    comp.layoutMode = "HORIZONTAL";
    comp.primaryAxisAlignItems = "CENTER";
    comp.counterAxisAlignItems = "CENTER";
    comp.itemSpacing = 8;
    comp.paddingTop = 0;
    comp.paddingRight = 0;
    comp.paddingBottom = 0;
    comp.paddingLeft = 0;
    comp.setBoundVariable("itemSpacing", vars.gap);
    page.appendChild(comp);
    created.push(comp.id);

    const leftKey = comp.addComponentProperty("Left label", "TEXT", "Field Label");
    const rightKey = comp.addComponentProperty("Right label", "TEXT", "Field Label");
    const showLeftKey = comp.addComponentProperty("Show left label", "BOOLEAN", false);
    const showRightKey = comp.addComponentProperty("Show right label", "BOOLEAN", false);

    const left = figma.createText();
    left.name = "Left label";
    bindText(left, vars[labelRole]);
    left.characters = "Field Label";
    left.resize(68, 16);
    comp.appendChild(left);
    left.visible = false;
    left.componentPropertyReferences = { characters: leftKey, visible: showLeftKey };
    created.push(left.id);

    const track = figma.createFrame();
    track.name = "Toggle track";
    track.layoutMode = "NONE";
    track.resize(40, 20);
    track.fills = [solid(vars[trackRole])];
    track.strokes = [solid(vars[borderRole])];
    track.strokeAlign = "INSIDE";
    track.strokeWeight = 1;
    track.cornerRadius = 9999;
    track.clipsContent = true;
    for (const side of ["Top", "Right", "Bottom", "Left"]) {
      track.setBoundVariable("stroke" + side + "Weight", vars.stroke);
    }
    for (const corner of ["topLeftRadius", "topRightRadius", "bottomRightRadius", "bottomLeftRadius"]) {
      track.setBoundVariable(corner, vars.radius);
    }
    track.effects = state === "Focus" ? focusEffects(toggle === "On") : innerEffects();
    comp.appendChild(track);
    created.push(track.id);

    const thumb = figma.createEllipse();
    thumb.name = "Thumb";
    thumb.resize(16.666666, 16.666666);
    thumb.fills = [solid(vars[thumbRole])];
    thumb.strokes = [];
    track.appendChild(thumb);
    thumb.x = toggle === "On" ? 21.666666 : 1.666666;
    thumb.y = 1.666666;
    created.push(thumb.id);

    const right = figma.createText();
    right.name = "Right label";
    bindText(right, vars[labelRole]);
    right.characters = "Field Label";
    right.resize(68, 16);
    comp.appendChild(right);
    right.visible = false;
    right.componentPropertyReferences = { characters: rightKey, visible: showRightKey };
    created.push(right.id);

    comp.layoutSizingHorizontal = "HUG";
    comp.layoutSizingVertical = "HUG";
    components.push(comp);
    variantDetails.push({ id: comp.id, name: comp.name, childIds: [left.id, track.id, thumb.id, right.id], propertyKeys: [leftKey, rightKey, showLeftKey, showRightKey] });
  }
}

const set = figma.combineAsVariants(components, page);
set.name = "Toggle";
set.description = "Control binario On/Off. Estados visuales Default, Hover, Focus y Disabled. Etiquetas opcionales a izquierda y derecha; ambas ocultas por defecto. Usa variables semánticas locales de AI Design System. No define interacciones de prototipo ni comportamiento web.";
set.descriptionMarkdown = set.description;
set.x = 260;
set.y = 180;
const gapX = 128;
const gapY = 80;
for (const child of set.children) {
  const props = child.variantProperties;
  const col = ["Default", "Hover", "Focus", "Disabled"].indexOf(props.State);
  const row = ["On", "Off"].indexOf(props.Toggle);
  if (col < 0 || row < 0) throw new Error("Unexpected variant after combine");
  child.x = 80 + col * (40 + gapX);
  child.y = 80 + row * (20 + gapY);
}
set.resizeWithoutConstraints(704, 280);
created.push(set.id);

const title = figma.createText();
title.name = "Page title";
title.fontName = { family: "Manrope", style: "SemiBold" };
title.characters = "Toggles";
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
bindText(note, vars.textPrimary);
note.characters = "On / Off × Default / Hover / Focus / Disabled. Etiquetas opcionales; variables locales. Auditoría humana pendiente.";
note.resize(690, 40);
page.appendChild(note);
note.x = 80;
note.y = 500;
created.push(note.id);

return {
  pageId: page.id,
  componentSetId: set.id,
  variantDetails,
  documentationNodeIds: [title.id, note.id],
  createdNodeIds: created,
  componentPropertyDefinitions: set.componentPropertyDefinitions,
  pageChildren: page.children.map(n => ({ id: n.id, name: n.name, type: n.type })),
  variantCount: set.children.length,
  publishStatus: await set.getPublishStatusAsync()
};
