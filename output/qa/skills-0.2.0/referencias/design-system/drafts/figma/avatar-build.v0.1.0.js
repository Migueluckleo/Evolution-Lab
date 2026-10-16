// AVATAR-001 · inject the decoded bytes from sources/figma-snapshots/avatar-source-face-48.png.base64 at the placeholder below.
figma.skipInvisibleInstanceChildren = false;
if (figma.root.children.some(p => p.name === "Avatars")) throw new Error("Avatars page already exists");
const iconMain = await figma.importComponentByKeyAsync("77a821b72c03fcfbd0ca9b2910c3fb5c98ed210f");
if (!iconMain || iconMain.key !== "77a821b72c03fcfbd0ca9b2910c3fb5c98ed210f") throw new Error("User icon import mismatch");
const dotMains = {};
for (const [name, id] of Object.entries({ Small: "155:125", Medium: "155:124", Large: "155:123" })) {
  const n = await figma.getNodeByIdAsync(id);
  if (!n || n.type !== "COMPONENT" || n.name !== "Type=Active, Size=" + name || n.parent?.id !== "155:144") throw new Error("Dot dependency mismatch " + name);
  dotMains[name] = n;
}
const ids = {
  bg: ["VariableID:164:122", "color/background/avatar-fallback"],
  border: ["VariableID:13:18", "color/border/on-brand"],
  icon: ["VariableID:13:23", "color/icon/on-brand"],
  text: ["VariableID:13:33", "color/text/on-brand"],
  textPrimary: ["VariableID:13:27", "color/text/primary"],
  family: ["VariableID:10:2", "font/family/base"],
  semibold: ["VariableID:10:5", "font/weight/semibold"],
  regular: ["VariableID:10:3", "font/weight/regular"],
  font10: ["VariableID:164:123", "font/size/avatar-small"],
  font12: ["VariableID:10:8", "font/size/xs"],
  font14: ["VariableID:10:9", "font/size/sm"],
  font20: ["VariableID:10:11", "font/size/lg"],
  lineDoc: ["VariableID:12:9", "font/line-height/md"],
  lineNote: ["VariableID:12:8", "font/line-height/sm"],
  radius: ["VariableID:13:11", "radius/full"],
  stroke: ["VariableID:12:41", "stroke/xs"],
  size8: ["VariableID:12:20", "size/sm"],
  size12: ["VariableID:12:21", "size/md"],
  size16: ["VariableID:12:22", "size/lg"],
  size24: ["VariableID:12:23", "size/xl"],
  size32: ["VariableID:12:24", "size/2xl"],
  size48: ["VariableID:12:26", "size/4xl"]
};
const v = {};
for (const [key, [id, name]] of Object.entries(ids)) {
  const x = await figma.variables.getVariableByIdAsync(id);
  if (!x || x.name !== name || x.variableCollectionId !== "VariableCollectionId:6:2") throw new Error("variable mismatch " + key);
  v[key] = x;
}
await figma.loadFontAsync({ family: "Manrope", style: "SemiBold" });
await figma.loadFontAsync({ family: "Manrope", style: "Regular" });
function solid(x) { return figma.variables.setBoundVariableForPaint({ type: "SOLID", color: { r: 1, g: 1, b: 1 } }, "color", x); }
const sourcePngBytes = new Uint8Array(__AVATAR_IMAGE_BYTES__);
if (sourcePngBytes.length !== 5103 || sourcePngBytes[0] !== 137 || sourcePngBytes[1] !== 80) throw new Error("Avatar sample PNG does not match source export");
const sampleImage = figma.createImage(sourcePngBytes);
const page = figma.createPage();
page.name = "Avatars";
await figma.setCurrentPageAsync(page);
const created = [page.id], comps = [], details = [];
const sizes = {
  Small: { face: 20, dot: 5, dotMain: dotMains.Small, icon: 16, font: 10, fontVar: v.font10, faceVar: null, iconVar: v.size16 },
  Medium: { face: 24, dot: 8, dotMain: dotMains.Small, icon: 20, font: 12, fontVar: v.font12, faceVar: v.size24, iconVar: null },
  Large: { face: 32, dot: 12, dotMain: dotMains.Medium, icon: 24, font: 14, fontVar: v.font14, faceVar: v.size32, iconVar: v.size24 },
  "Extra Large": { face: 48, dot: 16, dotMain: dotMains.Large, icon: 32, font: 20, fontVar: v.font20, faceVar: v.size48, iconVar: v.size32 }
};
for (const type of ["Image", "Icon", "Text"]) {
  for (const size of ["Extra Large", "Large", "Medium", "Small"]) {
    const spec = sizes[size];
    const comp = figma.createComponent();
    comp.name = "Type=" + type + ", Size=" + size;
    comp.resize(spec.face, spec.face);
    comp.layoutMode = "NONE";
    comp.fills = [];
    comp.strokes = [];
    comp.clipsContent = false;
    if (spec.faceVar) { comp.setBoundVariable("width", spec.faceVar); comp.setBoundVariable("height", spec.faceVar); }
    page.appendChild(comp);
    created.push(comp.id);
    const showKey = comp.addComponentProperty("Show status", "BOOLEAN", true);
    let initialsKey = null, iconKey = null;
    if (type === "Text") initialsKey = comp.addComponentProperty("Initials", "TEXT", "JA");
    if (type === "Icon") iconKey = comp.addComponentProperty("Icon", "INSTANCE_SWAP", iconMain.id);

    const face = figma.createFrame();
    face.name = type === "Image" ? "Image face" : "Fallback face";
    face.resize(spec.face, spec.face);
    face.layoutMode = "NONE";
    face.clipsContent = true;
    face.cornerRadius = 9999;
    face.fills = type === "Image" ? [{ type: "IMAGE", imageHash: sampleImage.hash, scaleMode: "FILL" }] : [solid(v.bg)];
    face.strokes = type === "Image" ? [] : [solid(v.border)];
    if (type !== "Image") {
      face.strokeWeight = 1;
      face.strokeAlign = "INSIDE";
      for (const side of ["Top", "Right", "Bottom", "Left"]) face.setBoundVariable("stroke" + side + "Weight", v.stroke);
    }
    for (const corner of ["topLeftRadius", "topRightRadius", "bottomRightRadius", "bottomLeftRadius"]) face.setBoundVariable(corner, v.radius);
    if (spec.faceVar) { face.setBoundVariable("width", spec.faceVar); face.setBoundVariable("height", spec.faceVar); }
    comp.appendChild(face);
    face.x = 0; face.y = 0;
    created.push(face.id);

    let iconId = null, vectorIds = [], textId = null;
    if (type === "Icon") {
      const icon = iconMain.createInstance();
      icon.name = "User icon";
      icon.resize(spec.icon, spec.icon);
      if (spec.iconVar) { icon.setBoundVariable("width", spec.iconVar); icon.setBoundVariable("height", spec.iconVar); }
      face.appendChild(icon);
      icon.x = (spec.face - spec.icon) / 2;
      icon.y = (spec.face - spec.icon) / 2;
      icon.componentPropertyReferences = { mainComponent: iconKey };
      for (const vector of icon.findAll(n => n.type === "VECTOR")) {
        vector.fills = [solid(v.icon)];
        vectorIds.push(vector.id);
        created.push(vector.id);
      }
      if (!vectorIds.length) throw new Error("User icon has no vector");
      iconId = icon.id;
      created.push(icon.id);
    }
    if (type === "Text") {
      const t = figma.createText();
      t.name = "Initials";
      t.fontName = { family: "Manrope", style: "SemiBold" };
      t.characters = "JA";
      t.fontSize = spec.font;
      t.lineHeight = { unit: "AUTO" };
      t.fills = [solid(v.text)];
      t.setBoundVariable("fontFamily", v.family);
      t.setBoundVariable("fontStyle", v.semibold);
      t.setBoundVariable("fontSize", spec.fontVar);
      t.textAutoResize = "WIDTH_AND_HEIGHT";
      face.appendChild(t);
      t.x = (spec.face - t.width) / 2;
      t.y = (spec.face - t.height) / 2;
      t.componentPropertyReferences = { characters: initialsKey };
      textId = t.id;
      created.push(t.id);
    }
    const dot = spec.dotMain.createInstance();
    dot.name = "Status dot";
    dot.resize(spec.dot, spec.dot);
    comp.appendChild(dot);
    dot.x = spec.face - spec.dot;
    dot.y = spec.face - spec.dot;
    dot.componentPropertyReferences = { visible: showKey };
    created.push(dot.id);
    comps.push(comp);
    details.push({ id: comp.id, type, size, faceId: face.id, iconId, vectorIds, textId, dotId: dot.id, dotSize: spec.dot, showKey, initialsKey, iconKey });
  }
}
const set = figma.combineAsVariants(comps, page);
set.name = "Avatar";
set.description = "Representación visual de identidad mediante imagen, icono o iniciales, con indicador opcional. La foto, JA y el punto verde son ejemplos. El producto debe definir la fuente de identidad, el fallback y el estado accesible.";
set.descriptionMarkdown = set.description;
set.x = 80; set.y = 160;
for (const child of set.children) {
  const p = child.variantProperties;
  const col = ["Extra Large", "Large", "Medium", "Small"].indexOf(p.Size);
  const row = ["Image", "Text", "Icon"].indexOf(p.Type);
  if (col < 0 || row < 0) throw new Error("Unexpected Avatar variant");
  child.x = 52 + col * 120;
  child.y = 48 + row * 100;
}
set.resizeWithoutConstraints(530, 350);
created.push(set.id);
const title = figma.createText();
title.name = "Page title";
title.fontName = { family: "Manrope", style: "SemiBold" };
title.characters = "Avatars";
title.fontSize = 20;
title.lineHeight = { unit: "PIXELS", value: 24 };
title.fills = [solid(v.textPrimary)];
title.setBoundVariable("fontFamily", v.family);
title.setBoundVariable("fontStyle", v.semibold);
title.setBoundVariable("fontSize", v.font20);
title.setBoundVariable("lineHeight", v.lineDoc);
page.appendChild(title);
title.x = 80; title.y = 80;
created.push(title.id);
const note = figma.createText();
note.name = "Usage and accessibility note";
note.fontName = { family: "Manrope", style: "Regular" };
note.characters = "Image, Icon y Text ofrecen tres representaciones visuales. La imagen y las iniciales son ejemplos; el punto indica Active solo visualmente. El producto debe proporcionar nombre y estado accesibles. Auditoría humana pendiente.";
note.fontSize = 14;
note.lineHeight = { unit: "PIXELS", value: 20 };
note.fills = [solid(v.textPrimary)];
note.setBoundVariable("fontFamily", v.family);
note.setBoundVariable("fontStyle", v.regular);
note.setBoundVariable("fontSize", v.font14);
note.setBoundVariable("lineHeight", v.lineNote);
note.textAutoResize = "HEIGHT";
note.resize(750, 80);
page.appendChild(note);
note.x = 80; note.y = 580;
created.push(note.id);
return { pageId: page.id, setId: set.id, sampleImageHash: sampleImage.hash, variants: details, createdNodeIds: created };
