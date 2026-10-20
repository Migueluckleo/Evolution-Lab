# Button · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `BUTTON-001` · API local 0.1.0 · categoría Acciones.

## Uso sin backend

Defaults del maestro: primary/large, texto Default y dos PlusCircle Light visibles; showLeftIcon/showRightIcon independientes. Los ejemplos de producto ocultan iconos salvo que aporten significado (REQ-BTN-014). button type=button por defecto; href crea enlace. Pseudoestados CSS del navegador, sin envío de formulario implícito.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function ButtonExample(){const [count,setCount]=useState(0);return <div className="flex flex-wrap items-center gap-4"><DS.Button showLeftIcon showRightIcon={false} onClick={()=>setCount(count+1)} leftIcon={<Plus/>}>Agregar · {count}</DS.Button><DS.Button showLeftIcon={false} showRightIcon={false} variant="default" size="middle">Secundario</DS.Button><DS.Button showLeftIcon={false} showRightIcon={false} variant="text" size="small">Texto</DS.Button><DS.Button showLeftIcon={false} showRightIcon={false} variant="link" href="#componer">Ver pantalla</DS.Button><DS.Button showLeftIcon={false} showRightIcon={false} disabled>Deshabilitado</DS.Button></div>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [actions.tsx](../../src/components/actions.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export type ButtonProps = {
  children?: ReactNode;
  variant?: 'primary' | 'default' | 'text' | 'link';
  size?: Size;
  leftIcon?: ReactNode;
  rightIcon?: ReactNode;
  showLeftIcon?: boolean;
  showRightIcon?: boolean;
  className?: string;
} & ({ href?: never } & ButtonHTMLAttributes<HTMLButtonElement> | { href: string; disabled?: never } & AnchorHTMLAttributes<HTMLAnchorElement>);
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Button: { children='Default', variant='primary', size='large', leftIcon=<PlusCircle weight="light"/>, rightIcon=<PlusCircle weight="light"/>, showLeftIcon=true, showRightIcon=true, className, ...props }: ButtonProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [button.contract.v0.2.0.md](../../../../specs/components/button.contract.v0.2.0.md) · SHA-256 `53e13fa8e664f70d0ce81116e850bbcb0ab7da9f14ac0f08607fa5fda09894a1`.
- [button-page-name.amendment.md](../../../../specs/components/button-page-name.amendment.md) · SHA-256 `b2c896cab9f2f5659101253dbc93ce0410c697081e53daafecebbc5b62895fd7`.
- [button.local-bindings.amendment.v0.2.2.md](../../../../specs/components/button.local-bindings.amendment.v0.2.2.md) · SHA-256 `57b84698047da82ebfd10c18ed828a1aac43482283856d49690d379b60d2e59c`.
- [button.semantic-scope-amendment.v0.2.1.md](../../../../specs/components/button.semantic-scope-amendment.v0.2.1.md) · SHA-256 `8655c79ae1f13c66be04ed406815066a1f3a44d553d2b948390f6bf1b6f1dfb9`.
- [six-family-color.amendment.v0.1.0.md](../../../../specs/components/six-family-color.amendment.v0.1.0.md) · SHA-256 `f569d5e132a0b5480f7b540dea8f157a601f27f24e86bb5ccb05b2d05f4b2cc9`.
- [button.typography.amendment.v0.1.0.md](../../../../specs/components/button.typography.amendment.v0.1.0.md) · SHA-256 `7bdede73c5ea2864ed61d4e74d5ec20c553ad29f158bf633dcc3e4b2d073607b`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
