# QA-DOT-FIGMA-001 · hallazgo antes de corrección

- **Resultado:** `FAIL` histórico para contraste no textual de Inactive sobre blanco; no invalida estructura ni bindings.
- **Lectura:** 15 variantes, 38 paints ligados, 60 radios, 60 lados de stroke, 28 dimensiones tokenizadas, seis textos editables y cero problemas de scope/categoría. Captura destino 685×613 visualmente cercana a la fuente.
- **Hallazgo:** Inactive Small/Medium/Large conservaban centro neutral/300 y borde exterior blanco de la fuente; contraste máximo perceptible contra blanco 1.23:1. Active 4.93:1 y Busy/Count 5.53:1.
- **Acción acotada:** nueva variable `color/border/status-inactive` alias neutral/500, scope `STROKE_COLOR`, vinculada solo a los tres bordes; mantener fills y geometría. Enmienda [0.1.1](../../drafts/contracts/dot.inactive-border-amendment.v0.1.1.md) y QA posterior requeridos.
