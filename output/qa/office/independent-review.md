# QA independiente · oficina Evolution Lab

Fecha: 2026-10-16. Perfil: **Vera**, verificadora. Ejecución revisora: `/root/review_governance`, distinta de la autora de la implementación. Elegí y confirmé el nombre Vera al recibir el encargo; Atlas incorporó esa elección a `office/README.md`. El nombre identifica un rol de IA, no una persona ni un proceso permanentemente activo.

Resultado del corte final: **PASS**, 24 pruebas, exit 0, sin skips. No quedan defectos abiertos de esta revisión. `user_audit: NOT_REQUIRED`; `human_review_policy: OPTIONAL_NON_BLOCKING`. Costes/tokens: **UNAVAILABLE**, sin ahorro cuantificado ni mediciones inventadas.

## Alcance, fuentes y aislamiento

Se inspeccionaron `scripts/evolution_office.py`, `office/config.json`, `office/dashboard.html`, `office/README.md` y `office/OPERATING-PROTOCOL.md`. Los hashes del corte revisado están en `reviewed-hashes.json`. Se consultó primero Graphify con `graphify query "Evolution Lab oficina virtual evolution_office ledger dashboard" --budget 700`; el grafo previo no contenía aún el módulo completo y se confirmaron las reglas en las fuentes.

Solo se crearon/modificaron `tests/office/test_office.py`, los artefactos QA de esta carpeta y la revisión propia `office/reviews/vera.md`. La revisora no editó implementación, configuración, plantilla, documentos de Atlas, ledger real ni dashboard real. Las escrituras de las pruebas usan `TemporaryDirectory`, una raíz independiente y copias de configuración/plantilla/script. Las pruebas CLI también corren una copia del script bajo esa raíz temporal.

## Pruebas ejecutadas

Comando: `python3 -m unittest discover -s tests/office -v`, con el Node empaquetado existente disponible en PATH para las pruebas JS aisladas. Resultado final: **24 tests, OK, exit 0, sin skips**, 1.070 s observados por unittest. La suite inicial de 20 casos pasó para la vista snapshot; la ampliación a chat HTTP añadió controles de estado, desconexión y concurrencia. La salida final se conserva en `tests.txt`. Se compararon hashes de implementación, configuración, plantilla y suite antes/después de ejecutar: sin cambios durante la pasada. No se instaló ninguna dependencia.

| Área | Comprobación | Resultado |
|---|---|---|
| Append e integridad | Conserva los bytes de eventos anteriores, encadena previous/sha256 y rechaza mutaciones históricas no reencadenadas. | PASS |
| Concurrencia | 12 escrituras concurrentes con cuatro workers: 12 IDs únicos, sin eventos perdidos y cadena válida. | PASS |
| Duplicados | Rechaza ID repetido sin cambiar ledger y segunda respuesta al mismo encargo. | PASS |
| Correlación | Una respuesta referencia solicitud existente, invierte emisor/receptor y conserva objetivo. Rechaza interlocutor u objetivo equivocados y solicitud inexistente. | PASS |
| Estados | Solicitud requiere DISPATCHED; solo response admite reply_to. PASS/COMPLETED requiere evidencia también en decisiones y notas. | PASS |
| Evidencia | Acepta archivo local existente; rechaza inexistente, directorio, ruta absoluta, traversal y symlink hacia fuera de raíz. | PASS |
| Respuesta completada | Response COMPLETED con reply_to válido y `qa/proof.md` existente se registra y valida. | PASS |
| CLI | Copia temporal ejecuta record --file para request y response COMPLETED, luego check y render, exit 0. | PASS |
| Escape embebido | Payload con cierre de script, nuevo script, img/onerror y ampersand permanece JSON inerte; no agrega tags ni script ejecutable. | PASS |
| Render DOM local | Ejecuta el JS del dashboard con DOM aislado en Node: datos se representan con textContent; el test falla si se usa innerHTML, se inyecta código, hay red o polling en modo file. | PASS |
| Comunicación honesta | La UI identifica perfiles bajo demanda, intercambios resumidos y registrados, modo archivo local y estado de conexión. No muestra tokens estimados ni presencia de agentes. | PASS |
| Chat HTTP | Red simulada: incorpora revisión nueva y respuesta con solicitud citada; payload remoto queda como texto; no reconstruye con revisión idéntica; error HTTP/desconexión preservan último corte; pestaña oculta no consulta; reconexión recupera etiqueta. | PASS |
| Estado publicado | HTML y state.json contienen el mismo objeto; revisión cambia con eventos/configuración y permanece estable al regenerar sin cambios. | PASS |
| Fallo previo al append | Plantilla ausente o sin placeholder válido no agrega evento ni oculta un guardado exitoso bajo error. | PASS |
| Fallo de panel después del append | OSError simulado al escribir solo el panel devuelve el ID persistido y aviso de no repetir record; render posterior recupera la vista con un solo evento. | PASS |
| Fallo de state.json después del append | Devuelve ID y aviso; conserva ledger y HTML nuevos, state anterior; render recupera ambos sin repetir record. | PASS |
| Render concurrente con record | Intercala regeneración de corte previo y append nuevo; el estado final conserva todos los eventos del ledger. | PASS |

La prueba `OfficeTests.test_completed_response_with_local_evidence_is_valid` es el caso positivo de cierre solicitado. Crea una solicitud Eva→Vera; responde Vera→Eva con el mismo objetivo, `reply_to` igual al ID real de la solicitud, `status: COMPLETED` y `evidence: ["qa/proof.md"]`; ese archivo se crea dentro de la raíz temporal. La validación devuelve esa solicitud como respondida. Se puede ejecutar aisladamente con `python3 tests/office/test_office.py OfficeTests.test_completed_response_with_local_evidence_is_valid -v`.

## Defectos identificados y correcciones revalidadas

- **OFFICE-REV-001 · evidencia de decisiones, resuelto.** La inspección inicial mostró que el gate de evidencia PASS/COMPLETED estaba dentro de la rama response. Permitía por estructura decisiones de cierre sin evidencia. Se consultó directamente a Atlas, quien confirmó el criterio general. Eva movió el control a todas las clases; tests de notas/decisiones sin evidencia y response válida/fallida pasan.
- **OFFICE-REV-002 · guardado con error ambiguo, resuelto.** Se reprodujo en temporal que una plantilla ausente causaba FileNotFoundError después de persistir un evento; el llamador no recibía el ID y podía repetir el registro. Eva prepara y valida el HTML antes de persistir. Si falla únicamente la escritura final del panel, conserva el evento y devuelve el ID con aviso de ejecutar render y no repetir record. Se comprobaron ambos caminos y recuperación.
- **OFFICE-DOC-001 · evidencia externa, resuelto.** El protocolo inicialmente permitía “evidencia externa verificable”, mientras el CLI solo acepta archivos locales existentes. Atlas corrigió README y protocolo: evidence es local bajo raíz; tool_ref es una referencia declarada que el CLI no consulta. La existencia del archivo no acredita su contenido.
- **OFFICE-REV-003 · render pisa mensajes nuevos, resuelto.** En temporal se intercaló record antes de la escritura de un render que había leído un corte antiguo. Observado: ledger contenía `[before, newer]`, state solo `[before]`; el chat podía retroceder indefinidamente hasta otro registro/render. Eva añadió el mismo lock exclusivo a render alrededor de load y ambas escrituras. La regresión reproduce el orden concurrente con dos workers y comprueba que HTML/estado final coinciden con el ledger; pasó aislada y en la suite final.

## Comunicación directa Vera–Atlas

Estos identificadores son etiquetas locales de este informe, no IDs de la herramienta ni eventos agregados al ledger por la revisora. Los intercambios ocurrieron mediante las herramientas de colaboración; Eva recibió copia resumida de cada etapa para integrarla al registro real.

| Referencia local | Emisor → receptor | Motivo y solicitud | Resultado observado |
|---|---|---|---|
| COMM-01 | Vera → Atlas, send_message | Alinear §6 con evidence local/tool_ref declarada; confirmar elección del nombre Vera. Mensaje inicial: “Atlas, soy Vera”. | Despacho confirmado; quedó pendiente mientras Atlas estaba completed. |
| COMM-02 | Vera → Atlas, send_message | Confirmar evidencia para todo PASS/COMPLETED, incluidas decisiones; mantener RECORDED informativo. Mensaje inicial: “Atlas, segunda consulta”. | Despacho confirmado; solicitud de criterio documental. |
| COMM-03 | Vera → Atlas, followup_task | Retomar las dos consultas pendientes y corregir solo sus documentos. Mensaje inicial: “Atlas, necesito tu cierre”. | Atlas reactivado; respondió que coincidía con el gate general y actualizaría los textos. |
| COMM-04 | Atlas → Vera, send_message | Comunicar correcciones aplicadas. Mensaje inicial: “Vera, cambios aplicados”. | README:15 registra nombre; README:66 y protocolo:62,70 alinean evidencia y estados. Lectura directa final confirmó los cambios. |
| COMM-05 | Vera → Atlas, send_message | Acusar recibo e informar revalidación. Mensaje inicial: “Gracias, Atlas”. | Despacho confirmado; sin decisiones documentales nuevas pendientes. |
| COMM-06 | Atlas → Vera, send_message | Solicita contraste de continuidad del protocolo 0.1.1 y sus cinco datos en note/RECORDED. | Lectura de documentos y esquema. |
| COMM-07 | Vera → Atlas, send_message | Devuelve PASS documental: continuidad usa campos de texto, no reply_to de response ni nuevo estado. | Copia a Eva; ejemplos no ejecutados, ahorro UNAVAILABLE. |
| COMM-08 | Vera → Atlas, send_message | Solicita alinear nuevo chat HTTP/state.json y modo file, sin afirmar tokenstream o agentes permanentes. | README y protocolo 0.1.2 incluyen ambos modos y límites; lectura directa confirmada. |
| COMM-09 | Vera → Atlas, send_message | Devuelve PASS documental de README/protocolo 0.1.2 y comunica 24 pruebas PASS/corrección de carrera concurrente. | Despacho confirmado; copia resumida a Eva. |

No se infiere actividad en vivo a partir del historial ni de un perfil con runtime asignado. La conversación resumida acredita intercambios observados en esta sesión; la escritura del ledger corresponde al operador y no ocurre por abrir el HTML.

## Límites y cierre

El dashboard no inicia agentes, no envía encargos, no sondea conversaciones de Codex ni estima tokens. En HTTP consulta state.json cada 3 s mientras está visible y muestra mensajes que el operador ya registró; no es un tokenstream ni confirma presencia permanente. En file muestra el corte embebido. El validador comprueba coherencia, archivos existentes y encadenamiento; no autentica que una herramienta haya enviado el mensaje, no comprueba contenido semántico de evidencias y no impide que alguien con acceso de escritura reescriba toda la cadena y recalcule hashes. No se presenta como firma criptográfica ni prueba de presencia.

Las pruebas JS usan un DOM aislado y fetch simulado: comprueban flujo y escape, no layout, accesibilidad integral, servidor HTTP real ni duración real de red. La evidencia UI del coordinador es separada y no se atribuye a esta revisión. HTML y JSON se sustituyen individualmente; ante fallo entre escrituras puede haber cortes distintos hasta recuperar con render, con aviso explícito al operador. No se probaron otros sistemas operativos; el mecanismo de lock actual utiliza fcntl del entorno local.

## Revisión de directrices propias

`office/reviews/vera.md` contiene tres propuestas concretas: seleccionar/reutilizar QA según impacto con hashes y entorno; preservar el ciclo defecto–corrección–revalidación; cerrar por evidencia técnica sin gates humanos rutinarios. Las propuestas se distinguen de la implementación revalidada y no cambian configuración ni protocolos. Incluyen criterios de comprobación; ahorro de tiempo/tokens sigue UNAVAILABLE.

No se hicieron push, instalaciones, publicaciones, Figma ni mutaciones del ledger real. El cierre de la oficina completa requiere que el coordinador registre los intercambios reales y los defectos/correcciones, regenere el snapshot y complete P05 sobre el lote. Este informe no afirma que Graphify o la publicación remota se hayan actualizado.
