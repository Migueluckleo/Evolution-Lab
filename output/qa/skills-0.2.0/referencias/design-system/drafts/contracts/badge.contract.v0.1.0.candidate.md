---
contract_schema: sdd-project/0.2
contract_id: BADGE-001
name: Badge
type: component
status: DRAFT
version: 0.1.0
owner: null
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Badges
sources: [SRC-FIGMA-BADGE-001, SRC-FIGMA-PHOSPHOR-001, SRC-TOKENS-INV-001, DEC-ICONS-001, DEC-LEGACY-MIGRATION-DELEGATION-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/badge.contract.v0.1.0.yaml]
dependencies: [FOUNDATIONS-TOKENS-001]
---

# Badge · candidato de contrato 0.1.0

Fuente: set `badge` `1234:65377` de la página `1234:53606` en la Librería anterior. Se inspeccionaron 37/37 nodos, incluidos seis vectores de iconos ocultos, y 27 variables usadas. El [YAML de evidencia](badge.contract.v0.1.0.yaml) preserva IDs y observaciones. Este candidato requiere QA documental antes de usar la delegación de construcción; no equivale a aprobación humana.

## 1. Purpose

Comunicar información breve o un estado en una superficie pequeña, sin interrumpir la interfaz. Esta finalidad procede de la descripción visible en la página fuente; el set no tiene Description propia.

## 2. Contract

| ID | Regla candidata para Figma | Fuerza | Procedencia | Criterio |
|---|---|---|---|---|
| REQ-BDG-001 | Crear una página exclusiva `Badges` y un set principal `Badge` en AI-Design-System, sin alterar otras familias. | MUST | Convención semántica delegada + P04 | AC-BDG-001 |
| REQ-BDG-002 | Crear las seis variantes del eje `Type`: base, light, informational, warning, error, success; default base. | MUST | Fuente directa | AC-BDG-002 |
| REQ-BDG-003 | Conservar auto layout horizontal, ancho HUG, alto FIXED de 25, padding 4/8/4/8, gap 4, radio 4 y anatomía icono izquierdo–texto–icono derecho. | MUST | Fuente directa + tokens locales | AC-BDG-003 |
| REQ-BDG-004 | Exponer texto editable `Badge text`, default `Light`; booleanos `Show left icon` default true y `Show right icon` default false, conectados a las doce instancias. | MUST | Fuente directa | AC-BDG-004 |
| REQ-BDG-005 | Mantener dos swaps de icono con default Presentation de Phosphor Icons, variante Outline/Fill key `3f0d7ae9a02577d4fb4e615737d09fa1b49ec230`, y opciones preferidas Phosphor; no detach. | MUST | Fuente + DEC-ICONS-001 | AC-BDG-005 |
| REQ-BDG-006 | Enlazar fondos, textos e iconos a roles semánticos locales por variante; en Light, usar `color/border/strong` en lugar de disabled y `stroke/xs` de 1 px. | MUST | Fuente + JSON + corrección semántica delegada | AC-BDG-006 |
| REQ-BDG-007 | Enlazar familia, estilo, tamaño, line-height, tracking, padding, gap y radios a variables locales existentes. | MUST | JSON aprobado | AC-BDG-007 |
| REQ-BDG-008 | Registrar diferencias, IDs, lectura posterior, captura y QA; mantener auditoría humana pendiente. | MUST | P04/P05/P06 + delegación | AC-BDG-008 |

## 3. Anatomy

```text
Badges (PAGE)
└─ Badge (COMPONENT_SET)
   └─ Type={base|light|informational|warning|error|success}
      ├─ Left icon (INSTANCE → Phosphor Presentation; visible)
      ├─ Label text (TEXT)
      └─ Right icon (INSTANCE → Phosphor Presentation; hidden)
```

## 4. Properties

| Propiedad destino | Tipo | Default | Fuente |
|---|---|---|---|
| Type | VARIANT | base | `type` |
| Badge text | TEXT | `Light` | `badge text#1241:27` |
| Show left icon | BOOLEAN | true | `show left icon#1234:7` |
| Show right icon | BOOLEAN | false | `show right icon#1234:0` |
| Left icon | INSTANCE_SWAP | Presentation Outline/Fill | `left icon#2817:26` |
| Right icon | INSTANCE_SWAP | Presentation Outline/Fill | `right icon#2817:33` |

Las keys internas `#...` se regeneran en Figma destino; no se copian sufijos de origen. Los swaps fuente tienen 1512 component sets Phosphor preferidos.

## 5. Variants

Se observan exactamente seis combinaciones del único eje `Type`: `base`, `light`, `informational`, `warning`, `error`, `success`. Todas las variantes miden 62×25 con el contenido de ejemplo `Light`. No se agregan estados no observados.

## 6. Sizes

No hay eje Size. Iconos 14×14; texto observado 12 px/16 px y dimensión 28×16. El ancho total se ajusta al texto; 62 px es la medida del ejemplo, no un mínimo de producto.

## 7. States

`Type` expresa apariencia/feedback, no interacción. No hay variantes hover, focus o disabled ni reacciones en el set. Un `color/border/disabled` aplicado a Light en la fuente no convierte Light en un estado disabled.

## 8. Behavior

No se observaron transiciones, click ni temporización. Las reglas de disparo, dismissal y actualización dinámica del contenido no se infieren del componente Figma.

## 9. Accessibility

La etiqueta es visible, pero no se verifican roles, anuncio de estados, significado no cromático ni teclado. La implementación Figma no certificará accesibilidad funcional de producto.

## 10. Design tokens

El [JSON aprobado](../../sources/inventories/tokens.inventory.json), digest `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`, gobierna nombres, aliases, valores, modos y descripciones. Los IDs siguientes son locales del destino.

| Type | Fondo | Texto | Iconos izquierdo/derecho |
|---|---|---|---|
| base | `color/background/default` `13:35` | `color/text/primary` `13:27` | `color/icon/primary` `13:20` |
| light | `color/background/subtle` `13:36` | `color/text/primary` `13:27` | `color/icon/primary` `13:20` |
| informational | `color/feedback/information/bg` `13:53` | `color/feedback/information/text` `13:54` | `color/feedback/information/icon` `13:56` |
| warning | `color/feedback/warning/bg` `13:45` | `color/feedback/warning/text` `13:46` | `color/feedback/warning/icon` `13:48` |
| error | `color/feedback/danger/bg` `13:49` | `color/feedback/danger/text` `13:50` | `color/feedback/danger/icon` `13:52` |
| success | `color/feedback/positive/bg` `13:41` | `color/feedback/positive/text` `13:42` | `color/feedback/positive/icon` `13:44` |

El prefijo completo de esos IDs es `VariableID:`. Light añade `color/border/strong` `VariableID:13:15` y `stroke/xs` `VariableID:12:41`. La fuente usaba `color/border/disabled` en una apariencia no deshabilitada; `strong` comparte su alias primitivo en los cuatro modos, pero se elige por su descripción de borde neutral perceptible, no solo por igualdad RGB. Los iconos derechos ocultos de cinco variantes usaban roles de texto; se normalizan a los roles de icono existentes. Ambas correcciones quedan para auditoría del usuario.

| Propiedad compartida | Variable destino |
|---|---|
| Familia / peso / tamaño | `font/family/base` `10:2` · `font/weight/regular` `10:3` · `font/size/xs` `10:8` |
| Interlineado / tracking | `font/line-height/xs` `12:7` · `font/letter-spacing/normal` `12:16` |
| Gap y padding 4 / padding 8 | `spacing/xs` `12:29` · `spacing/sm` `12:30` |
| Radio 4 | `radius/sm` `13:5` |

El set fuente liga `font/size/lg` a su propio padding de contenedor, no a un consumidor. Ese binding no visual queda fuera del componente destino.

## 11. Content rules

`Light` es el default editable de ejemplo en todas las variantes. No hay reglas observadas de longitud, truncamiento, pluralización ni localización. El icono no reemplaza la etiqueta por defecto.

## 12. Composition rules

Los dos iconos son instancias Phosphor independientes para poder mostrarlos, ocultarlos e intercambiarlos por separado. Su fill debe seguir el token de icono de la variante incluso cuando la instancia derecha esté oculta.

## 13. Responsive behavior

Ancho HUG ajustado al contenido y alto FIXED de 25 en Figma. No se observan breakpoints ni reglas de adaptación de texto largo.

## 14. Edge cases

Texto vacío, varias líneas, iconos dobles y contenido largo no están ejemplificados. La propiedad permite editar texto, pero no se inventan comportamientos de recorte.

## 15. Forbidden combinations

No hay combinaciones adicionales de ejes; los booleanos de icono no crean variantes. Estados ausentes no se declaran prohibidos para producto: solo fuera de este set.

## 16. Design ↔ Code mapping

La página `Badges` es un nombre funcional delegado, coherente con Buttons/Chips, no una copia del nombre decorado `❖ Badge ✅`. No se define API React ni CSS en esta versión.

## 17. Acceptance criteria

| ID | REQ | Evidencia posterior |
|---|---|---|
| AC-BDG-001 | 001 | Página única `Badges`, set único `Badge`, IDs reales y otras páginas intactas. |
| AC-BDG-002 | 002 | Seis variantes Type únicas, default base. |
| AC-BDG-003 | 003 | Anatomía 3 hijos, auto layout HUG/FIXED, medidas/padding/gap/radio leídos y captura sin recortes. |
| AC-BDG-004 | 004 | TEXT y dos BOOLEAN conectadas en las seis variantes, defaults exactos. |
| AC-BDG-005 | 005 | Doce instancias Phosphor con key default correcta; swaps independientes, preferidos y sin detach. |
| AC-BDG-006 | 006 | Fills y stroke por Type ligados a IDs locales semánticos, incluidos ambos iconos. |
| AC-BDG-007 | 007 | Readback tipográfico y de spacing/radio/stroke, aliases resueltos por modo. |
| AC-BDG-008 | 008 | Estado, mapa, diferencias, captura y QA registrados; `user_audit: PENDING`. |

## 18. Examples

- `Type=base`, texto `Light`, icono izquierdo visible y derecho oculto.
- `Type=warning`, texto editable y ambos iconos configurables con color de iconografía warning.

## 19. Source of truth

El [set Badge fuente](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1234-65377) sustenta estructura y estilos observados; [Phosphor Icons](https://www.figma.com/design/xZSksKpcQTp5H3C4dZApBL/Phosphor-Icons?node-id=7484-1322) y DEC-ICONS-001 sustentan la dependencia. El JSON aprobado define las variables de AI-Design-System. Las tres anomalías/normalizaciones se preservan en el YAML y no se esconden como equivalencia exacta.

## 20. Change management

Cambiar variantes, defaults, icono o mapeo semántico requiere nueva versión y QA. La delegación permite construir tras QA documental sin afirmar aprobación del contenido; la auditoría humana puede aceptar o pedir revisión.

## 21. Changelog

| Versión | Fecha | Cambio |
|---|---|---|
| 0.1.0 | 2026-09-23 | Primer candidato para seis apariencias Badge y mapeo a variables locales. |
