# QA · Filter Chip 0.2.1

Fecha: 2026-10-05. Resultado: PASS para la enmienda semántica y preservación cromática. Contrato: [Filter Chip 0.2.1](../../specs/components/filter-chip.semantic.amendment.v0.2.1.md). Auditoría humana PENDING; no publicación de biblioteca.

| Control | Resultado | Evidencia |
|---|---|---|
| AC-FC-SEM-001 | PASS | 12 etiquetas → color/text/inverse; 24 vectores opcionales → color/icon/inverse. Readback independiente de los 36 bindings. |
| AC-FC-SEM-002 | PASS | 126 paints efectivos con variables locales y scopes correctos. 60 paints desactivados de envolturas Phosphor excluidos explícitamente; sus vectores sí incluidos. |
| AC-FC-SEM-003 | PASS | 47 definiciones canónicas consumidas o dependencias verificadas por nombre, tipo, description, scope, codeSyntax, modos y aliases. Conversión numérica exacta a float32 del almacenamiento Figma, sin tolerancia ad hoc. Extensión VariableID:705:122 coincide con JSON y sus cuatro aliases a VariableID:8:93. |
| AC-FC-SEM-004 | PASS | 181 nodos/30 variantes, geometría, texto/fuentes, pinturas y reacciones mantienen sus fingerprints. Los únicos cambios de API son el texto descriptivo anunciado; defaults, ocho propiedades y los 1512 valores preferidos por swap se conservan. Overrides de instancias idénticos. Captura posterior revisada: sin recorte, solapamiento o cambio de distribución. |
| AC-FC-SEM-005 | PASS | 18 variantes comparables, 75 paints fuente/destino iguales en RGB y opacidad. Otras 12 son derivadas aprobadas en 0.2.0; no se presentan como observaciones fuente. Mantienen sus recetas previas, con 92%/85% y Disabled idéntico entre selecciones. |
| P-SLOTS | NOT_APPLICABLE | Etiqueta y dos posiciones fijas opcionales, ya cubiertas por propiedades; no cardinalidad variable ni Slot nativo declarado. |

## Evidencia reproducible

La captura posterior tiene SHA-256 `0a37beae3477782d77020eea80d1c0da0fa23a760c8713bcd52bc75247baada8`: coincide byte a byte con la captura aprobada de 0.2.0. El contrato base conserva SHA-256 `325a408cfa6a5880c2136aee89a448e9ab3a6d928199543d946d6ae3a52a6cb8` y su modelo `40e9e3464b86560255c185bf893518dea2a445170678fa797c8ff6925218e48c`. Enmienda 0.2.1: `0c6dba55ac393a09f17176c6a23e5aeb4835e93490c057d883746a258ad2865f`; extensión JSON: `7f982ccc0952adbc3eef0ec9e96da0f5531fe9ce643a69156492fab0a8372a7f`.

[Preflight](filter-chip.semantic.v0.2.1.preflight.json), [variables previas](filter-chip.semantic.v0.2.1.variables-before.json), [escritura](../../implementations/figma/filter-chip.semantic.v0.2.1.write.json), [readback](filter-chip.semantic.v0.2.1.readback.json), [comparación fuente](filter-chip.semantic.v0.2.1.source-comparison.json), [captura 780×508](filter-chip.semantic.v0.2.1.png) y [estado](../../implementations/figma/filter-chip.semantic.v0.2.1.state.json).

La primera comprobación independiente no pudo resolver un ID de vector anidado mediante getNodeByIdAsync. No hubo escritura en esa llamada; se corrigió el método de lectura al recorrido del set con hijos invisibles habilitados. La lectura exhaustiva posterior pasó sin errores. No se ocultó ni se transformó ese fallo en evidencia positiva.

## Límites

[Mediciones de contraste](filter-chip.semantic.v0.2.1.contrast.json): Hover no seleccionado Administrativo conserva texto4.442:1* e icono opcional2.790:1*. Añadido a la auditoría por excepciones bajo la decisión de preservar paleta; no se recolorea ni se declara WCAG PASS.

Sin cambios cromáticos, tipográficos, de anatomía o comportamiento. La captura muestra el default sin iconos; sus bindings ocultos sí se verificaron estructuralmente. Los estados Disabled conservan menor contraste; este QA no certifica WCAG, comportamiento de teclado ni producto. Las normalizaciones geométricas/tipográficas de 0.2.0 permanecen aprobadas, no se reescribe su evidencia.
