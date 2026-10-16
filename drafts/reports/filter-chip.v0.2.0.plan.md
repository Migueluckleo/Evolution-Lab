---
report_id: PLAN-FILTER-CHIP-FIGMA-001
contract_id: FILTER-CHIP-001
contract_version: 0.2.0
target: figma
operation: CREATE
status: PREPARED
date: 2026-09-23
---

# Plan de construcción · Filter Chip 0.2.0

## Estado leído del destino

- Archivo `AI-Design-System`, key `tj3WIBEZDGLVs7MJWKCwgf`.
- Página existente única `Buttons`, ID `0:1`, con un set `button` ID `26:81`, 60 variantes. No existe página `Chips` ni Filter Chip local en el preflight.
- Colección `semantic` ID `VariableCollectionId:6:2`, cuatro modos: Contable `6:0`, Administrativo `6:1`, Servicios `6:2`, Personas `6:3`.
- Colección `primitive` ID `VariableCollectionId:6:3`, modo Value `6:4`.
- Los 26 nombres de variable del componente fuente existen en `semantic` local del destino, con tipos y scopes apropiados. También existen `font/family/base` y `font/weight/medium`. El [mapa](../contracts/filter-chip.build.v0.2.0.yaml) registra IDs fuente y destino distintos.
- Readback individual del mapa: 28/28 IDs resolvieron al nombre previsto en `semantic` y tienen valores para los cuatro modos; 14 COLOR, 12 FLOAT y 2 STRING, sin discrepancias.
- Una instancia de PlusCircle dentro de Button apunta al componente key `46d251bb4099700c5852180f2370d265e5166432`, ID destino `26:3`, de Phosphor Icons. Se reutilizará esa dependencia remota.
- Bibliotecas conectadas observadas: Material 3 Design Kit, Simple Design System e iOS 18 and iPadOS 18. La búsqueda de `Filter Chip` local no devolvió un componente del destino; sí encontró el set de la biblioteca fuente.

## Decisiones adoptadas y diferencia respecto al origen

La respuesta del usuario «Seguir la descripción y completar variantes» resuelve las tres contradicciones de fuente para este candidato: iconos ocultos por defecto, tamaños Sm/Md/Xl y estados independientes de Selected. Los nombres internos `small/middle/large` son los del Button ya existente; sus alturas 32/40/48 permiten el mapeo Sm/Md/Xl. Por tanto, el alcance es 30 variantes, no 24 observadas ni 40 del producto cartesiano con x-small. Las 12 variantes selected de estados no Default para estos tres tamaños son nuevas. `x-small` permanece en la evidencia original, fuera de este alcance.

La descripción define explícitamente el fondo inverso con opacidad 92% en selected+hover y 85% en selected+press, y el Disabled idéntico entre selecciones. Selected+focus combina el fondo selected/default con el anillo Focus observado; esta derivación queda visible en el candidato para aprobación.

## Secuencia planeada tras aprobación

| Lote | Requisitos | Objetos afectados | Lectura posterior |
|---|---|---|---|
| 1 | REQ-FC-001 | Crear o reutilizar página `Chips` si su identidad es inequívoca; no tocar `Buttons`. | IDs/nombres de páginas y contenido inicial. |
| 2 | REQ-FC-002–005 | Crear 30 componentes con auto layout, 60 instancias vinculadas a PlusCircle, 30 etiquetas, boolean/text/swap properties y unir como set. | Matriz, jerarquía, key de iconos, definiciones y defaults. |
| 3 | REQ-FC-006–008 | Aplicar variables existentes de destino a fondo, texto, icono, tipografía, radius, padding, gap y anillo; opacidad 92/85%. | Todas las referencias de variable por ID de destino, propiedades y paints. |
| 4 | REQ-FC-009 | Registrar mapa de IDs, captura, readback independiente y QA Figma. | Resultado por criterio AC-FC-001–009. |

La [Description propuesta](../figma/filter-chip.description.v0.2.0.md) define el texto exacto del set, sin afirmar comportamiento web. El nombre del set será `Filter Chip` y la página `Chips`.

## Condición antes de escribir

El contrato [0.2.0](../contracts/filter-chip.contract.v0.2.0.md) necesita revisión y aprobación humana de esa versión y sus dos datos vinculados. P04 exige entonces comprobar que el archivo sigue sin una página Chips con identidad conflictiva y que los IDs de las 28 variables y del icono aún resuelven. La solicitud de construcción está autorizada; la aprobación del contenido técnico de la versión es el gate pendiente.
