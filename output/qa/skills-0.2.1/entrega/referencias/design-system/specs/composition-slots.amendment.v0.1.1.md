---
contract_id: COMPOSITION-SLOTS-002
version: 0.1.1
status: DELEGATED_FOR_BUILD
date: 2026-09-30
user_audit: PENDING
implementation_status: VALIDATED
slot_applicability: REQUIRED
---

# Slots · Steps, Pagination y leyendas Charts

## Alcance y autoridad

Continuación explícita del usuario del 30 de septiembre de 2026. Aplica P-SLOTS 0.1.0 y las decisiones delegadas de migración. Complementa, sin sustituir otras familias ni su QA, [COMPOSITION-SLOTS-001](composition-slots.amendment.v0.1.0.md).

Enmienda exclusivamente Anatomy, Properties, Composition rules, Responsive behavior, Edge cases y Acceptance criteria de [Steps 0.1.0](steps.contract.v0.1.0.md), su [enmienda de marca 0.1.1](steps.brand-theme.amendment.v0.1.1.md), [Pagination 0.1.0](navigation-pagination.contract.v0.1.0.md) y [Charts 0.1.0](../drafts/contracts/charts.contract.v0.1.0.md). El contrato Charts aún está en su ubicación histórica; este cambio no acredita su revisión cromática global ni promoción automática. No modifica observaciones fuente.

## Anatomía y propiedades

| Región | Propietario y mecanismo | Contenido de muestra / permitido |
|---|---|---|
| Steps / Indicators | Slot nativo dentro de Steps Combination; el grupo legacy de Gallery On Primary también requiere Slot editable. Gallery y Gallery only reutilizan Combination. | Presets de 2–7 indicadores; no son límites. Instancias locales Steps Dot. El grupo legacy conserva sus roles y geometría particulares. |
| Pagination / Pages | Slot nativo Pages por variante, propiedad compartida en el set. | Tres celdas de página y un separador son muestra. Celdas de página y separadores con los bindings semánticos y tipográficos existentes. |
| Chart Header / Legend | Slot nativo de leyendas; conservar Show legend. | Tres instancias locales Chart Legend Label, no máximo. |
| Progress Chart Item / Legend rows | Slot nativo vertical para filas completas de Detail; Top conserva el Slot oculto. | Dos filas de muestra, cada una con tres instancias Chart Legend Label. La cantidad de filas no está limitada a dos. Los textos de cada fila son editables; no se infiere un modelo de datos por sus valores de demo. |

Se permiten insertar, eliminar, reordenar y sustituir hijos desde instancias vinculadas, sin detach ni editar principales. Los límites de producto mínimo/máximo siguen UNRESOLVED; no se configuran límites artificiales. El contenido admitido es una recomendación semántica documentada, no una restricción técnica que Figma no haya demostrado.

## Composición, dimensiones y temas

- Steps: indicadores de caja 8×8 y separación 8; anfitrión y grupo crecen horizontalmente por contenido. Conservar Back/Next y Count, las seis variantes públicas, los cuatro Dot y los 27 presets Combination. Number/Step describen el preset; una composición personalizada no calcula selección ni cantidad automáticamente. No cambia la regla de marca de la enmienda 0.1.1.
- Pagination: Pages horizontal HUG, gap 4; filas de celdas 26 de alto. El contenedor completo crece con la lista. Mantener controles, selector y padding existentes; no implementar algoritmo de rangos, ellipsis, scroll o navegación.
- Celdas Pagination: mínimo de ancho 26, altura 26 y padding horizontal ligado a spacing/sm; HUG permite números largos sin solapar celdas. Con la muestra original, las cinco variantes siguen en 354×66. Las celdas son frames editables del Slot, no nuevas variantes públicas ni instancias desacopladas. Clonar una celda existente conserva roles y tipografía; una celda insertada desde otra biblioteca necesita el mapeo contextual antes de considerarse conforme.
- Charts: Header conserva tres leyendas iniciales y su visibilidad; cada fila de Detail distribuye sus elementos en el ancho disponible. El anfitrión conserva sus medidas iniciales. Las leyendas largas requieren HUG o truncado explícito conforme a evidencia de QA; no se aceptan solapamientos silenciosos.
- Ajuste de layout Charts derivado del QA: Header y sus leyendas usan HUG; las leyendas conservan su ancho mínimo inicial. Detail usa FILL en Header, Body y Bar para responder a 320 px sin desbordar el track; el relleno de muestra sigue midiendo 247 px, no es una proporción calculada. Las celdas de leyenda son FILL con texto truncado a una línea. Los principales conservan 638×48 y 639×104.
- Los modos Contable, Administrativo, Servicios y Personas se heredan con bindings semánticos. Steps y Charts no necesitan variables nuevas. Pagination incorpora exclusivamente la [extensión contextual de estado](foundations.pagination-slot-state.amendment.v0.1.0.md): ocho roles de color y un grosor, todos aliases de tokens existentes; no hay primitivas ni colores nuevos. Ningún paint nuevo se vincula directamente a primitivas.
- La propiedad SLOT conserva contenido personalizado; no equivale a un algoritmo que propague State, On color, Step o selección a los hijos. Las composiciones personalizadas son responsabilidad del consumidor: ajustar las propiedades de sus hijos al contexto. QA debe comprobar y registrar qué preserva realmente cada cambio de variante. Si un cambio hace incorrecta la apariencia, registrar la limitación y no certificar propagación automática ni un PASS incondicional.
- Vacío: probar estructura del editor sin inferir una política de producto. El placeholder del Slot no es un estado vacío de producto. Ancho estrecho: crecimiento/overflow documentado; no se introduce scroll automático.
- Excepción a la limitación de propagación: Pagination sí debe imponer Disabled al contenido conforme del Slot mediante la colección contextual, manteniendo cantidad, textos y orden. Enabled recupera los estados de las celdas personalizadas, no calcula automáticamente qué celda seleccionar al cambiar Active/Hover/Focus.
- Steps conserva composiciones separadas para Gallery On White y el grupo legacy On Primary porque sus roles son distintos. Cambiar de contexto muestra la composición de ese contexto, sin recolorear ni destruir la del anterior. Gallery↔Gallery only y el regreso desde Numbers deben conservar la composición del mismo contexto; documentar la evidencia real.

## Criterios de aceptación

Aplicar SLOT-QA-01…09: readback de tipo SLOT y propiedad real; edición de instancia vinculada; cantidades 0, 1, menor, muestra y mayor; reordenar/sustituir; texto largo/ancho reducido; cuatro modos; cambios de variante; defaults y principales ajenos conservados. Los IDs y mediciones reales se registran en evidencia de implementación, no se deducen.

QA documental y de implementación: PASS acotado, con [matriz de controles y excepciones](../qa/implementations/composition-slots.v0.1.1.figma.review.md) y [estado/IDs](../implementations/figma/composition-slots.v0.1.1.state.json). La corrección final de Progress sustituye los Slots de celdas por el Slot de filas completas; [QA final](../qa/implementations/composition-slots.v0.1.1.charts-rows.json) prueba0/1/2/5 filas, modos, cambios Top/Detail y320px. No equivale a aprobación humana, revisión cromática global ni publicación de la biblioteca Figma.
