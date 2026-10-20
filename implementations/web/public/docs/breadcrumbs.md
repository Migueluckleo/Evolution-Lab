# Breadcrumbs · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `BREADCRUMBS-001` · API local 0.1.0 · categoría Navegación.

## Uso sin backend

Lista ordenada; solo enlaces con href navegan, último segmento aria-current=page. Cantidades variables sin convertir 2–5 en un máximo.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function BreadcrumbsExample(){return <DS.Breadcrumbs items={[{id:'inicio',label:'Inicio',href:'#componer'},{id:'documentos',label:'Documentos',href:'#table'},{id:'detalle',label:'Detalle'}]}/>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [navigation.tsx](../../src/components/navigation.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface BreadcrumbItem { id: string; label: string; href?: string; disabled?: boolean; icon?: ReactNode; type?:'default'|'icon'|'shortened' }

export interface BreadcrumbItemProps { label?:string; href?:string; disabled?:boolean; icon?:ReactNode; type?:'default'|'icon'|'shortened'; current?:boolean }

export interface BreadcrumbsProps { items: readonly BreadcrumbItem[]; label?: string; onBack?: ()=>void; showBack?:boolean; children?:ReactNode }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Breadcrumbs: {items,label='Ruta de navegación',onBack,showBack=true,children}:BreadcrumbsProps
BreadcrumbItem: {label='Breadcrumb',href,disabled=false,icon=<House size={24} weight="light"/>,type='default',current=false}:BreadcrumbItemProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. items. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [breadcrumbs.contract.v0.1.0.md](../../../../specs/breadcrumbs.contract.v0.1.0.md) · SHA-256 `241c1b03d7f0d93c8c39324e604739a670926d719e3c801e82ed7c018c59323d`.
- [six-family-color.amendment.v0.1.0.md](../../../../specs/components/six-family-color.amendment.v0.1.0.md) · SHA-256 `f569d5e132a0b5480f7b540dea8f157a601f27f24e86bb5ccb05b2d05f4b2cc9`.
- [composition-slots.amendment.v0.1.0.md](../../../../specs/composition-slots.amendment.v0.1.0.md) · SHA-256 `3573e964d3f523470e9c3d733993911ccec94dd2484ea6211d739a1588c81cb5`.
- [breadcrumbs.typography.amendment.v0.1.0.md](../../../../specs/components/breadcrumbs.typography.amendment.v0.1.0.md) · SHA-256 `0f1fc99d903177a8b55c12638fd37e7028b6083f3b6b2faf65f5a0f729632980`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
