---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-DOT-INACTIVE-BORDER-001
name: Dot inactive border semantic role
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.5
last_updated: 2026-09-23
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.dot-inactive-border.v0.1.0.json]
---

# Foundations · borde Dot Inactive 0.1.5

Se añade un único rol `color/border/status-inactive`, `COLOR`, scope exclusivo `STROKE_COLOR`, con alias a la primitiva existente `color/neutral/500` en Contable, Administrativo, Servicios y Personas. El [JSON canónico](../foundations/ai-design-system.dot-inactive-border.v0.1.0.json) gobierna descripción, nombres, modos y aliases; no se edita el inventario fuente ni la extensión de fondos ya construida.

El único consumidor previsto son los strokes exteriores de las tres variantes Inactive de Dot. Su fondo `color/background/status-inactive` permanece neutral/300. El borde blanco de origen daba 1.23:1 contra blanco; neutral/500 alcanza 4.76:1. El cambio busca visibilidad con la menor desviación del centro pálido. No implica que Inactive equivalga a Disabled.

Se verifican ausencia previa del nombre, creación en colección `semantic`, un solo scope, cuatro aliases, ID real de Figma y readback de los tres consumidores. La biblioteca permanece sin publicar y la auditoría humana pendiente.
