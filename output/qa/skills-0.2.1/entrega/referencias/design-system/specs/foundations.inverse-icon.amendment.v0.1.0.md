---
contract_id: FOUNDATIONS-INVERSE-ICON-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-05
review_targets: [figma]
---

# Foundations · iconografía inversa

Extensión aditiva de FOUNDATIONS-TOKENS-001 bajo DEC-SEMANTIC-EXTENSIONS-001. No sustituye variables existentes ni modifica el inventario de origen.

El [JSON canónico de extensión](tokens/ai-design-system.inverse-icon.v0.1.0.json) gobierna exclusivamente nombre, tipo, description, scopes, codeSyntax y aliases del nuevo rol. Añade una variable semántica, cero primitivas y cero colecciones. Su primer consumidor es [Filter Chip 0.2.1](components/filter-chip.semantic.amendment.v0.2.1.md).

REQ-INV-001: crear o reutilizar por identidad verificada el rol en la colección semantic local y sus cuatro modos existentes. El ID generado se conserva en el registro de implementación, no se inventa en el JSON previo.

REQ-INV-002: cada alias debe apuntar a color/neutral/100 local, correspondiente al ID fuente VariableID:57:82 del inventario aprobado. No usar el RGB directo en consumidores ni cambiar el blanco.

REQ-INV-003: verificar por lectura independiente todos los campos del JSON y los cuatro aliases antes de vincular Chips. El código WEB documentado es metadato de handoff; no acredita implementación CSS.

La auditoría humana permanece PENDING; la creación de este rol no publica una biblioteca.
