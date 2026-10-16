# QA implementación · SELECT-001 v0.1.0

2026-09-29. **PASS técnico acotado** para las dos presentaciones documentadas. No aprobación humana ni certificado de tokenización completa o accesibilidad.

## Evidencia
- Set457:470, página Select444:122; variantes456:402/456:421, guía456:486, prueba de ancho458:470.
- Readback: select.v0.1.0.readback.json; mapa: select.v0.1.0.tokens.json; script reproducible qa/contracts/validate-select-composition.cjs.
- Capturas inspeccionadas: fuente1780:2989; set457:470; página Select tras integración. Nueva guía legible, variantes separadas y overflow del menú correcto. No se modifica la guía anterior.

## Controles
- REQ-SEL-001–003 PASS: dos presentaciones únicas Closed/Open, siete instancias directas de dependencias. Field y cinco opciones expuestos; instancia de prueba muestra seis grupos editables. Edición de Option1 verificada sin modificar principales.
- REQ-SEL-004 PASS: envolturas464×96; menú464×200,y80; cinco filas40, radio8, clipping solo en menú. A320px campo/menú/filas se adaptan manteniendo altura; texto largo trunca.
- REQ-SEL-005 PASS: cero reacciones propias y cero modos explícitos en variantes. No se construye selección funcional.
- REQ-SEL-006 PASS para conservación de las dependencias: 136nodos recorridos incluyendo invisibles;75SOLID inspeccionados,70 pinturas consumidoras correctamente ligadas a roles semánticos locales, scope correcto y RGB coincidente. Cinco pinturas restantes tienen visible=false en wrappers Loader; no consumen color.20textos tienen cinco bindings tipográficos; diez etiquetas de Checkbox escalado y oculto conservan exactamente las métricas/bindings de Dropdown Item446:165, sin ampliar su cobertura histórica.
- REQ-SEL-007 PASS: las dos sombras coinciden con el snapshot, eliminando únicamente referencias remotas. Excepción literal documentada, no tokenización integral ni uso de roles de foco/texto.
- REQ-SEL-008–009 PASS: misma página, principales previos intactos, guía y ejemplo independientes. Validación canónica112comparaciones +4de extensión;29variables en cuatro modos. Sin nuevos tokens, primitivas, estilos o cambios al JSON.

## Avisos y contraste
El primer chequeo genérico produjo35avisos:30por métricas de10etiquetas ocultas escaladas y5por fills desactivados de Loader. El diagnóstico y comparación con la dependencia prueban que no son cambios introducidos por Select; se conservan íntegros en initialBroadAudit del readback. No se borran ni se afirma que los bindings numéricos existan.
Texto primary/blanco≈17.85:1; tertiary/blanco≈4.76:1. Borde neutral400/blanco≈2.56:1*. Filas40px*. No recolorear. Medidas de contraste exactas reproducibles en script.
Pendiente auditoría por excepciones: sombras literales*, helper cubierto por menú, etiquetas ocultas escaladas heredadas. Lógica de producto/ARIA fuera de alcance. Biblioteca UNPUBLISHED; auditoría humana PENDING; Graphify STALE.
