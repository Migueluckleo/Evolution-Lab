# QA técnico Figma · Dropdown Item 0.1.0

Fecha: 2026-09-28. Resultado **PASS técnico** para REQ-DI-001–009. No es aprobación humana ni certificación WCAG.

## Alcance y evidencia

- Página Select `444:122`; set Dropdown Item `446:528`. Guía `445:122`; ejemplos `448:312`; texto largo `448:569`.
- [Readback](dropdown-item.v0.1.0.readback.json): 18 variantes con dimensiones 251×48/40/32, nombres únicos y ejes válidos; 180 conexiones de las 10 propiedades; 72 instancias directas de dependencias y 93 al contar sus internas.
- 186 pinturas SOLID auditadas, incluidas capas ocultas: cero bindings ausentes, remotos, primitivos directos, fuera de scope o desalineados con el valor resuelto.
- [Integración](dropdown-item.v0.1.0.integration.json): doce instancias con seis opciones activadas, distribuidas entre cuatro modos, más texto largo. Todas conservan geometría y truncado, sin ancho negativo. Las dos propiedades INSTANCE_SWAP cambiaron realmente Eye↔X conservando color/icon/primary.
- [Mapa de variables](../../sources/figma-snapshots/select.target-tokens.v0.1.0.json) cotejado por `qa/contracts/validate-select-tokens.cjs`: 24 roles ×4 modos=96 comprobaciones, PASS; JSON canónico sin cambio.
- Checkbox y Loader son dependencias locales; sus mains no se modificaron. Los iconos son instancias Phosphor, no redibujos ni detach. Los ciclos de Loader se heredan, no se revalidan como nueva implementación de animación.
- No se añadieron variables, estilos ni primitivas. Sin Code Connect ni frontend.

## Comparación visual y corrección

La primera captura detectó 24 pinturas textuales cuyo valor de respaldo era blanco aunque el binding primary resolvía el gris oscuro correcto. Se corrigieron los valores de pintura desde el valor resuelto del mismo token, manteniendo todos los bindings. El readback posterior comprobó igualdad real entre color y variable; la segunda captura del set mostró texto, foco, selección y tamaños correctos.
La captura de integración de los cuatro modos mostró opciones visibles alineadas y tema coherente. Después del swap de prueba se inspeccionó solo la instancia modificada; el texto largo también se verificó renderizado y truncado. No se repitieron capturas de maestros sin cambios.

Normalizaciones ya delegadas en contrato: AUTO22/19→24/20 de interlineado; segunda columna sin recorte; checkbox seleccionado/deshabilitado coherente; roles de icon/text correctos; divisor como trazo; swap derecho. Colores Contable preservados. No se afirma igualdad tipográfica literal con la fuente.

## Contraste y limitaciones *

Cálculo desde pinturas actuales y sus valores resueltos, luminancia sRGB; ratios redondeados a dos decimales:

| Par | Contable | Administrativo | Servicios | Personas |
|---|---:|---:|---:|---:|
| Texto Default / blanco | 17.85 | 17.85 | 17.85 | 17.85 |
| Texto Selected / surface/brand | 5.01 | 5.63 | 3.05* | 5.66 |
| Texto Disabled / blanco | 2.56* | 2.56* | 2.56* | 2.56* |

Servicios Selected requiere revisión de legibilidad. Disabled se evalúa en contexto como control inactivo: no se declara incumplimiento automático. Alturas Medium40 y Small32 requieren evaluar tamaño táctil en producto. No cambiar colores por estas mediciones; asteriscos solo documentales.

## Cierre

Implementación VALIDATED para este contrato visual, con limitaciones conocidas documentadas. Contrato DELEGATED_FOR_BUILD; auditoría humana PENDING; biblioteca Figma UNPUBLISHED. Se autoriza promoción documental a specs por la decisión vigente de migración. Las composiciones Select abierta/cerrada permanecen fuera de este alcance y pendientes; no declarar la familia entera completa. Graphify STALE sin regenerar.

