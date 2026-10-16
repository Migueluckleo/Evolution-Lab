# QA de recuperación de consumidores contextuales · 0.1.1

Esta revisión distingue conformidad tipográfica, preservación del cuadro de texto y preservación literal de la tinta renderizada. No cambia el resultado de ninguna llamada histórica ni declara validación global del archivo.

## Alcance y criterio

El [mapping 0.1.1](../../../../implementations/figma/typography.v0.1.1.mapping.json) y el [catálogo canónico](../../../../specs/tokens/ai-design-system.typography.v0.1.1.json) asignan tracking normal a 66 consumidores contextuales de Button. La vinculación del principal propagó temporalmente tracking `0.1%` a esos consumidores. Los preflights ordinarios detectaron la discrepancia. La recuperación usa las identidades explícitas de esos reportes y estilos ya existentes: 14 etiquetas Small→Compact Bold, 44 Medium→Normal y 8 Medium Underline→Normal Underline. No cambia familia, peso, tamaño, interlineado ni decoración.

El [preparador y sus límites](../../../../implementations/figma/typography.contextual-recovery.md) exigen receta completa e ID real de origen, hash de preservación original y dimensiones originales. Después de asignar el estilo por rango, verifican ID/receta de destino y vuelven a leer todos los nodos de la página, incluidos textos editoriales y contenido oculto. Un destino ya enlazado se consulta sin volver a asignarlo. Las mutaciones directas y las actualizaciones heredadas se contabilizan por separado.

## Resultados históricos conservados

| Familia | Etiquetas comprobadas | Setters directos / actualizadas por herencia | Conformidad canónica y preservación original del texto | Guard literal de página |
|---|---:|---:|---|---|
| FileUpload | 6 | 6 / 0 | PASS: sin errores posteriores de estilo, dimensiones o preservación | PASS con ledger geométrico acotado; exige lectura global independiente |
| Modal | 36 | 4 / 32 | PASS: sin errores posteriores de estilo, dimensiones o preservación | FAIL histórico: 36 diferencias del registro de nodo en las etiquetas; no se persistió el detalle de campos |
| Empty States | 16 | 8 / 8 | PASS: sin errores posteriores de estilo, dimensiones o preservación | FAIL histórico: 14 diferencias del registro de nodo; diez diagnósticos completos señalan únicamente `absoluteRenderBounds` |
| Conversation | 8 | 4 / 4 | PASS: sin errores posteriores de estilo, dimensiones o preservación | FAIL histórico: dos diferencias, ambas exclusivamente `absoluteRenderBounds`, documentadas por completo |

Fuentes directas: [FileUpload](contextual.394-122.apply.json), [Modal](contextual.565-122.apply.json), [Empty States](contextual.639-128.apply.json) y [Conversation](contextual.765-6.apply.json). Los reportes Modal, Empty States y Conversation siguen con `status:FAILED` y `pageGuard.status:FAIL`; `errors:[]` acredita que se completaron sin errores los controles posteriores de receta y preservación, pero no anula las violaciones independientes del guard. Se comprobaron las 66 etiquetas: 22 recibieron setters directos y 44 se actualizaron por herencia.

FileUpload leyó 752 nodos/230 textos antes y después; Modal 587/104; Empty States 559/32; Conversation 342/61. No hubo altas/bajas de nodos detectadas. Los IDs afectados por las violaciones Modal/Empty/Conversation son exclusivamente etiquetas del alcance. Sus contenedores y los demás nodos no produjeron violaciones. Esto no permite atribuir un campo exacto a una diferencia cuyo detalle no fue persistido.

## FileUpload: restauración geométrica medida

La [lectura previa](file-upload.contextual-geometry.json), el censo original y la [prueba en copia](file-upload.geometry-probe.json) justifican una única excepción: `I420:299;26:104` recupera ancho `122→121`, `x:8→9`, la misma traslación de un píxel en sus matrices y el cambio correspondiente de `absoluteBoundingBox`. El resto de sus propiedades permanece exacto. La caja del Button sigue en `154×32`; Dropzone y Success no cambian. La copia se [eliminó](file-upload.geometry-probe.cleanup.json), y la prueba verificó los originales intactos.

La llamada real de recuperación aplicó esas cinco tuplas exactas y obtuvo cero errores y cero violaciones en la página completa. No se permitió una tolerancia general de un píxel ni una excepción para otros ancestros.

## Empty States: tinta renderizada frente al cuadro de texto

Los diez diagnósticos completos persistidos muestran únicamente cambios en X/ancho de `absoluteRenderBounds`. Y y altura de la tinta permanecen exactas. Los cuadros de texto y su contenido conservan las medidas y los hashes del censo original; no aparecen errores de estilo, API/bindings ni cambios en los padres en ese reporte.

Por ejemplo, `I645:150;26:88` pasa de ancho de tinta `88.41610717773438` a `88.256103515625`, y X de `435.8681335449219` a `435.9481201171875`. El rango subrayado `I645:157;26:112` pasa de ancho `82.46310424804688` a `82.33514404296875`, y X de `438.7719421386719` a `438.8359375`. Los valores completos permanecen en el JSON; las diferencias aproximadas de `0.16/0.08px` y `0.128/0.064px` no se usan como tolerancias de QA.

La interpretación es **DERIVED**: restaurar tracking `0.1%→0` reduce la separación entre glifos y modifica la caja de tinta aunque el cuadro de texto conserve su tamaño. A 16px, cada intervalo aporta `0.016px` con tracking `0.1%`; los deltas observados son compatibles con esa corrección, incluida su representación float32. Es un efecto esperado de volver a la receta canónica, no una nueva receta ni una autorización de movimiento estructural.

Las cuatro etiquetas restantes con violación no tienen un detalle de campos persistido por el límite de diez diagnósticos. No se presenta su ink como preservado ni se convierte por inferencia el guard completo en PASS. El resultado de conformidad canónica se registra por separado.

## Límite de la evidencia Modal

La llamada Modal verificó los 36 destinos, dimensiones y hashes originales, y detectó diferencias únicamente en los registros de esas etiquetas. Esa versión del guard aún no devolvía valores de campos. El cambio de tinta al restaurar tracking es una explicación consistente con Empty States, pero para Modal sigue siendo **INFERRED**, no una observación completa de los 36 `absoluteRenderBounds`. Se conserva el FAIL literal histórico y no se repite una mutación para intentar cambiar ese resultado.

## Conversation: diferencia de tinta observada por completo

Las ocho etiquetas pasaron los controles posteriores de estilo, dimensiones y preservación. Solo dos produjeron diferencias del guard, y ambos diagnósticos están completos. Para `I766:186;765:355;26:92`, el ancho de tinta cambia de `103.96903991699219` a `103.77302551269531`, y X de `184.54759216308594` a `184.6455841064453`. Para `I766:186;765:356;26:104`, el ancho cambia de `139.3311767578125` a `139.07916259765625`, y X de `329.48309326171875` a `329.6091003417969`. Y y altura permanecen exactas.

No hay otros campos con diferencias en esos nodos, otros nodos afectados ni errores de receta. A 14px, restaurar `0.1%→0` elimina `0.014px` por intervalo; los cambios aproximados `0.196px` y `0.252px` de ancho son compatibles con esa restauración. Se conserva el FAIL literal de tinta; la conformidad canónica de las ocho etiquetas es PASS.

## Criterios finales separados

La solicitud exige tipografía canónica y estilos consumibles, no conservar el tracking heredado incorrecto. Por tanto, se evalúan tres resultados independientes:

1. **Conformidad canónica:** ID real de TextStyle, receta completa y bindings previstos por contrato/mapping. Las 66 etiquetas de este reporte pasan los controles posteriores de las llamadas, sin errores ni violaciones de estilo/binding. Este PASS acotado no cambia el estado de los 103 enlaces escalados pendientes.
2. **Preservación del contenido y estructura:** dimensiones y hash originales de las 66 etiquetas, más comparación de todos los nodos de cada página y el ledger explícito de FileUpload. La evidencia completa de FileUpload y Conversation permite separar la tinta de los demás campos; Modal y cuatro diferencias de Empty conservan la limitación de detalle indicada arriba. No se inventan registros históricos faltantes.
3. **Identidad literal de tinta:** compara `absoluteRenderBounds` sin tolerancias. Restaurar tracking cambia naturalmente la distribución de glifos, por lo que los FAIL históricos observados se mantienen. Ese criterio más estricto no transforma una receta correcta en incumplimiento tipográfico, ni permite ignorar movimientos de cajas, contenido, API o bindings.

El PASS canónico acotado y el FAIL histórico literal pueden coexistir. El censo final debe corroborar la conformidad de todos los consumidores y los límites globales se documentan por separado; esta interpretación no concede una excepción general de ink bounds al guard.

## Cierre pendiente

El censo final independiente debe corroborar los IDs de TextStyle, recetas, dimensiones y preservación de los 66 consumidores, junto con el resto del alcance. La evidencia de esta revisión no prueba identidad literal de toda la tinta ni sustituye la comprobación global. Los 103 rangos escalados siguen fuera de estas escrituras y con su bloqueo específico; esta recuperación no los valida.

La implementación local pasó 33 escenarios del guard y 25 de recuperación, además de parseo y SHA de los cuatro scripts generados. Esas pruebas de software respaldan la detección de alteraciones y la conservación de reportes ante proxies rematerializados; no reemplazan evidencia de Figma.

## Integridad de los reportes revisados

| Archivo | SHA256 |
|---|---|
| `contextual.394-122.apply.json` | `5f60a1ac4b4742f0721e9b975ef167d9ed2e1609e4a716f31f52cd96b0194cfc` |
| `contextual.565-122.apply.json` | `634e8af99cdebd5bd380192e3aecab8eb6640069e208167b0e3c4776dd0b291e` |
| `contextual.639-128.apply.json` | `a4adbcef60e386cdc3e97a95c4eed083637eac98d8f0b05bc9ff08fd570191c3` |
| `contextual.765-6.apply.json` | `413c762d8ef802b35009299793f45e10827e2e2faf0d43959f3cb6be1648c69d` |
