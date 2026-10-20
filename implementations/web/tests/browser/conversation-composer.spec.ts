import { test, expect } from '@playwright/test';
import { mkdirSync, writeFileSync } from 'node:fs';

test('Composer: aviso opcional, callback independiente y reflow en cuatro temas', async ({ page }) => {
 const evidence='../../output/qa/conversation-composer-2026-10-20';
 mkdirSync(evidence,{recursive:true});
 await page.goto('/#conversation');
 await page.evaluate(()=>document.fonts.ready);
 const preview=page.locator('.component-preview');
 const composer=preview.locator('.ds-composer');
 const notice=composer.locator('.ds-composer-action-container');
 await expect(notice).toBeHidden();
 await preview.getByRole('switch',{name:'Mostrar aviso de ejemplo'}).check();
 await expect(notice).toBeVisible();
 await composer.getByRole('textbox',{name:'Mensaje',exact:true}).fill('Mensaje conservado');
 await notice.getByRole('button',{name:'Ver detalle'}).click();
 await expect(preview.getByRole('status')).toContainText('Acción local de ejemplo');
 await expect(composer.getByRole('textbox',{name:'Mensaje',exact:true})).toHaveValue('Mensaje conservado');
 await expect(preview.locator('.ds-conversation-message')).toHaveCount(0);
 const rows=[];
 for(const theme of ['contable','administrativo','servicios','personas']){
  await page.getByLabel('Tema del sistema de diseño').selectOption(theme);
  for(const width of [616,360]){
   await composer.evaluate((el,width)=>{el.style.width=`${width}px`;},width);
   const metrics=await notice.evaluate(el=>{
    const box=el.querySelector('.ds-composer-action-message')!;
    const text=el.querySelector('.ds-composer-action-description')!;
    const button=el.querySelector('button')!;
    const b=box.getBoundingClientRect(),t=text.getBoundingClientRect(),a=button.getBoundingClientRect();
    const style=getComputedStyle(box);
    return {width:el.getBoundingClientRect().width,messageHeight:b.height,textWidth:t.width,textHeight:t.height,
     textFits:t.right<=a.left,buttonFits:a.right<=b.right,gap:a.left-t.right,
     border:style.borderTopColor,expectedBorder:getComputedStyle(el).getPropertyValue('--ds-color-border-subtle').trim(),
     typography:getComputedStyle(text).getPropertyValue('--ds-type-style-id').trim(),
     emphasis:getComputedStyle(text.querySelector('strong')!).getPropertyValue('--ds-type-style-id').trim()};
   });
   expect(metrics.textFits).toBe(true);expect(metrics.buttonFits).toBe(true);expect(metrics.gap).toBe(8);
   expect(metrics.typography).toBe('caption-regular');expect(metrics.emphasis).toBe('caption-semibold');
   rows.push({theme,...metrics});
  }
 }
 expect(new Set(rows.map(r=>r.border)).size).toBe(4);
 await page.getByLabel('Tema del sistema de diseño').selectOption('contable');
 await composer.screenshot({path:evidence+'/web-360.png'});
 await notice.locator('.ds-composer-action-description').evaluate(el=>{el.textContent='Aviso largo de prueba sin reglas de negocio. '.repeat(12);});
 const long=await notice.evaluate(el=>({scrollWidth:el.scrollWidth,width:el.clientWidth,height:el.clientHeight}));
 expect(long.scrollWidth).toBeLessThanOrEqual(long.width);
 expect(long.height).toBeGreaterThan(rows.find(r=>r.width===360)!.messageHeight);
 await preview.getByRole('switch',{name:'Mostrar aviso de ejemplo'}).uncheck();
 await expect(notice).toBeHidden();
 await composer.getByRole('button',{name:'Enviar mensaje'}).click();
 await expect(preview.locator('.ds-conversation-message')).toHaveText('Mensaje conservado');
 writeFileSync(evidence+'/web-results.json',JSON.stringify({result:'PASS',rows,long,callbackIndependent:true,sendPreserved:true},null,2));
});
