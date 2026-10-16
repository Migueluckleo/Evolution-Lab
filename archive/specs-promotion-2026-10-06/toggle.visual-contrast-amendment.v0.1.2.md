---
amendment_id: AMD-TOGGLE-VISUAL-CONTRAST-002
status: DELEGATED_FOR_BUILD
applies_to: TOGGLE-001
base_contract_version: 0.1.0
base_contract_digest_sha256: c3b6d1100241e3bdb5c89cc98e89854cda999c87f775a8552211280979326c38
supersedes: AMD-TOGGLE-CONTRAST-001
version: 0.1.2
affected_requirements: [REQ-TGL-005, AC-TGL-005]
decision_refs: [DEC-TOGGLE-VISUAL-CONTRAST-002, DEC-SEMANTIC-EXTENSIONS-001]
data_ref: sources/inventories/tokens.inventory.json
data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
extension_data_ref: drafts/foundations/ai-design-system.control-colors.v0.1.0.json
extension_data_digest_sha256: 4ef75143af30b0e934cb94aa62d3acb56c32874dc7e229a500a31c8928a7f839
last_updated: 2026-09-23
user_audit: PENDING
---

# Enmienda delegada 0.1.2 · equilibrio visual y contraste del Toggle apagado

Esta enmienda reemplaza la solución de color Off/Default y Off/Focus de [AMD-TOGGLE-CONTRAST-001](toggle.contrast-amendment.v0.1.1.md) y corrige dos bindings semánticos del contrato base en Off/Hover y Off/Disabled. La lectura visual [QA-TOGGLE-FIGMA-003](../../qa/implementations/toggle.v0.1.1.visual-fidelity-finding.md) encontró que los dos fondos oscuros de 0.1.1, aunque contrastantes, se alejaron demasiado de la fuente. Los demás requisitos y normalizaciones de TOGGLE-001 0.1.0 no cambian.

## Sustitución de REQ-TGL-005

En los tracks `Toggle=Off, State=Default` (`111:145`) y `Toggle=Off, State=Focus` (`111:155`), el fill vuelve a `color/background/muted` (`VariableID:13:37`), mismo valor pálido visible de la fuente. El stroke pasa a la nueva variable semántica `color/border/control`, ligada a `color/neutral/500` (`VariableID:8:97`) en los cuatro modos. No se cambia su geometría, thumb, texto ni anillo de foco. La solución se aproxima mucho más a la fuente: solo el borde neutral de 1 px se oscurece.

Off/Hover (`111:150`) sustituye el fill `color/text/tertiary` por la nueva variable `color/background/control-hover`; conserva el mismo gris primitivo y apariencia, con scope de fondo correcto. El thumb de Off/Disabled (`111:161`) sustituye `color/icon/on-brand` por el rol existente `color/background/default` (`VariableID:13:35`), que conserva el blanco y admite `SHAPE_FILL`. No cambian los demás paints, geometría ni propiedades.

El JSON fuente carece de un rol de borde neutral que cumpla 3:1 contra blanco; `color/border/default` resuelve a 2.56:1 y `color/border/strong` a 1.23:1. La autorización explícita posterior del usuario permite agregar roles nuevos siempre que el JSON de destino y Figma permanezcan fieles. Sus definiciones canónicas viven en `drafts/foundations/ai-design-system.control-colors.v0.1.0.json`, separadas del inventario histórico de la Librería fuente. Los dos roles toman el gris primitivo existente `color/neutral/500` (#64748b), 4.76:1 contra blanco en los cuatro modos, pero tienen scopes distintos para stroke y fill. Se deben crear y verificar en Figma **antes** de actualizar los consumidores. No se modifica un token compartido preexistente ni se cambia el JSON fuente.

## Sustitución de AC-TGL-005

`AC-TGL-005` pasa si el readback de Off/Default y Off/Focus confirma fill `VariableID:13:37` y stroke ligado por ID real a `color/border/control`; Off/Hover confirma fill `color/background/control-hover`; Off/Disabled thumb confirma fill `VariableID:13:35`; ambas variables nuevas coinciden campo por campo con el JSON de extensión y sus cuatro aliases apuntan a `VariableID:8:97`; se mantienen los demás bindings de la versión base y de las enmiendas no sustituidas; y el borde de ambos Off activos ofrece ≥3:1 contra `color/background/default` en los cuatro modos. Para los demás estados activos, el track o contorno que comunica el control también debe ofrecer ≥3:1. Los 40 paints visibles deben quedar ligados a roles con scope compatible y semántica apropiada. La captura posterior debe mostrar los dos Off pálidos con delineado neutro, no fondo oscuro. No se reajusta el umbral después de medir.

No se atribuye aprobación humana ni publicación de biblioteca. Se conservan el hallazgo de contraste inicial, el QA técnico de 0.1.1 y el hallazgo de fidelidad como historial. [QA documental](../../qa/contracts/toggle.visual-contrast-amendment.v0.1.2.review.md) `PASS`.
