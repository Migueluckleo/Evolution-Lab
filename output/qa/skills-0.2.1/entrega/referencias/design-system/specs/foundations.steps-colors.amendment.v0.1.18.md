---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-STEPS-COLORS-001
name: Steps semantic colors
type: foundations-amendment
status: SUPERSEDED
version: 0.1.18
last_updated: 2026-09-24
review_targets: [figma]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.steps-colors.v0.1.0.json]
user_audit: PENDING
---

# Enmienda cromática de Steps

**Histórica:** [Foundations 0.1.21](foundations.steps-brand.amendment.v0.1.21.md) y el JSON 0.1.1 sustituyen estos aliases fijos por el mapeo vigente por tema.

Esta extensión añade siete roles semánticos a AI Design System y **ninguna primitiva**. El [JSON de extensión](../drafts/foundations/ai-design-system.steps-colors.v0.1.0.json) gobierna nombres, descripciones, scopes, IDs de destino, aliases y cuatro modos; el inventario aprobado conserva los valores primitivos. Las formas de punto usan exclusivamente `SHAPE_FILL`; el contador usa exclusivamente `TEXT_FILL`. La variable semántica, no la primitiva, debe estar vinculada al consumidor visible.

El azul y el gris de `On White` coinciden exactamente con primitivas existentes. Las diferencias para `On Primary` y para el contador se aceptan como aproximación autorizada bajo [la enmienda transversal vigente](MIGRATION-TOKEN-TRACEABILITY.amendment.v0.1.2.md), con ΔE76 y RGB fuente registrados en JSON. Dos roles `legacy-gallery` conservan la contradicción de la variante pública histórica; no son paleta general ni sustituyen el contexto primario coherente del subcomponente.

La implementación debe demostrar paridad de las siete variables en los cuatro modos, ninguna primitiva nueva, cero binding directo a primitiva en los dots, y ausencia de uso de tokens `text` en formas o `shape` en texto. La aceptación humana y publicación de biblioteca permanecen pendientes.
