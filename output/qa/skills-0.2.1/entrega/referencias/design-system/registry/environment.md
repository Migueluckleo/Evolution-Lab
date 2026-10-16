# Environment Registry

## Web y Graphify · cotejo contractual0.1.3 · 2026-10-13

Herramientas existentes READY; versiones locales sin cambios.43 familias cotejadas;59 pruebas Chrome,9 unitarias, TypeScript/build/generación comprobados. [QA y resolución del permiso](../qa/implementations/web.contract-audit.v0.1.3.review.md). La lectura de metadatos/trazados Figma fue posible; auto-review rechazó inicialmente exportar los dos raster privados de Modal. Después de la autorización específica del usuario, ambos se copiaron y sus hashes se verificaron. No se instalaron herramientas.

Graphify STALE durante el lote `2026-10-13-web-contract-audit`; cierre con respaldo, actualización AST y extracción semántica de documentos/capturas, hashes/manifiesto/consultas y readback. El estado definitivo reside en su closure.json y scripts/ds check. Ninguna frase de esta entrada anticipa CURRENT. Uso semántico medido UNAVAILABLE; no se declara cero. La vigencia del grafo y la validación visual web son estados distintos.

## Web y Graphify · cierre de fidelidad · 2026-10-13

Herramientas existentes READY; sin instalaciones ni cambios globales. Figma MCP disponible para lectura y las ocho exportaciones Logos restantes;72/72 locales al cierre. Chrome/localhost autorizado por auto-review, sin rechazo de aprobación. Suite final15/15, código8/8, TypeScript/build/generación PASS. [QA](../qa/implementations/web.fidelity.v0.1.2.review.md).

Graphify STALE durante las ediciones; lote completo `2026-10-13-web-fidelity` con respaldo, AST y semántica por fuentes cambiadas, reutilización por hashes del resto, readback JSON/reporte/HTML, integridad/cobertura/manifiesto y consultas. CURRENT únicamente tras closure.json y scripts/ds check coincidentes con el corpus. Uso semántico medido UNAVAILABLE. Esta entrada sustituye los límites de assets web anteriores, no sus resultados históricos ni el QA Figma.

## Web · 2026-10-13

[DEC-WEB-COMPONENTS-001](decisions.md) habilita dependencias locales. Node 24.19.0 existente en `/Users/miguel.leo/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin`; pnpm 11.25.0. Instalación confinada a implementations/web, versiones y lockfile registrados allí. React 19.3.0, Next 16.4.0, Tailwind 4.3.3, TypeScript 7.0.2; fuente Manrope e iconos Phosphor locales. Sin actualizaciones globales.

Figma MCP corporativo permitió inspección y 64 exportaciones de Logos; alcanzó el límite de consultas con ocho pendientes. Sin escrituras Figma. Chrome existente utilizado para QA local. El sandbox impidió inicialmente escuchar en localhost; ejecución local de Chrome/servidor autorizada por auto-review. [Evidencia y comandos](../qa/implementations/web.v0.1.0.review.md).

Grafo STALE durante el lote. Cierre completo `2026-10-13-web-components-v2` por P05; CURRENT exclusivamente si graphify-out/runs/2026-10-13-web-components-v2/closure.json y el check final confirman hashes y cobertura. Se preserva el corte anterior; uso semántico medido UNAVAILABLE. Node_modules, builds, public/assets y metadatos duplicados quedan fuera del corpus según configuración. El detector se complementa con tres fuentes web exactas: los dos CSS de autoría y pnpm-lock.yaml, omitidos por su detección genérica; se registran como texto semántico y se controlan por hash.

## Retención Git · 2026-10-13

Git y Python/stdlib existentes. [Política](../references/ARTIFACT-RETENTION.md) y [verificación de recuperación](../qa/tooling/retention.2026-10-13.review.md): 673 bajas del índice, archivos locales conservados y respaldo tar.gz de 7,840,848 bytes con digest y restauración probados. Se mantienen 1,187 archivos de fuentes/evidencia/entregables con hashes idénticos. Sin instalación, commit, publicación remota ni reescritura de historia.

El cierre de este lote usa scripts/ds graph prepare/close con ID 2026-10-13-retention y el corpus completo. Grafo STALE durante las ediciones; CURRENT solamente si graphify-out/runs/2026-10-13-retention/closure.json y el check final lo verifican. Cachés y copias before/staged/after son locales según la política; comprobantes y semántica se conservan. Uso semántico medido UNAVAILABLE.

## Herramientas de prioridades altas · 2026-10-13

[DEC-PROJECT-HIGH-PRIORITIES-001](decisions.md) implementada mediante [scripts/ds](../scripts/ds) y [configuración](../config/ds-project.json). Graphify 0.9.65/Python 3.12.13 y Ruby/Psych 3.1.0 existentes; ninguna instalación. CLI local: check, status, graph plan/prepare/close/check y test. Node no disponible en el PATH comprobado; verificadores .cjs históricos no se ejecutaron ni se atribuyó nuevo QA Figma.

La ejecución requerida graphify update . salió 0, produjo un corte AST de 7,546 nodos/13,581 relaciones e indicó cuatro fuentes fuera del detector ordinario. Se preservaron su log/resultados y se restauraron por hash los ocho outputs previos antes del cierre completo; un resultado AST aislado no acredita vigencia documental. Evidencia en graphify-out/runs/2026-10-13-tooling-ast-check/.

[QA y límites](../qa/tooling/project-tooling.2026-10-13.review.md). Grafo STALE durante el lote. CURRENT exclusivamente cuando scripts/ds check confirme corpus/vista/outputs y el cierre de graphify-out/runs/2026-10-13-high-priorities/ indique CURRENT. HTML agregado por comunidades (>5,000 nodos); uso semántico medido UNAVAILABLE. No nuevas capacidades externas, hooks o configuración global.

## Graphify · verificación y diagnóstico del proyecto · 2026-10-13

Solicitud: verificar instalación Graphify y analizar optimización documental. **Herramienta READY**: `graphifyy` 0.9.65 vía uv, Python 3.12.13; CLI, importación, extracción AST temporal y consultas probadas. Skill local `.codex/skills/graphify/SKILL.md`; no instalaciones ni configuración global. Hooks Git no instalados; `.codex/hooks.json` presente, activación por el host no verificada.

El corte inicial coincide con los 1,172 hashes del manifiesto y outputs del cierre Fuentes: 8,058 nodos, 18,019 relaciones, cero IDs duplicados/endpoints rotos. 459 JSON parseados; 21 enlaces relativos históricos siguen documentados. Detector genérico requiere los suplementos de diseño ya existentes. [Evidencia calculada](../graphify-out/runs/2026-10-13-project-audit/baseline-verification.json) y [reporte con propuestas](../drafts/reports/project-optimization.audit.2026-10-13.md). Recomendaciones no adoptadas; sin cambios a contratos, tokens o Figma.

Este lote documental requiere cierre incremental por P05 §8/DEC-GRAPH-CONTINUOUS-SYNC-001, en `graphify-out/runs/2026-10-13-project-audit/`, preservando respaldo. **CURRENT solo con verification.json y manifest-check.json PASS y hashes finales concordantes**; STALE/BLOCKED si falla. HTML agregado por comunidades al superar 5,000 nodos; coste semántico medido UNAVAILABLE, no cero. No certifica QA de Figma ni aceptación humana.

## Chat layout · inspección y grafo2026-10-09

Figma MCP READY para lectura; cuatro principales/478 nodos recorridos. Lotes iniciales superaron salida20480bytes; relectura acotada completa sin escrituras. [QA](../qa/implementations/chat-layout.v0.1.1.review.md). Graphify/runtime existentes, sin instalaciones. Sincronización incremental estructural+semántica del corpus completo bajo P05; respaldo y artefactos en `graphify-out/runs/2026-10-09-chat-layout/`. CURRENT solo con verification.json, manifest-check.json y closure.json PASS/CURRENT y hashes finales concordantes; STALE/BLOCKED en caso contrario. HTML agrega comunidades por >5000 nodos; uso medido de agentes UNAVAILABLE, no cero. No publicación remota ni cambios frontend.

## Graphify y Figma · Characters2026-10-08

Figma MCP READY, fuente read-only y destino verificado. Límites código50000 caracteres/salida20480 bytes, construcción en lotes4/4/5. Graphify READY; sync completo autorizado por P05§8/DEC-GRAPH-CONTINUOUS-SYNC-001. STALE durante delta; CURRENT condicionado a verification.json/manifest-check.json PASS y closure.json en graphify-out/runs/2026-10-08-characters/. Sin instalaciones/servicios nuevos. HTML >5000 nodos agrega comunidades; coste agentes UNAVAILABLE, no cero.

## Chat Section · corte de grafo · 2026-10-08

MCP corporativo permitió fuente en lectura y construcción/QA acotados en AI Design System. Sin instalaciones ni publicación remota. [Handoff](SESSION-HANDOFF-2026-10-08-CHAT.md). Sincronización del corpus completo por delta bajo P05§8: run2026-10-08-chat-section, respaldo del corte anterior, reutilización semántica por hash y extracción del delta. CURRENT solo si [verification](../graphify-out/runs/2026-10-08-chat-section/verification.json) y [manifest-check](../graphify-out/runs/2026-10-08-chat-section/manifest-check.json) indican PASS y siguen coincidiendo los bytes; de otro modo STALE/BLOCKED. Los registros de cierre forman parte del corte antes de extraer. Uso de tokens de agente UNAVAILABLE, no cero.

## Graphify · sincronización completa · 2026-10-08

La decisión [DEC-GRAPH-CONTINUOUS-SYNC-001](DEC-GRAPH-CONTINUOUS-SYNC-001.md) autoriza esta actualización local y la sincronización de futuros cierres relevantes según P05 0.2.4. El estado de este corte se determina por [verification.json](../graphify-out/runs/2026-10-08-full-sync/verification.json) y [manifest-check.json](../graphify-out/runs/2026-10-08-full-sync/manifest-check.json): **CURRENT únicamente si ambos existen, indican PASS y los hashes del corpus siguen coincidiendo**; en otro caso STALE/BLOCKED. Esta entrada no declara PASS por anticipado.

Extracción estructural de datos/código, semántica de documentos modificados y reutilización comprobada por hash de aportes sin cambios. Incluye Conversation, la excepción de identidad BENI/NAVI, promociones a specs, refinamientos y fuentes Mermaid del flujo FigJam. Respaldo del corte anterior y procedencia conservados en `before/` del run. Se inspeccionan y añaden únicamente las rutas de datos de diseño filtradas por nombre; no se desactiva el filtro de secretos. Los registros anteriores conservan su estado histórico, no describen este nuevo corte.

Graphify y runtimes existentes; sin instalaciones, configuración global, publicaciones ni cambios en Figma. Consumo medido de agentes UNAVAILABLE, no cero. JSON, reporte, HTML, cobertura de fuentes, integridad de relaciones y manifiesto se contrastan antes de declarar el cierre. El grafo no sustituye contratos, datos canónicos ni QA de implementación.

## FigJam · documentación del flujo SDD · 2026-10-07

Figma MCP permitió leer/escribir el tablero `2SYQAjj9nZMF2a2yUSbPTf` mediante la conexión personal; la conexión corporativa no tenía acceso de edición. Se verificó la identidad con whoami, sin modificar permisos. Skills figma-use, figma-use-figjam y figma-generate-diagram aplicadas. Una retirada del boceto inicial fue rechazada automáticamente; se conservó íntegro en histórico y se completó por la alternativa no destructiva. Graphify consultado como índice, contrastado con fuentes, permanece STALE sin regeneración; su last_query_stamp cambió por la consulta. [Entrega y QA](SESSION-HANDOFF-2026-10-07-FIGJAM-FLOW.md).

## GitHub · publicación de repositorio privado · 2026-10-07

Git `2.50.1 (Apple Git-155)` disponible. Cuenta GitHub verificada: `Migueluckleo`. GitHub CLI `2.102.0` descargado y verificado temporalmente con autorización expresa, sin instalación ni configuración global. Publicación `READY`: `Migueluckleo/CONTPAQi-Design-System-1.0`, visibilidad privada y 1.893 archivos del commit inicial contrastados con la API remota. `origin` configurado y rama `main` con seguimiento de `origin/main`. Alcance y evidencias en [el registro de publicación](github-publication.md). Graphify permanece `STALE` y se conserva sin regeneración.

## App Shell · incorporación Figma · 2026-10-06

MCP Figma corporativo usado para fuente en solo lectura y destino AI Design System. Escritura limitada a nueva página/componente App Shell y pruebas temporales propias. Sin instalaciones, frontend, variables nuevas ni publicación de biblioteca. Graphify consultado para localizar Header/Sidebar; fuentes verificadas directamente. Grafo **STALE** para los nuevos artefactos; no regenerado ni convertido en norma. Snapshot, mapas, QA y contrato en specs conservan el punto de continuidad.

## Anticipa · contrato de composición · 2026-10-06

Lectura local de snapshot/contratos/JSON y consulta orientativa Graphify; escritura solo de candidato, lock derivado, reporte/QA y registros. Sin instalación, nuevo acceso Figma, cambios de código ni publicación. Grafo **STALE_FOR_THIS_NEW_CONTRACT**, no regenerado; specs/inventario/snapshot/grafo conservados según [verificación](../qa/contracts/anticipa-screen-composition.v0.1.0.verification.json). MD es el contrato solicitado; no se crea un YAML normativo paralelo ni otro catálogo editable de tokens.

## Specs · promoción administrativa · 2026-10-06

Solo herramientas locales de lectura/edición y consulta Graphify. Sin instalación, red, cambios Figma ni archivos de código. Grafo STALE_AFTER_REFINEMENT conservado byte a byte; no regenerado para esta operación documental. [Verificación de archivos y datos protegidos](../qa/contracts/specs-promotion.2026-10-06.verification.json). El índice no acredita los19 traslados nuevos; consultar registro de contratos y handoff Specs.

## Logos · paso3 · 2026-10-06

MCP corporativo permitió comparación de2967 nodos, pruebas en clones y cleanup. Principales intactos. No se instalaron herramientas ni se publicaron componentes. Grafo STALE_AFTER_REFINEMENT conservado; consulta solo orientativa y memoria actualizada, no regeneración. Ningún archivo de código modificado.

## Refinamiento Radio/Checkbox · 2026-10-06

MCP corporativo permitió lecturas, corrección de ocho posiciones, pruebas desde instancias y cleanup verificado. Sin instalaciones ni publicación. Graphify **STALE_AFTER_REFINEMENT**: conserva el corte curado anterior, no cubre la promoción documental del punto1 ni este cierre. Consulta acotada usada solo para navegación; ninguna regeneración global en este turno. No se modificaron archivos de código.

## Refinamiento cromático de seis familias · 2026-10-05

Figma MCP corporativo: escritura y readback verificados;832 pinturas,84 definiciones canónicas,42 bindings y doce roles de extensión alineados, cero primitivas nuevas. [QA](../qa/implementations/six-families.color.v0.1.0.review.md). Herramientas READY, sin instalaciones ni publicación remota.

Graphify **STALE_AFTER_SIX_FAMILY_COLOR** respecto de estos contratos, JSON y evidencias nuevas. Se ejecutó el refresco AST obligatorio después de editar scripts, pero produjo3645nodos/5568aristas frente al corte curado4056/8830, sin cubrir la documentación nueva. Para no reemplazar el índice curado por una actualización parcial, se restauraron graph.json, reporte, etiquetas, manifiesto y coste desde el respaldo automático `graphify-out/2026-10-05/`, cuyo hash de graph.json coincide con el corte verificado anterior (`f8db46d0f4dce231c0a3e429f8e80f5cdb210e5afe3bbef0b8f44b84a88a1720`); HTML reexportado desde ese mismo JSON. No se presenta como CURRENT. Los documentos canónicos y el cierre técnico están actualizados independientemente del índice derivado; no se ejecutó una reextracción semántica global en esta tarea cromática.

## Conciliación de pendientes · corte vigente · 2026-10-05

Graphify CURRENT para el corte documental de la lista operativa, condicionado a la [verificación del run](../graphify-out/runs/2026-10-05-pending-reconciliation/verification.json) PASS y su [manifiesto](../graphify-out/runs/2026-10-05-pending-reconciliation/manifest-check.json). Los artefactos previos se conservan en before/ de ese run. Solo se reextraen los documentos cambiados; no nueva auditoría Figma ni lectura del editor. Se conserva herramienta READY, runtime y configuración existentes, sin instalaciones ni nuevas fuentes normativas. El estado de construcción se consulta en [lista vigente](../specs/MIGRATION-TRACEABILITY-STATUS.md), no en colas históricas del índice. Uso de agentes UNAVAILABLE, no cero.

## Estado vigente tras refinamiento Buttons y Chips · 2026-10-05

Graphify **CURRENT** para este cierre, con herramienta READY. El corte incorpora la enmienda Buttons0.2.2 y Chips0.2.1, sus evidencias y registros; sustituye operativamente las marcas STALE inferiores sin borrar su historial. [Verificación del corte](../graphify-out/runs/2026-10-05-refinement-close/verification.json) y [manifiesto comprobado](../graphify-out/runs/2026-10-05-refinement-close/manifest-check.json). El corpus incluye855 archivos soportados;470 contribuciones semánticas sin cambios se reutilizaron por hash. La cobertura del índice no acredita aprobación humana ni QA adicional del DS.

Figma MCP corporativo: Chips conserva30variantes y181nodos;36bindings corregidos y un rol local nuevo, color/icon/inverse, aliasan primitivas existentes sin alterar colores ni geometría. Sus cuatro modos y scopeSHAPE_FILL fueron verificados por readback. [Estado y evidencia](../implementations/figma/filter-chip.semantic.v0.2.1.state.json). Inventario histórico y contrato aprobado intactos. No se instaló software, no se modificó configuración global ni se publicó la biblioteca. Respaldo y extracción incremental en graphify-out/runs/2026-10-05-refinement-close/; coste de agentes UNAVAILABLE, no cero.

## Histórico: estado posterior al refinamiento Buttons · 2026-10-05

Graphify **STALE_AFTER_BUTTON_LOCAL_BINDINGS**: la actualización anterior fue verificada, pero no incluye la enmienda0.2.2, su QA ni el cierre del hallazgo de722bindings. Artefactos del grafo conservados, sin regeneración en esta tarea. La herramienta sigue READY; esta marca no invalida la integridad del corte anterior.

Figma MCP corporativo: lectura, escritura acotada y readback comprobados en set26:81. Nueve variables locales existentes verificadas;722bindings sustituidos sin crear variables/nodos. [Estado y evidencia](../implementations/figma/buttons.local-bindings.v0.2.2.state.json). No se instaló software ni se modificó configuración global.

## Graphify · actualización solicitada · 2026-10-05

Estado de ejecución: CURRENT; herramienta READY (graphifyy0.9.65, Python3.12.13, instalación uv existente). El usuario solicitó explícitamente actualizar el grafo. No se modificaron contratos, Figma, hooks ni configuración global.

Corpus acotado del sistema de diseño:825 archivos soportados, incluidos tres JSON de tokens incorporados por sus rutas previamente verificadas.58 derivados detectados se excluyen: graphify-out, output, tmp, .codex-build y .codex-finalizer; no se ingieren renders/exportaciones como nueva autoridad. El filtro general de secretos permanece activo. Los nombres excluidos por ese filtro e incorporados tras comprobar su estructura de datos de diseño son sources/inventories/tokens.inventory.json, sources/figma-snapshots/input-fields.followups.target-tokens.json y qa/implementations/select.v0.1.0.tokens.json.

417 contribuciones semánticas sin cambios se reutilizan por hash y procedencia;54 documentos y9SVG se extraen de nuevo, además del análisis estructural local. Respaldo en graphify-out/runs/2026-10-05/before/. Script reproducible: graphify-out/refresh-2026-10-05.py, fases prepare/ast/supplement/assemble/verify/manifest. Los contadores de uso de agentes no están disponibles: coste UNAVAILABLE, no cero.

Verificación PASS:825/825 archivos representados,3958 nodos,8588 relaciones,326 comunidades; cero endpoints faltantes, IDs duplicados o bucles. HTML/JSON concordantes, reporte leído e inventario canónico intacto. Consultas search/refinement/current y buttons/remote recuperan Search0.1.1 cerrado y Buttons no corregido; son pruebas acotadas, no búsquedas exhaustivas. [Verificación](../graphify-out/runs/2026-10-05/verification.json), [manifiesto](../graphify-out/runs/2026-10-05/manifest-check.json), [consultas](../graphify-out/runs/2026-10-05/query-smoke.txt). La extracción no acredita QA del DS. Las notas STALE y CURRENT inferiores son cortes históricos, sustituidos operativamente por esta entrada.

## Graphify · contraste de refinamiento · 2026-10-05

Estado: STALE_AFTER_HEADER_TABLE_MODAL_SIDEBAR_EMPTY_STATES_SEARCH_REFINEMENT. Consulta search con budget1300:99 coincidencias,29 mostradas; no cobertura exhaustiva. Relaciones contrastadas con contratos, QA y lecturas Figma. Search vigente es0.1.1, no0.1.0 indexado. No regeneración ni mutación de artefactos Graphify. [Delta y continuación](SESSION-HANDOFF-2026-10-05-REFINEMENT.md).

## Empty states · 2026-10-05

MCP Figma operativo para lectura/escritura, Slots nativos, SVG editable y variables. Importación de ilustraciones privadas por key no disponible; transferidas mediante SVG exportado de origen. Seisroles nuevos en colecciónsemantic, cero primitivas. Sin instalaciones ni permisos ampliados. GraphifySTALE_AFTER_HEADER_TABLE_MODAL_SIDEBAR_EMPTY_STATES; no regenerado. [Continuación](SESSION-HANDOFF-2026-10-05-EMPTY-STATES.md).

## Sidebar · 2026-10-05

MCP Figma operativo para lectura, clones locales sin detach, variables, Slots y QA. Página614:125; tres variables nuevas, sin primitivas. Graphify `STALE_AFTER_HEADER_TABLE_MODAL_SIDEBAR`, no regenerado ni instaladas herramientas. Fuente operativa: [handoff Sidebar](SESSION-HANDOFF-2026-10-05-SIDEBAR.md). SigueEmpty states; publicaciónFigma no realizada.

## Modal · capacidades y delta documental · 2026-10-01

MCP Figma verificado para lectura de fuente, creación en destino, Slots nativos editables desde instancias, variables locales y readback. Página Modal565:122; no instalación ni cambio de permisos. El inventario local conserva332variables; no se crearon variables ni primitivas. Estilos compartidos nuevos deModal documentados en el manifest.

Graphify permanece `STALE_AFTER_HEADER_TABLE_MODAL`. Consulta acotada `modal` usada solo como índice; el estado se confirmó con handoff y Figma. No se regeneró el grafo. La fuente operativa es [continuaciónModal](SESSION-HANDOFF-2026-10-01-MODAL.md) y la matriz vigente; siguiente familiaSidebar.

## Graphify · delta Header · 2026-10-01

STALE respecto a los nuevos artefactos Header creados después del corte Graphify inferior. Se conservó el índice y su evidencia histórica sin reetiquetarlo como actualizado. Este turno construyó Header, sus roles, contratos y QA; no regeneró el grafo global. Próxima actualización debe ingerir el delta y las rutas canónicas en specs, sin reutilizar hashes previos para estos archivos. La consulta de estado vigente se apoya mientras tanto en MIGRATION-TRACEABILITY-STATUS y el handoff Header.

## Graphify · actualización autorizada por lotes · 2026-10-01

**Estado operativo de esta ejecución: CURRENT; herramienta READY.** Sustituye la pausa del preflight inferior y las notas STALE de cortes históricos. El usuario autorizó proceder con el alcance que mejor convenga al proyecto: conciliar registros y actualizar el corpus del proyecto por lotes, conservando historial y respaldo. No incluye reconstrucción de componentes ni publicación Figma. La versión CLI se conserva en 0.9.65; no se cambian hooks ni configuración global.

El corpus comprende 648 archivos de documentación, scripts, datos y capturas soportados de la raíz; los outputs derivados Graphify y `.git` no se reingieren. Se conservan las fuentes históricas con su procedencia, no se promueven a normas. Las tres rutas JSON excluidas por el nombre `tokens` se examinaron como datos Figma y se incorporaron mediante suplemento explícito de rutas exactas; no se modificó el filtro general de secretos ni el contenido del inventario.

- Extracción: AST local, reutilización semántica solo con contenido y fuente coincidentes, 16 lotes de extracción por agentes y deltas de cierre. Los JSON se indexan por identidad, referencias y campos explícitos; el inventario incluye sus 270 tokens y aliases resolubles. No es una nueva validación de bindings Figma.
- Verificación: cobertura de archivos, parseo, IDs, endpoints, bucles, enlaces MD, inventario inalterado, lectura de JSON/reporte/HTML, consultas `slots continuation`, `header continuation` y `search conflict`, y comparación de hashes contra manifiesto. Evidencia reproducible y cifras finales en [verificación](../graphify-out/runs/2026-10-01/verification.json) y [manifiesto comprobado](../graphify-out/runs/2026-10-01/manifest-check.json).
- Se corrigieron colisiones de raíces MD/YAML y se eliminaron autorreferencias triviales introducidas por la normalización de identidades de Graphify. La extracción y evidencia original se conservan en el directorio de ejecución; los pares con varias citas conservan `evidence_records`.
- Respaldo anterior a la ejecución: `graphify-out/runs/2026-10-01/before/`. `graphify-out/2026-09-23/` conserva su carácter histórico, no es otro índice vigente. Los tres outputs activos están directamente en `graphify-out/`.
- Los contadores de tokens de agentes no están expuestos; coste marcado UNAVAILABLE, no cero. El benchmark CLI es una estimación orientativa de recuperación, no consumo medido ni certificación de exactitud.
- Limitaciones: imágenes tratadas como evidencia visual; archivos no soportados conservados sin declarar extracción (paquete ZIP, snapshots de archivo y metadatos de sistema). Las referencias citadas no prueban existencia ni aprobación. CURRENT describe el índice del corte, no el cierre de la migración. DOC-SEARCH-001 sigue abierto en la auditoría y Header sigue como próxima familia.

Comandos reproducibles: intérprete registrado + `graphify-out/refresh-2026-10-01.py` (fases explícitas prepare/ast/supplement/assemble/verify/manifest), `-m graphify export html` y consultas indicadas. El script y los fragmentos son artefactos derivados de esta ejecución, no un nuevo protocolo normativo. Una ejecución futura debe detectar cambios y extraer los deltas antes de reutilizar sus fragmentos; no ejecutar manifest para ocultar trabajo pendiente.

## Graphify · preflight de actualización · 2026-10-01

El usuario autorizó actualizar los grafos y conciliar los registros tras la revisión de desfase. Se consultaron AGENTS, P01, P05, la referencia GRAPH-OPERATIONS y la skill local de Graphify, incluida su referencia incremental. No se modificó Figma ni se reinstaló la herramienta.

- Herramienta verificada: graphifyy 0.9.65, mediante el intérprete ya registrado; ayuda CLI accesible.
- Detección incremental sobre la raíz: 645 archivos soportados, aproximadamente 400180 palabras; 217 de código/datos, 423 documentos y 5 imágenes. El detector encoló 635 archivos como nuevos/cambiados; esta clasificación no significa que todos hayan sido editados desde la última revisión.
- Carpetas principales por número de archivos: drafts 219, qa 189, implementations 113, specs 49 y sources 29. Sin archivos eliminados detectados ni errores de recorrido.
- El detector omitió como potencialmente sensibles `qa/implementations/select.v0.1.0.tokens.json`, `sources/figma-snapshots/input-fields.followups.target-tokens.json` y `sources/inventories/tokens.inventory.json`. Es una clasificación del detector, no una constatación de credenciales. No se alteró el filtro ni se renombraron las fuentes; su cobertura deberá resolverse explícitamente antes de declarar CURRENT.
- La skill exige confirmar alcance al superar 500 archivos. Se pausó antes de extraer, fusionar o sustituir artefactos, para acordar el procesamiento por carpetas/lotes.
- Estado del grafo: **STALE**. Los grafos del 23/09 y su manifiesto se conservaron sin cambios. La conciliación documental y la regeneración siguen pendientes; este preflight no acredita actualización ni QA del sistema de diseño.

## Graphify · historial de instalación y primeros cortes

```yaml
tool: Graphify
package: graphifyy
version: 0.9.65
status: READY
authority: https://github.com/Graphify-Labs/graphify
installation_method: uv tool install graphifyy
installation_scope: user-isolated CLI with project-scoped Codex integration
cli_path: /Users/miguel.leo/.local/bin/graphify
tool_python: /Users/miguel.leo/.local/share/uv/tools/graphifyy/bin/python
tool_python_version: 3.12.13
uv_version: 0.12.17
project_integration: .codex/skills/graphify
codex_hook: .codex/hooks.json
codex_agent_instructions: AGENTS.md graphify section
codex_multi_agent: true
codex_multi_agent_config: /Users/miguel.leo/.codex/config.toml
shell_path_configuration:
  - /Users/miguel.leo/.profile
  - /Users/miguel.leo/.bashrc
graph_root: graphify-out
graph_state: STALE
graph_state_reason: Protocol documentation, approved token records, Button approval/amendment/implementation/QA records, Phosphor Icons source/decision, and approved/published Button 0.2.0 usage documentation changed; Graphify refresh was outside these tasks' authorization.
primary_outputs:
  - graphify-out/graph.html
  - graphify-out/GRAPH_REPORT.md
  - graphify-out/graph.json
supporting_outputs:
  - graphify-out/manifest.json
  - graphify-out/cost.json
  - graphify-out/.graphify_labels.json
  - graphify-out/.graphify_health.json
  - graphify-out/.graphify_python
  - graphify-out/.graphify_root
last_verified: 2026-09-22T13:25:52-06:00
notes:
  - The host system Python is 3.9.6 and does not satisfy Graphify's Python 3.10+ requirement.
  - Graphify runs in uv's isolated environment with Python 3.12.13.
  - The first graph contains 36 nodes, 46 edges, and 9 communities from 17 detected files.
  - Graph health passed with no missing or dangling endpoints, self-loops, duplicate edges, or collapsed endpoint pairs.
  - Semantic extraction used the Codex host agent because no Gemini key was configured; no API key was requested or stored.
  - The graph remains STALE after the Button documentation was added; it was queried only as a non-authoritative index and was not regenerated.
```

### Installation and configuration commands

```bash
curl -LsSf https://astral.sh/uv/install.sh -o /private/tmp/graphify-uv-install.sh
sh /private/tmp/graphify-uv-install.sh
/Users/miguel.leo/.local/bin/uv tool install graphifyy
/Users/miguel.leo/.local/bin/graphify install --project --platform codex
/Users/miguel.leo/.local/bin/uv tool update-shell
```

Codex configuration was completed by setting `multi_agent = true` under
`[features]` in `/Users/miguel.leo/.codex/config.toml`. The official project
installer added the Graphify skill, the Codex hook, and the authorized
Graphify section in `AGENTS.md`.

### Verification commands

```bash
/Users/miguel.leo/.local/bin/uv --version
/Users/miguel.leo/.local/bin/graphify --version
/Users/miguel.leo/.local/share/uv/tools/graphifyy/bin/python --version
/bin/bash -lc 'graphify hook-check'
/Users/miguel.leo/.local/bin/graphify god-nodes --top 5
/Users/miguel.leo/.local/bin/graphify query "What governs the Design System reconstruction and validation?" --budget 800
```

Verification results:

- The CLI reports `graphify 0.9.65`.
- A new login shell resolves `graphify` from `/Users/miguel.leo/.local/bin`.
- The Codex hook check exits successfully with status `0`.
- `graph.json` parses successfully and contains 36 nodes and 46 edges.
- `god-nodes` and a scoped natural-language query both return graph results.
- `graph.html`, `GRAPH_REPORT.md`, and `graph.json` were generated and read back.

### Protocol comparison

No conflicting installation command was found. The current official
documentation still supports `uv tool install graphifyy`,
`graphify install --project --platform codex`, the `graphify` CLI name, and
`multi_agent = true` for Codex parallel extraction. The installed version also
creates a project `.codex/hooks.json` and adds an always-on Graphify section to
`AGENTS.md`; these integration artifacts are not enumerated in Protocol 01 but
do not contradict it.

## Figma · reconstrucción de variables

```yaml
integration: Figma MCP use_figma
integration_version: UNKNOWN
target_file: AI-Design-System
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
editor_type_observed: figma
scope: project destination file only
read_variables: READY
write_collections_modes_variables: READY
readback_variables: READY
component_write_capability: UNKNOWN
verified_on: 2026-09-22
```

El preflight de solo lectura encontró `Page 1` vacía, sin colecciones, variables ni estilos locales. La cuenta autenticada mostró una licencia de edición en un equipo Pro; la capacidad efectiva sobre **este archivo** quedó confirmada al crear y leer de vuelta dos colecciones, cinco modos y 270 variables. No se comprobó escritura de componentes ni páginas. La integración no expuso una versión verificable en esta tarea. Véanse [implementación](implementations.md) y [QA](../qa/implementations/foundations-tokens.figma.review.md).

## Figma · inspección de componentes

```yaml
integration: Figma MCP get_metadata + get_screenshot + use_figma
integration_version: UNKNOWN
target_file: AI-Design-System
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
scope: read-only inspection of node 26:81 and active dependency 26:3/26:2
read_nodes_and_descendants: READY
read_component_properties: READY
read_reactions: READY
read_bound_variables_and_resolve_values: READY
read_named_styles: READY
component_write_capability: UNKNOWN
verified_on: 2026-09-23
```

La lectura completa recorrió 364 nodos sin pendientes, resolvió 35 variables y una dependencia de componente, y conservó una captura visual. No se ejecutaron setters, creación, importación ni otras escrituras. La capacidad de escritura de componentes/páginas sigue sin comprobarse y no se infiere de la lectura.

## Figma · página Buttons y QA de Button

```yaml
integration: Figma MCP use_figma + get_screenshot
integration_version: UNKNOWN
target_file: AI-Design-System
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
scope: page rename and post-write readback of existing Button component set
read_pages_and_components: READY
rename_existing_page: READY
readback_component_properties_bindings_and_reactions: READY
create_new_page: UNKNOWN
write_component_internals: UNKNOWN
verified_on: 2026-09-23
```

Se renombró la página existente `0:1` a `Buttons` sin cambiar el set `26:81`. El readback posterior confirmó 60 variantes, 120 instancias Phosphor y 35 variables vinculadas resueltas. Una captura actual de 516×1883 se inspeccionó mediante el MCP; la URL efímera no se conserva como evidencia persistente. Véanse [implementación](implementations.md) y [QA](../qa/implementations/button.figma.review.md). Esto no prueba capacidad de crear páginas nuevas ni editar internamente componentes.

## Figma · metadatos de componente Button

```yaml
integration: Figma MCP use_figma
integration_version: UNKNOWN
target_file: AI-Design-System
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
scope: component-set metadata update on existing node 26:81
write_description: READY
write_descriptionMarkdown: READY
readback_description: READY
team_library_publish_capability: UNKNOWN
verified_on: 2026-09-23
```

Se escribieron y leyeron de vuelta los campos `description` y `descriptionMarkdown` del set local `26:81`. La lectura final confirmó el contenido aprobado; `documentationLinks` siguió vacío. El set informó `getPublishStatusAsync() = UNPUBLISHED`: capacidad de guardar metadatos en el archivo verificada, publicación de biblioteca de equipo no ejecutada ni afirmada.

## Figma · inspección fuente de Filter Chip

```yaml
integration: Figma MCP get_metadata + get_screenshot + use_figma
integration_version: UNKNOWN
source_file_key: 9zs5RMR8LB5wHjW9Bd59BA
source_node: "8203:10"
scope: read-only source inspection
read_nodes_and_descendants: READY
read_component_properties: READY
read_bound_variables_and_resolve_values: READY
read_named_styles: READY
write_source: NOT_AUTHORIZED
verified_on: 2026-09-23
```

La lectura recorrió 145 nodos sin pendientes, resolvió 26 variables y una dependencia remota activa. No se ejecutaron escrituras. El grafo existente se consultó únicamente como índice y no se regeneró; queda `STALE` respecto de `FILTER-CHIP-001` y sus registros nuevos.

## Figma · preflight del destino Chips

```yaml
integration: Figma MCP use_figma + get_metadata + get_libraries + search_design_system
integration_version: UNKNOWN
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
scope: read-only destination discovery for Filter Chip
pages_and_component_sets: READY
local_variables_and_modes: READY
read_dependency_key: READY
create_page_and_components: UNKNOWN_NOT_EXECUTED
write_in_this_task: NOT_EXECUTED
verified_on: 2026-09-23
```

El destino contenía solo `Buttons` (`0:1`) y el set `button` (`26:81`). Las colecciones locales `semantic` (`VariableCollectionId:6:2`, 129 variables) y `primitive` (`VariableCollectionId:6:3`, 141 variables) continúan. Se localizaron los 26 tokens del componente fuente, `font/family/base`, `font/weight/medium` y PlusCircle con key coincidente con Phosphor. La búsqueda de Filter Chip identificó el set de la biblioteca fuente; no hay un set local en el destino. No se escribieron páginas ni nodos.

## Figma · construcción y lectura posterior de Chips

```yaml
integration: Figma MCP use_figma + get_screenshot
integration_version: UNKNOWN
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
scope: create page, component set and variants; bind properties and local variables; inspect screenshot and readback
create_page_and_components: READY
write_component_properties_and_bindings: READY
readback_component_properties_and_bindings: READY
team_library_publish_capability: UNKNOWN_NOT_EXECUTED
verified_on: 2026-09-23
```

Se creó y leyó de vuelta la página `Chips` (`67:122`) y el set `Filter Chip` (`72:298`) con 30 variantes. La comprobación final resolvió los 28 tokens usados en cuatro modos, verificó 126 paints, ocho propiedades y 60 instancias Phosphor. La captura final se conserva en [la implementación](../implementations/figma/filter-chip.v0.2.0.png) y el resultado en [QA-FILTER-CHIP-FIGMA-001](../qa/implementations/filter-chip.v0.2.0.figma.review.md). Esta verificación actualiza la capacidad observada, sin alterar el preflight histórico anterior.

## Índice Graphify · actualización de protocolo 0.2.1

El grafo `graphify-out/` se consultó como índice antes de actualizar las reglas de páginas semánticas y mapeo de variables desde el JSON aprobado. Sus referencias todavía señalan rutas de protocolos anteriores; queda `STALE` frente a esta edición documental. No se regeneró el grafo porque esta solicitud autoriza actualizar el protocolo, no reconstruir el índice derivado.

## Graphify · lote Chat Toolbar2026-10-08

Entorno READY: Graphify0.9.65 instalado con uv; intérprete /Users/miguel.leo/.local/share/uv/tools/graphifyy/bin/python. Sin instalaciones ni servicios nuevos. Sincronización autorizada por P05§8 y DEC-GRAPH-CONTINUOUS-SYNC-001; alcance corpus completo, extracción AST y semántica incremental por hashes, preservando fuentes históricas y respaldo del corte anterior. Grafo STALE durante el delta; CURRENT solo con verification.json y manifest-check.json PASS en graphify-out/runs/2026-10-08-chat-toolbar/ y hashes finales concordantes. Outputs graph.json/graph.html/GRAPH_REPORT.md; cierre legible en [handoff](./SESSION-HANDOFF-2026-10-08-CHAT-TOOLBAR.md). Coste medido no expuesto por agentes; no declarar cero. HTML agrega comunidades si supera5000 nodos; relaciones fuente históricas rotas se reportan sin convertirlas en tareas de diseño.

## Fuentes · cierre de lote 2026-10-09

Figma corporativo leído/escrito en destino AI DS, fuente Navi solo lectura. [Estado](../implementations/figma/fuentes.v0.1.0.state.json), [QA](../qa/implementations/fuentes.v0.1.0.review.md). Capacidades de Slots, reflow y variables verificadas. Sin instalaciones, servicios externos, credenciales nuevas ni publicación remota. Grafo requiere cierre incremental estructural y semántico de este lote; su resultado real queda en [closure.json](../graphify-out/runs/2026-10-09-fuentes/closure.json), sin inferir CURRENT antes de verificar.
