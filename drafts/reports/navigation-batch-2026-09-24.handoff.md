# Handoff · Navigation, 2026-09-24

**Alcance ejecutado:** migración delegada de las subfamilias `Pagination` y `Tab` desde la página Navigation de la Librería anterior a la página existente `Navigation` de `AI-Design-System`. `Switch Tab Item` y `Switch Tab` ya estaban cerrados técnicamente y no se reconstruyeron otra vez. El archivo fuente se leyó sin escribirle.

## Contratos y extensiones

- [Pagination](../../specs/navigation-pagination.contract.v0.1.0.md): cinco variantes, siete propiedades; [estado Figma](../../implementations/figma/navigation-pagination.v0.1.0.state.json), [QA](../../qa/implementations/navigation-pagination.v0.1.0.figma.review.md). Un rol nuevo de borde específico con [JSON](../foundations/ai-design-system.navigation-pagination-border.v0.1.0.json) y [enmienda](../../specs/foundations.navigation-pagination-border.amendment.v0.1.14.md).
- [Tab](../../specs/navigation-tab.contract.v0.1.0.md): 17 variantes, diez propiedades, cuatro reacciones hover observadas; [estado Figma](../../implementations/figma/navigation-tab.v0.1.0.state.json), [QA](../../qa/implementations/navigation-tab.v0.1.0.figma.review.md). Dos roles de borde nuevos con [JSON](../foundations/ai-design-system.navigation-tab-borders.v0.1.0.json) y [enmienda](../../specs/foundations.navigation-tab-borders.amendment.v0.1.15.md).

## Evidencia y comprobaciones

Se inspeccionaron los sets fuente `2461:714` y `1183:1146` con estructura completa, capturas, propiedades, variables y reacciones. Sus contratos observacionales MD/YAML permanecen en `drafts/contracts/`. En el destino se leyó de vuelta la página `275:122`, Pagination `297:454` y Tab `316:200`. Las variables nuevas usan aliases a primitivas aprobadas, no colores hardcodeados. Pagination: 125/125 pinturas con binding, cinco variantes, 25 iconos y cero reacciones. Tab: 107/107 pinturas con binding, 17 variantes, 33 iconos, 16 Dot, ocho divisores y cuatro reacciones exactas. JSON y YAML parsean.

## Excepciones y estado

En Tab, la fuente usa roles semánticos incorrectos en cinco lugares; se mapearon a roles correctos conservando el RGB. `Dynamic/On/Selected` mantiene su anatomía excepcional sin crear combinaciones nuevas. El desplazamiento inicial de 1 px en Dynamic/Off/Hovered se corrigió con un contorno absoluto vinculado al mismo token: el contenido y la geometría ya coinciden con la fuente. El número anidado de Dot conserva el tamaño fuente literal de 8 px porque el JSON aprobado no tiene primitiva de ese tamaño; color, familia y peso son locales. Las tres keys de Caret locales de Pagination se sustituyeron por variantes Phosphor publicadas de la misma forma, con keys de destino registradas. Ninguna excepción requiere una decisión de producto antes de continuar otras familias.

Los cuatro contratos/enmiendas están en `specs/` con estado `DELEGATED_FOR_BUILD`. Ambas implementaciones tienen QA técnico `PASS`, auditoría humana `PENDING` y biblioteca Figma `UNPUBLISHED`. No se atribuye aprobación humana ni conformidad web.

## Siguiente frente

`Scrollbar` aún no tiene contrato en este repositorio ni implementación registrada; la Librería anterior lo contiene en la página `3910:928`, con el set principal `7664:49488` de ocho variantes y subpartes adicionales. Empezar por inventariar la composición y dependencias, producir MD/YAML y contrato de destino con mapa al JSON aprobado, después construir en su página semántica y hacer QA propio. Evitar otra ronda general de revalidación retroactiva antes de ese trabajo; el seguimiento de familias ya construidas permanece en la matriz de trazabilidad y auditoría por excepciones.
