# Tipografía 0.1.2 · cierre de consumidores

Fecha: 2026-10-15. **PASS para el consumo tipográfico verificado**. Auditoría humana `PENDING`; biblioteca Figma sin publicar. Esta revisión sustituye el estado pendiente de los 103 rangos del [cierre histórico 0.1.1](typography.v0.1.1.review.md), conservando sus evidencias y límites.

## Resultado comprobado

| Alcance | Resultado |
|---|---|
| Consumidores Figma | 34 páginas, 3351 nodos UI y 3353 rangos: 3250 con TextStyle ID directo y 103 con herencia nativa comprobada. Cero rangos sin resolución. |
| Textos editoriales de las páginas de componentes | 150 preservados; no se confunden con textos UI. |
| Estilos compartidos | 79: 18 base y 61 complementarios necesarios. IDs, métricas y bindings conservados en 0.1.2. |
| Specs | 43 enmiendas de familia: 39 con consumo, cuatro sin texto UI. La enmienda 0.1.2 precisa el mecanismo nativo de Select, Dropdown Item, Header y App Shell. |
| Pilotos y temporales | Checkbox 2/3, Checkbox 5/6 y Count 4/3: tres pruebas A→B→A, 36 controles, originales preservados y todas las copias temporales retiradas. |

El [QA global](typography/consumption-v0.1.1/consumer-final.global.v0.1.2.json) concilia la [selección final de censos](typography/consumption-v0.1.1/consumer-final.selection.json), el [overlay de herencia](typography/consumption-v0.1.1/consumer-final.native-inheritance.v0.1.2.json) y el [QA independiente de los 79 estilos](../../implementations/figma/typography.v0.1.2.styles.qa.json). La selección es posterior a la última asignación de estilos a consumidores. Las escrituras posteriores afectan únicamente descripciones y documentación de Typography; los pilotos usaron copias y comprobaron preservación de originales.

## Herencia nativa y documentación

La [enmienda explícita](../../specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md) regula únicamente las 103 entradas comprobadas. Sus IDs locales permanecen vacíos, tal como devuelve Figma. La evidencia identifica el estilo del principal, la cadena real por API, la escala nativa, la receta efectiva y la ausencia de overrides tipográficos; no se inventaron IDs ni se asignó otra vez el estilo materializado a una instancia ya escalada.

La [evaluación de las 103 cadenas](typography/consumption-v0.1.1/inheritance103.review.md) recorre 242 rutas API, nueve textos principales y cinco componentes. Conserva seis fallos crudos de contraparte exterior y demuestra su frontera de contenido local en el Slot Options. Cada Checkbox interior conserva un principal real verificable. Las ocho pruebas del evaluador incluyen casos de rechazo de identidades, bindings y cadenas incorrectas.

Count pasó la [prueba causal completa](typography/consumption-v0.1.1/inheritance-count-four-thirds/evaluation.json). La lectura independiente posterior confirma restauración exacta y eliminación de las raíces temporales `1063:1392` y `1063:1414`. El bloqueo previo por límite de uso quedó resuelto al reanudar; su respuesta original permanece en el registro histórico.

Se sincronizaron tres descripciones de TextStyle, sus tres tarjetas y ocho textos de estado/referencia en [Typography de AI-Design-System](https://www.figma.com/design/tj3WIBEZDGLVs7MJWKCwgf/AI-Design-System?node-id=1003-412). La [lectura y revisión visual](typography/consumption-v0.1.1/native-cards.visual-review.md) no detectó recortes ni solapamientos. Las 80 recetas locales —79 vigentes y un estilo histórico conservado— permanecieron iguales durante la operación.

El [catálogo canónico 0.1.2](../../specs/tokens/ai-design-system.typography.v0.1.2.json) conserva una sola `description` por estilo. Web usa la receta materializada una sola vez; Figma verifica la relación nativa. Las skills resuelven esta diferencia mediante fuentes y evidencia, sin convertirla en una excepción automática para nuevas instancias.

## Límites conservados

Este PASS acredita tipografía y los controles de preservación capturados. El timeout histórico de Table impidió recuperar el guard completo de sus propiedades no textuales; el censo acredita sus 1446 rangos UI y la comparación externa preservó las otras 35 páginas. No se presenta ese guard perdido como PASS ni se promete ausencia de discrepancias ajenas al alcance comprobado.

Los FAIL históricos de comparación literal de tinta siguen disponibles: corregir tracking puede variar la tinta sin cambiar caja ni layout. El QA final distingue esos resultados de la receta tipográfica correcta. Tampoco equivale a aprobación humana o publicación remota.

La distribución de ambas skills, sus versiones, pruebas e instalación se registra en [skills.md](../../registry/skills.md). La vigencia estructural y semántica de Graphify se acredita en su propio cierre; esta revisión no la anticipa.
