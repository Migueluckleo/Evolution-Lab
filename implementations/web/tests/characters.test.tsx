import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import characters from '../src/generated/characters.json';

type Matrix = number[][];
const identity: Matrix = [[1,0,0],[0,1,0]];
function compose(a:Matrix,b:Matrix):Matrix {
  return a.map((row,i)=>row.map((_,j)=>a[i][0]*b[0][j]+a[i][1]*b[1][j]+(j===2?a[i][2]:0)));
}
type SourceNode={id:string;absoluteTransform:Matrix;vectorPaths?:{data:string}[];children?:SourceNode[]};
type WebNode={id:string;transform?:Matrix;paths:{d:string}[];children:WebNode[]};

test('los 13 fotogramas conservan coordenadas absolutas de los 64 vectores fuente',()=>{
 const source=JSON.parse(readFileSync('../../sources/figma-snapshots/characters.ecosistema.2026-10-08.json','utf8'));
 const frames=[...characters.frames.beni,...characters.frames.navi] as WebNode[];
 assert.equal(frames.length,13);let vectors=0;
 source.frames.forEach((frame:SourceNode,i:number)=>{
   const inspect=(original:SourceNode,derived:WebNode,parent:Matrix)=>{
     assert.equal(derived.id,original.id);
     const actual=compose(parent,derived.transform??identity);
     // CHARACTERS-001 AC-02 autoriza 0.001px por serialización de Figma.
     for(let row=0;row<2;row++)for(let col=0;col<3;col++)assert.ok(Math.abs(actual[row][col]-original.absoluteTransform[row][col])<=0.001,`${original.id}: matrix[${row}][${col}]`);
     if(original.vectorPaths){vectors++;for(const path of derived.paths)assert.ok(original.vectorPaths.some(p=>p.data===path.d),`${original.id}: path sin modificaciones`);}
     assert.equal(derived.children.length,original.children?.length??0);
     original.children?.forEach((child,j)=>inspect(child,derived.children[j],actual));
   };
   inspect(frame,frames[i],frame.absoluteTransform);
 });
 assert.equal(vectors,64);
});
