# Plan de construcción Figma · Metric Cards 0.1.0

- **Destino:** `AI-Design-System`, página exclusiva `Metric Cards` ausente en preflight, acción `CREATE`.
- **Contrato:** `METRIC-CARD-001` 0.1.0 `DELEGATED_FOR_BUILD`; fuente 119/119 nodos, QA fuente `PASS`, QA documental destino `PASS` antes de escritura.
- **Dependencias locales:** colección `semantic` `VariableCollectionId:6:2`; colores, tamaños, espacios, radios y tipografía requeridos presentes. Se resolvieron duplicados de nombre de peso/tracking y se elegirán IDs semánticos con scopes `FONT_STYLE` y `LETTER_SPACING`, no sus primitivas homónimas. Manrope Regular disponible.
- **Dependencias externas:** importar CurrencyCircleDollar key `441865351ce8a0390c7544fee2348dd8ae895f51` y ArrowUpRight key `8f20fac8635901c6627e086c16fdf197d5134b7f`; validar key antes de crear variantes.
- **Orden:** crear página y ocho componentes → combinar como variantes → configurar props → inspeccionar screenshot/readback → ajustar solo clipping o geometría documentada → QA de bindings/contraste → estado/registro. No publicar.
- **Riesgos:** diferencias de métricas textuales por render de Manrope local y el Title 18→20 de V1 Small; no ampliar sin evidencia de clipping. Si el import remoto falla, inspeccionar estado antes de reintentar.
