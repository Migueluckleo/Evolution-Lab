# Logos · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `LOGOS-001` · API local 0.1.0 · categoría Contenido.

## Uso sin backend

72/72 exportaciones originales locales con IDs/hashes. PNG o SVG según el exportador, sin recolorear; PNG no promete escalado vectorial. assetId desconocido produce error explícito y src permite asset local propio. Completar los assets web no resuelve el QA geométrico histórico de la biblioteca Figma.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function LogosExample(){const [id,setId]=useState('435:2654');return <div className="grid gap-6"><label>Asset local<select className="block mt-2 border border-ds-border rounded-ds p-2 max-w-full" value={id} onChange={e=>setId(e.target.value)}>{DS.logoAssets.map(a=><option key={a.id} value={a.id}>{a.family} · {a.name}</option>)}</select></label><DS.Logos assetId={id} alt="Logotipo original CONTPAQi" height={64}/></div>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [content.tsx](../../src/components/content.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface LogosProps { assetId?:string; src?:string; alt:string; height?:number; className?:string }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Logos: {assetId='435:2654',src,alt,height=48,className}:LogosProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [logos.contract.v0.1.0.md](../../../../drafts/contracts/logos.contract.v0.1.0.md) · SHA-256 `088b7e86d695541b4587b891a658a2d50e1843e9bb0e98a1ef0cdfc340bf4f56`.
- [logos.scope.amendment.v0.1.1.md](../../../../specs/components/logos.scope.amendment.v0.1.1.md) · SHA-256 `f72b740ff43d134c794fb2ad6ea596ffa36bc4f09afeae3996575b04a5fe7467`.
- [logos.typography.amendment.v0.1.0.md](../../../../specs/components/logos.typography.amendment.v0.1.0.md) · SHA-256 `f31a958e685c621afa2b295eadab9889e23845299519a9341d370cdedefb13fb`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
