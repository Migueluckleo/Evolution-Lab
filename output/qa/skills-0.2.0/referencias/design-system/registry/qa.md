# Registro de QA

## QA-WEB-CONTRACT-AUDIT-013 · 2026-10-13

[Reporte0.1.3](../qa/implementations/web.contract-audit.v0.1.3.review.md), [matriz43](../qa/implementations/web-contract-audit-2026-10-13/family-matrix.md) y [resultados](../qa/implementations/web-contract-audit-2026-10-13/results.json):43 familias cotejadas con valores esperados explícitos por caso/tema y capturas inspeccionadas.725 fixtures×4 temas,59 pruebas de navegador y9 unitarias; build/TypeScript/generación comprobados. No se certifican cada píxel ni combinaciones arbitrarias. El rechazo inicial de extracción de raster Modal se resolvió tras autorización explícita: ambos originales están copiados, sus hashes coinciden y las variantes se revalidaron con las imágenes presentes. Fuente normativa, evidencia OBSERVED y adaptación web diferenciadas.

## QA-WEB-FIDELITY-012 · 2026-10-13

[QA0.1.2](../qa/implementations/web.fidelity.v0.1.2.review.md) y [resultados](../qa/implementations/web-fidelity-2026-10-13/results.json): PASS de generación43 familias,8 pruebas de código, TypeScript, build y15 pruebas Chrome.442 referencias sin errores/assets rotos; Sidebar22 recetas×4 temas, geometría de campos/cards/modal/scrollbar/charts/table/header/shell/toolbar y regresión BENI. [Matriz por familia](../qa/implementations/web-fidelity-2026-10-13/family-matrix.md) distingue medidas de revisión/render. No comparación por píxel de todas las combinaciones ni auditoría WCAG global. Las diferencias de adaptación corregidas0.1.0 quedan históricas; excepciones normativas y auditoría Figma sin cambios.

## QA-WEB-CHARACTERS-011 · 2026-10-13

[Reporte](../qa/implementations/web.characters.v0.1.1.review.md) y [resultados](../qa/implementations/web.characters.v0.1.1.results.json): corrección de doble traslación de los ojos de BENI/NAVI. 8 pruebas React/generación y build PASS; 2 pruebas Chrome PASS; geometría verificada de 64 vectores, 47 paths pintados y 13 frames. Capturas web comparadas con Figma existente; colores/proporciones preservados. Alcance estático, sin afirmar animación o accesibilidad global.

## QA-WEB-COMPONENTS-001 · 2026-10-13

[Reporte](../qa/implementations/web.v0.1.0.review.md) y [resultados/hashes](../qa/implementations/web.v0.1.0.results.json): 43 familias con código/API/ficha/ejemplo; TypeScript, 7 pruebas y build estático PASS; 6 recorridos de navegador PASS, incluida pantalla sin backend y temas. Gate de documentación comprobado por alteración temporal/restauración. Inspección visual acotada y límites explícitos. Logos PARTIAL_ASSETS 64/72 por límite Figma. No QA visual global ni aprobación humana simulada.

## QA-ARTIFACT-RETENTION-001 · 2026-10-13

[Reporte](../qa/tooling/retention.2026-10-13.review.md), [manifiesto por archivo](../qa/tooling/retention.2026-10-13.manifest.json) y [resultados del índice](../qa/tooling/retention.2026-10-13.results.json): PASS en restauración de 673 derivados, comparación local, bajas exactas del índice y conservación de 1,187 fuentes/evidencias/entregables. Reducción de 151,743,579 bytes lógicos del índice; no es reducción de historia ni de disco. Cierre Graphify independiente conforme a P05; no QA Figma nuevo.

## QA-PROJECT-TOOLING-001 · 2026-10-13

[QA local de herramientas](../qa/tooling/project-tooling.2026-10-13.review.md): controles documentales deterministas, resolución conservadora de bases/enmiendas, protección de fuentes y publicación con recuperación. Pruebas de regresión ejecutadas; grafo/vista requieren además los gates finales descritos en el reporte. No representa QA visual nuevo, aprobación contractual ni publicación de biblioteca.

## QA-CHAT-LAYOUT-001 · 2026-10-09

[Revisión](../qa/implementations/chat-layout.v0.1.1.review.md):478 nodos recorridos,84 registros de layout,40 Slots sin violaciones actuales. Verificador read-only PASS: cinco definiciones de spacing/20 aliases y hash JSON canónico sin cambio. QA interactivo/overflow PARTIAL, no ejecutado.358px solo en muestras frente a574 en principales, description542 desfasada y Messages VERTICAL sin clipping documentados; no reparaciones ni aprobación humana ficticia. [Contrato](../specs/components/chat.layout.amendment.v0.1.1.md).

## QA-CHARACTERS-001 · 2026-10-08

[Documental](../qa/contracts/characters.v0.1.0.review.md) y [técnico](../qa/implementations/characters.v0.1.0.review.md) PASS; [readback](../qa/implementations/characters.v0.1.0.audit.json).64 paths round-trip,13 frames,47 bindings,4 temas,2 pruebas escala. Fallos iniciales de igualdad textual/float conservados y explicados. No certificación perceptual/WCAG.

## QA-CHAT-SECTION-001 · 2026-10-08

[Documental](../qa/contracts/chat-section.v0.1.0.review.md) y [técnico](../qa/implementations/chat-section.v0.1.0.review.md) PASS para integración visual delegada0.1.0.39 roles/156 aliases y tres identidades frente al JSON;62 pinturas/13 textos visibles sin errores de bindings; Slots0/1/3/5 y conservación de overrides. Readback asentado de crecimiento hasta1093.74/930px. Contraste de sugerencias* preservado, sin WCAG PASS. Seis Count Small ocultos heredados. Cleanup de fixtures propio comprobado; biblioteca no publicada por este lote.

## QA-CONVERSATION-CHARACTERS-011 · 2026-10-08

[Documental](../qa/contracts/conversation.characters.v0.1.1.review.md) y [técnico](../qa/implementations/conversation.characters.v0.1.1.review.md) PASS acotados: JSON/Figma iguales, personajes fijos en cuatro temas y fuente original exacta; no alias semántico ni cambio de geometría. Los QA0.1.0 sobre color temático de personajes quedan sustituidos, no borrados.

## QA-CONVERSATION-001 · 2026-10-08

[QA documental](../qa/contracts/conversation.v0.1.0.review.md) y [técnico](../qa/implementations/conversation.v0.1.0.review.md) PASS acotados.124 pinturas locales con scope correcto,40 roles/38 primitivas/160 aliases verificados;216 resoluciones en cuatro temas. Doce Slots probados desde instancias, BENI→NAVI conserva Body, vista360px sin desbordes. Nueve Count Small ocultos conservan excepción Dot; contraste Servicios3.236:1* y bordes bajos explícitos. No nuevas variables ni WCAG PASS. Auditoría PENDING y sin publicación de biblioteca.

## QA-FIGJAM-SDD-FLOW-2026-10-07

[Revisión del tablero explicativo](../qa/implementations/figjam-sdd-flow.2026-10-07.review.md) PASS documental/estructural/visual acotado. Diez secciones, ocho flujos, 149/149 relaciones preservadas; cero extremos discrepantes, desbordes y solapamientos de contenido. Síntesis sustentada en 17 archivos con digests. No revalida componentes ni aprueba excepciones. Originales y boceto histórico conservados; sin bloqueo pendiente de la entrega.

## QA-APP-SHELL-001 · 2026-10-06

[Documental](../qa/contracts/app-shell.v0.1.0.review.md) y [Figma](../qa/implementations/app-shell.v0.1.0.figma.review.md) PASS para envoltura App Shell y dependencias consumidas, no QA global de familias.12casos desktop/Content, edición/reset sin detach, cuatro temas,60/60pinturas con scopes compatibles y93/93definiciones canónicas. Readback independiente y captura revisada. Limitaciones de contraste/Logos heredadas no se cierran ni generan nuevas tareas. Sin publicación remota, humana PENDING.

## QA-ANTICIPA-SCREEN-COMPOSITION-001 · 2026-10-06

[Revisión](../qa/contracts/anticipa-screen-composition.v0.1.0.review.md): PASS de consistencia documental del candidato con límites, no READY para construir. [Verificación local](../qa/contracts/anticipa-screen-composition.v0.1.0.verification.json): estructura, enlaces, IDs fuente,30 digests directos,37 referencias semánticas y270 variables/512 aliases del inventario base. DRAFT, sin adopción de propuestas; nuevo QA Figma/funcional NOT_RUN. Fuentes, specs, inventario y grafo preservados; no cambios cromáticos ni capacidades inventadas.

## QA-SPECS-PROMOTION-20261006 · 2026-10-06

[Verificación administrativa](../qa/contracts/specs-promotion.2026-10-06.review.md) de19 promociones respaldadas por QA documental/técnico existente. No se repitió auditoría Figma. [Resultado local](../qa/contracts/specs-promotion.2026-10-06.verification.json): hashes, enlaces, estado, referencias y originales conservados. PASS de publicación documental acotada, no aprobación humana ni cierre global de Tooltip/Toggle/Avatar/Logos. QA históricos intactos; sus alcances sustituidos siguen históricos.

## QA-LOGOS-REFINEMENT-001 · 2026-10-06

[Informe](../qa/implementations/logos.refinement.v0.1.1.review.md): seis sets/72 variantes/2967 nodos, cero bindings, cuatro dependencias locales. Personas exacto;57 diferencias geométricas hasta0.00030517578125px en otros cinco sets. Pruebas temporales retiradas y principales sin cambios. QA global no aprobado: requiere decisión explícita sobre esos deltas, no una nueva ronda técnica. [QA de alcance](../qa/contracts/logos.scope.v0.1.1.review.md) PASS documental únicamente. Sin publicación.

## QA-RADIO-CHECKBOX-REFINEMENT-001 · 2026-10-06

[QA documental](../qa/contracts/radio-checkbox.refinement.v0.1.2.review.md) y [QA implementación](../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md) PASS técnico:40 etiquetas,200 bindings tipográficos,22 definiciones/88 modos,80 combinaciones de etiquetas y20 cambios de variante. Solo ocho coordenadas Checkbox corregidas; no regresión leída. Capturas revisadas; pruebas temporales retiradas. Excepciones y auditoría humana PENDING separadas; no publicación.

## QA-SIX-FAMILY-COLOR-001 · 2026-10-05

PASS documental e implementación **solo en alcance cromático**. [Informe](../qa/implementations/six-families.color.v0.1.0.review.md), [readback consolidado](../qa/implementations/six-families.color.v0.1.0.verification.json).832 pinturas,84 definiciones canónicas, cero errores de scope/categoría/remotos;179 definiciones con geometría/API intactas.42 bindings modificados;48 aliases de extensión verificados, cuatro roles nuevos y ocho existentes corregidos. Gris Charts aproximado y12 pinturas adicionales de Slots explican las diferencias frente a fuente. Auditoría humana PENDING; sin publicación remota.

## Conciliación de pendientes · 2026-10-05

PASS documental acotado para separar estados vigentes de cortes históricos. Se contrastaron MIGRATION-TRACEABILITY-STATUS, MIGRATION-AUDIT, contratos, registro Slots y los QA existentes de Chips, Buttons, Search, Header, Tooltip, Toggle, Avatar y Logos. Se corrigieron referencias operativas Search0.1.0, Slots Sidebar/Empty states y la integración de logos en Header sin editar contratos normativos ni resultados históricos.

La lista consolida ocho familias con revisión técnica restante, QA parcial de seis sets de Logos y excepciones de equipo. No declara esas familias defectuosas, ni reabre doce logos omitidos. QA de Slots cerrado en la cola registrada. Alcance local documental únicamente: no lectura/escritura Figma, no nuevo PASS cromático y no publicación. [Lista y límites](../specs/MIGRATION-TRACEABILITY-STATUS.md).

## QA-FILTER-CHIP-SEMANTIC-021 · 2026-10-05

[Documental](../qa/contracts/filter-chip.semantic.v0.2.1.review.md) y [Figma](../qa/implementations/filter-chip.semantic.v0.2.1.figma.review.md) PASS: 36 bindings corregidos, 126 paints, 47 definiciones canónicas y nueva extensión comprobados. 18 variantes/75 paints comparables iguales a fuente; 12 derivadas conservadas. 30 variantes/181 nodos sin cambios visuales. No aprobación WCAG ni publicación.

## QA-BUTTON-LOCAL-BINDINGS-022 · 2026-10-05

[Documental](../qa/contracts/button.local-bindings.v0.2.2.review.md) y [Figma](../qa/implementations/button.local-bindings.v0.2.2.figma.review.md) PASS acotados. 722/722bindings,36aliases por modo, cero remotos/no resolubles y cero píxeles cambiados. Ocho raíces consumidoras/control sin regresiones; 60IDs/variantes intactos. No QA cromático global ni auditoría humana. [Verificación](../qa/implementations/buttons.local-bindings.v0.2.2.verification.json).

## QA-SEARCH-011 · 2026-10-05

[QA documental0.1.1](../qa/contracts/search.v0.1.1.review.md) y [correspondencia Figma0.1.1](../qa/implementations/search.v0.1.1.figma.review.md): PASS acotado. DOC-SEARCH-001 CLOSED,12 variantes y22 variables locales comprobadas. No cambios Figma ni repetición de QA completo de temas/contraste/visual. Los párrafos cruzados de QA0.1.0 quedan sustituidos, no sus evidencias originales.

Buttons: el [descubrimiento](../qa/implementations/buttons.refinement.v0.1.0.discovery.json) confirmó722 referencias a nueve variables remotas. Hallazgo cerrado posteriormente por QA-BUTTON-LOCAL-BINDINGS-022; el descubrimiento histórico no equivale al QA de corrección.

## QA-EMPTY-STATES-001 · 2026-10-05

[Documental](../qa/contracts/empty-states.v0.1.0.review.md) y [Figma](../qa/implementations/empty-states.v0.1.0.figma.review.md) PASS acotado.64operacionesSlots,16transiciones que conservan contenido/orden/texto; cuatro pruebasresponsive y cuatro swaps/visibilidad.108paints efectivos,31roles/124aliases,264comparaciones de tema sin discrepancias. IDs efímeros ytexto oculto de pruebas iniciales explicados en QA; no se ocultaron fallos históricos. Servicios3.236:1*, sin WCAGPASS.

## QA-SIDEBAR-001 · 2026-10-05

[Documental](../qa/contracts/sidebar.v0.1.0.qa.md) y [técnico](../qa/implementations/sidebar.v0.1.0.figma.review.md) PASS acotado.141paints,42variables,576comparaciones,16checksSlots y16texto largo; cero scopes incorrectos y referencias externas. Contraste original limitado explícito; no WCAGPASS ni aprobación humana.

## QA-MODAL-001 · 2026-10-01

[Documental](../qa/contracts/modal.v0.1.0.review.md) y [técnico](../qa/implementations/modal.v0.1.0.figma.review.md) PASS acotado.25pruebas de composición,123paints efectivos,53textos con bindings completos,34 tokens/136 aliases y392comparaciones de cuatrotemas sin errores. Imágenes originales conservadas. Excepciones de tipografía y contraste explícitas; sin afirmarWCAG ni aprobaciónhumana.

## QA-TABLE-001 · 2026-10-01

[Documental](../qa/contracts/table.v0.1.0.review.md) y [técnico](../qa/implementations/table.v0.1.0.figma.review.md) PASS acotado:27checks,899paints semánticos,36tokens/144aliases y cuatrotemas. Hover+8px, negro→neutral900, divisor1.233:1* y320pxUNSUPPORTED explícitos. Metadatos fuenteparciales no se califican como extracción completa. No WCAGniaprobaciónhumana.

## QA-HEADER-001 · 2026-10-01

[QA documental](../qa/contracts/header.v0.1.0.review.md) y [QA técnico](../qa/implementations/header.v0.1.0.figma.review.md) PASS acotado. [Evidencia estructurada](../qa/implementations/header.v0.1.0.final.json): scopes correctos, aliases canónicos, pruebas Slots y temas. No WCAG PASS ni aprobación humana. Mantener limitaciones de contraste y geometría documentadas; no altera QA pendiente de otras familias.

## QA-GRAPH-REFRESH-2026-10-01

2026-10-01 · Actualización del índice y conciliación documental bajo DEC-GRAPH-REFRESH-2026-10-01. PASS acotado a cobertura/integridad del grafo, lectura de outputs, recuperación de fuentes recientes y hashes del manifiesto; [cifras y comprobaciones](../graphify-out/runs/2026-10-01/verification.json), [manifiesto](../graphify-out/runs/2026-10-01/manifest-check.json). Se conserva el respaldo anterior y el historial. Se corrigió únicamente una ruta relativa rota en QA-ICON-BUTTON-CONTRACT-001; no cambia su resultado histórico.

Hallazgo separado **DOC-SEARCH-001**: el contrato Search0.1.0 y sus QA mezclan cláusulas File Upload/Textarea. Se reabre la revisión documental de esas cláusulas en [auditoría](../specs/MIGRATION-AUDIT.md), sin nuevo readback ni cambios Figma, y sin inferir que el componente esté mal construido. Este PASS del grafo no cierra ese CONFLICT, las revisiones cromáticas anteriores ni la auditoría humana.

## QA-COMPOSITION-SLOTS-002

2026-09-30 · [Documental](../qa/contracts/composition-slots.v0.1.1.review.md) y [técnico](../qa/implementations/composition-slots.v0.1.1.figma.review.md) PASS para tres regiones familiares restantes. Native SLOT, edición desde instancia, cardinalidad, variantes, largo/estrecho y cuatro temas. Pagination: 200 comparaciones RGB sin diferencias; 16 transiciones preservan ocho celdas y Disabled neutraliza activo/foco. Charts: corregido track fijo detectado en QA a 320 px. Las limitaciones constan por separado; no hay PASS global ni aprobación humana simulada.

## QA-COMPOSITION-SLOTS-001

2026-09-29 · [QA documental](../qa/contracts/composition-slots.v0.1.0.review.md) y [QA técnico](../qa/implementations/composition-slots.v0.1.0.figma.review.md) PASS acotados a Select, Switch Tab y Breadcrumbs. P-SLOTS01…09 con evidencia por control. Conteo variable, edición en consumidor enlazado, preservación de contenido entre variantes y cuatro modos. Se conserva evidencia inicial de dos fallos de layout Breadcrumbs y sus correcciones/captura posterior. JSON canónico intacto; auditoría humana PENDING. No cubre los candidatos pendientes ni certifica toda la biblioteca.

## QA-SELECT-001

2026-09-29 · SELECT-0010.1.0 · [QA documental PASS](../qa/contracts/select.v0.1.0.review.md), [QA técnico acotado PASS](../qa/implementations/select.v0.1.0.figma.review.md).70pinturas consumidoras con binding,29variables/116comparaciones por modo, dos variantes, pruebas de ancho320/464 y edición anidada. Diez etiquetas ocultas con métricas heredadas sin binding numérico y cinco fills desactivados documentados; no declaración de tokenización integral. Capturas de fuente/set/página inspeccionadas. Auditoría humana pendiente.

## QA-DROPDOWN-ITEM-001

- **Fecha:**2026-09-28. DROPDOWN-ITEM-0010.1.0, digest en registro de contratos.
- **CONTRACT_REVIEW:** [revisión documental](../qa/contracts/dropdown-item.v0.1.0.review.md) PASS, antes de construir. Comparación24roles×4modos PASS, JSON intacto.
- **IMPLEMENTATION_REVIEW:** [revisión Figma](../qa/implementations/dropdown-item.v0.1.0.figma.review.md) PASS para18variantes,10propiedades,186pinturas y180referencias. Capturas y doce ejemplos temáticos revisados; swaps y texto largo verificados. Dos limitaciones de contraste documentadas sin recolorear.
- **Promoción:** contrato en specs, DELEGATED_FOR_BUILD; auditoría humana PENDING y biblioteca UNPUBLISHED. No declara completa toda la familia Select.

## QA-LOGOS-001

- **Fecha:**2026-09-28. LOGOS-001 v0.1.0, digest en registro de contratos.
- **CONTRACT_REVIEW:** [revisión documental](../qa/contracts/logos.v0.1.0.review.md) PASS antes de construir.
- **IMPLEMENTATION_REVIEW:** [revisión parcial](../qa/implementations/logos.v0.1.0.figma.review.md) PENDING. Conteos de seis sets,72variantes, propiedades y bindings correctos; quedan12assets y diferencias geométricas subpíxel.
- **Evidencia:** [readback](../qa/implementations/logos.v0.1.0.partial-readback.json) y [dependencias/propiedades](../qa/implementations/logos.v0.1.0.properties-readback.json). Auditoría humana PENDING; no VALIDATED ni promoción documental.


## QA-TOKENS-001

- **Tipo:** `CONTRACT_REVIEW`.
- **Fecha:** 2026-09-22.
- **Contrato:** `FOUNDATIONS-TOKENS-001` versión `0.1.0`, SHA-256 bytes `e89ddaf95e1ee07998fa851c50ef9787b4ec3f9072e0c1ea44e07eb3e298e1da`.
- **Registro detallado:** [revisión documental](../qa/contracts/foundations-tokens.review.md).
- **Alcance:** documentación candidata; no se inspeccionó implementación.
- **Resultado:** `PASS` para revisión humana; aprobación pendiente. Figma `NOT_STARTED`.

Este registro acredita el resultado documental en la fecha de su revisión; su mención de aprobación pendiente es histórica. La aprobación posterior consta en [DEC-TOKENS-001](decisions.md).

## QA-TOKENS-FIGMA-001

- **Tipo:** `IMPLEMENTATION_REVIEW`.
- **Fecha:** 2026-09-22.
- **Contrato:** [FOUNDATIONS-TOKENS-001 0.1.0 aprobado](../specs/foundations/foundations-tokens.contract.md), SHA-256 bytes `e7362c364aa2c93a1a5bd50e0024d6b551f8ec6c6947bb62c6779ee25c1b7999`.
- **Datos:** inventario SHA-256 bytes `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.
- **Registro detallado:** [revisión de Figma](../qa/implementations/foundations-tokens.figma.review.md).
- **Resultado:** `PASS`; implementación de las variables `VALIDATED` para este alcance. No acredita componentes ni web.

## QA-BUTTON-001

- **Tipo:** `CONTRACT_REVIEW`.
- **Fecha:** 2026-09-23.
- **Contrato:** `BUTTON-001` versión `0.1.0`, SHA-256 Markdown `a2124c2d1236108c5ff129e6d552510568b625a1012ab3653d18528f89c0d6a0`.
- **Modelo técnico:** SHA-256 YAML `734b85826ad4cb4c2caa08932e4364516a6e2f31f4be8e8ce6b0decda6ec4e1b`.
- **Registro detallado:** [revisión documental](../qa/contracts/button.review.md), SHA-256 `12dc9151e4a2befab8a5e7c07f159f6622000dc5e8e180e5dee64c530199a9c9`.
- **Fuente de iconos:** [DEC-ICONS-001](decisions.md) y `SRC-FIGMA-PHOSPHOR-001`; cotejo de keys de PlusCircle `PASS`.
- **Historia:** esta revisión sustituye el QA documental inicial del mismo candidato, cuyo registro tenía SHA-256 `80860415d587d399f858308bb64ed8a59d67480730dce08356c81bf43be4f327`; nunca fue aprobación humana ni QA de implementación.
- **Resultado:** `PASS` para revisión humana. La aprobación posterior consta en [DEC-BUTTON-001](decisions.md). Preparación de la actualización de página `BLOCKED`; `IMPLEMENTATION_REVIEW` integral no ejecutado.

La frase anterior es histórica del QA documental; la aprobación y validación Figma posteriores se registran por separado.

## QA-BUTTON-FIGMA-001

- **Tipo:** `IMPLEMENTATION_REVIEW` parcial de preflight, previo al renombrado.
- **Registro:** [button.figma.preflight.md](../qa/implementations/button.figma.preflight.md), SHA-256 bytes `b331fb587de9a3e0f17d4807c021487a409aa9cb4737a306da43593636eee418`.
- **Resultado:** `BLOCKED` en ese momento por nombre de página pendiente; conserva el historial de lectura sin afirmar QA final.

## QA-BUTTON-FIGMA-002

- **Tipo:** `IMPLEMENTATION_REVIEW` posterior a la última escritura.
- **Contrato y enmienda:** [BUTTON-001 0.1.0](../specs/components/button.contract.md), SHA-256 `4b94f80787c1fc9d9990f806c99900e17db060e65b624471b0c8d93f534f2abb`; [AMD-BUTTON-PAGE-001](../specs/components/button-page-name.amendment.md), SHA-256 `b2c896cab9f2f5659101253dbc93ce0410c697081e53daafecebbc5b62895fd7`.
- **Registro:** [button.figma.review.md](../qa/implementations/button.figma.review.md), SHA-256 bytes `349ade7952772613c1d61e77f96ac2d6bf18bc66352ffcecd812902c7385707e`.
- **Resultado:** `PASS`; Button `VALIDATED` únicamente para el alcance Figma estructural/visual aprobado. Interacciones web, accesibilidad WCAG y producto permanecen fuera del alcance.

## QA-BUTTON-USAGE-002

- **Tipo:** `CONTRACT_REVIEW` de la revisión candidata `BUTTON-001` 0.2.0.
- **Candidato:** [contrato de uso](../drafts/contracts/button.contract.v0.2.0.md), SHA-256 bytes `c97cd24a1505236cfdac32d85a676d8eb2b4394ec074412305d7cfd3abf37ae5`.
- **Registro:** [revisión documental](../qa/contracts/button-usage.v0.2.0.review.md); [síntesis](../drafts/reports/button-usage.v0.2.0.synthesis.md).
- **Resultado histórico:** `PASS` para decisión humana; en esa revisión previa la publicación de Description y Documentation link estaba `BLOCKED` por aprobación y URL, respectivamente. La aprobación posterior consta en [DEC-BUTTON-USAGE-002](decisions.md); el resultado de implementación se registra aparte.

## QA-BUTTON-FIGMA-USAGE-003

- **Tipo:** `IMPLEMENTATION_REVIEW` de Description y regresión estructural posterior a la última escritura.
- **Contrato:** [BUTTON-001 0.2.0 aprobado](../specs/components/button.contract.v0.2.0.md), SHA-256 bytes `53e13fa8e664f70d0ce81116e850bbcb0ab7da9f14ac0f08607fa5fda09894a1`.
- **Registro:** [revisión de Figma](../qa/implementations/button-description.v0.2.0.figma.review.md), SHA-256 bytes `53f0215666ea8c5f086bfa5f7f7fe5abdb73f66a3b3cfc0a8614a345c6b87397`.
- **Resultado:** `PASS` para metadatos del archivo Figma. `descriptionMarkdown` coincide exactamente con el texto aprobado; 60 variantes, 120 iconos Phosphor, 35 IDs de variables y 23 reacciones permanecen. Figma reporta `UNPUBLISHED` para biblioteca de equipo, fuera del alcance de esta escritura.

## QA-FILTER-CHIP-001

- **Tipo:** `CONTRACT_REVIEW`.
- **Fecha:** 2026-09-23.
- **Contrato:** `FILTER-CHIP-001` versión `0.1.0`, SHA-256 Markdown `f7dd64cfcf072c3e02f5bb11e273894a2baeb9c12888a2e9accd521f73a6b13a`; YAML técnico `af6918afb5ce050047c06153d9def42d9365efb3f2fbbee949f2845a2932632e`.
- **Registro detallado:** [filter-chip.review.md](../qa/contracts/filter-chip.review.md).
- **Alcance:** documentación candidata desde el nodo fuente `8203:10`; no se inspeccionó ni implementó el destino.
- **Resultado:** `BLOCKED` por `CONFLICT-FC-001` a `003`. El candidato permanece `DRAFT` y la implementación `NOT_STARTED`.

## QA-FILTER-CHIP-002

- **Tipo:** `CONTRACT_REVIEW` de la revisión candidata `FILTER-CHIP-001` 0.2.0.
- **Contrato:** [candidato 0.2.0](../drafts/contracts/filter-chip.contract.v0.2.0.md), SHA-256 bytes `bd82e46bcbde849890af30e9c8f6d5fad3b1d0cb2b3b5b2f5ac1cacd1127ab96`.
- **Datos:** [YAML observacional](../drafts/contracts/filter-chip.contract.yaml), SHA-256 `af6918afb5ce050047c06153d9def42d9365efb3f2fbbee949f2845a2932632e`; [modelo de construcción](../drafts/contracts/filter-chip.build.v0.2.0.yaml), SHA-256 `40e9e3464b86560255c185bf893518dea2a445170678fa797c8ff6925218e48c`.
- **Registro:** [revisión documental](../qa/contracts/filter-chip.v0.2.0.review.md).
- **Resultado:** `PASS` para decisión humana; contrato `IN_REVIEW`, implementación `NOT_STARTED`.

Este resultado es histórico de la revisión documental previa. La aprobación posterior consta en [DEC-FILTER-CHIP-APPROVAL-002](decisions.md), y la validación del archivo Figma se registra a continuación.

## QA-FILTER-CHIP-FIGMA-001

- **Tipo:** `IMPLEMENTATION_REVIEW` posterior a la última escritura.
- **Contrato:** [FILTER-CHIP-001 0.2.0 aprobado](../specs/components/filter-chip.contract.v0.2.0.md), SHA-256 bytes `325a408cfa6a5880c2136aee89a448e9ab3a6d928199543d946d6ae3a52a6cb8`.
- **Registro:** [revisión de Figma](../qa/implementations/filter-chip.v0.2.0.figma.review.md), SHA-256 bytes `4d2ce4b368313b70b61150fd0c1428e43a97545f9f1c186e5d3e780d420e22af`.
- **Resultado:** `PASS` para AC-FC-001–009: 30 variantes, ocho propiedades, iconos Phosphor, bindings locales y 112/112 resoluciones token×modo; inspección visual final sin recortes aparentes. Alcance exclusivo del archivo Figma, set `UNPUBLISHED`.

## QA-TOOLTIP-001

- **Tipo:** `CONTRACT_REVIEW` de `TOOLTIP-001` 0.1.0 bajo decisión delegada.
- **Candidato revisado:** [Tooltip](../drafts/contracts/tooltip.contract.v0.1.0.candidate.md), SHA-256 bytes `be1b92f6026cc2825a5bdbc105718c2b9dffbc097a5da39a8cc84745f00d4359`; YAML `0e091b8057c012d012668d01bdc152cf920faa85ae27265fb5a82df374918d2d`.
- **Registro:** [QA documental](../qa/contracts/tooltip.v0.1.0.review.md), `PASS` para DOC-01–18; no acredita implementación ni aprobación humana.
- **Estado posterior:** `DELEGATED_FOR_BUILD` con `user_audit: PENDING`.

## QA-TOOLTIP-FIGMA-001

- **Tipo:** `IMPLEMENTATION_REVIEW` posterior a la última escritura.
- **Contrato:** [TOOLTIP-001 0.1.0 delegado](../drafts/contracts/tooltip.contract.v0.1.0.md), SHA-256 bytes `522b74426f781231dbf0a3ce7daed35909ab8f1358e347efe97e34f454416402`.
- **Registro:** [revisión de Figma](../qa/implementations/tooltip.v0.1.0.figma.review.md).
- **Resultado:** `PASS` técnico para AC-TTIP-001–008; cuatro variantes, propiedad de texto conectada, bindings locales, lectura de sombras, 52 relaciones token-modo y captura visual. `user_audit: PENDING`, set `UNPUBLISHED`; no acredita comportamiento web o accesibilidad funcional.

## QA-BADGE-001

- **Tipo:** `CONTRACT_REVIEW` de `BADGE-001` 0.1.0 bajo decisión delegada.
- **Candidato:** [Badge](../drafts/contracts/badge.contract.v0.1.0.candidate.md), SHA-256 bytes `388812c1028c1dfaedda1a885b7043fec25e36a7ef7bf23411b513bd64b84830`; YAML SHA-256 `b087af4f17a478f136e3bb50e3c4a5eaa3b9c789deb1325310c6a669f879087b`.
- **Registro:** [QA documental](../qa/contracts/badge.v0.1.0.review.md), `PASS` para DOC-01–18; no acredita implementación ni aprobación humana.
- **Estado posterior:** `DELEGATED_FOR_BUILD`, `user_audit: PENDING`.

## QA-BADGE-AMD-001

- **Tipo:** revisión de la enmienda de contraste `AMD-BADGE-CONTRAST-001` 0.1.1; [candidato](../drafts/contracts/badge.contrast-amendment.v0.1.1.candidate.md) SHA-256 `c85abd212d654762afb491588d093211fde9531600558918e55e720c82d516b6`.
- **Registro:** [QA documental](../qa/contracts/badge.contrast-amendment.v0.1.1.review.md), `PASS`; decisión delegada, auditoría humana pendiente.

## QA-BADGE-FIGMA-001

- **Tipo:** hallazgo de implementación previo a la enmienda. [Registro](../qa/implementations/badge.v0.1.0.contrast-finding.md), `FAIL` por contraste informativo y warning. Se conserva como historial.

## QA-BADGE-FIGMA-002

- **Tipo:** revisión de implementación histórica bajo la enmienda 0.1.1. [Registro](../qa/implementations/badge.v0.1.1.figma.review.md), `PASS` técnico para su criterio de contraste anterior; los tres colores restaurados y umbrales quedaron `SUPERSEDED` por 0.1.2. `user_audit: PENDING`, set `UNPUBLISHED`.

## QA-TOGGLE-001

- **Tipo:** revisión documental de `TOGGLE-001` 0.1.0. [Registro](../qa/contracts/toggle.v0.1.0.review.md), `PASS`; candidato SHA-256 `95bc256260c71c32158b7d2d62f29e1cbafdd90176859a7903afe9dcc321f123`, YAML `4010c12aaae2784df134268f776a25f7cad1c26d4a6a09f35a1a9cb28fb320f0`.

## QA-TOGGLE-AMD-001

- **Tipo:** revisión de enmienda 0.1.1. [Registro](../qa/contracts/toggle.contrast-amendment.v0.1.1.review.md), `PASS`; candidato SHA-256 `4933c5d554eb76f436b6e7e7ee426e679ff5ad84e6867ff40bb43cce965f038e`.

## QA-TOKENS-EXT-001 y QA-CONTROL-COLORS-FIGMA-001

- **Tipo:** [revisión documental](../qa/contracts/foundations.control-colors.amendment.v0.1.1.review.md) `PASS` y [verificación de variables en Figma](../qa/implementations/control-colors.v0.1.0.figma.review.md) `PASS`. Dos roles nuevos, ocho aliases al primitivo existente, scopes propios y JSON/Figma coincidentes. Auditoría humana pendiente.

## QA-BUTTON-AMD-001 y QA-BUTTON-FIGMA-SEMANTIC-004

- **Tipo:** [revisión documental](../qa/contracts/button.semantic-scope-amendment.v0.2.1.review.md) `PASS` y [lectura posterior Figma](../qa/implementations/button.semantic-scope.v0.2.1.figma.review.md) `PASS`. Nueve textos Disabled corregidos, 60 nodos TEXT sin roles de icono, sin cambio RGB; auditoría humana pendiente.

## QA-TOGGLE-AMD-002

- **Tipo:** [revisión documental 0.1.2](../qa/contracts/toggle.visual-contrast-amendment.v0.1.2.review.md), `PASS`; candidato SHA-256 `431752526d2defb4a043d569806c10d36d4566eecab5c1e9ba5a5657c8b1309a`.

## QA-TOGGLE-FIGMA-001

- **Tipo:** hallazgo inicial de contraste Off/Default y Off/Focus 1.23:1. [Registro](../qa/implementations/toggle.v0.1.0.contrast-finding.md), `FAIL` histórico.

## QA-TOGGLE-FIGMA-002

- **Tipo:** revisión Figma posterior a la corrección. [Registro](../qa/implementations/toggle.v0.1.1.figma.review.md), `PASS` técnico para AC-TGL-001–008; 40 pinturas, 80 bindings tipográficos, 25 roles semánticos × cuatro modos y mínimo activo 3.24:1. `user_audit: PENDING`, `UNPUBLISHED`.

## QA-TOGGLE-FIGMA-003

- **Tipo:** [hallazgo visual de 0.1.1](../qa/implementations/toggle.v0.1.1.visual-fidelity-finding.md), `FAIL` histórico: los dos fondos Off oscuros se apartaban demasiado de la fuente.

## QA-TOGGLE-FIGMA-004

- **Tipo:** [revisión final 0.1.2](../qa/implementations/toggle.v0.1.2.figma.review.md), `PASS` técnico: 40/40 paints con scope y semántica correctos, 23 roles × cuatro modos, Off claro con contorno neutral 4.76:1 y mínimo activo general 3.24:1. `user_audit: PENDING`, `UNPUBLISHED`.

## QA-SEMANTIC-SCOPE-001

- **Tipo:** [revisión retrospectiva cruzada](../qa/implementations/semantic-scope-retrospective.v0.1.0.review.md), `PASS`: 430 paints sólidos renderizados en cinco familias, cero problemas vigentes de scope o categoría semántica. Los fills de envoltura Phosphor no ligados están `visible:false` y no se contaron como pinturas renderizadas. Auditoría humana pendiente.

## QA-TOKENS-FOCUS-001 y QA-FOCUS-EFFECTS-FIGMA-001

- **Tipo:** [revisión documental](../qa/contracts/foundations.focus-effects.amendment.v0.1.2.review.md) `PASS` y [lectura de variables en Figma](../qa/implementations/focus-effects.v0.1.0.figma.review.md) `PASS`: dos roles `EFFECT_COLOR`, ocho aliases, JSON/Figma coincidentes y colección semántica 133. Auditoría humana pendiente.

## QA-TOGGLE-AMD-003, QA-TOGGLE-FIGMA-005 y QA-TOGGLE-FIGMA-006

- **Tipo:** [enmienda documental](../qa/contracts/toggle.focus-effect-amendment.v0.1.3.review.md) `PASS`; [hallazgo de efectos](../qa/implementations/toggle.v0.1.2.effect-scope-finding.md) `FAIL` histórico; [readback y captura tras corrección](../qa/implementations/toggle.v0.1.3.figma.review.md) `PASS`. Cuatro bindings de foco cambiaron a roles propios de efecto sin variar apariencia. Auditoría humana pendiente.

## QA-TOGGLE-AMD-004 y QA-TOGGLE-FIGMA-007

- **Tipo:** [revisión documental de Mixed](../qa/contracts/toggle.mixed-amendment.v0.1.4.review.md) `PASS`; [readback y captura de cuatro variantes nuevas](../qa/implementations/toggle.mixed.v0.1.4.figma.review.md) `PASS`. Se repararon referencias de propiedades perdidas en etiquetas clonadas; 12 variantes y ocho IDs originales verificados. No se crearon tokens ni se publicó el set; auditoría humana pendiente. La reapertura cromática previa de Toggle continúa.

## QA-MIGRATION-TRACEABILITY-001

- **Tipo:** [QA documental del contrato transversal](../qa/contracts/migration-token-traceability.v0.1.0.review.md) `PASS` para la regla de trazabilidad. No valida por sí solo familias, variables ni colores Figma; la [matriz](../specs/MIGRATION-TRACEABILITY-STATUS.md) conserva pendientes.

## QA-TOOLTIP-TRACEABILITY-001

- **Tipo:** [readback transversal de Tooltip](../qa/implementations/tooltip.traceability.v0.1.0.review.md): `PASS` para 12 paints y aliases de color, `IN_PROGRESS` para fidelidad total por normalización tipográfica explícita (AUD-004). No hubo cambios Figma ni tokens nuevos.

## QA-TOGGLE-AMD-005 y QA-TOGGLE-FIGMA-008

- **Tipo:** [revisión documental 0.1.5](../qa/contracts/toggle.source-color-amendment.v0.1.5.review.md) y [readback de dos strokes Off](../qa/implementations/toggle.source-color.v0.1.5.figma.review.md), ambos `PASS` acotado. El ratio original 1.23:1 queda marcado `*`; el umbral de 0.1.2 se sustituye solo para esos bordes. El barrido de fills/strokes heredados coincide en RGB; halo Focus `#F8FAFC`→`#FFFFFF` permanece abierto como AUD-003. No es `PASS` cromático global ni aprobación humana.

## QA-RADIO-SOURCE-001 y QA-RADIO-CONTRACT-001

- **Tipo:** [revisión documental de la fuente](../qa/contracts/radio-button.source.component-contract.review.md) `PASS` y [contrato de destino](../qa/contracts/radio-button.v0.1.0.review.md) `PASS`; matriz de ocho variantes, dependencia local, 12 variables fuente y diferencias semánticas documentadas. Auditoría humana pendiente.

## QA-RADIO-TOKENS-001 y QA-RADIO-INDICATOR-COLORS-FIGMA-001

- **Tipo:** [revisión documental de extensión](../qa/contracts/foundations.radio-indicator-colors.amendment.v0.1.3.review.md) `PASS` y [readback Figma](../qa/implementations/radio-indicator-colors.v0.1.0.figma.review.md) `PASS`; dos variables `SHAPE_FILL`, ocho aliases, JSON/Figma coincidentes, colección semántica 135. Auditoría humana pendiente.

## QA-RADIO-BUTTON-FIGMA-001

- **Tipo:** [QA de implementación](../qa/implementations/radio-button.v0.1.0.figma.review.md) `PASS`: página propia, 8+8 variantes, ocho instancias emparejadas, 36 paints y cuatro efectos ligados con scopes correctos, 16 etiquetas conectadas, contraste activo mínimo 3.24:1. `user_audit: PENDING`, `UNPUBLISHED`.

## QA-CHECKBOX-SOURCE-001 y QA-CHECKBOX-CONTRACT-001

- **Tipo:** [revisión documental de origen](../qa/contracts/checkbox.source.component-contract.review.md) `PASS` y [contrato de destino](../qa/contracts/checkbox.v0.1.0.review.md) `PASS`: 86/86 nodos fuente, matriz 3×4, dependencias Phosphor y tokens locales mapeados; auditoría humana pendiente.

## QA-CHECKBOX-FIGMA-001

- **Tipo:** [QA de implementación](../qa/implementations/checkbox.v0.1.0.figma.review.md) `PASS`: 12 variantes, ocho iconos Phosphor, 24 etiquetas conectadas, 46 paints visibles y seis efectos semánticos, cero errores de scope/categoría, contraste activo mínimo 3.24:1. `user_audit: PENDING`, `UNPUBLISHED`.

## QA-DOT-SOURCE-001 y QA-DOT-CONTRACT-001

- **Tipo:** [QA documental fuente](../qa/contracts/dot.source.component-contract.review.md) y [destino](../qa/contracts/dot.v0.1.0.review.md) `PASS`: 22/22 nodos, 15 variantes, contradicciones de la Description antigua excluidas y riesgo de tipografía 4/8 px explícito. Auditoría humana pendiente.

## QA-DOT-BACKGROUND-COLORS-FIGMA-001

- **Tipo:** [QA Figma de variables](../qa/implementations/dot-background-colors.v0.1.0.figma.review.md) `PASS`: cuatro roles `FRAME_FILL`, 16 aliases, JSON/Figma coincidentes, colección semántica 139.

## QA-DOT-INACTIVE-BORDER-001, QA-DOT-AMD-001 y QA-DOT-INACTIVE-BORDER-FIGMA-001

- **Tipo:** [QA documental de variable](../qa/contracts/foundations.dot-inactive-border.amendment.v0.1.5.review.md) y [enmienda](../qa/contracts/dot.inactive-border-amendment.v0.1.1.review.md) `PASS`; [QA Figma](../qa/implementations/dot-inactive-border.v0.1.0.figma.review.md) `PASS` para scope, cuatro aliases y tres consumidores. Auditoría humana pendiente.

## QA-DOT-FIGMA-001

- **Tipo:** [QA Figma histórico](../qa/implementations/dot.v0.1.1.figma.review.md) `PASS` para la enmienda anterior: 15 variantes, 36/36 paints con binding y categoría correctos, contorno Inactive 4.76:1 y textos editables. El color de ese contorno quedó `SUPERSEDED` por 0.1.2; `user_audit: PENDING`, `UNPUBLISHED`; fontSize 4/8 no avalado para uso accesible de producción.

## QA-DOT-SOURCE-COLOR-002

- **Tipo:** [QA documental](../qa/contracts/dot.source-color-amendment.v0.1.2.review.md), [QA Figma](../qa/implementations/dot.source-color.v0.1.2.figma.review.md) y [QA de publicación en specs](../qa/contracts/dot.specs-publication.v0.1.2.review.md) `PASS` técnico: cuatro aliases de borde Inactive a primitiva blanca, 15 variantes/36 paints coincidentes con fuente, cero bindings perdidos. Limitación `*`; auditoría humana `PENDING`, set `UNPUBLISHED`.

## QA-AVATAR-SOURCE-001 y QA-AVATAR-CONTRACT-001

- **Tipo:** [QA documental fuente](../qa/contracts/avatar.source.component-contract.review.md) y [destino](../qa/contracts/avatar.v0.1.0.review.md) `PASS`: matriz 3×4, 16 instancias, 18 variables fuente, imagen preservada, cambios de tipografía y color delimitados. Auditoría humana pendiente.

## QA-AVATAR-ROLES-001 y QA-AVATAR-ROLES-FIGMA-001

- **Tipo:** [QA documental](../qa/contracts/foundations.avatar-roles.amendment.v0.1.6.review.md) y [QA Figma](../qa/implementations/avatar-roles.v0.1.0.figma.review.md) `PASS`: dos variables de scopes exclusivos, ocho aliases, JSON/Figma coincidentes, colección semántica 142.

## QA-AVATAR-FIGMA-001

- **Tipo:** [QA Figma histórico](../qa/implementations/avatar.v0.1.0.figma.review.md) `PASS` para el criterio anterior: 12 variantes, propiedades conectadas, 1512 preferencias Phosphor, 48/48 paints semánticos y cuatro imágenes. El contraste fallback mínimo 4.72:1 quedó `SUPERSEDED` en Servicios por el color fuente orange/500; `user_audit: PENDING`, `UNPUBLISHED`.

## QA-AVATAR-SOURCE-COLOR-002

- **Tipo:** [QA documental](../qa/contracts/avatar.source-color-amendment.v0.1.1.review.md) y [QA Figma](../qa/implementations/avatar.source-color.v0.1.1.figma.review.md) `PASS` cromático técnico: alias Servicios, ocho consumidores de fondo, doce Dot y cuatro textos verificados. Contraste `*`, tipografía AUD-006, auditoría humana `PENDING`, set `UNPUBLISHED`.

## QA-FEEDBACK-ICON-SCOPES-001 y QA-FEEDBACK-ICON-SCOPES-FIGMA-001

- **Tipo:** [QA documental](../qa/contracts/foundations.feedback-icon-scopes.amendment.v0.1.7.review.md) y [QA Figma](../qa/implementations/feedback-icon-scopes.v0.1.0.figma.review.md) `PASS`: tres icon roles con scope exclusivo `SHAPE_FILL`, valores y descripciones intactos, dos consumidores Badge de tipo VECTOR, 80 tokens COLOR semánticos sin incompatibilidades categoría/scope. Auditoría humana pendiente.

## QA-INLINE-NOTIFICATION-SOURCE-001

- **Tipo:** [QA documental fuente](../qa/contracts/inline-notification.source.component-contract.review.md) `PASS`: 46/46 nodos, cinco variantes, diez instancias Phosphor, 23 variables y anomalías de texto/iconos/hipervínculo documentadas. No acredita contrato destino ni Figma nuevo.

## QA-INLINE-NOTIFICATION-CONTRACT-001

- **Tipo:** [QA documental destino](../qa/contracts/inline-notification.v0.1.0.review.md) `PASS`: 21 secciones, cinco variantes, bindings semánticos, diferencias visuales y de contenido delimitadas. Auditoría humana pendiente; no acredita implementación Figma.

## QA-INLINE-NOTIFICATION-FIGMA-001

- **Tipo:** [QA Figma histórico](../qa/implementations/inline-notification.v0.1.0.figma.review.md) `PASS` para el criterio previo: cinco variantes, diez instancias Phosphor, 25/25 pinturas visibles vinculadas, cero errores de scope o categoría. La afirmación de contraste mínimo de icono 3.61:1 quedó `SUPERSEDED` por Warning de origen 2.96:1; `user_audit: PENDING`, `UNPUBLISHED`.

## QA-INLINE-NOTIFICATION-WARNING-SOURCE-COLOR-002

- **Tipo:** [QA documental](../qa/contracts/inline-notification.warning-source-color.v0.1.1.review.md), [QA Figma](../qa/implementations/inline-notification.warning-source-color.v0.1.1.figma.review.md) y [QA de publicación en specs](../qa/contracts/inline-notification.specs-publication.v0.1.1.review.md) `PASS` técnico. Cinco variantes, Warning `#C97B00` restaurado y pseudoenlace sin URL omitido conforme al contrato. Limitación `*`; auditoría humana `PENDING`, set `UNPUBLISHED`.

## QA-ICON-BUTTON-SOURCE-001, QA-ICON-BUTTON-CONTRACT-001 y QA-ICON-BUTTON-BACKGROUNDS-001

- **Tipo:** [QA de fuente](../qa/contracts/icon-button.source.component-contract.review.md), [contrato de destino](../qa/contracts/icon-button.v0.1.0.review.md) y [extensión de fondos](../qa/contracts/foundations.icon-button-backgrounds.amendment.v0.1.9.review.md) `PASS` documental. Treinta variantes, dos roles nuevos y anomalía Focus documentados; aún no acredita construcción Figma. Auditoría humana pendiente.

## QA-ICON-BUTTON-BACKGROUNDS-FIGMA-001

- **Tipo:** [QA Figma de variables](../qa/implementations/icon-button-backgrounds.v0.1.0.figma.review.md) `PASS`: dos fondos `FRAME_FILL`, ocho aliases a primitivas locales y cero diferencias JSON/Figma. Auditoría humana pendiente.

## QA-ICON-BUTTON-FIGMA-001

- **Tipo:** [QA Figma de Icon Button](../qa/implementations/icon-button.v0.1.0.figma.review.md) `PASS` técnico para AC-ICB-001–008: 30 variantes, 60 dependencias anidadas, 159/159 pinturas visibles vinculadas, scopes/categorías correctos y comparación visual 289×960. Auditoría humana pendiente; no publicado.

## QA-BREADCRUMB-ITEM-SOURCE-001, QA-BREADCRUMBS-SOURCE-001 y QA-BREADCRUMBS-CONTRACT-001

- **Tipo:** [QA fuente del ítem](../qa/contracts/breadcrumb-item.source.component-contract.review.md), [QA fuente de composición](../qa/contracts/breadcrumbs.source.component-contract.review.md) y [QA del contrato destino](../qa/contracts/breadcrumbs.v0.1.0.review.md) `PASS` documental. Dos sets, diez variantes observadas, excepción Inter/Manrope, normalización de iconos 20→24 y ajuste de ancho tras captura registradas. Auditoría humana pendiente.

## QA-BREADCRUMB-CURRENT-TEXT-CONTRACT-001 y QA-BREADCRUMB-CURRENT-TEXT-FIGMA-001

- **Tipo:** [QA documental de extensión](../qa/contracts/foundations.breadcrumb-current-text.amendment.v0.1.0.review.md) y [QA Figma de variable y consumidores](../qa/implementations/breadcrumb-current-text.v0.1.0.figma.review.md) `PASS`: `TEXT_FILL` exclusivo, cuatro aliases a primitivas existentes, cinco textos Current vinculados y contraste mínimo 5.56:1 entre modos. Auditoría humana pendiente.

## QA-BREADCRUMBS-FIGMA-001

- **Tipo:** [QA Figma de Breadcrumbs](../qa/implementations/breadcrumbs.v0.1.0.figma.review.md) `PASS` técnico para AC-BRC-001–007: diez variantes en dos sets, 14 instancias locales, 38/38 pinturas visibles vinculadas, 19 textos con tipografía local completa, corrección de clipping y revisión visual posterior. Auditoría humana pendiente; no publicado.

## QA-WARNING-ICON-CONTRAST-001 y QA-WARNING-ICON-CONTRAST-FIGMA-001

- **Tipo:** [QA documental](../qa/contracts/foundations.warning-icon-contrast.amendment.v0.1.8.review.md) y [QA Figma](../qa/implementations/warning-icon-contrast.v0.1.0.figma.review.md) `PASS` histórico: warning/icon aliasó amber/700 en cuatro modos por contraste 4.38:1. Los aliases fueron sustituidos por el override fuente 0.1.1; no usar este PASS como prueba del estado actual. Auditoría humana pendiente.

## QA-WARNING-ICON-SOURCE-COLOR-002

- **Tipo:** [QA documental](../qa/contracts/foundations.warning-icon-source-color.v0.1.10.review.md), [readback Figma](../qa/implementations/warning-icon-source-color.v0.1.1.figma.review.md) y [QA de publicación en specs](../qa/contracts/foundations.warning-icon-specs-publication.v0.1.10.review.md) `PASS`: warning/icon alias amber/600 en cuatro modos, scope/descripción intactos y consumidor Inline Notifications `#C97B00` verificado. Contraste 2.96:1 marcado `*`; auditoría humana pendiente.

## QA-BADGE-SOURCE-COLOR-002

- **Tipo:** [QA documental](../qa/contracts/badge.source-color-amendment.v0.1.2.review.md), [QA Figma](../qa/implementations/badge.source-color.v0.1.2.figma.review.md) y [QA de publicación en specs](../qa/contracts/badge.specs-publication.v0.1.2.review.md) `PASS` técnico: seis variantes, 19 paints visibles con color fuente, cuatro bindings corregidos, 17 roles/25 consumidores con scope y alias verificados y seis textos tipográficos coincidentes. El contraste bajo se documenta `*`; no es certificación WCAG ni aprobación humana.

## QA-METRIC-CARD-SOURCE-001

- **Tipo:** [QA de evidencia fuente](../qa/contracts/metric-card.source.component-contract.review.md) `PASS` documental: ocho variantes, 119 nodos, 16 instancias, 36 textos y 31 variables locales conciliados. No acredita todavía contrato ni construcción en AI Design System.

## QA-METRIC-CARD-ROLES-001

- **Tipo:** [QA documental](../qa/contracts/foundations.metric-card-roles.amendment.v0.1.0.review.md) y [QA Figma de variables](../qa/implementations/metric-card-roles.v0.1.0.figma.review.md) `PASS` técnico: dos roles, ocho aliases, scopes exclusivamente `TEXT_FILL`/`SHAPE_FILL`, paridad JSON/Figma y 20 consumidores correctos. Auditoría humana posterior.

## QA-METRIC-CARD-CONTRACT-001

- **Tipo:** [QA documental destino](../qa/contracts/metric-card.v0.1.0.review.md) `PASS`: ocho variantes, mapa estricto de tokens por consumidor, iconos Phosphor y cambios tipográficos/editabilidad delimitados. No acredita todavía construcción Figma; auditoría humana pendiente.

## QA-METRIC-CARD-FIGMA-001

- **Tipo:** [QA Figma final](../qa/implementations/metric-card.v0.1.0.figma.review.md) `PASS` técnico: ocho variantes, 16 instancias Phosphor, 70/70 pinturas visibles ligadas, 36/36 textos con tipografía semántica, cero incompatibilidades de scope/categoría y cero reacciones. Captura final 806×935 comparada; `UNPUBLISHED`, auditoría humana pendiente.

## QA-CHART-LABEL-CELL-SOURCE-001

- **Tipo:** [QA documental fuente](../qa/contracts/chart-label-cell.source.component-contract.review.md) `PASS`: cuatro variantes, 17 nodos, cinco variables y dos anomalías de tokenización registradas. No acredita aún contrato destino ni Figma.

## QA-CHART-CELL-SOURCE-001

- **Tipo:** [QA documental fuente](../qa/contracts/chart-cell.source.component-contract.review.md) `PASS`: 13 variantes, 26 nodos y ocho variables conciliados; 27 cruces ausentes y rol de barra genérico documentados. No acredita aún contrato destino ni Figma.

## QA-CHART-PROGRESS-ITEM-SOURCE-001

- **Tipo:** [QA documental fuente](../qa/contracts/chart-progress-item.source.component-contract.review.md) `PASS`: dos variantes, 40 nodos, seis instancias `labelCell`, diez textos y 17 variables; relleno Progress con rol iconográfico y discordancia muestra/barra documentados. No acredita destino.

## QA-CHART-DONUT-SOURCE-001

- **Tipo:** [QA documental fuente](../qa/contracts/chart-donut.source.component-contract.review.md) `PASS`: tres variantes, 13 nodos, seis vectores con paths preservados, tres textos y seis variables. No acredita destino.

## QA-CHART-HEADER-SOURCE-001

- **Tipo:** [QA documental fuente](../qa/contracts/chart-header.source.component-contract.review.md) `PASS`: componente suelto de 17 nodos con tres instancias `labelCell`, cinco textos y doce variables; errata y roles de swatch documentados. No acredita destino.

## QA-CHARTS-CONTRACT-001

- **Tipo:** [QA documental destino](../qa/contracts/charts.v0.1.0.review.md) `PASS` bajo `DELEGATED_FOR_BUILD`: cinco piezas/23 definiciones, mapa de roles por categoría y scope, siete variables JSON/Figma verificadas, diferencias y límites explícitos. No acredita por sí solo Figma; auditoría humana pendiente.

## QA-CHART-COLORS-FIGMA-001

- **Tipo:** [QA de variables](../qa/implementations/chart-colors.v0.1.0.figma.review.md) `PASS`: siete roles locales con paridad JSON/Figma en cuatro modos y 33 pinturas consumidoras; cero cruces semánticos/de scope. Auditoría humana pendiente.

## QA-CHARTS-FIGMA-001

- **Tipo:** [QA Figma final](../qa/implementations/charts.v0.1.0.figma.review.md) `PASS` técnico: página única, 23 definiciones, nueve instancias locales, seis vectores, 28 textos completos, 76 pinturas ligadas (72 visibles por defecto), cero incompatibilidades y cero reacciones. Comparación visual y diferencias registradas; `UNPUBLISHED`, auditoría humana pendiente.

## QA-LINEAR-PROGRESS-BAR-SOURCE-001

- **Tipo:** [QA documental fuente](../qa/contracts/linear-progress-bar.source.component-contract.review.md) `PASS`: 48 variantes, 336 nodos, 144 textos y doce variables conciliados; discrepancia de 36 porcentajes visibles y roles de barra incorrectos documentados. No acredita aún destino.

## QA-LINEAR-PROGRESS-COLORS-CONTRACT-001 y QA-LINEAR-PROGRESS-COLORS-FIGMA-001

- **Tipo:** [QA documental de extensión](../qa/contracts/foundations.linear-progress-colors.v0.1.0.review.md) y [QA Figma de variables/consumidores](../qa/implementations/linear-progress-colors.v0.1.0.figma.review.md) `PASS`: cinco roles `FRAME_FILL`, veinte aliases a primitivas locales, paridad JSON/Figma y 96 fondos consumidores correctos. Auditoría humana pendiente.

## QA-LINEAR-PROGRESS-BAR-CONTRACT-001

- **Tipo:** [QA documental destino](../qa/contracts/linear-progress-bar.v0.1.0.review.md) `PASS`: matriz completa de 48 variantes, porcentajes derivados, roles semánticos estrictos y cambios visuales delimitados. Auditoría humana pendiente.

## QA-LINEAR-PROGRESS-BAR-FIGMA-001

- **Tipo:** [QA Figma final](../qa/implementations/linear-progress-bar.v0.1.0.figma.review.md) `PASS` técnico: página única, 48 combinaciones, 240/240 paints y 720/720 bindings tipográficos correctos, propiedades conectadas, cero incompatibilidades o reacciones. Captura fuente/destino comparada; `UNPUBLISHED`, auditoría humana pendiente.

## QA-SELECTION-CONTROL-SOURCE-COLOR-002

- **Tipo:** [QA documental](../qa/contracts/selection-control-source-color.v0.1.1.review.md) y [QA Figma posterior](../qa/implementations/selection-control-source-color.v0.1.1.figma.review.md) `PASS` **acotado**: cuatro aliases, tres contornos consumidores, 12+8 variantes conservadas, fondo hover intacto y cero consumidores Toggle. Contraste neutral/400 ~2.56:1 `*`; auditoría humana `PENDING`, Figma `UNPUBLISHED`.

## QA-MIGRATION-COLOR-FIDELITY-REOPEN-001

- **Fecha:** 2026-09-24. Las decisiones [fidelidad cromática](decisions.md#dec-migration-visual-fidelity-001--prioridad-de-color-de-origen) y [limitaciones marcadas](decisions.md#dec-migration-contrast-limitations-001--fidelidad-cromática-y-revisión-interna) cambian el criterio posterior a varios `PASS` técnicos históricos.
- **Estado:** `STALE` solo para la comparación cromática y el contraste final de las familias con ajustes deliberados; no se borra el `PASS` que documentó la lectura anterior ni se invalida por defecto la estructura, propiedades o bindings no afectados.
- **Alcance conocido:** Avatar, Badge, Breadcrumbs, Charts, Checkbox, Dot, Inline Notification, Linear Progress Bar, Metric Card, Radio Button y Toggle; revisar además los consumidores anidados de roles compartidos, incluido Icon Button cuando cambie Dot. El inventario exacto de pares queda en [auditoría por excepciones](../specs/MIGRATION-AUDIT.md).
- **Cierre:** restaurar o remapear al color fuente mediante rol del scope correcto y primitiva existente, sincronizar JSON/Figma/contrato, leer el destino de nuevo y medir contraste. Marcar con `*` solo limitaciones confirmadas; no afirmar accesibilidad completa ni promoción a `specs/` del contrato afectado con QA cromático obsoleto.

## QA-NAVIGATION-SWITCH-TAB-ITEM-001

- **Tipo:** [QA documental](../qa/contracts/navigation-switch-tab-item.v0.1.0.review.md) `PASS` y [QA Figma final](../qa/implementations/navigation-switch-tab-item.v0.1.0.figma.review.md) `PASS` técnico: tres variantes, dimensiones fuente, propiedades y dependencias reutilizables verificadas; cero discrepancias de binding. Contrato en `specs/`, Figma `UNPUBLISHED`, auditoría humana `PENDING`.

## QA-FOUNDATIONS-NAVIGATION-TAB-COLORS-001

- **Tipo:** [QA de variable local](../qa/implementations/navigation-tab-colors.v0.1.0.figma.review.md) `PASS` técnico: nombre, descripción, scope de fondo, cuatro aliases y colores originales concuerdan con el JSON de extensión. Auditoría humana `PENDING`.

## QA-NAVIGATION-SWITCH-TAB-001

- **Tipo:** [QA documental](../qa/contracts/navigation-switch-tab.v0.1.0.review.md) y [QA Figma final](../qa/implementations/navigation-switch-tab.v0.1.0.figma.review.md) `PASS` técnico: componente 488×46 con cuatro instancias locales, nueve bindings geométricos y fill sutil original verificados; cero reacciones. Contrato en `specs/`, Figma `UNPUBLISHED`, auditoría humana `PENDING`.

## QA-FOUNDATIONS-NAVIGATION-PAGINATION-BORDER-001

- **Tipo:** [QA de variable local](../qa/implementations/navigation-pagination-border.v0.1.0.figma.review.md) `PASS` técnico: scope de borde y cuatro aliases a primitivas aprobadas concuerdan entre JSON y Figma, incluido el rojo original de Servicios. Auditoría humana `PENDING`.

## QA-NAVIGATION-PAGINATION-FIGMA-001

- **Tipo:** [QA documental](../qa/contracts/navigation-pagination.v0.1.0.review.md) y [QA Figma final](../qa/implementations/navigation-pagination.v0.1.0.figma.review.md) `PASS` técnico: cinco variantes 354×66, siete propiedades probadas, 25 instancias Caret, 125 pinturas ligadas sin cruces de scope y 75 bindings tipográficos; cero reacciones. Contrato en `specs/`, Figma `UNPUBLISHED`, auditoría humana `PENDING`.

## QA-NAVIGATION-TAB-SOURCE-001

- **Tipo:** [QA de inventario fuente](../qa/contracts/navigation-tab.source.component-contract.review.md) `PASS`: 17 variantes no cartesianas, 132 nodos, 49 instancias en total y cuatro reacciones hover conciliadas; cinco usos semánticos cruzados registrados sin trasladarlos al destino.

## QA-FOUNDATIONS-NAVIGATION-TAB-BORDERS-001

- **Tipo:** [QA de variables y consumidores](../qa/implementations/navigation-tab-borders.v0.1.0.figma.review.md) `PASS` técnico: dos roles de borde con aliases a primitivas locales, paridad JSON/Figma en cuatro modos y 107 pinturas consumidoras sin cruces semánticos/de scope. Auditoría humana `PENDING`.

## QA-NAVIGATION-TAB-FIGMA-001

- **Tipo:** [QA documental](../qa/contracts/navigation-tab.v0.1.0.review.md) y [QA Figma final](../qa/implementations/navigation-tab.v0.1.0.figma.review.md) `PASS` técnico: 17 variantes, diez propiedades, 33 ImageSquare, 16 Dot, ocho divisores, 107 pinturas locales y cuatro reacciones hover; alineación de Dynamic/Off/Hovered corregida y verificada. Contrato en `specs/`, Figma `UNPUBLISHED`, auditoría humana `PENDING`.

## QA-SCROLLBAR-SOURCE-001

- **Tipo:** [QA de inventario fuente](../qa/contracts/scrollbar.source.component-contract.review.md) `PASS` observacional: cinco sets, 30 variantes, 125 nodos, RGB y discrepancia nominal `75%` delimitados.

## QA-SCROLLBAR-CONTRACT-001

- **Tipo:** [QA documental](../qa/contracts/scrollbar.v0.1.0.review.md) `PASS` para delegación: 21 secciones, página `Scrollbars`, matriz no cartesiana, extensión cromática, límites funcionales y criterios verificables. Auditoría humana `PENDING`.

## QA-SCROLLBAR-COLORS-FIGMA-001

- **Tipo:** [QA histórico 0.1.0](../qa/implementations/scrollbar-colors.v0.1.0.figma.review.md) `STALE` para el estado actual. [QA vigente 0.1.1](../qa/implementations/scrollbar-colors.v0.1.1.figma.review.md) `PASS`: rol `SHAPE_FILL`, cuatro aliases a neutral/300 existente, 30 thumbs consumidores y primitiva 350 fuera del inventario local. Auditoría humana `PENDING`.

## QA-SCROLLBAR-FIGMA-001

- **Tipo:** [QA estructural histórico 0.1.0](../qa/implementations/scrollbar.v0.1.0.figma.review.md) `STALE` solo para color; [QA vigente 0.1.1](../qa/implementations/scrollbar.v0.1.1.figma.review.md) `PASS` técnico: ocho variantes públicas, 22 internas, 30/30 fills ligados al token semántico aliasado a neutral/300 y contraste `*` registrado. Contrato/enmienda en `specs/`, biblioteca `UNPUBLISHED`, auditoría humana `PENDING`; AUD-007 es baja prioridad.

## QA-MIGRATION-TRACEABILITY-AMENDMENT-001

- **Tipo:** [QA histórico 0.1.1](../qa/contracts/migration-token-traceability.amendment.v0.1.1.review.md) `SUPERSEDED`; [QA vigente 0.1.2](../qa/contracts/migration-token-traceability.amendment.v0.1.2.review.md) `PASS`: sustituye solo REQ-MTT-004 para preferir primitiva existente semejante con rol semántico.

## QA-STEPS-CONTRACT-001

- **Tipo:** [QA documental base 0.1.0](../qa/contracts/steps.v0.1.0.review.md) histórico para acentos fijos; [QA documental vigente 0.1.1](../qa/contracts/steps.brand-theme.v0.1.1.review.md) `PASS` para marca por tema. Las 37 variantes y la anomalía `On Primary` permanecen; auditoría humana `PENDING`.

## QA-STEPS-FIGMA-001

- **Tipo:** [QA Figma histórico 0.1.0](../qa/implementations/steps.v0.1.0.figma.review.md) `STALE` solo para color; [QA vigente 0.1.1](../qa/implementations/steps.v0.1.1.figma.review.md) `PASS` técnico: 37 variantes, 27/27 combinaciones correctas, 173/173 pinturas vinculadas, 28/28 aliases por modo y cero cruces de scope/categoría. Contrato en `specs/`, biblioteca `UNPUBLISHED`, auditoría humana `PENDING`; AUD-008 persiste.

## QA-STEPPER-CONTRACT-001

- **Tipo:** [QA documental base 0.1.0](../qa/contracts/stepper.v0.1.0.review.md) histórico para acentos fijos; [QA documental vigente 0.1.1](../qa/contracts/stepper.brand-theme.v0.1.1.review.md) `PASS` para marca por tema. Las 26 variantes fuente, icono y propiedades permanecen; auditoría humana `PENDING`.

## QA-STEPPER-FIGMA-001

- **Tipo:** [QA Figma 0.1.0](../qa/implementations/stepper.v0.1.0.figma.review.md) `STALE` solo para color; [QA Figma 0.1.1](../qa/implementations/stepper.v0.1.1.figma.review.md) `PASS` técnico: 18 ítems, ocho conectores, 122/122 pinturas vinculadas sin cruce semántico y doce aliases coincidentes con marca en cuatro temas. Los 54 textos/216 bindings y seis controles probados siguen vigentes. Tracking AUD-009 y Caption `*`; biblioteca `UNPUBLISHED`, auditoría humana `PENDING`.

## QA-SEARCH-001

- [Documental](../qa/contracts/search.v0.1.0.review.md) y [Figma](../qa/implementations/search.v0.1.0.figma.review.md): PASS técnico, 2026-09-28. 12 variantes, roles semánticos locales, propiedades probadas y última captura visual aprobada. Contraste con asteriscos; no implica aprobación humana ni validación funcional web.

## QA-TEXTAREA-001

- [Documental](../qa/contracts/textarea.v0.1.0.review.md) y [Figma](../qa/implementations/textarea.v0.1.0.figma.review.md): PASS técnico, 2026-09-28. 4 variantes, roles semánticos locales, propiedades probadas y última captura visual aprobada. Contraste con asteriscos; no implica aprobación humana ni validación funcional web.

## QA-FILE-UPLOAD-001

- [Documental](../qa/contracts/file-upload.v0.1.0.review.md) y [Figma](../qa/implementations/file-upload.v0.1.0.figma.review.md): PASS técnico, 2026-09-28. 6 variantes, roles semánticos locales, propiedades probadas y última captura visual aprobada. Contraste con asteriscos; no implica aprobación humana ni validación funcional web.

## QA-INPUT-FIELD-CONTRACT-001

- **Tipo:** [QA documental](../qa/contracts/input-field.v0.1.0.review.md) PASS. 21 secciones, 30 variantes, doce propiedades, nombres de página/ejes, roles y dependencias explícitos. Corrección de soporte Focus revalidada antes de promover a specs.

## QA-INPUT-FIELD-FIGMA-001

- **Vigente 0.1.1, alcance acotado:** [QA](../qa/implementations/input-field.v0.1.1.figma.review.md) PASS, seis Disabled usan el mismo token de texto; tres cambios exactos, 27 fills de texto conservados y 30 variantes intactas. La aprobación del usuario afecta solo a este color; el QA previo no acredita el nuevo binding de los tres Filled/Disabled.

- **Tipo:** [QA de implementación](../qa/implementations/input-field.v0.1.0.figma.review.md) PASS técnico, 2026-09-28. 306 paints, 14 efectos, 750 bindings tipográficos, 132 aliases y pruebas de edición/visibilidad/ancho; capturas fuente/destino inspeccionadas. Sin nuevos tokens ni primitivas. Contrato en specs, auditoría humana PENDING, biblioteca UNPUBLISHED. Contraste y diferencias tipográficas declarados; no se valida frontend.

## QA-CHAT-TOOLBAR-001 · 2026-10-08

[Documental](../qa/contracts/chat-toolbar.v0.1.0.review.md) y [implementación](../qa/implementations/chat-toolbar.v0.1.0.review.md) PASS técnico:9 variantes,36 roles/144 aliases,136 paints/48 visibles,21 textos. Slots nativos y cuatro temas; controles heredados conservan excepciones propias. Servicios mantiene contraste limitado documentado; no WCAG PASS.

## QA-FUENTES-001 · 2026-10-09

[Documental](../qa/contracts/fuentes.v0.1.0.review.md) y [técnico visual](../qa/implementations/fuentes.v0.1.0.review.md) PASS. [Readback](../qa/implementations/fuentes.v0.1.0.final.json), [verificador](../qa/implementations/fuentes.v0.1.0.verify.cjs), [contraste](../qa/implementations/fuentes.v0.1.0.contrast.json). No equivale a cumplimiento integral WCAG ni aprobación humana. Ruta8px y pares de contraste preservados con asterisco; no recolorear.
