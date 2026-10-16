# Donut · contrato de evidencia fuente

- **Origen:** [Libreria v1.1.0, set Donut](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=3086-1090), página `268:20756`, set `3086:1090`, key `c23b7c56a0b6d559794bff1d8892069320f13328`.
- **Inspección:** `COMPLETE`, 13/13 nodos, solo lectura; captura dedicada 323×510 y paths vectoriales de seis nodos preservados en [JSON de geometría](../../sources/figma-snapshots/chart-donut.vector-paths.json), SHA-256 `60e22a15421f6be666e175bc64905074562f00453abb2032c3203c587c5ad764`. El nombre fuente `Donut` representa visualmente un semicírculo, no una dona completa.

## Component Identity

**OBSERVED:** set `Donut` 323×510 con tres componentes 283×142: `Progress=75%`, `50%` y `25%`. `Progress` es eje VARIANT, default 75%. No hay descripción propia.

## Anatomy

Cada variante tiene vector `Total` (arco semicircular de pista), vector `Completed` (arco parcial) y texto Percent centrado dentro del hueco. Son seis vectores fuente y tres textos; no hay instancias ni imágenes raster.

## Dependencies

Seis variables únicas, todas locales: `color/interactive/primary/active`, `color/interactive/primary/default`, `color/icon/brand`, `color/text/primary`, `font/line-height/md` y `font/size/2xl`. Cero estilos nombrados, componentes anidados y reacciones. Los colores de arcos usan roles interactive/icon incompatibles con una representación de datos estrictamente semántica en destino.

## Properties

Solo `Progress` VARIANT con tres valores. El texto 75/50/25% no tiene propiedad TEXT editable; cambiarlo sin cambiar arco sería incoherente. No hay número libre ni propiedad de color.

## Variants

| Progreso | ID | Arco Completed (caja) | Texto |
|---|---|---:|---|
| 75% | `3086:1089` | 241.56×141.5 | 75% |
| 50% | `3086:1091` | 141.5×141.5 | 50% |
| 25% | `3086:1095` | 82.04×100.06, desplazado 42 px | 25% |

Todas las variantes tienen arco Total 283×141.5 y caja componente 283×142. Los paths exactos están conservados en el JSON; las dimensiones redondeadas aquí son solo lectura humana.

## States

`Progress` representa tres muestras fijas de valor, no estado de carga interactiva ni animación. Cero reacciones.

## Layout

Los componentes no usan auto layout: vectores posicionados absolutamente en la caja 283×142 y Percent aproximadamente x=89, y=76, caja 105×66. El set distribuye tres muestras verticales con separación visible. El arco muestra la mitad superior de un anillo y termina en línea horizontal inferior.

## Visual Styles

Total `#5F85FB`, Completed `#3255F7`, Percent `#0F172A`. Total usa `color/interactive/primary/active`; Completed usa `color/interactive/primary/default` en 75/25% y `color/icon/brand` en 50%, pese a tener el mismo RGB. Percent usa `color/text/primary`. Esta inconsistencia de roles se documenta sin equiparar semánticamente los tokens fuente.

## Typography

Percent: Manrope SemiBold 32 px, line-height 24 px, tracking 0.1% literal; `font/size/2xl` y `font/line-height/md` enlazados, familia/peso/tracking sin binding observado. La caja alta de 66 px no implica line-height de 66.

## Tokens

Seis IDs y scopes en el [YAML sincronizado](chart-donut.source.component-contract.yaml). Los arcos requieren roles de gráfico con scope `SHAPE_FILL` en destino; no debe copiarse un token interactive o icon para vectores de datos.

## Content

`75%`, `50%` y `25%` son ejemplos estáticos que coinciden con la geometría de cada arco. No hay cálculo, formato, locale o interpolación observada.

## Interactions

`UNDEFINED`: cero reacciones; no hay animación o actualización de valor.

## Accessibility

`REQUIRES_DEFINITION`: el porcentaje visible aporta pista textual, pero el componente no define nombre de métrica, rango, unidad, lectura de progreso o contraste funcional para lectores de pantalla.

## External Dependencies

Ninguna dependencia remota activa ni estilo externo expuesto.

## Unresolved Information

No se sabe si el semicírculo representa completitud, objetivo o distribución; no se extrapolan valores distintos a 75/50/25%. Los roles fuente de arcos son semánticamente inconsistentes y deben remapearse con aliases a primitivas existentes.

## Implementation Notes

Conservar los seis paths vectoriales originales mediante datos read-only y crear variantes locales, sin importar el componente antiguo como dependencia remota ni rasterizarlo. Mantener texto y arco sincronizados por variante. El nombre destino puede aclarar `Semi-donut`/`Gauge`, pero el mapeo a `Donut` fuente debe persistir.

## Evidence / Confidence

**FIGMA_DIRECT:** metadata, screenshot, traversal 13 nodos, seis paths vectoriales, tres textos, seis variables y cero reacciones. **DERIVED:** lectura como semicírculo de progreso. **REQUIRES_DEFINITION:** significado y accesibilidad de datos. Confianza `HIGH` para forma y contenido observado.
