---
contract_schema: sdd-project/0.2
contract_id: LOGOS-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: LOGOS-001
amends_version: 0.1.0
typography_applicability: NOT_APPLICABLE
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# Logos · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda registra, por delegación específica de esa tarea, la exclusión tipográfica justificada de `LOGOS-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../../drafts/contracts/logos.contract.v0.1.0.md) y documenta que su anatomía no presenta consumidores tipográficos; no sustituye sus reglas de artwork ni crea una asignación de TextStyle. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [logos.scope.amendment.v0.1.1.md](logos.scope.amendment.v0.1.1.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

NOT_APPLICABLE: las letras de los logotipos son artwork vectorial y no se convierten en texto editable. Los cuatro textos del censo de la página son documentación sin owner de componente; no son parte de las 72 variantes de artwork ni de los 12 assets sueltos. La excepción de Logos sin variables internas permanece vigente.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Logos](../../sources/figma-snapshots/typography/census.before.427-122.json) | Página `427:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `20b2b77f065459c44f4c5a7cfe1bb6ef6e15803a67e072de4e46b7af998df09a`. |
| [Base histórica](../../drafts/contracts/logos.contract.v0.1.0.md) | SHA-256 `088b7e86d695541b4587b891a658a2d50e1843e9bb0e98a1ef0cdfc340bf4f56`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **0 nodos UI, 0 rangos, 0 estilos lógicos**. La revisión incluyó descendientes ocultos y dependencias del alcance censado. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

El censo registra **cero textos UI** en esta página y 4 textos editoriales `DOCUMENTATION`. `NOT_APPLICABLE` acredita ausencia de consumidor textual en el alcance observado, no omisión del análisis ni un PASS de migración.

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
