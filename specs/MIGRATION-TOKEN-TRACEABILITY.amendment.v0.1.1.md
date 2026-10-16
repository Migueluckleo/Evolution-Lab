---
contract_id: MIGRATION-TOKEN-TRACEABILITY-001
version: 0.1.1
type: amendment
status: SUPERSEDED
supersedes_requirement: REQ-MTT-004
base_contract: specs/MIGRATION-TOKEN-TRACEABILITY.contract.md
decision_refs: [DEC-MIGRATION-MISSING-PRIMITIVE-001]
last_updated: 2026-09-24
user_audit: PENDING
---

# Enmienda 0.1.1 · primitiva fuente ausente

**Estado histórico:** sustituida en el tratamiento de colores sin primitiva exacta por la [enmienda 0.1.2](MIGRATION-TOKEN-TRACEABILITY.amendment.v0.1.2.md), conforme a la instrucción posterior del usuario. No aplicar esta regla para nuevas familias.

Esta enmienda sustituye **solo** la prohibición absoluta de crear una primitiva en `REQ-MTT-004` del [contrato transversal 0.1.0](MIGRATION-TOKEN-TRACEABILITY.contract.md). La decisión posterior explícita del usuario [DEC-MIGRATION-MISSING-PRIMITIVE-001](../registry/decisions.md) permite completar una primitiva ausente para conservar exactamente un color observado de la Librería anterior. No cambia `REQ-MTT-001–003` ni `005–006`.

**REQ-MTT-004 revisado:** si falta un rol, primero buscar una primitiva de RGB idéntico en el JSON aprobado y las extensiones vigentes. Si existe, crear solo el rol semántico con scope correcto y alias a esa primitiva. Si no existe y la fidelidad al color fuente lo exige, documentar el RGB y la búsqueda negativa, crear una primitiva de destino en un JSON de extensión versionado y una variable local, y crear un rol semántico aliasado a ella en todos los modos. Registrar nombres, IDs, modos, valores, `description` única, scopes y consumidores; hacer QA documental antes de aplicarlos y readback de Figma/JSON/consumidores después. No modificar el inventario histórico ni primitivas compartidas para acomodar el caso.

La cadena de evidencia de la sección 3 del contrato base admite ahora `primitiva aprobada o primitiva nueva autorizada y versionada`; no basta coincidencia visual sin alias ni scope. Esta excepción no autoriza colores nuevos no observados, ni cambio cromático por contraste. [Scrollbar](scrollbar.contract.v0.1.0.md) es el primer consumidor: `#C3C6D4` no existía en las primitivas del destino, así que se registró [Foundations 0.1.16](foundations.scrollbar-colors.amendment.v0.1.16.md) y se comprobaron sus 30 bindings.

**Impacto:** los contratos previos que ya usan primitivas existentes no se reescriben ni revalidan por esta enmienda. Las familias futuras aplican esta regla solo tras evidencia de ausencia exacta. Auditoría humana de la extensión y publicación de biblioteca continúan separadas.
