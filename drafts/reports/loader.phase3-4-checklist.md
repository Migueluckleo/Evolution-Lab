# Loader · Phase 3 y 4 Checklist

## Phase 3 · Construcción

- P3.a Preparar prototipo Sm/Primary con anillo hueco, gradiente angular y remate. PASS: captura de 24×24 px comparable a la fuente.
- P3.b Comprobar binding real del stop opaco y del remate a color/icon/brand. PASS: ambos persisten en readback Figma.
- P3.c Construir 16 secuencias Size×Color de 24 fotogramas. PASS: 384 fotogramas.
- P3.d Enlazar cada secuencia en ciclo con AFTER_TIMEOUT, CHANGE_TO y SMART_ANIMATE lineal. PASS: 384 reacciones.
- P3.e Construir set público Loader con Size×Color y dependencia local. PASS: 16 variantes e instancias locales.
- P3.f Alinear la cuadrícula con la fuente y ocultar los sets de apoyo. PASS: 331×512 px y posiciones idénticas a las 16 variantes fuente.

Phase 3 Summary: construcción terminada en la página Loaders; no se crearon tokens ni se publicaron componentes.

## Phase 4 · QA y documentación

- P4.a Revisar tamaños, nombres, instancias y transiciones. PASS: 16 variantes y 384 fotogramas/enlaces sin errores.
- P4.b Revisar bindings de gradiente y remate. PASS: 384/384 stops y 384/384 remates.
- P4.c Revisar cuatro modos de las variables y scopes. PASS: roles existentes SHAPE_FILL y aliases a primitivas aprobadas.
- P4.d Comparar captura fuente/destino. PASS: cuadrícula, silueta, diámetros y paleta Contable conservados; técnica vectorial equivalente documentada.
- P4.e Registrar contrato, decisión delegada, IDs y QA. PASS documental; auditoría humana PENDING y biblioteca UNPUBLISHED.

Phase 4 Summary: QA técnico VALIDATED, publicación documental en specs, sin aprobación humana simulada ni publicación de biblioteca Figma. Continúa pendiente probar ejecución continua del prototipo y definir accesibilidad/reduced motion para una eventual implementación web.
