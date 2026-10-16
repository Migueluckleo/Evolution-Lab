---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-METRIC-CARD-ROLES-001
name: Metric Card semantic color roles
type: foundations_amendment
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
sources: [SRC-FIGMA-METRIC-CARD-001, SRC-TOKENS-INV-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.metric-card-roles.v0.1.0.json]
user_audit: PENDING
---

# Enmienda Foundations · colores de Metric Card

## Decisión

Agregar exactamente dos variables locales a la colección semántica de AI Design System: `color/text/metric/trend` con scope exclusivo `TEXT_FILL` y `color/icon/metric/brand` con scope exclusivo `SHAPE_FILL`. El [JSON canónico](../foundations/ai-design-system.metric-card-roles.v0.1.0.json) gobierna nombres, descripciones, tipos, modos, aliases y scopes; Figma debe coincidir por lectura posterior. No se añaden primitivas ni se modifica el inventario histórico del origen.

## Motivo y alcance

La fuente usa `color/text/brand` para seis porcentajes y `color/icon/brand` para iconos en las ocho variantes. En Servicios, ambos resuelven a orange/500: contraste 3.24:1 sobre blanco y 2.95:1 sobre fondo sutil. Los otros tres modos superan 5:1 sobre sutil. El alias nuevo conserva blue/400, green/500 y purple/500, pero usa orange/700 en Servicios: 7.20:1 sobre blanco y 6.57:1 sobre sutil. Son roles distintos aunque compartan valores: un texto no puede consumir un token de icono ni un vector uno de texto.

## Propagación obligatoria

Crear las dos variables en Figma con aliases a las ocho referencias de primitivas declaradas en JSON, verificar los cuatro modos, y después vincular únicamente los porcentajes al rol text y los vectores visibles de CurrencyCircleDollar/ArrowUpRight al rol icon. Registrar IDs reales de destino en un estado separado, actualizar el contrato Metric Cards y auditar todas las pinturas visibles. La fuente permanece intacta.

## Criterios de aceptación

- JSON y Figma concuerdan en nombre, descripción, tipo, scope, colección y cuatro aliases de cada variable.
- Cada alias apunta a una primitiva existente en la colección del destino; no hay color literal nuevo.
- Texto de tendencia ≥4.5:1 e iconos ≥3:1 sobre ambos fondos en los cuatro modos.
- Cero usos fuera de categoría semántica o scope; no se presenta esta enmienda como aprobada por auditoría humana hasta revisión posterior.
