---
contract_schema: figma-component-contract/0.1.0
status: OBSERVED
source_file_key: 9zs5RMR8LB5wHjW9Bd59BA
source_node_id: "1133:31549"
read_only: true
---

# Dot · contrato técnico de la fuente

El [YAML sincronizado](dot.source.component-contract.yaml) registra IDs, variantes y dependencias. Este documento describe el Figma antiguo, no prescribe aún el destino ni comportamiento de producto.

## Identidad y evidencia

- [Set `dot`](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1133-31549), ID `1133:31549`, key `bc7fd5437899a1868aeba789925329c30d5b6996`, página `1133:20620` (`❖ Dot  ✅`). Set 201×290 con 15 variantes, 22/22 nodos leídos, seis textos, cero instancias, 12 variables únicas, cero estilos nombrados y cero reacciones. Captura 201×290 inspeccionada.
- **FIGMA_DIRECT, nota de página:** comunica información breve, estados, notificaciones, conteos, niveles o disponibilidad; puede acompañar iconos, botones o avatares sin interrumpir la experiencia.
- La `description` del set contiene texto de procedencia no demostrada y dos afirmaciones falsas: dice que faltan variantes large de Busy/Inactive aunque existen, y describe un cambio automático a pill sin reacción observada. Se conserva como evidencia literal disponible en Figma, pero no gobierna matriz ni comportamiento.

## Propiedades, variantes y contenido

| Propiedad | Tipo | Default | Valores |
|---|---|---|---|
| `type` | VARIANT | active | active, busy, inactive, number, number expand |
| `size` | VARIANT | large | small, middle, large |

La matriz 5×3 está completa. No hay propiedad TEXT; los seis textos numéricos están hardcoded: `1` para Number y `99+` para Number Expand. No se observa cálculo de umbral, actualización automática ni animación.

| Type | Small | Middle | Large |
|---|---|---|---|
| active | `1133:31550` 8×8 | `1133:31551` 12×12 | `1241:39842` 16×16 |
| busy | `1133:31562` 8×8 | `1133:31563` 12×12 | `1241:39854` 16×16 |
| inactive | `1133:31560` 8×8 | `1133:31561` 12×12 | `1241:39856` 16×16 |
| number | `1133:31552` 8×8 | `1133:31554` 12×12 | `1241:39859` 16×16 |
| number expand | `1133:31556` 12×8 | `1133:31558` 23×12 | `1241:39851` 23×16 |

Active/Busy/Inactive son discos sin texto. Number y Number Expand tienen texto Manrope Bold blanco. Small usa 4 px (texto 2×5 para `1`, 8×5 para `99+`); Middle y Large usan 8 px (texto de `99+` 15×11). Tracking −2%, con line-height Auto o 160% según variante. El tamaño y contenido son hechos observados, no validación de legibilidad. Los numeric components usan auto layout vertical y padding lateral 2 o 4 en la fuente; el resto layout NONE.

## Geometría y colores

Todos son componentes raíz con radio visual full (literal 9,999,999), stroke blanco exterior de 1 px y fill sólido. Active usa `color/feedback/positive/icon` #098300; Busy, Number y Number Expand usan `color/feedback/danger/icon` #d40000; Inactive usa `color/background/disabled` #e2e8f0. El stroke usa `color/border/on-brand` blanco y el texto numérico `color/text/on-brand` blanco. Aunque los roles `feedback/*/icon` tienen scope FRAME_FILL en la fuente, su categoría semántica de icono no describe estos fondos; no debe copiarse ese uso al destino.

El set usa 12 variables: nueve locales (`feedback positive/danger icon`, `background disabled`, `border on-brand`, `text on-brand`, `font family`, `font weight bold`, `spacing none/xs`) y tres remotas de radio full, stroke 1 y padding vertical 0. Se conservan IDs en YAML; igualdad de color no equivale a misma función. Los tamaños 8/12/16 y font sizes 4/8 son literales en las variantes, no bindings tipográficos locales observados.

## Interacciones, accesibilidad y límites

No hay reacciones, instancias anidadas ni estilos nombrados. El set no demuestra lógica de notificación, límite `99+`, actualización dinámica, número accesible, contraste usable en todo contexto, hit target o semántica web. El texto de 4/8 px plantea un riesgo de legibilidad que el contrato destino debe decidir y documentar; no se corrige silenciosamente en esta evidencia.

## Evidencia

- `E001` set `1133:31549`: identidad, Description, propiedades y variantes.
- `E002` 15 variantes: dimensiones, fills, strokes, radios, texto, bindings y cero reacciones.
- `E003` seis textos: contenido, 4/8 px, Manrope Bold, blanco, sin TEXT property.
- `E004` 12 variables usadas, nueve locales y tres remotas; sin componentes ni estilos.
- `E005` nota de página `1133:31513` y captura 201×290.

**REQUIRES_DEFINITION:** reglas funcionales de presencia, conteos, umbral, consumo accesible y tratamiento de tamaños numéricos reducidos.
