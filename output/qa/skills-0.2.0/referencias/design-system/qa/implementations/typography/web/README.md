# QA web de tipografía · 2026-10-15

**PASS · evidencia DERIVED, no aprobación visual ni fuente normativa.** Copia íntegra de `/tmp/typography-web-qa`; los JSON y logs conservan sus rutas originales de ejecución. El [resumen](implementation-summary.json) registra los hashes del corte probado y los archivos afectados.

Fuente canónica: [ai-design-system.typography.v0.1.0.json](../../../../specs/tokens/ai-design-system.typography.v0.1.0.json), SHA-256 `0c5f6cf139ff9d32fd0f9cfaf250846e23e101ed23083733470c308e5f7669b3` (18 base + 54 complementarios). Las mediciones acreditan este corte; un cambio posterior requiere revisar el QA afectado.

## Resultados

| Verificación | Resultado | Evidencia |
|---|---:|---|
| Generación determinista, TypeScript y build estático Next.js | PASS | [verify](typography-verify.log), [determinismo](typography-determinism.log), [typecheck final](typography-typecheck.log) |
| Pruebas Python de unidades y referencias del generador | 8/8 PASS | [log](typography-python-tests.log) |
| Pruebas unitarias de componentes | 9/9 PASS | [verify](typography-verify.log) |
| Suite completa Chrome: contratos, estados, Slots, galería y tipografía | 61/61 PASS | [reporte](browser-suite-61.json), [log](typography-browser-final.log) |
| Auditoría contractual de 43 familias | 20,860 comprobaciones PASS | Un JSON y PNG por familia en este directorio |
| Clases tipográficas en cuatro temas | 288 recetas PASS (72 × 4) | [métricas, FontFace y fuente realmente usada mediante CDP](typography/styles.json) |
| Consumidores: 43 familias en cuatro temas | 2,956 textos PASS | [mediciones completas por familia, variante y tema](typography/consumers.json) |
| Preservación de declaraciones no tipográficas | 717 reglas idénticas | [comparación](geometry-preservation.json) |

La última ejecución específica guardó las mediciones completas por texto: [reporte de 2 pruebas](browser-typography-measurements.json), [log](typography-browser-evidence.log). No reemplaza el reporte separado de la suite completa de 61 pruebas.

Inspección visual manual adicional limitada a [Header](header.png) y [Conversation](conversation.png), sin defectos visibles encontrados. La existencia de las otras capturas no significa que se hayan inspeccionado manualmente. El QA cubre Chrome con Manrope local; no certifica Figma, otros motores, WCAG completo ni toda composición arbitraria aportada a Slots. El marco del catálogo queda fuera de los defaults tipográficos del DS.

## Comandos ejecutados

Desde la raíz del repositorio:

```sh
python3 -m unittest discover -s implementations/web/scripts -p test_typography.py -v
python3 implementations/web/scripts/typography.py --check
```

Desde `implementations/web`, usando Node/pnpm del runtime local disponible:

```sh
export PATH=/Users/miguel.leo/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin:$PATH
pnpm ds:generate
pnpm verify
DS_AUDIT_OUTPUT=/tmp/typography-web-qa DS_TYPOGRAPHY_OUTPUT=/tmp/typography-web-qa/typography pnpm test:browser
pnpm typecheck
DS_AUDIT_OUTPUT=/tmp/typography-web-qa DS_TYPOGRAPHY_OUTPUT=/tmp/typography-web-qa/typography pnpm exec playwright test tests/browser/typography.spec.ts
```

Playwright utilizó Chrome instalado y el servidor HTTP local temporal configurado para `out/`. No se instalaron paquetes ni se publicaron servicios. Para otra corrida, elegir un directorio de evidencia nuevo antes de copiar sus resultados; no sobrescribir este corte histórico.

Revisión posterior: [75 estilos con tres recetas de escala materializada](revision-75/README.md). Este documento y sus resultados anteriores continúan describiendo el corte histórico de 72.
