# QA de la página Typography

**Fecha:** 2026-10-15 · **Destino:** [Typography · AI-Design-System](https://www.figma.com/design/tj3WIBEZDGLVs7MJWKCwgf/AI-Design-System?node-id=1003-412) · **Página:** `1003:412`.

**Resultado:** `PASS` para el readback técnico de la documentación y para las dos muestras visuales inspeccionadas. **Migración de componentes existentes:** `BLOCKED`, conforme al [informe de bloqueo](Figma-blocker.md). Esta página documenta foundations; no crea una familia de componentes y Slots es `NOT_APPLICABLE`.

## Fuente y cobertura técnica

La fuente es el [catálogo canónico 0.1.0](../../../specs/tokens/ai-design-system.typography.v0.1.0.json), SHA-256 `2b47811d3175b801f41e32e3bb174060697e7c265053741541bf7e602700afed`: 18 estilos base y 57 de compatibilidad, incluidos los tres derivados de escala documentada. El [QA de estilos](../../../implementations/figma/typography.v0.1.0.styles.qa.json) valida 75 definiciones, 304 bindings y 1,216 resoluciones de aliases en los cuatro modos; excluye expresamente la migración de componentes.

El [readback final de la página](specimens.readback.json) registra `PASS`, 75 tarjetas de estilos, 316 textos, 79 frames y `errors: []`. La distribución consta en el [estado de construcción](../../../implementations/figma/typography.v0.1.0.specimens.state.json):

| Tablero | ID | Estilos | Dimensiones |
|---|---|---:|---:|
| 01 · Base · 18 estilos | `1006:292` | 18 | 1,100 × 5,385 px |
| 02 · Compatibilidad · 1 de 3 | `1006:387` | 19 | 1,100 × 5,082 px |
| 03 · Compatibilidad · 2 de 3 | `1006:487` | 19 | 1,100 × 5,179 px |
| 04 · Compatibilidad · 3 de 3 | `1006:587` | 19 | 1,100 × 5,286 px |

Cada tarjeta contiene nombre, muestra en su estilo propio, valores y descripción canónica completa. Las descripciones utilizan Body/Regular de 14 px. Los contenedores usan Auto Layout y variables semánticas existentes de texto, fondo, separación y radio. La cabecera distingue los 18 estilos base de los complementarios y conserva el estado «Estilos listos · Migración de componentes pendiente».

## Inspección visual realizada

Se abrieron y revisaron las dos capturas locales siguientes. Los valores numéricos se acreditan por el catálogo y el readback; la inspección visual comprueba legibilidad, jerarquía, separación y ausencia de recortes o superposiciones visibles en estas muestras.

| Muestra | Evidencia | Resultado visual |
|---|---|---|
| Heading 1/Bold · tarjeta `1006:297`, texto `1006:299` | [Captura Heading 1](specimen.heading-1-bold.png) | `PASS`: la muestra ocupa dos líneas, ambas completas; nombre, métricas y descripción quedan separados y legibles. La descripción completa permanece dentro de la tarjeta, sin solaparse con la muestra de 56 px. |
| Body/Regular · tarjeta `1006:367`, texto `1006:369` | [Captura Body](specimen.body-regular.png) | `PASS`: muestra de una línea y descripción de dos líneas completas, con valores y nombre legibles, sin recorte ni superposición visible. |

No se inspeccionaron capturas de las 75 tarjetas ni vistas completas de los cuatro tableros. Estas dos imágenes no certifican otros modos visuales, todos los estilos Micro ni la tipografía de los componentes existentes. La cobertura técnica de 75 tarjetas se sustenta en el readback, separada de esta muestra visual.

## Falso negativo inicial de radios

El [estado inicial](../../../implementations/figma/typography.v0.1.0.specimens.state.json) conserva `READBACK_FAILED`: `errorCount: 75`, veinte errores detallados y 55 omitidos de la respuesta por tamaño, todos correspondientes al control inicial de `cornerRadius`. Ese control buscaba `boundVariables.cornerRadius`, mientras que Figma expone cuatro bindings de esquina. La lectura real confirmó `topLeftRadius`, `topRightRadius`, `bottomLeftRadius` y `bottomRightRadius`, cada uno con `VariableID:13:6` y 8 px.

Se corrigió únicamente la comprobación del [script de construcción](../../../implementations/figma/typography.v0.1.0.specimens.build.js), sin volver a mutar el lienzo por este ajuste. El [readback posterior](specimens.readback.json) resolvió el falso negativo. No se cambia el JSON histórico a `PASS` ni se interpreta su `visualQA: NOT_RUN` como descripción de esta revisión posterior.

La página y el catálogo están listos dentro del alcance documentado. Este QA no acredita la migración bloqueada ni aprobación visual humana del sistema completo.
