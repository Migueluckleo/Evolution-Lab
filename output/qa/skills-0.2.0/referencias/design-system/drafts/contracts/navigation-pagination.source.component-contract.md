# Contrato fuente · Navigation / Pagination

**Fuente:** [Librería anterior · Group Pagination](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2461-714). **Estado:** `SOURCE_INSPECTED`, read-only. Set `2461:714`, key `0d6540ee619c7896a844d6607854415727b43345`, página `268:20245`. Recorrido completo de 146 nodos: cinco componentes, 65 frames, 25 instancias, 25 vectores, 25 textos, diez frames ocultos y 31 variables usadas. Cero reacciones. [YAML determinista](navigation-pagination.source.component-contract.yaml).

## 1. Purpose

**Observed:** control visual de páginas con flechas anterior/siguiente, números, elipsis y selector de cantidad por página. No se puede derivar paginación funcional de este set.

## 2. Anatomy

**Observed:** cada variante contiene `Content` horizontal: control anterior, grupo `1 · … · 2 · 3`, control siguiente y caja `20 por pag` con CaretDown. Dos controles dobles de inicio/fin existen como frames ocultos en cada variante. Los 25 iconos son instancias Caret, no vectores independientes del set.

## 3. Dependencies

**Observed:** cinco variantes Outline/Light de CaretDoubleLeft, CaretLeft, CaretRight, CaretDoubleRight y CaretDown; cinco instancias de cada una. CaretLeft/Right usan mains remotos importables; los otros tres mains son locales al archivo fuente y sus keys no se importan directamente en destino. La biblioteca Phosphor disponible en destino contiene variantes Outline/Light de los mismos tres iconos, con geometría de vector comparable; esto es una sustitución de dependencia que se valida visualmente, no una identidad de key.

## 4. Properties

**Observed:** solo `State` VARIANT, default `Default`, valores `Default`, `Active`, `Hover`, `Focus`, `Disabled`. Los textos `1`, `…`, `2`, `3` y `20 por pag` no son propiedades TEXT de origen; son ejemplos literales.

## 5. Variants

Cinco variantes de 354×66 px, IDs: Default `2461:715`, Active `2461:741`, Hover `2461:767`, Focus `2461:793`, Disabled `2461:819`. No hay tamaños ni número de páginas como ejes.

## 6. States

**Observed:** la mayor parte de la estructura permanece constante. `Active` cambia fill, borde y texto de la página `1` a roles brand. `Hover` cambia su fill a `color/background/subtle`. `Focus` usa `color/focus/ring` y stroke 2 px en esa página. `Disabled` atenúa números, elipsis y control siguiente, pero conserva el selector `20 por pag` con apariencia normal; no implica bloqueo funcional probado.

## 7. Layout

**Observed:** componente HORIZONTAL de 354×66, padding top 16, right 24, bottom 24, left 24. `Content` mide 306×26, gap 12; controles de 26×26; grupo Pages 116×26, gap 4; caja de cantidad 102×26, gap 4 y padding 8. Controles dobles ocultos no ocupan espacio. Radio 4 en las celdas y caja.

## 8. Visual styles

**Observed:** blanco `color/background/default`; gris claro `color/background/subtle` = neutral/200; bordes `color/border/subtle/default/brand` y focus ring; textos `color/text/primary/brand/disabled`; iconos `color/icon/primary/disabled/brand`. Todos son roles fuente, no IDs de destino. Captura de los cinco estados inspeccionada.

## 9. Typography

**Observed:** Manrope 14 Regular para números y cantidad; elipsis SemiBold. Interlineado 160 %, tracking −2 %. No se halló propiedad TEXT editable en el set.

## 10. Tokens

**Observed:** 31 variables distintas en el subárbol, 21 locales y diez remotas, sin variables irresueltas. El YAML conserva los nombres e IDs. La traducción a AI Design System debe usar roles locales de la misma categoría y scope, sin equiparar keys o IDs por igualdad visual.

## 11. Content

`1`, `…`, `2`, `3` y `20 por pag` son muestras. La fuente no define cálculo del rango, totales, disabled de Prev/Next ni opciones del selector.

## 12. Interactions

Cero reacciones. **Requires definition:** navegación de página, salto, tamaño de página, límites y datos.

## 13. Accessibility

**Requires definition:** nombres accesibles de flechas y números, estado actual programático, foco, teclado, feedback de resultados y disabled funcional.

## 14. External dependencies

CaretLeft y CaretRight son remotos; biblioteca exacta/versión no expuesta por la lectura del archivo fuente. CaretDoubleLeft/Right/Down tienen mains locales. La equivalencia de sustitutos de destino se valida por nombre, variante, tamaño y geometría vectorial, no se registra como key fuente idéntica.

## 15. Unresolved information

No hay regla de páginas dinámicas, rango, truncamiento, lista de opciones de cantidad ni efecto de los controles dobles ocultos. No inferir estados adicionales.

## 16. Implementation notes

Construir cinco variantes en el set `Pagination` dentro de la página `Navigation`; reutilizar instancias Caret de Phosphor. Mantener los controles dobles ocultos por defecto si se exponen como booleanas de destino. Las propiedades TEXT de números y cantidad son mejora de editabilidad, no requisito fuente. Conservar las medidas y colores por modo al mapear al JSON aprobado.

## 17. Evidence / confidence

`E001` set/propiedades; `E002` recorrido 146 nodos; `E003` estructura y geometría Default; `E004` diferencias por estado; `E005` 31 variables; `E006` cinco mains iconográficos y sustitutos; `E007` captura. Confianza `HIGH` para estructura/visual; comportamiento de datos `UNRESOLVED`.
