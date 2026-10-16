# QA técnico · Navigation / Pagination 0.1.0

**Fecha:** 2026-09-24 · **Resultado:** `PASS` técnico · **Contrato:** [Navigation / Pagination](../../specs/navigation-pagination.contract.v0.1.0.md) · **Auditoría humana:** `PENDING` · **Publicación Figma:** `UNPUBLISHED`.

| Criterio | Evidencia verificada |
|---|---|
| Identidad y ubicación | Un set `Pagination` en la página `Navigation` de `AI-Design-System`: set `297:454`, página `275:122`. No se escribió en la Librería fuente. |
| Variantes y tamaño | Cinco variantes `Default`, `Active`, `Hover`, `Focus`, `Disabled`, cada una 354×66 px, Content 306 px y Pages 116 px. El set está separado espacialmente de Switch Tab Item y Switch Tab. |
| Anatomía | Cinco instancias de Caret por variante, 25 en total; controles primero/último ocultos por defecto; ninguna instancia desprendida. |
| Propiedades | Un eje `State` y seis propiedades de texto/visibilidad: `Page 1`, `Page 2`, `Page 3`, `Items per page`, `Show first control`, `Show last control`. Una instancia temporal cambió los cuatro textos y mostró ambos controles; lectura posterior correcta y prueba retirada. |
| Tokens y semántica | 125/125 pinturas con variables locales; cero bindings de categoría o scope equivocados. El borde específico de Pagination usa `VariableID:290:122` con cuatro aliases de primitivas; 25 textos contienen 75 aliases de familia, peso y tamaño. Los paddings principales conservan sus aliases. |
| Estados | Página 1 cambia solo según la fuente; Focus usa `color/focus/ring` y `stroke/md` de 2 px. Disabled atenúa páginas, elipsis y control siguiente; el selector conserva la apariencia fuente. |
| Visual e interacción | Capturas del set fuente y destino comparadas; geometría y colores de los cinco estados concordantes. Cero reacciones. |

La fuente contiene 146 nodos, diez frames ocultos y 31 variables; el contrato fuente conserva esa observación. Las keys locales de CaretDoubleLeft, CaretDoubleRight y CaretDown no eran importables; se usaron las variantes Phosphor publicadas del mismo nombre y peso, sin fingir identidad de key. Las teclas, cálculo de páginas, navegación real y accesibilidad web quedan fuera del alcance documentado.

La primera lectura detectó una contracción de 64 px en las cuatro celdas de página por auto layout; se corrigió antes de crear los otros estados. La lectura de Focus detectó 1,5 px por `stroke/sm`; se corrigió a `stroke/md` de 2 px. La comparación de capturas también detectó fondos blancos visibles en las instancias Caret importadas: las 25 pinturas quedaron ocultas, como en la fuente, sin eliminar sus aliases ni desprender las instancias. La captura final ya no presenta ese rectángulo blanco. Ninguna de las tres discrepancias permanece.
