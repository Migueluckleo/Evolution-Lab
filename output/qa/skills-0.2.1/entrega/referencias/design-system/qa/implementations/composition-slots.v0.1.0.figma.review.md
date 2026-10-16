# QA de implementación · Slots de composición 0.1.0

2026-09-29 · **PASS técnico acotado** para Select, Switch Tab y Breadcrumbs. Contrato COMPOSITION-SLOTS-0010.1.0 DELEGATED_FOR_BUILD; auditoría humana PENDING. No certifica toda la biblioteca, fidelidad cromática histórica pendiente, accesibilidad web ni publicación Figma.

## Evidencia

- [Select](composition-slots.v0.1.0.select.json): 1/3/5/8/0 opciones; filas40 y alturas40/120/200/320. Slot vacío conserva200 de placeholder. Opciones originales5 sin modificar. Reordenamiento y swap a Selected=True desde consumidor, texto largo truncado. Open→Closed→Open conserva ocho opciones y overrides; Closed oculta el Slot.
- [Switch Tab](composition-slots.v0.1.0.switch-tab.json): 1/2/4/7/0 pestañas; anchos128/248/488/848 con contenido normal. Cuatro hijos originales conservados; siete y etiqueta larga producen ancho natural1241. En320 la fila desborda deliberadamente; no se añadió scroll/wrap. Vacío conserva placeholder480×38 dentro del host488×46.
- Breadcrumbs: [prueba inicial](composition-slots.v0.1.0.breadcrumbs.initial.json), [corrección de sizing](composition-slots.v0.1.0.breadcrumbs.correction.json) y [readback final](composition-slots.v0.1.0.breadcrumbs.final.json). 1/3/5/8/0 segmentos. La primera prueba encontró ancho fijo; la primera captura mostró etiquetas superpuestas. Corregidos Slot y host a HUG y cuatro ítems textuales a HUG con minWidth histórico. Los cuatro principales conservan248/372/496/620×24. La etiqueta larga ocupa551px y la ruta completa1391 en el Slot, sin solapamiento. Tras cambios Level2/3/4/5 los ocho hijos y sus propiedades persisten. Los overrides de ancho del consumidor y la variante pueden conservar caja restringida y overflow; no se promete preservar un ancho explícito al cambiar Level.
- [Cambio de ítems Breadcrumb](../../implementations/figma/composition-slots.v0.1.0.breadcrumb-item-fix.json): IDs190:189/202/206/208, minWidth120/120/92/92, default sin desviación geométrica; ninguna modificación de pintura. Impacta el crecimiento de etiquetas largas en sus consumidores; no se declara auditado todo consumidor externo.
- [Guías Figma](../../implementations/figma/composition-slots.v0.1.0.guides.json) y [estado consolidado](../../implementations/figma/composition-slots.v0.1.0.state.json).

## P-SLOTS

| Control | Resultado | Alcance comprobado |
|---|---|---|
| SLOT-QA-01 | PASS | Enmienda identifica propietarios, contenido, cardinalidad, operaciones y límites. |
| SLOT-QA-02 | PASS | Readback real type=SLOT y propiedad SLOT: Options#466:0, Tabs#468:0, Trail#470:0. La conversión conserva los IDs originales de frames. |
| SLOT-QA-03 | PASS | Adición, eliminación, reordenamiento, sustitución y edición desde consumidores INSTANCE, sin detach. Los principales no se editaron para cambiar el conteo de las pruebas. |
| SLOT-QA-04 | PASS | Casos menores/muestra/mayores y un elemento según evidencias enlazadas. No son límites de producto. |
| SLOT-QA-05 | PASS estructural | Cero hijos permitido técnicamente, sin min/max; conserva espacio de edición. La presentación vacía de producto continúa UNRESOLVED; no se inventó mensaje ni interacción. |
| SLOT-QA-06 | PASS con límites explícitos | Select320 y texto largo truncado; filas crecen. Switch Tab/Breadcrumbs horizontales hug, sin solapamiento tras corrección, overflow a ancho reducido; scroll/wrap no definidos. Capturas inline inspeccionadas. |
| SLOT-QA-07 | PASS acotado | Select81, Switch Tab44 y Breadcrumbs16 pinturas ligadas por modo en las instancias probadas, cuatro modos cada una; cero errores de scope, resolución o procedencia local en el control. No se alteraron aliases. |
| SLOT-QA-08 | PASS / NOT_APPLICABLE | SelectClosed/Open y BreadcrumbsLevel2–5 preservan contenido/overrides. Switch Tab es componente único, sin variante de anfitrión. Selección de hijos es manual, no calculada. |
| SLOT-QA-09 | PASS acotado | IDs principales y originales conservados; default geometry sin cambio. No se tocó Figma fuente. Corrección de dependencia Breadcrumb explícita en contrato; demás principales no fueron editados. No se afirma QA de todos los consumidores ajenos. |

## Comprobaciones complementarias y límites

El validador existente validate-select-composition.cjs pasó112 comprobaciones canónicas y4 de extensión,29 variables; sirve para su mapa de tokens histórico, no como prueba de Slots. SHA256 del JSON canónico sigue cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474. Variables creadas/modificadas:0. Las sombras literales del menú y métricas numéricas de etiquetas Checkbox ocultas siguen siendo excepciones de Select; no se borraron ni se declaró tokenización integral.

Capturas inspeccionadas: Select467:1052 (ocho filas), Switch Tab469:282 (muestra), Breadcrumbs470:241 antes y después de corrección. La segunda captura de Breadcrumbs sustituye visualmente a la fallida; no se oculta el fallo inicial. Un intento de leer documentación trató un TEXT como contenedor: error recuperable, corregido con narrowing de tipo; no produjo una nueva mutación de componentes.

Las pruebas dejaron15 instancias de demostración identificadas con «Slots QA», fuera de los objetos existentes. Solo se eliminaron hijos de esas instancias recién creadas durante las pruebas de cardinalidad, nunca originales del usuario. Se pueden reiniciar desde los principales. Biblioteca permanece sin publicar. Graphify STALE sin regeneración.
