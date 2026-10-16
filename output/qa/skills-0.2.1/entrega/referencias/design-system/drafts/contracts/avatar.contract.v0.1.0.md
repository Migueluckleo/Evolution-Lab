---
contract_schema: sdd-project/0.2
contract_id: AVATAR-001
name: Avatar
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Avatars
sources: [SRC-FIGMA-AVATAR-001, SRC-FIGMA-DOT-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/avatar.source.component-contract.yaml, drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-AVATAR-ROLES-001, DOT-001, SRC-FIGMA-PHOSPHOR-001]
user_audit: PENDING
---

# Avatar · contrato de reconstrucción 0.1.0

## 1. Purpose

Representación visual compacta de una persona o entidad mediante imagen, icono o iniciales, con indicador opcional de estado. La [fuente MD](avatar.source.component-contract.md) y [YAML](avatar.source.component-contract.yaml) documentan solo lo observado; el componente no autentica ni calcula identidad.

## 2. Contract

Crear página funcional `Avatars` y set `Avatar` en AI Design System. Conservar matriz 3×4, tamaños y composición visual. Usar variables locales del JSON aprobado y [extensión de Avatar](../foundations/ai-design-system.avatar-roles.v0.1.0.json); anidar el Dot ya construido y el icono User Phosphor real. No crear primitivas ni publicar biblioteca.

## 3. Anatomy

Cada variante tiene wrapper COMPONENT 20/24/32/48, cara circular del mismo tamaño y un Dot activo anidado en esquina inferior derecha. Image usa muestra raster exportada del frame fuente; Icon usa instancia Phosphor User; Text usa iniciales Manrope SemiBold. La foto es solo contenido de ejemplo, no imagen obligatoria de producto. El set expone Show status para visibilidad del Dot.

## 4. Properties

| Propiedad | Tipo | Default | Mapeo fuente |
|---|---|---|---|
| Type | VARIANT | Image | Image, Icon, Text |
| Size | VARIANT | Extra Large | small→Small, middle→Medium, large→Large, extra-large→Extra Large |
| Initials | TEXT | `JA` | `Content` de fuente; cuatro Text |
| Icon | INSTANCE_SWAP | User | `icon` de fuente; cuatro Icon |
| Show status | BOOLEAN | true | `show badge Indicator`; doce Dot |

El picker de Icon reutiliza las 1512 alternativas preferidas de Phosphor ya verificadas en Chips; no crea variantes ni dependencias activas adicionales. No hay propiedad de imagen genérica compatible con el set observado. La muestra Image se reemplaza directamente en el fill de la instancia cuando un producto tenga permiso sobre su asset; no se infiere carga automática ni fallback.

## 5. Variants

Matriz completa Type Image/Icon/Text × Size Small/Medium/Large/Extra Large = 12. Defaults Image/Extra Large. El estado del Dot no genera un tercer eje, porque la fuente solo muestra Active. No se duplican 1512 alternativas del picker Phosphor como variantes.

## 6. Sizes

Wrapper y cara: Small 20×20, Medium 24×24, Large 32×32, Extra Large 48×48. Medium, Large y Extra Large usan tokens `size/xl`, `size/2xl`, `size/4xl`. Small 20 queda geometría literal documentada porque la escala primitiva aprobada no contiene 20. Iconos 16/20/24/32 de fuente; 20 se documenta como excepción literal, los demás se tokenizan cuando encajan. Dot 5/8/12/16 de fuente; Small 5 es resize literal de instancia con el mismo componente, los demás usan sus tamaños ya definidos.

## 7. States

No hay estados de interacción. Show status controla visibilidad, no presencia real. El Dot anidado permanece visualmente Active como en la fuente; Busy/Inactive/Count/Overflow no son estados públicos de Avatar 0.1.0.

## 8. Behavior

Componente estático. Sin click, selección, carga de foto, iniciales automáticas, transición Image→Text ni presencia en tiempo real. La futura API de producto definirá `src`, fallback, status, nombre accesible y comportamiento de error por separado.

## 9. Accessibility

La cara de 20 px no es objetivo táctil validado. El consumidor debe proveer nombre accesible y texto de presencia cuando esta información sea esencial. Initials Small sube de 6 a 10 px y Medium de 9 a 12 px para legibilidad relativa; 10 px sigue siendo compacto y no certifica accesibilidad integral. Large 14 y Extra Large 20 se preservan. Los fondos de fallback con texto/icono blanco logran mínimo 4.72:1 en los cuatro modos tras el ajuste acotado de Servicios.

## 10. Design tokens

| Consumidor | Token y scope |
|---|---|
| Cara Icon/Text | `color/background/avatar-fallback`, `FRAME_FILL` |
| Borde de cara | `color/border/on-brand`, `STROKE_COLOR` |
| Vector de User | `color/icon/on-brand`, `SHAPE_FILL` |
| Initials | `color/text/on-brand`, `TEXT_FILL` |
| Initials familia/peso | `font/family/base`, `font/weight/semibold` |
| Initials tamaño | Small `font/size/avatar-small` 10, Medium `font/size/xs` 12, Large `font/size/sm` 14, Extra Large `font/size/lg` 20; todos `FONT_SIZE` |
| Cara geometría | `radius/full`, `stroke/xs`, size locales disponibles |
| Dot | tokens propios de DOT-001; no se sobrescriben con rol de icono |

La imagen es fill IMAGE, no color y no lleva variable cromática. Su muestra fuente 48×48 está conservada en [PNG codificado](../../sources/figma-snapshots/avatar-source-face-48.png.base64) para reproducibilidad. Las dos variables nuevas aliasan primitivas existentes en cuatro modos y se leen de vuelta antes de construir.

## 11. Content rules

`JA` y la fotografía fuente son muestras. No se deducen reglas de nombre, iniciales, privacidad, URL ni almacenamiento. El icono User es el fallback iconográfico observado y es intercambiable con un componente Phosphor de la misma biblioteca.

## 12. Composition rules

El Dot se anida como instancia, no se dibuja como copia. Su centro verde y borde blanco vienen del set `Dot` del destino. La posición inferior derecha sigue x/y fuente por tamaño; Show status no cambia el tamaño de la cara. Icono y texto se centran dentro de la cara sin clipping.

## 13. Responsive behavior

No hay breakpoints observados. Size es selección explícita; el componente no cambia automáticamente con viewport.

## 14. Edge cases

Iniciales largas podrían desbordar los círculos pequeños; el contrato cubre la muestra de dos caracteres y pide validación del consumidor. Si falta imagen real, el producto debe elegir explícitamente Icon o Text; el Figma no implementa fallback. Sin Show status, no se reserva espacio adicional para el Dot.

## 15. Forbidden combinations

Solo los 12 pares Type×Size. No crear estados Hover/Pressed/Disabled ni un eje de presencia no observado. No usar `color/interactive/*` para la cara no interactiva ni `color/text/*` para iconos o shapes.

## 16. Design ↔ Code mapping

Figma Type/Size/Initials/Icon/Show status son controles visuales. Una futura API web deberá definir assets, error fallback, estado real y accesibilidad; no se genera frontend ahora.

## 17. Acceptance criteria

| ID | Requisito verificable |
|---|---|
| AC-AVT-001 | Página `Avatars` única y set `Avatar` con 12 combinaciones; páginas previas intactas. |
| AC-AVT-002 | Tamaños 20/24/32/48, caras circulares y matriz/defaults correctos. |
| AC-AVT-003 | Dos variables nuevas JSON/Figma idénticas: scopes `FRAME_FILL`/`FONT_SIZE`, ocho aliases primitivos y readback anterior al consumo. |
| AC-AVT-004 | Fills/strokes/textos/iconos visibles usan categorías semánticas y scopes estrictos; sin RGB solid hardcoded salvo contenido IMAGE. |
| AC-AVT-005 | 12 Dot anidados, cuatro User Phosphor verdaderos, propiedades Show status/Initials/Icon conectadas y 1512 alternativas preferidas verificadas. |
| AC-AVT-006 | Imagen ejemplo fuente preservada, 4×3 visual comparado, textos 10/12/14/20 y diferencia Servicios naranja 600 documentados. |
| AC-AVT-007 | Contraste fallback blanco ≥4.5:1 en cuatro modos; límites de objetivo táctil, identidad y presencia registrados. |
| AC-AVT-008 | Cero reacciones nuevas, set `UNPUBLISHED`, auditoría humana pendiente; sin afirmación web. |

## 18. Examples

Initials `JA`, icono User y fotografía de origen ilustran la API visual. No son identidad ni contenido prescriptivo.

## 19. Source of truth

Markdown gobierna reglas; JSON de base y extensión gobiernan tokens. Set origen `1132:21344`, key `2df4b15820fade1cc23c83fde049c755286bfdc4`; IDs destino se registran tras creación. La fuente es evidencia, no autoridad para usar roles fuera de semántica.

## 20. Change management

Se renombra Size para consumo claro, se preserva matriz y se añade rol de fondo no interactivo. Se aumenta tipografía Small/Medium y se oscurece solo Servicios por contraste; cambios rastreados para auditoría. Cualquier comportamiento de identidad/estado requiere contrato de producto.

## 21. Changelog

- 0.1.0 delegado: reconstrucción 12 variantes con Dot reutilizado, Phosphor User, muestra fotográfica y dos roles semánticos nuevos.
