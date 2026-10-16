// ICON-BUTTON-001 · add only the verified Phosphor picker alternatives.
const chip = await figma.getNodeByIdAsync("72:298");
const set = await figma.getNodeByIdAsync("183:311");
if (!chip || chip.type !== "COMPONENT_SET" || chip.name !== "Filter Chip" ||
    !set || set.type !== "COMPONENT_SET" || set.name !== "Icon Button") throw new Error("set mismatch");
const preferred = chip.componentPropertyDefinitions["left icon#72:3"]?.preferredValues;
if (!preferred || preferred.length !== 1512 || preferred.some(x => x.type !== "COMPONENT_SET")) throw new Error("Phosphor picker mismatch");
const matches = Object.keys(set.componentPropertyDefinitions).filter(k => k.startsWith("Icon#"));
if (matches.length !== 1) throw new Error("Icon property ambiguity");
const key = matches[0];
const current = set.componentPropertyDefinitions[key].preferredValues;
if (!current || (current.length !== 0 && current.length !== 1512)) throw new Error("Unexpected picker state");
if (current.length === 0) set.editComponentProperty(key, { preferredValues: preferred });
return {
  mutatedNodeIds: current.length === 0 ? [set.id] : [],
  setId: set.id,
  key,
  preferredCount: set.componentPropertyDefinitions[key].preferredValues.length,
  showCountKey: Object.keys(set.componentPropertyDefinitions).find(k => k.startsWith("Show count#"))
};
