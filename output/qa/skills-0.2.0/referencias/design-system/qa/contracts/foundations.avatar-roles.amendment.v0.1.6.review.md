# QA-AVATAR-ROLES-001 · extensión de Foundations

- **Resultado:** `PASS` documental para construcción delegada; auditoría humana `PENDING`.
- **Datos:** [JSON canónico](../../drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json) con dos variables, ocho aliases a primitivas existentes, `FRAME_FILL` y `FONT_SIZE` exclusivos, una descripción y `codeSyntax={}` por variable. El inventario fuente no se altera.
- **Necesidad:** el fondo del Avatar fuente no es interactivo aunque use rol de interacción; Small usa iniciales de 6 px. El nuevo fondo conserva la paleta por modo, salvo Servicios, que pasa de orange/500 3.24:1 a orange/600 4.72:1 con blanco. Small sube a 10 px mediante una primitiva ya aprobada.
- **Límite:** pendiente creación/readback en Figma y QA del componente; el token de 10 px no equivale a certificación de accesibilidad.
