// FOUNDATIONS-BREADCRUMB-CURRENT-TEXT-001 · P1.b creation from canonical extension JSON.
const name = "color/text/breadcrumb/current";
const description = "Texto del último segmento de Breadcrumb sobre fondo claro; conserva el acento de marca de cada modo con contraste suficiente para texto normal.";
const collectionId = "VariableCollectionId:6:2";
const existing = (await figma.variables.getLocalVariablesAsync()).filter(v => v.name === name && v.variableCollectionId === collectionId);
if (existing.length) throw new Error("Breadcrumb current-text variable already exists; inspect before retry");
const collection = (await figma.variables.getLocalVariableCollectionsAsync()).find(c => c.id === collectionId);
if (!collection || collection.name !== "semantic") throw new Error("Semantic collection mismatch");
const aliases = [
  ["6:0", "VariableID:8:87", "color/blue/400"],
  ["6:1", "VariableID:8:62", "color/green/500"],
  ["6:2", "VariableID:8:73", "color/orange/700"],
  ["6:3", "VariableID:8:80", "color/purple/500"]
];
if (collection.modes.length !== 4 || aliases.some(([mode]) => !collection.modes.some(m => m.modeId === mode))) throw new Error("Mode mismatch");
for (const [, id, expectedName] of aliases) {
  const v = await figma.variables.getVariableByIdAsync(id);
  if (!v || v.name !== expectedName || v.resolvedType !== "COLOR" || v.variableCollectionId !== "VariableCollectionId:6:3") throw new Error("Primitive mismatch " + expectedName);
}
const created = figma.variables.createVariable(name, collection, "COLOR");
created.description = description;
created.scopes = ["TEXT_FILL"];
for (const [mode, id] of aliases) created.setValueForMode(mode, { type: "VARIABLE_ALIAS", id });
return { createdVariableIds: [created.id], name: created.name, collectionId: created.variableCollectionId, scopes: created.scopes, description: created.description, valuesByMode: created.valuesByMode, codeSyntax: created.codeSyntax };
