---
contract_id: MIGRATION-TOKEN-TRACEABILITY-001
version: 0.1.0
status: APPROVED
scope: legacy-library-to-ai-design-system
source_file_key: 9zs5RMR8LB5wHjW9Bd59BA
destination_file_key: tj3WIBEZDGLVs7MJWKCwgf
canonical_token_data: sources/inventories/tokens.inventory.json
canonical_token_data_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
decision_refs:
  - DEC-LEGACY-MIGRATION-DELEGATION-001
  - DEC-SEMANTIC-EXTENSIONS-001
  - DEC-MIGRATION-VISUAL-FIDELITY-001
  - DEC-MIGRATION-CONTRAST-LIMITATIONS-001
  - DEC-MIGRATION-TRACEABILITY-001
last_updated: 2026-09-24
---

# Contrato transversal · fidelidad y trazabilidad de tokens

Este contrato fija **cómo** se documenta y comprueba cada componente migrado. La instrucción del usuario aprueba esta regla de trabajo, **no** aprueba retrospectivamente los contratos de cada familia ni declara conformes sus implementaciones. Se aplica a contratos existentes cuando se revalidan y a todos los siguientes. [AGENTS.md](../AGENTS.md) y los protocolos P02–P06 siguen rigiendo estados, autorización, construcción y QA.

## Autoridad y definición única

1. El contrato vigente de cada familia gobierna anatomía, variantes, estados, roles de consumo y criterios de aceptación. Sus enmiendas sustituyen solo los requisitos que identifican; una enmienda antigua no prevalece por fecha o nombre.
2. El [inventario aprobado](../sources/inventories/tokens.inventory.json), vinculado por `FOUNDATIONS-TOKENS-001`, gobierna nombre, tipo, modos, valores, aliases, scopes y la única `description` de cada token heredado. Las extensiones de destino versionadas gobiernan **solo** los tokens nuevos o overrides que declaran. Este MD no es un segundo catálogo de valores o descripciones.
3. El archivo Figma fuente es evidencia visual y estructural; el Figma destino aporta los IDs locales y el readback de bindings. Un snapshot o un QA anterior no prueba el estado actual del archivo.
4. El [registro de decisiones](../registry/decisions.md) gobierna el criterio explícito del usuario. La [auditoría por excepciones](MIGRATION-AUDIT.md) conserva tensiones o limitaciones y la [matriz de cobertura](MIGRATION-TRACEABILITY-STATUS.md) conserva el estado de comprobación; ninguno sustituye el contrato de familia.

## Cadena obligatoria por consumidor

Para cada pintura, propiedad tipográfica, efecto, tamaño o espacio tokenizado que consuma una variante, el contrato y su evidencia de QA deben permitir reconstruir esta cadena:

`nodo/propiedad de origen → color o valor observado por modo → primitiva aprobada → rol semántico de destino → variable local por ID → nodo/propiedad vinculada en Figma → readback y captura`.

La matriz del contrato puede referenciar el JSON y las evidencias por localizador en vez de repetir todos sus valores. Debe distinguir `EXPLICIT`, `OBSERVED`, `DERIVED`, `INFERRED`, `UNRESOLVED` y `CONFLICT`. Si el origen tiene un literal sin primitiva idéntica, registrarlo como excepción; no fingir equivalencia. Si la apariencia coincide pero el rol es incorrecto, el binding no pasa QA.

| ID | Regla obligatoria | Verificación mínima |
|---|---|---|
| REQ-MTT-001 | Conservar el color y demás rasgos visuales de origen al reconstruir; una mejora semántica no los cambia silenciosamente. | Comparación fuente/destino por estado y modo, con pares de color y captura. |
| REQ-MTT-002 | Consumir el rol correspondiente al uso: texto→texto, superficie→background, trazo→border, iconografía→icon, efecto→effect/focus y propiedades tipográficas→tipo compatible. El scope Figma debe admitir exactamente ese consumidor. | Readback de nombre, tipo, `scopes`, `description`, `boundVariables` y propiedad consumidora. |
| REQ-MTT-003 | Vincular cada rol a la primitiva documentada mediante aliases verificables en **todos** los modos; igualdad RGB aislada no basta. | Comparación campo por campo entre JSON canónico/extensión y variable local, con mapa de IDs origen→destino. |
| REQ-MTT-004 | Si falta un rol, crear una extensión semántica de destino versionada, con alias a primitiva existente, JSON/contrato/QA antes de Figma y readback después. No inventar primitiva ni modificar el inventario histórico de origen. | Digest de JSON de extensión, contrato de Foundations, variable local y aliases por modo. |
| REQ-MTT-005 | Si el color de origen limita el contraste, conservarlo y marcar la medición verificada con `*` para revisión interna. No declarar accesibilidad aprobada ni recolorear solo para cumplir un umbral. | Par medido, ratio, contexto y aplicabilidad del criterio en la auditoría. |
| REQ-MTT-006 | No promover un contrato a `specs/` ni dar QA cromático `PASS` con un readback obsoleto o contradicción material. La auditoría humana continúa `PENDING` bajo la delegación. | QA documental y de implementación vigentes, estado de publicación y excepción trazados por separado. |

## Puerta de revisión para contratos existentes

Cada familia ya construida vuelve a pasar una revisión de trazabilidad en la [matriz](MIGRATION-TRACEABILITY-STATUS.md). La revisión incluye todas sus variantes y estados, no solo una muestra: IDs de fuente y destino, consumidor visible, binding real, rol/scope, alias por modo, par cromático, tipografía y excepciones. Un `PASS` histórico previo a las decisiones de fidelidad y contraste puede seguir vigente para estructura, pero queda `STALE` para color hasta nuevo readback. Las divergencias se corrigen mediante enmienda acotada y QA nuevo, conservando el historial.

## Puerta para nuevas familias

Antes de construir: inspección profunda de la fuente, contrato versionado con página semántica y matriz de tokens, QA documental, preflight de variables/dependencias y ausencia de conflicto bloqueante. Después: readback completo, comparación visual, QA de bindings y aliases, registro de IDs/estado, y actualización de la matriz. `DELEGATED_FOR_BUILD` no significa `APPROVED`; `VALIDATED` técnico no significa publicado en la biblioteca ni auditado por el usuario.

## Criterios de aceptación de esta regla

- `AC-MTT-001`: ningún contrato nuevo omite la cadena de procedencia y binding anterior; un campo desconocido queda señalado, nunca completado por conjetura.
- `AC-MTT-002`: el QA puede demostrar paridad entre JSON, variable local y consumidor en cada modo, o reportar la discrepancia específica.
- `AC-MTT-003`: la matriz indica con claridad qué familias ya fueron revalidadas bajo esta versión y cuáles aún no; no convierte cobertura documental en conformidad visual.
- `AC-MTT-004`: toda excepción material apunta a evidencia y decisión pendiente o limitación aceptada en un solo documento de auditoría.

## Cambio de esta regla

Una modificación futura de este contrato requiere versión nueva, decisión registrada y análisis de impacto sobre contratos/QA existentes. Los valores de tokens se cambian solo en su JSON canónico o extensión aplicable y se sincronizan con Figma; nunca se editan indirectamente desde este MD.
