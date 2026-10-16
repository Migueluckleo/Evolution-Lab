# Revisión final independiente · MD autosuficiente

Esta revisión sustituye el informe preliminar. Entrada final: `/tmp/contpaqi-offline-final-v2-20261014/entrega/replicar-en-figma.md`.

Se leyó la skill final distribuida en `output/skills/0.1.0/contpaqi-figma-screens/SKILL.md` y `references/handoff-and-qa.md`. Se consumió el bloque JSON dentro del Markdown y las fuentes del snapshot final. No se abrió ni requirió el JSON externo del handoff, HTML, carpeta de capturas ni archivos del proyecto del productor. No se llamó Figma ni se modificó código.

## Veredicto

**PASS para consumo documental del MD y compatibilidad del alcance referenciado.** Los tres hallazgos del primer fixture están resueltos en esta entrega. El bloque contiene identidad, contenido, estructura, medidas, estilos, props, estados y evidencia suficientes para preparar su reconstrucción con el DS. Esto no certifica una implementación Figma, disponibilidad de la biblioteca ni fidelidad visual total.

## Comprobaciones independientes

- Un bloque JSON parseable, `schema_version=1`, producer `contpaqi-po-prototypes`, consumer `contpaqi-figma-screens`.
- Diez instancias documentadas, una pantalla, siete estados y dos viewports1440×900/1000×760. Los14 pares de captura esperados están presentes.
-82 registros de nodo: IDs únicos por captura; parent_id existente; órdenes sin colisiones entre hermanos; ningún ciclo; identity/componentId coherentes.
- Bounding boxes numéricas finitas, visibilidad y computed_style presentes: tipografía, tamaños, padding/gap, flex/grid, posición y overflow.
- `declared_props` coincide con props/stateProps correspondiente en todos los registros. Search contiene value=PO solo en el estado filled. `evidence.observedStates` coincide con los estados realmente incluidos para cada instancia.
- Los14 conjuntos `unmapped_text` están vacíos en la evidencia embebida. Este dato es evidencia declarada del productor; la revisión no volvió a ejecutar un navegador.
- Hash de HTML del handoff y de capture coincide. Los hashes de HTML/capturas son referencias declaradas cuyos bytes no se inspeccionaron en esta prueba documental.

## Compatibilidad con el paquete final

El MD declara release0.1.0 y ds_digest `6a116f362fa0e135a019dde498261be977287b585a68401ef6b79455c1e73fb1`. El paquete Figma final0.1.0 declara `05f59b74952cf681ac81049a33c368d49e4fa16656e3dee883424f5650367443`: **los snapshots completos no se presentan como idénticos**.

Se aplicó la rama de compatibilidad por fuentes de la skill:

1. Verificador del snapshot final: PASS,1,373 archivos, cero errores.
2. Todas las14 fuentes `sources[].path/sha256` del MD se resolvieron contra `assets/design-system/` final y sus SHA-256 coincidieron.
3. El hash referenciado de `implementations/web/src/generated/tokens.manifest.json` coincidió; los32 archivos/hashes de dependencias que enumera también se comprobaron en el snapshot final, sin diferencias.
4. Contratos, enmiendas, inventario base y metadata de tokens consumidos están disponibles en la versión final. La compatibilidad verificada corresponde a ese alcance referenciado; no constituye una comparación global de los dos corpus ni una revisión de fuentes Figma en vivo.

## Hallazgos preliminares resueltos

| Hallazgo | Resultado final comprobado |
|---|---|
| F1: título y Consulta sin nodos/medidas propios | RESUELTO. `heading` y `feedback` son `kind=local-content`, identidad local, razón, parent=composition y orden propios. Heading: x32/y32,174.25×20,Manrope14px/400; feedback: x32/y268,98.984375×20 con «Consulta: vacía» y84.515625×20 con «Consulta: PO». Cada uno conserva estilos computados por estado/viewport. |
| F2: textContent incluía MXN y and link ocultos | RESUELTO. En los82 registros no aparece ninguno de los dos textos ocultos. Search contiene «Buscar», indicador y helper visible; los modales contienen título/contenido visible. La evidencia ahora distingue estos textos del contenido oculto del DS. |
| F3: Media declarado con Body Slot variable incompatible | RESUELTO. `media-modal` usa Media con Title/Content TEXT y `NOT_APPLICABLE` para Body Slot; mide580×472. `side-modal` es instancia separada SideBySide840×484 con región variable REQUIRED; Avatar/Logo/Button tienen parent=side-modal y solo aparecen en demo/side. El atajo M que alterna hacia SideBySide está declarado como decisión local de prueba, no comportamiento normativo. |

## Simulación de consumo

Prepararía las composiciones1440×900 y1000×760 con la columna principal: heading, InputField Buscar, Button Abrir detalle y feedback Consulta. Conservaría el margen exterior32 y gap24 observados. El estado filled modifica value aPO y el texto de feedback.

Abrir/Enter muestran el Media centrado con título Detalle portable y el texto «Presiona M para ver el detalle con contenido variable.». El atajo local M lleva al estado SideBySide con Avatar, logo oficial y Button Volver al medio en su Body. Cerrar/Escape devuelve a la composición principal. Las reacciones se traducirían a capacidades Figma reales; no se promete ejecución de JavaScript ni equivalencia de teclado sin comprobarlas.

Los componentes DS se resuelven contra sus contratos/enmiendas y los IDs/keys reales se obtendrían al inspeccionar la biblioteca. Heading/feedback son texto local editable, sin inventar una nueva familia. El overlay fixed se mantiene fuera del flujo de Auto Layout normal aunque su parent lógico sea composition. Los contratos y defaults del snapshot permiten resolver anatomía/assets y distinguir bindings de colores observados.

`figmaTarget=null`: en una ejecución real queda por resolver el archivo de prototipo autorizado antes de escribir. Esa decisión no requiere solicitar JSON externo, HTML ni capturas. Las omisiones `figmaProperties=null` se verifican contra las propiedades reales del componente, como indica la skill.

## Límites y observaciones no bloqueantes

- La tabla `transitions` sigue siendo agregada demo→demo. Las acciones y estados embebidos aportan detalle suficiente para el mapa básico; no se interpretan como QA de cada conexión Figma.
- La lista tokens de una instancia es un subconjunto declarado, no un override de todas sus propiedades. Se completa desde contratos/JSON canónicos, conservando scopes y aliases.
- El primer párrafo todavía menciona abrir HTML; el propio MD y la skill final aclaran expresamente que HTML/JSON externo/capturas son opcionales. En esta prueba se consumió únicamente el MD como entrada de producto.
- La correspondencia por defecto de assets se resuelve en el snapshot; no se afirma haber comparado imágenes de captura ni inspeccionado pixels de Figma.

## QA real separado

Figma real, importación, creación de archivo/pantallas, Slots nativos, lectura posterior, captura propia y comparación visual externa: **NOT_RUN**.

Los PASS de captura/file:// son evidencia declarada del productor. El PASS de este informe acredita revisión documental independiente, hashes comprobados y coherencia del handoff final. No equivale a APPROVED, publicación de biblioteca ni VALIDATED de implementación Figma.

## Fuentes embebidas comprobadas

- `drafts/contracts/avatar.contract.v0.1.0.md` · SHA-256 `465296694978a14e8019b2f52af61f42b88f78fecfa480d0081d4f877e122396`.
- `drafts/contracts/logos.contract.v0.1.0.md` · SHA-256 `088b7e86d695541b4587b891a658a2d50e1843e9bb0e98a1ef0cdfc340bf4f56`.
- `implementations/web/src/generated/tokens.manifest.json` · SHA-256 `cc511daaa507efe81d0edfac356273a4269a9af16264d7ef9d0637149be223b8`.
- `sources/inventories/tokens.inventory.json` · SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.
- `specs/components/avatar.source-color-amendment.v0.1.1.md` · SHA-256 `f1a010f1dc3f6ee85b756dc3131840d7fcfd3b6f346077bbb4fb3d445d79832d`.
- `specs/components/button-page-name.amendment.md` · SHA-256 `b2c896cab9f2f5659101253dbc93ce0410c697081e53daafecebbc5b62895fd7`.
- `specs/components/button.contract.v0.2.0.md` · SHA-256 `53e13fa8e664f70d0ce81116e850bbcb0ab7da9f14ac0f08607fa5fda09894a1`.
- `specs/components/button.local-bindings.amendment.v0.2.2.md` · SHA-256 `57b84698047da82ebfd10c18ed828a1aac43482283856d49690d379b60d2e59c`.
- `specs/components/button.semantic-scope-amendment.v0.2.1.md` · SHA-256 `8655c79ae1f13c66be04ed406815066a1f3a44d553d2b948390f6bf1b6f1dfb9`.
- `specs/components/logos.scope.amendment.v0.1.1.md` · SHA-256 `f72b740ff43d134c794fb2ad6ea596ffa36bc4f09afeae3996575b04a5fe7467`.
- `specs/components/six-family-color.amendment.v0.1.0.md` · SHA-256 `f569d5e132a0b5480f7b540dea8f157a601f27f24e86bb5ccb05b2d05f4b2cc9`.
- `specs/input-field.contract.v0.1.0.md` · SHA-256 `e01e90d9dbc4dfdfc4230aac875f8d8a7374673b0a02bbda44eabf9962403c2d`.
- `specs/input-field.disabled-text.amendment.v0.1.1.md` · SHA-256 `fc73aef18bd2c4ca6fcdd4eaa17d92c9e65aee0f4e54ff993eb9aeefc0f98a45`.
- `specs/modal.contract.v0.1.0.md` · SHA-256 `589a78693d2bad3f3d9233a8ea6ecd5e9254f1aae429aac6da941b030cc78f57`.

MD final SHA-256: `8bc47bcbb220c768d5aef85c8a1212c2d05148ec34b9f2f8f66186cfe5ab386b`.
