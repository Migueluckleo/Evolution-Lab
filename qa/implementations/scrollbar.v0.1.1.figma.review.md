# QA técnico · Scrollbar 0.1.1

**Fecha:** 2026-09-24 · **Resultado:** `PASS` técnico contra [enmienda cromática](../../specs/scrollbar.color-approximation.amendment.v0.1.1.md) y [contrato base](../../specs/scrollbar.contract.v0.1.0.md) · **Auditoría humana:** `PENDING` · **Biblioteca Figma:** `UNPUBLISHED`.

| Criterio | Evidencia |
|---|---|
| Estructura conservada | Set público `330:194` con ocho variantes, cuatro sets internos con 22 variantes y ocho instancias locales; sin cambios de nodos, propiedades ni geometría pública desde [QA estructural 0.1.0](scrollbar.v0.1.0.figma.review.md). |
| Binding actualizado | Los 30 thumbs conservan fill ligado a `color/background/scrollbar/thumb`, no a la primitiva. La variable semántica aliasa neutral/300 en los cuatro modos y su scope es `SHAPE_FILL`; cero fallos en el recorrido explícito de componentes e instancias. |
| Captura | Nueva captura del set público muestra las mismas longitudes y posiciones con `#E2E8F0`, más claro que el `#C3C6D4` original. Esta diferencia está autorizada y documentada, no se califica como fidelidad cromática exacta. |
| Estado | La primitiva creada inicialmente no figura entre las variables locales activas. JSON 0.1.1, Figma y la enmienda vigente coinciden. Cero reacciones añadidas; la prueba de variantes anterior no fue afectada por el cambio de alias. |

**Limitaciones `*`:** el contraste del thumb sobre blanco baja de 1.70:1 fuente a 1.23:1 destino. Revisar internamente si el thumb debe cumplir 3:1 como información visual indispensable. El rótulo `75%` sigue siendo nominal e inexacto; el usuario lo consideró de baja prioridad. No se valida scroll funcional ni accesibilidad web.
