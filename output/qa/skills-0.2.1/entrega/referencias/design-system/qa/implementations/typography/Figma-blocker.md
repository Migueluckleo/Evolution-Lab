# Bloqueo de vinculación tipográfica en Figma

**Fecha:** 2026-10-15 · **Destino:** `AI-Design-System`, `tj3WIBEZDGLVs7MJWKCwgf` · **Resultado:** `BLOCKED` para la aplicación estable de TextStyles a los componentes existentes.

La aplicación de un TextStyle a textos existentes de Button produce cambios posteriores en otros textos que comparten una referencia de propiedad de componente. Una lectura inmediatamente después de cada asignación puede coincidir con lo esperado y dejar de coincidir tras asignar el siguiente estilo. Por ello, el catálogo creado y los resultados locales por iteración **no acreditan una migración de componentes Figma `VALIDATED`**. La restauración ya se contrastó contra el censo completo: la preservación de métricas, contenido y propiedades capturadas pasa; la igualdad literal histórica sigue fallando por adiciones canónicas de bindings, documentadas por separado.

Este informe registra evidencia de ejecución, no modifica requisitos tipográficos ni aprueba una reconstrucción. Sigue la separación entre evidencia, restauración y validación de [P06](../../../protocols/06-QA-AND-VALIDATION.md). La causa interna del comportamiento compartido de Figma sigue `UNRESOLVED`; su asociación con `componentPropertyReferences` es una observación reproducida, no una explicación confirmada del motor.

## Alcance y fuente esperada

El [mapping derivado](../../../implementations/figma/typography.v0.1.0.mapping.json) cubre 34 páginas, 3,501 nodos y 3,503 rangos del censo. Su alcance UI comprende 3,351 nodos y 3,353 rangos; los 150 textos editoriales históricos quedan fuera de la aplicación. `READY_FOR_APPLICATION` y cero rangos sin receta describen la cobertura del plan, no el estado real de Figma.

El [catálogo canónico](../../../specs/tokens/ai-design-system.typography.v0.1.0.json), SHA-256 `2b47811d3175b801f41e32e3bb174060697e7c265053741541bf7e602700afed`, contiene 75 estilos: 18 base, 54 complementarios de compatibilidad y tres derivados de escala documentada. El [QA del catálogo](../../../implementations/figma/typography.v0.1.0.styles.qa.json) es `PASS`: 75 definiciones, 304 bindings semánticos y 1,216 resoluciones de aliases en cuatro modos. El [estado de creación](../../../implementations/figma/typography.v0.1.0.styles.state.json) y su [readback](../../../implementations/figma/typography.v0.1.0.styles.readback.json) conservan la trazabilidad. Este resultado no demuestra que todos los consumidores mantengan aplicado el nuevo estilo.

## Hechos comprobados en los archivos de ejecución

| Control | Resultado y alcance | Evidencia |
|---|---|---|
| Estado previo de Buttons | 60 textos. `26:84`, dentro del componente `26:82` del set `26:81`, tiene Manrope Bold 16 px, interlínea 20 px, tracking `0.10000000149011612%`, caja 58 × 20 y `textStyleId` vacío. | [Censo anterior de Buttons](../../../sources/figma-snapshots/typography/census.before.0-1.json) |
| Primera asignación a maestros | `FAIL`: 60 errores `STYLE_MISMATCH`; las métricas podían conservarse mientras el ID de estilo seguía vacío. | [masters.0-1.json](masters.0-1.json) |
| Lectura inmediata del reintento | 60 textos comprobados y cero errores en esa ejecución. Ese alcance temporal resulta insuficiente para afirmar estabilidad del conjunto. | [masters.0-1.retry.json](masters.0-1.retry.json) y [plantilla de aplicación](../../../implementations/figma/typography.v0.1.0.apply.template.js) |
| Lectura/aplicación posterior del conjunto | `FAIL`: 78 errores en 39 textos, repartidos entre `GEOMETRY_CHANGE` y `STYLE_MISMATCH`. Hay cambios de 16 a 14 px y de 58 a 51 px de ancho. | [consumers.0-1.0.json](consumers.0-1.0.json) |
| Intento anterior de recuperación | `FAIL`: 55 textos discrepantes entre 60 procesados. En `26:84`, el readback indica Bold 14 px y caja 51 × 20 frente a Bold 16 px y 58 × 20 esperados. Este archivo **no** es prueba de restauración exitosa. | [buttons.recovery.json](buttons.recovery.json) |
| Restauración posterior de Buttons | `PASS` acotado al readback de restauración: 60 IDs originales procesados, `errors: []`. La plantilla realiza la comparación después de completar las escrituras; restaura las métricas anteriores, no certifica nuevos TextStyles. | [restored.0-1.json](restored.0-1.json) y [plantilla de restauración](../../../implementations/figma/typography.v0.1.0.restore.template.js) |
| Reproducción en copia temporal | `FAIL`: set temporal `996:412`, 60 textos, 190 discrepancias de campo en 55 textos (`font`, `size`, `width`, `decoration`, `styleId`). `originalsUnchanged: true` corresponde a esta prueba aislada. | [shared-format.isolated-copy-qa.json](shared-format.isolated-copy-qa.json) |

Los números de errores son comprobaciones fallidas, no el número de familias afectadas. No se extrapola el defecto a todos los componentes; el fallo reproducido en una familia ya impide validar globalmente la operación solicitada.

## Pruebas de aislamiento

La ejecución principal realizó las siguientes pruebas de aislamiento. Las pruebas de desvinculación y propiedad nueva utilizan la copia temporal `996:412`; la muestra de componentes nuevos tiene IDs propios:

1. Restablecer `characters` no eliminó el comportamiento compartido. Es una observación comunicada por la ejecución principal; este corte no contiene un readback separado de ese intento y no le atribuye un control `PASS`.
2. Vaciar temporalmente `componentPropertyReferences` antes de aplicar los estilos permitió mantener los 60 textos con su estilo correspondiente: `beforeRebindFailures: []`. [Readback de desvinculación](shared-format.unbind-probe.json).
3. Reasignar las referencias de propiedad hizo que los textos volvieran a adoptar el último estilo aplicado; el readback enumera 45 textos discrepantes en `afterRebindFailures`. [Readback de revinculación](shared-format.unbind-probe.json).
4. Crear otra definición común de propiedad, `Isolated label test#997:0`, dejó 45 textos discrepantes. [Readback de propiedad nueva](shared-format.new-property-probe.json).
5. Dos componentes con nodos Text creados desde cero sí mantuvieron estilos distintos en las dos etapas de la prueba reducida: `995:419` Bold y `995:420` Regular, ambos con referencia `Label#995:3`. [Readback de componentes nuevos](shared-format.new-components-probe.json).

Estos resultados son observaciones de diagnóstico; no autorizan quitar las propiedades públicas de Button ni sustituir sus nodos. La prueba de dos componentes nuevos tampoco demuestra preservación de las 60 variantes, sus instancias y sus overrides. El [readback inicial de la copia](shared-format.isolated-copy-qa.json) solo acredita su propio fallo y la ausencia de cambios en los originales durante esa prueba; los readbacks posteriores conservan su alcance específico.

El último [ensayo de sustitución de textos en una copia de Button](button-repair-proposal.json) también terminó en `FAIL`: el archivo persistido contiene 12 discrepancias en seis textos (`decoration`, `size`, `w`, `styleId`) entre 60 textos comprobados. Conservó las definiciones de propiedades y dejó los originales sin cambios (`componentDefinitionsPreserved: true`, `originalsUnchanged: true`), pero no preservó todo lo requerido. La [limpieza posterior](button-repair-proposal.cleanup.json) registra 364 IDs eliminados de la prueba; la [limpieza de los experimentos de formato compartido](shared-format.cleanup.json) registra otros 374 IDs. Los `removedNodeIds` del ensayo original identificaban únicamente los textos reemplazados dentro de la prueba; se conserva la respuesta de limpieza separada. **No hay una propuesta de reparación lista para aplicar ni para presentar como validada.**

## Restauración completa y diferencia histórica conservada

El [QA de preservación](../../../implementations/figma/typography.v0.1.0.preservation.qa.json) es `PASS` sobre 3,501 textos y 3,503 rangos de las 34 páginas originales: compara 3,351 textos UI y 150 editoriales, no registra cambios de segmentación, conserva los 3,503 IDs de estilo previos y obtiene igualdad de los 3,501 fingerprints de propiedades capturadas. Preserva métricas, contenido, formato, dimensiones, IDs y bindings existentes dentro de ese alcance.

El [QA de restauración literal](../../../implementations/figma/typography.v0.1.0.restoration.qa.json) permanece `FAIL`, con 244 diferencias de `boundVariables`. El [desglose](../../../implementations/figma/typography.v0.1.0.restoration.binding-differences.json) y el QA de preservación identifican adiciones canónicas en 244 rangos de 242 nodos, procedentes de 17 TextStyles reutilizados; suman 1,202 referencias añadidas. El control complementario verifica esas adiciones contra el catálogo y sus bindings reales. No se elimina el fallo histórico ni se lo presenta como igualdad literal.

La revisión cubre las propiedades capturadas: sus fingerprints no criptográficos no prueban identidad sin posibilidad de colisión; el censo mide ancho y alto del texto, no todas las posiciones de frames ni el recorte renderizado de cada componente. La nueva documentación Typography queda fuera del censo original. La preservación `PASS` no acredita consumo integral del nuevo catálogo: `componentMigration` sigue `BLOCKED` y la auditoría humana, `PENDING`.

## Catálogo y página Typography

La [página Typography](https://www.figma.com/design/tj3WIBEZDGLVs7MJWKCwgf/AI-Design-System?node-id=1003-412) queda disponible como documentación de foundations. Su [readback final](specimens.readback.json) es `PASS`: 75 tarjetas de estilos, 316 textos y 79 frames, con cero errores. La [revisión visual](specimens.review.md) registra las dos capturas inspeccionadas y sus límites.

El [estado inicial de la construcción](../../../implementations/figma/typography.v0.1.0.specimens.state.json) conserva `READBACK_FAILED` y 75 comprobaciones fallidas de `cornerRadius`. Fue un falso negativo del verificador: Figma expone el binding en `topLeftRadius`, `topRightRadius`, `bottomLeftRadius` y `bottomRightRadius`, todos vinculados a `VariableID:13:6` y resueltos en 8 px. La lectura posterior con esa representación correcta pasa. El archivo histórico no se reescribe y el resultado de la página no cambia el bloqueo de los componentes.

## Las tres recetas escaladas son un asunto distinto

La prueba de herencia del contador de AppShell preservó la geometría y la escala `1.3333333730697632`, con `differences: []` y `overrides: []`, pero mantuvo `textStyleId: ""` en `I737:305;522:408;183:164;155:137`. Véanse el [respaldo anterior](scaled-counter.pre-inheritance.json) y el [readback de herencia](scaled-inheritance.readback.json). La ausencia de overrides directos no prueba consumo de un TextStyle.

Las únicas tres ampliaciones de catálogo necesarias para ese problema ya están documentadas en el JSON canónico:

| ID lógico derivado | Consumo existente | Escala original de instancia |
|---|---|---:|
| `ui-checkbox-label-scaled-two-thirds` | 14 rangos de Checkbox | `0.6666666865348816` |
| `ui-checkbox-label-scaled-five-sixths` | 76 rangos de Checkbox | `0.8333333134651184` |
| `micro-count-small-scaled-four-thirds` | 13 rangos de Count en Header/AppShell | `1.3333333730697632` |

Su evidencia de escala está en [Checkbox](../../../sources/figma-snapshots/typography/scaled-instance-evidence.json) y [Header](../../../sources/figma-snapshots/typography/header-scaled-instance-evidence.json). El mapping separa `instanceScale` de `recipeScale = expectedScale = 1`: aplica la receta materializada sin multiplicarla otra vez. Las tres recetas no resuelven el comportamiento compartido de propiedades observado en Button. Este bloqueo no justifica más estilos ni un rediseño de tamaños, pesos, interlíneas o tracking.

## Decisión y condiciones de cierre

- **Aplicación Figma: `BLOCKED`.** Los fallos observados se conservan como `FAIL`; no se convierten en `PASS` por existir el catálogo, el mapping o una lectura inmediata favorable.
- **Restauración completa: preservación `PASS`, igualdad literal `FAIL`.** Se compararon los 3,501 textos y 3,503 rangos de las 34 páginas. Las 244 adiciones canónicas de bindings quedan explícitas; no se ocultan bajo el resultado de preservación.
- **Catálogo y página Typography: `PASS` en su alcance documentado.** Los 75 estilos y la documentación están disponibles; la migración de componentes sigue pendiente.
- **Web: resultado independiente.** El [QA de 75 estilos](web/revision-75/README.md) conserva su alcance y no acredita aplicación en Figma.
- **Sustitución de nodos Text: ensayo fallido, ninguna propuesta lista.** No se aplicó como solución a los maestros. Cualquier alternativa futura requiere demostrar preservación y evaluar el cambio de IDs, referencias de propiedades, overrides de instancias, bindings, segmentos y geometría antes de plantear su autorización.
- **Revalidación necesaria.** Después de cualquier solución autorizada, leer todo el conjunto afectado tras la última escritura y comparar contra el censo, el mapping y los IDs reales de estilos; incluir instancias consumidoras y los rangos ocultos. Verificar identidad, propiedades, contenido, segmentos, bindings, medidas y estilos. El resultado favorable de una iteración individual no sustituye esta lectura final.

La aplicabilidad de Slots es `NOT_APPLICABLE` para este informe de diagnóstico, que no cambia contenido variable ni composición. Una eventual sustitución de nodos deberá revisar las dependencias afectadas de nuevo. Este registro añade solo evidencia y límites de implementación; mantiene el catálogo canónico y los contratos vigentes.
