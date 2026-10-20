# QA documental · arquitectura de chat embebido 0.1.1

2026-10-20. CONTRACT_REVIEW: PASS para el alcance de arquitectura y consumo documental de [APP-SHELL-EMBEDDED-CHAT-001](../../specs/components/app-shell.embedded-chat.amendment.v0.1.1.md). `user_audit: NOT_REQUIRED`; `human_review_policy: OPTIONAL_NON_BLOCKING`. No implica aprobación humana ni canonicalidad completa de la instancia.

## Fuente y cobertura

Inspección directa, solo lectura, de `1108:3201` en `tj3WIBEZDGLVs7MJWKCwgf`. [Índice](../../sources/figma-snapshots/embedded-chat-shell.1108-3201.index.2026-10-20.json) y lotes de propiedades conservan340 nodos,96 instancias,55 principales,98 variables y20 estilos. Incluye21 Slots y descendientes ocultos. Propiedades de alternativas preferidas resumidas por cantidad, sin importar componentes remotos ni resolver todas las alternativas.

[Contrato de observación MD](../../drafts/contracts/embedded-chat-shell/component-contract.md) y [YAML](../../drafts/contracts/embedded-chat-shell/component-contract.yaml), derivados de un mismo modelo. [Captura1440×1024](../../output/qa/embedded-chat-shell-2026-10-20/figma.png) revisada: contexto global conservado, bienvenida y escritura centrales, historial derecho y cabecera contextual sobre ambos.

## Controles

| Control | Resultado y alcance |
|---|---|
| DOC-01–06,09,11,15 | PASS: enmienda de composición, activación explícita del usuario, alcance restringido al caso embebido; muestras separadas de requisitos. |
| DOC-07,08,10,18 | PASS documental: bindings/valores conservados como evidencia; fuente canónica referenciada. Wrappers sin binding, estilos vacíos y dependencias remotas no se presentan como normalizados. |
| DOC-12,13,16,17 | PASS: mapeo a exports existentes, página Layout de la instancia diferenciada de App Shell del principal; criterios verificables y límites por destino explícitos. |
| DOC-14 | PASS: Figma leído sin mutaciones, snapshots originales conservados. |
| ECS-02–05 | PASS de cotejo estructural: Header+Body, rail+Content, cabecera+fila, Chat Section izquierda e historial derecha. |
| ECS-06 | PASS documental: máximo816 heredado de Chat Layout0.1.1; máximo542 del contrato base sustituido por esa enmienda vigente. |
| ECS-07 / SLOT-QA-01–02 | PASS de inspección: tipos SLOT reales e identidades registrados. Las cantidades visibles son muestras. |
| SLOT-QA-03–08 | NOT_APPLICABLE a esta ejecución de documentación sin mutaciones; no se declara una nueva validación funcional de edición de Slots. Una construcción futura requiere esos controles. |
| ECS-08–09 | PASS documental con límites: separación efectiva0 frente a itemSpacing32, override Contable y casos estrechos no probados. |
| ECS-10–11 | Mapeo y criterio de aceptación documentados; publicación e integridad del catálogo se comprueban en el cierre P08. |

## Limitaciones materiales

No se normalizan ni certifican los detalles locales del diseño. Description y Beta carecen de estilo compartido; hay controles remotos y un modo Contable explícito en Toolbar. El personaje expone una reacción por timeout que no convierte esta arquitectura en un nuevo contrato de animación. Las bibliotecas/versiones fuente remotas no están expuestas por MCP.

El QA cubre una muestra desktop Standby, no Active, colapso, temas alternativos, listas extensas, móvil, foco o backend. No se genera un componente web nuevo; se documenta composición de componentes existentes. La implementación web previa no certifica igualdad visual de esta pantalla.

Los primeros payloads excedieron48000 bytes; la extracción se completó por lotes con preferidos resumidos por cantidad. No se realizaron escrituras Figma. No hay cambios de tokens, estilos ni Code syntax.
