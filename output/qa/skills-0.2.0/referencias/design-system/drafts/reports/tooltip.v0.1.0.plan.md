# PLAN-TOOLTIP-FIGMA-001 · construcción delegada

- **Contrato:** `TOOLTIP-001` 0.1.0, `DELEGATED_FOR_BUILD`, SHA-256 bytes `522b74426f781231dbf0a3ce7daed35909ab8f1358e347efe97e34f454416402`.
- **Decisión de alcance:** [DEC-LEGACY-MIGRATION-DELEGATION-001](../../registry/decisions.md); auditoría del usuario posterior.
- **Destino:** archivo `AI-Design-System` `tj3WIBEZDGLVs7MJWKCwgf`; operación `CREATE` de página exclusiva `Tooltips` y set `Tooltip`. Preflight comprobó que solo existían Buttons y Chips.
- **Dependencias:** JSON de variables aprobado, SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`; 13 variables semánticas locales localizadas; ningún componente anidado ni nueva variable.
- **Construcción:** cuatro componentes Align=Right/Down/Up/Left, auto layout según dirección, body/label/arrow, propiedad TEXT editable y fills/typography/spacing/radius enlazados. Fuente vectorial reproducida desde la ruta observada. Dos sombras literales preservadas como excepción documentada.
- **Reversibilidad:** no eliminar, mover ni renombrar páginas o componentes preexistentes. Registrar cada ID creado; si un lote falla, leer el estado real antes de reintentar.
- **Readback/QA:** página y set únicos, cuatro variantes, propiedad TEXT conectada, bindings de todos los colores y tokens aplicables, resolución por modo, shadow readback y captura visual. Comparar Buttons/Chips antes/después. Registrar cualquier diferencia de interlineado/tracking y `user_audit: PENDING`.
