// CONVERSATION-COMPOSER-SLOT-001; preserves the existing message and child IDs.
await figma.setCurrentPageAsync(await figma.getNodeByIdAsync('765:6'));
figma.skipInvisibleInstanceChildren = false;
const owner = await figma.getNodeByIdAsync('765:397');
const container = await figma.getNodeByIdAsync('1087:383');
const message = await figma.getNodeByIdAsync('1087:372');
if (owner.type !== 'COMPONENT' || container.parent.id !== '1087:497') throw new Error('Unexpected host');
for (const t of message.findAllWithCriteria({types:['TEXT']})) {
  for (const s of t.getStyledTextSegments(['fontName'])) await figma.loadFontAsync(s.fontName);
}
const none = await figma.variables.getVariableByIdAsync('VariableID:12:18');
const gap = await figma.variables.getVariableByIdAsync('VariableID:12:30');
if (none.name !== 'spacing/none' || gap.name !== 'spacing/sm') throw new Error('Token identity mismatch');
let slot = container.children.find(n => n.type === 'SLOT' && n.name === 'Notice content');
const createdNodeIds = [];
if (!slot) { slot = owner.createSlot(); createdNodeIds.push(slot.id); container.appendChild(slot); }
slot.name = 'Notice content';
slot.layoutMode = 'VERTICAL';
slot.resize(message.width, message.height);
slot.layoutSizingHorizontal = 'FILL';
slot.layoutSizingVertical = 'HUG';
slot.primaryAxisAlignItems = 'MIN';
slot.counterAxisAlignItems = 'MIN';
slot.fills = [];
slot.strokes = [];
slot.clipsContent = false;
for (const field of ['paddingTop','paddingBottom','paddingLeft','paddingRight']) slot.setBoundVariable(field, none);
slot.setBoundVariable('itemSpacing', gap);
if (message.parent.id !== slot.id) slot.appendChild(message);
message.layoutSizingHorizontal = 'FILL';
message.layoutSizingVertical = 'HUG';
const property = slot.componentPropertyReferences.slotContentId;
owner.editComponentProperty(property, {
  name: 'Notice content',
  description: 'Bloques del aviso opcional. Insertar, quitar, reordenar o sustituir desde una instancia vinculada. La muestra de un bloque no fija un máximo.',
  slotSettings: {stretchChildOnInsert:true,displayEmptyByDefault:false,minChildren:null,maxChildren:null,allowPreferredValuesOnly:false}
});
const definition = owner.componentPropertyDefinitions[property];
return {
  createdNodeIds, mutatedNodeIds:[owner.id,container.id,slot.id,message.id],
  slot:{id:slot.id,type:slot.type,name:slot.name,property,propertyType:definition.type,settings:definition.slotSettings,
    parent:slot.parent.id,children:slot.children.map(n=>({id:n.id,type:n.type,name:n.name})),
    layoutMode:slot.layoutMode,width:slot.width,height:slot.height,horizontal:slot.layoutSizingHorizontal,vertical:slot.layoutSizingVertical,boundVariables:slot.boundVariables},
  previousSlots:owner.findAllWithCriteria({types:['SLOT']}).map(n=>({id:n.id,name:n.name,count:n.children.length})),
  preserved:{message:message.id,text:'1087:365',button:'1087:399'},
};
