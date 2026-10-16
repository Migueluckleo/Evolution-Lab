# QA documental · Avatar, color de origen Servicios

**Resultado:** `PASS` documental para construcción delegada · 2026-09-24. Auditoría humana `PENDING`.

- La fuente `1132:21344` y destino `165:247` tienen doce variantes. Los paints visibles en Contable coinciden; readback de aliases identificó una desviación cromática por modo: Servicios source orange/500, destino orange/600, en el único rol de fondo fallback compartido por ocho variantes Icon/Text.
- La primitiva `color/orange/500` existe localmente como `VariableID:8:71`. El override JSON 0.1.1 cambia solo ese alias; mantiene scope `FRAME_FILL`, descripción y los otros tres modos. No modifica Dot ni tipografía.
- La limitación de texto blanco sobre orange/500 se conserva `*`. Las diferencias de tamaño 6/9→10/12 px son previas y se llevan a auditoría separada; esta enmienda no las resuelve por implicación.
