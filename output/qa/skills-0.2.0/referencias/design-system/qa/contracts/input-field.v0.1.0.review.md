# Input Field · P0–P2 y QA documental 0.1.0
Fecha: 2026-09-28. Resultado: PASS documental. En la primera revisión, implementación NOT_STARTED; ahora concluida con [QA técnico PASS](../implementations/input-field.v0.1.0.figma.review.md). Auditoría humana PENDING.

## P0 · descubrimiento
- P0.a: página fuente 20:3, cuatro sets/52 variantes preliminares. Alcance inmediato set 186:14461 (Input Field): 30 variantes y 493 nodos leídos, incluidos 60 ocultos. Search/Textarea/File Upload quedan pendientes.
- P0.b: destino leído: 20 páginas, ninguna Input Fields; dos colecciones locales semantic/primitive.
- P0.c: dependencias Question/Eye Outline/Light identificadas. Búsqueda de librería completada; no importar Input Field legado. Question publicado actual usa key distinta, se registra sustitución.
- P0.d: nombre Input Fields adoptado bajo delegación por su función de captura, no color/estado. Contrato de 21 secciones; 30 combinaciones observadas y 12 propiedades.
- P0.e: gaps no bloqueantes: interacción web desconocida, procedencia remota parcial, normalización tipográfica y aproximación halo #F8FAFC→#FFFFFF. No se ocultan.
- P0.f: contrato fuente MD/YAML y snapshots persistentes. YAML parseado por Ruby; invariantes 30 variantes/60 instancias/36 variables PASS. Corrección editorial del MD: 29 variables locales y 7 remotas.

## P1/P2 · foundations
No creación ni modificación de variables. Inventario base SHA-256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474; extensión de efectos 0baef3e14a121d3284c04d28bd8bf2cc66a940270f3486994a23e3456d7fc3d4.
Preflight colores: 26 roles disponibles × cuatro modos comparados con JSON, todos valores/scopes PASS; solo el subconjunto indicado en contrato será consumido.
33 roles necesarios con IDs, scopes y aliases por identidad lógica en input-field.target-aliases.preflight.json. Tipografía Manrope Regular/Bold disponible; se carga antes de cada escritura.
La geometría de efectos no tiene categoría tokenizada: literal observado, color EFFECT_COLOR obligatorio. Dimensiones de control observadas no se ligan a GAP.
No se crea página Foundations ni se modifica ningún componente existente.

## QA documental
- DOC: 21 secciones, fuente file/node, destino explícito, tokens por rol/estado, dependencias y criterios AC-IF-001..006.
- Matriz: Size×State×Value=30; autoFocus fuente correlacionado se elimina, sin perder variante.
- Paleta fuente conservada salvo halo blanco aproximado declarado. Focus de cuatro px en dos variantes se conserva; propuesta inicial de unificarlo fue descartada antes de escribir.
- Tracking y line-height normalizados a tokens aprobados, registrados para auditoría; prefijo Small mejora 12→16 de interlineado.
- Datos de comportamiento desconocidos no se inventan. No se crea contrato web.
- DRAFT revisado: digest d8fef8ab7b0d6c8d90fa37d9cf029f27e968a66eac3cc11f73198f5bd9f69fa1. Este PASS habilita DELEGATED_FOR_BUILD, no APPROVED.
- P04 readiness: READY para CREATE en AI Design System. Importación de iconos requiere comprobar la variante real antes de instanciar.
- Graphify: STALE para estos nuevos documentos; no regenerado. No hubo cambios de código de producto ni instalaciones.

## Revalidación previa a promoción
La corrección de foco conserva seis soportes decorativos equivalentes a la fuente. REQ-IF-007 y Anatomy se actualizaron antes de escribirlos. Fondo background/default y efecto EFFECT_COLOR existente; no crea roles ni cambia paleta. QA documental afectado PASS; captura posterior confirma el contorno.

P3.a–P3.f y P4 completos para Input Field, no para Search/Textarea/File Upload. 33 roles / 132 aliases comparados con JSON sin diferencias. [Contrato vigente](../../specs/input-field.contract.v0.1.0.md) promovido a specs; no queda copia normativa editable en drafts. El digest inicial anterior identifica el candidato previo, no la versión final.
