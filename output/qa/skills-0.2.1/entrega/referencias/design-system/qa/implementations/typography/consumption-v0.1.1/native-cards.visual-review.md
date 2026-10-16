# Typography 0.1.2 · aclaración de herencia

Revisión visual del 15 de octubre de 2026: **PASS acotado**. Se inspeccionaron las capturas posteriores a la escritura de las tarjetas `1006:672`, `1006:677` y `1006:682`: [Small](native-card-1.png), [Medium](native-card-2.png), [Count](native-card-3.png).

Los títulos, muestras, métricas, identificadores y descripciones aparecen completos, legibles en su escala documentada y sin recortes ni solapamientos. Las descripciones explican la receta efectiva para web y la herencia nativa en Figma, sin aplicar dos veces el factor. Cada tarjeta creció 22 px por Auto Layout para alojar una línea adicional. El tamaño diminuto de la muestra Count es la excepción existente documentada; esta revisión no modifica su receta ni generaliza su uso.

El [readback independiente](native-cards.after.json) comprueba tres tarjetas y ocho referencias, con cero desbordes. La [escritura](native-descriptions.apply.result.json) conservó las recetas de los 80 estilos locales, incluido el estilo histórico ajeno al catálogo vigente, y los estilos de los 11 textos editoriales modificados. Solo cambiaron tres descripciones de TextStyle y 11 textos de documentación. El catálogo normativo contiene 79 estilos; no se eliminaron estilos históricos.

Esta inspección valida las tarjetas modificadas. El consumo de componentes y los 79 estilos se acreditan mediante sus verificadores independientes; no se deduce de estas capturas.

## Precisión final de ámbitos de uso

Una revisión cruzada de las familias precisó dos prefijos: Dropdown Item Small a2/3 y Dropdown Item Medium/Select a5/6. Los dos TextStyles y sus tarjetas se actualizaron a la description canónica final, sin cambiar métricas, muestras ni dimensiones. El [readback](native-scope-clarification/cards.after.json), [QA de texto y geometría](native-scope-clarification/cards.qa.json) y las capturas finales [Small](native-scope-clarification/card-1.png) y [Medium](native-scope-clarification/card-2.png) pasan. Se inspeccionaron ambas imágenes: texto completo, sin recortes o solapamientos. Las imágenes anteriores permanecen como evidencia de la fase previa; Count no tuvo otra modificación.
