---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-TOKENS-001
name: Foundations y tokens del inventario recibido
type: tokens
status: IN_REVIEW
version: 0.1.0
owner: null
last_updated: 2026-09-22
review_targets:
  - figma
sources:
  - SRC-TOKENS-INV-001
  - SRC-TOKENS-AUD-001
data_refs:
  - sources/inventories/tokens.inventory.json
dependencies: []
---

# Contrato candidato: foundations y tokens

**No aprobado.** Los `MUST` siguientes son propuestas para revisión humana, no permiso de construcción. El inventario preservado es evidencia candidata; solo una aprobación explícita de esta versión y su digest le conferiría el alcance normativo indicado.

## 1. Propósito y alcance

Especificar la reconstrucción futura de las variables declaradas en `SRC-TOKENS-INV-001`, sin inventar componentes, usos concretos ni equivalencias web. El alcance inicial propuesto es Figma. El archivo de extracción declarado por el inventario y el archivo de reconstrucción son distintos.

## 2. Fuentes y propiedad de datos

| ID | Ruta y localizador | Versión/snapshot | Digest | Autoridad comprobada | Campos delegados si se aprueba |
|---|---|---|---|---|---|
| SRC-TOKENS-INV-001 | [Inventario](../../sources/inventories/tokens.inventory.json), `collections`, `fileKey` | Archivo recibido 2026-09-22 | SHA-256 bytes `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474` | Evidencia sin aprobación constatada | Colecciones, IDs de origen, nombres, tipos, modos, valores, aliases, `description`, scopes y `codeSyntax` |
| SRC-TOKENS-AUD-001 | [Auditoría](../../sources/audits/tokens.audit.md), “Ajustes realizados” y “Validación de integridad” | Informe recibido 2026-09-22 | SHA-256 bytes `5882f1b4be20ce0e038ec9ccdec262a54af2e749b633f52da7d21451a4ac15e3` | Informe sin aprobación constatada | Explicación de ajustes y límites; no redefine los campos del JSON |

El JSON sería el único propietario editable de los datos delegados. Este MD propone reglas de preservación, trazabilidad y aceptación; no replica el catálogo de 270 variables. Ante divergencia futura entre informe y JSON en un campo delegado, se detiene el requisito afectado y se solicita resolución.

## 3. Inventario y cobertura

| Colección | ID | Variables | Modos (ID) | Predeterminado | Fuente |
|---|---|---:|---|---|---|
| `primitive` | `VariableCollectionId:52:690` | 141 | `Value` (`52:0`) | `52:0` | `SRC-TOKENS-INV-001`, `/collections/0` |
| `semantic` | `VariableCollectionId:52:726` | 129 | `Contable` (`52:2`), `Administrativo` (`2849:0`), `Servicios` (`2849:1`), `Personas` (`2849:2`) | `52:2` | `SRC-TOKENS-INV-001`, `/collections/1` |

Total de esta versión: 270 variables (`COLOR`: 149; `FLOAT`: 110; `STRING`: 11). Todas contienen los campos `id`, `name`, `resolvedType`, `valuesByMode`, `description`, `scopes` y `codeSyntax`, y un valor para cada modo de su colección. El inventario no es prueba de que estos sean todos los foundations existentes fuera de este archivo.

## 4. Modelo de tokens

Las dos capas efectivamente declaradas son `primitive` y `semantic`. Los nombres cubren `color`, `font`, `spacing`, `size`, `radius`, `stroke` y `logo`. La mayoría de valores semánticos son aliases; `logo/categoria` contiene cadenas literales por modo. No se fusionarán tokens por compartir literal o valor resuelto. La intención por token se consulta en su `description`, no en una lista paralela aquí.

## 5. Requisitos candidatos

| ID | Requisito propuesto | Fuerza | Procedencia | Fuente | Comprobación |
|---|---|---|---|---|---|
| REQ-TOK-001 | Reconstruir las dos colecciones y sus modos, manteniendo identidad lógica, nombres y tipos declarados. | MUST | EXPLICIT | `SRC-TOKENS-INV-001`, `/collections` | AC-TOK-001 |
| REQ-TOK-002 | Preservar por variable y modo la distinción entre literal y `VARIABLE_ALIAS`, así como el destino lógico de cada alias; no sustituir aliases por literales visualmente equivalentes. | MUST | EXPLICIT + regla local de AGENTS.md | `SRC-TOKENS-INV-001`, `/collections/*/variables/*/valuesByMode`; [AGENTS.md](../../AGENTS.md) | AC-TOK-002 |
| REQ-TOK-003 | Preservar `description`, `scopes` y `codeSyntax` exactamente como figuran en esta versión del JSON; no crear un campo paralelo de uso. | MUST | EXPLICIT + regla local de AGENTS.md | `SRC-TOKENS-INV-001`, `/collections/*/variables/*`; [AGENTS.md](../../AGENTS.md) | AC-TOK-003 |
| REQ-TOK-004 | Registrar los IDs reales de variables y colecciones del destino y mapearlos a los IDs de origen, sin asumir que las cadenas de ID serán iguales entre archivos. | MUST | EXPLICIT | [P05](../../protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md), §6; [P06](../../protocols/06-QA-AND-VALIDATION.md), §4 | AC-TOK-004 |
| REQ-TOK-005 | Implementar y leer de vuelta solo en el destino Figma autorizado, `tj3WIBEZDGLVs7MJWKCwgf`, después de aprobación y verificación de capacidades. | MUST | EXPLICIT | [AGENTS.md](../../AGENTS.md); [P04](../../protocols/04-FIGMA-CONSTRUCTION.md) | AC-TOK-005 |

## 6. Modos y resolución de aliases

Hay 512 entradas `VARIABLE_ALIAS` y 145 valores literales por modo. El análisis del JSON recibido halló cero referencias a IDs ausentes, cero ciclos y cero incompatibilidades de `resolvedType`. Los 129 tokens semánticos tienen valores en sus cuatro modos y los 141 primitivos en `Value`. La resolución de un alias dirigido a `primitive` usa el único modo `Value` de esa colección; esta es una transformación de análisis, no una nueva relación almacenada. La reconstrucción debe conservar la referencia entre variables, no solo el color o número resuelto.

## 7. Descripciones canónicas

El único campo de documentación semántica por token es `description` en `SRC-TOKENS-INV-001`; las 270 variables tienen una cadena no vacía. No se crea `usage`, `figmaDescription` ni `aiDescription`. La auditoría explica cambios y reporta observaciones, pero no reemplaza esa descripción. Un uso específico de Button, Badge, Input u otro componente necesita fuente propia.

## 8. Tipos, unidades y conversiones

| Grupo/campo | Tipo de origen | Unidad demostrada | Figma | Web | Pendiente |
|---|---|---|---|---|---|
| Valores de color | `COLOR`; literales RGBA o aliases | Canales RGBA expresos | Conservar tipo, valores, aliases y modos | Fuera de alcance | Reglas de serialización web no entregadas |
| Dimensiones, espaciado, radios, trazos y tipografía numérica | `FLOAT` | `UNRESOLVED` para equivalencia CSS o unidades de plataforma | Conservar valor numérico y variable/binding | Fuera de alcance | No convertir a `px`, `%` o `em` por nombre |
| Familia, peso y categoría | `STRING` | No aplica como unidad física | Conservar cadenas y aliases | Fuera de alcance | No mapear pesos textuales a números sin contrato web |

`codeSyntax` es `{}` en las 270 variables. No se generarán nombres CSS/JS ni conversiones implícitas a partir de este vacío.

## 9. Reconstrucción en Figma

Destino propuesto: `AI-Design-System`, file key `tj3WIBEZDGLVs7MJWKCwgf`, según [AGENTS.md](../../AGENTS.md) y P04. El `fileKey` `9zs5RMR8LB5wHjW9Bd59BA` de `SRC-TOKENS-INV-001` es metadato del inventario y no cambia el destino. La futura implementación debe crear o reconciliar variables solo tras leer el estado real del destino, preservar colecciones, modos, campos y aliases, y producir un mapa de IDs de origen a IDs de destino. No se ha hecho lectura del destino ni construcción en esta fase. La regla de una página por familia aplica a componentes; este contrato no inventa una página de foundations.

## 10. Consumo web

Fuera del alcance de esta versión. Naming, unidades, conversiones, modos y pruebas web permanecen sin contrato de implementación; `codeSyntax: {}` no los define.

## 11. Cambios de auditoría, conflictos y límites

| Hallazgo | Fuente | Presente en el JSON recibido | Decisión o límite | Destino |
|---|---|---|---|---|
| `font/size/2xs`, scope `FONT_STYLE` en cuatro pesos, alias naranja de `color/border/subtle` en Servicios y scopes de fondos/estados interactivos | `SRC-TOKENS-AUD-001`, “Ajustes realizados” | Sí; contrastado contra IDs y campos actuales | No se reaplican. El estado previo no fue entregado: el diff histórico no está verificado. | Figma futuro |
| Descripción de `color/background/overlay` | `SRC-TOKENS-AUD-001`, §7 | Sí | El informe atribuye la precisión a consumidores de Modal; no se inspeccionaron aquí. | Figma futuro |
| Diferencias de scopes en iconos de feedback, `ALL_SCOPES` complementario y `logo/categoria` | `SRC-TOKENS-AUD-001`, “Observaciones auditadas que NO se modificaron” | Sí | Preservar, no normalizar por apariencia. | Figma futuro |
| `fileKey` fuente distinto del destino | `SRC-TOKENS-INV-001`, `/fileKey`; AGENTS.md | Sí | Roles distintos, no contradicción de destino. | Figma futuro |

No consta aprobación previa del inventario. La auditoría dice que hubo ajustes “autorizados”, pero no incluye la decisión humana verificable ni la versión anterior; esa afirmación no se adopta como aprobación de este candidato.

## 12. Acceptance criteria

| ID | Requisito | Destino | Comprobación posterior a construcción | Evidencia requerida |
|---|---|---|---|---|
| AC-TOK-001 | REQ-TOK-001 | Figma | Leer colecciones, modos, nombres y tipos; comparar todas las entidades con el inventario exacto. | Snapshot de lectura y mapa de IDs |
| AC-TOK-002 | REQ-TOK-002 | Figma | Comparar cada `valuesByMode` y los 512 enlaces de alias usando el mapa de IDs, sin sustituir por literals. | Lectura completa de variables y grafo de aliases |
| AC-TOK-003 | REQ-TOK-003 | Figma | Comparar las 270 descripciones, scopes y `codeSyntax` campo por campo. | Snapshot completo o evidencia equivalente verificable |
| AC-TOK-004 | REQ-TOK-004 | Registro | Resolver cada ID fuente a un ID de destino real y comprobar que la relación no es ambigua. | Registro de implementación y mapa |
| AC-TOK-005 | REQ-TOK-005 | Figma | Comprobar file key del destino y readback posterior al último cambio. | Localizador y registro QA de implementación |

Si la herramienta no expone algún campo requerido, la comprobación afectada queda `BLOCKED`, no `PASS` por parecido visual.

## 13. Versionado y aprobación

Esta es la versión candidata `0.1.0`, `IN_REVIEW`. Aprobación humana: **pendiente**. No hay implementación ni validación Figma. Una eventual aprobación debe identificar esta versión, su SHA-256 de bytes, el SHA-256 del inventario y el alcance Figma, y resolver cualquier cambio solicitado en una revisión explícita. `READY` para Figma no se puede establecer antes de ese gate y de verificar destino/capacidades.

## 14. Changelog

| Versión | Fecha | Cambio | Fuente/decisión |
|---|---|---|---|
| 0.1.0 | 2026-09-22 | Primer candidato a partir del inventario y auditoría recibidos; no aprobado | `SRC-TOKENS-INV-001`, `SRC-TOKENS-AUD-001` |

## Anexo de revisión

Véanse el [reporte de síntesis](../reports/foundations-tokens.synthesis.md) y la [revisión documental](../../qa/contracts/foundations-tokens.review.md). Ambos registran la cobertura y las preguntas pendientes sin sustituir los datos canónicos.
