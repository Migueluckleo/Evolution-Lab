# QA Figma · Textarea 0.1.0

Resultado técnico: **PASS**. Auditoría humana PENDING; biblioteca Figma UNPUBLISHED. No certifica accesibilidad web ni lógica de producto.

## Alcance y evidencia

Destino tj3WIBEZDGLVs7MJWKCwgf, Input Fields 394:122, set 419:247. Fuente 2049:37125; contrato [vigente](../../specs/textarea.contract.v0.1.0.md). [Readback completo](input-fields.followups.v0.1.0.audit.json); [estado e IDs](../../implementations/figma/textarea.v0.1.0.state.json).

4 variantes, 41 nodos (incluidas capas ocultas), 29/29 pinturas con roles semánticos locales, 0 efectos tokenizados, 80 bindings tipográficos, 32 referencias de propiedades y 4 instancias. Cero errores de binding/scope. Métricas de padding/gaps vinculadas; tamaños fijos e iconos conservan su geometría documentada.

## Geometría y QA visual

- State=Default: 305×160
- State=Focus: 305×160
- State=Disabled: 305×160
- State=Error: 305×160

Capturas fuente y destino inspeccionadas. Última captura después de excluir strokes del padding: cuatro controles160px, tipografía local20/16 y superficie108px; sin recorte.

## Pruebas funcionales del componente Figma

Texto precargado mantiene Disabled; Show helper y Show counter funcionan; ancho320, altura136 al ocultar ayuda.

Las siete instancias temporales de QA se eliminaron tras lectura; ningún principal ajeno se modificó. Input Field conserva30 variantes y su set397:152.

## Paridad y contraste

Valores de variables base comparados con el inventario JSON: cero diferencias en cuatro modos. Readback conserva aliases a primitivas, no valores literales. Extensiones existentes: foco y progress/positive; cero tokens/primitivas nuevos. Los ámbitos correctos de feedback/icon se conservan.

- Contorno normal: #94a3b8/#ffffff = 2.56:1 *.
- Texto Disabled sobre sutil: #94a3b8/#f1f5f9 = 2.34:1 *.
- Texto terciario: #64748b/#ffffff = 4.76:1.
- Success: #098300/#ffffff = 4.93:1.
- Error: #d40000/#ffffff = 5.53:1.

Los asteriscos son limitaciones para revisión contextual, no recoloración ni declaración automática de incumplimiento en Disabled. Search Small32px no constituye por sí solo objetivo táctil44px. File Upload Success conserva formatos10px de la fuente. No se implementaron teclado, búsqueda, contador, validación ni cargas.

## Cierre

QA técnico permite promoción documental a specs bajo delegación; cualquier ajuste posterior se hace allí. No se publicó biblioteca. Graphify STALE, sin regenerar.

