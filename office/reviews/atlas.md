# Atlas · Revisión de directrices y mantenimiento documental

Fecha: 2026-10-16. Destinataria: Eva. Alcance: perfil documentalista y documentación de la oficina. Estado: revisión documental y contraste independiente de continuidad `PASS`; ajuste posterior de documentación del chat realizado. Ahorro de tokens y tiempo: `UNAVAILABLE`.

## Solicitud y fuentes

El usuario pidió que cada integrante revise sus propias directrices y proponga cómo optimizar los objetivos primarios desde su responsabilidad. Eva asignó a Atlas mantenimiento, duplicaciones, consulta eficiente y continuidad, con permiso para modificar únicamente README/protocolo de oficina y este informe. No se cambió configuración, AGENTS, fuentes del DS ni publicación.

Fuentes consultadas: [configuración, perfil atlas y directivas comunes](../config.json), [README](../README.md), [protocolo operativo](../OPERATING-PROTOCOL.md) y [P05, secciones 2, 7, 8 y 9](../../protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md). Se reutilizó la lectura de P05 realizada en este mismo encargo documental; no se afirma una comprobación nueva de sus hashes.

## Directrices revisadas

El perfil de Atlas ya exige conservar fuentes/autoridad/versiones, facilitar consulta y detectar duplicaciones. Son adecuadas, pero no especifican una unidad mínima de continuidad ni cómo evitar lecturas repetidas. Las reglas comunes ya cubren evidencia, foco y preflight; repetirlas completas en el perfil aumentaría el mantenimiento sin añadir una responsabilidad distinta.

Propuesta exacta para sustituir las tres directivas de Atlas en `config.json`, pendiente de integración por Eva:

1. Conservar y enlazar la fuente canónica, su autoridad, versión y evidencia; mantener historia sin duplicar requisitos editables.
2. Ofrecer una entrada de consulta por necesidad y una nota de continuidad por cierre o transferencia; comprobar cambios antes de reutilizar lecturas.
3. Detectar duplicaciones y contradicciones, corregir la fuente responsable dentro del alcance y medir la consulta cuando haya datos; declarar UNAVAILABLE si no existe medición.

## Hallazgos y mejoras

| Evidencia concreta | Problema | Mejora y estado |
|---|---|---|
| README anterior, «Continuar una misión», pedía leer protocolo, configuración y eventos pertinentes sin ordenar la búsqueda; protocolo 0.1.0 §6 pedía consultar historial sin un punto de entrada. | Una sesión nueva debía reconstruir por su cuenta qué leer primero. | **Prioridad 1, aplicada:** cuatro rutas de consulta por necesidad y una nota de continuidad dentro de los eventos existentes. No se añadió otra fuente de estado. |
| `config.json`, `agents[id=atlas].directives`; README «Equipo»; protocolo §2. | Existen descripciones en tres superficies. Su función no estaba completamente delimitada y podrían evolucionar como reglas paralelas. | **Aplicada:** README identifica su tabla como resumen, configuración como fuente de directivas y protocolo como fuente del procedimiento común. No se borraron resúmenes útiles ni se duplicaron directivas nuevas. |
| README «Autorización, fuentes y límites» referencia la historia de `EVOLUTION-LAB.md` en la copia pública; P05 §2 exige rutas reales y §9 continuidad sin depender de conversación. | La nota de procedencia es válida para el trabajo inicial, pero no es una entrada estable para consultar el estado vigente de toda la entrega. | **Propuesta acotada:** al consolidar la entrega, Eva debe enlazar el documento canónico publicado y su evidencia de estado. No se sustituyó esa referencia por una ruta supuesta ni se verificó otra vez GitHub en esta revisión. |

## Antes y después comprobable

| Medida estructural | Antes | Después | Interpretación |
|---|---:|---:|---|
| Rutas explícitas de consulta por necesidad en README | 0 | 4 | Se pueden comprobar contando las cuatro filas de «Consulta por necesidad». No mide velocidad de consulta. |
| Formatos mínimos de nota de continuidad en protocolo §6 | 0 | 1 | La nota contiene cinco datos resumidos y usa el registro existente. No afirma que ya se haya escrito una nota real. |
| Nuevos archivos editables de estado requeridos | 0 | 0 | La nota usa `events.jsonl`; este informe es evidencia de revisión, no estado canónico. |
| Tokens o segundos ahorrados | `UNAVAILABLE` | `UNAVAILABLE` | No hay contador ni comparación de sesiones equivalentes. |

Modificaciones exactas: README añade «Consulta por necesidad», aclara autoridad de los resúmenes y ordena reanudación. OPERATING-PROTOCOL pasa a 0.1.1 con alcance de revisión explícito y añade el párrafo de nota de continuidad en §6. La revisión conserva comprobación de fuentes, protocolos obligatorios, QA y permiso de ejecución.

Comprobación local ejecutada tras guardar: los tres archivos existen; se contaron cuatro rutas y un párrafo de continuidad; la cabecera del protocolo declara 0.1.1; no se encontraron destinos de archivo inexistentes en sus enlaces Markdown. Este control no comprobó el renderizado de los fragmentos de sección ni midió la recuperación en una sesión nueva.

## Prueba prioritaria propuesta

En el siguiente cierre real, registrar una nota con los cinco datos establecidos. En una reanudación independiente, comprobar si el lector puede identificar la solicitud, último resultado, siguiente acción, bloqueos y evidencia empezando por esa nota y sus enlaces, sin depender de la conversación. Criterio de aceptación: cinco datos localizables, referencias existentes y ausencia de contradicción con eventos/evidencia; un dato que no aplique se indica como tal.

Medir archivos y eventos consultados, errores de recuperación y, solo si está disponible, tokens/tiempo. Para comparar ahorro se requiere otra misión equivalente o una referencia previa observable; hasta entonces no se atribuye mejora cuantitativa. No se requiere ejecutar una misión ficticia para fabricar esa comparación.

## Cierre y límites

Atlas conserva su nombre elegido. Esta revisión y sus modificaciones son reales, dentro del alcance asignado. Vera contrastó README, protocolo 0.1.1 §6 e informe y respondió `PASS` para las cuatro rutas y la nota: sus cinco datos caben en texto con `note/RECORDED`, sin nuevos estados. Las correlaciones de esa nota se conservan en texto; `reply_to` corresponde a respuestas. Este QA documental no equivale a repetir pruebas de implementación. El intercambio y su resultado se registran desde los mensajes efectivamente enviados. La integración de propuestas de directiva en configuración y la generación del panel corresponden a Eva. La sincronización del grafo se realiza con el lote de oficina, sin declarar CURRENT desde este informe.

## Ajuste posterior solicitado: chat con actualización

Eva comunicó la implementación del chat solicitada por el usuario. Atlas alineó README y protocolo 0.1.2: `record` y `render` generan HTML y estado; el chat por HTTP consulta ese estado cada tres segundos mientras está visible, informa desconexión y muestra mensajes resumidos registrados. Abrir el archivo HTML directamente conserva el corte incluido. Se añadió el comando del servidor local y su enlace. Se retiró la indicación de regenerar manualmente después de registrar. Este ajuste no afirma transmisión de tokens, despacho desde el panel ni actividad permanente de agentes. La comprobación de comportamiento del chat corresponde al QA de implementación de Eva/Vera; Atlas documentó la interfaz comunicada y no ejecutó una prueba de navegador.
