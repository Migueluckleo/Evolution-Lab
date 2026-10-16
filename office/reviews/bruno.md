# Autorrevisión de Bruno — construcción

Fecha: 2026-10-16. Perfil: `bruno`. Nombre adoptado: **Bruno**. Ejecución: `/root/office_builder`.

Encargo de Eva: revisar las directrices del constructor y proponer mejoras centradas en mantenimiento consultable, construcción documentada y eficiencia antes de construir. Este informe es una propuesta; no modifica directrices canónicas, componentes, Figma ni skills.

## Fuentes consultadas y preflight

- [Configuración canónica](../config.json): tres directrices actuales de Bruno y directrices comunes.
- [Protocolo de oficina](../OPERATING-PROTOCOL.md): secciones 1–7; preflight, comunicación real, optimización, QA y registro.
- AGENTS.md 0.5.0 suministrado en el encargo: autoridad, cierre técnico y alcance de protocolos.
- [P04](../../protocols/04-FIGMA-CONSTRUCTION.md): secciones 1, 2, 4, 7 y 8; requisitos de escritura, destino de reconstrucción, preparación, recuperación y lectura posterior.
- [P07](../../protocols/07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md): secciones 1, 2, 3, 4 y 6; independencia de Figma, entregables y validación por destino.
- [P08](../../protocols/08-SKILLS-AND-RELEASES.md): secciones 4–6; reutilización, pruebas proporcionales y separación del motor respecto del catálogo remoto.

Se reutilizó la configuración existente y se leyeron secciones pertinentes de protocolos. No hizo falta inspeccionar componentes, consultar Figma, instalar herramientas ni delegar otra revisión. El cambio autorizado aquí es únicamente este informe. Consumo y ahorro de tokens: `UNAVAILABLE`; no hay medición atribuible que permita afirmar una reducción.

## Hallazgos y recomendaciones

### B1 — Preparación comprobable por destino (prioridad alta)

**Observado:** «comprobar capacidades del destino» no hace visible la diferencia entre reconstruir la biblioteca con P04 y consumirla mediante la skill de pantallas. P04 identifica AI-Design-System como destino de reconstrucción; la oficina exige otro archivo explícito para la skill de Figma. Los procedimientos ya distinguen estos casos, pero la directriz abreviada del constructor no apunta a esa decisión.

**Propuesta exacta para la directriz:**

> Antes de escribir, distinguir reconstrucción del DS, consumo en Figma o implementación web; registrar versión de fuentes, operación, destino autorizado y capacidades verificadas según el protocolo aplicable. En consumo Figma, exigir MCP con escritura, archivo explícito distinto de la biblioteca maestra y acceso a los componentes reales; web no exige Figma. Un requisito ausente bloquea solo la operación afectada.

**Beneficio esperado, todavía hipótesis:** descubrir incompatibilidades de destino antes de escribir y evitar preparar una solución que después deba descartarse. Mantener las comprobaciones detalladas en sus protocolos, sin duplicarlas en el perfil.

**Prueba propuesta:** revisar cuatro escenarios: consumo dirigido al maestro, consumo sin capacidad de escritura, reconstrucción autorizada del maestro y trabajo web sin Figma. Los dos primeros deben detener la escritura afectada; el tercero se rige por P04 y sus restantes requisitos; el cuarto no debe quedar bloqueado por Figma. Registrar escrituras intentadas antes de resolver un requisito indispensable: criterio `0`.

### B2 — Reutilización con decisión explícita de existencia (prioridad alta)

**Observado:** Bruno ya prioriza componentes existentes y prohíbe recrearlos para eludir acceso. Falta explicitar qué decisión habilita construir algo nuevo y cómo conservar la evidencia consultada. P08 §4 ya distingue una necesidad no cubierta de un componente inaccesible.

**Propuesta exacta para la directriz:**

> Consultar primero el catálogo vigente del encargo y las implementaciones existentes; registrar componente y versión reutilizados. Distinguir «no cubre la necesidad» de «existe sin acceso». Crear una composición o componente local nuevo solo cuando el DS no cubra la necesidad y el alcance lo permita, documentando la búsqueda y sin promoverlo automáticamente al DS.

**Beneficio esperado, todavía hipótesis:** reducir duplicación de familias y búsquedas repetidas, conservando una referencia breve al mismo corte de datos durante el encargo.

**Prueba propuesta:** verificar una necesidad cubierta y accesible, otra cubierta sin acceso y una no cubierta. La primera reutiliza; la segunda registra el impedimento y no fabrica una sustitución; la tercera documenta cobertura y decisión local. Al repetir el mismo encargo sin cambios materiales se reutiliza el resultado de búsqueda; un nuevo trabajo consulta nuevamente el canal como exige P08 §6. Medir búsquedas repetidas y duplicados evitables en una misión real antes de afirmar ahorro.

### B3 — Plan de evidencia y cierre según el cambio (prioridad media)

**Observado:** «registrar cambios, IDs reales y pruebas» no explicita lectura posterior ni diferencias entre compilación, QA visual y vigencia de consumo. P04 §8 exige lectura después de cada lote significativo; P07 separa QA por destino; P08 §6 evita actualizar el motor por cambios compatibles únicamente del contenido.

**Propuesta exacta para la directriz:**

> Preparar antes de construir un plan breve de cambios, dependencias y comprobaciones posteriores; ejecutar lotes verificables y leer el resultado real. Revalidar lo afectado y sus consumidores relevantes, conservando evidencia vigente de lo independiente. Distinguir compilación, QA funcional o visual y publicación consumible; al cerrar cambios DS aplicar P08, actualizando catálogo o motor según lo que cambió.

**Beneficio esperado, todavía hipótesis:** evitar pruebas indiscriminadas, omisiones de cierre y reinstalaciones innecesarias. Esta directriz no permite omitir pruebas obligatorias ni asumir que un hash sin cambios demuestra por sí solo equivalencia del entorno.

**Prueba propuesta:** para un cambio acotado, enumerar requisitos y dependencias afectadas antes de editar y contrastar esa lista con la evidencia final. El cierre debe identificar pruebas ejecutadas y límites por destino. Un cambio solo de contenido compatible conserva la versión del motor, valida el catálogo y comprueba el consumo; un cambio del motor exige sus pruebas y entrega correspondientes. Los controles obligatorios sin evidencia no reciben `PASS`.

## Comparación y límites

Las tres oportunidades se apoyan en requisitos ya existentes; el defecto observado es su poca precisión en las directrices del perfil, no una falla demostrada de una construcción. La referencia disponible es el perfil de tres directrices antes de esta revisión. Coste de coordinación, duración de construcción, tokens y retrabajo comparables: `UNAVAILABLE`.

Se recomienda integrar B1 y B2 primero por su efecto sobre destino y reutilización, y B3 como condición de entrega. No se ejecutaron los escenarios propuestos: estado `NOT_RUN`. Las propuestas no habilitan reconstrucción, publicación, instalaciones ni agentes permanentes. La revisión humana rutinaria continúa siendo opcional y no bloqueante; los requisitos técnicos siguen vigentes.

## Registro del encargo

Bruno comunicó a Eva su nombre y las tres oportunidades candidatas mediante la herramienta de coordinación; no solicitó acciones a otros perfiles. Entregable: este informe. Cambios realizados: únicamente `office/reviews/bruno.md`. Integración de directrices, registro de eventos y cierre del grafo quedan a cargo de Eva dentro del lote de revisión de todos los perfiles.
