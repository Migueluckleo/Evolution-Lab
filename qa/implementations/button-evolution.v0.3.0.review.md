# Button 0.3.0 · QA de implementación

Fecha: 2026-10-23. Estado de implementación Figma/web: PASS técnico. Publicación Git: HOLD_UNTIL_USER_REVIEW.

## Figma

Set 26:81: 90 variantes, 60 identidades previas conservadas, posiciones originales del grid conservadas. Se agregaron 15 variantes danger y 15 loading y se actualizó el foco de los cinco tipos/tres tamaños. Tres tokens nuevos aliases de red/600–800 en cuatro modos. Se reutiliza Loader local; no se modificaron sus principales.

Evidencia: [mutación](../../implementations/figma/button-evolution.v0.3.0.mutation.json), [tokens](../../implementations/figma/button-evolution.v0.3.0.token-map.json), [readback](../../implementations/figma/button-evolution.v0.3.0.readback.json), [muestra](https://www.figma.com/design/tj3WIBEZDGLVs7MJWKCwgf/AI-Design-System?node-id=1170-218).

La prueba de clones detectó pérdida de referencias de propiedades tras reparentado; se restauraron conexiones canónicas de texto, visibilidad y swaps en las variantes nuevas. Las 30 variantes pasan edición de texto y flags de iconos. Se corrigió recorte de los frames auxiliares de revisión; no se cambió la anatomía de los botones por ese ajuste.

Figma: PASS técnico. Se comprobaron las 90 identidades/alturas/estilos, los 15 Loader (24/20/16, principales locales), los 15 focos (-4/-4, +8/+8, stroke 2 INSIDE, radio 12 y bindings locales), la edición de texto y cambios de variante. Comparación por huella de propiedades de los 243 nodos originales: cero diferencias fuera del stroke de foco sustituido. La [prueba de propiedades](../../implementations/figma/button-evolution.v0.3.0.properties-qa.json), la [regresión](../../implementations/figma/button-evolution.v0.3.0.regression-qa.json) y el [cambio de variantes](../../implementations/figma/button-evolution.v0.3.0.swap-qa.json) conservan resultados reales.

Contraste calculado sRGB con texto blanco: #D40000 5.53:1, #9D0000 8.63:1, #680000 13.22:1. Mismos aliases en los cuatro modos; no se afirma conformidad WCAG integral ni se altera la política de contraste histórica de otros tipos/estados.

## Web

TypeScript: PASS. Se corrigió el filtro del generador P07 para excluir contratos TOOLING de la matriz de componentes, igual que FOUNDATIONS/MIGRATION; no se añadió una familia visual ficticia. La primera prueba de CSS detectó los roles danger aún ausentes del derivado anterior; tras regenerar, las nueve pruebas generales pasan.

Resultados finales: `pnpm typecheck` PASS; `pnpm test` 9/9 PASS; `pnpm build` PASS (export estático Next.js); `python3 implementations/web/scripts/generate.py --check` PASS, 43 familias y cero derivados desactualizados. `playwright test tests/browser/button-evolution.spec.ts` 2/2 PASS: bloqueo de clic/Enter/Espacio y navegación durante carga, recuperación de acción y foco, cinco tipos × tres tamaños × cuatro temas, geometría Loader y focus ring, tres colores destructivos y peso tipográfico. Para medir Loader se activa reducedMotion; la primera medición sin ello incluía la rotación en su caja envolvente y no era una medición de tamaño válido. El servidor temporal localhost se ejecutó con permiso de entorno después del bloqueo del sandbox y terminó con la prueba.

[Evidencia de navegador](button-evolution.v0.3.0.browser.json). Revisión visual del frame Figma 1170:218: tres tamaños, seis estados destructivos, carga y foco de los otros tipos, sin recortes. El render web puede consultarse en implementations/web/test-results/button-evolution.png.

## Distribución, índice y límites

Los resultados locales de P05/P08 se guardan en [comprobante de distribución](../../output/button-evolution/distribution.json) y el cierre del grafo en graphify-out/ds-closure.json. Esos resultados derivados deben consultarse para determinar vigencia; el PASS Figma/web de este documento no los sustituye. Retener publicación Git hasta revisión del usuario, incluidos catálogo y paquetes. No hubo commit, push ni publicación de biblioteca. No se declara aprobación visual humana ni conformidad WCAG integral.
