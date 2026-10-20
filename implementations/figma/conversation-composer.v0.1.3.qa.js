await figma.setCurrentPageAsync(await figma.getNodeByIdAsync('765:6'));
figma.skipInvisibleInstanceChildren = false;
const owner = await figma.getNodeByIdAsync('765:397');
for (const t of owner.findAllWithCriteria({types:['TEXT']}))
  for (const s of t.getStyledTextSegments(['fontName'])) await figma.loadFontAsync(s.fontName);
const collection = await figma.variables.getVariableCollectionByIdAsync('VariableCollectionId:6:2');
const border = await figma.variables.getVariableByIdAsync('VariableID:13:14');
const frame = figma.createAutoLayout();
frame.name = 'QA Composer Slot 0.1.3 · temporary';
frame.layoutMode = 'HORIZONTAL'; frame.itemSpacing = 40; frame.fills = []; frame.clipsContent = false;
frame.x = Math.max(...figma.currentPage.children.filter(n=>n.id!==frame.id).map(n=>n.x+n.width))+120;
frame.y = 80;
const created = [frame.id], tests = [], samples = [];
function slotOf(n) { return n.findAllWithCriteria({types:['SLOT']}).find(s=>s.name==='Notice content'); }
function metrics(n) {
  const slot = slotOf(n);
  return {instance:n.id,main:n.mainComponent.id,slot:slot.id,count:slot.children.length,width:n.width,height:n.height,
    slotWidth:slot.width,slotHeight:slot.height,gap:slot.itemSpacing,violations:slot.limitViolations,
    children:slot.children.map(c=>({id:c.id,type:c.type,width:c.width,height:c.height,y:c.y,
      inside:c.width<=slot.width+0.1,borderId:c.boundVariables.strokes?.[0]?.id,
      text:c.findAllWithCriteria({types:['TEXT']}).filter(t=>t.name==='description').map(t=>({id:t.id,width:t.width,height:t.height,styles:t.getStyledTextSegments(['textStyleId']).map(s=>({start:s.start,end:s.end,style:s.textStyleId})),fits:t.x+t.width<=c.width+0.1}))}))};
}
for (const width of [616,360]) {
  const instance = owner.createInstance(); created.push(instance.id); frame.appendChild(instance);
  instance.resize(width,instance.height); instance.layoutSizingHorizontal='FIXED';instance.layoutSizingVertical='HUG';
  instance.setProperties({'Show action#1087:0':true}); samples.push(instance.id);
  const slot=slotOf(instance);
  for(const mode of collection.modes){
    instance.setExplicitVariableModeForCollection(collection,mode.modeId);
    tests.push({case:'sample',mode:mode.name,...metrics(instance),border:border.resolveForConsumer(slot.children[0])});
  }
  instance.setExplicitVariableModeForCollection(collection,'6:0');
  const first=slot.children[0];
  for(let i=0;i<2;i++){const c=first.clone();slot.appendChild(c);c.layoutSizingHorizontal='FILL';created.push(c.id);}
  tests.push({case:'three',...metrics(instance)});
  const order=slot.children.map(c=>c.id);slot.insertChild(0,slot.children[2]);
  tests.push({case:'reorder',before:order,after:slot.children.map(c=>c.id),pass:slot.children[0].id===order[2]});
  const removed=slot.children[1].id;slot.children[1].remove();
  const replacement=slot.children[0].clone();slot.insertChild(1,replacement);replacement.layoutSizingHorizontal='FILL';created.push(replacement.id);
  tests.push({case:'replace',removed,inserted:replacement.id,...metrics(instance)});
  const beforeToggle=slot.children.map(c=>c.id);instance.setProperties({'Show action#1087:0':false});instance.setProperties({'Show action#1087:0':true});
  tests.push({case:'visibility',pass:JSON.stringify(beforeToggle)===JSON.stringify(slot.children.map(c=>c.id))});
  const text=slot.children[0].findAllWithCriteria({types:['TEXT']}).find(t=>t.name==='description');
  const style=await figma.getStyleByIdAsync('S:ed58d525ce135d142794e5c47e201096c023a800,');
  text.characters='Aviso largo de prueba sin reglas de negocio. '.repeat(8);
  await text.setTextStyleIdAsync(style.id);
  tests.push({case:'long',...metrics(instance)});
  for(const c of [...slot.children])c.remove();
  tests.push({case:'empty',...metrics(instance)});
  slot.resetSlot();
  tests.push({case:'reset',...metrics(instance)});
  // Final visual samples: one block wide, three blocks narrow.
  if(width===360){for(let i=0;i<2;i++){const c=slot.children[0].clone();slot.appendChild(c);c.layoutSizingHorizontal='FILL';created.push(c.id);}}
}
return {frameId:frame.id,samples,createdNodeIds:created,mutatedNodeIds:samples,tests,
  masterSlots:owner.findAllWithCriteria({types:['SLOT']}).map(s=>({id:s.id,name:s.name,count:s.children.length})),
  existingInstance: (await figma.getNodeByIdAsync('766:246')).mainComponent.id};
