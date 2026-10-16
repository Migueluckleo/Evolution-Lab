# QA-TOGGLE-FIGMA-003 · revisión de fidelidad visual

```yaml
qa_id: QA-TOGGLE-FIGMA-003
review_type: VISUAL_FIDELITY_REVIEW
contract_ref: TOGGLE-001
amendment_version: 0.1.1
implementation_ref: IMP-TOGGLE-FIGMA-001
target: figma
result: FAIL
executed_at: 2026-09-23
```

La captura posterior a la enmienda 0.1.1 mostró Off/Default y Off/Focus con un track neutral oscuro, aunque en la fuente ambos son pálidos. El contraste activo pasó, pero la superficie cambió de forma material frente al requisito de conservar el estilo de la Librería anterior con las menores desviaciones posibles. La aclaración del usuario del 2026-09-23 reafirma esa prioridad. Esta revisión visual marca la solución 0.1.1 `FAIL` en fidelidad, sin borrar su QA técnico previo, que acreditó los bindings de esa versión.

Preflight read-only: no hay un rol `color/border/*` neutral que llegue a 3:1 contra blanco en el inventario actual; `color/border/default` ofrece 2.56:1 y `color/border/strong` 1.23:1. `color/text/tertiary` da 4.76:1 pero su scope `TEXT_FILL` no corresponde a un stroke. La instrucción posterior del usuario autorizó agregar un token nuevo cuando sea necesario, con fidelidad entre JSON y variables Figma. La solución propuesta se actualizó para definir `color/border/control` en un JSON de extensión separado de la fuente y verificar su variable en el destino.
