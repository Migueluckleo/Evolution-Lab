# Stepper · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `STEPPER-001` · API local 0.1.0 · categoría Navegación.

## Uso sin backend

Un item visual con orientación, posición y estado; default no se renombra como paso actual. No avanza ni deriva Checked de acciones.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function StepperExample(){return <div className="flex"><DS.Stepper position="start" state="checked" step="PASO 1" title="Datos" caption="Captura"/><DS.Stepper position="middle" state="default" step="PASO 2" title="Revisión" caption="Detalles"/><DS.Stepper position="end" state="inactive" step="PASO 3" title="Final" caption="Resultado"/></div>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [navigation.tsx](../../src/components/navigation.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface StepperConnectorProps { orientation?:'horizontal'|'vertical'; state?:'checked'|'default'; position?:'start'|'end'; className?:string }

export interface StepperProps { orientation?:'horizontal'|'vertical'; state?:'checked'|'default'|'inactive'; position?:'start'|'middle'|'end'; step?:string; title:string; caption?:string; icon?:ReactNode; showStep?:boolean; showCaption?:boolean }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Stepper: {orientation='horizontal',state='default',position='middle',step,title,caption,showStep=true,showCaption=true,icon=<CheckFat size={16} weight="fill"/>}:StepperProps
StepperConnector: {orientation='horizontal',state='default',position='start',className}:StepperConnectorProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [stepper.contract.v0.1.0.md](../../../../specs/stepper.contract.v0.1.0.md) · SHA-256 `5c3f8d75fe20736fd08411654db5757ea9517af6dd6b078234a17627bac19466`.
- [stepper.brand-theme.amendment.v0.1.1.md](../../../../specs/stepper.brand-theme.amendment.v0.1.1.md) · SHA-256 `de9981eddd06b1c39b1f0830fa2f298a09d8d63511fb6e078f88023f3081c6bf`.
- [stepper.typography.amendment.v0.1.0.md](../../../../specs/components/stepper.typography.amendment.v0.1.0.md) · SHA-256 `b794b59799d96f82830d40b9951cdcefe9f190619d5ec96302ad82795ced1220`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
