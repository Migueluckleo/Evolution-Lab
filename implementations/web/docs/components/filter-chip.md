# FilterChip · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `FILTER-CHIP-001` · API local 0.1.0 · categoría Acciones.

## Uso sin backend

Defaults Chip, Large, selected=false y dos PlusCircle Light ocultos. showLeftIcon/showRightIcon y swaps son independientes. selected es controlado; onSelectedChange propone el valor, no filtra datos internamente.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function FilterChipExample(){const [selected,setSelected]=useState(false);return <DS.FilterChip showLeftIcon selected={selected} onSelectedChange={setSelected} leftIcon={<Check/>}>Facturas</DS.FilterChip>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [actions.tsx](../../src/components/actions.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface FilterChipProps extends Omit<ButtonHTMLAttributes<HTMLButtonElement>,'onChange'> {
  selected?: boolean;
  size?: Size;
  leftIcon?: ReactNode;
  rightIcon?: ReactNode;
  showLeftIcon?: boolean;
  showRightIcon?: boolean;
  onSelectedChange?: (selected: boolean) => void;
}
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
FilterChip: {selected=false,size='large',leftIcon=<PlusCircle weight="light"/>,rightIcon=<PlusCircle weight="light"/>,showLeftIcon=false,showRightIcon=false,onSelectedChange,onClick,children='Chip',className,...props}:FilterChipProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [filter-chip.contract.v0.2.0.md](../../../../specs/components/filter-chip.contract.v0.2.0.md) · SHA-256 `325a408cfa6a5880c2136aee89a448e9ab3a6d928199543d946d6ae3a52a6cb8`.
- [filter-chip.semantic.amendment.v0.2.1.md](../../../../specs/components/filter-chip.semantic.amendment.v0.2.1.md) · SHA-256 `0c6dba55ac393a09f17176c6a23e5aeb4835e93490c057d883746a258ad2865f`.
- [filter-chip.typography.amendment.v0.1.0.md](../../../../specs/components/filter-chip.typography.amendment.v0.1.0.md) · SHA-256 `c5d3dfe599d71b9f9c738c691a1a694083e91cbafc31f58f86130b9f80deabd1`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
