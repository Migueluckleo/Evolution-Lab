# Input Field · evidencia de origen
Inspección de solo lectura, 2026-09-28. Estado PARTIAL únicamente para procedencia remota y reglas de producto no expuestas; los 493 nodos del set fueron recorridos, incluidos 60 ocultos. Modelo sincronizado: [YAML](input-field.source.component-contract.yaml).

## 1. Component Identity
Observed from Figma: set `186:14461`, key `814bb871551c71ccd763ba87c7707521e816a254`, página `20:3` de `9zs5RMR8LB5wHjW9Bd59BA`.

## 2. Anatomy
Etiqueta con Question oculto y asterisco; superficie con texto, prefijo MXN oculto y Eye visible; ayuda inferior. 30 variantes, 493 nodos.

## 3. Dependencies
Dos componentes remotos: Question y Eye, Outline/Light, 30 instancias cada uno. 36 variables (29 locales, 7 remotas) y dos estilos de efecto locales. Identidades y ejemplos de consumidores en [snapshot](../../sources/figma-snapshots/input-field.dependencies.json).

## 4. Properties
Las 12 propiedades de contenido/visibilidad/intercambio están enumeradas en YAML. Defaults: Label, Placeholder text, Optional helper text, MXN; etiqueta, texto, ayuda, asterisco e icono visibles; Question y prefijo ocultos.

## 5. Variants
Derived structure: 3 tamaños × 5 estados × 2 valores = 30. autoFocus solo vale on en focus; no es un cuarto eje independiente.

## 6. States
default, success, error, focus y disabled. value=False/True modifica la jerarquía del texto; no demuestra datos de entrada reales.

## 7. Layout
Ancho 464; controles large/middle/small de 48/40/32 px. Alturas totales 96/88/80, también para value=True; los metadatos superficiales que indicaban 96 para todos no prevalecen sobre la lectura Plugin API.
Auto layout vertical, gap etiqueta-control 8; helper con padding superior 4. [Base](../../sources/figma-snapshots/input-field.base.json), [30 combinaciones](../../sources/figma-snapshots/input-field.variants.json).

## 8. Visual Styles
Fondo blanco, disabled gris sutil, borde neutral/400, success verde y error rojo. Focus normalmente spread 2; middle/small vacíos usan exterior 4 e interior 2. [Efectos exactos](../../sources/figma-snapshots/input-field.focus.json).

## 9. Typography
Manrope; Label/asterisco Bold 14/20; texto y prefijo Regular 14; ayuda Regular 12. El texto usa interlineado AUTO; el prefijo pequeño usa 12 px, los otros 16. Label/asterisco/prefijo tienen tracking 0.1%; los demás 0.

## 10. Tokens
36 dependencias con rol, ID, valor resuelto y consumidor ejemplo. El inventario histórico no se altera. Dos estilos de foco tienen colores literales; un rectángulo fuente usa color/focus/ring como fill, que no es un binding válido para trasladar al destino.

## 11. Content
Cinco cadenas de ejemplo; no definen política de validación ni formato. El texto de value=True sigue diciendo Placeholder text.

## 12. Interactions
UNDEFINED: cero reacciones. El Eye no demuestra mostrar/ocultar contraseña; Question no demuestra tooltip funcional.

## 13. Accessibility
Requires definition: teclado, asociación label/input, lectura de helper y anuncio de validación. Los estados dibujados no demuestran accesibilidad implementada.

## 14. External Dependencies
Las keys remotas están identificadas. La procedencia original completa y versiones de librería no están expuestas; no se inventan. La búsqueda de destino encuentra Eye y Question publicados en Phosphor Icons; la key actual de Question difiere de la histórica.

## 15. Unresolved Information
Comportamiento web y procedencia remota, no bloqueantes de la reconstrucción Figma acotada. Las alternativas sugeridas del intercambio de icono no se inspeccionan exhaustivamente.

## 16. Implementation Notes
No importar el Input antiguo para desligarlo. Preservar fuentes y remapear tokens locales; las mejoras de construcción viven en un contrato separado. Los snapshots conservan geometría, tipografía y diferencias por variante.

## 17. Evidence / Confidence
Alta para anatomía y apariencia observadas; no se atribuye intención donde falta evidencia. YAML y snapshots son la proyección estructurada; ninguna extracción monolítica truncada se presenta como evidencia completa.
