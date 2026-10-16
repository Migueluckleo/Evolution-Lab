# Conversation · primera incorporación externa

Fecha: 2026-10-08. Estado de fuente INDEXED; inspección PARTIAL; contrato normativo destino NOT_STARTED; implementación NOT_STARTED. No equivale a aprobación ni publicación.

## Solicitud y alcance

El usuario aporta el nodo Anticipa `20355:72763` como el primero de otros componentes que deben vivir en AI Design System. Fuente `zuUq3gcF9T3CLid44bjY6W`; destino previsto `tj3WIBEZDGLVs7MJWKCwgf`. No se incorpora el resto del archivo ni una lista futura de componentes por inferencia.

Se aplicaron figma-component-contract/figma-use para inspección de solo lectura, P02/P05 para persistencia y P-SLOTS para clasificación. Graphify se consultó para localizar relaciones; su salida recortada no se tomó como inventario completo y las referencias pertinentes se confirmaron en archivos.

## Entregables de esta ingesta

- [Contrato de evidencia MD](../contracts/conversation.source.component-contract.md) y [modelo YAML](../contracts/conversation.source.component-contract.yaml).
- [Snapshot](../../sources/figma-snapshots/conversation.20355-72763.observation.2026-10-08.json):147 nodos, cuatro variantes,47 instancias/21 principales, siete Slots,51 variables y tres estilos. Cobertura parcial por propiedad, expresamente delimitada.
- Inventario canónico sin modificaciones: `sources/inventories/tokens.inventory.json`, SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.

## Propuesta de integración — no norma adoptada

Página semántica candidata: **Conversation**. Es coherente con PROP-03 de [Anticipa Screen Composition](../contracts/anticipa-screen-composition.contract.v0.1.0.md), que continúa siendo DRAFT; no se aprueban sus demás propuestas.

Separar la evidencia de Message Sent, respuestas BENI/NAVI y composer. Valorar componentes de mensaje y composer reutilizables sin convertir nombres genéricos como `Property 2` en una API final. Mantener reconocible la apariencia y el contenido de demostración. No introducir estados ni acciones de producto sin respaldo.

Antes de construir, contrastar las dependencias con contratos y enmiendas vigentes de Buttons, [Icon Button](../../specs/icon-button.contract.v0.1.0.md), [Badge](../../specs/components/badge.contract.v0.1.0.md) e iconos; no copiar principales remotos ni reconstruir controles ya existentes. [Textarea](../../specs/textarea.contract.v0.1.0.md) no demuestra por sí solo un composer completo ni autoriza importar sus restricciones como reglas de chat.

Resolver cada token de interfaz al JSON canónico y extensiones normativas aplicables, con rol/scope correcto y variable local comprobada; conservar aliases y herencia de temas. No usar primitivas directamente ni importar variables internas `Color/...`, `Font/...`, `Size/...` de Anticipa por coincidencia visual. Las variables `message-Actions/state-ThumbsUp` y `state-ThumbsDown` son evidencia de prototipo, no nuevos tokens de Foundations por defecto.

La identidad gráfica de BENI/NAVI requiere tratamiento explícito como dependencia de artwork. La excepción agnóstica autorizada para Logos no se extiende automáticamente a personajes nuevos. Tampoco se recolorean sus vectores como si fueran iconos funcionales. Su alcance visual/animado debe quedar definido en el contrato antes de implementarlo.

## P-SLOTS

Aplicabilidad REQUIRED para regiones de respuesta compuesta, previews y acciones variables. Se leyeron Slots nativos AnswerText/Secondary actions/previews duplicados en las dos respuestas y text en el composer. No se probó todavía insertar, retirar, reordenar o sustituir desde instancias consumidoras. No hay QA de implementación. El ejemplo no impone una cantidad máxima de previews ni de acciones.

## Límite antes de P04

P03 acota DEC-LEGACY-MIGRATION-DELEGATION-001 al archivo raíz `9zs5RMR8LB5wHjW9Bd59BA`; la excepción Table corresponde únicamente a Table. La nueva intención de incorporar Conversation no se registra como aprobación de un contrato todavía inexistente ni como extensión automática de delegación a todos los componentes de Anticipa.

Confirmar una sola vez si los nodos externos que el usuario señale seguirán el mismo esquema delegado: contrato y mapa de tokens, QA documental, construcción, QA técnico, promoción a specs y auditoría humana por excepciones. Registrar el alcance explícito antes de habilitar P04. No hace falta una aprobación adicional por cada dependencia conforme una vez autorizado ese alcance.

## Continuidad y comprobaciones

Lectura realizada: identidad/árbol/layouts/propiedades del set, textos, principales activos, referencias de variables/estilos y resumen de reacciones. Limitaciones detalladas en el MD/YAML: getter de propiedades con error en origen, estilos y aliases parcialmente resueltos, condicionales y detalles gráficos incompletos. Resolver lo pertinente al contrato destino; no duplicar contratos de dependencias.

Sin cambios en Figma fuente o destino, sin nuevas variables, sin publicación de biblioteca, sin frontend. Grafo STALE_FOR_CONVERSATION_INTAKE, no regenerado. Estos son pasos necesarios de esta incorporación concreta, no una auditoría global ni nuevos pendientes del resto del DS.
