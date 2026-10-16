# QA-AVATAR-ROLES-FIGMA-001

- **Resultado:** `PASS` técnico; auditoría humana `PENDING`.
- **Fuente canónica:** [JSON de extensión](../../drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json), SHA-256 `66a680bbb494895c76b43b9ca0d1b081c51afbb9c4dd079b6cf841c6488dc1f6`.
- **Readback:** dos variables nuevas en `semantic`: `color/background/avatar-fallback` `VariableID:164:122`, scope exclusivo `FRAME_FILL`, y `font/size/avatar-small` `VariableID:164:123`, scope exclusivo `FONT_SIZE`. Descripciones y `codeSyntax={}` coinciden; ocho aliases apuntan a primitivas correctas. Conteo semántico 140→142, sin primitivas nuevas.
- **Contraste:** fallback con blanco por modo: Contable 5.56:1, Administrativo 5.93:1, Servicios 4.72:1 con orange/600 y Personas 6.32:1. No se altera `color/interactive/primary/default` ni otra variable compartida.
- **Consumo:** ocho caras Icon/Text usan el nuevo fill; Initials Small consume la variable tipográfica de 10 px. El resto de la tipografía usa tokens existentes.
- **Límite:** no certifica el producto, la identidad ni una implementación web.
