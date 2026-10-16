---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-CHART-COLORS-001
name: Chart semantic color roles
type: foundations_amendment
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
sources: [SRC-FIGMA-CHART-001, SRC-TOKENS-INV-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.chart-colors.v0.1.0.json]
user_audit: PENDING
---

# Enmienda Foundations · colores de Charts

## Decisión

Agregar exactamente siete variables locales a la colección `semantic` de AI Design System. El [JSON canónico](../foundations/ai-design-system.chart-colors.v0.1.0.json) gobierna sus nombres, descripciones, tipos, cuatro modos, aliases y scopes. No se alteran las primitivas ni el inventario histórico de la fuente.

## Motivo y semántica

En la fuente, formas de datos y swatches consumen roles genéricos de marca, interactivo o incluso icono. Estos roles nuevos expresan el uso de Charts sin tomar categorías ajenas: `color/background/chart/bar` admite solo `FRAME_FILL`; los seis `color/shape/chart/*` admiten solo `SHAPE_FILL`. El track de fondo lineal reutiliza `color/background/muted`, mientras que el borde discontinuo del Chart Cell reutiliza `color/border/accent`, ambos con categoría y scope correctos.

Los aliases por modo conservan la familia cromática original. El swatch neutro sin serie definida cambia del gris literal claro a `neutral/500` para hacerse visible. La segunda serie deja el azul pastel original y toma acentos medios por modo; es una desviación visual mínima documentada para distinguirla sobre blanco. Los roles de avance y tramo restante, incluido su swatch de leyenda, usan dos tonos de la misma familia y nunca codifican por sí solos éxito o fracaso.

## Propagación obligatoria

Crear las siete variables en Figma con los aliases exactos del JSON y verificar su lectura posterior. Registrar sus IDs locales separados del JSON canónico. Actualizar los contratos y construir las cinco piezas de Charts, usando cada rol solo en capas de su categoría. Auditar bindings y contraste observable por modo; no declarar accesibilidad integral de las visualizaciones sin revisar su contexto y la codificación no cromática.

## Criterios de aceptación

- Coincidencia JSON/Figma de nombre, descripción, tipo, colección, scope y cuatro aliases por variable.
- Cero primitivas nuevas y cero bindings de texto, icono, fondo o forma en otra categoría semántica.
- Cero colores literales en las capas visibles reconstruidas; todo swatch y segmento usa variables locales.
- Las variantes y dependencias reales del origen se mantienen; las diferencias visuales se registran para auditoría humana posterior.
