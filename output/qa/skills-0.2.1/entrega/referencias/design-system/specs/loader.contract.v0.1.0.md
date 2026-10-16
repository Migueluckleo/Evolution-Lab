---
contract_schema: sdd-project/0.2
contract_id: LOADER-001
name: Loader
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-25
review_targets: [figma]
figma_page_name: Loaders
sources: [SRC-FIGMA-LOADER-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-MIGRATION-NEAREST-PRIMITIVE-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/loader.source.component-contract.yaml]
dependencies: [FOUNDATIONS-TOKENS-001]
user_audit: PENDING
---

# Loader 0.1.0 · contrato de construcción

## 1. Purpose

Indicar actividad de carga indeterminada mediante un anillo circular animado. No expresa porcentaje. La página semántica del destino se llama Loaders y contendrá la familia Loader; no se reutiliza el archivo fuente.

## 2. Contract

Construir un set público Loader de 16 variantes y 16 secuencias internas locales de 24 fotogramas cada una, una por combinación Size×Color. La fuente solo tiene cuatro secuencias Primary y overrides cromáticos en el primer fotograma de los otros colores; el destino corrige ese salto de color sin cambiar la paleta. La reconstrucción toma como baseline la [observación fuente](../drafts/contracts/loader.source.component-contract.md) y su [YAML](../drafts/contracts/loader.source.component-contract.yaml). Este contrato cubre Figma, no una implementación web. Los IDs fuente y destino se mantienen separados.

## 3. Anatomy

Cada variante pública instancia el primer fotograma de su combinación Size×Color. Cada fotograma interno contiene un anillo hueco con gradiente angular y un remate. El origen lo construye con Subtract y remate vectorial; el destino puede usar un arco elíptico y remate de igual apariencia para mantener geometría editable. Se prohíbe convertir los 24 fotogramas en 24 opciones públicas de una propiedad.

## 4. Properties

Usar Size={Sm,Md,Lg,Xl} y Color={Primary,Secondary,Default,On color}, con defaults Sm y Primary. Size corrige el error de capitalización SIze de la fuente; la corrección es solo de nombre, sin alterar valores. No hay propiedad de porcentaje, texto ni estado Disabled.

## 5. Variants

El producto de cuatro tamaños por cuatro colores contiene exactamente 16 variantes públicas. Cada combinación usa la secuencia local del tamaño correspondiente y el mismo rol semántico para el stop opaco y el remate.

## 6. Sizes

Sm 24×24 px, Md 40×40 px, Lg 64×64 px y Xl 88×88 px. El anillo escala con su set de origen; conservar la silueta circular y la relación entre grosor y diámetro observadas.

## 7. States

No hay eje State en la fuente. Primary, Secondary, Default y On color son contextos cromáticos, no estados interactivos. No añadir Hover, Focus, Disabled ni Success por inferencia.

## 8. Behavior

Cada secuencia interna recorre 24 fotogramas con paso angular de -15 grados y vuelve al primero. Trigger AFTER_TIMEOUT de 0.001 s, acción CHANGE_TO, transición SMART_ANIMATE lineal de 0.05 s. Todos los fotogramas de una secuencia conservan el mismo rol Color: ningún paso vuelve a Primary por accidente. No añadir transiciones al set público ni comportamiento de cálculo de progreso.

## 9. Accessibility

La fuente no define etiqueta accesible ni reduced motion. En este artefacto Figma no afirmar soporte de lector de pantalla o de preferencias del sistema. Una implementación de producto deberá definir ambos antes de publicar el componente de código; esa ausencia no bloquea la reconstrucción visual de Figma.

## 10. Design tokens

Fuente canónica para nombres, aliases, cuatro modos, valores, scopes y única description: sources/inventories/tokens.inventory.json, SHA-256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474. Las variables de destino existentes se verificaron en la colección semantic con modos Contable, Administrativo, Servicios y Personas. Ningún color visible debe ligarse directamente a una primitiva.

| Color | Fuente observada en Contable | Rol semántico destino | Variable local | Scope |
|---|---|---|---|---|
| Primary | #3255F7 | color/icon/brand | VariableID:13:25 | SHAPE_FILL |
| Secondary | #64748B | color/icon/secondary | VariableID:13:21 | SHAPE_FILL |
| Default | #0F172A | color/icon/primary | VariableID:13:20 | SHAPE_FILL |
| On color | #FFFFFF | color/icon/on-brand | VariableID:13:23 | SHAPE_FILL |

El rol brand cambia de alias primitivo entre los cuatro temas; los otros tres roles conservan su semántica de icono. En cada uno de los 384 fotogramas, vincular tanto el stop opaco del gradiente como el remate al rol correspondiente y verificar la persistencia del binding. Los stops transparentes se mantienen transparentes, no se les asigna un color de producto. Si el binding del stop no persiste por limitación de API, detener esa parte y registrar brecha; no dejar un literal que se presente como temático. No se requieren nuevos tokens ni modificaciones al JSON.

## 11. Content rules

No hay texto visible ni propiedades de contenido. El Loader es indeterminado: no mostrar porcentaje o tiempo estimado.

## 12. Composition rules

Las 16 secuencias internas viven en la página Loaders como dependencias locales y no se publican como familias independientes. El set público solo usa instancias locales del mismo archivo, sin importar Loader desde la Librería anterior.

## 13. Responsive behavior

No hay breakpoints observados. Los cuatro tamaños son discretos; no inferir escalado fluido.

## 14. Edge cases

On color es blanco y necesita un contexto de muestra contrastante para inspección; el componente mismo no añade fondo. El alias brand varía por tema: comprobar los cuatro modos, no solo Contable.

## 15. Forbidden combinations

No se añaden combinaciones fuera de cuatro tamaños por cuatro colores. Los 24 fotogramas no se exponen como opciones públicas ni se mezclan entre tamaños.

## 16. Design ↔ Code mapping

Size y Color son propiedades de Figma. La API web, el ciclo de vida de carga y la accesibilidad de código quedan fuera de alcance; no se promete equivalencia uno a uno.

## 17. Acceptance criteria

- AC-LD-001: página Loaders y set público de 16 variantes con tamaños exactos 24, 40, 64 y 88 px.
- AC-LD-002: 16 secuencias internas de 24 fotogramas, 384 transiciones secuenciales, cierre de ciclo, paso de -15 grados y color constante durante cada ciclo.
- AC-LD-003: 384 stops opacos y 384 remates vinculados al rol semántico del color, con scopes correctos y cero primitivas usadas directamente en paints visibles.
- AC-LD-004: los aliases de los cuatro modos coinciden con el JSON y los roles se resuelven en Figma; Primary cambia con el tema.
- AC-LD-005: comparación visual fuente/destino, IDs separados, QA técnico registrado, auditoría humana PENDING y estado de biblioteca explícito.

## 18. Examples

Sm/Primary ilustra el caso predeterminado; Xl/On color ilustra el mayor diámetro y la necesidad de un fondo de muestra externo. No son componentes adicionales.

## 19. Source of truth

Este Markdown gobierna las reglas de Loader. El JSON aprobado gobierna los datos de variables delegados. La observación fuente conserva lo histórico; el Figma destino es la implementación, no la autoridad para corregir el contrato por su mera existencia.

## 20. Change management

Cualquier cambio de colores, tamaños, movimiento, aliases o semántica exige enmienda trazable y QA afectado. La delegación permite construir y validar técnicamente sin aprobación previa por componente, pero no equivale a aprobación humana final.

## 21. Changelog

- 0.1.0, 2026-09-25: baseline de construcción a partir de 16 variantes y 96 fotogramas observados; se normaliza Size, se exige binding temático y se corrige la pérdida de color con 384 fotogramas de destino.
---
