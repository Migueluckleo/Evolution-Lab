---
contract_schema: sdd-project/0.2
contract_id: FILEUPLOAD-001
name: File Upload
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-28
review_targets: [figma]
figma_page_name: Input Fields
sources: [SRC-FIGMA-FILE-UPLOAD-001, SRC-TOKENS-INV-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.feedback-icon-scopes.v0.1.0.json, drafts/foundations/ai-design-system.linear-progress-colors.v0.1.0.json, drafts/contracts/file-upload.source.component-contract.yaml]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-LINEAR-PROGRESS-COLORS-001, specs/components/button.contract.v0.2.0.md]
user_audit: PENDING
---

# File Upload 0.1.0 · contrato de construcción

## 1. Purpose

Reconstruir File Upload en AI Design System, página semántica Input Fields, junto a Input Field sin modificarlo.

## 2. Contract

REQ-01: materializar 6 variantes locales desde la evidencia, con auto layout, propiedades editables y tokens semánticos. Alcance Figma y documentación; no código.

## 3. Anatomy

Dropzone vertical con icono, mensaje, formatos, progreso en Success y Button opcional; Helper fuera. Reutilizar Button local Small/Default o Small/Disabled. Progress se reconstruye como fondo y frame de valor sin importar la rama Tooltip oculta no expuesta por propiedades; esta rama se conserva solo en evidencia histórica.

## 4. Properties

REQ-02: propiedades conectadas en todos los estados donde existen.

| Nombre | Tipo | Default |
|---|---|---|
| Message prefix | TEXT | Haz clic para |
| Action text | TEXT | subir tu archivo |
| Message suffix | TEXT | o arrástralo aquí |
| Success message | TEXT | Archivo cargado exitosamente |
| Error message | TEXT | Error al cargar el archivo |
| Formats | TEXT | Formatos compatibles: .XLS, XLSX o CSV - Tamaño máximo 50 MB |
| Helper | TEXT | Optional helper text |
| Show helper | BOOLEAN | true |
| Show button | BOOLEAN | false |
| Upload icon | INSTANCE_SWAP | CloudArrowUp Outline/Light |

File Upload separa Success message y Error message para no compartir un default engañoso entre estados; Button permite editar su propiedad de texto anidada.

## 5. Variants

REQ-03: State={Default,Success,Hover,Focus,Disabled,Error}; 6 variantes. Default inicial, sin estados inventados.

## 6. Sizes

REQ-04: Ancho500; padding16, gap12, radio12, dash5/5. Upload40; feedback32. Default/Hover/Focus/Disabled total148 (fuente147); Error140 (fuente142); Success162 (fuente163). Las diferencias se deben exclusivamente a interlineados tokenizados20/16; el progress conserva10px. Sin botón visible por defecto. Dimensiones observadas y dash son literales geométricos; no usar tokens GAP para ancho/alto.

## 7. States

REQ-05: Disabled mantiene texto deshabilitado aunque se reemplace por datos precargados; no usar primary para valores deshabilitados. Success/Error conservan feedback semántico. No agregar reacciones.

## 8. Behavior

Tipos XLS/XLSX/CSV, 50MB y progreso100% son ejemplos visuales, no validación de archivos ni carga real. No se crea flujo de eventos.

## 9. Accessibility

Medir contraste y marcar limitaciones con asterisco sin recolorear. Figma no demuestra semántica HTML, teclado, bloqueo de eventos ni objetivos táctiles. Etiquetas/ayudas editables.

## 10. Design tokens

REQ-06: inventario canónico sources/inventories/tokens.inventory.json; no crear primitivas ni tokens nuevos.

| Parte | Token | Variable local | Scope |
|---|---|---|---|
| Dropzone | color/background/default | VariableID:13:35 | FRAME_FILL, SHAPE_FILL |
| Hover surface | color/background/brand | VariableID:13:78 | FRAME_FILL, SHAPE_FILL |
| Border | color/border/default | VariableID:13:13 | STROKE_COLOR |
| Hover border | color/border/brand | VariableID:13:16 | STROKE_COLOR |
| Disabled border | color/border/disabled | VariableID:13:17 | STROKE_COLOR |
| Error border | color/feedback/danger/border | VariableID:13:51 | STROKE_COLOR |
| Focus border | color/focus/ring | VariableID:13:71 | STROKE_COLOR |
| Text | color/text/primary | VariableID:13:27 | TEXT_FILL |
| Action | color/text/brand | VariableID:13:32 | TEXT_FILL |
| Formats | color/text/tertiary | VariableID:13:29 | TEXT_FILL |
| Disabled/helper | color/text/disabled | VariableID:13:30 | TEXT_FILL |
| Success text | color/feedback/positive/text | VariableID:13:42 | TEXT_FILL |
| Error text | color/feedback/danger/text | VariableID:13:50 | TEXT_FILL |
| Upload icon | color/icon/primary | VariableID:13:20 | SHAPE_FILL |
| Disabled icon | color/icon/disabled | VariableID:13:24 | SHAPE_FILL |
| Success icon | color/feedback/positive/icon | VariableID:13:44 | SHAPE_FILL |
| Error icon | color/feedback/danger/icon | VariableID:13:52 | SHAPE_FILL |
| Progress track | color/background/muted | VariableID:13:37 | FRAME_FILL, SHAPE_FILL |
| Progress fill frame | color/background/progress/positive | VariableID:219:125 | FRAME_FILL |

Tipografía: font/family/base, font/weight/regular,bold,semibold; font/size/sm=14,xs=12,2xs=10 (solo formatos Success); font/line-height/sm20 y xs16; font/letter-spacing/normal. Normalización explícita de AUTO/% y tracking a la escala local, conservando pesos. Espaciado none/xs/sm/md/lg y radios md/lg/full; stroke/xs1 o sm1.5 en File Upload Focus. Instancias iconográficas usan exclusivamente roles icon. Los cuatro modos se heredan. No sustituir aliases por literales ni fijar Contable.

Extensiones existentes: focus-effects.v0.1.0 (Search), feedback-icon-scopes.v0.1.0 y linear-progress-colors.v0.1.0 (File Upload). No redefinir sus datos. El verde de progreso se aplica a FRAME_FILL, no a un rectángulo con rol icon.

## 11. Content rules

Los textos de la fuente son demos editables. No convertirlos en requisitos de producto. File Upload conserva el énfasis y subrayado de la acción mediante tres nodos de texto editables separados por spacing/xs=4; se eliminan espacios terminales que Figma no incluye en el ancho HUG. Disabled conserva subrayado pero sin color de acción. El mensaje permite wrap. Strokes no se incluyen en el cálculo de padding.

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

AC-01: 6 variantes únicas y propiedades enlazadas.
AC-02: dimensiones según sección6 y QA visual sin recortes.
AC-03: todas las pinturas semánticas locales, scopes correctos y cuatro modos verificados.
AC-04: cinco bindings tipográficos por texto nuevo; dependencias reales.
AC-05: pruebas de contenido/visibilidad, fuente preservada y registros con IDs.
AC-06: promoción a specs solo tras QA documental e implementación PASS.

## 18. Examples

Default para estado inicial; Disabled con contenido precargado conserva texto Disabled. Otros estados son presentaciones, no transiciones.

## 19. Source of truth

Este MD gobierna construcción; JSON canónico y extensiones gobiernan valores. Evidencia: drafts/contracts/file-upload.source.component-contract.yaml y sources/figma-snapshots/file-upload.deep.json. IDs destino se registran separados de origen.

## 20. Change management

DRAFT→QA documental→DELEGATED_FOR_BUILD. Auditoría humana PENDING por excepciones. Tras QA técnico PASS se promueve a specs; cambios posteriores allí como versión/enmienda. Graphify STALE, no regenerado.

## 21. Changelog

0.1.0 · 2026-09-28: contrato inicial; mapeo semántico, propiedades editables, mejoras documentadas y regla Disabled aplicada. Promovido a specs tras QA documental y técnico PASS. Auditoría humana PENDING; biblioteca UNPUBLISHED. [QA](../qa/implementations/file-upload.v0.1.0.figma.review.md) y [estado con IDs](../implementations/figma/file-upload.v0.1.0.state.json).
