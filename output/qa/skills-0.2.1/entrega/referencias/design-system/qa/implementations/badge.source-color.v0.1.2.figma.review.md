# QA Figma · Badge · fidelidad cromática 0.1.2

**Resultado:** `PASS` técnico para `AC-BDG-007–008` y revisión transversal de color, bindings y tipografía; **fecha:** 2026-09-24. `user_audit: PENDING`; set `UNPUBLISHED`.

## Resultado

- Fuente: set `1234:65377`, seis variantes. Destino: página `Badges` `94:122`, set `98:128`, seis variantes con IDs previos intactos. Comparación read-only posterior de los **19 paints visibles**: cero diferencias RGB por variante. La captura del set posterior mostró de nuevo texto Informational azul y texto/icono Warning ámbar.
- Se reconectaron exactamente cuatro fills: texto Informational `97:185`→`color/feedback/information/text` `VariableID:13:54`; texto Warning `97:191`→`color/feedback/warning/text` `VariableID:13:46`; vectores Warning izquierdo y opcional derecho `I97:189;8899:60223` / `I97:192;8899:60223`→`color/feedback/warning/icon` `VariableID:13:48`. El último vector pertenece a una instancia oculta por defecto, pero quedó listo para la propiedad opcional. No cambió ningún fill o componente ajeno en esta operación.
- Revisión de los seis componentes y sus instancias, incluidas las ocultas: 17 roles de color y 25 consumidores de paint vinculados. Los roles de texto usan `TEXT_FILL`, los iconos `SHAPE_FILL`, los fondos `FRAME_FILL`/`SHAPE_FILL` y el borde `STROKE_COLOR`; los aliases de cada rol están presentes en los cuatro modos. Las primitivas locales consultadas y el RGB renderizado corresponden al [JSON aprobado](../../sources/inventories/tokens.inventory.json) más el [override Warning 0.1.1](../../drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.1.json).
- Las seis etiquetas mantienen Manrope Regular, 12 px, interlineado 16 px y tracking 0 px, iguales a las seis etiquetas fuente. Familia, peso, tamaño, interlineado y tracking siguen vinculados a variables locales de su tipo.
- No se crearon variables, no cambiaron los fondos, radios, propiedades ni tamaños; el QA histórico de estructura continúa aplicable. La enmienda de contraste 0.1.1 queda `SUPERSEDED` solo en los tres colores restaurados y sus umbrales.

## Limitaciones conservadas `*`

Informational text `#007FC8` sobre `#DBEDFE`: 3.61:1. Warning text/icon `#C97B00` sobre `#FDF2C8`: 2.96:1. Se conservan por fidelidad al origen y se revisarán internamente; este `PASS` significa correspondencia técnica con el contrato vigente, **no** conformidad WCAG. El asterisco está en [MIGRATION-AUDIT](../../specs/MIGRATION-AUDIT.md), no dibujado en Figma. Auditoría humana pendiente y biblioteca sin publicar.
