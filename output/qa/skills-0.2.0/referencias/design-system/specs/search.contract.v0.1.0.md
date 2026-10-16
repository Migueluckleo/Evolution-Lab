---
contract_schema: sdd-project/0.2
contract_id: SEARCH-001
name: Search
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-28
review_targets: [figma]
figma_page_name: Input Fields
sources: [SRC-FIGMA-SEARCH-001, SRC-TOKENS-INV-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.focus-effects.v0.1.0.json, drafts/contracts/search.source.component-contract.yaml]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-FOCUS-EFFECTS-001]
user_audit: PENDING
---

# Search 0.1.0 · contrato de construcción

## 1. Purpose

Reconstruir Search en AI Design System, página semántica Input Fields, junto a Input Field sin modificarlo.

## 2. Contract

REQ-01: materializar 12 variantes locales desde la evidencia, con auto layout, propiedades editables y tokens semánticos. Alcance Figma y documentación; no código.

## 3. Anatomy

Label y Surface horizontal con Text, Clear opcional por estado, Divider y Search icon. Focus con soporte decorativo absoluto detrás de Surface.

## 4. Properties

REQ-02: propiedades conectadas en todos los estados donde existen.

| Nombre | Tipo | Default |
|---|---|---|
| Label | TEXT | Buscar |
| Text | TEXT | Buscar |
| Show label | BOOLEAN | true |
| Search icon | INSTANCE_SWAP | MagnifyingGlass Outline/Light |
| Clear icon | INSTANCE_SWAP | X Outline/Light |

File Upload Status message conserva el texto propio de Success/Error; Button permite editar su propiedad de texto anidada.

## 5. Variants

REQ-03: Size={Large,Medium,Small} × State={Default,Selected,Focus,Disabled}; 12 variantes. Default inicial, sin estados inventados.

## 6. Sizes

REQ-04: Ancho 464; superficies 48/40/32; totales 76/68/60. Padding horizontal 16 y vertical 8, gap16, radio8, iconos20. Dimensiones observadas y dash son literales geométricos; no usar tokens GAP para ancho/alto.

## 7. States

REQ-05: Disabled mantiene texto deshabilitado aunque se reemplace por datos precargados; no usar primary para valores deshabilitados. Success/Error conservan feedback semántico. No agregar reacciones.

## 8. Behavior

Selected representa la presentación observada con contenido y botón de limpieza; no implementa selección de resultados ni búsqueda real.

## 9. Accessibility

Medir contraste y marcar limitaciones con asterisco sin recolorear. Figma no demuestra semántica HTML, teclado, bloqueo de eventos ni objetivos táctiles. Etiquetas/ayudas editables.

## 10. Design tokens

REQ-06: inventario canónico sources/inventories/tokens.inventory.json; no crear primitivas ni tokens nuevos.

| Parte | Token | Variable local | Scope |
|---|---|---|---|
| Surface | color/background/default | VariableID:13:35 | FRAME_FILL, SHAPE_FILL |
| Surface Disabled | color/background/subtle | VariableID:13:36 | FRAME_FILL, SHAPE_FILL |
| Border | color/border/default | VariableID:13:13 | STROKE_COLOR |
| Divider selected/focus | color/border/strong | VariableID:13:15 | STROKE_COLOR |
| Label/value | color/text/primary | VariableID:13:27 | TEXT_FILL |
| Placeholder | color/text/tertiary | VariableID:13:29 | TEXT_FILL |
| Disabled text | color/text/disabled | VariableID:13:30 | TEXT_FILL |
| Search icon | color/icon/brand | VariableID:13:25 | SHAPE_FILL |
| Clear icon | color/icon/primary | VariableID:13:20 | SHAPE_FILL |
| Disabled icon | color/icon/disabled | VariableID:13:24 | SHAPE_FILL |
| Focus effect | color/focus/effect-outer | VariableID:136:122 | EFFECT_COLOR |

Tipografía: font/family/base, font/weight/regular,bold,semibold; font/size/sm=14,xs=12,2xs=10 (solo formatos Success); font/line-height/sm20 y xs16; font/letter-spacing/normal. Normalización explícita de AUTO/% y tracking a la escala local, conservando pesos. Espaciado none/xs/sm/md/lg y radios md/lg/full; stroke/xs1 o sm1.5 en File Upload Focus. Instancias iconográficas usan exclusivamente roles icon. Los cuatro modos se heredan. No sustituir aliases por literales ni fijar Contable.

Extensiones existentes: focus-effects.v0.1.0 (Search), feedback-icon-scopes.v0.1.0 y linear-progress-colors.v0.1.0 (File Upload). No redefinir sus datos. El verde de progreso se aplica a FRAME_FILL, no a un rectángulo con rol icon.

## 11. Content rules

Los textos de la fuente son demos editables. No convertirlos en requisitos de producto. File Upload conserva el énfasis y subrayado de la acción mediante tres nodos de texto editables; Disabled conserva subrayado pero sin color de acción.

## 12. Composition rules

REQ-07: una sección documental y un set por subfamilia en Input Fields. Iconos Phosphor como instancias con intercambio; no dibujarlos de memoria. No modificar principales ajenos. Publicación de biblioteca no incluida.

## 13. Responsive behavior

Ancho inicial observado, descendientes FILL y textos editables; no se declaran breakpoints. Documentar límites de contenido extenso sin prometer ancho ilimitado.

## 14. Edge cases

Ocultar Label/Helper/Counter/Button debe reajustar auto layout. Si la fila de mensaje de File Upload se estrecha, permitir reflujo o declarar el mínimo soportado; no recortar texto silenciosamente.

## 15. Forbidden combinations

No text como icon/background; no primitivas directas; no estado Filled Disabled de color activo; no simular funcionamiento real. Tooltip oculto de progreso no se expone como funcionalidad nueva.

## 16. Design ↔ Code mapping

Se normalizan nombres de ejes/capitalización, no estados. Search middle→Medium, focused→Focus; Textarea type monovalor se suprime. Frontend fuera de alcance.

## 17. Acceptance criteria

AC-01: 12 variantes únicas y propiedades enlazadas.
AC-02: dimensiones según sección6 y QA visual sin recortes.
AC-03: todas las pinturas semánticas locales, scopes correctos y cuatro modos verificados.
AC-04: cinco bindings tipográficos por texto nuevo; dependencias reales.
AC-05: pruebas de contenido/visibilidad, fuente preservada y registros con IDs.
AC-06: promoción a specs solo tras QA documental e implementación PASS.

## 18. Examples

Default para estado inicial; Disabled con contenido precargado conserva texto Disabled. Otros estados son presentaciones, no transiciones.

## 19. Source of truth

Este MD gobierna construcción; JSON canónico y extensiones gobiernan valores. Evidencia: drafts/contracts/search.source.component-contract.yaml y sources/figma-snapshots/search.deep.json. IDs destino se registran separados de origen.

## 20. Change management

DRAFT→QA documental→DELEGATED_FOR_BUILD. Auditoría humana PENDING por excepciones. Tras QA técnico PASS se promueve a specs; cambios posteriores allí como versión/enmienda. Graphify STALE, no regenerado.

## 21. Changelog

0.1.0 · 2026-09-28: contrato inicial; mapeo semántico, propiedades editables, mejoras documentadas y regla Disabled aplicada. Promovido a specs tras QA documental y técnico PASS. Auditoría humana PENDING; biblioteca UNPUBLISHED. [QA](../qa/implementations/search.v0.1.0.figma.review.md) y [estado con IDs](../implementations/figma/search.v0.1.0.state.json).
