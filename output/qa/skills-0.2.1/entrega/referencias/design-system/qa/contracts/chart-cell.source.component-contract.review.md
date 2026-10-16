# QA-CHART-CELL-SOURCE-001

- **Resultado:** `PASS` de evidencia fuente, no autorización del diseño destino.
- **Cobertura:** set `cell` 26/26 nodos, 13 variantes observadas (una vacía, doce con barra), 13 strokes punteados, doce fills de barra, ocho variables (seis locales/dos remotas), cero textos, instancias, estilos nombrados y reacciones.
- **Consistencia:** [MD](../../drafts/contracts/chart-cell.source.component-contract.md) y [YAML](../../drafts/contracts/chart-cell.source.component-contract.yaml) concuerdan en identidad, matriz, dimensiones, colores, radios, padding y límites. YAML parseado; 13 variantes y ocho variables conciliadas.
- **Límites:** 27 cruces cartesianos ausentes; color de barra atado a `color/brand/default` genérico; valor y semántica de datos no definidos. Fuente sin modificaciones.
