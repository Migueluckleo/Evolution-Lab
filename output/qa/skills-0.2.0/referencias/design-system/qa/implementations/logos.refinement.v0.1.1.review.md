# Logos · refinamiento del paso3 · 2026-10-06

**Resultado: geometría pendiente de decisión explícita; no PASS global.** Principales intactos, auditoría humana PENDING, biblioteca no publicada.

## Alcance y evidencia

Seis sets/72 variantes/2967 nodos, incluidos invisibles. Doce assets OMITTED_BY_USER quedan fuera por [enmienda de alcance](../../specs/components/logos.scope.amendment.v0.1.1.md), que formaliza DEC-LOGOS-REMAINDER-OMITTED-001 sin alterar fidelidad. [Plan](logos.refinement.v0.1.1.plan.md), [resultado](logos.refinement.v0.1.1.verification.json), [geometría por nodo y campo](logos.refinement.v0.1.1.geometry.json).

Se reutilizó el script canónico íntegro de `sources/figma-snapshots/logos.fidelity-baseline.v0.1.0.json`; se añadieron firmas por campo con la misma canonicalización. Comparación fuente y destino actuales, IDs separados, sin modificar la Librería anterior. [Fuente](logos.refinement.v0.1.1.source.json), [destino anterior](logos.refinement.v0.1.1.before.json), [readback final](logos.refinement.v0.1.1.after.json). Las firmas duales son checksums de ingeniería, no prueba criptográfica; los archivos se identifican por SHA-256 en el manifiesto.

## Resultados

- PASS de conservación: nombres, jerarquía/tipos, pinturas, gradientes, efectos, imágenes, trazados/vectorNetwork, constraints, layout y propiedades/defaults. Cero bindings. Cuatro dependencias de categoría locales, remote=false. Los seis digests finales de principales son iguales a los anteriores: cero mutaciones permanentes.
- Personas conserva igualdad estructural completa con fuente:306 nodos,12 variantes, checksum cdde9566-5ca49d0c.
- Persisten57 registros geométricos distintos en los otros cinco sets. Máximo absoluto0.00030517578125px; campos width/height/traslación de relativeTransform. No se amplía tolerancia, no se redondean datos y no se declara igualdad exacta.
- P-SLOTS: NOT_APPLICABLE por artwork fijo. No se crearon tokens ni primitivas.

## Diagnóstico seguro ejecutado

1. Clones temporales en las coordenadas absolutas fuente: [resultado](logos.refinement.v0.1.1.clone-test.json). Categorías llegó a igualdad completa en esa copia; los otros conjuntos con diferencias no. Esto demuestra que el contexto de copia/posición afecta al menos esa lectura, no una causa universal demostrada.
2. Clones de cinco sets en dos marcos temporales con transforms de los ancestros fuente: [resultado](logos.refinement.v0.1.1.nested-coordinate-test.json). Las diferencias restantes persistieron. No se escaló ni reescribió la geometría de principales.
3. Todos los clones y marcos temporales fueron retirados por IDs conocidos; lookup posterior null. Readback de principales confirmó digests y propiedades intactos, además de las cuatro dependencias locales.

No se repitió el intento histórico de escribir el transform del grupo corporativo429:480: ya constaba que desplazaba sus45 hijos. No se usa resize de grupos porque escala el artwork y la propia regla de fidelidad lo prohíbe. No se afirma imposibilidad absoluta de otra herramienta; las alternativas seguras verificadas no acreditan corrección exacta.

## Fuente actual frente al baseline

Tres ajustes de exportación SVG fuente difieren del corte2026-09-28: administrativos/16 (vende horizontal), contables/19 (anticipa horizontal), servicios/4 (VDI horizontal). Los exportSettings del destino coinciden exactamente con la firma de la fuente histórica y con su readback anterior. No son regresiones del destino, no afectan artwork y no se propagaron ni se añadieron como tarea nueva. [Detalles fuente](logos.refinement.v0.1.1.source-details.json), [destino](logos.refinement.v0.1.1.target-details.json).

## Única decisión necesaria para cerrar este punto

Propuesta, NO aprobada: aceptar únicamente las57 diferencias geométricas enumeradas, de hasta0.00030517578125px, conservando copia nativa, IDs, arte y dependencias. No sería una tolerancia general para el DS ni autorizaría discrepancias futuras. Con aceptación explícita se documentaría VALIDATED_WITH_EXCEPTIONS y se promovería el contrato; por ahora no se hace ninguna de esas dos cosas.

No hay nuevas capturas de composición: no cambió artwork. Las capturas históricas registradas conservan su alcance visual; este turno aporta cotejo numérico y pruebas temporales, no una nueva certificación pixel-perfect.
