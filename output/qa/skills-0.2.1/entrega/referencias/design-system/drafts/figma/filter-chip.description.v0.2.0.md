---
contract_id: FILTER-CHIP-001
contract_version: 0.2.0
status: IN_REVIEW
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
target_page: Chips
target_component_set: Filter Chip
---

# Description propuesta para el component set

El texto entre los marcadores `FIGMA_DESCRIPTION_START` y `FIGMA_DESCRIPTION_END` es el contenido exacto propuesto para `description` y `descriptionMarkdown` del set. Los marcadores y este encabezado no se publican.

<!-- FIGMA_DESCRIPTION_START -->
Filter Chip permite representar un filtro seleccionado dentro de un conjunto pequeño. Usa `small` (32 px), `middle` (40 px) o `large` (48 px) según el contexto; mantén el mismo tamaño dentro de un grupo.

`selected` indica la selección visual. Cada valor de `selected` dispone de `default`, `hover`, `press`, `focus` y `disabled`. El fondo del seleccionado conserva el token inverso: hover lo muestra al 92% y press al 85%; focus agrega el anillo de foco. Disabled tiene el mismo aspecto con o sin selección.

La referencia inicial muestra solo texto. Activa un icono izquierdo o derecho cuando aporte significado; ambos slots usan por defecto PlusCircle de Phosphor Icons y permiten cambiar la instancia. Mantén una etiqueta breve y específica. Los colores, tipografía, espaciado, radio y anillo están vinculados a variables propias de AI Design System y responden a sus cuatro modos.

Estos estados son representaciones visuales de Figma. La lógica de selección, teclado y accesibilidad funcional se especifica por separado.
<!-- FIGMA_DESCRIPTION_END -->
