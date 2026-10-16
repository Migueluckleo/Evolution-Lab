# QA técnico · Navigation / Tab 0.1.0

**Fecha:** 2026-09-24 · **Resultado:** `PASS` técnico · **Contrato:** [Tab](../../specs/navigation-tab.contract.v0.1.0.md) · **Auditoría humana:** `PENDING` · **Publicación Figma:** `UNPUBLISHED`.

| Criterio | Evidencia de lectura posterior |
|---|---|
| Identidad | Un set `Tab` en la página `Navigation` de `AI-Design-System`: set `316:200`, página `275:122`. La Librería anterior permaneció read-only. |
| Variantes | 17 exactas: ocho Base, ocho Dynamic ordinarias y una Dynamic/On/Selected excepcional. Base 135×42; Dynamic On 136×35, Off 133×35 y Selected 135×35. No se agregaron combinaciones teóricas. |
| Anatomía | 33 instancias ImageSquare, 16 Dot ocultos y ocho divisores. Selected conserva un solo icono, sin Dot ni divisor. Cero detach. |
| Propiedades | Tres ejes y siete propiedades de contenido/visibilidad/swap, diez en total. Instancias temporales confirmaron cambio de etiqueta, Dot, visibilidad de iconos, swap Light→Regular y ocultamiento del divisor; se retiraron tras la prueba. |
| Tokens | 107/107 pinturas auditadas con variables locales y cero violaciones de scope o categoría; dos roles de borde nuevos sincronizados con JSON y Figma. Las 17 etiquetas tienen 51 bindings tipográficos; los 16 números Dot tienen 32 de familia/peso y un literal de 8 px sin token compatible en el JSON aprobado. |
| Focus | Cuatro rectángulos de fondo usan `color/background/default` y efecto exterior ligado a `color/focus/effect-outer`; captura posterior muestra el contorno de 2 px. Las líneas inferiores Base conservan los pesos de 2 y 1 px. |
| Prototipado | Cuatro reacciones `ON_HOVER → CHANGE_TO` con destinos exactos Default→Hovered leídas de vuelta. No se agregaron otras interacciones. |
| Visual | Capturas fuente/destino revisadas: paleta, tipografía, radios, fondos, subrayados, contornos y la variante Selected coinciden en la muestra. Dynamic/Off/Hovered conserva 133×35 px y posiciones internas x=16/40/101 como en la fuente. El set destino separa Selected en una quinta fila para que no quede solapada como en la fuente. |

**Corrección de alineación:** el stroke aplicado al marco Dynamic/Off/Hovered desplazaba el contenido 1 px. Se sustituyó por un rectángulo de contorno absoluto, ligado al mismo token de borde, peso y radio; el padding sigue vinculado a 16 px. La lectura posterior confirma el tamaño, las posiciones internas y 107/107 pinturas con bindings válidos, sin introducir un padding literal de 15 px.

El Dot anidado heredaba al importarse un color y tipografía remotos: se vincularon localmente sus 16 textos antes del `PASS`. Una primera aplicación del efecto Focus directamente en el componente no renderizó el contorno; se movió a la capa interna como en la fuente, y la captura final confirma el resultado.
