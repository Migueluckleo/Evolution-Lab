# FOUNDATIONS-HEADER-RELEASE-001 · enmienda0.1.0

2026-10-01 · DELEGATED_FOR_BUILD; auditoría humana PENDING. Amplía Foundations únicamente en tres roles semánticos para HEADER-001, según delegación vigente y selección de primitiva existente más cercana.

Datos canónicos: [JSON Header0.1.0](../drafts/foundations/ai-design-system.header-release.v0.1.0.json). Ese JSON gobierna nombre,tipo,description única,scope yaliases por modo. No modifica el inventario histórico ni otras definiciones.

| Rol | ID local | Scope | Primitiva en cuatro modos |
|---|---|---|---|
| color/background/header-release-start | VariableID:516:122 | FRAME_FILL | color/purple/400 |
| color/background/header-release-end | VariableID:516:123 | FRAME_FILL | color/blue/400 |
| color/icon/header-caret-stroke | VariableID:516:124 | STROKE_COLOR | color/neutral/900 |

Los dos stops aproximan#844AEC→#A146FB y#2868FD→#3255F7; el caret coincide con#0F172A. No crean primitivas. El acento preliminar permanece fijo como en la fuente; empresa/perfil conservan roles de marca por tema.

QA: [readback independiente](../implementations/figma/header.v0.1.0.foundation-readback.json),3variables/12aliases,scopes ydescripciones iguales,0errores. [Contrato consumidor](header.contract.v0.1.0.md) y [QA](../qa/implementations/header.v0.1.0.figma.review.md). Asterisco de contraste del extremo violeta documentado; no se atribuye conformidad de accesibilidad.

Cambios posteriores versionados en specs, sincronizados con JSON yFigma. Esta enmienda no aprueba ni publica la biblioteca.

