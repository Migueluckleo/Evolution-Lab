---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-TYPOGRAPHY-001-FORMATTING-001
name: Consumo de subrayado mediante estilos compartidos
type: amendment
status: DELEGATED_FOR_BUILD
user_audit: PENDING
version: 0.1.1
last_updated: 2026-10-15
amends: specs/foundations/typography.contract.v0.1.0.md
data_refs:
  - specs/tokens/ai-design-system.typography.v0.1.1.json
supersedes_scope: Selección del catálogo activo y tratamiento de UNDERLINE como override posterior en 27 rangos existentes
slot_applicability: NOT_APPLICABLE
readiness_by_target:
  figma: BLOCKED
  web: READY
---

# Tipografía: formato subrayado · enmienda 0.1.1

La [delegación específica](../../registry/DEC-TYPOGRAPHY-STYLES-001.md) autoriza 18 estilos base y los complementarios necesarios para integrar las recetas existentes, manteniendo geometría, identidad y API de los componentes. Esta enmienda registra una solución técnica `DERIVED` dentro de ese alcance; su detalle mantiene auditoría humana `PENDING`. Las pruebas de implementación constituyen evidencia, no una aprobación humana.

## Alcance sustituido

El catálogo activo pasa a [ai-design-system.typography.v0.1.1.json](../tokens/ai-design-system.typography.v0.1.1.json): 79 estilos, 18 base y 61 complementarios. Conserva todas las métricas, unidades, bindings y tres derivaciones de escala de la versión 0.1.0. Explicita `textDecoration: NONE` para los 75 estilos previos y añade cuatro estilos de formato `UNDERLINE` para las recetas que ya lo requieren. Los datos 0.1.0 y sus resultados históricos se conservan sin reescribir.

Esta enmienda sustituye únicamente la selección del catálogo y el tratamiento del subrayado como setter/override posterior a la asignación de estilo, en §§1,3–4,7–8 del contrato 0.1.0 y sus referencias consumidoras afectadas. El resto del contrato sigue vigente: contenido, color, métricas, layout, propiedades, IDs y Slots conservan sus requisitos. La versión nueva no transforma un `FAIL` histórico en `PASS` ni acredita por sí sola consumo Figma.

## Cuatro identidades y consumidores existentes

| Estilo lógico | Receta de origen | Rangos existentes | Uso acotado |
|---|---|---:|---|
| `ui-action-label-medium-underline` | `ui-action-label-medium` | 10 | Button Link Middle/Large |
| `ui-action-label-small-underline` | `ui-action-label-small` | 5 | Button Link Small |
| `ui-action-label-normal-underline` | `ui-action-label-normal` | 8 | Link dentro de Empty states, incluidas muestras anidadas |
| `ui-upload-action-feedback-underline` | `ui-upload-action-feedback` | 4 | Acción de File Upload; success/error conservan NONE |

El JSON es el único propietario de nombres, descripciones de uso, recetas y `consumerScope.ranges`. El [mapping 0.1.1](../../implementations/figma/typography.v0.1.1.mapping.json) debe reasignar exclusivamente esos 27 rangos; los otros 3,326 rangos UI conservan su ID lógico. Los 150 textos editoriales históricos siguen fuera del alcance. El universo anterior continúa siendo 34 páginas, 3,501 nodos y 3,503 rangos; la implementación UI comprende 3,351 nodos y 3,353 rangos.

`derivedFormattingFrom` identifica `baseStyleId`, `overrides: {textDecoration: UNDERLINE}` y el motivo. Exige igualdad exacta de familia, peso, tamaño, interlineado, tracking y `tokenRefs` con la receta de origen. Es distinto de `derivedFrom`, que conserva exclusivamente las tres escalas Float32 ya documentadas. Ninguna derivación de formato introduce tamaños, tokens o primitivas; no modifica escalas de instancia.

## Evidencia y técnica de aplicación

Los censos anteriores de [Buttons](../../sources/figma-snapshots/typography/census.before.0-1.json), [Input Fields/File Upload](../../sources/figma-snapshots/typography/census.before.394-122.json) y [Empty states](../../sources/figma-snapshots/typography/census.before.639-128.json) registran el subrayado existente. Los contratos y los hashes específicos se identifican por estilo en el catálogo.

El [ensayo de setter de decoración](../../qa/implementations/typography/consumption-v0.1.1/probe.decoration-setter.failure.json) conserva su `FAIL`: once asignaciones causaron 140 discrepancias de comprobación en el clon. El [ensayo con estilos que contienen UNDERLINE](../../qa/implementations/typography/consumption-v0.1.1/probe.format-styles.persisted-and-instance-edit.json) registra cero errores de persistencia, de edición de propiedades TEXT en seis instancias y de sus efectos sobre los maestros de la copia. Este piloto sustenta la técnica de aplicación; no valida las 43 familias ni sustituye el censo final.

La implementación aplica `setRangeTextStyleIdAsync(start,end,id)` con intervalos del snapshot/mapping y estilos completos. Conserva los bindings anteriores compatibles, carga fuentes actuales y destino y evita setters de formato posteriores para reparar el resultado. No elimina ni recrea textos, propiedades o referencias. Debe conservar `componentPropertyDefinitions`, `componentPropertyReferences`, contenido, IDs y overrides ajenos al cambio; un ID de estilo sin propiedades concordantes no satisface el contrato.

Si la aplicación deja una propiedad divergente, registrar el fallo y detener la operación afectada: no corregir silenciosamente medidas ni fabricar una receta adicional. Los 103 rangos escalados conservan las tres recetas materializadas históricas y la separación `recipeScale = 1` / `instanceScale`, pero su aplicación Figma queda **UNRESOLVED_SCALED_LINK**. El [ensayo de receta derivada](../../qa/implementations/typography/consumption-v0.1.1/probe.scaled-derived.failure.json) registra que el setter por rango vuelve a escalarla; el [ensayo de receta principal](../../qa/implementations/typography/consumption-v0.1.1/probe.scaled-base.no-style.json) conserva medidas pero devuelve ID de estilo vacío. El mapping identifica los 103 rangos como `NO_WRITE_PENDING_SCALE_BINDING_RESOLUTION`: sus métricas conocidas no acreditan un vínculo directo válido. El piloto de Button no resuelve este bloqueo. No se inventan estilos adicionales ni se alteran escalas para ocultarlo.

## Web y criterios de aceptación

El generador web consume `textDecoration`, emite `--ds-type-ID-decoration` y la propiedad CSS `text-decoration-line` en cada clase compartida. Los consumidores subrayados usan su ID de formato; el marcador `--ds-type-style-id` debe coincidir con las métricas y la decoración calculadas. `NONE` es el valor por defecto al leer catálogos históricos que no incluyen el campo. Los cuatro complementos preservan la presentación existente y no añaden acciones, enlaces o estados de producto.

- Comprobar 79 IDs únicos y cuatro derivaciones de formato válidas; conservar las 75 recetas y tres escalas anteriores.
- Verificar exactamente 27 cambios de ID lógico, con los mismos límites, contenido y métricas; cero rangos UI sin correspondencia.
- Comparar todos los consumidores Figma después de la última escritura y en lectura independiente: estilos reales, decoración, bindings, contenido, geometría, IDs, API pública y rangos ocultos/anidados.
- Comprobar en web la generación determinista y los 79 estilos por cuatro temas, incluyendo decoración y consumidores afectados; typecheck y build conservan su alcance técnico.
- Mantener estados de catálogo, aplicación Figma, web, documentación, skills y auditoría separados. La enmienda está documentada; los `PASS` finales requieren sus reportes de ejecución.

P-SLOTS: `NOT_APPLICABLE` para el catálogo y esta sustitución de formato; no modifica anatomía ni cardinalidad de los componentes.
