# Fuentes · QA de implementación 0.1.0 · 2026-10-09

**PASS técnico del contrato visual**, no certificación de accesibilidad. [Contrato](../../specs/components/fuentes.contract.v0.1.0.md), [estado](../../implementations/figma/fuentes.v0.1.0.state.json), [readback final](fuentes.v0.1.0.final.json), [verificador reproducible](fuentes.v0.1.0.verify.cjs).

- Página Fuentes847:7 única; set848:41 con dos variantes Default/Hover y Path Item848:8. Validación estructural adaptada de validateCreation con getNodeByIdAsync:5/5.
- Ambas muestras167.6667×90; min150/max168, padding8/gap8/radio8/trazo1INSIDE. Info y Path crecen con contenido; sin scroll interno ni reacciones inventadas.
- 22 pinturas auditadas, cero bindings fuera de colección semántica local o scope;16 nodos de texto leídos. Textos propios ligados a familia/peso/interlineado/tracking;8px de ruta/contador es excepción observada, no un token ficticio.
- 19 roles existentes preflight en cuatro modos, más el nuevo rol Hover de [extensión](../../sources/inventories/ai-design-system.fuentes-hover.v0.1.0.json). Nombre, description, scopes, aliases e identidades primitivas iguales al JSON. Primitivas nuevas0; inventario base sin cambios.
- Dot155:134 reutilizado, comparación de fills/strokes/geometría contra lectura previa PASS; contador editable por propiedad anidada. No escrituras al archivo fuente ni al principal Dot.
- Path nativo SLOT:0/1/2/4 elementos, reorder/replacement/StateSwap conservan contenido sin detach. [Prueba operativa](fuentes.v0.1.0.slots.json) es anterior a la corrección de ancho HUG; sus alturas son históricas. El readback final la sustituye para geometría.
- Corrección de QA: Label dejó ancho fijo72 y ahora HUG/max116/alto automático; Path Item max132. Separador12. Dos segmentos caben en una línea; cuatro ocupan dos; texto largo a150px produce tarjeta202px sin desborde. El Slot vacío conserva16px de alto; no se promete colapso. Separadores se mantienen manualmente después de reordenar.
- Capturas de review848:42 y QA849:44 inspeccionadas: Default/Hover, cuatro marcas, cardinalidades y textos largos. No se importaron assets remotos ni se conservaron enlaces efímeros como evidencia canónica.

## Limitaciones* conservadas

[Mediciones de contraste](fuentes.v0.1.0.contrast.json) usando paints resueltos por tema y primitivas canónicas, no paleta hipotética:
- Texto brand Servicios:3.24:1 Default y3.05:1 Hover (<4.5).
- Ruta tertiary sobre Hover: Contable4.29, Servicios4.48, Personas4.26 (<4.5).
- Borde accent:1.24–1.71 según marca/estado (<3). Es una medición de borde, no por sí sola un dictamen completo de conformidad de una interfaz.
- Ruta y contador8px requieren revisión de legibilidad en producto. No se recolorea por contraste, conforme al criterio del usuario.

No bloquean la reproducción visual delegada. Navegación, URL, teclado, foco, acción de apertura y política de vacío no están especificados por la fuente; no se implementan ni se inventan como nuevas tareas de migración. Auditoría humana PENDING por excepciones; biblioteca no publicada. Las pruebas de Slots son edición de instancias en Figma, no tests de una aplicación web.

