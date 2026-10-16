---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-BREADCRUMB-CURRENT-TEXT-001
name: Breadcrumb current text
type: foundations_amendment
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
sources: [SRC-TOKENS-INV-001, SRC-FIGMA-BREADCRUMBS-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.breadcrumb-current-text.v0.1.0.json]
user_audit: PENDING
---

# Enmienda Foundations · texto Current de Breadcrumb

## Necesidad y alcance

En el modo Servicios, `color/text/brand` resuelve a orange/500 y produce 3.24:1 sobre el fondo blanco de los Breadcrumbs, por debajo del umbral 4.5:1 para texto normal. La captura fuente usa ese color; su valor en los otros tres modos produce 5.56/5.93/6.32:1. Esta enmienda crea un solo rol semántico específico de **texto** para el segmento Current. No modifica `color/text/brand`, otros componentes ni primitivas.

## Datos canónicos delegados

El [JSON de destino](../foundations/ai-design-system.breadcrumb-current-text.v0.1.0.json) gobierna nombre, tipo, descripción única, scope, modos, aliases y codeSyntax. Los cuatro aliases son a primitivas locales existentes: blue/400, green/500, orange/700 y purple/500. El inventario histórico aprobado permanece idéntico. No se crea `usage` ni descripción paralela.

## Reglas

- Crear en colección `semantic`, scope exclusivo `TEXT_FILL`, resolvedType `COLOR`, codeSyntax vacío como indica JSON.
- Alias por modo a las cuatro primitivas del JSON; prohibido copiar valores RGB literales al rol.
- Consumidor autorizado: texto de la variante `State=Default, Current=true` de `Breadcrumb item` y sus cuatro instancias anidadas en `Breadcrumbs`. No usar en shapes, iconos o fondos.
- Validar que los cuatro modos resuelvan al alias previsto. Contraste sobre `color/background/default`: al menos 4.5:1 en los cuatro modos; Servicios debe resolver orange/700 (~7.20:1).
- No publicar hasta QA de variables y componente y auditoría humana posterior.

## Trazabilidad

Se aplica DEC-SEMANTIC-EXTENSIONS-001. La propuesta corrige un fallo contrastado sin cambiar la apariencia de Contable, Administrativo ni Personas. La desviación naranja se comunica al usuario antes de crear el rol. El estado `DELEGATED_FOR_BUILD` no equivale a aprobación humana.
