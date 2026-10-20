# Avatar · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `AVATAR-001` · API local 0.1.0 · categoría Contenido.

## Uso sin backend

src explícito; foto incluida de muestra, sin iniciales ni fallback fabricado. Show status=true conserva el default visual del maestro; el dot es decorativo salvo que la pantalla aporte statusLabel. No se infiere presencia real.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function AvatarExample(){return <div className="flex gap-4 items-center"><DS.Avatar label="Persona de muestra"/><DS.Avatar type="text" initials="ML" label="Miguel Leo" showStatus statusLabel="Activo, dato de muestra"/><DS.Avatar type="icon" size="large" label="Usuario"/></div>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [content.tsx](../../src/components/content.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface AvatarProps { type?:'image'|'icon'|'text'; size?:'small'|'medium'|'large'|'extra-large'; src?:string; initials?:string; icon?:ReactNode; label:string; showStatus?:boolean; statusLabel?:string }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Avatar: {type='image',size='extra-large',src='/assets/avatar.png',initials='JA',icon=<User weight="light"/>,label,showStatus=true,statusLabel}:AvatarProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [avatar.contract.v0.1.0.md](../../../../drafts/contracts/avatar.contract.v0.1.0.md) · SHA-256 `465296694978a14e8019b2f52af61f42b88f78fecfa480d0081d4f877e122396`.
- [avatar.source-color-amendment.v0.1.1.md](../../../../specs/components/avatar.source-color-amendment.v0.1.1.md) · SHA-256 `f1a010f1dc3f6ee85b756dc3131840d7fcfd3b6f346077bbb4fb3d445d79832d`.
- [avatar.typography.amendment.v0.1.0.md](../../../../specs/components/avatar.typography.amendment.v0.1.0.md) · SHA-256 `b0a593025a3fc3c453869a80dcc34b9ed9f01e88e36502fc9706853286dc97d6`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
