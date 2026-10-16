---
contract_id: FILTER-CHIP-001
version: 0.2.1
type: component-amendment
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-05
review_targets: [figma]
slot_applicability: NOT_APPLICABLE
---

# Filter Chip · semántica inversa 0.2.1

Enmienda acotada al [contrato aprobado 0.2.0](filter-chip.contract.v0.2.0.md), bajo DEC-SEMANTIC-EXTENSIONS-001, MIGRATION-TOKEN-TRACEABILITY-001 y la autorización del usuario para continuar el refinamiento. No atribuye aprobación humana a esta revisión.

## Sustitución exacta

Sustituye únicamente los roles de texto e iconografía de las cuatro recetas `selected=true × state=default/hover/press/focus` de las secciones 7 y 10, el mapa derivado de esas recetas y AC-FC-006/007 en esa parte. Conserva los demás requisitos de 0.2.0, incluido el fondo neutral inverso, opacidades 100/92/85/100%, las 30 variantes y los iconos ocultos por defecto.

| Consumidor | Referencia histórica | Rol vigente | Variable local |
|---|---|---|---|
| 12 etiquetas seleccionadas habilitadas | color/text/on-brand | color/text/inverse | VariableID:13:31 |
| 24 vectores de iconos opcionales seleccionados habilitados | color/icon/on-brand | color/icon/inverse | ID generado, registrado en el estado de implementación |

REQ-FC-SEM-001 (MUST, DERIVED): texto e iconos sobre fondo neutral inverso consumen los roles inversos de su categoría, no roles de marca. La descripción canónica del fondo identifica intención neutral; las descripciones `on-brand` identifican marca. La igualdad RGB no satisface esta distinción.

REQ-FC-SEM-002 (MUST): preservar colores resueltos y opacidades, todos los IDs, geometría, fuentes, contenido, propiedades y dependencia Phosphor. No alterar los estados no seleccionados ni disabled. Las superficies `interactive/secondary/*` conservan las recetas explícitamente aprobadas de 0.2.0; esta enmienda no redefine esos estados.

REQ-FC-SEM-003 (MUST): reutilizar la variable local de texto e incorporar el único rol de icono definido por [Foundations inverse icon](../foundations.inverse-icon.amendment.v0.1.0.md), aliasando la primitiva blanca existente en los cuatro modos, sin nuevas primitivas ni cambios del inventario histórico.

## Fuentes y trazabilidad

Origen: Librería `9zs5RMR8LB5wHjW9Bd59BA`, set `8203:10`, [lectura de las 24 variantes](../../qa/implementations/filter-chip.semantic.v0.2.1.source.json). Se excluyen las seis x-small del destino y se distinguen las 12 combinaciones selected no Default derivadas de la descripción y aprobadas en 0.2.0.

Destino: AI-Design-System `tj3WIBEZDGLVs7MJWKCwgf`, página Chips `67:122`, set `72:298`. [Preflight](../../qa/implementations/filter-chip.semantic.v0.2.1.preflight.json) y [variables leídas](../../qa/implementations/filter-chip.semantic.v0.2.1.variables-before.json).

El [inventario canónico](../../sources/inventories/tokens.inventory.json), SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`, mantiene nombres, tipos, aliases, modos y description de los roles existentes. La extensión gobierna solo el nuevo rol. El mapa de IDs y su QA son evidencia derivada, no otro catálogo editable.

## Slots y límites

P-SLOTS 0.1.0: NOT_APPLICABLE. La anatomía sigue siendo etiqueta única y dos posiciones fijas opcionales de icono; TEXT, BOOLEAN e INSTANCE_SWAP cubren esas ediciones. No es una lista de cardinalidad variable. Se sustituye en la descripción Figma la palabra informal «slots» por «posiciones de icono» para no atribuir Slots nativos inexistentes.

No define comportamiento de producto, frontend, teclado ni publicación de biblioteca. Las limitaciones de contraste se conservan sin recolorear. La aprobación humana de 0.2.0 permanece histórica y no se transfiere a esta enmienda.

## Aceptación

- AC-FC-SEM-001: lectura posterior de 12 textos y 24 vectores con IDs locales y roles esperados; cero bindings on-brand en esos consumidores.
- AC-FC-SEM-002: 126 pinturas efectivas, incluidos iconos opcionales, con scopes y aliases correctos; omitir del conteo los 60 paints desactivados de envolturas Phosphor, no confundirlos con contenido visible.
- AC-FC-SEM-003: aliases de los roles de color comparados por nombre de modo y primitiva contra JSON; nuevo rol comprobado campo por campo.
- AC-FC-SEM-004: comparación antes/después sin cambio de estructura, geometría, tipografía, propiedades, colores u opacidades; captura posterior sin recortes ni superposiciones nuevos.
- AC-FC-SEM-005: 18 variantes comparables conservan los paints fuente; las 12 variantes derivadas se comparan con las recetas aprobadas, no se declaran observadas en la Librería.

## Changelog

0.2.1 — 2026-10-05: corrección semántica sobre fondo inverso, sin rediseño; precisión de terminología Slots.
