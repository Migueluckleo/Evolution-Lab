# NavigationSwitchTab · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `NAVIGATION-SWITCH-TAB-001` · API local 0.1.0 · categoría Navegación.

## Uso sin backend

Lista de pestañas controlada con flechas/Home/End y paneles opcionales. IDs por instancia. items permite 0..n; no se fija la muestra en cuatro.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function NavigationSwitchTabExample(){const [value,setValue]=useState('lista');return <DS.NavigationSwitchTab label="Presentación de documentos" value={value} onValueChange={setValue} items={[{id:'lista',label:'Lista',content:<p className="py-4">Contenido de la lista</p>},{id:'resumen',label:'Resumen',content:<p className="py-4">Contenido del resumen</p>}]}/>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [navigation.tsx](../../src/components/navigation.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface TabItem { id:string; label:string; disabled?:boolean; content?:ReactNode; leftIcon?:ReactNode; count?:string }

export interface NavigationSwitchTabProps { items:readonly TabItem[]; value:string; onValueChange:(value:string)=>void; label:string }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
NavigationSwitchTab: {items,value,onValueChange,label}:NavigationSwitchTabProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. items/content. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [navigation-switch-tab.contract.v0.1.0.md](../../../../specs/navigation-switch-tab.contract.v0.1.0.md) · SHA-256 `c9007112a7155c155a5fc32ee8e809fa28576005069c8964f3205e9f77fb4cf1`.
- [composition-slots.amendment.v0.1.0.md](../../../../specs/composition-slots.amendment.v0.1.0.md) · SHA-256 `3573e964d3f523470e9c3d733993911ccec94dd2484ea6211d739a1588c81cb5`.
- [navigation-switch-tab.typography.amendment.v0.1.0.md](../../../../specs/components/navigation-switch-tab.typography.amendment.v0.1.0.md) · SHA-256 `81abdad4e64d4ccad34270fbc60d2f0de8047384af0abe19f971131722a05b16`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
