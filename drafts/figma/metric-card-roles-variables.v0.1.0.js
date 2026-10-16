// FOUNDATIONS-METRIC-CARD-ROLES-001 · create exactly the two JSON-declared semantic roles.
const collectionId = "VariableCollectionId:6:2";
const collection = (await figma.variables.getLocalVariableCollectionsAsync()).find(c => c.id === collectionId);
if (!collection || collection.name !== "semantic") throw new Error("Semantic collection mismatch");
const specs = [
  { name: "color/text/metric/trend", description: "Texto de variación porcentual en Metric Card sobre fondo claro o sutil; expresa el acento de marca sin inferir por sí solo si la variación es favorable.", scope: "TEXT_FILL" },
  { name: "color/icon/metric/brand", description: "Iconos de marca dentro de Metric Card sobre fondo claro o sutil, incluidos el icono de categoría y la flecha Navigate; no se usa para texto ni fondo.", scope: "SHAPE_FILL" }
];
const aliases = [
  ["6:0", "VariableID:8:87", "color/blue/400"],
  ["6:1", "VariableID:8:62", "color/green/500"],
  ["6:2", "VariableID:8:73", "color/orange/700"],
  ["6:3", "VariableID:8:80", "color/purple/500"]
];
const local = await figma.variables.getLocalVariablesAsync();
if (specs.some(s => local.some(v => v.name === s.name))) throw new Error("A metric role exists; inspect before retry");
if (collection.modes.length !== 4 || aliases.some(([mode]) => !collection.modes.some(m => m.modeId === mode))) throw new Error("Mode mismatch");
for (const [, id, expectedName] of aliases) {
  const v = await figma.variables.getVariableByIdAsync(id);
  if (!v || v.name !== expectedName || v.resolvedType !== "COLOR" || v.variableCollectionId !== "VariableCollectionId:6:3") throw new Error("Primitive mismatch " + expectedName);
}
const createdVariableIds = [];
for (const spec of specs) {
  const v = figma.variables.createVariable(spec.name, collection, "COLOR");
  v.description = spec.description;
  v.scopes = [spec.scope];
  for (const [mode, id] of aliases) v.setValueForMode(mode, { type: "VARIABLE_ALIAS", id });
  createdVariableIds.push(v.id);
}
return { createdVariableIds, collectionId, variables: createdVariableIds.map(id => { const v = local.find(x => x.id === id); return v ? { id: v.id, name: v.name } : { id }; }) };
