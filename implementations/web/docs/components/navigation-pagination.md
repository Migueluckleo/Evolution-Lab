# NavigationPagination · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `NAVIGATION-PAGINATION-001` · API local 0.1.0 · categoría Navegación.

## Uso sin backend

La API web calcula un rango compacto de páginas a partir de page/pages; es una decisión técnica de esta capa. No obtiene ni pagina datos. pageSize y callbacks son opcionales. No se deducen totales desde el texto Figma.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function NavigationPaginationExample(){const [page,setPage]=useState(1);const [size,setSize]=useState(20);return <DS.NavigationPagination page={page} pages={8} onPageChange={setPage} pageSize={size} onPageSizeChange={setSize} showFirstLast/>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [navigation.tsx](../../src/components/navigation.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface NavigationPaginationProps { page: number; pages: number; onPageChange: (page:number)=>void; disabled?: boolean; pageSize?: number; pageSizes?: readonly number[]; onPageSizeChange?: (size:number)=>void; showFirstLast?: boolean; showFirst?:boolean; showLast?:boolean; pageItems?:ReactNode }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
NavigationPagination: {page,pages,onPageChange,disabled=false,pageSize=20,pageSizes=[20,50,100],onPageSizeChange,showFirstLast=false,showFirst=showFirstLast,showLast=showFirstLast,pageItems}:NavigationPaginationProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. pages/pageSizes. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [navigation-pagination.contract.v0.1.0.md](../../../../specs/navigation-pagination.contract.v0.1.0.md) · SHA-256 `314ad6b95a6938aa1c6527b22b867f8714d21bbf138a21956333d43c8f40c0ee`.
- [composition-slots.amendment.v0.1.1.md](../../../../specs/composition-slots.amendment.v0.1.1.md) · SHA-256 `784535d06d9d996568346426144234fcd49050f509b14976e92ee74e74e3c041`.
- [navigation-pagination.typography.amendment.v0.1.0.md](../../../../specs/components/navigation-pagination.typography.amendment.v0.1.0.md) · SHA-256 `f10067cc08c9df901cc20fb3412467ebf132359f8b9e90ed5bb7f16a2b83f6b5`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
