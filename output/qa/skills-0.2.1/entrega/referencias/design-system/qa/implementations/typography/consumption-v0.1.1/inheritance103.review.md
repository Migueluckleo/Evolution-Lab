# Evidencia de herencia nativa · 103 rangos

**QA de evidencia: PASS.** La [evaluación reproducible](inheritance103.evaluation.json) verifica103 rangos en3 páginas,242 rutas API,9 textos principales en5 componentes y3 pilotos causales con36 controles. Conserva103 IDs locales vacíos,0 overrides tipográficos de instancia y los factores nativos14×2/3,76×5/6 y13×4/3. Este resultado no modifica contratos ni convierte una observación en aprobación.

El [verificador](../../../../implementations/figma/typography_inheritance_qa.py) ensambla las6 partes crudas del [suplemento preservado](../continuation-2026-10-15/typography-inheritance-supplement-v3/audit.js), comprueba fingerprints y el mapping fuente, y exige cobertura exacta. Para cada rango coteja la instancia más cercana, su `getMainComponentAsync`, la ruta real de hijos al principal, su TextStyle ID canónico, sus bindings exactos, receta efectiva y escala. Recorre todas las cadenas de ancestros y sus contrapartes; no reconstruye IDs mediante sufijos ni multiplica escalas de ancestros.

Los6 `COUNTERPART_PATH_MISSING` originales permanecen en `rawIssues`. Afectan a contenido local adicional en índices5/6/7 de la instancia467:1052. La instancia `I467:1052;456:440` y el principal456:440 son nodos API **SLOT**, ambos con `slotContentId: Options#466:0`. [COMPOSITION-SLOTS-001](../../../../specs/composition-slots.amendment.v0.1.0.md) permite insertar, quitar, reordenar y sustituir opciones; la muestra de5 no define un máximo. El verificador clasifica44 rutas que cruzan esa frontera, conserva los6 fallos de contraparte exterior y no utiliza vecinos del mismo índice como identidad. Cada Checkbox interior sí acredita su principal canónico mediante su propio vínculo real.

Los pilotos [Checkbox5/6](inheritance-checkbox-five-sixths/evaluation.json), [Checkbox2/3](inheritance-checkbox-two-thirds/evaluation.json) y [Count4/3](inheritance-count-four-thirds/evaluation.json) efectuaron A→B→A únicamente sobre principales copiados. Los readbacks independientes confirman propagación, controles estables, guards de originales iguales y restauración exacta; las tres limpiezas terminaron correctamente. El ID local de los textos escalados permaneció vacío durante los cambios causales.

Validación local ejecutada:

```sh
python3 -B implementations/figma/typography_inheritance_qa.py --self-test
python3 -B implementations/figma/typography_inheritance_qa.py --output qa/implementations/typography/consumption-v0.1.1/inheritance103.evaluation.json
```

[Ocho pruebas](inheritance103.self-test.log) pasan: alcance real y rechazo de main erróneo, override tipográfico, frame llamado Slot, binding de instancia nuevo, binding principal de identidad distinta, principal sin ID y parte de transporte ausente.

El overlay final debe añadir la selección vigente de34 censos, preservación de3250 rangos directos/150 editoriales, QA del catálogo79 y activación explícita de la enmienda. Esta evaluación deja intactos el mapping0.1.1 y su checker estricto histórico.
