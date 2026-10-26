import {test,expect} from '@playwright/test';

test('loading bloquea clic, teclado y navegación; salir de carga restaura la acción',async({page})=>{
 await page.goto('/#button');
 const preview=page.locator('.component-preview');
 const danger=preview.locator('.ds-button-danger');
 await danger.click();await expect(danger).toHaveText('Eliminar · 1');
 await preview.getByRole('button',{name:'Mostrar carga de ejemplo'}).click();
 await expect(danger).toHaveAttribute('aria-busy','true');
 await danger.dispatchEvent('click');await danger.focus();await page.keyboard.press('Enter');await page.keyboard.press('Space');
 await expect(danger).toContainText('Eliminar · 1');await expect(danger).toBeFocused();
 await expect(danger.locator('.ds-icon')).toHaveCount(0);
 const link=preview.getByRole('link',{name:/Enlace de ejemplo/});
 await expect(link).not.toHaveAttribute('href');await link.dispatchEvent('click');await link.focus();await page.keyboard.press('Enter');await expect(page).toHaveURL(/#button$/);
 await preview.getByRole('button',{name:'Finalizar carga de ejemplo'}).click();await danger.click();await expect(danger).toHaveText('Eliminar · 2');await expect(link).toHaveAttribute('href','#componer');
});

test('matriz: tres tamaños, cinco tipos, Loader y foco en cuatro temas',async({page})=>{
 await page.emulateMedia({reducedMotion:'reduce'});
 await page.goto('/#button');await page.getByRole('tab',{name:'Variantes',exact:true}).click();
 for(const theme of ['contable','administrativo','servicios','personas']){
  await page.getByLabel('Tema del sistema de diseño').selectOption(theme);
  for(const [size,height,loaderSize] of [['large',48,24],['middle',40,20],['small',32,16]] as const){
   for(const variant of ['primary','default','text','link','danger']){
    const busy=page.locator(`[data-case="${variant}/${size}/loading"] .ds-button`);
    expect((await busy.boundingBox())?.height).toBe(height);
    expect((await busy.locator('.ds-loader').boundingBox())?.width).toBeCloseTo(loaderSize,1);
    await busy.focus();await page.keyboard.press('Tab');await page.keyboard.press('Shift+Tab');
    const ring=await busy.evaluate(e=>{const c=getComputedStyle(e,'::after');return{inset:c.top,width:c.borderTopWidth,radius:c.borderTopLeftRadius};});
    expect(ring).toEqual({inset:'-4px',width:'2px',radius:'12px'});
   }
   const danger=page.locator(`[data-case="danger/${size}/default"] .ds-button`);
   await page.mouse.move(0,0);expect(await danger.evaluate(e=>getComputedStyle(e).backgroundColor)).toBe('rgb(212, 0, 0)');
   await danger.hover();expect(await danger.evaluate(e=>getComputedStyle(e).backgroundColor)).toBe('rgb(157, 0, 0)');
   await page.mouse.down();expect(await danger.evaluate(e=>getComputedStyle(e).backgroundColor)).toBe('rgb(104, 0, 0)');await page.mouse.up();
   expect(await danger.evaluate(e=>getComputedStyle(e).fontWeight)).toBe('700');
  }
 }
 await page.screenshot({path:'test-results/button-evolution.png',fullPage:true});
});
