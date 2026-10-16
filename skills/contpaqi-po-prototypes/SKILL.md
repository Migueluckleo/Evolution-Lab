---
name: contpaqi-po-prototypes
description: Construye prototipos CONTPAQi con React, TypeScript, Tailwind y Next.js, entrega un HTML interactivo que abre sin servidor y un Markdown con evidencia para replicarlo mediante contpaqi-figma-screens. Úsala para pantallas y flujos de producto portables.
---

# Prototipos CONTPAQi para producto

Entrega `entrega/render.html` y `entrega/replicar-en-figma.md`, con referencias y
capturas. El usuario abre el HTML directamente, sin Node, servidor ni red. La
fuente editable permanece fuera de la entrega. Preparar el Markdown no ejecuta
Figma: invoca **`$contpaqi-figma-screens`** en la futura sesión del diseñador.

El motor instalado y el contenido del DS tienen versiones independientes. Los contratos conservan su autoridad y sus estados; descargarlos no aprueba documentos ni valida implementaciones.

## Consultar GitHub antes de cada trabajo

Aplica primero una revisión breve de ahorro: identifica las familias necesarias y reutiliza evidencia vigente. Ejecuta `python3 <skill-instalada>/scripts/resolve_ds.py --output <carpeta-nueva-de-ejecucion>` una vez al iniciar el trabajo. Requiere Python 3.10 o posterior y HTTPS hacia GitHub público; no requiere cuenta ni token GitHub. Lee [consumo remoto](references/remote-source.md) para resolver fallos o continuar un trabajo existente.

El resultado debe ser `PASS`. Desde ese momento, **todas las rutas de scripts, referencias, assets y snapshot de esta guía se resuelven respecto de la carpeta de ejecución devuelta**, no de la instalación. No vuelvas a ejecutar el cargador desde esa carpeta durante el mismo trabajo. La carpeta contiene una copia temporal verificada del corte remoto, fijado para evitar mezclar versiones; el siguiente trabajo vuelve a consultar GitHub. Registra digest, identidad del catálogo y versión del motor. Lee solo los contratos necesarios, aunque la descarga incluya el corpus completo.

Si no hay Python, ejecución de scripts o salida HTTPS, informa la capacidad faltante y conserva la preparación. Si GitHub no responde, el catálogo aún no está publicado o falla la integridad, no construyas con una copia antigua ni afirmes que los specs están actualizados. La instalación en Genspark no garantiza esas capacidades: se comprueban en su entorno.

1. Extrae objetivo, pantallas, contenido, acciones, tema y viewport. Resuelve solo
   decisiones materiales faltantes. En ausencia de indicación usa Contable y
   escritorio 1440×900 como supuestos locales. Emplea datos ficticios y memoria.
2. Lee [consumo del DS](references/design-system.md) y contratos/enmiendas de las
   familias utilizadas. Usa sus componentes, CSS, artwork y tokens incluidos.
   Incluye la enmienda tipográfica de cada familia y el catálogo activo para
   resolver estilo, rol, variante y decoración sin inventar recetas locales.
   Conserva la diferencia entre receta materializada web y vínculo nativo Figma;
   incluye la enmienda de herencia y su evidencia cuando el componente la consuma.
   Para algo no cubierto, compón componentes existentes y documenta la decisión
   local; no la declares variante o componente oficial ni inventes una aprobación.
3. Lee [build y QA offline](references/build.md). Ejecuta
   `node <skill>/scripts/init.mjs <salida-nueva>`. Edita `prototype/page.tsx`, estilos
   locales y `brief.json`; `app/` y `ui/` son derivados regenerados. Todos los pasos
   viven en una entrada cliente, con estado/hash. No abras el catálogo del DS.
4. Implementa respuestas visibles y estados reales. Conserva API, tokens,
   geometría y composición. Marca instancias con `DSNode`/`data-ds-node`, identidad
   contractual y props. Marca también títulos, textos y contenedores locales
   relevantes; captura estados con acciones/aserciones en `brief.json`.
   [Esquema de evidencia y handoff](references/handoff.md).
5. Compila con `npm run build`, luego `npm run capture`. El script abre una copia
   renombrada del HTML por `file://`, aislada y con HTTP(S) bloqueado; mide nodos y
   toma capturas. Revisa esas imágenes y prueba el recorrido, teclado, retornos,
   contenido largo y viewports solicitados. Capturar no sustituye revisión visual.
6. Completa decisiones, limitaciones y checks reales; repite captura tras cualquier
   cambio de brief/HTML. Ejecuta `npm run handoff` y revisa el Markdown contra las
   capturas. Incluye IDs/contratos/hashes/props y omisiones reales; nunca inventes
   un ID Figma. Un destino Figma aún desconocido no bloquea la entrega del prompt.

Entrega enlaces al HTML, Markdown y carpeta/ZIP completos. Abre el HTML si el visor
disponible admite JavaScript; de lo contrario indica doble clic en navegador.
Si falta capacidad de navegador, conserva `NOT_RUN` y describe la limitación. Si
la ejecución falla, conserva `FAIL` y corrige; no presentes el prototipo como
funcional ni uses localhost para cubrir el fallo. No publicar, ejecutar Figma ni
modificar el maestro o las habilidades instaladas durante este flujo.
