// LINEAR-PROGRESS-BAR-001 · read-only destination QA; no source write.
figma.skipInvisibleInstanceChildren=false;
const expected=__PROGRESS_VARIANTS_JSON__.variants;
const pages=figma.root.children.filter(p=>p.name==="Linear Progress Bars");
if(pages.length!==1)throw new Error(`Expected one Linear Progress Bars page, found ${pages.length}`);
const page=pages[0];await figma.setCurrentPageAsync(page);
const sets=page.children.filter(n=>n.type==="COMPONENT_SET");
if(sets.length!==1||sets[0].name!=="Linear Progress Bar")throw new Error("Expected exactly one Linear Progress Bar set");
const set=sets[0];
const defs=set.componentPropertyDefinitions;
const names=Object.keys(defs).map(x=>x.split("#")[0]).sort();
const expectedNames=["Helper text","Label","Progress","Show helper text","Show label","Show percentage","Size","Type"].sort();
if(JSON.stringify(names)!==JSON.stringify(expectedNames))throw new Error("Component property definitions mismatch");
for(const [axis,values] of Object.entries({Type:["Primary","Warning","Positive","Danger"],Size:["Small","Medium","Large"],Progress:["25%","50%","75%","100%"]})){
  if(JSON.stringify(defs[axis].variantOptions)!==JSON.stringify(values))throw new Error(`Variant options mismatch ${axis}`);
}
if(set.children.length!==48||expected.length!==48)throw new Error("Variant count mismatch");
const ids={track:"VariableID:219:122",primary:"VariableID:219:123",warning:"VariableID:219:124",positive:"VariableID:219:125",danger:"VariableID:219:126",text:"VariableID:13:27",secondary:"VariableID:13:28",family:"VariableID:10:2",regular:"VariableID:10:3",size12:"VariableID:10:8",size14:"VariableID:10:9",line16:"VariableID:12:7",line20:"VariableID:12:8",tracking:"VariableID:12:16",gap:"VariableID:12:29",radius:"VariableID:13:11"};
const variables={};for(const [role,id] of Object.entries(ids)){const v=await figma.variables.getVariableByIdAsync(id);if(!v||v.variableCollectionId!=="VariableCollectionId:6:2")throw new Error(`Missing local semantic variable ${role}`);variables[role]=v;}
const errors=[],keys=new Set();let solidPaints=0,texts=0,typographyBindings=0,propertyRefs=0,radiusBindings=0,gapBindings=0,reactions=0,instances=0;
function check(condition,message){if(!condition)errors.push(message);}
function alias(value,id){return value?.id===id&&value?.type==="VARIABLE_ALIAS";}
function paint(node,id,category){const p=node.fills;check(Array.isArray(p)&&p.length===1&&p[0].type==="SOLID"&&alias(p[0].boundVariables?.color,id),`${node.parent?.name}/${node.name} paint binding`);const v=Object.values(variables).find(x=>x.id===id);check(!!v&&v.scopes.includes(category)&&((category==="TEXT_FILL"&&v.name.startsWith("color/text/"))||(category==="FRAME_FILL"&&v.name.startsWith("color/background/"))),`${node.name} paint semantic scope`);solidPaints++;}
function text(node,chars,color,size,line){check(node.type==="TEXT"&&node.characters===chars,`${node.name} characters`);paint(node,color,"TEXT_FILL");const b=node.boundVariables||{};for(const [key,id] of Object.entries({fontFamily:ids.family,fontStyle:ids.regular,fontSize:size,lineHeight:line,letterSpacing:ids.tracking})){check(alias(b[key]?.[0],id),`${node.name} ${key}`);typographyBindings++;}texts++;}
for(const c of set.children){
  const p=c.variantProperties,key=`${p.Type}/${p.Size}/${p.Progress}`;check(!keys.has(key),`duplicate ${key}`);keys.add(key);
  const s=expected.find(x=>x.type===p.Type.toLowerCase()&&x.size===(p.Size==="Medium"?"middle":p.Size.toLowerCase())&&x.percentage===p.Progress);check(!!s,`unexpected ${key}`);if(!s)continue;
  const size=p.Size,rowHeight=size==="Small"?16:20,compHeight=size==="Small"?44:size==="Medium"?52:56;
  check(c.width===246&&c.height===compHeight&&c.layoutMode==="VERTICAL",`${key} component geometry`);
  check(c.x===s.x&&c.y===s.y,`${key} matrix position`);
  check(alias(c.boundVariables?.itemSpacing,ids.gap),`${key} gap`);gapBindings++;
  check(c.children.length===3,`${key} child count`);const [row,track,helper]=c.children;
  check(row.name==="Label and percentage"&&row.width===246&&row.height===rowHeight&&row.layoutMode==="HORIZONTAL",`${key} row geometry`);
  check(track.name==="Track"&&track.width===246&&track.height===s.trackHeight&&track.children.length===1,`${key} track geometry`);
  check(row.children.length===2,`${key} label row children`);
  const [label,pct]=row.children,bar=track.children[0];
  check(bar.name==="Progress bar"&&bar.width===s.fillWidth&&bar.height===s.trackHeight&&bar.x===0,`${key} bar geometry`);
  check(track.clipsContent===true,`${key} track clipping`);
  for(const n of [track,bar]){for(const corner of ["topLeftRadius","topRightRadius","bottomLeftRadius","bottomRightRadius"]){check(alias(n.boundVariables?.[corner],ids.radius),`${key} ${n.name} ${corner}`);radiusBindings++;}}
  paint(track,ids.track,"FRAME_FILL");paint(bar,ids[p.Type.toLowerCase()],"FRAME_FILL");
  text(label,"Label",ids.text,size==="Small"?ids.size12:ids.size14,size==="Small"?ids.line16:ids.line20);
  text(pct,p.Progress,ids.text,size==="Small"?ids.size12:ids.size14,size==="Small"?ids.line16:ids.line20);
  text(helper,"Optional helper text",ids.secondary,ids.size12,ids.line16);
  for(const [node,prop,definition] of [[row,"visible","Show label"],[label,"characters","Label"],[pct,"visible","Show percentage"],[helper,"characters","Helper text"],[helper,"visible","Show helper text"]]){const actual=node.componentPropertyReferences?.[prop];check(typeof actual==="string"&&actual.split("#")[0]===definition&&defs[actual],`${key} ${definition} reference`);propertyRefs++;}
  for(const n of [c,row,label,pct,track,bar,helper]){reactions+=(n.reactions||[]).length;if(n.type==="INSTANCE")instances++;}
}
check(keys.size===48,"Incomplete variant matrix");check(solidPaints===240,"Paint count");check(texts===144,"Text count");check(typographyBindings===720,"Typography binding count");check(propertyRefs===240,"Property reference count");check(radiusBindings===384,"Radius binding count");check(gapBindings===48,"Gap binding count");check(reactions===0,"Unexpected reactions");check(instances===0,"Unexpected instances");
return {result:errors.length?"FAIL":"PASS",pageId:page.id,setId:set.id,variantCount:set.children.length,uniqueVariantCombinations:keys.size,solidPaints,framePaints:96,textPaints:144,texts,typographyBindings,propertyRefs,radiusBindings,gapBindings,reactions,instances,errors:errors.slice(0,30),errorCount:errors.length};
