# Header · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `HEADER-001` · API local 0.1.0 · categoría Composición.

## Uso sin backend

Composición sin menús ficticios. logo es contenido explícito para no elegir un artwork ausente o recolorearlo por tema. Eventos company/user son callbacks del consumidor. Geometría desktop, puede requerir overflow del anfitrión.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function HeaderExample(){return <DS.Header logo={<DS.Logos alt="CONTPAQi Contable"/>} version="2.0.0" releaseLabel="ALPHA .1" actions={<DS.IconButton showCount={false} label="Notificaciones" icon={<Bell/>}/>} company="Empresa de ejemplo" taxId="RFC de muestra" user={<DS.Avatar type="text" initials="ML" label="Usuario de muestra"/>}/>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [layout.tsx](../../src/components/layout.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface HeaderProps { logo:ReactNode; version?:string; releaseLabel?:string; actions?:ReactNode; company?:string; taxId?:string; user?:ReactNode; showVersion?:boolean; showActions?:boolean; showCompany?:boolean; showUser?:boolean; onCompanyClick?:()=>void; onUserClick?:()=>void }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Header: {logo,version='2.0.0',releaseLabel='ALPHA .1',actions,company='Empresa SA de CV',taxId='CAC840428RH1',user,showVersion=true,showActions=true,showCompany=true,showUser=true,onCompanyClick,onUserClick}:HeaderProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. logo/actions/user. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [header.contract.v0.1.0.md](../../../../specs/header.contract.v0.1.0.md) · SHA-256 `18b87c9e1cb91346d6f75359d51f78c825ffeb2bf1a6ba1b148a6f8e4291e00e`.
- [header.typography.amendment.v0.1.0.md](../../../../specs/components/header.typography.amendment.v0.1.0.md) · SHA-256 `9bf2db753a9224da9ee9bfdd2d33f229c7a99d15632d1ee810861ee927f49440`.
- [TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md](../../../../specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md) · SHA-256 `ece3fcbaef98505b403c11f6cba06cdf7a4ec393edddaca29cc243e52e752a55`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
