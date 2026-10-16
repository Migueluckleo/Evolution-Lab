---
contract_schema: sdd-project/0.2
contract_id: SCROLLBAR-001
name: Scrollbar color approximation
type: component-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.1
supersedes: [SCROLLBAR-001/0.1.0/AC-SB-003, FOUNDATIONS-SCROLLBAR-COLORS-001/0.1.16]
decision_refs: [DEC-MIGRATION-NEAREST-PRIMITIVE-001]
data_refs: [drafts/foundations/ai-design-system.scrollbar-colors.v0.1.1.json]
last_updated: 2026-09-24
user_audit: PENDING
---

# Scrollbar 0.1.1 · aproximación cromática autorizada

La instrucción posterior del usuario cambia únicamente el color de destino de [Scrollbar 0.1.0](scrollbar.contract.v0.1.0.md) y la extensión de Foundations vinculada. La fuente conserva el fill literal `#C3C6D4`. El destino debe consumir el rol `color/background/scrollbar/thumb` con scope `SHAPE_FILL`, aliasado en cuatro modos a la primitiva existente `color/neutral/300` `#E2E8F0`; no aplicar la primitiva directamente a los 30 rectángulos. Se conserva el ID del rol semántico y las 30 conexiones de componentes. La única `description` vigente del rol vive en el [JSON 0.1.1](../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.1.json).

La selección se basa en comparación CIELAB ΔE76 de primitivas locales: neutral/300 12.24 frente a neutral/400 14.73 y otras alternativas más distantes. `#E2E8F0` es notablemente más claro que la fuente; no se declara fidelidad cromática ni conformidad de contraste. La primitiva nueva `color/neutral/350` de 0.1.0 se elimina solo después de verificar que no tenga aliases ni consumidores directos. El [JSON 0.1.0](../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.0.json) y [QA previo](../qa/implementations/scrollbar-colors.v0.1.0.figma.review.md) quedan como historia, no como estado actual.

**Aceptación acotada:** cuatro aliases semánticos a neutral/300, descripción y scope sincronizados entre JSON y Figma; 30/30 thumbs conservan binding al rol semántico; cero uso directo de primitiva en shapes; captura y ratio sobre blanco medidos de nuevo. Geometría, variantes, propiedades y decisión nominal `75%` del contrato base no cambian. La auditoría humana continúa `PENDING` y Figma `UNPUBLISHED`.
