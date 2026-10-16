> **Corte histórico.** Count y los 103 rangos escalados quedaron resueltos al reanudar; las copias temporales se retiraron. Consultar el [cierre vigente 0.1.2](typography.v0.1.2.review.md). El texto inferior conserva el estado del bloqueo anterior.

# Tipografía 0.1.1 · consumo de componentes

Fecha: 2026-10-15. Estado de este cierre: **PARTIAL / BLOCKED_BY_USAGE_LIMIT**. Auditoría humana: `PENDING`. Este reporte conserva separados el catálogo, la asignación a consumidores y la distribución. No reemplaza el [QA histórico 0.1.0](typography.v0.1.0.review.md).

## Alcance solicitado y fuentes

Aplicar estilos compartidos a todos los componentes de AI-Design-System y precisar su uso por rol/variante en las Specs. La [enmienda transversal](../../specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) enlaza las 43 enmiendas de familia y sus fuentes congeladas. El [catálogo 0.1.1](../../specs/tokens/ai-design-system.typography.v0.1.1.json) contiene 79 estilos: 18 base y 61 complementarios sustentados por usos existentes; cuatro complementarios incorporan el subrayado a la propia definición del estilo.

El inventario original de tokens permanece intacto. No se publicaron cambios de biblioteca remota. Las instrucciones de uso y los valores canónicos tienen propietarios separados: reglas en Markdown y receta/description en el catálogo JSON.

## Evidencia completada

- Documentación: 43 familias, 39 con consumo y cuatro exclusiones justificadas por ausencia de texto UI. Las tablas cubren 3351 nodos y 3353 rangos de UI; explicitan los 103 rangos escalados pendientes de la comprobación de herencia.
- Catálogo Figma: [lectura independiente](../../implementations/figma/typography.v0.1.1.styles.readback.json) y [QA](../../implementations/figma/typography.v0.1.1.styles.qa.json), 79 estilos y sus bindings/resoluciones.
- Muestras Figma: [lectura](typography/consumption-v0.1.1/specimens.readback.json) y [revisión visual de las cuatro tarjetas nuevas](typography/consumption-v0.1.1/specimens.visual-review.md). El resultado contiene 79 tarjetas.
- Etiquetas contextuales: [revisión de 66 rangos](typography/consumption-v0.1.1/contextual-recovery.review.md), con 22 asignaciones directas y 44 heredadas. Los FAIL históricos del guard literal se conservan. Corregir tracking de 0.1% a 0 puede cambiar la tinta sin cambiar la caja de texto ni el layout; ambas comprobaciones se reportan por separado.
- Table: el readback posterior a la escritura confirma IDs asignados en sus 1446 rangos UI. La [comparación externa](typography/consumption-v0.1.1/global-after-table.comparison.json) conserva iguales las otras 35 páginas en el corte anterior/posterior a esa operación. El timeout impidió recuperar el resultado del guard completo dentro de Table: esta evidencia no acredita ese guard perdido ni permite reconstruir retrospectivamente una comparación de propiedades no conservada.
- Web: [QA de 79 estilos](typography/web/revision-79/README.md), generación determinista, TypeScript/build y mediciones de consumidores en cuatro temas. Su PASS tiene el alcance medido y no valida por sí mismo Figma.

## Resultado independiente del censo y punto de continuación

El censo completó las 34 páginas, 3501 nodos y 3503 rangos. Se conservaron los 3501 hashes de contenido/propiedades capturadas y no se encontraron discrepancias métricas. El primer corte detectó 72 vínculos antiguos en Chat; se corrigieron con [guard de página completa PASS](typography/consumption-v0.1.1/chat72.apply.json), sin diferencias de geometría, receta, contenido ni API en sus 1119 nodos. La [selección final](typography/consumption-v0.1.1/consumer-final.selection.json) conserva 33 páginas de ese corte y sustituye únicamente Chat por su lectura posterior, sin sobrescribir capturas históricas.

El [QA por alcance](typography/consumption-v0.1.1/consumer-final.v0.1.1.scopes.json) acredita **3250 rangos UI aplicables en 3248 nodos: PASS**, y 150 textos editoriales preservados. Los 103 rangos escalados conservan métricas pero siguen **BLOCKED** bajo el contrato de vínculo directo; no se reinterpretó su ID vacío como un ID real.

Las pruebas causales de Checkbox a 5/6 y 2/3 completaron A→B→A con controles y restauración exacta; sus copias fueron retiradas. La prueba Count a 4/3 quedó preparada en copias, pero su lectura A no pudo completarse: la revisión automática de la herramienta informó límite de uso y **no ejecutó la llamada**. No fue un rechazo por inseguridad. Se preservó la respuesta exacta en el [punto de continuación](../../registry/SESSION-HANDOFF-2026-10-15-TYPOGRAPHY-CONSUMERS.md).

Permanecen dos raíces temporales Count en Headers: `1063:1392` y `1063:1414`. Ningún cambio B del piloto se ejecutó; no se alteraron originales mediante esa prueba. Retirar esas copias por sus IDs verificados forma parte del cierre pendiente.

El catálogo 0.1.2 iniciado antes del bloqueo se conserva como [candidato DRAFT](../../drafts/observations/typography-native-inheritance/ai-design-system.typography.v0.1.2.candidate.json), fuera del catálogo activo, con la aclaración de herencia aún sin activar. El catálogo activo permanece 0.1.1; las skills publicadas permanecen 0.2.0. Graphify está **STALE** respecto de este lote y no se declara CURRENT.

## Cierre pendiente

1. Completar la prueba Count, registrar restauración y retirar las dos copias temporales.
2. Cerrar el verificador de las 103 cadenas y documentar las seis fronteras de contenido local SLOT observadas en Select. Activar una enmienda de herencia solo con toda la evidencia requerida.
3. Sincronizar las tres descripciones de recetas derivadas y su documentación Figma si se adopta la enmienda; emitir QA final por control.
4. Actualizar, verificar e instalar los paquetes de skills y cerrar Graphify con el corpus final. El candidato offline provisional pasó sus pruebas, pero ya difiere del corpus y no es el release final.

El estado definitivo se actualizará aquí con evidencia del resultado; los reportes crudos y versiones históricas permanecerán intactos.
