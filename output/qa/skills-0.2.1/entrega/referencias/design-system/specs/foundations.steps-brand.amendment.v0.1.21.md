---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-STEPS-COLORS-001
name: Steps semantic colors by theme
type: foundations-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.21
last_updated: 2026-09-24
review_targets: [figma]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.steps-colors.v0.1.1.json]
user_audit: PENDING
---

# Enmienda cromática de Steps por tema

Sustituye los aliases de [Foundations 0.1.18](foundations.steps-colors.amendment.v0.1.18.md) mediante el [JSON 0.1.1](../drafts/foundations/ai-design-system.steps-colors.v0.1.1.json), única definición vigente de nombres, IDs locales, descripciones, scopes y alias por modo para los siete roles. No se crean variables ni primitivas.

La instrucción explícita del usuario exige que los acentos de Steps respondan al color de marca del tema. Por criterio delegado, el punto seleccionado `On White` sigue `color/brand/default`, mientras los dos acentos azul/300 observados en `On Primary` siguen el nivel 300 de la familia cromática de cada tema (azul, verde, naranja, morado). Los roles de Steps aliasan **directamente** las primitivas locales correspondientes; sus consumidores permanecen ligados a los roles específicos, no a las primitivas. Los puntos blancos, grises y el texto de contador no cambian. La diferencia entre Gallery pública y `.Dot` contextual sigue documentada; esta enmienda no unifica sus usos.

Verificar en cada modo siete variables y sus scopes, los 28 aliases del JSON, la equivalencia del punto `On White` seleccionado con `color/brand/default`, el nivel 300 de los dos roles contextuales y los bindings de todas las variantes. Si Foundations cambia el mapa de marca en el futuro, actualizar y revalidar estos aliases directos; no se propagan transitivamente. La auditoría humana y la publicación de biblioteca siguen pendientes.
