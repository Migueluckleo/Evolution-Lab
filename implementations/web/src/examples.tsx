'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from './index';

// example: button
export function ButtonExample(){const [count,setCount]=useState(0);return <div className="flex flex-wrap items-center gap-4"><DS.Button showLeftIcon showRightIcon={false} onClick={()=>setCount(count+1)} leftIcon={<Plus/>}>Agregar · {count}</DS.Button><DS.Button showLeftIcon={false} showRightIcon={false} variant="default" size="middle">Secundario</DS.Button><DS.Button showLeftIcon={false} showRightIcon={false} variant="text" size="small">Texto</DS.Button><DS.Button showLeftIcon={false} showRightIcon={false} variant="link" href="#componer">Ver pantalla</DS.Button><DS.Button showLeftIcon={false} showRightIcon={false} disabled>Deshabilitado</DS.Button></div>;}
// example: icon-button
export function IconButtonExample(){const [count,setCount]=useState(1);return <DS.IconButton showCount label="Ver notificaciones de ejemplo" icon={<Bell/>} variant="outline" count={String(count)} onClick={()=>setCount(count+1)}/>;}
// example: filter-chip
export function FilterChipExample(){const [selected,setSelected]=useState(false);return <DS.FilterChip showLeftIcon selected={selected} onSelectedChange={setSelected} leftIcon={<Check/>}>Facturas</DS.FilterChip>;}
// example: badge
export function BadgeExample(){return <div className="flex gap-3 flex-wrap">{(['base','light','informational','warning','error','success'] as const).map(tone=><DS.Badge key={tone} tone={tone} leftIcon={<Info/>}>{tone}</DS.Badge>)}</div>;}
// example: dot
export function DotExample(){return <div className="flex items-center gap-5">{(['active','busy','inactive','count','overflow'] as const).map(type=><DS.Dot key={type} type={type} size="large" label={type}/>)}</div>;}
// example: inline-notification
export function InlineNotificationExample(){const [visible,setVisible]=useState(true);return visible?<DS.InlineNotification tone="info" title="Datos de demostración" onDismiss={()=>setVisible(false)}>Esta pantalla utiliza datos locales editables.</DS.InlineNotification>:<DS.Button showLeftIcon={false} showRightIcon={false} variant="text" onClick={()=>setVisible(true)}>Mostrar aviso</DS.Button>;}
// example: linear-progress-bar
export function LinearProgressBarExample(){const [progress,setProgress]=useState<25|50|75|100>(25);return <div className="grid gap-4"><DS.LinearProgressBar label="Avance de muestra" progress={progress} size="medium" helper="Valor elegido localmente"/><DS.Button showLeftIcon={false} showRightIcon={false} variant="text" size="small" onClick={()=>setProgress(progress===100?25:(progress+25) as 50|75|100)}>Cambiar avance</DS.Button></div>;}
// example: loader
export function LoaderExample(){return <div className="flex items-center gap-6"><DS.Loader/><DS.Loader size="md" color="secondary"/><DS.Loader size="lg" color="default"/></div>;}
// example: tooltip
export function TooltipExample(){return <DS.Tooltip content="Información complementaria" align="down"><span className="inline-flex items-center gap-2"><Info size={20}/>Detalle</span></DS.Tooltip>;}
// example: input-field
export function InputFieldExample(){const [value,setValue]=useState('');return <DS.InputField label="Nombre de la pantalla" placeholder="Escribe un nombre" value={value} onChange={e=>setValue(e.target.value)} helper="Texto editable, sin validación de negocio" required/>;}
// example: textarea
export function TextareaExample(){const [value,setValue]=useState('');return <DS.Textarea label="Descripción" value={value} onChange={e=>setValue(e.target.value)} placeholder="Describe el contenido" counter={`${value.length} caracteres`} helper="El contador se calcula en este ejemplo."/>;}
// example: checkbox
export function CheckboxExample(){const [checked,setChecked]=useState(false);return <DS.Checkbox showRightLabel label="Incluir datos de muestra" checked={checked} onChange={e=>setChecked(e.target.checked)}/>;}
// example: radio-button
export function RadioButtonExample(){const [value,setValue]=useState('a');return <fieldset className="grid gap-3"><legend className="mb-3 font-semibold">Vista inicial</legend>{['a','b'].map(v=><DS.RadioButton showRightLabel key={v} name="radio-demo" value={v} label={`Vista ${v.toUpperCase()}`} checked={value===v} onChange={()=>setValue(v)}/>)}</fieldset>;}
// example: toggle
export function ToggleExample(){const [checked,setChecked]=useState(false);return <DS.Toggle showRightLabel label="Mostrar detalles" checked={checked} onChange={e=>setChecked(e.target.checked)}/>;}
// example: search
export function SearchExample(){const [value,setValue]=useState('');return <div className="grid w-full gap-4"><DS.Search value={value} onValueChange={setValue}/><p>{['Facturas','Clientes','Reportes'].filter(x=>x.toLowerCase().includes(value.toLowerCase())).join(' · ')||'Sin coincidencias en la muestra'}</p></div>;}
// example: dropdown-item
export function DropdownItemExample(){const [selected,setSelected]=useState(false);return <div className="w-72"><DS.DropdownItem selected={selected} leadingIcon={<FileText/>} onClick={()=>setSelected(!selected)}>Documento de muestra</DS.DropdownItem><DS.DropdownItem size="middle" disabled>No disponible</DS.DropdownItem></div>;}
// example: select
export function SelectExample(){const [value,setValue]=useState('');return <DS.Select label="Tipo de documento" value={value} onValueChange={setValue} helper="Opciones locales" options={[{value:'factura',label:'Factura'},{value:'reporte',label:'Reporte'},{value:'archivo',label:'Archivo',disabled:true}]}/>;}
// example: file-upload
export function FileUploadExample(){const [files,setFiles]=useState<string[]>([]);return <div className="grid gap-3"><DS.FileUpload onFilesChange={items=>setFiles(items.map(f=>f.name))} formats="Selecciona archivos de tu equipo. No se enviarán." multiple/><p role="status">{files.length?`Seleccionados localmente: ${files.join(', ')}`:'Ningún archivo seleccionado'}</p></div>;}
// example: breadcrumbs
export function BreadcrumbsExample(){return <DS.Breadcrumbs items={[{id:'inicio',label:'Inicio',href:'#componer'},{id:'documentos',label:'Documentos',href:'#table'},{id:'detalle',label:'Detalle'}]}/>;}
// example: navigation-pagination
export function NavigationPaginationExample(){const [page,setPage]=useState(1);const [size,setSize]=useState(20);return <DS.NavigationPagination page={page} pages={8} onPageChange={setPage} pageSize={size} onPageSizeChange={setSize} showFirstLast/>;}
// example: navigation-switch-tab
export function NavigationSwitchTabExample(){const [value,setValue]=useState('lista');return <DS.NavigationSwitchTab label="Presentación de documentos" value={value} onValueChange={setValue} items={[{id:'lista',label:'Lista',content:<p className="py-4">Contenido de la lista</p>},{id:'resumen',label:'Resumen',content:<p className="py-4">Contenido del resumen</p>}]}/>;}
// example: navigation-switch-tab-item
export function NavigationSwitchTabItemExample(){const [active,setActive]=useState(true);return <DS.NavigationSwitchTabItem active={active} count="3" leftIcon={<FileText/>} aria-pressed={active} onClick={()=>setActive(!active)}>Documentos</DS.NavigationSwitchTabItem>;}
// example: navigation-tab
export function NavigationTabExample(){const [active,setActive]=useState(true);return <div className="flex gap-4"><DS.NavigationTab active={active} aria-pressed={active} onClick={()=>setActive(!active)} leftIcon={<FileText/>}>Resumen</DS.NavigationTab><DS.NavigationTab variant="dynamic" active={!active} aria-pressed={!active} onClick={()=>setActive(!active)}>Detalle</DS.NavigationTab></div>;}
// example: steps
export function StepsExample(){const [current,setCurrent]=useState(1);return <DS.Steps total={3} current={current} onStepChange={setCurrent}/>;}
// example: stepper
export function StepperExample(){return <div className="flex"><DS.Stepper position="start" state="checked" step="PASO 1" title="Datos" caption="Captura"/><DS.Stepper position="middle" state="default" step="PASO 2" title="Revisión" caption="Detalles"/><DS.Stepper position="end" state="inactive" step="PASO 3" title="Final" caption="Resultado"/></div>;}
// example: avatar
export function AvatarExample(){return <div className="flex gap-4 items-center"><DS.Avatar label="Persona de muestra"/><DS.Avatar type="text" initials="ML" label="Miguel Leo" showStatus statusLabel="Activo, dato de muestra"/><DS.Avatar type="icon" size="large" label="Usuario"/></div>;}
// example: characters
export function CharactersExample(){const [frame,setFrame]=useState<1|2|3|4|5|6>(1);return <div className="grid gap-4"><div className="flex gap-8"><DS.Characters character="beni" frame={frame} label="BENI"/><DS.Characters character="navi" frame={frame} label="NAVI"/></div><DS.Button showLeftIcon={false} showRightIcon={false} variant="text" size="small" onClick={()=>setFrame(frame===6?1:(frame+1) as 2|3|4|5|6)}>Siguiente fotograma</DS.Button></div>;}
// example: logos
export function LogosExample(){const [id,setId]=useState('435:2654');return <div className="grid gap-6"><label>Asset local<select className="block mt-2 border border-ds-border rounded-ds p-2 max-w-full" value={id} onChange={e=>setId(e.target.value)}>{DS.logoAssets.map(a=><option key={a.id} value={a.id}>{a.family} · {a.name}</option>)}</select></label><DS.Logos assetId={id} alt="Logotipo original CONTPAQi" height={64}/></div>;}
// example: empty-states
export function EmptyStatesExample(){return <DS.EmptyStates presentation="compact" title="Aún no hay documentos" mainActions={<DS.Button showLeftIcon={false} showRightIcon={false} size="middle" onClick={()=>alert('Acción local de ejemplo')}>Agregar documento</DS.Button>}>Agrega un documento de muestra para explorar esta pantalla.</DS.EmptyStates>;}
// example: metric-card
export function MetricCardExample(){return <DS.MetricCard title="Documentos" description="Datos de demostración" values={[{label:'Este mes',value:'128'},{label:'Mes anterior',value:'112'}]} icon={<FileText/>}/>;}
// example: table
export function TableExample(){const rows=[{id:'doc-1',name:'Documento A',status:'Revisado'},{id:'doc-2',name:'Documento B',status:'Pendiente'}];return <DS.Table caption="Documentos de ejemplo" rows={rows} rowKey={r=>r.id} columns={[{id:'name',header:'Documento',cell:r=>r.name},{id:'status',header:'Estado',cell:r=><DS.Badge tone={r.status==='Revisado'?'success':'warning'}>{r.status}</DS.Badge>}]}/>;}
// example: modal
export function ModalExample(){const [open,setOpen]=useState(false);return <><DS.Button showLeftIcon={false} showRightIcon={false} onClick={()=>setOpen(true)}>Abrir diálogo</DS.Button><DS.Modal open={open} onOpenChange={setOpen} title="Editar muestra" actions={<><DS.Button showLeftIcon={false} showRightIcon={false} variant="default" size="middle" onClick={()=>setOpen(false)}>Cancelar</DS.Button><DS.Button showLeftIcon={false} showRightIcon={false} size="middle" onClick={()=>setOpen(false)}>Listo</DS.Button></>}><DS.InputField label="Nombre" defaultValue="Documento de ejemplo"/></DS.Modal></>;}
// example: scrollbar
export function ScrollbarExample(){return <div className="flex gap-8"><DS.Scrollbar thumbSize="25%"/><DS.ScrollArea label="Lista larga de muestra" height={200} className="w-72"><ul className="grid gap-4 pr-4">{Array.from({length:20},(_,i)=><li key={i}>Elemento {i+1}</li>)}</ul></DS.ScrollArea></div>;}
// example: fuentes
export function FuentesExample(){return <DS.Fuentes reference="2" type="Manual de referencia" source="CONTPAQi®" location="Mi cuenta" path={<><DS.FuentesPathItem>Inicio</DS.FuentesPathItem><DS.FuentesPathItem separator>Documentación</DS.FuentesPathItem></>}/>;}
// example: charts
export function ChartsExample(){return <DS.Charts title="Resumen de muestra" description="Composición visual con valores de ejemplo" legend={<><DS.ChartLegendLabel swatch="series-1">Serie 1</DS.ChartLegendLabel><DS.ChartLegendLabel swatch="series-2">Serie 2</DS.ChartLegendLabel></>}><DS.SemiDonutGauge progress={75}/><DS.ProgressChartItem label="Ejemplo estático" value="$100k"/></DS.Charts>;}
// example: header
export function HeaderExample(){return <DS.Header logo={<DS.Logos alt="CONTPAQi Contable"/>} version="2.0.0" releaseLabel="ALPHA .1" actions={<DS.IconButton showCount={false} label="Notificaciones" icon={<Bell/>}/>} company="Empresa de ejemplo" taxId="RFC de muestra" user={<DS.Avatar type="text" initials="ML" label="Usuario de muestra"/>}/>;}
// example: sidebar
export function SidebarExample(){const [expanded,setExpanded]=useState(true);const [active,setActive]=useState('home');return <div className="grid gap-6"><label className="flex items-center gap-2"><input type="checkbox" checked={expanded} onChange={e=>setExpanded(e.target.checked)}/>Expanded</label><DS.Sidebar expanded={expanded} onExpandedChange={setExpanded} items={[{id:'home',label:'Home',active:active==='home',onClick:()=>setActive('home')},{id:'sub1',label:'Submenu 1',submenu:true,active:active==='sub1',onClick:()=>setActive('sub1')},{id:'sub2',label:'Submenu 2',submenu:true,active:active==='sub2',onClick:()=>setActive('sub2')},...Array.from({length:5},(_,i)=>({id:`menu-${i}`,label:`Menu item ${i+1}`,active:active===`menu-${i}`,onClick:()=>setActive(`menu-${i}`)}))]} lowerOptions={<><hr/><DS.MenuItem type={expanded?'expanded':'collapsed'} isActive={false} label="Help" lightIcon={<Question weight="light"/>} fillIcon={<Question weight="fill"/>} showRightIcon={false}/></>}/></div>;}
// example: app-shell
export function AppShellExample(){return <DS.AppShell header={<DS.Header logo={<DS.Logos alt="CONTPAQi Contable"/>}/>} sidebar={<DS.Sidebar items={[{id:'home',label:'Inicio',icon:<House/>,href:'#componer',active:true}]}/>}><div className="p-8"><h2 className={`${DS.typographyClass('heading-5-semibold')} mb-6`}>Pantalla de ejemplo</h2><DS.MetricCard title="Documentos" values={[{label:'Total',value:'128'}]}/></div></DS.AppShell>;}
// example: chat-history-item
export function ChatHistoryItemExample(){const [selected,setSelected]=useState(false);return <div className="w-80"><DS.ChatHistoryItem selected={selected} updated="1 sem" onSelect={()=>setSelected(!selected)} actions={<DS.IconButton showCount={false} size="small" label="Acción de ejemplo" icon={<Info/>}/>}>Consulta de documentos</DS.ChatHistoryItem></div>;}
// example: chat-tool-item
export function ChatToolItemExample(){const [count,setCount]=useState(0);return <div className="w-72"><DS.ChatToolItem label={`Nuevo chat · ${count}`} onClick={()=>setCount(count+1)}/><DS.ChatToolItem label="Herramienta no disponible" disabled/></div>;}
// example: chat-toolbar
export function ChatToolbarExample(){const [expanded,setExpanded]=useState(true);return <DS.ChatToolbar expanded={expanded} onExpandedChange={setExpanded} header={<strong>Anticipa · demo</strong>} tools={<DS.ChatToolItem label="Nuevo chat"/>} chats={<DS.ChatHistoryItem updated="1 sem">Consulta de ejemplo</DS.ChatHistoryItem>} plan={<p>Plan de demostración</p>}/>;}
// example: conversation
export function ConversationExample(){
 const [value,setValue]=useState('');const [messages,setMessages]=useState<string[]>([]);
 const [showAction,setShowAction]=useState(false);const [actionResult,setActionResult]=useState('');
 const [noticeMode,setNoticeMode]=useState('default');
 const notices=noticeMode==='reordered'?['Tercero','Primero','Segundo']:noticeMode==='replacement'?['Sustituto']:['Primero','Segundo','Tercero'];
 const noticeContent=noticeMode==='default'?undefined:noticeMode==='empty'?null:notices.map(name=><DS.InlineNotification key={name} title={name} showDismiss={false} showIcon={false}><span>Contenido local del aviso. </span><DS.Button variant="text" size="small" showLeftIcon={false} showRightIcon={false} onClick={()=>setActionResult(`Acción local: ${name}`)}>Acción {name}</DS.Button></DS.InlineNotification>);
 return <div className="grid gap-6 w-full">
  <DS.Toggle label="Mostrar aviso de ejemplo" checked={showAction} onChange={e=>setShowAction(e.target.checked)}/>
  <label>Contenido del aviso <select value={noticeMode} onChange={e=>setNoticeMode(e.target.value)}><option value="default">Aviso inicial</option><option value="empty">Vacío</option><option value="multiple">Tres bloques</option><option value="reordered">Reordenados</option><option value="replacement">Sustituido</option></select></label>
  <DS.Conversation><DS.ConversationResponse agent="beni" badge={<DS.Badge>Ejemplo</DS.Badge>}>Esta respuesta es contenido local de muestra.</DS.ConversationResponse>{messages.map((m,i)=><DS.ConversationMessage key={i}>{m}</DS.ConversationMessage>)}</DS.Conversation>
  <DS.ConversationComposer value={value} onValueChange={setValue} onSend={text=>{setMessages([...messages,text]);setValue('');}} disclaimer="Demostración local, sin servicio de IA." showAction={showAction} noticeContent={noticeContent} actionLabel="Ver detalle" onAction={()=>setActionResult('Acción local de ejemplo. No se consultaron créditos ni se realizó una compra.')}/>
  <p role="status">{actionResult}</p>
 </div>;
}
// example: chat-section
export function ChatSectionExample(){const [value,setValue]=useState('');const [messages,setMessages]=useState<string[]>([]);return <DS.ChatSection state={messages.length?'active':'standby'} userName="Miguel" subtitle="Explora una conversación local" messages={messages.map((m,i)=><DS.ConversationMessage key={i}>{m}</DS.ConversationMessage>)} suggestions={<DS.ChatSuggestion onClick={()=>setValue('Ver documentos')}>Ver documentos</DS.ChatSuggestion>} composer={<DS.ConversationComposer value={value} onValueChange={setValue} onSend={text=>{setMessages([...messages,text]);setValue('');}} showDisclaimer={messages.length>0} disclaimer="Solo datos locales de ejemplo."/>}/>;}
