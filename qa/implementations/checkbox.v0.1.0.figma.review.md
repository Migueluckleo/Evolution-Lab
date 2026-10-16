# QA-CHECKBOX-FIGMA-001 · Checkbox 0.1.0

- **Resultado:** `PASS` técnico para AC-CBX-001–007; auditoría humana `PENDING`.
- **Destino:** página única `Checkboxes` `149:122` y set `Checkbox` `149:199` en AI Design System; las páginas previas permanecen. Doce variantes `Selection=Selected/Indeterminate/Unselected × State=Default/Hover/Focus/Disabled`, defaults Selected/Default.
- **Fuente y autoridad:** [contrato de fuente](../../drafts/contracts/checkbox.source.component-contract.md) y [YAML](../../drafts/contracts/checkbox.source.component-contract.yaml), traversal 86/86; [contrato de construcción](../../drafts/contracts/checkbox.contract.v0.1.0.md), SHA-256 `bc189560b843aad787b5f17f38f51a60e4a2635955d111a176b9a5d81d2966bd`.
- **Estructura:** 12 wrappers 24×24 sin etiquetas visibles, 12 rectángulos 18×18 con 48 radios tokenizados, 16 bindings laterales de stroke en las cuatro variantes Unselected, 12 gaps ligados a `spacing/sm`.
- **Iconos:** ocho instancias Phosphor (cuatro Check Outline/Light y cuatro Minus Outline/Regular) importadas por key, re-leídas después de importar, anidadas sin detachment. Ocho vectores visibles usan `color/icon/on-brand` y 16 bindings width/height al token `size/md` de 12 px. No hay iconos en Unselected.
- **Etiquetas:** 24 ocultas con dos propiedades TEXT y dos BOOLEAN conectadas; 120 bindings tipográficos en labels, más colores `TEXT_FILL` apropiados. Sin texto de producto inventado.
- **Colores y scopes:** 46 paints sólidos visibles ligados a variables; cero paints sin binding o categoría/scope incorrectos. Tres Focus usan el estilo compartido `Focus/Selection Outset` de spread 4/2 y seis colores ligados a `EFFECT_COLOR`. El cambio de nombre del estilo no modificó ID, efectos ni apariencia de Radio Button.
- **Contraste:** mínimo cromático activo 3.24:1 en Servicios; contorno Unselected Default/Focus 4.76:1 sobre blanco. Disabled no se presenta como control operable.
- **Captura:** fuente 680×290 y destino 691×474 inspeccionadas inline. Se conservan los tres tipos y cuatro estados; diferencia del contorno neutral y documentación de página registradas. Sin recorte aparente. Reacciones: cero.
- **Límite:** set `UNPUBLISHED`; no se afirma selección funcional, grupo, teclado, hit target, WCAG ni implementación web.
