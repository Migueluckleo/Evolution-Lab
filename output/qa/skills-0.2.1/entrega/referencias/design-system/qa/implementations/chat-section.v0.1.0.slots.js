figma.skipInvisibleInstanceChildren=false;
const page=await figma.getNodeByIdAsync('783:6');await figma.setCurrentPageAsync(page);
await Promise.all(['Regular','Bold'].map(style=>figma.loadFontAsync({family:'Manrope',style})));
const stand=await figma.getNodeByIdAsync('783:24'),active=await figma.getNodeByIdAsync('783:116'),sug=await figma.getNodeByIdAsync('783:14'),message=await figma.getNodeByIdAsync('765:271'),response=await figma.getNodeByIdAsync('765:274');
const before={stand:stand.findAll(()=>true).length,active:active.findAll(()=>true).length};
const tests=[],made=[],errors=[];
for(const [main,name,dep] of [[stand,'Suggestions',sug],[active,'Messages',message]]){
 const inst=main.createInstance();page.appendChild(inst);inst.x=4000;inst.y=2000;made.push(inst.id);
 const get=()=>inst.findOne(n=>n.type==='SLOT'&&n.name===name);let slot=get();const initial=slot.children.length,counts=[];
 for(const count of [0,1,3,5]){for(const c of [...slot.children])c.remove();for(let i=0;i<count;i++){const c=dep.createInstance();slot.appendChild(c);c.name='QA '+i;if(name==='Messages')c.layoutSizingHorizontal='FILL';}counts.push({requested:count,actual:slot.children.length,height:inst.height,slotHeight:slot.height});if(count!==slot.children.length)errors.push(name+' count');}
 const last=slot.children[4];slot.insertChild(0,last);const reordered=slot.children[0].id===last.id;
 slot.children[1].remove();const replacement=(name==='Messages'?response:sug).createInstance();slot.insertChild(1,replacement);if(name==='Messages')replacement.layoutSizingHorizontal='FILL';const replaced=slot.children[1].id===replacement.id;
 const first=slot.children[0],key=Object.keys(first.componentProperties).find(k=>k.startsWith(name==='Messages'?'Message text#':'Label#'));first.setProperties({[key]:'Contenido largo de demostración para verificar crecimiento sin recorte. '.repeat(10)});
 const longHeight=inst.height,widths=[];
 for(const width of [574,782,1024]){inst.resize(width,inst.height);widths.push({width:inst.width,height:inst.height,columnWidth:inst.children[0].width,slotWidth:slot.width,overflow:slot.children.filter(n=>n.x<-.5||n.x+n.width>slot.width+.5).map(n=>n.id)});}
 const signature=()=>get().children.map(n=>({name:n.name,main:n.type==='INSTANCE'?n.mainComponent?.id:null}));const a=signature();inst.setProperties({State:main===stand?'Active':'Standby'});inst.setProperties({State:main===stand?'Standby':'Active'});const b=signature(),preserved=JSON.stringify(a)===JSON.stringify(b);
 if(!reordered||!replaced||!preserved||widths.some(w=>w.overflow.length))errors.push(name+' composition');
 tests.push({host:main.id,slot:name,initial,counts,reordered,replaced,longHeight,widths,preserved,instanceType:inst.type});inst.remove();
}
const t=stand.createInstance();page.appendChild(t);t.x=4000;t.y=4000;made.push(t.id);
const uk=Object.keys(t.componentProperties).find(k=>k.startsWith('User name#'));t.setProperties({[uk]:'María del Carmen Rodríguez Hernández de la Torre'});
const username=t.findOne(n=>n.type==='TEXT'&&n.name==='User name');const greeting={value:username.characters,width:username.width,height:username.height,parentWidth:username.parent.width,hostHeight:t.height};if(username.width>username.parent.width+.5)errors.push('Greeting overflow');
const collection=await figma.variables.getVariableCollectionByIdAsync('VariableCollectionId:6:2'),brand=await figma.variables.getVariableByIdAsync('VariableID:13:32'),body=await figma.variables.getVariableByIdAsync('VariableID:773:275'),hero=t.findOne(n=>n.name==='BENI body');const themes=[];
for(const mode of collection.modes){t.setExplicitVariableModeForCollection(collection,mode.modeId);themes.push({mode:mode.name,brand:brand.resolveForConsumer(username),beni:body.resolveForConsumer(hero)});}t.remove();
const after={stand:stand.findAll(()=>true).length,active:active.findAll(()=>true).length};if(JSON.stringify(before)!==JSON.stringify(after))errors.push('Main tree changed');
return {status:errors.length?'FAIL':'PASS',tests,greeting,themes,before,after,temporaryRootIdsRemoved:made,errors};
