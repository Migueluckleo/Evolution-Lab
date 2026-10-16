# QA Figma · Avatar, fondo Servicios de origen

**Resultado:** `PASS` técnico para `AC-TOK-AVA-001–003` y `AC-AVA-008–009` en el alcance cromático · 2026-09-24. `user_audit: PENDING`; set sin publicar.

- Fuente `1132:21344` y destino `165:247`: doce variantes cada uno. Readback fuente confirmó que el fondo Icon/Text usa blue/400, green/500, orange/500 y purple/500 por modo. El destino ahora conserva exactamente esos cuatro aliases en `color/background/avatar-fallback` `VariableID:164:122`, scope exclusivo `FRAME_FILL`, descripción y tipo `COLOR` intactos. Servicios apunta a `color/orange/500` `VariableID:8:71` `#FF5300` conforme al [JSON 0.1.1](../../drafts/foundations/ai-design-system.avatar-roles.v0.1.1.json).
- Ocho frames de fondo Icon/Text permanecen ligados al rol. Los doce Dot anidados mantienen sus bindings de fill y stroke; cuatro variantes Image no consumen el rol. El texto de iniciales permanece vinculado a `color/text/on-brand` y conserva tamaños 10/12/14/20 px; no se editó tipografía.
- La relación de blanco sobre orange/500 (~3.24:1) queda `*` para revisión interna. El tamaño fuente Small/Medium 6/9 px frente a destino 10/12 px sigue como normalización documental independiente. Este QA no prueba todos los detalles de imagen o geometría ni certifica WCAG; el QA antiguo de orange/600 es histórico para ese modo.
