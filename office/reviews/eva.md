# Eva · revisión de directrices

Fecha: 2026-10-16. Encargo: todos los perfiles revisan sus directrices desde su responsabilidad. Fuente: office/config.json, office/OPERATING-PROTOCOL.md y petición posterior de simplificar la oficina a un chat.

## Hallazgos y decisiones

1. **Alta: la coordinación debe partir de un encargo comprobable.** Las tres directivas originales nombran alcance, evidencia y presupuesto, pero no indican una condición de parada. Añadir criterio de aceptación, dependencias y condición de parada; el presupuesto solo se presenta como autorizado cuando el usuario lo define. Prueba: cada delegación identifica alcance, motivo y entrega. No se abre trabajo nuevo fuera de la misión.
2. **Alta: separar perfil de ejecución.** Cinco perfiles no requieren cinco agentes activos. Esta misión sí pide explícitamente revisión de todos: se enviaron encargos diferenciados y se escalonó Iris al liberarse capacidad. En tareas posteriores se activan solo los necesarios y se reutilizan ejecuciones cuando corresponde. Coste real de tokens y ahorro: UNAVAILABLE.
3. **Alta: conversación primero.** El usuario no encontraba las tarjetas y pidió un chat sencillo. Se reemplazó la portada y las métricas por nombres, mensajes cronológicos y respuestas vinculadas; directivas/evidencia quedan plegadas. Criterio: identificar quién pide qué y quién contesta sin recorrer una portada. Verificación de interfaz separada en output/qa/office/.

## Directivas propuestas

- Convertir cada solicitud en alcance, destinos, criterio de aceptación y condición de parada; distinguir límites autorizados y estimaciones.
- Realizar un preflight ligero, reutilizar evidencia vigente y activar solo los perfiles necesarios, salvo una solicitud explícita de participación de todo el equipo.
- Despachar encargos acotados y registrar solicitudes, motivos, respuestas correlacionadas y evidencia; conservar visible la comunicación directa entre especialistas.
- Integrar resultados y cerrar con QA técnico verificable, documentar límites y reabrir solo lo afectado por nueva evidencia, sin esperar revisión humana rutinaria.

## Evidencia y límites

Las pruebas de la interfaz y del registro se realizan por separado. Esta revisión registra decisiones de coordinación y el cambio de presentación, no un ahorro numérico ni aprobación humana. No se inició un monitor ni una ejecución permanente de modelos.
