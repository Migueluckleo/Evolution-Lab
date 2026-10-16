---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-NAVIGATION-PAGINATION-BORDER-001
name: Navigation pagination subtle border color
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.14
last_updated: 2026-09-24
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.navigation-pagination-border.v0.1.0.json]
decision_refs: [DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001, DEC-MIGRATION-VISUAL-FIDELITY-001]
---

# Foundations · borde sutil de Pagination 0.1.14

La [extensión JSON](../drafts/foundations/ai-design-system.navigation-pagination-border.v0.1.0.json) define un único rol `color/border/pagination/subtle`, `COLOR`, colección `semantic`, scope exclusivo `STROKE_COLOR`. Conserva los aliases azul/200 en Contable, verde/200 en Administrativo, rojo/200 en Servicios y morado/200 en Personas, todas primitivas aprobadas. La única `description` editable del token vive en el JSON.

La lectura fuente→destino encontró una diferencia precisa en `color/border/subtle` para Servicios: fuente `#FFBBB0`, destino compartido `#FFD8C8`; los otros tres modos coinciden. Crear este rol específico evita cambiar globalmente otros consumidores y mantiene la fidelidad del borde de Pagination. No se crea primitiva ni se recolorea otro componente.

La variable local fue creada y leída de vuelta: `VariableID:290:122`, colección semántica, scope `STROKE_COLOR` y cuatro aliases a las primitivas anteriores. El JSON registra ese ID real. Los 125 paints de Pagination están ligados a variables con categoría y scope correctos. Figma permanece `UNPUBLISHED`, auditoría humana `PENDING`.
