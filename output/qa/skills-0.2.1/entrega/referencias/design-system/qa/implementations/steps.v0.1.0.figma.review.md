# QA de implementación · Steps 0.1.0

Estado histórico: `STALE` solo para aliases cromáticos por la [enmienda de marca 0.1.1](../../specs/steps.brand-theme.amendment.v0.1.1.md). La estructura y los conteos permanecen como evidencia; el [QA vigente](steps.v0.1.1.figma.review.md) revalida los colores. Auditoría humana `PENDING`; biblioteca `UNPUBLISHED`. Inspección original: 2026-09-24.

## Destino y estructura

AI Design System, página `Steps` (`341:122`), set público `Steps` (`343:212`) con seis variantes, `Steps Dot` (`342:139`) con cuatro y `Steps Combination` (`342:445`) con 27. Las seis variantes públicas conservan 191×32, 196×32 o 40×8 px según Type. Los botones locales se ajustan a 76×32 y 75×32 px con `Back`/`Next`, flechas de Phosphor y propiedades editables; el contador `5 / 6` es texto editable de 14/20 px vinculado a variables locales de familia, peso, tamaño y altura de línea. No se importó el botón de la Librería antigua. Las 27 combinaciones tienen 2–7 dots separados 16 px y exactamente un seleccionado que coincide con `Step`; cero errores en la comprobación de las 27.

## Cadena cromática verificada

Las siete variables del [JSON canónico de extensión](../../drafts/foundations/ai-design-system.steps-colors.v0.1.0.json) existen en la colección `semantic` con el mismo nombre, descripción, scope y alias a primitiva en los cuatro modos Contable, Administrativo, Servicios y Personas. No se creó primitiva nueva. La lectura recursiva de los tres sets encontró **173/173 pinturas visibles con binding**, cero pinturas sin variable y cero cruces de categoría semántica. Los roles de Steps llegan a la forma o al texto; ningún dot consume directamente la primitiva. Los botones anidados consumen `color/text/primary`, `color/icon/primary`, `color/text/on-brand` y `color/icon/on-brand` según contexto.

| Evidencia de fuente | Resolución de destino | Resultado |
|---|---|---|
| Dot On White `#3255F7` / `#E2E8F0` | blue/400 / neutral/300, vía roles de Steps | exacto |
| Dot interno On Primary blanco / `#7D9AFF` | neutral/100 / blue/300, vía roles de Steps | blanco exacto; azul claro aproximado |
| Public Gallery On Primary `#0073EA` / `#DCDFEC` | blue/300 / neutral/300, vía roles `legacy-gallery` | aproximado; inconsistencia de fuente preservada |
| Public Gallery only On Primary azul/gris de On White | roles On White | anomalía fuente preservada |
| Count On White aprox. `#323338` | neutral/800, vía rol de texto de Steps | aproximado |

La captura del set público y la rejilla de 27 combinaciones se revisaron contra la sección fuente. La variante contextual On Primary aparece parcialmente invisible sobre el fondo blanco transparente del set; esto no es un fill perdido: debe situarse sobre un fondo primario en uso. El set público no tiene reacciones y no se inventó destino para la reacción hover rota de la fuente.

## Límites y seguimiento

No se certifica contraste, comportamiento de navegación, sincronía del contador con datos, teclado ni atributos ARIA. La inconsistencia cromática pública de On Primary y las cuatro aproximaciones de color permanecen en la [auditoría por excepciones](../../specs/MIGRATION-AUDIT.md). Este PASS no es aprobación humana ni autorización para publicar la biblioteca.
