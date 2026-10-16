// Release regression: real Next build, isolated file://, conditional assets, keyboard,
// native dialog return, measured identities, and self-contained Markdown handoff.
import {readFileSync,writeFileSync,symlinkSync} from 'node:fs';
import {spawnSync} from 'node:child_process';
import path from 'node:path';
const [packagedSkill,modulesArg,outputArg]=process.argv.slice(2);
if(!outputArg)throw new Error('Uso: node scripts/verify-offline.mjs <skill-empaquetada> <node_modules-existente> <salida-nueva>');
const skill=path.resolve(packagedSkill),modules=path.resolve(modulesArg),output=path.resolve(outputArg);
const run=(script,args=[],cwd=output)=>{
 const result=spawnSync(process.execPath,[script,...args],{cwd,stdio:'inherit',env:{...process.env,PATH:path.dirname(process.execPath)+path.delimiter+process.env.PATH}});
 if(result.status!==0)throw new Error(`Fallo ${script}: ${result.status??result.error}`);
};
run(path.join(skill,'scripts/init.mjs'),[output],path.dirname(output));
symlinkSync(modules,path.join(output,'node_modules'),'dir');
const manifest=JSON.parse(readFileSync(path.join(output,'references/snapshot-manifest.json')));
const family=name=>manifest.components.find(item=>(item.exports??[item.exportName]).includes(name));
for(const name of ['Button','Modal','Avatar','Logos','InputField'])if(!family(name))throw new Error(`Falta familia ${name}`);
const ids=Object.fromEntries(['Button','Modal','Avatar','Logos','InputField'].map(name=>[name,family(name).id]));
const buttonProps={showLeftIcon:false,showRightIcon:false};
const modalProps={open:true,variant:'media',title:'Detalle portable'};
const inputProps={label:'Buscar',value:'',showTrailingIcon:false};
writeFileSync(path.join(output,'prototype/page.tsx'),`'use client';
import {useEffect,useState} from 'react';
import {Button,Modal,Avatar,Logos,InputField} from '@contpaqi/ui';
import {DSNode} from './evidence';
export default function Page(){
 const [open,setOpen]=useState(false);const [variant,setVariant]=useState<'media'|'side-by-side'>('media');const [value,setValue]=useState('');
 useEffect(()=>{const handler=(event:KeyboardEvent)=>{if(open&&event.key==='m')setVariant('side-by-side');};window.addEventListener('keydown',handler);return()=>window.removeEventListener('keydown',handler);},[open]);
 const bp=${JSON.stringify(buttonProps)};const mp={open:true,variant,title:'Detalle portable'};const ip={label:'Buscar',value,showTrailingIcon:false};
 return <main data-ds-theme="contable" className="min-h-screen p-8">
 <DSNode id="composition" component="LOCAL-demo" props={{}}><section className="flex flex-col gap-6 items-start">
 <DSNode id="heading" component="LOCAL-heading" props={{}}><h1 className="ds-type-heading-5-bold">Prueba portable CONTPAQi</h1></DSNode>
 <DSNode id="search" component="${ids.InputField}" props={ip}><InputField {...ip} id="search-input" onChange={event=>setValue(event.target.value)}/></DSNode>
 <DSNode id="open" component="${ids.Button}" props={bp}><Button {...bp} id="open-modal" onClick={()=>setOpen(true)}>Abrir detalle</Button></DSNode>
 <DSNode id="feedback" component="LOCAL-feedback" props={{}}><p id="value" className="ds-type-body-regular">Consulta: {value||'vacía'}</p></DSNode>
 {open&&variant==='media'&&<DSNode id="media-modal" component="${ids.Modal}" props={mp}><Modal {...mp} onOpenChange={setOpen}>Presiona M para ver el detalle con contenido variable.</Modal></DSNode>}
 {open&&variant==='side-by-side'&&<DSNode id="side-modal" component="${ids.Modal}" props={mp}><Modal {...mp} onOpenChange={setOpen}>
  <div className="flex flex-col gap-4 items-start">
   <DSNode id="avatar" component="${ids.Avatar}" props={{label:'Persona ficticia'}}><Avatar label="Persona ficticia"/></DSNode>
   <DSNode id="logo" component="${ids.Logos}" props={{alt:'CONTPAQi'}}><Logos alt="CONTPAQi"/></DSNode>
   <DSNode id="switch" component="${ids.Button}" props={bp}><Button {...bp} id="switch-media" onClick={()=>setVariant('media')}>Volver al medio</Button></DSNode>
  </div>
 </Modal></DSNode>}
 </section></DSNode></main>;
}
`);
const baseNodes=['composition','heading','search','open','feedback'];
const opened=[...baseNodes,'media-modal'];
const sideOpened=[...baseNodes,'side-modal','avatar','logo','switch'];
const click={type:'click',selector:'#open-modal'};
const states=[
 {id:'initial',name:'Inicial',actions:[],expect:[{selector:'dialog',visible:false},{selector:'#value',text:'vacía'}],nodes:baseNodes},
 {id:'open',name:'Modal Media con contenido textual',actions:[click],expect:[{selector:'dialog',visible:true},{selector:'.ds-modal-body',text:'Presiona M'}],nodes:opened},
 {id:'side',name:'Medio dinámico y contenido variable SideBySide',actions:[click,{type:'press',selector:'dialog',key:'m'}],expect:[{selector:'.ds-modal-side-by-side',visible:true},{selector:'img[alt="CONTPAQi"]',visible:true}],nodes:sideOpened},
 {id:'close',name:'Cerrar y volver',actions:[click,{type:'click',selector:'button[aria-label="Cerrar diálogo"]'}],expect:[{selector:'dialog',visible:false},{selector:'#open-modal',visible:true}],nodes:baseNodes},
 {id:'keyboard',name:'Activar con Enter',actions:[{type:'press',selector:'#open-modal',key:'Enter'}],expect:[{selector:'dialog',visible:true}],nodes:opened},
 {id:'escape',name:'Cancelar con Escape',actions:[click,{type:'press',selector:'dialog',key:'Escape'}],expect:[{selector:'dialog',visible:false}],nodes:baseNodes},
 {id:'filled',name:'Entrada controlada',actions:[{type:'fill',selector:'#search-input',value:'PO'}],expect:[{selector:'#value',text:'Consulta: PO'}],nodes:baseNodes}
];
const ds=(instanceId,exportName,props,extra={})=>({instanceId,componentId:ids[exportName],exportName,kind:'ds',placement:'Composición de verificación',props,tokens:['color/background/default'],slots:[{name:'contenido',status:exportName==='Modal'?'REQUIRED':'NOT_APPLICABLE',content:exportName==='Modal'?'Contenido variable Avatar, Logos y acción':'Anatomía y props de la familia; sin región abierta adicional'}],omissions:[],...extra});
const localContent=instanceId=>({instanceId,componentId:'LOCAL-'+instanceId,exportName:instanceId==='heading'?'h1':'p',kind:'local-content',placement:'Columna principal',props:{},tokens:['color/text/primary','font/family/base'],slots:[{name:'text',status:'NOT_APPLICABLE',content:'Texto simple con tipografía y color del DS'}],omissions:[],reason:'Contenido local del prototipo, no nueva familia DS'});
const brief={title:'Verificación offline',objective:'Verificar HTML autónomo, assets condicionales, fuente, teclado y traspaso',theme:'Contable',viewports:[{width:1440,height:900},{width:1000,height:760}],screens:[{id:'demo',name:'Demo',entry:'Abrir el archivo',layout:'Columna con padding 32 px y gap 24 px; modal nativo según contrato.',content:'Datos ficticios de validación.',states}],transitions:[{from:'demo',action:'Abrir/Cerrar detalle y Escape',to:'demo',feedback:'Modal visible u oculto sin recargar'}],components:[localContent('heading'),localContent('feedback'),{instanceId:'composition',componentId:'LOCAL-demo',exportName:'DemoComposition',kind:'local-composition',placement:'Raíz',props:{},tokens:['color/background/default'],slots:[{name:'body',status:'REQUIRED',content:'InputField, Button y Modal condicional'}],omissions:[],reason:'Composición local para verificar el release; no componente nuevo de biblioteca',compositionOf:Object.values(ids)},ds('search','InputField',inputProps,{stateProps:{'demo/filled':{...inputProps,value:'PO'}}}),ds('open','Button',buttonProps),ds('media-modal','Modal',modalProps,{slots:[{name:'Title/Content',status:'NOT_APPLICABLE',content:'Media conserva título y contenido TEXT; sin BodySlot variable'}]}),ds('side-modal','Modal',{...modalProps,variant:'side-by-side'}),ds('avatar','Avatar',{label:'Persona ficticia'}),ds('logo','Logos',{alt:'CONTPAQi'}),ds('switch','Button',buttonProps)],decisions:['Composición local de verificación y datos ficticios','Atajo M local para cambiar de Media a SideBySide durante la prueba; no comportamiento normativo del DS'],limitations:['No backend; no fidelidad Figma afirmada'],checks:[{name:'Revisión visual',status:'NOT_RUN',evidence:'Abrir los PNG de capture después de ejecutar este script.'}],figmaTarget:null};
writeFileSync(path.join(output,'brief.json'),JSON.stringify(brief,null,2)+'\n');
run('scripts/prepare.mjs');
run(path.join(modules,'next/dist/bin/next'),['build','--webpack']);
run('scripts/inline-export.mjs',['out/index.html','render.html']);
run('scripts/capture.mjs');
run('scripts/handoff.mjs');
const report=JSON.parse(readFileSync(path.join(output,'capture/report.json')));
if(report.status!=='PASS'||report.states.length!==14)throw new Error('QA no completó todos los estados/viewports.');
const md=readFileSync(path.join(output,'entrega/replicar-en-figma.md'),'utf8');
const block=md.match(/```json\n([\s\S]*?)\n```/);
if(!block)throw new Error('Markdown no incluye bloque autosuficiente.');
const handoff=JSON.parse(block[1]);
if(handoff.consumer_skill!=='contpaqi-figma-screens'||handoff.capture.states.length!==14||handoff.components.length!==10)throw new Error('Traspaso incompleto.');
for(const state of report.states){
 const heading=state.nodes.find(node=>node.id==='heading');
 if(heading?.typography_style_id!=='heading-5-bold'||!heading.text_runs.some(run=>run.typography_style_id==='heading-5-bold'&&run.computed_style.fontSize==='24px'))throw new Error('Identidad tipográfica no capturada desde CSS efectivo.');
}
// Keep the offline gate aligned with the current normative dependency closure.
const requiredTypographySources=[
 'specs/tokens/ai-design-system.typography.v0.1.2.json',
 'specs/foundations/typography.contract.v0.1.0.md',
 'specs/foundations/typography.formatting.amendment.v0.1.1.md',
 'specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md',
 'specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md',
 ...['Button','Modal','Avatar','Logos','InputField'].map(name=>{
  const amendment=family(name).amendments?.find(source=>source.includes('.typography.amendment.'));
  if(!amendment)throw new Error(`Falta enmienda tipográfica de ${name}`);
  return amendment;
 })
];
if(!requiredTypographySources.every(required=>handoff.sources.some(source=>source.path===required)))throw new Error('Markdown pierde una fuente normativa de tipografía 0.1.2.');
if(!handoff.typography.styles.some(style=>style.id==='heading-5-bold')||!handoff.capture.states.every(state=>state.nodes.find(node=>node.id==='heading')?.text_runs.some(run=>run.typography_style_id==='heading-5-bold')))throw new Error('Markdown pierde identidad o métricas tipográficas.');
console.log(`PASS: 14 estados/viewports, assets condicionales, modal, teclado, fuente, nodos/props, identidad tipográfica efectiva y Markdown autosuficiente. Evidencia ${output}`);
