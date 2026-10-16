# Oficina virtual de Evolution Lab

La oficina reúne cinco perfiles de IA con nombres estables, directivas consultables y un registro de intercambios reales. Codex ejecuta y coordina el trabajo; el panel muestra los registros guardados. Cada solicitud permite consultar quién la envió, a quién, qué necesita, por qué, con qué alcance y qué respuesta obtuvo.

## Consulta por necesidad

| Necesidad | Entrada mínima y fuente de detalle |
|---|---|
| Retomar una misión | Última nota de continuidad y sus solicitudes relacionadas en [events.jsonl](events.jsonl); formato en [continuidad](OPERATING-PROTOCOL.md#6-registro-panel-y-continuidad). |
| Saber quién hace qué | Perfil concreto de [config.json](config.json); [identidad de ejecución](OPERATING-PROTOCOL.md#2-perfiles-e-identidad-de-ejecución). |
| Registrar un intercambio | [Uso local](#uso-local) y [conversaciones verificables](OPERATING-PROTOCOL.md#3-conversaciones-verificables). |
| Evaluar una mejora | [Preflight](OPERATING-PROTOCOL.md#1-misión-y-preflight-obligatorio), [optimización](OPERATING-PROTOCOL.md#4-directiva-común-de-optimización) y evidencia de la misión. |

Esta tabla orienta la lectura; no omite los protocolos y dependencias que la tarea haga obligatorios. La primera sesión lee el protocolo completo. En una reanudación se comprueban su versión y cambios antes de reutilizar lo leído.

## Equipo

| Nombre | Perfil | Responsabilidad |
|---|---|---|
| Eva | Orquestadora | Delimitar la misión, realizar el preflight de tokens, coordinar y cerrar con evidencia. |
| Atlas | Documentalista | Conservar fuentes, contratos, decisiones y documentación fácil de consultar. |
| Bruno | Constructor | Implementar lo solicitado en el destino autorizado y documentar el resultado real. |
| Vera | Verificadora | Comprobar los criterios de aceptación, las regresiones y los límites de la evidencia. |
| Iris | Optimizadora | Buscar y contrastar mejoras de los objetivos primarios sin ampliar el alcance por iniciativa propia. |

Los nombres identifican responsabilidades. No implican personas, conciencia ni procesos activos permanentemente. Atlas eligió su nombre al recibir el encargo documental y Vera confirmó el suyo durante la revisión de esta oficina; los demás nombres son la propuesta inicial del equipo. La configuración conserva la identidad operativa y el registro identifica el agente concreto cuando exista una ejecución real. Cinco perfiles no obligan a ejecutar cinco modelos en cada tarea. Esta tabla es un resumen: las directivas de cada perfil se mantienen en `config.json`; el procedimiento común se mantiene en el protocolo, sin definir aquí reglas alternativas.

## Tres objetivos primarios

1. Facilitar mantenimiento y consulta: una fuente canónica, documentación localizable y consumo versionado desde GitHub sin reinstalar una skill por cada cambio de specs.
2. Completar el trabajo solicitado del Design System mediante los protocolos aplicables: fuentes, specs, contratos, QA, documentación y construcción Figma o web cuando ese destino esté autorizado.
3. Ahorrar tokens antes de construir y durante la ejecución: reutilizar evidencia vigente, consultar solo lo necesario y comparar el coste de delegar con el beneficio esperado.

Todos los perfiles buscan oportunidades de mejora mientras trabajan en una misión autorizada. Registran una hipótesis y una referencia comprobable; implementan solo lo que cabe en ese alcance. Las propuestas adicionales permanecen como propuestas, sin iniciar monitores ni trabajo en segundo plano.

## Archivos de la oficina

| Archivo | Función |
|---|---|
| [OPERATING-PROTOCOL.md](OPERATING-PROTOCOL.md) | Reglas de coordinación, comunicación, optimización y cierre. |
| [config.json](config.json) | Perfiles, nombres y directivas que consume el panel. |
| [events.jsonl](events.jsonl) | Historial de eventos registrados, solicitudes y respuestas correlacionadas. |
| [dist/index.html](dist/index.html) | Chat con perfiles, mensajes, citas de respuesta y detalles de cada intercambio. |
| [dist/state.json](dist/state.json) | Estado derivado que el chat consulta cuando se abre por HTTP. |
| [evolution_office.py](../scripts/evolution_office.py) | Validación, registro y generación del panel. |
| [evolution_office_server.py](../scripts/evolution_office_server.py) | Servidor local del chat y envío de solicitudes a Codex CLI. |

El chat muestra intercambios reales registrados y permite enviar una solicitud mediante el servidor local. El servidor inicia una ejecución nueva de Codex CLI por mensaje, muestra sus avances públicos durante la ejecución y registra su respuesta final; los intercambios entre especialistas solo aparecen si realmente se despacharon y registraron. `record` actualiza los archivos de la vista al guardar; `render` permite regenerarlos explícitamente. Abierto por HTTP, el chat consulta `state.json` cada tres segundos mientras está visible y muestra si pierde la conexión. Abierto directamente como archivo, permite consultar el corte incluido sin enviar solicitudes. No es una transmisión de tokens ni del razonamiento privado de los agentes.

## Uso local

Desde la raíz del repositorio:

```sh
python3 scripts/evolution_office.py check
python3 scripts/evolution_office.py record --file evento.json
python3 scripts/evolution_office.py render
```

Para abrir el chat con campo de envío, inicia el servidor desde la raíz:

```sh
python3 scripts/evolution_office_server.py
```

Abre [la oficina local](http://127.0.0.1:8766/office/dist/index.html). El servidor necesita permanecer abierto durante el trabajo y utiliza `codex` disponible en PATH; `--codex` permite indicar otra ruta. Requiere que Codex CLI tenga su propia autenticación guardada. Su conexión, herramientas y servidores MCP pueden diferir de los disponibles en la aplicación Codex.

Cada envío abre una ejecución nueva: consulta los registros del repositorio, pero no continúa automáticamente el hilo de la aplicación ni una ejecución CLI anterior. El servidor acepta un trabajo a la vez; si está ocupado, informa el conflicto sin iniciar otro. Repetir el mismo identificador de solicitud con el mismo contenido recupera su trabajo, no crea uno nuevo. El actor `user` identifica al usuario en el historial y no agrega un sexto perfil de IA.

El servidor escucha solo en `127.0.0.1` y valida el origen y un token local al enviar. Los datos de ejecución se guardan bajo `output/office-runtime/`: solicitud/estado, resultado y logs. Los logs no se ofrecen por HTTP; el resultado puede consultarse como evidencia local. Esta carpeta queda fuera de Git mediante la regla de exclusión del proyecto. La solicitud y la respuesta también se reflejan en el historial del chat, por lo que ese historial debe revisarse antes de cualquier publicación. El servidor no hace commits ni pushes por sí mismo; publicar secretos o prompts privados no forma parte del flujo automático.

Una ejecución que termina produce una respuesta `RECORDED`; eso acredita que se guardó una respuesta, no que pasó QA ni que el objetivo esté validado. Un fallo se informa como tal. Esta documentación describe el contrato observado del servidor; los resultados de sus pruebas se registran por separado.

`record` recibe un evento JSON acorde con el esquema que valida el CLI y lo agrega al historial. No envía mensajes ni ejecuta modelos. Registra una solicitud solo después de que la herramienta confirme su envío real. Una respuesta usa `reply_to` para vincularse al ID de la solicitud, invierte emisor y receptor y enlaza evidencia existente. El CLI agrega ID, fecha y los campos de encadenamiento del registro.

Esta plantilla ilustra el formato; **no es una solicitud ejecutada ni debe agregarse al historial sin un envío real**:

```json
{
  "kind": "request",
  "from": "eva",
  "to": "atlas",
  "message": "Atlas, documenta las reglas de comunicación de esta misión.",
  "why": "La solicitud del usuario exige poder consultar quién pide qué y por qué.",
  "scope": "Documentación de la oficina dentro de la misión autorizada.",
  "deliverable": "Protocolo con solicitudes, respuestas y referencias de evidencia.",
  "objective": "maintenance",
  "status": "DISPATCHED",
  "evidence": ["office/OPERATING-PROTOCOL.md"]
}
```

Los identificadores de perfil son `eva`, `atlas`, `bruno`, `vera` e `iris`. Los objetivos se identifican como `maintenance`, `construction` y `efficiency`. `evidence` utiliza rutas relativas de archivos locales existentes dentro de la raíz del proyecto. `tool_ref` conserva una referencia declarada de herramienta; el CLI no comprueba el contenido externo de esa referencia. Todo evento `PASS` o `COMPLETED`, incluida una decisión, requiere evidencia local; una nota o decisión informativa puede usar `RECORDED`, y una prueba sin ejecutar usa `NOT_RUN`. Consulta la ayuda del CLI para el esquema y sus opciones vigentes.

Tras `record`, `render` o un registro del servidor, el chat servido por HTTP incorpora el estado generado en su siguiente consulta. Puedes abrir `office/dist/index.html` directamente para inspeccionar el corte sin servidor, sin envío. El CLI de bitácora sigue sin despachar modelos; el servidor local es el puente que ejecuta Codex CLI al enviar una solicitud.

## Continuar una misión en otra sesión

Parte de la última nota de continuidad registrada, su solicitud y sus respuestas; sigue sus referencias a las fuentes y resultados. Si aún no existe esa nota, reconstruye el estado desde los eventos, sin asumir pendientes resueltos. Lee el [protocolo de operación](OPERATING-PROTOCOL.md) en la primera sesión y comprueba cambios del protocolo y la configuración al reanudar. Eva asigna los perfiles necesarios a ejecuciones reales y registra esos vínculos; un nombre de perfil por sí solo no recupera memoria ni inicia un agente.

Una solicitud entre agentes debe quedar registrada junto con el resultado efectivo de su despacho. La respuesta conserva la correlación, el trabajo realizado, sus comprobaciones y sus límites. El panel no sustituye los contratos del DS ni sus registros canónicos.

## Autorización, fuentes y límites

El usuario solicitó una oficina virtual dentro de Codex con orquestador, especialistas nombrados, comunicación visible y búsqueda continua de mejoras centrada en los tres objetivos primarios. Autorizó el cierre técnico del trabajo solicitado sin esperar una revisión humana rutinaria. Esta oficina documenta esa solicitud y mantiene los permisos y límites del proyecto.

Fuentes consultadas: [P05](../protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md), [DEC-AI-TECHNICAL-CLOSURE-001](../registry/DEC-AI-TECHNICAL-CLOSURE-001.md) y el documento `EVOLUTION-LAB.md` de la copia pública preparada del repositorio. La sección posterior de ese documento declara implementado el consumo remoto y sustituye su descripción histórica de snapshots incluidos; esta oficina no convierte esa declaración en una prueba nueva de Genspark.

El estado técnico se acredita mediante las comprobaciones y eventos correspondientes. Este README describe el funcionamiento previsto del módulo, no certifica por sí solo su implementación ni una sesión activa. Los costes de tokens sin medición disponible se declaran `UNAVAILABLE`; una estimación debe etiquetarse como estimación.

### Cierre del servidor

Detén el servidor con Ctrl+C (SIGINT) o SIGTERM: cancela la ejecución activa y termina su grupo de procesos. Una terminación forzada con SIGKILL no permite esa limpieza; antes de reiniciar tras una caída forzada, comprueba y detén cualquier proceso Codex de la oficina que haya quedado activo. El estado `failed` recuperado no prueba que un proceso huérfano haya terminado.

### Avances durante la ejecución

El chat recibe los mensajes públicos antes del cierre, junto con actividad de herramientas resumida y última actualización. Si no llegan eventos durante treinta segundos, lo indica explícitamente. Recargar recupera el trabajo activo o el último y sus avances guardados. No se transmite razonamiento privado; las respuestas registradas de los especialistas aparecen con su identidad real. El estado de ejecución no equivale a QA aprobado.
