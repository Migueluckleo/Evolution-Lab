# QA fuente · Navigation / Tab

**Fecha:** 2026-09-24 · **Resultado:** `PASS` para inventario fuente; la preparación y construcción del destino se registran en QA separado.

La [evidencia MD](../../drafts/contracts/navigation-tab.source.component-contract.md) y el [YAML](../../drafts/contracts/navigation-tab.source.component-contract.yaml) fueron contrastados contra el set de la Librería anterior `1183:1146`. El recorrido cuenta 17 variantes, 132 nodos, 16 nodos ocultos, 33 instancias ImageSquare, 16 Dot y cuatro reacciones de hover. El YAML parsea y enumera las 17 variantes y cuatro reacciones. La captura del set se inspeccionó, incluidas las dimensiones Base 135×42 y Dynamic 133–136×35.

La matriz fuente no es cartesiana: `Selected` existe solo en Dynamic/On y tiene anatomía y bindings de propiedades distintos. Se documentan cinco usos semánticamente incompatibles de variables de origen y un efecto Focus de 2 px no tokenizado en la fuente. No se incorporaron como reglas al destino; la [especificación en specs](../../specs/navigation-tab.contract.v0.1.0.md) y el [QA Figma](../implementations/navigation-tab.v0.1.0.figma.review.md) registran su conciliación posterior.
