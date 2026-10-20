# DropdownItem · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `DROPDOWN-ITEM-001` · API local 0.1.0 · categoría Formularios.

## Uso sin backend

Una opción o acción con contenido secundario y decoración opcional. role se elige según el anfitrión. El checkbox visual no crea otro control anidado.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function DropdownItemExample(){const [selected,setSelected]=useState(false);return <div className="w-72"><DS.DropdownItem selected={selected} leadingIcon={<FileText/>} onClick={()=>setSelected(!selected)}>Documento de muestra</DS.DropdownItem><DS.DropdownItem size="middle" disabled>No disponible</DS.DropdownItem></div>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [forms.tsx](../../src/components/forms.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface DropdownItemProps { children: ReactNode; size?: Size; selected?: boolean; disabled?: boolean; leadingIcon?: ReactNode; trailingIcon?: ReactNode; secondaryText?: string; loading?: boolean; showDivider?: boolean; showCheckbox?: boolean; onClick?: ()=>void; tabIndex?: number; role?: 'option'|'menuitem'; id?: string; type?:'base'|'header'; showLeadingIcon?:boolean; showTrailingIcon?:boolean; showSecondaryText?:boolean }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
DropdownItem: {children,size='large',selected=false,disabled=false,leadingIcon=<Eye weight="light"/>,trailingIcon=<X weight="light"/>,secondaryText="2nd Column",loading,showDivider,showCheckbox,onClick,tabIndex,role,id,type='base',showLeadingIcon=false,showTrailingIcon=false,showSecondaryText=false}:DropdownItemProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [dropdown-item.contract.v0.1.0.md](../../../../specs/dropdown-item.contract.v0.1.0.md) · SHA-256 `414040f481f994316406dfd61ca09a4c5a52b4b9ec97e30dcb2a1dc90ef27d42`.
- [dropdown-item.typography.amendment.v0.1.0.md](../../../../specs/components/dropdown-item.typography.amendment.v0.1.0.md) · SHA-256 `5ba8f1a160b2122fac8bc624f6d34436fcaae2b5456df3850732775de4bd582d`.
- [TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md](../../../../specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md) · SHA-256 `ece3fcbaef98505b403c11f6cba06cdf7a4ec393edddaca29cc243e52e752a55`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
