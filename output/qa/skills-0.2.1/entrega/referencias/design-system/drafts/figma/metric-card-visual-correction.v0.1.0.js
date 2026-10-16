// METRIC-CARD-001 · correct source-aligned positioning and distinct Horizontal sample values.
figma.skipInvisibleInstanceChildren = false;
const page = await figma.getNodeByIdAsync("202:208");
const set = await figma.getNodeByIdAsync("202:327");
if (!page || page.type !== "PAGE" || page.name !== "Metric Cards" || !set || set.type !== "COMPONENT_SET" || set.name !== "Metric Card" || set.parent?.id !== page.id) throw new Error("Metric Cards identity mismatch");
await figma.setCurrentPageAsync(page);
const expect = {
  "202:281": ["One Metric V1", "Large"], "202:292": ["One Metric V1", "Small"],
  "202:303": ["One Metric V2", "Large"], "202:315": ["One Metric V2", "Small"]
};
for (const [id, [type, size]] of Object.entries(expect)) {
  const n = await figma.getNodeByIdAsync(id);
  if (!n || n.parent?.id !== set.id || n.variantProperties?.Type !== type || n.variantProperties?.Size !== size || n.counterAxisAlignItems !== "CENTER") throw new Error("Variant mismatch " + id);
}
const defs = set.componentPropertyDefinitions;
if (Object.keys(defs).some(k => k.startsWith("Horizontal amount "))) throw new Error("Horizontal value properties already exist; inspect before retry");
const targets = [
  ["202:259", "Horizontal amount 1 value", 135], ["202:262", "Horizontal amount 2 value", 135],
  ["202:277", "Horizontal amount 1 value", 112], ["202:280", "Horizontal amount 2 value", 112]
];
for (const [id] of targets) { const n = await figma.getNodeByIdAsync(id); if (!n || n.type !== "TEXT" || n.characters !== "$123,456.00") throw new Error("Source sample mismatch " + id); }
await figma.loadFontAsync({ family: "Manrope", style: "Regular" });
const keys = {
  "Horizontal amount 1 value": set.addComponentProperty("Horizontal amount 1 value", "TEXT", "$123,320.00"),
  "Horizontal amount 2 value": set.addComponentProperty("Horizontal amount 2 value", "TEXT", "$123,320.00")
};
const mutated = [];
for (const id of Object.keys(expect)) { const n = await figma.getNodeByIdAsync(id); n.counterAxisAlignItems = "MIN"; mutated.push(id); }
for (const [id, prop, width] of targets) {
  const n = await figma.getNodeByIdAsync(id);
  n.componentPropertyReferences = { characters: keys[prop] };
  n.characters = "$123,320.00";
  n.resize(width, n.height);
  mutated.push(id);
}
return { pageId: page.id, setId: set.id, createdPropertyKeys: keys, mutatedNodeIds: mutated, horizontalSamples: targets.map(([id]) => ({ id, characters: "$123,320.00" })) };
