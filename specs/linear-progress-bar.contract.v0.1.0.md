---
contract_schema: sdd-project/0.2
contract_id: LINEAR-PROGRESS-BAR-001
name: Linear Progress Bars
type: component_family
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Linear Progress Bars
sources: [SRC-FIGMA-LINEAR-PROGRESS-BAR-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.linear-progress-colors.v0.1.0.json, drafts/contracts/linear-progress-bar.source.component-contract.yaml]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-LINEAR-PROGRESS-COLORS-001]
user_audit: PENDING
---

# Linear Progress Bars · contrato de reconstrucción 0.1.0

> Vigencia cromática: la [enmienda SIX-FAMILY-COLOR-001](components/six-family-color.amendment.v0.1.0.md) sustituye exclusivamente las recetas/umbrales allí identificados. Publicación documental 2026-10-05; auditoría humana PENDING. Los apartados históricos se leen junto con esa enmienda.

## 1. Purpose

Mostrar una fracción de progreso lineal con etiqueta, porcentaje y ayuda opcional en cuatro tonos y tres tamaños. El [contrato fuente](../drafts/contracts/linear-progress-bar.source.component-contract.md) respalda estructura y geometría; no define cálculo, animación o semántica de datos.

## 2. Contract

Crear página exclusiva `Linear Progress Bars` en AI Design System y un set `Linear Progress Bar` de 48 variantes, exactamente Type primary/warning/positive/danger × Size Small/Medium/Large × Progress 25/50/75/100%. Mantenerlo `UNPUBLISHED` y vincular todos los colores y tipografías a variables locales. El [JSON de extensión](../drafts/foundations/ai-design-system.linear-progress-colors.v0.1.0.json) gobierna los cinco roles de fondo.

## 3. Anatomy

Componente vertical: fila Label + Percentage, pista redondeada con segmento de avance redondeado y helper text. No hay iconos, instancias anidadas ni adornos. El porcentaje visible debe ser el mismo valor que el eje Progress y la fracción de anchura.

## 4. Properties

| Propiedad destino | Tipo | Default | Regla |
|---|---|---|---|
| Type | VARIANT | Primary | Primary/Warning/Positive/Danger, función de tono visual. |
| Size | VARIANT | Small | Small/Medium/Large; fuente small/middle/large. |
| Progress | VARIANT | 25% | 25/50/75/100%; controla simultáneamente relleno y texto visible. |
| Label | TEXT | Label | Título editable, ligado en 48 variantes. |
| Helper text | TEXT | Optional helper text | Ayuda editable, ligada en 48 variantes. |
| Show label | BOOLEAN | true | Controla la fila completa tal como fuente. |
| Show percentage | BOOLEAN | true | Oculta solo el texto de porcentaje. |
| Show helper text | BOOLEAN | true | Oculta solo helper. |

Se elimina el TEXT libre `✏️ Percentage` de la fuente: allí las 36 variantes 50/75/100% muestran `25%` por default compartido. No exponer dos fuentes editables del mismo valor. El usuario puede seleccionar cualquiera de las cuatro variantes consistentes; valores arbitrarios requieren otro contrato.

## 5. Variants

Matriz completa de 48 combinaciones; no crear Loading, Hover, Disabled ni valores adicionales. El set fuente contiene las 48, por lo que no se completan cruces inexistentes.

## 6. Sizes

Ancho 246 px. Small 246×44 con barra 4 px; Medium 246×52 con barra 8 px; Large 246×56 con barra 12 px. La fuente Middle/Large mide 51/55 px, pero el interlineado semántico de 20 px para el texto de 14 px requiere +1 px. Small conserva 44 px. Segmento de avance 61.5/123/184.5/246 px para 25/50/75/100%; pista siempre 246 px. Radio local `radius/full` en lugar del literal 999 fuente: mismo resultado visible a estas alturas.

## 7. States

No hay estados interactivos. Los cuatro tonos no implican por sí mismos validación, éxito o error de un proceso; el producto debe aportar esa semántica si aplica. Prototipos: cero.

## 8. Behavior

En Figma, Progress elige una muestra estática y sincroniza texto/geometría por variante. No implementar cálculo continuo, animación ni avance temporal. Ocultar Label o helper colapsa su espacio por auto layout; Show percentage solo retira el número.

## 9. Accessibility

Las etiquetas y porcentajes visibles deben permanecer legibles y no depender solo de color. Para frontend futuro se requiere nombre, valor, máximo y estado programático, todavía `UNRESOLVED`; esta construcción Figma no valida lectores de pantalla ni teclado. La corrección del porcentaje evita una lectura visual contradictoria.

## 10. Design tokens

Inventario base SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`. Los cinco roles nuevos tienen aliases y scopes definidos solo en el JSON versionado y verificados en Figma. Mapa obligatorio:

| Consumidor | Variable local | Scope |
|---|---|
| Pista de 48 variantes | `color/background/progress/track` | FRAME_FILL |
| Segmento Primary/Warning/Positive/Danger | `color/background/progress/primary/warning/positive/danger` según Type | FRAME_FILL |
| Label y Percentage | `color/text/primary` | TEXT_FILL |
| Helper | `color/text/secondary` | TEXT_FILL |
| Tipografía | `font/family/base`, `font/weight/regular`, `font/size/xs/sm`, `font/line-height/xs/sm`, `font/letter-spacing/normal` | FONT_FAMILY/FONT_STYLE/FONT_SIZE/LINE_HEIGHT/LETTER_SPACING |
| Gaps y radio | `spacing/xs`, `radius/full` | GAP/CORNER_RADIUS |

Servicios usa orange/600 en Primary para 4.31:1 sobre pista, frente a orange/500 de 2.95:1. Warning amber/600 alcanza 3.03:1, Positive emerald/600 4.50:1, Danger red/600 5.05:1 y las otras tres marcas superan 5:1. No usar feedback/icon para frames ni texto para pistas.

## 11. Content rules

Label y Helper son ejemplos editables. Percentage se deriva del eje Progress y no es un TEXT libre; así las 48 combinaciones muestran el número correcto. No se define locale, precisión adicional, unidad ni longitud máxima.

## 12. Composition rules

Fila superior distribuye Label a izquierda y Percentage a derecha. Pista y segmento son frames separados, con avance al inicio y clipping redondeado. Helper queda debajo. No anidar otro componente ni importar un asset del origen.

## 13. Responsive behavior

Small/Medium/Large son variantes de densidad, no breakpoints. El ancho 246 px es referencia del set fuente; responsividad web queda sin definir.

## 14. Edge cases

Si se ocultan todos los textos, la barra permanece. Si se oculta solo Percentage, no se reserva espacio para un número invisible. Label/helper largos pueden requerir más ancho o altura; no truncar valores críticos silenciosamente. El 100% llena toda la pista sin borde restante visible.

## 15. Forbidden combinations

No mostrar `25%` con barra 50/75/100; no aplicar roles `feedback/*/icon` o `color/text/*` a frames; no dejar track literal; no crear colores primitivos nuevos; no inventar animación, valor arbitrario o interacciones.

## 16. Design ↔ Code mapping

Figma `Progress` es una variante discreta; frontend futuro debería recibir valor numérico tipado y formatear porcentaje desde la misma fuente. Type mapea tono, no lógica de estado. No se crea código en esta tarea.

## 17. Acceptance criteria

| ID | Verificación |
|---|---|
| AC-LPB-001 | Página única `Linear Progress Bars`, un set y 48 variantes Type×Size×Progress. |
| AC-LPB-002 | 48 anchos de barra corresponden exactamente a 25/50/75/100% de 246 px; el texto visible coincide con cada eje. |
| AC-LPB-003 | Tres tamaños y anatomía visual reproducidos; diferencias de altura +1 px Middle/Large documentadas sin clipping. |
| AC-LPB-004 | Propiedades Label/Helper y tres booleanas conectadas; Percentage no es TEXT libre contradictorio. |
| AC-LPB-005 | 96 fondos y 144 textos ligados a variables locales correctas; cero errores de scope/categoría; tipografía completa. |
| AC-LPB-006 | Cinco roles nuevos coinciden JSON/Figma en cuatro modos y colores de barra superan 3:1 contra pista. |
| AC-LPB-007 | Cero reacciones, set `UNPUBLISHED`, QA estructural/visual y auditoría humana posterior registrada. |

## 18. Examples

Primary/Small/25% muestra barra corta azul; Warning/Medium/50% muestra media barra amber; Positive/Large/75% muestra tres cuartos green; Danger/Large/100% llena la pista red. Son ejemplos, no datos vivos.

## 19. Source of truth

Este Markdown gobierna requisitos de destino; el inventario y el JSON de extensión gobiernan variables. El YAML fuente conserva los 48 IDs y su anomalía textual; el estado de implementación guarda IDs reales de Figma destino.

## 20. Change management

Cambios deliberados: fuente `middle`→destino `Medium`; texto porcentual vinculado conceptualmente a Progress y sin propiedad TEXT independiente; fondo track tokenizado; cuatro barras remapeadas a roles de fondo; Servicios Primary orange/500→orange/600; radios a `radius/full`; Middle/Large +1 px por interlineado local. No se toca la fuente.

## 21. Changelog

- 0.1.0 delegado: 48 muestras consistentes, cinco roles de fondo y auditoría humana posterior.
