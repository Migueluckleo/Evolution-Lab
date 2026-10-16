---
amendment_id: AMD-AVATAR-SOURCE-COLOR-002
status: DELEGATED_FOR_BUILD
applies_to: AVATAR-001
base_contract_version: 0.1.0
base_contract_digest_sha256: 465296694978a14e8019b2f52af61f42b88f78fecfa480d0081d4f877e122396
version: 0.1.1
supersedes_scope: AVATAR-001 only for fallback color Servicios and related contrast claim
foundation_dependency: drafts/contracts/foundations.avatar-fallback-source-color.amendment.v0.1.11.md
last_updated: 2026-09-24
user_audit: PENDING
---

# Avatar · fallback Servicios fiel a la fuente 0.1.1

Las doce variantes de Avatar y sus roles semánticos permanecen. En Servicios, las ocho variantes Icon/Text resuelven el fondo `color/background/avatar-fallback` a `color/orange/500` `#FF5300` mediante la [enmienda Foundations 0.1.11](foundations.avatar-fallback-source-color.amendment.v0.1.11.md), no a orange/600. El componente fuente usa la misma primitiva en el rol interactivo de origen; el destino conserva su rol correcto de fondo no interactivo `FRAME_FILL`.

Las cuatro variantes Image, el icono blanco, las iniciales blancas, el stroke, los Dot anidados y los modos Contable/Administrativo/Personas no cambian. Los tamaños de iniciales Small/Medium siguen normalizados a 10/12 px conforme al contrato base; la fuente mide 6/9 px y esta diferencia se registra por separado para auditoría. `AC-AVA-008`: readback de 12 variantes y todos los fondos/iconos/textos/Dot por modo, con RGB fuente para el fondo. `AC-AVA-009`: el fondo conserva binding semántico, alias JSON y scope correctos; contraste Servicios `*`, sin recoloración adicional ni afirmación WCAG. Auditoría humana pendiente, set sin publicar.
