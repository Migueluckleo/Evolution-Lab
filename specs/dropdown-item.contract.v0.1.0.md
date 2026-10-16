---
contract_schema: sdd-project/0.2
contract_id: DROPDOWN-ITEM-001
name: Dropdown Item
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-28
review_targets: [figma]
figma_page_name: Select
sources: [SRC-FIGMA-SELECT-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001]
data_refs: [sources/inventories/tokens.inventory.json, sources/figma-snapshots/select.source.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, CHECKBOX-001, LOADER-001]
user_audit: PENDING
---

# Dropdown Item 0.1.0 · contrato de construcción

## 1. Purpose
Fila reutilizable de una lista desplegable. Página funcional **Select**, compartida solo con futuras composiciones de esa familia. Reconstrucción Figma, no implementación web.

## 2. Contract
REQ-DI-001: reconstruir 18 variantes del set fuente `2479:11730` en `9zs5RMR8LB5wHjW9Bd59BA`, como un set local **Dropdown Item** en AI Design System `tj3WIBEZDGLVs7MJWKCwgf`. No importar ni desacoplar el set legado. Las instancias de Checkbox y Loader reutilizan los componentes locales existentes. Iconos Phosphor Eye/X Outline Light por key real; no redibujarlos.

## 3. Anatomy
Auto layout horizontal de altura fija: Selector container opcional de 44 px; Content con padding horizontal y gap de 16 px; Eye opcional, Label flexible, Secondary text opcional, X opcional, Loader opcional. Separador absoluto inferior representado como trazo, no como fill de fondo. Contenido y selector no tienen pinturas propias.

## 4. Properties
REQ-DI-002: Size={Large,Medium,Small}; State={Default,Hover,Disabled,Focus}; Selected={False,True}; Type={Base,Header}. Defaults Large/Default/False/Base.
Dos TEXT: Label="Option text", Secondary text="2nd Column".
Seis BOOLEAN en false: Show checkbox, Show leading icon, Show trailing icon, Show divider, Show secondary text, Show loading.
Dos INSTANCE_SWAP: Leading icon=Eye, Trailing icon=X. El segundo swap es mejora delegada frente al icono derecho fijo de la fuente; no crea variantes. Las propiedades de texto/visibilidad se conectan a todas las variantes. Preferencias de swap limitadas a dependencias verificadas; no copiar los 1512 candidatos de la biblioteca fuente.

## 5. Variants
REQ-DI-003: conservar únicamente las 18 combinaciones observadas, no completar un producto cartesiano:
- Por cada Size: Base/Selected=False en Default, Hover, Disabled y Focus (12).
- Por cada Size: Base/Selected=True/State=Default (3).
- Por cada Size: Header/Selected=False/State=Default (3).
El mapa de IDs fuente en el snapshot es evidencia canónica de la matriz. Header conserva la misma presentación observada que Base Default; no inventar encabezados en negritas.

## 6. Sizes
REQ-DI-004: ancho inicial 251 px; alturas Large/Medium/Small 48/40/32 px; iconos, Loader y Checkbox 24/20/16 px. Escalar instancias proporcionalmente, no recortar sus vectores. Selector container=44 px en los tres tamaños. Content ocupa el ancho restante. Textos de 16/14/14 px.
Normalización delegada: interlineado AUTO observado 22/19/19 → tokens 24/20/20 px; Secondary text deja su altura fija de 16 px para no recortar. Ambos textos truncan en una línea; el secundario mantiene ancho inicial 101.5 px. No cambiar altura del control. Dimensiones observadas se conservan literales, no se vinculan a tokens GAP como si fueran WIDTH_HEIGHT.

## 7. States
REQ-DI-005: fondo blanco salvo Hover neutral300 y Selected superficie de marca. Texto e iconos primary, disabled o brand según estado/selección. Focus añade stroke/md=2 px OUTSIDE y radius/sm=4; resto radius/none. No modificar los RGB por contraste.
Normalización delegada del checkbox oculto: Selected=True usa Checkbox Selected/Default; Disabled usa Unselected/Disabled; Hover usa Unselected/Hover; Focus conserva Unselected/Default para evitar doble anillo. La fuente deja Unselected/Enabled en todas las filas, incluso las seleccionadas; corregir esa incoherencia sin cambiar el aspecto por defecto.
Loader conserva Primary en todos los estados, como la fuente; esta entrega no redefine sus ciclos. No usar tokens de texto sobre iconos.

## 8. Behavior
REQ-DI-006: cero reacciones propias, igual que la fuente. Los estados son presentaciones, no lógica funcional de selección, teclado o carga. Loader mantiene la animación del componente local. Header no adquiere por inferencia una acción seleccionable.
Las composiciones 2488:13364–13372 son ejemplos fuente, no un set Select. Su construcción y cualquier interacción de apertura/cierre quedan fuera de este contrato, pendientes del siguiente bloque. No declarar la familia Select completa con esta entrega.

## 9. Accessibility
REQ-DI-007: medir texto/fondo y documentar limitaciones con asterisco sin recolorear. Disabled comunica falta de disponibilidad, no un valor vacío. Alturas Medium/Small inferiores a 44 px se documentan como limitación táctil contextual. El contrato no certifica ARIA ni accesibilidad frontend. Mantener foco visible y textos editables.

## 10. Design tokens
REQ-DI-008: el JSON canónico es `sources/inventories/tokens.inventory.json`, SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`. Nombres, tipos, modos, valores, aliases y description proceden de ese JSON; no duplicar definiciones editables. El mapa local y sus cadenas observadas están en `sources/figma-snapshots/select.target-tokens.v0.1.0.json`. Cero variables, primitivas o estilos nuevos.

| Parte | Token semántico | Variable destino |
|---|---|---|
| Fondo normal / Hover | color/background/default / color/background/muted | VariableID:13:35 / VariableID:13:37 |
| Fondo Selected | color/surface/brand | VariableID:13:69 |
| Texto normal / Disabled / Selected | color/text/primary / color/text/disabled / color/text/brand | VariableID:13:27 / VariableID:13:30 / VariableID:13:32 |
| Iconos normal / Disabled / Selected | color/icon/primary / color/icon/disabled / color/icon/brand | VariableID:13:20 / VariableID:13:24 / VariableID:13:25 |
| Divisor (trazo) | color/border/strong | VariableID:13:15 |
| Foco (trazo) | color/focus/ring | VariableID:13:71 |
| Tipografía | font/family/base, font/weight/regular | VariableID:10:2 / VariableID:10:3 |
| Tamaño Large / Medium-Small | font/size/md / font/size/sm | VariableID:10:10 / VariableID:10:9 |
| Interlineado Large / Medium-Small | font/line-height/md / font/line-height/sm | VariableID:12:9 / VariableID:12:8 |
| Tracking | font/letter-spacing/normal | VariableID:12:16 |
| Padding/gap | spacing/lg / spacing/none | VariableID:12:32 / VariableID:12:18 |
| Radio normal / Focus | radius/none / radius/sm | VariableID:12:39 / VariableID:13:5 |
| Divisor / Focus | stroke/xs / stroke/md | VariableID:12:41 / VariableID:13:3 |

El texto Selected usa color/text/brand en lugar de interactive/primary/default; los iconos usan color/icon en lugar de text. Conservan RGB Contable, corrigen semántica. El separador rectangular fuente que consumía background/muted se sustituye por un stroke de color/border/strong con el mismo RGB. Todos los roles heredan los cuatro modos; no fijar un tema. Focus sigue la identidad de foco constante del JSON, no se convierte silenciosamente en marca.

## 11. Content rules
Label y Secondary text son ejemplos, no datos de producto. Visibilidades independientes como la fuente; los iconos no implican acciones X/Eye por sí solos. Cadenas largas deben truncar sin superar la altura.

## 12. Composition
Instancias de Checkbox set149:199 y Loader set378:1869, sin duplicar sus mains. Eye reutiliza key e59dc310706bfe83ca2f09b69441d517c7372db1; X key 4046be769b352c4e707a75fd12c03a00eb63f3f4. Binding de paints vectoriales en instancias del consumidor, no modificación global de los masters Phosphor.
Prueba de opciones visibles a ancho ampliado y a ancho inicial. El consumidor debe dar ancho suficiente si habilita simultáneamente todas las opciones; no inventar ancho mínimo de producto.

## 13. Implementation and readiness
Operación CREATE. Preparación Figma READY tras QA documental y comparación automática de los 24 roles con el JSON. Fuentes y dependencias identificadas; no hay incertidumbre material bloqueante para estas 18 presentaciones. Los campos fuente y destino permanecen separados.
Guía de página en español y descripción canónica del set. No Code Connect ni frontend en alcance. No publicación de biblioteca.
REQ-DI-009: QA post-build debe comprobar 18 nombres únicos y geometría, 10 propiedades no-variant conectadas, 72 instancias directas de dependencias (más las internas heredadas), aliases locales/scopes, cuatro modos, captura visual y prueba de opciones. Conservar readback/IDs y promover a specs solo con QA documental y técnico PASS.

## 14. Evidence and unresolved
OBSERVED: snapshot fuente, 18 variantes, 72 instancias, 19 variables referenciadas directa o indirectamente; captura de set y dependencias invisibles inspeccionadas.
DERIVED: matriz acotada, roles destino y normalizaciones enumeradas arriba.
UNRESOLVED: lógica web/teclado y composición Select; no bloquean este artefacto visual ni se presentan como implementadas.
Auditoría humana PENDING por delegación. Las limitaciones de contraste se consolidan por excepciones; no pedir aprobación rutinaria por variante.
