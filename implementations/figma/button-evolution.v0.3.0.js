const page=await figma.getNodeByIdAsync('0:1');await figma.setCurrentPageAsync(page);
const set=await figma.getNodeByIdAsync('26:81');if(set.children.length!==60)throw new Error('Expected original 60 variants');
const original=[...set.children];const positions=original.map(n=>({id:n.id,row:n.gridRowAnchorIndex,col:n.gridColumnAnchorIndex}));
const fonts=new Map();for(const n of set.findAll(n=>n.type==='TEXT'))for(const seg of n.getStyledTextSegments(['fontName']))fonts.set(seg.fontName.family+'|'+seg.fontName.style,seg.fontName);
for(const f of fonts.values())await figma.loadFontAsync({family:f.family,style:f.style});
const created=[];const mutated=[set.id];const clones=[];const get=(type,size,state)=>set.children.find(n=>n.variantProperties.type===type&&n.variantProperties.size===size&&n.variantProperties.state===state);
const sizes=['large','middle','small'];const states=['default','hover','press','disabled','focus'];
const dangerVars={default:await figma.variables.getVariableByIdAsync('VariableID:1167:2'),hover:await figma.variables.getVariableByIdAsync('VariableID:1167:3'),press:await figma.variables.getVariableByIdAsync('VariableID:1167:4')};
set.gridRowCount=30;for(let i=20;i<30;i++)set.gridRowSizes[i].type='HUG';set.resize(set.width,2823);
let count=0;
function addClone(base,name){const n=base.clone();page.appendChild(n);n.name=name;set.appendChildAt(n,20+Math.floor(count/3),count%3);for(let i=0;i<base.children.length;i++)n.children[i].componentPropertyReferences={...base.children[i].componentPropertyReferences};count++;clones.push(n);created.push(n.id,...n.findAll(()=>true).map(c=>c.id));return n;}
for(const state of states)for(const size of sizes){const n=addClone(get('primary',size,state),'type=danger, size='+size+', state='+state);if(state!=='disabled')n.fills=[figma.variables.setBoundVariableForPaint({...n.fills[0]},'color',dangerVars[state]||dangerVars.default)];}
const dangerMap=new Map();for(const state of states)for(const size of sizes)dangerMap.set(get('primary',size,state).id,get('danger',size,state).id);
for(const n of clones){const reactions=JSON.parse(JSON.stringify(n.reactions));for(const r of reactions){delete r.action;for(const a of r.actions||[])if(a.destinationId&&dangerMap.has(a.destinationId))a.destinationId=dangerMap.get(a.destinationId);}await n.setReactionsAsync(reactions);}
const loaderWhite=await figma.getNodeByIdAsync('378:1804');const loaderBrand=await figma.getNodeByIdAsync('378:1789');
for(const type of ['primary','default','text','link','danger'])for(const size of sizes){
 const n=addClone(get(type,size,'default'),'type='+type+', size='+size+', state=loading');
 await n.setReactionsAsync([]);
 for(const child of [...n.children])if(child.type==='INSTANCE'){child.componentPropertyReferences={};child.visible=false;}
 const loader=(type==='primary'||type==='danger'?loaderWhite:loaderBrand).createInstance();n.appendChild(loader);loader.name='Loading indicator';
 if(size!=='large')loader.rescale((size==='middle'?20:16)/24);
 n.primaryAxisSizingMode='AUTO';created.push(loader.id,...loader.findAll(()=>true).map(c=>c.id));
}
const color=await figma.variables.getVariableByIdAsync('VariableID:13:71');const weight=await figma.variables.getVariableByIdAsync('VariableID:13:3');const radius=await figma.variables.getVariableByIdAsync('VariableID:13:7');
const focusNodes=set.children.filter(n=>n.variantProperties.state==='focus');
for(const n of focusNodes){n.strokes=[];n.clipsContent=false;const ring=figma.createRectangle();n.appendChild(ring);ring.name='Focus ring';ring.layoutPositioning='ABSOLUTE';ring.fills=[];ring.resize(n.width+8,n.height+8);ring.x=-4;ring.y=-4;ring.strokes=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',color)];ring.strokeWeight=2;ring.strokeAlign='INSIDE';ring.cornerRadius=12;for(const field of ['strokeTopWeight','strokeBottomWeight','strokeLeftWeight','strokeRightWeight'])ring.setBoundVariable(field,weight);for(const field of ['topLeftRadius','topRightRadius','bottomLeftRadius','bottomRightRadius'])ring.setBoundVariable(field,radius);ring.constraints={horizontal:'STRETCH',vertical:'STRETCH'};created.push(ring.id);mutated.push(n.id);}
const after=original.map(n=>({id:n.id,row:n.gridRowAnchorIndex,col:n.gridColumnAnchorIndex}));
return JSON.stringify({createdNodeIds:created,mutatedNodeIds:mutated,variants:set.children.map(n=>({id:n.id,name:n.name,width:n.width,height:n.height})),oldPositionsPreserved:JSON.stringify(after)===JSON.stringify(positions),grid:{rows:set.gridRowCount,width:set.width,height:set.height},count:set.children.length});
