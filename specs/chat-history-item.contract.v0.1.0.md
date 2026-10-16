---
contract_id: CHAT-HISTORY-ITEM-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
figma_page_name: Chat
slot_applicability: REQUIRED
---

# Chat History Item

## 1. Purpose

Dependencia local reutilizable de Chat Toolbar, fuente20355:72852.

## 2. Contract

CHAT-HISTORY-ITEM-001; construcción CREATE en páginaChat783:6 por delegación externa.

## 3. Anatomy

Horizontal258×40, FILL enToolbar232; minHeight40,HUG. Padding8/16, radio8; gap8 en no seleccionado default y16 en otros. Title FILL/HUG14/20; timestamp12/20Medium. Acciones2iconos24/gap16 en Hover; timestamp oculto entonces.

## 4. Properties

Updated TEXT=1 sem; Title SLOT; Actions SLOT. Título editable directamente dentro de Title, no propiedad cruzada del anfitrión.

## 5. Variants

Selected=false/true × State=Default/Hover (4).

## 6. Sizes

Horizontal258×40, FILL enToolbar232; minHeight40,HUG. Padding8/16, radio8; gap8 en no seleccionado default y16 en otros. Title FILL/HUG14/20; timestamp12/20Medium. Acciones2iconos24/gap16 en Hover; timestamp oculto entonces.

## 7. States

Default transparente; Hover color/interactive/secondary/hover; Selected ambos estados color/surface/brand. Título primary, timestamp tertiary, iconosprimary.

## 8. Behavior

ON_HOVER Default→Hover para cada Selected. No cambiar Selected porclick ni inventar pin/delete. La booleana fuente it\u0027s collapsible no tiene función comprobada y no se propaga.

## 9. Accessibility

No certificación; hereda límites y requisitos futuros de Chat Toolbar, especialmente acceso alternativo a acciones Hover.

## 10. Design tokens

Consume exclusivamente roles y preflight de [Chat Toolbar](./chat-toolbar.contract.v0.1.0.md#10-design-tokens). No JSON paralelo ni tokens nuevos.

## 11. Content rules

Etiquetas de muestra editables; wrapping con altura automática, sin límite ficticio de caracteres.

## 12. Composition rules / Slots

Title y Actions REQUIRED; Title demo un texto, Actions demo PushPin y DotsThree. Ambos existen en todas las variantes, Actions oculto Default. Sin máximo; probar0/1/3, swap y overrides entreHover/Selected.

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

[Fuente read-only](../drafts/contracts/chat-history-item.source.component-contract.md), [organismo](./chat-toolbar.contract.v0.1.0.md), [delegación](../registry/DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md).

## 20. Change management

Promover con organismo tras QA técnico; cambios posteriores en specs versionados, grafo sincronizado.

## 21. Deviations and readiness

API simplificada y roles temáticos documentados antes de construir; READY documental, implementación NOT_STARTED. No aprobación humana simulada.

## 22. Cierre técnico · 2026-10-08

QA documental e implementación PASS. [Evidencia y límites](../qa/implementations/chat-toolbar.v0.1.0.review.md), [IDs y lectura final](../qa/implementations/chat-toolbar.v0.1.0.final.json). PáginaChat783:6; Toolbar798:284, Tool Item796:494, History Item796:495; revisión798:290. Nueve variantes;36 roles/144 aliases sin variables nuevas. Esta sección actualiza el NOT_STARTED de la preparación histórica: implementación VALIDATED para el contrato visual, user_audit PENDING por excepciones. Promovido a specs; ajustes posteriores aquí. Biblioteca remota no publicada.

