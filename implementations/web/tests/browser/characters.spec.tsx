import { test,expect } from '@playwright/test';
import { execFileSync } from 'node:child_process';
import { readFileSync,writeFileSync } from 'node:fs';
const evidence=process.env.DS_AUDIT_OUTPUT??'../../qa/implementations/web-contract-audit-2026-10-13';

type SourceNode={id:string;visible:boolean;absoluteTransform:number[][];fills?:{visible?:boolean}[];vectorPaths?:{data:string}[];children?:SourceNode[]};
const source=JSON.parse(readFileSync('../../sources/figma-snapshots/characters.ecosistema.2026-10-08.json','utf8'));
function expectedPaths(frame:SourceNode){
 const paths:number[][]=[];
 function visit(n:SourceNode){if(!n.visible)return;for(const paint of n.fills??[])if(paint.visible!==false)for(const path of n.vectorPaths??[]){const m=n.absoluteTransform;paths.push([m[0][0],m[1][0],m[0][1],m[1][1],m[0][2]-frame.absoluteTransform[0][2],m[1][2]-frame.absoluteTransform[1][2]]);}n.children?.forEach(visit);}
 visit(frame);return paths;
}
test('BENI en Chat y 13 frames coinciden con las coordenadas fuente en SVG',async({page})=>{
 await page.goto('/#chat-section');
 const hero=page.locator('.ds-chat-welcome .ds-chat-welcome-art');await expect(hero).toBeVisible();
 const readMatrices=(svg:SVGSVGElement)=>Array.from(svg.querySelectorAll('path')).map(path=>{const m=svg.getCTM()!.inverse().multiply(path.getCTM()!);return [m.a,m.b,m.c,m.d,m.e,m.f];});
 const check=(actual:number[][],expected:number[][])=>{expect(actual).toHaveLength(expected.length);actual.forEach((m,i)=>m.forEach((v,j)=>expect(Math.abs(v-expected[i][j])).toBeLessThanOrEqual(0.001)));};
 const welcome=JSON.parse(readFileSync('../../implementations/figma/chat-section.v0.1.0.build.js','utf8').match(/const HERO=(.*);/)![1]);
 const welcomePaths=welcome.vectors.flatMap((v:{x:number;y:number;paths:{data:string}[]})=>v.paths.map(p=>({matrix:[1,0,0,1,v.x,v.y],path:p.data})));
 check(await hero.evaluate(readMatrices),welcomePaths.map((p:{matrix:number[]})=>p.matrix));
 expect(await hero.locator('path').evaluateAll(ps=>ps.map(p=>p.getAttribute('d')))).toEqual(welcomePaths.map((p:{path:string})=>p.path));
 await hero.screenshot({path:evidence+'/beni.web.png'});
 await page.locator('.component-preview').screenshot({path:evidence+'/chat-section.web.png'});
 const markup=execFileSync(process.execPath,['--import','tsx','tests/render-characters.tsx'],{encoding:'utf8'});
 const preview=page.locator('.component-preview');await preview.evaluate((el,html)=>{el.innerHTML=html;Object.assign((el as HTMLElement).style,{width:'1340px',maxWidth:'none',padding:'16px',display:'block'});},markup);
 const frames=preview.locator('.ds-character');await expect(frames).toHaveCount(13);
 let paths=0;
 for(let i=0;i<13;i++){const expected=expectedPaths(source.frames[i]);check(await frames.nth(i).evaluate(readMatrices),expected);paths+=expected.length;}
 await preview.screenshot({path:evidence+'/characters.web.png'});
 writeFileSync('test-results/characters-geometry.json',JSON.stringify({status:'PASS',frames:13,paintedPaths:paths,chatHero:'PASS',tolerance:0.001,toleranceSource:'CHARACTERS-001 AC-02',scope:'SVG CTM matches source absolute matrices; visual review separate'},null,2));
});
