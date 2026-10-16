# QA documental · bordes Checkbox y Radio Button

**Resultado:** `PASS` documental para construcción delegada · 2026-09-24. Auditoría humana `PENDING`.

- Comparación read-only de fuente y destino: Checkbox tiene doce variantes; solo Unselected Default/Focus difieren `#94A3B8`→`#64748B`. Radio Button tiene ocho variantes; solo Off Default difiere en ese contorno. Otros paints visibles conservan el RGB observado, aunque la anatomía de Selected Radio difiere de forma documentada.
- El rol compartido `color/border/control` ya existe con scope exclusivo `STROKE_COLOR`; neutral/400 `VariableID:8:96` es primitiva local aprobada. Toggle no lo consume actualmente. El override 0.1.1 altera solo cuatro aliases de ese rol y preserva `color/background/control-hover`.
- Dos enmiendas de componente sustituyen únicamente el ajuste cromático por contraste. La visibilidad original del contorno se marca `*`, sin cambiar efectos ni certificar accesibilidad.
