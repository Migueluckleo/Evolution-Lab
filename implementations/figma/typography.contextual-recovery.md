# Recuperación contextual de 66 etiquetas Button

Estado de este documento: **PREPARADOR LOCAL; no acredita escrituras ni validación de Figma**.

La aplicación del estilo del Button principal propagó su tracking de `0.1%` a consumidores que tenían tracking normal. Los intentos ordinarios detectaron el desajuste y no escribieron. La recuperación conserva las recetas originales del catálogo/mapping 0.1.1; no crea estilos ni redefine contratos.

| Página | Etiquetas | Evidencia de preflight sin escrituras |
|---|---:|---|
| Input Fields `394:122` | 6 FileUpload | [Resultado](../../qa/implementations/typography/consumption-v0.1.1/apply.394-122.1.range-indexed.json) |
| Modal `565:122` | 36 | [Resultado](../../qa/implementations/typography/consumption-v0.1.1/apply.565-122.whole-page.detail.json) |
| Empty States `639:128` | 16 | [Resultado](../../qa/implementations/typography/consumption-v0.1.1/apply.639-128.whole-page.detail.json) |
| Conversation `765:6` | 8 | [Resultado](../../qa/implementations/typography/consumption-v0.1.1/apply.765-6.whole-page.detail.json) |

El preparador [typography_contextual_recovery.py](typography_contextual_recovery.py) utiliza el guard completo de página fijado por SHA. No añade excepciones al template ordinario. Obtiene los IDs explícitos de esos cuatro reportes, comprueba sus cantidades y los vincula al mapping canónico. Los consumidores deben ser instancias UI sin escala y con un solo rango. La referencia de receta principal corresponde a un texto directo de Buttons presente en el mismo mapping; en ejecución se exige el ID real de ese estilo y todas sus métricas. No se acepta una identidad supuesta solo por el sufijo del nodo.

Solo se permiten estas tres transformaciones, manteniendo familia, peso, tamaño, interlineado y decoración:

| Origen heredado | Destino contextual | Cantidad |
|---|---|---:|
| `ui-action-label-small` | `ui-label-compact-bold` | 14 |
| `ui-action-label-medium` | `ui-action-label-normal` | 44 |
| `ui-action-label-medium-underline` | `ui-action-label-normal-underline` | 8 |

Las tres restauran tracking `0.1%` → `0px`. También se admite un nodo ya restaurado con ID y métricas exactas de destino, para que un reintento sea idempotente. Todos los demás textos, incluidos los editoriales, conservan exactamente sus recetas, enlaces, contenido y bindings. El guard conserva la lectura y comparación de todos los nodos, relaciones reales de instancias, geometría, layout, propiedades públicas y definiciones de componentes.

La única excepción geométrica es `I420:299;26:104`, cuyo ancho original de `121×20` está en el censo. La [lectura actual](../../qa/implementations/typography/consumption-v0.1.1/file-upload.contextual-geometry.json) registra `122×20`. Una [prueba en copia](../../qa/implementations/typography/consumption-v0.1.1/file-upload.geometry-probe.json), posteriormente [eliminada](../../qa/implementations/typography/consumption-v0.1.1/file-upload.geometry-probe.cleanup.json), observa únicamente estas restauraciones al aplicar el estilo contextual:

| Campo | Antes | Después esperado |
|---|---|---|
| `x` | 8 | 9 |
| `width` | 122 | 121 |
| `relativeTransform` | traslación X 8 | traslación X 9 |
| `absoluteTransform` | traslación X 857 | traslación X 858 |
| `absoluteBoundingBox` | X 857, ancho 122 | X 858, ancho 121 |

Las coordenadas absolutas trasladan al original el delta observado en la copia. Los restantes valores de cada matriz/caja permanecen exactos. El Button sigue en `154×32`; Dropzone y Success no cambian. No se deduce que HUG deba reducir el Button: la prueba observada determina este caso. `absoluteRenderBounds` sigue en `null`.

El ledger contiene tuplas completas `before`/`after`, no tolerancias. Cada entrada tiene archivos de evidencia existentes, hash SHA256 y localizador. El preparador admite una única fila geométrica para esa etiqueta. Durante la ejecución, el estado leído debe coincidir exactamente con la tupla previa o la ya restaurada, y el final con la restaurada. Cualquier otro campo o nodo permanece inmutable. El preparador verifica los hashes; no convierte una observación en aprobación normativa.

El ledger JSON usa `schema_version:1`, `pageId:"394:122"`, `ids` con las seis identidades FileUpload en orden fijo, `geometry:[{id,fields:{campo:{before,after}}}]` y `evidence:[{path,sha256,locator}]`.

```bash
python3 implementations/figma/typography_contextual_recovery.py \
  --ledger /tmp/typography-contextual-ledger.json \
  --output /tmp/typography-contextual-calls
node tests/test_typography_contextual_recovery.mjs
node tests/test_typography_page_guard.mjs /tmp/typography-contextual-calls
```

La salida consta de cuatro scripts, `explicit-allowlist.json` con las 66 identidades y fuentes, y un manifiesto con tamaños y hashes. Cada script ejecuta únicamente setters de estilo por rango, secuenciales. No contiene setters de métricas, geometría, decoración ni propiedades. Después del último setter vuelve a leer la página completa, incluso si falla un setter, y comprueba las dimensiones y el hash de preservación originales de las etiquetas. Usa una consulta nueva de nodos para evitar proxies de instancia invalidados durante la segunda lectura. Un fallo en las comprobaciones posteriores conserva el listado de mutaciones y se reporta como error. Ambos TextStyles deben conservar definiciones y bindings intactos.

La comprobación independiente global posterior sigue siendo obligatoria: `PASS_PAGE_GUARD_GLOBAL_READBACK_REQUIRED` no equivale a validación global. Los reportes históricos de fallos permanecen intactos. Si el guard detecta diferencias, `recipeDiffs` y `geometryDiffs` muestran los campos antes/después de hasta diez nodos; los valores internados se decodifican y las omisiones por presupuesto se declaran expresamente. Estas observaciones no añaden excepciones de aceptación para ink bounds, layout ni otros campos.

Las 25 pruebas de recuperación local cubren corrección exacta, reintento sin escrituras, rechazo previo de otro estilo/tracking/contenido/caja/alias y detección posterior de alteraciones fuera del ledger, incluidas API, color, texto editorial, estilos compartidos y cambios geométricos mínimos. Incluyen bindings nodales de fills, que deben conservarse y no se confunden con bindings del TextStyle. Las 33 pruebas del guard ordinario cubren también rematerialización de nodos, conservación del reporte ante fallos posteriores y equivalencia exacta del tracking cero PIXELS/PERCENT documentada por el mapping; no aceptan valores no cero ni epsilon. Son pruebas con objetos simulados y de parseo/hash de los scripts; no acreditan una ejecución en Figma.
