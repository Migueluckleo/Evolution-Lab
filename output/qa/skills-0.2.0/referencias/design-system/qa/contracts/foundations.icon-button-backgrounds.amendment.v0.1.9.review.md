# QA-ICON-BUTTON-BACKGROUNDS-001 · Foundations 0.1.9

- **Resultado:** `PASS` documental para extensión delegada; auditoría humana `PENDING`.
- **JSON:** dos variables `COLOR`, scope único `FRAME_FILL`, ocho aliases por identidad a ocho primitivas preexistentes, cuatro modos, una `description` por variable y `codeSyntax` vacío como las variables base aprobadas.
- **Justificación:** roles Hover/Active de Icon Button faltaban con los valores de la fuente; reutilizar `active` para Hover o `default` para Active violaría el protocolo semántico del usuario. No hay primitiva nueva ni cambio de apariencia previsto.
- **Gate Figma:** verificar ausencia, crear y leer de vuelta ambas variables antes de consumirlas; QA documental no acredita la escritura.
