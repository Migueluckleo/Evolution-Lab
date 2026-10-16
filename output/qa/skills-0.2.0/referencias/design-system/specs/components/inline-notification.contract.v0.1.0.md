---
contract_schema: sdd-project/0.2
contract_id: INLINE-NOTIFICATION-001
name: Inline Notification
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Inline Notifications
sources: [SRC-FIGMA-INLINE-NOTIFICATION-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/inline-notification.source.component-contract.yaml, drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-WARNING-ICON-CONTRAST-001, FOUNDATIONS-FEEDBACK-ICON-SCOPES-001, SRC-FIGMA-PHOSPHOR-001]
user_audit: PENDING
---

# Inline Notification · contrato de reconstrucción 0.1.0

## 1. Purpose

Mensaje contextual dentro del flujo de una interfaz. La [fuente MD](../../drafts/contracts/inline-notification.source.component-contract.md) y [YAML](../../drafts/contracts/inline-notification.source.component-contract.yaml) describen lo observado en la Librería anterior. El componente de Figma representa apariencia, no entrega de mensajes ni anuncio accesible.

## 2. Contract

Crear página `Inline Notifications` y set `Inline Notification` en AI Design System. Preservar cinco tratamientos visuales y composición, con variables locales semánticas del JSON aprobado. No crear tokens ni primitivas adicionales. Mantener el set sin publicar y pendiente de auditoría humana.

## 3. Anatomy

Cada variante contiene superficie horizontal con icono de estado 24, columna de título/descripción y un icono Close de 16 al extremo superior. Padding vertical 16 y horizontal 24, gap principal 16, gap de texto 4, radio 8. El contenedor es auto layout y se adapta al texto sin superposiciones.

## 4. Properties

| Propiedad | Tipo | Default | Evidencia/decisión |
|---|---|---|---|
| Type | VARIANT | Light | Light, Success, Danger, Warning, Info, mapeo uno a uno de `type` fuente |
| Title | TEXT | `Título` | normaliza la muestra fuente `Tittle` sin cambiar el eje |
| Description | TEXT | texto de ejemplo neutro en dos líneas | conserva la edición de contenido sin simular enlace |
| Show title | BOOLEAN | true | visibilidad de título fuente |
| Show description | BOOLEAN | true | visibilidad de descripción fuente |
| Show icon | BOOLEAN | true | visibilidad de icono principal fuente |
| Show dismiss | BOOLEAN | true | visibilidad de Close fuente, solo visual |

Los seis iconos activos se conservan como instancias Phosphor. No se expone INSTANCE_SWAP: la fuente no lo tiene y sustituir un icono de severidad podría romper su semántica.

## 5. Variants

Una variante por Type: Light, Success, Danger, Warning, Info. No se generan combinaciones adicionales de estado. Default Light.

## 6. Sizes

Anchura de referencia 602 px. Altura base de destino 108 px, cuatro más que la fuente de 104, para alojar título de 24 px y descripción de dos líneas con interlineado semántico de 24 px, gap 4 y padding vertical 16. Width 602 es geometría observada literal sin token de categoría compatible. Iconos 24/16 ligados a `size/xl`/`size/lg`.

## 7. States

Type es tratamiento semántico visual y no estado interactivo. No añadir Hover, Pressed, Focus ni Disabled. Show dismiss no significa dismissed.

## 8. Behavior

No hay prototipado de cierre, persistencia, duración ni prioridad. El contrato de Figma no define acción del botón, live region ni navegación. Un producto debe especificarlos antes de implementación web.

## 9. Accessibility

El texto mantiene contraste mayor a 6:1 en los fondos de estado observados. Los iconos de estado tienen al menos 3:1; Warning usa la corrección aprobada de alias ámbar 700, aproximadamente 4.38:1 frente a su fondo. Close de 16 px no es un objetivo táctil suficiente por sí solo. Si se vuelve funcional, su implementación necesitará nombre accesible, target ampliado y control por teclado. No se certifica WCAG integral ni semántica de alerta.

## 10. Design tokens

| Consumidor | Rol destino y scope obligatorio |
|---|---|
| Superficie Light | `color/background/default`, `FRAME_FILL` |
| Superficies Success/Danger/Warning/Info | `color/feedback/positive/bg`, `danger/bg`, `warning/bg`, `information/bg`, todos `FRAME_FILL` |
| Icono Light y Close | `color/icon/primary`, `SHAPE_FILL` |
| Iconos Success/Danger/Warning/Info | `color/feedback/positive/icon`, `danger/icon`, `warning/icon`, `information/icon`, todos `SHAPE_FILL` |
| Título | `color/text/primary`, `TEXT_FILL`; `font/family/base`, `font/weight/regular`, `font/size/md`, `font/line-height/md` |
| Descripción | `color/text/secondary`, `TEXT_FILL`; `font/family/base`, `font/weight/regular`, `font/size/sm`, `font/line-height/md` |
| Composición | `spacing/lg` 16, `spacing/xl` 24, `spacing/xs` 4, `radius/md` 8, `size/xl` 24 y `size/lg` 16 |

La fuente aprobada es `sources/inventories/tokens.inventory.json` SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`. La enmienda [Warning Icon Contrast](../../drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.0.json) gobierna solo el alias de ese rol en el destino; la [enmienda de scopes](../foundations/foundations.feedback-icon-scopes.amendment.v0.1.7.md) limita los tres iconos de feedback corregidos a `SHAPE_FILL`. Bindings reales, nunca colores pegados.

## 11. Content rules

`Título` y la descripción son muestras editables, no copy de producto. El segmento azul subrayado de la fuente tiene `hyperlink=null`, de modo que no se traslada como enlace aparente. Un enlace real requeriría URL, acción y un contrato específico.

## 12. Composition rules

Las seis instancias Phosphor permanecen anidadas, sin detach. La columna de texto crece verticalmente; el icono principal y Close quedan alineados arriba. Ocultar título, descripción o iconos usa propiedades de componente y el auto layout recompone el espacio.

## 13. Responsive behavior

No hay breakpoints observados. El ancho 602 es referencia de catálogo; el contrato no prescribe reflujo móvil. La futura implementación debe probar anchuras de producto.

## 14. Edge cases

Texto largo puede aumentar la altura y requiere revisión del consumidor. Si Show title y Show description son falsos, un mensaje sin contenido queda fuera de uso recomendado, aunque Figma pueda representarlo. Show icon y Show dismiss pueden apagarse independientemente.

## 15. Forbidden combinations

No añadir severidades, estados interactivos o enlaces ficticios. No usar `color/text/*` en vectores, `color/icon/*` en texto, ni `color/feedback/*/bg` en texto. No confundir el icono Close con una interacción funcional.

## 16. Design ↔ Code mapping

Type, Title, Description y cuatro booleanas son controles de diseño. Una futura API de producto definirá severidad, rol ARIA, anuncio, acción dismiss, persistencia y contenido; no se genera frontend en esta fase.

## 17. Acceptance criteria

| ID | Requisito verificable |
|---|---|
| AC-INL-001 | Página única `Inline Notifications`, set `Inline Notification`, cinco variantes y default Light. |
| AC-INL-002 | Anatomía, iconos Phosphor y propiedades TEXT/BOOLEAN conectadas; sin detach. |
| AC-INL-003 | Padding 16/24, gaps 16/4, radio 8 e iconos 24/16 con variables locales; ancho 602, altura base 108 documentada. |
| AC-INL-004 | Todos los paints visibles usan categoría y scope semánticos correctos; cero RGB solid hardcoded. |
| AC-INL-005 | Warning icon usa alias ámbar 700 verificado y contraste ≥3:1; textos ≥4.5:1. |
| AC-INL-006 | Copy normalizado y ningún enlace azul subrayado sin destino. |
| AC-INL-007 | Captura comparada con fuente; cinco variantes distinguibles, sin recorte o superposición. |
| AC-INL-008 | Cero reacciones añadidas, biblioteca `UNPUBLISHED`, auditoría humana pendiente; sin afirmar comportamiento web. |

## 18. Examples

La rejilla mostrará cinco tipos con título y descripción de ejemplo. La muestra no determina mensajes de producción ni severidades de negocio.

## 19. Source of truth

Este Markdown gobierna reglas de reconstrucción; JSON base y enmiendas gobiernan variables. Set fuente `2778:10287`, key `55b0bfd8fb39f8b1d16eee72f95a1b44481062ec`. Los IDs de destino se registran después de crear. La fuente es evidencia, no permiso para heredar bindings fuera de scope.

## 20. Change management

Se preservan cinco tipos y tratamiento cromático; se normaliza `Tittle`, se elimina la apariencia de link sin URL y se corrige Light/Close de `text` a `icon`. Warning icon consume el alias contrastado ya registrado. La altura base crece 4 px por el token de interlineado. Todo queda sujeto a auditoría humana.

## 21. Changelog

- 0.1.0 delegado: cinco variantes visuales, seis iconos Phosphor únicos activos en el set, roles estrictamente semánticos y propiedades de contenido/visibilidad.
