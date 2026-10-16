---
contract_schema: figma-component-contract/0.1.0
status: OBSERVED
source_file_key: 9zs5RMR8LB5wHjW9Bd59BA
source_node_id: "1430:18850"
read_only: true
---

# Button Icon · contrato técnico de la fuente

El [YAML sincronizado](icon-button.source.component-contract.yaml) conserva los 30 IDs de variante, las 60 instancias y las 27 dependencias de variables. Este documento describe la Librería anterior; no prescribe el destino.

## Identidad y cobertura

- [Set `Button Icon`](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1430-18850), ID `1430:18850`, key `fbc267a15caab7547a5d782a8887da547ee7cf03`, página `1430:18021` (`❖ Buttons icon ✅`), frame padre `1430:18766`. Set 289×960; description y links vacíos.
- Traversal read-only 151/151 nodos: 30 COMPONENT, 60 INSTANCE, 30 VECTOR y 30 TEXT dentro del set. La captura 289×960 muestra una matriz de tres tamaños por diez filas; no hay reacciones.

## Ejes y propiedades

La matriz es completa: `state` default/disabled/hover/focus/active × `size` small/middle/large × `type` default/outline = 30. Defaults Figma: state default, size small, type default. La propiedad `icon` es INSTANCE_SWAP con Bell Phosphor activo, key `ef703d88cfc6792cdd17351c4cc923a019b91855`, y 1512 component sets preferidos; no son variantes activas. `show badge indicator` es BOOLEAN true y controla 30 instancias de Dot numérico. El Bell es intercambiable en las 30 variantes. No hay propiedad editable para el número del Dot en el set padre; los textos visibles muestran `1` como ejemplo.

## Anatomía y medidas

Cada componente contiene Bell y Dot en ese orden, sin texto de botón. Small mide 24×24, Bell 16 y Dot 8 con padding 4; Middle 48×48, Bell 24 y Dot 12 con padding 8; Large 56×56, Bell 32 y Dot 16 con padding 8. Radio del cuerpo 8, stroke 1 cuando existe. Bell se ubica a (4,4) Small o (12,12) Middle/Large. Dot se ubica a (12,12), (24,18) o (28,20) respectivamente. Los tres Dot son instancias del set fuente `Dot`, variantes `type=number` de tamaño small/middle/large, keys `a100dec6c0f77e6ff8c357f51878be1cee8bd61a`, `06df8e9033e095bd1ca776691d73501daf5fdda9` y `309ba73acbf0853df307a033c09a1a40856357d5`.

## Apariencia por estado

| State | Type default | Type outline | Bell |
|---|---|---|---|
| default | transparente, sin borde | transparente, borde `color/border/subtle` | `color/icon/primary` |
| disabled | transparente, sin borde | `color/background/subtle`, borde `color/border/disabled` | `color/icon/disabled` |
| hover | `color/surface/brand` | mismo fondo y borde `color/border/hover` | `color/icon/primary` |
| focus | `color/background/default`, borde `color/focus/ring` | igual | `color/icon/primary` |
| active | `color/interactive/primary/default` | mismo fondo y borde `color/border/subtle` | `color/icon/on-brand` |

El Dot numérico permanece rojo (`color/feedback/danger/icon` aplicado al fill de un contenedor, scope de categoría incorrecta) con borde blanco `color/border/on-brand`, incluso en Disabled. Su texto blanco usa `color/text/on-brand`, Manrope Bold y tamaños 4/8 px según variante. El Bell usa una instancia remota Phosphor; su VECTOR toma el rol iconográfico correspondiente. Solo `state=focus, size=large, type=default` tiene estilo de efecto `focus/outset` con dos sombras además del borde de foco; las otras cinco variantes Focus no tienen efecto. Este carácter aislado es evidencia, no una regla coherente inferida.

## Tokens y dependencias

27 variables únicas usadas: 21 locales y seis remotas, entre color, spacing, radio, tipografía, tamaño iconográfico y stroke. El YAML conserva sus IDs, roles y locality. La propiedad `font/weight/bold` de la fuente tiene scope `ALL_SCOPES`; el destino no debe extender esa amplitud por analogía. Las igualdades visuales no sustituyen bindings. Hay un estilo nombrado `focus/outset` local, usado una sola vez.

La fuente tiene dos componentes dependientes activos: Bell Phosphor y Dot local; en total 60 instancias. El Dot local ya cuenta con contrato propio en esta migración, pero su anatomía no se reescribe aquí. Las 1512 alternativas del picker se registran como disponibilidad, no como dependencias resueltas una por una.

## Interacciones y accesibilidad

No hay reacciones ni acción definida para click, focus, keyboard, badge o cambio de icono. La página describe verbalmente Default/Hover/Active/Focus/Disabled, pero no implementa comportamiento. Small 24×24 es visualmente compacto y no demuestra objetivo táctil suficiente. El número de badge de 4 px es ilegible como dato operativo; `1` es contenido ejemplo. No hay nombre accesible ni semántica de notificación definidos. El contraste no se certifica a partir de la captura.

Evidencias: E001 identidad y 151 nodos; E002 matriz y cinco propiedades; E003 geometría y posición; E004 pinturas y 27 variables; E005 60 instancias y keys; E006 efecto único; E007 captura 289×960. Sin truncamiento de traversal; los 1512 candidatos del picker no se enumeraron deliberadamente.
