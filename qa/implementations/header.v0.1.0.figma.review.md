# QA-HEADER-FIGMA-001 · 2026-10-01

**PASS técnico acotado**, no conformidad WCAG ni aprobación humana. Contrato [HEADER-001](../../specs/header.contract.v0.1.0.md). Auditoría PENDING; biblioteca UNPUBLISHED.

## Evidencia y cobertura
- Fuente110/110nodos,25instancias,16mains y35variables; no estilos nombrados en el recorrido. [Fuente MD](../../drafts/contracts/header.source.component-contract.md) y YAML sincronizado.
- Página518:122; componente518:123; Slot518:124; helper privado de caret521:124. [Build](../../implementations/figma/header.v0.1.0.build.json).
- [Readback final](header.v0.1.0.final.json):43tokens,172comparaciones de modos; nombres,tipo,scope,description,aliases y valores iguales a sus JSON canónicos.38base +3Header +1Dot +1Avatar, con overrideServicios0.1.1. logo/categoria verificado aparte en los cuatro modos.
- [Pinturas](header.v0.1.0.paint-readback.json):268consumidores inspeccionados en main,4temas,5casosSlots ytexto largo;0errores, todos semánticos/locales conscope correcto.26paints del main incluidoslos descendientes ocultos accesibles; logos excluidos por excepción agnóstica.
- Tres roles nuevos y12aliases leídos de vuelta: [Foundations](../../implementations/figma/header.v0.1.0.foundation-readback.json). Inventario histórico SHA256sin cambio:cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474.
- Slots0/1/3/5/7, borrar,agregar,reordenar yShow actions off/on: contenido/props/orden conservados, sin detach ni violaciones. La primera muestra comparaba IDs sintéticos y dio falsos negativos; el QA definitivo compara contenido y hace readback independiente. No se oculta ese resultado inicial.
- Cuatro booleanas: grupos ocultos/leídos y restaurados en llamadas separadas. Figma invalida referencias efímeras al rematerializar grupos; no usar handles previos para QA. Initials editado aML, verificado y restaurado aJA. Avatar main tiene isExposedInstance=true.
- Company/RFC largos truncados visualmente,160×20/160×16; textAutoResizeTRUNCATE. APImaxLinesnormaliza anull; la altura contractual permite una línea.
- Capturas fuente/baseline/fourthemes/longtext inspeccionadas. GetScreenshot sobre526:255:1192×676. No guardar URL efímera. Main1143.6909×96; regiones170/296/304/136. Correcciones previas al cierre: gapVersion8, strokeexcluido de layoutCompany y radio8 del iconoCompany.
- Cuatro assets locales de logo: mismas pinturas,trazados ygeometría del main. FrameLogo175.7922 frente175.6909fuente; delta≈0.1013px documentado. No revalida Logos global.
- Caret fuente local no importable por key; se utilizó SVG exacto24px como helper privado, token color/icon/brand. [SVG](../../sources/figma-snapshots/header.company-caret.source.svg).

## Excepciones explícitas
- *Texto empresaServicios/blanco3.236:1; inicialesAvatarServicios/blanco3.236:1. Mantener paleta; revisión interna.
- *Texto blanco frente a extremo violetaA146FB4.389:1; frenteazul3255F7 5.558:1. Son pares medidos, no certificación global del gradiente.
- AUTO line-height versión y trackingempresa0.1% literales por incompatibilidad de escala/unidad; geometría literal donde no hay dimensión compatible. No tokenización integral ficticia.
- Header320px con todos los grupos no soportado; prueba negativa rotulada. ComposiciónDesktop requiere espacio o reducción de acciones. No promesaresponsiveuniversal.
- Navegación,menús,teclado,permisos y nombres accesibles de producto no definidos por la fuente y no implementados en web.

## Cierre
Promoción documental a specs bajo DELEGATED_FOR_BUILD. No cambiar colores para ocultar excepciones; no publicar biblioteca. Siguiente familia: Table, sin repetirQAglobal. Documentación/grafo: cambios Header posteriores al corte del índice; registrar desfase, no fingir CURRENT.

