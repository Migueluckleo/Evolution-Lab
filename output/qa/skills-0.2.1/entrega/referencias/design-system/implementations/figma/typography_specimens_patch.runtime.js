// Generated from canonical JSON by typography_specimens_patch.py. Do not edit data here.
// This file only changes documentation on Typography; it never edits TextStyles or components.
const APPLY = __APPLY__;
const PLAN = __PLAN__;
const {source,styles,baseCards,boards,updates,cardRoles,newStyleIds,oldStyleIds}=PLAN;
const changedExistingIds=new Set(),createdNodeIds=[],createdCards=[],events=[];
let writesStarted=false;
const failure=(kind,detail)=>{throw Error(kind+': '+detail);};
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const unitEqual=(actual,expected,line)=>actual.unit===expected.unit&&(expected.unit==='AUTO'||actual.value===expected.value||actual.value===(line&&expected.unit==='PERCENT'?Math.fround(expected.value/100)*100:Math.fround(expected.value)));
const recipeEqual=(actual,s)=>actual.fontName?.family===s.fontFamily&&actual.fontName?.style===s.fontStyle&&(actual.fontSize===s.fontSize||actual.fontSize===Math.fround(s.fontSize))&&unitEqual(actual.lineHeight,s.lineHeight,true)&&unitEqual(actual.letterSpacing,s.letterSpacing,false)&&(actual.textDecoration??'NONE')===s.textDecoration;
const role=(card,name)=>{const found=card.children.filter(n=>n.name===name);if(found.length!==1||found[0].type!=='TEXT')failure('CARD_ROLE',card.id+'/'+name);return found[0];};
const tokenId=name=>PLAN.tokens.find(row=>row[0]===name)[1];
function checkCardBindings(card){
 for(const [field,name] of [['itemSpacing','spacing/lg'],...['paddingTop','paddingBottom','paddingLeft','paddingRight'].map(field=>[field,'spacing/xl']),...['topLeftRadius','topRightRadius','bottomLeftRadius','bottomRightRadius'].map(field=>[field,'radius/md'])])if(card.boundVariables?.[field]?.id!==tokenId(name))failure('CARD_BINDING',card.id+'/'+field);
 if(card.fills?.[0]?.boundVariables?.color?.id!==tokenId('color/background/subtle'))failure('CARD_FILL',card.id);
 for(const name of cardRoles)if(role(card,name).fills?.[0]?.boundVariables?.color?.id!==tokenId(name==='Valores'?'color/text/secondary':'color/text/primary'))failure('TEXT_FILL',card.id+'/'+name);
}
const walk=n=>[n,...('children' in n?n.children.flatMap(walk):[])];
const glyphSnapshot=n=>({id:n.id,parent:n.parent?.id,name:n.name,characters:n.characters,fontName:n.fontName,fontSize:n.fontSize,lineHeight:n.lineHeight,letterSpacing:n.letterSpacing,textDecoration:n.textDecoration,textCase:n.textCase,paragraphSpacing:n.paragraphSpacing,paragraphIndent:n.paragraphIndent,textStyleId:n.textStyleId,textAutoResize:n.textAutoResize,width:n.width,height:n.height,layoutSizingHorizontal:n.layoutSizingHorizontal,layoutSizingVertical:n.layoutSizingVertical,fills:n.fills,strokes:n.strokes,boundVariables:n.boundVariables,componentPropertyReferences:n.componentPropertyReferences});
const frameSnapshot=n=>({id:n.id,parent:n.parent?.id,name:n.name,width:n.width,height:n.height,layoutMode:n.layoutMode,primaryAxisSizingMode:n.primaryAxisSizingMode,counterAxisSizingMode:n.counterAxisSizingMode,layoutSizingHorizontal:n.layoutSizingHorizontal,layoutSizingVertical:n.layoutSizingVertical,itemSpacing:n.itemSpacing,paddingTop:n.paddingTop,paddingBottom:n.paddingBottom,paddingLeft:n.paddingLeft,paddingRight:n.paddingRight,cornerRadius:n.cornerRadius,fills:n.fills,strokes:n.strokes,boundVariables:n.boundVariables,clipsContent:n.clipsContent,children:n.children.map(c=>c.id)});
const copyPattern=n=>{const value=frameSnapshot(n);for(const key of ['id','parent','name','height','children'])delete value[key];return value;};
const fontCache=new Set();
async function loadFont(font){const key=JSON.stringify(font);if(!fontCache.has(key)){await figma.loadFontAsync(font);fontCache.add(key);}}
async function loadTextFonts(n){for(const segment of n.getStyledTextSegments(['fontName']))await loadFont(segment.fontName);}
const texts=[],expectedText=[],originalCards=[],allOriginalText=[],liveStyles=new Map();
let page,lastBoard,originalTextBefore,originalCardsBefore,boardBefore;
try{
 if(figma.editorType!=='figma')failure('EDITOR','Figma Design required');
 if(figma.fileKey!==PLAN.fileKey)failure('FILE_KEY','Verify intended AI-Design-System before execution');
 page=await figma.getNodeByIdAsync(PLAN.pageId);
 if(!page||page.type!=='PAGE'||page.name!=='Typography')failure('PAGE',PLAN.pageId);
 if(typeof page.loadAsync==='function')await page.loadAsync();
 const resolvedBoards=[];
 for(const b of boards){const node=await figma.getNodeByIdAsync(b.id);if(!node||node.type!=='FRAME'||node.parent?.id!==page.id||node.name!==b.name||node.layoutMode!=='VERTICAL')failure('BOARD',b.id);resolvedBoards.push(node);}
 lastBoard=resolvedBoards[3];
 const oldNames=new Set(oldStyleIds.map(id=>'Estilo · '+id)),newNames=new Set(newStyleIds.map(id=>'Estilo · '+id));
 for(let i=0;i<resolvedBoards.length;i++){
  const b=resolvedBoards[i];const cards=b.children.filter(n=>n.type==='FRAME');
  const originals=cards.filter(n=>oldNames.has(n.name));
  if(originals.length!==boards[i].originalCount)failure('ORIGINAL_CARD_COUNT',b.id);
  for(const child of b.children){
   if(child.type==='TEXT'&&['Título','Estado','Introducción','Referencia'].includes(child.name)){allOriginalText.push(child);continue;}
   if(child.type!=='FRAME'||!(oldNames.has(child.name)||(i===3&&newNames.has(child.name))))failure('UNEXPECTED_BOARD_CHILD',child.id);
   if(child.layoutMode!=='VERTICAL'||child.children.length!==4)failure('CARD_STRUCTURE',child.id);
   for(const name of cardRoles){const text=role(child,name);if(Object.keys(text.componentPropertyReferences??{}).length)failure('SHARED_PROPERTY_REFERENCE',text.id);}
   if(oldNames.has(child.name)){originalCards.push(child);allOriginalText.push(...child.children);}
  }
  if(b.children.filter(n=>n.type==='TEXT').length!==4)failure('HEADER_COUNT',b.id);
 }
 if(originalCards.length!==75||new Set(originalCards.map(n=>n.name)).size!==75)failure('ORIGINAL_COVERAGE','Expected 75 unique unchanged identities');
 const lastOriginal=lastBoard.children.filter(n=>oldNames.has(n.name)).at(-1);
 if(lastOriginal?.id!==PLAN.lastOriginalCardId)failure('APPEND_ANCHOR',PLAN.lastOriginalCardId);
 const existingNew=lastBoard.children.filter(n=>newNames.has(n.name));
 if(new Set(existingNew.map(n=>n.name)).size!==existingNew.length||!existingNew.every((n,i)=>n.name==='Estilo · '+newStyleIds[i]))failure('PARTIAL_ORDER','Unexpected or duplicate new card order; inspect before retry');
 const appended=lastBoard.children.slice(lastBoard.children.indexOf(lastOriginal)+1);
 if(!equal(appended.map(n=>n.id),existingNew.map(n=>n.id)))failure('APPEND_TAIL','New cards must be the final children');
 for(const s of styles){const actual=await figma.getStyleByIdAsync(s.styleId);if(!actual||actual.type!=='TEXT'||actual.name!==s.name||actual.description!==s.description||!recipeEqual(actual,s))failure('TEXT_STYLE_PREFLIGHT',s.id);liveStyles.set(s.id,actual);await loadFont(actual.fontName);}
 const semantic=await figma.variables.getVariableCollectionByIdAsync(PLAN.collection.id);
 if(!semantic||semantic.name!=='semantic'||!semantic.modes.some(m=>m.modeId===PLAN.collection.modeId&&m.name==='Contable'))failure('SEMANTIC_COLLECTION',PLAN.collection.id);
 for(const [name,id,type,scope] of PLAN.tokens){const variable=await figma.variables.getVariableByIdAsync(id);if(!variable||variable.name!==name||variable.variableCollectionId!==semantic.id||variable.resolvedType!==type||!variable.scopes.includes(scope))failure('VARIABLE_PREFLIGHT',name);}
 for(const b of resolvedBoards)if(b.explicitVariableModes?.[semantic.id]!==PLAN.collection.modeId)failure('BOARD_MODE',b.id);
 for(const entry of baseCards){
  const card=await figma.getNodeByIdAsync(entry.cardId);
  if(!card||card.type!=='FRAME'||card.name!=='Estilo · '+entry.baseStyleId||!originalCards.includes(card))failure('BASE_CARD',entry.cardId);
  entry.node=card;checkCardBindings(card);
  const sample=role(card,'Muestra');
  if(sample.getRangeTextStyleId(0,sample.characters.length)!==styles.find(s=>s.id===entry.baseStyleId).styleId)failure('BASE_SAMPLE_STYLE',sample.id);
  const desc=role(card,'Descripción');
  if(desc.characters!==entry.oldDescription&&desc.characters!==entry.description)failure('BASE_DESCRIPTION_DRIFT',desc.id);
  texts.push({node:desc,characters:entry.description,styleId:'body-regular',kind:'base-description'});
 }
 for(const update of updates){const node=await figma.getNodeByIdAsync(update.nodeId);if(!node||node.type!=='TEXT'||node.name!==update.name||node.parent?.id!==update.boardId)failure('HEADER',update.nodeId);if(node.characters!==update.before&&node.characters!==update.after)failure('HEADER_DRIFT',update.nodeId+' '+node.characters);texts.push({node,characters:update.after,styleId:update.styleId,kind:'header'});}
 for(const item of texts){await loadTextFonts(item.node);if(item.node.getRangeTextStyleId(0,item.node.characters.length)!==liveStyles.get(item.styleId).id)failure('EDITORIAL_STYLE',item.node.id);}
 for(const card of [...baseCards.map(x=>x.node),...existingNew])for(const text of card.children)await loadTextFonts(text);
 originalTextBefore=JSON.parse(JSON.stringify(allOriginalText.map(glyphSnapshot)));originalCardsBefore=JSON.parse(JSON.stringify(originalCards.map(frameSnapshot)));boardBefore=JSON.parse(JSON.stringify(resolvedBoards.map(frameSnapshot)));
 const preflight={status:'PREFLIGHT_PASS_NO_MUTATION',pageId:page.id,originalCards:75,newCardsAlreadyPresent:existingNew.length,willAppend:4-existingNew.length,existingTextsSelected:texts.length,existingTextTargets:texts.map(item=>({id:item.node.id,parentId:item.node.parent.id,name:item.node.name,kind:item.kind,styleLogicalId:item.styleId})),styleCount:PLAN.styleCount,baseCount:18,compatibilityCount:61,source,mappingApplicationBlockedSegments:PLAN.applicationBlockedSegments,consumerValidation:'NOT_PERFORMED',visualQA:'NOT_RUN'};
 if(!APPLY)return preflight;
 async function updateText(node,characters,logicalId,isNew=false){
  const target=liveStyles.get(logicalId);const spec=styles.find(s=>s.id===logicalId);
  if(node.characters!==characters||node.getRangeTextStyleId(0,node.characters.length)!==target.id||!recipeEqual(node,spec)){
   writesStarted=true;if(!isNew)changedExistingIds.add(node.id);
   node.characters=characters;
   await node.setRangeTextStyleIdAsync(0,node.characters.length,target.id);
   events.push({nodeId:node.id,logicalId,kind:isNew?'NEW_CARD_TEXT':'EXISTING_DOCUMENTATION_TEXT'});
  }
  expectedText.push({node,characters,spec});
 }
 for(const entry of baseCards){
  const spec=styles.find(s=>s.id===entry.newStyleId);let card=lastBoard.children.find(n=>n.name==='Estilo · '+entry.newStyleId);let createdNow=false;
  if(!card){writesStarted=true;card=entry.node.clone();createdNow=true;for(const node of walk(card))createdNodeIds.push(node.id);card.name='Estilo · '+entry.newStyleId;lastBoard.appendChild(card);createdCards.push({logicalId:entry.newStyleId,cardId:card.id});}
  if(!equal(copyPattern(card),copyPattern(entry.node)))failure('CLONE_PATTERN',card.id);checkCardBindings(card);
  await updateText(role(card,'Nombre'),spec.name,'subheading-1-semibold',createdNow);
  await updateText(role(card,'Muestra'),entry.sample,spec.id,createdNow);
  await updateText(role(card,'Valores'),entry.values,'body-regular',createdNow);
  await updateText(role(card,'Descripción'),spec.description,'body-regular',createdNow);
 }
 for(const item of texts)await updateText(item.node,item.characters,item.styleId);
 const errors=[];
 for(const id of newStyleIds)checkCardBindings(lastBoard.children.find(n=>n.name==='Estilo · '+id));
 for(const expected of expectedText){const n=expected.node;if(n.characters!==expected.characters||n.getRangeTextStyleId(0,n.characters.length)!==expected.spec.styleId||!recipeEqual(n,expected.spec)||n.height<=0)errors.push({kind:'EXPECTED_TEXT',id:n.id});}
 const changedIds=new Set(texts.map(t=>t.node.id));
 for(const before of originalTextBefore){const node=allOriginalText.find(n=>n.id===before.id),after=glyphSnapshot(node);if(changedIds.has(before.id)){for(const key of ['characters','height']){delete before[key];delete after[key];}}if(!equal(before,after))errors.push({kind:'ORIGINAL_TEXT_PRESERVATION',id:node.id});}
 const changedCardIds=new Set(baseCards.map(e=>e.cardId));
 for(const before of originalCardsBefore){const node=originalCards.find(n=>n.id===before.id),after=frameSnapshot(node);if(changedCardIds.has(before.id)){delete before.height;delete after.height;}if(!equal(before,after))errors.push({kind:'ORIGINAL_CARD_PRESERVATION',id:node.id});}
 for(let i=0;i<resolvedBoards.length;i++){const before=boardBefore[i],after=frameSnapshot(resolvedBoards[i]);delete before.height;delete after.height;if(i===3){after.children=after.children.filter(id=>!lastBoard.children.some(n=>n.id===id&&newNames.has(n.name)));before.children=before.children.filter(id=>!existingNew.some(n=>n.id===id));}if(!equal(before,after))errors.push({kind:'BOARD_PRESERVATION',id:after.id});}
 const finalCards=resolvedBoards.flatMap(b=>b.children.filter(n=>n.type==='FRAME'));
 if(finalCards.length!==79||new Set(finalCards.map(n=>n.name)).size!==79)errors.push({kind:'FINAL_CARD_COVERAGE',count:finalCards.length});
 return {status:errors.length?'PATCH_READBACK_FAILED':events.length||createdCards.length?'PATCH_APPLIED_AWAITING_INDEPENDENT_QA':'UNCHANGED_AWAITING_INDEPENDENT_QA',pageId:page.id,createdNodeIds,createdCards,changedExistingIds:[...changedExistingIds],events,originalCardsPreserved:75,styleCards:finalCards.length,styleCount:79,baseCount:18,compatibilityCount:61,boards:resolvedBoards.map(b=>({id:b.id,name:b.name,cards:b.children.filter(n=>n.type==='FRAME').length,width:b.width,height:b.height})),errors,source,mappingApplicationBlockedSegments:PLAN.applicationBlockedSegments,consumerValidation:'NOT_PERFORMED',visualQA:'NOT_RUN'};
}catch(error){return {status:writesStarted?'PARTIAL_FAILURE_REQUIRES_READBACK':'PREFLIGHT_FAILED_NO_MUTATION',error:String(error),pageId:page?.id??null,createdNodeIds,createdCards,changedExistingIds:[...changedExistingIds],events,source,consumerValidation:'NOT_PERFORMED',visualQA:'NOT_RUN'};}
