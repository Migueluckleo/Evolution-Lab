# RadioButton · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `RADIO-BUTTON-001` · API local 0.1.0 · categoría Formularios.

## Uso sin backend

input radio nativo; agrupar por name y entregar value. Selección inicial del producto explícita, independiente del default Figma.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function RadioButtonExample(){const [value,setValue]=useState('a');return <fieldset className="grid gap-3"><legend className="mb-3 font-semibold">Vista inicial</legend>{['a','b'].map(v=><DS.RadioButton showRightLabel key={v} name="radio-demo" value={v} label={`Vista ${v.toUpperCase()}`} checked={value===v} onChange={()=>setValue(v)}/>)}</fieldset>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [forms.tsx](../../src/components/forms.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface RadioButtonProps extends Omit<InputHTMLAttributes<HTMLInputElement>,'type'|'size'|'children'> { label: string; hideLabel?: boolean; labelSide?: 'left'|'right'; name: string; value: string; leftLabel?:ReactNode; rightLabel?:ReactNode; showLeftLabel?:boolean; showRightLabel?:boolean }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
RadioButton: {label,hideLabel,labelSide,leftLabel,rightLabel,showLeftLabel=labelSide==='left',showRightLabel=labelSide==='right',className,...props}:RadioButtonProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [radio-button.contract.v0.1.0.md](../../../../specs/radio-button.contract.v0.1.0.md) · SHA-256 `37be63a92fd4b30468c15d50689487e84a3a67de5c43547c390a083a2427fbfe`.
- [radio-checkbox.refinement.amendment.v0.1.2.md](../../../../specs/components/radio-checkbox.refinement.amendment.v0.1.2.md) · SHA-256 `a53c4ed47b9dd7871009a67983ccc2ad3e2ba69d96bc5b8faa05ac0fa48f75a1`.
- [radio-button.source-color-amendment.v0.1.1.md](../../../../specs/radio-button.source-color-amendment.v0.1.1.md) · SHA-256 `55ed04efb099953c15097bbd2cc8ca64b5f9141e67bd54601fe4150e7df0e5e0`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
