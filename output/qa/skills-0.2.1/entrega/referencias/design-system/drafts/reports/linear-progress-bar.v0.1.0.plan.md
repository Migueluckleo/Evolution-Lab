# Plan de construcción Figma · Linear Progress Bar 0.1.0

- **Destino:** AI Design System, página exclusiva `Linear Progress Bars`, set único con 48 variantes. La página no existía al preflight; no se escribe en la fuente ni se publica.
- **Dependencias:** cinco variables semánticas de fondo verificadas contra JSON y primitivas existentes; roles locales de texto, tipografía, espacio y radio con scopes adecuados.
- **Construcción:** crear las 48 combinaciones desde el snapshot fuente, mantener ancho 246 px y barras 4/8/12 px; ligar pista y tramo a sus roles de fondo, los tres textos a roles de texto y tipografía completa; exponer Label/Helper editables y tres booleanas de visibilidad.
- **QA:** leer el destino tras construir; comprobar unicidad de página, 48 combinaciones, tamaños y longitudes, porcentaje visible, propiedades, 240 paints, 720 bindings tipográficos, 20 aliases Foundation y categorías/scopes. Inspeccionar captura fuente/destino; dejar auditoría humana pendiente.
