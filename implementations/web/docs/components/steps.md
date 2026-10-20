# Steps · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `STEPS-001` · API local 0.1.0 · categoría Navegación.

## Uso sin backend

La enmienda Slots permite total variable y indicators personalizado. current/total provienen de la pantalla; no se limitan a los presets 2–7. Las anomalías históricas On Primary/Gallery se conservan en sus roles. No define qué significa completar un paso.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function StepsExample(){const [current,setCurrent]=useState(1);return <DS.Steps total={3} current={current} onStepChange={setCurrent}/>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [navigation.tsx](../../src/components/navigation.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface StepsDotProps { onColor?:'white'|'primary'; selected?:boolean; legacyGallery?:boolean }

export interface StepsCombinationProps { current:number; total:number; onColor?:'white'|'primary'; legacyGallery?:boolean; children?:ReactNode }

export interface StepsProps { current: number; total: number; indicators?:ReactNode; type?: 'gallery'|'numbers'|'gallery-only'; onColor?: 'white'|'primary'; onStepChange?: (step:number)=>void; previousLabel?:string; nextLabel?:string }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Steps: {current,total,indicators,type='gallery',onColor='white',onStepChange,previousLabel='Anterior',nextLabel='Siguiente'}:StepsProps
StepsDot: {onColor='white',selected=false,legacyGallery=false}:StepsDotProps
StepsCombination: {current,total,onColor='white',legacyGallery=false,children}:StepsCombinationProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. indicators. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [steps.contract.v0.1.0.md](../../../../specs/steps.contract.v0.1.0.md) · SHA-256 `dad5b88393048c35391c09a5a13369849adf5b6fb9f1bfdd9fe16847690697e9`.
- [composition-slots.amendment.v0.1.1.md](../../../../specs/composition-slots.amendment.v0.1.1.md) · SHA-256 `784535d06d9d996568346426144234fcd49050f509b14976e92ee74e74e3c041`.
- [steps.brand-theme.amendment.v0.1.1.md](../../../../specs/steps.brand-theme.amendment.v0.1.1.md) · SHA-256 `d13f98fb092e845e72844ccf7f0936816d3f3cdba8a432d4e68b22bbe3bbcc8b`.
- [steps.typography.amendment.v0.1.0.md](../../../../specs/components/steps.typography.amendment.v0.1.0.md) · SHA-256 `4be55b25120f34acb52a2876e07e42a85ae12a48c9b1dcbf3d3e7b69b37e5e52`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
