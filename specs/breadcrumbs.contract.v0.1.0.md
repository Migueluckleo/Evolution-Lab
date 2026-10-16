---
contract_schema: sdd-project/0.2
contract_id: BREADCRUMBS-001
name: Breadcrumbs
type: component_family
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Breadcrumbs
sources: [SRC-FIGMA-BREADCRUMB-ITEM-001, SRC-FIGMA-BREADCRUMBS-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.breadcrumb-current-text.v0.1.0.json, drafts/contracts/breadcrumb-item.source.component-contract.yaml, drafts/contracts/breadcrumbs.source.component-contract.yaml]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-BREADCRUMB-CURRENT-TEXT-001, SRC-FIGMA-PHOSPHOR-001]
user_audit: PENDING
---

# Breadcrumbs · contrato de reconstrucción 0.1.0

> Vigencia cromática: la [enmienda SIX-FAMILY-COLOR-001](components/six-family-color.amendment.v0.1.0.md) sustituye exclusivamente las recetas/umbrales allí identificados. Publicación documental 2026-10-05; auditoría humana PENDING. Los apartados históricos se leen junto con esa enmienda.

## 1. Purpose

Representar una ruta jerárquica mediante ítems reutilizables y cuatro ejemplos de longitud. La [evidencia del ítem](../drafts/contracts/breadcrumb-item.source.component-contract.md) y la [composición fuente](../drafts/contracts/breadcrumbs.source.component-contract.md) son observaciones; este contrato decide su reconstrucción en AI Design System. Figma no implementa destinos de navegación.

## 2. Contract

Crear página exclusiva `Breadcrumbs` con dos sets principales de la misma familia: `Breadcrumb item` y `Breadcrumbs`. El primero contiene seis variantes observadas y el segundo cuatro niveles compuestos mediante instancias locales del primero. Usar variables semánticas locales del JSON aprobado y la [extensión de texto Current](../drafts/foundations/ai-design-system.breadcrumb-current-text.v0.1.0.json), con alias a primitivas existentes. Mantener ambos sets `UNPUBLISHED` hasta auditoría.

## 3. Anatomy

`Breadcrumb item`: texto o icono House; CaretRight cuando corresponde. `Breadcrumbs`: ArrowLeft de 24 px, gap 8, frame de ítems, gap 4, 2–5 instancias de `Breadcrumb item`; el último ítem es Current. House, CaretRight y ArrowLeft son instancias Phosphor, sin detach ni vectores duplicados como componentes principales.

## 4. Properties

| Set | Propiedad | Tipo | Default | Mapeo fuente |
|---|---|---|---|---|
| Breadcrumb item | State | VARIANT | Default | default, Shortened, Disabled, Hover, Icon |
| Breadcrumb item | Current | VARIANT | false | `active=off/on` |
| Breadcrumb item | Label | TEXT | Breadcrumb | `text` para los cuatro ítems textuales no acortados; Shortened conserva `...` como muestra fija |
| Breadcrumbs | Level | VARIANT | 2 | `type=Level 2/3/4/5` |

El set `Breadcrumbs` no promete propiedades de texto a nivel padre que la fuente no exponía; las etiquetas se editan en sus instancias internas. No convertir la presencia de icono en un eje adicional.

## 5. Variants

`Breadcrumb item`: Default/false, Icon/false, Shortened/false, Disabled/false, Default/true y Hover/false. `Breadcrumbs`: Level 2, 3, 4 y 5. Solo diez componentes en total. No generar producto cartesiano State×Current: la fuente no muestra cuatro combinaciones restantes.

## 6. Sizes

Ítems destino: Default 120×24; Icon 52×24; Shortened 42×24; Disabled 120×24; Current 92×24; Hover 92×24. El texto `Breadcrumb` se autoajusta a su ancho natural leído de 91 px bajo la tipografía local; las cajas redondeadas a 92 px evitan clipping. Composiciones destino: 248/372/496/620×24, ArrowLeft24 y separadores según la variante de ítem. El set catálogo mantiene 650×296 y las cuatro filas de origen. Gap interior `spacing/xs`=4 y exterior `spacing/sm`=8; House y todos los CaretRight usan `size/xl`=24. La fuente tenía ítems textuales de 88 px y composiciones 242/362/482/602 px, además House y caret Disabled/Icon en 20 px y cajas Icon 44×20, Disabled 112×24. Preflight confirmó que el JSON/Figma destino carecen de primitiva y token semántico de dimensión 20 px; el cambio a 24 px evita un literal sin binding. Los anchos de contenido se amplían solo lo necesario para no cortar etiquetas y conservar la escala tipográfica local. Estas desviaciones visuales concretas quedan para auditoría.

## 7. States

Default es ruta anterior; Current es el último segmento y no muestra CaretRight. Disabled atenúa texto e icono. Hover muestra solo texto fuerte, sin caret como en la fuente. Shortened muestra `...` con caret. Icon muestra House y caret. Los nombres de estado no prueban navegación, hover real ni bloqueo de eventos.

## 8. Behavior

Los cuatro niveles son muestras estáticas. No hay reacciones. El producto debe definir enlaces, destinos, actualización dinámica, retroceso y truncamiento; Figma solo representa apariencia.

## 9. Accessibility

El consumidor debe definir semántica de navegación, lista ordenada o equivalente y señal de página actual, además de nombre accesible para el ítem Icon, foco y alcance táctil. No certificar teclado, `aria-current` o WCAG desde Figma. Si el texto Disabled sigue en la ruta real, producto debe definir su significado; no se infiere de la muestra.

## 10. Design tokens

El inventario aprobado tiene SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`; sus aliases/valores/descripciones gobiernan. Mapa por rol (IDs locales destino se confirman en preflight y estado de implementación):

| Parte | Variable semántica destino | Scope |
|---|---|---|
| Texto Default/Shortened | `color/text/tertiary` | `TEXT_FILL` |
| Texto Disabled | `color/text/disabled` | `TEXT_FILL` |
| Texto Current | `color/text/breadcrumb/current` de la extensión 0.1.0 | `TEXT_FILL` |
| Texto Hover | `color/text/brand/strong` | `TEXT_FILL` |
| House | `color/icon/brand` | `SHAPE_FILL` |
| CaretRight Default/Icon/Shortened | `color/icon/secondary` | `SHAPE_FILL` |
| CaretRight Disabled | `color/icon/tertiary` | `SHAPE_FILL` |
| ArrowLeft | `color/icon/primary` | `SHAPE_FILL` |
| Texto | `font/family/base`, `font/weight/regular` o `font/weight/semibold`, `font/size/md`, `font/line-height/md`, `font/letter-spacing/tight` | `FONT_FAMILY`, `FONT_STYLE`, `FONT_SIZE`, `LINE_HEIGHT`, `LETTER_SPACING` |
| Layout | `spacing/xs`, `spacing/sm`, `size/xl` | `GAP`, `WIDTH_HEIGHT` |

La fuente usa tracking −2%; `font/letter-spacing/tight` aprobado contiene el valor −0.01 sin unidad semántica demostrada para web. En Figma se enlaza la variable local y se registra la diferencia de render, sin convertir el valor a porcentaje ni afirmar equivalencia numérica. El nuevo rol Current conserva el acento de marca en tres modos y pasa orange/500→orange/700 en Servicios para alcanzar 7.20:1 sobre blanco. Los fills blancos ocultos de wrapper Phosphor no se consideran pinturas visibles consumidoras. Ningún rol de texto se aplica a vector o shape.

## 11. Content rules

`Breadcrumb`, `...` y House son ejemplos. `Label` edita las etiquetas textuales normales del ítem; `...` representa acortamiento visual, no algoritmo de truncamiento. No inventar nombres de niveles ni rutas reales.

## 12. Composition rules

Construir primero `Breadcrumb item` y usar sus instancias en `Breadcrumbs`; 2, 3, 4 y 5 ítems por nivel. Los previos son Default/false y el último Default/true. Los CaretRight pertenecen a los ítems previos. ArrowLeft es una instancia por composición. Mantener definiciones principales de iconos en su biblioteca Phosphor y las de ítem en esta página, sin detach.

## 13. Responsive behavior

No se observa breakpoint ni regla de colapso automático. Level es una elección explícita de variante. Si se necesita longitud dinámica o responsive, se define fuera de esta reconstrucción estática.

## 14. Edge cases

No hay variante de un solo nivel ni más de cinco; no se extrapolan. Etiquetas largas pueden alterar ancho de ejemplo; el producto debe decidir truncamiento y contenedor. Icon no tiene etiqueta visible; accesibilidad requiere nombre. Hover carece de caret en fuente; se conserva, aunque difiera de Default.

## 15. Forbidden combinations

No crear las cuatro combinaciones State×Current no observadas. No usar Inter remoto ni un estilo externo para las etiquetas activas del destino; se corrige la inconsistencia de la composición fuente usando Manrope local. No ligar tokens text a iconos ni tokens icon a textos. No usar `color/text/brand` en Current del modo Servicios porque solo alcanza 3.24:1. No duplicar `Breadcrumb item` como frames planos en el set compuesto.

## 16. Design ↔ Code mapping

Figma `State`/`Current`/`Level`/`Label` son controles visuales. Una API web futura debe definir segmentos/destinos, enlace, página actual, responsive, longitud arbitraria y semántica de navegación. No se genera código ahora.

## 17. Acceptance criteria

| ID | Requisito verificable |
|---|---|
| AC-BRC-001 | Página única `Breadcrumbs`, dos sets y diez variantes observadas, defaults correctos. |
| AC-BRC-002 | Seis ítems con contenido completo de una línea, caret/House y colores de estado de fuente; House y caret pequeños se normalizan 20→24 px, etiquetas de 88→92 px y cajas derivadas ajustadas. |
| AC-BRC-003 | Cuatro niveles de 248/372/496/620 px con 2–5 instancias locales reales, un ArrowLeft por nivel y el último Current; catálogo 650×296 sin clipping. |
| AC-BRC-004 | Todas las pinturas sólidas visibles ligadas a variable local de scope y categoría semántica correctos; cinco textos Current usan el rol nuevo `TEXT_FILL`, con cuatro aliases JSON/Figma verificados y contraste ≥4.5:1. |
| AC-BRC-005 | Texto vinculado a familia, peso, tamaño, line-height y tracking semánticos locales; desviación Inter y tracking documentada. |
| AC-BRC-006 | Gaps y tamaños de icono 24 px tokenizados con variables semánticas; cero dimensiones 20 px sin binding en el destino. |
| AC-BRC-007 | Comparación visual con captura fuente, cero reacciones y sets `UNPUBLISHED`; auditoría humana pendiente. |

## 18. Examples

Level 2 muestra una ruta de dos segmentos; Level 5, una de cinco. Son demostraciones estáticas de densidad, no reglas de rutas.

## 19. Source of truth

Este Markdown gobierna reglas; el JSON aprobado y la extensión de texto Current gobiernan tokens. [YAML de ítem](../drafts/contracts/breadcrumb-item.source.component-contract.yaml) y [YAML de composición](../drafts/contracts/breadcrumbs.source.component-contract.yaml) conservan la evidencia; el set fuente del ítem es `2425:35897` y el compuesto `2425:35937`. Los IDs de destino se registrarán aparte. La descripción de la página fuente es contexto, no texto copiado al destino.

## 20. Change management

Se normalizan nombres de ejes, se elige Manrope semántico para las cuatro etiquetas activas de ejemplo, se adopta tracking tight local, se uniforman a 24 px los iconos de las variantes Icon/Disabled que medían 20 px sin token de dimensión y se amplían cajas de texto/composición lo mínimo necesario tras constatar clipping en la captura inicial. La auditoría de contraste añadió un rol Current exclusivo de texto que cambia solo Servicios a orange/700. Estas diferencias quedan sujetas a auditoría humana posterior. No modificar el Figma fuente ni inventario histórico.

## 21. Changelog

- 0.1.0 delegado: familia de dos sets, seis ítems y cuatro composiciones, tokens existentes y diferencias tipográficas explícitas.
