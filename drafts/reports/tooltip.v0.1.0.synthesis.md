# SYN-TOOLTIP-001 · síntesis para Tooltip 0.1.0

- **Fuente principal:** set `2599:10469` de la página `2599:10321` en la Librería anterior; lectura read-only completa de 21 nodos, 4 variantes, 12 variables usadas y 0 estilos nombrados. [Modelo de evidencia](../contracts/tooltip.contract.v0.1.0.yaml).
- **Datos canónicos:** [JSON aprobado](../../sources/inventories/tokens.inventory.json), SHA-256 bytes `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`, y variables locales de `AI-Design-System` leídas por ID en el preflight.
- **Candidato revisado:** [tooltip.contract.v0.1.0.candidate.md](../contracts/tooltip.contract.v0.1.0.candidate.md), SHA-256 bytes `be1b92f6026cc2825a5bdbc105718c2b9dffbc097a5da39a8cc84745f00d4359`; [QA documental](../../qa/contracts/tooltip.v0.1.0.review.md) `PASS`.
- **Versión delegada:** [tooltip.contract.v0.1.0.md](../contracts/tooltip.contract.v0.1.0.md), SHA-256 bytes `522b74426f781231dbf0a3ce7daed35909ab8f1358e347efe97e34f454416402`. No implica aprobación humana; `user_audit: PENDING`.

## Cobertura y transformaciones

Las cuatro variantes Align observadas se adoptan sin completar combinaciones inexistentes. Se confirma la propiedad TEXT conectada a las cuatro etiquetas, ancho FIXED y alto HUG. El texto del ejemplo sigue siendo editable; no define contenido de producto. La ruta vectorial de flecha y las dos sombras se conservaron como evidencia; no hay instancia de icono que sustituir.

Los tokens de color, familia/peso/tamaño, spacing y radius se mapean por nombre/rol desde el JSON aprobado hacia IDs locales. El texto fuente usa `color/text/on-brand` sobre `color/background/inverse`; el contrato selecciona `color/text/inverse`, porque la `description` aprobada de este último identifica fondos oscuros. Ambos aliases resuelven a blanco, pero la decisión se fundamenta en intención, no solo igualdad RGB. El interlineado fuente 160% de 14 y tracking −2% no tienen equivalencia exacta probada con los tokens locales; la versión delegada usa `font/line-height/md` y `font/letter-spacing/tight` como normalización visible para auditar. La sombra permanece literal porque el JSON no define una categoría de elevación.

La página fuente contiene una frase de plantilla sobre tamaños de Modal dentro de una instancia documental; se excluye porque no describe Tooltip. No se observaron reacciones del set, por lo que no se infiere lógica web ni accesibilidad funcional.

## Preparación Figma

El destino leído contiene Buttons y Chips, ninguna página Tooltips. La colección semántica local ofrece los 13 tokens destino usados en los cuatro modos; no se crearán variables. P04 puede crear una página `Tooltips` y un set `Tooltip` sin actualizar contenido existente. Las decisiones de normalización y la ausencia de sombra tokenizada se conservarán para auditoría posterior.
