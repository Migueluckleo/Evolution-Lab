# Modal · contrato observacional de origen

Fuente: [Librería raíz](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=7419-38329). Fecha2026-10-01. **Evidencia de Figma en solo lectura; normalización PARTIAL**, no contrato de implementación.
[YAML sincronizado](modal.source.component-contract.yaml) · [snapshot completo de campos leídos](../../sources/figma-snapshots/modal.v0.1.0.source.json).

## 1. Component Identity
Página4886:869. Basic7419:38329; Media7419:38363; SideBySide7419:38372; Footer7419:38385; Image7419:38400; Header7419:38401. Estos seis roots delimitan la inspección.

## 2. Anatomy
Basic = Header / Body Slot / Footer. Media = Image / Content / Close / Footer. SideBySide = columnasContent+Image / Footer. Footer contiene contenido lateral y dos acciones de muestra.
Observed from Figma:359nodos recorridos,70marcados invisibles;0nodos pendientes.

## 3. Dependencies
131instancias agrupadas en17mains:11locales y6remotos. Identidad y superficie activa leídas; resolución formal PARTIALLY_RESOLVED por metadatos de sets/procedencia incompletos. No se importó nada para inspeccionar.
Las dependencias están enumeradas por key e instance_ids en YAML.

## 4. Properties
Basic: Size, Scroll, Body SLOT. Header: Title/Subtitle TEXT, Subtitle/Icon boolean, Icon swap. Footer: visibilidad contenido lateral/secundario y If scroll. Media: Title/Text/Image swap. SideBySide: Body SLOT.
Candidatos de iconos no expandidos: Header1513preferred values; solo valor activo inspeccionado.

## 5. Variants
Basic: Small/Medium/Large × No/Yes =6. Media ySideBySide son componentes sin matriz propia. Header2 yFooter2.

## 6. States
Observed ScrollNo/Yes. No reglas observadas de error/loading/disabled global del diálogo.

## 7. Layout
Basic480/580/840; alturas266/320/383/383/400/400. Header112,Footer80. Media580×466; SideBySide840×480.
Campos individuales y relaciones padre/hijo conservados en snapshot; no se afirma normalización exhaustiva de layout en YAML.

## 8. Visual Styles
Superficies blancas; texto/icono neutral; acentos de marca. Radius16. ShadowLarge negro30%,blur50,offset0/15; FooterScroll negro20%,blur20,offset0/6.
Body muestra placeholder editorial amarillo “Replace me”. Imágenes raster originales con hashes c501b83c7359259626cc55a14fd37122b56ad90f y73f7fc927575ad4cf7008efc6fe4f8a9cb5b27fe.

## 9. Typography
TítuloManropeBold24/30,tracking-0.1px; cuerpoManropeRegular16/22. Texto lateral14/20. Hay textosMIXED: neutral y sufijo brand; segmentos específicos inspeccionados, no todas las tipografías convertidas al modelo normalizado.

## 10. Tokens
29variables usadas:25locales,4remotas. Referencias, aliases por modo y used_by en YAML/snapshot; colección/modo consumidor no expandido completamente, por eso PARTIALLY_RESOLVED.4estilos nombrados remotos, RESOLVED por identidad leída. No se sustituyeron tokens por literales.

## 11. Content
Las cadenas “Modal title”, “Replace me”, “Secondary”, “Main CTA”, “Don’t show again” y “Side actions text” son ejemplos. Cardinalidad de producto no determinada por muestras.

## 12. Interactions
FIGMA_DEFINED: existen reacciones ON_CLICK/NAVIGATE con destinationId=null. No prueban cierre ni navegación utilizable. El texto de marca no tiene hyperlink.

## 13. Accessibility
REQUIRES_DEFINITION: foco, teclado, escape, backdrop, semántica dialog y regreso de foco. Esta extracción no certifica WCAG.

## 14. External Dependencies
Identidad/key/remote se preservan; library/source/version no expuestos se marcan NOT_EXPOSED_BY_FIGMA_MCP. No se deducen por nombre.

## 15. Unresolved Information
Normalización detallada de camposMIXED, layout/visual y procedencia externa parcial. Snapshot conserva los359nodos leídos; esto no equivale a un contrato normalizado COMPLETE.

## 16. Implementation Notes
Este documento no recomienda cambios de producto, no modifica Figma ni genera frontend. La reconstrucción tiene contrato normativo separado en specs una vez validada.

## 17. Evidence / Confidence
FIGMA_DIRECT: snapshot SHA256 cf55d6f96b11c37b68391198f1f8e3014197dee950fdeccc3f03cc4159d4d60f. DERIVED: agrupación de6variantesBasic y2composiciones. ConfidenceMEDIUM por límites explícitos. Markdown/YAML comparten estos conteos y estados.

