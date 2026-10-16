# Tipografía web 0.1.1 · 79 estilos

**Resultado: PASS en el alcance web comprobado.** Fecha: 2026-10-15. Fuente canónica: [catálogo 0.1.1](../../../../../specs/tokens/ai-design-system.typography.v0.1.1.json), SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. La [enmienda de formato](../../../../../specs/foundations/typography.formatting.amendment.v0.1.1.md) separa esta validación de la aplicación Figma.

Los 18 estilos base y 61 complementarios se generan desde una sola fuente. Las cuatro nuevas identidades `-underline` incluyen la decoración existente; sus métricas y bindings son idénticos a las recetas de origen. Las 75 definiciones métricas históricas se conservan. El generador valida la derivación de formato separada de las tres escalas materializadas.

## Verificaciones

| Control | Resultado y evidencia |
|---|---|
| Generador Python | 11 pruebas PASS, incluidas conversión de unidades, aliases, escala Float32 sin doble multiplicación, derivación UNDERLINE y rechazo de cambios métricos/bindings encubiertos. |
| Determinismo | `python3 scripts/typography.py --check`: cero derivados desactualizados. |
| TypeScript | `node node_modules/typescript/bin/tsc --noEmit`: PASS. |
| Build | `pnpm build`: compilación y exportación estática PASS. |
| 79 clases por cuatro temas | 316 mediciones: familia Manrope real comprobada por Chrome, identidad, peso, tamaño, interlineado, tracking y decoración concordantes. [styles.json](styles.json). |
| Consumidores de 43 familias | 2,956 mediciones por cuatro temas, cero diferencias contra el catálogo. Incluye verificaciones expresas de Button Link, File Upload y Link de Empty states. [consumers.json](consumers.json). |
| Comparación con revisión 75 | Las 2,956 mediciones conservan familia, tamaño, peso, interlineado, tracking, texto y clasificación observados. Cero diferencias métricas; 48 identidades web pasan a los cuatro estilos subrayados a través de temas/variantes. [consumer-preservation.json](consumer-preservation.json). |
| Ejecución de navegador | Dos tests PASS en Chrome. [browser-report.json](browser-report.json). El primer arranque no pudo abrir localhost dentro del sandbox; no ejecutó aserciones. La ejecución local autorizada completó las pruebas. |

El [resumen con hashes de fuentes](implementation-summary.json) registra comandos, cobertura y límites. Los 48 cambios medidos en la galería web son observaciones de sus variantes/temas; no se confunden con los 27 rangos existentes del censo Figma.

## Revisión visual

Se abrieron y revisaron las tres capturas reales del tema Personas: [Button Link](button.underline.png), [File Upload](file-upload.underline.png) y [Empty states](empty-states.underline.png). El subrayado aparece en las acciones esperadas; sus textos resultan legibles y no se observa recorte dentro de esas capturas. Los mensajes de éxito/error conservan sus identidades sin subrayado en las mediciones de variantes.

La comparación automática mide propiedades tipográficas y contenido; no mide todas las posiciones de frames ni demuestra identidad visual universal. La revisión visual cubre esas tres muestras, no todas las composiciones posibles. Este QA no ejecuta Figma ni declara consumo de sus estilos: los 103 rangos escalados mantienen el bloqueo registrado por su ejecución independiente.
