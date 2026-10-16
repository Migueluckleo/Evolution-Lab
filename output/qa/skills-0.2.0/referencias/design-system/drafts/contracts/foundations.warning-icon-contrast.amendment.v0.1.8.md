---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-WARNING-ICON-CONTRAST-001
name: Warning icon contrast
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.8
last_updated: 2026-09-23
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.0.json]
---

# Foundations · contraste del icono Warning 0.1.8

Se sustituyen solo los cuatro aliases por modo de `color/feedback/warning/icon` `VariableID:13:48`: de la primitiva `color/amber/600` a la primitiva ya existente `color/amber/700`. El [JSON de override](../foundations/ai-design-system.warning-icon-contrast.v0.1.0.json) gobierna esos cuatro valores. La descripción canónica permanece en el inventario base; no se duplica. Nombre, tipo `COLOR`, scope exclusivo `SHAPE_FILL` establecido por la enmienda anterior y `codeSyntax` quedan intactos.

En el fondo semántico `color/feedback/warning/bg` (alias amber/100), el contraste del icono pasa de 2.96:1 a 4.38:1 en los cuatro modos. El cambio mantiene el tono ámbar de la fuente y evita una variable nueva. El preflight de nueve páginas de componentes existentes no encontró consumidores actuales de este token; el primer consumidor será Inline Notification Warning. Esto no certifica accesibilidad del mensaje, solo mejora la distinción no textual del icono. Se verifica Figma por readback antes de construir la familia; auditoría humana pendiente.
