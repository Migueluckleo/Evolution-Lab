# NavigationTab · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `NAVIGATION-TAB-001` · API local 0.1.0 · categoría Navegación.

## Uso sin backend

Base/Dynamic, activo y deshabilitado. selectedPresentation solo aplica a Dynamic activo; no modifica datos ni crea un panel. El consumidor asigna rol/atributos según uso.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function NavigationTabExample(){const [active,setActive]=useState(true);return <div className="flex gap-4"><DS.NavigationTab active={active} aria-pressed={active} onClick={()=>setActive(!active)} leftIcon={<FileText/>}>Resumen</DS.NavigationTab><DS.NavigationTab variant="dynamic" active={!active} aria-pressed={!active} onClick={()=>setActive(!active)}>Detalle</DS.NavigationTab></div>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [navigation.tsx](../../src/components/navigation.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface NavigationSwitchTabItemProps extends ButtonHTMLAttributes<HTMLButtonElement> { active?: boolean; leftIcon?: ReactNode; rightIcon?: ReactNode; count?: string; showLeftIcon?:boolean; showRightIcon?:boolean; showCount?:boolean }

export interface NavigationTabProps extends NavigationSwitchTabItemProps { variant?: 'base'|'dynamic'; selectedPresentation?: boolean; showDot?: boolean; showDivisor?:boolean }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
NavigationTab: {variant='base',active=false,selectedPresentation=false,showDot=false,showDivisor=true,leftIcon=<ImageSquare weight={selectedPresentation?'regular':'light'}/>,rightIcon=<ImageSquare weight="light"/>,showLeftIcon=true,showRightIcon=true,showCount:ignoredCount,count:ignoredCountText,children='Tab title',className,...props}:NavigationTabProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [navigation-tab.contract.v0.1.0.md](../../../../specs/navigation-tab.contract.v0.1.0.md) · SHA-256 `1f28dbd13b0e5c055d2dc551e6a957b2b64f91701425d0b1089ef505c9b0035c`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
