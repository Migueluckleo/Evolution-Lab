---
contract_schema: sdd-project/0.2
contract_id: INPUT-FIELD-001
name: Input Field
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-28
review_targets: [figma]
figma_page_name: Input Fields
sources: [SRC-FIGMA-INPUT-FIELD-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.focus-effects.v0.1.0.json, drafts/contracts/input-field.source.component-contract.yaml]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-FOCUS-EFFECTS-001]
user_audit: PENDING
---

# Input Field 0.1.0 · contrato de construcción

## 1. Purpose
Captura visual de una línea de información. Página semántica: **Input Fields**, propuesta y adoptada bajo delegación para agrupar controles de captura. Esta entrega implementa únicamente Input Field; Search, Textarea y File Upload tienen inventario inicial y no se declaran construidos.

## 2. Contract
REQ-IF-001: reconstruir localmente el set de 30 variantes desde la evidencia fuente, sin importar ni desacoplar el componente legado. Conservar colores fuente; todas las pinturas, efectos y tipografía deben usar roles locales de scope correcto. Alcance Figma, no frontend.

## 3. Anatomy
Auto layout vertical: Label row (Question opcional, Label y Required); Control group (Surface con Text, Prefix y Trailing icon; Helper).
Question y Eye son instancias Phosphor Outline/Light. Focus conserva un rectángulo decorativo de soporte, absoluto detrás de Surface, con las mismas dimensiones y radio. Su fondo usa background/default y su efecto exterior spread=2 usa focus/effect-outer; no se usa un token de borde como fill. La superficie conserva los efectos particulares indicados en REQ-IF-007. No se añade una dependencia Tooltip funcional no demostrada.

## 4. Properties
REQ-IF-002: Size={Large,Medium,Small}; State={Default,Success,Error,Focus,Disabled}; Value={Empty,Filled}. autoFocus se elimina como eje redundante: Focus ya expresa el estado visual, no un comportamiento de navegador.

| Propiedad | Tipo | Default |
|---|---|---|
| Label | TEXT | Label |
| Text | TEXT | Placeholder text |
| Helper | TEXT | Optional helper text |
| Prefix | TEXT | MXN |
| Show label | BOOLEAN | true |
| Show text | BOOLEAN | true |
| Show helper | BOOLEAN | true |
| Required | BOOLEAN | true |
| Show help icon | BOOLEAN | false |
| Show trailing icon | BOOLEAN | true |
| Show prefix | BOOLEAN | false |
| Trailing icon | INSTANCE_SWAP | Eye Outline/Light |

No se amplía el conjunto de variantes por estas propiedades.

## 5. Variants
REQ-IF-003: exactamente 30 combinaciones de 3 tamaños × 5 estados × 2 valores. Defaults Large/Default/Empty. No añadir Hover o Readonly.

## 6. Sizes
REQ-IF-004: ancho inicial 464 px. Surface Large/Medium/Small: 48/40/32 px; altura total con etiqueta y helper: 96/88/80 px. Radios Surface 8 y Prefix 4; iconos 20×20. Padding horizontal 16; vertical Large 12, Medium/Small 8. Gap de etiqueta 8 y de helper 4. Mantener la altura fija del control y su alineación centrada aun cuando el padding vertical declarado sea mayor que el espacio libre.

## 7. States
REQ-IF-005: Default/Focus usan borde neutral; Success/Error usan sus roles de borde y helper. Disabled usa superficie sutil y texto de etiqueta/helper/icono deshabilitado. El valor Filled mantiene texto primary incluso en Disabled, como la fuente: no se recolorea por criterio propio. Required conserva danger/text.

## 8. Behavior
No añadir reacciones: la fuente tiene cero. Value es presentación Empty/Filled, no captura real de datos. No inferir lógica del Eye, validación automática o tooltip.

## 9. Accessibility
No declarar accesibilidad web implementada. Medir contraste real y registrar asteriscos sin recolorear. Borde normal #94A3B8/blanco y texto Disabled requieren revisión contextual. Etiqueta y helper deben seguir editables.

## 10. Design tokens
REQ-IF-006: JSON canónico `sources/inventories/tokens.inventory.json`, SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`; la extensión existente de foco gobierna sus dos roles. Esos JSON son la única autoridad de nombres, valores, aliases, modos, scopes y description. No hay nuevos tokens ni primitivas.

| Parte / estado | Rol destino | Variable local |
|---|---|---|
| Surface normal | color/background/default | VariableID:13:35 |
| Surface Disabled, diferenciación neutral sutil observada | color/background/subtle | VariableID:13:36 |
| Borde Default/Focus/Disabled | color/border/default | VariableID:13:13 |
| Borde Success / Error | color/feedback/positive/border / color/feedback/danger/border | VariableID:13:43 / VariableID:13:51 |
| Label y Filled | color/text/primary | VariableID:13:27 |
| Empty y Helper normal | color/text/tertiary | VariableID:13:29 |
| Label/Helper/Empty Disabled | color/text/disabled | VariableID:13:30 |
| Required y Helper Error | color/feedback/danger/text | VariableID:13:50 |
| Helper Success | color/feedback/positive/text | VariableID:13:42 |
| Prefix: fondo / texto | color/background/brand / color/text/secondary | VariableID:13:78 / VariableID:13:28 |
| Eye normal / Disabled | color/icon/primary / color/icon/disabled | VariableID:13:20 / VariableID:13:24 |
| Question | color/icon/brand | VariableID:13:25 |
| Efecto de foco exterior / interior | color/focus/effect-outer / color/focus/effect-inner | VariableID:136:122 / VariableID:136:123 |

Fondos solo FRAME_FILL/SHAPE_FILL; texto TEXT_FILL; iconos SHAPE_FILL; bordes STROKE_COLOR; efectos EFFECT_COLOR. No usar focus/ring en fills.

Tipografía: font/family/base; font/weight/bold en Label/Required y regular en Text/Prefix/Helper; font/size/sm=14 salvo Helper xs=12; line-height/sm=20 en Label/Required/Text y xs=16 en Prefix/Helper; letter-spacing/normal en todas. La normalización AUTO≈19→20 y tracking 0.1%→0 está explícita, con auditoría pendiente. Prefix Small pasa de interlineado 12 a 16 para evitar recorte, sin cambiar tamaño del control; el prefijo es oculto por defecto.

Espaciado: spacing/none,xs,sm,md,lg; radios radius/md y radius/sm; borde stroke/xs. Medidas globales 464 y alturas 48/40/32 se conservan como dimensiones observadas, no se enlazan a tokens GAP como si fueran WIDTH_HEIGHT.

REQ-IF-007: conservar la diferencia de foco fuente: Medium/Small Empty tienen efecto exterior spread=4 e interior spread=2; los otros Focus, spread=2 exterior. Todos sin blur ni desplazamiento. Además, cada Focus conserva el soporte decorativo con efecto exterior spread=2 observado en la fuente; sus dimensiones siguen a Surface al cambiar el ancho. La prueba de renderizado mostró que omitir este soporte hacía desaparecer el foco, aunque los efectos del frame se leyeran correctamente. La geometría de efectos es literal observada porque el inventario no define esa categoría de magnitudes. El halo interior aproxima #F8FAFC→#FFFFFF con la primitiva existente y el rol EFFECT_COLOR existente; se registra, no se presenta como igualdad exacta.

Los cuatro modos se heredan; no fijar Contable en variantes. Question sigue marca; Prefix sigue los aliases existentes de background/brand, sin modificar ese token compartido.

## 11. Content rules
Las cuatro cadenas editables no son valores de producto. La etiqueta debe conservar el asterisco independiente; no incrustarlo en Label. Helper puede crecer verticalmente al editar su contenido, mejora respecto al NONE de la fuente.

## 12. Composition rules
REQ-IF-008: una página Input Fields, documentación y set. Reutilizar iconos publicados, sin modificar sus definiciones. Eye histórico key e59dc310706bfe83ca2f09b69441d517c7372db1; Question puede obtenerse del set Phosphor actual 42f044d97a4523a55ce4e9a49a566c2fbc731e7d, seleccionando Outline/Light y registrando su key real. No duplicar principales locales ajenos.

## 13. Responsive behavior
Ancho inicial 464; Surface y Text deben ajustarse con auto layout al redimensionar la instancia. No se declaran breakpoints. Los contenidos muy extensos requieren revisión de producto; no hay garantía de longitud ilimitada.

## 14. Edge cases
Ocultar etiqueta/helper/prefix/icono debe conservar auto layout, sin huecos de capas ocultas. El estado Disabled no garantiza bloqueo de eventos porque esto es Figma.

## 15. Forbidden combinations
No exponer autoFocus separado de State. No convertir nombres de iconos en eje VARIANT. No importar colores de bibliotecas remotas ni usar primitivas directamente en paints.

## 16. Design ↔ Code mapping
size large/middle/small→Size Large/Medium/Small; status→State; value False/True→Value Empty/Filled. Resto son propiedades de composición. El componente de código y su API están fuera de alcance.

## 17. Acceptance criteria
- AC-IF-001: 30 variantes únicas, tres ejes y 12 propiedades de contenido; todos los bindings de propiedades conectados.
- AC-IF-002: 464×96/88/80 con defaults, Surface 48/40/32; radios, iconos y gaps verificables.
- AC-IF-003: pinturas y efectos semánticos locales del scope correcto, sin literals visibles ni primitivas directas.
- AC-IF-004: cinco bindings tipográficos en cada texto; aliases y valores de los cuatro modos coinciden con JSON.
- AC-IF-005: 60 instancias iconográficas conservadas; captura fuente/destino inspeccionada y pruebas de edición/visibilidad.
- AC-IF-006: documentación, fuente, QA, estado real e IDs trazables; solo promover a specs tras PASS técnico.

## 18. Examples
Large/Default/Empty muestra el caso inicial. Small/Disabled/Filled conserva texto primary y demuestra la diferencia entre contenido y disponibilidad. Medium/Focus/Empty conserva doble halo.

## 19. Source of truth
Este MD gobierna la construcción. Los JSON citados gobiernan variables. [Fuente MD](../drafts/contracts/input-field.source.component-contract.md), [YAML](../drafts/contracts/input-field.source.component-contract.yaml) y snapshots conservan observaciones históricas. El destino no modifica por sí mismo la especificación. [QA técnico](../qa/implementations/input-field.v0.1.0.figma.review.md) y [estado real](../implementations/figma/input-field.v0.1.0.state.json) registran la implementación; no redefinen sus reglas.

## 20. Change management
Estado inicial DRAFT; promoción a DELEGATED_FOR_BUILD solo tras QA documental. Auditoría humana PENDING por excepciones. Después de promoción, cambios normativos directamente en specs mediante versión/enmienda; publicación documental y biblioteca Figma son estados distintos.

## 21. Changelog
- 0.1.0, 2026-09-28: 30 variantes; ejes semánticos sin autoFocus redundante; tipografía local, foco con roles de efecto existentes y propiedades editables; Search/Textarea/File Upload fuera de esta entrega.
- Corrección previa a publicación: conservar seis soportes decorativos de foco tras detectar y aislar la diferencia en QA visual. Sin cambios de tokens, ejes, propiedades ni dimensiones.
- Publicación documental en specs tras QA técnico PASS. DELEGATED_FOR_BUILD y auditoría humana PENDING se conservan; biblioteca Figma UNPUBLISHED.
