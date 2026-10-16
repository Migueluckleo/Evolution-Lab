// BREADCRUMBS-001 · bind the dedicated Current text role after variable JSON/Figma QA.
const page = await figma.getNodeByIdAsync("190:188");
const itemSet = await figma.getNodeByIdAsync("190:210");
const compositionSet = await figma.getNodeByIdAsync("191:229");
const text = await figma.getNodeByIdAsync("190:207");
const variable = await figma.variables.getVariableByIdAsync("VariableID:196:122");
if (!page || page.type !== "PAGE" || page.name !== "Breadcrumbs" || !itemSet || itemSet.type !== "COMPONENT_SET" || !compositionSet || compositionSet.type !== "COMPONENT_SET" || !text || text.type !== "TEXT" || text.parent?.id !== "190:206" || text.characters !== "Breadcrumb") throw new Error("Breadcrumb Current target mismatch");
if (!variable || variable.name !== "color/text/breadcrumb/current" || variable.variableCollectionId !== "VariableCollectionId:6:2" || variable.resolvedType !== "COLOR" || variable.scopes.join(",") !== "TEXT_FILL") throw new Error("Current text variable mismatch");
await figma.setCurrentPageAsync(page);
await figma.loadFontAsync({ family: "Manrope", style: "Regular" });
text.fills = [figma.variables.setBoundVariableForPaint({ type: "SOLID", color: { r: 1, g: 1, b: 1 } }, "color", variable)];
const affected = [text.id];
for (const variant of compositionSet.children) {
  const items = variant.children.find(n => n.name === "Items" && n.type === "FRAME");
  if (!items) throw new Error("Items frame missing");
  const last = items.children[items.children.length - 1];
  if (!last || last.type !== "INSTANCE" || last.mainComponent?.id !== "190:206") throw new Error("Current instance mismatch");
  affected.push(last.id);
  for (const nested of last.findAll(n => n.type === "TEXT" && n.characters === "Breadcrumb")) affected.push(nested.id);
}
return { mutatedNodeIds: affected, currentTextId: text.id, variableId: variable.id, boundFillId: text.fills[0].boundVariables?.color?.id, affectedInstanceCount: 4 };
