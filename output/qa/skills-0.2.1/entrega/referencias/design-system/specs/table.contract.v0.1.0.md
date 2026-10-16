---
contract_id: TABLE-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
source: Anticipa / 15006:84823
target: AI-Design-System / tj3WIBEZDGLVs7MJWKCwgf
figma_page_name: Table
user_audit: PENDING
---

# Table · contrato de reconstrucción 0.1.0

## 1. Propósito
Composición tabular de escritorio para datos, selección y acciones opcionales. EXPLICIT: el usuario sustituye la fuente legacy por Anticipa y ordena continuar. [Decisión](../registry/DEC-TABLE-ANTICIPA-SOURCE-001.md). La fuente se conserva intacta.

## 2. Contrato
Destino exclusivo AI-Design-System, página funcional **Table**. Construir Table, Table Header, Table Header Cell, Table Cell, Table Actions Cell y Table Row (Default/Hover). Helpers privados solo para artwork exacto no importable y acción de producto; reutilizar Checkbox, Badge, Icon Button, Dot y logo locales. No autoriza frontend ni publicación de biblioteca.
P-SLOTS: REQUIRED para Rows, Header/Cells, Row/Cells y Actions Cell/Actions. NOT_APPLICABLE para texto, checkbox, badge, logo y copy/sort individuales: cardinalidad fija y propiedades propias. La delegación para esta fuente está registrada explícitamente; no significa aprobación humana.

## 3. Anatomía
Table → Header + Rows SLOT. Header → Checkbox oculto + cabecera Actions oculta + Cells SLOT.
Row → Checkbox oculto + Actions Cell oculta + Cells SLOT. Hover añade DotsThree24 antes de Cells.
Header Cell → logo16 oculto + texto + sort16 oculto.
Body Cell → Badge oculto + texto + copy16 oculto. El texto continúa visible al mostrar Badge como en fuente; no inferir exclusividad.
Actions Cell → Actions SLOT (Icon Button de documento y acción de producto). El logo es agnóstico: no tokenizar ni recolorear sus vectores.

## 4. Propiedades
Table: Rows SLOT y Header expuesto.
Header: Cells SLOT, Show selection=false, Show actions=false; Checkbox expuesto para elegir Selected/Unselected/Indeterminate.
Header Cell: Content TEXT=UUID; Show brand=false; Show sort=false.
Table Cell: Content TEXT=UUID; Show status=false; Show copy=false. Badge expuesto para texto/tipo/iconos.
Row: State=Default/Hover; Cells SLOT; Show selection=false; Show actions=false. Checkbox y Actions Cell expuestos.
Actions Cell: Actions SLOT. Propiedades internas de Icon Button y producto permanecen editables.
DERIVED: TEXT editables y nombres funcionales; no añadir ejes de cantidad ni combinaciones de negocio.

## 5. Variantes
Solo Row posee dos variantes globales: State=Default/Hover, correspondientes a hover=false/true. Las demás piezas tienen un main. No crear Selected/Disabled/Error de fila por analogía con controles internos. La matriz de Checkbox no se duplica en Row.

## 6. Tamaños
Baseline Table1280×412: Header52 y diez filas36. Columnas observadas:156,371.999755859375,132,224,156,88,88. Gap8; padding exterior de fila/cabecera8 horizontal; celdas8 horizontal y Body8 vertical, Header16 vertical. Radio exterior8.
Main de celda184 de ancho; texto14/20. Actions Cell main112×56 con dos acciones40 y gap16; dentro de la fila conserva el override140×64. Activarla aumenta la altura de la fila; cabecera Actions140.
Hover observado1287.9998×36: acción24, gap8 y primera celda132; resto de columnas igual. **Limitación TABLE-AUD-001:** añade8px al ancho y desplaza columnas; se conserva como evidencia visual, no como alineación correcta. Un ancho fijo consumidor puede ocultar el extremo si no lo amplía.
Geometría sin token de dimensión equivalente se conserva literal; no ligar anchos arbitrarios a spacing. Icon Button local Medium se consume con override40×40 para igualar la muestra, sin modificar su main48×48.

## 7. Estados
Default fondo blanco; Hover fondo auxiliar solo en Cells SLOT, DotsThree de marca y fila transparente. Sin cambios de color por contraste.
La fuente usa ON_HOVER→CHANGE_TO. Conservar esta reacción entre los dos Row locales, sin inventar selección, ordenamiento ni acciones. El ejemplo debe mostrar también Hover separado para revisión.

## 8. Comportamiento
Los Slots permiten insertar, quitar, sustituir y reordenar instancias sin detach. Rows, Cells y Actions: min0, maxsin límite; recomendaciones a componentes locales actuales, sin keys obsoletas.
Rows10/Cells7/Actions2 son ejemplos, no límites. Estado vacío de Slot no inventa mensaje “sin datos”.
Show selection/actions debe coordinarse entre header y filas por el consumidor. No hay sincronización automática, sort real, cálculo de subtotal, copy al portapapeles ni navegación implementados.
La conservación de contenido al cambiar Row State debe verificarse en instancias; cualquier limitación se registra explícitamente, no se oculta.

## 9. Accesibilidad
No se declara conformidad web por QA visual. Producto define nombres accesibles, selección de grupo, navegación por teclado, estado de orden y acceso al texto completo truncado.
Texto fuente negro→neutral900 es aproximación autorizada a paleta existente; encabezado ya usa neutral900 exacto. Divisores E2E8F0 sobre blanco son sutiles; medir y señalar con asterisco si se interpretan como límites esenciales. No oscurecerlos silenciosamente.
Iconos16 no constituyen targets accesibles por sí solos. El consumidor define área interactiva y foco; controles locales mantienen su contrato.

## 10. Design tokens
Fuente canónica: [tokens.inventory.json](../sources/inventories/tokens.inventory.json), SHA256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474. Aplican contrato transversal y enmienda0.1.2. No se añaden variables/primitivas ni se modifica el JSON aprobado.
Mapa real de variables en [preflight](../sources/figma-snapshots/table.target-preflight.v0.1.0.json); nombres/aliases/modos del JSON gobiernan, IDs reales de destino se verifican.
- Cabecera #EFF3FF → color/background/brand (13:78), FRAME_FILL; neutralidad de estado no usa rol feedback. Alias por tema exactamente como JSON; no corregir sus modos dentro de Table.
- Fila blanca → color/background/default (13:35); Hover #F1F5F9 → color/background/subtle (13:36).
- Borde #E2E8F0 → color/border/strong (13:15), STROKE_COLOR. Su nombre histórico no permite sustituirlo por default de otro gris.
- Texto principal → color/text/primary (13:27), TEXT_FILL, neutral900 #0F172A. Body fuente#000000 no tiene primitiva exacta: usar este neutral, registrar delta RGB(15,23,42). No usar primitiva directa.
- Sort/copy → color/icon/primary (13:20), SHAPE_FILL, misma aproximación respecto al negro fuente. Copia usa trazado visible expandido: no duplicar el path de stroke oculto del main.
- DotsThree y documento → color/icon/brand, SHAPE_FILL; bordes de Icon Button según su contrato y cuatro temas.
- Manrope Regular/Bold: font/family/base10:2, font/weight/regular10:3,bold10:6; font/size/sm10:9=14; font/line-height/sm12:8=20; font/letter-spacing/normal12:16=0.
- spacing/none12:18=0, spacing/sm12:30=8, spacing/lg12:32=16, GAP; radius/md13:6=8, CORNER_RADIUS; stroke/xs12:41=1, STROKE_FLOAT.
Dependencias canónicas reutilizadas: [Dot backgrounds0.1.0](../drafts/foundations/ai-design-system.dot-background-colors.v0.1.0.json) y [Control border0.1.1](../drafts/foundations/ai-design-system.control-colors.v0.1.1.json). Badge usa positive/bg,text,icon; Circle consume color/feedback/positive/icon13:44. No inventar el nombre success/icon.
Todas las referencias son VariableID:prefijo. Los controles reutilizados conservan extensiones locales vigentes; no importar bindings remotos a los paints consumidores. No fijar modo en componentes base; pruebas en cuatro modos.

## 11. Reglas de contenido
Valores de tabla son demos. Cabeceras y filas de la captura se guardan en [inventario observado](../sources/figma-snapshots/table-anticipa.v0.1.0.inventory.json). TEXT de una línea, truncado ENDING/maxLines1, ancho FILL. No imponer formato fiscal, moneda o número de filas por los ejemplos.

## 12. Composición
Rows vertical HUG, gap0; Cells horizontal HUG, gap8; Actions horizontal HUG, gap16. Table HUG como fuente. Cada Slot está conectado a una propiedad SLOT real, no es frame renombrado.
Recomendaciones: Row para Rows, Header Cell para Header/Cells, Table Cell para Row/Cells, Icon Button y acción de producto para Actions. Permitir composición alternativa; el consumidor coordina tipos y anchos de columnas. P-SLOTS no promete grid algorítmico ni alineación automática.

## 13. Responsive
No breakpoint/móvil ni columnas ocultables automáticas en fuente. Para ancho reducido usar un contenedor de producto con overflow definido o menos columnas; no comprimir arbitrariamente el contenido. Test de ancho reducido documenta límite, no PASS responsive universal.

## 14. Edge cases
QA consumidor: Rows0/1/5/10/12, Cells0/1/3/7/9, Actions0/1/2/3; insertar/eliminar/reordenar y asegurar retorno a estado original sin detach. Texto largo, booloff/on, badge/copy/logo/sort visibles, cuatro temas, Row Default↔Hover. Evaluar diferencias de ancho y retención de overrides expresamente.
Vacíos no inventan semántica de producto; mensajes Empty State quedan fuera de Table.

## 15. Combinaciones prohibidas
Primitiva aplicada a paints; tokens text en shapes/background/stroke; fijar azul a todos los temas en roles de marca; duplicar set por cantidad; detach para Slots; modificar mains externos; afirmar datos calculados, aprobación humana, accesibilidad o publicación sin evidencia.

## 16. Design↔Code
Nombres orientativos Table/Header/Row/Cell/Actions y props Content/Show*. No código ni correspondencia ejecutable autorizada. Comportamientos de selección, sort, navegación y virtualización requieren definición independiente.

## 17. Criterios de aceptación
Contrato versionado, fuentes y decisión explícita; QA documental; páginaTable; anatomía default y textos comparables con fuente; propiedades conectadas; Slots nativos editables; tokens semánticos locales compatibles; modos sin hardcodes de marca; QA por readback y screenshot. PASS técnico puede incluir limitaciones fuente documentadas, nunca afirmar alineación Hover ni cobertura responsive total.

Verificación final:899paints no agnósticos tokenizados,0fallos de scope/localidad;36tokens/144aliases por modo comprobados;27checks estructuralesPASS y320pxno soportado. [QA](../qa/implementations/table.v0.1.0.figma.review.md).

## 18. Ejemplos
Baseline diez filas, controles opcionales, Hover y pruebas de Slots quedan separados de los mains en la páginaTable. No contaminar la biblioteca con variantes de prueba.

IDs reales: página546:122; Table548:895; Header548:408; Rowset548:893 (Default548:726/Hover548:853); HeaderCell546:257; BodyCell546:292; ActionsCell548:372. Ejemplos&QA550:588. [Manifest](../implementations/figma/table.v0.1.0.build.json).

## 19. Source of truth
Este MD gobierna reconstrucción; JSON aprobado gobierna tokens. [MD fuente](../drafts/contracts/table-anticipa.source.component-contract.md), [YAML](../drafts/contracts/table-anticipa.source.component-contract.yaml) y snapshots son evidencia, no norma.
La extracción recorre1449nodos/456instancias; dependencias se referencian por15keys. Metadatos parciales declarados: paths de variables muestreados y overrides completos no archivados. No impide esta reconstrucción acotada desde geometrías, RGB, propiedades activas y dependencias locales verificadas; no declarar contratos individuales completos de las dependencias.

## 20. Gestión de cambios
DRAFT→DELEGATED_FOR_BUILD mediante decisión de fuente y orden de continuar, condicionado a QA documental. Construir sin aprobación repetitiva; después de QA de implementación promover a specs. Auditoría humana PENDING; biblioteca sin publicar. Ajustes posteriores en specs con versión/trazabilidad. IDs reales se registran tras escritura, nunca se infieren.

Cierre2026-10-01: promovido a specs después de QA técnico acotado. Bordes excluidos de auto layout como fuente; Circle de Badge enlazado al rol positive/icon en consumidorTable. Contraste texto17.853sobreblanco/16.097cabeceraazul/15.974cabeceravioleta/16.296Hover. Divisor1.233:1*; iconoServiciossobreblanco3.236:1. Metadatos fuente parciales permanecen explícitos.

## 21. Changelog
2026-10-01 · 0.1.0: fuenteAnticipa, composición con Slots, propiedades editables, reutilización local y cero tokens nuevos. Hover y aproximación de negro documentados antes de construir.

