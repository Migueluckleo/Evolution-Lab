---
contract_schema: sdd-project/0.2
contract_id: TOOLTIP-001
name: Tooltip
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
owner: null
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Tooltips
sources: [SRC-FIGMA-TOOLTIP-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/tooltip.contract.v0.1.0.yaml]
dependencies: [FOUNDATIONS-TOKENS-001]
---

# Tooltip · contrato delegado 0.1.0 para Figma

Lectura **read-only** del component set fuente `2599:10469`, página `2599:10321` del archivo anterior. El [YAML de evidencia](tooltip.contract.v0.1.0.yaml) y este MD describen el mismo set: cuatro variantes, 21 nodos inspeccionados, cero instancias internas, 12 variables usadas y cero estilos nombrados. [QA-TOOLTIP-001](../../qa/contracts/tooltip.v0.1.0.review.md) pasó sobre el candidato preservado por digest; esta versión pasa a `DELEGATED_FOR_BUILD` bajo [DEC-LEGACY-MIGRATION-DELEGATION-001](../../registry/decisions.md). No está aprobada por el usuario y queda sujeta a auditoría humana posterior.

## 1. Purpose

La documentación visible de la página fuente describe información breve y contextual al pasar el cursor o enfocar un elemento. El set no tiene Description propia. Se reconstruye la **representación visual** de la burbuja y sus cuatro posiciones de flecha; activación, temporización y relación con el elemento disparador no están definidos por el set.

## 2. Contract

| ID | Regla candidata para Figma | Fuerza | Procedencia | Criterio |
|---|---|---|---|---|
| REQ-TTIP-001 | Crear una página exclusiva `Tooltips` y un único set principal `Tooltip`, sin modificar Buttons ni Chips. | MUST | Decisión delegada de nombre funcional + P04 | AC-TTIP-001 |
| REQ-TTIP-002 | Crear exactamente las cuatro variantes observadas del eje `Align`: Right, Down, Up, Left; default Right. | MUST | Fuente directa | AC-TTIP-002 |
| REQ-TTIP-003 | Cada variante tiene cuerpo, etiqueta editable y flecha vectorial con geometría/orientación propia; ancho FIXED observado y alto HUG. | MUST | Fuente directa | AC-TTIP-003 |
| REQ-TTIP-004 | Exponer propiedad TEXT para el contenido, default `Tooltips label`, y mantenerla conectada a las cuatro etiquetas. | MUST | Definición fuente | AC-TTIP-004 |
| REQ-TTIP-005 | Enlazar fondo y flecha a `color/background/inverse`; el texto a `color/text/inverse` del destino. No usar `color/text/on-brand` solo porque comparte blanco: el JSON define `inverse` para fondos oscuros. | MUST | Fuente + semántica del JSON + decisión delegada explícita | AC-TTIP-005 |
| REQ-TTIP-006 | Enlazar familia, peso, tamaño, interlineado y tracking a variables semánticas locales, además de padding, gap y radio aplicables, según la tabla de tokens. | MUST | JSON aprobado + normalización delegada | AC-TTIP-006 |
| REQ-TTIP-007 | Conservar las dos sombras literales observadas porque el JSON aprobado no define un token/effect style de sombra; no inventar variable. | MUST | Fuente directa + excepción acotada P03 | AC-TTIP-007 |
| REQ-TTIP-008 | Registrar IDs reales, diferencias frente a la fuente, lectura posterior, captura visual y QA; mantener auditoría del usuario pendiente. | MUST | P04/P05/P06 + delegación | AC-TTIP-008 |

## 3. Anatomy

```text
Tooltips (PAGE propuesta)
└─ Tooltip (COMPONENT_SET)
   ├─ Align=Right / Align=Left (auto layout horizontal)
   │  ├─ Body (FRAME) → Label (TEXT)
   │  └─ Arrow area (FRAME) → arrow (VECTOR)
   └─ Align=Up / Align=Down (auto layout vertical)
      ├─ Body (FRAME) → Label (TEXT)
      └─ Arrow area (FRAME) → arrow (VECTOR)
```

El orden visual cambia según la dirección: izquierda y arriba ubican la flecha antes del cuerpo; derecha y abajo, después. La flecha fuente es un vector de 16×10 con la misma ruta en los cuatro casos y distinta transformación; la ruta se conserva en el YAML.

## 4. Properties

| Propiedad conceptual | Tipo Figma | Default | Opciones | Evidencia |
|---|---|---|---|---|
| Content | TEXT | `Tooltips label` | texto editable | `componentPropertyDefinitions["✏️ Content#2998:29"]` |
| Align | VARIANT | Right | Up, Right, Left, Down | `componentPropertyDefinitions.Align` |

La key interna de la propiedad TEXT será generada por Figma en el destino; no se copia su sufijo `#2998:29`. No se introducen propiedades de estado que la fuente no tiene.

## 5. Variants

| Variante fuente | Medida observada | Posición de flecha |
|---|---:|---|
| Right | 116×38 | derecha |
| Down | 107×48 | abajo |
| Up | 107×48 | arriba |
| Left | 116×38 | izquierda |

Estas medidas son evidencia fuente, no dimensiones fijas universales. En el set fuente, el ancho de cada variante está en `FIXED` y el alto en `HUG`; el texto tiene ancho `FILL` y auto-resize `HEIGHT`. La tokenización de interlineado puede variar la altura destino: no se promete igualdad pixel a pixel sin comparar la captura final.

## 6. Sizes

No existe eje Size en el set. Cuerpo observado de aproximadamente 106–107×38, padding 8/12/8/12, radio 8, flecha 16×10. La anchura debe acompañar el contenido; no se crea un eje de tamaños.

## 7. States

No se observaron variantes hover, focus, disabled ni reacciones en el set. Esos estados no se inventan. El uso contextual descrito en la página no demuestra cómo aparece o desaparece el tooltip.

## 8. Behavior

No hay transiciones de prototipo en las cuatro variantes. Disparador, retraso, duración, dismissal, relación con el elemento ancla y adaptación al borde de viewport requieren una definición de producto fuera de este alcance Figma.

## 9. Accessibility

Se observó una etiqueta visible. No se verifican rol, asociación accesible con el disparador, lectura por tecnología asistiva, teclado ni contraste WCAG desde esta inspección.

## 10. Design tokens

El [inventario JSON aprobado](../../sources/inventories/tokens.inventory.json), SHA-256 bytes `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`, gobierna nombres, tipos, modos, aliases, valores y `description`. No se duplican esos datos como catálogo editable. El mapeo siguiente usa la colección `semantic` local del destino (`VariableCollectionId:6:2`) en Contable, Administrativo, Servicios y Personas.

| Parte/propiedad | Fuente observada | Variable semántica destino | ID destino leído | Decisión |
|---|---|---|---|---|
| Cuerpo y flecha, fill | `color/background/inverse` | `color/background/inverse` | `VariableID:13:39` | misma intención |
| Etiqueta, fill | `color/text/on-brand` | `color/text/inverse` | `VariableID:13:31` | fondo inverso; ambos resuelven a blanco, pero la semántica decide |
| Familia | `font/family/base` | `font/family/base` | `VariableID:10:2` | misma intención |
| Peso | `font/weight/regular` | `font/weight/regular` | `VariableID:10:3` | misma intención |
| Tamaño | `font/size/sm` | `font/size/sm` | `VariableID:10:9` | misma intención, 14 observado |
| Interlineado | literal 160% de 14 ≈ 22.4 | `font/line-height/md` | `VariableID:12:9` | normalización a token 24; desviación visual explícita |
| Tracking | literal −2% | `font/letter-spacing/tight` | `VariableID:12:15` | token semántico; la equivalencia de unidad no está demostrada y se verificará visualmente |
| Separación cero | variable remota 0 | `spacing/none` | `VariableID:12:18` | reemplazo semántico local |
| Flecha, padding 4 | `spacing/xs` | `spacing/xs` | `VariableID:12:29` | misma intención |
| Cuerpo, padding vertical 8 | `spacing/sm` | `spacing/sm` | `VariableID:12:30` | misma intención |
| Cuerpo, padding horizontal 12 | variable remota 12 | `spacing/md` | `VariableID:12:31` | reemplazo semántico local |
| Cuerpo, gap 24 | variable remota 24 | `spacing/xl` | `VariableID:12:33` | reemplazo semántico local; un solo hijo |
| Cuerpo, radio 8 | variable remota 8 | `radius/md` | `VariableID:13:6` | reemplazo semántico local |

Las sombras fuente son dos DROP_SHADOW literales: desplazamiento (0,2), radio 4, color oscuro al 5%; desplazamiento (0,4), radio 6, mismo color al 10%. El JSON aprobado carece de categoría de sombra/elevación. Se conservan como excepción observada, no como variable inventada. El interlineado y tracking destino son decisiones de normalización sujetas a auditoría posterior; si la captura revela pérdida de legibilidad, se documenta y corrige dentro de este alcance delegado.

## 11. Content rules

`Tooltips label` es contenido de ejemplo y default de la propiedad TEXT, no una regla de redacción. No se observaron límites de longitud, truncamiento ni localización. La etiqueta debe permanecer editable sin desacoplar las variantes.

## 12. Composition rules

El cuerpo y la flecha comparten `color/background/inverse`. Su orden sigue `Align`; la flecha no es iconografía independiente ni debe sustituirse por un icono Phosphor. La etiqueta enlaza `characters` con la propiedad TEXT en las cuatro variantes. El set no contiene instancias internas.

## 13. Responsive behavior

No se observaron reglas de colocación responsiva, inversión automática de flecha o breakpoints. El ancho FIXED y el alto HUG son comportamiento de layout Figma, no una promesa de posicionamiento en producto.

## 14. Edge cases

Texto vacío, textos largos, múltiples líneas, colisión con el borde de pantalla y superposición con otros elementos requieren definición fuera de esta reconstrucción. No se agregan variantes para ellos.

## 15. Forbidden combinations

No hay combinaciones adicionales de ejes: solo Align con cuatro opciones. No se infiere que estados ausentes estén prohibidos en producto; simplemente no forman parte de este set.

## 16. Design ↔ Code mapping

`figma_page_name: Tooltips` es una decisión semántica delegada basada en la familia Tooltip y en la convención ya observada de páginas Buttons/Chips; no proviene literalmente del nombre `❖ Tooltip` y no dicta una regla universal de plural. No se define API React, tooltip trigger ni props web.

## 17. Acceptance criteria

| ID | REQ | Evidencia posterior requerida |
|---|---|---|
| AC-TTIP-001 | 001 | Página `Tooltips` única, set principal `Tooltip`, IDs reales; Buttons/Chips intactas. |
| AC-TTIP-002 | 002 | Cuatro nombres únicos y default Right; sin extras. |
| AC-TTIP-003 | 003 | Cuatro anatomías con BODY/TEXT/VECTOR, direcciones, ancho FIXED y alto HUG leídos; captura visual sin recorte. |
| AC-TTIP-004 | 004 | Propiedad TEXT conectada a las cuatro etiquetas, default exacto. |
| AC-TTIP-005 | 005 | Fills de cuerpo/flecha enlazados al fondo inverso y etiquetas al texto inverso por ID local. |
| AC-TTIP-006 | 006 | Readback de variables locales de tipografía/spacing/radio en propiedades aplicables y resolución en cuatro modos. |
| AC-TTIP-007 | 007 | Dos efectos de sombra por variante leídos con valores fuente; excepción documentada. |
| AC-TTIP-008 | 008 | Diario, mapa, QA documental y de implementación; `user_audit: PENDING`. |

## 18. Examples

- `Align=Right`, Content=`Tooltips label`: flecha a la derecha, configuración inicial.
- `Align=Up`, Content editable: flecha arriba, sin cambio de semántica de color.

## 19. Source of truth

El set [Tooltip fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2599-10469) y su lectura read-only sustentan variantes, anatomía y estilos observados. El JSON y `FOUNDATIONS-TOKENS-001` gobiernan variables. La frase de una instancia de documentación que habla de tamaños de Modal en la página Tooltip se identifica como plantilla ajena; no genera requisitos. Las decisiones de normalización figuran explícitas en este contrato, pendientes de auditoría del usuario.

## 20. Change management

Una revisión del mapeo de tokens, dirección de flecha, dimensiones o variantes crea una nueva versión y requiere QA. La implementación Figma de esta versión puede validarse técnicamente bajo la delegación, pero no se convertirá en `APPROVED` por el usuario sin una auditoría explícita.

## 21. Changelog

| Versión | Fecha | Cambio |
|---|---|---|
| 0.1.0 | 2026-09-23 | Primer candidato para reconstrucción semántica de Tooltip, con cuatro posiciones y tokens locales. |
