/**
 * bindVariablesToComponent
 *
 * Binds design token variables to the visual properties of a component node.
 * Supports fills, strokes, all padding directions, item spacing, and corner radius.
 * Only binds properties for which a variable ID is provided in `bindings`.
 *
 * This function should be called on each variant individually within a component
 * set, OR on the component set itself for properties shared by all variants.
 *
 * @param {ComponentNode | FrameNode | RectangleNode} component
 *   The Figma node to mutate. Usually a ComponentNode or one of its children.
 * @param {{
 *   fills?: string,
 *   strokes?: string,
 *   paddingTop?: string,
 *   paddingBottom?: string,
 *   paddingLeft?: string,
 *   paddingRight?: string,
 *   itemSpacing?: string,
 *   cornerRadius?: string
 * }} bindings
 *   Each key is a visual property name; each value is a Figma Variable ID
 *   (e.g. "VariableID:123:456"). Omit a key to skip binding that property.
 * @returns {Promise<{ mutatedNodeIds: string[] }>}
 *   List of node IDs that were mutated (for audit/validation purposes).
 */
async function bindVariablesToComponent(component, bindings) {
  const mutatedNodeIds = []

  if (!component) {
    return { mutatedNodeIds }
  }

  // Batch every getVariableByIdAsync call upfront in a single Promise.all rather
  // than awaiting per-property — the lookups are independent and IPC-bound.
  const floatBindings = [
    ['paddingTop', 'paddingTop'],
    ['paddingBottom', 'paddingBottom'],
    ['paddingLeft', 'paddingLeft'],
    ['paddingRight', 'paddingRight'],
    ['itemSpacing', 'itemSpacing'],
    ['cornerRadius', 'cornerRadius'],
  ]

  const requestedIds = []
  if (bindings.fills) requestedIds.push(['fills', bindings.fills])
  if (bindings.strokes) requestedIds.push(['strokes', bindings.strokes])
  for (const [bindingKey] of floatBindings) {
    if (bindings[bindingKey]) requestedIds.push([bindingKey, bindings[bindingKey]])
  }

  const resolved = await Promise.all(
    requestedIds.map(([, id]) => figma.variables.getVariableByIdAsync(id)),
  )
  const varByKey = {}
  for (let i = 0; i < requestedIds.length; i++) {
    varByKey[requestedIds[i][0]] = resolved[i]
  }

  const markMutated = () => {
    if (!mutatedNodeIds.includes(component.id)) {
      mutatedNodeIds.push(component.id)
    }
  }

  // --- Fills ---
  const fillVar = varByKey.fills
  if (fillVar) {
    const existingFills = component.fills
    if (Array.isArray(existingFills) && existingFills.length > 0) {
      // Bind the color of the first fill to the variable
      const boundFill = figma.variables.setBoundVariableForPaint(existingFills[0], 'color', fillVar)
      component.fills = [boundFill, ...existingFills.slice(1)]
    } else {
      // No existing fill — create a solid fill bound to the variable
      const boundFill = figma.variables.setBoundVariableForPaint(
        { type: 'SOLID', color: { r: 0.5, g: 0.5, b: 0.5 } },
        'color',
        fillVar,
      )
      component.fills = [boundFill]
    }
    markMutated()
  }

  // --- Strokes ---
  const strokeVar = varByKey.strokes
  if (strokeVar) {
    const existingStrokes = component.strokes
    if (Array.isArray(existingStrokes) && existingStrokes.length > 0) {
      const boundStroke = figma.variables.setBoundVariableForPaint(
        existingStrokes[0],
        'color',
        strokeVar,
      )
      component.strokes = [boundStroke, ...existingStrokes.slice(1)]
    } else {
      const boundStroke = figma.variables.setBoundVariableForPaint(
        { type: 'SOLID', color: { r: 0.5, g: 0.5, b: 0.5 } },
        'color',
        strokeVar,
      )
      component.strokes = [boundStroke]
    }
    markMutated()
  }

  // --- Spacing properties (FLOAT variables bound via setBoundVariable) ---
  for (const [bindingKey, figmaProp] of floatBindings) {
    const variable = varByKey[bindingKey]
    if (variable) {
      component.setBoundVariable(figmaProp, variable)
      markMutated()
    }
  }

  return { mutatedNodeIds }
}

const p=await figma.getNodeByIdAsync("847:7");await figma.setCurrentPageAsync(p);
if(p.children.length)throw Error("Non-empty page: inspect before retry");
await Promise.all([{family:"Inter",style:"Regular"},{family:"Manrope",style:"Regular"},{family:"Manrope",style:"Bold"}].map(f=>figma.loadFontAsync(f)));
const MAP={"font/family/base":"VariableID:10:2","font/weight/regular":"VariableID:10:3","font/weight/bold":"VariableID:10:6","font/size/xs":"VariableID:10:8","font/line-height/xs":"VariableID:12:7","font/letter-spacing/normal":"VariableID:12:16","spacing/none":"VariableID:12:18","spacing/xs":"VariableID:12:29","spacing/sm":"VariableID:12:30","stroke/xs":"VariableID:12:41","radius/md":"VariableID:13:6","color/border/accent":"VariableID:13:12","color/text/primary":"VariableID:13:27","color/text/secondary":"VariableID:13:28","color/text/tertiary":"VariableID:13:29","color/text/brand":"VariableID:13:32","color/background/default":"VariableID:13:35","color/background/subtle":"VariableID:13:36","color/interactive/ghost/active":"VariableID:13:63","color/background/source-card/hover":"VariableID:847:6"},ids=Object.values(MAP),fetched=await Promise.all(ids.map(id=>figma.variables.getVariableByIdAsync(id)));
const vars=Object.fromEntries(Object.keys(MAP).map((k,i)=>[k,fetched[i]]));
const created=[],styles=[];function keep(n){created.push(n.id);return n;}
function b(n,f,k){n.setBoundVariable(f,vars[k]);}
function col(n,k){n.fills=[figma.variables.setBoundVariableForPaint({type:"SOLID",color:{r:0,g:0,b:0}},"color",vars[k])];}
function layout(n,name,dir,w,h=16){n.name=name;n.layoutMode=dir;n.resize(w,h);n.layoutSizingHorizontal="FIXED";n.layoutSizingVertical="HUG";n.primaryAxisAlignItems="MIN";n.counterAxisAlignItems="MIN";n.fills=[];n.clipsContent=false;for(const f of ["paddingTop","paddingBottom","paddingLeft","paddingRight","itemSpacing"])b(n,f,"spacing/none");}
const oldstyles=await figma.getLocalTextStylesAsync();
function style(name,size,bold){if(oldstyles.some(s=>s.name===name))throw Error("Style exists");const s=figma.createTextStyle();s.name=name;s.fontName={family:"Manrope",style:bold?"Bold":"Regular"};s.fontSize=size;s.lineHeight={unit:"PIXELS",value:16};s.letterSpacing={unit:"PIXELS",value:0};s.setBoundVariable("fontFamily",vars["font/family/base"]);s.setBoundVariable("fontStyle",vars[bold?"font/weight/bold":"font/weight/regular"]);if(size===12)s.setBoundVariable("fontSize",vars["font/size/xs"]);s.setBoundVariable("lineHeight",vars["font/line-height/xs"]);s.setBoundVariable("letterSpacing",vars["font/letter-spacing/normal"]);s.description=size===8?"Metadato de Fuentes. Tamaño8px observado sin token equivalente; limitación de legibilidad documentada en FUENTES-001.":"Título compacto de tarjeta Fuentes. Consume tipografía semántica del AI DS.";styles.push(s.id);return s;}
const titleStyle=style("Fuentes/Source",12,true),metaStyle=style("Fuentes/Path",8,false),caption=oldstyles.find(s=>s.id==="S:00ebc27da069f50e5d170d9e45cc9f392042a351,");
if(!caption)throw Error("Caption missing");
async function text(parent,name,copy,st,color,width,fill=true){const t=keep(figma.createText());parent.appendChild(t);t.name=name;await t.setTextStyleIdAsync(st.id);t.textAutoResize="HEIGHT";t.resize(width,16);t.characters=copy;t.layoutSizingHorizontal=fill?"FILL":"HUG";t.layoutSizingVertical="HUG";col(t,color);for(const [f,k]of [["fontFamily","font/family/base"],["fontStyle",st.id===titleStyle.id?"font/weight/bold":"font/weight/regular"],["lineHeight","font/line-height/xs"],["letterSpacing","font/letter-spacing/normal"]])b(t,f,k);if(st.id!==metaStyle.id)b(t,"fontSize","font/size/xs");return t;}
const item=keep(figma.createComponent());p.appendChild(item);layout(item,"Fuentes Path Item","HORIZONTAL",100);item.layoutSizingHorizontal="HUG";item.maxWidth=132;item.counterAxisAlignItems="MIN";
const sep=await text(item,"Separator"," · ",metaStyle,"color/text/tertiary",12,false);
const label=await text(item,"Label","generales contpaqi",metaStyle,"color/text/tertiary",116,false);label.maxWidth=116;label.textAutoResize="HEIGHT";
const lk=item.addComponentProperty("Label","TEXT","generales contpaqi"),sk=item.addComponentProperty("Show separator","BOOLEAN",false);label.componentPropertyReferences={characters:lk};sep.componentPropertyReferences={visible:sk};sep.visible=false;item.description="Segmento de metadatos de Fuentes; no navegación. Texto editable. Mostrar separador excepto en primer elemento; el autor mantiene orden. Tamaño8px con limitación documentada.";
item.x=40;item.y=400;
const comp=keep(figma.createComponent());p.appendChild(comp);layout(comp,"State=Default","VERTICAL",167.6666717529297,90);comp.minWidth=150;comp.maxWidth=168;comp.strokesIncludedInLayout=true;comp.strokeAlign="INSIDE";comp.strokeWeight=1;comp.clipsContent=false;
await bindVariablesToComponent(comp,{fills:MAP["color/background/default"],strokes:MAP["color/border/accent"],paddingTop:MAP["spacing/sm"],paddingRight:MAP["spacing/sm"],paddingBottom:MAP["spacing/sm"],paddingLeft:MAP["spacing/sm"],itemSpacing:MAP["spacing/sm"],cornerRadius:MAP["radius/md"]});
b(comp,"strokeWeight","stroke/xs");
const info=keep(figma.createAutoLayout("VERTICAL"));comp.appendChild(info);layout(info,"Info","VERTICAL",149.6666717529297,48);info.layoutSizingHorizontal="FILL";
const row=keep(figma.createAutoLayout("HORIZONTAL"));info.appendChild(row);layout(row,"Reference and type","HORIZONTAL",149.6666717529297);row.layoutSizingHorizontal="FILL";row.counterAxisAlignItems="CENTER";b(row,"itemSpacing","spacing/xs");
const dotMain=await figma.getNodeByIdAsync("155:134");const dot=keep(dotMain.createInstance());row.appendChild(dot);dot.name="Reference";dot.setProperties({"Count#155:6":"2"});dot.isExposedInstance=true;dot.strokes=[];col(dot,"color/background/subtle");const dt=dot.findAllWithCriteria({types:["TEXT"]})[0];col(dt,"color/text/secondary");created.push(dt.id);
const ty=await text(row,"Type","Manual de referencia",caption,"color/text/secondary",133.6666717529297);
const so=await text(info,"Source","CONTPAQi®",titleStyle,"color/text/primary",149.6666717529297);
const lo=await text(info,"Location","Mi cuenta",caption,"color/text/brand",149.6666717529297);
const props={};for(const [name,node,copy]of [["Type",ty,"Manual de referencia"],["Source",so,"CONTPAQi®"],["Location",lo,"Mi cuenta"]]){props[name]=comp.addComponentProperty(name,"TEXT",copy);node.componentPropertyReferences={characters:props[name]};}
const slot=keep(comp.createSlot());layout(slot,"Path","HORIZONTAL",149.6666717529297);slot.layoutSizingHorizontal="FILL";slot.layoutWrap="WRAP";slot.counterAxisSpacing=0;slot.counterAxisAlignContent="AUTO";b(slot,"counterAxisSpacing","spacing/none");
const slotKey=slot.componentPropertyReferences.slotContentId;comp.editComponentProperty(slotKey,{name:"Path",description:"Ruta variable de metadatos; insertar/quitar/reordenar/sustituir segmentos. Dos es muestra, no máximo. Sin navegación implícita.",preferredValues:[{type:"COMPONENT",key:item.key}],slotSettings:{stretchChildOnInsert:false,displayEmptyByDefault:false,minChildren:0,maxChildren:null,allowPreferredValuesOnly:false}});
for(const [copy,show]of [["generales contpaqi",false],["conocimiento",true]]){const i=keep(item.createInstance());slot.appendChild(i);i.setProperties({[lk]:copy,[sk]:show});i.layoutSizingHorizontal="HUG";i.layoutSizingVertical="HUG";for(const n of i.findAll(()=>true))created.push(n.id);}
comp.x=40;comp.y=40;
return JSON.stringify({pageId:p.id,baseId:comp.id,pathItemId:item.id,pathItemKeys:{label:lk,separator:sk},slotKey:slot.componentPropertyReferences.slotContentId,slotId:slot.id,props,styles,createdNodeIds:created,baseSize:{width:comp.width,height:comp.height},pathItemSize:{width:item.width,height:item.height}});
