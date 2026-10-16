import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const template=execFileSync('python3',['-c',"import sys;sys.path.insert(0,'implementations/figma');from typography_contextual_recovery import recovery_template;print(recovery_template())"],{cwd:root,encoding:'utf8'});
const AsyncFunction=Object.getPrototypeOf(async function(){}).constructor;
const clone=x=>JSON.parse(JSON.stringify(x));
const hash=x=>{let a=2166136261,b=5381;for(const c of JSON.stringify(x)){let t=c.charCodeAt(0);a=Math.imul(a^t,16777619)>>>0;b=(Math.imul(b,33)^t)>>>0;}return a.toString(36)+'.'+b.toString(36);};
const ids=['I420:232;26:104','I420:249;26:104','I420:266;26:104','I420:283;26:299','I420:299;26:104','I420:313;26:104'];
const widths=[90,90,90,90,121,124],lengths=[13,13,13,13,18,16];
const binding={type:'VARIABLE_ALIAS',id:'VariableID:family'};
const target={fontFamily:'Manrope',fontStyle:'Bold',fontWeight:700,fontSize:14,lineHeight:{unit:'PIXELS',value:20},letterSpacing:{unit:'PIXELS',value:0},textDecoration:'NONE',figmaId:'S:target',bindings:{fontFamily:binding}};
const source={...clone(target),letterSpacing:{unit:'PERCENT',value:0.1},figmaId:'S:source'};
const cases=[
 ['six exact corrections','PASS'],
 ['already restored retry','PASS'],
 ['wrong source style','PREFLIGHT'],
 ['other tracking','PREFLIGHT'],
 ['original content changed','PREFLIGHT'],
 ['unexpected current width','PREFLIGHT'],
 ['missing geometry ledger','PREFLIGHT'],
 ['current geometry mismatch','PREFLIGHT'],
 ['foreign alias before','PREFLIGHT'],
 ['existing fill alias retained','PASS'],
 ['fill alias changed','FAIL'],
 ['geometry exception on Success','PREFLIGHT'],
 ['wrong restored width','FAIL'],
 ['ancestor layout drift','FAIL'],
 ['unlisted geometry drift','FAIL'],
 ['listed geometry wrong after','FAIL'],
 ['outside style drift','FAIL'],
 ['outside tiny metric drift','FAIL'],
 ['outside component API drift','FAIL'],
 ['wrong alias after','FAIL'],
 ['unexpected color drift','FAIL'],
 ['shared source style mutation','FAIL'],
 ['other typography changed','FAIL'],
 ['non-typographic format changed','FAIL'],
 ['throw after write still guards','FAIL'],
];
for(const [name,want] of cases){
 const doc={id:'root',type:'DOCUMENT'},page={id:'394:122',type:'PAGE',name:'Input Fields',parent:doc,children:[]};
 const component={id:'420:290',type:'COMPONENT',name:'Success',parent:page,children:[],width:500,height:162,layoutMode:'VERTICAL',componentPropertyDefinitions:{},boundVariables:{}};
 const buttons=ids.map((id,i)=>({id:id.split(';')[0].slice(1),type:'INSTANCE',name:'Button',parent:component,children:[],width:widths[i]+32+(i===4?1:0),height:32,layoutMode:'HORIZONTAL',itemSpacing:8,boundVariables:{},componentProperties:{Label:{type:'TEXT',value:'Original'}},async getMainComponentAsync(){return{id:'main'+i};}}));
 const make=(id,parent,width,characters)=>({id,type:'TEXT',name:'Label',parent,width,height:20,characters,visible:false,textAutoResize:'WIDTH_AND_HEIGHT',textCase:'ORIGINAL',textDecoration:'NONE',textAlignHorizontal:'LEFT',textAlignVertical:'TOP',paragraphSpacing:0,paragraphIndent:0,componentPropertyReferences:{characters:'Label#0'},boundVariables:{fontFamily:[clone(binding)]},recipe:{fontName:{family:'Manrope',style:'Bold'},fontWeight:700,fontSize:14,lineHeight:{unit:'PIXELS',value:20},letterSpacing:{unit:'PERCENT',value:Math.fround(0.1)},textDecoration:'NONE',textCase:'ORIGINAL',textStyleId:'S:source',textStyleOverrides:[],boundVariables:{fontFamily:clone(binding)},fills:[],hyperlink:null,paragraphSpacing:0,paragraphIndent:0},getStyledTextSegments(fields,start=0,end=this.characters.length){return[{characters:this.characters.slice(start,end),start,end,...Object.fromEntries(fields.filter(f=>f in this.recipe).map(f=>[f,clone(this.recipe[f])]))}];},getRangeTextStyleId(){return this.recipe.textStyleId;}});
 const nodes=ids.map((id,i)=>make(id,buttons[i],widths[i]+(i===4?1:0),'X'.repeat(lengths[i])));
 const outsider=make('outside',component,120,'Other');
 buttons.forEach((button,i)=>button.children=[nodes[i]]);component.children=[...buttons,outsider];page.children=[component];
 const all=[component,...buttons,...nodes,outsider];page.findAll=f=>all.filter(f);page.findAllWithCriteria=({types})=>all.filter(n=>types.includes(n.type));
 const liveStyles=Object.fromEntries([source,target].map(s=>[s.figmaId,{id:s.figmaId,type:'TEXT',fontName:{family:s.fontFamily,style:s.fontStyle},fontSize:s.fontSize,lineHeight:clone(s.lineHeight),letterSpacing:clone(s.letterSpacing),textDecoration:s.textDecoration,boundVariables:clone(s.bindings)}]));
 const preservation=n=>hash({characters:n.characters,textCase:n.textCase,textDecoration:n.textDecoration,fills:[[]],hyperlinks:[null],paragraphSpacing:0,paragraphIndent:0,props:n.componentPropertyReferences,ancestors:[n.parent.id,component.id,page.id],visible:false,textAutoResize:n.textAutoResize,textAlignHorizontal:n.textAlignHorizontal,textAlignVertical:n.textAlignVertical});
 const entries=nodes.map((n,i)=>[i,widths[i],20,preservation(n)]);
 nodes[4].x=8;const geometry=[{id:ids[4],fields:{width:{before:122,after:121},x:{before:8,after:9}}}];
 let writes=0;
 for(const [i,n] of nodes.entries())n.setRangeTextStyleIdAsync=async()=>{
  writes++;n.recipe.textStyleId=target.figmaId;n.recipe.letterSpacing=clone(target.letterSpacing);
  if(i===4){n.width=121;n.x=9;}
  if(writes!==1)return;
  if(name==='wrong restored width')nodes[4].width=120;
  if(name==='ancestor layout drift')component.itemSpacing=9;
  if(name==='unlisted geometry drift')buttons[0].width++;
  if(name==='listed geometry wrong after')nodes[4].x=10;
  if(name==='outside style drift')outsider.recipe.textStyleId=target.figmaId;
  if(name==='outside tiny metric drift')outsider.recipe.fontSize+=1e-7;
  if(name==='outside component API drift')buttons[1].componentProperties.Label.value='Changed';
  if(name==='wrong alias after')nodes[0].recipe.boundVariables.fontFamily.id='foreign';
  if(name==='fill alias changed')nodes[0].boundVariables.fills[0].id='foreign';
  if(name==='unexpected color drift')nodes[0].recipe.fills=[{type:'SOLID',color:{r:1,g:0,b:0}}];
  if(name==='shared source style mutation')liveStyles['S:source'].fontSize++;
  if(name==='other typography changed')nodes[0].recipe.lineHeight.value=21;
  if(name==='non-typographic format changed')nodes[0].recipe.textCase='UPPER';
  if(name==='throw after write still guards'){outsider.width++;throw Error('injected interrupted setter');}
 };
 // Failures that must survive all six sequential writes are applied by the last setter.
 const last=nodes[5].setRangeTextStyleIdAsync;
 nodes[5].setRangeTextStyleIdAsync=async()=>{await last();if(name==='wrong restored width')nodes[4].width=120;if(name==='listed geometry wrong after')nodes[4].x=10;};
 if(name==='already restored retry'){for(const n of nodes){n.recipe.textStyleId=target.figmaId;n.recipe.letterSpacing=clone(target.letterSpacing);}nodes[4].width=121;nodes[4].x=9;}
 if(name==='wrong source style')nodes[0].recipe.textStyleId='S:foreign';
 if(name==='other tracking')nodes[0].recipe.letterSpacing.value=0.2;
 if(name==='original content changed')nodes[0].characters='Y'.repeat(lengths[0]);
 if(name==='unexpected current width')nodes[1].width++;
 if(name==='missing geometry ledger')geometry.splice(0,1);
 if(name==='current geometry mismatch')nodes[4].x=7;
 if(name==='foreign alias before')nodes[0].boundVariables.fontFamily[0].id='foreign';
 if(name==='existing fill alias retained'||name==='fill alias changed')for(const n of nodes)n.boundVariables.fills=[{type:'VARIABLE_ALIAS',id:'VariableID:13:32'}];
 if(name==='geometry exception on Success')geometry.push({id:component.id,fields:{width:{before:500,after:499}}});
 const replacements={PAGE_ID:page.id,PAGE_EXPECTATIONS:{paths:ids,logical:['ui-label-compact-bold'],ranges:lengths.map(n=>[[0,n,0]]),rows:ids.map((id,i)=>[0,i,i])},STYLES:{'ui-action-label-small':source,'ui-label-compact-bold':target},PAGE_GUARD_METADATA:{test:true},ENTRIES:entries,RECOVERY_RULES:{pageId:page.id,rows:ids.map(id=>({id,source:'ui-action-label-small',target:'ui-label-compact-bold'})),geometry,evidence:[{path:'fixture',sha256:'fixture',locator:'exact tuples'}]}};
 let code=template;for(const [k,v]of Object.entries(replacements))code=code.replace(k,JSON.stringify(v));
 const figma={getNodeByIdAsync:async id=>id===page.id?page:all.find(n=>n.id===id),setCurrentPageAsync:async()=>{},getStyleByIdAsync:async id=>liveStyles[id],loadFontAsync:async()=>{}};
 const result=await new AsyncFunction('figma',code)(figma);
 const actual=result.status==='PREFLIGHT_FAILED_NO_WRITE'?'PREFLIGHT':result.status==='PASS_PAGE_GUARD_GLOBAL_READBACK_REQUIRED'?'PASS':'FAIL';
 assert.equal(actual,want,JSON.stringify({name,result}));
 if(want==='PREFLIGHT'||name==='already restored retry')assert.equal(writes,0,name);
 if(name==='six exact corrections'){assert.equal(writes,6);assert.equal(result.pageGuard.nodesBefore,15);assert.equal(result.pageGuard.nodesAfter,15);assert.equal(result.pageGuard.violationCount,0);}
 if(name==='throw after write still guards')assert.ok(result.pageGuard.affectedNodeCount>0);
 console.log(name,actual);
}
console.log(`PASS: ${cases.length} exact contextual recovery scenarios`);
