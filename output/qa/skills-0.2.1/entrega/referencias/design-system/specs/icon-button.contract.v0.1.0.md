---
contract_schema: sdd-project/0.2
contract_id: ICON-BUTTON-001
name: Icon Button
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Icon Buttons
sources: [SRC-FIGMA-ICON-BUTTON-001, SRC-FIGMA-DOT-001, SRC-FIGMA-PHOSPHOR-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/icon-button.source.component-contract.yaml, drafts/foundations/ai-design-system.icon-button-backgrounds.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-ICON-BUTTON-BACKGROUNDS-001, DOT-001, SRC-FIGMA-PHOSPHOR-001]
user_audit: PENDING
---

# Icon Button · contrato de reconstrucción 0.1.0

> Vigencia cromática: la [enmienda SIX-FAMILY-COLOR-001](components/six-family-color.amendment.v0.1.0.md) sustituye exclusivamente las recetas/umbrales allí identificados. Publicación documental 2026-10-05; auditoría humana PENDING. Los apartados históricos se leen junto con esa enmienda.

## 1. Purpose

Acción iconográfica compacta con un indicador numérico opcional. La [fuente MD](../drafts/contracts/icon-button.source.component-contract.md) y [YAML](../drafts/contracts/icon-button.source.component-contract.yaml) documentan lo observado; el Figma destino no implementa ejecución de acción ni cálculo del conteo.

## 2. Contract

Crear página exclusiva `Icon Buttons` y set `Icon Button` en AI Design System. Conservar 30 combinaciones, medidas, icono Bell y Dot Count anidado, usando roles locales estrictamente semánticos. Dos nuevos fondos de estado definidos en [JSON de extensión](../drafts/foundations/ai-design-system.icon-button-backgrounds.v0.1.0.json) deben existir y leerse de vuelta antes de construir. No publicar biblioteca.

## 3. Anatomy

Cada variante tiene un cuerpo cuadrado con radio 8, instancia Bell Phosphor centrada y una instancia Count del Dot local superpuesta en cuadrante inferior derecho. El Bell es icono intercambiable; el Dot puede ocultarse sin alterar el cuerpo. No se dibujan copias del Dot ni se hace detach.

## 4. Properties

| Propiedad | Tipo | Default | Mapeo fuente |
|---|---|---|---|
| Style | VARIANT | Ghost | `type=default`→Ghost, `outline`→Outline |
| Size | VARIANT | Small | `small`→Small, `middle`→Medium, `large`→Large |
| State | VARIANT | Default | Default, Disabled, Hover, Focus, Active |
| Icon | INSTANCE_SWAP | Bell Outline/Light | `icon` activo, 1512 component sets Phosphor preferidos |
| Show count | BOOLEAN | true | `show badge indicator` |

La disponibilidad de 1512 iconos en el picker no crea variantes ni dependencias activas. El texto Count=`1` permanece editable dentro de Dot; no se promete una propiedad de número en el set padre que Figma no pueda conectar de forma verificable.

## 5. Variants

Matriz completa Style Ghost/Outline × Size Small/Medium/Large × State Default/Disabled/Hover/Focus/Active = 30. Defaults Ghost/Small/Default. No eje adicional de conteo ni de icono.

## 6. Sizes

Small 24×24 con Bell16 y Dot8, padding4; Medium 48×48 con Bell24 y Dot12, padding8; Large 56×56 con Bell32 y Dot16, padding8. Usar `size/xl`, `size/4xl`, `size/5xl` para cuerpos; `size/lg`, `size/xl`, `size/2xl` para Bell, `spacing/xs`/`spacing/sm` para padding y `radius/md`. Posiciones del Dot copiadas de la fuente: Small (12,12), Medium (24,18), Large (28,20).

## 7. States

Default Ghost transparente/sin borde; Outline transparente con borde sutil. Disabled Ghost transparente y Bell atenuado; Outline con fondo y borde disabled. Hover en ambos estilos usa fondo pálido interactivo; Outline añade borde hover. Focus usa fondo neutral, borde focus; se aplica de forma consistente a los seis Focus sin copiar el efecto extra aislado de la fuente. Active usa fondo de marca y Bell on-brand; Outline mantiene borde sutil. El Dot Count rojo permanece visible salvo Show count=false, también en Disabled, como información visual separada de la disponibilidad de acción.

## 8. Behavior

Los estados son representaciones de diseño, no transiciones prototipadas. Active no es selección persistente ni carga. Disabled indica una acción no disponible, pero la notificación anidada puede seguir mostrando un conteo. El producto define click, atajos, cambios de estado, conteo y vaciado de notificaciones.

## 9. Accessibility

Cada uso requiere nombre accesible independiente del icono y descripción del conteo cuando sea información relevante. Small de 24 px no se certifica como objetivo táctil; debe existir área interactiva mayor en producto o elegirse tamaño superior. El Count Small conserva tipografía de 4 px del Dot reutilizado y no debe ser la única vía de comunicar un número. La señal Focus tiene borde semántico en todos los tamaños/estilos; no se atribuye navegación por teclado al Figma.

## 10. Design tokens

| Consumidor | Rol y scope |
|---|---|
| Hover body Ghost/Outline | `color/interactive/icon-button/hover-bg`, `FRAME_FILL`, aliases blue/green/orange/purple 100 |
| Active body Ghost/Outline | `color/interactive/icon-button/active-bg`, `FRAME_FILL`, aliases blue400/green500/orange500/purple500 |
| Disabled Outline body | `color/interactive/disabled/bg`, `FRAME_FILL` |
| Focus body | `color/background/default`, `FRAME_FILL` |
| Outline Default/Active border | `color/border/subtle`, `STROKE_COLOR` |
| Outline Disabled/Hover border | `color/border/disabled` / `color/border/hover`, `STROKE_COLOR` |
| Focus border | `color/focus/ring`, `STROKE_COLOR` |
| Bell Default/Hover/Focus, Disabled, Active | `color/icon/primary`, `color/icon/disabled`, `color/icon/on-brand`, `SHAPE_FILL` |
| Dot Count | sus tokens propios de DOT-001: fondo `color/background/notification-count`, borde `color/border/on-brand`, texto `color/text/on-brand` |
| Estructura | `spacing/xs`, `spacing/sm`, `radius/md`, `stroke/xs` y escala `size/*` indicada |

El inventario aprobado de referencia tiene SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`. No usar `color/feedback/danger/icon` como fondo del Dot, ni tokens de texto en iconos o shapes. La extensión no modifica primitivas.

## 11. Content rules

Bell y el número `1` son muestras. El consumidor puede cambiar Icon mediante picker. La regla de cómo se calcula o formatea el conteo, incluida la ocultación de cero y el overflow, no se define aquí.

## 12. Composition rules

Bell y Dot se superponen intencionalmente; por ello el cuerpo puede usar coordenadas internas explícitas en vez de auto layout lineal. Las definiciones de Dot permanecen en su página; Icon Buttons contiene 30 instancias Count, una por variante. Show count se conecta a la visibilidad de esas instancias.

## 13. Responsive behavior

No hay breakpoint observado. Size es selección explícita. El componente no cambia de tamaño según viewport o densidad.

## 14. Edge cases

Un icono sustituto con geometría distinta debe mantener caja 16/24/32 y contraste del rol correspondiente. Conteos largos podrían desbordar el Dot; el umbral no se inventa. Si Show count=false, Bell conserva su posición. Disabled con conteo visible es permitido visualmente, pero el producto debe asegurar que el número no parezca una acción disponible.

## 15. Forbidden combinations

No crear estilos, tamaños o estados fuera de la matriz 2×3×5. No usar Active como token de Hover ni Default como token de Active aunque coincidan cromáticamente. No copiar el efecto `focus/outset` solo a Large/Ghost, porque dejaría cinco Focus inconsistentes. No hacer detach de Bell o Dot.

## 16. Design ↔ Code mapping

Figma Style/Size/State/Icon/Show count son controles visuales. Una futura API web necesita definir `aria-label`, acción, disabled nativo, focus-visible, count, announcement e hit target; no se genera código de aplicación ahora.

## 17. Acceptance criteria

| ID | Requisito verificable |
|---|---|
| AC-ICB-001 | Página `Icon Buttons` única y set `Icon Button` con 30 combinaciones y defaults correctos. |
| AC-ICB-002 | Geometrías 24/48/56, iconos 16/24/32, Dot Count 8/12/16 y posiciones fuente. |
| AC-ICB-003 | 30 Bell Phosphor y 30 Dot Count anidados sin detach; Icon INSTANCE_SWAP y Show count BOOLEAN conectados. |
| AC-ICB-004 | Dos variables nuevas JSON/Figma con scope `FRAME_FILL`, cuatro aliases primitivos cada una y readback antes de consumo. |
| AC-ICB-005 | Todos los paints visibles tienen binding, scope y categoría semántica correctos; Focus uniforme con borde, sin efecto aislado. |
| AC-ICB-006 | Tamaño, padding, radio y stroke enlazados a variables locales cuando corresponden; matriz visual comparada con fuente. |
| AC-ICB-007 | 1512 preferencias Phosphor verificadas en el picker; no añadidas como variantes. |
| AC-ICB-008 | Cero reacciones nuevas, set `UNPUBLISHED`; límites de accesibilidad y auditoría humana pendiente registrados. |

## 18. Examples

Bell con Dot Count=`1` demuestra la representación. No especifica catálogo de acciones ni política de notificaciones.

## 19. Source of truth

Este Markdown gobierna reglas; JSON base y extensión gobiernan tokens. Set fuente `1430:18850`, key `fbc267a15caab7547a5d782a8887da547ee7cf03`; IDs destino se registran tras creación. La fuente es evidencia, no autoridad para propagar anomalías de scope.

## 20. Change management

Se renombran ejes para consumo claro y se preservan 30 combinaciones. Dos roles nuevos alinean estados y valores sin nuevas primitivas. Dot Count del destino corrige rol de fondo; Focus elimina solo el efecto inconsistente de una variante y mantiene el borde en seis. Cualquier comportamiento de producto requiere contrato aparte.

## 21. Changelog

- 0.1.0 delegado: Icon Button 2×3×5 con Bell intercambiable, Dot Count opcional y dos fondos de estado semánticos nuevos.
