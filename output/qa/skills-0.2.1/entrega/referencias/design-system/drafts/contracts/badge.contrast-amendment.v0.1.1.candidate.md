---
amendment_id: AMD-BADGE-CONTRAST-001
status: DRAFT
applies_to: BADGE-001
base_contract_version: 0.1.0
base_contract_digest_sha256: abc4e0e768be75831c343fe8e32322322e650ad437b7eae4860e498cbdc6f216
version: 0.1.1
affected_requirements: [REQ-BDG-006, AC-BDG-006]
decision_ref: DEC-BADGE-CONTRAST-001
data_ref: sources/inventories/tokens.inventory.json
data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
last_updated: 2026-09-23
user_audit: PENDING
---

# Enmienda candidata 0.1.1 · contraste de Badge

La construcción inicial de [BADGE-001 0.1.0](badge.contract.v0.1.0.md) reprodujo los roles semánticos de feedback del JSON. El readback calculó contraste de texto/icono 3.61:1 en Informational y 2.96:1 en Warning; las otras apariencias quedaron en 4.59:1 o más para texto. Para texto normal, [WCAG 2.2 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) usa 4.5:1; para iconografía necesaria, [1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) usa 3:1. Esta evaluación de Figma es de color estático, no una certificación de producto accesible.

## Cambio acotado de REQ-BDG-006

En las variantes `informational` y `warning`, el texto usará la variable local existente `color/text/primary` (`VariableID:13:27`) en lugar de `color/feedback/information/text` y `color/feedback/warning/text`. En `warning`, ambos vectores de icono usarán `color/icon/primary` (`VariableID:13:20`) en lugar de `color/feedback/warning/icon`. El icono de `informational` conserva `color/feedback/information/icon` (`VariableID:13:56`), cuyo contraste observado es 3.61:1. Fondos, iconos y textos de las otras cuatro variantes, bordes, propiedades, geometría y jerarquía no cambian.

La comparación read-only de los tokens locales resueltos para Contable mostró: texto principal sobre fondo Information 14.93:1, texto/icono principal sobre fondo Warning 15.91:1. La revisión de implementación debe repetir la medición en los cuatro modos después de la escritura. Estos tokens existen en el JSON aprobado y no se crea ni modifica ninguna variable. El cambio es una decisión de diseño delegada para corregir contraste; difiere visiblemente del color de texto e icono fuente y queda sujeto a auditoría humana.

## Sustitución de AC-BDG-006

`AC-BDG-006` pasa si el readback confirma los IDs anteriores en los nodos afectados, mantiene los demás bindings del contrato base y demuestra texto ≥4.5:1 e iconos semánticamente necesarios ≥3:1 en las seis variantes y cuatro modos. Un resultado bajo el umbral es `FAIL`; no se ajusta la tolerancia después de medir.

Todos los demás REQ/AC de BADGE-001 0.1.0 permanecen intactos. Esta enmienda no aprueba su contenido en nombre del usuario ni implica publicación de la biblioteca.
