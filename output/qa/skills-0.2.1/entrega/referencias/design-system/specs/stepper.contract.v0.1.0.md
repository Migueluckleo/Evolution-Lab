---
contract_schema: sdd-project/0.2
contract_id: STEPPER-001
name: Stepper Item
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-24
review_targets: [figma]
figma_page_name: Steppers
sources: [SRC-FIGMA-STEPPER-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/stepper.source.component-contract.yaml, drafts/foundations/ai-design-system.stepper-colors.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-STEPPER-COLORS-001]
user_audit: PENDING
---

# Stepper Item 0.1.0 · contrato de construcción

**Vigencia cromática:** [la enmienda 0.1.1](stepper.brand-theme.amendment.v0.1.1.md) sustituye solo los colores fijos de Checked/Default y `AC-SI-003`. Las demás reglas de este contrato siguen vigentes.

## Propósito y fuente

Representar una etapa etiquetada de un flujo secuencial, en disposición vertical u horizontal. La [observación de la fuente](../drafts/contracts/stepper.source.component-contract.md) y su [YAML](../drafts/contracts/stepper.source.component-contract.yaml) gobiernan anatomía, tamaños y valores fuente. Este Stepper no sustituye `Steps`, que es un indicador compacto de puntos. Crear una página propia `Steppers` en AI Design System.

## Sets, propiedades y composición

Crear `Stepper Item` con 18 variantes `Orientation={Vertical,Horizontal}` × `State={Checked,Default,Inactive}` × `Position={Start,Middle,End}`. Mantener un subcomponente `Stepper Connector` de ocho variantes `Orientation={Vertical,Horizontal}` × `State={Checked,Default}` × `Position={Start,End}`. `Inactive` reutiliza el conector Default; no fabricar una novena apariencia. Las dos piezas del conector a cada lado de Middle deben ser instancias locales, no copias rasterizadas ni remotas.

Conservar `Step`, `Title` y `Caption` como contenidos de texto editables y `Show step`/`Show caption` como controles booleanos cuando Figma permita exponerlos sin alterar medidas. El icono CheckFat de 16×16 debe ser una instancia intercambiable de Phosphor, no vector aplanado; la fuente expone icon swap. En el destino se prefiere mantener esa propiedad. Registrar si alguna exposición de propiedad no se puede reproducir técnicamente, sin decir que está validada.

| Orientación | Start | Middle | End |
|---|---:|---:|---:|
| Horizontal | 116×97 | 200×97 | 161×97 |
| Vertical | 117×57 | 117×104 | 117×68 |

El círculo mide 32×32 px. En Horizontal: círculo en x=0 para Start o x=84 para Middle/End; conectores visibles de 80×4 px en x=0 y/o x=120 según posición; detalles en y=40 y x=0 o 84. En Vertical: círculo en y=0 para Start o y=36 para Middle/End; conectores visibles 4×21 para Start y 4×32 para Middle/End, centrados en x=14; detalles en x=40 y y=0/23.5/11. Las líneas emplean extremos redondeados de 8 px junto al círculo, cero en el extremo exterior. No copiar el bar blanco oculto de Horizontal/End.

## Tokens y tipografía

Los ocho roles nuevos se definen únicamente en el [JSON de extensión](../drafts/foundations/ai-design-system.stepper-colors.v0.1.0.json). Cada rol aliasa una primitiva **ya existente y del mismo RGB fuente** en los cuatro modos. Los fondos del círculo tienen scope `FRAME_FILL`, conectores `SHAPE_FILL` y textos `TEXT_FILL`; los consumidores se vinculan al rol semántico, nunca directamente a la primitiva. El icono blanco de Checked/Default usa `color/icon/on-brand`; el gris de Inactive usa `color/icon/secondary`, ambos `SHAPE_FILL` y ya existentes. Radio de círculo `radius/full` donde coincida; separación con variables locales del valor correspondiente.

Los textos usan familia Manrope; Step y Caption Regular 10 px, Title SemiBold 14 px. Vincular familia, peso y tamaño a variables locales. La fuente mide 15/21 px de línea; si la escala destino solo ofrece 16/20 px, elegir esos tokens existentes, documentar la desviación de 1 px y mantener las cajas de 77×15/21/15 y el bloque de 77×57 px para preservar la composición visual. No crear primitivas tipográficas nuevas para una desviación menor sin decisión material.

## Estados, contenido y comportamiento

Checked es verde, Default azul, Inactive gris. La fuente conserva el icono CheckFat en todos los estados; solo cambia su color. Los rótulos de muestra `STEP 1`, `Step details` y `Caption` no son datos calculados. Cero reacciones observadas: no atribuir navegación, click, progreso automático o cálculo de estado. El diseño no demuestra foco, teclado ni anuncios accesibles; estos requisitos son del futuro contrato de comportamiento/frontend.

## Criterios de aceptación

- `AC-SI-001`: página `Steppers`, 18 variantes públicas y ocho conectores locales, sin dependencia de componentes de la Librería anterior.
- `AC-SI-002`: geometría de seis tamaños, conectores, posiciones y textos según la fuente; instancias de icono y conectores sin detach.
- `AC-SI-003`: ocho roles nuevos con alias exacto en cuatro modos, scope correcto y bindings reales; ninguna primitiva nueva ni token de texto en forma.
- `AC-SI-004`: contenido y visibilidad editables; si la propiedad de intercambio de icono no se logra, registrar desviación y no declarar ese criterio `PASS`.
- `AC-SI-005`: QA técnico, IDs separados de fuente/destino, auditoría humana `PENDING` y biblioteca `UNPUBLISHED`.

## Gestión de cambios

El contrato delegado permite construir y probar la biblioteca, no aprobarla ni publicarla. No renombrar `Default` como paso actual sin una regla explícita de comportamiento. La composición de varios Stepper Items en un flujo es ejemplo, no otro set inferido.
