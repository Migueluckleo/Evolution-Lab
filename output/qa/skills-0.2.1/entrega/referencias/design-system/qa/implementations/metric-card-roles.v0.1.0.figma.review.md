# QA-METRIC-CARD-ROLES-FIGMA-001

- **Resultado:** `PASS` técnico para la creación, readback y consumidores de las dos variables; auditoría humana `PENDING`.
- **Identidad:** colección semántica local de AI Design System. `color/text/metric/trend` → `VariableID:200:122`, scope solo `TEXT_FILL`; `color/icon/metric/brand` → `VariableID:200:123`, scope solo `SHAPE_FILL`.
- **Paridad JSON/Figma:** coincidencia exacta de nombres, descripciones, tipo COLOR, colección, `codeSyntax` vacío, scopes y cuatro aliases por variable. Las primitivas blue/400, green/500, orange/700 y purple/500 ya existían; no se creó ninguna primitiva.
- **Contraste:** mínimo 5.07:1 sobre fondo sutil y 5.56:1 sobre blanco entre los cuatro modos. El valor naranja original de 2.95:1 sobre sutil se sustituye solo para estos roles.
- **Consumidores verificados:** cuatro textos Trend usan solo el rol `TEXT_FILL` y 16 vectores CurrencyCircleDollar/ArrowUpRight solo el rol `SHAPE_FILL`; cero errores de categoría o scope en las ocho variantes. [QA de Metric Cards](metric-card.v0.1.0.figma.review.md).
