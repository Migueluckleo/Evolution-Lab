# QA · Radio Buttons y Checkboxes · refinamiento 0.1.2

2026-10-06 · IMPLEMENTATION_REVIEW · **PASS técnico del alcance** · auditoría humana PENDING · publicación de biblioteca no ejecutada.

## Referencias

[Radio](../../specs/radio-button.contract.v0.1.0.md), [Checkbox](../../specs/checkbox.contract.v0.1.0.md), [enmienda 0.1.2](../../specs/components/radio-checkbox.refinement.amendment.v0.1.2.md), [QA documental](../contracts/radio-checkbox.refinement.v0.1.2.review.md). Las enmiendas cromáticas0.1.1 siguen vigentes. [Resultado calculado](radio-checkbox.refinement.v0.1.0.verification.json) y [tokens leídos](radio-checkbox.refinement.v0.1.0.tokens.json).

## Cobertura y resultados

| Control | Resultado y evidencia |
|---|---|
| REF-01 Anatomía/API | PASS. Radio: ocho variantes públicas y ocho helper, correspondencia 1:1. Checkbox: doce variantes y ocho instancias Phosphor con keys originales. IDs preservados.24×24, indicador18×18, centro Radio8×8, iconos12×12, radio Checkbox4. |
| REF-02 Tipografía | PASS contra la normalización delegada, no identidad con fuente.40 etiquetas ocultas,200 bindings tipográficos. Manrope Regular14,20px de interlineado y0px tracking. Fuente18px/0%; cambio18→20 y desplazamiento y3→2 explícitos. TEXT/BOOLEAN conectadas. |
| REF-03 Posición Checkbox | PASS. Ocho iconos corregidos de y6 a6.413887023925781, x6 intacta. Snapshot posterior independiente; comparación normalizada confirma que son los únicos ocho cambios. Vectores, tamaños, paints, effects, propiedades y demás geometría idénticos al snapshot anterior. |
| REF-04 Normalizaciones | PASS. Discos Radio18/8 equivalen geométricamente al contorno5; el helper local evita overrides. Checkbox elimina grupos redundantes y helper singular, conservando iconos como instancias. No se afirma identidad de jerarquías. |
| REF-05 Tokens y colores | PASS.22 definiciones canónicas y88 comparaciones por modo: nombre/tipo,description,scopes,codeSyntax, alias y valor primitivo coinciden.92 paints sólidos consumidores incluyendo el helper Radio cumplen binding local/scope. No se cambió ningún token/color ni el JSON histórico. Efectos conservados, con halo interior aproximado previamente documentado. |
| REF-06 Instancias | PASS.80 casos:20 variantes × cuatro combinaciones de etiquetas; textos largos, altura24, orden y no solapamiento.20 cambios de estado conservan texto.32 casos Radio y48 Checkbox. Instancias temporales retiradas, cleanup true; principales intactos. |
| P-SLOTS0.1.0 | NOT_APPLICABLE justificado en contrato: control individual de anatomía fija; la cardinalidad de grupos pertenece al anfitrión. |
| Visual | PASS. Capturas inline de20 instancias con etiquetas visibles revisadas a escala1: sin recorte ni superposición. Checkbox posterior a corrección. Comparación fuente Checkbox y evidencia estructural fuente Radio. No se afirma galería visual en cuatro temas; la cobertura de modos es de aliases/valores. |

## Evidencia reproducible

Snapshots `radio-checkbox.refinement.v0.1.0.radio-source.json` (53nodos), `radio-destination.json` (66 incluyendo helper), `checkbox-source.json` (86), `checkbox-destination.json` y `checkbox-after.json` (77). En cada archivo, `nodes` referencia `groups` por índice para conservar todas las capas sin duplicar información. El snapshot fuente Checkbox omite bindings remotos para acotar salida; no se usa para afirmar auditoría de sus tokens. Los del destino sí los incluyen.

Pruebas: [Radio](radio-checkbox.refinement.v0.1.0.radioTests.json), [Checkbox](radio-checkbox.refinement.v0.1.0.checkboxTests.json). Escritura e IDs: [registro](../../implementations/figma/radio-checkbox.refinement.v0.1.2.write.json). Manifiesto de bytes: `radio-checkbox.refinement.v0.1.2.manifest.json` en este directorio.

El cálculo local compara metadatos y cuatro aliases de cada rol con `tokens.inventory.json`, las extensiones radio-indicator-colors/focus-effects0.1.0 y control-colors0.1.0 con override0.1.1. No crea otra definición canónica. Para no regresión, normalizar únicamente y de los ocho INSTANCE12×12 de checkbox-after a6 produce exactamente el JSON checkbox-destination. No se editaron scripts ni se regeneró Graphify; su estado derivado permanece STALE.

## Límites conservados

Interlineado18→20, halo interior#F8FAFC→blanco y normalizaciones de anatomía permanecen visibles en la auditoría por excepciones; no son nuevos defectos ni aprobación humana simulada. Contornos neutral/400 sobre blanco2.56:1* permanecen sin recolorear. No se certifica accesibilidad web, comportamiento de grupo ni publicación de biblioteca. No se tocaron consumidores externos a estas familias ni se atribuye este QA a todos sus anfitriones.

## Cierre documental

Ambas bases y enmiendas cromáticas promovidas a specs, con punteros en rutas anteriores. Los hashes/QA antiguos siguen históricos; la revisión actual referencia la enmienda0.1.2. No queda una operación técnica abierta de este punto2.
