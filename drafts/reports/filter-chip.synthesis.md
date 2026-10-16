---
report_schema: sdd-project/0.2
report_type: CONTRACT_SYNTHESIS
report_id: SYN-FILTER-CHIP-001
contract_id: FILTER-CHIP-001
contract_version: 0.1.0
created_at: 2026-09-23T15:11:23Z
review_status: BLOCKED
---

# Reporte de síntesis · Filter Chip

## 1. Encargo y entregables

Se recibió una URL al nodo Figma `8203:10` y una confirmación genérica para continuar. Se aplicó el paso seguro del flujo SDD: inspección profunda de solo lectura y generación del candidato [filter-chip.contract.md](../contracts/filter-chip.contract.md) y su modelo [filter-chip.contract.yaml](../contracts/filter-chip.contract.yaml). No se escribió en Figma, no se construyó en `AI-Design-System` y no se generó frontend.

## 2. Fuentes revisadas

| SRC | Ruta/URL y nodo | Tipo | Snapshot | Digest | Cobertura | Autoridad |
|---|---|---|---|---|---|---|
| SRC-FIGMA-FILTER-CHIP-001 | Archivo `9zs5RMR8LB5wHjW9Bd59BA`, nodo `8203:10` | Figma read-only | `2026-09-23T15:11:23Z` | Snapshot `013be40…`; PNG `b39aa241…` | 145/145 nodos, 24 variantes, 48 instancias, 26 variables | Evidencia observacional, no aprobación |

Artefactos preservados: [snapshot JSON](../../sources/figma-snapshots/filter-chip-8203-10.snapshot.json) y [captura PNG](../../sources/figma-snapshots/filter-chip-8203-10.png).

## 3. Matriz de evidencia

| Evidencia | Afirmación | Clasificación | Localizador | REQ |
|---|---|---|---|---|
| E001–E002 | Identidad y contexto visual del set | OBSERVED | `node:8203:10`, screenshot | REQ-FC-001 |
| E004–E005 | Anatomía repetida y dependencia `PlusCircle` | OBSERVED | hijos e instancias | REQ-FC-002, REQ-FC-005 |
| E007 | Matriz observada de 24 variantes | OBSERVED | hijos directos del set | REQ-FC-001 |
| E009 | Ocho propiedades nativas y defaults | OBSERVED | `componentPropertyDefinitions` | REQ-FC-003 |
| E010 | 26 variables locales resueltas en modo Contable | OBSERVED | bindings + `resolveForConsumer` | REQ-FC-004 |
| D001 | Faltan 16 combinaciones del producto cartesiano | DERIVED | diferencia determinista entre ejes e hijos | REQ-FC-001 |
| R001–R003 | Producto, accesibilidad y web requieren definición | UNRESOLVED | ausencia de fuente aplicable | REQ-FC-006 |

## 4. Transformaciones realizadas

- Se normalizó `8203-10` a `8203:10`.
- Se recorrió explícitamente el subárbol, incluidos descendientes invisibles; no hubo truncamiento.
- Se agruparon 48 instancias por key de componente principal en una dependencia.
- Se consolidaron 26 variables usadas y cero estilos nombrados.
- Se proyectó un modelo normalizado único a Markdown y YAML.
- Se conservaron la fuente Figma y la evidencia visual sin modificar el documento.

## 5. Requisitos y decisiones de adopción

| REQ | Respaldo | Regla propuesta | Adopción pendiente | AC |
|---|---|---|---|---|
| REQ-FC-001 | E007, D001 | Limitarse a combinaciones observadas hasta resolver conflicto | Sí | AC-FC-001 |
| REQ-FC-002 | E005 | Preservar anatomía y orden | Sí | AC-FC-002 |
| REQ-FC-003 | E009 | Preservar propiedades nativas | Sí | AC-FC-003 |
| REQ-FC-004 | E010 | Preservar bindings semánticos | Sí | AC-FC-004 |
| REQ-FC-005 | E004 | Preservar dependencia activa | Sí | AC-FC-005 |
| REQ-FC-006 | E011, R002–R003 | No inventar conducta | Sí | AC-FC-006 |

## 6. Conflictos

| ID | Campos enfrentados | Regla | Impacto | Decisión necesaria |
|---|---|---|---|---|
| CONFLICT-FC-001 | Description vs component properties | Defaults de iconos `off` vs `true` | Default no determinista | Elegir default canónico de ambos booleanos |
| CONFLICT-FC-002 | Description vs eje Size | `Sm/Md/Xl` vs `x-small/small/middle/large` | Nombres/mapeo no deterministas | Confirmar vocabulario canónico y equivalencias |
| CONFLICT-FC-003 | Description vs hijos del set | Independencia Selected/State vs 16 combinaciones ausentes | Matriz no determinista | Confirmar si se crean, prohíben o excluyen las combinaciones |

## 7. Inferencias y propuestas no normativas

| PROP | Propuesta | Por qué no está demostrada | Confirmación |
|---|---|---|---|
| PROP-FC-001 | Tratar el chip como selección única dentro de un grupo | La description solo dice “switch between filters” | Producto |
| PROP-FC-002 | Usar `aria-pressed` o equivalente en web | Figma no define rol ni patrón de selección | Accesibilidad/web |
| PROP-FC-003 | Considerar los anchos como mínimos, no fijos | El layout es HUG, pero no hay regla de contenido largo | Diseño/producto |

## 8. Preguntas y preparación por destino

| Q | Información faltante | Bloquea Figma | Bloquea web | Bloquea aprobación |
|---|---|---:|---:|---:|
| Q-FC-001 | Defaults canónicos de iconos | Sí | Sí | Sí |
| Q-FC-002 | Vocabulario canónico de Size | Sí | Sí | Sí |
| Q-FC-003 | Matriz Selected × State | Sí | Sí | Sí |
| Q-FC-004 | Semántica, teclado y selección | No para evidencia visual; sí para conducta | Sí | No para un alcance exclusivamente visual tras resolver conflictos |

Preparación Figma: `CONFLICT`. Preparación web: `BLOCKED` y fuera de alcance.

## 9. Resultado de revisión documental

La revisión [QA-FILTER-CHIP-001](../../qa/contracts/filter-chip.review.md) verifica estructura y trazabilidad, pero el resultado global es `BLOCKED` por `DOC-09`: description, defaults y matriz de variantes no son coherentes. El candidato permanece `DRAFT`.

## 10. Estado final y entrega al usuario

Versión `0.1.0`, estado `DRAFT`. SHA-256 del Markdown candidato: `f7dd64cfcf072c3e02f5bb11e273894a2baeb9c12888a2e9accd521f73a6b13a`; YAML técnico: `af6918afb5ce050047c06153d9def42d9365efb3f2fbbee949f2845a2932632e`. La inspección técnica está completa y los inventarios reconcilian; aprobación y construcción están bloqueadas hasta resolver `CONFLICT-FC-001` a `003`.

## 11. Historial

Primera síntesis de `FILTER-CHIP-001`; no existen versiones aprobadas o implementaciones registradas. Graphify fue consultado como índice pero no actualizado; queda `STALE` respecto de estos nuevos artefactos.
