'use client';
import {useEffect,useState} from 'react';
import {Button,Modal,Avatar,Logos,InputField} from '@contpaqi/ui';
import {DSNode} from './evidence';
export default function Page(){
 const [open,setOpen]=useState(false);const [variant,setVariant]=useState<'media'|'side-by-side'>('media');const [value,setValue]=useState('');
 useEffect(()=>{const handler=(event:KeyboardEvent)=>{if(open&&event.key==='m')setVariant('side-by-side');};window.addEventListener('keydown',handler);return()=>window.removeEventListener('keydown',handler);},[open]);
 const bp={"showLeftIcon":false,"showRightIcon":false};const mp={open:true,variant,title:'Detalle portable'};const ip={label:'Buscar',value,showTrailingIcon:false};
 return <main data-ds-theme="contable" className="min-h-screen p-8">
 <DSNode id="composition" component="LOCAL-demo" props={{}}><section className="flex flex-col gap-6 items-start">
 <DSNode id="heading" component="LOCAL-heading" props={{}}><h1 className="ds-type-heading-5-bold">Prueba portable CONTPAQi</h1></DSNode>
 <DSNode id="search" component="INPUT-FIELD-001" props={ip}><InputField {...ip} id="search-input" onChange={event=>setValue(event.target.value)}/></DSNode>
 <DSNode id="open" component="BUTTON-001" props={bp}><Button {...bp} id="open-modal" onClick={()=>setOpen(true)}>Abrir detalle</Button></DSNode>
 <DSNode id="feedback" component="LOCAL-feedback" props={{}}><p id="value" className="ds-type-body-regular">Consulta: {value||'vacía'}</p></DSNode>
 {open&&variant==='media'&&<DSNode id="media-modal" component="MODAL-001" props={mp}><Modal {...mp} onOpenChange={setOpen}>Presiona M para ver el detalle con contenido variable.</Modal></DSNode>}
 {open&&variant==='side-by-side'&&<DSNode id="side-modal" component="MODAL-001" props={mp}><Modal {...mp} onOpenChange={setOpen}>
  <div className="flex flex-col gap-4 items-start">
   <DSNode id="avatar" component="AVATAR-001" props={{label:'Persona ficticia'}}><Avatar label="Persona ficticia"/></DSNode>
   <DSNode id="logo" component="LOGOS-001" props={{alt:'CONTPAQi'}}><Logos alt="CONTPAQi"/></DSNode>
   <DSNode id="switch" component="BUTTON-001" props={bp}><Button {...bp} id="switch-media" onClick={()=>setVariant('media')}>Volver al medio</Button></DSNode>
  </div>
 </Modal></DSNode>}
 </section></DSNode></main>;
}
