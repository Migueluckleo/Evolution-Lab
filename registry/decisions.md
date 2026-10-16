# Registro de decisiones

## DEC-TYPOGRAPHY-STYLES-001 · mecanismo nativo0.1.2 · 2026-10-15

`EXPLICIT`: continuación de la solicitud de aplicar estilos a todos los componentes y documentar sus requisitos, sin repetir aprobaciones por familia. `DERIVED`: la [enmienda nativa 0.1.2](../specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md) admite, exclusivamente con cadena/escala/estilo principal y evidencia causal verificables, el consumo nativo de 103 rangos cuyo ID local puede ser vacío. Mantiene el ID lógico de receta y todas las métricas; conserva asignación directa en los 3250 restantes. No aprueba automáticamente cualquier vacío ni modifica anatomía, Slots, geometría o componentes por preferencia.

El [catálogo 0.1.2](../specs/tokens/ai-design-system.typography.v0.1.2.json) corrige tres descripciones/motivos y metadatos, sin añadir estilos. Los43 Specs y sus fuentes históricas se conservan; cuatro cierres de familia añaden esta enmienda explícita. Estado `DELEGATED_FOR_BUILD`, auditoría `PENDING`, consumo tipográfico `VALIDATED` en el [QA final0.1.2](../qa/implementations/typography.v0.1.2.review.md), con su alcance y límite de Table explícitos. La [decisión detallada](DEC-TYPOGRAPHY-STYLES-001.md) y los registros de implementación/skills separan resultados y cierres.

## DEC-TYPOGRAPHY-STYLES-001 · ampliación de consumo 0.1.1 · 2026-10-15

`EXPLICIT`: el usuario solicita aplicar los estilos a todos los componentes Figma y documentar en cada Spec las tipografías requeridas, continuando la elección de 18 estilos base más complementarios necesarios. La [decisión específica](DEC-TYPOGRAPHY-STYLES-001.md) incorpora esta ampliación sin simular aprobación humana del detalle. La [enmienda transversal con 43 Specs de consumo](../specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../specs/foundations/typography.formatting.amendment.v0.1.1.md) registran la sustitución exacta y conservan las bases históricas; estado `DELEGATED_FOR_BUILD`, auditoría `PENDING`.

`DERIVED`: cuatro complementarios con UNDERLINE preservan formato y receta de 27 rangos existentes. El catálogo activo contiene 79 estilos. La técnica ensayada aplica estilos completos por rango, sin setters posteriores de formato ni reemplazo de textos/propiedades. Ejecución Figma `IN_PROGRESS`, con 103 rangos escalados `BLOCKED`; el piloto Button no valida otros consumidores. Se mantienen fallos y restauración históricos, y el QA final por destino permanece separado. Esta decisión no autoriza publicación ni normalización visual indiscriminada.

## DEC-WEB-CONTRACT-AUDIT-001 · 2026-10-13

EXPLICIT: el usuario solicita «cotejalos todos, no puede existir ni una discrepancia», continuando el barrido Sidebar/BENI y la capa web de43 familias. Autoriza cotejar y corregir la implementación local contra contratos/enmiendas existentes, sus props/defaults/Slots, documentación y ejemplos. No aprueba nuevas necesidades, variantes, colores o cambios de diseño ni publica Figma. La evidencia de QA distingue cumplimiento medido de exactitud universal y bloqueos. [QA0.1.3](../qa/implementations/web.contract-audit.v0.1.3.review.md).

La extracción de los dos originales raster Modal fue rechazada por revisión automática de permisos; se solicitó autorización explícita para esa copia local. El usuario autorizó explícitamente «Sí, copiar ambas imágenes al proyecto». Permiso limitado a esa copia local; los originales se recuperaron después y sus hashes fueron verificados. No autoriza otras extracciones ni escrituras Figma.

## DEC-WEB-FIDELITY-001 · 2026-10-13

EXPLICIT usuario: «La sidebar no se parece ni tiene los parametros correctos de acuerdo a los specs ni componente, necesito que hagas un barrido y todo quede permeado exactamente a lo que se documentó». Autoriza corregir la biblioteca web existente contra los contratos vigentes; no cambiar requisitos visuales para justificar diferencias del código. Se mantiene la instrucción de no inventar necesidades.

DERIVED: barrido de43 familias, API y galería de referencia, recuperación de los ocho assets web Logos faltantes desde sus IDs originales y ampliación de QA por geometría. [Reporte0.1.2](../qa/implementations/web.fidelity.v0.1.2.review.md) y [matriz](../qa/implementations/web-fidelity-2026-10-13/family-matrix.md). [P07 v0.1.1](../protocols/07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md) concreta la correspondencia de defaults/visibilidades y medición de cambios en futuras altas. Sin nuevos tokens, backend, publicación o escrituras Figma; no equivale a aprobación humana de contratos ni paridad pixel global. Sustituye las limitaciones técnicas web0.1.0 corregidas expresamente en el reporte; preserva su historia.

## DEC-WEB-COMPONENTS-001 · 2026-10-13

EXPLICIT usuario: «a cada componente le hagamos su lenguaje de código y documentación técnica para crear pantallas que aunque no tengan el backend puedan facilitar el diseño sin necesidad de figma»; stack «Tailwind, Typescript, React, con el framework NextJS»; obligación de documentar cada nuevo componente del DS. Respuesta sobre versiones: «Usar versiones estables compatibles». No inventar necesidades adicionales.

Autoriza biblioteca, ejemplos, catálogo y dependencias locales del proyecto, documentación y protocolo permanente. Sustituye la previsión Vite para este destino. DERIVED: [P07](../protocols/07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md), [API web 0.1.0 y adaptaciones](../implementations/web/docs/WEB-ADAPTATION.md), cobertura de 43 familias y versiones fijadas. Código y pruebas son evidencia por destino, no aprobación visual general. Mantener las excepciones y registrar las ocho variantes Logos sin exportación. No autoriza backend, instalación global, publicación ni cambios Figma. [QA](../qa/implementations/web.v0.1.0.review.md).

## DEC-ARTIFACT-RETENTION-001 · 2026-10-13

EXPLICIT usuario: «Dale», en respuesta a la recomendación de continuar con clasificación de derivados, retención y reducción del peso en Git, preservando fuentes, evidencia y recuperación. Autoriza este lote local posterior a las prioridades altas. No extiende el alcance a simplificación de protocolos, frontend, cambios de diseño o publicación remota.

DERIVED implementación: [política de retención](../references/ARTIFACT-RETENTION.md), exclusiones acotadas en .gitignore y retiro del índice de 673 derivados ya respaldados y restaurados para verificación. Todos los originales siguen en disco. Se conservan el grafo activo, semántica por lote, QA, entregables e historia Git. La política define conservación de respaldos y condiciones de una futura compactación; no instala ni ejecuta una purga automática. [QA del lote](../qa/tooling/retention.2026-10-13.review.md).

## DEC-PROJECT-HIGH-PRIORITIES-001 · 2026-10-13

EXPLICIT usuario: «Dale empieza con las Altas», después de la [auditoría de optimización](../drafts/reports/project-optimization.audit.2026-10-13.md). Autoriza implementar las propuestas 1–3: entrada local común de verificación/cierre, vista derivada del estado por familia y QA documental determinista. [Guía operativa](../references/PROJECT-TOOLING.md), [QA del lote](../qa/tooling/project-tooling.2026-10-13.review.md).

DERIVED implementación: configuración de corpus, guardas por hashes, extracción semántica de la sesión, parser seguro Ruby/Psych ya instalado y vistas regenerables. Se reconcilia la versión documental del paquete en 0.2.4. No modifica autoridad, aprobaciones, contratos, datos canónicos ni diseños. Retención Git, simplificación transversal, servicios externos y frontend no se ejecutan en este alcance.

## DEC-CHARACTERS-ECOSISTEMA-INTEGRATION-001 · 2026-10-08

EXPLICIT: incorporar Ecosistema AI885:16275 a AI Design System. Aplican [delegación externa](DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md) e [identidad fija](DEC-CHARACTER-IDENTITY-001.md). DERIVED delegado: página Characters, sets BENI Standby/NAVI Analysis y Frame numerado por ciclo. Tres tokens reutilizados y solo sombra NAVI original añadida, sin semánticos intermedios ni temas. [Contrato](../specs/characters.contract.v0.1.0.md) explicita normalización API y límites, sin inventar producto ni aprobación humana.

## DEC-CHAT-SECTION-INTEGRATION-001 · 2026-10-08

EXPLICIT usuario: «Ahora integraremos esto» con Anticipa20355:74859. Se aplica DEC-EXTERNAL-COMPONENTS-DELEGATION-001 al nodo concreto. [Contrato](../specs/chat-section.contract.v0.1.0.md) registra antes de construir la homologación delegada: dos estados, Slots de mensajes/sugerencias, nombre temático, personajes de identidad fija, poses/lectura estáticas sin backend, reutilización Conversation y ancho desktop documentado. No se adopta Selected de los chips fuente como lógica de filtro. No aprobación humana simulada; excepciones de contraste permanecen para revisión interna. [Continuidad](SESSION-HANDOFF-2026-10-08-CHAT.md).

## DEC-GRAPH-CONTINUOUS-SYNC-001 · 2026-10-08

[Autorización permanente de sincronización local](DEC-GRAPH-CONTINUOUS-SYNC-001.md): actualización completa ahora y cierre incremental automático por lote relevante; P05 0.2.4/GRAPH-SYNC-01–04. No es una automatización programada ni ampliación a servicios externos.

## DEC-CHARACTER-IDENTITY-001 · 2026-10-08

[Decisión explícita](DEC-CHARACTER-IDENTITY-001.md): BENI/NAVI mantienen originales, tokenizados directamente sin semánticos y ajenos al tema. Única nueva excepción, limitada a los personajes. Sustituye su homologación anterior; [enmienda](../specs/components/conversation.character-identity.amendment.v0.1.1.md) y JSON sincronizados.

## DEC-EXTERNAL-COMPONENTS-DELEGATION-001 · 2026-10-08

[Decisión explícita](DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md): el usuario extiende el flujo delegado a los nodos externos que señale y pide ejecutar Conversation ya, homologado al JSON canónico y tokens existentes. Alcance inicial Anticipa20355:72763 → AI Design System/Conversation. No aprobación ficticia ni publicación de biblioteca.

## DEC-APP-SHELL-INTEGRATION-001 · 2026-10-06

Usuario solicita «Incluyelo en el DS con nuestros tokens y json canonico» para8284:12565. [Alcance y normalizaciones delegadas](DEC-APP-SHELL-INTEGRATION-001.md): App Shell desktop, Header/Sidebar DS, Slot nativo y Auto Layout. Cero primitivas/variables nuevas; no breakpoints inventados ni aprobación integral de Anticipa. APP-SHELL-0010.1.0 permanece DELEGATED_FOR_BUILD; promoción documental por QA y auditoría humana por excepciones PENDING.

## USR-ANTICIPA-COMPOSITION-001 · encargo documental · 2026-10-06

EXPLICIT: el usuario pide documentar las especificaciones observadas en un contrato MD, incluyendo propuestas de construcción de componentes, sin discrepar con JSON canónico, contratos y DS establecidos, para consumo por un agente/skill. Autoriza síntesis documental desde SRC-FIGMA-ANTICIPA-LAYOUT-OBSERVATION-001 y comprobación de dependencias; no aprueba automáticamente las propuestas resultantes ni autoriza escritura Figma/frontend. [Candidato0.1.0](../drafts/contracts/anticipa-screen-composition.contract.v0.1.0.md), [síntesis](../drafts/reports/anticipa-screen-composition.synthesis.v0.1.0.md). Se conserva la autoridad de los contratos propietarios; las decisiones contextuales D01–D07 están delimitadas, no resueltas por inferencia ni convertidas en tareas generales del DS.

## DEC-SPECS-PROMOTION-20261006 · alcance administrativo

EXPLICIT: «Specs: promover las bases y enmiendas todavía en drafts cuando cierre el QA correspondiente». Se ejecuta la promoción de19 enmiendas con QA del alcance cerrado conforme a DEC-MIGRATION-SPECS-AUDIT-001 y DEC-MIGRATION-SPECS-CANONICAL-001; [detalle](../qa/contracts/specs-promotion.2026-10-06.review.md). No cambia requisitos, tokens, estados de aprobación ni autoriza publicación remota. La instrucción Paso4 no responde afirmativamente a la excepción geométrica Logos del paso3. Bases con QA afectado aún abierto permanecen sin promover.

## DEC-RADIO-CHECKBOX-REFINEMENT-001 · 2026-10-06

EXPLICIT: «Pasa al punto2», referido al cotejo restante de Radio Buttons y Checkboxes. Aplicación de la delegación de refinamiento: conservar las normalizaciones ya contratadas y corregir ocho posiciones Checkbox desde la evidencia fuente. [Enmienda](../specs/components/radio-checkbox.refinement.amendment.v0.1.2.md) registrada antes de escritura. No autoriza publicar biblioteca ni implica aceptación humana de excepciones. Bases y enmiendas cromáticas promovidas a specs después del QA.

## DEC-SIX-FAMILY-COLOR-REFINEMENT-001 · 2026-10-05

EXPLICIT: «Has la 1», en referencia al primer grupo de la lista entregada: colores, tokens y bindings de seis familias. Ejecuta la delegación de refinamiento vigente y la fidelidad cromática/semántica ya autorizada; no constituye aprobación humana final. Se documentan antes de aplicar las correcciones mediante SIX-FAMILY-COLOR-001. No se amplía a Radio/Checkbox, Logos, frontend ni publicación remota.

## DEC-FILTER-CHIP-INVERSE-001 · refinamiento delegado · 2026-10-05

Usuario: «Sigue, recuerda que la idea es refinar, no crear más pendientes, así que tienes permitido continuar con todo lo que nos haga falta». Aplicación acotada de DEC-SEMANTIC-EXTENSIONS-001 y trazabilidad: texto e iconos seleccionados sobre fondo neutral inverso abandonan roles on-brand. Se anunció antes de escribir; 12 textos reutilizan inverse, 24 vectores consumen un único rol nuevo, alias al blanco existente. No se cambian colores, estados ni variantes. [Enmienda](../specs/components/filter-chip.semantic.amendment.v0.2.1.md); auditoría humana posterior, no aprobación individual ficticia.

## DEC-BUTTON-LOCAL-BINDINGS-001 · ejecución delegada · 2026-10-05

Solicitud actual del usuario: «Continúa con las tareas pendientes». El pendiente confirmado era la sustitución de nueve variables externas de Buttons, con722referencias. En aplicación de DEC-MIGRATION-TRACEABILITY-001 y la delegación vigente, se anunció y documentó antes de escribir el ajuste semántico sin cambios de geometría/colores. [Enmienda0.2.2](../specs/components/button.local-bindings.amendment.v0.2.2.md).

Decisión técnica delegada: usar nueve roles locales ya aprobados, tras comprobar JSON, scopes, aliases y cuatro modos. La capitalización Regular/Manrope→regular/manrope del dato canónico no altera las fuentes renderizadas, comprobado por readback ycaptura idéntica. Sin nuevas variables ni cambio a Foundations. No es aprobación humana individual; auditoríaPENDING. Preserva0.2.0/0.2.1 salvo la sustitución acotada expresamente indicada. No autoriza otra paleta, publicación remota ni ampliación de tareas.

## DEC-MODAL-ROOT-BUILD-001 · 2026-10-01

Usuario: «Ahora si continúa con DS desde el raíz». Modal usa exclusivamente la Librería raíz; Table conserva Anticipa como excepción. Ejecución delegada, no aprobación humana por familia. Decisiones anunciadas antes de construcción: interlineados30/22→32/24 de la escala, Slots nativos y cero variables nuevas. Contrato registra tracking0, placeholder editorial omitido y sombras originales literales; criterios de geometría definidos antes del QA. [Contrato](../specs/modal.contract.v0.1.0.md), [continuación](SESSION-HANDOFF-2026-10-01-MODAL.md). Auditoría por excepciones PENDING.

## DEC-TABLE-ANTICIPA-SOURCE-001 · 2026-10-01

[Decisión explícita](DEC-TABLE-ANTICIPA-SOURCE-001.md): Table usa Anticipa15006:84823, no la fuente legacy. «Ya continua» reanuda esta familia en AI-Design-System bajo construcción delegada y auditoría posterior. [Contrato](../drafts/contracts/table.contract.v0.1.0.md): Slots nativos, cero tokens nuevos, aproximación de negro a neutral900 y geometría Hover original señaladas antes de construir. No autoriza otras familias de Anticipa ni publicar biblioteca.

## DEC-HEADER-COMPOSITION-001 · 2026-10-01

Alcance EXPLICIT: «Dale» autoriza continuar con Header bajo delegación de migración. Aplicación DERIVED de P-SLOTS: sustituir helper Amount1–5 por Actions0..n nativo, cuatro textos editables y Avatar expuesto. Se preserva la cabecera Desktop sin inventar navegación/móvil.

Tres roles semánticos según política vigente: dos stops aproximados a primitivas existentes y un stroke de icono exacto; no crear colores primitivos. El caret local fuente no importable se reproduce desde SVG exacto en helper privado, con binding de marca. Fuente y dependencias principales intactas. [Contrato y excepciones](../specs/header.contract.v0.1.0.md), [QA](../qa/implementations/header.v0.1.0.figma.review.md). Esta decisión técnica delegada no equivale a aprobación humana.

## DEC-GRAPH-REFRESH-2026-10-01 · actualización del índice y conciliación

2026-10-01 · EXPLICIT: tras revisar el desfase, el usuario solicitó «Continuemos por dejar todo actualizado» y, ante el aviso de tamaño del corpus, «Hazlo como mejor convenga al proyecto».

DERIVED: actualizar por lotes el corpus soportado del proyecto; reutilizar evidencia semántica solo con archivo y hash de contenido coincidentes; conservar respaldos e historial. Conciliar listas operativas sin alterar contratos, tokens ni resultados de QA. Inspeccionar e incluir por ruta exacta los tres JSON de diseño omitidos por el heurístico de nombre `tokens`, sin desactivar filtros globales de secretos. No autoriza publicación Figma, nuevas variantes, frontend, servicios externos de pago ni configuración global. Ver [entorno](environment.md) para ejecución y limitaciones; el grafo permanece evidencia derivada.

## DEC-SLOTS-CONTINUATION-002 · Steps, Pagination y Charts

2026-09-30 · EXPLICIT: el usuario solicita «Continúa con el resto», después de la cola de Slots. Se completa esa cola bajo la delegación de migración; no se amplía a publicación de biblioteca ni frontend. [Enmienda en specs](../specs/composition-slots.amendment.v0.1.1.md), [QA](../qa/implementations/composition-slots.v0.1.1.figma.review.md).

DERIVED, decisión técnica anunciada antes de aplicar: para que Disabled afecte también a celdas insertadas en Pagination sin perder cantidad/textos, se añade una colección contextual de dos modos y nueve tokens que aliasan roles existentes. [Contrato Foundations](../specs/foundations.pagination-slot-state.amendment.v0.1.0.md) y [JSON único](../drafts/foundations/ai-design-system.pagination-slot-state.v0.1.0.json). No son variables preexistentes ni una aprobación humana nueva; DELEGATED_FOR_BUILD, auditoría PENDING. Cero colores/primitivas nuevos; 200 comparaciones de color originales sin diferencia. Alcance limitado a Pages; no altera otros componentes.

OBSERVED: Figma conserva contenido personalizado de Slots; no calcula selección ni traslada roles automáticamente entre contextos distintos. Steps mantiene el grupo legacy On Primary separado; el contrato registra la preservación al volver al contexto original. Vacío y límites de producto siguen UNRESOLVED sin bloquear la capacidad estructural verificada.

## DEC-SLOTS-REVIEW-001 · revisión obligatoria de Slots

2026-09-29 · EXPLICIT, instrucción del usuario: «Necesito que vayas agregando Slots donde se requieran, ya que por ejemplo los dropdown pueden tener más o menos elementos»; precisión posterior: «necesito que lo pongas como protocolo de revisión para implementación de Slots».

Se incorpora [P-SLOTS0.1.0](../protocols/SLOTS-REVIEW-AND-IMPLEMENTATION.md) a AGENTS, P03/P04/P05/P06 y plantilla de componente. La revisión de aplicabilidad es obligatoria; la implementación se exige cuando corresponde, no indiscriminadamente. No simularla con nombres de capas ni listas fijas. Select es el primer caso REQUIRED, con [adopción pendiente](SLOTS-REVIEW-STATUS.md). La solicitud no valida una capacidad de Figma todavía no comprobada ni aprueba contratos futuros. Este turno modifica documentación, no Figma ni variables. Graphify STALE, sin regeneración.

## DEC-SELECT-COMPOSITION-001 · decisión de construcción delegada

2026-09-29. Bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y solicitud de continuar, se normalizan dos ejemplos de Select en Presentation Closed/Open, con instancias locales expuestas; no se inventa comportamiento ni variantes adicionales. Se conservan Eye y helper superpuesto como evidencia observada. Las dos sombras se preservan literalmente bajo P03§11/P04§6: no existe categoría canónica de sombras, no se usan roles de foco/texto ni nuevas primitivas. Se anunció antes de construir. No es aprobación humana específica; excepción sujeta a auditoría. [Contrato](../specs/select.contract.v0.1.0.md).

## DEC-TOKENS-001 · aprobación para Figma

- **Fecha:** 2026-09-22.
- **Actor:** usuario, en la conversación de esta tarea.
- **Decisión explícita:** “De acuerdo, está aprobado. Entonces empieza a construir”, inmediatamente después de la explicación de campos delegados y de la aprobación de versión y alcance del [candidato](../drafts/contracts/foundations-tokens.contract.md).
- **Entidad y alcance adoptados:** `FOUNDATIONS-TOKENS-001` versión `0.1.0`, reconstrucción de las variables del inventario vinculado en el archivo Figma de destino `AI-Design-System`. No incluye componentes ni web.
- **Candidato revisado:** SHA-256 bytes `e89ddaf95e1ee07998fa851c50ef9787b4ec3f9072e0c1ea44e07eb3e298e1da`.
- **Contrato publicado:** [specs/foundations/foundations-tokens.contract.md](../specs/foundations/foundations-tokens.contract.md), SHA-256 bytes `e7362c364aa2c93a1a5bd50e0024d6b551f8ec6c6947bb62c6779ee25c1b7999`.
- **Datos vinculados aprobados:** [sources/inventories/tokens.inventory.json](../sources/inventories/tokens.inventory.json), SHA-256 bytes `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.
- **Cambios entre candidato y publicado:** solo metadatos y redacción administrativa de estado/autoridad; no se alteraron REQ, AC, conteos, campos JSON ni alcance. El candidato se conserva.
- **Límite:** la aprobación no acredita que Figma esté `READY`, que exista una implementación o que haya pasado QA. P01/P04/P06 siguen vigentes.

## DEC-ICONS-001 · fuente única de iconos

- **Fecha:** 2026-09-23 UTC (2026-09-22 en America/Merida).
- **Actor:** usuario, en la conversación de esta tarea.
- **Decisión explícita:** “todos los iconos los vas a consumir de” el archivo [Phosphor Icons](https://www.figma.com/design/xZSksKpcQTp5H3C4dZApBL/Phosphor-Icons?node-id=7484-1322&t=5f3sI6AFFHMgcXfl-1), file key `xZSksKpcQTp5H3C4dZApBL`.
- **Alcance adoptado:** procedencia de los iconos para la reconstrucción del sistema de diseño. En Button, ambos slots y cualquier swap futuro deben referenciar componentes de ese archivo; la coincidencia se verifica por key del componente, no por apariencia.
- **Verificación de la dependencia activa:** [SRC-FIGMA-PHOSPHOR-001](sources.md) comprobó que las keys del set y variante `PlusCircle / Outline / Light` coinciden con las que usa Button. Esto no acredita todos los iconos de otras familias.
- **Límite:** no es aprobación de `BUTTON-001` completo, de interacciones, nombre/operación de página, migración de variables ni implementación web. No autoriza sustituir iconos por SVGs/copias locales desvinculadas.

## DEC-BUTTON-001 · aprobación del contrato Button para Figma

- **Fecha:** 2026-09-23 UTC (2026-09-22 en America/Merida).
- **Actor:** usuario, en la conversación de esta tarea.
- **Decisión explícita:** “Dale, comienza a hacerlo, por favor. Está aprobado”, después de explicar que se publicaría el contrato Button, se revisaría el set existente en Figma y se haría QA posterior.
- **Entidad y alcance adoptados:** `BUTTON-001` versión `0.1.0`, reconstrucción/validación en el archivo Figma `AI-Design-System`. Incluye la regla de fuente de iconos `DEC-ICONS-001`; no incluye frontend web ni comportamiento que el contrato deja `UNRESOLVED`.
- **Candidato revisado:** [drafts/contracts/button.contract.md](../drafts/contracts/button.contract.md), SHA-256 bytes `a2124c2d1236108c5ff129e6d552510568b625a1012ab3653d18528f89c0d6a0`.
- **Modelo técnico vinculado:** [drafts/contracts/button.contract.yaml](../drafts/contracts/button.contract.yaml), SHA-256 bytes `734b85826ad4cb4c2caa08932e4364516a6e2f31f4be8e8ce6b0decda6ec4e1b`.
- **Contrato publicado:** [specs/components/button.contract.md](../specs/components/button.contract.md), SHA-256 bytes `4b94f80787c1fc9d9990f806c99900e17db060e65b624471b0c8d93f534f2abb`.
- **Fuentes preservadas:** snapshot Button SHA-256 `1d58b485a6324a8bdd2618ba43f34efbfb50b609f1467b18579fe875067c5dca`; snapshot Phosphor SHA-256 `c3529c0ecc28a2cb1cdb2af852b3b72bd7f5751639bf89c73e712037e9813e60`.
- **Cambios entre candidato y publicado:** solo estado, redacción administrativa de aprobación, rutas de enlaces y fila de publicación en changelog; `REQ-BTN-001–009`, `AC-BTN-001–009`, valores, conteos y alcance permanecen idénticos. El candidato se conserva.
- **Límite:** la aprobación no decide el nombre canónico de la página ni autoriza por sí sola una operación de renombrado/migración; tampoco acredita que la implementación esté `VALIDATED`. Las variables remotas conservan su identidad hasta una decisión distinta, sin sustituirlas por equivalentes visuales.

## DEC-BUTTON-PAGE-001 · nombre de página

- **Fecha:** 2026-09-23 UTC (2026-09-22 en America/Merida).
- **Actor:** usuario, en la conversación de esta tarea.
- **Decisión explícita:** “Se tiene que llamar, Buttons”, en respuesta a la pregunta sobre el nombre de la página exclusiva para Button.
- **Alcance:** completa el nombre pendiente de `REQ-BTN-007` y `AC-BTN-007` del contrato `BUTTON-001` versión `0.1.0`. La [enmienda aprobada](../specs/components/button-page-name.amendment.md) fija el nombre exacto `Buttons`.
- **Destino y operación:** el preflight verificó que `Page 1` (`0:1`) contiene únicamente el set Button `26:81`; se puede renombrar esa página, sin crear otra ni mover el set. No se aprueban cambios de variantes, interacciones, tokens o web.
- **Ejecución:** la página `0:1` se renombró a `Buttons`; el readback conservó el set `26:81` y [QA-BUTTON-FIGMA-002](../qa/implementations/button.figma.review.md) validó el alcance Figma. La decisión no se amplió a otras familias.

## DEC-BUTTON-USAGE-REQUEST-001 · solicitud de guía, no aprobación

- **Fecha:** 2026-09-23 UTC (2026-09-22 en America/Merida).
- **Actor:** usuario, en esta tarea.
- **Solicitud explícita:** redactar instrucciones de cómo, cuándo y dónde usar las variantes y los iconos izquierdo/derecho; integrarlas en el contrato y revisar la documentación, usando como referencia Material Design, Tailwind, Carbon y Human Interface Guidelines.
- **Fuente visual adjunta:** [SRC-BTN-CONFIG-001](sources.md) muestra Description y Link vacíos. El contenido de la imagen se trata como evidencia de interfaz, no como instrucciones independientes.
- **Alcance autorizado:** síntesis y revisión del candidato [BUTTON-001 0.2.0](../drafts/contracts/button.contract.v0.2.0.md). La solicitud no aprueba automáticamente las reglas concretas INFERRED de esa versión ni sustituye la aprobación de 0.1.0.
- **Pendiente:** decisión humana sobre 0.2.0, especialmente semántica local de iconos por lado y uso de type=link. Solo después se podrá publicar Description y validar mediante readback; Documentation link exige URL pública verificable.

## DEC-BUTTON-USAGE-002 · aprobación de Button 0.2.0

- **Fecha:** 2026-09-23 UTC (2026-09-22 en America/Merida).
- **Actor:** usuario, en esta tarea.
- **Decisión explícita:** “Bien ya publica”, después de que se le mostró el [candidato 0.2.0](../drafts/contracts/button.contract.v0.2.0.md), se aclaró que el contrato anterior seguía intacto y que Description en Figma aún esperaba aprobación.
- **Entidad y alcance adoptados:** `BUTTON-001` versión `0.2.0`, reglas de uso para los cuatro tipos, tres tamaños y cinco estados, etiquetas, composición de iconos izquierdo/derecho y resumen de Description del component set en la página Buttons. Se conserva el baseline técnico aprobado 0.1.0 y la enmienda de página.
- **Candidato revisado:** SHA-256 bytes `c97cd24a1505236cfdac32d85a676d8eb2b4394ec074412305d7cfd3abf37ae5`.
- **Texto de Description revisado:** [borrador](../drafts/figma/button.description.v0.2.0.md), SHA-256 bytes `22ca686667bc9c815d461c6d1e246817b8861e04fb9e448440b96e478d98c56c`. El texto publicable es solo la sección indicada para pegar; los encabezados de estado y la nota sobre Documentation link son instrucciones de registro, no parte del campo Figma.
- **Contrato publicado:** [specs/components/button.contract.v0.2.0.md](../specs/components/button.contract.v0.2.0.md), SHA-256 bytes `53e13fa8e664f70d0ce81116e850bbcb0ab7da9f14ac0f08607fa5fda09894a1`.
- **Dato técnico vinculado sin cambios:** [YAML](../drafts/contracts/button.contract.yaml), SHA-256 bytes `734b85826ad4cb4c2caa08932e4364516a6e2f31f4be8e8ce6b0decda6ec4e1b`.
- **Cambios entre candidato y publicado:** solo metadatos, referencias relativas, tiempo verbal y declaración administrativa de autoridad; los REQ-BTN-010–019, AC-BTN-010–019, matrices, medidas y límites de alcance no cambiaron.
- **Límite:** la aprobación autoriza publicar Description y verificarla, no crear URL pública, modificar iconos/variantes/interacciones o implementar web. Documentation link seguirá vacío hasta disponer de URL pública verificable.

## DEC-FILTER-CHIP-DIRECTION-001 · dirección de la revisión 0.2.0

- **Fecha:** 2026-09-23.
- **Actor:** usuario, en esta tarea.
- **Solicitud de construcción:** «Cuando tengas el contrato necesito que lo construyas en AI Design System en su propia página llamada Chips, además necesito que lo hagas con las mejores prácticas y usando los tokens de las variables propias de AI Design System».
- **Decisión explícita sobre conflictos:** «Seguir la descripción y completar variantes», en respuesta a la elección entre reproducir las 24 variantes observadas o adoptar la descripción con iconos ocultos por defecto, tamaños Sm/Md/Xl y estados Selected independientes.
- **Interpretación propuesta para revisión:** mapeo Sm/Md/Xl → small/middle/large (32/40/48 px, como Button en el destino), 30 variantes completas y `x-small` fuera del alcance. Las recetas seleccionadas hover/press toman 92%/85% de la descripción. Selected+focus y padding middle normalizado son propuestas explícitas del [candidato 0.2.0](../drafts/contracts/filter-chip.contract.v0.2.0.md).
- **Límite:** esta dirección resuelve la prioridad entre fuentes y autoriza preparar la construcción, pero la versión candidata 0.2.0 con sus detalles derivados requiere aprobación explícita antes de ejecutar P04 según P03/P04.

## DEC-FILTER-CHIP-APPROVAL-002 · aprobación del contrato 0.2.0 para Figma

- **Fecha:** 2026-09-23.
- **Actor:** usuario, en esta tarea.
- **Decisión explícita:** «Si», en respuesta a la pregunta que identificó `FILTER-CHIP-001` versión `0.2.0`, SHA-256 candidato `bd82e46bcbde849890af30e9c8f6d5fad3b1d0cb2b3b5b2f5ac1cacd1127ab96`, su modelo de construcción, 30 variantes en la página Chips y las dos decisiones derivadas selected+focus y padding middle.
- **Alcance adoptado:** construcción y QA del component set Filter Chip en la página exclusiva `Chips` de `AI-Design-System` (`tj3WIBEZDGLVs7MJWKCwgf`), con variables locales del destino y PlusCircle de Phosphor Icons. No incluye web ni publicación de biblioteca de equipo.
- **Candidato revisado:** [filter-chip.contract.v0.2.0.md](../drafts/contracts/filter-chip.contract.v0.2.0.md), SHA-256 bytes `bd82e46bcbde849890af30e9c8f6d5fad3b1d0cb2b3b5b2f5ac1cacd1127ab96`.
- **Datos vinculados aprobados:** [YAML de observación](../drafts/contracts/filter-chip.contract.yaml), SHA-256 bytes `af6918afb5ce050047c06153d9def42d9365efb3f2fbbee949f2845a2932632e`; [modelo de construcción](../drafts/contracts/filter-chip.build.v0.2.0.yaml), SHA-256 bytes `40e9e3464b86560255c185bf893518dea2a445170678fa797c8ff6925218e48c`; [Description](../drafts/figma/filter-chip.description.v0.2.0.md), SHA-256 bytes `a76fec95af4ab8fbfdbb865fef71842bba16f2bd990d98596c0b43b9d4ca86f2`.
- **Contrato publicado:** [specs/components/filter-chip.contract.v0.2.0.md](../specs/components/filter-chip.contract.v0.2.0.md), SHA-256 bytes `325a408cfa6a5880c2136aee89a448e9ab3a6d928199543d946d6ae3a52a6cb8`.
- **Diferencias administrativas entre candidato y publicado:** `status`, redacción de aprobación y rutas relativas; REQ-FC-001–009, AC-FC-001–009, matriz, tamaños, estados y bindings no cambiaron.
- **Límite:** la aprobación no acredita construcción ni QA; se registran por separado tras lectura posterior.

## DEC-PROTOCOL-SEMANTIC-PAGES-001 · páginas y variables semánticas para futuras familias

- **Fecha:** 2026-09-23.
- **Actor:** usuario, en la conversación de esta tarea.
- **Solicitud explícita:** integrar un protocolo de nombramiento o creación de páginas por componente, con semántica funcional y uso explícito de colores, tipografías y variables locales del Figma `AI-Design-System`; basarse especialmente en el JSON de variables ya existente.
- **Alcance adoptado:** actualización prospectiva de [P03](../protocols/03-CONTRACT-SYNTHESIS.md), [P04](../protocols/04-FIGMA-CONSTRUCTION.md), [P05](../protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md), [P06](../protocols/06-QA-AND-VALIDATION.md) y la [plantilla de componentes](../templates/component.contract.template.md). El [inventario JSON aprobado](../sources/inventories/tokens.inventory.json), SHA-256 bytes `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`, gobierna los datos de variables; los IDs locales se leen del destino.
- **Límite:** no cambia retrospectivamente `BUTTON-001` ni `FILTER-CHIP-001`, no renombra páginas ni aprueba nuevos contratos o tokens. Cualquier nombre nuevo de página y equivalencia semántica aún requieren evidencia y aprobación de la familia concreta.

## DEC-LEGACY-MIGRATION-DELEGATION-001 · reconstrucción con auditoría posterior

- **Fecha:** 2026-09-23.
- **Actor:** usuario, en la conversación de esta tarea.
- **Solicitud explícita:** después de entregar la URL de la [Librería anterior](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=7339-129&t=sZOrF8YSnEjHSpdU-1), pidió usar el mejor criterio, construir todo sin solicitar su aprobación previa por componente y pedirle auditoría al terminar.
- **Alcance delegado:** inspeccionar las familias de componentes del archivo fuente `9zs5RMR8LB5wHjW9Bd59BA`, sintetizar contratos versionados, verificar cada contrato documentalmente, reconstruir los que estén `READY` en `AI-Design-System` `tj3WIBEZDGLVs7MJWKCwgf` con variables del JSON aprobado y hacer QA técnico. La decisión es una autorización de trabajo y juicio acotado, no una afirmación de que el usuario revisó o aprobó requisitos aún no escritos.
- **Estado y límite:** los contratos pueden marcarse `DELEGATED_FOR_BUILD` solo tras QA documental `PASS` sin bloqueos; `user_audit: PENDING` hasta la revisión posterior. No se inventan variables, se omiten conflictos, ni se ejecutan reemplazos destructivos sin autorización específica. Una familia bloqueada se documenta y las demás pueden continuar.

## DEC-BADGE-CONTRAST-001 · ajuste delegado de contraste en Badge

- **Fecha:** 2026-09-23.
- **Actor:** Codex dentro de la delegación acotada DEC-LEGACY-MIGRATION-DELEGATION-001; no es aprobación humana.
- **Evidencia:** [hallazgo de implementación](../qa/implementations/badge.v0.1.0.contrast-finding.md) con 3.61:1 en Informational y 2.96:1 en Warning; referencias oficiales [WCAG 2.2 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) y [1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).
- **Decisión propuesta:** entre variables ya aprobadas, usar `color/text/primary` en el texto de Informational y Warning, y `color/icon/primary` en ambos iconos Warning; conservar icono Information y los fondos de feedback. No modificar ni inventar tokens.
- **Alcance:** solo REQ-BDG-006/AC-BDG-006 mediante enmienda 0.1.1, sujeto a QA documental y auditoría posterior del usuario. No altera otras familias ni comportamiento web.

## DEC-TOGGLE-CONTRAST-001 · ajuste delegado de contraste en Toggle Off

- **Fecha:** 2026-09-23.
- **Actor:** Codex dentro de DEC-LEGACY-MIGRATION-DELEGATION-001; no es aprobación humana.
- **Evidencia:** [hallazgo](../qa/implementations/toggle.v0.1.0.contrast-finding.md): Off/Default y Off/Focus 1.23:1 contra la superficie, frente a referencia 3:1 para UI no textual.
- **Decisión propuesta:** usar el rol semántico existente `color/background/inverse` para los dos fills del track, con 14.63:1 calculado en los cuatro modos; conservar el resto. No crear ni modificar variables.
- **Alcance:** solo REQ-TGL-005/AC-TGL-005 mediante enmienda 0.1.1, sujeto a QA documental, readback y auditoría posterior. No se cambia el comportamiento web.

## DEC-TOGGLE-NORMALIZATION-001 · normalizaciones delegadas del contrato base

- **Fecha:** 2026-09-23.
- **Actor:** Codex dentro de DEC-LEGACY-MIGRATION-DELEGATION-001; no es aprobación humana.
- **Evidencia:** [TOGGLE-001 0.1.0](../drafts/contracts/toggle.contract.v0.1.0.md) y [YAML fuente](../drafts/contracts/toggle.contract.v0.1.0.yaml).
- **Decisiones acotadas:** `defualt`→`Default`; nombre funcional `Toggles`/`Toggle`; radios Off/Focus de `font/size/lg`→`radius/full`; borde Off/Focus de disabled→strong, con el mismo alias primitivo; line-height de label 15→16 con token existente; color del halo focus claro literal→`color/background/default`. Se preservan las demás variantes y propiedades observadas.
- **Límite:** decisiones de construcción para Figma, registradas antes de QA final; auditoría humana `PENDING`, sin efecto en variables aprobadas ni web.

## DEC-TOGGLE-VISUAL-CONTRAST-002 · corrección para mantener el estilo fuente

- **Fecha:** 2026-09-23.
- **Actor:** Codex dentro de DEC-LEGACY-MIGRATION-DELEGATION-001, tras la aclaración del usuario de que la reconstrucción debe parecerse mucho a la Librería anterior mientras aplica mejores prácticas; no es aprobación humana del detalle.
- **Evidencia:** [QA-TOGGLE-FIGMA-003](../qa/implementations/toggle.v0.1.1.visual-fidelity-finding.md): el fondo oscuro de 0.1.1 se apartó demasiado de la fuente. El JSON fuente no tiene borde neutral ≥3:1; `color/text/tertiary` da 4.76:1, pero su scope es solo `TEXT_FILL`.
- **Autorización ampliada del usuario:** «Necesito que las variables y el JSON sean fieles. Entonces, si lo vas a grabar en el JSON, necesito que también se aplique en las variables de Figma. No importa si lo tienes que agregar, tú agrégalo». Esta decisión sustituye, solo para esta necesidad documentada, la prohibición previa de crear variables bajo la delegación general; no atribuye al usuario aprobación de un valor o nombre aún no auditado.
- **Decisión acotada:** en Off/Default y Off/Focus, restaurar fill pálido de fuente y oscurecer solo el stroke de 1 px con `color/border/control`, scope `STROKE_COLOR`. En Off/Hover, reemplazar el fill `color/text/tertiary` por `color/background/control-hover`, scope `FRAME_FILL`/`SHAPE_FILL`, conservando el color. En el thumb Off/Disabled, usar el existente `color/background/default` en lugar de `color/icon/on-brand`, conservando el blanco. Ambos tokens nuevos aliasan en cuatro modos al primitivo `color/neutral/500`. Definirlos en el [JSON de extensión de destino](../drafts/foundations/ai-design-system.control-colors.v0.1.0.json) y crear variables equivalentes en AI Design System. No alterar el JSON histórico fuente ni tokens compartidos.
- **Alcance:** enmienda 0.1.2 que sustituye únicamente la solución 0.1.1 sobre REQ-TGL-005/AC-TGL-005, condicionada a QA documental, verificación de la variable en Figma y readback posterior. Auditoría humana pendiente.

## DEC-SEMANTIC-EXTENSIONS-001 · extensiones vinculadas a primitivas y scopes estrictos

- **Fecha:** 2026-09-23.
- **Actor:** usuario, durante la migración de la Librería anterior a AI Design System.
- **Decisión explícita:** autoriza ampliar colores, tokens y variables cuando sea necesario para mejorar la reconstrucción, conservar lo posible del estilo fuente y avisar de cada cambio. Exige que todo rol nuevo quede vinculado a una primitiva existente, que JSON, contratos y Figma reflejen lo mismo, y que la categoría semántica y el scope técnico sean estrictamente adecuados a la propiedad consumidora.
- **Aplicación:** una extensión nueva se define en un JSON de destino versionado, distinto del snapshot inmutable de origen; pasa QA documental, se construye y lee de vuelta en Figma antes de aplicarse. Se registran IDs reales, aliases por modo, consumidores, diferencia visual y auditoría humana pendiente. No se crean primitivas nuevas ni se alteran variables compartidas por mera igualdad de color.
- **Primer caso anunciado:** dos roles para Toggle: `color/border/control` y `color/background/control-hover`, ambos alias de `color/neutral/500` con scopes distintos. Se corrige además el thumb Disabled con `color/background/default` existente. Véase [JSON de extensión](../drafts/foundations/ai-design-system.control-colors.v0.1.0.json).

## DEC-TOGGLE-FOCUS-EFFECT-003 · scopes propios para colores de efectos

- **Fecha:** 2026-09-23.
- **Actor:** Codex bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; auditoría humana del detalle `PENDING`.
- **Hallazgo:** [QA-TOGGLE-FIGMA-005](../qa/implementations/toggle.v0.1.2.effect-scope-finding.md) confirmó cuatro colores de DROP_SHADOW ligados a roles de stroke o fill, aunque el RGB era correcto.
- **Decisión acotada:** añadir en [JSON de extensión](../drafts/foundations/ai-design-system.focus-effects.v0.1.0.json) `color/focus/effect-outer` y `color/focus/effect-inner`, scope exclusivo `EFFECT_COLOR`, aliasados respectivamente a las primitivas existentes `color/blue/500` y `color/neutral/100` en los cuatro modos. Cambiar solo los cuatro bindings de efectos de `111:135` y `111:155`, sin variar color, geometría ni otros estados. No ampliar el scope de `color/focus/ring` ni el de `color/background/default` porque sus usos de stroke y fill siguen correctos.
- **Verificación:** [QA documental Foundations](../qa/contracts/foundations.focus-effects.amendment.v0.1.2.review.md), [QA documental Toggle](../qa/contracts/toggle.focus-effect-amendment.v0.1.3.review.md), [QA Figma variables](../qa/implementations/focus-effects.v0.1.0.figma.review.md) y [QA Figma Toggle](../qa/implementations/toggle.v0.1.3.figma.review.md). El inventario fuente permanece intacto; no se publica la biblioteca ni se implementa web.

## DEC-RADIO-NORMALIZATION-001 · selección y dependencia local

- **Fecha:** 2026-09-23.
- **Actor:** Codex bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; auditoría humana del detalle `PENDING`.
- **Evidencia:** [fuente Radio Button](../drafts/contracts/radio-button.source.component-contract.md) con ocho variantes, indicador local y etiquetas no editables como propiedades; [contrato de reconstrucción](../drafts/contracts/radio-button.contract.v0.1.0.md).
- **Decisión acotada:** una página funcional `Radio Buttons` con un helper `Radio Indicator` y set público `Radio Button`, ambos de ocho variantes `Selected=True/False × State=Default/Hover/Focus/Disabled`. On de 5 px se representa por dos círculos concéntricos para no crear un primitivo stroke de 5. Off Default adopta `color/border/control` neutral 500 para contraste, frente al neutral 400 de fuente. Se añaden dos propiedades TEXT para labels, se usa interlineado semántico 20 y el halo interior de foco se liga al token de efecto blanco. Los dos rellenos cromáticos nuevos se definen en JSON y aliasan primitivas aprobadas con scope `SHAPE_FILL`.
- **Verificación:** QA documental del contrato y extensión, lectura posterior de variables, QA Figma de 8+8 variantes y captura comparada. No se atribuye aprobación humana ni comportamiento web.

## DEC-CHECKBOX-NORMALIZATION-001 · matriz y estilo de selección compartido

- **Fecha:** 2026-09-23.
- **Actor:** Codex bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; auditoría humana del detalle `PENDING`.
- **Evidencia:** [Checkbox fuente](../drafts/contracts/checkbox.source.component-contract.md), 12 variantes y tres dependencias principales; [contrato destino](../drafts/contracts/checkbox.contract.v0.1.0.md).
- **Decisión acotada:** conservar la matriz 3×4 y Check/Minus Phosphor; usar `color/background/control-selected` y hover para fill de selección, `color/border/control` para Unselected Default/Focus, `radius/sm` local para los 4 px de fuente, TEXT editables para 24 labels y foco con tokens `EFFECT_COLOR`. El helper interno usado una sola vez se normaliza a anatomía directa. Se renombra el estilo reutilizable de Radio a `Focus/Selection Outset` para ambos controles; no cambian su ID, spreads, colores o bindings.
- **Verificación:** QA documental, importación/readback de keys Phosphor, QA Figma 12 variantes y comparación visual. No se atribuye aprobación humana ni comportamiento web.

## DEC-DOT-SEMANTIC-ROLES-001 · fondos propios y borde Inactive

- **Fecha:** 2026-09-23.
- **Actor:** Codex bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; auditoría humana del detalle `PENDING`.
- **Evidencia:** [Dot fuente](../drafts/contracts/dot.source.component-contract.md) tiene matriz 5×3, pero usa roles de icono para fondos y declara falsamente ausentes dos variantes Large. [Hallazgo de contraste](../qa/implementations/dot.v0.1.0.inactive-contrast-finding.md) documentó el borde Inactive de 1.23:1 contra blanco.
- **Decisión acotada:** conservar los colores y tamaños observados con cuatro roles `color/background/*` exclusivos `FRAME_FILL`, aliasados a primitivas existentes en el [JSON de fondos](../drafts/foundations/ai-design-system.dot-background-colors.v0.1.0.json). Para Inactive únicamente, conservar el fill pálido y reemplazar su borde blanco por `color/border/status-inactive`, `STROKE_COLOR`, alias neutral/500 en el [JSON de borde](../drafts/foundations/ai-design-system.dot-inactive-border.v0.1.0.json). Este borde alcanza 4.76:1 sobre blanco. No se usan roles `text` ni `icon` fuera de su categoría; no se añaden primitivas.
- **Límite:** los textos numéricos de 4/8 px se conservan como referencia visual, no se avalan para información esencial; no se infiere transformación automática Count→Overflow. [QA Figma](../qa/implementations/dot.v0.1.1.figma.review.md) técnico `PASS`, usuario por auditar, web fuera de alcance.

## DEC-DOT-SOURCE-COLOR-002 · borde Inactive fiel a la fuente

- **Fecha:** 2026-09-24. **Actor:** Codex por delegación de migración y decisiones posteriores de fidelidad cromática; auditoría humana `PENDING`.
- **Evidencia:** readback de ambos sets: solo tres strokes Inactive diferían, blanco en fuente y neutral/500 en destino. Los otros 33 paints visibles ya coincidían. El dato histórico 1.23:1 describe el relleno neutral/300 contra blanco; el borde blanco contra blanco es 1.00:1.
- **Decisión acotada:** sustituir únicamente el alias neutral/500 del rol semántico `color/border/status-inactive` por neutral/100 en cuatro modos mediante [JSON 0.1.1](../drafts/foundations/ai-design-system.dot-inactive-border.v0.1.1.json), sin variable o primitiva nueva. [Enmienda Foundations 0.1.6](../specs/foundations/foundations.dot-inactive-border-source-color.amendment.v0.1.6.md) y [Dot 0.1.2](../specs/components/dot.source-color-amendment.v0.1.2.md) sustituyen solo el color y la afirmación de contraste de DEC-DOT-SEMANTIC-ROLES-001; no revierten los roles semánticos ni los otros requisitos. Limitación `*` para auditoría interna.
- **Verificación:** [QA Figma](../qa/implementations/dot.source-color.v0.1.2.figma.review.md) `PASS` técnico, 15 variantes, 36 paints visibles y cero diferencias RGB; Avatar/Icon Button no consumen este rol en sus sets actuales. Biblioteca sin publicar.

## DEC-AVATAR-FALLBACK-001 · semántica de fondo y legibilidad de iniciales

- **Fecha:** 2026-09-23.
- **Actor:** Codex bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; auditoría humana del detalle `PENDING`.
- **Evidencia:** [Avatar fuente](../drafts/contracts/avatar.source.component-contract.md) con doce variantes, Dot y User anidados, rol `color/interactive/primary/default` en una cara no interactiva y fontSize 6/9 px en Small/Medium. [Contrato destino](../drafts/contracts/avatar.contract.v0.1.0.md).
- **Decisión acotada:** crear `color/background/avatar-fallback` `FRAME_FILL` y `font/size/avatar-small` `FONT_SIZE`, ambos aliasados a primitivas existentes mediante [JSON versionado](../drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json). Mantener azul, verde y morado de origen; en Servicios usar orange/600 en lugar de orange/500 para mejorar el contraste blanco de 3.24:1 a 4.72:1. Iniciales Small/Medium 10/12 px, Large/Extra Large 14/20 como fuente. Reutilizar Dot, User Phosphor y muestra PNG exportada de fuente, no dibujarlos de cero; picker con 1512 sets Phosphor verificados en Chips.
- **Verificación:** QA documental y Figma [PASS](../qa/implementations/avatar.v0.1.0.figma.review.md), auditoría humana pendiente. No se edita el inventario histórico ni se crea primitiva; no se implementa identidad, presencia o fallback web.

## DEC-AVATAR-SOURCE-COLOR-002 · fondo Servicios fiel a la fuente

- **Fecha:** 2026-09-24. **Actor:** Codex bajo delegación y DEC-MIGRATION-VISUAL-FIDELITY-001; auditoría humana `PENDING`.
- **Evidencia:** readback fuente/destino de doce variantes y aliases por modo. Solo el fondo fallback Servicios estaba en orange/600 por contraste; la fuente usa orange/500. Los ocho consumidores Icon/Text comparten el rol semántico correcto.
- **Decisión acotada:** el [JSON de override 0.1.1](../drafts/foundations/ai-design-system.avatar-roles.v0.1.1.json) cambia solo el alias Servicios de `color/background/avatar-fallback` a la primitiva existente orange/500. [Foundations 0.1.11](../drafts/contracts/foundations.avatar-fallback-source-color.amendment.v0.1.11.md) y [Avatar 0.1.1](../drafts/contracts/avatar.source-color-amendment.v0.1.1.md) sustituyen únicamente ese color y su afirmación de contraste de DEC-AVATAR-FALLBACK-001; preservan la mejora de tamaño de iniciales y la someten a AUD-006. No se crean variables ni primitivas.
- **Verificación:** [QA Figma](../qa/implementations/avatar.source-color.v0.1.1.figma.review.md) `PASS` técnico, color Servicios de origen restaurado y limitación 3.24:1 `*` registrada. Biblioteca sin publicar.

## DEC-FEEDBACK-ICON-SCOPES-001 · roles iconográficos sin scope de fondo

- **Fecha:** 2026-09-23.
- **Actor:** Codex bajo DEC-SEMANTIC-EXTENSIONS-001 y la exigencia explícita del usuario de scopes estrictamente semánticos; auditoría humana `PENDING`.
- **Hallazgo:** tres variables `color/feedback/*/icon` existentes admitían `FRAME_FILL` además de `SHAPE_FILL`; `color/feedback/information/icon` ya era exclusivo shape. Preflight de nueve páginas encontró únicamente dos consumidores existentes, ambos vectores Badge, cero fills de frame.
- **Decisión acotada:** [JSON de override](../drafts/foundations/ai-design-system.feedback-icon-scopes.v0.1.0.json) cambia solo `scopes` de positive, warning y danger icon a `[SHAPE_FILL]`, sin duplicar sus descripciones o valores canónicos. [QA Figma](../qa/implementations/feedback-icon-scopes.v0.1.0.figma.review.md) confirmó aliases y consumidores intactos y cero incompatibilidades en 80 variables de color.
- **Límite:** no modifica RGB, primitives, componentes o apariencia; auditoría humana pendiente.

## DEC-WARNING-ICON-CONTRAST-001 · ajuste ámbar del icono Warning

- **Fecha:** 2026-09-23.
- **Actor:** Codex bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; auditoría humana `PENDING`.
- **Hallazgo:** al preparar Inline Notifications, el icono Warning con `color/feedback/warning/icon` amber/600 daba 2.96:1 sobre `color/feedback/warning/bg` amber/100. Ninguna de las nueve páginas de componentes construidas consumía todavía ese token.
- **Decisión acotada:** mantener el rol y su scope `SHAPE_FILL`, cambiar solo sus cuatro aliases a la primitiva existente amber/700 mediante [JSON de override](../drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.0.json); contraste resultante 4.38:1, tono ámbar conservado. [Readback Figma](../qa/implementations/warning-icon-contrast.v0.1.0.figma.review.md) confirmó nombre, descripción, syntax y scope intactos.
- **Límite:** no se añade variable ni primitiva, no se altera ninguna familia previa; la semántica/acción de una notificación se documentará en su propio contrato.

## DEC-MIGRATION-SPECS-AUDIT-001 · promoción por QA y auditoría por excepciones

- **Fecha:** 2026-09-24.
- **Actor:** usuario, durante la continuación de la migración.
- **Decisión explícita:** los contratos de componentes que ya pasaron QA técnico deben pasar a `specs/`; no desea revisar ni aprobar cada componente por separado. Solicita un documento único donde pueda ver solamente ambigüedades o puntos que no estén completamente resueltos.
- **Aplicación:** para esta migración, tras QA documental e implementación `PASS` vigente, promover el contrato normativo a `specs/` sin duplicar su definición. Conservar `status: DELEGATED_FOR_BUILD` y `user_audit: PENDING`; ubicación publicada no se equipara a `APPROVED`. Registrar digest antes/después si el cambio de ruta obliga a reparar enlaces administrativos. El [documento de auditoría](../specs/MIGRATION-AUDIT.md) concentra decisiones pendientes; requisitos conformes no se someten a aprobación individual.
- **Límite:** no publica por sí solo componentes en la biblioteca Figma ni convierte un QA anterior en vigente si cambia la regla evaluada. Los contratos con conflicto material o QA afectado esperan corrección y revalidación antes de promoción.

## DEC-MIGRATION-VISUAL-FIDELITY-001 · prioridad de color de origen

- **Fecha:** 2026-09-24.
- **Actor:** usuario, durante la continuación de la migración.
- **Decisión explícita:** AI Design System puede recibir componentes y ajustes de buenas prácticas, pero no debe cambiar sus colores ni otros rasgos visuales equivalentes respecto a la Librería anterior sin necesidad demostrada. Si falta un rol semántico, debe definirse un token de destino aliasado a una primitiva existente y sincronizado con JSON, contrato y variable Figma; no inventar una primitiva nueva.
- **Aplicación:** auditar las desviaciones cromáticas ya registradas antes de promover contratos afectados; conservar el valor de origen cuando exista primitiva equivalente y scope correcto. Si fidelidad exacta, contraste y primitivas disponibles no pueden cumplirse simultáneamente, registrar la tensión en [auditoría por excepciones](../specs/MIGRATION-AUDIT.md) sin elegir silenciosamente. Se mantiene la separación entre Figma técnico, publicación de biblioteca y frontend.
- **Relación:** precisa y restringe DEC-SEMANTIC-EXTENSIONS-001 para nuevas construcciones y revisiones cromáticas; no borra las decisiones históricas ni afirma que las implementaciones anteriores ya estén corregidas.

## DEC-CHARTS-DEMO-VALUE-001 · porcentaje de muestra en Charts

- **Fecha:** 2026-09-24.
- **Actor:** usuario, en respuesta a AUD-001 de la auditoría por excepciones.
- **Decisión explícita:** el texto `80%` de Charts es solamente para demos. Se conserva como muestra estática; no expresa un cálculo ni una correspondencia numérica demostrada con el largo de las barras.
- **Límite:** esta decisión cierra el punto de la reconstrucción Figma, pero no define la regla de datos de un producto futuro. El contrato de Charts ya distingue muestras y comportamiento no inferido; no se modifica su definición ni su digest de QA.

## DEC-MIGRATION-CONTRAST-LIMITATIONS-001 · fidelidad cromática y revisión interna

- **Fecha:** 2026-09-24.
- **Actor:** usuario, en respuesta a AUD-002 de la auditoría por excepciones.
- **Decisión explícita:** mantener por ahora los colores de la Librería anterior aun cuando existan limitaciones de contraste; marcar las limitaciones verificadas con un asterisco para revisión interna del equipo, sin ajustar el color solo para alcanzar un umbral.
- **Aplicación:** revertir los cambios cromáticos hechos exclusivamente por contraste en las implementaciones afectadas, conservando bindings semánticos del scope correcto a primitivas existentes y paridad JSON/Figma. Medir cada par relevante después del cambio y registrar en [la auditoría](../specs/MIGRATION-AUDIT.md) el valor, el criterio aplicable y `*` si incumple. El marcador es documental, no contenido visible del componente.
- **Límite:** no equivale a certificar accesibilidad. Los QA anteriores basados en colores modificados quedan `STALE` para la parte cromática hasta restauración y readback; el resto de sus comprobaciones históricas no se borra.

## DEC-TOGGLE-MIXED-001 · selección agregada parcial

- **Fecha:** 2026-09-24.
- **Actor:** usuario, mediante explicación verbal y [PNG adjunto](../references/toggle-mixed-user-2026-09-24.png); criterio de implementación delegado a Codex, auditoría humana `PENDING`.
- **Decisión explícita:** cuando un control representa varios toggles y algunos están activos mientras otros están inactivos, mostrar un valor visual neutral o mixto con guion centrado. Se permite agregar propiedades si hiciera falta para evitar confusión.
- **Normalización acotada:** ampliar la propiedad existente `Toggle` con `Mixed` y conservar `State` como eje independiente; no añadir un eje redundante. Añadir Mixed en Default/Hover/Focus/Disabled con la apariencia del PNG y roles de icono del JSON existente, sin cambiar colores de las ocho variantes anteriores ni crear tokens nuevos. Ver [enmienda 0.1.4](../drafts/contracts/toggle.mixed-amendment.v0.1.4.md) y [comportamiento](../drafts/behavior/toggle-mixed/behavior-contract.md).
- **Límite:** no se ha definido qué hace el clic sobre Mixed ni el caso de grupo vacío. Esta enmienda no implementa comportamiento web ni publica la biblioteca.

## DEC-MIGRATION-TRACEABILITY-001 · contrato transversal de fidelidad y bindings

- **Fecha:** 2026-09-24.
- **Actor:** usuario, al solicitar revisar todos los contratos existentes y seguir migrando las familias restantes.
- **Decisión explícita:** todos los contratos deben documentar consistentemente colores y tokens vinculados, comprobar su concordancia con los datos reales y conservar una regla escrita en Markdown que se aplique a la migración futura.
- **Aplicación:** [MIGRATION-TOKEN-TRACEABILITY-001](../specs/MIGRATION-TOKEN-TRACEABILITY.contract.md) es la regla transversal. El [JSON aprobado](../sources/inventories/tokens.inventory.json) y las extensiones versionadas retienen la autoridad sobre datos de tokens; el contrato transversal define la cadena obligatoria de procedencia y QA, sin duplicar descripciones ni valores. La [matriz de cobertura](../specs/MIGRATION-TRACEABILITY-STATUS.md) distingue auditorías vigentes de pendientes. Continuar con las familias restantes solo tras su contrato, QA documental y preflight.
- **Límite:** esta decisión no declara que todos los contratos previos ya cumplen ni aprueba retroactivamente sus detalles. Un QA cromático previo a las decisiones de fidelidad debe revalidarse antes de promoción a `specs/`.

## DEC-MIGRATION-MISSING-PRIMITIVE-001 · excepción acotada para un RGB fuente ausente

- **Fecha:** 2026-09-24. **Actor:** usuario, al ampliar la autoridad de migración para agregar elementos que falten en AI Design System, conservando los colores de la Librería anterior y creando el token a partir de su primitiva; auditoría humana de cada resultado `PENDING`.
- **Alcance:** sustituye únicamente la prohibición anterior de añadir una primitiva cuando el color fuente no existe en el inventario ni en las variables del destino. Primero se verifica la ausencia exacta; después se registra la nueva primitiva en un JSON de extensión versionado, se crea la variable local, se define un rol semántico de scope correcto que la aliasa, y se comprueba paridad JSON/Figma/consumidores. No autoriza recolorear componentes, modificar primitivas existentes ni usar roles fuera de categoría.
- **Aplicación concreta:** [Scrollbar](../specs/scrollbar.contract.v0.1.0.md) requiere el gris original `#C3C6D4`, ausente en las primitivas previas. [Foundations 0.1.16](../specs/foundations.scrollbar-colors.amendment.v0.1.16.md) crea `color/neutral/350` y `color/background/scrollbar/thumb`; [QA](../qa/implementations/scrollbar-colors.v0.1.0.figma.review.md) comprueba cuatro aliases y 30 consumidores. El inventario histórico de la Librería anterior no se sobrescribe.
- **Estado posterior:** criterio de crear primitiva nueva sustituido por [DEC-MIGRATION-NEAREST-PRIMITIVE-001](#dec-migration-nearest-primitive-001--preferir-una-primitiva-existente-con-token-semántico). La extensión 0.1.0 y su QA son históricos; no describen el alias vigente. Esta decisión no aprobó el significado funcional del rótulo `75%` ni publicó la biblioteca Figma.

## DEC-MIGRATION-NEAREST-PRIMITIVE-001 · preferir una primitiva existente con token semántico

- **Fecha:** 2026-09-24. **Actor:** usuario, tras la construcción inicial de Scrollbar; auditoría humana de los componentes `PENDING`.
- **Decisión explícita posterior:** cuando el RGB de origen no tenga primitiva exacta, usar la primitiva existente que más se asemeje en el JSON y las variables de Figma; no aplicar la primitiva directamente al componente, sino consumir un token semántico del scope adecuado aliasado a ella. La instrucción desplaza para ese caso la extensión de primitiva nueva de DEC-MIGRATION-MISSING-PRIMITIVE-001. Conservar y documentar la diferencia visual respecto del origen; no afirmar fidelidad cromática exacta.
- **Aplicación a Scrollbar:** la comparación perceptual CIELAB ΔE76 de las primitivas COLOR locales previas a la extensión dio `color/neutral/300` `#E2E8F0` como más cercana a `#C3C6D4` (12.24); neutral/400 obtuvo 14.73. La variable semántica `color/background/scrollbar/thumb` conserva su identidad y scope `SHAPE_FILL`, pero sus cuatro aliases pasan a neutral/300. La primitiva nueva `color/neutral/350` queda obsoleta y se retirará tras comprobar que no tiene consumidores directos. Contrato, JSON, QA y auditoría registran el cambio.
- **Límite:** esta autorización no permite usar un rol de texto/icono como fondo, modificar neutral/300, cambiar colores donde sí exista primitiva exacta ni ocultar el contraste reducido.

## DEC-BADGE-SOURCE-COLOR-001 · restauración delegada de colores Feedback

- **Fecha:** 2026-09-24.
- **Actor:** Codex bajo las decisiones explícitas DEC-MIGRATION-VISUAL-FIDELITY-001 y DEC-MIGRATION-CONTRAST-LIMITATIONS-001; auditoría humana `PENDING`.
- **Evidencia:** comparación de seis variantes Badge fuente/destino encontró tres colores desviados por la corrección de contraste anterior: Informational text y Warning text/icon. El rol compartido warning/icon también afectaba un vector de Inline Notifications.
- **Decisión acotada:** restaurar los roles y RGB fuente mediante [enmienda Badge 0.1.2](../specs/components/badge.source-color-amendment.v0.1.2.md) y [override Foundations 0.1.1](../drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.1.json), con alias a la primitiva amber/600 existente, scopes correctos y readback de ambos consumidores. Conservar la limitación de contraste `*` en [auditoría](../specs/MIGRATION-AUDIT.md); no modificar colores de otras familias ni crear variables.
- **Límite:** el QA de contraste previo queda histórico en los aliases/paints sustituidos; esta decisión no certifica accesibilidad ni aprueba/publica la biblioteca.

## DEC-SELECTION-CONTROL-SOURCE-COLOR-002 · contorno neutral de origen

- **Fecha:** 2026-09-24. **Actor:** Codex bajo DEC-MIGRATION-VISUAL-FIDELITY-001 y DEC-MIGRATION-CONTRAST-LIMITATIONS-001; auditoría humana `PENDING`.
- **Hallazgo:** Checkbox Unselected Default/Focus y Radio Button Off Default usan neutral/400 `#94A3B8` en la fuente, pero el rol semántico compartido `color/border/control` resolvía neutral/500 en el destino. Las frases de contraste de DEC-RADIO-NORMALIZATION-001 y de la construcción Checkbox 0.1.0 quedan históricas solo para esos tres contornos.
- **Decisión acotada:** [override JSON 0.1.1](../drafts/foundations/ai-design-system.control-colors.v0.1.1.json) y [enmienda Foundations 0.1.12](../drafts/contracts/foundations.control-border-source-color.amendment.v0.1.12.md) sustituyen solo cuatro aliases del rol existente por la primitiva neutral/400, sin cambiar scope, descripción ni `color/background/control-hover`. [Checkbox 0.1.1](../drafts/contracts/checkbox.source-color-amendment.v0.1.1.md) y [Radio Button 0.1.1](../drafts/contracts/radio-button.source-color-amendment.v0.1.1.md) acotan la sustitución de sus contratos base.
- **Verificación y límite:** [QA Figma](../qa/implementations/selection-control-source-color.v0.1.1.figma.review.md) `PASS` para tres consumidores y cuatro modos. Contraste original ~2.56:1 `*`; no se certifica accesibilidad, aprobación humana ni publicación.

## DEC-STEPPER-BRAND-THEMING-001 · acentos de Stepper por tema

- **Fecha:** 2026-09-24. **Actor:** usuario, mediante instrucción explícita posterior a la construcción inicial de Stepper.
- **Decisión explícita del usuario:** los acentos de Stepper deben ser colores de marca para cambiar con el tema. Esta intención sustituye el verde/azul fijo observado en la Librería anterior.
- **Normalización delegada de Codex:** `Checked` usa marca fuerte en círculo y conector; `Default` usa marca base en círculo; `Inactive` y conectores neutros permanecen sin cambio. La distinción fuerte/base aprovecha roles existentes y preserva jerarquía visual; no se atribuye al usuario la elección exacta de esos dos roles.
- **Aplicación:** [enmienda de componente 0.1.1](../specs/stepper.brand-theme.amendment.v0.1.1.md), [Foundations 0.1.20](../specs/foundations.stepper-brand.amendment.v0.1.20.md) y [JSON vigente 0.1.1](../drafts/foundations/ai-design-system.stepper-colors.v0.1.1.json). Tres roles de Stepper aliasan directamente las primitivas de `color/brand/strong` o `color/brand/default` en cada modo. Los consumidores retienen bindings semánticos; cero variables y primitivas nuevas.
- **Verificación y límite:** [QA Figma 0.1.1](../qa/implementations/stepper.v0.1.1.figma.review.md) comprobó doce equivalencias de alias y 122 pinturas vinculadas. La decisión no modifica anatomía, comportamiento, auditoría humana ni publicación; si cambia el mapa de marca, se debe revalidar Stepper.

## DEC-STEPS-BRAND-THEMING-001 · acentos de Steps por tema

- **Fecha:** 2026-09-24. **Actor:** usuario, al pedir para Steps el mismo cambio de marca por tema solicitado para Stepper.
- **Decisión explícita del usuario:** los acentos de Steps deben responder al color de marca cuando cambia el tema. Sustituye el azul fijo observado en la Librería anterior, sin pedir cambio de anatomía ni de los blancos/neutros contextuales.
- **Normalización delegada de Codex:** el dot seleccionado `On White` sigue `color/brand/default`; el no seleccionado `On Primary` y el seleccionado de la Gallery legada siguen el nivel 300 de la familia cromática de cada tema. La elección exacta de base/300 no se atribuye al usuario; conserva la jerarquía visual del origen. Los roles siguen siendo semánticos de `SHAPE_FILL`, aliasados directamente a primitivas existentes en cada modo.
- **Aplicación:** [enmienda Steps 0.1.1](../specs/steps.brand-theme.amendment.v0.1.1.md), [Foundations 0.1.21](../specs/foundations.steps-brand.amendment.v0.1.21.md) y [JSON vigente 0.1.1](../drafts/foundations/ai-design-system.steps-colors.v0.1.1.json). No se crearon variables ni primitivas y se conserva la diferencia histórica `On Primary` de AUD-008.
- **Verificación y límite:** [QA Figma 0.1.1](../qa/implementations/steps.v0.1.1.figma.review.md) comprobó 28 aliases, 173 pinturas y 27 combinaciones. Auditoría humana y publicación siguen pendientes; un cambio posterior al mapa de marca exige resincronizar estos aliases directos.
## DEC-LOADER-COLOR-CYCLE-001 · color estable durante toda la animación

- **Fecha:** 2026-09-25. **Actor:** Codex bajo la delegación de migración de la Librería anterior; auditoría humana PENDING.
- **Hallazgo observado:** Loader fuente contiene cuatro ciclos de 24 fotogramas Primary. Las variantes públicas Secondary, Default y On color sobrescriben solo el primer fotograma; las transiciones apuntan a fotogramas que conservan Primary. El origen no demuestra persistencia cromática.
- **Resolución delegada:** mantener los 16 nombres y tamaños públicos, pero construir una secuencia local de 24 fotogramas para cada combinación Size×Color. Todos los fotogramas consumen el mismo rol semántico color/icon del color de su variante, con aliases existentes en cuatro modos. Se preservan los RGB de Contable y no se añaden tokens.
- **Verificación:** [contrato Loader](../specs/loader.contract.v0.1.0.md) y [QA Figma](../qa/implementations/loader.v0.1.0.figma.review.md) comprueban 384 transiciones y 768 pinturas vinculadas. No implica aprobación humana ni publicación.
## DEC-MIGRATION-SPECS-CANONICAL-001 · ajustes normativos directamente en specs

- **Fecha:** 2026-09-25. **Actor:** usuario, al confirmar que todos los contratos completados de la migración deben pasar a specs y que los ajustes posteriores se hagan allí.
- **Decisión explícita:** una vez que un contrato de componente tenga QA documental y QA técnico de implementación PASS, promoverlo a specs. Cualquier ajuste posterior a ese contrato se redacta en specs, no como contrato normativo paralelo en drafts.
- **Aplicación:** conservar la versión anterior y hacer una revisión versionada o enmienda que identifique las reglas sustituidas; actualizar QA, referencias y Figma/JSON cuando el ajuste los afecte. La observación fuente y los reportes de trabajo pueden seguir en drafts.
- **Límite:** estar en specs no cambia DELEGATED_FOR_BUILD a aprobación humana, no publica automáticamente la biblioteca Figma y no permite promover contratos cuyo QA técnico esté pendiente. [Loader](../specs/loader.contract.v0.1.0.md) ya cumple la ubicación requerida.

## DEC-SLOTS-IMPLEMENTATION-001 · aplicación a composiciones existentes

- **Fecha/actor:** 2026-09-29, usuario: «Revisa los componentes y aplica el protocolo a los que consideres pertinentes dede su contrato y en figma».
- **Alcance:** revisar aplicabilidad y actualizar contratos y Figma conforme a P-SLOTS. Primera intervención justificada: Select/Options, Switch Tab/Tabs y Breadcrumbs/Trail, según [enmienda COMPOSITION-SLOTS-001](../specs/composition-slots.amendment.v0.1.0.md). Selección técnica delegada, no aprobación humana individual.
- **Límites:** conservar paleta, tokens, dependencias y principales; no inventar selección automática, límites de producto o frontend. Pruebas desde instancias consumidoras y readback nativo obligatorios. Otros candidatos quedan identificados en la matriz, no validados por extensión.
- **Estado:** QA documental PASS; implementación y QA técnico se registran separadamente. Auditoría humana PENDING, biblioteca sin publicar, Graphify STALE.

## DEC-INPUT-FIELD-NORMALIZATION-001 · reconstrucción semántica del campo

- **Fecha:** 2026-09-28. **Actor:** agente bajo delegación de migración, no aprobación humana individual.
- **Alcance:** Input Field fuente 186:14461 → destino 397:152. Tres ejes Size/State/Value conservan 30 combinaciones. autoFocus redundante se absorbe en State=Focus; cuatro textos, siete booleanas y swap de icono quedan editables.
- **Tokens:** reutilizar 33 roles existentes y sus aliases; no crear primitivas ni roles. Tipografía Manrope local con tracking 0 y line-height 20/16; diferencias frente a origen y halo #F8FAFC→blanco explícitas en [contrato](../specs/input-field.contract.v0.1.0.md).
- **Corrección por evidencia:** seis soportes rectangulares de Focus preservan el render original. Fondo background/default, efecto focus/effect-outer: sin reutilizar STROKE_COLOR como fill. QA visual y estructural posterior PASS.
- **Límite:** contraste original conservado; no inferir Eye, tooltip o validación web. Auditoría humana PENDING; no modifica otras familias ni publica biblioteca Figma.

## DEC-INPUT-FIELD-DISABLED-TEXT-001

- **Fecha/actor:** 2026-09-28, usuario. Aprobación explícita: «De acuerdo aplica el cambio en su documentación y en figma», después de la propuesta de unificar el color Disabled para placeholder y valor precargado.
- **Decisión:** State=Disabled usa color/text/disabled independientemente de Value. Se conserva Value=Empty/Filled como contenido, no como disponibilidad. Sustituye la conservación de texto primary en Filled/Disabled del contrato 0.1.0.
- **Alcance aprobado:** [enmienda 0.1.1](../specs/input-field.disabled-text.amendment.v0.1.1.md), SHA-256 fc73aef18bd2c4ca6fcdd4eaa17d92c9e65aee0f4e54ff993eb9aeefc0f98a45. Tres textos y descripción del set; no aprueba otros cambios ni otras familias.
- **Resultado:** [QA acotado PASS](../qa/implementations/input-field.v0.1.1.figma.review.md), sin variables nuevas. Contraste Disabled conservado; auditoría global pendiente y biblioteca sin publicar.

## DEC-LOGOS-REMAINDER-OMITTED-001 · continuar con las siguientes familias

Este alcance omitido no bloquea Select ni otras familias. El punto actual está en [continuación de Select](SESSION-HANDOFF-2026-09-28-SELECT.md).

- **Fecha/actor:** 2026-09-28, usuario: «Continúa con los siguientes componentes, omite el resto de logos».
- **Alcance EXPLICIT:** omitir la copia de los doce assets sueltos pendientes. Conservar los seis sets ya copiados y su evidencia; no borrar, reimportar ni afirmar que se completó toda la familia.
- **Efecto:** el acceso al navegador para copiar esos assets deja de ser un bloqueo del proyecto. Select es la siguiente familia en construcción bajo la delegación vigente. Las diferencias geométricas ya registradas en Logos y su QA global pendiente no se resuelven ni se ocultan por esta decisión.
- **Trazabilidad:** el estado de Logos registra el remanente fuera del alcance actual. Graphify permanece STALE; no se modifican primitivas, tokens ni archivos Figma por esta decisión.

## DEC-DROPDOWN-ITEM-NORMALIZATION-001 · semántica y editabilidad

- **Fecha/actor:**2026-09-28, agente bajo delegación de migración; no aprobación humana individual.
- **Fuente:**18 variantes de drop-down-item2479:11730. Reconstrucción en página Select con nombres de ejes del destino. No completar combinaciones no observadas.
- **Decisión acotada:** texto Selected usa color/text/brand; iconos usan color/icon del estado; divisor se representa como trazo de border/strong. Mismos RGB, scopes correctos, sin tokens nuevos. Interlineado AUTO22/19→24/20 tokenizado y segunda columna sin recorte; checkbox coherente con selección/disponibilidad; swap de icono derecho añadido.
- **Alcance:** [DROPDOWN-ITEM-0010.1.0](../specs/dropdown-item.contract.v0.1.0.md), no las composiciones Select. QA técnico PASS, auditoría humana PENDING. Contraste original conservado con asterisco; no biblioteca publicada.

## DEC-LOGOS-AGNOSTIC-ASSETS-001 · documentar primero y copiar fielmente

- **Fecha/actor:** 2026-09-28, usuario. Instrucción explícita: «Los logos, necesito que queden bien documentados primero [...] no usan nada de variables ni tokens del json, son agnósticos [...] hay que copiarlos y pegarlos».
- **Alcance EXPLICIT:** exclusivamente Logos de la Librería anterior hacia AI Design System. Documentar antes de copiar los originales fielmente, sin redibujarlos, aproximar sus colores a la paleta UI ni adaptarlos al tema. Sin consumo de variables, primitivas directas o tokens semánticos en el asset.
- **Excepción normativa acotada:** para el artwork de Logos no se exige la cadena de tokenización de REQ-MTT-002–004 del contrato transversal y su enmienda 0.1.2. La documentación del asset justificará `Design tokens: NOT_APPLICABLE` por esta decisión. La excepción no se extiende a fondos, textos, botones u otros controles que acompañen al logo.
- **Documentación previa:** inventario y variantes realmente observadas; nombres e IDs fuente, dimensiones/proporciones, vectores/imágenes/gradientes y dependencias; destino previsto y, después de copiar, mapa de IDs reales. No inventar variantes ni reglas de marca no demostradas.
- **QA posterior:** comparación visual y estructural fuente/destino, preservación de colores, proporciones y recursos, y ausencia de bindings a variables en el asset. Si existen bindings heredados, documentarlos y preservar la apariencia al desvincularlos en destino, sin modificar la fuente. Este registro no declara ese QA ejecutado.
- **Impacto conocido:** el [descubrimiento histórico de Logo Categoria](../drafts/reports/logo-categoria.discovery.v0.1.0.md) describe cuatro variantes y propone mapear `logo/categoria`. Esa propuesta queda sustituida para el asset; la selección del logo desde un consumidor como Header se documentará por separado, sin introducir variables dentro del logo. El informe histórico no se reescribe como observación nueva.
- **Cierre documental:** leídos P05, contrato transversal/enmienda 0.1.2 y descubrimiento histórico; registrados criterio y matriz de pendientes. Contrato completo e inventario de Logos aún pendientes; copia Figma NOT_STARTED en esta entrega. No se modificaron Figma, JSON ni otras familias. Graphify sigue STALE, sin regenerar. No se requiere otra aprobación para esta excepción explícita.

## DEC-CHAT-TOOLBAR-INTEGRATION-001 · 2026-10-08

Solicitud EXPLICIT del usuario: integrar20355:72872 y sus dependencias locales del mismo archivo. Se aplica [delegación externa](./DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md), no nueva aprobación humana. Decisiones DERIVED de construcción en [contrato](../specs/chat-toolbar.contract.v0.1.0.md): tres sets/nueve variantes, roles temáticos existentes, logo agnóstico, texto configurable y Slots nativos, barra estática28% coherente con42/150. No importar todos los componentes Anticipa ni crear tokens nuevos. Diferencias visuales/contraste documentadas; QA PASS no cambia auditoría PENDING.
