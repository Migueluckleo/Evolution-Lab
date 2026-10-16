# QA-BUTTON-FIGMA-SEMANTIC-004 · texto Disabled

```yaml
qa_id: QA-BUTTON-FIGMA-SEMANTIC-004
review_type: IMPLEMENTATION_REVIEW
contract_ref: BUTTON-001
amendment_ref: AMD-BUTTON-SEMANTIC-SCOPE-001
implementation_ref: IMP-BUTTON-SEMANTIC-SCOPE-FIGMA-001
target: figma
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

En `AI-Design-System`, página `Buttons` (`0:1`), set `button` (`26:81`), se actualizaron exactamente nueve labels Disabled para usar `color/text/disabled` (`VariableID:13:30`) en vez de `color/icon/disabled` (`VariableID:13:24`). Ambos aliasan `color/neutral/400` (`VariableID:8:96`) en los cuatro modos; la identidad del color no sustituyó la corrección del binding. Se cargó la fuente de los textos antes de mutarlos.

Lectura independiente posterior: las nueve IDs objetivo tienen el nuevo binding; las doce etiquetas Disabled del set usan `color/text/disabled`; entre los 60 nodos TEXT hay cero tokens de icono y cero scopes incompatibles. Se preservaron 60 variantes, 364 nodos, 120 instancias de icono, ocho definiciones de propiedad y 23 reacciones. La captura final 516×1883 no mostró cambio visual aparente, recortes o solapamientos nuevos.

`AC-BTN-004` pasa para la enmienda acotada. Los demás AC del contrato aprobado 0.2.0 se mantienen por lectura de estructura y por no haber sido editados en este lote; no se revalida producto web, teclado ni semántica de disabled. Auditoría humana `PENDING`, biblioteca `UNPUBLISHED`.
