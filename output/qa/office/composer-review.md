# Revisión independiente · compositor conectado

Fecha: 2026-10-16. Revisora: **Vera**, `/root/review_governance`, distinta de Eva y Bruno, autores del cambio. Alcance: compositor en el servidor local, actor `user`, aceptación/idempotencia, estado de trabajo, aislamiento HTTP, persistencia y runner. No sustituye `independent-review.md`, que conserva la revisión histórica del chat sin envío.

**Resultado: PASS técnico del alcance independiente, con los límites indicados abajo.** La suite integrada pasó **42 tests, exit 0, sin skips**, en 34.835 s. Un smoke real posterior de Eva encontró una incompatibilidad de argumentos de Codex que el ejecutable falso no detectaba. Bruno corrigió ese argumento y reportó PASS del único caso afectado; Vera contrastó la llamada final con la ayuda real guardada. Se reutiliza la evidencia de áreas sin cambios y se conserva el PASS de 42 como histórico del corte anterior. No se declara cerrado el envío con modelo real por las pruebas simuladas; el nuevo smoke de Eva es evidencia separada.

`user_audit: NOT_REQUIRED`; `human_review_policy: OPTIONAL_NON_BLOCKING`. Tiempo/tokens del modelo y ahorro: **UNAVAILABLE**. No se inició ningún modelo real desde esta revisión.

## Evidencia y alcance ejecutado

Se consultó primero Graphify (`graphify query "Evolution Lab compositor servidor mensajes request_id seguridad" --budget 700`); el subgrafo fue poco específico y se confirmaron los hallazgos en las fuentes. Se leyeron `scripts/evolution_office.py`, `scripts/evolution_office_server.py`, `office/dashboard.html`, configuración, README/protocolo de oficina y pruebas. El protocolo 0.1.3 distingue ejecución CLI nueva de continuidad automática de conversación.

La suite se ejecutó con Python stdlib y el Node ya disponible; no hubo instalaciones. HTTP usa puerto loopback efímero, raíz temporal y CLI falso. La prueba integrada obtuvo permiso de ejecución para el puerto de pruebas; no cambió los permisos del runner de producción. Las pruebas independientes sin socket interceptan fallos de disco con mocks; las UI ejecutan el JS real con `window`, DOM, temporizadores y fetch simulados, incluyendo `initComposer`.

- `composer-tests.txt`: salida completa de la suite integrada de 42 pruebas.
- `composer-reviewed-hashes.json`: hashes de implementación/tests antes y después de esa pasada, estables en ese intervalo. Identifican el corte anterior a corregir argv.
- `tests/office/test_composer.py`: seis pruebas nuevas de comportamiento UI.
- `tests/office/test_server_review.py`: cuatro regresiones independientes de aislamiento y persistencia.
- `tests/office/test_server.py`: ocho pruebas de Bruno, ejecutadas también por Vera.
- `tests/office/test_office.py`: 24 regresiones de ledger/chat ejecutadas de nuevo en el corte con compositor; no se reutilizó su PASS histórico como si fuera actual.
- `codex-exec-help.txt`, líneas 58–59: la ayuda del CLI instalado declara que `--approve-for-me` usa revisión automática y sandbox `workspace-write`. La llamada actual contiene ese flag y no contiene bypass de aprobaciones/sandbox.

Tras la pasada integrada, Bruno amplió solo la tolerancia de la fixture de servidor (15→60 s del ejecutable falso, 30→65 s de observación) por latencia observada en su entorno. El PASS de Vera ocurrió con los límites anteriores, más estrictos; no se afirma haber ejecutado otra suite global con la fixture posterior. La corrección funcional posterior se limita a eliminar el flag `--sandbox workspace-write` redundante/incompatible de argv y actualizar la aserción. Bruno reportó el caso `test_success_records_request_response_and_safe_arguments`: **1 test PASS, 0.512 s**. Vera no repitió ese test por instrucción de Eva y distingue ese resultado delegado de sus 42 pruebas ejecutadas directamente.

## Resultados por comportamiento

| Comprobación | Evidencia observada | Estado |
|---|---|---|
| Envío UI | Ctrl+Enter dispara exactamente un POST con token; estado aceptado limpia el texto y bloquea otro envío. | PASS simulado |
| Confirmación perdida | La red falla después de aceptar; texto e identificador se conservan. Segundo clic usa el mismo cuerpo y se obtiene un solo trabajo. No aparecen mensajes ficticios antes del registro. | PASS simulado |
| Trabajo ocupado/final | Sesión con trabajo activo impide POST; completed/failed desbloquea y muestra resultado/error; 409 conserva texto y consulta estado sin reenviar. | PASS simulado |
| Token renovado | 403 conserva texto/request_id, recupera sesión y permite reintento explícito sin envío automático. | PASS simulado |
| Actor usuario | `user` aparece como “Tú”, respuesta cita solicitud y payload HTML permanece texto inerte. | PASS simulado |
| Origen y autorización | Host ajeno, Origin ajeno, token ausente y Sec-Fetch-Site cross-site devuelven 403; consultar trabajo exige token. | PASS HTTP local |
| Rutas y límites | Rechaza rutas fuera de lista, traversal, archivos/symlinks, cuerpo/shape/ID inválidos y mensaje mayor al límite. Logs privados no se sirven ni se incluyen en el error público. | PASS HTTP local |
| Idempotencia servidor | Mismo ID/texto recupera el trabajo; ID con otro texto y otro trabajo durante busy devuelven 409. Reinicio ordenado conserva idempotencia. | PASS CLI falso |
| Respuesta y fallo | Request user→Eva DISPATCHED y respuesta correlacionada Eva→user RECORDED; salida de fallo produce FAIL. Timeout detiene proceso. No se convierte una respuesta en QA PASS. | PASS CLI falso |
| Evidencia HTML | Solo el dashboard se sirve como HTML activo; evidencia HTML se sirve como texto con nosniff, sin acceso ejecutable al origen de órdenes. | PASS handler aislado |
| Fallos de almacenamiento | Fallo inicial libera worker y admite reintento mismo ID; fallo después de spawn termina proceso/libera worker; fallo al persistir resultado libera worker y reporta failed. | PASS inyección de fallos |
| Contrato argv final | Ayuda CLI real confirma workspace-write + revisión automática con `--approve-for-me`; fuente usa solo ese flag; test específico de Bruno PASS. | PASS por inspección + prueba delegada |
| Modelo real | Primer smoke de Eva rechazó la combinación previa; el nuevo smoke corresponde a Eva y no se infiere de la suite simulada. | Fuera de esta revisión |

## Defectos detectados y tratamiento

1. **COMPOSER-REV-001 · HTML de evidencia en origen de ejecución.** Detectado por inspección: una evidencia HTML podía ejecutar script junto a `/api/session` y usar el token para enviar órdenes. Bruno cambió el MIME de evidencias HTML a texto; prueba independiente pasa. No se ejecutó un exploit contra el servidor real.
2. **COMPOSER-REV-002 · fallos de persistencia dejaban worker ocupado.** Las escrituras iniciales/finales y la rama de fallo de arranque podían lanzar antes de liberar `active`; la carpeta de una aceptación fallida también impedía repetir ID. Bruno corrigió limpieza y recuperación de carpeta. Las cuatro ramas relevantes pasan con fallos OSError controlados.
3. **COMPOSER-REV-003 · token caducado sin recuperación.** La UI indicaba reintentar pero conservaba el token rechazado. Eva agregó recuperación de sesión ante 401/403 sin envío automático; la prueba conserva texto/ID y demuestra un único trabajo.
4. **COMPOSER-CLI-001 · combinación de flags incompatible, corregida.** Hallazgo del smoke real de Eva, no de Vera: `--sandbox workspace-write` junto con `--approve-for-me` fue rechazado por el CLI instalado. La suite falsa validaba una lista de argumentos inválida para ese ejecutable, mostrando su límite. Bruno eliminó el flag redundante y actualizó la aserción; reportó PASS del caso específico. Vera confirmó contra ayuda guardada que no se eliminan sandbox ni revisión automática. La comprobación integral real posterior pertenece al smoke de Eva.

## Coordinación y límites

Vera consultó directamente a Bruno endpoints y estados; comunicó el riesgo de HTML y fallos de persistencia, después los bordes de retry de carpeta y cleanup tras spawn. Bruno confirmó correcciones y Vera devolvió resultados ejecutados. Eva recibió copia resumida de cada intercambio y corrigió token/UI. Vera consultó a Atlas sobre documentación de ejecución nueva, estados RECORDED/FAIL y ausencia de actividad ficticia. Estas referencias describen mensajes reales de colaboración; Vera no agregó conversaciones al ledger real.

La garantía de un trabajo activo se verificó con servidor vivo y cierre ordenado. **Una caída abrupta/SIGKILL puede dejar un runner huérfano**: el proceso separado podría seguir activo mientras un servidor nuevo marca el trabajo previo fallido. No se probó ni implementó supervisor de vida del proceso; límite comunicado a Bruno y Eva para documentación explícita. No se infiere seguridad de reinicio abrupto a partir del test de reinicio ordenado.

No se comprobó equivalencia de herramientas/MCP entre CLI y aplicación, autenticación real, ejecución del modelo, layout/accesibilidad integral ni aislamiento frente a un proceso local ya autorizado a escribir código/configuración. Esas capacidades no se deducen de un nonce HTTP. La UI no transmite tokens ni razonamiento privado; muestra el registro y estado del trabajo. Fallos de disco pueden impedir persistir toda evidencia y exigen recuperación; no se promete durabilidad cuando el almacenamiento falla.

Vera solo editó pruebas y este reporte/evidencia propios, sin publicar, editar implementación ni mutar el ledger de uso real. El smoke visual/real corresponde a Eva y se mantiene como evidencia separada. Los informes históricos conservan su corte.
