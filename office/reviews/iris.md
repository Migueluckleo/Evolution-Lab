# Iris · revisión de mis directrices

Fecha: 2026-10-16. Para: Eva. Nombre confirmado: **Iris**, optimizadora. Estado: **PROPUESTAS**; este informe no cambia las directivas canónicas ni acredita una mejora medida.

Revisé mi perfil y las reglas comunes de [configuración](../config.json), el [protocolo operativo](../OPERATING-PROTOCOL.md) y los informes de [Atlas](atlas.md), [Bruno](bruno.md) y [Vera](vera.md). El alcance es simplificar la optimización durante encargos autorizados. Reutilicé estos informes; no volví a ejecutar sus comprobaciones ni a consultar componentes del DS. El usuario pidió expresamente revisar todos los perfiles en esta misión; eso no obliga a activarlos todos en las siguientes.

## 1. Preflight reutilizable y selección proporcional — prioridad alta

**Hallazgo:** el protocolo ya define un preflight ligero; mi perfil no concreta cuándo dejar de analizar oportunidades. Atlas propone continuidad, Bruno reutilización por destino y Vera QA por impacto. Conviene integrar esas referencias una vez, sin crear otra ronda obligatoria de revisión.

**Directiva exacta propuesta:** “Antes de proponer una optimización, reutiliza el preflight vigente y vincula el problema con un objetivo primario y el alcance solicitado. Prioriza la alternativa mínima que pueda comprobarse; pide otra ejecución solo por una dependencia concreta o una revisión obligatoria. No repitas el análisis sin un cambio material.”

**Comparación y parada:** comprobar si la propuesta ayuda al criterio de aceptación de la misión y qué lecturas, herramientas, intercambios y correcciones requiere. Conservar el flujo más simple que cumpla los requisitos. Parar al cumplir el encargo, alcanzar su límite autorizado o encontrar una dependencia material; una oportunidad ajena queda registrada, sin ejecutarla. Un límite propuesto no se presenta como presupuesto aprobado.

## 2. Chat legible con evidencia consultable — prioridad alta

**Hallazgo:** el usuario pidió ver cómo se responden los agentes y señaló complejidad excesiva. El protocolo admite lenguaje natural y mantiene correlación/evidencia. Esa trazabilidad puede conservarse sin obligar al usuario a leer todos los campos de cada evento.

**Directiva exacta propuesta:** “Comunica a cada destinatario una solicitud o respuesta breve con su motivo y resultado. Conserva correlación, alcance y evidencia en el registro y permite consultarlos bajo demanda; evita mensajes ceremoniales, duplicaciones y conversaciones simuladas.”

**Comparación y parada:** verificar en la misma conversación real que se identifica quién habla, a quién responde y qué necesita o entrega; después comprobar que los detalles siguen accesibles. Comparar pasos necesarios para seguir una respuesta y errores de interpretación, cuando se observen. Parar cuando el chat permita esa lectura y conserve trazabilidad; no añadir paneles o ceremonias que no resuelvan una necesidad del encargo. Actualización de la vista y ejecución real de agentes siguen siendo capacidades diferentes.

## 3. Medir coste completo y conservar independencia del catálogo — prioridad media

**Hallazgo:** mi segunda directiva menciona coordinación y retrabajo, pero el beneficio no está cuantificado. Bruno recuerda que un cambio compatible de contenido del DS no exige cambiar el motor de las skills. Es un requisito que debe conservarse, no un ahorro que esta revisión haya demostrado.

**Directiva exacta propuesta:** “Compara alternativas con el mismo alcance y requisitos, incluyendo ejecución, consultas, coordinación y retrabajo. Declara UNAVAILABLE donde falten mediciones; conserva solo mejoras verificadas sin regresión. Mantén separadas las actualizaciones compatibles del catálogo DS y las del motor de las skills; no propongas reinstalaciones por cambios solo de contenido.”

**Comparación y parada:** antes de experimentar, fijar el resultado esperado y la evidencia necesaria, reutilizando los controles vigentes de Bruno y Vera. Para contenido compatible, comprobar que el motor instalado obtiene el nuevo corte remoto y que un trabajo iniciado conserva el suyo, conforme P08. No ejecutar otra vez esas pruebas si su vigencia y alcance ya están comprobados. Parar cuando haya evidencia suficiente; si falta una referencia comparable, concluir hipótesis o resultado inconcluso sin fabricar porcentajes.

## Medición, coordinación y cierre

| Dato | Resultado de esta revisión |
|---|---|
| Directivas propias leídas | 3, en `agents[id=iris].directives` del corte consultado |
| Informes de otros perfiles reutilizados | 3: Atlas, Bruno y Vera |
| Nuevos encargos a especialistas por Iris | 0; los informes resolvieron las dependencias de esta revisión |
| Tokens, tiempo, coste de coordinación y retrabajo comparables | `UNAVAILABLE` |
| Ahorro demostrado o experimento comparativo ejecutado | Ninguno; `NOT_RUN` |

Los conteos describen esta revisión, no miden ahorro. El coste de adoptar las propuestas incluye integrarlas una vez en la configuración y verificar su coherencia; el ajuste visual y su QA pertenecen al encargo de Eva. No se añade una aprobación de Iris a cada trabajo ni una revisión humana rutinaria.

Cambio realizado: únicamente este informe. Comprobación local: archivo guardado y referencias locales existentes. La integración, el registro del intercambio real, la validación del chat y el cierre del grafo corresponden al lote coordinado por Eva. No se modificaron componentes, skills ni publicación remota.
