# EmptyStates · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `EMPTY-STATES-001` · API local 0.1.0 · categoría Contenido.

## Uso sin backend

Cuatro composiciones. Seis ilustraciones locales con geometría original y colores de extensión semántica. Ilustración sustituible. Main exige 548px; no se fuerza a móvil ni se deduce un estado de error.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function EmptyStatesExample(){return <DS.EmptyStates presentation="compact" title="Aún no hay documentos" mainActions={<DS.Button showLeftIcon={false} showRightIcon={false} size="middle" onClick={()=>alert('Acción local de ejemplo')}>Agregar documento</DS.Button>}>Agrega un documento de muestra para explorar esta pantalla.</DS.EmptyStates>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [content.tsx](../../src/components/content.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface EmptyStateIllustrationProps { asset?:'2281'|'2298'|'2323'|'2346'|'2364'|'2381' }

export interface EmptyStatesProps { presentation?:'default'|'compact'|'inline'|'main'; title?:ReactNode; children?:ReactNode; illustration?:ReactNode; mainActions?:ReactNode; supportingActions?:ReactNode; showVisual?:boolean; showTitle?:boolean; showMainActions?:boolean; showSupportingActions?:boolean }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
EmptyStates: {presentation='default',title,children,illustration,mainActions,supportingActions,showVisual=presentation!=='inline',showTitle=presentation!=='inline',showMainActions=presentation!=='inline',showSupportingActions=true}:EmptyStatesProps
EmptyStateIllustration: {asset='2381'}:EmptyStateIllustrationProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. mainActions/supportingActions. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [empty-states.contract.v0.1.0.md](../../../../specs/empty-states.contract.v0.1.0.md) · SHA-256 `25de9da45c7e835f9b244867b7b70d3ec496a270ab61ec785e49775526fd750f`.
- [empty-states.typography.amendment.v0.1.0.md](../../../../specs/components/empty-states.typography.amendment.v0.1.0.md) · SHA-256 `9fe00f6d09fe88c4d1d20299b099e04600a33e488e265197c8606a19c4ee8333`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
