# QA-BUTTON-FIGMA-002 · validación de Button en Figma

```yaml
qa_id: QA-BUTTON-FIGMA-002
review_type: IMPLEMENTATION_REVIEW
contract_ref: BUTTON-001
contract_version: 0.1.0
contract_digest: 4b94f80787c1fc9d9990f806c99900e17db060e65b624471b0c8d93f534f2abb
amendment_ref: AMD-BUTTON-PAGE-001
amendment_digest: b2c896cab9f2f5659101253dbc93ce0410c697081e53daafecebbc5b62895fd7
implementation_ref: IMP-BUTTON-FIGMA-001
target: figma
scope: representación estructural y visual de Button en AI-Design-System; excluye comportamiento web, semántica de producto y conformidad WCAG
blocked_items: []
accepted_deviations: []
reviewer: Codex
executed_at: 2026-09-23T00:59:54Z
result: PASS
```

## Resultado

El set existente se conservó. La única escritura en Figma fue renombrar `Page 1` a `Buttons` en el mismo page ID `0:1`; el component set mantuvo ID `26:81` y key `ad6968e790043ee654b3590596d5e593ebcbe73d`. El readback y los controles siguientes se ejecutaron después de esa escritura.

| Criterio | Resultado | Evidencia de lectura posterior |
|---|---|---|
| AC-BTN-001 | PASS | 60 variantes únicas y producto completo 4 tipos × 3 tamaños × 5 estados; sin combinaciones faltantes o extras. |
| AC-BTN-002 | PASS | Ocho definiciones nativas coinciden en clave, tipo y defaults: 2 Boolean, TEXT, 2 INSTANCE_SWAP, 3 VARIANT. |
| AC-BTN-003 | PASS | 364 nodos incluyendo el set, 60 textos y 120 instancias. 57 variantes tienen icono–texto–icono directos y las tres `default/focus` conservan el wrapper `btn-default` con la misma anatomía funcional. |
| AC-BTN-004 | PASS para el alcance especificado | En las 60 variantes se comprobaron alto, tipografía, line-height, tamaño de iconos, gap, layout horizontal y ancho `HUG`; 35 IDs de variables vinculadas coinciden exactamente con el YAML, 35/35 resuelven (26 locales, 9 remotas), sin IDs faltantes o extra. Los 60 textos tienen bindings de familia, tamaño, estilo, line-height y fill; los 60 contenedores tienen gap y radio vinculados. El padding está vinculado en 57 contenedores y en los tres wrappers `default/focus`. No hay fills ni strokes SOLID visibles sin binding en los 364 nodos. Se inspeccionó captura actual de 516×1883: no se aprecian recortes ni solapamientos. |
| AC-BTN-005 | PASS | Texto default `Default` en 60/60 variantes; ambos swaps apuntan a `26:3`; los 120 iconos resuelven a la misma key principal. |
| AC-BTN-006 | PASS en el alcance Figma aprobado | Se leyeron 23 reacciones `CHANGE_TO` sin transición: 12 default→hover, 3 link/hover→press y 8 focus→hover. Se conservan las dos transiciones observadas de `default/focus middle|small` a `default/large/hover`; no se corrigieron ni se completaron eventos ausentes. Esto no valida un modelo conductual web. |
| AC-BTN-007 | PASS | Una página llamada exactamente `Buttons`, page ID `0:1`, contiene como único nodo superior el set `26:81`; sin otra familia, páginas duplicadas ni cambio de IDs. |
| AC-BTN-008 | NOT_APPLICABLE | No se creó ni se validó frontend; el contrato excluye web de esta versión. |
| AC-BTN-009 | PASS | Las 120 instancias tienen main component key `46d251bb4099700c5852180f2370d265e5166432`, idéntica a la variante `PlusCircle / Outline / Light` leída en el archivo Phosphor Icons elegido por el usuario. |

## Medidas y tipografía

| Size | Variantes | Alto | Anchos observados con contenido de ejemplo | Icono | Texto | Gap |
|---|---:|---:|---|---:|---:|---:|
| large | 20 | 48 px | 154 / 135 px | 24 px | 16 px | 8 px |
| middle | 20 | 40 px | 146 / 127 px | 20 px | 16 px | 8 px |
| small | 20 | 32 px | 139 / 120 px | 20 px | 14 px | 8 px |

Las 60 etiquetas usan `Manrope`; 45 tienen peso 700 y 15 peso 400; las 15 variantes `link` están subrayadas. Las 12 variantes `focus` conservan stroke exterior de 2 px. Estas comprobaciones no equivalen a auditoría de contraste, teclado o WCAG.

## Límite conocido

La matriz de interacciones del nodo es incompleta y tiene los dos destinos que cambian de tamaño. Es evidencia documentada por el contrato, no una desviación corregida ni una aprobación de comportamiento de producto. Cualquier cambio de esos destinos o una implementación web requerirá especificación y aprobación nuevas. El resultado `PASS` certifica únicamente la representación Figma definida por `BUTTON-001` y la enmienda de página.
