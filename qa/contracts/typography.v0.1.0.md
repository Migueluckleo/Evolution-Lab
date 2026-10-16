---
qa_id: QA-TYPOGRAPHY-CONTRACT-001
review_type: CONTRACT_REVIEW
contract_ref: specs/foundations/typography.contract.v0.1.0.md
contract_version: 0.1.0
target: documentation
scope: catalogo_75_y_reglas_de_consumo
result: PASS
execution_status: COMPLETE_FOR_SCOPE
readiness: READY
pending_scopes:
  - consumer_migration
  - stable_consumer_implementation_readback
release_closure: REQUIRES_P08_CLOSURE
user_audit: PENDING
last_updated: 2026-10-15
---

# QA documental · estilos tipográficos 0.1.0

**Resultado documental: PASS para el catálogo de 75 estilos y sus reglas de consumo.** Se comprobaron los 18 base, los 57 complementarios de compatibilidad, sus 304 referencias a tokens y la evidencia de las recetas conservadas. Los resultados técnicos separados acreditan los 75 estilos Figma, la documentación Typography, la preservación acotada del censo y la implementación web. La restauración literal conserva su `FAIL` histórico y la migración de consumidores Figma permanece `BLOCKED`. No se declara un PASS global ni migración de componentes realizada. La [decisión específica](../../registry/DEC-TYPOGRAPHY-STYLES-001.md) autoriza el alcance; los resultados inferiores se basan en archivos examinados, no en una nueva inspección propia mediante Figma.

## Paquete de revisión

- [Contrato 0.1.0](../../specs/foundations/typography.contract.v0.1.0.md): reglas de consumo y aceptación; preparación separada por subconjuntos. El digest del contrato final se registrará al cerrar sus referencias y el paquete completo.
- [Catálogo canónico](../../specs/tokens/ai-design-system.typography.v0.1.0.json): corte completo revisado de 75 estilos, SHA-256 `2b47811d3175b801f41e32e3bb174060697e7c265053741541bf7e602700afed`. El corte inicial base, SHA-256 `ff0d585f2fc1753bc590083a5c41c46f8ee51aa2e301622ee0f68a465c4be187`, queda identificado como evidencia histórica de los controles BASE y BASE-FIGMA; no es el hash vigente del catálogo ampliado.
- [Referencia visual del usuario](../../sources/references/typography/user-style-list.2026-10-15.png): SHA-256 comprobado `52053d2a71f5db76f1a28c436a647597b46da486b543d88eff85b920e010e00e`; lectura visual completa de sus 18 filas.
- [Descubrimiento del destino](../../sources/figma-snapshots/typography.discovery.2026-10-15.json): SHA-256 `4ca04daba00fe38ad6835839c7acecb8ce96ec6b4cc667112e4121357e3b4ce6`. El archivo registra 34 páginas, 20 estilos existentes y las fuentes Manrope necesarias; es evidencia del snapshot, no una nueva inspección propia ni un censo de consumidores completo.
- [Variables locales](../../sources/figma-snapshots/typography/variables.before.json): SHA-256 `aef5738fbcee59d6d8b262083c37375dac98599d61e6c203d8791a30d63f8be2`. Referencias de la base verificadas en la colección semántica `VariableCollectionId:6:2` y sus aliases a la primitiva `VariableCollectionId:6:3`.
- [Variables locales de métricas](../../sources/figma-snapshots/typography/metric-variables.before.json): SHA-256 `5d4e3a0658a7bf3c82ff8f73f5f9a8fd8c3aa5c116839de72bbd1fbbb7f01f84`. IDs y scopes de roles semánticos de interlineado y tracking; sus referencias se contrastaron con las unidades PIXELS del catálogo y sus valores canónicos. Este snapshot de aliases no acredita por sí solo valores resueltos tras la escritura.
- [Extensión Avatar](../../drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json), delegada por [FOUNDATIONS-AVATAR-ROLES-001](../../specs/foundations/foundations.avatar-roles.amendment.v0.1.6.md): SHA-256 `66a680bbb494895c76b43b9ca0d1b081c51afbb9c4dd079b6cf841c6488dc1f6`; resuelve `font/size/avatar-small` sin modificar el inventario histórico.
- [Readback de estilos base](../../implementations/figma/typography.base.v0.1.0.state.json): SHA-256 `df73a13b43b999c4856fb1d42fa04386c2c7a0638399d56d0d6c1c380b21b0db`; contiene 18 IDs creados, cero reutilizados y campos leídos de los 18 estilos. No contiene una migración de consumidores.
- Censo detallado en [typography/](../../sources/figma-snapshots/typography/), archivos `census.before.<page-id-con-guion>.json`. Se reconciliaron 34 archivos/páginas contra discovery: 3501 nodos y 3503 segmentos. Esquema 2: `columns` define cada array de `nodes`, y los segmentos referencian `recipes`; longitudes de filas e índices de recetas comprobados. No se confunde con la exportación preliminar `before.*.json`.
- Digest agregado del censo: `c73e10d9cdae7e4a778a1c254d2f53498d4c68ad8fc78d9115ee9a599296fa0b`. Método: SHA-256 de UTF-8 JSON del mapa `{ruta relativa: SHA-256 de bytes}` de los 34 archivos `census.before.*.json`, claves ordenadas, separadores `(',', ':')`, `ensure_ascii=False`. Es un digest agregado, no el hash de bytes de un archivo individual. La cobertura de migración requiere su matriz y validación propias.
- [Inventario histórico](../../sources/inventories/tokens.inventory.json): SHA-256 esperado `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`; no debe alterarse para acomodar los nuevos estilos.
- [Mapa de consumidores](../../implementations/figma/typography.v0.1.0.mapping.json): SHA-256 `292ae3b24fd617172a0434fcb579419f54c3813df7ae07be877dce13debd162b`; el catálogo y el mapa identifican 103 rangos que requieren derivados. `recipeScale: 1` compara la receta materializada; `instanceScale` conserva el factor observado del componente. Es preparación, no resultado de aplicación.
- La [evidencia previa de Count](../../qa/implementations/typography/scaled-counter.pre-inheritance.json), SHA-256 `bbdaca3a2dcd3d476c82867f150a33311ba1e604021d313da776b83456405046`, acredita el estado anterior de una instancia, su escala y `textStyleId` vacío. No prueba éxito de herencia, asignación del derivado ni persistencia final.

## Controles documentales del catálogo completo

| Control | Contraste requerido | Estado | Evidencia y alcance |
|---|---|---|---|
| DOC-01–03 | Tipo foundations, identidad, versión, fuentes y alcance sin metadatos inventados | PASS | Contrato y JSON identifican versión, 18 base, 57 complementarios y fuentes reales; no se inventan IDs de estilos futuros. |
| DOC-04–06 | Procedencia y separación de autorización, observación y guía de uso | PASS | Imagen leída y evidencia por fila; los complementarios distinguen reglas contractuales de propiedades `OBSERVED` preservadas por la delegación actual. `description_provenance` identifica la redacción de uso delegada. |
| DOC-07–08 | Datos completos, referencias resolubles y única `description` | PASS | CAT-01–06: 75 IDs/nombres/descripciones únicos, 304 referencias válidas y evidencia por estilo. |
| DOC-09–10 | Consistencia de recetas, unidades y alcance de sustitución | PASS | Base exacta de la referencia; complementarios de compatibilidad exacta con unidades conservadas. La creación de estilos no acredita migración ni altera recetas por preferencia. |
| DOC-11 | No introducir defaults o propiedades de componentes por clasificación tipográfica | PASS | Contrato conserva las propiedades de componentes y no define una API o defaults nuevos. |
| DOC-12 | Mapeo Figma/web y límites explícitos | PASS | Unidades y transformaciones declaradas; se separa la verificación documental de la prueba posterior de escritura/render. |
| DOC-13 | Criterios verificables por alcance | PASS | AC-TYP-001–009 distinguen creación base, complementarios, consumo, bindings, readback y otros destinos. |
| DOC-14 | Originales e inventario preservados | PASS | SHA-256 de imagen e inventario comprobados; nuevas definiciones en JSON separado. |
| DOC-15–16 | Delegación y preparación por alcance sin aprobación ficticia | PASS | `DELEGATED_FOR_BUILD`, `user_audit: PENDING`, catálogo 75 READY y resultados técnicos separados; consumo Figma BLOCKED. |
| DOC-17 | Página semántica por familia de componentes | NOT_APPLICABLE | Se crean TextStyles globales, no una nueva familia de componentes; una galería no es requisito para crear la base. |
| DOC-18 | Referencias y mapa a variables locales verificables | PASS | Nombres/scopes locales de 304 referencias comprobados; valores canónicos resueltos en cuatro modos. La asignación y lectura posterior tienen QA técnico separado, identificado abajo. |
| SLOT-QA-01 | Aplicabilidad de Slots | NOT_APPLICABLE | Definiciones de estilo sin regiones de contenido variable; los consumidores conservan sus Slots. |

La selección de complementarios está revisada y su creación tiene readback técnico separado. La migración Figma requiere resolver el bloqueo reproducible y leer de nuevo todos los consumidores afectados después de la última escritura. El QA web tiene alcance propio. La vigencia de paquetes se consulta en [registry/skills.md](../../registry/skills.md), conforme a P08; este PASS documental no sustituye ese cierre.

## Comprobaciones ejecutadas sobre los 75 estilos

| Control | Resultado | Evidencia y límite |
|---|---|---|
| CAT-01 | PASS | JSON parseado: 75 IDs, nombres y descripciones únicos; 18 `base` y 57 `complementary`. Los 57 complementarios declaran `compatibilityOnly: true`; familia y pesos se corresponden con Manrope y sus fuentes disponibles. |
| CAT-02 | PASS | 243 referencias de evidencia a 68 archivos reales. Se verificaron los hashes declarados por referencia y en metadatos superiores. Cada complementario tiene respaldo contractual `EXPLICIT` y censo `OBSERVED`; las propiedades exactas observadas no se atribuyen falsamente al contrato. |
| CAT-03 | PASS | 207 cotejos de recetas citadas y 290 referencias a nodos muestra: se reconstruyeron IDs desde `idParts`/`paths`, se comprobó pertenencia a índices de receta y se cotejaron familia, estilo, peso, tamaño, interlineado y tracking. Únicas equivalencias: codificación float32 documentada y tracking cero entre PIXELS/PERCENT. Los conteos son referencias comprobadas, no nodos únicos ni cobertura total de la migración. |
| CAT-04 | PASS | 304 `tokenRefs`: 303 resuelven mediante el inventario histórico y una mediante la extensión Avatar; 1216 resoluciones canónicas en cuatro modos, con scope correcto. Los nombres/scopes y cuatro aliases locales están presentes en los dos snapshots de variables. No se vinculan porcentajes o AUTO a variables PIXELS. |
| CAT-05 | PASS | Las 54 descripciones limitan uso a roles existentes y sus instancias, explican la preservación y no forman una escala alternativa. El contrato reserva los 18 base para texto local nuevo y no autoriza cambios de UI por coincidencia parcial de tamaño/peso. La guía es redacción delegada y su auditoría humana sigue `PENDING`. |
| CAT-06 | PASS | Tres derivados adicionales limitan su uso a 103 rangos censados: 14 de Checkbox a dos tercios, 76 a cinco sextos y 13 de Count a cuatro tercios. Cada `derivedFrom` identifica base, fracción y `FLOAT32_BASE_TIMES_FLOAT32_SCALE`; tamaño y métricas PIXELS coinciden exactamente con esa operación, y los porcentajes se conservan. Se cotejaron los 103 IDs, sus recetas anteriores y su asignación en el mapa. Los seis bindings adicionales son de familia/peso; no se inventan tokens fraccionarios ni se reintroducen tamaños sin escalar. |

La revisión anterior acredita el catálogo y su selección, no que los consumidores ya tengan estos estilos. Las métricas de compatibilidad siguen siendo evidencia `OBSERVED` preservada por la solicitud delegada; su inclusión no transforma el censo ni el detalle del catálogo en `APPROVED`.

## Comprobaciones ejecutadas sobre la base

| Control acotado | Resultado | Evidencia y límite |
|---|---|---|
| BASE-01 | PASS | SHA-256 de la imagen calculado y contrastado; las 18 filas se leyeron visualmente y se transcribieron al corte de JSON identificado arriba. |
| BASE-02 | PASS | JSON parseado; 18 IDs y nombres únicos; familia, peso, tamaño, porcentajes y tracking cotejados con las filas. `SemiBold` corresponde al nombre de fuente registrado en discovery; `Semibold` es la etiqueta visible. |
| BASE-03 | PASS | 54 referencias a tokens semánticos existentes verificadas por nombre y scope; valores resueltos contrastados en cuatro modos, 216 correspondencias. Familia base, pesos y tamaños coinciden; no se inventaron tokens de porcentaje. |
| BASE-04 | PASS | Cada estilo base tiene `description` con uso y límite, procedencia de valores y unidades explícitas. La guía de uso se identifica como redacción delegada, no intención histórica observada. |
| BASE-05 | PASS | Las 54 referencias de la base también resuelven en `variables.before.json`: scopes compatibles, cuatro aliases por semántica y valores correspondientes en la colección primitiva. `discovery` incluye las cuatro fuentes Manrope requeridas: Regular, Medium, SemiBold y Bold. |
| CENSUS-01 | PASS | 34 páginas censadas coinciden con discovery; 3501 nodos y 3503 segmentos. Es una comprobación estructural de la exportación inicial, no validación de selección ni migración. |

Los controles BASE conservan su alcance original y el corte identificado; CAT amplía la revisión documental a los 75 estilos. El readback base se evalúa por separado a continuación. Ninguno de estos controles valida consumidores o layout.

## Readback de los 18 estilos base

Se contrastó el archivo `typography.base.v0.1.0.state.json` contra la base canónica y las variables locales. Esta revisión usa el snapshot posterior proporcionado por la ejecución; no afirma haber operado Figma desde la revisión documental.

| Control | Resultado | Evidencia |
|---|---|---|
| BASE-FIGMA-01 | PASS | 18 nombres e IDs únicos; los IDs de `styles` coinciden exactamente con `createdStyleIds`; cero estilos declarados reutilizados. |
| BASE-FIGMA-02 | PASS | Familia, nombre de fuente, peso por `variationSettings.wght`, tamaño y `description` coinciden exactamente con las 18 entradas canónicas. |
| BASE-FIGMA-03 | PASS | 54 bindings reales: familia, peso y tamaño de cada estilo enlazados al ID semántico esperado en `variables.before.json`. |
| BASE-FIGMA-04 | PASS | Unidades porcentuales y tracking exactos. Interlineado comparado por igualdad con `Math.fround(p / 100) × 100`, representación observada documentada en el contrato. |

La fórmula de representación se reprodujo mediante conversión IEEE-754 float32 de la fracción y multiplicación por 100. Los resultados son exactamente `125`, `133.00000429153442`, `150` y `160.0000023841858`. No se utilizó tolerancia, truncamiento ni modificación del JSON para hacer pasar la comparación; CSS conserva las proporciones canónicas. Para tracking la base devuelve el valor canónico exacto: no se le aplica la fórmula de interlineado.

**Límite:** estos cuatro PASS acreditan únicamente los estilos base leídos y sus campos/bindings. No acreditan que algún componente ya los consuma, ni ausencia de overrides, clipping, cambios de geometría o regresiones de layout. El readback final del censo acredita preservación según el alcance siguiente; la migración de consumidores continúa bloqueada.

## Resultados técnicos finales por alcance

La [revisión de implementación](../implementations/typography.v0.1.0.review.md) consolida estos resultados sin convertirlos en aprobación humana:

| Alcance | Resultado | Evidencia y límite |
|---|---|---|
| Estilos Figma | PASS | [QA independiente](../../implementations/figma/typography.v0.1.0.styles.qa.json): 75 estilos, 304 bindings y 1216 resoluciones en cuatro modos. Se contrastaron recetas, descripciones, IDs semánticos, scopes, identidades de aliases y valores reales. [Mapa actual de 75 IDs](../../implementations/figma/typography.v0.1.0.catalog.state.json). |
| Documentación Figma | PASS | Página Typography `1003:412`: [readback](../implementations/typography/specimens.readback.json), 75 tarjetas, 316 textos, 79 frames y cero errores. No representa los consumidores existentes. |
| Preservación del censo | PASS acotado | [QA independiente](../../implementations/figma/typography.v0.1.0.preservation.qa.json): 34 páginas, 3501 nodos y 3503 rangos; 3351 nodos UI/3353 rangos UI y 150 editoriales. Contenido, métricas, propiedades capturadas, cajas, IDs originales y 3501 hashes de preservación coinciden. `allowedCanonicalStyleBindings` identifica 244 rangos de 242 nodos y 17 estilos reutilizados, con 1202 referencias añadidas; cada adición coincide con el catálogo, el binding del estilo y las variables reales por nombre, ID, scope y cuatro modos. No hay pérdida, sustitución ni referencia ajena. |
| Restauración literal | FAIL histórico | [Reporte estricto conservado](../../implementations/figma/typography.v0.1.0.restoration.qa.json): 244 diferencias de bindings aditivos. SHA-256 `160cd9ee9f961141862e0f503d707c12a18810c70a36eb77ea7b2521b0d03cfb`; el QA adicional no sobrescribe ni convierte este resultado en PASS. |
| Migración de consumidores Figma | BLOCKED | [Diagnóstico](../implementations/typography/Figma-blocker.md): propagación observada al asignar estilos entre textos con referencias a propiedades. La causa interna sigue `UNRESOLVED`. El catálogo, el mapa y la preservación no acreditan consumo global; se conservan IDs originales y no se declara VALIDATED. |
| Implementación web | PASS acotado | [Corte de 75 estilos](../implementations/typography/web/revision-75/README.md): 300 recetas renderizadas (75 × cuatro temas) y 2956 mediciones de texto en 43 familias por cuatro temas. Nueve pruebas del generador, determinismo, TypeScript, build y dos pruebas Chrome afectadas pasan. La suite previa de 61 pruebas es evidencia histórica, no una repetición en este corte. |

El QA de estilos tiene SHA-256 `0017bd85f6e4805f24410c19cd3abe3e7615518798dde4f2405a511946e3a8dd`; el de preservación, `9cf26f856ea8685b2f28ca0bb94869897baea3771a4e048dbba15794c4b4f702`. La actualización autorizada de la foundation añade bindings canónicos a estilos reutilizados sin alterar las métricas originales; por ello preservación acotada y restauración literal tienen resultados diferentes. Los hashes y las cajas capturadas no prueban igualdad visual universal de todas las composiciones.

## Límites de esta revisión

La lectura del inventario y los contratos identificó que familia, pesos y tamaños de la referencia disponen de tokens existentes, mientras que sus porcentajes no pueden equipararse automáticamente a interlineados y tracking históricos. La validación de referencias del corte base confirma esa correspondencia acotada; no acredita una operación en Figma.

La selección de los 57 complementarios ya tiene evidencia y revisión documental. El universo inicial está censado; antes de cerrar la migración debe verificarse qué estilo corresponde a cada consumidor y qué excepciones/exclusiones siguen vigentes. No se acepta una afirmación de cobertura basada solo en nombres de estilos o en los nodos muestra del catálogo.

El QA de migración de consumidores sigue `BLOCKED` y deberá comprobar AC-TYP-004–009 sobre evidencia final estable después de resolver el fallo. La preservación del censo acredita recuperación de propiedades originales con las adiciones delimitadas; no acredita asignación de los estilos previstos a todos los rangos. Los resultados web y Figma son independientes y no certifican por sí mismos vigencia de las skills.

## Condición para actualizar el resultado

Para cerrar la migración Figma, resolver el fallo reproducible mediante una intervención concreta comprobada y volver a ejecutar los controles afectados sobre el conjunto completo después de la última escritura. Conservar los resultados históricos y registrar las nuevas evidencias por destino; solo los controles ejecutados pueden pasar a PASS. El cierre de paquetes se registra separadamente conforme a P08. Mantener `user_audit: PENDING` aunque los resultados técnicos sean conformes.
