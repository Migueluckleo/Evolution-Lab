# ChatToolbar · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `CHAT-TOOLBAR-001` · API local 0.1.0 · categoría Composición.

## Uso sin backend

Altura791 y ancho79/264 según contrato y enmienda0.1.1. Contenido conservado al contraer. Show indicators=false y Show plan=true. Se conserva la ausencia de overflow de la fuente; listas que excedan el alto son la limitación documental conocida.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function ChatToolbarExample(){const [expanded,setExpanded]=useState(true);return <DS.ChatToolbar expanded={expanded} onExpandedChange={setExpanded} header={<strong>Anticipa · demo</strong>} tools={<DS.ChatToolItem label="Nuevo chat"/>} chats={<DS.ChatHistoryItem updated="1 sem">Consulta de ejemplo</DS.ChatHistoryItem>} plan={<p>Plan de demostración</p>}/>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [layout.tsx](../../src/components/layout.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface ChatToolbarProps { expanded:boolean; onExpandedChange:(expanded:boolean)=>void; header?:ReactNode; tools?:ReactNode; indicators?:ReactNode; chats?:ReactNode; plan?:ReactNode; planName?:string; indicatorsTitle?:string; chatsTitle?:string; showIndicators?:boolean; showPlan?:boolean }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
ChatToolbar: {expanded,onExpandedChange,header=<Logos assetId="434:3979" alt="Anticipa" height={24}/>,tools,indicators,chats,plan,planName='Pro Plan',indicatorsTitle='Indicadores',chatsTitle='Chats',showIndicators=false,showPlan=true}:ChatToolbarProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. header/tools/indicators/chats/plan. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [chat-toolbar.contract.v0.1.0.md](../../../../specs/chat-toolbar.contract.v0.1.0.md) · SHA-256 `2b96dccbb48044dae0157cf09c068b368cac7d8dbdecd4a13e7ef7caf6d8fb43`.
- [chat.layout.amendment.v0.1.1.md](../../../../specs/components/chat.layout.amendment.v0.1.1.md) · SHA-256 `f381c86b294d48087bc8c8eea2f216f4dcba9b6a900affe783601ef94f3e7b9c`.
- [chat-toolbar.typography.amendment.v0.1.0.md](../../../../specs/components/chat-toolbar.typography.amendment.v0.1.0.md) · SHA-256 `762ae9b620eff3b8c95c54582c165a0a13a64d7ff79785fb2720df40ff438cf4`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
