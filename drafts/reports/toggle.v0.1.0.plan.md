# TOGGLE-001 · plan de construcción delegado

- **Fuente:** set `1230:23858`, página `1084:7229`, Librería anterior. 41/41 nodos y 24 variables fuente leídos.
- **Contrato:** [TOGGLE-001 0.1.0](../contracts/toggle.contract.v0.1.0.md), SHA-256 `c3b6d1100241e3bdb5c89cc98e89854cda999c87f775a8552211280979326c38`; QA documental `PASS`, auditoría humana pendiente.
- **Datos:** JSON aprobado `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.
- **Destino:** `AI-Design-System` `tj3WIBEZDGLVs7MJWKCwgf`; crear página funcional exclusiva `Toggles` y set `Toggle`.
- **P0/P1/P2:** destino preflight con Buttons, Chips, Tooltips y Badges; ninguna página Toggles. Colecciones `semantic` (cuatro modos) y `primitive` (Value) existentes; 24 roles de destino previstos, todos presentes. Búsqueda de librería encontró `toggled` solo en la Librería anterior, no un set local compatible. No se crean colecciones, variables ni estilos.
- **P3:** una llamada de construcción en la nueva página para ocho componentes, track/thumb, dos textos opcionales por variante, propiedades enlazadas, bindings cromáticos/tipográficos/geométricos y efectos. Posicionar los componentes en rejilla de cuatro columnas × dos filas y redimensionar el set a su bounding box. Documentación mínima en la misma página. Guardar todos los IDs devueltos antes de otra operación.
- **P4:** readback separado de ocho variantes y propiedades, 24 roles×4 modos, todos los fills/strokes y focus effects, reacciones, nombres y screenshot. Contrast/target-size solo como observación estática; no afirmar accesibilidad web.
- **Diferencias visibles o semánticas:** `defualt`→`Default`; radio Off/Focus de token tipográfico→`radius/full`; Off/Focus de roles disabled→muted/strong; line-height 15→16; halo focus claro literal→`background/default` blanco; contenedor documental fuente no se copia. Off/Hover conserva text/tertiary por falta de rol neutral hover equivalente.
- **Riesgo:** los efectos tienen geometría fraccional y su variable de color debe verificarse tras escritura. Cualquier error interrumpe P4 y queda documentado, sin borrar la fuente ni otras páginas.
