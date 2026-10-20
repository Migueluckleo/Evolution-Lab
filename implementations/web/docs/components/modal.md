# Modal · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `MODAL-001` · API local 0.1.0 · categoría Contenido.

## Uso sin backend

Ocho configuraciones y medidas mínimas del contrato; dialog local controlado, Escape y devolución de foco nativos. Media/SideBySide usan las dos imágenes originales verificadas por SHA-1 Figma y SHA-256 local. media admite sustitución explícita o null para vacío. Sin backend ni recoloración por tema.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function ModalExample(){const [open,setOpen]=useState(false);return <><DS.Button showLeftIcon={false} showRightIcon={false} onClick={()=>setOpen(true)}>Abrir diálogo</DS.Button><DS.Modal open={open} onOpenChange={setOpen} title="Editar muestra" actions={<><DS.Button showLeftIcon={false} showRightIcon={false} variant="default" size="middle" onClick={()=>setOpen(false)}>Cancelar</DS.Button><DS.Button showLeftIcon={false} showRightIcon={false} size="middle" onClick={()=>setOpen(false)}>Listo</DS.Button></>}><DS.InputField label="Nombre" defaultValue="Documento de ejemplo"/></DS.Modal></>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [content.tsx](../../src/components/content.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface ModalProps { open:boolean; onOpenChange:(open:boolean)=>void; title:string; subtitle?:ReactNode; children?:ReactNode; actions?:ReactNode; sideContent?:ReactNode; size?:'small'|'medium'|'large'; variant?:'basic'|'media'|'side-by-side'; media?:ReactNode; scroll?:boolean; icon?:ReactNode; showIcon?:boolean; showSubtitle?:boolean; showLink?:boolean; link?:ReactNode; showClose?:boolean }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Modal: {open,onOpenChange,title,subtitle,children,actions,sideContent,size='medium',variant='basic',media=<img src={`/assets/modal-${variant==='media'?'media':'side-by-side'}.png`} alt=""/>,scroll=false,icon,showIcon=false,showSubtitle=true,showLink=false,link='and link.',showClose=true}:ModalProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. children/actions/sideContent/media. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [modal.contract.v0.1.0.md](../../../../specs/modal.contract.v0.1.0.md) · SHA-256 `589a78693d2bad3f3d9233a8ea6ecd5e9254f1aae429aac6da941b030cc78f57`.
- [modal.typography.amendment.v0.1.0.md](../../../../specs/components/modal.typography.amendment.v0.1.0.md) · SHA-256 `f00dc2b2a44144fe0039946ed6b8e9df3e5a074e075c04fad60832d9bb7a00e6`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
