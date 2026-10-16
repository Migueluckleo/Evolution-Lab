# QA Figma · Inline Notification Warning, color de origen

**Resultado:** `PASS` técnico para `AC-INL-008–010` · 2026-09-24. `user_audit: PENDING`; set sin publicar. No hubo mutación adicional de Figma en esta revalidación: el alias compartido se restauró en Foundations previamente.

- Los sets fuente `2778:10287` y destino `175:432` contienen cinco variantes. Readback de 20 pinturas estructurales fuente/destino (fondos, iconos principales, títulos y cierres) confirmó RGB coincidente; las cinco descripciones base también coinciden en gris `#475569`. Los 25 paints sólidos del destino mantienen variables locales con categoría/scope correctos.
- Warning: vector `I175:417;8899:88650` ligado a `color/feedback/warning/icon` `VariableID:13:48`, `SHAPE_FILL`, alias a `color/amber/600` `VariableID:8:108` en cuatro modos; resuelve `#C97B00`, igual que el icono fuente, sobre `#FDF2C8`. Contraste ~2.96:1 marcado `*`.
- La fuente contiene cinco tramos finales de 18 caracteres en color brand azul y estilo SemiBold, sin URL. Su omisión en el destino es la normalización explícita del contrato, no una equivalencia cromática afirmada. El copy de destino es una muestra propia y no una reproducción literal de Lorem Ipsum.
- Permanecen las normalizaciones tipográficas y de altura del contrato base. Este QA no certifica comportamiento dismiss, anuncio accesible ni conformidad WCAG; el QA anterior sobre amber/700 es histórico para el criterio sustituido.
