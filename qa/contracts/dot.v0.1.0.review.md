# QA-DOT-CONTRACT-001 · reconstrucción 0.1.0

- **Resultado:** `PASS` documental para construcción delegada, con limitación de legibilidad registrada; auditoría humana `PENDING`.
- **Cobertura:** 21 secciones y AC-DOT-001–007; matriz fuente completa 5×3 y tamaños observados conservados. [Contrato](../../drafts/contracts/dot.contract.v0.1.0.md).
- **Fuente:** [MD](../../drafts/contracts/dot.source.component-contract.md) y [YAML](../../drafts/contracts/dot.source.component-contract.yaml), 22/22 nodos, 15 variantes, seis textos y 12 variables usadas. Las afirmaciones contradictorias de la Description antigua se excluyen de reglas.
- **Tokens:** cuatro nuevos roles `FRAME_FILL` definidos únicamente en [JSON de extensión](../../drafts/foundations/ai-design-system.dot-background-colors.v0.1.0.json), aliasados a tres primitivas existentes; `font/weight/bold`, `stroke/xs`, `radius/full`, `size/sm/md/lg`, `text/on-brand` y `border/on-brand` comprobados en Figma. Los fontSize 4/8 permanecen literales porque no existe primitiva tipográfica correspondiente y no se inventa una.
- **Legibilidad:** variante numérica Small no se valida como comunicación accesible de un conteo. El contrato obliga alternativa textual de producto y auditoría antes de uso. Mantenerla en Figma preserva evidencia visual; no equivale a aprobarla para producción.
- **Límite:** QA documental no acredita todavía variables creadas ni set construido. Sin comportamiento automático, umbral `99+`, implementación web o publicación.
