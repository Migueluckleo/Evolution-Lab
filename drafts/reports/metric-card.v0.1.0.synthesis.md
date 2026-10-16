# Síntesis · Metric Cards 0.1.0

- **Origen:** [Card/Metric fuente](../contracts/metric-card.source.component-contract.md) y su YAML, ocho variantes completas. La página fuente `❖ Cards ✅` es solo lectura.
- **Decisión delegada:** página destino `Metric Cards`, set `Metric Card` con los ocho cruces observados. Se preservan fondo, borde, jerarquía, iconos y disposición. Se añaden propiedades de texto para valores y tendencia; no se inventan interacciones.
- **Foundations:** `color/text/metric/trend` y `color/icon/metric/brand` son roles separados y ya coinciden JSON/Figma en cuatro modos. Servicios cambia orange/500→orange/700 para contraste; no hay nuevas primitivas.
- **Desviación tipográfica:** One Metric V1 Small pasa Title 18→20 px con `font/size/lg` existente. V1 Large/Small aumenta cinco píxeles de alto para alojar Trend con line-height semántico de 20 px. Horizontal Small mantiene importe 20 px. Horizontal conserva su ejemplo `$123,320.00` con propiedades de valor separadas de Vertical.
- **Autoridad:** [contrato destino](../contracts/metric-card.contract.v0.1.0.md) delegado para construir bajo las decisiones globales del usuario; auditoría humana final pendiente.
