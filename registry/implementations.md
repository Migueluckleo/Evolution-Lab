# Registro de implementaciones

## IMP-CONVERSATION-COMPOSER-012 · 2026-10-20

[Enmienda0.1.2](../specs/components/conversation.composer-action.amendment.v0.1.2.md): Figma y web local `VALIDATED` exclusivamente para aviso opcional y correcciones. Destino AI-Design-System, página Conversation765:6, principal765:397; cuatro nodos actualizados1087:497/383/372/365, cero variables/componentes nuevos, Slots765:400/413 preservados. Instancia existente766:246 verificada. [QA y límites](../qa/implementations/conversation-composer.v0.1.2.review.md), [estado](../implementations/figma/conversation-composer.v0.1.2.state.json). Web incluye API, documentación generada y ejemplo local;9 tests/build y prueba Chrome dedicada PASS. Revisión humana OPTIONAL_NON_BLOCKING/NOT_REQUIRED; sin publicación remota.

## IMP-TYPOGRAPHY-CONSUMERS-012 · 2026-10-15

**PASS para consumo tipográfico verificado**: 34 páginas, 3351 nodos UI y 3353 rangos, desglosados en3250 vínculos directos y103 herencias nativas comprobadas; cero rangos sin resolución. [Reporte vigente](../qa/implementations/typography.v0.1.2.review.md), [catálogo79 0.1.2](../specs/tokens/ai-design-system.typography.v0.1.2.json) y [enmienda de herencia](../specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md).43Specs de consumo,150editoriales preservados, tres pilotos causales completos y todas sus copias retiradas. IDs locales vacíos103 conservados como observación, sin inventar vínculos. Auditoría humana `PENDING`; biblioteca no publicada. El guard completo no textual de Table perdido por timeout sigue sin evidencia; este PASS no lo sustituye. Skills y Graphify tienen cierres separados; consultar [skills.md](skills.md) y `graphify-out/ds-closure.json`.

La entrada0.1.1 inferior conserva el corte histórico previo al bloqueo, resuelto por esta continuación.

## IMP-TYPOGRAPHY-CONSUMERS-011 · 2026-10-15

Corrección solicitada de consumo tipográfico en todos los componentes: [enmienda transversal y 43 Specs por familia](../specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md), [catálogo activo 0.1.1 de 79 estilos](../specs/tokens/ai-design-system.typography.v0.1.1.json) y [reporte vigente de implementación](../qa/implementations/typography.v0.1.1.review.md). Estado `PARTIAL / BLOCKED_BY_USAGE_LIMIT`: censo completo de 34 páginas; 3250 rangos UI con vínculo directo correcto y 150 editoriales preservados. La herencia de 103 rangos escalados sigue en comprobación y dos copias temporales de Count pendientes de retirada. [Continuación exacta](SESSION-HANDOFF-2026-10-15-TYPOGRAPHY-CONSUMERS.md). Skills publicadas 0.2.0; Graphify STALE. Auditoría humana `PENDING`. Los estados y fallos del corte 0.1.0 inferior son históricos; no se reescriben como evidencia del nuevo corte.

## IMP-TYPOGRAPHY-001 · 2026-10-15

[Contrato 0.1.0](../specs/foundations/typography.contract.v0.1.0.md) `DELEGATED_FOR_BUILD`, [catálogo canónico](../specs/tokens/ai-design-system.typography.v0.1.0.json) de 75 estilos (18 base y 57 complementarios) y [decisión específica](DEC-TYPOGRAPHY-STYLES-001.md). Auditoría humana `PENDING`; resultado global `PARTIAL / BLOCKED`, detallado en el [QA de implementación](../qa/implementations/typography.v0.1.0.review.md).

| Destino / alcance | Estado y evidencia |
|---|---|
| Specs y catálogo | [QA documental PASS](../qa/contracts/typography.v0.1.0.md); reglas en Markdown y valores/única description en JSON. |
| Figma: estilos compartidos | [PASS independiente](../implementations/figma/typography.v0.1.0.styles.qa.json): 75 estilos, 304 bindings semánticos y 1216 resoluciones en cuatro modos. [Mapa actual de IDs](../implementations/figma/typography.v0.1.0.catalog.state.json). |
| Figma: documentación | AI-Design-System `tj3WIBEZDGLVs7MJWKCwgf`, página Typography `1003:412`: [readback PASS](../qa/implementations/typography/specimens.readback.json), 75 tarjetas, 316 textos y 79 frames. |
| Figma: preservación | [PASS acotado](../implementations/figma/typography.v0.1.0.preservation.qa.json): 34 páginas, 3501 nodos y 3503 rangos con métricas, contenido, propiedades capturadas, cajas e IDs originales preservados. Excepción explícita de 244 rangos con adiciones canónicas de bindings a 17 estilos reutilizados; sin pérdidas, reemplazos ni referencias ajenas. El [FAIL histórico de restauración literal](../implementations/figma/typography.v0.1.0.restoration.qa.json) se conserva. |
| Figma: consumidores existentes | [BLOCKED](../qa/implementations/typography/Figma-blocker.md): propagación observada de estilos entre textos con referencias a propiedades. No se declara consumo global VALIDATED; el mapa es preparación y los IDs originales se conservan. |
| Web local | [PASS en alcance medido](../qa/implementations/typography/web/revision-75/README.md): 75 estilos × cuatro temas, 2956 mediciones de texto de 43 familias por cuatro temas, generador, TypeScript y build. IMPLEMENTED_FOR_LOCAL_PROTOTYPING; no valida Figma ni igualdad visual universal. |

No se publicó la biblioteca remota ni se modifica retrospectivamente el QA histórico de las familias. El cierre de skills se registra en [skills.md](skills.md), conforme a P08; la vigencia de Graphify requiere su propia evidencia de cierre del lote.

## IMP-WEB-CONTRACT-AUDIT-013 · 2026-10-13

Cotejo contractual de43 familias del destino web: [QA0.1.3](../qa/implementations/web.contract-audit.v0.1.3.review.md), [matriz por familia](../qa/implementations/web-contract-audit-2026-10-13/family-matrix.md), [resultados/hashes](../qa/implementations/web-contract-audit-2026-10-13/results.json). Código/API/defaults/estilos y43 fichas sincronizados; estados en4 temas,725 fixtures,59 pruebas Chrome y9 de código. Corrige controles, navegación, auxiliares, Table, Modal, Charts y Chat con trazabilidad a fuentes. Estado IMPLEMENTED_FOR_LOCAL_PROTOTYPING; PASS solo en alcance medido. Modal Media/SideBySide incorporan los dos raster originales después de la autorización explícita del usuario; bloqueo inicial resuelto y hashes cotejados. No igualdad universal por píxel ni aprobación humana simulada. Esta revisión sustituye el cotejo web0.1.2, sin reescribir sus reportes históricos. Graphify requiere cierre del lote2026-10-13-web-contract-audit.

## IMP-WEB-FIDELITY-012 · 2026-10-13

Biblioteca web local corregida contra43 contratos y enmiendas, con442 casos de referencia. [QA0.1.2](../qa/implementations/web.fidelity.v0.1.2.review.md), [matriz](../qa/implementations/web-fidelity-2026-10-13/family-matrix.md), [resultados](../qa/implementations/web-fidelity-2026-10-13/results.json). Sidebar/MenuItem/TopBar, controles, Metric Card, Table, Modal, Charts y composiciones rectificados. Props/defaults, exports, ejemplos y43 fichas sincronizados. Scrollbar visual separado de ScrollArea nativo; ConversationGlyph original32px; Logos72/72. BENI conserva coordenadas de la corrección0.1.1.

Estado IMPLEMENTED_FOR_LOCAL_PROTOTYPING; PASS solo para QA registrado:8 pruebas de código,15 Chrome, TypeScript/build,88 mediciones de recetas Sidebar en4 temas y medidas acotadas de otras familias. No igualdad global por píxel, publicación ni validación Figma nueva. [Adaptación vigente](../implementations/web/docs/WEB-ADAPTATION.md). Estados históricos0.1.0/0.1.1 permanecen como evidencia de sus cortes.

## IMP-WEB-CHARACTERS-011 · 2026-10-13

Corrección del defecto reportado por el usuario en BENI del catálogo. El generador SVG ahora calcula coordenadas locales desde matrices absolutas del snapshot original y evita duplicar traslaciones de los ojos. 13 frames BENI/NAVI y consumidores web corregidos; API, colores y contratos visuales intactos. [QA y evidencia](../qa/implementations/web.characters.v0.1.1.review.md), resultado PASS acotado. El estado web0.1.0 inferior conserva su alcance histórico y queda sustituido solo para la geometría Characters por esta revisión. Sin cambios Figma ni backend.

## IMP-WEB-COMPONENTS-001 · 2026-10-13

Destino local [implementations/web](../implementations/web/README.md), API 0.1.0, **IMPLEMENTED_FOR_LOCAL_PROTOTYPING**. 43 familias con export React, props TypeScript, estilos/tokens, ficha y ejemplo ejecutable; una pantalla compuesta con datos locales. [Índice](../implementations/web/docs/components/README.md), [adaptaciones](../implementations/web/docs/WEB-ADAPTATION.md), [QA por alcance](../qa/implementations/web.v0.1.0.review.md). Estado web separado del estado Figma/contrato; no VALIDATED visual global ni aprobación humana simulada.

Logos PARTIAL_ASSETS: 64/72 archivos; ocho IDs ausentes por límite MCP, detallados en manifiesto. No sustituidos. Las excepciones de las fuentes siguen vigentes. Publicación NOT_REQUESTED; no backend. Protocolo P07 exige el mismo entregable para cada alta o modificación posterior.

## CHAT-LAYOUT-001 · revisión read-only · 2026-10-09

[Estado vigente por alcance](../implementations/figma/chat-layout.v0.1.1.state.json): DOCUMENTED_READ_ONLY, implementación PARTIAL para nuevo layout. [Enmienda](../specs/components/chat.layout.amendment.v0.1.1.md): columna816; Active FIXED/scroll Messages; Toolbar Expanded FIXED. No mutaciones Figma ni JSON. Los VALIDATED0.1.0 inferiores son históricos para dimensiones/overflow afectados, no QA del ajuste del usuario. [Handoff](SESSION-HANDOFF-2026-10-09-CHAT-LAYOUT.md).

## IMP-CHARACTERS-FIGMA-001 · 2026-10-08

VALIDATED técnico: Characters820:7, BENI822:6 (6 variantes), NAVI822:7 (7). [Estado](../implementations/figma/characters.v0.1.0.final.json), [QA](../qa/implementations/characters.v0.1.0.review.md).47 bindings,13 transiciones, tres variables reutilizadas y sombra nueva. Biblioteca UNPUBLISHED, auditoría PENDING; Conversation/Chat intactos.

## IMPL-CHAT-SECTION-001 · 2026-10-08

[CHAT-SECTION-0010.1.0](../specs/chat-section.contract.v0.1.0.md) → AI Design System tj3WIBEZDGLVs7MJWKCwgf, página Chat783:6. Set784:98, Standby783:24/Active783:116; sugerencias784:96, Default783:14/Hover783:21; auxiliar783:9; revisión784:99. [Estado e IDs](../implementations/figma/chat-section.v0.1.0.state.json). VALIDATED técnico con limitaciones cromáticas registradas, no certificación de accesibilidad. Reutiliza Conversation; cuatro Slots propios probados desde instancia. Sin nuevos tokens ni cambios a principales ajenos; fuente intacta. user_audit PENDING. Publicación remota no realizada en este lote.

## IMP-CONVERSATION-CHARACTERS-011 · 2026-10-08

UPDATE VALIDATED: siete fills principales de BENI/NAVI vinculados a tres variables directas773:275–277 en colección character-identity773:274, modo fijo773:0.27 apariciones heredan correctamente;40 resoluciones en cuatro temas. [Estado](../implementations/figma/conversation.characters.v0.1.1.state.json). Geometría/IDs/Slots preservados; semánticos UI intactos. Sustituye solo colores de personajes del cierre inferior.

## IMP-CONVERSATION-FIGMA-001 · 2026-10-08

[Conversation](https://www.figma.com/design/tj3WIBEZDGLVs7MJWKCwgf/AI-Design-System?node-id=766-120), página765:6; Message765:271, Response766:119, Composer765:397; siete principales/cuatro configuraciones públicas/doce Slots. VALIDATED técnico:179 nodos,124 paints,40 roles/160 aliases y cuatro temas, sin variables nuevas. [Estado e IDs](../implementations/figma/conversation.v0.1.0.state.json), [QA](../qa/implementations/conversation.v0.1.0.review.md). Controles DS reutilizados; fuente intacta. Excepciones de Dot oculto/contraste documentadas, auditoría PENDING, biblioteca UNPUBLISHED.

## IMP-FIGJAM-SDD-FLOW-2026-10-07 · documentación del proceso

[Tablero FigJam](https://www.figma.com/board/2SYQAjj9nZMF2a2yUSbPTf?node-id=11-798), raíz `11:798`: diez secciones y ocho flujos editables del proceso SDD aplicado, con estados, responsables, ejemplos y publicación privada GitHub. [Manifiesto y fuentes reproducibles](../implementations/figjam/sdd-flow-2026-10-07/manifest.json); [QA acotado](../qa/implementations/figjam-sdd-flow.2026-10-07.review.md) PASS: 151 nodos de flujo, 149 conectores visibles, relaciones conservadas y cero desbordes/solapamientos de contenido. Documento derivado, no contrato ni nueva aprobación. Biblioteca y datos canónicos intactos; Graphify STALE. [Continuidad](SESSION-HANDOFF-2026-10-07-FIGJAM-FLOW.md).

## IMP-APP-SHELL-FIGMA-001 · 2026-10-06

AI Design System / App Shell737:303 / componente737:304, Slot737:447. [Contrato0.1.0](../specs/app-shell.contract.v0.1.0.md), [ledger](../implementations/figma/app-shell.v0.1.0.state.json) y [todos los IDs creados](../implementations/figma/app-shell.v0.1.0.build.json). VALIDATED técnico:37bindings propios,60pinturas UI,48variables consumidas y93definiciones/aliases cotejados;12casos de composición, cuatro temas. Header518:123 y Sidebar619:481/496 reutilizados, no modificados. Instancia temporal737:448 retirada; solo permanece main en página. Auditoría humana PENDING; biblioteca no publicada. CanonicalJSON SHA256cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474 intacto.

## Referencias canónicas después de paso 4 · 2026-10-06

[Mapa de19 contratos antiguos→specs y hashes](../qa/contracts/specs-promotion.2026-10-06.manifest.json). Las implementaciones existentes conservan IDs, versiones técnicas, QA y digests del momento de ejecución; no se reescribe su historia para simular una nueva construcción. Para la norma vigente, resolver las rutas antiguas mediante sus punteros y aplicar las sustituciones indicadas en specs. No se hizo ninguna llamada Figma, cambio de variables ni publicación de biblioteca. Bases aún pendientes conservan su estado.

## IMP-LOGOS-REFINEMENT-001 · 2026-10-06

Página427:122, seis sets existentes conservados sin mutaciones permanentes. Clones y marcos temporales de diagnóstico retirados por IDs; lookup null y digests principales intactos. [QA/readback](../qa/implementations/logos.refinement.v0.1.1.review.md), [estado](../implementations/figma/logos.v0.1.0.state.json). No se crearon variables, copiaron assets omitidos ni publicó biblioteca. Cierre exacto bloqueado por57 deltas ya documentados, no defectos nuevos.

## IMP-RADIO-CHECKBOX-REFINEMENT-001 · 2026-10-06

AI-Design-System: Radio página142:122, sets142:144/143:166; Checkbox página149:122,set149:199. Solo [ocho posiciones de iconos](../implementations/figma/radio-checkbox.refinement.v0.1.2.write.json) modificadas; no variables ni IDs nuevos permanentes. [QA vigente](../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md). Las entradas base conservan historia y los ledgers enlazan refinamiento0.1.2; VALIDATED contra contrato delegado, no aprobado por usuario ni publicado.

## IMP-SIX-FAMILY-COLOR-001 · 2026-10-05

Seis familias con validación cromática vigente según [estado](../implementations/figma/six-family-color.v0.1.0.state.json) y [QA](../qa/implementations/six-families.color.v0.1.0.review.md).42 bindings actualizados,179 definiciones preservadas,12 roles de extensión verificados. Auditoría PENDING; no se publicó la biblioteca. Los estados históricos de cada familia incorporan colorRefinement como referencia vigente.

## IMP-FILTER-CHIP-SEMANTIC-021 · 2026-10-05

[Estado](../implementations/figma/filter-chip.semantic.v0.2.1.state.json): set72:298/página Chips67:122 actualizado in situ. 12 textos y 24 vectores usan roles inverse; nueva variable705:122 alias neutral/100 en cuatro modos. 30 variantes/181 nodos intactos. VALIDATED para alcance semántico/cromático; auditoría PENDING, no publicación remota.

## IMP-BUTTON-LOCAL-BINDINGS-FIGMA-001 · 2026-10-05

[Estado0.2.2](../implementations/figma/buttons.local-bindings.v0.2.2.state.json): UPDATE aplicado al set26:81 en Buttons0:1. 722 bindings en123 nodos ahora usan nueve roles locales ya existentes. 60variantes y364nodos conservados; sin variables, primitivas ni nodos nuevos. Capturas idénticas y regresión sin cambios en Modal/Empty states; Sidebar no tiene consumidores directos en el alcance leído. VALIDATED técnico acotado; auditoríaPENDING. No publicación de biblioteca.

## Search · revisión documental 0.1.1 · 2026-10-05

[Estado vigente](../implementations/figma/search.v0.1.1.state.json) vincula el set418:263 al contrato Search0.1.1. Ninguna mutación Figma: los IDs, variantes y geometría se conservan. VALIDATED para correspondencia documental; no nueva validación cromática global. Biblioteca UNPUBLISHED y auditoría PENDING según registro.

Histórico del corte Search: Buttons26:81 tenía722 referencias a nueve variables remotas; quedó resuelto por IMP-BUTTON-LOCAL-BINDINGS-FIGMA-001, no por el QA de Search. [Continuación](SESSION-HANDOFF-2026-10-05-REFINEMENT.md).

## IMP-EMPTY-STATES-FIGMA-001 · 2026-10-05

VALIDATED técnico/visual acotado: página639:128, set645:275, revisión649:291. Cuatro variantes, seis ilustraciones vectoriales y ochoSlots nativos.108paints,80bindings tipográficos,31variables/124aliases,264comparaciones por tema sin errores. [Ledger](../implementations/figma/empty-states.v0.1.0.state.json), [QA](../qa/implementations/empty-states.v0.1.0.figma.review.md). AuditoríaPENDING, bibliotecaUNPUBLISHED; límites cromáticos/tipográficos explícitos.

## IMP-SIDEBAR-FIGMA-001 · 2026-10-05

VALIDATED visual/técnico acotado. Página614:125; Menu Item615:355, Sidebar619:480, Top bar619:607; Review625:264.141paints/35textos,42variables,576comparaciones de tema,16checksSlots y16texto largo. [Estado](../implementations/figma/sidebar.v0.1.0.state.json), [QA](../qa/implementations/sidebar.v0.1.0.figma.review.md). AuditoríaPENDING, bibliotecaUNPUBLISHED.

## IMP-MODAL-FIGMA-001 · 2026-10-01

VALIDATED para alcance visual delegado. PáginaModal565:122; Basic567:360,Media569:301,SideBySide569:327; Review578:301. [Estado](../implementations/figma/modal.v0.1.0.state.json), [QA](../qa/implementations/modal.v0.1.0.figma.review.md).25pruebas de composición,123paints,53textos,34 tokens/136 aliases,392comparaciones de temas. Excepciones tipográficas/contraste/comportamiento documentadas. BibliotecaUNPUBLISHED; auditoríaPENDING.

## IMP-TABLE-FIGMA-001 · 2026-10-01

VALIDATED con alcance técnico y excepcionesdocumentadas. PáginaTable546:122/main548:895;Header548:408,Rowset548:893,HeaderCell546:257,BodyCell546:292,ActionsCell548:372. [Estado](../implementations/figma/table.v0.1.0.state.json), [manifestfinal](../implementations/figma/table.v0.1.0.final.json), [QA](../qa/implementations/table.v0.1.0.figma.review.md).27checks estructurales,899bindingslocales,36tokens/144aliases. Fuentes/mains externos intactos; cero variablesnuevas. Auditoría humanaPENDING, bibliotecanopublicada.

## IMP-HEADER-FIGMA-001 · 2026-10-01

VALIDATED técnico: página Headers518:122, componente518:123, Slot518:124 y caret privado521:124. [Estado](../implementations/figma/header.v0.1.0.state.json), [QA](../qa/implementations/header.v0.1.0.figma.review.md).43tokens/172comparaciones de modos y268pinturas sin errores. Slots0/1/3/5/7, cuatro temas, texto largo, booleanas e iniciales probados. No cambios a mains reutilizados ni logos. Tres aliases semánticos nuevos sincronizados con JSON. Asteriscos de contraste y responsive Desktop en auditoría. Biblioteca UNPUBLISHED; usuario PENDING.

## IMP-COMPOSITION-SLOTS-FIGMA-002

2026-09-30 · VALIDATED para Slots de Steps/Gallery, Pagination/Pages y leyendas Charts; variantes e IDs principales preservados. Nueve variables contextuales nuevas de Pagination, cero primitivas/RGB nuevos; JSON/Figma coinciden. [Estado/IDs](../implementations/figma/composition-slots.v0.1.1.state.json), [QA](../qa/implementations/composition-slots.v0.1.1.figma.review.md), [continuación](SESSION-HANDOFF-2026-09-30-SLOTS.md). Biblioteca UNPUBLISHED; auditoría PENDING. No revalida la paleta histórica de Charts. Vistas consumidoras: Steps491:322, Navigation499:313, Charts488:167.

## IMP-COMPOSITION-SLOTS-FIGMA-001

2026-09-29 · UPDATE bajo COMPOSITION-SLOTS-0010.1.0. Slots nativos Options/Select457:470, Tabs/Switch Tab283:128 y Trail/Breadcrumbs191:229. VALIDATED exclusivamente para el alcance Slots y corrección de texto largo declarada. IDs originales y tamaños por defecto conservados; cero variables nuevas/modificadas. [Estado y IDs](../implementations/figma/composition-slots.v0.1.0.state.json), [QA](../qa/implementations/composition-slots.v0.1.0.figma.review.md), [continuación](SESSION-HANDOFF-2026-09-29-SLOTS.md).15 instancias de prueba identificadas; sin detach, sin publicar biblioteca. Los registros0.1.0 siguientes describen su alcance histórico y se complementan con esta enmienda.

## IMP-SELECT-FIGMA-001

2026-09-29 · SELECT-0010.1.0 · VALIDATED para dos presentaciones documentadas. Destino tj3WIBEZDGLVs7MJWKCwgf, página Select444:122, set457:470, variantes456:402/456:421, guía456:486 y ejemplo458:470. Se reutilizan Input Field397:152 y Dropdown Item446:528 sin modificar sus principales. Cero variables/estilos/primitivas nuevos. [Estado](../implementations/figma/select.v0.1.0.state.json), [QA](../qa/implementations/select.v0.1.0.figma.review.md). Excepciones no ocultas: sombras literales, métricas ocultas heredadas. Biblioteca UNPUBLISHED, auditoría humana PENDING.

## IMP-DROPDOWN-ITEM-FIGMA-001

- **Destino:** AI Design System / Select444:122, set Dropdown Item446:528; guía445:122 y ejemplos448:312.
- **Contrato:** [DROPDOWN-ITEM-001 v0.1.0](../specs/dropdown-item.contract.v0.1.0.md), digest en registro de contratos; datos canónicos intactos.
- **Operación/estado:** CREATE, VALIDATED técnicamente.18 variantes,10 propiedades editables,180 referencias y186 pinturas verificadas.72 instancias directas de dependencias,93 incluyendo internas.
- **Evidencia:** [estado](../implementations/figma/dropdown-item.v0.1.0.state.json), [mapa de IDs y creación](../implementations/figma/dropdown-item.v0.1.0.creation.json), [QA](../qa/implementations/dropdown-item.v0.1.0.figma.review.md). Cuatro temas, swaps y truncado probados. Sin variables ni primitivas nuevas.
- **Límites:** auditoría humana PENDING, biblioteca UNPUBLISHED; no frontend. Las composiciones Select siguen pendientes. [Continuación](SESSION-HANDOFF-2026-09-28-SELECT.md). Graphify STALE.

## IMP-LOGOS-FIGMA-001 · Logos

- **Destino:** AI Design System / Logos427:122, guía428:122. Seis sets locales,72variantes,2,967nodos de artwork.
- **Estado:** implementación parcial, QA global PENDING. Los doce frames restantes están OMITIDOS por instrucción del usuario; la sesión del editor ya no bloquea otras familias. Se conservan los seis sets existentes y las diferencias geométricas documentadas.
- **Contrato:** [LOGOS-001 v0.1.0](../drafts/contracts/logos.contract.v0.1.0.md), [estado e IDs](../implementations/figma/logos.v0.1.0.state.json), [QA parcial](../qa/implementations/logos.v0.1.0.figma.review.md), [reanudación](SESSION-HANDOFF-2026-09-28-LOGOS.md).
- **Verificado:** cero bindings,72variantes y propiedades/defaults iguales, cuatro dependencias locales; paths, paints, imágenes y efectos coincidentes. Diferencias geométricas máximas0.00030517578125px; no se ocultan bajo PASS ni se redibuja artwork.
- **Sin cambios:** fuente original, JSON de tokens, otras familias. Auditoría humana PENDING; biblioteca UNPUBLISHED; Graphify STALE.


**Nota de vigencia cromática (2026-09-24):** los estados `VALIDATED` de abajo describen el QA técnico efectuado sobre las versiones entonces construidas. La posterior decisión de [conservar colores de origen y marcar limitaciones](decisions.md#dec-migration-contrast-limitations-001--fidelidad-cromática-y-revisión-interna) reabre únicamente la conformidad cromática de las familias afectadas; [QA-MIGRATION-COLOR-FIDELITY-REOPEN-001](qa.md#qa-migration-color-fidelity-reopen-001) registra el alcance. Ningún color de Figma se declara restaurado por esta nota.

## IMP-TOKENS-FIGMA-001

- **Artefacto:** variables de foundations/tokens en Figma.
- **Destino:** `AI-Design-System`, file key `tj3WIBEZDGLVs7MJWKCwgf`.
- **Estado:** `VALIDATED` (2026-09-22), limitado a las variables del contrato aprobado.
- **Contrato aprobado:** [FOUNDATIONS-TOKENS-001 0.1.0](../specs/foundations/foundations-tokens.contract.md), SHA-256 bytes `e7362c364aa2c93a1a5bd50e0024d6b551f8ec6c6947bb62c6779ee25c1b7999`.
- **Datos:** [inventario](../sources/inventories/tokens.inventory.json), SHA-256 bytes `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.
- **Operación:** `CREATE`; preflight del destino encontró una página vacía, cero colecciones, cero variables y cero estilos locales.
- **Creado:** colección `semantic`, ID destino `VariableCollectionId:6:2`, modos Contable `6:0`, Administrativo `6:1`, Servicios `6:2`, Personas `6:3`; colección `primitive`, ID destino `VariableCollectionId:6:3`, modo Value `6:4`; 129 variables semánticas y 141 primitivas. Se preservaron 512 aliases y 145 literales por modo.
- **Mapa y diario:** [estado de construcción](../implementations/figma/foundations-tokens.state.json).
- **QA de implementación:** [QA-TOKENS-FIGMA-001](../qa/implementations/foundations-tokens.figma.review.md), `PASS` para REQ-TOK-001–005. Lectura final posterior a la última escritura: cero discrepancias, aliases rotos, tipos incompatibles o ciclos.
- **Fuera de alcance:** componentes, páginas de documentación, estilos no especificados, bindings de consumidores y frontend. `Page 1` permaneció vacía.

## IMP-BUTTON-FIGMA-001 · página Buttons y validación

- **Artefacto y destino:** Button en `AI-Design-System`, file key `tj3WIBEZDGLVs7MJWKCwgf`.
- **Estado:** `VALIDATED` para la representación Figma especificada por `BUTTON-001` y `AMD-BUTTON-PAGE-001`; no acredita frontend ni comportamiento de producto.
- **Contrato aprobado:** [BUTTON-001 0.1.0](../specs/components/button.contract.md), SHA-256 bytes `4b94f80787c1fc9d9990f806c99900e17db060e65b624471b0c8d93f534f2abb`; decisión [DEC-BUTTON-001](decisions.md).
- **Operación:** `UPDATE` solo del nombre de la página, de `Page 1` a `Buttons`, conforme a [DEC-BUTTON-PAGE-001](decisions.md) y [AMD-BUTTON-PAGE-001](../specs/components/button-page-name.amendment.md). El set existente se clasificó `VALIDATE_ONLY`; no se recreó, movió, duplicó ni alteró internamente.
- **Mapa de IDs reales:** página antes `0:1` → página después `0:1`; set antes `26:81` → set después `26:81`, key `ad6968e790043ee654b3590596d5e593ebcbe73d`. No se asignaron IDs nuevos.
- **Antes:** una página `Page 1` con el set Button como único nodo superior, 60 variantes, ocho definiciones de propiedad, 120 iconos Phosphor y 23 reacciones; [QA parcial de preflight](../qa/implementations/button.figma.preflight.md).
- **Acción completada:** se renombró la página `0:1` a `Buttons`, con guardas previas de nombre, contenido e identidad del set; la respuesta de escritura devolvió el page ID mutado.
- **Después:** lectura independiente confirmó una única página `Buttons` con el mismo set `26:81`; 60 variantes únicas, 364 nodos, 60 textos, 120 instancias, 35 IDs de variables exactos y resueltos, 23 reacciones documentadas y captura visual de 516×1883 sin recortes o solapamientos aparentes.
- **QA de implementación:** [QA-BUTTON-FIGMA-002](../qa/implementations/button.figma.review.md), `PASS` para AC-BTN-001–007 y 009; AC-BTN-008 fuera del alcance web. No se corrigieron las dos transiciones focus/default que cambian de tamaño porque el contrato no autoriza inferir esa corrección.

## IMP-BUTTON-FIGMA-DOC-002 · Description de Buttons 0.2.0

- **Artefacto y destino:** metadatos del component set `button` (`26:81`) en la página `Buttons` (`0:1`) de `AI-Design-System`.
- **Estado:** `VALIDATED` para Description dentro del archivo Figma, no para distribución de biblioteca ni web.
- **Contrato aprobado:** [BUTTON-001 0.2.0](../specs/components/button.contract.v0.2.0.md), SHA-256 bytes `53e13fa8e664f70d0ce81116e850bbcb0ab7da9f14ac0f08607fa5fda09894a1`; decisión [DEC-BUTTON-USAGE-002](decisions.md).
- **Operación:** `UPDATE` de `description` y `descriptionMarkdown` del set local existente. `documentationLinks` permaneció vacío porque no hay URL pública verificada. No se editaron variantes, propiedades, interacciones, iconos ni variables.
- **Antes/después y mapa:** [estado reproducible](../implementations/figma/button-description.v0.2.0.state.json), SHA-256 bytes `aff95f7a55fe93c7568420f185d8a54482e427b80fe2be277aaa740e37909120`; IDs `0:1` y `26:81` conservados.
- **QA:** [QA-BUTTON-FIGMA-USAGE-003](../qa/implementations/button-description.v0.2.0.figma.review.md), `PASS`; readback independiente de texto exacto y de 60 variantes, 120 iconos Phosphor, 35 variables y 23 reacciones.
- **Límite:** `getPublishStatusAsync() = UNPUBLISHED`; la actualización está en el archivo, sin afirmar que se haya distribuido como biblioteca de equipo.

## IMP-FILTER-CHIP-FIGMA-001 · Chips 0.2.0

- **Artefacto y destino:** Filter Chip en `AI-Design-System`, file key `tj3WIBEZDGLVs7MJWKCwgf`.
- **Estado:** `VALIDATED` (2026-09-23) para la representación Figma aprobada; no acredita frontend ni comportamiento de producto.
- **Contrato aprobado:** [FILTER-CHIP-001 0.2.0](../specs/components/filter-chip.contract.v0.2.0.md), SHA-256 bytes `325a408cfa6a5880c2136aee89a448e9ab3a6d928199543d946d6ae3a52a6cb8`; decisión [DEC-FILTER-CHIP-APPROVAL-002](decisions.md).
- **Operación:** `CREATE`. Preflight confirmó que solo existía Buttons `0:1` con su set `26:81`; 28/28 variables del mapa resolvieron en la colección semantic y PlusCircle key coincidió con Phosphor.
- **Creado:** página exclusiva `Chips` `67:122`; set `Filter Chip` `72:298`, 30 variantes únicas `small/middle/large × selected false/true × default/hover/press/focus/disabled`, variante inicial `70:122`, 30 etiquetas y 60 instancias Phosphor PlusCircle ocultas por defecto y conectadas a propiedades booleanas y de swap. Ambos swaps ofrecen 1512 component sets Phosphor preferidos.
- **Bindings:** variables locales `semantic` por identidad para colores, tamaños, tipografía, radio, gap y paddings; 28 tokens usados resueltos en los cuatro modos (112/112 pares) y 126 paints verificados. Description rica aprobada y propiedades del set leídas de vuelta.
- **Mapa y diario:** [filter-chip.v0.2.0.state.json](../implementations/figma/filter-chip.v0.2.0.state.json); [captura final](../implementations/figma/filter-chip.v0.2.0.png), SHA-256 bytes `0a37beae3477782d77020eea80d1c0da0fa23a760c8713bcd52bc75247baada8`.
- **QA:** [QA-FILTER-CHIP-FIGMA-001](../qa/implementations/filter-chip.v0.2.0.figma.review.md), `PASS` para AC-FC-001–009 tras la última escritura; Buttons conserva su página, set y 60 variantes.
- **Límite:** set `UNPUBLISHED` como biblioteca de equipo; no se ejecutó publicación ni se implementó web.

## IMP-BUTTON-SEMANTIC-SCOPE-FIGMA-001 · ajuste de texto Disabled

- **Artefacto y destino:** actualización acotada del set Button `26:81` en la página `Buttons` `0:1` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [AMD-BUTTON-SEMANTIC-SCOPE-001 0.2.1](../drafts/contracts/button.semantic-scope-amendment.v0.2.1.md); `user_audit: PENDING`.
- **Operación:** nueve textos Disabled pasaron de `color/icon/disabled` a `color/text/disabled`. Ambos roles aliasan `color/neutral/400`; no se creó token ni cambió RGB. Los iconos conservan su rol iconográfico.
- **Lectura final:** doce labels Disabled correctos; cero tokens de icono en 60 textos. 60 variantes, 364 nodos, 120 instancias, ocho propiedades y 23 reacciones intactos. Captura 516×1883 inspeccionada.
- **Mapa y QA:** [estado](../implementations/figma/button.semantic-scope.v0.2.1.state.json); [QA-BUTTON-FIGMA-SEMANTIC-004](../qa/implementations/button.semantic-scope.v0.2.1.figma.review.md) `PASS`. Biblioteca no publicada; web fuera de alcance.

## IMP-TOOLTIP-FIGMA-001 · Tooltips 0.1.0

- **Artefacto y destino:** Tooltip en `AI-Design-System`, file key `tj3WIBEZDGLVs7MJWKCwgf`.
- **Estado:** `VALIDATED` técnicamente para el contrato delegado; `user_audit: PENDING`, sin atribuir aprobación humana. Web fuera del alcance.
- **Contrato:** [TOOLTIP-001 0.1.0](../drafts/contracts/tooltip.contract.v0.1.0.md), SHA-256 bytes `522b74426f781231dbf0a3ce7daed35909ab8f1358e347efe97e34f454416402`; datos canónicos `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`; [decisión delegada](decisions.md).
- **Operación:** `CREATE`. Página exclusiva `Tooltips` `85:122`, set `Tooltip` `88:122`, cuatro variantes con flecha vectorial y propiedad TEXT `Content#88:0`; título y nota mínimos dentro de la misma página. Buttons y Chips se conservaron.
- **Bindings:** fondo y flecha `color/background/inverse`, texto `color/text/inverse`, familia/peso/tamaño/interlineado/tracking y spacing/radio semánticos por ID local. 52 relaciones token-modo verificadas; cero fills o strokes sólidos sin binding. Dos sombras por variante se preservan literalmente porque el JSON no contiene categoría de sombra.
- **Diferencia visible:** con interlineado 24 y tracking −0.01 px del destino, el ancho se ajustó para mantener una línea: Right/Left 121×40, Up/Down 111×50. La fuente medía 116×38 y 107×48. La normalización está en el contrato delegado y queda pendiente de auditoría humana.
- **Mapa y diario:** [tooltip.v0.1.0.state.json](../implementations/figma/tooltip.v0.1.0.state.json). Captura de 636×130 inspeccionada inline; no se retuvo URL efímera como archivo.
- **QA:** [QA-TOOLTIP-FIGMA-001](../qa/implementations/tooltip.v0.1.0.figma.review.md), `PASS` para AC-TTIP-001–008; contraste calculado 14.63:1 en los cuatro modos, sin afirmar accesibilidad funcional del disparador.
- **Límite:** set `UNPUBLISHED`; no se creó Code Connect ni se implementó web.

## IMP-BADGE-FIGMA-001 · Badges 0.1.0 + contraste 0.1.1

- **Artefacto y destino:** Badge en `AI-Design-System`, file key `tj3WIBEZDGLVs7MJWKCwgf`; página exclusiva `Badges` `94:122`, set `Badge` `98:128`.
- **Estado histórico:** `VALIDATED` técnicamente bajo el criterio previo para contrato delegado [BADGE-001 0.1.0](../specs/components/badge.contract.v0.1.0.md) y [AMD-BADGE-CONTRAST-001 0.1.1](../drafts/contracts/badge.contrast-amendment.v0.1.1.md); los colores/umbrales afectados fueron sustituidos por 0.1.2. `user_audit: PENDING`.
- **Operación:** `CREATE` de seis variantes Type y `UPDATE` acotado de cuatro nodos por contraste. Doce instancias Phosphor Presentation enlazadas, propiedades TEXT, dos BOOLEAN y dos INSTANCE_SWAP con 1512 preferidos. Variables locales semánticas; no se crearon tokens.
- **Contraste histórico bajo 0.1.1:** texto mínimo 4.59:1 e iconos mínimos 3.61:1 en los cuatro modos según el QA de entonces. El readback 0.1.2 restauró los colores fuente y sustituyó esta medición para Informational/Warning; captura 582×105 de ese estado histórico conservada.
- **Diferencias:** Light 64×25 frente a 62×25 de fuente por stroke interior bajo HUG; texto principal en Informational/Warning e iconos principales en Warning; otras dos normalizaciones semánticas de rol documentadas. Las diferencias quedan para auditoría humana.
- **Mapa y diario:** [badge.v0.1.0.state.json](../implementations/figma/badge.v0.1.0.state.json). **QA:** [QA-BADGE-FIGMA-002](../qa/implementations/badge.v0.1.1.figma.review.md), `PASS`; [hallazgo previo](../qa/implementations/badge.v0.1.0.contrast-finding.md) permanece `FAIL` histórico.
- **Límite:** set `UNPUBLISHED`; no se acredita web ni accesibilidad funcional.

## IMP-CONTROL-COLORS-FIGMA-001 · extensión semántica de colores

- **Artefacto y destino:** dos variables nuevas en la colección `semantic` de `AI-Design-System`, sin página de Foundations inventada.
- **Estado:** `VALIDATED` técnicamente para [AMD-FOUNDATIONS-CONTROL-COLORS-001 0.1.1](../drafts/contracts/foundations.control-colors.amendment.v0.1.1.md); `user_audit: PENDING`.
- **JSON canónico:** [extensión de colores de control](../drafts/foundations/ai-design-system.control-colors.v0.1.0.json), SHA-256 `4ef75143af30b0e934cb94aa62d3acb56c32874dc7e229a500a31c8928a7f839`; inventario original `SRC-TOKENS-INV-001` intacto.
- **Creado y leído de vuelta:** `color/border/control` `VariableID:123:122` con scope `STROKE_COLOR` y `color/background/control-hover` `VariableID:123:123` con scopes `FRAME_FILL`/`SHAPE_FILL`. Ocho aliases apuntan a la primitiva local `color/neutral/500` `VariableID:8:97`; nombres, `description`, tipo y `codeSyntax` coinciden con JSON. La colección semántica contiene 131 variables tras la extensión.
- **Mapa y QA:** [estado](../implementations/figma/control-colors.v0.1.0.state.json); [QA-CONTROL-COLORS-FIGMA-001](../qa/implementations/control-colors.v0.1.0.figma.review.md) `PASS`. No se publicó biblioteca ni se generó código web.

## IMP-TOGGLE-FIGMA-001 · Toggles 0.1.0 + fidelidad/contraste 0.1.2 + efecto 0.1.3

- **Artefacto y destino:** Toggle en `AI-Design-System`, página exclusiva `Toggles` `111:122`, set `Toggle` `111:163`.
- **Estado:** `VALIDATED` técnicamente para [TOGGLE-001 0.1.0](../drafts/contracts/toggle.contract.v0.1.0.md) más [AMD-TOGGLE-VISUAL-CONTRAST-002 0.1.2](../drafts/contracts/toggle.visual-contrast-amendment.v0.1.2.md) y [AMD-TOGGLE-FOCUS-EFFECT-003 0.1.3](../drafts/contracts/toggle.focus-effect-amendment.v0.1.3.md); `user_audit: PENDING`. La enmienda 0.1.1 y su PASS técnico son historial, con hallazgo visual posterior.
- **Operación:** `CREATE` de página y ocho variantes; `UPDATE` 0.1.1 de dos fills Off; `UPDATE` 0.1.2 de seis paints en cuatro nodos para devolver fondos claros, dar contorno neutral contrastante y corregir roles de fondo/shape. Cuatro propiedades TEXT/BOOLEAN conectadas en las ocho variantes y dos anillos de focus preservados.
- **Lectura final:** 40 pinturas sólidas ligadas con cero errores de scope o categoría, 80 bindings tipográficos, 32 radios, 32 lados de stroke, 23 roles×cuatro modos sin alias roto; contraste activo mínimo 3.24:1. Capturas destino 704×280 y fuente 680×194 inspeccionadas inline.
- **Diferencias:** Off/Default y Off/Focus recuperan el fondo pálido de la fuente y oscurecen solo el contorno neutral de 1 px; Off/Hover y thumb Disabled mantienen color con roles correctos. `defualt` corregido, radio semántico, interlineado 16 y halo focus blanco tokenizado. Sombras internas conservadas literalmente por falta de token de sombra. El tamaño visual 40×20 no acredita hit target web.
- **Efectos de foco:** dos roles nuevos de scope `EFFECT_COLOR` sustituyen cuatro bindings en `111:135` y `111:155`. Los colores y geometría de los 25 efectos del set no cambiaron; ocho variantes y anillos visibles leídos de nuevo. [Hallazgo previo](../qa/implementations/toggle.v0.1.2.effect-scope-finding.md) conservado como `FAIL` histórico.
- **Mapa y diario históricos:** [toggle.v0.1.0.state.json](../implementations/figma/toggle.v0.1.0.state.json); script base reproducible [toggle-build.v0.1.0.js](../drafts/figma/toggle-build.v0.1.0.js). [QA-TOGGLE-FIGMA-004](../qa/implementations/toggle.v0.1.2.figma.review.md) y [QA-TOGGLE-FIGMA-006](../qa/implementations/toggle.v0.1.3.figma.review.md) conservan validez para sus comprobaciones no sustituidas; la afirmación de contraste/fidelidad de los dos bordes Off está `SUPERSEDED` por 0.1.5. [QA técnico 0.1.1](../qa/implementations/toggle.v0.1.1.figma.review.md) y [hallazgo de fidelidad](../qa/implementations/toggle.v0.1.1.visual-fidelity-finding.md) se conservan.

## IMP-TOGGLE-MIXED-FIGMA-001 · ampliación Mixed 0.1.4

- **Destino:** página `Toggles` `111:122`, set `Toggle` `111:163` en AI Design System. [Estado y mapa](../implementations/figma/toggle.mixed.v0.1.4.state.json).
- **Contrato:** [enmienda Mixed 0.1.4](../drafts/contracts/toggle.mixed-amendment.v0.1.4.md), `DELEGATED_FOR_BUILD`; [comportamiento de agregado](../drafts/behavior/toggle-mixed/behavior-contract.md). `user_audit: PENDING`.
- **Resultado:** `VALIDATED` para las cuatro variantes añadidas y sus bindings; [QA-TOGGLE-FIGMA-007](../qa/implementations/toggle.mixed.v0.1.4.figma.review.md) `PASS`. El set suma 12 variantes, pero continúa `UNPUBLISHED`. La reapertura cromática de las ocho variantes anteriores sigue separada y no se da por cerrada con este QA.
- **Límite:** set `UNPUBLISHED`; no se implementó web, teclado ni semántica de producto.

## IMP-TOGGLE-SOURCE-COLOR-FIGMA-001 · dos bordes Off restaurados 0.1.5

- **Destino:** página `Toggles` `111:122`, set `Toggle` `111:163`; tracks `111:145` y `111:155` modificados, con los demás nodos intactos. [Estado de readback](../implementations/figma/toggle.source-color.v0.1.5.state.json).
- **Contrato:** [enmienda 0.1.5](../drafts/contracts/toggle.source-color-amendment.v0.1.5.md) `DELEGATED_FOR_BUILD`, QA documental `PASS`, auditoría humana `PENDING`.
- **Resultado:** ambos strokes consumen `color/border/strong` local, alias neutral/300 en cuatro modos. Fills y doce variantes intactos; cero variables nuevas. [QA Figma](../qa/implementations/toggle.source-color.v0.1.5.figma.review.md) `PASS` acotado y captura visual inspeccionada.
- **Pendiente:** el halo Focus fuente `#F8FAFC` no coincide con el blanco del destino y carece de primitiva exacta en el JSON; [AUD-003](../specs/MIGRATION-AUDIT.md) queda abierto. Set `UNPUBLISHED`; no cerrar QA cromático global ni promover Toggle a `specs/` todavía.

## IMP-FOCUS-EFFECTS-FIGMA-001 · extensión semántica de foco

- **Artefacto y destino:** dos variables `COLOR` nuevas en colección `semantic` de `AI-Design-System`, sin alterar Foundations originales.
- **Estado:** `VALIDATED` técnicamente para [AMD-FOUNDATIONS-FOCUS-EFFECTS-001 0.1.2](../drafts/contracts/foundations.focus-effects.amendment.v0.1.2.md); auditoría humana `PENDING`.
- **JSON canónico:** [extensión de foco](../drafts/foundations/ai-design-system.focus-effects.v0.1.0.json), SHA-256 `0baef3e14a121d3284c04d28bd8bf2cc66a940270f3486994a23e3456d7fc3d4`.
- **Creado y releído:** `color/focus/effect-outer` `VariableID:136:122` y `color/focus/effect-inner` `VariableID:136:123`; scope exclusivo `EFFECT_COLOR`, ocho aliases a `color/blue/500` y `color/neutral/100`, respectivamente. Colección semántica de 131 a 133. [Estado](../implementations/figma/focus-effects.v0.1.0.state.json), [QA](../qa/implementations/focus-effects.v0.1.0.figma.review.md) `PASS`.
- **Límite:** sin publicación ni implementación web.

## IMP-RADIO-INDICATOR-COLORS-FIGMA-001 · extensión de rellenos de selección

- **Artefacto y destino:** dos variables `COLOR` en colección `semantic` de `AI-Design-System`, sin modificar primitivas ni el inventario fuente.
- **Estado:** `VALIDATED` técnicamente para [enmienda Foundations 0.1.3](../drafts/contracts/foundations.radio-indicator-colors.amendment.v0.1.3.md); auditoría humana `PENDING`.
- **JSON canónico:** [extensión Radio](../drafts/foundations/ai-design-system.radio-indicator-colors.v0.1.0.json), SHA-256 `46f53dc329a93374f486ad26452cdd991c6cb0651a6c068865e34352d8e6161a`.
- **Creado y releído:** `color/background/control-selected` `VariableID:140:122` y `color/background/control-selected-hover` `VariableID:140:123`; scope exclusivo `SHAPE_FILL`, ocho aliases por modo, colección semántica 133→135. [Estado](../implementations/figma/radio-indicator-colors.v0.1.0.state.json) y [QA](../qa/implementations/radio-indicator-colors.v0.1.0.figma.review.md) `PASS`.
- **Límite:** sin publicación ni implementación web.

## IMP-RADIO-BUTTON-FIGMA-001 · Radio Buttons 0.1.0

- **Artefacto y destino:** página exclusiva `Radio Buttons` `142:122` de `AI-Design-System`; set local `Radio Indicator` `142:144` y API pública `Radio Button` `143:166`.
- **Estado:** `VALIDATED` técnicamente para [RADIO-BUTTON-001 0.1.0](../drafts/contracts/radio-button.contract.v0.1.0.md) y extensión de color de selección; auditoría humana `PENDING`.
- **Operación:** `CREATE` de 8+8 variantes, estilo de foco reutilizable ahora llamado `Focus/Selection Outset`, ocho instancias anidadas, 16 etiquetas ocultas conectadas a dos TEXT y dos BOOLEAN. Página rotulada con función de ambos sets.
- **Lectura final:** 36 paints sólidos ligados, cuatro efectos de foco `EFFECT_COLOR`, 80 bindings tipográficos en etiquetas, ocho correspondencias de instancia correctas, cero errores semánticos, cero reacciones y mínimo de contraste activo 3.24:1 en los cuatro modos. Capturas fuente 678×194 y destino 696×713 inspeccionadas inline.
- **Diferencias deliberadas al construir 0.1.0:** On con dos círculos concéntricos en vez de stroke literal de 5 px; Off Default tuvo contorno neutral más contrastante, **sustituido por la restauración cromática 0.1.1**; labels editables e interlineado 20; halo claro tokenizado y helper local expandido. Se mantiene la apariencia general de fuente.
- **Mapa y QA:** [estado](../implementations/figma/radio-button.v0.1.0.state.json), [QA-RADIO-BUTTON-FIGMA-001](../qa/implementations/radio-button.v0.1.0.figma.review.md) `PASS`; scripts [indicador](../drafts/figma/radio-indicator-build.v0.1.0.js) y [wrapper](../drafts/figma/radio-button-build.v0.1.0.js).
- **Límite:** sets `UNPUBLISHED`; no se implementó web, exclusión mutua funcional ni teclado.

## IMP-CHECKBOX-FIGMA-001 · Checkboxes 0.1.0

- **Artefacto y destino:** página exclusiva `Checkboxes` `149:122`, set `Checkbox` `149:199` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [CHECKBOX-001 0.1.0](../drafts/contracts/checkbox.contract.v0.1.0.md); auditoría humana `PENDING`.
- **Operación:** `CREATE` de doce variantes, ocho instancias Phosphor Check/Minus con keys verificadas y 24 etiquetas conectadas a dos TEXT y dos BOOLEAN. Se renombró el estilo compartido de foco a `Focus/Selection Outset`, sin cambio de ID, colores ni efectos; Radio Button conserva su apariencia.
- **Lectura final:** 46 paints visibles ligados, seis colores de efecto `EFFECT_COLOR`, 120 bindings tipográficos, 48 radios, 16 lados de stroke, 12 gaps y 16 dimensiones de icono tokenizados; cero incidencias de categoría/scope y cero reacciones. Contraste activo mínimo 3.24:1. Capturas fuente 680×290 y destino 691×474 inspeccionadas inline.
- **Diferencias deliberadas al construir 0.1.0:** contorno neutral Unselected más contrastante, **sustituido por la restauración cromática 0.1.1**; radio local `radius/sm` de 4 px, interlineado de etiqueta 20 px, fill cromático de selección con rol propio y helper local de uso único simplificado.
- **Mapa y QA:** [estado](../implementations/figma/checkbox.v0.1.0.state.json), [QA-CHECKBOX-FIGMA-001](../qa/implementations/checkbox.v0.1.0.figma.review.md) `PASS`, [script reproducible](../drafts/figma/checkbox-build.v0.1.0.js).
- **Límite:** `UNPUBLISHED`; no se implementó selección funcional, grupo, teclado ni web.

## IMP-DOT-BACKGROUND-COLORS-FIGMA-001 · fondos semánticos Dot

- **Estado:** `VALIDATED` técnicamente; auditoría humana `PENDING`.
- **Creado y releído:** cuatro roles nuevos exclusivos `FRAME_FILL`, 16 aliases a primitivas existentes, colección semántica 135→139. [JSON canónico](../drafts/foundations/ai-design-system.dot-background-colors.v0.1.0.json), [estado](../implementations/figma/dot-background-colors.v0.1.0.state.json) y [QA](../qa/implementations/dot-background-colors.v0.1.0.figma.review.md).
- **Límite:** inventario histórico y primitivas intactos; sin publicación ni web.

## IMP-DOT-INACTIVE-BORDER-FIGMA-001 · borde semántico Inactive

- **Estado:** `VALIDATED` técnicamente; auditoría humana `PENDING`.
- **Creado y releído:** `color/border/status-inactive`, scope `STROKE_COLOR`, cuatro aliases a neutral/500, colección semántica 139→140. Tres strokes Inactive lo consumen sin alterar sus fills. [JSON canónico](../drafts/foundations/ai-design-system.dot-inactive-border.v0.1.0.json), [estado](../implementations/figma/dot-inactive-border.v0.1.0.state.json) y [QA](../qa/implementations/dot-inactive-border.v0.1.0.figma.review.md).

## IMP-DOT-FIGMA-001 · Dots 0.1.0 + enmienda 0.1.1

- **Artefacto y destino:** página exclusiva `Dots` `155:122`, set `Dot` `155:144` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [DOT-001](../drafts/contracts/dot.contract.v0.1.0.md) y su [enmienda Inactive](../drafts/contracts/dot.inactive-border-amendment.v0.1.1.md); auditoría humana `PENDING`.
- **Lectura final:** 15 variantes Type×Size, seis labels conectadas a dos propiedades TEXT, 36 pinturas ligadas con scope correcto, 60 radios, 60 lados de stroke, 28 dimensiones y 12 bindings de familia/peso. Cero reacciones. Capturas fuente 201×290 y destino 685×613 inspeccionadas inline.
- **Diferencias deliberadas:** roles de fondo propios sustituyen roles de icono; Inactive conserva fill pálido y gana contorno neutral 500 visible sobre blanco; `1`/`99+` son editables. FontSize 4/8 de fuente queda literal y señalado como riesgo de legibilidad.
- **Mapa y QA:** [estado](../implementations/figma/dot.v0.1.0.state.json), [QA-DOT-FIGMA-001](../qa/implementations/dot.v0.1.1.figma.review.md) `PASS`; scripts [base](../drafts/figma/dot-build.v0.1.0.js) y [enmienda](../drafts/figma/dot-inactive-border.v0.1.1.js).
- **Límite:** `UNPUBLISHED`; no se afirma comportamiento automático, WCAG ni implementación web.

## IMP-DOT-SOURCE-COLOR-FIGMA-002 · restauración del borde Inactive

- **Estado:** `VALIDATED` técnicamente para [Foundations 0.1.6](../specs/foundations/foundations.dot-inactive-border-source-color.amendment.v0.1.6.md) y [Dot 0.1.2](../specs/components/dot.source-color-amendment.v0.1.2.md); auditoría humana `PENDING`.
- **Cambio y readback:** mismo rol `color/border/status-inactive` `STROKE_COLOR`, cuatro aliases neutral/100, tres strokes Inactive blancos; 15 variantes y 36 paints visibles coinciden con la fuente. Avatar e Icon Button no consumen el rol en sus sets. [Estado](../implementations/figma/dot.source-color.v0.1.2.state.json) y [QA](../qa/implementations/dot.source-color.v0.1.2.figma.review.md).
- **Límite:** sustituye solo el contorno neutral/500 de la enmienda anterior; conserva `*` de visibilidad, `UNPUBLISHED` y ninguna afirmación WCAG.

## IMP-AVATAR-ROLES-FIGMA-001 · roles de fondo y tipografía Avatar

- **Estado:** `VALIDATED` técnicamente; auditoría humana `PENDING`.
- **Creado y releído:** `color/background/avatar-fallback` `FRAME_FILL` y `font/size/avatar-small` `FONT_SIZE`, ocho aliases primitivos, colección semántica 140→142. Servicios usa orange/600 por 4.72:1 con blanco. [JSON](../drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json), [estado](../implementations/figma/avatar-roles.v0.1.0.state.json) y [QA](../qa/implementations/avatar-roles.v0.1.0.figma.review.md).

## IMP-AVATAR-FIGMA-001 · Avatars 0.1.0

- **Artefacto y destino:** página exclusiva `Avatars` `165:198`, set `Avatar` `165:247` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [AVATAR-001](../drafts/contracts/avatar.contract.v0.1.0.md); auditoría humana `PENDING`.
- **Lectura final:** 12 variantes, 12 Dot Active anidados, cuatro iconos User Phosphor y cuatro iniciales editables; propiedades Icon swap, Initials y Show status conectadas; picker con 1512 alternativas Phosphor. 48/48 paints visibles ligados con categoría/scope correcto, cuatro IMAGE fills de muestra fuente, cero reacciones.
- **Visual y cambios:** capturas fuente 324×312 y destino 727×533 inspeccionadas; 3×4 y proporciones conservadas. Initials Small/Medium suben 6/9→10/12; solo Servicios oscurece el fallback a orange/600. [PNG fuente codificado](../sources/figma-snapshots/avatar-source-face-48.png.base64) conservado; no se inventó imagen.
- **Mapa y QA:** [estado](../implementations/figma/avatar.v0.1.0.state.json), [QA-AVATAR-FIGMA-001](../qa/implementations/avatar.v0.1.0.figma.review.md) `PASS`; scripts [base](../drafts/figma/avatar-build.v0.1.0.js) y [picker](../drafts/figma/avatar-preferred-icons.v0.1.0.js).
- **Límite:** `UNPUBLISHED`; no se implementó fallback de imagen, identidad o presencia funcional ni web.

## IMP-AVATAR-SOURCE-COLOR-FIGMA-002 · fallback Servicios de origen

- **Estado:** [enmienda Foundations 0.1.11](../drafts/contracts/foundations.avatar-fallback-source-color.amendment.v0.1.11.md) y [Avatar 0.1.1](../drafts/contracts/avatar.source-color-amendment.v0.1.1.md) con `PASS` cromático técnico; auditoría humana `PENDING`.
- **Readback:** alias del rol `color/background/avatar-fallback` Servicios orange/600→orange/500, otros tres modos intactos; ocho faces ligadas, doce Dot y cuatro textos sin pérdida de binding. [Estado](../implementations/figma/avatar.source-color.v0.1.1.state.json) y [QA](../qa/implementations/avatar.source-color.v0.1.1.figma.review.md).
- **Límite:** iniciales Small/Medium normalizadas quedan AUD-006; contraste Servicios 3.24:1 `*`, `UNPUBLISHED`.

## IMP-FEEDBACK-ICON-SCOPES-FIGMA-001 · scopes estrictos de feedback/icon

- **Estado:** `VALIDATED` técnicamente; auditoría humana `PENDING`.
- **Operación:** scope de `color/feedback/positive/icon`, warning/icon y danger/icon restringido de `[FRAME_FILL, SHAPE_FILL]` a `[SHAPE_FILL]`. Nombres, descripciones, aliases y valores intactos. [JSON de override](../drafts/foundations/ai-design-system.feedback-icon-scopes.v0.1.0.json), [estado](../implementations/figma/feedback-icon-scopes.v0.1.0.state.json), [QA](../qa/implementations/feedback-icon-scopes.v0.1.0.figma.review.md).
- **Regresión:** dos consumidores existentes en Badge siguen siendo vectores; barrido de 80 variables de color encontró cero incompatibilidades categoría/scope. Sin cambio visual ni publicación.

## IMP-WARNING-ICON-CONTRAST-FIGMA-001 · alias del icono Warning

- **Estado histórico:** `VALIDATED` técnicamente bajo la regla anterior; los cuatro aliases amber/700 fueron sustituidos por la restauración 0.1.1. Auditoría humana `PENDING`.
- **Operación:** `color/feedback/warning/icon` conserva identidad, descripción y scope `SHAPE_FILL`; sus cuatro aliases pasan de amber/600 a amber/700. Sobre warning/bg mejora contraste 2.96→4.38:1. [JSON](../drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.0.json), [estado](../implementations/figma/warning-icon-contrast.v0.1.0.state.json) y [QA](../qa/implementations/warning-icon-contrast.v0.1.0.figma.review.md).
- **Regresión:** cero consumidores previos entre nueve páginas de componentes; no hubo cambio visual en familias ya construidas. Primer consumidor será Inline Notification Warning.

## IMP-WARNING-ICON-SOURCE-COLOR-FIGMA-001 · alias Warning restaurado

- **Operación:** `color/feedback/warning/icon` `VariableID:13:48` conserva identidad, descripción y scope `SHAPE_FILL`; sus cuatro aliases regresan a `color/amber/600` local mediante [JSON 0.1.1](../drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.1.json). [Estado](../implementations/figma/warning-icon-source-color.v0.1.1.state.json).
- **Readback:** cuatro modos y vector existente de Inline Notifications `#C97B00` vinculados; [QA Figma](../qa/implementations/warning-icon-source-color.v0.1.1.figma.review.md) `PASS` técnico, contraste 2.96:1 `*`. No se creó variable; auditoría humana `PENDING`.

## IMP-BADGE-SOURCE-COLOR-FIGMA-001 · colores de origen restaurados

- **Destino:** página `Badges` `94:122`, set `Badge` `98:128`; seis IDs previos intactos. [Enmienda 0.1.2](../specs/components/badge.source-color-amendment.v0.1.2.md) y [estado](../implementations/figma/badge.source-color.v0.1.2.state.json).
- **Operación:** cuatro fills reconectados a roles de texto/icono de feedback con scope correcto. Informational y Warning vuelven a los colores de fuente; el icono derecho opcional oculto también queda preparado. Cero variables nuevas.
- **Readback:** 19 paints visibles comparados por RGB con la fuente, sin divergencias; 17 roles y 25 consumidores de paint incluidos opcionales, aliases por cuatro modos y seis etiquetas tipográficas verificados. [QA Figma](../qa/implementations/badge.source-color.v0.1.2.figma.review.md) `PASS` técnico; limitaciones 3.61/2.96:1 `*`; auditoría humana `PENDING`, set `UNPUBLISHED`.

## IMP-INLINE-NOTIFICATION-FIGMA-001 · Inline Notifications 0.1.0

- **Artefacto y destino:** página exclusiva `Inline Notifications` `175:391`, set `Inline Notification` `175:432` de AI Design System.
- **Estado histórico:** `VALIDATED` técnicamente para [INLINE-NOTIFICATION-001](../specs/components/inline-notification.contract.v0.1.0.md); Warning amber/700 quedó sustituido por la enmienda 0.1.1. Auditoría humana `PENDING`.
- **Lectura final:** cinco variantes, seis iconos Phosphor únicos entre diez instancias, seis propiedades TEXT/BOOLEAN más Type, 25/25 pinturas sólidas visibles ligadas con scope/categoría correcta y cero reacciones. Contraste mínimo de descripción 6.29:1 y de icono de estado 3.61:1.
- **Visual y cambios:** fuente y destino 650×990 comparados; geometría y color conservados con título de ejemplo corregido, falso enlace eliminado, iconografía Light/Close con rol `icon`, Warning ámbar 700 y altura por variante 104→108 por token de interlineado.
- **Mapa y QA:** [estado](../implementations/figma/inline-notification.v0.1.0.state.json), [QA-INLINE-NOTIFICATION-FIGMA-001](../qa/implementations/inline-notification.v0.1.0.figma.review.md) `PASS`, [script](../drafts/figma/inline-notification-build.v0.1.0.js).
- **Límite:** `UNPUBLISHED`; no se implementó dismiss, navegación, live region ni web.

## IMP-INLINE-NOTIFICATION-WARNING-SOURCE-COLOR-002 · Warning de origen

- **Estado:** [enmienda 0.1.1](../specs/components/inline-notification.warning-source-color-amendment.v0.1.1.md) revalidada `PASS` técnico sin nueva mutación Figma; auditoría humana `PENDING`.
- **Readback:** cinco variantes; fondos, iconos, títulos, cierres y color base de descripción coinciden con fuente. Warning icon vuelve a amber/600 `#C97B00` por variable compartida. El pseudoenlace azul sin URL permanece omitido deliberadamente. [Estado](../implementations/figma/inline-notification.warning-source-color.v0.1.1.state.json) y [QA](../qa/implementations/inline-notification.warning-source-color.v0.1.1.figma.review.md).
- **Límite:** Warning 2.96:1 `*`, no certificación WCAG, sin dismiss funcional ni publicación.

## IMP-ICON-BUTTON-BACKGROUNDS-FIGMA-001 · fondos Hover/Active de Icon Button

- **Estado:** `VALIDATED` técnicamente; auditoría humana `PENDING`.
- **Operación:** dos variables de fondo interactivas de Icon Button creadas en `semantic` con scope exclusivo `FRAME_FILL`, ocho aliases a primitivas existentes y cero diferencias contra el [JSON canónico](../drafts/foundations/ai-design-system.icon-button-backgrounds.v0.1.0.json). [Estado](../implementations/figma/icon-button-backgrounds.v0.1.0.state.json) y [QA](../qa/implementations/icon-button-backgrounds.v0.1.0.figma.review.md).
- **Límite:** el readback de Foundations no acredita aún el set consumidor ni implica publicación.

## IMP-ICON-BUTTON-FIGMA-001 · Icon Buttons 0.1.0

- **Artefacto y destino:** página exclusiva `Icon Buttons` `183:160`, set `Icon Button` `183:311` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [ICON-BUTTON-001](../drafts/contracts/icon-button.contract.v0.1.0.md); auditoría humana `PENDING`.
- **Lectura final:** 30 variantes 2×3×5, 30 Bell Phosphor y 30 Dot Count local anidados, dos propiedades Icon swap/Show count conectadas en todas las variantes, picker con 1512 component sets preferidos. 159/159 pinturas visibles ligadas, cero incompatibilidades de scope o categoría, cero reacciones.
- **Visual y cambios:** capturas fuente/destino 289×960 inspeccionadas; se conserva la matriz y geometría. Se normalizan ejes, se usan roles semánticos propios de Hover/Active y del Dot, y se omite un único efecto Focus inconsistente de la fuente. Small24 y Count4 quedan como límites de accesibilidad documentados.
- **Mapa y QA:** [estado](../implementations/figma/icon-button.v0.1.0.state.json), [QA-ICON-BUTTON-FIGMA-001](../qa/implementations/icon-button.v0.1.0.figma.review.md) `PASS`; scripts [base](../drafts/figma/icon-button-build.v0.1.0.js) y [picker](../drafts/figma/icon-button-preferred-icons.v0.1.0.js).
- **Límite:** `UNPUBLISHED`; no se implementa acción, conteo dinámico, navegación por teclado ni web.

## IMP-BREADCRUMB-CURRENT-TEXT-FIGMA-001 · texto Current semántico

- **Estado:** `VALIDATED` técnicamente; auditoría humana `PENDING`.
- **Operación:** variable `color/text/breadcrumb/current` `TEXT_FILL` creada en colección semántica con cuatro aliases a primitivas aprobadas y JSON/Figma concordantes. Cinco textos Current la consumen; Servicios sube de 3.24 a 7.20:1 sobre blanco y los otros modos conservan color. [JSON](../drafts/foundations/ai-design-system.breadcrumb-current-text.v0.1.0.json), [estado](../implementations/figma/breadcrumb-current-text.v0.1.0.state.json) y [QA](../qa/implementations/breadcrumb-current-text.v0.1.0.figma.review.md).

## IMP-BREADCRUMBS-FIGMA-001 · Breadcrumbs 0.1.0

- **Artefacto y destino:** página exclusiva `Breadcrumbs` `190:188`, set `Breadcrumb item` `190:210` y set `Breadcrumbs` `191:229` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [BREADCRUMBS-001](../drafts/contracts/breadcrumbs.contract.v0.1.0.md); auditoría humana `PENDING`.
- **Lectura final:** seis ítems y cuatro niveles, 14 instancias locales del ítem, 19 iconos Phosphor activos, 38/38 pinturas visibles ligadas con scope/categoría correcta, cinco textos Current con rol nuevo y cuatro modos con contraste ≥5.56:1. 19 textos con tipografía completa, 19 iconos dimensionados por token, cero reacciones.
- **Visual y cambios:** capturas fuente y destino inspeccionadas. Corregido clipping inicial; los textos se muestran completos en una línea. Iconos compactos 20→24 px, Inter de ejemplo→Manrope local, tracking ligado y anchos de composición 248/372/496/620 por ajuste de texto. Servicios usa orange/700 para Current; otros modos conservan su alias.
- **Mapa y QA:** [estado](../implementations/figma/breadcrumbs.v0.1.0.state.json), [QA-BREADCRUMBS-FIGMA-001](../qa/implementations/breadcrumbs.v0.1.0.figma.review.md) `PASS`; scripts [ítem](../drafts/figma/breadcrumb-item-build.v0.1.0.js), [composición](../drafts/figma/breadcrumbs-composition-build.v0.1.0.js), [ajuste de texto](../drafts/figma/breadcrumbs-text-fit.v0.1.0.js) y [binding Current](../drafts/figma/breadcrumb-current-text-bind.v0.1.0.js).
- **Límite:** dos sets `UNPUBLISHED`; no se implementa navegación, estado dinámico, teclado, responsive ni web.

## IMP-METRIC-CARD-ROLES-FIGMA-001 · colores semánticos de Metric Cards

- **Estado:** `VALIDATED` técnicamente; auditoría humana `PENDING`.
- **Operación:** dos variables en colección semántica, `TEXT_FILL` para Trend y `SHAPE_FILL` para vectores de icono, cuatro aliases por variable a primitivas existentes, JSON/Figma coincidentes. Cuatro textos y 16 vectores consumidores verificados. [Estado](../implementations/figma/metric-card-roles.v0.1.0.state.json), [QA](../qa/implementations/metric-card-roles.v0.1.0.figma.review.md).

## IMP-METRIC-CARD-FIGMA-001 · Metric Cards 0.1.0

- **Artefacto y destino:** página exclusiva `Metric Cards` `202:208`, set `Metric Card` `202:327` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [METRIC-CARD-001](../drafts/contracts/metric-card.contract.v0.1.0.md); auditoría humana `PENDING`.
- **Lectura final:** ocho variantes 4×2, 16 iconos Phosphor reales, 36 textos y 70/70 pinturas visibles ligadas; cero incompatibilidades de categoría/scope, cero reacciones. Títulos, visibilidades, swaps y contenido numérico conectados a propiedades.
- **Visual y cambios:** fuente y destino 806×935 comparados. Se restauró la alineación superior de V1/V2 y el importe ejemplo Horizontal; V1 subió cinco píxeles de alto para interlineado de tendencia y Title V1 Small pasó 18→20 por token semántico. Servicios usa orange/700 solo en los nuevos roles de texto/icono.
- **Mapa y QA:** [estado](../implementations/figma/metric-card.v0.1.0.state.json), [QA-METRIC-CARD-FIGMA-001](../qa/implementations/metric-card.v0.1.0.figma.review.md) `PASS`; scripts [base](../drafts/figma/metric-card-build.v0.1.0.js) y [corrección](../drafts/figma/metric-card-visual-correction.v0.1.0.js).
- **Límite:** `UNPUBLISHED`; no se implementa navegación, actualización de datos, formato monetario ni frontend.

## IMP-CHART-COLORS-FIGMA-001 · colores semánticos de Charts

- **Estado:** `VALIDATED` técnicamente; auditoría humana `PENDING`.
- **Operación:** siete variables de Charts en colección semántica, una `FRAME_FILL` y seis `SHAPE_FILL`; cuatro aliases a primitivas existentes por variable y JSON/Figma coincidentes. 33 pinturas consumidoras ligadas, cuatro en swatches ocultos por defecto. [Estado](../implementations/figma/chart-colors.v0.1.0.state.json), [QA](../qa/implementations/chart-colors.v0.1.0.figma.review.md).

## IMP-CHARTS-FIGMA-001 · Charts 0.1.0

- **Artefacto y destino:** página exclusiva `Charts` `210:122`, sets `Chart Legend Label` `210:145`, `Chart Cell` `210:171`, `Progress Chart Item` `213:161`, `Semi-donut Gauge` `211:134` y main `Chart Header` `213:162`.
- **Estado:** `VALIDATED` técnicamente para [CHARTS-001](../drafts/contracts/charts.contract.v0.1.0.md); auditoría humana `PENDING`, `UNPUBLISHED`.
- **Lectura final:** 23 definiciones, nueve instancias locales de leyenda, seis vectores, 28/28 textos con tipografía completa, 76/76 pinturas sólidas ligadas —72 visibles por defecto—, cero incompatibilidades de scope/categoría y cero reacciones. Seis paths conservan comandos y geometría fuente con normalización numérica máxima de 0.0000002385 px.
- **Visual y cambios:** capturas fuente/destino inspeccionadas. Avance Gauge más oscuro para distinguirlo de pista, swatch neutro y segunda serie más visibles, Header +1 px, Title corregido, padding central de Cell 6 px literal por ausencia de token. La muestra `80%` no se interpreta como cálculo de las barras.
- **Mapa y QA:** [estado](../implementations/figma/charts.v0.1.0.state.json), [QA-CHARTS-FIGMA-001](../qa/implementations/charts.v0.1.0.figma.review.md) `PASS`; scripts [base](../drafts/figma/charts-foundation-build.v0.1.0.js), [Gauge](../drafts/figma/chart-gauge-build.v0.1.0.js), [Progress/Header](../drafts/figma/chart-progress-header-build.v0.1.0.js) y [auditoría](../drafts/figma/charts-final-qa.v0.1.0.js).
- **Límite:** sin datos dinámicos, semántica funcional de gráfico, responsive ni frontend.

## IMP-LINEAR-PROGRESS-COLORS-FIGMA-001 · colores semánticos de Linear Progress Bar

- **Estado:** `VALIDATED` técnicamente; auditoría humana `PENDING`.
- **Operación:** cinco variables locales `color/background/progress/*`, solo `FRAME_FILL`, veinte aliases a primitivas existentes en cuatro modos y paridad exacta con [JSON canónico](../drafts/foundations/ai-design-system.linear-progress-colors.v0.1.0.json). 96 pinturas de frame consumidoras verificadas; cero cruces de scope/categoría. [Estado](../implementations/figma/linear-progress-colors.v0.1.0.state.json) y [QA](../qa/implementations/linear-progress-colors.v0.1.0.figma.review.md).

## IMP-LINEAR-PROGRESS-BAR-FIGMA-001 · Linear Progress Bar 0.1.0

- **Artefacto y destino:** página exclusiva `Linear Progress Bars` `220:122`, set `Linear Progress Bar` `220:460` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [LINEAR-PROGRESS-BAR-001](../drafts/contracts/linear-progress-bar.contract.v0.1.0.md); auditoría humana `PENDING`, `UNPUBLISHED`.
- **Lectura final:** 48 combinaciones únicas, texto de porcentaje y ancho de barra sincronizados, 96/96 pinturas de fondo y 144/144 de texto con roles semánticos correctos, 144 textos con tipografía completa, 240 referencias de propiedades, cero incompatibilidades y cero reacciones.
- **Visual y cambios:** capturas fuente/destino 1034×1402 inspeccionadas. 36 porcentajes fuente discordantes corregidos; pista literal y rellenos iconográficos sustituidos por fondos semánticos; Medium/Large +1 px, Servicios Primary orange/600 para contraste y Middle→Medium.
- **Mapa y QA:** [estado](../implementations/figma/linear-progress-bar.v0.1.0.state.json), [QA-LINEAR-PROGRESS-BAR-FIGMA-001](../qa/implementations/linear-progress-bar.v0.1.0.figma.review.md) `PASS`; scripts [construcción](../drafts/figma/linear-progress-bar-build.v0.1.0.js) y [auditoría](../drafts/figma/linear-progress-bar-final-qa.v0.1.0.js).
- **Límite:** sin valores continuos, animación, accesibilidad programática ni frontend.

## IMP-SELECTION-CONTROL-SOURCE-COLOR-002 · borde original de Checkbox y Radio Button

- **Estado:** `PASS` técnico acotado; [QA de readback](../qa/implementations/selection-control-source-color.v0.1.1.figma.review.md). Auditoría humana `PENDING`; ambos sets `UNPUBLISHED`.
- **Operación:** variable existente `color/border/control` `VariableID:123:122` cambia sus cuatro aliases de neutral/500 a `color/neutral/400` `VariableID:8:96`; cero variables, nodos o primitivas creados.
- **Consumidores comprobados:** Checkbox `149:182`, `149:192`; Radio Button `I143:148;142:137`, todos resuelven `#94A3B8` y conservan binding `STROKE_COLOR`. `color/background/control-hover` no cambió; Toggle tiene cero consumidores del rol modificado. Capturas posteriores de ambos sets inspeccionadas.
- **Límite:** contraste original ~2.56:1 `*`; anatomía y tipografía normalizadas siguen documentadas y pendientes de cotejo transversal.

## IMP-NAVIGATION-SWITCH-TAB-ITEM-FIGMA-001 · Switch Tab Item

- **Artefacto y destino:** página `Navigation` `275:122`, set `Switch Tab Item` `276:395` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [NAVIGATION-SWITCH-TAB-ITEM-001](../specs/navigation-switch-tab-item.contract.v0.1.0.md); auditoría humana `PENDING`, `UNPUBLISHED`.
- **Lectura final:** tres variantes, seis propiedades, icono y Dot Count anidados. [Estado](../implementations/figma/navigation-switch-tab-item.v0.1.0.state.json) y [QA](../qa/implementations/navigation-switch-tab-item.v0.1.0.figma.review.md).

## IMP-NAVIGATION-TAB-COLORS-FIGMA-001 · fondo activo de Switch Tab Item

- **Estado:** `VALIDATED` técnicamente; auditoría humana `PENDING`, `UNPUBLISHED`.
- **Operación:** `color/background/navigation-tab-active` en scope `FRAME_FILL`, cuatro aliases a primitivas aprobadas. [JSON](../drafts/foundations/ai-design-system.navigation-tab-colors.v0.1.0.json) y [QA](../qa/implementations/navigation-tab-colors.v0.1.0.figma.review.md).

## IMP-NAVIGATION-SWITCH-TAB-FIGMA-001 · Switch Tab

- **Artefacto y destino:** página `Navigation` `275:122`, componente `Switch Tab` `283:128` con cuatro instancias de Switch Tab Item.
- **Estado:** `VALIDATED` técnicamente para [NAVIGATION-SWITCH-TAB-001](../specs/navigation-switch-tab.contract.v0.1.0.md); auditoría humana `PENDING`, `UNPUBLISHED`.
- **Lectura final:** 488×46 px, bindings de fondo y geometría locales, cuatro estados de ítem como ejemplo. [Estado](../implementations/figma/navigation-switch-tab.v0.1.0.state.json) y [QA](../qa/implementations/navigation-switch-tab.v0.1.0.figma.review.md).

## IMP-NAVIGATION-PAGINATION-BORDER-FIGMA-001 · borde semántico de Pagination

- **Estado:** `VALIDATED` técnicamente; auditoría humana `PENDING`, `UNPUBLISHED`.
- **Operación:** un rol `STROKE_COLOR` con cuatro aliases a primitivas locales; JSON/Figma sincronizados. [JSON](../drafts/foundations/ai-design-system.navigation-pagination-border.v0.1.0.json) y [QA](../qa/implementations/navigation-pagination-border.v0.1.0.figma.review.md).

## IMP-NAVIGATION-PAGINATION-FIGMA-001 · Pagination

- **Artefacto y destino:** página `Navigation` `275:122`, set `Pagination` `297:454` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [NAVIGATION-PAGINATION-001](../specs/navigation-pagination.contract.v0.1.0.md); auditoría humana `PENDING`, `UNPUBLISHED`.
- **Lectura final:** cinco variantes 354×66, siete propiedades, 25 Caret, 125/125 pinturas con variables locales y cero reacciones. [Estado](../implementations/figma/navigation-pagination.v0.1.0.state.json) y [QA](../qa/implementations/navigation-pagination.v0.1.0.figma.review.md).

## IMP-NAVIGATION-TAB-BORDERS-FIGMA-001 · bordes semánticos de Tab

- **Estado:** `VALIDATED` técnicamente; auditoría humana `PENDING`, `UNPUBLISHED`.
- **Operación:** dos roles `STROKE_COLOR` con aliases a primitivas locales y paridad JSON/Figma. [JSON](../drafts/foundations/ai-design-system.navigation-tab-borders.v0.1.0.json) y [QA](../qa/implementations/navigation-tab-borders.v0.1.0.figma.review.md).

## IMP-NAVIGATION-TAB-FIGMA-001 · Tab

- **Artefacto y destino:** página `Navigation` `275:122`, set `Tab` `316:200` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [NAVIGATION-TAB-001](../specs/navigation-tab.contract.v0.1.0.md); auditoría humana `PENDING`, `UNPUBLISHED`.
- **Lectura final:** 17 variantes, diez propiedades, 33 iconos, 16 Dot, ocho divisores, 107/107 pinturas con variables locales y cuatro reacciones hover. Alineación interna de Dynamic/Off/Hovered corregida y verificada. [Estado](../implementations/figma/navigation-tab.v0.1.0.state.json) y [QA](../qa/implementations/navigation-tab.v0.1.0.figma.review.md).

## IMP-SCROLLBAR-COLORS-FIGMA-001 · gris fuente y rol de thumb

- **Estado:** `VALIDATED` técnicamente en versión 0.1.1; auditoría humana `PENDING`, biblioteca `UNPUBLISHED`. La versión 0.1.0 con primitiva nueva es histórica.
- **Operación vigente:** `color/background/scrollbar/thumb` mantiene scope `SHAPE_FILL` y aliasa la primitiva existente neutral/300 en cuatro modos. La primitiva 350 ya no aparece en el inventario local. [JSON 0.1.1](../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.1.json) y [QA](../qa/implementations/scrollbar-colors.v0.1.1.figma.review.md) verifican 30 consumidores y la diferencia cromática.

## IMP-SCROLLBAR-FIGMA-001 · Scrollbar

- **Artefacto y destino:** página `Scrollbars` `328:122`, set público `Scrollbar` `330:194` y cuatro sets internos `329:138`, `330:151`, `330:160`, `330:169` en AI Design System.
- **Estado:** `VALIDATED` técnicamente para [SCROLLBAR-001](../specs/scrollbar.contract.v0.1.0.md) con [enmienda 0.1.1](../specs/scrollbar.color-approximation.amendment.v0.1.1.md); auditoría humana `PENDING`, biblioteca `UNPUBLISHED`.
- **Lectura final:** ocho variantes públicas, 22 internas, ocho instancias locales anidadas, 30/30 thumbs ligados al rol semántico, alias neutral/300 en cuatro modos y cero reacciones. Geometría pública conservada; color destino más claro por instrucción posterior. [Estado vigente](../implementations/figma/scrollbar.v0.1.1.state.json) y [QA](../qa/implementations/scrollbar.v0.1.1.figma.review.md); [estado 0.1.0](../implementations/figma/scrollbar.v0.1.0.state.json) histórico `STALE` para color.

## IMP-STEPS-FIGMA-001 · Steps

- **Artefacto y destino:** página `Steps` `341:122`, set público `Steps` `343:212`, internos `Steps Dot` `342:139` y `Steps Combination` `342:445` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [STEPS-001](../specs/steps.contract.v0.1.0.md) con [enmienda de marca 0.1.1](../specs/steps.brand-theme.amendment.v0.1.1.md); auditoría humana `PENDING`, biblioteca `UNPUBLISHED`.
- **Lectura final:** 6+4+27 variantes, 27/27 combinaciones correctas, 173/173 pinturas vinculadas, siete roles semánticos con 28/28 aliases verificados y tres acentos temáticos con 33 consumidores, sin variables/primitivas nuevas en esta corrección. [Estado vigente](../implementations/figma/steps.v0.1.1.state.json) y [QA](../qa/implementations/steps.v0.1.1.figma.review.md) documentan el cambio; [estado 0.1.0](../implementations/figma/steps.v0.1.0.state.json) histórico `STALE` para color. AUD-008 permanece.

## IMP-STEPPER-FIGMA-001 · Stepper Item

- **Artefacto y destino:** página `Steppers` `347:122`, set público `Stepper Item` `350:347` y set interno `Stepper Connector` `348:138` de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [STEPPER-001](../specs/stepper.contract.v0.1.0.md) con [enmienda de marca 0.1.1](../specs/stepper.brand-theme.amendment.v0.1.1.md); auditoría humana `PENDING`, biblioteca `UNPUBLISHED`.
- **Lectura final:** 18+8 variantes, seis propiedades de contenido/visibilidad/icono probadas, 122/122 pinturas con variables locales del scope correcto. Los tres roles de acento tienen doce aliases iguales a marca base/fuerte por tema, sin variables/primitivas nuevas. [Estado vigente](../implementations/figma/stepper.v0.1.1.state.json) y [QA](../qa/implementations/stepper.v0.1.1.figma.review.md) documentan el cambio intencional; [estado 0.1.0](../implementations/figma/stepper.v0.1.0.state.json) histórico `STALE` para color. AUD-009 y Caption `*` permanecen.

## IMP-LOADER-FIGMA-001 · Loader

- **Artefacto y destino:** página `Loaders` `377:122`, set público `Loader` `378:1869` y 16 sets internos ocultos de AI Design System.
- **Estado:** `VALIDATED` técnicamente para [LOADER-001](../specs/loader.contract.v0.1.0.md); auditoría humana `PENDING`, biblioteca `UNPUBLISHED`.
- **Lectura final:** 16 variantes públicas, 384/384 fotogramas, 384/384 transiciones, 384/384 stops opacos y 384/384 remates ligados a roles semánticos locales. Sin variables ni primitivas nuevas; el color se conserva durante cada ciclo. [Estado](../implementations/figma/loader.v0.1.0.state.json) y [QA](../qa/implementations/loader.v0.1.0.figma.review.md) documentan los IDs y límites.

## IMP-SEARCH-FIGMA-001 · Search

- **Destino:** AI Design System / Input Fields 394:122 / set 418:263, 12 variantes. [Contrato](../specs/search.contract.v0.1.0.md).
- **Estado:** VALIDATED técnico; [QA](../qa/implementations/search.v0.1.0.figma.review.md) PASS, auditoría humana PENDING, biblioteca UNPUBLISHED.
- **Lectura:** 82 paints, 3 efectos, 120 bindings tipográficos y 54 referencias de propiedades, incluidos ocultos. [IDs y mapa origen/destino](../implementations/figma/search.v0.1.0.state.json). Sin cambios a Input Field ni nuevas variables.

## IMP-TEXTAREA-FIGMA-001 · Textarea

- **Destino:** AI Design System / Input Fields 394:122 / set 419:247, 4 variantes. [Contrato](../specs/textarea.contract.v0.1.0.md).
- **Estado:** VALIDATED técnico; [QA](../qa/implementations/textarea.v0.1.0.figma.review.md) PASS, auditoría humana PENDING, biblioteca UNPUBLISHED.
- **Lectura:** 29 paints, 0 efectos, 80 bindings tipográficos y 32 referencias de propiedades, incluidos ocultos. [IDs y mapa origen/destino](../implementations/figma/textarea.v0.1.0.state.json). Sin cambios a Input Field ni nuevas variables.

## IMP-FILE-UPLOAD-FIGMA-001 · File Upload

- **Destino:** AI Design System / Input Fields 394:122 / set 420:320, 6 variantes. [Contrato](../specs/file-upload.contract.v0.1.0.md).
- **Estado:** VALIDATED técnico; [QA](../qa/implementations/file-upload.v0.1.0.figma.review.md) PASS, auditoría humana PENDING, biblioteca UNPUBLISHED.
- **Lectura:** 78 paints, 0 efectos, 160 bindings tipográficos y 72 referencias de propiedades, incluidos ocultos. [IDs y mapa origen/destino](../implementations/figma/file-upload.v0.1.0.state.json). Sin cambios a Input Field ni nuevas variables.

## IMP-INPUT-FIELD-FIGMA-001 · Input Field

- **Actualización vigente 0.1.1:** [estado](../implementations/figma/input-field.v0.1.1.state.json) y [QA](../qa/implementations/input-field.v0.1.1.figma.review.md) VALIDATED para base + enmienda Disabled aprobada. Tres textos Filled/Disabled ahora ligados a color/text/disabled; seis Disabled consistentes. IDs/propiedades/geometría intactos. La lectura 0.1.0 inferior es histórica para esos tres fills.

- **Destino:** AI Design System, página Input Fields 394:122, set Input Field 397:152; 30 variantes y doce propiedades de contenido/composición.
- **Estado:** VALIDATED técnico para [INPUT-FIELD-001](../specs/input-field.contract.v0.1.0.md), auditoría humana PENDING, biblioteca UNPUBLISHED.
- **Lectura final:** 487 nodos, 306/306 paints, 14/14 efectos, 750 bindings tipográficos, 360 referencias de propiedades y 60 instancias iconográficas. Edición, visibilidad y ancho 320 px comprobados; seis soportes de foco conservan el render fuente. Cero tokens o primitivas nuevos.
- **Trazabilidad:** [estado e IDs base](../implementations/figma/input-field.v0.1.0.state.json), [QA base](../qa/implementations/input-field.v0.1.0.figma.review.md), [132 aliases](../qa/implementations/input-field.v0.1.0.alias-parity.json). El set fuente no se modificó. Search/Textarea/File Upload tienen entradas propias VALIDATED; no deben reconstruirse de nuevo.

## Chat Toolbar y dependencias · cierre2026-10-08

VALIDATED para contrato visual v0.1.0. Chat783:6; Toolbar798:284 (2), Tool Item796:494 (3), History Item796:495 (4); muestra798:290. [Readback](../qa/implementations/chat-toolbar.v0.1.0.final.json), [QA](../qa/implementations/chat-toolbar.v0.1.0.review.md), [contrato](../specs/chat-toolbar.contract.v0.1.0.md). Sin variables nuevas; fuente y principales reutilizados intactos. Publicación remota NOT_PERFORMED; no implementación frontend.

## IMP-FUENTES-FIGMA-001 · 2026-10-09

VALIDATED del [contrato visual](../specs/components/fuentes.contract.v0.1.0.md), con limitaciones de accesibilidad documentadas. AI DS/Fuentes847:7/set848:41; Default848:11, Hover848:26, Path Item848:8; revisión848:42. [Estado](../implementations/figma/fuentes.v0.1.0.state.json) y [QA](../qa/implementations/fuentes.v0.1.0.review.md).22 paints, cuatro temas, Slot probado0/1/2/4 y long150. Una variable semántica nueva, cero primitivas. Biblioteca NOT_PERFORMED; humana PENDING.


## Conversation Composer Slot · 2026-10-20

IMP-CONVERSATION-COMPOSER-013 · Slot Notice content1103:192 en principal765:397; instancia766:246 vinculada. [Estado](../implementations/figma/conversation-composer.v0.1.3.state.json), [QA PASS](../qa/implementations/conversation-composer.v0.1.3.review.md). Figma y web local VALIDATED solo para este alcance. Draft/Tools y muestra original preservados; pruebas temporales eliminadas.

user_audit: NOT_REQUIRED; human_review_policy: OPTIONAL_NON_BLOCKING.
