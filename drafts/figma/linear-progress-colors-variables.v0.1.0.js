// FOUNDATIONS-LINEAR-PROGRESS-COLORS-001 · runner injects the canonical JSON.
const spec=__PROGRESS_COLORS_JSON__;
const collection=(await figma.variables.getLocalVariableCollectionsAsync()).find(c=>c.id===spec.collection.targetId);
if(!collection||collection.name!==spec.collection.name)throw new Error("Semantic collection mismatch");
const modes=Object.keys(spec.collection.modes);
if(modes.length!==4||modes.some(id=>!collection.modes.some(m=>m.modeId===id)))throw new Error("Mode mismatch");
const local=await figma.variables.getLocalVariablesAsync();
if(spec.variables.some(s=>local.some(v=>v.name===s.name)))throw new Error("Progress role exists; inspect before retry");
for(const s of spec.variables){
  if(s.resolvedType!=="COLOR"||JSON.stringify(s.scopes)!==JSON.stringify(["FRAME_FILL"]))throw new Error("Role schema mismatch "+s.name);
  for(const mode of modes){const alias=s.valuesByMode[mode];const p=await figma.variables.getVariableByIdAsync(alias.targetId);if(!p||p.name!==alias.name||p.resolvedType!=="COLOR"||p.variableCollectionId!=="VariableCollectionId:6:3")throw new Error("Primitive mismatch "+alias.name);}
}
const created=[];for(const s of spec.variables){const v=figma.variables.createVariable(s.name,collection,"COLOR");v.description=s.description;v.scopes=s.scopes;for(const mode of modes)v.setValueForMode(mode,{type:"VARIABLE_ALIAS",id:s.valuesByMode[mode].targetId});created.push({id:v.id,name:v.name});}
return {collectionId:collection.id,created};
