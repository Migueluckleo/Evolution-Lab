# Charts · clasificación inicial de fuente

- **Archivo fuente:** [Libreria v1.1.0, página Charts](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=268-20756), página `268:20756`, solo lectura. Captura de la página 2435×1754 (vista 1400×1009) inspeccionada.
- **Estado:** `SOURCE_INSPECTED`: las cinco piezas ya tienen contrato MD/YAML y QA de evidencia `PASS`; aún no hay contrato destino ni construcción Charts. El destino previsto es una página semántica `Charts` con piezas internas reutilizables; esta agrupación se revisa en la síntesis de destino.

| Pieza fuente | ID / key | Variantes observadas | Nodos / textos / instancias | Dependencias activas |
|---|---|---:|---:|---|
| `cell` | `2977:2066` / `ddc93f484212024c51d2cdddc480ea242a4db18f` | 13 | 26 / 0 / 0 | ninguna |
| `labelCell` | `3086:992` / `b5deacd96d67b6a46805de3d5abc20cc2717a4ea` | 4 | 17 / 4 / 0 | ninguna |
| `Progress chart item` | `3075:871` / `e0f0518afea25fa255f066c83708099842d1ccc7` | 2 | 40 / 10 / 6 | seis `labelCell` |
| `Donut` | `3086:1090` / `c23b7c56a0b6d559794bff1d8892069320f13328` | 3 | 13 / 3 / 0 | ninguna |
| `Header` | `3075:764` / `e322384d309997e64a5446a93ad07fd3560f7cf4` | 1 | 17 / 5 / 3 | tres `labelCell` |

El total de componentes materializados es 23. Los cuatro gráficos grandes de ejemplo en la parte superior de la página son composiciones demostrativas, no sets principales adicionales. No se inventará un componente de gráfico completo solo por su apariencia.

## Dependencias y riesgos detectados

- `labelCell` debe definirse antes de `Header` y `Progress chart item`; las nueve instancias existentes se contaron en sus árboles fuente. El `Header` es un componente suelto, no variante de set.
- `cell` presenta 13 combinaciones: una vacía y 12 con contenido (`position` first/middle/last × `segment` solo/upper/middle/lower). No se debe generar el cartesiano completo de tres ejes.
- La fuente aplica `color/brand/default` a fills de barras, `color/icon/brand` a un rectángulo de progreso y colores `interactive` a vectores de Donut. Aunque varios RGB coincidan, esos roles no son semánticamente adecuados para superficies de datos en el destino.
- `labelCell` usa un swatch gris `#D9D9D9` sin variable y tamaño de fuente Large de 16 px sin binding explícito; requiere mapeo a tokens existentes o extensión semántica documentada.
- `Donut` dibuja arcos con vectores cuya geometría es distinta para 75/50/25%. Su porcentaje es texto de ejemplo, sin dato dinámico ni reacción Figma. Debe conservarse la forma sin fingir cálculo automático.
- La página fuente tiene cero reacciones en estas cinco piezas. Comportamiento de datos, accesibilidad de gráficos, ejes y responsividad siguen sin definición de producto.

## Próximo trabajo técnico

Contratos fuente completados: [labelCell](../contracts/chart-label-cell.source.component-contract.md), [cell](../contracts/chart-cell.source.component-contract.md), [Progress chart item](../contracts/chart-progress-item.source.component-contract.md), [Donut](../contracts/chart-donut.source.component-contract.md) y [Header](../contracts/chart-header.source.component-contract.md). Sigue auditar scopes/contraste y dependencias, sintetizar contrato destino y solo después construir la página Charts. Preservar el archivo fuente y el inventario de tokens original.
