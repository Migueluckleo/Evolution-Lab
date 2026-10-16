// AMD-DOT-INACTIVE-BORDER-001 · run only after DOT-001 0.1.0 exists.
const token = await figma.variables.getVariableByIdAsync("VariableID:157:122");
if (!token || token.name !== "color/border/status-inactive" ||
    token.variableCollectionId !== "VariableCollectionId:6:2" ||
    token.scopes.length !== 1 || token.scopes[0] !== "STROKE_COLOR") {
  throw new Error("Inactive border semantic variable does not match the contract");
}
const expected = [
  ["155:129", "Type=Inactive, Size=Large"],
  ["155:130", "Type=Inactive, Size=Medium"],
  ["155:131", "Type=Inactive, Size=Small"]
];
const changed = [];
for (const [id, name] of expected) {
  const component = await figma.getNodeByIdAsync(id);
  if (!component || component.type !== "COMPONENT" || component.name !== name ||
      component.parent?.id !== "155:144" ||
      component.boundVariables?.fills?.[0]?.id !== "VariableID:154:124") {
    throw new Error("Inactive Dot variant does not match the expected baseline: " + id);
  }
  const current = component.boundVariables?.strokes?.[0]?.id;
  if (current !== "VariableID:13:18" && current !== token.id) {
    throw new Error("Unexpected prior stroke binding: " + id);
  }
  if (current !== token.id) {
    component.strokes = [figma.variables.setBoundVariableForPaint(
      { type: "SOLID", color: { r: 1, g: 1, b: 1 } }, "color", token
    )];
  }
  changed.push({ id, name, strokeVariableId: component.boundVariables?.strokes?.[0]?.id });
}
return { amendment: "AMD-DOT-INACTIVE-BORDER-001", changed };
