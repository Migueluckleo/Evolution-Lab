# Chat · revisión de ajustes del usuario · 2026-10-09

## Resultado y límites

Documentación de observaciones completada; QA de configuración/readback acotado. **No VALIDATED global:** no se probó Present con exceso de mensajes, listas largas ni redimensionamiento mediante fixtures. Figma permaneció read-only; no se cambiaron principales, instancias, variables, estilos, descriptions o prototipos. Sin publicación remota ni frontend.

La [enmienda0.1.1](../../specs/components/chat.layout.amendment.v0.1.1.md) separa las reglas observadas de las discrepancias y sustituye únicamente el alcance de layout indicado de las bases. Delegación documental vigente; user_audit PENDING, no aprobación humana inventada.

## Método y evidencia

Lectura de P02/P03/P05/P06/P-SLOTS, P01/P04 como dependencias; skill figma-component-contract/figma-use para inspección sin escrituras, Graphify para localizar fuentes y sincronizar el índice. Contratos base y evidencias/build históricos contrastados sin reescribirlos. Censo de los principales Standby783:24, Active783:116, Expanded797:316 y Collapsed797:458:478 nodos incluyendo ocultos, sin nodos pendientes de recorrido. El censo no equivale a inspeccionar todos los atributos de cada nodo o todos los principales de dependencia.

Lectura de layout84 nodos propios/instancias directas;40 Slots con limitViolations vacías; propiedades de ambos sets leídas. Dos capturas de revisión examinadas (784:99 y798:290) corroboran visualmente la configuración actual, sin probar scrolling. Capturas vistas en MCP, no guardadas como archivos persistentes; los valores verificables quedan en los JSON enlazados. Tres primeros lotes excedieron el límite de salida20480 bytes y no devolvieron evidencia; se acotó el payload y los lotes definitivos completaron la lectura. Esos errores no se cuentan como QA ni implicaron escrituras.

## Comparación

|Chequeo|Resultado|
|---|---|
|Columna Section542→816|Confirmado en ambos principales y muestras; no es un ancho fijo816|
|Mínimo Section|574 en principales,358 en muestras: override, no regla global|
|Active775/HUG→733/FIXED|Confirmado; minHeight eliminado y columna683 FIXED|
|Messages|FILL/FILL; scroll VERTICAL; clipsContent=false; Status/Composer fuera del Slot|
|Toolbar Expanded|FIXED; región central FILL/minHeight=null, sin scroll VERTICAL|
|Slots|REQUIRED,12 propios entre cuatro variantes y28 anidados;40 total; sin violaciones actuales; edición no reejecutada|
|Espaciado|Cinco definiciones locales y20 aliases contrastados contra inventario; resultado en verificador|
|Colores/tipografías|No cambiados por esta revisión; no se ejecutó auditoría completa de todas sus definiciones/modos|
|Reacción Toolbar|CHANGE_TO local conservada, Smart Animate/EASE_OUT ~300ms; no prueba de playback|

## Observaciones concretas, sin cambios automáticos

1. La description del set784:98 todavía menciona542 y altura adaptable: difiere de los atributos actuales y de la enmienda.
2. Las dos muestras tienen minWidth358 y sus principales574. No inferir soporte móvil ni propagar el override automáticamente.
3. Scroll operativo de Messages no verificado: VERTICAL y clipsContent=false, sin captura con desborde real ni ejecución de Present. La alineación MAX observada tampoco equivale a autoscroll.
4. Toolbar Expanded fijo y listas HUG sin scroll configurado: el QA histórico de crecimiento con seis Tool Items no certifica la nueva configuración. No se afirma defecto visible en la muestra actual ni se inventa una corrección.

## Reproducción y fuentes

Ejecutar `node qa/implementations/chat-layout.v0.1.1.verify.cjs` desde la raíz. Es read-only y comprueba coherencia de evidencia, cardinalidades y spacing, no Figma live ni interacción. [Layout](chat-layout.v0.1.1.observed.json), [estructura](chat-layout.v0.1.1.structure.json), [instancias/spacing](chat-layout.v0.1.1.instances-and-spacing.json), [verificador](chat-layout.v0.1.1.verify.cjs).

Baselines: [Section](chat-section.v0.1.0.review.md), [Toolbar](chat-toolbar.v0.1.0.review.md), [estado Section](../../implementations/figma/chat-section.v0.1.0.state.json). Sus PASS siguen históricos; no se recalifican ni se trasladan al nuevo layout.
