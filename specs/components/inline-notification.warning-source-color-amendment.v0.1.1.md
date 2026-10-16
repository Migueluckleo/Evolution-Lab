---
amendment_id: AMD-INLINE-NOTIFICATION-WARNING-SOURCE-COLOR-001
status: DELEGATED_FOR_BUILD
applies_to: INLINE-NOTIFICATION-001
base_contract_version: 0.1.0
base_contract_digest_sha256: 2d732e7621da22e8aaf9055602ac194582bf84deeba9e9d23eea10649ecdb17e
version: 0.1.1
supersedes_scope: REQ/AC-INL-005 and section 6 only for Warning icon alias, RGB, and contrast threshold
foundation_dependency: specs/foundations/foundations.warning-icon-source-color.amendment.v0.1.10.md
last_updated: 2026-09-24
user_audit: PENDING
---

# Inline Notification · Warning fiel a la fuente 0.1.1

El contrato base 0.1.0 exigía temporalmente `color/feedback/warning/icon` en amber/700 y contraste de al menos 3:1. La [enmienda Foundations vigente](../../specs/foundations/foundations.warning-icon-source-color.amendment.v0.1.10.md) restaura el alias de ese rol a `color/amber/600` en cuatro modos, para coincidir con la Librería anterior. Esta enmienda sustituye **solo** la regla de color y umbral Warning del contrato base: el icono conserva binding a `color/feedback/warning/icon` `VariableID:13:48`, scope `SHAPE_FILL`, y resuelve `#C97B00` sobre fondo `#FDF2C8` (aproximadamente 2.96:1). Se marca `*` para revisión interna; no se declara conformidad WCAG.

El readback de las cinco variantes muestra iguales los fondos, iconos, títulos y cierres respecto de la fuente. La descripción fuente tiene cinco tramos finales azules que simulan enlaces sin URL; el destino mantiene deliberadamente el texto de ejemplo neutro y su rol `color/text/secondary`, como ya exigen AC-INL-006 y la sección 7 del contrato base. No se añade enlace aparente ni se altera geometría, propiedades o variables.

`AC-INL-008`: readback del icono Warning, su alias en cuatro modos, scope y RGB originales. `AC-INL-009`: registrar la limitación de contraste `*` y confirmar la normalización documental de los cinco tramos sin URL, sin interpretarla como discrepancia no resuelta. `AC-INL-010`: preservar cinco variantes, cinco fondos, cinco iconos principales, cinco títulos y cinco cierres con sus bindings semánticos. La auditoría humana sigue pendiente y el set no se publica.
