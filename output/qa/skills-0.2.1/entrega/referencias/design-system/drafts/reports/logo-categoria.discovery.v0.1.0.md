# Descubrimiento de fuente · Logo Categoria · 0.1.0

**Estado:** `SOURCE_INSPECTION_IN_PROGRESS` · 2026-09-24. Evidencia read-only para la dependencia de Header; no es todavía un contrato de construcción ni una aprobación de usar literales en UI ordinaria. Aplica [MIGRATION-TOKEN-TRACEABILITY-001](../../specs/MIGRATION-TOKEN-TRACEABILITY.contract.md).

## Identidad y matriz observadas

El Header fuente `1349:4907` consume una instancia `Logo Categoria` `2873:23060` de 175.69×48, con `categoria=contable`. Su componente principal `8321:294` pertenece al set `Logo Categoria` `8321:504`, key `f1a7cf5b92134fa211a64c2ea547a35fb4b7111c`. El set tiene un eje `categoria` y cuatro valores, sin estados adicionales observados:

| Variante | ID fuente | Dimensiones | Producto anidado |
|---|---|---:|---|
| contable | `8321:294` | 175.79×48 | `product=contabilidad, type=horizontal` |
| comercial | `8321:346` | 152.10×48 | `product=comercial_premium, type=horizontal` |
| servicios | `8321:420` | 159.58×48 | `product=respaldos, type=horizontal` |
| personas | `8321:466` | 150.86×48 | `product=colabora, type=horizontal` |

Las cuatro variantes suman 210 nodos en traversal explícito, incluidos cuatro componentes, cuatro instancias de producto, 131 vectores, 67 grupos, cuatro rectángulos, 98 fills sólidos, 37 gradientes y cuatro fills de imagen. La inspección inicial no encontró variables COLOR vinculadas en estos nodos; los fills pertenecen a arte de marca, no a superficies, texto o iconos funcionales de UI. La variable `logo/categoria` sí existe en el destino y gobierna la selección de categoría del Header, no los colores internos del asset.

## Colores y límite de tokenización

La inspección encontró azules literales `#005AB2` y `#005CB9`, grises `#5B5B5B` y `#5C5C5C`, negro, blanco y un acento `#92F9D8`, además de gradientes e imágenes. Una comparación RGB de las primitivas COLOR del JSON aprobado no encontró equivalencia exacta para los azules, grises ni el acento. No se debe asignar un token cercano ni crear una primitiva nueva por conjetura. Los colores forman parte del artwork del logotipo; si se incorpora como asset local fiel, esa excepción debe quedar explícita y verificarse visualmente. No se debe usar esta excepción para fills ordinarios de componentes.

## Estado de destino y próximos gates

AI Design System aún no tiene un set local `Logo Categoria` ni página semántica `Logos`. `Icon Button`, `Dot` y `Avatar` ya existen localmente, pero no sustituyen este arte. Se requiere comprobar un método de importación que preserve vectores, gradientes, imágenes y las cuatro variantes como componentes locales, sin depender en tiempo de uso de la Librería antigua. Después: contrato MD/YAML completo, mapeo `logo/categoria` a los cuatro modos, QA documental, construcción en página `Logos`, readback de cuatro variantes, y recién entonces Header. Si la fidelidad del asset o el uso de literales de marca no puede resolverse bajo la política vigente, registrar `CONFLICT` y no construir Header con un sustituto visual.
