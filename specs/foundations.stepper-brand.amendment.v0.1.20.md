---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-STEPPER-COLORS-001
name: Stepper semantic colors by theme
type: foundations-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.20
last_updated: 2026-09-24
review_targets: [figma]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.stepper-colors.v0.1.1.json]
user_audit: PENDING
---

# Enmienda cromática de Stepper por tema

Sustituye íntegramente los datos de aliases de [Foundations 0.1.19](foundations.stepper-colors.amendment.v0.1.19.md) y su JSON 0.1.0, sin cambiar identidad, scope ni consumidores de los ocho roles. El [JSON 0.1.1](../drafts/foundations/ai-design-system.stepper-colors.v0.1.1.json) es la única definición vigente de nombre, descripción, scope, ID local y alias por modo. Cero variables y cero primitivas nuevas.

Por instrucción explícita del usuario, los acentos son de marca dependiente del tema, aun cuando esto se aparte del verde y azul fijos observados en la fuente. La elección concreta de marca **fuerte** para círculo y conector Checked y marca **base** para círculo Default es una normalización delegada de Codex, no una asignación dictada por el usuario; conserva jerarquía visual usando roles existentes. Cada rol específico de Stepper aliasa **directamente** la misma primitiva que usa el rol de marca correspondiente en Contable, Administrativo, Servicios y Personas. Los consumidores conservan su binding al rol de Stepper, no a la primitiva ni al rol genérico de marca. Inactive, conectores Default y textos mantienen sus neutros fuente.

La comprobación debe comparar en cada modo el alias de Stepper con el alias vigente de `color/brand/strong` o `color/brand/default`, además de scope y pinturas ligadas. Si Foundations cambia en el futuro su mapa de marca, los roles de Stepper deben actualizarse junto con ese cambio; su alias actual por modo no constituye un vínculo transitivo automático. La auditoría humana y la publicación de biblioteca siguen separadas.
