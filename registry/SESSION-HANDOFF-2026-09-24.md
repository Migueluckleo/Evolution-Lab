# Pausa de migración · 2026-09-24

**Estado histórico:** `PAUSED_BY_USER` después de terminar la ampliación Mixed de Toggle. El usuario indicó posteriormente **continuar**; esta pausa ya no está vigente. Motivo operativo original: asistencia para cambiar su antivirus. El progreso posterior consta en [registro de implementaciones](implementations.md) y [matriz de trazabilidad](../specs/MIGRATION-TRACEABILITY-STATUS.md).

## Punto cerrado antes de pausar

- El [PNG del usuario](../references/toggle-mixed-user-2026-09-24.png) se preservó e indexó como `SRC-TOGGLE-MIXED-PNG-001`.
- El [contrato de comportamiento](../drafts/behavior/toggle-mixed/behavior-contract.md) y su [YAML](../drafts/behavior/toggle-mixed/behavior-contract.yaml) definen Mixed cuando un grupo contiene On y Off. Clic desde Mixed y grupo vacío siguen `REQUIRES_DEFINITION`; no bloquean la representación visual Figma.
- La [enmienda visual 0.1.4](../drafts/contracts/toggle.mixed-amendment.v0.1.4.md) tiene [QA documental PASS](../qa/contracts/toggle.mixed-amendment.v0.1.4.review.md), `DELEGATED_FOR_BUILD`, auditoría humana pendiente.
- AI Design System conserva la página `Toggles` `111:122` y set `Toggle` `111:163`. Ahora tiene 12 variantes: los ocho IDs anteriores intactos y cuatro Mixed, Default `232:122`, Hover `232:128`, Focus `232:134`, Disabled `232:140`. `Toggle={On,Off,Mixed}` y `State={Default,Hover,Focus,Disabled}`. No se añadieron variables.
- Se reconectaron las propiedades de las ocho etiquetas ocultas de Mixed tras observar que el clonado de Figma no conservó sus referencias. El [QA de implementación](../qa/implementations/toggle.mixed.v0.1.4.figma.review.md) es `PASS` para la ampliación Mixed, con [estado/IDs](../implementations/figma/toggle.mixed.v0.1.4.state.json). Página y set permanecen `UNPUBLISHED`.
- Medición del guion: Default 5.56 / 5.93 / 3.24 / 6.32:1 según modo; Hover 11.07 / 9.53 / 7.20 / 10.01:1; Disabled 2.34:1 marcado `*` en [auditoría por excepciones](../specs/MIGRATION-AUDIT.md). No se cambió color para elevar contraste.

## Pendiente al reanudar

1. Retomar el trabajo anterior de fidelidad cromática de la migración: restaurar colores de origen ajustados solo por contraste, con scopes semánticos correctos, JSON/Figma sincronizados y nueva medición real. Los QA cromáticos previos se consideran `STALE` según [registro](qa.md); Mixed no los cierra.
2. Promover a `specs/` los contratos que cumplan QA documental y de implementación vigente conforme a `DEC-MIGRATION-SPECS-AUDIT-001`. El contrato base de Toggle y sus enmiendas aún están en `drafts/contracts/`; no declarar que ya se publicaron en specs ni en la biblioteca Figma.
3. Continuar después con las familias restantes de la Librería fuente, usando el documento único de auditoría por excepciones. No solicitar aprobación por componente salvo ambigüedad material.
4. Cuando el producto requiera interacción real, definir `UPD-001` (clic desde Mixed) y `UPD-002` (grupo vacío) antes de implementarla en web. No son decisiones necesarias para la variante visual ya terminada.

## Comprobación de cierre

Leídos: contrato Toggle base, JSON de tokens aprobado, página/set Figma actuales, PNG adjunto, guías/protocolos de contratos, Figma y QA. Cambiados: contratos Mixed, fuente preservada, cuatro componentes Figma, descripción/nota de página, registros de decisión/implementación/QA y auditoría. Verificados: 12 combinaciones, seis definiciones de propiedad, ocho IDs previos, 16 referencias de etiquetas, cuatro fills de guion y 16 radios ligados a variables locales, foco y aliases por cuatro modos, captura visual, estado `UNPUBLISHED`. Bloqueado: nada para la ampliación visual. Pendiente: auditoría humana y los trabajos de migración enumerados arriba. No se modificó el Figma fuente.
