# Radio Button · contrato técnico observado en Figma

**Fuente:** [Librería v1.1.0, set `radio button`](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1230-24283) · `1230:24283` · inspección de solo lectura, 2026-09-23. **Estado:** extracción completa del set: 53/53 nodos, incluidos 16 textos invisibles. Este documento describe evidencia de Figma; no es código ni una definición de interacción web. [YAML sincronizado](radio-button.source.component-contract.yaml).

## 1. Component Identity

**Observed from Figma:** set local `radio button`, key `92e794dad0b717afa2e923d7bf2db0b041e9f230`, 678×194 px, página `❖ Radio button  ✅` `1144:34653`. El set no tiene Description; una nota de la página explica que las opciones son mutuamente excluyentes y deben tener etiqueta clara. Es contexto documental de página, no propiedad del set.

## 2. Anatomy

**Observed from Figma:** ocho componentes de 24×24; cada uno contiene `Label` oculto, una instancia local `radio` de 24×24 y `Label right` oculto. La instancia contiene un círculo visible de 18×18 centrado a x=3,y=3. En las variantes On hay un grupo intermedio; en Off, el círculo es hijo directo de `Content`. **Derived structure:** etiqueta opcional izquierda + indicador reutilizado + etiqueta opcional derecha.

## 3. Dependencies

**Observed from Figma:** ocho instancias de un set local `radio` `1144:34813`, key `9a7212da688ebc11ad48818760d8265d5ed0a019`. Cuatro usan main `State=active` `1144:34814`, key `e7e03dc78344bdff6df2adac7aa643e9a131cc91`; cuatro usan main `State=default` `1144:34824`, key `86581df5fac3d8ec945e4e055656830c93bcb4f7`. El set interno define además `focus` y `hover`, pero el wrapper no selecciona esos mains: aplica overrides a los activos/default. Las dos dependencias de main son locales y resueltas. Doce variables distintas y un estilo de efecto con nombre se enumeran abajo.

## 4. Properties

| Propiedad Figma | Tipo | Default | Evidencia |
|---|---|---|---|
| `radio` | VARIANT | `on` | opciones `on`, `off` |
| `state` | VARIANT | `enabled` | `enabled`, `hover`, `focus`, `disabled` |
| `show left field label#20125:0` | BOOLEAN | false | ligado a `visible` en los ocho `Label` |
| `show right field label#102635:0` | BOOLEAN | false | ligado a `visible` en los ocho `Label right` |

**Requires definition:** no se observó propiedad TEXT para editar el contenido de ambas etiquetas; esto limita la API de instancia del origen, sin demostrar una regla de producto.

## 5. Variants

| `radio` | `state` | Componente fuente |
|---|---|---|
| on | enabled | `1230:24305` |
| on | hover | `1230:24284` |
| on | focus | `1230:24291` |
| on | disabled | `1230:24298` |
| off | enabled | `1230:24312` |
| off | hover | `1230:24319` |
| off | focus | `1230:24326` |
| off | disabled | `1230:24333` |

Las ocho combinaciones observadas completan el producto de dos valores por cuatro estados; no hay otras en el set inspeccionado.

## 6. States

**Observed from Figma:** On usa contorno de 5 px; Off, 2 px. Enabled/Focus On usan `color/border/brand`; Hover de ambos usa `color/border/hover`; Disabled de ambos usa `color/border/disabled`; Off Enabled usa `color/border/default`, Off Focus usa `color/border/brand`. Focus de ambos añade estilo `focus/outset` con dos DROP_SHADOW. No hay reacciones de prototipo en las ocho variantes.

## 7. Layout

**Observed from Figma:** wrapper HORIZONTAL HUG, sin padding, separación 8 px entre hijos visibles. Sin etiquetas visibles, tamaño 24×24. Cada texto fuente mide 68×18 y se ubica a y=3. Instancia 24×24 con círculo 18×18 centrado. La instancia usa internamente `spacing/xl` (12 px en la lectura) y `radius/sm` remoto, pero su aspecto visible depende de los overrides del círculo. La observación no demuestra regla responsive o tamaño táctil.

## 8. Visual Styles

El círculo tiene fill blanco `color/background/default`. Su contorno cambia por estado según la sección 6. El estilo local `focus/outset`, key `db4f7e95726995e57ca781fbe41ec23bcab72a1e`, tiene dos sombras sin variables de color: exterior azul #1d21b0, spread 4; interior #f8fafc, spread 2; ambas radius 0 y offset 0. La presencia visual de foco está demostrada; su activación por teclado no.

## 9. Typography

**Observed from Figma:** 16 etiquetas `Field Label`, Manrope Regular 14 px, line-height 18 px, tracking 0%, auto-resize ancho/alto. Familia y tamaño ligados a `font/family/base` y `font/size/sm`; interlineado y tracking son literales. Texto primary en Enabled/Hover/Focus y disabled en Disabled. Todos los textos están ocultos en el estado predeterminado.

## 10. Tokens

**Observed from Figma:** 12 variables únicas: `color/background/default`, `color/border/{brand,hover,disabled,default}`, `color/text/{primary,disabled}`, `font/family/base`, `font/size/sm`, y tres variables remotas `spacing/xl`, `radius/sm`, `stroke/stroke-focus`. Se conservan referencias originales e IDs exactos en el YAML. Los bindings fuente son evidencia, no asignación automática de IDs del destino.

## 11. Content

**Example content:** `Field Label` es texto de muestra en las 16 capas; no es contenido obligatorio. La nota de página exige una etiqueta clara para el grupo de opciones, pero Figma no conecta esa necesidad con un nombre accesible o propiedad TEXT.

## 12. Interactions

**Observed from Figma:** ninguna reacción definida en las ocho variantes ni en los mains internos usados. **Requires definition:** selección exclusiva, teclado, cambios de estado y validación funcional no están definidos por la apariencia de Figma.

## 13. Accessibility

**Observed from Figma:** las variantes muestran diferencia visual On/Off y anillo Focus; las dos etiquetas están ocultas por defecto. **Requires definition:** nombre accesible, agrupación semántica, orden de foco, estado expuesto a tecnologías de asistencia, área táctil y contraste evaluado. No se afirma cumplimiento WCAG.

## 14. External Dependencies

Tres variables remotas del indicador: `spacing/xl`, `radius/sm`, `stroke/stroke-focus`. Su biblioteca, proyecto, URL y versión no quedan expuestos por la lectura MCP; cada referencia está resuelta por ID/nombre/tipo, no por procedencia editorial.

## 15. Unresolved Information

El archivo fuente no define comportamiento web ni una propiedad TEXT para las etiquetas; se requieren decisiones de reconstrucción explícitas. La diferencia entre la nota de página que recomienda etiqueta y ambas etiquetas ocultas es una tensión de uso, no una contradicción de la estructura del set. No hubo truncamiento de nodos.

## 16. Implementation Notes

Un destino que quiera conservar composición debe tratar `radio` como dependencia reutilizable y documentar cualquier cambio de API, tokens o estructura antes de construir. El círculo On usa grosor literal 5 px sin variable fuente, mientras el destino de foundations no contiene ese grosor; esta diferencia requiere solución trazable, no asignación ficticia.

## 17. Evidence / Confidence

**HIGH** para estructura, variantes, variables usadas, estilo y apariencia: metadata del set, captura 678×194, traversal 53/53 con invisibles, lectura de mains, tokens y estilo. **Requires definition** para semántica y comportamiento de producto. La cuenta de dependencias es: 8 instancias, 2 mains locales resueltos, 12 variables resueltas (9 locales, 3 remotas), 1 estilo local resuelto.
