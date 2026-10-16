---
contract_schema: figma-component-contract/0.1.0
status: OBSERVED
source_file_key: 9zs5RMR8LB5wHjW9Bd59BA
source_node_id: "2461:651"
read_only: true
---

# Navigation · Switch Tab Item · evidencia de origen

Fuente: [Tab item](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2461-651), página Navigation `268:20245`. Inspección de solo lectura el 2026-09-24; [YAML sincronizado](navigation-switch-tab-item.source.component-contract.yaml). La nota de la página describe navegación entre secciones sin recarga, pero no define semántica web.

## 1. Component Identity

**Observed from Figma:** `COMPONENT_SET` `Tab item`, ID `2461:651`, key `44cd079b3bb28629bd1fdcb794dcffc89ee81a2a`. Contiene tres variantes `State=Active/Default/Disabled`; descripción del set vacía. Recorrido completo: 25 nodos, tres hijos invisibles, nueve instancias, 21 variables usadas al incluir descendientes de instancias, cero estilos nombrados y cero reacciones. Captura del bloque `2461:634` inspeccionada.

## 2. Anatomy

**Observed from Figma:** cada variante es un auto layout horizontal con cuatro hijos directos en este orden: icono izquierdo AddressBook oculto; texto `Tab title`; Dot numérico visible; icono derecho AddressBook visible. Los dos iconos miden 14×14; Dot mide 12×12. Los vectores internos de AddressBook se agregan a la dependencia, no a la anatomía funcional.

## 3. Dependencies

**Observed from Figma:** seis instancias AddressBook Outline/Light, key `ba5343589d88e1f18b0ed731cebcb3ec41138ebb`, definición remota identificada pero parcialmente resuelta; tres instancias locales Dot `type=number, size=middle`, key `06df8e9033e095bd1ca776691d73501daf5fdda9`, con contrato local existente. No se enumeraron los 1,512 posibles valores de swap de cada propiedad.

## 4. Properties

**Observed from Figma:** `State` es VARIANT, default `Active`. `show left icon` BOOLEAN default false, `Show Badge` BOOLEAN default true, `show right icon` BOOLEAN default true; `left icon` y `right icon` son INSTANCE_SWAP con AddressBook como valor activo. El texto `Tab title` **no** tiene propiedad TEXT en el set; es contenido observado, no regla de microcopy.

## 5. Variants

| Estado fuente | ID | Tamaño | Texto |
|---|---|---:|---|
| Active | `2461:660` | 120×38 | Manrope Bold 14 |
| Default | `2461:656` | 116×38 | Manrope Regular 14 |
| Disabled | `2461:652` | 116×38 | Manrope Regular 14 |

## 6. States

**Observed from Figma:** Active tiene fondo acento; Default no tiene fill de contenedor visible; Disabled usa texto/icono neutral/400. No se observan Hover, Focus ni Press en este set. Disabled es solo variante visual observada: no demuestra bloqueo funcional.

## 7. Layout

**Observed from Figma:** HORIZONTAL, gap 8, padding superior/inferior 8, izquierdo/derecho 12, radio 8, altura 38. La anchura varía con el peso de la etiqueta; no se infiere comportamiento responsive.

## 8. Visual Styles

**Observed from Figma:** Active usa `color/interactive/accent/default` en fill del frame, que resuelve morado/400 `#A146FB` en Contable/Servicios y azul/400 `#3255F7` en Administrativo/Personas. Texto e icono Active son blancos mediante roles `color/text/on-brand` y `color/icon/on-brand`. Default usa `color/text/primary` y `color/icon/primary` neutral/900 `#0F172A`. Disabled usa `color/text/disabled` y `color/icon/disabled` neutral/400 `#94A3B8`. El Dot numérico anidado conserva rojo/600, borde y cifra blancos.

## 9. Typography

**Observed from Figma:** etiqueta Manrope 14; Active Bold, otros Regular; line-height 160% (22.4 px) y tracking −2% (−0.28 px). El número `1` del Dot es Manrope Bold 8. Familia/peso están tokenizados en la fuente; el valor literal de 160% y −2% no se debe atribuir a un token de destino inexistente.

## 10. Tokens

**Observed from Figma:** 21 variables distintas en el subárbol completo: nueve roles cromáticos/typography locales de etiqueta y Dot, más variables de geometría de los iconos y Dot, incluidos cinco remotos. El YAML conserva IDs y nombres; valores de origen y bindings de destino no son la misma identidad. El inventario JSON aprobado del destino gobierna la traducción.

## 11. Content

**Observed from Figma:** `Tab title` y `1` son ejemplos. **Requires definition:** etiqueta real, cantidad del badge y tratamiento de desbordamiento del grupo.

## 12. Interactions

**Observed from Figma:** cero reacciones en las tres variantes. **Requires definition:** clic, selección exclusiva, teclado y navegación real.

## 13. Accessibility

**Requires definition:** rol tab, nombre accesible, foco, estado seleccionado programático, área de activación y contrastes por contexto. El set no prueba conformidad WCAG.

## 14. External Dependencies

AddressBook es componente remoto de biblioteca no identificada por la API; nombre de biblioteca, archivo y versión: `NOT_EXPOSED_BY_FIGMA_MCP`. La key y variante activa sí se conocen, pero no su definición completa. El Dot es local a la Librería anterior.

## 15. Unresolved Information

El set no define estados Hover/Focus, propiedad TEXT ni interacción. No inventar esas combinaciones como variantes fuente. El comportamiento del `Switch Tab` compuesto `2461:1740` se documenta aparte; no se infiere a partir de este item.

## 16. Implementation Notes

La reconstrucción puede reutilizar el Dot numérico local del destino y resolver AddressBook como instancia; un rol de fondo exclusivo debe conservar el color acento sin usar un token de text o icon para el frame. Esto es una restricción de migración, no modificación de la fuente.

## 17. Evidence / Confidence

`E001` identidad/set/propiedades; `E002` 25 nodos y nueve instancias; `E003` tres variantes y geometría; `E004` paints, tipografía y 21 bindings; `E005` definiciones activas AddressBook/Dot; `E006` captura de contexto. Confianza `HIGH` para la anatomía observada; comportamiento y accesibilidad requieren definición externa.
