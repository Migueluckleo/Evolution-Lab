# QA-BADGE-FIGMA-002 · revisión final de Badge con enmienda de contraste

```yaml
qa_id: QA-BADGE-FIGMA-002
review_type: IMPLEMENTATION_REVIEW
contract_ref: BADGE-001
contract_version: 0.1.0
amendment_ref: AMD-BADGE-CONTRAST-001
amendment_version: 0.1.1
implementation_ref: IMP-BADGE-FIGMA-001
target: figma
result: PASS
executed_at: 2026-09-23
user_audit: PENDING
publish_status: UNPUBLISHED
```

La lectura posterior a la última escritura confirmó la página exclusiva `Badges` (`94:122`), el set `Badge` (`98:128`) y seis variantes Type (`97:170`, `97:176`, `97:182`, `97:188`, `97:194`, `97:200`). La construcción previa había verificado la anatomía, geometría, propiedades vinculadas, doce instancias Phosphor Presentation, 1512 preferidos de swap, 30/30 bindings tipográficos, 4/4 lados de trazo, 12/12 fills vectoriales y 104 relaciones token×modo. La enmienda únicamente cambió los bindings de `97:185`, `97:191`, `I97:189;8899:60223` e `I97:192;8899:60223`; el readback posterior confirmó los nuevos IDs locales. Un nuevo recorrido del set encontró 25 pinturas sólidas visibles, todas con binding.

| Criterio | Resultado | Evidencia |
|---|---|---|
| AC-BDG-001 | PASS | Página semántica exclusiva y set identificados; Buttons, Chips y Tooltips conservan sus páginas. |
| AC-BDG-002 | PASS | Seis valores Type únicos, base por defecto. |
| AC-BDG-003 | PASS | Auto layout horizontal, HUG/FIXED 25, padding 4/8/4/8, gap 4, radio 4 y tres hijos por variante. Captura posterior de 582×105 sin recortes aparentes. |
| AC-BDG-004 | PASS | TEXT `Badge text` y booleanos izquierdo/derecho conectados; Light, true y false por defecto. |
| AC-BDG-005 | PASS | Doce instancias Presentation de Phosphor sin detach, dos swaps independientes y 1512 opciones preferidas. |
| AC-BDG-006 | PASS | 25/25 pinturas sólidas visibles ligadas a variables locales. Informational usa texto principal; Warning usa texto e iconos principales conforme a la enmienda. En cuatro modos, texto mínimo 4.59:1 e iconos mínimos 3.61:1. |
| AC-BDG-007 | PASS | Bindings tipográficos, spacing, radio y trazo releídos; 104 aliases visuales resolvieron en los cuatro modos. |
| AC-BDG-008 | PASS | IDs, decisión, enmienda, desviaciones, hallazgo FAIL histórico, captura y estado registrados; auditoría humana pendiente. |

Contrastes de texto/icono por apariencia en los cuatro modos: base 17.85:1; light 16.30:1; informational 14.93:1 / 3.61:1; warning 15.91:1; error 4.59:1; success 4.64:1. Los cuatro modos resuelven los mismos valores en el inventario vigente. El QA anterior [QA-BADGE-FIGMA-001](badge.v0.1.0.contrast-finding.md) permanece `FAIL` como historial; esta revisión no lo sobrescribe.

La variante Light mide 64×25 en destino frente a 62×25 en la fuente por el trazo interior de 1 px por lado con HUG. El set conserva geometría y tokens originales; esta diferencia y los cambios de color de la enmienda requieren auditoría visual posterior del usuario. `PASS` acredita Figma estático, no publicación de biblioteca, teclado, accesibilidad funcional ni web.
