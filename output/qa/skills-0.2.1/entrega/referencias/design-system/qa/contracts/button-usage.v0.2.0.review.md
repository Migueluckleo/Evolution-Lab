---
qa_id: QA-BUTTON-USAGE-002
review_type: CONTRACT_REVIEW
contract_ref: BUTTON-001
contract_version: 0.2.0
contract_digest: c97cd24a1505236cfdac32d85a676d8eb2b4394ec074412305d7cfd3abf37ae5
data_refs:
  - drafts/contracts/button.contract.yaml
implementation_ref: null
target: figma-documentation
scope: nueva guía de uso y texto candidato para Description
blocked_items:
  - aprobación humana de BUTTON-001 0.2.0 pendiente
  - URL pública del contrato aprobado no verificada
  - semántica web de link y comportamiento real fuera de alcance
accepted_deviations: []
reviewer: Codex
executed_at: 2026-09-23
result: PASS
---

# QA-BUTTON-USAGE-002 · revisión documental

PASS significa apto para decisión humana, no aprobado ni publicado en Figma. El contrato 0.1.0 sigue vigente y la implementación validada conserva su alcance anterior.

| Control | Resultado | Evidencia |
|---|---|---|
| DOC-01 | PASS | 21 secciones de componente; no se fuerza anatomía a tokens. |
| DOC-02 | PASS | Frontmatter YAML parseado, tablas y secciones legibles. |
| DOC-03 | PASS | BUTTON-001 0.2.0 IN_REVIEW, base 0.1.0, fuentes y dependencias explícitas. |
| DOC-04 | PASS | REQ-BTN-010–019 indican fuerza y procedencia; la guía externa se diferencia de decisión local. |
| DOC-05 | PASS | OBSERVED, EXPLICIT, INFERRED y UNRESOLVED separados; no se declara intención histórica. |
| DOC-06 | PASS | No se importaron tamaños o tipos ajenos ni tokens de las guías. |
| DOC-07 | PASS | YAML técnico existente referenciado sin reescribir; las 60 combinaciones vienen del baseline aprobado. |
| DOC-08 | PASS | Sin description o usage paralelos para tokens; Description propuesta es del componente. |
| DOC-09 | PASS | Defaults técnicos de dos PlusCircle distinguidos de recomendaciones para instancias; ninguna variante se elimina. |
| DOC-10 | PASS | Medidas 48/40/32, iconos 24/20/20 y texto 16/16/14 corresponden al contrato 0.1.0. |
| DOC-11 | PASS | Icon-only fuera de alcance, texto visible recomendado, booleanos conservados. |
| DOC-12 | PASS | type=link visual no se equipara a elemento web; Tailwind no se convierte en contrato conductual. |
| DOC-13 | PASS | AC-BTN-010–019 enlazan a REQ homólogos y tienen comprobación observable. |
| DOC-14 | PASS | Snapshot, YAML, 0.1.0 y Figma no se editaron; captura copiada byte a byte. |
| DOC-15 | PASS | No existe aprobación de 0.2.0; Description Figma sigue vacía. |
| DOC-16 | PASS | URL pública, teclado, touch target, danger, icon-only, RTL y web quedan acotados. |

## Controles adicionales

| Control | Resultado | Evidencia |
|---|---|---|
| USAGE-01 | PASS | Las 60 variantes quedan cubiertas por producto cartesiano de tablas type, size, state; no se inventan 60 usos individuales. |
| USAGE-02 | PASS | Carbon y Material discrepan en colocación de icono; la regla izquierda/derecha se etiqueta como adaptación INFERRED. |
| USAGE-03 | PASS | El borrador de Description resume todas las dimensiones sin atribuir WCAG ni semántica web. |
| USAGE-04 | BLOCKED | No hay URL pública verificada para Documentation link; se deja vacío. |
| USAGE-05 | BLOCKED | Publicación y QA de Description requieren aprobación de 0.2.0 y escritura/readback posteriores. |

## Comprobaciones mecánicas

- Frontmatter parseado con Ruby/Psych y Date permitida.
- Se encontraron las 21 secciones requeridas.
- El candidato conserva los cuatro types, tres sizes y cinco states, con cobertura 60/60 por composición.
- SHA-256 bytes del candidato: c97cd24a1505236cfdac32d85a676d8eb2b4394ec074412305d7cfd3abf37ae5.
- SHA-256 bytes de Description candidata: 22ca686667bc9c815d461c6d1e246817b8861e04fb9e448440b96e478d98c56c.
- SHA-256 bytes de baseline aprobado 0.1.0: 4b94f80787c1fc9d9990f806c99900e17db060e65b624471b0c8d93f534f2abb.

Resultado: PASS de revisión documental con dos controles de publicación BLOCKED. No se ejecutó IMPLEMENTATION_REVIEW de 0.2.0.
