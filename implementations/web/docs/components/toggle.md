# Toggle · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `TOGGLE-001` · API local 0.1.0 · categoría Formularios.

## Uso sin backend

On/Off usa switch nativo. Mixed usa checkbox mixto con guion 24×4; no alterna ni calcula agregados por sí solo. onMixedAction deja la decisión al consumidor, porque clic/grupo vacío siguen sin regla de producto. El halo conserva la excepción AUD-003; no certifica fidelidad completa.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function ToggleExample(){const [checked,setChecked]=useState(false);return <DS.Toggle showRightLabel label="Mostrar detalles" checked={checked} onChange={e=>setChecked(e.target.checked)}/>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [forms.tsx](../../src/components/forms.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface ToggleProps extends Omit<InputHTMLAttributes<HTMLInputElement>,'type'|'size'|'children'> { label: string; hideLabel?: boolean; labelSide?: 'left'|'right'; mixed?: boolean; onMixedAction?: ()=>void; leftLabel?:ReactNode; rightLabel?:ReactNode; showLeftLabel?:boolean; showRightLabel?:boolean }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Toggle: {label,hideLabel,labelSide,leftLabel,rightLabel,showLeftLabel=labelSide==='left',showRightLabel=labelSide==='right',className,mixed=false,onMixedAction,...props}:ToggleProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [toggle.contract.v0.1.0.md](../../../../drafts/contracts/toggle.contract.v0.1.0.md) · SHA-256 `c3b6d1100241e3bdb5c89cc98e89854cda999c87f775a8552211280979326c38`.
- [toggle.focus-effect-amendment.v0.1.3.md](../../../../specs/components/toggle.focus-effect-amendment.v0.1.3.md) · SHA-256 `efcdc635b43774559b3c8001f96f51ea6d3d21c435ea8fea0c7fa8359299d364`.
- [toggle.mixed-amendment.v0.1.4.md](../../../../specs/components/toggle.mixed-amendment.v0.1.4.md) · SHA-256 `1c2f085490c2ad330d92778306d5e9f09f93b625d7f08fdc5ec905ce9ed50b47`.
- [toggle.source-color-amendment.v0.1.5.md](../../../../specs/components/toggle.source-color-amendment.v0.1.5.md) · SHA-256 `b9d4b868ed8dbd1d6eab558d8ce3b5a32919d08f6083055bca1ffe3ca527e6e2`.
- [toggle.visual-contrast-amendment.v0.1.2.md](../../../../specs/components/toggle.visual-contrast-amendment.v0.1.2.md) · SHA-256 `8010307c88f303d8faff80c357956630ac557ff43de71ef9853d22fdaf264357`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
