---
contract_id: FOUNDATIONS-EMPTY-STATES-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
---
# Foundations · roles de Empty states

Extensión limitada a seis roles nuevos del [JSON canónico de destino](../drafts/foundations/ai-design-system.empty-states.v0.1.0.json). DEC-SEMANTIC-EXTENSIONS-001 y DEC-MIGRATION-NEAREST-PRIMITIVE-001 autorizan aliases a primitivas existentes, no colores nuevos. Inventario histórico SHA256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474, sin modificación.

El JSON gobierna nombre, tipo, cuatro modos, aliases, scopes y única description. Código WEB no definido: codeSyntax vacío, no se inventan nombres CSS. Los IDs destino de este JSON son localizadores derivados verificados en preflight, nunca sustituyen IDs del inventario.

REQ-FES-01 MUST crear/reutilizar exclusivamente esos seis roles y verificar todos sus campos y 24 aliases antes de consumidores. REQ-FES-02 MUST separar fill de trazo y no aplicar text a ilustraciones. REQ-FES-03 MUST conservar colores de controles con marca por modo. Los motivos son decoración, no estados de feedback ni colores de marca.

Aproximación reproducible: distancia euclídea OKLab sobre sRGB lineal de todas las primitivas COLOR locales corroboradas en JSON. Se elige mínimo, sin nuevas primitivas. Tabla y alternativas en [evidencia](../sources/figma-snapshots/empty-states.v0.1.0.color-approximation.json). Las máscaras geométricas no son pinturas visibles; se conserva como geometría observada, fuera de la paleta decorativa y sin usarlo en consumidores de UI.

QA de datos: nombres únicos, seis roles COLOR, scopes explícitos, 24 aliases existentes y de tipo COLOR. Human audit PENDING; esta delegación no publica biblioteca.
