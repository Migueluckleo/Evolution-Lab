# PLAN-INLINE-NOTIFICATION-FIGMA-001

- **Operación:** `CREATE` en `AI-Design-System`, página exacta `Inline Notifications`; preflight: nueve páginas existentes, ninguna homónima, sin set Inline Notification local. Biblioteca externa Notification no reutilizable por tokens, matriz y propiedad incompatibles con el contrato local.
- **Contrato:** [INLINE-NOTIFICATION-001 0.1.0](../contracts/inline-notification.contract.v0.1.0.md), `DELEGATED_FOR_BUILD`, QA documental `PASS`, auditoría humana `PENDING`.
- **Dato base:** `sources/inventories/tokens.inventory.json` SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`; dos enmiendas de iconos ya implementadas y leídas de vuelta.
- **P3.a — gate:** confirmar página ausente, 27 variables locales de color/tipo/espacio/radio/tamaño, Manrope Regular/SemiBold, alias Warning ámbar 700 y scopes estrictos.
- **P3.b — composición:** crear una página, cinco componentes Type, auto layout horizontal 602×108 base; icono 24, columna 482, Close 16; texto y cuatro booleanas en cada variante; combinar set y ordenar rejilla vertical.
- **P3.c — bindings:** 5 fondos `FRAME_FILL`, 10 iconos `SHAPE_FILL`, 10 textos `TEXT_FILL`; familia/peso/tamaño/interlineado, gaps, padding, radio y tamaños iconográficos con variables locales. Phosphor se importa por key dentro de la misma llamada de construcción.
- **P3.d — QA:** readback de cinco variantes, seis propiedades no-variant, instancias y keys, pinturas visibles y scopes, dimensiones y ausencia de reacciones; captura frente a fuente; registrar IDs de destino y estado sin publicar. La separación final de filas replica la fuente: set 650×990.
- **Riesgos:** importación remota puede fallar; no repetir tras error sin revisar `safeToRetryWithoutCanvasRead`. Una diferencia de 4 px de altura y copy normalizado quedan explícitos para auditoría. No se implementa dismiss funcional.
