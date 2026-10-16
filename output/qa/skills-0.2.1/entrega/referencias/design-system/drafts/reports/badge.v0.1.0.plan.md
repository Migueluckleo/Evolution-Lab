# PLAN-BADGE-FIGMA-001 · construcción delegada

- **Contrato:** `BADGE-001` 0.1.0, `DELEGATED_FOR_BUILD`; auditoría humana pendiente.
- **Destino:** `AI-Design-System` `tj3WIBEZDGLVs7MJWKCwgf`; crear página exclusiva `Badges` y set `Badge`, sin mover ni modificar Buttons, Chips o Tooltips.
- **Dependencias:** JSON de variables aprobado sin cambios; 26 roles visuales de la colección semantic; componente remoto Phosphor Presentation Outline/Fill por key exacta. No se crearán variables.
- **Construcción:** seis variantes Type; auto layout horizontal con icono izquierdo, etiqueta, icono derecho; booleans para visibilidad, TEXT para contenido y dos INSTANCE_SWAP. Fills, borde, tipografía, spacing, radio y stroke por tokens locales. Preferidos de iconos desde Phosphor, no iconos inventados.
- **Diferencias sujetas a auditoría:** Light usa borde strong en vez de disabled; iconos derechos usan roles de icono en lugar de texto. Los aliases de color preservan la apariencia observada.
- **QA:** leer identidad de página/set, variantes, defaults, instancias y keys, propiedades conectadas, cada binding local y resolución por modo, dimensiones y captura. Registrar estado `UNPUBLISHED` si no se publica.
