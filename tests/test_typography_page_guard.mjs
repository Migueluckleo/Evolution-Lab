import fs from 'node:fs';
import assert from 'node:assert/strict';
import path from 'node:path';
import { createHash } from 'node:crypto';
const template=fs.readFileSync(new URL('../implementations/figma/typography.v0.1.1.apply-ranges.js',import.meta.url),'utf8');
const AsyncFunction=Object.getPrototypeOf(async function(){}).constructor;
const clone=x=>JSON.parse(JSON.stringify(x));
const hash=x=>{let a=2166136261,b=5381;for(const c of JSON.stringify(x)){let t=c.charCodeAt(0);a=Math.imul(a^t,16777619)>>>0;b=(Math.imul(b,33)^t)>>>0;}return a.toString(36)+'.'+b.toString(36);};
const spec={fontFamily:'Manrope',fontStyle:'Regular',fontWeight:400,fontSize:14,lineHeight:{unit:'PIXELS',value:20},letterSpacing:{unit:'PERCENT',value:0},textDecoration:'NONE',figmaId:'S:good',bindings:{fontFamily:{type:'VARIABLE_ALIAS',id:'VariableID:family'}}};
const tests=[
 ['own+expected outside link','PASS',ctx=>ctx.link(ctx.b)],
 ['outside tiny metric drift','FAIL',ctx=>ctx.b.recipe.fontSize+=1e-7],
 ['outside wrong ID','FAIL',ctx=>ctx.b.recipe.textStyleId='S:foreign'],
 ['editorial canonical ID','FAIL',ctx=>ctx.link(ctx.doc)],
 ['ancestor geometry','FAIL',ctx=>ctx.frame.width+=1],
 ['outside text content','FAIL',ctx=>ctx.b.characters='oops'],
 ['outside property reference','FAIL',ctx=>ctx.b.componentPropertyReferences={characters:'other#1'}],
 ['noncanonical binding','FAIL',ctx=>{ctx.link(ctx.b);ctx.b.recipe.boundVariables.fontFamily.id='VariableID:wrong';}],
 ['equivalent Manrope axis','PASS',ctx=>ctx.b.recipe.fontName.variationSettings={wght:400}],
 ['other Manrope axis','FAIL',ctx=>ctx.b.recipe.fontName.variationSettings={wght:500}],
 ['nontext binding','FAIL',ctx=>ctx.frame.boundVariables={width:{type:'VARIABLE_ALIAS',id:'x'}}],
 ['shared style mutation','FAIL',ctx=>ctx.style.fontSize=15],
 ['exception still guards','FAIL',ctx=>{ctx.frame.width++;throw Error('setter');}],
 ['empty editorial binding','FAIL',ctx=>ctx.empty.boundVariables={fontSize:{type:'VARIABLE_ALIAS',id:'x'}}],
 ['hidden outsider format','FAIL',ctx=>ctx.doc.recipe.textDecoration='UNDERLINE'],
 ['variant definitions getter guarded','PASS',ctx=>{}],
 ['large preferences preserved','PASS',ctx=>{}],
 ['large shared preferences changed','FAIL',ctx=>ctx.frame.componentProperties.icon.preferredValues[999].key='changed'],
 ['cycle before writes','FAIL',ctx=>{}],
 ['cycle after write','FAIL',ctx=>{const cyclic={};cyclic.self=cyclic;ctx.frame.effects=cyclic;}],
 ['real main relationship changed','FAIL',ctx=>ctx.frame.actualMainId='different'],
 ['dictionary key order equivalent','PASS',ctx=>ctx.frame.componentProperties={a:{a:1,b:2},z:3}],
 ['font key order equivalent','PASS',ctx=>ctx.b.recipe.fontName={style:'Regular',family:'Manrope'}],
 ['node singleton alias array','PASS',ctx=>{}],
 ['node uniform alias array','PASS',ctx=>{}],
 ['node mixed alias array','FAIL',ctx=>{}],
 ['node wrong singleton alias','FAIL',ctx=>{}],
 ['rematerialized descendant proxy','PASS',ctx=>{}],
 ['post getter unreadable retained report','FAIL',ctx=>{}],
 ['post style unreadable retained report','FAIL',ctx=>{}],
 ['exact zero tracking unit conversion','PASS',ctx=>ctx.b.recipe.letterSpacing={unit:'PIXELS',value:0}],
 ['nonzero tracking unit conversion','FAIL',ctx=>ctx.b.recipe.letterSpacing={unit:'PIXELS',value:0.1}],
 ['tiny nonzero tracking is not zero','FAIL',ctx=>ctx.b.recipe.letterSpacing={unit:'PIXELS',value:1e-10}]
];
for(const [name,want,sideEffect] of tests){
 const root={id:'root',type:'DOCUMENT'},page={id:'p',type:'PAGE',name:'Table',parent:root,children:[]};
 const frame={id:'frame',type:'FRAME',name:'frame',parent:page,width:100,height:100,children:[],boundVariables:{}};
 const make=(id,chars='Text')=>({id,type:'TEXT',name:id,parent:frame,width:30,height:20,characters:chars,visible:true,textAutoResize:'WIDTH_AND_HEIGHT',textCase:'ORIGINAL',textDecoration:'NONE',textAlignHorizontal:'LEFT',textAlignVertical:'TOP',paragraphSpacing:0,paragraphIndent:0,componentPropertyReferences:{},boundVariables:{},textStyleId:'',recipe:{fontName:{family:'Manrope',style:'Regular'},fontWeight:400,fontSize:14,lineHeight:{unit:'PIXELS',value:20},letterSpacing:{unit:'PERCENT',value:0},textDecoration:'NONE',textCase:'ORIGINAL',textStyleId:'',textStyleOverrides:[],boundVariables:{},fills:[],hyperlink:null,paragraphSpacing:0,paragraphIndent:0},getStyledTextSegments(fields,start=0,end=this.characters.length){if(!this.characters.length)return [];return [{characters:this.characters.slice(start,end),start,end,...Object.fromEntries(fields.filter(f=>f in this.recipe).map(f=>[f,clone(this.recipe[f])]))}];},getRangeTextStyleId(){return this.recipe.textStyleId;}});
 const a=make('a'),b=make('b'),doc=make('doc'),empty=make('empty','');doc.visible=false;
 if(name.startsWith('node ')){a.boundVariables={fontFamily:[clone(spec.bindings.fontFamily)]};if(name==='node uniform alias array')a.boundVariables.fontFamily.push(clone(spec.bindings.fontFamily));if(name==='node mixed alias array')a.boundVariables.fontFamily.push({type:'VARIABLE_ALIAS',id:'other'});if(name==='node wrong singleton alias')a.boundVariables.fontFamily[0].id='other';}
 const set={id:'set',type:'COMPONENT_SET',name:'set',parent:page,children:[],componentPropertyDefinitions:{},boundVariables:{}};
 const variant={id:'variant',type:'COMPONENT',name:'variant',parent:set,children:[],boundVariables:{},get componentPropertyDefinitions(){throw Error('variant definitions forbidden');}};set.children=[variant];
 let preferenceReads=0,mainReads=0,writeCalls=0;
 if(name.startsWith('large')){const preferences={icon:{type:'INSTANCE_SWAP',value:'icon',preferredValues:Array.from({length:1500},(_,i)=>({type:'COMPONENT',key:'a'.repeat(60)+i}))}};Object.defineProperty(frame,'componentProperties',{get(){preferenceReads++;return preferences;}});}
 if(name==='cycle before writes'){frame.effects={};frame.effects.self=frame.effects;}
 if(name==='real main relationship changed'){frame.type='INSTANCE';frame.actualMainId='main';frame.getMainComponentAsync=async()=>{mainReads++;return {id:frame.actualMainId};};}
 if(name==='dictionary key order equivalent')frame.componentProperties={z:3,a:{b:2,a:1}};
 frame.children=[a,b,doc,empty];page.children=[frame,set];const all=[frame,a,b,doc,empty,set,variant];page.findAll=fn=>all.filter(fn);page.findAllWithCriteria=({types})=>all.filter(n=>types.includes(n.type));
 if(name==='rematerialized descendant proxy'||name==='post getter unreadable retained report'){
  let lookups=0,stale=false;const fresh={...a};Object.defineProperty(a,'width',{get(){if(stale)throw Error('stale proxy');return 30;}});
  page.findAllWithCriteria=({types})=>{lookups++;if(lookups>1)stale=true;return all.filter(n=>types.includes(n.type)).map(n=>lookups>1&&n===a&&name==='rematerialized descendant proxy'?fresh:n);};
 }
 const style={id:'S:good',type:'TEXT',fontName:{family:'Manrope',style:'Regular',variationSettings:{wght:400}},fontSize:14,lineHeight:{unit:'PIXELS',value:20},letterSpacing:{unit:'PERCENT',value:0},textDecoration:'NONE',boundVariables:clone(spec.bindings)};
 const link=n=>{n.recipe.textStyleId='S:good';n.recipe.boundVariables=clone(spec.bindings);n.boundVariables=clone(spec.bindings);};
 a.setRangeTextStyleIdAsync=async()=>{writeCalls++;link(a);sideEffect({a,b,doc,empty,frame,style,link});};
 const preservation=hash({characters:a.characters,textCase:a.textCase,textDecoration:a.textDecoration,fills:[[]],hyperlinks:[null],paragraphSpacing:0,paragraphIndent:0,props:{},ancestors:['frame','p'],visible:true,textAutoResize:a.textAutoResize,textAlignHorizontal:'LEFT',textAlignVertical:'TOP'});
 const replacements={PAGE_ID:'p',PAGE_EXPECTATIONS:{paths:['a','b'],logical:['test'],ranges:[[[0,4,0]]],rows:[[0,0,0],[0,1,0]]},STYLES:{test:spec},PAGE_GUARD_METADATA:{test:true},ENTRIES:[[0,30,20,preservation]]};
 let source=template;for(const[k,v]of Object.entries(replacements))source=source.replace(k,JSON.stringify(v));
 let styleReads=0;const figma={getNodeByIdAsync:async()=>page,setCurrentPageAsync:async()=>{},getStyleByIdAsync:async()=>{styleReads++;if(name==='post style unreadable retained report'&&styleReads>1)throw Error('style proxy unavailable');return style;},loadFontAsync:async()=>{}};
 const result=await new AsyncFunction('figma',source)(figma);
 const actual=result.status==='PASS_PAGE_GUARD_GLOBAL_READBACK_REQUIRED'?'PASS':'FAIL';assert.equal(actual,want,JSON.stringify({name,result}));
 if(want==='FAIL')assert.ok(result.errorCount>0, name);
 if(name.startsWith('large'))assert.equal(preferenceReads,name.endsWith('changed')?3:2,'Each phase must read the full preferences exactly once');
 if(name==='cycle before writes')assert.equal(writeCalls,0,'Unreadable before evidence must prevent writes');
 if(name==='cycle after write')assert.equal(result.pageGuard.status,'BLOCKED_UNREADABLE');
 if(name==='real main relationship changed')assert.equal(mainReads,2,'Re-read actual relationships after writes');
 if(name.startsWith('post ')){assert.deepEqual(result.mutatedNodeIds,['a']);assert.ok(result.errors.some(e=>e.some(v=>String(v).includes('UNREADABLE'))));}
 if(name==='outside tiny metric drift')assert.equal(result.recipeDiffs[0].fields[0].field,'fontSize');
 if(name==='ancestor geometry')assert.deepEqual(result.geometryDiffs[0].fields,[{field:'props.width',before:100,after:101}]);
 if(name==='large shared preferences changed'){const diff=result.geometryDiffs[0].fields.find(f=>f.field==='props.componentProperties');assert.equal(diff.before.omitted,true);assert.match(diff.before.preview,/preferredValues/);assert.ok(!('valueRef' in diff.before));}
 console.log(name,actual,result.pageGuard?.affectedNodeCount??'-');
}
let parsed=0;
if(process.argv[2]){
 const directory=path.resolve(process.argv[2]);
 const manifest=JSON.parse(fs.readFileSync(path.join(directory,'manifest.json'),'utf8'));
 const actual=fs.readdirSync(directory).filter(p=>p.endsWith('.js')).sort();
 assert.deepEqual(actual,manifest.map(m=>m.name+'.js').sort(),'Generated files must match the manifest exactly');
 for(const entry of manifest){const bytes=fs.readFileSync(path.join(directory,entry.name+'.js'));assert.equal(bytes.length,entry.bytes);assert.equal(createHash('sha256').update(bytes).digest('hex'),entry.sha256);new AsyncFunction('figma',bytes.toString('utf8'));parsed++;}
}
console.log(`PASS: ${tests.length} mutation/preservation scenarios${process.argv[2]?`; ${parsed} exact generated scripts parse`:''}`);
