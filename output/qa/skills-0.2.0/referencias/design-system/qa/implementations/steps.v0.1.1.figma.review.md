# QA de implementación · Steps marca por tema 0.1.1

Estado: `PASS` técnico, `VALIDATED` para [STEPS-001](../../specs/steps.contract.v0.1.0.md) con [enmienda 0.1.1](../../specs/steps.brand-theme.amendment.v0.1.1.md). Auditoría humana `PENDING`; biblioteca `UNPUBLISHED`. Inspección: 2026-09-24.

## Alcance y cadena de tokens

AI Design System, página `Steps` (`341:122`), set público `Steps` (`343:212`) con seis variantes, `Steps Dot` (`342:139`) con cuatro y `Steps Combination` (`342:445`) con 27. Los tres sets conservan sus IDs y estructura; no se añadieron nodos, variables ni primitivas. El [JSON 0.1.1](../../drafts/foundations/ai-design-system.steps-colors.v0.1.1.json) define siete roles existentes y 28 aliases por modo. El readback comprobó 7/7 nombres, IDs, descripciones y scopes, 28/28 aliases y cero discrepancias.

El dot seleccionado `On White` usa el rol semántico `color/shape/steps/dot/on-white/selected`: alias a la primitiva correspondiente a `color/brand/default` en Contable, Administrativo, Servicios y Personas. El dot no seleccionado `On Primary` y el seleccionado de Gallery legada usan roles separados que aliasan el tono 300 de la familia de marca de cada tema. Los cuatro roles de blanco, neutros y texto conservan sus aliases. Los consumidores siguen ligados a roles semánticos `SHAPE_FILL` o `TEXT_FILL`, no a primitivas directas.

## Readback y vista

La lectura recursiva de los tres sets encontró **173/173 pinturas visibles vinculadas**, cero pinturas sin variable y cero cruces de scope/categoría. Los tres roles modificados tienen 33 consumidores visibles. Las 27 combinaciones conservan exactamente un dot seleccionado acorde con `Step`: **27/27**, cero errores. La inspección visual del set público en modo Servicios mostró acentos naranja y mantuvo los blancos/neutros contextuales; después se eliminó el modo explícito de prueba y una lectura independiente confirmó `explicitVariableModes: {}` en el set público. No se modificaron geometría, textos, propiedades ni comportamiento.

## Diferencias y límites

El azul fijo de la Librería anterior cambia intencionalmente con el tema por instrucción posterior del usuario. La selección exacta de marca base para `On White` y tono 300 para los dos acentos contextuales es criterio delegado documentado en [DEC-STEPS-BRAND-THEMING-001](../../registry/decisions.md). La anomalía de las variantes públicas `On Primary` y las aproximaciones cromáticas/neutras permanecen en [AUD-008](../../specs/MIGRATION-AUDIT.md). Los aliases a primitivas son directos; si cambia el mapa de `color/brand/default`, debe sincronizarse de nuevo el JSON y Figma. No se certifican contraste, navegación, teclado ni ARIA. Este `PASS` no es aprobación humana ni publicación de biblioteca.
