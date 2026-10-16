import { test, expect, type Page } from '@playwright/test';
import { readFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import registry from '../../components.registry.json';

// Expected values come from the canonical source, never from generated CSS/metadata.
const source = 'specs/tokens/ai-design-system.typography.v0.1.1.json';
const sourceBytes = readFileSync('../../'+source);
const document = JSON.parse(sourceBytes.toString());
const styles = Object.fromEntries(document.styles.map((style:any) => [style.id, style]));
const themes = ['contable', 'administrativo', 'servicios', 'personas'];
const evidence = process.env.DS_TYPOGRAPHY_OUTPUT ?? 'test-results/typography';

async function metrics(page:Page, selector:string) {
  return page.locator(selector).evaluateAll(nodes => nodes.filter(element => {
    if (!element.getClientRects().length) return false;
    return Array.from(element.childNodes).some(node => node.nodeType === Node.TEXT_NODE && node.textContent?.trim()) || element.matches('input:not([type=hidden]),textarea');
  }).map(element => {
    const css = getComputedStyle(element);
    return { id:css.getPropertyValue('--ds-type-style-id').trim(), case:element.closest('.variant-case')?.getAttribute('data-case'), tag:element.tagName, classes:element.getAttribute('class'), text:(element.textContent??'').trim().slice(0,80), family:css.fontFamily, size:css.fontSize, weight:css.fontWeight, lineHeight:css.lineHeight, tracking:css.letterSpacing, decoration:css.textDecorationLine };
  }));
}
function discrepancies(rows:Awaited<ReturnType<typeof metrics>>) {
  return rows.flatMap<unknown>(row => {
    const style:any = styles[row.id];
    if (!style) return [{...row, error:'Missing canonical style identity'}];
    const expectedLine = style.lineHeight.unit === 'AUTO' ? 'normal' : style.lineHeight.unit === 'PERCENT' ? style.fontSize*style.lineHeight.value/100 : style.lineHeight.value;
    const expectedTracking = style.letterSpacing.unit === 'PERCENT' ? style.fontSize*style.letterSpacing.value/100 : style.letterSpacing.value;
    const near = (actual:string, value:number) => Math.abs(parseFloat(actual)-value)<0.001;
    const expectedDecoration=(style.textDecoration??'NONE').toLowerCase();
    const failed = !row.family.includes('Manrope Variable') || !near(row.size, style.fontSize) || Number(row.weight)!==style.fontWeight || (expectedLine==='normal' ? row.lineHeight!=='normal' : !near(row.lineHeight, expectedLine)) || !near(row.tracking==='normal'?'0':row.tracking,expectedTracking) || row.decoration!==expectedDecoration;
    return failed ? [{...row, expected:{fontSize:style.fontSize,fontWeight:style.fontWeight,lineHeight:expectedLine,letterSpacing:expectedTracking,textDecoration:expectedDecoration}}] : [];
  });
}
async function gallery(page:Page, slug:string) {
  await page.goto('/#'+slug);
  await page.getByRole('tab', {name:'Variantes',exact:true}).click();
  await page.locator('.variant-case').first().waitFor();
  await page.evaluate(() => window.document.fonts.ready);
}

test(`${document.styles.length} estilos: unidades, identidad y Manrope real en los cuatro temas`, async ({page}) => {
  await page.goto('/');
  await page.evaluate(ids => {
    const host=window.document.createElement('section');host.id='typography-probes';
    for(const id of ids){const node=window.document.createElement('div');node.className='ds-type-'+id;node.textContent='Manrope ágil 0123';host.append(node);}
    window.document.body.append(host);
  }, Object.keys(styles));
  await page.evaluate(() => window.document.fonts.ready);
  const faces=await page.evaluate(() => Array.from(window.document.fonts).map(face=>({family:face.family,status:face.status})));
  expect(faces.some(face=>face.family.includes('Manrope Variable')&&face.status==='loaded')).toBe(true);
  const cdp=await page.context().newCDPSession(page);await cdp.send('DOM.enable');await cdp.send('CSS.enable');
  const {root}=await cdp.send('DOM.getDocument');const {nodeId}=await cdp.send('DOM.querySelector',{nodeId:root.nodeId,selector:'#typography-probes>div'});
  const {fonts}=await cdp.send('CSS.getPlatformFontsForNode',{nodeId});
  expect(fonts.some(font=>font.familyName.includes('Manrope')&&font.isCustomFont&&font.glyphCount>0)).toBe(true);
  const results=[];
  for(const theme of themes){await page.getByLabel('Tema del sistema de diseño').selectOption(theme);await page.locator('#typography-probes').evaluate((node,value)=>node.setAttribute('data-ds-theme',value),theme);const rows=await metrics(page,'#typography-probes>div');expect(rows).toHaveLength(document.styles.length);expect(discrepancies(rows)).toEqual([]);results.push({theme,rows});}
  mkdirSync(evidence,{recursive:true});writeFileSync(`${evidence}/styles.json`,JSON.stringify({source,sha256:createHash('sha256').update(sourceBytes).digest('hex'),fonts,faces,status:'PASS',results},null,2));
});

test('consumidores de las 43 familias: receta completa heredada o explícita y desvíos corregidos', async ({page}) => {
  test.setTimeout(180000);
  const results=[];const failures:unknown[]=[];
  const expectedIds:Record<string,Record<string,string>> = {
    button:{'.ds-button-primary.ds-size-middle':'ui-action-label-medium','.ds-button-text.ds-size-small':'ui-action-text-small','.ds-button-link.ds-size-middle .ds-button-label':'ui-action-label-medium-underline','.ds-button-link.ds-size-small .ds-button-label':'ui-action-label-small-underline'},
    'file-upload':{'.ds-upload-action':'ui-upload-action-feedback-underline'},
    'empty-states':{'.ds-empty-support .ds-button-link .ds-button-label':'ui-action-label-normal-underline'},
    textarea:{'.ds-counter':'ui-caption-compact-emphasis'},
    breadcrumbs:{'.ds-breadcrumb-shortened':'ui-breadcrumb-shortened','[aria-current=page]':'ui-breadcrumb-label'},
    'navigation-pagination':{'.ds-pagination-pages>.contents>span[aria-hidden]':'body-semibold'},
    'navigation-tab':{'.ds-navigation-tab.is-active:not(.is-selected-presentation)':'ui-navigation-tab-active'},
    avatar:{'.ds-avatar-large .ds-avatar-face':'ui-navigation-emphasis-auto'},
    charts:{'.ds-gauge text':'ui-chart-gauge-value','.ds-chart-legend-small.ds-type-ui-caption-compact-emphasis':'ui-caption-compact-emphasis'},
    header:{'.ds-header-company strong':'ui-action-text-small','.ds-header-version small':'ui-header-release'},
    'chat-toolbar':{'.ds-chat-toolbar-body h3':'ui-body-compact','.ds-plan-count':'ui-chat-metadata'},
    conversation:{'.ds-preview-copy>strong':'ui-conversation-preview-title'},
  };
  for(const family of registry){await gallery(page,family.slug);
    for(const [selector,id] of Object.entries(expectedIds[family.slug]??{})){
      const selected=page.locator('.variant-gallery '+selector).first();await expect(selected).toHaveCount(1);
      expect(await selected.evaluate(el=>getComputedStyle(el).getPropertyValue('--ds-type-style-id').trim()),`${family.slug} ${selector}`).toBe(id);
    }
    for(const theme of themes){await page.getByLabel('Tema del sistema de diseño').selectOption(theme);const rows=await metrics(page,'.variant-content [class*="ds-"], .variant-content [class*="ds-"] *');const differences=discrepancies(rows);results.push({family:family.slug,theme,count:rows.length,styleIds:[...new Set(rows.map(row=>row.id))],measurements:rows});if(differences.length)failures.push({family:family.slug,theme,differences});}
    const captureSelector=({'button':'.ds-button-link','file-upload':'.ds-upload-action','empty-states':'.ds-empty-support .ds-button-link'} as Record<string,string>)[family.slug];
    if(captureSelector){mkdirSync(evidence,{recursive:true});await page.locator('.variant-case').filter({has:page.locator(captureSelector)}).first().screenshot({path:`${evidence}/${family.slug}.underline.png`});}
  }
  mkdirSync(evidence,{recursive:true});writeFileSync(`${evidence}/consumers.json`,JSON.stringify({source,sha256:createHash('sha256').update(sourceBytes).digest('hex'),status:failures.length?'FAIL':'PASS',results,failures},null,2));
  expect(failures).toEqual([]);
});
