# Continuación · refinamiento · 2026-10-05

## Punto vigente · cierre de Chips

[Filter Chip0.2.1](../specs/components/filter-chip.semantic.amendment.v0.2.1.md) aplicado y [QA](../qa/implementations/filter-chip.semantic.v0.2.1.figma.review.md) PASS: 12 textos y24 vectores usan roles inverse; único token nuevo color/icon/inverse (VariableID:705:122) alias neutral/100 en cuatro modos, sin RGB nuevos. 30 variantes/181 nodos y apariencia conservados; 126 paints auditados, 18 variantes fuente comparables, 12 derivadas aprobadas. JSON histórico intacto. No reabrir Chips para repetir esta revisión; las limitaciones originales no son defectos nuevos. [Estado](../implementations/figma/filter-chip.semantic.v0.2.1.state.json).

La autorización actual cubre continuar refinamientos existentes y actualizar el grafo. El estado del grafo al cierre debe comprobarse en el registro de entorno y el manifiesto del último run, no en las menciones STALE de cortes históricos inferiores. Auditoría humana PENDING; no publicación Figma en este trabajo. Doce logos siguen OMITTED_BY_USER.

## Punto vigente · cierre de Buttons

**Search y el hallazgo de bindings remotos de Buttons están cerrados en sus respectivos alcances.** [Enmienda Buttons0.2.2](../specs/components/button.local-bindings.amendment.v0.2.2.md), [QA](../qa/implementations/button.local-bindings.v0.2.2.figma.review.md) y [estado](../implementations/figma/buttons.local-bindings.v0.2.2.state.json).

- 722 referencias en123nodos sustituidas por nueve roles semánticos locales existentes. Cero referencias remotas/no resolubles en el readback nodal de Buttons. Inventario JSON sin cambios.
- 60variantes/364nodos, geometría, textos, fuentes, pinturas, iconos, API yreacciones intactos; capturas idénticas (0píxeles cambiados). No se crearon variables ni componentes.
- Modal (Footer/Basic/Media/SideBySide) yEmpty states conservan estructura, bindings yoverrides. Sidebar usa Icon Buttons, no Buttons, en las tres raíces inspeccionadas; control sin cambios. No censo global del archivo.
- P-SLOTS: NOT_APPLICABLE para Button por anatomía fija; no se tocaron Slots de anfitriones.
- Auditoría humana PENDING; no se publicó biblioteca. QA acotado a este ajuste, no nueva certificación cromática/WCAG.

**Pendientes ya registrados, no tareas nuevas:** excepciones cromáticas/tipográficas y QA geométrico parcial de los seis sets de Logos permanecen con su alcance histórico; los doce logos omitidos no se reabren. No asumir una nueva familia sin evidencia de la cola. Las decisiones de producto fuera de alcance no se convierten en implementación automática.

Graphify se actualizó y verificó después del primer corte de este archivo, pero queda **STALE_AFTER_BUTTON_LOCAL_BINDINGS** respecto de este cierre; no se regeneró otra vez. Consultar [entorno](environment.md). El historial inferior explica el descubrimiento, no el estado actual.

## Alcance autorizado
Continuar las tareas y contrastarlas con documentación y grafos. Prioridad: resolver inconsistencias concretas, sin reconstruir familias ya cerradas ni reactivar los doce logos omitidos.

## Terminado
- Search: [contrato vigente 0.1.1](../specs/search.contract.v0.1.1.md), [QA documental](../qa/contracts/search.v0.1.1.review.md) y [QA de correspondencia](../qa/implementations/search.v0.1.1.figma.review.md) PASS acotado. DOC-SEARCH-001 cerrado: eliminadas cláusulas ajenas de File Upload/Textarea.
- Lectura actual de fuente1560:44694 y destino418:263: matriz de12 variantes, anatomía y tipografía coherentes;22 variables locales. [Estado](../implementations/figma/search.v0.1.1.state.json).
- Ninguna escritura Figma ni cambio en tokens, colores o geometría. Los contratos/QA0.1.0 permanecen históricos; no usar su prosa cruzada como requisito vigente.

## Histórico · pendiente Buttons antes de 0.2.2
- Set26:81:60 variantes,364 nodos. [Descubrimiento](../qa/implementations/buttons.refinement.v0.1.0.discovery.json):722 referencias a nueve variables remotas, no722 componentes.
- [Definiciones remotas](../qa/implementations/buttons.refinement.v0.1.0.remote-variables.json): spacing/sm, spacing/lg, spacing/xs, radius/md, stroke/xs, stroke/md, font/weight/bold, font/weight/regular y font/family/base.
- Estado: CONFIRMED_FINDING / NOT_IMPLEMENTED. Verificar contrato vigente, aliases y valores resueltos en los cuatro modos frente a equivalentes locales; registrar enmienda antes de modificar. Preservar60 IDs, geometría, propiedades y overrides de consumidores.
- Verificar impacto acotado en consumidores de Modal, Sidebar y Empty states. No asumir que todos heredan sin overrides ni que igualdad de nombre basta para sustituir variables.

## Histórico · grafo y límites del primer corte
Se consultó Graphify mediante query search (budget1300):99 coincidencias,29 mostradas; resultado parcial, contrastado con archivos canónicos y Figma. El índice aún referencia Search0.1.0 y no incorpora deltas de Header/Table/Modal/Sidebar/Empty states.
Estado STALE_AFTER_HEADER_TABLE_MODAL_SIDEBAR_EMPTY_STATES_SEARCH_REFINEMENT; no regenerado. No usarlo como autoridad ni afirmar cobertura exhaustiva. Regeneración requiere autorización específica según AGENTS.

Auditoría humana PENDING; biblioteca UNPUBLISHED según último registro, no publicación remota comprobada en esta revisión. Persisten excepciones de contraste/tipografía y QA parcial de Logos. No decisión adicional necesaria para cerrar DOC-SEARCH-001; Buttons necesita completar preparación técnica, no una aprobación rutinaria por variante.
