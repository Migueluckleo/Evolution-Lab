---
amendment_id: AMD-BUTTON-LOCAL-BINDINGS-001
applies_to: BUTTON-001
base_contract_version: 0.2.0
version: 0.2.2
status: DELEGATED_FOR_BUILD
user_audit: PENDING
operation: UPDATE
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
target_page: Buttons
target_page_id: "0:1"
target_set_id: "26:81"
slot_applicability: NOT_APPLICABLE
data_ref: sources/inventories/tokens.inventory.json
data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
last_updated: 2026-10-05
---

# Buttons · sustitución acotada de bindings externos

## Autoridad y sustitución

La solicitud de continuar los pendientes y la decisión transversal [DEC-MIGRATION-TRACEABILITY-001](../../registry/decisions.md) autorizan corregir esta brecha confirmada, bajo la delegación y auditoría posterior de P03/P04. Este detalle no recibe aprobación humana implícita.

Esta enmienda sustituye **solo** la preservación de nueve variables remotas en REQ-BTN-004/AC-BTN-004 y §10 de [BUTTON-001 0.1.0](button.contract.md), incorporados por [0.2.0](button.contract.v0.2.0.md). Para esos bindings, la referencia exigida pasa a ser la variable semántica local equivalente del JSON aprobado. No sustituye las reglas de uso 0.2.0, la página Buttons ni la [corrección de texto Disabled 0.2.1](button.semantic-scope-amendment.v0.2.1.md).

## Fuentes y mapa

- OBSERVED: descubrimiento previo de [nueve variables remotas](../../qa/implementations/buttons.refinement.v0.1.0.remote-variables.json).
- OBSERVED: [preflight y mapa derivado 0.2.2](../../implementations/figma/buttons.local-bindings.v0.2.2.token-map.json): IDs reales, modos, aliases y equivalencia con el JSON.
- OBSERVED: [estado previo y plan por nodo/propiedad](../../qa/implementations/buttons.local-bindings.v0.2.2.before.json), 60 variantes, 364 nodos y 722 referencias en 123 nodos afectados.
- EXPLICIT: [contrato transversal](../MIGRATION-TOKEN-TRACEABILITY.contract.md), JSON canónico y autorizaciones referidas. El JSON conserva autoridad exclusiva sobre nombres, tipos, modos, valores, aliases, scopes y description. Los snapshots son evidencia, no otro catálogo editable.

| Rol semántico existente | ID local verificado | Scope | Referencias que sustituir |
|---|---|---|---:|
| spacing/sm | VariableID:12:30 | GAP | 170 |
| spacing/lg | VariableID:12:32 | GAP | 90 |
| spacing/xs | VariableID:12:29 | GAP | 40 |
| radius/md | VariableID:13:6 | CORNER_RADIUS | 252 |
| stroke/xs | VariableID:12:41 | STROKE_FLOAT | 60 |
| stroke/md | VariableID:13:3 | STROKE_FLOAT | 48 |
| font/weight/bold | VariableID:10:6 | FONT_STYLE | 45 |
| font/weight/regular | VariableID:10:3 | FONT_STYLE | 15 |
| font/family/base | VariableID:10:2 | FONT_FAMILY | 2 |

DERIVED: los seis roles numéricos y Bold conservan valores idénticos en Contable, Administrativo, Servicios y Personas. Los strings externos Regular/Manrope difieren en capitalización del JSON regular/manrope; no son bytes idénticos. La sustitución exige conservar el fontName renderizado Manrope Regular/Bold y sus métricas, usando las fuentes disponibles verificadas. Si cambia la fuente real o la geometría, no pasa QA y se revierte el binding afectado. No se altera el JSON ni se crean adaptadores o variables nuevas.

## Requisitos y aceptación

| ID | Regla MUST / MUST NOT | Comprobación |
|---|---|---|
| REQ-BTN-LOCAL-01 | Sustituir exactamente las 722 referencias identificadas por sus nueve roles semánticos locales; nunca por primitivas ni literales. | Readback independiente de cada nodo/propiedad del plan, cero referencias a los nueve IDs remotos y resolución local conforme al JSON en los cuatro modos. |
| REQ-BTN-LOCAL-02 | Conservar los 60 IDs de variantes, el set 26:81, página 0:1, anatomía, propiedades, defaults, contenido, fuentes renderizadas, geometría, pinturas, iconos y reacciones. | Comparación previa/posterior por categorías, dimensiones de variantes y captura del set. Ningún cambio de color ni corrección de interacciones. |
| REQ-BTN-LOCAL-03 | No modificar variables compartidas, inventario, principales Phosphor ni overrides de consumidores. | QA de paridad de valores/aliases y regresión acotada en Footer/Basic/Media/SideBySide de Modal y Empty states. Sidebar se comprueba como control sin consumidor directo de Buttons; no se reconstruye. |
| REQ-BTN-LOCAL-04 | Mantener trazabilidad en specs y separar QA técnico, auditoría humana y publicación de biblioteca. | Enmienda, QA documental, QA Figma y estado enlazados; user_audit PENDING. Sin publicación remota ni frontend. |

Cobertura de regresión: raíces Modal 566:280,567:360,569:301,569:327 (20 instancias contando helper y composiciones), Empty states 645:275 (ocho instancias) y controles Sidebar 615:355,619:480,619:607. Es un alcance delimitado, no un censo global de todas las instancias del archivo.

## Revisión P-SLOTS 0.1.0

NOT_APPLICABLE justificado: Button tiene una etiqueta editable y dos posiciones fijas de icono gobernadas por Boolean/INSTANCE_SWAP. No presenta una lista de hijos de cardinalidad variable. El término histórico “slot izquierdo/derecho” no acredita un Slot nativo y no lo exige para estos swaps individuales. Las regiones extensibles pertenecen a sus anfitriones Modal/Empty states, cuyos Slots no se cambian en esta corrección.

## Límites y gestión

No revalida globalmente contraste, colores por todos los temas, comportamiento web, teclado ni las 1512 alternativas Phosphor. Conserva las limitaciones históricas. Las huellas de regresión FNV-1a:length son detectores de cambio, no hashes criptográficos de fuente; los hashes de archivos se calculan aparte.

2026-10-05: candidata 0.2.2 creada en specs antes de aplicar el ajuste, con preflight de nueve pares y cuatro modos. La promoción de estado requiere QA documental; implementación aún no realizada en este punto del historial.

2026-10-05: QA documental PASS ([revisión](../../qa/contracts/button.local-bindings.v0.2.2.review.md)); estado delegado habilitado para el ajuste exacto, sin aprobación humana del detalle.

2026-10-05: implementación y [QA Figma](../../qa/implementations/button.local-bindings.v0.2.2.figma.review.md) PASS acotados. 722 referencias locales, 60 variantes y cero píxeles cambiados. Consumidores comprobados sin regresiones; auditoría humana PENDING.
