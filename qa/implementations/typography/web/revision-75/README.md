# QA tipográfico web · revisión de 75 estilos

**PASS · 2026-10-15 · evidencia DERIVED.** Esta revisión amplía el [corte histórico de 72](../README.md) con tres recetas de escala materializada. Conserva los resultados anteriores; no los sustituye por una validación que no se haya ejecutado.

Fuente: [JSON canónico](../../../../../specs/tokens/ai-design-system.typography.v0.1.0.json), SHA-256 `2b47811d3175b801f41e32e3bb174060697e7c265053741541bf7e602700afed`. Total: 18 estilos base y 57 complementarios. Los tres nuevos preservan 103 rangos existentes de Figma según su evidencia; el resultado web no acredita la aplicación en Figma.

| Comprobación ejecutada | Resultado | Evidencia |
|---|---:|---|
| Generador: unidades, refs y escala FLOAT32 exacta, sin doble escala | 9 pruebas PASS | [log](python-tests.log) |
| Generación determinista | PASS | [generación](generate.log), [check](determinism.log) |
| TypeScript y build estático | PASS | [typecheck](typecheck.log), [build](build.log) |
| Clases: 75 estilos × cuatro temas con Manrope local | 300 recetas PASS | [mediciones](typography/styles.json) |
| Consumidores: 43 familias × cuatro temas | 2,956 textos PASS | [mediciones](typography/consumers.json) |
| Comparación con el corte de 72 | Consumidores y cinco hashes de fuente idénticos | [preservación](consumer-preservation.json) |

La ejecución Chrome afectada contiene dos pruebas: [reporte](browser-report.json), [log](browser.log). La suite completa de 61 pruebas **no se repitió**; su [reporte anterior](../browser-suite-61.json) permanece disponible. [El resumen](implementation-summary.json) registra los hashes y las métricas exactas de las tres recetas nuevas.

CSS conserva literalmente `5.333333492279053`, `9.333333969116211` / `13.333333969116211` y `11.666666030883789` / `16.66666603088379` px. El generador valida `FLOAT32(base × FLOAT32(ratio))` y emite la medida resuelta; no vuelve a escalarla. Los porcentajes se conservan relativos. La serialización de `getComputedStyle` en Chrome tiene su propia precisión; las pruebas del generador verifican los literales completos por separado.

## Comandos ejecutados

Desde la raíz:

```sh
python3 -m unittest discover -s implementations/web/scripts -p test_typography.py -v
python3 implementations/web/scripts/typography.py --check
```

Desde `implementations/web`, con el runtime Node/pnpm local:

```sh
export PATH=/Users/miguel.leo/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin:$PATH
pnpm ds:generate
pnpm typecheck
pnpm build
DS_AUDIT_OUTPUT=/tmp/typography-web-qa-75 DS_TYPOGRAPHY_OUTPUT=/tmp/typography-web-qa-75/typography pnpm exec playwright test tests/browser/typography.spec.ts
```

Chrome instalado y servidor HTTP temporal de `out/`, sin instalación ni publicación. Se copió íntegramente `/tmp/typography-web-qa-75`; las rutas internas de ejecución se conservaron. Este corte no añade inspección visual manual ni certifica otros motores o composiciones arbitrarias de Slots.
