# Conversation · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `CONVERSATION-001` · API local 0.1.0 · categoría Composición.

## Uso sin backend

Message/Response/Composer/Preview y glifos originales de32px; no se escala la pose de Characters para sustituirlos. Slots y booleanas de visibilidad conservan contenido oculto. Draft admite composición; envío llama onSend. Identidad BENI/NAVI fija en los cuatro temas, sin respuesta IA fabricada. Aviso opcional: showAction=false; actionMessage y actionLabel editables; onAction callback local independiente de onSend. La muestra de créditos/fecha no define política de producto. Texto nuevo caption-regular/caption-semibold; Button default/small sin iconos. Draft y Tools conservan sus regiones. Slot nativo Notice content para todo el aviso: noticeContent undefined conserva muestra, null permite vacío y colecciones admiten composición/orden. En Figma el Slot vacío conserva una caja de edición de49px; ocultar Show action retira la región. Para chat embebido en un aplicativo aplicar APP-SHELL-EMBEDDED-CHAT-001: conservar Header y navegación global, cabecera de contexto dentro de Content y Chat Section a la izquierda con historial Chat Toolbar a la derecha. La columna max816 hereda Chat Layout0.1.1; no crear un chat flotante ni sustituir la navegación global.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

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
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [layout.tsx](../../src/components/layout.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface ConversationGlyphProps { agent?:'beni'|'navi'; label?:string }

export interface ConversationMessageProps { children:ReactNode }

export interface ConversationResponseProps { agent?:'beni'|'navi'; children?:ReactNode; badge?:ReactNode; previews?:ReactNode; secondaryContent?:ReactNode; additionalActions?:ReactNode; feedbackActions?:ReactNode; showPreviews?:boolean; showSecondaryContent?:boolean; showAdditionalActions?:boolean }

export interface ConversationComposerProps { value:string; onValueChange:(value:string)=>void; onSend:(value:string)=>void; placeholder?:string; label?:string; disclaimer?:ReactNode; tools?:ReactNode; modelSelector?:ReactNode; showModelSelector?:boolean; modelLabel?:string; draft?:ReactNode; showDisclaimer?:boolean; disabled?:boolean; showAction?:boolean; actionMessage?:ReactNode; actionLabel?:string; onAction?:()=>void; noticeContent?:ReactNode }

export interface ConversationPreviewProps { title:string; icon?:ReactNode; badge?:ReactNode; children?:ReactNode }

export interface ConversationProps { children:ReactNode; label?:string }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Conversation: {children,label='Conversación'}:ConversationProps
ConversationGlyph: {agent='beni',label}:ConversationGlyphProps
ConversationMessage: {children}:ConversationMessageProps
ConversationResponse: {agent='beni',children,badge=<Badge tone="light" showLeftIcon={false}>{agent==='beni'?'Fiscal y contable':'Super Agente'}</Badge>,previews,secondaryContent,additionalActions,feedbackActions=<><IconButton showCount={false} label="Me gusta" icon={<ThumbsUp weight="light"/>}/><IconButton showCount={false} label="No me gusta" icon={<ThumbsDown weight="light"/>}/><IconButton showCount={false} label="Copiar respuesta" icon={<TableGlyph type="copy"/>}/></>,showPreviews=false,showSecondaryContent=false,showAdditionalActions=false}:ConversationResponseProps
ConversationComposer: {value,onValueChange,onSend,placeholder='Escribe un mensaje',label='Mensaje',disclaimer='Te recomendamos revisar la información importante para asegurar un resultado óptimo',tools=<><IconButton label="Adjuntar" showCount={false} icon={<Paperclip weight="light"/>}/><IconButton label="Micrófono" showCount={false} icon={<Microphone weight="light"/>}/></>,modelSelector,showModelSelector=false,modelLabel='Navi Auto V1.0',draft,showDisclaimer=true,disabled=false,showAction=false,actionMessage=<><strong>Alcanzaste tu límite mensual de créditos. </strong>Se renuevan el 1 de noviembre.</>,actionLabel='Default',onAction,noticeContent}:ConversationComposerProps
ConversationPreview: {title,icon=<TableIcon size={24} weight="light"/>,badge=<Badge tone="light" showLeftIcon={false}>Tabla</Badge>,children}:ConversationPreviewProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. children; Response: body/previews/secondaryContent/additionalActions/feedbackActions; Composer: tools/modelSelector; Composer: draft/Notice content (noticeContent). ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [conversation.contract.v0.1.0.md](../../../../specs/conversation.contract.v0.1.0.md) · SHA-256 `ac9d904d56d94263f53225c4dfb4afb74c6e64d7af0f710b4ee6114584d41be6`.
- [conversation.character-identity.amendment.v0.1.1.md](../../../../specs/components/conversation.character-identity.amendment.v0.1.1.md) · SHA-256 `8112028e22246a5aec596d640d8fafba3e7748afe744d58e12b9bd79a948779f`.
- [conversation.typography.amendment.v0.1.0.md](../../../../specs/components/conversation.typography.amendment.v0.1.0.md) · SHA-256 `e4e72ab5c84cb6e2e7fb2f5209f5bb42c25c03ed325eaedb94b63f36d38fc5d0`.
- [conversation.composer-action.amendment.v0.1.2.md](../../../../specs/components/conversation.composer-action.amendment.v0.1.2.md) · SHA-256 `70b8a9efc172797049ceab6125d8fdfd257eff86eb4221afc2468e266338a3a5`.
- [conversation.composer-slot.amendment.v0.1.3.md](../../../../specs/components/conversation.composer-slot.amendment.v0.1.3.md) · SHA-256 `ee58562f873ddc27de09da898e19c3747bc2f6bea1e0909040cb84401474a4b3`.
- [app-shell.embedded-chat.amendment.v0.1.1.md](../../../../specs/components/app-shell.embedded-chat.amendment.v0.1.1.md) · SHA-256 `2850341f3b876228f9101faa14455ed25a4e1903dc38841fc8c54ba0497dbcd8`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/conversation-composer.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
