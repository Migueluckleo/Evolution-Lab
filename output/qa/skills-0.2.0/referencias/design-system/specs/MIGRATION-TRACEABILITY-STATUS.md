# Cobertura de trazabilidad · Librería anterior → AI Design System

## Chat · readback de ajustes del usuario · 2026-10-09

[Enmienda de layout0.1.1](components/chat.layout.amendment.v0.1.1.md) y [estado](../implementations/figma/chat-layout.v0.1.1.state.json) actualizan el alcance de Section/Toolbar: width816, sizing y scroll. Documentación/readback completados; QA interactivo PARTIAL, sin reusar PASS históricos para atributos cambiados. No variables nuevas ni cambios Figma. [Continuidad](../registry/SESSION-HANDOFF-2026-10-09-CHAT-LAYOUT.md). Las secciones0.1.0 inferiores conservan el cierre histórico de los requisitos no modificados.

## Incorporación Characters · 2026-10-08

[Contrato](characters.contract.v0.1.0.md) en specs y [QA](../qa/implementations/characters.v0.1.0.review.md) PASS técnico. Characters820:7, dos sets6+7 frames,13 transiciones,47 bindings y una variable de identidad. Inventario intacto. [Continuidad](../registry/SESSION-HANDOFF-2026-10-08-CHARACTERS.md); auditoría PENDING, biblioteca UNPUBLISHED.

## Incorporación externa: Chat Section · 2026-10-08

Anticipa20355:74859 no pertenece a la Librería raíz. [CHAT-SECTION-0010.1.0](chat-section.contract.v0.1.0.md) construido en página Chat, con QA técnico/documental PASS;39 roles/156 aliases y tres tokens de identidad existentes alineados. Slots propios REQUIRED/IMPLEMENTED. Publicado documentalmente en specs, DELEGATED_FOR_BUILD/user_auditPENDING por excepciones. [Estado](../implementations/figma/chat-section.v0.1.0.state.json), [handoff](../registry/SESSION-HANDOFF-2026-10-08-CHAT.md). Sin publicación remota ni nueva familia iniciada.

## Conversation · identidad fija vigente · 2026-10-08

[Enmienda de personajes0.1.1](components/conversation.character-identity.amendment.v0.1.1.md) implementada: tres variables directas nuevas en colección fija, colores originales preservados en cuatro temas. El conteo inferior de cero variables nuevas es histórico0.1.0; el resto de UI sigue semántico. QA acotado PASS, sin publicación de biblioteca; grafo STALE.

## Incorporación externa · Conversation · 2026-10-08

Anticipa20355:72763 incorporado por delegación explícita externa. [Contrato](conversation.contract.v0.1.0.md), [estado](../implementations/figma/conversation.v0.1.0.state.json), [QA](../qa/implementations/conversation.v0.1.0.review.md): PASS técnico, siete principales/cuatro configuraciones, doce Slots,40 roles/160 aliases y cuatro temas cotejados. Cero variables nuevas. Auditoría humana por excepciones PENDING, biblioteca UNPUBLISHED. No reabre el inventario de la Librería raíz ni propuestas restantes de Anticipa; Graphify STALE para esta incorporación, sin regeneración.

## Incorporación adicional solicitada · App Shell · 2026-10-06

Nodo fuente Breakpoints8284:12565 integrado como **App Shell**, página737:303/main737:304. [Contrato en specs](app-shell.contract.v0.1.0.md) y [QA](../qa/implementations/app-shell.v0.1.0.figma.review.md) PASS técnico: Header/Sidebar DS reutilizados, Content Slot nativo,37bindings propios,60pinturas y93definiciones verificadas;sin tokens nuevos. No afecta cierres anteriores ni agrega tareas de refinamiento. Auditoría humana PENDING por excepciones heredadas; no publicación de biblioteca. Anticipa screen composition permanece DRAFT independiente. Grafo STALE.

## Paso 4 · promoción a specs · 2026-10-06

**19 enmiendas promovidas** con QA documental/técnico del alcance cerrado:13 Foundations, una Buttons, una Avatar y cuatro Toggle. [Índice y QA](../qa/contracts/specs-promotion.2026-10-06.review.md), [verificación](../qa/contracts/specs-promotion.2026-10-06.verification.json). Rutas previas son punteros; datos JSON y QA históricos intactos. Los campos sustituidos remiten a sus enmiendas vigentes; no se reactivan ajustes de contraste históricos.

**Bases aún sin promoción:** Tooltip (AUD-004), Toggle (AUD-003 y revisión transversal), Avatar (AUD-006), Logos (57 deltas sin aceptación). Son asuntos ya registrados, no tareas añadidas. Las demás bases cerradas ya están en specs. Publicar enmiendas acotadas no certifica estas cuatro familias completas. No hubo cambios Figma ni publicación de biblioteca; Graphify sigue STALE.

## Paso3 · Logos verificado, decisión requerida · 2026-10-06

[Refinamiento ejecutado](../qa/implementations/logos.refinement.v0.1.1.review.md): seis sets/72 variantes intactos;57 deltas geométricos ya conocidos, máximo0.00030517578125px. Dos pruebas seguras en clones no acreditaron igualdad; clones retirados. No hay nueva cola técnica: falta aceptar o rechazar esta excepción concreta para cerrar y promover Logos. No inventar tolerancia ni repetir el diagnóstico sin nueva evidencia. Puntos1/2 cerrados, doce logos omitidos, publicación y auditoría interna separadas.

## Cierre del punto2 · Radio Buttons y Checkboxes · 2026-10-06

**PASS técnico del cotejo restante**, [QA](../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md): anatomía,40 etiquetas/200 bindings,22 roles/88 modos,80 casos y20 cambios de variante. Ocho posiciones Checkbox corregidas; Radio no necesitó cambios. Bases y enmiendas cromáticas en specs. Auditoría humana PENDING, biblioteca no publicada. No repetir esta revisión.

**Restante técnico de aquella lista:** solo la discrepancia geométrica documentada de los seis sets Logos. Excepciones del equipo y publicación siguen separadas. No se añaden pendientes.

## Cierre del punto 1 · colores, tokens y bindings · 2026-10-05

Las seis familias Buttons, Icon Buttons, Breadcrumbs, Metric Cards, Charts y Linear Progress Bars quedan **PASS técnico cromático**:832 pinturas,84 definiciones canónicas,42 bindings corregidos, ocho roles actualizados y cuatro roles nuevos, sin primitivas nuevas. Geometría/API intactas. [Enmienda](components/six-family-color.amendment.v0.1.0.md), [QA](../qa/implementations/six-families.color.v0.1.0.review.md). Bases promovidas a specs; auditoría humana PENDING. Contraste original marcado con asterisco y gris Charts aproximado. No se publicó biblioteca.

**Corte histórico al terminar el punto1:** quedaban Radio Buttons/Checkboxes y seis sets Logos. Radio/Checkbox se cerraron en el punto2 del2026-10-06, indicado arriba. Las decisiones del equipo y publicación mantienen su alcance separado.

## Histórico · lista operativa conciliada antes de este cierre · 2026-10-05

Solicitada por el usuario después del cierre Chips0.2.1. Esta lista consolida trabajo ya registrado; no añade familias, no convierte una revisión pendiente en un defecto demostrado y no modifica requisitos. Los cortes fechados inferiores son historial, no colas acumulativas. Las evidencias se contrastaron documentalmente; no hubo nueva lectura ni modificación Figma en esta conciliación.

### Trabajo técnico restante

| Orden | Familia | Trabajo pendiente ya registrado | Qué no repetir |
|---|---|---|---|
| 1 | Buttons e Icon Buttons | Completar el cotejo cromático fuente→rol→alias→binding de sus estados. Buttons conserva su cierre acotado0.2.2; Icon Buttons requiere revisar estados/fondos según la matriz. | No repetir los722bindings locales de Buttons ni reconstruir sus consumidores. |
| 2 | Breadcrumbs y Metric Cards | Verificar Current/tendencia, especialmente Servicios, contra color fuente y JSON; corregir solo diferencias comprobadas y registrar contraste sin recolorear por umbral. | Slots de Breadcrumbs ya validados; no reconstruir composición. |
| 3 | Charts y Linear Progress Bars | Cotejar series/gauge/leyendas y segmentos/pista; resolver la aproximación tokenizada de literales únicamente con primitivas existentes y documentar la diferencia. | El80% sigue siendo demo; Slots de leyendas y construcción de Progress ya tienen QA propio. |
| 4 | Radio Buttons y Checkboxes | Completar la comparación transversal de anatomía, tipografía y demás consumidores no cubiertos por el QA acotado de contornos. | Los tres contornos neutral/400 y sus aliases ya fueron restaurados. |
| 5 | Logos, solo seis sets copiados | Cerrar la discrepancia geométrica documentada de hasta0.00030517578125px sin inventar tolerancia. Si no puede corregirse preservando artwork, requiere aceptación explícita de esa diferencia. | No copiar los doce assets OMITTED_BY_USER, no añadir tokens, no repetir la integración de logos en Header. |

Los cuatro primeros renglones agrupan **ocho familias existentes**, no ocho construcciones nuevas. La promoción a specs de bases/enmiendas que aún permanecen en drafts es parte del cierre de su propia familia, una vez cubierto el QA vigente; no es otra ronda de aprobación por componente. [Registro de contratos](../registry/contracts.md).

### Revisión por excepciones, no implementación automática

- Tooltips (AUD-004), Toggles (AUD-003) y Avatars (AUD-006): los QA enlazados en la matriz inferior dejan diferencias tipográficas o de halo explícitas. No declarar PASS transversal total ni modificar valores compartidos por conjetura. La regla vigente de primitiva semejante sigue prevaleciendo; no se interpreta la pregunta histórica de AUD-003 como permiso para crear otra primitiva.
- Equipo: contraste marcado con `*`, normalizaciones de tipografía/geometría y TABLE-AUD-001 (Hover1288 frente1280). Las decisiones y diferencias completas se conservan únicamente en [auditoría por excepciones](MIGRATION-AUDIT.md), sin un segundo catálogo editable aquí.
- Diferidos de baja prioridad: Scrollbar75%, contextos On Primary de Steps y tracking de Stepper (AUD-007–009). No bloquean el refinamiento actual ni autorizan rediseño.
- Publicación de biblioteca Figma: último estado registrado UNPUBLISHED; no equivale a specs. Preparar el alcance de entrega y publicar lo técnicamente cerrado cuando corresponda; esta conciliación no ejecutó ni verificó una publicación remota.

### Cerrado o fuera de la cola

Chips0.2.1, DOC-SEARCH-001, bindings remotos de Buttons, Input Field Disabled, Slots implementados, Select Closed/Open, Navigation (cuatro subfamilias), Header, Table, Modal, Sidebar y Empty states no son construcciones pendientes. Conservan sus excepciones y alcances propios, no se les atribuye QA global por esta lista. Loader, Steps y Stepper mantienen sus cierres técnicos registrados. No se añaden familias desconocidas a partir de las28páginas del inventario preliminar.

Los doce logos omitidos quedan fuera de alcance. Frontend, reglas de producto, teclado, datos vivos y responsive no definidos pertenecen a una fase futura no autorizada como implementación actual. Los placeholders y ejemplos no son defectos nuevos.

**Trabajo realizado en esta conciliación:** separadas las colas históricas, actualizada referencia Search0.1.1, corregidos estados Slots de Sidebar/Empty states y aclarado el cierre de integración de logos en Header. Ningún cambio de contrato normativo, JSON, token o componente. Ver [registro de QA](../registry/qa.md).

## Cola vigente de refinamiento · 2026-10-05

**Chips: refinamiento semántico y cotejo cromático cerrados.** [Enmienda0.2.1](components/filter-chip.semantic.amendment.v0.2.1.md), [QA](../qa/implementations/filter-chip.semantic.v0.2.1.figma.review.md): 36 bindings inversos, 126 paints efectivos, 47 definiciones canónicas y una extensión de icono verificados; 18 variantes/75 paints coinciden con la fuente y 12 derivadas conservan recetas aprobadas. 30 variantes intactas, sin cambio de colores. Sustituye el PENDING histórico de Chips en este alcance. No es aprobación WCAG ni publicación remota.

**DOC-SEARCH-001 cerrado documentalmente** mediante [Search0.1.1](search.contract.v0.1.1.md) y [QA acotado](../qa/implementations/search.v0.1.1.figma.review.md).12 variantes y22 variables locales confirmadas; cero escrituras Figma. No equivale a repetir la auditoría completa de aliases, temas o contraste.

**Buttons: hallazgo de bindings externos cerrado.** [Enmienda0.2.2](components/button.local-bindings.amendment.v0.2.2.md) aplicada al set26:81:722referencias en123nodos ahora consumen nueve roles semánticos locales verificados contra JSON y cuatro modos.60variantes/364nodos conservados; cero píxeles cambiados. [QA acotado](../qa/implementations/button.local-bindings.v0.2.2.figma.review.md): cero variables remotas/no resolubles en el readback nodal; consumidoresModal/Empty states sin regresiones. Sidebar no consume Buttons en las raíces verificadas.

Esta cola sustituye DOC-SEARCH-001 y el hallazgo abierto de Buttons de cortes anteriores, no sus evidencias. No introduce nuevas familias/tareas. Persisten excepciones cromáticas/tipográficas y QA parcial de los seis sets de Logos; doce assets OMITTED_BY_USER. Graphify CURRENT incorpora los cierres de Buttons y Chips; [verificación del corte](../graphify-out/runs/2026-10-05-refinement-close/verification.json). [Continuación](../registry/SESSION-HANDOFF-2026-10-05-REFINEMENT.md). El PASS acotado de bindings de Buttons no completa por sí solo su revisión cromática global histórica.

## Histórico · estado tras Empty states · 2026-10-05

**Empty states terminado técnicamente.** Página639:128, set645:275: cuatro variantes, seis artworks ydosSlots por variante. [Contrato](empty-states.contract.v0.1.0.md), [QA](../qa/implementations/empty-states.v0.1.0.figma.review.md), [continuación](../registry/SESSION-HANDOFF-2026-10-05-EMPTY-STATES.md).31roles/124aliases,264comparaciones de tema; seisroles nuevos, cero primitivas. Paleta decorativa aproximada, tipografía normalizada yServicios3.236:1* explícitos.

Sigue **DOC-SEARCH-001** y consolidación de excepciones cromáticas, no reconstrucción de Sidebar/Empty states ya cerrados. AuditoríaPENDING ybibliotecaUNPUBLISHED. El inventario preliminar28páginas no equivale a cobertura exhaustiva de todos los nodos.12logos OMITTED_BY_USER. GraphifySTALE_AFTER_HEADER_TABLE_MODAL_SIDEBAR_EMPTY_STATES; no regenerado. Esta cola sustituye las pendientes históricas inferiores, sin borrar su evidencia.

## Histórico · estado tras Sidebar · 2026-10-05

**Sidebar terminado técnicamente; sigue Empty states.** Página614:125, Menu Item615:355 (22variantes), Sidebar619:480 (dos) yTop bar619:607. [Contrato en specs](sidebar.contract.v0.1.0.md), [QA](../qa/implementations/sidebar.v0.1.0.figma.review.md), [continuación](../registry/SESSION-HANDOFF-2026-10-05-SIDEBAR.md).141paints,42variables,576comparaciones de tema; Slots ytexto largo probados. Tres roles semánticos nuevos, ninguna primitiva. Contraste original y límites de composición documentados. AuditoríaPENDING, bibliotecaUNPUBLISHED. Esta cola sustituye las menciones históricas deSidebar pendiente; no cierra excepciones de otras familias niDOC-SEARCH-001. GraphifySTALE_AFTER_HEADER_TABLE_MODAL_SIDEBAR.

## Histórico · estado tras Modal · 2026-10-01

Modal ya está construido desde la Librería raíz: página565:122, Basic567:360,Media569:301,SideBySide569:327; [contrato](modal.contract.v0.1.0.md) en specs y [QA](../qa/implementations/modal.v0.1.0.figma.review.md) técnico PASS. Slots y34 tokens/136 aliases verificados; cero variables nuevas. **Sigue Sidebar, después Empty states**. Esta cola sustituye los pendientes históricos deModal/Table de abajo. Excepciones cromáticas ydocumentales generales siguen separadas; no repetir una auditoría global como gate. [Continuación](../registry/SESSION-HANDOFF-2026-10-01-MODAL.md). GraphifySTALE_AFTER_HEADER_TABLE_MODAL; bibliotecaUNPUBLISHED, auditoríaPENDING.

## Histórico · estado tras Table · 2026-10-01

Table ya está construida desde Anticipa por instrucción explícita: página546:122/main548:895, [contrato](table.contract.v0.1.0.md), [QA](../qa/implementations/table.v0.1.0.figma.review.md). Slots y36tokens/144aliases validados, cero tokens nuevos; auditoría humanaPENDING. La siguiente familia es **Modal**, despuésSidebar yEmpty states. Esta cola sustituye las referencias históricas a Tablependiente de abajo. No incluye otros componentes de Anticipa ni los logos omitidos. Graphify sigue STALE por deltasHeader/Table; no se regeneró.

## Histórico · estado consolidado · 2026-10-01

Estado actualizado tras construir Header y leer su resultado en Figma. Esta sección sustituye las colas operativas históricas de abajo, no sus evidencias ni resultados acotados.

- **Header terminado técnicamente:** página518:122, componente518:123, SlotActions518:124; [contrato en specs](header.contract.v0.1.0.md) y [QA](../qa/implementations/header.v0.1.0.figma.review.md). Tres roles semánticos nuevos sin primitivas, cuatro temas y Slots0/1/3/5/7 probados. Contraste y límites Desktop documentados; auditoría humana PENDING. **Construcción siguiente: Table**, sin repetir QA global. [Continuación](../registry/SESSION-HANDOFF-2026-10-01-HEADER.md).
- **Familias aún por delimitar y construir:** Table, Modal, Sidebar y Empty states. P-SLOTS permanece UNRESOLVED hasta inspeccionar su anatomía. El inventario de 28 páginas es preliminar; no es un recuento definitivo de componentes pendientes.
- **Select Closed/Open ya construido**, además de Dropdown Item; no repetir su construcción. Contrato base en specs y QA propio, seguidos de la enmienda de Slots.
- **Cola de seis composiciones Slots completada:** Select, Switch Tab, Breadcrumbs, Steps, Pagination y Charts; véase [registro vigente de adopción](../registry/SLOTS-REVIEW-STATUS.md). Su PASS no revalida automáticamente paletas ni comportamientos de producto.
- **Revisión transversal separada:** conservar PENDING/IN_PROGRESS de la matriz cromática y [excepciones](MIGRATION-AUDIT.md). No convertirlas en componentes por construir ni repetir QA global como requisito para Header.
- **DOC-SEARCH-001:** reapertura acotada de revisión documental por cláusulas cruzadas de File Upload/Textarea dentro de Search y sus QA. Su PASS técnico histórico no resuelve la contradicción; corregir versionadamente antes de reutilizar esas cláusulas, sin asumir un fallo Figma ni bloquear Header. Véase la auditoría enlazada.
- **Logos:** seis sets existentes con QA global parcial; doce assets restantes OMITTED_BY_USER. La integración de los cuatro artworks de categoría en Header ya fue comprobada sin cambiar sus colores ni geometría principal; no equivale a cerrar el resto de Logos.
- **Publicación:** specs es la ubicación normativa de los contratos promovidos; no implica aprobación humana ni publicación de biblioteca Figma. Los últimos registros dejan auditoría PENDING y biblioteca UNPUBLISHED.

El estado operativo de Graphify se consulta en [entorno](../registry/environment.md); las menciones STALE en cortes históricos describen su fecha, no el resultado de una actualización posterior.

## Actualización 2026-09-30 · cierre de la cola Slots

[COMPOSITION-SLOTS-002](composition-slots.amendment.v0.1.1.md) implementa y valida Steps/Gallery, Pagination/Pages y leyendas Charts. Sustituye el pendiente de Slots del resumen del 29/09, no sus demás estados históricos. [QA y excepciones](../qa/implementations/composition-slots.v0.1.1.figma.review.md). Pagination añade aliases contextuales de estado documentados; colores originales comprobados iguales en 200 pares y los cuatro temas. La paleta histórica de Charts sigue pendiente de su revisión separada. Próxima familia de migración: Header, sin repetir QA global de lo ya cerrado.

## Historial 2026-09-29 · Slots (cola sustituida por el cierre del 30/09)

[COMPOSITION-SLOTS-001](composition-slots.amendment.v0.1.0.md) añade Slots nativos validados en Select, Switch Tab y Breadcrumbs, sin cambios de paleta ni JSON. Este PASS corresponde a composición y herencia comprobadas, no promueve revisiones cromáticas pendientes de la matriz histórica. [Adopción por familia y cola restante](../registry/SLOTS-REVIEW-STATUS.md). Steps/Gallery, Pagination/Pages y leyendas Charts aún no tienen Slot validado; la migración continúa desde esa cola antes de Header.

## Actualización 2026-09-29 · Select

Composiciones Closed/Open construidas y [contrato en specs](select.contract.v0.1.0.md). Set457:470, página444:122; QA técnico acotado PASS. Se suma al Dropdown Item ya completado, no lo reemplaza.29variables verificadas en cuatro modos,70pinturas consumidoras vinculadas. Sombras literales y métricas numéricas de etiquetas ocultas escaladas heredadas documentadas; no tokenización integral. Biblioteca no publicada; auditoría humana PENDING. Esta actualización sustituye únicamente el pendiente histórico de composición Select; Header es siguiente familia a inspeccionar. Logos restantes omitidos.

**Corte inicial:** 2026-09-24. **Regla:** [MIGRATION-TOKEN-TRACEABILITY-001](MIGRATION-TOKEN-TRACEABILITY.contract.md). Esta matriz distingue existencia de contratos/QA históricos de una **revalidación vigente** de color, alias y binding real. `PENDING` no invalida por sí solo una estructura ya validada; indica que todavía no se ha demostrado la cadena completa bajo la decisión reciente de fidelidad cromática. No sustituye el [registro de contratos](../registry/contracts.md) ni la [auditoría por excepciones](MIGRATION-AUDIT.md).

| Familia existente | Contrato registrado | Revalidación transversal | Observación inicial |
|---|---|---|---|
| Buttons | Sí | PASS técnico cromático 2026-10-05 | [QA de seis familias](../qa/implementations/six-families.color.v0.1.0.review.md). Fuente→JSON→alias→binding cotejados en cuatro temas; contraste* y excepciones de alcance explícitas. |
| Chips / Filter Chip | Sí | PASS técnico 0.2.1 | [Enmienda semántica](components/filter-chip.semantic.amendment.v0.2.1.md) y [QA](../qa/implementations/filter-chip.semantic.v0.2.1.figma.review.md):126paints efectivos,47definiciones canónicas y extensión inverse-icon verificados;36bindings corregidos sin cambio visual.18variantes/75paints coinciden con la fuente;12derivadas conservan recetas aprobadas. Contraste Administrativo Hover limitado*, auditoría humana PENDING. |
| Tooltips | Sí | IN_PROGRESS | Doce paints y aliases de color verificados contra fuente/JSON/Figma. Normalización de interlineado/tracking documentada pero no idéntica: AUD-004. |
| Badges | Sí | PASS técnico | Seis variantes, 19 paints visibles y seis etiquetas contrastados con fuente; 17 roles/25 consumidores con scope y alias revisados. Colores originales restaurados; limitaciones `*`, auditoría humana PENDING. |
| Toggles | Sí | IN_PROGRESS | Dos bordes Off restaurados y QA acotado PASS; fills/strokes heredados coinciden en RGB. Halo Focus fuente `#F8FAFC` sin primitiva exacta: AUD-003 abierto. Mixed mantiene QA propio. |
| Radio Buttons | Sí | REVALIDATED | [QA0.1.2](../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md) PASS técnico: anatomía, etiquetas y tokens comparados; normalizaciones explícitas, contorno neutral/400 conservado. Contrato en specs; auditoría PENDING. |
| Checkboxes | Sí | REVALIDATED | [QA0.1.2](../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md) PASS técnico: ocho posiciones restauradas, pruebas de instancias y no regresión; dos contornos neutral/400 conservados. Contrato en specs; auditoría PENDING. |
| Dots | Sí | PASS técnico | Quince variantes y 36 paints visibles igualan RGB fuente; siete roles con categorías correctas. Borde Inactive blanco restaurado mediante alias a primitiva existente; limitación `*`, auditoría humana PENDING. |
| Avatars | Sí | IN_PROGRESS | Fondo Icon/Text de Servicios restaurado a orange/500 con ocho bindings y cuatro aliases verificados; Dot y texto preservados. Tamaños de iniciales 6/9→10/12 px pendientes de criterio: AUD-006. |
| Inline Notifications | Sí | PASS técnico | Cinco variantes: fondos, iconos, títulos, cierres y descripción base verificados; Warning amber/600 restaurado. Pseudoenlace fuente sin URL omitido según contrato; contraste `*`, auditoría humana PENDING. |
| Icon Buttons | Sí | PASS técnico cromático 2026-10-05 | [QA de seis familias](../qa/implementations/six-families.color.v0.1.0.review.md). Fuente→JSON→alias→binding cotejados en cuatro temas; contraste* y excepciones de alcance explícitas. |
| Breadcrumbs | Sí | PASS técnico cromático 2026-10-05 | [QA de seis familias](../qa/implementations/six-families.color.v0.1.0.review.md). Fuente→JSON→alias→binding cotejados en cuatro temas; contraste* y excepciones de alcance explícitas. |
| Metric Cards | Sí | PASS técnico cromático 2026-10-05 | [QA de seis familias](../qa/implementations/six-families.color.v0.1.0.review.md). Fuente→JSON→alias→binding cotejados en cuatro temas; contraste* y excepciones de alcance explícitas. |
| Charts | Sí | PASS técnico cromático 2026-10-05 | [QA de seis familias](../qa/implementations/six-families.color.v0.1.0.review.md). Fuente→JSON→alias→binding cotejados en cuatro temas; contraste* y excepciones de alcance explícitas. |
| Linear Progress Bars | Sí | PASS técnico cromático 2026-10-05 | [QA de seis familias](../qa/implementations/six-families.color.v0.1.0.review.md). Fuente→JSON→alias→binding cotejados en cuatro temas; contraste* y excepciones de alcance explícitas. |
| Navigation · Switch Tab Item, Switch Tab, Pagination y Tab | Sí | PASS técnico de cuatro subfamilias | [Item](navigation-switch-tab-item.contract.v0.1.0.md), [composición](navigation-switch-tab.contract.v0.1.0.md), [Pagination](navigation-pagination.contract.v0.1.0.md) y [Tab](navigation-tab.contract.v0.1.0.md) con QA propio cubren variantes, propiedades, dependencias y cadena cromática fuente→primitiva→token→binding. Las extensiones específicas de borde de Pagination y Tab coinciden entre JSON y Figma. No presupone que cualquier otra pieza de la página fuente esté migrada. |
| Scrollbars | Sí | PASS técnico 0.1.1 | [Contrato base](scrollbar.contract.v0.1.0.md), [enmienda cromática](scrollbar.color-approximation.amendment.v0.1.1.md) y [QA vigente](../qa/implementations/scrollbar.v0.1.1.figma.review.md): rol semántico aliasa neutral/300 existente, 30/30 bindings y diferencia visual `#C3C6D4`→`#E2E8F0` documentados. Primitiva 350 retirada de inventario local. Contraste `*` y AUD-007 de baja prioridad; Figma `UNPUBLISHED`. |
| Steps | Sí | PASS técnico 0.1.1 | [Contrato base](steps.contract.v0.1.0.md), [enmienda de marca](steps.brand-theme.amendment.v0.1.1.md) y [QA vigente](../qa/implementations/steps.v0.1.1.figma.review.md): 6 variantes públicas, 4 Dot, 27 Combination; 173/173 pinturas vinculadas y 28/28 aliases en cuatro modos. Tres acentos ahora siguen marca base/escala 300 por tema, sin variables/primitivas nuevas. Anomalía On Primary y aproximaciones en AUD-008; Figma `UNPUBLISHED`. |
| Steppers / Multi Step Indicator | Sí | PASS técnico 0.1.1 | [Contrato base](stepper.contract.v0.1.0.md), [enmienda de marca](stepper.brand-theme.amendment.v0.1.1.md) y [QA vigente](../qa/implementations/stepper.v0.1.1.figma.review.md): 18 ítems, 8 conectores; 122/122 pinturas con binding y doce aliases de acento coincidentes con marca base/fuerte en cuatro modos. El verde/azul fijo fuente se sustituye por instrucción posterior. Textos editables y 216 bindings tipográficos previos; tracking literal AUD-009, caption `*`; Figma `UNPUBLISHED`. |
| Loaders | Sí | PASS técnico 0.1.0 | [Contrato](loader.contract.v0.1.0.md) y [QA](../qa/implementations/loader.v0.1.0.figma.review.md): 16 variantes públicas, 16 ciclos de 24, 384/384 transiciones y 768/768 pinturas semánticas. Marca Primary por tema; tres colores alternativos conservan su rol durante todo el ciclo, corrigiendo un salto cromático de la fuente. Auditoría humana PENDING; Figma UNPUBLISHED. |
| Input Fields · Input Field | Sí | PASS técnico 0.1.1 | [Base](input-field.contract.v0.1.0.md) + [enmienda Disabled aprobada](input-field.disabled-text.amendment.v0.1.1.md); [QA acotado actual](../qa/implementations/input-field.v0.1.1.figma.review.md): seis Disabled usan color/text/disabled, solo tres fills modificados. Los 30 IDs, propiedades y dimensiones se conservan. QA base de 306 paints/14 efectos/750 bindings permanece histórico para lo no afectado. Sin nuevas variables; auditoría restante PENDING, Figma UNPUBLISHED. |
| Input Fields · Search | Sí | PASS documental y correspondencia 0.1.1 | [Contrato vigente](search.contract.v0.1.1.md), [QA acotado](../qa/implementations/search.v0.1.1.figma.review.md):12variantes/22variables, DOC-SEARCH-001 cerrado sin escritura Figma. Conteos82paints/3efectos/120bindings del QA0.1.0 son históricos, no una nueva auditoría cromática. |
| Input Fields · Textarea | Sí | PASS técnico 0.1.0 | [Contrato](textarea.contract.v0.1.0.md), set419:247: 4 variantes, 29 paints y 80 bindings tipográficos. Contador estático editable; alto160 preservado. |
| Input Fields · File Upload | Sí | PASS técnico 0.1.0 | [Contrato](file-upload.contract.v0.1.0.md), set420:320: 6 variantes, 78 paints y 160 bindings tipográficos, incluidos botones/iconos ocultos. Button local reutilizado, cuatro modos comprobados. Formatos/50MB/progreso son ejemplos. |

**Select · Dropdown Item — PASS técnico:** [contrato en specs](dropdown-item.contract.v0.1.0.md) y [QA](../qa/implementations/dropdown-item.v0.1.0.figma.review.md). Página444:122, set446:528; 18 variantes, 10 propiedades editables, 180 conexiones y 186 pinturas. Los 24 roles se cotejaron en cuatro modos; sin tokens nuevos. Composiciones Select abierta/cerrada aún pendientes, no incluidas en este PASS. [Punto de continuación](../registry/SESSION-HANDOFF-2026-09-28-SELECT.md).

La fuente [inventariada](../sources/figma-snapshots/legacy-library-pages.inventory.md) tiene 28 páginas preliminares, algunas con varias familias. Siguen pendientes Header ([descubrimiento inicial](../drafts/reports/header.discovery.v0.1.0.md)), composiciones de Select, Table, Modal, Sidebar y Empty states; también cualquier pieza de Navigation no identificada por el inventario profundo. Logos conserva seis sets con 72 variantes; los doce assets sueltos restantes fueron omitidos por el usuario, no bloquean esta lista. Su QA geométrico global sigue sin cerrar. Las cuatro subfamilias de Input Fields no deben repetirse. Esta lista depende de la fuente real, no promete variantes inferidas. Auditoría humana PENDING y biblioteca UNPUBLISHED.

**Excepción exclusiva de Logos:** [DEC-LOGOS-AGNOSTIC-ASSETS-001](../registry/decisions.md) exige assets fieles sin tokens. El [contrato](../drafts/contracts/logos.contract.v0.1.0.md) pasó QA documental; la [revisión parcial](../qa/implementations/logos.v0.1.0.figma.review.md) verifica cero bindings y cuatro dependencias locales, pero no PASS global. DEC-LOGOS-REMAINDER-OMITTED-001 excluye del trabajo actual los doce frames pendientes: no solicitar login para copiarlos ni bloquear otras familias. Conservar diferencias geométricas registradas y los seis sets existentes. La excepción agnóstica no se extiende a su UI consumidora. [Historial](../registry/SESSION-HANDOFF-2026-09-28-LOGOS.md). Graphify sigue STALE.

## Evidencia para cambiar `PENDING` a `PASS`

Registrar contrato/enmiendas vigentes y digests; tabla origen→rol→variable local por propiedad y estado; aliases y scopes por modo; readback Figma posterior a cualquier corrección; comparación cromática y captura; QA técnico actualizado; excepciones `*` y estado de auditoría humana por separado. Un hallazgo `CONFLICT` detiene solo el alcance afectado y se enlaza en la auditoría.

## Incorporación externa Chat Toolbar · cierre2026-10-08

Cerrado técnicamente el nodo20355:72872 y dependencias20355:72830/72852. [Toolbar](./chat-toolbar.contract.v0.1.0.md), [Tool Item](./chat-tool-item.contract.v0.1.0.md), [History Item](./chat-history-item.contract.v0.1.0.md) en specs con QA PASS. Nueve variantes, Slots y tokens locales; cero tokens nuevos. [Handoff vigente para este lote](../registry/SESSION-HANDOFF-2026-10-08-CHAT-TOOLBAR.md). No se añaden tareas especulativas; publicación remota y auditoría humana no se confunden con cierre técnico.

## Incorporación externa Fuentes · 2026-10-09

[Contrato](components/fuentes.contract.v0.1.0.md) y [Foundations](foundations/fuentes-hover.contract.v0.1.0.md) en specs; [QA](../qa/implementations/fuentes.v0.1.0.review.md) PASS técnico visual. Dos variantes, Path Slot,22 bindings cromáticos,19 roles existentes y un nuevo Hover en cuatro marcas; inventario canónico intacto. [Estado](../implementations/figma/fuentes.v0.1.0.state.json). Humana PENDING, biblioteca NOT_PERFORMED; no reabre familias anteriores. Vigencia del grafo: [cierre del lote](../graphify-out/runs/2026-10-09-fuentes/closure.json).
