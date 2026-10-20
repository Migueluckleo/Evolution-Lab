# AppShell · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `APP-SHELL-001` · API local 0.1.0 · categoría Composición.

## Uso sin backend

Shell de escritorio, base1440×1024, Header96 y rail104/266 con padding0/16/24. width/height pertenecen al anfitrión; sin mínimo ni breakpoint1024 inventado. Sidebar llena el alto disponible (904px en la base).

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function AppShellExample(){return <DS.AppShell header={<DS.Header logo={<DS.Logos alt="CONTPAQi Contable"/>}/>} sidebar={<DS.Sidebar items={[{id:'home',label:'Inicio',icon:<House/>,href:'#componer',active:true}]}/>}><div className="p-8"><h2 className={`${DS.typographyClass('heading-5-semibold')} mb-6`}>Pantalla de ejemplo</h2><DS.MetricCard title="Documentos" values={[{label:'Total',value:'128'}]}/></div></DS.AppShell>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [layout.tsx](../../src/components/layout.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface AppShellProps { header:ReactNode; sidebar:ReactNode; children?:ReactNode; expanded?:boolean; className?:string; width?:CSSProperties['width']; height?:CSSProperties['height'] }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
AppShell: {header,sidebar,children,expanded=false,className,width=1440,height=1024}:AppShellProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. header/sidebar/children. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [app-shell.contract.v0.1.0.md](../../../../specs/app-shell.contract.v0.1.0.md) · SHA-256 `f4735e43344b54477df4ab8058f55fa5c45b6c03fdbdf651c6d35feb5d75ad9e`.
- [app-shell.typography.amendment.v0.1.0.md](../../../../specs/components/app-shell.typography.amendment.v0.1.0.md) · SHA-256 `74768a9059fed6ab27bbe6bc4b081f1ba4bae3b4e504e334ab442c45785cb31b`.
- [TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md](../../../../specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md) · SHA-256 `ece3fcbaef98505b403c11f6cba06cdf7a4ec393edddaca29cc243e52e752a55`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
