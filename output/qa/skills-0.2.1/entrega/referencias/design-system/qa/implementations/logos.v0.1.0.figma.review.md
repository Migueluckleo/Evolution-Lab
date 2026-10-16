# Logos · QA de implementación parcial 0.1.0

- Fecha: 2026-09-28.
- Contrato: [LOGOS-001](../../drafts/contracts/logos.contract.v0.1.0.md), SHA-256 `088b7e86d695541b4587b891a658a2d50e1843e9bb0e98a1ef0cdfc340bf4f56`.
- Resultado global: **PENDING / no VALIDATED**. QA documental PASS no equivale a cierre Figma.
- Estado documental DELEGATED_FOR_BUILD; auditoría humana PENDING; biblioteca UNPUBLISHED.
- Página de destino: [Logos 427:122](https://www.figma.com/design/tj3WIBEZDGLVs7MJWKCwgf/AI-Design-System?node-id=427-122).
- Evidencia: [lectura parcial y deltas](logos.v0.1.0.partial-readback.json), [propiedades y dependencias](logos.v0.1.0.properties-readback.json), [baseline fuente](../../sources/figma-snapshots/logos.fidelity-baseline.v0.1.0.json).

## Comprobaciones terminadas

1. Copia nativa mediante importación por key y clone: seis sets locales y 72 variantes; 2,967 nodos de artwork. Conteos y orden interno iguales a fuente. Los 12 frames sueltos (32 nodos) no se han copiado.
2. Propiedades, opciones y defaults de los seis sets: coincidencia exacta por lectura posterior.
3. Las cuatro instancias de logo-categoria devuelven getMainComponentAsync local, remote=false: 434:3606, 434:1472, 434:4970, 434:4484.
4. Cero bindings de variables en los seis subtrees y página. No se crearon tokens, primitivas, colecciones ni estilos.
5. Firmas por campo coinciden para nombres, tipos, visibilidad, fills, strokes, gradientes, efectos, imágenes, paths y vectorNetwork, constraints, layout, exportSettings y reacciones. Las diferencias se limitan a width, height y relativeTransform según set.
6. Capturas renderizadas inspeccionadas: administrativos, contables, personas, servicios, corporativo y categorías. No se detectaron logos faltantes, recortes o recoloreados en esos sets. Son capturas visuales, no una prueba de igualdad numérica absoluta.
7. Se restauraron las opciones de exportación que clone no conservó; no se cambió artwork fuente.
8. Personas coincide incluso en la firma estructural completa: cdde9566-5ca49d0c.

## Diferencias geométricas abiertas

La copia/importación reporta diferencias subpíxel en bounds de grupos, en el alto del componente VDI/isotipo y en transformaciones de grupos/descendientes de categorías. Máximo delta absoluto medido: **0.00030517578125 px**. No se introduce una tolerancia ad hoc ni se declara igualdad exacta.

En corporativo, asignar el relativeTransform fuente al grupo 429:480 desplazó sus 45 hijos en la lectura del adaptador; se revirtió esa asignación para conservar la geometría de la copia nativa. Las opciones PNG restauradas sí permanecen. El checksum vigente está en el readback, no en el ledger inicial.

REQ-LOG-002 y la igualdad dimensional de la sección 6 permanecen sin PASS completo. No escalar ni redibujar grupos para ocultar esta discrepancia. El siguiente operador debe usar la evidencia por campo, no repetir toda la ingesta.

## Bloqueo de los 12 assets sueltos

El navegador integrado muestra “Want to check out this file? Sign up or Log in” para el nodo fuente 4969:325. El conector puede leer e importar componentes publicados, pero los 12 frames no son componentes importables por key. La copia nativa por portapapeles requiere sesión de Figma en ese navegador.

No se ingresaron credenciales ni se cambió el archivo fuente. No se usa exportación SVG/raster como reemplazo silencioso de la jerarquía original. Al copiar esos assets, eliminar solo sus ocho bindings heredados en destino, conservando los fills #3255F7/#FFFFFF especificados en contrato.

## Gate pendiente

No promover a specs ni marcar VALIDATED: faltan los 12 assets, comprobar sus fills congelados y cerrar la comparación geométrica. La diferencia técnica se registra, no se convierte en aprobación humana ficticia. Graphify STALE; ninguna otra familia se modificó.

