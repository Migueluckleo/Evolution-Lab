# QA independiente · avances públicos del chat

Fecha: 2026-10-16. Revisora: **Vera**, `/root/review_governance`. Autores: Bruno (lector JSONL/estado del servidor), Eva (UI). Alcance autorizado: mostrar avances públicos durante la ejecución y conservarlos al fallar o recargar, sin confundir proceso activo con progreso ni exponer razonamiento privado.

**Resultado: PASS técnico del alcance revisado.** La pasada dirigida ejecutó 18 pruebas; después de corregir el orden se ejecutaron 11 comprobaciones UI dependientes, todas PASS y sin skips. Son pasadas superpuestas, no 29 casos únicos. Evidencia previa del compositor permanece histórica en `composer-review.md`; no acredita por sí sola este nuevo lector ni la UI de avances. No se ejecutaron modelos, no se reinició ni interrumpió el servidor activo y no se modificó el ledger real desde esta revisión.

## Fuentes y pruebas

Graphify se consultó primero con `graphify query "evolution_office_server job updates streaming progreso" --budget 500`. Las relaciones derivadas se confirmaron leyendo `scripts/evolution_office_server.py`, `office/dashboard.html` y los tests. Inicialmente la revisión modificó pruebas y QA propios; Eva autorizó después a Vera a corregir exclusivamente el orden de filas en dashboard y regenerar la vista. El servidor de ejecución no fue modificado por Vera.

Se ampliaron `tests/office/test_composer.py` y `tests/office/test_server_review.py`. Se usa Python stdlib y Node existente, DOM/fetch simulados con `window` para activar el compositor real. Las pruebas de Bruno en `test_server_streaming.py` usan ejecutables falsos y servidores loopback efímeros en raíces temporales. No se conecta ningún modelo ni se usa el servidor de trabajo del usuario.

La pasada dirigida de Vera ejecutó **18 pruebas PASS, sin skips, exit 0, 5.110 s**: nueve de compositor, cinco independientes de privacidad/persistencia y cuatro de streaming. Salida en `streaming-tests.txt`; hashes estables antes/después en `streaming-reviewed-hashes.json`. Esa evidencia acredita lector/privacidad y la UI previa al ajuste de orden.

La pasada posterior ejecutó **11 pruebas UI PASS, sin skips, exit 0, 0.627 s**: los nueve casos del compositor, incluido orden/no duplicación final, más las regresiones de sincronización HTTP y escape del DOM. Salida en `streaming-ui-final-tests.txt`; corte verificado en `streaming-ui-final-hashes.json`. Se reutilizó la evidencia del servidor, que no cambió desde la pasada de 18. Después, `python3 scripts/evolution_office.py render` terminó exit 0 y generó la vista con 37 eventos ya existentes; no añadió eventos al ledger. Eva fue avisada para recargar la pestaña y ejecutar su smoke separado.

| Caso | Criterio |
|---|---|
| Avances antes del final | JSONL llega en fragmentos UTF-8; API y job.json contienen mensaje público mientras status sigue running y el proceso espera liberación del test. |
| Mensajes vs actividad | Herramientas producen etiquetas generales; no se muestra comando, argumentos, salida privada ni razonamiento como mensaje. Proceso sin evento muestra espera/silencio. |
| Privacidad explícita | analysis/reasoning en channel/phase, tanto de item como del evento, se excluyen; commentary público se conserva. |
| Delegación | Solo operaciones conocidas y receiver_thread_ids válidos conservan referencia; actor es Eva, sin inventar nombre a partir de prompt o resultados. |
| Actualización e idempotencia | El mismo item actualiza su mensaje, duplicado no agrega burbuja; la respuesta final incorporada al ledger no se duplica. |
| Desconexión y error | Se conservan mensajes observados, error visible, sin reenvío automático; fallo terminal libera compositor. |
| Recarga | session.last_job recupera avances persistidos de un trabajo terminado sin reenviar ni fingir actividad actual. |
| Timeout y lectura | Se drenan stdout/stderr, incluido Unicode fragmentado; timeout o fallo de wait conservan avances públicos y liberan worker; logs privados no cruzan API. |

La prueba propia inicial de privacidad falló por comparar un acento literal con JSON escapado (`ensure_ascii=True`); se corrigió la aserción a representación Unicode. No fue una fuga del servidor. La fixture previa de persistencia final pasó a simular `stream` en su frontera, conservando su objetivo de inyectar fallo de disco sin simular un descriptor de proceso real.

## Hallazgos y comunicación

- **STREAM-REV-001 · etiquetas privadas en el evento exterior, resuelto.** La primera implementación filtraba channel/phase privados en item, pero no en el evento que lo contiene. Vera comunicó el borde a Bruno; añadió el rechazo en ambos niveles. Es defensa ante una forma marcada explícitamente privada, no afirmación de que el CLI instalado haya emitido esa forma. El test pasa con ocho combinaciones y comprueba que el comentario público sí se conserva.
- **STREAM-REV-002 · orden tras el final, resuelto.** `feed()` representaba primero todos los eventos del ledger y luego `paintLive()` agregaba los avances del trabajo. Al llegar la respuesta final al ledger, avances anteriores quedaban después de ella. Eva autorizó expresamente a Vera a corregir únicamente este punto: filas de ambos orígenes llevan timestamp y la lista combinada se ordena al terminar el render. En igualdad de tiempo, la respuesta final va después del avance; el resto conserva orden estable. La aserción de orden y no duplicación pasa junto con las regresiones dependientes; se añadió dataset a los DOM de prueba afectados.

Vera consultó el esquema a Bruno, informó del filtro defensivo y de una importación de TestCase que duplicaba ocho tests descubiertos; Bruno corrigió el import de la fixture. Su prueba de timeout necesitó esperar un marcador de arranque del intérprete falso antes de iniciar el tiempo medido; el timeout de producción no se cambió. Eva recibió copia resumida de los intercambios. Estos hechos provienen de coordinación real; no se agregaron conversaciones ficticias al chat.

## Límites

El servidor reconoce un conjunto de eventos JSONL. Eventos desconocidos no se transforman en progreso. Un comentario público es texto emitido por la ejecución; su aparición no prueba QA, aprobación humana ni cumplimiento de la tarea. Un mensaje de delegación no atribuye actividad a un especialista sin evidencia real. Se conserva un máximo de 500 actualizaciones de hasta 24 000 caracteres y un contador de recorte; no se promete un transcript ilimitado.

El modelo puede permanecer en silencio: la UI informa tiempo desde la última actividad conocida, no fabrica un avance periódico. El polling y los tests de DOM no equivalen a revisión visual completa, streaming de tokens ni acceso a razonamiento privado. El comportamiento con modelo real y navegador del usuario corresponde a evidencia separada de Eva. Continúa vigente el límite de runner huérfano tras SIGKILL descrito en README; este cambio no incorpora supervisor de procesos.

`user_audit: NOT_REQUIRED`; `human_review_policy: OPTIONAL_NON_BLOCKING`. Costes, tokens y ahorro: **UNAVAILABLE**. El cierre depende de los controles técnicos del alcance, sin gate humano rutinario.
