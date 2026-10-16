# Forward test · contpaqi-figma-screens

Evaluación independiente de instrucciones, no ejecución Figma. Entrada: crear un nuevo archivo con Cargas, Contable, 1440×900, Header, Sidebar, tres documentos, resumen cantidad/total/Continuar y detalle/volver. No se llamó Figma, no se creó archivo/pantalla real, no se modificó biblioteca ni fuentes del paquete.

## Resultado

PASS de integridad: `python3 -B scripts/verify_snapshot.py`, 1,373 archivos, cero errores, package_version 0.1.0, ds_digest `6a116f362fa0e135a019dde498261be977287b585a68401ef6b79455c1e73fb1`.

PASS de seguimiento documental: las instrucciones y recursos alcanzan para preparar el mapa, localizar contratos/estados y resolver Resumen de lote como composición local. No encontré contradicción bloqueante entre las instrucciones de la skill. La construcción real, importabilidad de componentes, disponibilidad de fuentes y Slots no se evaluaron; permanecen pendientes de herramientas reales.

## Mapa propuesto (simulado)

| ID lógico | Fuente | Configuración/decisión local | Figma real |
|---|---|---|---|
| cargas | APP-SHELL-001 0.1.0 | Frame 1440×900, tema Contable; Header96; Body804; rail104 y Content1336. Usar Content Slot. El cambio de altura es instancia desktop, no breakpoint nuevo. | Pendiente |
| cargas.header | HEADER-001 0.1.0 | Instancia existente; logo Contable, empresa/perfil de muestra; Show version=false y Show actions=false para evitar acciones sin propósito. | Pendiente |
| cargas.sidebar | SIDEBAR-001 0.1.0 | Presentation=Collapsed del shell; elemento Cargas activo en Menu items, label editable, icono importable verificado en preflight. | Pendiente |
| cargas.documents | TABLE-001 0.1.0 | Tres Row y siete Cells por fila; datos ficticios; Header/Rows coordinados, selección y Actions ocultos. Abrir detalle por reacción local de cada fila. | Pendiente |
| local.batch-summary | MetricCard + Button | Principal local de composición: MetricCard Horizontal Metric/Large, Title=Resumen de lote, etiquetas Documentos/Total, valores 3/$3,600.00, Show icon/action/detail=false; Button primary/large, texto Continuar, ambos iconos ocultos. | Pendiente |
| detail.doc-01..03 | App Shell + campos de texto + Button | Tres pantallas para los tres fixtures, título Detalle del documento y Volver a Cargas. Estado de datos definido en prototipo, sin backend. | Pendiente |
| batch-review | App Shell + resumen local + Button | Continuar lleva a una revisión local del lote, con Volver. Decisión de prototipo explícita; no confirma carga, pago ni procesamiento remoto. | Pendiente |

Los documentos de ejemplo aportan importes 1,000.00/1,200.00/1,400.00 (total3,600.00); son fixtures de UI, no una regla fiscal, moneda oficial ni algoritmo de negocio aprobado. Todas las pantallas usan textos editables. No se necesita preguntar por contenido de ejemplo ni por destino: el nuevo archivo ya está solicitado. Solo una selección de plan exigida por la herramienta oficial podría requerir intervención en la ejecución real.

## Decisiones de composición

La tarjeta exacta «Resumen de lote» no aparece en el índice. MetricCard ya cubre dos métricas; se reutiliza y se agrega el Button dentro de un anfitrión local, en lugar de dibujar una nueva familia. `kind=local-composition`, `compositionOf=[METRIC-CARD-001,BUTTON-001]`. Props locales: title, quantityLabel/value, totalLabel/value y continueLabel. `slot_applicability=NOT_APPLICABLE`: esos campos y una acción forman anatomía fija solicitada; no representan una lista extensible. La autorización del prompt permite crear el componente local sin nueva aprobación por componente.

Para conservar el ancho contractual de Table1280, propongo contenido vertical con padding24, gap24, tabla arriba y resumen debajo. Content1336 deja1288px interiores; no colocar tabla1280+tarjeta al lado ni comprimir arbitrariamente las columnas. El Hover contractual alcanza1288px: comprobar ese extremo sin clipping. Columnas originales156/371.999755859375/132/224/156/88/88, gap8 y paddinghorizontal8 se conservan; etiquetas locales Documento/UUID/Tipo/Fecha/Importe/Estado/Detalle. Tres filas no son un límite de producto.

Resumen: preservar caja MetricCard Horizontal Large311×192; anfitrión vertical y Button alineados a311px. Gap16 mediante spacing/lg. Ajustar únicamente wrappers locales si el texto largo exige más espacio; no alterar el main MetricCard ni sus ocho variantes.

## Tokens y dependencias

JSON base comprobado: semantic/Contable52:2; font/family/base → manrope; spacing/sm/lg/xl →8/16/24; radius/xl →16; color/background/default →neutral100; subtle→neutral200; brand→blue100; text/primary→neutral900; text/secondary→neutral600. Conservar aliases y scopes por propiedad; esos IDs de origen no sirven como IDs del nuevo archivo.

Header requiere su extensión de release, Avatar/Dot/Logo/Icon Button; Sidebar su extensión y Menu Item/Tooltip/Icon Button; Table conserva sus dependencias ocultas y extensiones de borde/Dot; MetricCard y Button aplican SIX-FAMILY-COLOR-001 junto a sus contratos. Las rutas existen en el paquete; antes de construir se leerían en profundidad solo las dependencias instanciadas o modificadas. La receta histórica de MetricCard que oscurecía Servicios está expresamente sustituida por SIX-FAMILY-COLOR; no es un permiso para recolorear.

Localizadores históricos encontrados, todos por verificar en vivo: AppShell737:304; Header518:123; Sidebar set619:480, Collapsed619:481; Table548:895; Button set26:81; MetricCard set202:327. Archivo fuente de lectura/importación: tj3WIBEZDGLVs7MJWKCwgf. El nuevo file key, component keys, variables y nodos destino no se inventan.

## Ejecución que correspondería fuera de esta simulación

1. Cargar los manuales oficiales señalados y crear nuevo archivo mediante figma-create-new-file. Leer su file key real.
2. Inspeccionar fuente y destino, principales, propiedades, variables/remotas, tipografías y capacidad Slot. Leer component keys reales, importar y preservar instancias/bindings.
3. Crear mapa de IDs fuera del maestro; componer lotes pequeños en archivo nuevo, principal local separado de pantallas; conectar Cargas→detalle→Cargas y Continuar→revisión→Cargas.
4. Leer/capturar cada estado y comparar a1440×900: anatomía, geometría, texto, alias/scope/tema, editabilidad, reacciones, overflow y sin detach.
5. Probar Slots de tabla con1/3/4 filas, inserción/retirada/reordenación, contenido largo y conservación de Row State. Header Actions y Sidebar Menu items conservan sus Slots propietarios; no confundir frame llamado Slot con capacidad nativa.
6. Si un existente es inaccesible, marcar UNAVAILABLE_EXISTING_COMPONENT, no declararlo inexistente. Si la API no permite Slots obligatorios, TOOL_LIMITATION/BLOCKED acotado; continuar partes independientes sin certificar esos requisitos.

## Evaluación de recursos

No hay fallo de integridad ni ruta operativa rota observado. El índice posee páginas y algunos null, pero el workflow explica que no prueban inexistencia; los state.json/contratos permiten localizar IDs históricos. Los contratos contienen instrucciones históricas de migración (incluyen destino maestro y afirmaciones antiguas de Graphify); references/design-system.md excluye expresamente reejecutarlas en consumo, por lo que no bloquean esta solicitud. El paquete depende de herramientas/manuales oficiales externos para escritura: están declarados, no embebidos ni certificados aquí.

QA Figma real: NOT_RUN (la prueba prohíbe esas llamadas). No hay URL, captura, readback, principal local ni pantalla entregable. Integridad del paquete no acredita actualidad de la biblioteca ni aprobación humana; se conservan DELEGATED_FOR_BUILD/PENDING de las familias aplicables.

## Fuentes leídas y hashes

- `specs/app-shell.contract.v0.1.0.md` · SHA-256 `f4735e43344b54477df4ab8058f55fa5c45b6c03fdbdf651c6d35feb5d75ad9e`.
- `specs/header.contract.v0.1.0.md` · SHA-256 `18b87c9e1cb91346d6f75359d51f78c825ffeb2bf1a6ba1b148a6f8e4291e00e`.
- `specs/sidebar.contract.v0.1.0.md` · SHA-256 `6ddb3bb5e4166d5c53396d1b5f0bdac56e2bf431cce926050d818c726447cc8f`.
- `specs/table.contract.v0.1.0.md` · SHA-256 `e3b7b1c999fa8f59c839a082cde95f5709d21375feb4bc2fefd26652c2394108`.
- `specs/metric-card.contract.v0.1.0.md` · SHA-256 `243abaf3460738916249876eb9b6064edf1341a98a242c54e4a05d78819b824e`.
- `specs/components/button.contract.v0.2.0.md` · SHA-256 `53e13fa8e664f70d0ce81116e850bbcb0ab7da9f14ac0f08607fa5fda09894a1`.
- `specs/components/button-page-name.amendment.md` · SHA-256 `b2c896cab9f2f5659101253dbc93ce0410c697081e53daafecebbc5b62895fd7`.
- `specs/components/button.local-bindings.amendment.v0.2.2.md` · SHA-256 `57b84698047da82ebfd10c18ed828a1aac43482283856d49690d379b60d2e59c`.
- `specs/components/button.semantic-scope-amendment.v0.2.1.md` · SHA-256 `8655c79ae1f13c66be04ed406815066a1f3a44d553d2b948390f6bf1b6f1dfb9`.
- `specs/components/six-family-color.amendment.v0.1.0.md` · SHA-256 `f569d5e132a0b5480f7b540dea8f157a601f27f24e86bb5ccb05b2d05f4b2cc9`.
- `specs/foundations/foundations-tokens.contract.md` · SHA-256 `e7362c364aa2c93a1a5bd50e0024d6b551f8ec6c6947bb62c6779ee25c1b7999`.
- `sources/inventories/tokens.inventory.json` · SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.
- `drafts/foundations/ai-design-system.header-release.v0.1.0.json` · SHA-256 `8c5e8d90c55c04edba7020cdf03a4749aea369b85047e1bc84b0055d363a202b`.
- `drafts/foundations/ai-design-system.sidebar.v0.1.0.json` · SHA-256 `800475639b8c18f683f8fe336105b8ae0a424e1cbac04b0f6aee6c9c6283615a`.
- `specs/tokens/ai-design-system.six-family-color.v0.1.0.json` · SHA-256 `42e29b60c02b629c4b4d537c8e1f1b6f14e492e7b4fe29e2ec17204e5e5cc2ff`.
- `protocols/SLOTS-REVIEW-AND-IMPLEMENTATION.md` · SHA-256 `e8e524a3d69a8770693ab0646463d55a2c4dc4542e044375666b6c2da61e8847`.
- `registry/contracts.md` · SHA-256 `5061c78a1c707cb4271a6514b97e14294092faa4531bc37d690edb3ea683ff48`.
- `specs/MIGRATION-AUDIT.md` · SHA-256 `8670891be92c485d97f50d8f5f362733bddfa97e7ebc69d5a9defad46bbb216e`.
