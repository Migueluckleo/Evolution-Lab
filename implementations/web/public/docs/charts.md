# Charts · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `CHARTS-001` · API local 0.1.0 · categoría Datos.

## Uso sin backend

23 definiciones visuales agrupadas en cinco piezas y composición Charts. Cell conserva padding first=8/4, middle=6/6, last=4/8 y dash2/2. Progress Top639×30/Detail639×104 conserva fills580/247 y dos leyendas de muestra; value no calcula porcentaje. Header638×48. Gauge conserva paths25/50/75. No motor de datos continuo.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function ChartsExample(){return <DS.Charts title="Resumen de muestra" description="Composición visual con valores de ejemplo" legend={<><DS.ChartLegendLabel swatch="series-1">Serie 1</DS.ChartLegendLabel><DS.ChartLegendLabel swatch="series-2">Serie 2</DS.ChartLegendLabel></>}><DS.SemiDonutGauge progress={75}/><DS.ProgressChartItem label="Ejemplo estático" value="$100k"/></DS.Charts>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [charts.tsx](../../src/components/charts.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface ChartLegendLabelProps { children:ReactNode; weight?:'regular'|'semibold'; size?:'small'|'medium'; swatch?:'neutral'|'series-1'|'series-2'|'series-3'|'progress'|'track'|false }

export interface ChartCellProps { hasContent?:boolean; position?:'first'|'middle'|'last'; segment?:'solo'|'upper'|'middle'|'lower'; label?:string }

export interface ChartHeaderProps { title:string; description?:string; legend?:ReactNode; showDescription?:boolean; showLegend?:boolean }

export interface ProgressChartItemProps { label:string; value:string; type?:'top'|'detail'; detail?:ReactNode }

export interface SemiDonutGaugeProps { progress?:25|50|75; label?:string }

export interface ChartsProps extends ChartHeaderProps { children:ReactNode }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Charts: {title,description,legend,showDescription,showLegend,children}:ChartsProps
ChartHeader: {title,description,legend,showDescription=true,showLegend=true}:ChartHeaderProps
ChartLegendLabel: {children,weight='regular',size='small',swatch='neutral'}:ChartLegendLabelProps
ChartCell: {hasContent=false,position='first',segment='solo',label}:ChartCellProps
ProgressChartItem: {label,value,type='top',detail}:ProgressChartItemProps
SemiDonutGauge: {progress=75,label='Avance'}:SemiDonutGaugeProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. children/legend/detail. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [charts.contract.v0.1.0.md](../../../../specs/charts.contract.v0.1.0.md) · SHA-256 `e65d084d9f7a9600df1d00f19922c1039b09e926315b9c3052746a1327d08cea`.
- [six-family-color.amendment.v0.1.0.md](../../../../specs/components/six-family-color.amendment.v0.1.0.md) · SHA-256 `f569d5e132a0b5480f7b540dea8f157a601f27f24e86bb5ccb05b2d05f4b2cc9`.
- [composition-slots.amendment.v0.1.1.md](../../../../specs/composition-slots.amendment.v0.1.1.md) · SHA-256 `784535d06d9d996568346426144234fcd49050f509b14976e92ee74e74e3c041`.
- [charts.typography.amendment.v0.1.0.md](../../../../specs/components/charts.typography.amendment.v0.1.0.md) · SHA-256 `fd174e3ad5e6f3dd16f875aa09ef3d65ff17cb5c9d97d07978d91615b33ca08b`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
