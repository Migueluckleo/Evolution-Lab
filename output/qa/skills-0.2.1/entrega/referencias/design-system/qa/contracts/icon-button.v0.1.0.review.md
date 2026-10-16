# QA-ICON-BUTTON-CONTRACT-001 · reconstrucción 0.1.0

- **Resultado:** `PASS` documental para construcción delegada; auditoría humana `PENDING`.
- **Cobertura:** 21 secciones y AC-ICB-001–008; matriz completa 2×3×5, 30 Bell y 30 Dot reconciliados con fuente de 151 nodos.
- **Dependencias:** Bell Phosphor key activa observada, Dot Count local ya validado; 1512 candidatos de picker se pueden reutilizar sin inflar variantes. No se requiere un nuevo helper visual.
- **Tokens:** dos roles exclusivos de fondo Hover/Active definidos en [JSON](../../drafts/foundations/ai-design-system.icon-button-backgrounds.v0.1.0.json), aliases a primitivas existentes. Los demás roles locales se verificaron por nombre, descripción y scope; Dot Count del destino evita el fill fuente con rol `icon`.
- **Desviaciones:** `type=default`→Ghost y `middle`→Medium; Focus mantiene borde consistente y omite un único efecto source Large/Ghost. Small24 y tipografía Count4 siguen sin acreditación de accesibilidad táctil/informativa.
- **Límite:** QA documental no acredita variables creadas, set, bindings, picker ni visual de destino. Sin comportamiento web o aprobación humana del detalle.

Nota editorial 2026-10-01: corregida únicamente la ruta relativa al JSON existente en drafts/foundations. No cambia el resultado histórico ni constituye un nuevo QA.
