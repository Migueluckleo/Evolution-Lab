'use client';
import {useState} from 'react';
import {Button} from '@contpaqi/ui';
import {DSNode} from './evidence';
// Replace the demonstration and fill brief.json before capturing or handing off.
export default function Page(){
 const [count,setCount]=useState(0);
 const props={variant:'primary' as const,showLeftIcon:false,showRightIcon:false};
 return <main data-ds-theme="contable" className="min-h-screen p-8 flex flex-col gap-6 items-start">
  <h1>Prototipo CONTPAQi</h1>
  <DSNode id="demo-button" component="BUTTON-001" props={props}><Button {...props} onClick={()=>setCount(count+1)}>Probar interacción</Button></DSNode>
  <p aria-live="polite">Interacciones: {count}</p>
 </main>;
}
