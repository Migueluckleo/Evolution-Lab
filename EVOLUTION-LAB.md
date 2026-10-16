# Evolution Lab

Oficina de agentes para optimizar la construcción y el mantenimiento del sistema de diseño CONTPAQi y sus skills. [Entrar a la oficina](office/dist/index.html) · [Guía operativa](office/README.md) · [Protocolo de comunicación](office/OPERATING-PROTOCOL.md).

## Objetivos y equipo

La configuración canónica de [perfiles y directivas](office/config.json) reúne cinco roles: Eva coordina, Atlas documenta, Bruno construye, Vera verifica e Iris optimiza. Son perfiles de IA activados por encargo; no se afirma que cinco procesos permanezcan ejecutándose. Atlas eligió su nombre y la verificadora adoptó Vera; los demás nombres de especialistas son asignaciones iniciales del orquestador.

El equipo prioriza documentación fácil de consultar, ejecución documentada de los protocolos del DS y ahorro de tokens antes de construir. En cada tarea busca mejoras relacionadas con estos objetivos, compara resultados y registra aprendizajes. Esa directiva no autoriza ampliar el alcance ni iniciar tareas periódicas.

## Comunicación observable

La oficina muestra un chat con nombres, solicitudes y respuestas correlacionadas en orden. Permite filtrar por agente y buscar texto; las directrices y la evidencia se abren bajo demanda. Su fuente es [el registro de eventos](office/events.jsonl), validado mediante [el CLI de oficina](scripts/evolution_office.py).

Codex realiza los envíos con sus herramientas de colaboración y el operador registra sus resultados reales. El chat servido por HTTP consulta el estado generado cada tres segundos mientras está visible; el archivo HTML abierto directamente conserva el corte guardado. Los intercambios se presentan resumidos conforme se registran; no contienen razonamiento privado. Al iniciar `python3 scripts/evolution_office_server.py`, el campo de mensaje despacha una ejecución nueva de Codex CLI por encargo usando la sesión local. Eva consulta los registros y activa los perfiles necesarios; no hereda automáticamente la conversación del escritorio ni sus conexiones MCP. El servidor acepta un encargo a la vez, conserva la correlación para evitar duplicados y publica en el chat el resultado real. El modo HTML sin ese servidor sigue siendo de consulta. Un hash encadenado detecta cambios accidentales en el registro, pero no es una firma ni prueba por sí solo que un agente habló.

## Construcción y QA

La solicitud determina los protocolos aplicables. La documentación, el QA y la evidencia de implementación permiten cerrar el trabajo técnico delegado sin una revisión humana rutinaria como bloqueo. Una prueba fallida o evidencia requerida ausente bloquea la parte afectada; una observación posterior del usuario abre una corrección acotada. No se simula aprobación humana.

Para pantallas Figma se necesita una conexión MCP autenticada con capacidad real de escritura y un archivo destino explícito distinto de la biblioteca maestra. Se reutilizan componentes auténticos del DS accesibles en ese destino; no se recrean familias existentes para eludir falta de acceso. Los componentes nuevos cubren necesidades ausentes del catálogo. La skill de prototipos no exige Figma.

## Distribución y mantenimiento

El contenido del DS se publica en GitHub independientemente de la versión del motor instalado. Las skills consultan `catalog/current.json` al comenzar un encargo, verifican manifiesto y archivos, reutilizan caché verificada y fijan ese corte durante el trabajo. No continúan silenciosamente con una copia antigua si no pueden comprobar la fuente.

El workflow de GitHub actualiza el catálogo tras cambios y comprobaciones satisfactorias. La primera ejecución corregida fue verificada en GitHub; los ZIP 0.3.2 descargaron fuentes sin credenciales en pruebas locales. Los instaladores se entregan localmente, no se publican en el repositorio. La ejecución dentro de Genspark es una prueba separada que realiza el usuario.

Los protocolos y fuentes existentes mantienen su autoridad. La oficina organiza la ejecución y visibilidad; sus perfiles no reemplazan los contratos ni los criterios de QA.
