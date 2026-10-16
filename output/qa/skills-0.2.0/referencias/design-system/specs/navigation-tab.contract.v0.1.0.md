---
contract_schema: sdd-project/0.2
contract_id: NAVIGATION-TAB-001
name: Tab
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-24
review_targets: [figma]
figma_page_name: Navigation
sources: [SRC-FIGMA-NAVIGATION-TAB-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-MIGRATION-VISUAL-FIDELITY-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/navigation-tab.source.component-contract.yaml, drafts/foundations/ai-design-system.navigation-tab-borders.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-NAVIGATION-TAB-BORDERS-001]
user_audit: PENDING
---

# Navigation · Tab 0.1.0

## 1. Purpose

Elemento visual de navegación por pestañas. `Tab=On` indica pestaña activa; `State=Disabled` indica indisponibilidad y no equivale a Off. No se define aquí la lógica de selección o navegación web.

## 2. Contract

Construir en la página existente `Navigation` un único set local `Tab` con las 17 variantes [observadas](../drafts/contracts/navigation-tab.source.component-contract.md) y enumeradas en [YAML](../drafts/contracts/navigation-tab.source.component-contract.yaml), no las 20 combinaciones cartesianas posibles. La variante `Type=Dynamic, Tab=On, State=Selected` mantiene su anatomía excepcional y no se extrapola a otros ejes.

## 3. Anatomy

Base: dos instancias ImageSquare Outline/Light, etiqueta y Dot oculto; línea inferior. Dynamic ordinario: mismas piezas y divisor externo, con fondos según estado. Dynamic Selected: una instancia ImageSquare Outline/Regular y etiqueta dentro de `content`, sin Dot ni divisor. Mantener instancias remotas enlazadas, sin detach.

## 4. Properties

Tres ejes `Type` (`Base|Dynamic`), `Tab` (`On|Off`) y `State` (`Default|Hovered|Selected|Focused|Disabled`). Texto `Label` editable con default `Tab title`; booleanas `Show Dot`, `Show Left Icon`, `Show Right Icon` y `Show Divisor`; swaps `Left Icon` y `Right Icon`. Selected solo ofrece los controles aplicables a su anatomía; no se fabrican el segundo icono, Dot o divisor para completar propiedades.

## 5. Variants

Base: On/Off × Default/Hovered/Focused/Disabled = ocho. Dynamic: On/Off × Default/Hovered/Focused/Disabled = ocho, más On/Selected = una. Total 17. Los nombres de variantes se normalizan en Title Case sin cambiar su significado.

## 6. Sizes

Base 135×42 px en todos los estados. Dynamic On ordinario 136×35, Dynamic Off 133×35; Dynamic Selected 135×35. Iconos y Dot 16×16; Manrope 14 px; gap 8, padding horizontal 16 y vertical 8 para variantes ordinarias; radio Dynamic 8. Selected conserva su centrado propio. El texto por defecto determina estas muestras; no hay regla responsive fuente.

## 7. States

Base On usa línea inferior de 2 px, texto/iconos de marca y peso Bold; Hovered usa marca fuerte, Focused agrega efecto exterior azul de 2 px y subrayado 2 px, Disabled atenúa texto/iconos/borde. Base Off usa línea inferior de 1 px, texto/iconos primarios y peso Regular; Hovered conserva el color original de su stroke, Focused agrega fondo blanco y efecto exterior de 2 px, Disabled atenúa bordes/textos/iconos.

Dynamic On usa fondo de superficie de marca, acento en Hovered, fondo blanco con efecto exterior en Focused y fondo Disabled en Disabled. Dynamic Off normalmente no tiene fondo; Hovered muestra contorno sutil, Focused muestra fondo blanco y efecto exterior, Disabled atenúa texto/iconos. El divisor permanece claro en variantes ordinarias. Selected mantiene el fondo de superficie de marca, pero texto/icono primarios y peso Regular como en la fuente.

## 8. Behavior

La fuente solo evidencia cuatro transiciones `ON_HOVER → CHANGE_TO`, una por variante Default ordinaria hacia su Hovered. El destino las reproduce y leyó de vuelta sus cuatro destinos exactos. No inferir clic, reversión, selección automática, teclado o ARIA.

## 9. Accessibility

No afirmar accesibilidad web, rol tab, `aria-selected`, gestión de foco ni orden de tabulación a partir del Figma.

## 10. Design tokens

El [JSON aprobado](../sources/inventories/tokens.inventory.json) gobierna roles preexistentes y la [extensión Tab](../drafts/foundations/ai-design-system.navigation-tab-borders.v0.1.0.json) gobierna dos roles nuevos. Fills: `color/background/default|disabled`, `color/surface/brand|brand/accent`; texto: `color/text/primary|brand|brand/strong|disabled`; vectores: `color/icon/primary|brand|hover|disabled`; borde: `color/border/brand|hover|subtle|navigation-tab/subtle|navigation-tab/disabled`; efecto: `color/focus/effect-outer`. Dot: roles de feedback de icono y borde on-brand existentes. Geometría: spacing, radius y stroke locales compatibles. No usar un token de texto o superficie sobre un stroke, aunque el RGB coincida.

El borde sutil nuevo aliasa blue/200, green/200, red/200 y purple/200; el borde Disabled nuevo aliasa neutral/400 en cuatro modos. `color/border/subtle` compartido solo se usa para Base Off Hovered, donde el color de la fuente procede de superficie/accent y coincide con ese rol por modo. `color/border/hover` existente corresponde al borde fuerte de Base On Hovered. El efecto Focus existente apunta a blue/500 en cuatro modos, como la fuente.

## 11. Content rules

`Tab title` es texto demo editable. Dot permanece oculto por defecto. No derivar conteos ni notificaciones desde su nombre.

## 12. Composition rules

Importar ImageSquare Outline/Light por key fuente `f273018f11d7d4e938078bd0b21b0b3a9e7f2634`, Dot por `309ba73acbf0853df307a033c09a1a40856357d5` e ImageSquare Outline/Regular de Selected por `7e704a5154aa535ff118cc9d6970e0bfce641037`. Las tres keys se resolvieron por importación en el destino. Ocultar los fills blancos de los frames ImageSquare como en la fuente; ligar solo los vectores visibles a roles iconográficos. El texto anidado del Dot usa color, familia y peso locales; su tamaño de 8 px permanece literal observado porque el inventario aprobado no contiene una primitiva de 8 px.

## 13. Responsive behavior

No documentado. Las medidas son placeholders de biblioteca.

## 14. Edge cases

Selected no tiene contraparte Off ni Base. Su único ImageSquare no hereda los swaps ni booleanas de las variantes ordinarias. La fuente declara miles de preferencias de swap; no copiar listas de 1512 referencias sin necesidad de representar las tres dependencias visibles.

## 15. Forbidden combinations

No crear `Base/Selected` ni `Dynamic/Off/Selected`; no convertir Off en Disabled; no cambiar el color por contraste ni usar roles semánticos fuera de scope.

## 16. Design ↔ Code mapping

`Tab` y `State` son estados visuales de Figma, no modelo de selección frontend. El frontend necesitará un contrato posterior para exclusividad, navegación, eventos, teclado y ARIA.

## 17. Acceptance criteria

`AC-NAV-TAB-001`: 17 variantes exactas y propiedades aplicables. `AC-NAV-TAB-002`: medidas/anatomía e instancias importadas preservadas; Selected excepcional. `AC-NAV-TAB-003`: JSON, variables y 100 % de pinturas visibles con roles/scopes correctos; colores de cuatro modos fieles a fuente. `AC-NAV-TAB-004`: captura fuente/destino y efecto Focus concordantes. `AC-NAV-TAB-005`: documentar transiciones observadas o limitación de herramienta, IDs reales, Figma `UNPUBLISHED` y auditoría `PENDING`.

## 18. Examples

La muestra `Tab title` con iconos ImageSquare sirve a la demostración; no representa iconografía obligatoria de producto.

## 19. Source of truth

Este MD gobierna estructura/estados. El JSON aprobado y su extensión gobiernan nombres, modos, aliases, valores y descripciones de tokens. El [contrato transversal](MIGRATION-TOKEN-TRACEABILITY.contract.md) gobierna la trazabilidad.

## 20. Change management

Resolver anomalías visuales fuente con tokens del rol correcto y primitivas del mismo RGB. Cambios de variantes, comportamiento, color o iconografía requieren nueva enmienda.

## 21. Changelog

- 0.1.0 delegado: 17 variantes observadas, dos extensiones de borde sincronizadas, cuatro prototipos hover y construcción Figma con QA técnico; auditoría humana pendiente.
