# QA de inventario fuente · Scrollbar

**Fecha:** 2026-09-24 · **Resultado:** `PASS` observacional; no es aprobación del diseño destino.

| Control | Evidencia |
|---|---|
| Alcance | Página fuente `3910:928` leída sin escritura; cinco sets, 30 variantes y 125 nodos de componente recorridos. MD y YAML separan set público de cuatro sets internos. |
| Variantes | Ocho variantes públicas 2×4 y 22 internas 8+6+4+4, sin inferir combinaciones adicionales. |
| Geometría | Vertical 14×280, horizontal 280×16; espesores de 6 px; longitudes y posiciones registradas por familia. La captura del set público verifica que la rotación interna se muestra horizontal. |
| Color | 30 thumbs con el mismo RGB `#C3C6D4`, sin binding fuente; track transparente. La variable de destino aún no se atribuye a la fuente. |
| Excepciones | El rótulo `75%` no concuerda con longitudes 240/272 y 248/280; la segunda posición interna usa radio 4. Se conserva como observación, no como cálculo funcional. |
| Interacción | Cero reacciones; no se deducen drag, teclado, ARIA ni estado disabled. Las descripciones genéricas de Button en la documentación de página no se transfieren al contrato. |

**Siguiente fase:** contraste con inventario de tokens y QA documental del contrato destino; auditoría humana posterior de la anomalía 75%.
