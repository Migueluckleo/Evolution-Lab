# QA-TOGGLE-FIGMA-001 · hallazgo de contraste antes de corrección

```yaml
qa_id: QA-TOGGLE-FIGMA-001
review_type: IMPLEMENTATION_REVIEW
contract_ref: TOGGLE-001
contract_version: 0.1.0
implementation_ref: IMP-TOGGLE-FIGMA-001
target: figma
result: FAIL
executed_at: 2026-09-23
```

La construcción inicial creó ocho variantes y las propiedades/bindings esperados. La captura de 704×280 reproduce visualmente la matriz fuente. En el readback cromático, los tracks Off/Default y Off/Focus sobre `color/background/default` blanco obtuvieron 1.23:1 en los cuatro modos, tanto en fill y contorno como en thumb blanco contra track. Esto no alcanza el referente de 3:1 para información visual necesaria de componentes de interfaz de [WCAG 2.2 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html). Los On no deshabilitados obtuvieron al menos 3.24:1, Off/Hover 4.76:1 y Disabled se trata como estado inactivo, no como prueba de legibilidad de control activo. Esta es una evaluación estática, no certificación web.

La alternativa semántica local `color/background/inverse` existe en el JSON aprobado y contrasta 14.63:1 con `color/background/default` en los cuatro modos; el anillo `color/focus/ring` contrasta 11.07:1 con esa superficie. El hallazgo original queda `FAIL` y no se borra por una corrección posterior.
