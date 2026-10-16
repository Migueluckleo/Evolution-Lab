# Contrato fuente · Navigation / Switch Tab

**Fuente:** [Librería anterior · Switch Tab](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2461-1740). **Estado:** `SOURCE_INSPECTED`, read-only. Componente `2461:1740`, key `a9b5398f81f4ca60c7f3eed597a90ffefc2029ad`, página `268:20245`. Recorrido completo: 33 nodos, cuatro ocultos, 16 instancias, ocho vectores, ocho textos, veinte variables distintas, cero reacciones y cero estilos nombrados. El [YAML](navigation-switch-tab.source.component-contract.yaml) conserva los datos deterministas.

## 1. Purpose

**Observed:** ejemplo de navegación entre secciones en un mismo contexto. La fuente no define lógica de selección ni destino de navegación.

## 2. Anatomy

**Observed:** componente contenedor con cuatro instancias locales de `Tab item` en orden: Active, Default, Default, Default. Cada item conserva su icono izquierdo oculto, texto, Dot numérico e icono derecho visibles; no se desprenden sus subcomponentes.

## 3. Dependencies

**Observed:** set local `Tab item` key `44cd079b3bb28629bd1fdcb794dcffc89ee81a2a`; cuatro instancias. Sus dependencias anidadas AddressBook remoto y Dot local ya se desglosan en el [contrato fuente del item](navigation-switch-tab-item.source.component-contract.md). No se infiere catálogo remoto completo.

## 4. Properties

**Observed:** el padre no tiene propiedades de componente. Cada instancia hija conserva propiedades State, iconos y visibilidad del item, pero no existe una propiedad del padre que garantice un único Active.

## 5. Variants

**Observed:** `Switch Tab` es un solo `COMPONENT`, no un set. Cuatro tabs visibles son una composición de ejemplo, no una matriz 1–4 ni variantes de selección.

## 6. States

**Observed:** primera instancia Active y otras tres Default. Disabled existe en el item pero no aparece en esta composición fuente.

## 7. Layout

**Observed:** frame 488×46, auto layout horizontal, gap 4, padding 4 en cuatro lados, radio 8. Hijos a x=4/128/248/368, y=4; anchos 120/116/116/116, altura 38.

## 8. Visual styles

**Observed:** fill `color/background/subtle` resuelve neutral/200 `#F1F5F9` en los cuatro modos de origen. Sin stroke, sombra ni efectos. La captura fuente confirma un rectángulo gris pálido con primer tab morado activo.

## 9. Typography

**Observed:** los cuatro textos `Tab title` provienen de las instancias `Tab item`: Active Manrope Bold 14, otros Regular 14. El contenedor no contiene texto propio.

## 10. Tokens

**Observed:** veinte variables únicas en el subárbol completo: una de fondo del contenedor y diecinueve heredadas de las instancias y sus dependencias. Para destino, el consumidor nuevo del padre requiere `color/background/subtle`, `spacing/xs` y `radius/md`, todos presentes en el JSON aprobado.

## 11. Content

**Observed:** los cuatro títulos `Tab title` y cuatro badges `1` son placeholders; no establecen cantidad de secciones ni conteos reales.

## 12. Interactions

**Observed:** cero reacciones. **Requires definition:** click, cambio de sección, exclusividad de Active, teclado y persistencia.

## 13. Accessibility

**Requires definition:** roles tablist/tab, nombre accesible, `aria-selected`, foco y área táctil fuera de Figma.

## 14. External dependencies

El contenedor no añade dependencias externas a las del item. La biblioteca remota completa de AddressBook no está expuesta por Figma; la variante activa sí está identificada.

## 15. Unresolved information

No hay regla fuente para diferente número de tabs, overflow, etiquetas largas, estado Disabled en grupo o más de una selección. No derivar variantes o comportamiento de un único ejemplo.

## 16. Implementation notes

Construir el contenedor como componente independiente con cuatro instancias del item local del destino; conservar `color/background/subtle` porque su alias y scope `FRAME_FILL` coinciden. No duplicar los dieciséis nodos anidados como formas sueltas.

## 17. Evidence / confidence

`E001` identidad y geometría; `E002` recorrido de 33 nodos; `E003` cuatro mains y propiedades hijas; `E004` tokens y aliases; `E005` captura aislada. Confianza `HIGH` en apariencia y estructura, `UNRESOLVED` en comportamiento de producto.
