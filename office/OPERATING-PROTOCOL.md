# Operación de la oficina Evolution Lab

Versión: 0.1.4. Alcance: coordinación de agentes para solicitudes del usuario sobre Evolution Lab y el Design System. Esta revisión incorpora avances públicos incrementales, recuperación del último trabajo y avisos de silencio; mantiene el envío mediante servidor local y una ejecución nueva de Codex CLI por mensaje; conserva la actualización HTTP de 0.1.2, consulta acotada y nota de continuidad de 0.1.1 y reglas de autorización, evidencia y QA de 0.1.0. Complementa [AGENTS.md](../AGENTS.md), [P05](../protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md) y [DEC-AI-TECHNICAL-CLOSURE-001](../registry/DEC-AI-TECHNICAL-CLOSURE-001.md). No amplía permisos ni sustituye contratos normativos del DS.

## 1. Misión y preflight obligatorio

Antes de construir, Eva registra el objetivo solicitado, alcance, entregable, destinos autorizados y criterio de aceptación. Realiza una revisión breve del coste antes de activar agentes:

- Localizar fuentes e índices existentes, comprobar vigencia y reutilizar evidencia por versión o hash cuando corresponda.
- Determinar el mínimo contexto y los archivos que requiere cada encargo; evitar copiar todo el repositorio o toda la conversación.
- Preferir una comprobación determinista cuando resuelve la necesidad. Delegar cuando exista trabajo independiente o revisión exigida y el beneficio justifique la coordinación.
- Establecer límites de iteración y una condición de parada apropiados para esa misión. No inventar un presupuesto aprobado; distinguir estimaciones y límites propuestos de límites indicados por el usuario.
- Registrar el coste medido cuando la herramienta lo exponga. Usar `UNAVAILABLE` si no existe medición, incluyendo coordinación y correcciones en las comparaciones cuando esos datos estén disponibles.

El preflight es ligero y se reutiliza mientras no cambie materialmente el alcance. No debe consumir más trabajo que el ahorro que pretende conseguir. La búsqueda necesaria para realizarlo no cuenta como construcción de una solución.

## 2. Perfiles e identidad de ejecución

Eva coordina, Atlas documenta, Bruno construye, Vera verifica e Iris optimiza. Los nombres canónicos y las directivas consumibles viven en `office/config.json`. Cada rol tiene una responsabilidad diferenciada y puede dirigirse a otro por su nombre.

Al asignar una tarea, se registra qué agente o ejecución real representa al perfil cuando ese dato existe. Si aún no hay ejecución, el perfil se muestra como definido o disponible, no como trabajando. Un cambio de nombre mantiene una referencia al perfil y al historial anterior. No se simulan cinco agentes porque el panel muestre cinco tarjetas.

Los perfiles pueden intercambiar solicitudes mediante las herramientas de coordinación disponibles en el alcance autorizado. Eva conserva visibilidad sobre dependencias, presupuesto y conflictos; no es obligatorio hacer pasar cada respuesta por una cadena artificial de intermediarios. Si la herramienta no permite contacto directo, Eva retransmite la solicitud y registra esa intermediación.

## 3. Conversaciones verificables

Cada solicitud debe permitir reconstruir estos datos, con los nombres concretos de campos del esquema validado por el CLI:

| Dato | Contenido necesario |
|---|---|
| Identidad | Evento, misión y correlación estables. |
| Emisor y receptor | Perfiles nombrados y vínculo de ejecución real cuando exista. |
| Solicitud | Acción concreta que se necesita. |
| Motivo | Razón operativa resumida y objetivo primario al que contribuye. |
| Alcance | Fuentes, archivos o destinos permitidos y dependencias relevantes. |
| Entregable | Resultado esperado y criterio de comprobación. |
| Estado y tiempo | Hecho observado y momento del registro; no actividad futura presentada como actual. |
| Evidencia | Referencias a fuentes, artefactos, resultados de herramientas o verificaciones. |

Una respuesta referencia la misma correlación de su solicitud y explica qué se hizo, qué se comprobó, el resultado, los límites y cualquier dependencia pendiente. Un mensaje que pide otra acción genera su propia solicitud vinculada; no se confunde con una respuesta final.

Se permite un estilo natural: un agente se dirige a otro por su nombre y explica lo que necesita. El contenido debe provenir de intercambios efectivamente realizados. Los ejemplos, ensayos y conversaciones planificadas se identifican como tales y no entran al historial de ejecución real.

Se registra una solicitud despachada solo después de que la herramienta confirme el envío real. Una herramienta fallida se documenta como fallo y no como mensaje recibido. La bitácora resume información útil; no necesita transcribir prompts completos, secretos ni razonamiento privado. El CLI de bitácora registra y valida eventos; no realiza el despacho. El servidor local descrito en §6 sí inicia Codex CLI cuando el usuario envía un mensaje.

## 4. Directiva común de optimización

Durante cada misión, todos los perfiles buscan mejoras en mantenimiento y documentación, ejecución completa del DS y consumo de tokens. Iris compara las oportunidades cuando se justifica un trabajo específico de optimización. Eva conserva el foco de la misión.

Cada propuesta identifica el problema, el objetivo primario afectado, una referencia medible, la hipótesis, el coste de comprobarla, los posibles efectos y el criterio para conservarla o revertirla. Una propuesta sin medición suficiente queda como hipótesis; no se comunica como ahorro demostrado.

Puede ejecutarse una mejora que apoye la solicitud vigente, respete sus restricciones y sea verificable con coste razonable. Si introduce una nueva línea de trabajo, se registra en la lista de propuestas para decisión posterior. La directiva no crea una autorización permanente para editar cualquier componente, publicar cambios adicionales o ejecutar tareas cuando no haya una misión activa.

Se conserva una mejora cuando la evidencia supera el criterio definido sin incumplir requisitos. Si no mejora, se descarta o revierte de forma controlada y se documenta el aprendizaje. Ante resultados inconclusos se mantiene ese estado. Se detiene la búsqueda al alcanzar el objetivo, el límite autorizado o una dependencia material que impida avanzar; se continúa lo independiente.

## 5. Pipeline y QA

El destino solicitado determina los protocolos aplicables. Para una construcción del DS: fuentes y contrato versionados, QA documental, delegación técnica registrada, preparación del destino, implementación, lectura del resultado y QA de implementación. P-SLOTS se revisa cuando se construye o modifica una familia. P07 y P08 se aplican según su alcance; este protocolo no activa Figma o frontend si el encargo solo pide documentación.

Vera debe ser una ejecución distinta del autor para cambios de flujo o alto impacto según la decisión de cierre técnico. Se reutilizan pruebas deterministas y evidencia vigente cuando basten. Cada agente documenta su propio trabajo; Atlas facilita organización y consulta sin convertirse en condición necesaria para registrar un resultado.

El cierre requiere QA suficiente, evidencia y entregables aplicables. Todo evento con estado `PASS` o `COMPLETED` exige evidencia local existente, también cuando sea una decisión y no una respuesta. Las notas o decisiones informativas sin cierre técnico pueden registrarse como `RECORDED`; una prueba sin ejecutar se registra como `NOT_RUN`. La existencia del archivo es una validación estructural: quien verifica debe comprobar además que su contenido sustenta el resultado declarado. Se registran `user_audit: NOT_REQUIRED` y `human_review_policy: OPTIONAL_NON_BLOCKING` en los nuevos registros de cierre técnico. `DELEGATED_FOR_BUILD` no equivale a aprobación humana; `VALIDATED` requiere comprobación real. Los estados `FAIL`, `BLOCKED`, `NOT_RUN` o `STALE` no se transforman en `PASS` por ausencia de revisión humana.

Una observación posterior del usuario abre corrección y revalidación del alcance afectado, conservando el cierre histórico. Los conflictos de fuentes, permisos ausentes, requisitos indispensables desconocidos o pruebas fallidas limitan la operación afectada; se documentan sin frenar tareas independientes.

Para la skill de Figma se conserva la conexión MCP autenticada con capacidad real de escritura, el destino explícito distinto de la biblioteca maestra y el acceso a los componentes reales del DS. La oficina no recrea familias existentes para eludir falta de acceso. La skill de prototipos mantiene independencia de Figma.

## 6. Registro, panel y continuidad

`office/events.jsonl` conserva los eventos registrados. Se agregan mediante el CLI y se validan antes de generar `office/dist/index.html`. Una corrección se documenta con referencia al evento afectado; no se reescribe la historia para ocultar una operación fallida. `evidence` solo admite rutas relativas de archivos locales existentes dentro de la raíz del proyecto. Para resultados externos se guarda un reporte local con lo observado y sus límites. `tool_ref` identifica una referencia declarada de herramienta; su presencia no implica que el CLI haya consultado o verificado el recurso externo. Una ruta prevista no demuestra un resultado.

El chat es una vista derivada del registro, con perfiles, mensajes cronológicos, citas de respuesta y detalles consultables de solicitud, motivo y evidencia. `record` y `render` generan HTML y `office/dist/state.json`; no se exige ejecutar `render` manualmente después de cada `record`. Servido por HTTP, el chat consulta ese estado cada tres segundos mientras está visible y muestra la desconexión cuando corresponde. Abierto directamente como archivo HTML conserva el corte incluido y no admite envío. Abrir la vista no inicia una ejecución: enviar una solicitud al servidor sí. No hay transmisión de tokens ni presencia permanente de agentes; cada estado expresa el último hecho registrado.

El servidor se inicia con `python3 scripts/evolution_office_server.py`, escucha en loopback en el puerto 8766 por defecto y exige origen coincidente y token local para enviar solicitudes. Utiliza Codex CLI con autenticación guardada y su propia configuración de herramientas/MCP, que no se presupone idéntica a la aplicación Codex. Cada mensaje inicia una ejecución nueva en la raíz del repositorio; no reanuda automáticamente el hilo de la aplicación ni una ejecución anterior. Se consultan instrucciones y registros pertinentes para recuperar continuidad. Solo se acepta un trabajo activo; repetir el mismo identificador con el mismo contenido no duplica la ejecución. El actor `user` representa al usuario, no un perfil adicional.

Durante la ejecución, el servidor procesa los eventos públicos de Codex incrementalmente. El chat consulta los avances cada dos segundos: muestra mensajes públicos, coordinación confirmada y la hora de la última actividad. Tras treinta segundos sin eventos informa «Sin novedades», sin deducir progreso del proceso abierto. No muestra razonamiento privado, argumentos de herramientas ni sus salidas crudas. Los avances se conservan en el trabajo local; al recargar se recupera el trabajo activo o el último. El historial permanente conserva las respuestas registradas; la vista de avances corresponde al trabajo más reciente.

El servidor registra la solicitud después de iniciar realmente el proceso y registra su respuesta final con `RECORDED` o el fallo con `FAIL`. Una respuesta recibida no equivale a QA `PASS`, aprobación humana ni cierre del objetivo. Los especialistas mantienen intercambios separados solo mediante ejecuciones y mensajes reales; el modelo no debe producir un diálogo ficticio entre perfiles para llenar el chat.

La solicitud, estado, resultado y logs del proceso se conservan localmente bajo `output/office-runtime/`, excluido de Git. Los logs no se sirven por HTTP; el resultado local puede enlazarse como evidencia. La bitácora y su vista también contienen solicitudes y respuestas: deben revisarse antes de publicar, no considerarse anónimas porque el runtime esté excluido. El servidor no publica automáticamente esos archivos, secretos ni prompts privados. Una publicación posterior conserva los permisos y revisión de alcance que correspondan.

Para reanudar, Eva consulta la configuración, el historial de la misión y los artefactos citados. Verifica cambios de fuentes y dependencias antes de reutilizar resultados. La correlación conecta el encargo y sus respuestas aunque cambie el agente concreto entre sesiones. Los hechos que solo sobreviven en la conversación deben registrarse antes de cerrar.

Antes del cierre o de una transferencia, el responsable agrega una nota de continuidad al registro existente con cinco datos resumidos: solicitud y correlaciones de referencia; último resultado comprobado; siguiente acción dentro de alcance o indicación de misión cerrada; bloqueos y límites; rutas de evidencia y versiones o hashes ya comprobados cuando existan. Usa `kind: note` y `status: RECORDED`, el esquema vigente y su contenido textual; no introduce otro formato de estado ni otro archivo editable que replique el historial. No inventa hashes ni pendientes para completar la nota. Esta nota facilita la navegación, pero no constituye un cierre `PASS` ni sustituye leer la evidencia pertinente. Al reanudar se comienza por ella y se amplía la lectura solo cuando fuentes, versiones o dependencias lo requieran. Si la nota falta, se reconstruye el estado desde los eventos y se informa la ausencia.

P05 rige la sincronización del grafo por lote coherente y los registros canónicos del proyecto. La bitácora de oficina enlaza esos registros, no crea una segunda definición editable de contratos, valores o aprobaciones. Un grafo desactualizado se informa como tal sin simular vigencia.

## 7. Criterio de entrega de la oficina

La configuración identifica los cinco perfiles y sus directivas; los eventos permiten rastrear solicitudes y respuestas; el validador comprueba el formato y la coherencia que declare soportar; el panel representa esos mismos datos. El cierre técnico informa qué controles se ejecutaron y qué capacidades quedan fuera del módulo. Una interfaz visible no acredita por sí sola un despacho de agente.

Esta versión permite enviar solicitudes al servidor local y actualizar los mensajes registrados. No presupone continuidad automática de conversaciones, igualdad de conexiones MCP con la aplicación, presencia permanente, transmisión de tokens ni seguimiento periódico después de una ejecución. El funcionamiento real del servidor y sus errores requieren QA propio; este protocolo no afirma pruebas por describir el flujo. La búsqueda continua de optimizaciones significa aplicar la directiva durante cada trabajo autorizado.
