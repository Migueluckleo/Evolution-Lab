# Registro de fuentes

## SRC-CONVERSATION-COMPOSER-20261020 · INDEXED

Lectura directa del nodo `765:397`, archivo `tj3WIBEZDGLVs7MJWKCwgf`, página Conversation `765:6`, 2026-10-20. [Snapshot antes de corregir](../sources/figma-snapshots/conversation-composer.765-397.before.2026-10-20.json), SHA-256 `50845ce0a209c032bf95d6c3228a87bd7a75be27a21b9ef943fa563a2aa4e6c5`; [rangos de texto originales](../sources/figma-snapshots/conversation-composer.text.before.2026-10-20.json). Evidencia `OBSERVED`, no aprobación. Cobertura: anatomía, API, geometría, bindings del aviso y dependencias; la lectura posterior incluye hijos ocultos mediante skipInvisibleInstanceChildren=false. [Preflight canónico](../implementations/figma/conversation-composer.v0.1.2.preflight.json) y [readback final](../qa/implementations/conversation-composer.v0.1.2.final.json).

## SRC-TYPOGRAPHY-NATIVE-INHERITANCE-012 · 2026-10-15

El [catálogo 0.1.2](../specs/tokens/ai-design-system.typography.v0.1.2.json), SHA-256 `074a31a83f09b30a02fa8b8f0a7730bdb33fc0a8a9c59e3c8d2469b5799e934c`, y la [enmienda nativa](../specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md) separan receta métrica materializada de vínculo real al estilo principal por escala nativa. El JSON conserva 79 recetas/IDs/bindings; los cambios están limitados a tres `description`/motivos y metadatos explicativos. La evidencia es OBSERVED/DERIVED; no aprobación humana.

Los pilotos causales [Checkbox5/6](../qa/implementations/typography/consumption-v0.1.1/inheritance-checkbox-five-sixths/evaluation.json) y [Checkbox2/3](../qa/implementations/typography/consumption-v0.1.1/inheritance-checkbox-two-thirds/evaluation.json) conservan su alcance y hashes propios. La [evaluación103](../qa/implementations/typography/consumption-v0.1.1/inheritance103.evaluation.json), SHA-256 `afc4a25f9ca37c48660f6fca159d0d9a66cda5c0a13483a08a4e14d0baaaaa3d`, y su [informe](../qa/implementations/typography/consumption-v0.1.1/inheritance103.review.md) documentan103 cadenas admitidas,242 rutas, tres pilotos/36 controles, cero overrides tipográficos y seis incidencias crudas preservadas de frontera SLOT. Ese PASS de evidencia se complementa con el [overlay final](../qa/implementations/typography/consumption-v0.1.1/consumer-final.native-inheritance.v0.1.2.json), el [QA global de3353 rangos](../qa/implementations/typography/consumption-v0.1.1/consumer-final.global.v0.1.2.json) y el [readback independiente de79 estilos](../implementations/figma/typography.v0.1.2.styles.qa.json), todos `PASS` en su alcance. La [revisión final](../qa/implementations/typography.v0.1.2.review.md) conserva la limitación del guard no textual de Table y distingue la documentación posterior. No deducir validación de nuevos destinos a partir de estos resultados. El mapping 0.1.1 y los34 censos originales permanecen sin reescritura.

## SRC-TYPOGRAPHY-CONSUMPTION-011 · 2026-10-15

Fuentes del corte normativo de consumo: [catálogo 0.1.1](../specs/tokens/ai-design-system.typography.v0.1.1.json), SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`; [mapping 0.1.1](../implementations/figma/typography.v0.1.1.mapping.json), SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`; [mapa de 79 TextStyle IDs reales](../implementations/figma/typography.v0.1.1.catalog.state.json), SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. La foundation y su enmienda delegan las recetas al JSON; mapping y state son evidencia derivada/observada y no aprobación ni lectura final de todos los consumidores.

Los 34 censos previos y las 68 fuentes normativas de familias se conservan. La [enmienda transversal](../specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y las 43 enmiendas enlazadas registran hashes, variantes, dependencias y selectores por rango: 3353 rangos UI con correspondencia, 27 cambios a estilos de formato UNDERLINE y 103 rangos escalados con vínculo todavía bloqueado. Los 150 textos editoriales se identifican por separado. La selección de fuentes no equivale a aprobación humana ni a implementación Figma validada.

## SRC-TYPOGRAPHY-FORMAT-PROBES-011 · 2026-10-15

Evidencia técnica preservada: [setter posterior de decoración](../qa/implementations/typography/consumption-v0.1.1/probe.decoration-setter.failure.json), SHA-256 `0ced2be9fad9f561eb3c6df62b131d1c34ecb7c11350ae017d0abf60f8fa416f`, `FAIL` con 140 discrepancias tras once asignaciones en el clon; [estilos completos por rango y edición de instancias](../qa/implementations/typography/consumption-v0.1.1/probe.format-styles.persisted-and-instance-edit.json), SHA-256 `c186ae02e8763f5444c2d15af40de1ca8d680b8a17e81a12b0ee07bbe059034e`, `PASS` limitado a persistencia en la copia de Button y edición de propiedades TEXT en seis instancias. Se conserva el fallo anterior: no describe el estado de toda aplicación futura.

Las pruebas [derivada escalada](../qa/implementations/typography/consumption-v0.1.1/probe.scaled-derived.failure.json) y [receta principal sin vínculo](../qa/implementations/typography/consumption-v0.1.1/probe.scaled-base.no-style.json) acotan el límite restante. La [enmienda de formato](../specs/foundations/typography.formatting.amendment.v0.1.1.md) registra la técnica y sus restricciones. Esta entrada documenta evidencia existente; no declara un nuevo censo final ni sustituye el QA por destino.

## SRC-TYPOGRAPHY-REFERENCE-001 · 2026-10-15

Referencia explícita entregada por el usuario: [tabla original de 18 estilos](../sources/references/typography/user-style-list.2026-10-15.png), SHA-256 `52053d2a71f5db76f1a28c436a647597b46da486b543d88eff85b920e010e00e`. Conservada sin modificación. Las descripciones de uso se redactan bajo [DEC-TYPOGRAPHY-STYLES-001](DEC-TYPOGRAPHY-STYLES-001.md); no se atribuyen a la imagen.

## SRC-TYPOGRAPHY-FIGMA-CENSUS-001 · 2026-10-15

[Descubrimiento](../sources/figma-snapshots/typography.discovery.2026-10-15.json) y censo `sources/figma-snapshots/typography/census.before.<page-id>.json`: 34 páginas, 3501 nodos de texto y 3503 rangos, incluidos ocultos. Lectura del destino `tj3WIBEZDGLVs7MJWKCwgf`, autoridad `OBSERVED`; no sustituye contratos. El esquema compacto declara columnas y diccionarios sin omitir nodos: `idParts` se resuelve con `paths` y `;`, `nameIndex` con `names`, y cada segmento con `recipes`. Las firmas de preservación son comprobaciones dobles de contenido/estructura, no hashes criptográficos ni copias completas del archivo Figma. Los snapshots completos iniciales de ocho páginas se conservan como evidencia adicional.

## SRC-WEB-CONTRACT-AUDIT-013 · 2026-10-13

Fuentes leídas:43 contratos/enmiendas listados con hashes en [fichas web](../implementations/web/docs/components/README.md), JSON canónico y snapshots enlazados. Nuevas lecturas Figma solo de geometría, propiedades y trazados: [Button](../sources/figma-snapshots/button.web-contract-audit.2026-10-13.json), [Scrollbar](../sources/figma-snapshots/scrollbar-parts.web-contract-audit.2026-10-13.json), [Stepper](../sources/figma-snapshots/stepper-connectors.web-contract-audit.2026-10-13.json), [Table](../sources/figma-snapshots/table-icons.web-contract-audit.2026-10-13.json), [Modal Close](../sources/figma-snapshots/modal-close.web-contract-audit.2026-10-13.json), [Modal Footer](../sources/figma-snapshots/modal-footer.web-contract-audit.2026-10-13.json). Live drift OBSERVED separado: [Navigation](../sources/figma-snapshots/navigation.live-source-drift.2026-10-13.json), [Avatar](../sources/figma-snapshots/avatar.live-source-drift.2026-10-13.json), [Toggle](../sources/figma-snapshots/toggle.live-source-drift.2026-10-13.json). No reemplaza contratos ni modifica Figma. Los dos raster Modal se recuperaron tras autorización explícita, posterior al rechazo automático inicial; [manifiesto de originales](../sources/assets/web/modal.manifest.json), SHA-1 Figma y SHA-256 local comprobados. [QA y límite](../qa/implementations/web.contract-audit.v0.1.3.review.md).

## SRC-WEB-FIDELITY-012 · 2026-10-13

Evidencia OBSERVED de solo lectura en AI Design System: [Sidebar22 recetas](../sources/figma-snapshots/sidebar.web-fidelity.2026-10-13.json), [Metric Card8](../sources/figma-snapshots/metric-card.web-fidelity.2026-10-13.json), [Header/Modal](../sources/figma-snapshots/header-modal.web-fidelity.2026-10-13.json), [Loader/Header](../sources/figma-snapshots/loader-header.web-fidelity.2026-10-13.json) y [caret perfil SVG](../sources/figma-snapshots/header.profile-caret.web-fidelity.2026-10-13.svg). Complementa contratos vigentes; no cambia su autoridad ni aprobación.

[Logos.manifest.json](../sources/assets/web/logos.manifest.json) incorpora ocho exportaciones PNG originales por ID:434:4672,434:4925,434:4970,434:5038,434:5062,435:2656,435:2658,435:2660.72 assets disponibles; hashes/formato/dimensiones conservados. No redibujo ni recoloración. Dibujo Conversation procede de vectores originales verificados con el snapshot Anticipa, no de Characters escalado. Capturas y medidas del resultado web en [QA](../qa/implementations/web.fidelity.v0.1.2.review.md).

## SRC-WEB-LOGOS-EXPORT-001 · 2026-10-13

OBSERVED_EXPORT de AI-Design-System tj3WIBEZDGLVs7MJWKCwgf, página Logos427:122: [manifiesto](../sources/assets/web/logos.manifest.json) con 64 archivos originales, IDs, nombres, formato, dimensiones observadas y hashes. PNG/SVG según exportador. Ocho variantes pendientes por límite de consultas de Figma, enumeradas explícitamente. Los URLs temporales de descarga no se conservan como fuentes normativas. Inspección/exportación de solo lectura; no nueva aprobación ni QA geométrico Logos.

La capa web reutiliza además snapshots originales de Avatar, EmptyStates, Charts y trazados Characters de implementación local; [assets.py](../implementations/web/scripts/assets.py) identifica sus rutas. Los contratos y el JSON aprobado siguen siendo autoridad.

## SRC-ARTIFACT-RETENTION-2026-10-13 · INDEXED

OBSERVED operativo, no normativa de diseño. [Manifiesto](../qa/tooling/retention.2026-10-13.manifest.json): inventario de 673 derivados seguidos por Git, con ruta, tamaño, SHA-256 de bytes actuales, modo y blob original del índice; commit de partida 41ab4c0bf4197ef0a5b1dda73c7a6be81c818933. Respaldo local graphify-out/retention/2026-10-13-git-retention/tracked-derivatives.tar.gz, 7,840,848 bytes, SHA-256 d748bd900b97d91bbf00020d2ec4248fab5b54d44f0e9e4437ca5fb2288f1280. Cobertura 673/673 restaurados y comprobados. [QA y límites](../qa/tooling/retention.2026-10-13.review.md). Los originales permanecen en su ubicación; no se incorporan fuentes de diseño nuevas.

## SRC-CHAT-LAYOUT-2026-10-09

Fuente de esta revisión: AI Design System `tj3WIBEZDGLVs7MJWKCwgf`, página Chat783:6; principales783:24/783:116/797:316/797:458 y muestras784:103/784:163/798:316. Usuario declara haber ajustado width/scrolling y solicita documentación. [Readback](../qa/implementations/chat-layout.v0.1.1.observed.json), [estructura](../qa/implementations/chat-layout.v0.1.1.structure.json), [muestras/spacing](../qa/implementations/chat-layout.v0.1.1.instances-and-spacing.json). OBSERVED de destino, no extracción nueva de Anticipa ni Librería raíz. [Enmienda y procedencia](../specs/components/chat.layout.amendment.v0.1.1.md); ninguna mutación Figma.

## SRC-ECOSISTEMA-CHARACTERS-001 · 2026-10-08

[Ecosistema AI885:16275](https://www.figma.com/design/IlNQJgDKvCSqyXAkONcjxl/Ecosistema-AI?node-id=885-16275): beniStandBy209:6943 y messageAnalisisNavi269:5947. Inspección read-only93 nodos; [snapshot](../sources/figma-snapshots/characters.ecosistema.2026-10-08.json) y [envolturas](../sources/figma-snapshots/characters.wrappers.2026-10-08.json). Contratos fuente [BENI](../drafts/contracts/beni-standby.source.component-contract.md) y [NAVI](../drafts/contracts/navi-analysis.source.component-contract.md) con YAML. Cero tokens en origen.

## SRC-CHAT-SECTION-001 · 2026-10-08

Anticipa20355:74859, key bade7cd7895f387b35107ba565fd79ad7a2b0281, fuente externa compartida explícitamente; INDEXED como evidencia, no normativa. [MD/YAML de observación](../drafts/contracts/chat-section.source.component-contract.md), [árbol116 nodos](../sources/figma-snapshots/chat-section.index.2026-10-08.json), [dependencias39 instancias/18 principales](../sources/figma-snapshots/chat-section.binding-index.2026-10-08.json). Inspección PARTIAL de propiedades/prototipos históricos, sin cambios en fuente. Contrato destino separado y homologado al JSON canónico.

## SRC-CONVERSATION-CHARACTER-IDENTITY-001 · 2026-10-08

[Lectura fuente](../sources/figma-snapshots/conversation.characters.original.2026-10-08.json): Anticipa, personajes20355:72771/72795, siete rellenos efectivos; azul, naranja y gris originales, sin escritura fuente. [Estado previo destino](../implementations/figma/conversation.characters.v0.1.1.before.json). Valores OBSERVED adoptados por DEC-CHARACTER-IDENTITY-001; extensión canónica de destino separada del inventario histórico.

## SRC-FIGMA-CONVERSATION-DESTINATION-001 · 2026-10-08

[Preflight local](../implementations/figma/conversation.v0.1.0.preflight.json), [tokens consumidos](../implementations/figma/conversation.v0.1.0.tokens-readback.json) y [lectura final](../qa/implementations/conversation.v0.1.0.final.json) son evidencia OBSERVED del destino, no nuevo inventario normativo. Se contrastan con JSON canónico y extensiones SIX-FAMILY-COLOR/DOT-BACKGROUND vigentes. La entrada fuente inferior conserva el corte de ingesta; implementación actual registrada aparte, sin modificar Anticipa.

## SRC-FIGMA-CONVERSATION-EXTERNAL-001 · INDEXED · 2026-10-08

Fuente externa nominada por el usuario: [Anticipa Conversation](https://www.figma.com/design/zuUq3gcF9T3CLid44bjY6W/Anticipa-Junio2026?node-id=20355-72763), página Components17001:89455, set20355:72763. Autoridad OBSERVED_NON_NORMATIVE. [Snapshot](../sources/figma-snapshots/conversation.20355-72763.observation.2026-10-08.json),160203 bytes, SHA-256 `f02bf89ff7c06a101d372fe62fdf34b335155f5a94be9a225582573477632193`; [MD](../drafts/contracts/conversation.source.component-contract.md) y [YAML](../drafts/contracts/conversation.source.component-contract.yaml) de evidencia PARTIAL.147 nodos recorridos incluidos26 con visible=false;47 instancias/21 principales,51 variables usadas, tres estilos, siete Slots y15 reacciones resumidas. Límites por propiedad/dependencia explícitos; no implementación ni QA destino. [Reporte de ingesta y alcance](../drafts/reports/conversation.external-intake.2026-10-08.md). JSON canónico intacto; grafo no regenerado.

## SRC-FIGMA-APP-SHELL-001 · INDEXED · 2026-10-06

Fuente observacional de solo lectura: Librería9zs5RMR8LB5wHjW9Bd59BA, Breakpoints8284:12565, página2798:22643. [Snapshot](../sources/figma-snapshots/app-shell.source.v0.1.0.json), SHA256eaae3b98b01ae2bdc32703b0b659980ad47c541665221b0e3ffb3350cf378021; [dependencias](../sources/figma-snapshots/app-shell.dependencies.v0.1.0.json), SHA25669f80b10cf07e0cfe660bb15e7b62e5684adf576a0506c24dd1eb5662c5b18a1.148nodos recorridos,48instancias/27mains,49variables referidas. [Proyección MD/YAML](../drafts/contracts/app-shell.source.component-contract.md) PARTIAL para detalles anidados no duplicados; no autoridad normativa. Destino se construye desde APP-SHELL-001 y contratos Header/Sidebar vigentes, no desde valores desconocidos. JSON aprobado sin cambios.

## SRC-SPECS-PROMOTION-20261006 · INDEXED

Diecinueve contratos/enmiendas locales y sus QA existentes leídos como evidencia para promoción. Los bytes previos se conservan en archive/specs-promotion-2026-10-06/; [manifiesto](../qa/contracts/specs-promotion.2026-10-06.manifest.json) registra SHA-256 de original, publicado, puntero, QA y datos protegidos. Los archivos archivados son historia, no norma paralela. Inventario fuente, extensiones JSON y QA originales intactos; ninguna nueva lectura del Figma fuente ni cambio de autoridad de esos datos.

## SRC-LOGOS-REFINEMENT-20261006 · INDEXED

Lectura actual de seis sets fuente/destino y57 diferencias previas; [evidencia](../qa/implementations/logos.refinement.v0.1.1.review.md). Checksum original conservado como baseline, sin reemplazarlo por observación reciente. Tres exportSettings SVG cambiaron en fuente desde el corte anterior; el destino coincide con el baseline en esos campos. No propagados ni convertidos en nueva tarea. Fuente intacta.

## SRC-RADIO-CHECKBOX-REFINEMENT-20261006 · INDEXED

Origen9zs5RMR8LB5wHjW9Bd59BA: Radio1230:24283 (53nodos), Checkbox1221:28710 (86). Destino tj3WIBEZDGLVs7MJWKCwgf: Radio142:144/143:166 (66), Checkbox149:199 (77). Lecturas OBSERVED, comparación DERIVED; snapshots y manifiesto enlazados en [QA](../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md). Tipografía y estructura comparadas con contratos reales y JSON canónico sin modificar la fuente. No se confunden IDs entre archivos.

## SRC-SIX-FAMILY-COLOR-20261005 · INDEXED

Lecturas de solo lectura de Librería9zs5RMR8LB5wHjW9Bd59BA y AI-Design-Systemtj3WIBEZDGLVs7MJWKCwgf. Raíces identificadas en la [enmienda](../specs/components/six-family-color.amendment.v0.1.0.md); snapshots fuente/antes/después en qa/implementations por familia. Los IDs de origen y destino están separados. JSON histórico preservado. Evidencia OBSERVED; cálculos RGB/contraste DERIVED. [QA](../qa/implementations/six-families.color.v0.1.0.review.md) delimita cobertura y no atribuye aprobación humana.

## SRC-FILTER-CHIP-SEMANTIC-021 · 2026-10-05

[Fuente viva de 24 variantes](../qa/implementations/filter-chip.semantic.v0.2.1.source.json), [preflight destino](../qa/implementations/filter-chip.semantic.v0.2.1.preflight.json) y [readback final](../qa/implementations/filter-chip.semantic.v0.2.1.readback.json). Roles y aliases existentes contrastados contra inventario canónico sin cambios; la única ampliación vive en [JSON inverse icon](../specs/tokens/ai-design-system.inverse-icon.v0.1.0.json). Evidencias OBSERVED/DERIVED, no aprobación humana. [QA](../qa/implementations/filter-chip.semantic.v0.2.1.figma.review.md).

## SRC-BUTTON-LOCAL-BINDINGS-022 · 2026-10-05

Readback vivo del destino tj3WIBEZDGLVs7MJWKCwgf/set26:81 y ocho raíces consumidoras/control. [Antes](../qa/implementations/buttons.local-bindings.v0.2.2.before.json), [después](../qa/implementations/buttons.local-bindings.v0.2.2.after.json), [matriz exacta](../qa/implementations/buttons.local-bindings.v0.2.2.exact-readback.json), [mapa derivado](../implementations/figma/buttons.local-bindings.v0.2.2.token-map.json) SHA-256 1a1edb0ef966871ae1a98de544d5fcedc861a5a9b367b1074166d5329401cf49. Inventario canónico intacto (cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474); fuente normativa de los nueve roles. Los snapshots son evidencia OBSERVED/DERIVED, no otro inventario editable. Capturas antes/después idénticas, SHA-256 8b4a7c85f3ec9138a0588f8b922b676696d81f8ffb503d2cef3bb04ba7a4bd04. Cobertura y límites en [QA](../qa/implementations/button.local-bindings.v0.2.2.figma.review.md).

## Evidencia de refinamiento · 2026-10-05

- SRC-FIGMA-SEARCH-001 ampliado con [readback fuente](../sources/figma-snapshots/search.v0.1.1.source-readback.json), solo lectura del set1560:44694; no modifica snapshot histórico.
- [Readback destino Search](../qa/implementations/search.v0.1.1.readback.json), set418:263: evidencia de correspondencia para0.1.1.
- [Descubrimiento Buttons](../qa/implementations/buttons.refinement.v0.1.0.discovery.json) y [variables remotas resueltas](../qa/implementations/buttons.refinement.v0.1.0.remote-variables.json), set26:81: evidencia, no especificación ni autorización de sustitución basada solo en nombres.
- Inventario canónico sin modificación; [cierre y pendientes](SESSION-HANDOFF-2026-10-05-REFINEMENT.md).

## SRC-FIGMA-EMPTY-STATES-001 · 2026-10-05

Raíz9zs5RMR8LB5wHjW9Bd59BA, página3027:406, sección7772:2225, set7772:2272. [Resumen](../sources/figma-snapshots/empty-states.v0.1.0.summary.json), [identidad](../sources/figma-snapshots/empty-states.v0.1.0.identity.json), [observación MD/YAML](../drafts/contracts/empty-states.source.component-contract.md) PARTIAL explícita:433nodos/27ocultos,11dependencias,22variables,2estilos. SeisSVG originales conservados, fuente sin mutaciones. [Manifest de hashes](../implementations/figma/empty-states.v0.1.0.manifest.json).

## SRC-FIGMA-SIDEBAR-001 · 2026-10-05

Fuente raíz9zs5RMR8LB5wHjW9Bd59BA, página268:20244; roots3365:23953,8283:544,8283:4142. [Snapshot](../sources/figma-snapshots/sidebar.v0.1.0.source.json), SHA2561ae050ab1e062a221edc4ab473456abeb8005037075b164acc960cd89005e73e.286nodos/93instancias,17dependencias,48variables. Fuente inmutable; [observación MD/YAML](../drafts/figma/sidebar.observed.v0.1.0.md) PARTIAL explícita, no contrato aprobado del origen.

## SRC-FIGMA-MODAL-001 · 2026-10-01

Librería raíz9zs5RMR8LB5wHjW9Bd59BA, página4886:869; seis roots en [snapshot](../sources/figma-snapshots/modal.v0.1.0.source.json), SHA256cf55d6f96b11c37b68391198f1f8e3014197dee950fdeccc3f03cc4159d4d60f.359nodos/131instancias,17mains,29variables,4estilos;70nodos ocultos. Fuente solo leída. [MD/YAML observacional](../drafts/contracts/modal.source.component-contract.md) PARTIAL en normalización y metadatos externos, no se declara COMPLETE.

## SRC-FIGMA-TABLE-ANTICIPA-001 · 2026-10-01

Fuente alternativa autorizada: Anticipa `zuUq3gcF9T3CLid44bjY6W`, nodo15006:84823. [MD/YAML observado](../drafts/contracts/table-anticipa.source.component-contract.md), snapshots `sources/figma-snapshots/table-anticipa.v0.1.0.*`:1449nodos/456instancias,15keys,36variables y2estilos. Fuente solo leída. Metadatos de dependencias parciales explícitos (paths/overrides); [decisión](DEC-TABLE-ANTICIPA-SOURCE-001.md).

## SRC-FIGMA-HEADER-001 · 2026-10-01

INDEXED · OBSERVED. Fuente9zs5RMR8LB5wHjW9Bd59BA, Header1349:4907. [Snapshot110nodos](../sources/figma-snapshots/header.source.v0.1.0.json), [25instancias/16mains](../sources/figma-snapshots/header.dependencies.v0.1.0.json), [35variables](../sources/figma-snapshots/header.source-variables.v0.1.0.json), [MD/YAML fuente](../drafts/contracts/header.source.component-contract.md) y [SVG de caret no importable](../sources/figma-snapshots/header.company-caret.source.svg). Recorrido de estilos:0referencias nombradas. Lectura fuente sin mutaciones; preferidos remotos resumidos, no desplegados como dependencias nuevas.

## SRC-FIGMA-SELECT-COMPOSITION-001

2026-09-29 · INDEXED · OBSERVED, no aprobación. Fuente9zs5RMR8LB5wHjW9Bd59BA, ejemplos2488:13364/2488:13365. [Snapshot](../sources/figma-snapshots/select-composition.source.v0.1.0.json), SHA-2562e426526a4637b3336212fbb019dcc7a210985b7cc8875512408fe3380e42f38. Recorrido134nodos,44invisibles;8principales agrupados,40variables,1estilo. Extracción profunda de dependencias referencial y metadatos externos parciales: ver [fuente MD](../drafts/contracts/select.source.component-contract.md). Fuente histórica inalterada.

## SRC-FIGMA-SELECT-001

- **Estado:** INDEXED, 2026-09-28. Fuente de solo lectura Librería anterior, página268:20247, set2479:11730; ejemplos2488:13364–13372.
- **Evidencia:** [snapshot](../sources/figma-snapshots/select.source.v0.1.0.json), SHA-256 `0c105f7924d2de0a3566764a063aac646a8a68852d699ba813daac11a0d4525c`; 18 variantes,361 nodos recorridos y72 instancias de dependencias.
- **Proyección:** [MD](../drafts/contracts/dropdown-item.source.component-contract.md) / [YAML](../drafts/contracts/dropdown-item.source.component-contract.yaml), PARTIAL exclusivamente para metadatos externos/candidatos de swap no usados; no simula comportamiento de producto.
- **Destino observado:** [24 roles locales y aliases](../sources/figma-snapshots/select.target-tokens.v0.1.0.json), SHA-256 `85d1a49b5fe191ca8c0d764a3e287e70cc60b6ae25fa08657e05fd211ca1e251`. Evidencia derivada, no reemplaza el JSON aprobado.

## SRC-FIGMA-LOGOS-001

- **Estado:** INDEXED, 2026-09-28. Librería anterior 9zs5RMR8LB5wHjW9Bd59BA, página 40:93; fuente de solo lectura.
- **Cobertura:** seis sets (72 variantes) y doce frames sueltos, 2,999 nodos; wrapper documental excluido.
- **Evidencia:** [inventario](../sources/figma-snapshots/logos.inventory.v0.1.0.json), SHA-256 `21e4c266cbf40da4fe984219bea8d4a0d7d3b0df60c053d809a40ad8d335e570`; [baseline](../sources/figma-snapshots/logos.fidelity-baseline.v0.1.0.json), SHA-256 `059d20b88c23b366af4c643daec5c2862e6434e24e1e9cd0b4a3a79b4fbea3ad`.
- **Bindings fuente:** ocho vectores de assets sueltos; [resolución de variables](../sources/figma-snapshots/logos.source-variables.v0.1.0.json). No autorizan bindings destino: DEC-LOGOS-AGNOSTIC-ASSETS-001 exige assets agnósticos.
- **Proyección:** [MD](../drafts/contracts/logos.source.component-contract.md) y [YAML](../drafts/contracts/logos.source.component-contract.yaml). No confundir con el discovery histórico de Header/Logo Categoria8321:504.


## SRC-TOGGLE-MIXED-PNG-001

- **Estado de ingesta:** `INDEXED` (2026-09-24).
- **Original preservado:** [PNG del usuario](../references/toggle-mixed-user-2026-09-24.png), 80×40 píxeles, SHA-256 bytes `cb4e42dec4d35d485f30520ad2848f6debce127f32068f818427f1bcbfd0b532`.
- **Procedencia y rol:** adjunto del usuario para el valor visual Mixed de un Toggle agregado. La copia local conserva la imagen entregada; no contiene un contrato de Figma ni define por sí sola comportamiento de clic.
- **Lectura:** pista azul en píldora con guion blanco horizontal centrado; junto con la explicación del usuario sustenta la [enmienda Mixed](../drafts/contracts/toggle.mixed-amendment.v0.1.4.md).

## SRC-TOKENS-INV-001

- **Estado de ingesta:** `INDEXED` (2026-09-22).
- **Ruta preservada:** [tokens.inventory.json](../sources/inventories/tokens.inventory.json).
- **Procedencia:** archivo entregado por el usuario en `/Users/miguel.leo/Downloads/tokens.inventory.json`; copia byte a byte comprobada con `cmp`. El nombre del archivo no acredita aprobación.
- **Clase y rol:** inventario JSON estructurado; evidencia candidata para datos canónicos de foundations/tokens.
- **SHA-256 de bytes:** `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.
- **Tamaño:** 198376 bytes. **Cobertura:** JSON completo analizado, 2 colecciones y 270 variables; sintaxis, campos, modos, valores y aliases recorridos programáticamente.
- **`fileKey` declarado:** `9zs5RMR8LB5wHjW9Bd59BA`. Es metadato del inventario/fuente, no el destino de reconstrucción `tj3WIBEZDGLVs7MJWKCwgf`. No se verificó el archivo Figma fuente.
- **Autoridad comprobada:** al ingresar no constaba aprobación. El usuario aprobó posteriormente estos bytes como datos canónicos vinculados al contrato `FOUNDATIONS-TOKENS-001` versión `0.1.0` para Figma; véase [DEC-TOKENS-001](decisions.md). El archivo no se modificó.
- **Relación:** la auditoría `SRC-TOKENS-AUD-001` afirma describir los ajustes presentes en este inventario. El hash de serialización canónica indicado en ella coincide con el calculado para estos bytes.

## SRC-TOKENS-AUD-001

- **Estado de ingesta:** `INDEXED` (2026-09-22).
- **Ruta preservada:** [tokens.audit.md](../sources/audits/tokens.audit.md).
- **Procedencia:** archivo entregado por el usuario en `/Users/miguel.leo/Downloads/tokens.audit.md`; copia byte a byte comprobada con `cmp`.
- **Clase y rol:** informe de ajustes y hallazgos, no instrucción operativa ni aprobación autónoma.
- **SHA-256 de bytes:** `5882f1b4be20ce0e038ec9ccdec262a54af2e749b633f52da7d21451a4ac15e3`.
- **Tamaño:** 7959 bytes. **Cobertura:** 233 líneas leídas.
- **Autoridad comprobada:** no consta aprobación independiente de los cambios. Las afirmaciones de inspección de Figma son del informe; no se inspeccionó Figma en esta tarea.
- **Relación:** el informe llama al resultado `tokens.inventory.corrected.json`, mientras el archivo recibido se llama `tokens.inventory.json`. Se confirma la correspondencia por el hash canónico declarado y el contenido final, no por el nombre. La versión previa `tokens.inventory.enriched.json` no fue entregada; no se verificó un diff histórico.

## SRC-AI-DS-CONTROL-COLORS-001

- **Clase y rol:** [JSON de extensión de destino](../drafts/foundations/ai-design-system.control-colors.v0.1.0.json), SHA-256 `4ef75143af30b0e934cb94aa62d3acb56c32874dc7e229a500a31c8928a7f839`, redactado durante esta migración bajo [DEC-SEMANTIC-EXTENSIONS-001](decisions.md). No es evidencia de que los dos roles existieran en la Librería fuente ni sustituye `SRC-TOKENS-INV-001`.
- **Cobertura y autoridad:** dos variables semánticas nuevas con scopes propios y ocho aliases a la primitiva ya aprobada `color/neutral/500`; `DELEGATED_FOR_BUILD`, [QA documental](../qa/contracts/foundations.control-colors.amendment.v0.1.1.review.md) `PASS`, [readback de Figma](../qa/implementations/control-colors.v0.1.0.figma.review.md) `PASS`, auditoría humana pendiente.

## Métodos de comprobación

SHA-256 calculado sobre bytes con `shasum -a 256`. El hash canónico de la auditoría se reprodujo con JSON UTF-8, `sort_keys=True`, `separators=(',', ':')` y `ensure_ascii=False`; ese hash no sustituye el SHA-256 de bytes. Ninguna de las dos fuentes es un contrato aprobado.

## SRC-FIGMA-BUTTON-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** `AI-Design-System`, file key `tj3WIBEZDGLVs7MJWKCwgf`, node `26:81`; URL original conservada en el [snapshot](../sources/figma-snapshots/button-26-81.snapshot.json).
- **Clase y rol:** nodo Figma observado mediante lectura propia; evidencia candidata para `BUTTON-001`, no aprobación ni especificación histórica.
- **Cobertura:** traversal completo read-only, 364 descubiertos/364 inspeccionados/0 pendientes; 60 variantes, 120 instancias, 60 textos, 35 variables y 0 estilos nombrados.
- **Snapshot JSON:** [button-26-81.snapshot.json](../sources/figma-snapshots/button-26-81.snapshot.json), SHA-256 bytes `1d58b485a6324a8bdd2618ba43f34efbfb50b609f1467b18579fe875067c5dca`.
- **Captura visual:** [button-26-81.png](../sources/figma-snapshots/button-26-81.png), 516×1883, SHA-256 bytes `8b4a7c85f3ec9138a0588f8b922b676696d81f8ffb503d2cef3bb04ba7a4bd04`.
- **Autoridad comprobada:** evidencia observacional. El usuario autorizó ejecutar el protocolo, pero no ha aprobado todavía el contrato candidato ni los hallazgos como requisitos.
- **Límite de rol:** el nodo ya reside en el archivo configurado como destino. Esta coincidencia no lo convierte automáticamente en fuente normativa ni autoriza modificarlo.

## SRC-FIGMA-PHOSPHOR-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador original:** [Phosphor Icons](https://www.figma.com/design/xZSksKpcQTp5H3C4dZApBL/Phosphor-Icons?node-id=7484-1322&t=5f3sI6AFFHMgcXfl-1), file key `xZSksKpcQTp5H3C4dZApBL`, página `7484:1322` (`Components`).
- **Procedencia y autoridad:** enlace entregado por el usuario junto con la decisión explícita de consumir todos los iconos desde ese archivo, registrada en [DEC-ICONS-001](decisions.md). El enlace por sí solo no aprueba el contrato Button.
- **Snapshot de verificación:** [phosphor-plus-circle.snapshot.json](../sources/figma-snapshots/phosphor-plus-circle.snapshot.json), SHA-256 bytes `c3529c0ecc28a2cb1cdb2af852b3b72bd7f5751639bf89c73e712037e9813e60`, 1270 bytes. Captura read-only a las `2026-09-23T00:38:37Z`.
- **Cobertura:** página identificada y 1512 component sets contados; se inspeccionó en profundidad solo el set `PlusCircle` (`8899:53875`, key `322a346f2ce54ea1534d8b0a682a8139d9f20e87`) y su variante `Format=Outline, Weight=Light` (`8899:53827`, key `46d251bb4099700c5852180f2370d265e5166432`). Ambas keys coinciden con la dependencia remota observada en Button (`26:2`/`26:3`). No se inventariaron todos los iconos ni se verificaron todas las familias.

## SRC-BTN-CONFIG-001

- **Estado de ingesta:** `INDEXED` (2026-09-23 UTC).
- **Original preservado:** [captura de configuración](../sources/screenshots/button-component-configuration.png), 35801 bytes, SHA-256 de bytes `d28ed34fb96435518e9cc7fcf3734b6f1efb8dd97ba301458f7ec30536db251c`; copia comprobada con `cmp`. El archivo temporal original no se eliminó.
- **Procedencia y rol:** imagen adjunta por el usuario. Muestra el campo Description con placeholder y el campo Link vacío; es evidencia de interfaz, no instrucciones ni aprobación del texto que se redacte.
- **Corroboración:** lectura read-only del component set `26:81` en `AI-Design-System` durante esta revisión: `description` cadena vacía y `documentationLinks` lista vacía. La captura no demuestra por sí sola la configuración interna; la lectura sí identifica el nodo.
- **Cobertura:** solo la configuración documental del set Button. No modifica ni revalida variantes, variables o interacciones.

## SRC-FIGMA-FILTER-CHIP-001

- **Estado de ingesta:** `CONFLICT` (2026-09-23) para los campos descritos abajo; la evidencia accesible quedó `INDEXED`.
- **Localizador original:** [Filter Chip](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=8203-10&t=sZOrF8YSnEjHSpdU-11), file key `9zs5RMR8LB5wHjW9Bd59BA`, nodo `8203:10`, página `7339:129` (`WIP Chips`). Es archivo fuente, no el destino `AI-Design-System`.
- **Clase y rol:** component set Figma observado mediante lectura propia; evidencia candidata para `FILTER-CHIP-001`, no aprobación ni especificación vigente.
- **Cobertura:** traversal read-only completo, 145 descubiertos/145 inspeccionados/0 pendientes; 24 variantes, 48 instancias `PlusCircle`, 24 textos, 48 vectores internos, 26 variables y 0 estilos nombrados.
- **Snapshot JSON:** [filter-chip-8203-10.snapshot.json](../sources/figma-snapshots/filter-chip-8203-10.snapshot.json), 5382 bytes, SHA-256 `013be40af5c346647a0b13bf4b3c4af7f27b5a54074aae8a348b18a297d1f189`.
- **Captura visual:** [filter-chip-8203-10.png](../sources/figma-snapshots/filter-chip-8203-10.png), 595×445, 35640 bytes, SHA-256 `b39aa2414e2e6677061b46130a878f694b7df362912b2dc2b04df984df8e5dd8`.
- **Dependencia activa:** set remoto `PlusCircle`, key `322a346f2ce54ea1534d8b0a682a8139d9f20e87`; variante `Format=Outline, Weight=Light`, key `46d251bb4099700c5852180f2370d265e5166432`. Las keys coinciden con `SRC-FIGMA-PHOSPHOR-001`; no se volvió a inventariar la biblioteca completa.
- **Conflictos:** `CONFLICT-FC-001` (defaults de iconos), `CONFLICT-FC-002` (vocabulario Size) y `CONFLICT-FC-003` (independencia Selected/State frente a 16 combinaciones ausentes). Véase [síntesis](../drafts/reports/filter-chip.synthesis.md).
- **Autoridad comprobada:** observacional. La autorización para inspeccionar y redactar no aprueba el candidato ni autoriza construcción.

## SRC-FIGMA-LEGACY-ROOT-001

- **Estado de ingesta:** `INDEXED` a nivel de páginas (2026-09-23); inspección profunda por familia pendiente.
- **Localizador original:** [Libreria v1.1.0](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=7339-129&t=sZOrF8YSnEjHSpdU-1), file key `9zs5RMR8LB5wHjW9Bd59BA`, nodo enlazado `7339:129` (`WIP Chips`). El alcance solicitado es el archivo anterior, no solo la página del enlace.
- **Clase y rol:** biblioteca Figma anterior; evidencia observacional para el inventario y contratos por familia. No reemplaza el JSON de variables aprobado ni el archivo destino `AI-Design-System`.
- **Cobertura actual:** listado de 28 páginas de componentes por Plugin API y metadatos XML de cada una; [inventario preliminar](../sources/figma-snapshots/legacy-library-pages.inventory.md), SHA-256 bytes `4cd76b296a6a5dd7e998b086e89d2905b08e405d28805f44599a4152db593a99`. Los 748 nodos `symbol` son un conteo de metadatos, no de contratos completos.
- **Límite:** fuentes y dependencias internas aún necesitan traversal y snapshot por componente. Los marcadores `✅`/`WIP` de Figma no son aprobaciones del proyecto.

## SRC-FIGMA-TOOLTIP-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Tooltip fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2599-10469), set `2599:10469`, página `2599:10321` del archivo anterior. Es fuente, no destino.
- **Cobertura:** traversal read-only 21 descubiertos/21 inspeccionados/0 pendientes, cuatro variantes Align, cero instancias internas, 12 variables fuente resueltas y cero estilos nombrados; [modelo YAML](../drafts/contracts/tooltip.contract.v0.1.0.yaml), SHA-256 bytes `0e091b8057c012d012668d01bdc152cf920faa85ae27265fb5a82df374918d2d`.
- **Visual:** captura 173×500 inspeccionada inline; la URL efímera no se conservó como archivo. No se usa la captura para demostrar bindings.
- **Autoridad:** evidencia observacional; la selección de tokens y página destino queda separada como decisión delegada en el contrato. Una frase de Modal ajena al set fue excluida.

## SRC-FIGMA-BADGE-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Badge fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1234-65377), set `1234:65377`, página `1234:53606` del archivo anterior; no es el destino.
- **Cobertura:** traversal read-only 37/37 nodos, incluidos seis vectores de iconos ocultos; seis variantes, doce instancias Presentation, 27 variables usadas, cero estilos nombrados y cero reacciones. [YAML de evidencia](../drafts/contracts/badge.contract.v0.1.0.yaml), SHA-256 bytes `b087af4f17a478f136e3bb50e3c4a5eaa3b9c789deb1325310c6a669f879087b`.
- **Dependencia:** Presentation Outline/Fill key `3f0d7ae9a02577d4fb4e615737d09fa1b49ec230`; set key `c2f4b3486a9480fe117be9260523dbb9500066e4` corroborada por búsqueda en Phosphor Icons. No se inventarió todo el catálogo.
- **Visual:** captura fuente 104×429 inspeccionada inline; URL efímera no conservada como archivo.
- **Autoridad:** evidencia observacional. Las correcciones semánticas de borde/iconos quedan en el contrato delegado para auditoría posterior.

## SRC-FIGMA-TOGGLE-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Toggle fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1230-23858), set `1230:23858`, página `1084:7229`; no es el destino.
- **Cobertura:** traversal read-only de 41/41 nodos, incluidas 16 etiquetas ocultas; ocho variantes On/Off × cuatro estados, cero instancias, 24 variables únicas, cero estilos nombrados y cero reacciones. [YAML de evidencia](../drafts/contracts/toggle.contract.v0.1.0.yaml), SHA-256 bytes `4010c12aaae2784df134268f776a25f7cad1c26d4a6a09f35a1a9cb28fb320f0`.
- **Visual:** captura 680×194 inspeccionada inline; URL efímera no conservada.
- **Anomalías:** `defualt` en el eje State; radio de Off/Focus ligado a `font/size/lg`; tokens disabled usados en Off/Focus. Se distinguen de las decisiones de normalización del contrato.
- **Autoridad:** evidencia observacional, no contrato ni aprobación.

## SRC-FIGMA-RADIO-BUTTON-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Radio Button fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1230-24283), set `1230:24283`, página `1144:34653`, key `92e794dad0b717afa2e923d7bf2db0b041e9f230`; no es el destino.
- **Cobertura:** traversal read-only 53/53 nodos; ocho variantes `radio=on/off × state=enabled/hover/focus/disabled`, 16 etiquetas ocultas, ocho instancias de indicador local, 12 variables únicas, un estilo de foco y cero reacciones. [MD de evidencia](../drafts/contracts/radio-button.source.component-contract.md), SHA-256 `739b6b023c26b50bfca00c51320403175e9be017ccb18371d5bd7f4051db912b`; [YAML](../drafts/contracts/radio-button.source.component-contract.yaml), SHA-256 `b6e66f541e7740cbea7d20512c5fca19a9d16b97175fa89a61deef02761cb3f4`.
- **Dependencia local:** indicador `radio` set `1144:34813`, key `9a7212da688ebc11ad48818760d8265d5ed0a019`; se observaron dos componentes principales y overrides por instancia. No se confunde con un componente externo.
- **Visual:** captura fuente 678×194 inspeccionada inline; URL efímera no conservada como archivo.
- **Autoridad:** evidencia observacional, separada de las mejoras delegadas del contrato destino.

## SRC-FIGMA-CHECKBOX-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Checkbox fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1221-28710), set `1221:28710`, página `1144:34368`, key `7cd9c016ecf140eef806b29fb23de1d00a718471`.
- **Cobertura:** 86/86 nodos read-only, doce variantes, 24 textos ocultos, nueve instancias, 19 variables usadas (14 locales, cinco remotas), un estilo nombrado, cero reacciones. [MD de evidencia](../drafts/contracts/checkbox.source.component-contract.md), SHA-256 `2bf391580a51709f1cb564c866ce1cec763870b962bdfd537a9261deb8c4207c`; [YAML](../drafts/contracts/checkbox.source.component-contract.yaml), SHA-256 `c71f16b4fcd3830966e3feb877f83cd50809483f102e6a2e3ccc3b24933b369b`.
- **Dependencias:** Check y Minus de Phosphor, más helper local `checkbox` usado solo en Unselected/Focus; estilo local `focus/outset`. Captura fuente 680×290 inspeccionada inline; URL efímera no conservada.
- **Anomalía de origen:** padding del set ligado a variables de scope GAP; ese uso de presentación no se replica en componentes destino.
- **Autoridad:** evidencia observacional, no contrato de producto ni aprobación del destino.

## SRC-FIGMA-DOT-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Dot fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1133-31549), set `1133:31549`, página `1133:20620`, key `bc7fd5437899a1868aeba789925329c30d5b6996`.
- **Cobertura:** traversal read-only de 22/22 nodos, matriz completa 5×3, seis textos, cero instancias, doce variables fuente, cero estilos y cero reacciones. [MD](../drafts/contracts/dot.source.component-contract.md), SHA-256 `e05bab6a993fe193fe2bc6e29d1b7c1df0adf0c985327fa5808613a5f252ec83`; [YAML](../drafts/contracts/dot.source.component-contract.yaml), SHA-256 `ad1d5d26b52621402aa27a5105e254d707421b94f7688277ebf77ac9bf87b146`.
- **Visual:** captura fuente 201×290 inspeccionada inline; URL efímera no conservada como archivo.
- **Anomalías de origen:** Description afirma que faltan Large de Busy/Inactive, aunque existen, y describe cambio automático a pill sin reacción observable. Los fills Active/Busy/Number usan roles de icono, incompatibles con la regla semántica estricta del destino.
- **Autoridad:** evidencia observacional; no define comportamiento de producto ni sustituye el JSON de variables de AI Design System.

## SRC-FIGMA-AVATAR-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Avatar fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1132-21344), set `1132:21344`, página `1132:8891`, key `2df4b15820fade1cc23c83fde049c755286bfdc4`.
- **Cobertura:** 49/49 nodos read-only, matriz Image/Icon/Text × cuatro tamaños, 16 instancias de dos dependencias activas, cuatro textos, 18 variables únicas, cero estilos y cero reacciones. [MD](../drafts/contracts/avatar.source.component-contract.md), SHA-256 `c2d5e37c157e112619090a6ce4ad27c58b1c52dddf85b706d29dd723d4fb8bf9`; [YAML](../drafts/contracts/avatar.source.component-contract.yaml), SHA-256 `581229e3dadb59f2808e7e20a091b5f08e070998ffa1f275ed988b32c48cbd96`.
- **Dependencias:** Dot local `1133:31549` en doce instancias y User Phosphor key `77a821b72c03fcfbd0ca9b2910c3fb5c98ed210f` en cuatro. Los 1512 preferredValues de icono son picker, no dependencias activas.
- **Asset y visual:** captura 324×312 inspeccionada inline; image hash fuente `33f6b019db4382817513e4485e94d3a7dd5a6ca2`. Exportación read-only del frame 48×48 `1132:21349` conservada como [PNG codificado](../sources/figma-snapshots/avatar-source-face-48.png.base64), SHA-256 binario `01e7a2b7781eb2b3c7f710295fa9b99339f13f2fafd612fa17afe0fcbe721c01`.
- **Riesgos:** cara no interactiva usa rol interactive; iniciales Small/Medium 6/9 px; Dot Small se redimensiona a 5 px; no hay comportamiento de identidad ni presencia definido. Evidencia observacional, no aprobación del destino.

## SRC-FIGMA-INLINE-NOTIFICATION-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Inline Notifications fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2778-10287), set `2778:10287`, página `1241:55464`, key `55b0bfd8fb39f8b1d16eee72f95a1b44481062ec`.
- **Cobertura:** 46/46 nodos read-only, cinco variantes 602×104, diez iconos Phosphor anidados, diez textos, 23 variables (18 locales, cinco remotas), cero estilos nombrados y cero reacciones. [MD](../drafts/contracts/inline-notification.source.component-contract.md), SHA-256 `1b70a8af80696ef6ef1ab49d109a352ab680dae0aa9d1217624d2aa90c9447d2`; [YAML](../drafts/contracts/inline-notification.source.component-contract.yaml), SHA-256 `75dc5a449c4292f4bb17344dd4bfe792c59aec663bee4f03695afdc876e550e3`.
- **Visual:** captura 650×990 inspeccionada inline; URL efímera no conservada.
- **Anomalías:** `Tittle` de ejemplo, Light/Close con rol de texto en vectores, tramo subrayado azul sin hyperlink y Close sin reacción. Evidencia observacional, no regla de producto.

## SRC-FIGMA-ICON-BUTTON-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Button Icon fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1430-18850), set `1430:18850`, página `1430:18021`, key `fbc267a15caab7547a5d782a8887da547ee7cf03`.
- **Cobertura:** 151/151 nodos read-only; 30 variantes, 60 instancias activas (Bell y Dot Count), 27 variables (21 locales/seis remotas), un estilo local y cero reacciones. [MD](../drafts/contracts/icon-button.source.component-contract.md), SHA-256 `728c5aef5d875765cac8e0cba06538384e2b5085320b210bbe7da511f88a7015`; [YAML](../drafts/contracts/icon-button.source.component-contract.yaml), SHA-256 `a1d197f0ed62ecb99196d08d79b9bdfe26c3f272c1cd277623e97cd3e01eca8d`.
- **Visual:** captura 289×960 inspeccionada inline; URL efímera no conservada.
- **Anomalías:** Dot usa rol iconográfico en fill de contenedor, `focus/outset` solo en una de seis variantes Focus, Small de 24 px y conteo de 4 px. Evidencia observacional, no regla de destino.

## SRC-FIGMA-BREADCRUMB-ITEM-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Breadcrumb item fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2425-35897), set `2425:35897`, página `1098:28190`, key `e96a86bbd1d613d821281d737f2cdc262791cbe6`.
- **Cobertura:** 22/22 nodos read-only, seis variantes, cinco instancias Phosphor, 16 variables (14 locales/dos remotas), cero estilos y reacciones. [MD](../drafts/contracts/breadcrumb-item.source.component-contract.md), SHA-256 `78f5121339023cc663992fa3e46a6382a648c112a4db4622315d1a545b5b19c1`; [YAML](../drafts/contracts/breadcrumb-item.source.component-contract.yaml), SHA-256 `27d86709f64f310eadc0b626786a1f4908cb5bed4559d070caca8c863b53fd26`.
- **Visual:** captura de la página fuente 1242×1106 inspeccionada inline; URL efímera no conservada. Cuatro combinaciones State×active teóricas no existen en el set.

## SRC-FIGMA-BREADCRUMBS-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Breadcrumbs fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2425-35937), set `2425:35937`, página `1098:28190`, key `6fb836fc24e1d24e6a0b0c933f97cfc32ff58680`.
- **Cobertura:** 65/65 nodos read-only, cuatro niveles, 28 instancias anidadas, 15 variables (11 locales/cuatro remotas), un estilo Inter remoto y cero reacciones. [MD](../drafts/contracts/breadcrumbs.source.component-contract.md), SHA-256 `89256b999daab4295a3b79bcd223d80f83b91db025ac4337291dafd5d1fc5c8e`; [YAML](../drafts/contracts/breadcrumbs.source.component-contract.yaml), SHA-256 `5c51cc7fc22050193a98de834adb0a1940a56104edddf14f41811af98c9aed48`.
- **Visual:** captura de la página fuente 1242×1106 inspeccionada inline; URL efímera no conservada. Las cuatro etiquetas activas de ejemplo usan Inter remoto aunque su definición base usa Manrope.

## SRC-FIGMA-METRIC-CARD-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Card/Metric fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=587-2751), set `587:2751`, página `258:130806`, key `9d7e8dc9398238b70936d1eeb37ef4651116a42d`.
- **Cobertura:** 119/119 nodos read-only, ocho variantes, 16 instancias remotas, 36 textos, 31 variables locales, cero estilos y cero reacciones. [MD](../drafts/contracts/metric-card.source.component-contract.md), SHA-256 `431b99b91122c781b39f0bdedc1c63e24ef3cb3c15f62684607203f5dcbc1cbb`; [YAML](../drafts/contracts/metric-card.source.component-contract.yaml), SHA-256 `b57528bf6bc80298d484e931c82f2675fb8d0fb0c255eeeb980749d5a288eb88`.
- **Visual:** captura del set 806×935 inspeccionada inline; URL efímera no conservada. Dependencias CurrencyCircleDollar y ArrowUpRight, ambas Phosphor remotas.
- **Anomalías:** One Metric V1 Small usa título de 18 px; la tendencia usa `color/text/brand`, cuya adecuación de contraste se debe comprobar por modo en el destino. Evidencia observacional, no regla de producto.

## SRC-FIGMA-CHART-LABEL-CELL-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [labelCell fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=3086-992), set `3086:992`, página `268:20756`, key `b5deacd96d67b6a46805de3d5abc20cc2717a4ea`.
- **Cobertura:** 17/17 nodos read-only, cuatro variantes, cuatro textos, cero instancias, cinco variables (cuatro locales/una remota), cero estilos/reacciones. [MD](../drafts/contracts/chart-label-cell.source.component-contract.md), SHA-256 `af7aa39f9885a799e4acc97a321640d21f5d37906a41054591e25848eda76aab`; [YAML](../drafts/contracts/chart-label-cell.source.component-contract.yaml), SHA-256 `2b583c9e1549720a77a99f3548d2e0a6581d2e5fbe843b5d416a6033ea4cd050`.
- **Anomalías:** swatch gris sin token, tamaño Large 16 px sin binding, spacing cero remoto. Es dependencia activa de Header y Progress chart item; fuente observacional, no norma de destino.

## SRC-FIGMA-CHART-CELL-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [cell fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2977-2066), set `2977:2066`, página `268:20756`, key `ddc93f484212024c51d2cdddc480ea242a4db18f`.
- **Cobertura:** 26/26 nodos read-only, 13 variantes, cero textos/instancias, ocho variables (seis locales/dos remotas), cero estilos/reacciones. [MD](../drafts/contracts/chart-cell.source.component-contract.md), SHA-256 `1fd4832f581d51b94316ccda46d9b55e8fa7f937a375831c9d20b4ad06eb5843`; [YAML](../drafts/contracts/chart-cell.source.component-contract.yaml), SHA-256 `30cfba0f619e0ade4dffa09d3c62c32f541e414a6c2a739c7ac423d0c56ab583`.
- **Anomalías:** 27 combinaciones teóricas ausentes; barra con rol genérico `color/brand/default`. Borde punteado y radios de segmento son evidencia visual, no significado de datos.

## SRC-FIGMA-CHART-PROGRESS-ITEM-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Progress chart item fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=3075-871), set `3075:871`, página `268:20756`, key `e0f0518afea25fa255f066c83708099842d1ccc7`.
- **Cobertura:** 40/40 nodos read-only, dos variantes, seis instancias locales `labelCell`, diez textos, 17 variables (16 locales/una remota), cero estilos/reacciones. [MD](../drafts/contracts/chart-progress-item.source.component-contract.md), SHA-256 `cf65a19048f2a4bb8cca26b18ef4d9c481ecdf5a8c665af318692f85252d335f`; [YAML](../drafts/contracts/chart-progress-item.source.component-contract.yaml), SHA-256 `4756bc0772bcf305d382cc9a06e55376d301bf6c740a0c2d3df510c0b28eb346`.
- **Anomalías:** Progress rectangle con `color/icon/brand`, cuatro paints de Dot ocultos y ancho de barras que no concuerda con ejemplo `80%`. Evidencia observacional, no norma de datos.

## SRC-FIGMA-CHART-DONUT-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Donut fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=3086-1090), set `3086:1090`, página `268:20756`, key `c23b7c56a0b6d559794bff1d8892069320f13328`.
- **Cobertura:** 13/13 nodos read-only, tres variantes, seis vectores, tres textos, seis variables locales, cero instancias/estilos/reacciones. [MD](../drafts/contracts/chart-donut.source.component-contract.md), SHA-256 `302f1f6e17f4f8bd0985486066da16a4b224ae16f5617d173289d8d30dc22e4a`; [YAML](../drafts/contracts/chart-donut.source.component-contract.yaml), SHA-256 `4f451c4bef6c2e97b6cacd0adab104d7ee7b8fa94ca50ecb97bb22b839313a97`.
- **Geometría:** [seis paths vectoriales](../sources/figma-snapshots/chart-donut.vector-paths.json), SHA-256 `60e22a15421f6be666e175bc64905074562f00453abb2032c3203c587c5ad764`, leídos de Figma fuente sin rasterizar. Captura 323×510 inspeccionada.
- **Anomalías:** semicírculo llamado Donut y roles interactive/icon aplicados a datos; evidencia observacional, no norma de destino.

## SRC-FIGMA-CHART-HEADER-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Header de Charts fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=3075-764), componente suelto `3075:764`, página `268:20756`, key `e322384d309997e64a5446a93ad07fd3560f7cf4`.
- **Cobertura:** 17/17 nodos read-only, tres instancias locales `labelCell`, cinco textos, doce variables (once locales/una remota), cero estilos/reacciones. [MD](../drafts/contracts/chart-header.source.component-contract.md), SHA-256 `29ba17d5b763ce6ee011ddd915186f73acb137b507694965f1432ddc7749cff4`; [YAML](../drafts/contracts/chart-header.source.component-contract.yaml), SHA-256 `480ffeccca334481d61518a421709abebba4d33d0cf958a9eac10734e1274d91`.
- **Anomalías:** errata de propiedad `Ttile`; swatches usan roles brand/interactive; textos de Value 1/2/3 no son props de Header. Evidencia observacional, no norma de destino.

## SRC-FIGMA-LINEAR-PROGRESS-BAR-001

- **Estado de ingesta:** `INDEXED` (2026-09-23).
- **Localizador:** [Linear Progress Bar fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=7596-48397), set `7596:48397`, página `7568:47417`, key `c65677f139942b3cc11a8a8e8b3754029d044d57`.
- **Cobertura:** 336/336 nodos read-only, 48 variantes (4 tonos × 3 tamaños × 4 porcentajes), 144 textos, doce variables locales, cero instancias/estilos/reacciones. [MD](../drafts/contracts/linear-progress-bar.source.component-contract.md), SHA-256 `d14be5a10bf63a89554ef9891711686b629bdc1b4928cff7cbd5eae7e655ed5d`; [YAML](../drafts/contracts/linear-progress-bar.source.component-contract.yaml), SHA-256 `58f61d6ed10c85ba343fb75f8adbba086ca1d7e5f5834d7fab9d161f9ac6e295`.
- **Snapshot de variantes:** [JSON read-only](../sources/figma-snapshots/linear-progress-bar.variants.json), SHA-256 `f191d85d9db708985ae5abe44c4b77a38404fb241018a6dab00593becbe285a1`; orden de 48 IDs fuente usado para el mapa uno a uno de destino.
- **Anomalías:** track literal sin variable; roles iconográficos sobre fondos; 36 variantes 50/75/100% conservan texto visible 25% aunque la barra sí cambia. Captura 1034×1402 inspeccionada; evidencia observacional, no norma de datos.

## SRC-FIGMA-HEADER-001 · descubrimiento inicial de Header

- **Localizador:** [componente Header fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1349-4907), componente `1349:4907`, página `268:20243`, key `5a29f5f658d3b85560303a84f025a92bee503f30`.
- **Cobertura:** lectura de identidad, propiedades y recorrido de 110 nodos, incluidos seis ocultos; 25 instancias activas/ocultas y 35 variables usadas. [Reporte de descubrimiento](../drafts/reports/header.discovery.v0.1.0.md), SHA-256 `9fa896fe5c11fedf5df39e094c88c5df7ce74ff300aa06b860b2c383ed685a81`.
- **Pendiente:** contratos MD/YAML profundos del helper `icon header` y Logo Categoria, resolución local de dependencias y mapa token/consumidor por modo. Este registro es evidencia parcial; todavía no existe contrato de destino `Header` listo para Figma.

## SRC-FIGMA-LOGO-CATEGORIA-001 · dependencia de Header

- **Localizador:** set `Logo Categoria` `8321:504` accesible como dependencia del Header de la Librería anterior, key `f1a7cf5b92134fa211a64c2ea547a35fb4b7111c`; el Header usa la instancia `2873:23060` de la variante contable. La lectura API no aportó página propietaria del set; no se atribuye una ubicación no comprobada.
- **Cobertura:** cuatro categorías y 210 nodos internos inventariados, con productos anidados, 131 vectores, 37 gradientes y cuatro fills de imagen. [Reporte de descubrimiento](../drafts/reports/logo-categoria.discovery.v0.1.0.md), SHA-256 `facb45a9307fe7a321fc552001ad8a780b23bc4af013a615aab6b6e7d0ba0971`.
- **Pendiente:** contrato fuente MD/YAML completo y método de preservación como componente local. Los colores literales de marca no tienen primitiva RGB idéntica en el JSON aprobado; [AUD-005](../specs/MIGRATION-AUDIT.md) registra el criterio pendiente. No hay construcción de Logo ni Header.

## SRC-FIGMA-NAVIGATION-001 · subfamilias Switch Tab

- **Estado de ingesta:** `INDEXED` (2026-09-24), lectura acotada a `Switch Tab Item` y su composición `Switch Tab`, no a toda la página.
- **Localizador:** [set fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2461-651), página `268:20245`, set `2461:651`, key `44cd079b3bb28629bd1fdcb794dcffc89ee81a2a`.
- **Cobertura:** 25/25 nodos, tres variantes, nueve instancias, 21 variables usadas y cero reacciones. [MD](../drafts/contracts/navigation-switch-tab-item.source.component-contract.md), SHA-256 `5114d57d5a031ef1b2e4b94b241989869629bde971aed7f95e14d608f6621510`; [YAML](../drafts/contracts/navigation-switch-tab-item.source.component-contract.yaml), SHA-256 `fce176b178a9e7702c8ffdfd62341775ecc6f8d8055e67560614daa224fc938f`.
- **Dependencias:** AddressBook Outline/Light remoto por key y Dot Count local por key; la biblioteca remota completa no está expuesta, pero la variante activa se importó y verificó en destino.
- **Composición fuente adicional:** [Switch Tab](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2461-1740), componente `2461:1740`, key `a9b5398f81f4ca60c7f3eed597a90ffefc2029ad`. Recorrido completo de 33 nodos, cuatro instancias directas de Tab item, 16 instancias en total y veinte variables. [MD](../drafts/contracts/navigation-switch-tab.source.component-contract.md), SHA-256 `9085b11b12b899d76321ed114782ddef946dcaf1f49138800c5a23f09c3666fa`; [YAML](../drafts/contracts/navigation-switch-tab.source.component-contract.yaml), SHA-256 `cce11d972640b709c930ddc3b10efe375972988527cc08e4d2bd7cfe306ab5d9`.
- **Cobertura de esta página:** `Switch Tab Item`, `Switch Tab`, `Pagination` y `Tab` tienen evidencia y construcción separadas; no se atribuye migración a otras piezas no inventariadas.

## SRC-FIGMA-NAVIGATION-PAGINATION-001

- **Estado de ingesta:** `INDEXED` (2026-09-24), lectura completa del set `Pagination`, sin atribuir cobertura a `Tab`.
- **Localizador:** [set fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2461-714), página `268:20245`, set `2461:714`, key `0d6540ee619c7896a844d6607854415727b43345`.
- **Cobertura:** 146/146 nodos, cinco variantes, 25 instancias Caret, diez frames ocultos, 31 variables y cero reacciones. [MD](../drafts/contracts/navigation-pagination.source.component-contract.md), SHA-256 `1f64b837e271cc9ffb1c8b5503bfc7e76451d02077bc15acfb6ab6ea029b0e9d`; [YAML](../drafts/contracts/navigation-pagination.source.component-contract.yaml), SHA-256 `ca6a57f32f520b6f040e37d5bab81ac164b0b867bb424e47647ffc8b8608c6c0`.
- **Dependencias:** CaretLeft y CaretRight importables por sus keys fuente; CaretDoubleLeft, CaretDoubleRight y CaretDown son locales al archivo antiguo, por lo que el destino usa variantes publicadas Phosphor de la misma silueta y peso. La sustitución de keys queda explícita en el estado de implementación.

## SRC-FIGMA-NAVIGATION-TAB-001

- **Estado de ingesta:** `INDEXED` (2026-09-24), lectura completa del set `tab` sin completar ejes teóricos.
- **Localizador:** [set fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1183-1146), página `268:20245`, set `1183:1146`, key `3fbabad3e0521532b6055ea2e5de2f74de4b2693`.
- **Cobertura:** 132 nodos, 17 variantes, 33 instancias ImageSquare, 16 Dot ocultos y cuatro reacciones hover. [MD](../drafts/contracts/navigation-tab.source.component-contract.md), SHA-256 `46b99bb3201dfb1fd089c4586f7dfe27c8ed7fa7ea1e38b7dc3f4db6ef0724d8`; [YAML](../drafts/contracts/navigation-tab.source.component-contract.yaml), SHA-256 `13e6ac5e13306ab5ab295ff117680dd787e3211e5e3949617427f51b6c960776`. [QA fuente](../qa/contracts/navigation-tab.source.component-contract.review.md) `PASS` de inventario.
- **Anomalías:** `Dynamic/On/Selected` es la decimoséptima variante con anatomía distinta; cinco usos de roles cromáticos incorrectos y un efecto Focus sin token fuente. El destino los resuelve sin inventar variantes.

## SRC-FIGMA-SCROLLBAR-001

- **Estado de ingesta:** `INDEXED` (2026-09-24), lectura profunda de solo lectura de la página `3910:928` de la Librería anterior.
- **Localizador:** [set público fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=7664-49488), key `d3d06e195e2bdb6fc5d2bc9e10f33a8edb2f357c`; sets internos `7706:49949`, `7706:50034`, `7706:50119` y `7706:50204`.
- **Cobertura:** cinco sets, 30 variantes, 125 nodos y 30 thumbs con fill literal `#C3C6D4` sin token, cero reacciones. [MD](../drafts/contracts/scrollbar.source.component-contract.md), SHA-256 `923983a5722eae8e5eb94b0d76e19081d59a56a554f64a8282850456f8415679`; [YAML](../drafts/contracts/scrollbar.source.component-contract.yaml), SHA-256 `4f41c96a75bd2ceed19f46da83c75a7caa990288589e91c38f49a7051d4e1f19`; [QA fuente](../qa/contracts/scrollbar.source.component-contract.review.md) `PASS`.
- **Anomalías:** el tamaño llamado `75%` dibuja ~88% del recorrido; los sets internos miden 280 px, el recorrido público 272 px, y la orientación horizontal usa rotación interna. Se conserva la fuente y se declara cada transformación de destino.

## Guías externas para la revisión candidata BUTTON-001 0.2.0

Estas fuentes se consultaron el 2026-09-23 UTC. Son referencias de buenas prácticas, no contratos aprobados del sistema. Sus nombres de variantes, valores y reglas particulares no se importan automáticamente.

| ID | URL oficial | Cobertura usada | Autoridad en este proyecto |
|---|---|---|---|
| SRC-GUIDE-MATERIAL-001 | [Material Web · Buttons](https://material-web.dev/components/button/) | Jerarquía de tipos; etiqueta que describe acción; icono opcional al inicio o final. | Referencia externa, no define los tipos locales. |
| SRC-GUIDE-CARBON-001 | [Carbon · Button usage](https://carbondesignsystem.com/components/button/usage/) | Acción frente a navegación, prioridad, tamaños por contexto, consistencia de grupo y moderación de iconos. Carbon coloca el icono al final en su sistema; la regla local izquierda/derecha se propone aparte. | Referencia externa; no se adopta literalmente. |
| SRC-GUIDE-APPLE-001 | [Apple HIG · Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) | Propósito claro, jerarquía, símbolos familiares y espacio de activación. | Referencia externa, no certifica accesibilidad del Figma. |
| SRC-GUIDE-TAILWIND-001 | [Tailwind CSS · Hover, focus, and other states](https://tailwindcss.com/docs/hover-focus-and-other-states) | Selectores hover, active, focus-visible y disabled. | Referencia técnica de estilo, no gobierna jerarquía ni semántica. |

## SRC-FIGMA-STEPS-001

- **Estado de ingesta:** `INDEXED` (2026-09-24), lectura profunda de la página `❖ Steps` de la Librería anterior.
- **Localizador:** [set público fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=8029-8267), página `7861:714`, sección `8029:8263`; sets internos `.Dot` `8029:8294` y `.Combination` `8029:8320`.
- **Cobertura:** tres sets principales, 37 variantes (6+4+27), tamaños, siete colores relevantes, dependencias de Button y Combination externos, y una reacción hover sin destino. [MD](../drafts/contracts/steps.source.component-contract.md), SHA-256 `7aef8f2392868bfafdd4629f429963d7a5e2d3fce6f8a4e413a02b16b5702d07`; [YAML](../drafts/contracts/steps.source.component-contract.yaml), SHA-256 `a30cbe261720dd35f6806ec4d3c2d9a702b867b7b365cc424f462078839405ff`.
- **Anomalía:** `On Primary / Gallery`, `On Primary / Gallery only` y `.Dot Primary=false` presentan tres paletas incompatibles. Conservadas como evidencia separada, no fusionadas por inferencia.

## SRC-FIGMA-STEPPER-001

- **Estado de ingesta:** `INDEXED` (2026-09-24), lectura profunda de la página `❖ Multi Step Indicator (Wizard)  ✅` de la Librería anterior.
- **Localizador:** [set público fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2166-1499), página `2166:596`, set `container` `2166:1499` y set `Progress line` `2473:1781`.
- **Cobertura:** 18 variantes públicas + ocho conectores; tamaños, icono, textos, propiedades, colores y radios observados; cero reacciones. [MD](../drafts/contracts/stepper.source.component-contract.md), SHA-256 `54b7b1a91c8a0ed4a423ed2d454e74b3e0b02ac3518f77d43415f0eaa4efd153`; [YAML](../drafts/contracts/stepper.source.component-contract.yaml), SHA-256 `d38f8a02ef9eb19f4948d297b63c1244c48ee1aad79dcac2ffc790c84450de04`.
- **Límite:** la navegación y el significado funcional de `Default` no están definidos; la línea blanca oculta de Horizontal/End no se traslada como elemento visible.
## SRC-FIGMA-LOADER-001

- **Estado de ingesta:** INDEXED (2026-09-25), lectura profunda de solo lectura de la página Loader de la Librería anterior.
- **Localizador:** [set público fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=7561-47164), página 3917:1263, set 7561:47164, key b7b6e1e6560ca57d1a8b9f431551d63fe65116eb. Sets internos 4283:240, 7556:45810, 7556:46291 y 7556:46652.
- **Cobertura:** 16 variantes públicas, 96 fotogramas internos, 96 reacciones, 581 nodos leídos, cuatro colores y tamaños. [MD](../drafts/contracts/loader.source.component-contract.md), SHA-256 c9435904cf805b2b51759c96a6a4f7778a6c5fccb997118c21120052dfeef3be; [YAML](../drafts/contracts/loader.source.component-contract.yaml), SHA-256 f9ec5a35627c9f537dacb85f1eb7c3de9bd736e3a7be9ef7b5e8b4516f77a67d.
- **Anomalía:** los tres colores no Primary solo sobrescriben el primer fotograma; el destino corrige la persistencia mediante ciclos completos por color. Sin datos de accesibilidad web ni reduced motion.

## SRC-FIGMA-SEARCH-001

- **Estado:** INDEXED, 2026-09-28; fuente de solo lectura 9zs5RMR8LB5wHjW9Bd59BA, página20:3, set1560:44694, key15aed9418fc72b46b83fe1ac0fae3dac4bd85dfa.
- **Cobertura:** 12 variantes; 99 descendientes incluidos ocultos. [Snapshot](../sources/figma-snapshots/search.deep.json), SHA-256 65181e87c3b7f49f02e9f4b8d029b4725338bc07332fee4b6b392a8674956d34. [MD](../drafts/contracts/search.source.component-contract.md) y [YAML](../drafts/contracts/search.source.component-contract.yaml).
- **Límite:** comportamiento de producto UNDEFINED y procedencia remota parcialmente expuesta; no bloquean la reconstrucción visual documentada.

## SRC-FIGMA-TEXTAREA-001

- **Estado:** INDEXED, 2026-09-28; fuente de solo lectura 9zs5RMR8LB5wHjW9Bd59BA, página20:3, set2049:37125, keyef06351d877b285ffd00aa4af5279cd5e7339c3a.
- **Cobertura:** 4 variantes; 40 descendientes incluidos ocultos. [Snapshot](../sources/figma-snapshots/textarea.deep.json), SHA-256 3e28afb962ab4865065aa3279b6005c1f541b8e529394b248b16fd42a81afb59. [MD](../drafts/contracts/textarea.source.component-contract.md) y [YAML](../drafts/contracts/textarea.source.component-contract.yaml).
- **Límite:** comportamiento de producto UNDEFINED y procedencia remota parcialmente expuesta; no bloquean la reconstrucción visual documentada.

## SRC-FIGMA-FILE-UPLOAD-001

- **Estado:** INDEXED, 2026-09-28; fuente de solo lectura 9zs5RMR8LB5wHjW9Bd59BA, página20:3, set2459:38944, key55fb5f5009a682e55c7f758648d1452652047721.
- **Cobertura:** 6 variantes; 96 descendientes incluidos ocultos. [Snapshot](../sources/figma-snapshots/file-upload.deep.json), SHA-256 8d5d6d232d25fc9872006fea3bd1a11acd6a7eb9e2eedbe0ddcd001b9f4d2f48. [MD](../drafts/contracts/file-upload.source.component-contract.md) y [YAML](../drafts/contracts/file-upload.source.component-contract.yaml).
- **Límite:** comportamiento de producto UNDEFINED y procedencia remota parcialmente expuesta; no bloquean la reconstrucción visual documentada.

## SRC-FIGMA-INPUT-FIELD-001

- **Estado:** INDEXED, 2026-09-28. Página fuente 20:3; set Input Field 186:14461 de Librería anterior 9zs5RMR8LB5wHjW9Bd59BA. Inspección de solo lectura.
- **Cobertura:** 30 variantes, 493 nodos incluidos 60 ocultos, 60 instancias de Eye/Question, 36 variables referenciadas (29 locales y 7 remotas); cero reacciones. Search/Textarea/File Upload solo inventariados en [snapshot de página](../sources/figma-snapshots/input-fields.inventory.json), no cerrados.
- **Artefactos:** [MD fuente](../drafts/contracts/input-field.source.component-contract.md), SHA-256 8c963e6cbf9214d13fb063f11cd39fdbc1fcbf151c05ec24f001aad0d9726fee; [YAML](../drafts/contracts/input-field.source.component-contract.yaml), SHA-256 89bd723d3e84fdc44a6f840b0e899ee6efdb1c3c4bc1709cb3dc7b6c6d57b5bd. Snapshots adicionales input-field.base/variants/dependencies/focus.json conservan evidencia.
- **Límites:** procedencia de estilos/variables remotos parcialmente observada, comportamiento de formulario no definido. No se deduce aprobación del inventario.

## SRC-FIGMA-ANTICIPA-LAYOUT-OBSERVATION-001

- **Estado:** `INDEXED`, 2026-10-06. Inspección Figma de solo lectura, previa a la creación de contratos, solicitada por el usuario. Autoridad: `OBSERVED_NON_NORMATIVE`.
- **Fuente:** [Anticipa Junio2026 — Beni Chat / Papeles de trabajo](https://www.figma.com/design/zuUq3gcF9T3CLid44bjY6W/Anticipa-Junio2026?node-id=19871-20287), file key `zuUq3gcF9T3CLid44bjY6W`, página `19871:20287`.
- **Evidencia derivada:** [snapshot de observación](../sources/figma-snapshots/anticipa-layouts.observation.2026-10-06.json), 638533 bytes; SHA-256 de bytes `c12e7ad37d8bb43ebc339b5fe844a9e94deb1e8970aad495600bcb88edab323d`. No es exportación íntegra del archivo Figma ni contrato.
- **Cobertura:** inventario de 61 páginas (43 no separadoras); 34 estados de la página enlazada y 199 frames/instancias adicionales recorridos en texto/estructura/reacciones; 19 capturas representativas inspeccionadas en el conector; dos páginas de diagramas leídas; anatomía focal de drawers, modales y shell; cuatro colecciones locales inventariadas. Los límites de extracción, deduplicación y muestreo se registran en `coverage` del snapshot.
- **Hallazgos:** patrones distintos de dashboard, tabla, lista-detalle, chat, panel integrado, drawer y modal; Slots nativos en drawer; cierre exterior contextual. Diferencias entre captura mensual embebida y lateral; nombres ZIP frente a salida XLS/PDF; validaciones, scroll y conexiones del prototipo parcialmente definidos. Las propuestas no se eligen por fecha o nombre.
- **Exclusiones:** Playground, Graveyard y MVP 2 no aprobado solo inventariados; sin validación de aplicación ejecutable, sin auditoría exhaustiva de tokens, sin cambios en Figma/AI Design System, sin contratos ni aprobación simulada. Los contenidos fiscales son ejemplos de la fuente, no validación legal o contable.
- **Continuidad:** usar esta evidencia para discutir el resumen antes de P03. No adoptar automáticamente variables internas del origen. Grafo `STALE_FOR_THIS_NEW_EVIDENCE`, no regenerado en esta tarea.

## SRC-FIGMA-CHAT-TOOLBAR-001 · 2026-10-08

Anticipa zuUq3gcF9T3CLid44bjY6W, Toolbar20355:72872 y dependencias Options and Tools20355:72830/ChatHistory20355:72852. Usuario solicitó organismo y dependencias del mismo archivo. Read-only,211 nodos conjuntos; fuente PARTIAL respecto de aliases históricos/remotos. [Toolbar MD/YAML](../drafts/contracts/chat-toolbar.source.component-contract.md), [Tool Item](../drafts/contracts/chat-tool-item.source.component-contract.md), [History Item](../drafts/contracts/chat-history-item.source.component-contract.md), [snapshot](../sources/figma-snapshots/chat-toolbar.deep.2026-10-08.json).

## SRC-FIGMA-FUENTES-001 · 2026-10-09

[Fuente Navi64:4164](https://www.figma.com/design/8qsdk3nalNNyCzBfUTrOcP?node-id=64-4164), set Fuentes, lectura25nodos/2variantes, una dependencia Dot key210ae593aa5c0007983efdf243cf30644fd86825. [Snapshot](../sources/figma-snapshots/fuentes.source.v0.1.0.json), [variables](../sources/figma-snapshots/fuentes.source.variables.v0.1.0.json), [dependencia](../sources/figma-snapshots/fuentes.source.dependency.v0.1.0.json), [extracción MD](../drafts/contracts/fuentes.source.component-contract.md). Fuente inmutable; origen PARTIAL por cadenas de variables externas no resueltas por completo. Mapeo destino al JSON aprobado verificado independientemente. [Extensión canónica del rol Hover](../sources/inventories/ai-design-system.fuentes-hover.v0.1.0.json), sin alterar inventario base.


## SRC-CONVERSATION-COMPOSER-SLOT-013 · 2026-10-20

Solicitud posterior y confirmación explícita: Slot para todo el aviso, texto y acciones. [Preflight leído](../implementations/figma/conversation-composer.v0.1.3.preflight.json), principal765:397 en tj3WIBEZDGLVs7MJWKCwgf; [tipos y cotejo](../qa/contracts/conversation-composer.v0.1.3.preflight.json). Conserva fuentes y QA0.1.2 como históricos; no altera su significado.
