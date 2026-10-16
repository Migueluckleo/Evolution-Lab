---
contract_schema: sdd-project/0.2
contract_id: TEXTAREA-001
name: Textarea
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-28
review_targets: [figma]
figma_page_name: Input Fields
sources: [SRC-FIGMA-TEXTAREA-001, SRC-TOKENS-INV-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/textarea.source.component-contract.yaml]
dependencies: [FOUNDATIONS-TOKENS-001]
user_audit: PENDING
---

# Textarea 0.1.0 · contrato de construcción

## 1. Purpose

Reconstruir Textarea en AI Design System, página semántica Input Fields, junto a Input Field sin modificarlo.

## 2. Contract

REQ-01: materializar 4 variantes locales desde la evidencia, con auto layout, propiedades editables y tokens semánticos. Alcance Figma y documentación; no código.

## 3. Anatomy

Label, Control group con Surface vertical (Text y Footer con Counter/Resize icon), Helper.

## 4. Properties

REQ-02: propiedades conectadas en todos los estados donde existen.

| Nombre | Tipo | Default |
|---|---|---|
| Label | TEXT | Enter your password |
| Text | TEXT | Enter your text here... |
| Counter | TEXT | 100/300 |
| Helper | TEXT | Helper text |
| Show label | BOOLEAN | true |
| Show helper | BOOLEAN | true |
| Show counter | BOOLEAN | true |
| Resize icon | INSTANCE_SWAP | Notches Outline/Light |

File Upload Status message conserva el texto propio de Success/Error; Button permite editar su propiedad de texto anidada.

## 5. Variants

REQ-03: State={Default,Error,Disabled,Focus}; 4 variantes. Se elimina type=Textarea como eje de valor único. Default inicial, sin estados inventados.

## 6. Sizes

REQ-04: Ancho305, total160. Label20+gap8+Surface108+gap8+Helper16. Surface padding16 horizontal/12 vertical, gap8; texto60, footer16, icono16, radio8. Ajuste explícito: Surface104→108 compensa Label22→20 y Helper18→16 al usar interlineados locales. Dimensiones observadas y dash son literales geométricos; no usar tokens GAP para ancho/alto.

## 7. States

REQ-05: Disabled mantiene texto deshabilitado aunque se reemplace por datos precargados; no usar primary para valores deshabilitados. Success/Error conservan feedback semántico. No agregar reacciones.

## 8. Behavior

El contador100/300 es texto de demo editable: no expresa longitud calculada ni límite300. Notches es affordance visual; no se implementa resize real.

## 9. Accessibility

Medir contraste y marcar limitaciones con asterisco sin recolorear. Figma no demuestra semántica HTML, teclado, bloqueo de eventos ni objetivos táctiles. Etiquetas/ayudas editables.

## 10. Design tokens

REQ-06: inventario canónico sources/inventories/tokens.inventory.json; no crear primitivas ni tokens nuevos.

| Parte | Token | Variable local | Scope |
|---|---|---|---|
| Surface | color/background/default | VariableID:13:35 | FRAME_FILL, SHAPE_FILL |
| Surface Disabled | color/background/subtle | VariableID:13:36 | FRAME_FILL, SHAPE_FILL |
| Border | color/border/default | VariableID:13:13 | STROKE_COLOR |
| Focus border | color/focus/ring | VariableID:13:71 | STROKE_COLOR |
| Error border | color/feedback/danger/border | VariableID:13:51 | STROKE_COLOR |
| Label | color/text/primary | VariableID:13:27 | TEXT_FILL |
| Content/counter/helper | color/text/tertiary | VariableID:13:29 | TEXT_FILL |
| Disabled text | color/text/disabled | VariableID:13:30 | TEXT_FILL |
| Error label/helper | color/feedback/danger/text | VariableID:13:50 | TEXT_FILL |
| Resize icon | color/icon/secondary | VariableID:13:21 | SHAPE_FILL |
| Disabled icon | color/icon/disabled | VariableID:13:24 | SHAPE_FILL |

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

AC-01: 4 variantes únicas y propiedades enlazadas.
AC-02: dimensiones según sección6 y QA visual sin recortes.
AC-03: todas las pinturas semánticas locales, scopes correctos y cuatro modos verificados.
AC-04: cinco bindings tipográficos por texto nuevo; dependencias reales.
AC-05: pruebas de contenido/visibilidad, fuente preservada y registros con IDs.
AC-06: promoción a specs solo tras QA documental e implementación PASS.

## 18. Examples

Default para estado inicial; Disabled con contenido precargado conserva texto Disabled. Otros estados son presentaciones, no transiciones.

## 19. Source of truth

Este MD gobierna construcción; JSON canónico y extensiones gobiernan valores. Evidencia: drafts/contracts/textarea.source.component-contract.yaml y sources/figma-snapshots/textarea.deep.json. IDs destino se registran separados de origen.

## 20. Change management

DRAFT→QA documental→DELEGATED_FOR_BUILD. Auditoría humana PENDING por excepciones. Tras QA técnico PASS se promueve a specs; cambios posteriores allí como versión/enmienda. Graphify STALE, no regenerado.

## 21. Changelog

0.1.0 · 2026-09-28: contrato inicial; mapeo semántico, propiedades editables, mejoras documentadas y regla Disabled aplicada. Promovido a specs tras QA documental y técnico PASS. Auditoría humana PENDING; biblioteca UNPUBLISHED. [QA](../qa/implementations/textarea.v0.1.0.figma.review.md) y [estado con IDs](../implementations/figma/textarea.v0.1.0.state.json).
