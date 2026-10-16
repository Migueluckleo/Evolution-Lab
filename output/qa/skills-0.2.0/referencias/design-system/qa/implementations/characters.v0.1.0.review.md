# Characters · QA de implementación v0.1.0

2026-10-08 · TECHNICAL QA PASS · implementación VALIDATED · DELEGATED_FOR_BUILD · auditoría humana PENDING · biblioteca UNPUBLISHED.

[Contrato vigente](../../specs/characters.contract.v0.1.0.md), [lecturas detalladas](characters.v0.1.0.audit.json), [estado e IDs](../../implementations/figma/characters.v0.1.0.final.json), [captura](../../implementations/figma/characters.v0.1.0.png).

## Alcance y resultados

- AC-01 PASS: Characters820:7 contiene BENI Standby822:6 (6 frames) y NAVI Analysis822:7 (7); propiedad Frame e inicial01. Muestra822:21 con13 instancias. Conversation/Chat intactos.
- AC-02 PASS:90 nodos de fotogramas,64 vectores y13 grupos; jerarquía, orden, opacidad, constraints, efectos y pinturas comparados. Máxima diferencia de posición/dimensiones0.00006103515625px (<0.001).17 vectores sin fill conservados.
- Paths: comparación textual inicial FAIL en46/64 por normalización API. Round-trip posterior de los64 paths fuente en vectores temporales coincide exactamente con destino; temporales eliminados. Figma reordena subpaths NONE y serializa coordenadas. Captura revisada: cuerpos, ojos, bigote y sombras coinciden visualmente; no igualdad textual del SVG bruto.
- AC-03 PASS:13 AFTER_TIMEOUT/CHANGE_TO, dos ciclos, tiempos/easing/destinos locales. Una espera0.8 se serializa como0.800000011920929 (delta1.1921e-8s, tolerancia1e-6). Sin certificación perceptual de reproducción.
- AC-04 PASS:47/47 pinturas con binding de identidad. Cuatro variables coinciden con JSON en nombre, tipo, description, scope SHAPE_FILL, codeSyntax y valor por modo. Tres intactas; solo sombra NAVI nueva VariableID:820:6. Sin aliases semánticos para esta excepción.
- Cuatro temas:47 pinturas invariantes por modo; muestra restaurada sin modo explícito. Pruebas BENI01/NAVI02 al50% mantienen geometría y bindings, delta0; ambas instancias temporales retiradas.
- AC-05 PASS: muestra sin clipping, captura1309×375 naturales, contrato en specs y registros persistentes. Sin publicar biblioteca.
- Slots NOT_APPLICABLE: anatomía ilustrativa fija; no slots artificiales.

## Contraste y límites

Rasgos/BENI5.381:1; rasgos/NAVI2.028:1; sombra/cuerpo NAVI1.278:1. Identidad original conservada. No son texto ni controles; no WCAG PASS/FAIL general. Reduced motion y backend se definirán solo al implementar un consumidor/frontend, fuera del alcance actual.

## Incidencias resueltas

Índice fuente excedió20480bytes y se releyó por lotes. Código inicial superó50000 caracteres: rechazado antes de ejecutar; luego lotes4/4/5 con guardas de número de nodos. build.js conserva receta completa; requiere dividir SOURCE y ajustar offset/guardas según batch-0/4/8.json, no ejecutarla como una sola llamada. Cambios limitados a página nueva y variable nueva. Retirados solo temporales QA propios.

## Cierre

Sin conflictos bloqueantes. Ajustes futuros en specs. [Continuidad](../../registry/SESSION-HANDOFF-2026-10-08-CHARACTERS.md).
