# InlineNotification · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `INLINE-NOTIFICATION-001` · API local 0.1.0 · categoría Estado y ayuda.

## Uso sin backend

El aviso usa role=status y solo solicita cierre mediante onDismiss. La pantalla decide cuándo mostrarlo.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function InlineNotificationExample(){const [visible,setVisible]=useState(true);return visible?<DS.InlineNotification tone="info" title="Datos de demostración" onDismiss={()=>setVisible(false)}>Esta pantalla utiliza datos locales editables.</DS.InlineNotification>:<DS.Button showLeftIcon={false} showRightIcon={false} variant="text" onClick={()=>setVisible(true)}>Mostrar aviso</DS.Button>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [feedback.tsx](../../src/components/feedback.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface InlineNotificationProps { tone?: 'light'|'success'|'danger'|'warning'|'info'; title?: ReactNode; children?: ReactNode; showIcon?: boolean; showTitle?: boolean; showDescription?: boolean; showDismiss?: boolean; icon?: ReactNode; onDismiss?: ()=>void; dismissLabel?: string; className?: string }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
InlineNotification: {tone='light',title,children,showIcon=true,showTitle=true,showDescription=true,showDismiss=true,icon,onDismiss,dismissLabel='Cerrar aviso',className}:InlineNotificationProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [inline-notification.contract.v0.1.0.md](../../../../specs/components/inline-notification.contract.v0.1.0.md) · SHA-256 `cdabc527b403751f7f69ca4fe15fd729142b56f404e91f9b28940f374856aa63`.
- [inline-notification.warning-source-color-amendment.v0.1.1.md](../../../../specs/components/inline-notification.warning-source-color-amendment.v0.1.1.md) · SHA-256 `064ee3d0de682fc8b00363aa91f26f24e75e3cc56bf436b2198eff7912378a33`.
- [inline-notification.typography.amendment.v0.1.0.md](../../../../specs/components/inline-notification.typography.amendment.v0.1.0.md) · SHA-256 `f28ca585fa37606021a9977aa3b3cc8be9d25f5090cfed915e6ef63559a4caf2`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
