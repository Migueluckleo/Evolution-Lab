---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-LINEAR-PROGRESS-COLORS-001
name: Linear Progress Bar semantic background roles
type: foundations_amendment
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
sources: [SRC-FIGMA-LINEAR-PROGRESS-BAR-001, SRC-TOKENS-INV-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.linear-progress-colors.v0.1.0.json]
user_audit: PENDING
---

# Enmienda Foundations · colores de Linear Progress Bar

## Decisión

Agregar exactamente cinco variables a la colección semántica local, todas con scope exclusivo `FRAME_FILL`: pista y cuatro tonos de tramo avanzado. El [JSON canónico](../foundations/ai-design-system.linear-progress-colors.v0.1.0.json) gobierna nombres, descripciones, tipos, modos, aliases y scopes. No se agregan primitivas ni se altera el inventario histórico del origen.

## Justificación

La pista fuente es el literal neutral/200. Primary usa un rol de marca genérico y los otros tres fondos usan roles `feedback/*/icon`; esos bindings son incompatibles con la categoría fondo estricta del destino. Los cuatro colores de barra fuente ya existen como primitivas locales. Primary conserva blue/400, green/500 y purple/500 según modo. En Servicios se elige orange/600 en vez de orange/500: sobre neutral/200, la relación pasa de 2.95:1 a 4.31:1. Warning amber/600, Positive emerald/600 y Danger red/600 conservan el tono observado y superan 3:1 sobre la pista.

## Propagación

Crear las cinco variables en Figma, leer nombre/description/tipo/scope/colección/aliases de vuelta, actualizar el contrato de familia y vincular 48 pistas y 48 barras solo a roles `color/background/progress/*`. El JSON registra las primitivas; los IDs semánticos reales de Figma viven en un estado de implementación separado. Ningún cambio se publica antes de auditoría humana.

## Aceptación

- Paridad JSON/Figma exacta en cinco roles y cuatro modos.
- Cada alias apunta a primitiva COLOR preexistente de AI Design System.
- 48 pistas y 48 barras con variable local de fondo y scope `FRAME_FILL`; cero colores literales visibles.
- Diferencia visual de Servicios y corrección de porcentaje visible documentadas en QA, sin inferir comportamiento web.
