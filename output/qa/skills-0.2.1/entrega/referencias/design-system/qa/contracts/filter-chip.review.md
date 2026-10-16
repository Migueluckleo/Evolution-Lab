---
qa_schema: sdd-project/0.2
qa_id: QA-FILTER-CHIP-001
review_type: CONTRACT_REVIEW
contract_ref: drafts/contracts/filter-chip.contract.md
contract_version: 0.1.0
contract_digest: f7dd64cfcf072c3e02f5bb11e273894a2baeb9c12888a2e9accd521f73a6b13a
data_refs: [drafts/contracts/filter-chip.contract.yaml]
implementation_ref: null
target: figma
scope: FILTER-CHIP-001 candidate and normalized YAML
reviewer: Codex
executed_at: 2026-09-23T15:11:23Z
result: BLOCKED
---

# QA documental · Filter Chip 0.1.0

## Resultado

`BLOCKED`. La cobertura técnica y trazabilidad son suficientes para conservar un borrador, pero tres contradicciones de la fuente impiden promoverlo a `IN_REVIEW` o construirlo.

| Control | Resultado | Evidencia | Nota |
|---|---|---|---|
| DOC-01 | PASS | Set `Filter Chip` y plantilla de componente | El tipo corresponde al contenido. |
| DOC-02 | PASS | Frontmatter, tablas, JSON y YAML validados | Formatos legibles; digest se completa tras validación final. |
| DOC-03 | PASS | Identidad, versión, fuente y dependencia declaradas | No se inventó owner ni paquete web. |
| DOC-04 | PASS | REQ-FC-001–006 con procedencia | Cada candidato enlaza evidencia o ausencia explícita. |
| DOC-05 | PASS | Etiquetas Observed/Derived/Requires definition | Observación, derivación y faltantes están separados. |
| DOC-06 | PASS | Comparación contra fuente real | No se copiaron decisiones de Button. |
| DOC-07 | PASS | 26/26 variables resueltas | IDs, keys, colección, modo y valores conservados. |
| DOC-08 | NOT_APPLICABLE | No se crean descripciones de tokens | El contrato referencia nombres y bindings, no duplica `description`. |
| DOC-09 | BLOCKED | CONFLICT-FC-001–003 | Description contradice defaults, tamaños y matriz observada. |
| DOC-10 | PASS | Tablas de tamaños y bindings | Literales se presentan como valores resueltos u observados. |
| DOC-11 | BLOCKED | Defaults booleanos y combinaciones | No puede certificarse coherencia hasta decisión humana. |
| DOC-12 | PASS | Sección Design ↔ Code | Web queda `UNRESOLVED`; no se promete equivalencia. |
| DOC-13 | PASS | AC-FC-001–006 | Todos los REQ tienen criterio verificable. |
| DOC-14 | PASS | Figma read-only; snapshots preservados | No hubo mutaciones. |
| DOC-15 | PASS | Estado `DRAFT` | Aprobación explícitamente pendiente. |
| DOC-16 | PASS | Preguntas por destino en síntesis | Figma en `CONFLICT`; web `BLOCKED`. |

## Reconciliación del modelo técnico

- Traversal: `145 inspected + 0 pending = 145 discovered` — PASS.
- Componentes: 1 dependencia, 48 instancias, 1 remota y resuelta — PASS.
- Variables: 26 dependencias, 26 locales, 26 resueltas, todas con `used_by` — PASS.
- Estilos: 0 dependencias — PASS.
- Variantes: 24 hijos directos; 20 no seleccionadas + 4 seleccionadas Default — PASS como observación.
- Interacciones: 0 reacciones; estado `UNDEFINED` — PASS.
- Markdown/YAML: misma identidad, conteos, propiedades, conflictos y límites — PASS.

## Elementos bloqueados

1. `CONFLICT-FC-001`: defaults de visibilidad de iconos.
2. `CONFLICT-FC-002`: vocabulario del eje Size.
3. `CONFLICT-FC-003`: combinaciones `Selected=true` con estados no Default.

No se ejecutó `IMPLEMENTATION_REVIEW`; no existe implementación autorizada para este contrato.
