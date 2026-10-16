---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-DOT-INACTIVE-BORDER-SOURCE-COLOR-002
name: Dot inactive border source color
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.6
last_updated: 2026-09-24
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.dot-inactive-border.v0.1.1.json]
decision_refs: [DEC-MIGRATION-VISUAL-FIDELITY-001, DEC-MIGRATION-CONTRAST-LIMITATIONS-001, DEC-MIGRATION-TRACEABILITY-001]
---

# Foundations · borde Dot Inactive, color de origen 0.1.6

Esta enmienda sustituye **solo los cuatro aliases** de `color/border/status-inactive` introducidos por [0.1.5](../../drafts/contracts/foundations.dot-inactive-border.amendment.v0.1.5.md): de `color/neutral/500` a la primitiva local existente `color/neutral/100` (`#FFFFFF`). El [JSON de override 0.1.1](../../drafts/foundations/ai-design-system.dot-inactive-border.v0.1.1.json) gobierna esos aliases y sustituye 0.1.0 únicamente en ese campo. La descripción canónica, nombre, tipo `COLOR`, `codeSyntax` y scope exclusivo `STROKE_COLOR` permanecen intactos. No se crea ni elimina variable.

La fuente Dot tiene borde blanco en Inactive Small/Medium/Large. El destino conserva el mismo rol semántico de borde inactivo y los tres bindings, pero su color vuelve al original por alias. La diferencia de contraste se registra como limitación `*`: el relleno `#E2E8F0` frente a blanco es aproximadamente 1.23:1; el borde blanco frente al lienzo blanco, 1:1. El dato 1.23:1 de la enmienda histórica corresponde al relleno, no al borde. No se declara conformidad WCAG.

`AC-TOK-DOT-001`: leer nombre, ID, descripción, scope y aliases en cuatro modos frente al JSON 0.1.1. `AC-TOK-DOT-002`: comprobar los tres strokes Dot Inactive `#FFFFFF`, con binding intacto y sin cambio de las otras doce variantes. `AC-TOK-DOT-003`: revisar consumidores anidados de Dot y marcar la limitación en la auditoría por excepciones. La biblioteca sigue sin publicar y la auditoría humana pendiente.
