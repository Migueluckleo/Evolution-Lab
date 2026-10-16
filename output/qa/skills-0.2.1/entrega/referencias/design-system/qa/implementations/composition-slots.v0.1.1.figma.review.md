# QA Figma · Slots 0.1.1

2026-09-30 · **PASS acotado** a Steps/Gallery, Pagination/Pages y leyendas Charts bajo [COMPOSITION-SLOTS-002](../../specs/composition-slots.amendment.v0.1.1.md). DELEGATED_FOR_BUILD; auditoría humana PENDING, biblioteca UNPUBLISHED.

## Evidencia y resultados

| Control P-SLOTS | Steps | Pagination | Charts |
|---|---|---|---|
| 01 · contrato | PASS: regiones y contextos diferenciados | PASS: Pages y Disabled contextual | PASS: Header y dos filas Detail |
| 02 · mecanismo nativo | PASS: 27 Slots Indicators en Combination y Legacy indicators en Gallery On Primary | PASS: cinco Pages leídos como SLOT | PASS: Header Legend y Progress Legend rows; réplica oculta de Legend rows en Top |
| 03 · edición consumidora | PASS: insertar, quitar, reordenar; swap de Dot enlazado | PASS: insertar/quitar, reordenar y sustituir celdas; padre continúa INSTANCE | PASS: insertar/quitar, reordenar y swap de Legend Label enlazado |
| 04 · cardinalidad | PASS: 0/1/2/3/9 por contexto | PASS: 0/1/2/4/8 celdas | PASS: Header 0/1/2/3/8 leyendas; Progress 0/1/2/5 filas completas |
| 05 · vacío | PASS estructural: placeholder 40×8, política de producto UNRESOLVED | PASS estructural: placeholder 116×26; política UNRESOLVED | PASS estructural: Header 202×16 y Legend rows639×40; política UNRESOLVED |
| 06 · layout | PASS: 3→9 indicadores, 191→287 px; a 100 px overflow sin clipping, no scroll | PASS: texto de doce dígitos ensancha celda a 107 px; ocho celdas producen 555×66; a 320 px overflow documentado | PASS: Header HUG; Detail distribuye y trunca; track corregido a FILL para 320 px sin solapamiento |
| 07 · bindings/temas | PASS: 79 pinturas visibles por modo, cero errores de scope | PASS: 182 pinturas por modo, cero errores; 200 comparaciones cromáticas sin diferencias | PASS final: 99 pinturas por modo, cero errores; evidencia anterior de Slots de celdas queda histórica |
| 08 · variantes | PASS con capacidad declarada: 9 indicadores sobreviven presets, Gallery/Gallery only y regreso desde Numbers; contexto legacy separado | PASS: 16 cambios de estado (4×4 temas), ocho celdas y textos conservados; Disabled neutraliza activo y foco, incluido grosor | PASS final: cinco filas completas sobreviven Detail→Top→Detail; Top las oculta y conserva altura30 |
| 09 · identidad/alcance | PASS: seis públicos, cuatro Dot y 27 presets con IDs originales; sin cambios cromáticos | PASS: cinco IDs y defaults 354×66; IDs de Pages y celdas originales conservados | PASS: IDs y nueve instancias de leyenda originales conservados; defaults Header638×48, Detail639×104 y Top639×30 |

Los conteos de pinturas corresponden a las muestras de prueba de cada fase, no a todo el archivo. Los cuatro modos son Contable, Administrativo, Servicios y Personas. No se certifica comportamiento de frontend, accesibilidad funcional ni toda la paleta histórica.

## Evidencia reproducible

- [Steps: cantidades, transiciones, variables y modos](composition-slots.v0.1.1.steps.json).
- [Pagination: comparación cromática, estados y cantidades](composition-slots.v0.1.1.pagination.json).
- [Charts: cantidades, transiciones y modos](composition-slots.v0.1.1.charts.json).
- [Charts final: cardinalidad de filas completas, transiciones y cuatro modos](composition-slots.v0.1.1.charts-rows.json). Esta evidencia sustituye el QA de los Slots de celdas iniciales de Progress, no el de Header.
- [Corrección de ancho Charts](composition-slots.v0.1.1.charts-correction.json).
- [Readback de nueve variables y dieciocho aliases](pagination-slot-state.v0.1.0.variables.json).
- [Retirada exacta de pruebas temporales y vistas retenidas](composition-slots.v0.1.1.cleanup.json).
- [Estado, contratos y mapeo de destino](../../implementations/figma/composition-slots.v0.1.1.state.json).

Capturas inspeccionadas: composición inicial Charts detectó track fijo al reducir ancho; captura posterior en 488:167 muestra corrección. Steps491:322 verificado después de añadir fondos inversos únicamente a las muestras On Primary; componentes no reciben fondos nuevos. Pagination499:313 muestra cinco defaults y ocho celdas Enabled/Disabled, sin solapamientos. Son los checks visuales finales; no se repitieron capturas sin cambios relevantes.

Corrección final de composición Charts: se retiraron las propiedades transitorias Legend row1/row2 y se creó Legend rows#502:0, Slots502:343/502:344, preservando los frames de fila213:135/213:148 y sus seis instancias. Una fila mide16 de alto, dos40 y cinco112 (gap8); Detail mide80/104/176 respectivamente. La captura final de488:167 muestra dos/cinco filas y cinco filas a320px. Las muestras de prueba de la estructura anterior se retiraron por IDs exactos, registrados en [build final](../../implementations/figma/composition-slots.v0.1.1.charts-rows-build.json).

## Limitaciones conservadas

1. Los Slots vacíos mantienen un placeholder de editor; no se define un estado vacío de producto.
2. Steps tiene composiciones independientes On White y Gallery On Primary por la excepción legacy; pasar a On Primary muestra sus tres elementos iniciales, volver a On White restaura los nueve personalizados. No se promete conversión automática de roles entre esos contextos.
3. Number/Step, selección de páginas y valores Charts siguen siendo presets/manuales. El 80% de Charts sigue siendo demostración sin cálculo.
4. En Pagination, insertar contenido conforme implica conservar los tokens contextuales y no fijar modos en hijos. Contenido externo arbitrario no recibe semántica correcta por magia del Slot. El selector «20 por pag» conserva su tratamiento original, incluso en Disabled.
5. Listas anchas no incorporan scroll, wrap ni límites inventados. Header Charts usa HUG; Detail trunca texto de leyenda a una línea. El relleno del gráfico es una muestra fija, no una proporción calculada.
6. La revisión cromática histórica de Charts sigue siendo un trabajo separado; este QA no la sustituye ni promueve automáticamente su contrato base.

## Incidente controlado

La primera prueba Pagination intentó establecer componentPropertyReferences en texto ya insertado como contenido personalizado. La API lo rechazó. La lectura posterior confirmó que el lote de muestras no persistió; se repitió el caso sin esa asignación inválida. No se reconstruyeron ni se duplicaron principales. Los datos conservados corresponden al lote exitoso.

No se modificó la fuente, no se publicaron componentes, no se tocó el inventario histórico ni los Slots validados el 29 de septiembre. Se retiraron únicamente pruebas temporales creadas por esta sesión; sus resultados e IDs permanecen en el registro. No hay decisión bloqueante nueva; las limitaciones quedan disponibles para auditoría por excepciones.
