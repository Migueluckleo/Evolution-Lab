# Badge · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `BADGE-001` · API local 0.1.0 · categoría Estado y ayuda.

## Uso sin backend

Seis tonos contractuales. Color informativo/warning conserva las enmiendas de fidelidad; no implica contraste certificado.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function BadgeExample(){return <div className="flex gap-3 flex-wrap">{(['base','light','informational','warning','error','success'] as const).map(tone=><DS.Badge key={tone} tone={tone} leftIcon={<Info/>}>{tone}</DS.Badge>)}</div>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [feedback.tsx](../../src/components/feedback.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface BadgeProps extends HTMLAttributes<HTMLSpanElement> { tone?: 'base'|'light'|'informational'|'warning'|'error'|'success'; leftIcon?: ReactNode; rightIcon?: ReactNode; showLeftIcon?: boolean; showRightIcon?: boolean }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Badge: {tone='base',leftIcon=<Presentation weight="fill"/>,rightIcon=<Presentation weight="fill"/>,showLeftIcon=true,showRightIcon=false,children='Light',className,...props}:BadgeProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [badge.contract.v0.1.0.md](../../../../specs/components/badge.contract.v0.1.0.md) · SHA-256 `886fd8376f440063532a526825287e030918bf9092d827108ca58a49596e4b0b`.
- [badge.source-color-amendment.v0.1.2.md](../../../../specs/components/badge.source-color-amendment.v0.1.2.md) · SHA-256 `5120317285938bb9fc06fd67ed0ce8b11b71c1d23051cd13464137c36280dabb`.
- [badge.typography.amendment.v0.1.0.md](../../../../specs/components/badge.typography.amendment.v0.1.0.md) · SHA-256 `de915ea9408252c6f6042c02219b4040e2c69843eaa66bd194328777e2008266`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
