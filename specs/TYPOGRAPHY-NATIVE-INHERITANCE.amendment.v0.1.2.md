---
contract_schema: sdd-project/0.2
contract_id: TYPOGRAPHY-NATIVE-INHERITANCE-001
name: Consumo tipográfico mediante herencia nativa de instancia
version: 0.1.2
type: amendment
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
review_targets: [figma, web]
slot_applicability: NOT_APPLICABLE
implementation_validation: VALIDATED
amends: specs/foundations/typography.contract.v0.1.0.md
data_refs:
  - specs/tokens/ai-design-system.typography.v0.1.2.json
supersedes_scope: Mecanismo verificable de vínculo de 103 rangos escalados, sin cambios de recetas ni sustitución de los 3250 rangos directos
---

# Consumo tipográfico por herencia nativa · enmienda0.1.2

## Autoridad y límite

La [delegación específica](../registry/DEC-TYPOGRAPHY-STYLES-001.md) y su continuación explícita autorizan documentar e integrar los estilos de todos los componentes. Esta enmienda resuelve técnicamente el mecanismo de consumo de 103 rangos ya censados; no registra aprobación humana del detalle, que sigue `PENDING`. La procedencia de las observaciones es `OBSERVED` y su interpretación técnica `DERIVED`. La regla no acredita por sí misma su aplicación. El estado inicial `VALIDATION_PENDING` se cerró mediante la evidencia exigida por rango y el QA global posterior enlazados al final; la validación se limita a esos consumidores.

El [catálogo 0.1.2](tokens/ai-design-system.typography.v0.1.2.json) conserva 79 estilos,18 base y61 complementarios. Sus métricas, unidades, nombres, IDs, bindings, decoración, factores y ámbitos de consumidor son idénticos a0.1.1. Cambia únicamente la explicación de uso y motivo técnico de tres recetas materializadas, una frase de codificación y metadatos de procedencia. No crea otra tipografía ni una escala alternativa. `description` sigue siendo el único propietario del uso; este documento regula el vínculo y su prueba.

## Sustituciones expresas

Las fuentes históricas permanecen intactas. Esta enmienda sustituye solamente:

| Fuente y versión | Requisito sustituido en el subconjunto103 |
|---|---|
| [Foundation 0.1.0](foundations/typography.contract.v0.1.0.md) | REQ-TYP-004, AC-TYP-004 y §3 «Derivados necesarios para instancias escaladas»: exigir el ID local del estilo materializado como única prueba de consumo. Conserva las fórmulas y todas las métricas. |
| [Formato 0.1.1](foundations/typography.formatting.amendment.v0.1.1.md) | Selección del catálogo y párrafo de `UNRESOLVED_SCALED_LINK` en «Evidencia y técnica de aplicación», exclusivamente cuando el overlay y la evidencia posterior satisfagan esta enmienda. Los27 rangos UNDERLINE y la técnica por rango continúan vigentes. |
| [Consumo transversal 0.1.0](TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) | TYC-01 y TYC-06: diferencia entre identidad métrica derivada y vínculo nativo al estilo principal en103 entradas. Las43 familias, restantes asignaciones y reglas de preservación no cambian. |
| [Select 0.1.0](components/select.typography.amendment.v0.1.0.md) | Cuatro filas Left/Right label de `ui-checkbox-label-scaled-five-sixths`,64 rangos; interpretación del ID Figma, §preparación y párrafo de derivados. |
| [Dropdown Item 0.1.0](components/dropdown-item.typography.amendment.v0.1.0.md) | Seis filas Left/Right label derivadas,12 rangos5/6 y14 rangos2/3; interpretación del ID Figma, §preparación y párrafo de derivados. |
| [Header 0.1.0](components/header.typography.amendment.v0.1.0.md) | Dos filas Count label,12 rangos4/3; interpretación del ID Figma, §preparación y párrafo de derivados. La sustitución empresa/RFC permanece intacta. |
| [App Shell 0.1.0](components/app-shell.typography.amendment.v0.1.0.md) | Una fila Count label,1 rango4/3; interpretación del ID Figma, §preparación y párrafo de derivados. |

Las13 filas conservan sus selectores `N`, textos, roles, variantes, `styleLogicalId` y recetas. Sus IDs de TextStyle materializado continúan existiendo en el catálogo; en este mecanismo no son el ID que se debe asignar al rango nativo. La fuente de escala efectiva y estilo principal se registra separadamente, por clave `{pageId,nodeId,start,end}` y no por el orden del array.

El [mapping 0.1.1](../implementations/figma/typography.v0.1.1.mapping.json), SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`, conserva su estado histórico y sus 3353 identidades. La nueva lectura no lo reescribe ni hace desaparecer su bloqueo previo. Solo un overlay posterior verificable puede sustituir la preparación de sus 103 entradas; ningún estado por nombre o fecha tiene precedencia automática.

## Regla de vínculo verificable

**NAT-01 · sustitución de REQ-TYP-004/TYC-01.** Todo rango UI debe resolver una identidad tipográfica compartida y sus propiedades. Los3250 rangos fuera del subconjunto conservan la exigencia de TextStyle ID directo, formato canónico y asignación completa por rango. Para las 103 entradas, se admite `INHERITED_NATIVE_SCALE` cuando el principal real tiene el estilo compartido correcto y la instancia hereda causalmente su efecto por la cadena nativa comprobada. El ID local vacío se conserva como observación; no se sustituye por un ID inventado ni se admite fuera del conjunto por parecido.

**NAT-02 · sustitución de §escalados/TYC-06.** Los tres IDs derivados siguen identificando la receta efectiva del catálogo y CSS. `recipeScale=1` compara la receta materializada; `nativeScale`/`instanceScale` describe el mecanismo Figma. No asignar el derivado a la instancia nativa ni multiplicar otra vez sus métricas. La receta del principal se transforma una sola vez con la escala efectiva documentada para comprobar la relación; nunca se multiplican los factores acumulados de ancestros.

| Identidad métrica conservada | Rangos | Estilo principal | ID real del principal en AI-Design-System | Escala de relación |
|---|---:|---|---|---|
| `ui-checkbox-label-scaled-two-thirds` |14|`ui-body-compact`|`S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,`|2/3|
| `ui-checkbox-label-scaled-five-sixths` |76|`ui-body-compact`|`S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,`|5/6|
| `micro-count-small-scaled-four-thirds` |13|`micro-count-small`|`S:2987fb55403e26b9fd23807ce894f58cc084820d,`|4/3|

Los IDs provienen del [state real 0.1.1](../implementations/figma/typography.v0.1.1.catalog.state.json); no acreditan por sí solos la cadena. Los valores Float32 y las recetas se consultan en el JSON canónico y sus fuentes, sin copiar otra definición editable aquí. Los porcentajes/AUTO y la equivalencia de tracking cero conservan exclusivamente las reglas ya documentadas; no se introduce tolerancia.

**NAT-03 · preservación.** Mantener IDs, caracteres, visibilidad, límites, contenido, propiedades, referencias públicas, bindings, fills, decoración, variantes, Slots y geometría. No cambiar escala, separar instancias, borrar referencias, reemplazar textos o añadir overrides para obtener un ID local. El estilo se asigna por rango al principal solo cuando corresponda a su propia regla; esta excepción contextual no autoriza cambiar la semántica de otras dependencias.

**NAT-04 · prueba de cadena.** Identificar por API cada relación instancia→principal y su ruta real al texto. Registrar el principal más cercano que gobierna el texto, TextStyle ID del principal, escala nativa y overrides tipográficos. Un Slot de contenido local puede cortar la correspondencia de ruta con un principal exterior: debe identificarse como tipo API `SLOT`, con propiedad de Slot y contenido real verificados; no tratarlo como un hijo desaparecido ni inventar una cadena exterior. No basta dividir un nodeId, tener medidas iguales o observar un ID vacío.

**NAT-05 · evidencia causal.** Exigir pilotos aislados A/B/A restaurado para 2/3,5/6 y4/3, cambiando solo el estilo del actor principal copiado. Verificar propagación al consumidor, control sin cambio, vínculo/escala estables, preservación de originales, restauración y limpieza. Cada piloto acredita su clase observada, no cobertura universal. La lectura exhaustiva final debe conciliar todas las 103 entradas, incluidas las seis rutas de Select contextualizadas por Slot, y sus propiedades reales.

**NAT-06 · aceptación por rango.** El overlay debe conservar claves únicas, fuente/hash del mapping, receta métrica, estilo principal/ID, escala, cadena, ID local observado, evidencias y resultado. `VALIDATION_PENDING`, una cadena incompleta, overrides incompatibles o un piloto faltante impiden aceptar el rango. La regla no generaliza automáticamente la excepción a otro archivo, componente, nueva instancia o rango; comprobar allí la relación concreta y registrar la diferencia respecto del snapshot.

## Evidencia y estados separados

La [evaluación de herencia 103](../qa/implementations/typography/consumption-v0.1.1/inheritance103.evaluation.json), SHA-256 `afc4a25f9ca37c48660f6fca159d0d9a66cda5c0a13483a08a4e14d0baaaaa3d`, registra `PASS` acotado a 103 rangos en 3 páginas: 242 rutas API, 9 textos principales en 5 componentes, 103 IDs locales vacíos y cero overrides tipográficos de instancia. Su [informe](../qa/implementations/typography/consumption-v0.1.1/inheritance103.review.md) preserva los seis fallos crudos de contraparte exterior y explica la frontera API SLOT `Options#466:0`, sin inventar correspondencias exteriores. Los pilotos [Checkbox5/6](../qa/implementations/typography/consumption-v0.1.1/inheritance-checkbox-five-sixths/evaluation.json), [Checkbox2/3](../qa/implementations/typography/consumption-v0.1.1/inheritance-checkbox-two-thirds/evaluation.json) y [Count4/3](../qa/implementations/typography/consumption-v0.1.1/inheritance-count-four-thirds/evaluation.json) aportan 36 controles causales y limpieza confirmada; ocho pruebas locales del verificador cubren rechazos. Esta evidencia sustenta la activación de la regla; no acredita por sí sola el cierre global de consumidores, catálogo y documentación después de sus últimas escrituras. El [overlay final](../qa/implementations/typography/consumption-v0.1.1/consumer-final.native-inheritance.v0.1.2.json) registra `PASS` para esas103 entradas. El [QA global](../qa/implementations/typography/consumption-v0.1.1/consumer-final.global.v0.1.2.json) verifica34 páginas,3351 nodos UI/3353 rangos resueltos —3250 directos y103 nativos—, cero rangos sin resolución,3501 fingerprints de preservación iguales y150 textos editoriales conservados. El [QA de79 estilos](../implementations/figma/typography.v0.1.2.styles.qa.json) comprueba322 bindings y1288 resoluciones de modo; su alcance permanece separado.

El [registro de implementación](../registry/implementations.md) conserva el estado por destino y sus reportes. Se requieren lectura global posterior a la última escritura de consumidores y controles de 3351 nodos/3353 rangos UI, además de 150 textos editoriales preservados. Las escrituras posteriores limitadas a tres descripciones de TextStyle y once textos editoriales de la página Typography, seguidas por la aclaración de dos prefijos descriptivos y sus dos tarjetas, conservan recetas, IDs y bindings y se verifican por su propio readback. La [revisión de tarjetas](../qa/implementations/typography/consumption-v0.1.1/native-cards.visual-review.md) conserva ambas fases; la [corrección documental](../qa/contracts/typography.native-inheritance.v0.1.2.description-correction.json) registra los bytes previos y finales. Typography está fuera de las34 páginas de consumidores; esos cambios de metadatos/documentación no invalidan la selección final del censo de componentes ni exigen recapturarla. La preservación se sustenta en la selección final, los guards de originales de los pilotos y la igualdad comprobada de las recetas. El informe debe separar rangos `DIRECT_STYLE_ID`, `INHERITED_NATIVE_SCALE` y `UNRESOLVED`: no informar cero IDs locales vacíos si Figma devuelve103. Solo cero rangos sin resolución, con evidencia, permite cerrar el consumo global.

Los FAIL de asignación directa y la restauración literal histórica no se reetiquetan. QA de estilos, documentación, web, preservación, consumo Figma y auditoría humana son estados distintos. La presente enmienda deja `implementation_validation: VALIDATED`; ninguna mera presencia de 79 estilos, documentación o HTML activa un PASS de consumidores.

## Web, handoff y distribución

Web sigue consumiendo las tres clases de receta materializada, sin una segunda transformación. El catálogo 0.1.2 no cambia ninguna de las 79 recetas CSS ni los cuatro estilos UNDERLINE; solo metadatos/documentación. Regenerar derivados desde el propietario JSON y demostrar ese diff acotado.

Las cuatro entradas del registro de componentes añaden esta enmienda al cierre normativo; las 43 enmiendas históricas permanecen disponibles. En el handoff, conservar identidad métrica, mediciones y fuentes/hashes, y distinguirlas del mecanismo Figma nativo. Cuando un componente use esta excepción, incluir la evidencia del overlay disponible; el QA histórico no acredita la nueva instancia del prototipo. La skill Figma debe resolver principales y bindings reales en destino y conservar `NOT_RUN`/pendientes hasta leerlo.

P-SLOTS: `NOT_APPLICABLE` al cambio de vínculo tipográfico; las familias mantienen su anatomía y cardinalidad. Los Slots observados son evidencia de composición existente, no autorización para alterar su contrato. P08 exige regenerar y verificar ambas skills desde el corte final, instalar únicamente copias gestionadas autorizadas y registrar el cierre en [skills.md](../registry/skills.md). No se anticipa release ni Graphify desde este contrato.
