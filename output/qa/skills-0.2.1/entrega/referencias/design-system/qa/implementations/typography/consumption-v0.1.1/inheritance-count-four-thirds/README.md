# Piloto causal Count4/3

Resultado: **CAUSAL_INHERITANCE_SUPPORTED_FOR_THIS_PILOT**. Los12 controles están en [evaluation.json](evaluation.json); el alcance es un consumidor, sin aprobación normativa implícita.

Se conservaron dos raíces temporales: el conjunto Dot y la instancia IconButton que contiene Count. El principal fuente155:136/texto155:137 recibió su contraparte copiada, obtenida por API y children reales; el control155:135 pertenece a otra variante del mismo conjunto. La copia conservó métricas, propiedades, referencias y relaciones. Solo se normalizaron dos entradas redundantes observadas de overrides `layoutPositioning/name` con valores iguales al original, IDs exactos y main verificado; el diagnóstico y el fallo inicial se conservan.

A `micro-count-small` → B `ui-metric-value-small` → A restaurado se aplicó únicamente al texto principal copiado. B propagó a Count tamaño26.666667938232422, Regular400, interlineado32px y tracking0px, mientras el ID local permanecía vacío. A restaurado recuperó5.333333492279053, Bold700, interlineado160.0000023841858% y tracking−2%.

Los tres readbacks independientes no registran issues; controles, guards de originales y relaciones permanecieron iguales. La observación A restaurada coincide exactamente con A y sus hashes completos internos. La limpieza terminó `CLEANUP_COMPLETE`. Los datos transportados omiten filas enormes de geometry/componentProperties y conservan sus hashes completos; las comparaciones internas continuaron usando las filas completas.

La [evaluación103](../inheritance103.evaluation.json) combina este piloto con los otros dos y las cadenas API completas. El ID vacío se conserva como hecho observado, no se reemplaza por un ID fabricado.
