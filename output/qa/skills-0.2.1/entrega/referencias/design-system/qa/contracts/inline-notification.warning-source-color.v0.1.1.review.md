# QA documental · Inline Notification Warning 0.1.1

**Resultado:** `PASS` documental para revalidación delegada · 2026-09-24. Auditoría humana `PENDING`.

- Se identificó el requisito concreto ya desactualizado del contrato base: amber/700 y umbral 3:1 para el icono Warning. La dependencia Foundations vigente exige amber/600 de la fuente y ya pasó QA Figma.
- La enmienda sustituye solo esa regla; mantiene cinco variantes, roles estrictamente semánticos y la decisión previa de no simular enlaces sin URL.
- La lectura de la fuente comprobó el tramo final azul de 18 caracteres en las cinco descripciones; es contenido demostrativo sin vínculo funcional. La decisión de omitirlo ya estaba explícita en el contrato base.
- La limitación de contraste Warning se marca `*`, sin cambio de color adicional ni certificación accesible.
