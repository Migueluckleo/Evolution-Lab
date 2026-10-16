# Reanudación · Logos · 2026-09-28

## Instrucción posterior vigente

El usuario decidió omitir los doce assets restantes y continuar con las siguientes familias: DEC-LOGOS-REMAINDER-OMITTED-001. No retomar la copia ni solicitar login como condición para avanzar. Conservar los seis sets existentes; la familia no tiene QA global PASS. Select pasa a ser la siguiente tarea. El procedimiento de copia descrito más abajo queda histórico y fuera del alcance actual.

## Decisión vigente

El usuario pidió documentar Logos primero y copiarlos como assets agnósticos, sin variables ni tokens JSON. Confirmó continuar. Aplican DEC-LOGOS-AGNOSTIC-ASSETS-001 y LOGOS-001 v0.1.0; no se amplía esta excepción al resto del sistema.

## Trabajo conservado

- [Contrato de construcción](../drafts/contracts/logos.contract.v0.1.0.md) y proyección fuente MD/YAML generados antes de construir.
- [QA documental](../qa/contracts/logos.v0.1.0.review.md) PASS.
- [QA parcial Figma](../qa/implementations/logos.v0.1.0.figma.review.md), sin PASS global.
- Página Logos 427:122; guía 428:122.
- administrativos: 434:1398, 24 variantes.
- contables: 434:3372, 21 variantes.
- personas: 434:4376, 12 variantes.
- servicios: 434:4924, 6 variantes.
- CONTPAQi: 429:356, 5 variantes.
- logo-categoria: 435:2653, 4 variantes.
- 72 variantes / 2,967 nodos de artwork copiados, sin bindings. Propiedades y defaults exactos; cuatro dependencias de categoría locales comprobadas.
- Biblioteca no publicada, contrato todavía en drafts (no cumple gate de promoción), auditoría humana PENDING.
- [Estado e IDs](../implementations/figma/logos.v0.1.0.state.json); [readback y diferencias](../qa/implementations/logos.v0.1.0.partial-readback.json). El copy-ledger inicial es histórico, anterior a restaurar exportSettings.

## Para retomar sin duplicar

1. Conservar los seis sets existentes; no volver a importarlos ni crear otra página Logos.
2. Resolver acceso de Figma en navegador integrado para copiar los doce frames originales. Actualmente exige iniciar sesión. No modificar la librería fuente.
3. Fuente 9zs5RMR8LB5wHjW9Bd59BA / página40:93. Assets pendientes: 4969:325 logo_SSCi; 4969:327 Logo_SaCi; 4969:328 Logo_FD; 4969:326 Logo_ADD; 4969:329 logo_SSCi-bco; 4969:331 Logo_SaCi-bco; 4969:333 Logo_FD-bco; 4969:335 Logo_ADD-bco; 5390:256 Capa_1; 5656:22 icono_i; 5390:263 Capa_1; 5639:1658 logo_mifactura.
4. Copiar jerarquía nativa; retirar ocho bindings heredados solo en destino, manteniendo #3255F7/#FFFFFF. No crear tokens/primitivas.
5. Resolver/documentar las diferencias geométricas ya localizadas (máximo 0.00030517578125 px), sin relajar pruebas ni redibujar. Paths/paints/images coinciden. Personas ya tiene igualdad estructural completa.
6. QA de 72 variantes +12 assets y ausencia de bindings; promover el contrato sin modificar requisitos a specs solo cuando corresponda. Actualizar registros y matriz. No publicar la biblioteca por inferencia.

## Alcance no tocado

Select, Header, Table, Modal, Sidebar y Empty states siguen pendientes. No reconstruir Search, Textarea, File Upload o Input Field. No se regeneró Graphify ni se modificó el inventario JSON de tokens.
