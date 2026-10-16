---
report_schema: sdd-project/0.2
report_type: CONTRACT_SYNTHESIS
report_id: SYN-BUTTON-001
contract_id: BUTTON-001
contract_version: 0.1.0
created_at: 2026-09-23
review_status: REVIEWED_WITH_BLOCKERS
---

# SYN-BUTTON-001 · síntesis del contrato Button

## 1. Encargo y entregables

El usuario compartió el nodo Figma `26:81` y pidió ejecutar todo el protocolo SDD. Se realizó ingesta, inspección read-only, síntesis, trazabilidad y QA documental. Se generaron el candidato [Markdown](../contracts/button.contract.md), el [modelo técnico YAML](../contracts/button.contract.yaml), este reporte y [QA-BUTTON-001](../../qa/contracts/button.review.md). No se modificó Figma ni se generó frontend.

P04 no puede comenzar hasta que exista aprobación explícita de `BUTTON-001` `0.1.0` y se decidan los bloqueos de alcance.

Actualización de fuente: el usuario fijó [Phosphor Icons](https://www.figma.com/design/xZSksKpcQTp5H3C4dZApBL/Phosphor-Icons?node-id=7484-1322&t=5f3sI6AFFHMgcXfl-1) como procedencia obligatoria de todos los iconos (`DEC-ICONS-001`). La inspección read-only de `SRC-FIGMA-PHOSPHOR-001` confirmó por key que el `PlusCircle` activo de Button proviene de ese archivo. Esta decisión resuelve la fuente de iconos, no las variables remotas ni la aprobación integral.

## 2. Fuentes revisadas

| SRC | Ruta/URL | Tipo | Snapshot | Cobertura | Autoridad |
|---|---|---|---|---|---|
| SRC-FIGMA-BUTTON-001 | Figma `tj3WIBEZDGLVs7MJWKCwgf`, node `26:81` | Nodo Figma | [JSON](../../sources/figma-snapshots/button-26-81.snapshot.json) | 364/364 nodos; 60 variantes | Evidencia observacional, no aprobación |
| SRC-FIGMA-BUTTON-001-IMG | [PNG](../../sources/figma-snapshots/button-26-81.png) | Captura | SHA-256 `8b4a7c85f3ec9138a0588f8b922b676696d81f8ffb503d2cef3bb04ba7a4bd04` | 516×1883 completa | Corroboración visual |
| SRC-FIGMA-PHOSPHOR-001 | [Phosphor Icons](https://www.figma.com/design/xZSksKpcQTp5H3C4dZApBL/Phosphor-Icons?node-id=7484-1322&t=5f3sI6AFFHMgcXfl-1) | Biblioteca Figma | [JSON acotado](../../sources/figma-snapshots/phosphor-plus-circle.snapshot.json) | Página + PlusCircle y variante activa; no biblioteca completa | Fuente elegida por usuario; identidad verificada |
| FOUNDATIONS-TOKENS-001 | [Contrato aprobado](../../specs/foundations/foundations-tokens.contract.md) | Especificación local | 0.1.0 | Variables locales ya validadas | Normativa solo para variables aprobadas |

## 3. Matriz de evidencia

| Evidencia | Afirmación | Clase | Localizador | REQ |
|---|---|---|---|---|
| E-001 | El objetivo es un COMPONENT_SET `button` en `Page 1` | OBSERVED | `node:26:81` | REQ-BTN-001 |
| E-002 | Hay 4 tipos, 3 tamaños y 5 estados | OBSERVED | `variantGroupProperties` | REQ-BTN-001 |
| E-003 | El producto observado contiene 60 variantes | DERIVED | `4 × 3 × 5`; hijos directos | REQ-BTN-001 |
| E-004 | Cada variante expone dos iconos y texto | OBSERVED | subtree y property references | REQ-BTN-002/003 |
| E-005 | Ambos swaps activos usan PlusCircle Outline Light | OBSERVED | main component `26:3`, set `26:2` | REQ-BTN-005 |
| E-006 | Se usan 35 variables, sin estilos nombrados | OBSERVED + DERIVED | bindings deduplicados | REQ-BTN-004 |
| E-007 | Figma expone 23 reacciones parciales | OBSERVED | `reactions` | REQ-BTN-006 |
| E-008 | Dos destinos focus/default cambian middle/small a large | OBSERVED | `26:243`, `26:248` | REQ-BTN-006 |
| E-009 | Las keys de PlusCircle y Outline/Light coinciden con la biblioteca indicada por el usuario | EXPLICIT + OBSERVED | `DEC-ICONS-001`; `8899:53875`/`8899:53827` vs. `26:2`/`26:3` | REQ-BTN-009 |

## 4. Transformaciones realizadas

- Se normalizó `26-81` a `26:81`.
- Se recorrió el subárbol con hijos invisibles habilitados para lectura; no aparecieron nodos invisibles.
- Se agruparon instancias por componente principal y variables por ID/key.
- Se resolvieron valores efectivos y modos para una ruta de uso representativa de cada variable.
- Se derivaron conteos y matrices sin modificar la fuente.
- Se conservó la captura PNG recibida del endpoint de Figma y se calculó su SHA-256.

## 5. Requisitos y decisiones de adopción

| REQ | Regla propuesta | Adopción pendiente | AC |
|---|---|---|---|
| REQ-BTN-001 | Preservar ejes y 60 combinaciones | Sí | AC-BTN-001 |
| REQ-BTN-002 | Preservar propiedades nativas de texto/iconos | Sí | AC-BTN-002 |
| REQ-BTN-003 | Preservar anatomía y excepción focus/default | Sí | AC-BTN-003 |
| REQ-BTN-004 | Preservar layout, visuales y bindings | Sí | AC-BTN-004 |
| REQ-BTN-005 | Preservar defaults y swap activo | Sí | AC-BTN-005 |
| REQ-BTN-006 | No completar o corregir interacciones sin decisión | Sí | AC-BTN-006 |
| REQ-BTN-007 | Cumplir página por familia | Sí | AC-BTN-007 |
| REQ-BTN-008 | Mantener web fuera de alcance | Sí | AC-BTN-008 |
| REQ-BTN-009 | Consumir iconos únicamente de la biblioteca Phosphor Icons indicada | La fuente ya es decisión explícita; su cumplimiento en cualquier implementación requiere QA | AC-BTN-009 |

## 6. Conflictos

No se halló una contradicción entre dos fuentes normativas aprobadas. Sí existen hallazgos observados que impiden adoptar el nodo sin decisión:

| ID | Hallazgo | Impacto | Decisión |
|---|---|---|---|
| OBS-BTN-INT-001 | Focus default middle/small cambia a hover large | Riesgo de cambio de tamaño | Conservar como baseline o corregir en una revisión aprobada |
| OBS-BTN-INT-002 | Reacciones incompletas y asimétricas | No existe contrato conductual completo | Aprobar solo visuales o definir comportamiento |
| OBS-BTN-PAGE-001 | Set en `Page 1` | No cumple aún P04 §3 | Aprobar nombre y operación de página |
| OBS-BTN-DEPS-001 | 9 variables y PlusCircle son remotos | La fuente de PlusCircle está identificada y debe conservarse; la procedencia y política de las 9 variables remotas siguen pendientes | Resolver variables sin sustituir iconos Phosphor por copias |

## 7. Inferencias y propuestas no normativas

| PROP | Propuesta | Por qué no está demostrada | Confirmación |
|---|---|---|---|
| PROP-BTN-001 | Nombrar la página `Button` | Derivado del nombre del set, no decisión | Usuario |
| PROP-BTN-002 | Corregir destinos focus/default al mismo tamaño | Parece un defecto, pero cambia comportamiento | Usuario |
| PROP-BTN-003 | Completar el ciclo default/hover/press/focus | Figma no define el modelo completo | Producto/UX |
| PROP-BTN-004 | Sustituir variables remotas por locales equivalentes | Igualdad de nombre/valor no prueba equivalencia semántica | Usuario + fuente de biblioteca |

## 8. Preguntas y preparación por destino

| Q | Información faltante | Bloquea Figma | Bloquea web | Bloquea aprobación completa |
|---|---|---|---|---|
| Q-BTN-001 | ¿Se adopta el baseline observado o se corrigen las interacciones? | Sí, conducta | Sí | Sí para conducta; no para visuales acotados |
| Q-BTN-002 | ¿Cuál es el nombre canónico de la página de familia? | Sí | No | Sí para P04 completo |
| Q-BTN-003 | ¿Cómo se gestionan las 9 variables remotas? La fuente de iconos ya se decidió. | Sí, reproducibilidad | Sí | Sí para reconstrucción independiente |
| Q-BTN-004 | Propósito, semántica, teclado y accesibilidad | Parcial | Sí | Sí para contrato integral |
| Q-BTN-005 | ¿La operación posterior será VALIDATE_ONLY, UPDATE o MIGRATE? | Sí | No | Sí para P04 |

Preparación Figma: `BLOCKED`. Web: fuera de alcance y sin contrato.

## 9. Resultado de revisión documental

[QA-BUTTON-001](../../qa/contracts/button.review.md) ejecutó DOC-01–DOC-16. Resultado global `BLOCKED` para aprobación integral y `PASS` para presentar el candidato a revisión humana. Los bloqueos son declarados y acotados; no se ocultaron como `NOT_APPLICABLE`.

## 10. Estado final y entrega

`BUTTON-001` `0.1.0` queda `IN_REVIEW`. La aprobación está pendiente. P04, readback de implementación y `IMPLEMENTATION_REVIEW` no se ejecutaron porque el gate de aprobación no se cumple.

## 11. Historial

Primera síntesis de esta entidad. No se encontraron contratos previos de Button en `registry/contracts.md` ni `specs/`.

El 2026-09-23 UTC se revisó el candidato aún no aprobado para incorporar `DEC-ICONS-001` y el cotejo de keys de `SRC-FIGMA-PHOSPHOR-001`. Se conserva versión `0.1.0` porque sigue siendo el mismo candidato en revisión; cambian sus digests y QA documental.
