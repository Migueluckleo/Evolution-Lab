---
contract_schema: sdd-project/0.2
contract_id: LOADER-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: LOADER-001
amends_version: 0.1.0
typography_applicability: NOT_APPLICABLE
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# Loader · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda registra, por delegación específica de esa tarea, la exclusión tipográfica justificada de `LOADER-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../loader.contract.v0.1.0.md) y documenta que su anatomía no presenta consumidores tipográficos; no sustituye sus reglas de artwork ni crea una asignación de TextStyle. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

NOT_APPLICABLE: el indicador, sus variantes y secuencias de movimiento no contienen texto. El contrato prohíbe añadir porcentaje o tiempo estimado. Una etiqueta accesible web no es un texto Figma existente.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Loaders](../../sources/figma-snapshots/typography/census.before.377-122.json) | Página `377:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `0a6e8d1ea50d682b4faf247dec74520069fca48416122e8133047fd229d25cbb`. |
| [Base histórica](../loader.contract.v0.1.0.md) | SHA-256 `2e20f1d300bef2c53acbbf79b400343efb344fb47a555b45e2afed62099bcf6b`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **0 nodos UI, 0 rangos, 0 estilos lógicos**. La revisión incluyó descendientes ocultos y dependencias del alcance censado. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

El censo registra **cero textos UI** en esta página y 0 textos editoriales `DOCUMENTATION`. `NOT_APPLICABLE` acredita ausencia de consumidor textual en el alcance observado, no omisión del análisis ni un PASS de migración.

No existe un TextStyle ID que asignar a vectores, imágenes, tracks o geometría. Si una futura revisión añade texto editable a esta familia, deberá declarar el rol y su estilo antes de construir; no hereda esta exclusión.

## Aceptación y estado de implementación

| Criterio | Evidencia requerida |
|---|---|
| TYP-FAM-01 · cobertura | Reconciliar todos los nodos/rangos de esta familia, incluidos ocultos, muestras e instancias; justificar cualquier sustitución de ID con trazabilidad anterior→nuevo. |
| TYP-FAM-02 · exclusión | Confirmar que la familia continúa sin texto UI y que ningún artwork se convirtió en texto para satisfacer un conteo artificial. |
| TYP-FAM-03 · integridad | Preservar contenido, colores/bindings ajenos, geometría, API de propiedades, variantes, Slots e instancias; documentar cualquier cambio técnico necesario y comprobar sus consumidores. |
| TYP-FAM-04 · aislamiento | Volver a leer componentes que comparten propiedades o dependencias, con pruebas de texto y cambio de variante cuando correspondan; no validar desde el resultado inmediato de un setter. |
| TYP-FAM-05 · destinos | Separar QA documental, asignación Figma, preservación, web y publicación de skills. El PASS anterior de estilos/web no prueba este nuevo consumo Figma. |

Esta enmienda fija requisitos y cobertura documental. **La validación de consumidores requiere el QA final de la tarea de aplicación.** El bloqueo histórico y sus pruebas se conservan en [Figma-blocker.md](../../qa/implementations/typography/Figma-blocker.md); ni esta tabla ni la presencia del catálogo lo convierten en `VALIDATED`. La evidencia nueva debe registrar por separado su resolución o las diferencias restantes.

## Cambio versionado

| Versión | Fecha | Cambio |
|---|---|
| 0.1.0 | 2026-10-15 | Identidades tipográficas explícitas por consumidor y variante, con fuentes conservadas y auditoría humana pendiente. |
