---
report_schema: sdd-project/0.2
report_type: CONTRACT_SYNTHESIS
report_id: SYN-TOKENS-001
contract_id: FOUNDATIONS-TOKENS-001
contract_version: 0.1.0
created_at: 2026-09-22
review_status: REVIEWED_PENDING_APPROVAL
---

# Síntesis de foundations/tokens

## 1. Encargo y entregables

Ante “Empecemos por esto” y la entrega de dos archivos de tokens, se ingestaron originales, se contrastó la auditoría con el JSON recibido, se redactó el [contrato candidato](../contracts/foundations-tokens.contract.md) y se ejecutó [QA documental](../../qa/contracts/foundations-tokens.review.md). Esta tarea no escribió Figma, no generó frontend, no instaló herramientas, no regeneró Graphify y no modificó el JSON entregado.

## 2. Fuentes revisadas

| SRC | Ruta | Tipo | Snapshot | SHA-256 de bytes | Cobertura | Autoridad |
|---|---|---|---|---|---|---|
| SRC-TOKENS-INV-001 | [Inventario](../../sources/inventories/tokens.inventory.json) | JSON | Copia idéntica del recibido 2026-09-22 | `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474` | Todas las colecciones, variables, campos y valores recorridos | Evidencia, no aprobado |
| SRC-TOKENS-AUD-001 | [Auditoría](../../sources/audits/tokens.audit.md) | Markdown | Copia idéntica del recibido 2026-09-22 | `5882f1b4be20ce0e038ec9ccdec262a54af2e749b633f52da7d21451a4ac15e3` | 233 líneas | Informe, no aprobación |

La auditoría afirma inspecciones de Figma. Este trabajo solo contrastó el informe con el JSON; no leyó Figma ni la versión anterior `tokens.inventory.enriched.json`.

## 3. Matriz de evidencia

| Evidencia | Afirmación | Clase | Localizador | Alcance | REQ |
|---|---|---|---|---|---|
| E-TOK-001 | Dos colecciones; 141 variables `primitive`, 129 `semantic`; modos e IDs indicados en el contrato | EXPLICIT + DERIVED (conteo) | `SRC-TOKENS-INV-001`, `/collections` | Archivo recibido | REQ-TOK-001 |
| E-TOK-002 | 512 entradas `VARIABLE_ALIAS`, 145 literales, cobertura completa; no referencias rotas, ciclos ni tipos incompatibles según recorrido | DERIVED | `SRC-TOKENS-INV-001`, `/collections/*/variables/*/valuesByMode` | Archivo recibido | REQ-TOK-002 |
| E-TOK-003 | 270 descripciones no vacías y 270 objetos `codeSyntax` vacíos | DERIVED | `SRC-TOKENS-INV-001`, `/collections/*/variables/*` | Archivo recibido | REQ-TOK-003 |
| E-TOK-004 | Auditoría y JSON recibido corresponden en estado final | DERIVED | `SRC-TOKENS-AUD-001`, “SHA-256 de serialización canónica”; JSON completo | Hash canónico `d64892320747c12a82a92df684aa42464646914f8a93392c61abde630b96fb7e` calculado sobre este JSON | REQ-TOK-001–003 |
| E-TOK-005 | Ajustes listados aparecen en el JSON actual | EXPLICIT + DERIVED | Auditoría “Ajustes realizados”; variables por ID en JSON | Estado actual, no diff histórico | REQ-TOK-003 |
| E-TOK-006 | Archivo destino distinto del `fileKey` del inventario | EXPLICIT | JSON `/fileKey`; [AGENTS.md](../../AGENTS.md) “Destino de reconstrucción” | Separación origen/destino | REQ-TOK-005 |

## 4. Transformaciones realizadas

Se copiaron los dos archivos byte por byte y se verificaron con `cmp` y SHA-256. El JSON se parseó completo; se contaron colecciones, variables, tipos, modos, campos, aliases y literales. Se recorrieron todos los enlaces para revisar IDs faltantes, ciclos y `resolvedType`. Se calculó el SHA-256 de una serialización JSON canónica (`sort_keys=True`, separadores compactos, UTF-8 sin escape ASCII), que coincide con el valor “después de correcciones” de la auditoría. El hash canónico no es el SHA-256 de bytes de la fuente. No se ejecutó ninguna corrección adicional ni se normalizaron scopes.

## 5. Requisitos y adopción

| REQ | Respaldo | Regla propuesta | Adopción pendiente | AC |
|---|---|---|---|---|
| REQ-TOK-001 | E-TOK-001 | Preservar colecciones, modos, identidades lógicas, nombres y tipos | Sí | AC-TOK-001 |
| REQ-TOK-002 | E-TOK-002 + AGENTS.md | Preservar valores y grafo de aliases | Sí | AC-TOK-002 |
| REQ-TOK-003 | E-TOK-003 + AGENTS.md | Preservar `description`, scopes y `codeSyntax` | Sí | AC-TOK-003 |
| REQ-TOK-004 | P05/P06 | Mapear IDs de origen/destino reales | Sí | AC-TOK-004 |
| REQ-TOK-005 | E-TOK-006 + P04 | Reconstruir solo en el archivo destino acordado tras aprobación | Sí | AC-TOK-005 |

## 6. Conflictos

No se identificó contradicción entre el estado final del JSON y las afirmaciones verificables de estado final de la auditoría. El nombre `tokens.inventory.corrected.json` usado por la auditoría difiere del nombre del adjunto, pero el hash canónico coincide. Los dos `fileKey` cumplen roles distintos. La ausencia del inventario previo impide verificar el cambio histórico, no invalida el contenido actual. No se encontró aprobación explícita de la versión recibida.

## 7. Inferencias no normativas

No se propone completar `codeSyntax`, normalizar los scopes conservados, reinterpretar `logo/categoria`, inventar opacidad o asignar unidades CSS. Esos movimientos requerirían fuentes o decisiones adicionales. Las motivaciones históricas de la auditoría se citan como afirmaciones del informe, no como inspección propia.

## 8. Preguntas y preparación por destino

| Q | Información faltante | Bloquea Figma | Bloquea web | Bloquea aprobación del alcance actual | Fuente/decisión requerida |
|---|---|---|---|---|---|
| Q-TOK-001 | ¿Se aprueba este contrato 0.1.0 y el JSON de SHA-256 indicado como baseline canónico para reconstrucción en Figma? | Sí | No aplica a esta fase | Sí | Decisión explícita del usuario sobre versión y alcance |
| Q-TOK-002 | Estado y capacidades de escritura/lectura reales del destino Figma | Sí, antes de construir/validar | No | No para aprobar el contrato | Verificación P01/P04 cuando se autorice implementación |
| Q-TOK-003 | Nombres, unidades y conversiones de plataforma web | No en el alcance Figma propuesto | Sí | No | Contrato web futuro |
| Q-TOK-004 | Versión anterior y evidencia independiente de inspección Figma para auditar los “antes” del informe | No para adoptar el estado final como baseline, si el usuario lo aprueba | No | No, salvo que se exija verificación histórica | Fuente anterior o inspección autorizada |

**Preparación:** Figma `BLOCKED` por falta de aprobación y preflight del destino. Web fuera de alcance. Ninguna implementación ha comenzado.

## 9. Resultado de QA documental

[QA-TOKENS-001](../../qa/contracts/foundations-tokens.review.md): controles documentales aplicables revisados; no se presenta como aprobación ni como QA de implementación. Las preguntas anteriores siguen abiertas.

## 10. Estado final

Contrato `FOUNDATIONS-TOKENS-001` versión `0.1.0`, `IN_REVIEW`; SHA-256 de bytes del candidato: `e89ddaf95e1ee07998fa851c50ef9787b4ec3f9072e0c1ea44e07eb3e298e1da`. Inventario vinculado: `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`. Aprobación humana pendiente. No existe versión publicada en `specs/`.

## 11. Historial

Primer candidato; no hay revisión previa de esta identidad lógica ni decisión de sustitución registrada.
