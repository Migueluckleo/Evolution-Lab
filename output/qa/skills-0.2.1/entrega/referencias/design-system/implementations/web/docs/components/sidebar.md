# Sidebar · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `SIDEBAR-001` · API local 0.1.0 · categoría Composición.

## Uso sin backend

22 combinaciones documentadas de MenuItem; la unión SVG conserva paths fuente y las variantes usan roles locales verificados. Sidebar mide 72/234×885px por defecto; height es la dimensión del anfitrión (904px dentro de AppShell). Los items tipados alternan expanded/collapsed, conservan submenús ocultos y aceptan 0..n elementos. children y lowerOptions conservan contenido y requieren composición explícita del anfitrión. No se inventa un estado Disabled ni Focus de submenú.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function SidebarExample(){const [expanded,setExpanded]=useState(true);const [active,setActive]=useState('home');return <div className="grid gap-6"><label className="flex items-center gap-2"><input type="checkbox" checked={expanded} onChange={e=>setExpanded(e.target.checked)}/>Expanded</label><DS.Sidebar expanded={expanded} onExpandedChange={setExpanded} items={[{id:'home',label:'Home',active:active==='home',onClick:()=>setActive('home')},{id:'sub1',label:'Submenu 1',submenu:true,active:active==='sub1',onClick:()=>setActive('sub1')},{id:'sub2',label:'Submenu 2',submenu:true,active:active==='sub2',onClick:()=>setActive('sub2')},...Array.from({length:5},(_,i)=>({id:`menu-${i}`,label:`Menu item ${i+1}`,active:active===`menu-${i}`,onClick:()=>setActive(`menu-${i}`)}))]} lowerOptions={<><hr/><DS.MenuItem type={expanded?'expanded':'collapsed'} isActive={false} label="Help" lightIcon={<Question weight="light"/>} fillIcon={<Question weight="fill"/>} showRightIcon={false}/></>}/></div>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [sidebar.tsx](../../src/components/sidebar.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export type MenuItemVariant =
  | { orientation?: 'vertical'; type?: 'expanded'|'collapsed'; status?: 'default'|'hover'|'focus' }
  | { orientation?: 'vertical'; type: 'sub-menu'; status?: 'default'|'hover' }
  | { orientation: 'horizontal'; type?: 'collapsed'; status?: 'default'|'hover'|'focus' };

export type MenuItemProps = MenuItemVariant & {
  label?: string; isActive?: boolean; showRightIcon?: boolean;
  fillIcon?: ReactNode; lightIcon?: ReactNode; href?: string; onClick?: () => void;
  className?: string;
};

export interface SidebarItem { id:string; label:string; icon?:ReactNode; fillIcon?:ReactNode; lightIcon?:ReactNode; href?:string; active?:boolean; onClick?:()=>void; submenu?:boolean; showRightIcon?:boolean }

export interface SidebarProps { expanded?:boolean; onExpandedChange?:(expanded:boolean)=>void; items?:readonly SidebarItem[]; children?:ReactNode; lowerOptions?:ReactNode; label?:string; height?:CSSProperties['height']; className?:string }

export interface TopBarProps { items?:readonly Omit<SidebarItem,'submenu'>[]; children?:ReactNode; label?:string; width?:CSSProperties['width']; className?:string }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
Sidebar: {expanded=false,onExpandedChange,items=[],children,lowerOptions,label='Navegación principal',height=885,className}:SidebarProps
MenuItem: {orientation='vertical',type='collapsed',status,isActive=true,label='Home',showRightIcon=true,fillIcon=<HouseLine weight="fill"/>,lightIcon=<HouseLine weight="light"/>,href,onClick,className}:MenuItemProps
TopBar: {items=[],children,label='Navegación superior',width=1399,className}:TopBarProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **REQUIRED**. Sidebar items/children y lowerOptions; TopBar items/children, 0..n. MenuItem tiene anatomía fija: NOT_APPLICABLE. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [sidebar.contract.v0.1.0.md](../../../../specs/sidebar.contract.v0.1.0.md) · SHA-256 `6ddb3bb5e4166d5c53396d1b5f0bdac56e2bf431cce926050d818c726447cc8f`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
