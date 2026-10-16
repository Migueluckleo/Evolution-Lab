// FOUNDATIONS-CHART-COLORS-001 · create exactly the seven JSON-declared semantic roles.
const collection = (await figma.variables.getLocalVariableCollectionsAsync()).find(c => c.id === "VariableCollectionId:6:2");
if (!collection || collection.name !== "semantic") throw new Error("Semantic collection mismatch");
const specs = [
  { name: "color/background/chart/bar", description: "Fondo de barra de datos de Chart Cell; no se usa como texto, icono o pista.", scope: "FRAME_FILL", aliases: ["VariableID:8:87", "VariableID:8:62", "VariableID:8:71", "VariableID:8:80"] },
  { name: "color/shape/chart/progress", description: "Forma de avance completado en gráficos de progreso lineales y semicirculares; no codifica por sí sola éxito o fracaso.", scope: "SHAPE_FILL", aliases: ["VariableID:8:88", "VariableID:8:63", "VariableID:8:73", "VariableID:8:81"] },
  { name: "color/shape/chart/track", description: "Forma del tramo restante en gráficos de progreso y su swatch de leyenda; acento suave de cada modo, separado visualmente del avance.", scope: "SHAPE_FILL", aliases: ["VariableID:8:86", "VariableID:8:60", "VariableID:8:70", "VariableID:8:78"] },
  { name: "color/shape/chart/legend-neutral", description: "Swatch neutral de ejemplo en Chart Legend Label antes de asignar una serie; solo shape de leyenda.", scope: "SHAPE_FILL", aliases: ["VariableID:8:97", "VariableID:8:97", "VariableID:8:97", "VariableID:8:97"] },
  { name: "color/shape/chart/series-1", description: "Swatch de la primera serie de Chart Header, de énfasis fuerte por modo.", scope: "SHAPE_FILL", aliases: ["VariableID:8:88", "VariableID:8:63", "VariableID:8:73", "VariableID:8:81"] },
  { name: "color/shape/chart/series-2", description: "Swatch de la segunda serie de Chart Header; acento medio calibrado para conservar diferenciación sobre blanco.", scope: "SHAPE_FILL", aliases: ["VariableID:8:86", "VariableID:8:61", "VariableID:8:72", "VariableID:8:79"] },
  { name: "color/shape/chart/series-3", description: "Swatch de la tercera serie de Chart Header; acento base de cada modo.", scope: "SHAPE_FILL", aliases: ["VariableID:8:87", "VariableID:8:62", "VariableID:8:71", "VariableID:8:80"] }
];
const modes = ["6:0", "6:1", "6:2", "6:3"];
if (collection.modes.length !== 4 || modes.some(id => !collection.modes.some(m => m.modeId === id))) throw new Error("Mode mismatch");
const local = await figma.variables.getLocalVariablesAsync();
if (specs.some(s => local.some(v => v.name === s.name))) throw new Error("Chart role already exists; inspect before retry");
for (const id of new Set(specs.flatMap(s => s.aliases))) {
  const v = await figma.variables.getVariableByIdAsync(id);
  if (!v || v.resolvedType !== "COLOR" || v.variableCollectionId !== "VariableCollectionId:6:3") throw new Error("Primitive mismatch " + id);
}
const created = [];
for (const spec of specs) {
  const v = figma.variables.createVariable(spec.name, collection, "COLOR");
  v.description = spec.description;
  v.scopes = [spec.scope];
  modes.forEach((mode, i) => v.setValueForMode(mode, { type: "VARIABLE_ALIAS", id: spec.aliases[i] }));
  created.push({ id: v.id, name: v.name });
}
return { collectionId: collection.id, created };
