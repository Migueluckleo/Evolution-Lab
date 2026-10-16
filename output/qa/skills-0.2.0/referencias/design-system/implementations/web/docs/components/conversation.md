# Conversation · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `CONVERSATION-001` · API local 0.1.0 · categoría Composición.

## Uso sin backend

Message/Response/Composer/Preview y glifos originales de32px; no se escala la pose de Characters para sustituirlos. Slots y booleanas de visibilidad conservan contenido oculto. Draft admite composición; envío llama onSend. Identidad BENI/NAVI fija en los cuatro temas, sin respuesta IA fabricada.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function ConversationExample(){const [value,setValue]=useState('');const [messages,setMessages]=useState<string[]>([]);return <div className="grid gap-6 w-full"><DS.Conversation><DS.ConversationResponse agent="beni" badge={<DS.Badge>Ejemplo</DS.Badge>}>Esta respuesta es contenido local de muestra.</DS.ConversationResponse>{messages.map((m,i)=><DS.ConversationMessage key={i}>{m}</DS.ConversationMessage>)}</DS.Conversation><DS.ConversationComposer value={value} onValueChange={setValue} onSend={text=>{setMessages([...messages,text]);setValue('');}} disclaimer="Demostración local, sin servicio de IA."/></div>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [layout.tsx](../../src/components/layout.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface ConversationGlyphProps { agent?:'beni'|'navi'; label?:string }

export interface ConversationMessageProps { children:ReactNode }

export interface ConversationResponseProps { agent?:'beni'|'navi'; children?:ReactNode; badge?:ReactNode; previews?:ReactNode; secondaryContent?:ReactNode; additionalActions?:ReactNode; feedbackActions?:ReactNode; showPreviews?:boolean; showSecondaryContent?:boolean; showAdditionalActions?:boolean }

export interface ConversationComposerProps { value:string; onValueChange:(value:string)=>void; onSend:(value:string)=>void; placeholder?:string; label?:string; disclaimer?:ReactNode; tools?:ReactNode; modelSelector?:ReactNode; showModelSelector?:boolean; modelLabel?:string; draft?:ReactNode; showDisclaimer?:boolean; disabled?:boolean }

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
ConversationComposer: {value,onValueChange,onSend,placeholder='Escribe un mensaje',label='Mensaje',disclaimer='Te recomendamos revisar la información importante para asegurar un resultado óptimo',tools=<><IconButton label="Adjuntar" showCount={false} icon={<Paperclip weight="light"/>}/><IconButton label="Micrófono" showCount={false} icon={<Microphone weight="light"/>}/></>,modelSelector,showModelSelector=false,modelLabel='Navi Auto V1.0',draft,showDisclaimer=true,disabled=false}:ConversationComposerProps
ConversationPreview: {title,icon=<TableIcon size={24} weight="light"/>,badge=<Badge tone="light" showLeftIcon={false}>Tabla</Badge>,children}:ConversationPreviewProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. children; Response: body/previews/secondaryContent/additionalActions/feedbackActions; Composer: tools/modelSelector. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [conversation.contract.v0.1.0.md](../../../../specs/conversation.contract.v0.1.0.md) · SHA-256 `ac9d904d56d94263f53225c4dfb4afb74c6e64d7af0f710b4ee6114584d41be6`.
- [conversation.character-identity.amendment.v0.1.1.md](../../../../specs/components/conversation.character-identity.amendment.v0.1.1.md) · SHA-256 `8112028e22246a5aec596d640d8fafba3e7748afe744d58e12b9bd79a948779f`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
