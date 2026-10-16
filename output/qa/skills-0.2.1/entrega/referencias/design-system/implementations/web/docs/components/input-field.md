# InputField · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `INPUT-FIELD-001` · API local 0.1.0 · categoría Formularios.

## Uso sin backend

Etiqueta asociada, helper e invalid enlazados por ID. value/onChange o defaultValue siguen React. status es presentación; no valida RFC, moneda ni datos. La enmienda Disabled exige texto disabled también con contenido.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function InputFieldExample(){const [value,setValue]=useState('');return <DS.InputField label="Nombre de la pantalla" placeholder="Escribe un nombre" value={value} onChange={e=>setValue(e.target.value)} helper="Texto editable, sin validación de negocio" required/>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [forms.tsx](../../src/components/forms.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface InputFieldProps extends Omit<InputHTMLAttributes<HTMLInputElement>,'size'|'prefix'> { label: string; hideLabel?: boolean; helper?: string; prefix?: string; trailingIcon?: ReactNode; size?: Size; status?: 'default'|'success'|'error'; showLabel?:boolean; showText?:boolean; showHelper?:boolean; showPrefix?:boolean; showTrailingIcon?:boolean; showHelpIcon?:boolean; helpIcon?:ReactNode }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
InputField: {label,hideLabel=false,helper='Optional helper text',prefix='MXN',trailingIcon=<Eye weight="light"/>,showLabel=true,showText=true,showHelper=true,showPrefix=false,showTrailingIcon=true,showHelpIcon=false,helpIcon=<Question weight="light" size={20}/>,size='large',status='default',id:providedId,className,required=true,disabled,placeholder="Placeholder text",...props}:InputFieldProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [input-field.contract.v0.1.0.md](../../../../specs/input-field.contract.v0.1.0.md) · SHA-256 `e01e90d9dbc4dfdfc4230aac875f8d8a7374673b0a02bbda44eabf9962403c2d`.
- [input-field.disabled-text.amendment.v0.1.1.md](../../../../specs/input-field.disabled-text.amendment.v0.1.1.md) · SHA-256 `fc73aef18bd2c4ca6fcdd4eaa17d92c9e65aee0f4e54ff993eb9aeefc0f98a45`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
