# Table · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `TABLE-001` · API local 0.1.0 · categoría Contenido.

## Uso sin backend

Piezas Table/Header/HeaderCell/Row/Cell/ActionsCell reutilizables y Slots 0..n. Show selection/actions/status/copy/brand/sort exponen la anatomía documentada. Hover conserva TABLE-AUD-001: añade 8px de ancho, muestra DotsThree y reduce 24px la primera celda de ancho explícito. No se inventan selección, copia ni orden automático; el consumidor aporta los callbacks.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function TableExample(){const rows=[{id:'doc-1',name:'Documento A',status:'Revisado'},{id:'doc-2',name:'Documento B',status:'Pendiente'}];return <DS.Table caption="Documentos de ejemplo" rows={rows} rowKey={r=>r.id} columns={[{id:'name',header:'Documento',cell:r=>r.name},{id:'status',header:'Estado',cell:r=><DS.Badge tone={r.status==='Revisado'?'success':'warning'}>{r.status}</DS.Badge>}]}/>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [content.tsx](../../src/components/content.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface TableGlyphProps { type:'sort'|'copy' }

export interface TableHeaderCellProps { children?:ReactNode; width?:number; brand?:ReactNode; showBrand?:boolean; showSort?:boolean; sortIcon?:ReactNode }

export interface TableCellProps { children?:ReactNode; width?:number; status?:ReactNode; showStatus?:boolean; showCopy?:boolean; onCopy?:()=>void }

export interface TableActionsCellProps { children?:ReactNode }

export interface TableHeaderProps { children?:ReactNode; showSelection?:boolean; selection?:ReactNode; showActions?:boolean; actionsLabel?:ReactNode }

export interface TableRowProps { children?:ReactNode; state?:'default'|'hover'; showSelection?:boolean; selection?:ReactNode; showActions?:boolean; actions?:ReactNode; hoverAction?:ReactNode }

export interface TableColumn<T> { id:string; header:ReactNode; width?:number; cell:(row:T)=>ReactNode; brand?:ReactNode; showBrand?:boolean; showSort?:boolean }

export interface TableProps<T> { columns:readonly TableColumn<T>[]; rows:readonly T[]; rowKey:(row:T)=>string; caption:string; showCaption?:boolean; actions?:(row:T)=>ReactNode; showSelection?:boolean; headerSelection?:ReactNode; rowSelection?:(row:T)=>ReactNode; header?:ReactNode; children?:ReactNode; width?:CSSProperties['width'] }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Table: {columns,rows,rowKey,caption,showCaption=false,actions,showSelection=false,headerSelection,rowSelection,header,children,width=1280}:TableProps<T>
TableHeader: {children,showSelection=false,selection=<Checkbox label="Seleccionar filas" hideLabel/>,showActions=false,actionsLabel='Acciones'}:TableHeaderProps
TableHeaderCell: {children='UUID',width,brand=<Logos assetId="434:3657" alt="CONTPAQi" height={16}/>,showBrand=false,showSort=false,sortIcon=<TableGlyph type="sort"/>}:TableHeaderCellProps
TableRow: {children,state,showSelection=false,selection=<Checkbox label="Seleccionar fila" hideLabel/>,showActions=false,actions,hoverAction=<DotsThree size={24} weight="light"/>}:TableRowProps
TableCell: {children='UUID',width,status=<Badge tone="success" showLeftIcon={false}>Status</Badge>,showStatus=false,showCopy=false,onCopy}:TableCellProps
TableActionsCell: {children}:TableActionsCellProps
TableGlyph: {type}:TableGlyphProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. columns/rows/cell/actions. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [table.contract.v0.1.0.md](../../../../specs/table.contract.v0.1.0.md) · SHA-256 `e3b7b1c999fa8f59c839a082cde95f5709d21375feb4bc2fefd26652c2394108`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
