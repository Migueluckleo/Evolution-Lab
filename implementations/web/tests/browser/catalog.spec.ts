import { test,expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import registry from '../../components.registry.json';
import { writeFileSync } from 'node:fs';
const evidence=process.env.DS_AUDIT_OUTPUT??'../../qa/implementations/web-contract-audit-2026-10-13';

test('todos los ejemplos se renderizan sin errores ni assets rotos',async({page})=>{
 const errors:string[]=[];page.on('pageerror',e=>errors.push(e.message));await page.goto('/');
 for(const row of registry){await page.locator('.catalog-nav-list').getByRole('link',{name:row.name,exact:true}).click();await expect(page.getByRole('heading',{name:row.name,exact:true,level:1})).toBeVisible();await expect(page.locator('.component-preview')).toBeVisible();const broken=await page.locator('.component-preview img').evaluateAll(imgs=>imgs.filter(i=>!(i as HTMLImageElement).complete||(i as HTMLImageElement).naturalWidth===0).length);expect(broken,row.slug).toBe(0);}
 expect(errors).toEqual([]);
});
test('controles locales y teclado funcionan',async({page})=>{
 await page.goto('/#checkbox');await page.getByLabel('Incluir datos de muestra').check();await expect(page.getByLabel('Incluir datos de muestra')).toBeChecked();
 await page.goto('/#toggle');await page.getByRole('switch').check();await expect(page.getByRole('switch')).toBeChecked();
 await page.goto('/#select');const combo=page.getByRole('combobox',{name:'Tipo de documento'});await combo.focus();await page.keyboard.press('ArrowDown');await page.keyboard.press('ArrowDown');await page.keyboard.press('Enter');await expect(combo).toContainText('Reporte');
 await page.goto('/#navigation-switch-tab');await page.getByRole('tab',{name:'Lista',exact:true}).focus();await page.keyboard.press('ArrowRight');await expect(page.getByRole('tab',{name:'Resumen',exact:true})).toHaveAttribute('aria-selected','true');
 await page.goto('/#modal');const trigger=page.getByRole('button',{name:'Abrir diálogo'});await trigger.click();await expect(page.getByRole('dialog')).toBeVisible();await page.keyboard.press('Escape');await expect(page.getByRole('dialog')).not.toBeVisible();await expect(trigger).toBeFocused();
 await page.goto('/#file-upload');await page.getByLabel('Seleccionar archivo').setInputFiles({name:'muestra.txt',mimeType:'text/plain',buffer:Buffer.from('Solo local')});await expect(page.getByRole('status')).toContainText('Seleccionados localmente: muestra.txt');
 await page.goto('/#conversation');await page.getByRole('textbox',{name:'Mensaje',exact:true}).fill('Mi mensaje local');await page.getByRole('button',{name:'Enviar mensaje'}).click();await expect(page.locator('.ds-conversation-message')).toContainText('Mi mensaje local');
});
test('los cuatro temas cambian marca y preservan personajes',async({page})=>{
 await page.goto('/#button');const colors=[];for(const theme of ['contable','administrativo','servicios','personas']){await page.getByLabel('Tema del sistema de diseño').selectOption(theme);colors.push(await page.locator('.component-preview .ds-button-primary').first().evaluate(e=>getComputedStyle(e).backgroundColor));}expect(new Set(colors).size).toBe(4);
 await page.goto('/#characters');const identity=[];for(const theme of ['contable','administrativo','servicios','personas']){await page.getByLabel('Tema del sistema de diseño').selectOption(theme);identity.push(await page.locator('.ds-character path').first().evaluate(e=>getComputedStyle(e).fill));}expect(new Set(identity).size).toBe(1);
});
test('pantalla compuesta agrega, filtra y conserva solo datos locales',async({page})=>{
 await page.goto('/#componer');await page.getByRole('button',{name:'Nuevo documento',exact:true}).click();await page.getByRole('textbox',{name:'Nombre',exact:true}).fill('Reporte agregado');await page.getByRole('button',{name:'Agregar a la muestra'}).click();await expect(page.getByRole('cell',{name:'Reporte agregado',exact:true})).toBeVisible();await page.getByRole('searchbox').fill('agregado');await expect(page.locator('.ds-table tbody tr')).toHaveCount(1);await page.reload();await expect(page.locator('.ds-table tbody tr')).toHaveCount(3);
 await page.screenshot({path:evidence+'/composition.web.png',fullPage:true});
});
test('semántica accesible básica y catálogo en ancho reducido',async({page})=>{
 await page.goto('/#input-field');const result=await new AxeBuilder({page}).disableRules(['color-contrast']).analyze();writeFileSync('test-results/accessibility.json',JSON.stringify(result,null,2));expect(result.violations).toEqual([]);
 await page.goto('/#button');await page.screenshot({path:evidence+'/catalog.web.png',fullPage:true});await page.setViewportSize({width:390,height:844});await expect(page.getByRole('heading',{name:'Button',exact:true,level:1})).toBeVisible();expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);await page.getByRole('button',{name:'Mostrar componentes'}).click();await expect(page.locator('.catalog-nav')).toBeVisible();
});

test('alturas de controles respetan los tres tamaños',async({page})=>{
 await page.goto('/#button');for(const [size,height] of [['small',32],['middle',40],['large',48]] as const){expect((await page.locator('.component-preview .ds-button.ds-size-'+size).first().boundingBox())?.height).toBe(height);}
});
