# QA-TOGGLE-FIGMA-002 · revisión final de Toggle

```yaml
qa_id: QA-TOGGLE-FIGMA-002
review_type: IMPLEMENTATION_REVIEW
contract_ref: TOGGLE-001
contract_version: 0.1.0
amendment_ref: AMD-TOGGLE-CONTRAST-001
amendment_version: 0.1.1
implementation_ref: IMP-TOGGLE-FIGMA-001
target: figma
result: PASS
executed_at: 2026-09-23
user_audit: PENDING
publish_status: UNPUBLISHED
```

Readback posterior a la última escritura: página única `Toggles` `111:122`, set `Toggle` `111:163`, ocho combinaciones On/Off × Default/Hover/Focus/Disabled, seis definiciones de propiedad con defaults correctos y 16 etiquetas ocultas conectadas. Los ocho componentes miden 40×20, con track y thumb fraccional en la posición correspondiente. Se inspeccionó la captura posterior de 704×280: On azul, Off neutral oscuro, hover y foco diferenciados, sin recortes aparentes.

| Criterio | Resultado | Evidencia |
|---|---|---|
| AC-TGL-001 | PASS | Página exclusiva y set único; Buttons, Chips, Tooltips y Badges conservan nombres y páginas. |
| AC-TGL-002 | PASS | 8/8 pares únicos; Toggle=On y State=Default por defecto, sin `defualt` en destino. |
| AC-TGL-003 | PASS | Ocho tracks 40×20 y thumbs 16⅔×16⅔, posiciones x 21⅔/1⅔ y y 1⅔; dos textos opcionales por variante. |
| AC-TGL-004 | PASS | Dos TEXT y dos BOOLEAN enlazadas a los 16 textos, defaults `Field Label`/false. |
| AC-TGL-005 | PASS | 40/40 pinturas sólidas de set con binding, 32/32 radios, 32/32 lados de stroke; Off/Default y Off/Focus ligados a `color/background/inverse` por la enmienda. 25 roles locales resueltos en cuatro modos. |
| AC-TGL-006 | PASS | 80/80 bindings tipográficos, 8/8 gaps, 4/4 colores de anillo de foco en efectos ligados a variables; sombras internas literales preservadas como excepción sin token de sombra. |
| AC-TGL-007 | PASS | Cero reacciones nuevas; web/teclado/área táctil no declarados como implementados. |
| AC-TGL-008 | PASS | IDs, contrato, enmienda, captura, hallazgo previo, diferencias y auditoría pendiente registrados. |

La comparación de track contra superficie blanca en las apariencias activas tiene mínimo 3.24:1 (On en modo Servicios), por encima del umbral estático 3:1 para información visual necesaria de [WCAG 2.2 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html). Off/Default y Off/Focus mejoraron de 1.23:1 a 14.63:1 en los cuatro modos; Off/Hover permanece 4.76:1. El anillo de foco contrasta 11.07:1 con la superficie. Disabled no se usa para justificar contraste de estado activo. El primer auditor de aliases marcó cuatro falsos positivos porque trató el valor numérico 0 de `font/letter-spacing/normal` como ausencia; una lectura independiente confirmó alias `VariableID:8:21` y valor 0 válido en los cuatro modos, por lo que son 100/100 relaciones token×modo.

La variante Off normal difiere visiblemente de la fuente al usar superficie inverse; también se normalizaron nombre Default, radio Off/Focus, line-height de labels y halo claro. Todas las decisiones están registradas para auditoría humana. El hallazgo [QA-TOGGLE-FIGMA-001](toggle.v0.1.0.contrast-finding.md) permanece `FAIL` histórico y no se sobrescribe. El componente visual 40×20 no demuestra área de interacción 44×44 ni accesibilidad funcional; eso corresponde a implementación web posterior. El set está `UNPUBLISHED`.
