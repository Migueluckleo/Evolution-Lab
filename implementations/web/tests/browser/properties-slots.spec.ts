import {test,expect} from '@playwright/test';
import {readFileSync,mkdirSync,writeFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

test('booleanas, swaps, Slots y piezas internas documentadas',async({page})=>{
 execFileSync(process.execPath,['--import','tsx','tests/render-contract-fixtures.tsx']);
 const fixtures=JSON.parse(readFileSync('test-results/contract-fixtures.json','utf8')) as {family:string;name:string;html:string;checks:{selector:string;visible:boolean;srOnly?:boolean}[];order?:string[]}[];
 await page.goto('/');await page.evaluate(()=>document.fonts.ready);
 await page.evaluate(html=>{document.body.innerHTML='<main id="fixtures" data-ds-theme="contable">'+html+'</main>';},fixtures.map((f,i)=>`<section data-fixture="${i}" style="width:1600px;padding:32px;">${f.html}</section>`).join(''));
 await page.evaluate(()=>{document.querySelectorAll('dialog').forEach(d=>{d.setAttribute('open','');d.style.position='relative';d.style.margin='0';});});
 const reports=[];
 for(const theme of ['contable','administrativo','servicios','personas']){
 await page.locator('#fixtures').evaluate((e,t)=>e.setAttribute('data-ds-theme',t),theme);
 const result=await page.evaluate(fixtures=>{
 const failures:unknown[]=[];const rows:unknown[]=[];let count=0;
 const visible=(el:Element|null):boolean=>{if(!el)return false;for(let n:Element|null=el;n;n=n.parentElement){const s=getComputedStyle(n);if(s.display==='none'||s.visibility==='hidden'||n.classList.contains('sr-only'))return false;}return true;};
 for(const [index,f] of fixtures.entries()){
 const root=document.querySelector(`[data-fixture="${index}"]`)!;
 for(const c of f.checks){const el=root.querySelector(c.selector);const actual=visible(el);count++;if(actual!==c.visible)failures.push({family:f.family,name:f.name,selector:c.selector,actual,expected:c.visible});}
 if(f.order){const actual=[...root.querySelectorAll('[data-slot-id]')].map(e=>e.getAttribute('data-slot-id'));count++;if(JSON.stringify(actual)!==JSON.stringify(f.order))failures.push({family:f.family,name:f.name,actual,expected:f.order});}
 if(f.name==='long-content'){const toolbar=root.querySelector('.ds-chat-toolbar')!,body=root.querySelector('.ds-chat-toolbar-body')!,plan=root.querySelector('.ds-chat-toolbar-plan')!;count++;if(toolbar.getBoundingClientRect().height<=791||plan.getBoundingClientRect().top<body.getBoundingClientRect().bottom)failures.push({family:f.family,name:f.name,reason:'Contenido recortado o plan solapado'});}
 if(f.name==='long-detail'){for(const el of root.querySelectorAll('.ds-chart-legend-text')){count++;if(getComputedStyle(el).textOverflow!=='ellipsis'||el.getBoundingClientRect().width>107)failures.push({family:f.family,name:f.name,reason:'Truncado ausente'});}}
 const box=(el:Element)=>({w:el.getBoundingClientRect().width,h:el.getBoundingClientRect().height});
 const assert=(label:string,actual:unknown,expected:unknown)=>{count++;if(JSON.stringify(actual)!==JSON.stringify(expected))failures.push({family:f.family,name:f.name,label,actual,expected});};
 if(f.name.startsWith('dot/')){assert('dot box',box(root.querySelector('svg')!),{w:8,h:8});assert('radius',root.querySelector('circle')?.getAttribute('r'),f.name.endsWith('true')?'4':'3');}
 if(f.name.startsWith('combination/')){const [,n,selected]=f.name.split('/');assert('dots',root.querySelectorAll('circle').length,Number(n));assert('selection',root.querySelectorAll('circle[r="4"]').length,1);assert('selected index',[...root.querySelectorAll('circle')].findIndex(e=>e.getAttribute('r')==='4')+1,Number(selected));assert('box',box(root.querySelector('.ds-step-dots')!),{w:16*Number(n)-8,h:8});}
 if(f.name.startsWith('connector/')){const [,orientation]=f.name.split('/');assert('connector',box(root.querySelector('.ds-stepper-connector')!),{w:orientation==='vertical'?12:80,h:32});assert('line',box(root.querySelector('.ds-stepper-connector>span')!),{w:orientation==='vertical'?4:80,h:orientation==='vertical'?32:4});}
 if(f.name.startsWith('thumb/')){const [,orientation,size,position]=f.name.split('/');assert('track',box(root.querySelector('.ds-scrollbar-thumb')!),{w:orientation==='vertical'?6:272,h:orientation==='vertical'?272:6});const el=root.querySelector('.ds-scrollbar-thumb>span') as HTMLElement;assert('radius',el.style.borderRadius,size==='75%'&&position==='2'?'4px':'3px');}
 if(f.name.startsWith('art/')){const id=f.name.split('/')[1];assert('art',box(root.querySelector('svg')!),{w:id==='2298'?500:id==='2381'?280:150,h:id==='2298'?320:id==='2381'?280:150});}
 rows.push({family:f.family,name:f.name,checks:f.checks.length,slots:f.order?.length});
 }return {count,failures,rows};
 },fixtures);reports.push({theme,...result});
 }
 const evidence=process.env.DS_AUDIT_OUTPUT??'../../qa/implementations/web-contract-audit-2026-10-13';mkdirSync(evidence,{recursive:true});writeFileSync(evidence+'/properties-and-slots.json',JSON.stringify({fixtures:fixtures.length,source:'implementations/web/tests/render-contract-fixtures.tsx',method:'SSR of real exports, computed visibility, slot order and independent dimensions. No claim of React state retention from SSR.',reports},null,2));
 expect(reports.flatMap(r=>r.failures).slice(0,20),'Full failures in properties-and-slots.json').toEqual([]);
});
