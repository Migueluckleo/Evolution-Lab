---
contract_schema: sdd-project/0.2
contract_id: STEPS-001
name: Steps
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-24
review_targets: [figma]
figma_page_name: Steps
sources: [SRC-FIGMA-STEPS-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-MIGRATION-NEAREST-PRIMITIVE-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/steps.source.component-contract.yaml, drafts/foundations/ai-design-system.steps-colors.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-STEPS-COLORS-001, BUTTON-001]
user_audit: PENDING
---

# Steps 0.1.0 · contrato de construcción

**Vigencia cromática:** [la enmienda 0.1.1](steps.brand-theme.amendment.v0.1.1.md) sustituye solo la tabla de acentos fijos y `AC-ST-003`. Las demás reglas siguen vigentes.

## Propósito y fuente

Mostrar una posición dentro de una secuencia discreta. La [observación de la fuente](../drafts/contracts/steps.source.component-contract.md) y su [YAML](../drafts/contracts/steps.source.component-contract.yaml) conservan los IDs, la geometría y las contradicciones de la Librería anterior. La página destino se llama `Steps`; no se reutiliza la página ni el archivo de origen.

## Estructura y variantes

Crear un set público `Steps` con seis variantes: `On color={On White, On Primary}` × `Type={Gallery, Numbers, Gallery only}`. `Gallery` mide 191×32 px y contiene botón anterior de 76×32, tres dots de 40×8 y botón siguiente de 75×32. `Numbers` mide 196×32 px y sustituye los dots por el ejemplo estático `5 / 6` de 45×20 px. `Gallery only` mide 40×8 px y contiene solo dots visibles. Sin fondo propio: el eje `On color` expresa contexto.

Crear además subcomponentes locales: `Steps Dot` de cuatro variantes `On color={On White, On Primary}` × `Selected={True, False}`, caja 8×8, dot de 8 px seleccionado y 6 px no seleccionado; y `Steps Combination` de 27 variantes `Number=02…07`, `Step=1…Number`. Cada combinación tiene una única selección, centros separados 16 px y ancho `16×Number−8` px. Las combinaciones no añaden states, breakpoints ni números fuera de 02…07. Las variantes públicas usan instancias locales donde la fuente ofrece esa composición; el caso cromático legado `On Primary / Gallery` se distingue sin introducir una dependencia remota de la librería antigua.

Los botones `Back` y `Next` se construyen con instancias del `button` local de AI Design System, variante `type=text, size=small, state=default`; ajustar sus propiedades de texto, iconos y visibilidad sin desprenderlos. Si la API de Figma no permite configurar la instancia local sin alterar el tamaño 76/75 px, registrar ese límite y usar subcomponentes locales equivalentes, no importar el botón de la Librería antigua. `Back`, `Next` y `5 / 6` son ejemplos editables, no textos calculados.

## Tokens y scopes

En esta versión base, el [JSON 0.1.0](../drafts/foundations/ai-design-system.steps-colors.v0.1.0.json) definía los siete roles; para la implementación vigente, sus aliases y descripciones se sustituyen exclusivamente por el [JSON 0.1.1](../drafts/foundations/ai-design-system.steps-colors.v0.1.1.json) según la enmienda. Cada rol existe en la colección local `semantic` con cuatro aliases a una primitiva *ya existente*; no se crean primitivas. Los dots son SHAPE_FILL, el contador es TEXT_FILL. Vincular directamente las formas y el texto al rol semántico, nunca a la primitiva. Los botones usan `color/text/primary` y `color/icon/primary` sobre blanco, `color/text/on-brand` y `color/icon/on-brand` sobre primario; el contador On Primary usa `color/text/on-brand`. Tamaño de letra: `font/size/sm` (14 px) y estilo Manrope Regular donde el componente local lo permita. Separaciones y radios se vinculan a variables locales equivalentes cuando existe un match de valor y scope.

La tabla siguiente registra la observación de origen y el alias de la versión base en Contable; los alias por tema vigentes de los tres acentos se consultan únicamente en el JSON 0.1.1.

| Caso fuente | Alias local | Resultado | Tratamiento |
|---|---|---|---|
| On White, seleccionado `#3255F7` | `color/blue/400` | exacto | dot semántico |
| On White, no seleccionado `#E2E8F0` | `color/neutral/300` | exacto | dot semántico |
| `.Dot` On Primary, seleccionado blanco | `color/neutral/100` | exacto | dot semántico |
| `.Dot` On Primary, no seleccionado `#7D9AFF` | `color/blue/300` | aproximado | excepción de paleta |
| Gallery legada On Primary, seleccionado `#0073EA` | `color/blue/300` | aproximado | rol separado por contradicción de origen |
| Gallery legada On Primary, no seleccionado `#DCDFEC` | `color/neutral/300` | aproximado | rol separado por contradicción de origen |
| Contador On White aprox. `#323338` | `color/neutral/800` | aproximado | texto semántico |

`On Primary / Gallery only` conserva los dots On White, tal como la variante pública observada. Es una anomalía de la fuente, no un uso recomendado para una nueva interfaz. La paleta contextual blanca/azul claro del subcomponente no sustituye silenciosamente a las dos variantes públicas inconsistentes. Se documenta en la auditoría por excepciones.

## Comportamiento, accesibilidad y límites

La fuente no demuestra transición entre pasos, activación de botones, límites del contador ni cálculo desde datos. La única reacción interna `ON_HOVER → CHANGE_TO` carece de destino; no reproducir un prototipo roto. En frontend, la posición actual y el total deberán proceder de datos y tener una descripción accesible; el ejemplo Figma no implementa `aria-current`, navegación por teclado ni anuncios de cambio. No presentar `5 / 6` como valor dinámico.

## Criterios de aceptación

- `AC-ST-001`: página `Steps`, set público de seis variantes, `Steps Dot` de cuatro y `Steps Combination` de 27, sin dependencias de la Librería anterior.
- `AC-ST-002`: tamaños públicos 191×32, 196×32, 40×8; puntos y espaciado indicados; botones y textos editables.
- `AC-ST-003`: siete variables semánticas locales, aliases a primitivas existentes en cuatro modos, scopes y bindings directos verificados contra JSON.
- `AC-ST-004`: comparación visual fuente/destino y diferencias de color documentadas, incluidas las dos contradicciones de On Primary; sin reacciones inventadas.
- `AC-ST-005`: IDs de fuente y destino separados, QA técnico, auditoría humana `PENDING` y librería `UNPUBLISHED` registrados.

## Control de cambios

Este contrato delegado autoriza construcción y QA técnico para la migración acotada, no aprobación humana ni publicación de la biblioteca. Cualquier cambio al significado de `On Primary`, al contenido calculado o a la paleta requiere enmienda y nueva medición.
