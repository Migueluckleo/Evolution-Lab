# DEC-TYPOGRAPHY-STYLES-001 · 2026-10-15

**Actor:** usuario. **Procedencia:** `EXPLICIT`, solicitud actual y elección posterior de alcance. **Auditoría humana del detalle:** `PENDING`.

El usuario solicita construir los estilos tipográficos de su referencia en `AI-Design-System`, documentar su especificación y uso, integrarlos en Figma y comprobar que los componentes consuman estilos. Después elige conservar **los 18 estilos base más los complementarios necesarios documentados**. Esta redacción registra el alcance comunicado; no pretende ser una cita literal de la conversación ni una aprobación ficticia de un catálogo todavía no auditado.

La solicitud autoriza la documentación e implementación local y en el archivo Figma `tj3WIBEZDGLVs7MJWKCwgf` para esta tarea. El [contrato tipográfico 0.1.0](../specs/foundations/typography.contract.v0.1.0.md) se tramita como `DELEGATED_FOR_BUILD` por esta **delegación específica**, con `user_audit: PENDING`. No se extiende la excepción histórica de migración a cualquier trabajo futuro. La preparación requiere el catálogo canónico completo, el censo de consumidores, QA documental y preflight; la decisión no acredita que esos controles ya hayan ocurrido.

## Alcance adoptado

- Incorporar la escala base de la [referencia preservada](../sources/references/typography/user-style-list.2026-10-15.png) como estilos de texto editables y documentados. El [catálogo canónico](../specs/tokens/ai-design-system.typography.v0.1.0.json) es el único propietario editable de sus nombres, propiedades, unidades y `description` de uso.
- Incorporar complementarios solo cuando una receta existente y su consumidor real los justifiquen. Conservar los casos compactos y las excepciones contractuales si imponer un estilo base alteraría la geometría o el contrato sin necesidad. La elección no exige que todos los textos usen uno de los 18 estilos base.
- Sustituir la dependencia de valores tipográficos aislados por referencias explícitas a estilos en los consumidores comprendidos por el censo. Mantener la distinción entre estilo asignado, propiedades resueltas y overrides: la mera presencia de un ID de estilo no prueba conformidad.
- Reutilizar familia, pesos, tamaños y bindings semánticos existentes cuando correspondan exactamente. Los porcentajes de la referencia gobiernan las composiciones nuevas; no se presentan como equivalentes de variables históricas con otra magnitud o unidad.
- Preservar el inventario histórico `sources/inventories/tokens.inventory.json`, los originales, IDs reutilizables, componentes, instancias, contenido, colores, propiedades, variantes, Slots y comportamientos. Cualquier ajuste geométrico necesario se registra y comprueba por consumidor; no se autoriza una normalización indiscriminada de alturas.
- Documentar y verificar los destinos afectados según P05/P06/P07/P08, manteniendo separado el QA Figma del QA web y de la integridad de las skills.

## Sustitución y límites

Esta decisión introduce el uso transversal de estilos para las propiedades tipográficas dentro del alcance censado. No borra las recetas históricas: una receta conservada se representa mediante un complementario documentado. Una sustitución por estilo base debe identificar su consumidor, requisito anterior, diferencia adoptada y evidencia posterior. La selección no se hace solo por tamaño ni por nombre parecido.

Los porcentajes explícitos de la nueva referencia se sustentan en esta solicitud, no en `DEC-SEMANTIC-EXTENSIONS-001`, cuya autorización histórica se limita a aliases de primitivas existentes. La tarea no autoriza retargetear silenciosamente variables compartidas, modificar el inventario recibido, inventar equivalencias numéricas ni crear primitivas nuevas por conveniencia. Un estilo compuesto puede gobernar un porcentaje exacto sin fingir que existe un token equivalente; se conserva y comprueba la unidad real según el contrato.

La autorización no incluye publicación remota de la biblioteca, alteración del archivo Figma fuente ni aprobación humana retroactiva de otros contratos. Los textos convertidos a geometría dentro de logos o ilustraciones no se reconstruyen como texto por esta instrucción; su exclusión se identifica en el censo. La publicación y el QA final requieren hechos registrados, no se deducen de esta decisión.

## Complementarios derivados por limitación de herencia escalada

La elección explícita de complementarios necesarios permite incorporar tres derivados de compatibilidad para las recetas escaladas ya observadas en Checkbox y Count. Es una resolución técnica `DERIVED` dentro del alcance delegado, no una aprobación humana nueva ni una solicitud de ampliar la escala general. Su finalidad es conservar medidas y geometría y, a la vez, cumplir la asignación verificable de un estilo real en los 103 rangos afectados.

La [evidencia previa de Count](../qa/implementations/typography/scaled-counter.pre-inheritance.json) registra su escala, propiedades, métricas materializadas y `textStyleId` vacío. Ese archivo no acredita la prueba posterior ni el resultado final. Cuando heredar el estilo del principal deja el rango sin estilo y asignar la receta del principal cambia sus medidas, la solución admitida es catalogar la receta resultante exacta, con `derivedFrom`, referencia al principal y codificación float32 documentada. No se aceptan valores próximos ni una multiplicación doble de la escala.

La revisión documental y el readback de los 75 estilos incluyen las tres nuevas entradas y sus fuentes; la migración de consumidores sigue `BLOCKED`. La matriz separa `instanceScale` de `recipeScale`: el componente conserva su escala y el derivado se compara sin volver a escalarlo. No se crean tokens primitivos fraccionarios ni se alteran los 18 estilos base. Los tres derivados quedan limitados a estos consumidores y sus instancias, con auditoría humana `PENDING`.

## Preservación con bindings canónicos añadidos

La actualización de la foundation reutiliza IDs de estilos originales y añade sus bindings canónicos. La [verificación independiente de preservación](../implementations/figma/typography.v0.1.0.preservation.qa.json) admite exclusivamente adiciones idénticas al catálogo y al readback del estilo, con nombre, ID, scope, cadena de aliases y valores de los cuatro modos comprobados. Se identifican 244 rangos de 242 nodos y 17 estilos reutilizados, con 1202 referencias añadidas; no se admite pérdida, reemplazo ni referencia ajena. Las métricas, contenido, propiedades capturadas, cajas e IDs originales se conservan en las 34 páginas censadas.

Este resultado `PASS` acotado no equivale a una restauración literalmente idéntica: el [control estricto](../implementations/figma/typography.v0.1.0.restoration.qa.json) conserva su `FAIL` histórico por las 244 diferencias aditivas. Tampoco acredita migración global de consumidores. La adición de bindings forma parte de la implementación delegada de estilos; no se registra como una nueva aprobación humana.

## Evidencia y estado

El [QA documental](../qa/contracts/typography.v0.1.0.md) conserva las comprobaciones y pendientes. La referencia preservada tiene SHA-256 de bytes `52053d2a71f5db76f1a28c436a647597b46da486b543d88eff85b920e010e00e`; sus 18 entradas base están transcritas en el catálogo. El [descubrimiento inicial](../sources/figma-snapshots/typography.discovery.2026-10-15.json) registra páginas, estilos y fuentes; el censo detallado cubre 34 páginas. El [readback base](../implementations/figma/typography.base.v0.1.0.state.json) permanece como evidencia del primer subconjunto.

El [QA de implementación por destino](../qa/implementations/typography.v0.1.0.review.md) registra el cierre parcial verificable:

- Catálogo de 75 estilos —18 base y 57 complementarios, incluidos tres derivados—: QA documental `PASS` y [QA independiente Figma](../implementations/figma/typography.v0.1.0.styles.qa.json) `PASS`, con 304 bindings y 1216 resoluciones por modo.
- Documentación Figma en página Typography `1003:412`: [readback](../qa/implementations/typography/specimens.readback.json) `PASS`, con 75 tarjetas, 316 textos y 79 frames.
- Preservación del censo: `PASS` con las adiciones identificadas arriba; restauración literal `FAIL` histórico conservado.
- [Implementación web](../qa/implementations/typography/web/revision-75/README.md): `PASS` acotado a 75 estilos por cuatro temas y 2956 mediciones de texto en 43 familias por cuatro temas, además de generador, TypeScript y build.
- [Consumidores Figma](../qa/implementations/typography/Figma-blocker.md): `BLOCKED` por propagación observada de estilos entre textos con referencias a propiedades de componente; la causa interna permanece `UNRESOLVED`. Se preservan los IDs originales. Una intervención estructural necesita una propuesta concreta comprobada antes de aplicarse; no se declara `VALIDATED` por disponer del catálogo o del mapa.

La auditoría humana sigue `PENDING`. El cierre de paquetes y su evidencia se consulta en [registry/skills.md](skills.md), conforme a P08; estos resultados no anticipan su estado ni el cierre de Graphify.
