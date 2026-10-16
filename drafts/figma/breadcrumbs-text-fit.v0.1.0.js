// BREADCRUMBS-001 deterministic fit correction after screenshot exposed clipping.
const page = await figma.getNodeByIdAsync("190:188");
const itemSet = await figma.getNodeByIdAsync("190:210");
const compositionSet = await figma.getNodeByIdAsync("191:229");
if (!page || page.type !== "PAGE" || page.name !== "Breadcrumbs" || !itemSet || itemSet.type !== "COMPONENT_SET" || !compositionSet || compositionSet.type !== "COMPONENT_SET") throw new Error("Breadcrumbs identity mismatch");
await figma.setCurrentPageAsync(page);
await figma.loadFontAsync({ family: "Manrope", style: "Regular" });
const rows = [
  { componentId: "190:189", textId: "190:190", width: 120 },
  { componentId: "190:202", textId: "190:203", width: 120 },
  { componentId: "190:206", textId: "190:207", width: 92 },
  { componentId: "190:208", textId: "190:209", width: 92 }
];
const mutated = [];
for (const row of rows) {
  const component = await figma.getNodeByIdAsync(row.componentId);
  const label = await figma.getNodeByIdAsync(row.textId);
  if (!component || component.type !== "COMPONENT" || component.parent?.id !== itemSet.id || !label || label.type !== "TEXT" || label.parent?.id !== component.id || label.characters !== "Breadcrumb") throw new Error("Breadcrumb label mismatch " + row.textId);
  label.textAutoResize = "WIDTH_AND_HEIGHT";
  if (label.width > 92 || label.height !== 24) throw new Error("Unexpected natural label dimensions " + label.id + ": " + label.width + "x" + label.height);
  component.resize(row.width, 24);
  mutated.push(label.id, component.id);
}
const compositions = [];
for (const comp of compositionSet.children) {
  if (comp.type !== "COMPONENT") throw new Error("Unexpected composition child");
  const level = Number(comp.variantProperties.Level);
  if (![2,3,4,5].includes(level)) throw new Error("Unexpected level");
  const expectedWidth = 248 + 124 * (level - 2);
  comp.resize(expectedWidth, 24);
  const items = comp.children.find(n => n.name === "Items" && n.type === "FRAME");
  if (!items || items.children.length !== level) throw new Error("Item frame mismatch Level " + level);
  items.resize(expectedWidth - 32, 24);
  mutated.push(comp.id, items.id);
  for (let i = 0; i < items.children.length; i++) {
    const inst = items.children[i];
    if (inst.type !== "INSTANCE") throw new Error("Non-instance breadcrumb");
    inst.resize(i === items.children.length - 1 ? 92 : 120, 24);
    mutated.push(inst.id);
  }
  compositions.push({ id: comp.id, level, width: comp.width, itemWidths: items.children.map(n => n.width) });
}
compositionSet.resizeWithoutConstraints(650, 296);
mutated.push(compositionSet.id);
return { mutatedNodeIds: mutated, itemTextSizes: rows.map(r => { const t = itemSet.findOne(n => n.id === r.textId); return { id: r.textId, width: t?.width, height: t?.height }; }), compositions, setSize: [compositionSet.width, compositionSet.height] };
