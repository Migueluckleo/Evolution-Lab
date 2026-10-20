import { test, expect } from '@playwright/test';
import { mkdirSync, writeFileSync } from 'node:fs';
test('Composer notice slot supports replacement, empty and ordered content without losing draft',async({page})=>{
 const evidence='../../output/qa/conversation-composer-slot-2026-10-20';
 mkdirSync(evidence,{recursive:true});
 await page.goto('/#conversation');await page.evaluate(()=>document.fonts.ready);
 const preview=page.locator('.component-preview'),composer=preview.locator('.ds-composer');
 const notice=composer.locator('.ds-composer-action-container'),slot=notice.locator('.ds-composer-notice-content');
 const picker=preview.getByLabel('Contenido del aviso');
 await expect(notice).toBeHidden();
 await preview.getByRole('switch',{name:'Mostrar aviso de ejemplo'}).check();
 await expect(slot.locator(':scope > *')).toHaveCount(1);
 const draft=composer.getByRole('textbox',{name:'Mensaje',exact:true});
 await draft.fill('Borrador conservado');
 await slot.getByRole('button',{name:'Ver detalle'}).click();
 await expect(draft).toHaveValue('Borrador conservado');
 await picker.selectOption('empty');await expect(slot.locator(':scope > *')).toHaveCount(0);
 await picker.selectOption('multiple');await expect(slot.locator(':scope > *')).toHaveCount(3);
 const rows=[];
 for(const theme of ['contable','administrativo','servicios','personas']){
  await page.getByLabel('Tema del sistema de diseño').selectOption(theme);
  for(const width of [616,360]){
   await composer.evaluate((el,w)=>el.style.width=`${w}px`,width);
   const m=await slot.evaluate(el=>{const r=el.getBoundingClientRect();const children=[...el.children].map(n=>{const b=n.getBoundingClientRect();return {top:b.top,bottom:b.bottom,left:b.left,right:b.right,scroll:n.scrollWidth,width:n.clientWidth};});return {width:r.width,height:r.height,gap:getComputedStyle(el).gap,fits:children.every(c=>c.left>=r.left&&c.right<=r.right&&c.scroll<=c.width),ordered:children.every((c,i)=>!i||c.top>=children[i-1].bottom),count:children.length};});
   expect(m.fits).toBe(true);expect(m.ordered).toBe(true);expect(m.gap).toBe('8px');rows.push({theme,...m,composerWidth:width});
  }
 }
 await picker.selectOption('reordered');await expect(slot.locator(':scope > *').first()).toContainText('Tercero');
 await preview.getByRole('switch',{name:'Mostrar aviso de ejemplo'}).uncheck();
 await preview.getByRole('switch',{name:'Mostrar aviso de ejemplo'}).check();
 await expect(slot.locator(':scope > *').first()).toContainText('Tercero');
 await slot.getByRole('button',{name:'Acción Tercero'}).click();
 await expect(preview.locator('p[role="status"]')).toContainText('Acción local: Tercero');
 await expect(draft).toHaveValue('Borrador conservado');
 await expect(preview.locator('.ds-conversation-message')).toHaveCount(0);
 await picker.selectOption('replacement');await expect(slot.locator(':scope > *')).toHaveCount(1);
 await expect(slot).toContainText('Sustituto');
 await picker.selectOption('multiple');await page.getByLabel('Tema del sistema de diseño').selectOption('contable');
 await composer.screenshot({path:evidence+'/web-360.png'});
 await picker.selectOption('default');await expect(slot.getByRole('button',{name:'Ver detalle'})).toBeVisible();
 await composer.getByRole('button',{name:'Enviar mensaje'}).click();
 await expect(preview.locator('.ds-conversation-message')).toHaveText('Borrador conservado');
 writeFileSync(evidence+'/web-results.json',JSON.stringify({result:'PASS',rows,cases:['undefined','null','three','reorder','replace','visibility','callback','draft','send']},null,2));
});
