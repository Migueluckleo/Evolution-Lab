# Breadcrumbs · contrato de evidencia fuente

- **Origen:** [Libreria v1.1.0, set Breadcrumbs](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2425-35937), página `1098:28190`, set `2425:35937`, key `6fb836fc24e1d24e6a0b0c933f97cfc32ff58680`.
- **Inspección:** `COMPLETE`, solo lectura, 65/65 nodos; captura de la página de origen 1242×1106 verificada. Es evidencia de Figma, no comportamiento implementado ni especificación aprobada de producto.

## Component Identity

**Observed from Figma:** set reutilizable `Breadcrumbs` 650×296 con cuatro composiciones `type=Level 2/3/4/5`; default Level 2. No tiene descripción propia.

## Anatomy

**Derived structure:** `Breadcrumbs` → variante de nivel → ArrowLeft 24 + frame horizontal `Breadcrumbs` → 2–5 instancias locales de `Breadcrumb item`; el último ítem usa `active=on`, los anteriores `default/off`. El caret separador pertenece al ítem, no al contenedor.

## Dependencies

**Observed from Figma:** 28 instancias en total: cuatro ArrowLeft remotas, 14 `Breadcrumb item` locales (diez default/off y cuatro default/on), y diez CaretRight remotos anidados. Cuatro componentes principales únicos, dos locales y dos remotos. 15 variables usadas: 11 locales y cuatro remotas. Un estilo de texto remoto `Body 1 - 16px/Regular` aparece en las cuatro etiquetas activas de ejemplo.

## Properties

**Observed from Figma:** solo `type` VARIANT, default `Level 2`, con opciones Level 2/3/4/5. Las instancias internas tienen propiedad TEXT editable `text`, pero el set padre no expone una propiedad para cada segmento ni para ArrowLeft.

## Variants

| Nivel | ID | Caja | Breadcrumb item | Separadores | ArrowLeft |
|---|---|---:|---:|---:|---:|
| Level 2 | `2425:35938` | 242×24 | 2 | 1 | 1 |
| Level 3 | `2425:35941` | 362×24 | 3 | 2 | 1 |
| Level 4 | `2425:35945` | 482×24 | 4 | 3 | 1 |
| Level 5 | `2425:35950` | 602×24 | 5 | 4 | 1 |

## States

**Observed from Figma:** los niveles anteriores usan default/off; el último usa default/on. No hay reacciones ni transición definida al cambiar nivel.

## Layout

**Observed from Figma:** cuatro variantes de auto layout horizontal con gap exterior 8 ligado a `spacing/sm`; ArrowLeft 24 px y frame interior horizontal con gap 4. Cada nivel suma 120 px de ancho, manteniendo alto 24. Set en rejilla vertical con filas y=24/98/172/246.

## Visual Styles

**Observed from Figma:** sin fondos/bordes de contenedor. ArrowLeft `color/icon/primary`, separadores `color/icon/secondary`, textos previos `color/text/tertiary`, último `color/text/brand`. Las pinturas visibles mantienen categoría semántica; los wrappers blancos de icono están ocultos.

## Typography

**Observed from Figma:** 14 etiquetas, 10 Manrope Regular previas y cuatro Inter Regular activas por override remoto; ambas 16 px, line-height 150% y letter-spacing −2%. El set `Breadcrumb item` original define el activo en Manrope, de modo que la composición tiene una excepción de fuente que debe decidirse en el contrato de destino.

## Tokens

**Observed from Figma:** 15 variables con IDs/consumidores en el [YAML sincronizado](breadcrumbs.source.component-contract.yaml). Cuatro referencias remotas incluyen fuente Inter/size/weight y gap 4; no se promoverán como tokens locales del sistema nuevo por mera coincidencia de valores.

## Content

**Observed from Figma:** las 14 etiquetas dicen `Breadcrumb`. Son ejemplos, no nombres de rutas ni estructura jerárquica real.

## Interactions

`UNDEFINED`: cero reacciones en los cuatro componentes. ArrowLeft se ve como icono; la acción de volver no está definida por Figma.

## Accessibility

`REQUIRES_DEFINITION`: faltan semántica de `nav`/lista, indicación de página actual, foco de teclado, nombres y destinos. La captura no certifica accesibilidad.

## External Dependencies

ArrowLeft y CaretRight son remotos; estilo Inter remoto. Biblioteca, URL y versión externa `NOT_EXPOSED_BY_FIGMA_MCP`.

## Unresolved Information

No se define longitud dinámica fuera de niveles 2–5, truncamiento responsive, comportamiento de back ni edición de labels desde el set padre. El override Inter/Manrope es un conflicto visual de fuente, no una obligación inferida.

## Implementation Notes

El contrato de destino debe conservar instancias del ítem, no copiar los vectores ni duplicar sus definiciones. La tipografía activa debe decidirse explícitamente y registrarse como desviación si se normaliza.

## Evidence / Confidence

**FIGMA_DIRECT:** metadata, screenshot, traversal de 65 nodos, 28 instancias, 15 variables y un estilo remoto. **DERIVED:** recuentos por nivel y anatomía. **REQUIRES_DEFINITION:** navegación, semántica y contenido dinámico. Confianza `HIGH` para estructura observada; origen externo no expuesto.
