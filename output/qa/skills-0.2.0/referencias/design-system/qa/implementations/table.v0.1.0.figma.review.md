# QA-TABLE-FIGMA-001

2026-10-01 · PASS técnico acotado. DELEGATED_FOR_BUILD; auditoría humana PENDING; biblioteca no publicada.

## Evidencia

[Contrato](../../specs/table.contract.v0.1.0.md), [Slots](table.v0.1.0.slots.json), [pruebas adicionales](table.v0.1.0.slots-final.json), [paint readback](table.v0.1.0.paint-readback.json), [validación canónica](table.v0.1.0.canonical-check.json) y [temas/primitivas](table.v0.1.0.theme-readback.json).

- Siete mains públicos en seis unidades funcionales: Table, Header, Header Cell, Cell, Actions Cell y dos variantes Row. Tres helpers privados: Sort, Copy y Product Action. Página546:122, Table548:895.
- Slots:19cardinalidades, reordenamiento, retención de contenido Default↔Hover y dos geometrías:23checksPASS. Cuatro comprobaciones adicionales de reordenamiento/restauración y visibilidadPASS. Total27.320pxesUNSUPPORTED, no PASSresponsive.
- Auditoría de1368nodos a través de mains y composiciones, incluyendo ocultos:899/899paints con token semántico local;0errores de scope/localidad/primitiva directa.31instancias de logo exentas por política agnóstica, no deuda de tokenización.
-36tokens/144aliases por modo y valores de primitivas coinciden con inventario aprobado y extensiones Control0.1.1/Dot0.1.0. Cero variables nuevas. Colores de marca comprobados en los cuatro modos.
- Geometría:Table1279.9998×412;Header1279.9998×52;RowDefault1279.9998×36;Hover1287.9998×36. La fracción<0.001px es la observada en fuente.
- Captura inline final revisada después de corregir bordes; coincide en medidas/columnas/truncado, salvo negro→neutral900 documentado. Capturas de selección/acciones, logo/sort y Badge/copy revisadas. No se guardaron URLs efímeras como evidencia permanente.

## Reparaciones

Los IDs remotos importados no persistieron entre llamadas: se resuelven por key en la misma ejecución. Readback tras primer error confirmó que Stage2 no dejó objetos. Segundo error: no puede exponerse isExposedInstance dentro deSlots; se mantienen editables directamente. La herramienta reportó reintento seguro.
El valor por defecto strokesIncludedInLayout=true sumaba2px al Header y1porfila. Fuente verificadafalse; corrección aplicada aTable/Header/Rows/celdas, seguida de readback y captura.
El icono Circle de Badge en Table quedó sin binding por usar el nombre inexistente success/icon. Se corrigió a color/feedback/positive/icon13:44 existente; el readback posterior cuenta899paints correctos. Se reveló temporalmente el Badge y se restaurófalse para acceder al vector; no se modificóBadgeglobal.

## Límites conservados

TABLE-AUD-001:Hover+8px y desplazamiento original; no se acredita alineación sin salto. Cardinalidad variable requiere coordinar anchosHeader/Rows. No responsive móvil ni sort/selección/copy/navegación funcionales.
Negro#000→#0F172A por primitiva existente vía roles text/icon. Texto17.853sobreblanco/16.097cabeceraazul/15.974violeta/16.296Hover. DivisorE2E8F0sobreblanco1.233:1*; iconoServiciossobreblanco3.236:1. Sin WCAGglobal.
El modelo fuente conserva PARTIAL_DEPENDENCY_METADATA (paths muestreados, no todos los overrides archivados);1449nodos y456instancias/15keys sí recorridos. No se simula extracción completa de otras bibliotecas.
GraphifySTALE_AFTER_TABLE_DELTA, no regenerado. Fuentes, JSONbase y mains locales externos intactos.

