---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-SCROLLBAR-COLORS-001
name: Scrollbar thumb color
type: foundation-amendment
status: SUPERSEDED
version: 0.1.16
last_updated: 2026-09-24
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.scrollbar-colors.v0.1.0.json]
decision_refs: [DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001, DEC-MIGRATION-VISUAL-FIDELITY-001, DEC-MIGRATION-MISSING-PRIMITIVE-001]
---

# Foundations · color del thumb de Scrollbar 0.1.16

**Estado histórico:** sustituido por [Foundations 0.1.17](foundations.scrollbar-colors.amendment.v0.1.17.md), que usa una primitiva existente conforme a la instrucción posterior del usuario. Este documento no describe el alias actual de Figma.

La [extensión JSON](../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.0.json) define una primitiva local `color/neutral/350` igual al único fill observado en los 30 thumbs de la fuente: `#C3C6D4`. Ninguna primitiva existente en el Figma destino reproduce ese RGB. La primitiva no tiene scope de uso de interfaz; el rol `color/background/scrollbar/thumb` la referencia por alias en Contable, Administrativo, Servicios y Personas, con scope `SHAPE_FILL` para el rectángulo.

El inventario histórico aprobado permanece inalterado. La extensión se almacena aparte; las variables locales se crearon y leyeron de vuelta en AI Design System: primitiva `VariableID:327:122` y rol semántico `VariableID:327:123`. Sus descripciones canónicas solo están en el JSON, no aquí. No se sustituyen colores por criterio de contraste, ni se afectan consumidores compartidos. El contrato de Scrollbar gobierna la aplicación y el QA posterior comprobará 30 consumidores, scopes, modos, aliases y RGB.
