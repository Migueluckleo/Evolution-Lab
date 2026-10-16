# MetricCard · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `METRIC-CARD-001` · API local 0.1.0 · categoría Contenido.

## Uso sin backend

Ocho estructuras exactas Type×Size. Valores y textos son muestras, sin cálculo; vertical/horizontal usan hasta dos pares, V1/V2 el primer valor. Show icon/action/detail son independientes. V1 tiene las alturas normalizadas156/116; V2 baldosa96/80 con icono64/48. action es una affordance de muestra; un botón/enlace real debe venir del consumidor.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function MetricCardExample(){return <DS.MetricCard title="Documentos" description="Datos de demostración" values={[{label:'Este mes',value:'128'},{label:'Mes anterior',value:'112'}]} icon={<FileText/>}/>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [content.tsx](../../src/components/content.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface MetricValue { label:string; value:string }

export interface MetricCardProps { variant?:'vertical'|'horizontal'|'one-v1'|'one-v2'; size?:'large'|'small'; title:string; description?:string; values:readonly MetricValue[]; trend?:string; icon?:ReactNode; action?:ReactNode; showIcon?:boolean; showAction?:boolean; showDetail?:boolean }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
MetricCard: {variant='vertical',size='large',title,description,values,trend,icon=<CurrencyCircleDollar weight="light"/>,action=<ArrowUpRight weight="light"/>,showIcon=true,showAction=true,showDetail=true}:MetricCardProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija, dos métricas en Vertical/Horizontal y una en V1/V2. Los swaps icon/action no crean cardinalidad variable. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [metric-card.contract.v0.1.0.md](../../../../specs/metric-card.contract.v0.1.0.md) · SHA-256 `243abaf3460738916249876eb9b6064edf1341a98a242c54e4a05d78819b824e`.
- [six-family-color.amendment.v0.1.0.md](../../../../specs/components/six-family-color.amendment.v0.1.0.md) · SHA-256 `f569d5e132a0b5480f7b540dea8f157a601f27f24e86bb5ccb05b2d05f4b2cc9`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
