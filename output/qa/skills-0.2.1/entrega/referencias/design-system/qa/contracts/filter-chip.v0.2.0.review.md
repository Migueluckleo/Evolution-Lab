---
qa_id: QA-FILTER-CHIP-002
review_type: CONTRACT_REVIEW
contract_id: FILTER-CHIP-001
contract_version: 0.2.0
contract_digest: bd82e46bcbde849890af30e9c8f6d5fad3b1d0cb2b3b5b2f5ac1cacd1127ab96
data_refs:
  - drafts/contracts/filter-chip.contract.yaml
  - drafts/contracts/filter-chip.build.v0.2.0.yaml
target: figma
reviewer: Codex
executed_at: 2026-09-23
result: PASS_FOR_HUMAN_REVIEW
---

# QA documental · Filter Chip 0.2.0

La revisión comprueba el candidato normativo contra la descripción fuente, la respuesta del usuario y el estado leído de AI Design System. `PASS_FOR_HUMAN_REVIEW` significa que puede someterse a aprobación; no equivale a aprobación ni a QA de implementación.

| Control | Resultado | Evidencia y límite |
|---|---|---|
| DOC-01 | PASS | Tipo component set; no se fuerza anatomía de Button. |
| DOC-02 | PASS | Frontmatter, tablas, YAML y enlaces se validan en la revisión automatizada final. |
| DOC-03 | PASS | Identidad, versión, destino, fuentes y PlusCircle declarados; owner desconocido. |
| DOC-04 | PASS | REQ-FC-001–009 trazan usuario, description, fuente observada o protocolo. |
| DOC-05 | PASS | Se separan 24 variantes observadas, 30 propuestas, x-small excluido y 12 variantes nuevas. |
| DOC-06 | PASS | No se importan variantes ni tokens del ejemplo Button; solo su escala de tamaño verificable del destino. |
| DOC-07 | PASS | Modelo de 26 variables fuente y mapa de 28 variables destino reconciliados por nombre/ID. |
| DOC-08 | PASS | El contrato no redefine `description` de tokens; sus definiciones canónicas siguen en foundations. |
| DOC-09 | PASS | La decisión del usuario resuelve defaults de iconos, tamaños y matriz; focus seleccionado se identifica como derivación candidata. |
| DOC-10 | PASS | Tamaños/padding/gap y tokens se relacionan en una única receta de construcción; se señala la normalización middle. |
| DOC-11 | PASS | Defaults `false/false`, matriz 3×2×5 y 30 variantes no se contradicen. |
| DOC-12 | PASS | Figma visual separado de comportamiento web. |
| DOC-13 | PASS | Nueve requisitos tienen nueve criterios de readback. |
| DOC-14 | PASS | El snapshot y el candidato 0.1.0 se conservan sin edición. |
| DOC-15 | PASS | Estado `IN_REVIEW`, sin aprobación inventada. |
| DOC-16 | PASS | Page/bindings Figma preparados; producto y web permanecen sin definir y fuera de alcance. |

## Reconciliación

- 3 tamaños × 2 selecciones × 5 estados = 30 combinaciones únicas.
- 10 recetas de estado se aplican a cada tamaño.
- 26 variables source se mapean por nombre a 26 variables locales del destino; dos variables de familia/peso del destino complementan la tipografía. Un readback individual confirmó 28/28 IDs, nombres, colección y cuatro modos.
- 60 slots de icono deben conservar la key Phosphor exacta; estarán ocultos por defecto, no desconectados.
- Los 4 modos de `semantic` de destino están identificados; sus aliases viven en el archivo destino.

## Gates posteriores

La aprobación explícita de `FILTER-CHIP-001` 0.2.0 debe identificar el candidato y su alcance. Después se publica el contrato aprobado y se ejecuta P04. La construcción debe tener revisión de implementación independiente antes de usar `VALIDATED`.
