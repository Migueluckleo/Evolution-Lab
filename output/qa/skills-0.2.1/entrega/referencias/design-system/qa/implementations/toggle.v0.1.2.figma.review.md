# QA-TOGGLE-FIGMA-004 · fidelidad visual, contraste y scopes

```yaml
qa_id: QA-TOGGLE-FIGMA-004
review_type: IMPLEMENTATION_REVIEW
contract_ref: TOGGLE-001
amendment_ref: AMD-TOGGLE-VISUAL-CONTRAST-002
implementation_ref: IMP-TOGGLE-FIGMA-001
target: figma
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

La lectura posterior a la última escritura identifica la página `Toggles` (`111:122`), set `Toggle` (`111:163`), ocho variantes Toggle On/Off × Default/Hover/Focus/Disabled y seis definiciones de propiedad (dos TEXT, dos BOOLEAN, dos VARIANT). La enmienda 0.1.2 afectó únicamente cuatro nodos y seis bindings de paint:

| Parte | Binding final | Resultado |
|---|---|---|
| Off/Default track `111:145` | fill `color/background/muted` `VariableID:13:37`; stroke `color/border/control` `VariableID:123:122` | PASS; 40×20, borde 1 px |
| Off/Focus track `111:155` | fill `color/background/muted` `VariableID:13:37`; stroke `color/border/control` `VariableID:123:122` | PASS; 40×20, borde 1 px y anillos focus preservados |
| Off/Hover track `111:150` | fill `color/background/control-hover` `VariableID:123:123` | PASS; gris #64748b visualmente igual al anterior, categoría y scope de fondo correctos |
| Off/Disabled thumb `111:161` | fill `color/background/default` `VariableID:13:35` | PASS; blanco preservado, sin rol de icono en shape de thumb |

Se recorrieron las 40 pinturas sólidas visibles del set: 40/40 ligadas a variables locales y **cero** usos de categoría semántica o scope incompatibles. Los dos tokens nuevos coincidieron en Figma con [su JSON de extensión](../../drafts/foundations/ai-design-system.control-colors.v0.1.0.json) en los cuatro modos según [QA-CONTROL-COLORS-FIGMA-001](control-colors.v0.1.0.figma.review.md). Para los seis estados activos, la comparación estática de fill o contorno necesario contra `color/background/default` dio mínimo 3.24:1 en los cuatro modos; Off/Default, Off/Hover y Off/Focus dieron 4.76:1 en cada modo. Disabled no se usó para justificar controles activos.

La captura del set posterior al ajuste (704×280) se inspeccionó junto a la captura fuente (680×194): Off/Default y Off/Focus vuelven al fondo pálido de origen y solo aumenta el contraste del contorno neutral de 1 px. Off/Hover y el thumb Disabled conservan su color. No se observaron recortes ni solapamientos aparentes. Las diferencias ya documentadas de normalización (`defualt`, radio, interlineado y halo) siguen vigentes; no se atribuye paridad píxel a píxel.

El [QA 0.1.1](toggle.v0.1.1.figma.review.md) queda como comprobación técnica histórica y el [hallazgo de fidelidad](toggle.v0.1.1.visual-fidelity-finding.md) como motivo de esta corrección. El set permanece `UNPUBLISHED`; QA técnico `PASS`, auditoría humana `PENDING`, sin afirmar accesibilidad funcional, hit target, teclado ni web.
