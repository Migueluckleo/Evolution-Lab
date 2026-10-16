// AVATAR-001 · run after Avatar and Chips exist; adds only preferred swap options.
const chip = await figma.getNodeByIdAsync("72:298");
const avatar = await figma.getNodeByIdAsync("165:247");
if (!chip || chip.type !== "COMPONENT_SET" || chip.name !== "Filter Chip" ||
    !avatar || avatar.type !== "COMPONENT_SET" || avatar.name !== "Avatar") {
  throw new Error("Source or destination component set mismatch");
}
const preferred = chip.componentPropertyDefinitions["left icon#72:3"]?.preferredValues;
if (!preferred || preferred.length !== 1512 || preferred.some(x => x.type !== "COMPONENT_SET")) {
  throw new Error("Verified Phosphor preference catalog mismatch");
}
const current = avatar.componentPropertyDefinitions["Icon#165:21"]?.preferredValues;
if (!current || (current.length !== 0 && current.length !== 1512)) {
  throw new Error("Unexpected Avatar icon picker state");
}
if (current.length === 0) avatar.editComponentProperty("Icon#165:21", { preferredValues: preferred });
return {
  mutatedNodeIds: current.length === 0 ? [avatar.id] : [],
  componentSetId: avatar.id,
  propertyKey: "Icon#165:21",
  preferredCount: avatar.componentPropertyDefinitions["Icon#165:21"].preferredValues.length
};
