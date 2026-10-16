# QA-CHART-COLORS-FIGMA-001

- **Resultado:** `PASS` técnico para creación, lectura posterior y consumidores de siete variables; auditoría humana `PENDING`.
- **Paridad JSON/Figma:** nombres, descripciones, tipo `COLOR`, colección `semantic`, scopes y cuatro aliases por variable coinciden exactamente con el [JSON canónico](../../drafts/foundations/ai-design-system.chart-colors.v0.1.0.json).
- **Scopes:** `color/background/chart/bar` solo `FRAME_FILL`; las seis variables `color/shape/chart/*` solo `SHAPE_FILL`.
- **Primitivas:** los dieciséis IDs distintos referenciados existen en la colección primitiva de AI Design System y son de tipo COLOR; no se creó ningún valor cromático nuevo.
- **Consumidores:** 12 barras `FRAME_FILL`, ocho shapes de avance, seis de pista, un swatch por cada una de las tres series de Header y cuatro swatches neutros principales: 33 paints ligados a roles nuevos, cuatro de ellos en swatches ocultos por propiedad, sin cruce de categoría o scope. La auditoría de Charts cubre los 76 paints ligados de la página, 72 visibles por defecto. El texto de la variable Track se aclaró para incluir su swatch de leyenda; JSON y Figma quedaron iguales por segunda lectura.
