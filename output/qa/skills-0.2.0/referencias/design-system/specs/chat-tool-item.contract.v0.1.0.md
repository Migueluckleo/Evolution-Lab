---
contract_id: CHAT-TOOL-ITEM-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
figma_page_name: Chat
slot_applicability: REQUIRED
---

# Chat Tool Item

## 1. Purpose

Dependencia local reutilizable de Chat Toolbar, fuente20355:72830.

## 2. Contract

CHAT-TOOL-ITEM-001; construcción CREATE en páginaChat783:6 por delegación externa.

## 3. Anatomy

Horizontal186×40 en principal; FILL en Toolbar232. Padding8/16, gap16; icono24, label14/20 Regular, radio8. Área principal horizontal gap4 y etiqueta FILL/HUG; caret24 opcional. Extra actions horizontalHUG con Chats24 demo.

## 4. Properties

Label TEXT=Nuevo chat; Icon INSTANCE_SWAP=NotePencil; Show caret BOOLEAN=false; Show extra actions BOOLEAN=false; Extra actions SLOT.

## 5. Variants

State=Default/Hover/Disabled (3). Fuente available=true,hover=false / true,true / false,false.

## 6. Sizes

Horizontal186×40 en principal; FILL en Toolbar232. Padding8/16, gap16; icono24, label14/20 Regular, radio8. Área principal horizontal gap4 y etiqueta FILL/HUG; caret24 opcional. Extra actions horizontalHUG con Chats24 demo.

## 7. States

Default transparente; Hover color/interactive/secondary/hover; Disabled texto color/interactive/disabled/text e iconos color/icon/disabled. Resto primary con roles texto/icono separados.

## 8. Behavior

Solo ON_HOVER Default→Hover300ms. Disabled sin reacción. Caret visible no define acordeón o destino.

## 9. Accessibility

No certificación; hereda límites y requisitos futuros de Chat Toolbar, especialmente acceso alternativo a acciones Hover.

## 10. Design tokens

Consume exclusivamente roles y preflight de [Chat Toolbar](./chat-toolbar.contract.v0.1.0.md#10-design-tokens). No JSON paralelo ni tokens nuevos.

## 11. Content rules

Etiquetas de muestra editables; wrapping con altura automática, sin límite ficticio de caracteres.

## 12. Composition rules / Slots

Extra actions REQUIRED, sin cardinalidad máxima; 0/1/3, reorder/replace, no detach. Hidden por Show extra actions; Hidden no equivale a Disabled.

## 13. Responsive behavior

FILL/HUG dentro del ancho264–310 de Toolbar; auto layout y crecimiento en altura.

## 14. Edge cases

QA de edición de texto, contenido0/1/3 y más que demo, reorder/replace, variants y cuatro temas.

## 15. Forbidden combinations

No primitive fills, textroles en iconos, detach ni modificación de dependencias compartidas.

## 16. Design ↔ Code mapping

Figma solamente, no lógica de producto implementada.

## 17. Acceptance criteria

Número de variantes correcto, Slots nativos editables y preservados, bindings semánticos, geometría y QA visual.

## 18. Examples

Instancias de cada estado en muestra conjunta; principales separados.

## 19. Source of truth

[Fuente read-only](../drafts/contracts/chat-tool-item.source.component-contract.md), [organismo](./chat-toolbar.contract.v0.1.0.md), [delegación](../registry/DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md).

## 20. Change management

Promover con organismo tras QA técnico; cambios posteriores en specs versionados, grafo sincronizado.

## 21. Deviations and readiness

API simplificada y roles temáticos documentados antes de construir; READY documental, implementación NOT_STARTED. No aprobación humana simulada.

## 22. Cierre técnico · 2026-10-08

QA documental e implementación PASS. [Evidencia y límites](../qa/implementations/chat-toolbar.v0.1.0.review.md), [IDs y lectura final](../qa/implementations/chat-toolbar.v0.1.0.final.json). PáginaChat783:6; Toolbar798:284, Tool Item796:494, History Item796:495; revisión798:290. Nueve variantes;36 roles/144 aliases sin variables nuevas. Esta sección actualiza el NOT_STARTED de la preparación histórica: implementación VALIDATED para el contrato visual, user_audit PENDING por excepciones. Promovido a specs; ajustes posteriores aquí. Biblioteca remota no publicada.

