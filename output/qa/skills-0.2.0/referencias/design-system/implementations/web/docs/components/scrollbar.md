# Scrollbar · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `SCROLLBAR-001` · API local 0.1.0 · categoría Contenido.

## Uso sin backend

Scrollbar representa las ocho variantes visuales fijas (orientación y Thumb Size); las etiquetas históricas no son porcentajes calculados. ScrollArea es el contenedor funcional nativo separado, que calcula su thumb por contenido. No hay drag ni posición continua en la pieza visual.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function ScrollbarExample(){return <div className="flex gap-8"><DS.Scrollbar thumbSize="25%"/><DS.ScrollArea label="Lista larga de muestra" height={200} className="w-72"><ul className="grid gap-4 pr-4">{Array.from({length:20},(_,i)=><li key={i}>Elemento {i+1}</li>)}</ul></DS.ScrollArea></div>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [content.tsx](../../src/components/content.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface ScrollbarProps { orientation?:'vertical'|'horizontal'; thumbSize?:'25%'|'33%'|'50%'|'75%'; label?:string; className?:string }

export type ScrollbarThumbProps = { orientation?:'vertical'|'horizontal'; className?:string } & ({thumbSize?:'25%';position?:'1/4'|'2/4'|'3/4'|'4/4'}|{thumbSize:'33%';position?:'1/3'|'2/3'|'3/3'}|{thumbSize:'50%'|'75%';position?:'1/2'|'2/2'});
/** Geometría interna normalizada al recorrido público272; posiciones discretas, sin drag. */

export interface ScrollAreaProps extends HTMLAttributes<HTMLDivElement> { orientation?:'vertical'|'horizontal'; label:string; height?:number }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Scrollbar: {orientation='vertical',thumbSize='25%',label,className}:ScrollbarProps
ScrollbarThumb: {orientation='vertical',thumbSize='25%',position,className}:ScrollbarThumbProps
ScrollArea: {orientation='vertical',label,height=280,children,className,...props}:ScrollAreaProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. El viewport web recibe children de cantidad/composición variable. La anatomía visual del scrollbar permanece fija; esta composición web no afirma Slots en Figma. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [scrollbar.contract.v0.1.0.md](../../../../specs/scrollbar.contract.v0.1.0.md) · SHA-256 `64326d0219578049084a46beed5181bfee13eba4b1c801a95098ce1b390cf9f9`.
- [scrollbar.color-approximation.amendment.v0.1.1.md](../../../../specs/scrollbar.color-approximation.amendment.v0.1.1.md) · SHA-256 `9706debe1203c2b29bd58d646060744be24bddcf5ad16b65ca9ca039f40b173e`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
