---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-TYPOGRAPHY-001
name: Estilos tipográficos base y complementarios
type: foundations
status: DELEGATED_FOR_BUILD
user_audit: PENDING
version: 0.1.0
owner: null
last_updated: 2026-10-15
review_targets:
  - figma
  - web
sources:
  - DEC-TYPOGRAPHY-STYLES-001
  - SRC-TOKENS-INV-001
  - sources/references/typography/user-style-list.2026-10-15.png
  - sources/figma-snapshots/typography.discovery.2026-10-15.json
data_refs:
  - specs/tokens/ai-design-system.typography.v0.1.0.json
  - sources/inventories/tokens.inventory.json
  - drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json
dependencies:
  - FOUNDATIONS-TOKENS-001
  - FOUNDATIONS-AVATAR-ROLES-001
  - MIGRATION-TOKEN-TRACEABILITY-001
slot_applicability: NOT_APPLICABLE
readiness_by_scope:
  figma_base18: READY
  figma_complementary_styles: READY
  figma_consumer_migration: BLOCKED
  web: READY
implementation_by_scope:
  figma_styles: PASS
  figma_documentation: PASS
  figma_preservation_allowed_bindings: PASS
  figma_literal_restoration: FAIL
  figma_consumer_migration: BLOCKED
  web_typography: PASS
  skills_release: REQUIRES_P08_CLOSURE
---

# Estilos tipográficos · contrato 0.1.0

La [decisión del usuario](../../registry/DEC-TYPOGRAPHY-STYLES-001.md) delega específicamente documentar, construir e integrar los estilos de la referencia y comprobar sus consumidores. El alcance elegido es **18 estilos base más complementarios necesarios documentados**, con auditoría humana del detalle `PENDING`. `DELEGATED_FOR_BUILD` no significa aprobación humana del catálogo ni validación de su implementación.

**Estado verificado:** QA documental y [QA independiente de los 75 estilos Figma](../../implementations/figma/typography.v0.1.0.styles.qa.json) `PASS`: 18 base y 57 complementarios, con 304 bindings y 1216 resoluciones reales por modo. La documentación Figma y la implementación tipográfica web tienen resultados propios `PASS`. La [preservación del censo](../../implementations/figma/typography.v0.1.0.preservation.qa.json) pasa con adiciones canónicas explícitas de bindings; la restauración literal conserva su `FAIL` histórico. La [migración de consumidores Figma](../../qa/implementations/typography/Figma-blocker.md) permanece `BLOCKED`; ninguno de los resultados anteriores acredita su consumo global.

## 1. Propósito y alcance

Convertir las decisiones tipográficas en composiciones reutilizables, trazables y editables. El catálogo base cubre la referencia entregada; los complementarios representan recetas existentes justificadas por consumidores reales. No se obliga a convertir todo texto al catálogo base ni a cambiar alturas, pesos o geometría para hacer coincidir una clasificación.

El alcance tipográfico comprende familia, peso/estilo de fuente, tamaño, interlineado y espaciado entre caracteres. Alineación, contenido, color, propiedades de componente, visibilidad, reglas de truncamiento, cajas y disposición conservan su contrato vigente salvo sustitución acotada registrada. Una clasificación visual de encabezado no impone por sí sola una etiqueta HTML ni jerarquía de accesibilidad.

P-SLOTS es `NOT_APPLICABLE` para estas definiciones de estilo: no contienen regiones de composición variable. Los componentes consumidores conservan su aplicabilidad, anatomía y mecanismos de Slots vigentes.

## 2. Fuentes y propiedad de datos

| Fuente | Localizador | Autoridad y campos propios | Estado de evidencia |
|---|---|---|---|
| Solicitud y elección del usuario | [DEC-TYPOGRAPHY-STYLES-001](../../registry/DEC-TYPOGRAPHY-STYLES-001.md) | Autoriza este alcance y la convivencia de base y complementarios | Registrada; detalle pendiente de auditoría humana |
| Referencia visual tipográfica | [Imagen del usuario](../../sources/references/typography/user-style-list.2026-10-15.png) | Fuente de los estilos base; no acredita sus IDs ni su implementación Figma | SHA-256 de bytes `52053d2a71f5db76f1a28c436a647597b46da486b543d88eff85b920e010e00e` |
| Catálogo tipográfico de destino | [ai-design-system.typography.v0.1.0.json](../tokens/ai-design-system.typography.v0.1.0.json) | Único propietario editable de identidad lógica, nombre, propiedades, unidades y `description` de cada estilo; referencias a tokens y procedencia | 18 base y 57 complementarios comprobados; hash del corte revisado en QA |
| Inventario histórico aprobado | [tokens.inventory.json](../../sources/inventories/tokens.inventory.json), colecciones `primitive` y `semantic`, variables `font/*` | Nombres, valores, aliases, modos, scopes y única `description` de los tokens existentes | SHA-256 de bytes `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474` |
| Contrato de variables | [FOUNDATIONS-TOKENS-001](foundations-tokens.contract.md), §§5–8 | Preservación del inventario y límites de unidades; no define por sí solo estilos compuestos | `APPROVED` para su alcance histórico |
| Extensión de Avatar | [FOUNDATIONS-AVATAR-ROLES-001](foundations.avatar-roles.amendment.v0.1.6.md) y [JSON canónico](../../drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json) | Identidad y alias de `font/size/avatar-small`; no se incorpora al inventario histórico | Extensión vigente para ese tamaño; se conserva su estado delegado y auditoría pendiente |
| Contratos de consumidores | Base y enmiendas vigentes por familia | Recetas, excepciones, estructura, geometría y criterios de cada consumidor | Identificar las referencias afectadas en la matriz de migración |
| Descubrimiento del destino | [typography.discovery.2026-10-15.json](../../sources/figma-snapshots/typography.discovery.2026-10-15.json) | Evidencia `OBSERVED` de páginas, estilos y fuentes disponibles en el destino | SHA-256 de bytes `4ca04daba00fe38ad6835839c7acecb8ce96ec6b4cc667112e4121357e3b4ce6`; no acredita cobertura de consumidores |
| Variables locales del destino | [variables.before.json](../../sources/figma-snapshots/typography/variables.before.json) | Evidencia `OBSERVED` de identidades, scopes y aliases locales; no redefine el inventario | SHA-256 de bytes `aef5738fbcee59d6d8b262083c37375dac98599d61e6c203d8791a30d63f8be2`; referencias de la base comprobadas contra `semantic` 6:2 y `primitive` 6:3 |
| Variables locales de métricas | [metric-variables.before.json](../../sources/figma-snapshots/typography/metric-variables.before.json) | Evidencia `OBSERVED` de IDs, scopes y aliases semánticos de interlineado y tracking | Referencias PIXELS cotejadas con el inventario; no se reinterpretan como porcentajes; hash en QA |
| Censo detallado del destino | [Directorio del censo](../../sources/figma-snapshots/typography/), archivos `census.before.<page-id-con-guion>.json` | Evidencia `OBSERVED` de textos/rangos, estilos, propiedades, límites y bindings reales | 34 páginas reconciliadas con discovery, 3501 nodos y 3503 segmentos; esquema 2 con arrays interpretados mediante `columns`; comprobación y digest agregado en QA |

Este Markdown gobierna reglas de consumo, sustitución y aceptación. No mantiene una segunda tabla editable de los valores ni del uso de los 18 estilos. Los nombres e IDs reales de Figma pertenecen al mapa de implementación; no se inventan en el contrato. El catálogo nuevo no modifica ni sustituye silenciosamente los datos históricos del inventario aprobado.

## 3. Cobertura y modelo

El catálogo revisado contiene 18 estilos base de la referencia y 57 complementarios de compatibilidad, identificados con `compatibilityOnly: true`. Incluyen 54 recetas de compatibilidad iniciales y tres derivados para instancias escaladas. Conservan recetas de UI ya observadas; no constituyen otra escala general de diseño.

Cada complementario requiere consumidor observado, respaldo contractual de su función y una razón para preservar su receta. Las propiedades exactas no transcritas en el contrato son `OBSERVED` y se preservan bajo la delegación específica; no se atribuyen a una aprobación humana inexistente. La guía `description` se redacta bajo esa delegación. En la UI existente, coincidir en familia, tamaño y peso con la base no autoriza cambiar interlineado o tracking por preferencia. Solo se admite equivalencia exacta, la representación numérica documentada y tracking cero equivalente entre PIXELS/PERCENT. Una instancia escalada no genera una receta nueva por sí sola.

Para texto local nuevo se usa el catálogo base de 18 estilos según su función. Los complementarios quedan limitados a los roles existentes y sus instancias declarados en su `description`; no se ofrecen como alternativas generales para pantallas nuevas. Compartir métricas entre consumidores no cambia su función, semántica ni contrato.

La matriz de consumidores debe incluir familia, principal o instancia, texto o rango, visibilidad, receta anterior, estilo elegido, bindings/overrides, procedencia y resultado. Distingue componentes sin texto, contenido editable, muestras documentales y geometría de artwork. Las exclusiones no se presentan como consumidores conformes.

### Derivados necesarios para instancias escaladas

Conservar las métricas de una instancia escalada sin un `textStyleId` real no satisface REQ-TYP-004. Cuando Figma materializa esas métricas en el texto y aplicar la receta del principal restablece su tamaño, se representa el resultado observado mediante un estilo derivado de compatibilidad. Esta excepción acotada no autoriza generar una escala tipográfica arbitraria: conserva tres recetas observadas de Checkbox y Count, con origen y consumidores identificados. La [evidencia previa de Count](../../qa/implementations/typography/scaled-counter.pre-inheritance.json) acredita su escala, medidas y ausencia de estilo en ese corte; no constituye readback final de la solución.

`derivedFrom` identifica la receta base, la razón técnica, la fracción de escala y su codificación. Las magnitudes en píxeles se derivan por `Float32(valorBase × Float32(numerador / denominador))`; los porcentajes conservan su valor canónico. No se redondea ni se inventan variables fraccionarias. Familia y peso mantienen sus bindings; no se asigna el token de tamaño o interlineado sin escalar si eso restablecería las medidas del principal.

La matriz distingue `instanceScale`, escala efectiva que debe conservar el componente, de `recipeScale`, multiplicador para comparar las métricas con el estilo elegido. En estos derivados, `recipeScale` y su alias `expectedScale` son 1 porque la receta ya contiene el resultado de la escala; multiplicarla otra vez es un error. El consumidor debe tener el ID real del derivado, sus campos resueltos y sus bindings conformes, sin overrides métricos que sustituyan el estilo. La escala del contenedor se verifica con evidencia posterior propia, no se infiere solo del tamaño de la letra. El readback final debe cubrir los 103 rangos escalados identificados por el mapa.

## 4. Requisitos

| ID | Regla | Fuerza | Procedencia | Criterio |
|---|---|---|---|---|
| REQ-TYP-001 | Conservar exactamente los estilos base de la referencia en el catálogo canónico, incluidas unidades y pesos, sin completar combinaciones no solicitadas. | MUST | EXPLICIT solicitud | AC-TYP-001 |
| REQ-TYP-002 | Añadir complementarios solo con receta/consumidor y motivo documentados, preservando los casos compactos y excepciones que no necesiten cambiar. | MUST | EXPLICIT elección del usuario + OBSERVED/contrato por consumidor | AC-TYP-002 |
| REQ-TYP-003 | Mantener una identidad lógica y una sola `description` por estilo en el JSON; generar desde allí descripciones o documentación derivadas, sin un `usage` editable paralelo. | MUST | Regla SDD de definición única | AC-TYP-003 |
| REQ-TYP-004 | Asignar un estilo explícito a cada texto o rango consumidor del alcance, incluyendo variantes y contenido oculto; comparar sus propiedades resueltas con la receta elegida. | MUST | EXPLICIT cobertura solicitada | AC-TYP-004 |
| REQ-TYP-005 | Reutilizar los tokens semánticos existentes por identidad, scope y significado cuando sean equivalentes. No sustituir aliases por literales ni atribuir equivalencia a magnitudes/unidades diferentes. | MUST | FOUNDATIONS-TOKENS-001 y trazabilidad | AC-TYP-005 |
| REQ-TYP-006 | Conservar los porcentajes y AUTO declarados por el catálogo sin redondeo o reinterpretación silenciosa. Registrar las conversiones deterministas por destino. | MUST | EXPLICIT referencia + preservación de complementarios | AC-TYP-006 |
| REQ-TYP-007 | Reutilizar estilos/componentes cuando correspondan; preservar IDs, vínculos, contenido, colores, propiedades y anatomía. Registrar cualquier sustitución o ajuste necesario y su alcance. | MUST | EXPLICIT alcance + contratos consumidores | AC-TYP-007 |
| REQ-TYP-008 | Leer después del último cambio todos los estilos y consumidores afectados; comprobar cobertura completa, fuentes disponibles y ausencia de recortes o regresiones de composición. | MUST | P04/P06 | AC-TYP-008 |
| REQ-TYP-009 | Mantener separadas autorización, preparación, QA documental, QA Figma, QA web y vigencia de skills; propagar el cambio a los destinos autorizados y revalidar lo afectado. | MUST | P05/P06/P07/P08 | AC-TYP-009 |

La delegación autoriza implementar estas reglas dentro de la tarea; no convierte observaciones desconocidas en requisitos demostrados ni elimina el preflight.

## 5. Tokens, modos y bindings

Las variables existentes conservan sus colecciones, aliases, modos y descripciones. No se retargetea un rol compartido de interlineado o tracking para acomodar el catálogo nuevo. Familia, peso y tamaño se vinculan a roles semánticos existentes cuando corresponden exactamente; los complementarios conservan también los roles de interlineado PIXELS y tracking PIXELS equivalentes declarados en `tokenRefs`. El mapa a IDs locales requiere lectura real del destino; mover el binding al TextStyle no permite perderlo ni cambiar su unidad.

Para campos porcentuales o AUTO definidos explícitamente en el catálogo, la composición canónica y su TextStyle gobiernan la propiedad. La comprobación exige la unidad y el valor reales del estilo y del consumidor; no exige fingir una variable histórica equivalente. Esta regla sustituye, únicamente para esos campos catalogados, la expectativa de representarlos mediante un binding individual inexistente o de otra unidad. Los bindings restantes y sus aliases continúan exigidos. Cualquier limitación de escritura o lectura se registra por propiedad y bloquea su validación.

Los modos de marca no cambian la receta tipográfica por inferencia. Se conserva la herencia de los consumidores y los bindings existentes, comprobando que la resolución de sus referencias no modifica indebidamente familia, peso o tamaño. El estilo de texto no absorbe ni reemplaza los roles de color.

La actualización autorizada de foundations conserva los bindings anteriores y permite añadir los bindings canónicos a TextStyles existentes reutilizados, manteniendo su ID. El cierre distingue esa actualización de una restauración literal: `allowedCanonicalStyleBindings` admite únicamente referencias aditivas idénticas al estilo canónico, verificadas por nombre, ID, scope, cadena de alias y cuatro modos reales. No permite retirar, reemplazar o introducir referencias ajenas ni cambiar métricas. La excepción comprobada comprende 244 rangos de 242 nodos sobre 17 estilos originales; no exime del requisito pendiente de migrar los demás consumidores.

## 6. Unidades y adaptación

El catálogo debe identificar la unidad de cada magnitud. Un FLOAT del inventario, por sí solo, no acredita `%`, `em` ni una conversión de plataforma. Las cadenas de peso canónicas y los nombres disponibles de fuente se mapean explícitamente sin editar los originales por capitalización.

Para una magnitud de interlineado porcentual `p` y tamaño `s`, la medida equivalente es `s × p / 100`; conservar el porcentaje original en Figma cuando la capacidad lo permita. En CSS puede expresarse como proporción `p / 100`. Para tracking porcentual `q`, la adaptación CSS es `q / 100 em`; su equivalencia en píxeles depende del tamaño. Son transformaciones derivadas, no nuevos valores editables. AUTO se conserva como decisión diferenciada y no se convierte a un número medido sin una sustitución explícita.

No reutilizar un adaptador que agregue `px` a todos los FLOAT para los porcentajes de este catálogo. La capa web debe consumir unidades explícitas y demostrar la equivalencia aplicable. El redondeo, la tolerancia de comparación o la elección de una fuente sustituta no se deciden después de observar un fallo para hacerlo pasar.

### Representación numérica del readback

`DERIVED`: la [lectura real de los estilos base](../../implementations/figma/typography.base.v0.1.0.state.json) representa el interlineado porcentual como `Math.fround(p / 100) × 100`. La comparación del campo Figma se hace por igualdad con esa codificación determinista: por ejemplo, el porcentaje canónico 133 se lee como `133.00000429153442`, y 160 como `160.0000023841858`; 125 y 150 se conservan exactamente. Esto identifica representación binaria float32 de la fracción, no una tolerancia ni un redondeo de diseño. Los valores canónicos y sus equivalentes CSS permanecen intactos.

La regla es específica de ese campo y de la evidencia observada: no se aplica indiscriminadamente a otras propiedades. El tracking de la base se lee exactamente como su valor canónico. En recetas históricas, magnitudes como 0.1 o −0.01 pueden estar representadas como float32 directo; comparar con su dato canónico/receta y codificación documentada, sin confundirlas con la codificación de fracción de interlineado. Una diferencia no explicada por la representación declarada sigue siendo discrepancia y no se absorbe mediante un epsilon genérico.

## 7. Uso y complementarios

El uso específico de cada estilo vive en su `description` canónica. Como regla general, elegir primero la función del texto y después el estilo compatible con ella y con su contrato. La jerarquía de una pantalla no se deduce de tamaño únicamente; una métrica, una etiqueta de control y un título pueden necesitar recetas distintas aunque compartan dimensiones.

Los complementarios preservan recetas justificadas cuando un estilo base cambia peso, tamaño, interlineado o geometría sin necesidad. La matriz explica la elección y enlaza la fuente; no mantiene otra descripción de uso editable. Un complementario no autoriza nuevos tamaños o variantes de componentes, ni elimina excepciones de legibilidad ya documentadas.

La sustitución transversal es pasar de valores aislados a estilos explícitos y verificables. Los contratos de familia continúan gobernando sus recetas conservadas. Si se adopta una receta base diferente, registrar qué requisito anterior queda sustituido, diferencias y consumidores afectados; no declarar intacto el contrato anterior ni borrar su QA histórico.

## 8. Integración y comprobación Figma

Destino autorizado: `AI-Design-System`, file key `tj3WIBEZDGLVs7MJWKCwgf`. Aplicar P04: leer fuentes disponibles, estilos locales y consumidores antes de escribir; comprobar la identidad de cualquier estilo reutilizado y conservar su alcance. Un nombre coincidente no basta para modificarlo.

Asignar estilos manteniendo instancias y principales, rangos de texto mixto, propiedades y contenido. Los overrides tipográficos que contradigan la receta elegida deben resolverse mediante una asignación compatible o una excepción explícita; conservar un ID de estilo mientras todos sus campos quedan sobreescritos no satisface REQ-TYP-004. Los overrides de contenido/color ajenos al alcance no se eliminan por rutina.

El censo inicial determina el universo y la lectura final debe reconciliarlo sin omitir variantes, textos ocultos, instancias anidadas o rangos mixtos. Los nodos sin contenido textual y artwork vectorizado se contabilizan aparte. Comprobar los ajustes necesarios de cajas, reflow, truncamiento y composición con contenido largo y tamaños existentes; no reconstruir anatomía ni convertir Slots por esta tarea.

## 9. Web, documentación y distribución

P07 exige reflejar los estilos y usos aplicables en la implementación y documentación web, conservando las reglas de los consumidores. El adaptador debe respetar las unidades del catálogo y las fuentes disponibles; no inventar una API pública de componente ni deducir validación de la evidencia Figma.

P08 exige incorporar el contrato, catálogo y recursos afectados en ambas skills del mismo corte versionado. La integridad del paquete no prueba fidelidad tipográfica en un prototipo o en Figma; cada destino conserva su QA. Los cambios en derivados no se presentan como edición de una segunda fuente canónica.

## 10. Criterios de aceptación

| ID | Alcance | Comprobación | Evidencia requerida |
|---|---|---|---|
| AC-TYP-001 | Catálogo base | Comparar los 18 estilos con la referencia preservada, incluidos pesos y unidades exactas. | Fuente con hash + verificación del JSON |
| AC-TYP-002 | Complementarios | Cada estilo adicional tiene receta, consumidor y motivo; las excepciones conservadas siguen identificadas. | Censo y matriz con referencias contractuales |
| AC-TYP-003 | Datos | IDs únicos, referencias resolubles, propiedades/unidades completas y una `description` canónica por estilo; no catálogo editable duplicado. | QA documental y hashes de datos |
| AC-TYP-004 | Consumo Figma | Todo texto/rango incluido tiene estilo esperado y propiedades resueltas compatibles; cero consumidores pendientes ocultados. | Readback exhaustivo y cobertura antes/después |
| AC-TYP-005 | Variables | Preservar inventario histórico; verificar bindings aplicables, scopes, aliases y resolución por modos con IDs locales reales. | Hash histórico, mapa y readback |
| AC-TYP-006 | Unidades | Cotejar porcentajes, AUTO y conversiones por destino; ninguna sustitución silenciosa por valores próximos. | Campos reales y pruebas del adaptador |
| AC-TYP-007 | Integridad | Conservar vínculos, contenido, propiedades, colores, variantes y Slots; documentar sustituciones y ajustes geométricos necesarios. | Comparación estructural y matriz de cambios |
| AC-TYP-008 | Resultado Figma | Leer después del último cambio y revisar composiciones afectadas, fuentes y recortes. | QA por consumidor, capturas y lectura final |
| AC-TYP-009 | Cierre | Estados separados, documentación/implementación web y skills actualizadas con controles aplicables ejecutados. | Registros y QA por destino |

Sin lectura real no hay PASS de Figma. Un universo incompleto impide afirmar cobertura total; las limitaciones quedan `BLOCKED`, no `NOT_APPLICABLE`. La auditoría humana permanece pendiente aunque el QA técnico resulte conforme.

## 11. Preparación, versión y límites actuales

El [QA documental](../../qa/contracts/typography.v0.1.0.md) conserva `PASS` para el catálogo de 75 estilos. Los resultados de implementación permanecen separados:

| Alcance | Estado | Evidencia y límite |
|---|---|---|
| Estilos Figma | PASS | [QA independiente](../../implementations/figma/typography.v0.1.0.styles.qa.json): 75 definiciones, 304 bindings y 1216 resoluciones reales en cuatro modos; [mapa vigente](../../implementations/figma/typography.v0.1.0.catalog.state.json). |
| Documentación Figma | PASS | Página `Typography` `1003:412`; [readback](../../qa/implementations/typography/specimens.readback.json) de 75 tarjetas, 316 textos y 79 frames, sin errores registrados. |
| Preservación del diseño previo | PASS acotado | [QA adicional](../../implementations/figma/typography.v0.1.0.preservation.qa.json): 34 páginas, 3501 nodos y 3503 rangos; métricas, contenido, propiedades capturadas, cajas e IDs conservados. Solo 244 rangos con 1202 referencias añadidas canónicas. |
| Restauración literal | FAIL histórico conservado | [QA estricto](../../implementations/figma/typography.v0.1.0.restoration.qa.json): las 244 adiciones no son igualdad literal. El reporte no se modifica ni se convierte en PASS. |
| Consumidores Figma | BLOCKED | [Diagnóstico y pruebas](../../qa/implementations/typography/Figma-blocker.md): la asignación de TextStyles puede propagarse entre textos con referencias de propiedad compartidas; la causa interna sigue sin resolver. No se sustituyeron los IDs originales como solución. |
| Tipografía web | PASS acotado | [Revisión de 75 estilos](../../qa/implementations/typography/web/revision-75/README.md): 75 × cuatro temas y 2956 mediciones de textos en 43 familias; generador, determinismo, TypeScript y build comprobados. No acredita Figma ni composiciones arbitrarias. |

La preservación compara las propiedades capturadas por el censo y las cajas de texto; no sustituye una revisión visual universal de todos los frames. El cierre de skills y Graphify corresponde a su lote y conserva sus propios controles. Resolver el bloqueo Figma requiere una intervención concreta evaluada y una nueva lectura completa tras la última escritura; el catálogo y el mapping no autorizan a declarar `VALIDATED` a sus consumidores.

Los cambios normativos futuros se versionan por su impacto en consumidores y se registran con alcance. La introducción de estilos no cambia el estado de aprobación de los contratos históricos. Los hashes del contrato y sus datos se guardan fuera de sus propios contenidos cuando corresponda; el contrato no incorpora su propio digest.

| Versión | Fecha | Cambio | Decisión |
|---|---|---|---|
| 0.1.0 | 2026-10-15 | Catálogo documental y 75 estilos Figma PASS; documentación y web PASS por alcance; preservación con adiciones canónicas PASS, restauración literal FAIL conservado y consumidores Figma BLOCKED | DEC-TYPOGRAPHY-STYLES-001 |
