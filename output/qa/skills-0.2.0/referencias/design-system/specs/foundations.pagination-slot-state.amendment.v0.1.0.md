---
contract_id: FOUNDATIONS-PAGINATION-SLOT-STATE-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
date: 2026-09-30
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.pagination-slot-state.v0.1.0.json]
---

# Pagination · herencia de Disabled en contenido de Slots

Extensión acotada para [COMPOSITION-SLOTS-002](composition-slots.amendment.v0.1.1.md). El [JSON canónico de esta extensión](../drafts/foundations/ai-design-system.pagination-slot-state.v0.1.0.json) es la única definición editable de nombres, tipos, scopes, descripciones y aliases; el inventario histórico no cambia.

Se crea una colección contextual de dos modos, Enabled y Disabled, independiente de los cuatro modos de marca de semantic. Sus ocho roles de color y un grosor aliasan roles existentes que ya apuntan a primitivas aprobadas. No hay RGB, primitivas, paleta ni tipografía nuevos. Esta capa contextual permite heredar simultáneamente estado y tema; no sustituye ni añade modos a semantic.

El anfitrión Pagination establece su modo contextual: Disabled en la variante homónima y Enabled en las restantes. El contenido Pages conserva el contexto heredado, sin fijar modos en sus celdas. Incluso un ítem con override de estado activo/foco conserva su contenido, pero sus colores y grosor se neutralizan en Disabled. Al volver a Enabled recupera su estilo anterior. No calcula la página seleccionada, el rango ni la elipsis.

Las celdas del Slot deben reutilizar los roles de esta extensión, no primitivas ni pinturas libres. Una inserción arbitraria que incumpla esta regla queda fuera del contrato. Las celdas normales, activas, hover y foco conservan en Enabled sus colores y medidas anteriores. Las celdas creadas desde la muestra Disabled usan el rol normal con modo Disabled heredado, de forma que puedan volver a Enabled sin quedarse atenuadas.

QA documental PASS: necesidad delimitada por Slots, aliases existentes leídos en Figma, scopes estrictos, fuente de datos única y sin cambio cromático. Antes del cierre se exige readback JSON↔Figma de nueve variables y sus dieciocho aliases; comparación de defaults; prueba de contenido personalizado al pasar por Disabled en los cuatro temas y restablecer Enabled. Si la herencia no funciona, no declarar VALIDATED.
