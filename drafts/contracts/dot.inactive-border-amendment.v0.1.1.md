---
contract_schema: sdd-project/0.2
contract_id: AMD-DOT-INACTIVE-BORDER-001
amends: DOT-001
base_version: 0.1.0
version: 0.1.1
status: DELEGATED_FOR_BUILD
last_updated: 2026-09-23
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.dot-inactive-border.v0.1.0.json]
---

# Dot · enmienda de contraste Inactive 0.1.1

Sustituye únicamente la regla de stroke de Type=Inactive en las secciones 7 y 10 y los criterios AC-DOT-004/006 de [DOT-001 0.1.0](dot.contract.v0.1.0.md). Todo lo demás permanece: 15 variantes, tamaños, fills, textos, propiedades, página y límites funcionales.

En Inactive Small/Medium/Large, el borde exterior de 1 px usa `color/border/status-inactive` (`STROKE_COLOR`) en lugar de `color/border/on-brand`. El nuevo rol aliasa `color/neutral/500` y se define en [JSON de extensión](../foundations/ai-design-system.dot-inactive-border.v0.1.0.json). El fondo pálido `color/background/status-inactive` no cambia. La comparación visual debe mostrar solo el contorno más oscuro de esas tres variantes.

La razón es el hallazgo de contraste 1.23:1 del conjunto Inactive original contra blanco. El borde neutral propuesto da 4.76:1 en los cuatro modos; no certifica accesibilidad integral del Dot, especialmente la tipografía numérica de 4/8 px. No se aplica a otros tipos ni se modifica el token global `color/border/on-brand`.
