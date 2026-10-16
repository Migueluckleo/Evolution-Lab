---
contract_id: MIGRATION-TOKEN-TRACEABILITY-001
version: 0.1.2
type: amendment
status: DELEGATED_FOR_BUILD
supersedes_requirement: REQ-MTT-004
base_contract: specs/MIGRATION-TOKEN-TRACEABILITY.contract.md
supersedes: specs/MIGRATION-TOKEN-TRACEABILITY.amendment.v0.1.1.md
decision_refs: [DEC-MIGRATION-NEAREST-PRIMITIVE-001]
last_updated: 2026-09-24
user_audit: PENDING
---

# Enmienda 0.1.2 · reutilizar primitiva y tokenizar semánticamente

Esta enmienda sustituye solo `REQ-MTT-004` del [contrato transversal base](MIGRATION-TOKEN-TRACEABILITY.contract.md) y la [enmienda histórica 0.1.1](MIGRATION-TOKEN-TRACEABILITY.amendment.v0.1.1.md), tras la instrucción posterior [DEC-MIGRATION-NEAREST-PRIMITIVE-001](../registry/decisions.md). `REQ-MTT-001–003` y `005–006` permanecen vigentes excepto la diferencia visual expresamente autorizada cuando no existe primitiva exacta.

**REQ-MTT-004 vigente:** buscar primero una primitiva de RGB idéntico en el JSON aprobado y las variables del destino. Si existe, crear o reutilizar un rol semántico con scope correcto y alias a ella. Si no existe, comparar las primitivas existentes, elegir la que mejor se asemeje por evidencia de color y uso, crear o reutilizar un rol semántico que la aliasa en todos los modos y **no aplicar la primitiva directamente al componente**. Documentar RGB fuente y destino, método de comparación, diferencia visual, contraste, JSON de extensión, IDs locales y bindings leídos de vuelta. No crear una primitiva nueva por defecto ni usar un rol de otra categoría por coincidencia cromática. Una excepción futura que vuelva a requerir primitiva nueva necesitará decisión explícita adicional.

La cadena de procedencia ahora incluye `primitiva existente idéntica o aproximada y diferencia documentada → rol semántico → variable local → consumidor`. [Scrollbar 0.1.1](scrollbar.color-approximation.amendment.v0.1.1.md) es el primer caso: `neutral/300` fue la primitiva existente perceptualmente más cercana, y los 30 thumbs consumen el rol de fondo. Los contratos ya construidos con color exacto no cambian por esta enmienda. La auditoría humana y la publicación de biblioteca siguen separadas.
