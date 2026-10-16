# QA técnico · Scrollbar 0.1.0

**Fecha:** 2026-09-24 · **Resultado histórico:** `PASS` técnico antes del cambio de color; `STALE` para el estado actual desde [QA 0.1.1](scrollbar.v0.1.1.figma.review.md) · **Contrato:** [Scrollbar](../../specs/scrollbar.contract.v0.1.0.md) · **Auditoría humana:** `PENDING` · **Publicación Figma:** `UNPUBLISHED`.

| Criterio | Evidencia de lectura posterior |
|---|---|
| Identidad | Página exclusiva `Scrollbars` `328:122`, set público `Scrollbar` `330:194` y cuatro sets internos `Scrollbar Thumb / 25%`, `/ 33%`, `/ 50%`, `/ 75%`. El archivo fuente quedó read-only. |
| Variantes | Ocho públicas 2×4 y 22 internas 8+6+4+4; ninguna posición no observada añadida. Orientación y tamaño de una instancia temporal cambiaron al destino esperado, y tres pruebas de posición/orientación internas pasaron; las instancias temporales se eliminaron. |
| Geometría pública | Vertical 14×280 px y horizontal 280×16 px; ocho instancias locales, espesor de 6 px y longitudes 70, 90.6667, 136 y 240 px en ambas orientaciones. Padding de 4 px vinculado a `spacing/xs`; radio `radius/full` da la misma cápsula visible que el radio fuente de 3–4 px sobre un grosor de 6 px. |
| Color | 30/30 thumbs con fill local `color/background/scrollbar/thumb`, scope `SHAPE_FILL`; cuatro aliases a primitiva local `#C3C6D4` concuerdan con el [JSON](../../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.0.json). Cero issues de binding, cero reacciones. |
| Visual | Capturas del set público fuente y destino inspeccionadas: cuatro barras verticales y cuatro horizontales, longitudes, track transparente y gris original comparables. La disposición en la página destino es más legible sin alterar el tamaño de cada variante pública. |

**Transformaciones explícitas:** los cuatro sets internos se normalizaron a un recorrido local de 272 px, que es el recorrido visible del set público, en vez de los 280 px de los sets internos fuente. Las variantes horizontales tienen geometría horizontal real, no instancias giradas. Para 25% se distribuyeron las posiciones intermedias sobre los 202 px libres para no desbordar el nuevo recorrido. Las longitudes y primera posición públicas permanecen iguales. El rótulo fuente `75%` se conservó, aunque 240/272 ≈ 88.24%; no se presenta como porcentaje funcional. Estos puntos siguen en auditoría humana, pero no son desviaciones ocultas respecto del contrato delegado.

No se validan drag, scroll real, teclado, ARIA, contraste sobre todo fondo ni publicación de biblioteca.
