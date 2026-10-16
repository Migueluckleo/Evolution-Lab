# Propuesta acotada: consumo tipográfico mediante herencia nativa de103 rangos

**Estado: PROPUESTA LOCAL; NO NORMA ACTIVA.** Este archivo no modifica Specs, datos, Figma, Graphify ni paquetes. Auditoría humana continúa PENDING. Solo puede materializarse dentro de la delegación existente después de comprobar103 cadenas reales y tres pilotos causales; no deducir aprobación de esos resultados.

## Evidencia disponible y condición de entrada

El único piloto causal completo leído en este corte es `inheritance-checkbox-five-sixths/evaluation.json`: `CAUSAL_INHERITANCE_SUPPORTED_FOR_THIS_PILOT`, una relación original446:167→149:179 y actor149:180/control149:183. Las lecturas A/B/A restaurado conservaron ID vacío en la instancia; el cambio de estilo del actor principal propagó propiedades tipográficas y su restauración recuperó todos los campos. Cero writes sobre el texto de instancia y limpieza confirmada. El propio reporte limita su alcance a ese piloto.

Antes de adoptar la excepción se requieren: (a) las103 cadenas completas leídas por API, incluyendo cada salto instancia→principal y la ruta real al texto; (b) pilotos causales aislados de2/3,5/6 y4/3, con controles, guards de originales y restauración exacta; (c) lectura final independiente de todos los103 rangos después de la última escritura. Un piloto, el sufijo de un nodeId, la igualdad numérica o una escala aparente no sustituyen esa prueba. No doy por existentes ni PASS los otros dos pilotos ni el reporte103; se añadirán sus rutas y hashes reales cuando existan.

## Alcance normativo exacto de la sustitución propuesta

Crear **una enmienda transversal nueva**, ruta propuesta `specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md`, sin reescribir los siete MD históricos siguientes. Su encabezado debe enumerar cada fuente, versión, sección y subconjunto sustituido:

| Fuente existente | Sustitución acotada |
|---|---|
| `specs/foundations/typography.contract.v0.1.0.md` | REQ-TYP-004 y su criterio AC-TYP-004; §3 «Derivados necesarios para instancias escaladas», únicamente obligación de ID local del derivado y significado de su vínculo Figma. Las fórmulas/métricas siguen vigentes. |
| `specs/foundations/typography.formatting.amendment.v0.1.1.md` | Párrafo de103 `UNRESOLVED_SCALED_LINK` en «Evidencia y técnica de aplicación» y selección del catálogo activo. Preservar íntegramente solución UNDERLINE27 y técnica por rango3250. |
| `specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md` | TYC-01 y TYC-06 solo para entradas del overlay103; interpretación de preparación/bloqueo para ese subconjunto. La selección lógica, identidad métrica y demás obligaciones de las43 familias continúan. |
| `specs/components/select.typography.amendment.v0.1.0.md` | Cuatro filas Left/Right label del derivado5/6:64 rangos; §preparación y párrafo derivados. |
| `specs/components/dropdown-item.typography.amendment.v0.1.0.md` | Seis filas Left/Right label derivadas:12 rangos5/6 y14 rangos2/3; §preparación y párrafo derivados. |
| `specs/components/header.typography.amendment.v0.1.0.md` | Dos filas Count label:12 rangos4/3; §preparación y párrafo derivados. No tocar sustitución histórica empresa/RFC. |
| `specs/components/app-shell.typography.amendment.v0.1.0.md` | Una fila Count label:1 rango4/3; §preparación y párrafo derivados. |

La enmienda única identifica las13 filas y su selección completa en un overlay de103 pares nodo/rango; no duplica sus recetas ni genera43 enmiendas nuevas. Añadirla a `amendments` de esas cuatro entradas en `components.registry.json` y a registros vigentes hace que cada cierre contractual sea base + enmienda tipográfica histórica + overlay nuevo. Las39 familias restantes conservan sus reglas. Si se exige navegación desde un Spec aislado sin consultar el registro, añadir cuatro enmiendas breves de vínculo; es alternativa de cinco MD, no necesaria para el cierre indexado actual y no permite editar silenciosamente0.1.0.

### Redacción sustitutiva propuesta

**REQ-TYP-004 / TYC-01:** Cada rango UI debe resolver una identidad tipográfica compartida verificable y sus propiedades. Fuera del overlay103, exigir el TextStyle ID directo de su asignación. Para las103 entradas cerradas por evidencia, admitir `INHERITED_NATIVE_SCALE`: el principal real conserva el TextStyle ID de origen y la instancia hereda su efecto mediante la cadena nativa comprobada. Conservar el ID local vacío tal como lo reporta Figma; no fabricar un ID resuelto en ese campo ni aceptar vacíos fuera del conjunto. La prueba incluye cadena, fuente de estilo, escala nativa, propiedades resueltas, bindings y ausencia de overrides incompatibles.

**§escalados / TYC-06:** Los tres IDs derivados continúan identificando las recetas efectivas materializadas del catálogo y del CSS; `recipeScale=1` gobierna su comparación numérica. El mecanismo Figma demostrado usa el estilo principal y `nativeScale` observado. No asignar el TextStyle materializado a la instancia nativa ni volver a escalar la receta derivada. No restablecer transformaciones, separar instancias, reemplazar nodos, borrar propiedades ni añadir overrides para fabricar cumplimiento. Una relación que pierda cadena, estilo principal, escala, propiedades o controles vuelve a `BLOCKED`.

Esto amplía el mecanismo admisible de consumo con evidencia; no declara que un ID vacío sea siempre válido, ni reclasifica retroactivamente como PASS los fallos de aplicación directa.

## Overlay de binding: separación de identidad métrica y vínculo real

Ruta **propuesta, aún inexistente**: `implementations/figma/typography.native-inheritance.v0.1.2.binding.json`. Mantener el mapping0.1.1 inmutable y referenciar su SHA; así sus índices N y las43 tablas históricas no cambian. El overlay se une por `{pageId,nodeId,start,end}`, nunca por orden del array. Debe incluir exactamente103 claves únicas existentes, ninguna UI adicional.

Campos propuestos por entrada (nombres finales coordinados con el verificador):

- `metricStyleLogicalId`: ID derivado existente; mantiene receta y `recipeScale:1`.
- `bindingMode: INHERITED_NATIVE_SCALE`; `principalStyleLogicalId`, `principalTextStyleId` y `principalTextNodeId` leídos y verificados.
- `nativeScale`: valor Float32 observado, ratio documentado y procedencia. No multiplicar factores acumulados de ancestros ni inferir escala desde fontSize.
- `instanceChain`: todos los saltos reales a principales y rutas a texto comprobadas mediante API, con IDs y fuentes/hash de la lectura. La cadena es evidencia, no reconstrucción textual del ID.
- `observedLocalTextStyleId`: valor real, incluso `""`; mantener separado de `principalTextStyleId`.
- `evidence`: lectura103, piloto de la clase2/3,5/6 o4/3, verificación final y sus hashes/alcances. `applicationStatus` solo pasa de pendiente con todos los controles satisfechos.

| Receta métrica conservada | Rangos | Estilo principal real requerido | TextStyle ID principal existente | Escala efectiva |
|---|---:|---|---|---|
| `ui-checkbox-label-scaled-two-thirds` |14|`ui-body-compact`|`S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,`|Float32(2/3)|
| `ui-checkbox-label-scaled-five-sixths` |76|`ui-body-compact`|`S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,`|Float32(5/6)|
| `micro-count-small-scaled-four-thirds` |13|`micro-count-small`|`S:2987fb55403e26b9fd23807ce894f58cc084820d,`|Float32(4/3)|

Estos IDs están presentes en catalog.state0.1.1; su presencia no acredita cada cadena. La comprobación de receta debe conservar dos comparaciones separadas: receta efectiva actual contra derivado a escala1 y receta de principal transformada una sola vez por la escala nativa documentada, con codificación Float32 existente. No añadir tolerancia ni reinterpretar porcentajes/AUTO.

## Catálogo0.1.2: cambio documental, cero nuevas tipografías

Crear `specs/tokens/ai-design-system.typography.v0.1.2.json` a partir del1.1; conservar79 estilos, orden, IDs, nombres, familia/peso/tamaño, lineHeight, letterSpacing, textDecoration, tokenRefs, derivedFormattingFrom, factores/ratios y consumerScope. No crear80.º estilo ni modificar los cuatro UNDERLINE.

Cambio de contenido de estilos limitado a `description` y `derivedFrom.reason` en los tres IDs de la tabla. Sustituir la promesa «Permite un TextStyle explícito…» por la explicación de receta efectiva para comparar/exportar; en los103 consumidores Figma comprobados el vínculo procede del estilo principal mediante herencia nativa y escala, no de asignar el materializado a la instancia. Mantener el rol y restricción de uso propios al inicio de cada description; no duplicar uso en otro campo.

**Una frase global también requiere aclaración:** `units.derived_style_encoding` hoy termina «recipeScale=1 al aplicar el estilo derivado». Propuesta mínima: «recipeScale=1 al comparar la receta materializada; el mecanismo Figma de los consumidores incluidos en el overlay se rige por la enmienda de herencia nativa». Es corrección de metadatos explicativos, no de valores/unidades. Si se mantiene literalmente por limitar la nueva versión a tres estilos, la enmienda debe sustituir expresamente su lectura operativa; recomiendo corregirla para evitar dos instrucciones incompatibles. Actualizar version/supersedes/authority y fuentes/hash solo como metadatos de procedencia, sin reescribir inventarios históricos.

El diff de validación permite esas seis cadenas, la frase de units y metadatos de versión/procedencia; toda diferencia restante en `styles` debe fallar. La documentación derivada web/Figma y las tres descripciones reales de TextStyle deben reflejar la única description nueva; no reconstruir79 tarjetas ni cambiar muestras o métricas. El styleMap79 conserva IDs y exige nuevo readback de descripciones tras la escritura autorizada.

## Archivos mínimos y derivaciones afectadas

Núcleo nuevo: **un MD normativo transversal + un JSON canónico1.2 + un overlay de binding**. Evidencia de103 cadenas, pilotos y readback final en sus archivos propios; no generar rutas ficticias antes de existir. Modificación de registro: `components.registry.json` añade una referencia en cuatro familias; `registry/contracts.md`, `sources.md`, `decisions.md`/DEC y `implementations.md` registran versión, alcance, procedencia y QA por destino, conservando entradas históricas.

Verificador: `typography_qa.py` debe leer overlay de manera explícita, conservar modo directo y fallos históricos, y rechazar vacío/ID ajeno fuera de sus103 claves. Emitir contadores separados:3250 rangos directos,103 por herencia probada y0 sin resolución **solo si la lectura completa lo demuestra**. `typography_mapping.py` no tiene que reescribir0.1.1 ni cambiar3353 identidades: puede emitir el overlay desde evidencia independiente. Los preparadores de llamadas nunca asignarán el derivado a esas instancias.

Web: actualizar selector de catálogo en `implementations/web/scripts/typography.py`, regenerar metadatos/documentación y verificar que las79 recetas/CSS de presentación no cambian. Sí cambian hashes/procedencia y texto documental; comparar métricas/identidades por clase es pertinente, no rediseñar componentes.

Skills: actualizar las referencias activas al catálogo1.2 y la excepción acotada en ambas habilidades. `handoff.mjs` debe incluir enmienda nueva + catálogo1.2, y el overlay/evidencia cuando un componente usado los consuma; conservar el ID lógico de receta, no reemplazarlo por el estilo principal solo porque las métricas web son materializadas. Revisión de `verify-offline.mjs` y `HandoffTypographyTests` para que exijan las dependencias nuevas y rechacen vacíos sin evidencia; ejecutar pruebas reales de HTML/handoff. Los snapshots ya seleccionan `specs/**`, `implementations/figma/**` y QA pertinente: no hace falta ampliar config ni introducir copias editables. AGENTS/P07 deben apuntar a la nueva enmienda/catálogo vigente sin alterar históricos.

P08: después de completar evidencia, documento y derivados, reconstituir candidato y ejecutar `skills sync --bump patch`, `check`, `export` y la instalación gestionada autorizada; desde current0.2.0 corresponde0.2.1 si sigue sin publicarse. Ambas skills comparten corte/digest. No reutilizar los ZIP provisionales actuales ni sus hashes: ya representan otro corte. No hay actualización automática de otras máquinas, hooks o daemon; el instalador conserva copias editadas por el usuario. El registro de cierre vive en registry/skills.md y qa/skills, fuera del fingerprint. Graphify se cierra por root después del lote, no por esta propuesta.

## Criterios antes de liberar el corte

1. Tres pilotos causales con A/B/A, controles, restauración/limpieza y guards de originales;103 cadenas reales completas. Conservar toda evidencia previa FAIL/NO_STYLE.
2. Overlay103 exacto: Select64, Dropdown Item26, Header12 y App Shell1; grupos14/76/13; conjunto idéntico al mapping1.1 bloqueado. Ninguna correspondencia por nombre o índice cambiante.
3. Catálogo79 conserva todas las recetas; cambio documental restringido. Styles readback y documentación actualizados con evidencia real y estados propios.
4. Lectura global posterior a la última escritura:3351 nodos/3353 rangos UI,150 editoriales conservados y páginas pertinentes; contenido, IDs, geometría, propiedades, bindings y decoración sin regresiones. La excepción no borra exigencias del resto de consumidores.
5. QA separa `DIRECT_STYLE_ID`, `INHERITED_NATIVE_SCALE`, `UNRESOLVED`; no afirma0 IDs locales vacíos si Figma devuelve103. Cero sin resolución exige prueba, no traducción de métricas correctas a estilos.
6. QA documental, web y candidato offline/handoff de las dos skills después del nuevo corte; freeze explícito antes de publicar. Hasta entonces, mantener ejecución IN_PROGRESS y103 BLOCKED en los documentos activos existentes.

## Fuentes exactas leídas

- `specs/foundations/typography.contract.v0.1.0.md` · SHA256 `d82bcd7feac16fcf7c6211da0c3dc5f0cabd75899dcc1098a20bd3e1230fc217`
- `specs/foundations/typography.formatting.amendment.v0.1.1.md` · SHA256 `62af87741a8785b4b842a0305e0c6ebec407e24909707be59ede6dedcaa866f6`
- `specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md` · SHA256 `da00e475aef0de122831af0ba454b375772294d3afd1f7df4a962de52f778b59`
- `specs/components/select.typography.amendment.v0.1.0.md` · SHA256 `a417b478c62fe0cf04bcaf6c2621611628208578b8428e681254e9734d74caba`
- `specs/components/dropdown-item.typography.amendment.v0.1.0.md` · SHA256 `5ba8f1a160b2122fac8bc624f6d34436fcaae2b5456df3850732775de4bd582d`
- `specs/components/header.typography.amendment.v0.1.0.md` · SHA256 `9bf2db753a9224da9ee9bfdd2d33f229c7a99d15632d1ee810861ee927f49440`
- `specs/components/app-shell.typography.amendment.v0.1.0.md` · SHA256 `74768a9059fed6ab27bbe6bc4b081f1ba4bae3b4e504e334ab442c45785cb31b`
- `specs/tokens/ai-design-system.typography.v0.1.1.json` · SHA256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`
- `implementations/figma/typography.v0.1.1.mapping.json` · SHA256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`
- `implementations/figma/typography.v0.1.1.catalog.state.json` · SHA256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`
- `qa/implementations/typography/consumption-v0.1.1/inheritance-checkbox-five-sixths/evaluation.json` · SHA256 `313189ee23f4ee89b0120fc26d2e7e337b0d111fb769618bed5cc1eac4db5715`
- `protocols/08-SKILLS-AND-RELEASES.md` · SHA256 `71cb5c40b6c18ae10494a55698dbd5b0bc423eb71a3cf4b72417fa180c8c5783`
- `config/ds-skills.json` · SHA256 `effbee7cb0d731587ec2df7763810b25902a2989ea25841bd26f3d99352aa69b`
