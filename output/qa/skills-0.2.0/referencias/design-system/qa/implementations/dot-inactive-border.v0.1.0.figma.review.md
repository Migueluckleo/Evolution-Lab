# QA-DOT-INACTIVE-BORDER-FIGMA-001

- **Resultado:** `PASS` técnico; auditoría humana `PENDING`.
- **Fuente canónica:** [JSON de extensión](../../drafts/foundations/ai-design-system.dot-inactive-border.v0.1.0.json), SHA-256 `edd8a4afe5f70502a395a5a1190aa11db3600b6a84472298f9b3a5e325f8c98a`.
- **Lectura Figma:** `color/border/status-inactive` `VariableID:157:122`, colección `semantic`, scope único `STROKE_COLOR`, descripción y `codeSyntax={}` coincidentes, cuatro aliases a `color/neutral/500` `VariableID:8:97`. Conteo semántico 139→140.
- **Consumo:** únicamente strokes de Inactive Large `155:129`, Medium `155:130` y Small `155:131`. Sus fills siguen ligados a `color/background/status-inactive` `VariableID:154:124`; los otros doce Dot conservan el borde blanco.
- **Contraste:** contorno neutral 500 contra superficie blanca 4.76:1 en los cuatro modos, frente a 1.23:1 del Dot Inactive original. Esto no certifica legibilidad de los textos numéricos ni accesibilidad del componente anfitrión.
