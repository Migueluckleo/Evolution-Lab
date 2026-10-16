---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-NAVIGATION-TAB-BORDERS-001
name: Navigation Tab border colors
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.15
last_updated: 2026-09-24
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.navigation-tab-borders.v0.1.0.json]
decision_refs: [DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001, DEC-MIGRATION-VISUAL-FIDELITY-001]
---

# Foundations · bordes semánticos de Navigation Tab 0.1.15

La [extensión JSON](../drafts/foundations/ai-design-system.navigation-tab-borders.v0.1.0.json) define dos y solo dos roles `COLOR` en colección `semantic`, scope exclusivo `STROKE_COLOR`. `color/border/navigation-tab/subtle` referencia azul/200, verde/200, rojo/200 y morado/200 en los cuatro modos. `color/border/navigation-tab/disabled` referencia neutral/400 en todos los modos. Las primitivas ya existen en el inventario aprobado; no se agrega ni cambia ninguna.

La fuente aplica incorrectamente `color/text/disabled` a bordes Base Disabled y usa `color/border/subtle` en el contorno Off y en divisores, con Servicios `#FFBBB0`. El destino compartido `color/border/subtle` en Servicios resuelve `#FFD8C8`, por lo que un rol específico de Tab preserva la fuente sin alterar otros componentes. El borde Disabled actual del destino resuelve neutral/300, no neutral/400; el segundo rol evita usar un token de texto sobre un stroke.

Los dos roles ya se crearon y leyeron de vuelta desde Figma: `VariableID:309:122` y `VariableID:309:123`. El JSON guarda esos IDs reales y coincide en nombre, descripción, scope, `codeSyntax` y cuatro aliases. Los 107 paints auditados de Tab utilizan variables locales del rol correcto. La única descripción canónica por token vive en el JSON. Figma permanece `UNPUBLISHED` y la auditoría humana `PENDING`.
