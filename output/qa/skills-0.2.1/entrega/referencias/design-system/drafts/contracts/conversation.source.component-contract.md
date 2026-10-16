# Conversation · contrato de evidencia fuente

Fuente: [Anticipa, nodo 20355:72763](https://www.figma.com/design/zuUq3gcF9T3CLid44bjY6W/Anticipa-Junio2026?node-id=20355-72763).
Inspección: **PARTIAL**, 2026-10-08T17:01:41Z. Evidencia Figma de solo lectura; **no contrato normativo aprobado ni implementación en AI Design System**.
Modelo sincronizado: [YAML](conversation.source.component-contract.yaml). [Snapshot](../../sources/figma-snapshots/conversation.20355-72763.observation.2026-10-08.json).

## 1. Component Identity

Observed from Figma: `Molecules | Anticipa | Conversation`, COMPONENT_SET, key `b1a6e3743798f36af3df685ddecac3245d644886`; página Components `17001:89455`, sección Chat Components `20355:72762`.
Posición184,263; tamaño648×533; visible, clipping true, opacidad1. Sin descripción ni documentación explícitas.

## 2. Anatomy

Derived structure: 147 nodos recorridos, incluidos 26 con visible=false; 47 instancias, 20 textos, siete Slots nativos, 41 vectores y dos grupos. Recorrido estructural completo, no todas las propiedades.
- Message Sent: burbuja y texto.
- answer Beni / answer Navi: personaje, nombre, badge, AnswerText, previews oculto, Secondary actions oculto, acciones de valoración/copiar.
- Text Field: disclaimer, Slot text, selector de modelo oculto, adjuntar/micrófono/enviar.
Árbol funcional completo en YAML; vectores omitidos de la anatomía funcional.

## 3. Dependencies

21 principales únicos: tres LOCAL y18 REMOTE; los21 PARTIALLY_RESOLVED. Las47 instancias están agrupadas sin duplicados. Identidad real leída; propiedades, overrides y definiciones de los sets no están completamente resueltos.

| Main ID | Dependencia fuente | Localidad | Instancias |
|---|---|---|---:|
| 17084:9568 | Presentation / Format=Outline, Weight=Fill | REMOTE | 8 |
| 18311:28196 | Table / Format=Outline, Weight=Light | REMOTE | 2 |
| 17029:48637 | DownloadSimple / Format=Outline, Weight=Light | REMOTE | 4 |
| 12788:92698 | PlusCircle / Format=Outline, Weight=Light | REMOTE | 4 |
| 19784:32781 | ThumbsUp / Format=Outline, Weight=Light | REMOTE | 2 |
| 19784:32784 | ThumbsDown / Format=Outline, Weight=Light | REMOTE | 2 |
| 12744:90302 | CaretDown / Format=Outline, Weight=Light | REMOTE | 1 |
| 17095:10812 | Paperclip / Format=Outline, Weight=Light | REMOTE | 1 |
| 18568:31231 | Microphone / Format=Outline, Weight=Light | REMOTE | 1 |
| 17095:10859 | PaperPlaneTilt / Format=Outline, Weight=Light | REMOTE | 1 |
| 20355:72915 | Atom | Isologo / logo=NAVI | LOCAL | 1 |
| 20355:72956 | Chat Components / molecule | Ecosistema AI | actions | LOCAL | 2 |
| 20210:164221 | ▶ messageAnalisisNavi / Property 1=1 | REMOTE | 1 |
| 20355:71022 | messageAnalisisBeni / Property 1=standby | REMOTE | 1 |
| 20355:72950 | Copy / state=Default | LOCAL | 2 |
| 20601:24296 | icon-button / type=ghost, size=small, selected=false, state=default | REMOTE | 2 |
| 20601:24057 | badge / type=info, size=medium | REMOTE | 4 |
| 20601:24239 | dot / type=notification, size=small | REMOTE | 3 |
| 20569:63259 | button / type=primary, size=small, state=default | REMOTE | 2 |
| 20601:24266 | icon-button / type=secondary, size=small, selected=false, state=default | REMOTE | 1 |
| 20569:63262 | button / type=secondary, size=small, state=default | REMOTE | 2 |

## 4. Properties

Observed from Figma: cinco BOOLEAN — disclaimer=true; show additional actions=false; secondary action=false; Show model selector=false; Contains Preview=false. Cuatro definiciones SLOT: text, AnswerText, Secondary actions, previews; ninguna con preferredValues sugeridos. Un eje VARIANT: Property 2. Sin propiedades TEXT expuestas en este set.
La lectura de componentProperties de una instancia falló: “Component set for node has existing errors”; no se atribuye a una instancia concreta porque esa llamada no devolvió resultado parcial.

## 5. Variants

Observed from Figma:

| ID | Property 2 | Medida observada |
|---|---|---|
|20355:72764|Message Sent|616×51|
|20355:72767|answer Beni|616×76|
|20355:72791|answer Navi|616×76|
|20355:72815|Text Field|616×130|

Son tipos de contenido, no cuatro estados equivalentes. No se inventa un producto cartesiano.

## 6. States

Requires definition: matriz pública de estados del composer y mensajes. Las reacciones anidadas no demuestran Loading, Error, Disabled ni entrega del mensaje.

## 7. Layout

Observed from Figma:37 registros de layout en YAML/snapshot. Set vertical gap56 padding16 (rejilla de muestra, no transcript). Burbuja494×51 con padding16; respuestas con contenedor/columna y gap8. Composer vertical gap−1; disclaimer22px, campo109px padding16 gap16, acciones41px. Modelo oculto184×32. Estas son medidas de la muestra, no breakpoints ni límites de producto.

## 8. Visual Styles

Observed from Figma: captura inspeccionada de las cuatro variantes. Burbuja con fondo de acento; personajes diferenciados; composer blanco con borde, sombra y separador. Pinturas/efectos de37 contenedores conservados con sus bindings en snapshot. Auditoría individual de pinturas de texto/vectores aún parcial. El borde morado del set no es borde del componente.

## 9. Typography

Observed from Figma:20 textos Manrope. Cuerpo14/20 Regular; nombres14/20 Bold; badges12/16 Regular; títulos de preview16/20 Bold; disclaimer12 con line-height AUTO. YAML conserva cada texto y estilo aplicado; no se han extraído todos los segmentos tipográficos.
Tres estilos usados: body/regular y subheading 2/emphasis locales; elevation/shadow/md remoto. Los tres PARTIALLY_RESOLVED: identidad leída, definición completa pendiente.

## 10. Tokens

51 variables usadas: ocho LOCAL y43 REMOTE; las51 PARTIALLY_RESOLVED. Nombres, tipos y valuesByMode/aliases fuente conservados; colección detallada, resolución terminal y modo consumidor no verificados.
**Estos son tokens observados en Anticipa, no un mapa aprobado del destino.** La coincidencia de nombres no prueba bindings locales correctos.

| Nombre fuente | ID fuente | Localidad |
|---|---|---|
| Color /Brand/brand-primary | VariableID:15001:198366 | LOCAL |
| Color/background/base | VariableID:17569:27778 | LOCAL |
| color/background/default | VariableID:4133fceadb3cde506fd63ae1fbb1bd0878fde9dc/3639:881 | REMOTE |
| color/background/overlay | VariableID:871163d3ec0b8faa7dbde096441d286160b07ea7/3639:892 | REMOTE |
| color/border/brand | VariableID:8e0deb55fcbf5eca145c56fd706bcd7a229242fa/8864:0 | REMOTE |
| color/border/strong | VariableID:017d25b88e19d9ed2b94881cb4822fe28a2ca422/7190:3 | REMOTE |
| color/border/subtle | VariableID:17c0c6e22f8a4d0294edd46d9c6fa7648e021d63/6609:3 | REMOTE |
| color/border/surface | VariableID:fa5c6286ab4314e98428f50ac21345d18859eab0/8917:5 | REMOTE |
| color/feedback/danger/icon | VariableID:9b1e68d1f4dd4f9560cbe322415f543969f12fdf/6075:39 | REMOTE |
| color/feedback/information/bg | VariableID:d8c061da98c68de0d409bbe4c021fe9c679a79d9/3639:889 | REMOTE |
| color/feedback/information/icon | VariableID:da2119fc30b893e3dcded2c41fc39a2c1b822150/8852:7 | REMOTE |
| color/feedback/information/text | VariableID:b58ae05e2f3b00af923cd3f74cda5376ce310a29/8852:3 | REMOTE |
| color/icon/brand | VariableID:6343eff370d284d2b13be99a19d4fcad477ce4fd/8864:1 | REMOTE |
| color/icon/on-brand | VariableID:a073f8e354fa6ce36ab0d8ac7a78109f53bb54e5/3639:919 | REMOTE |
| color/icon/primary | VariableID:d54da22e7e50c1893e114ea6cd0d90d2d2769a04/3639:915 | REMOTE |
| color/interactive/primary/default | VariableID:0be1d4f729e0115993584e7075baede84506f24f/8860:0 | REMOTE |
| Color/stroke/base | VariableID:17569:27786 | LOCAL |
| color/surface/brand/accent | VariableID:6e6180531221bed26d61dc036ec9e3f0e362360b/6075:103 | REMOTE |
| Color/text/auxiliar | VariableID:17569:27771 | LOCAL |
| Color/text/base | VariableID:17569:27770 | LOCAL |
| color/text/brand | VariableID:80588ae3ad8e2411323f00e7322938e8e73c2ecb/8864:2 | REMOTE |
| color/text/on-brand | VariableID:21c68664aad258aad360610ceb69cc12c98be563/3639:900 | REMOTE |
| color/text/primary | VariableID:ca2ca2cc17d99357b05a0401d6eb230dfad804b5/3639:893 | REMOTE |
| color/text/tertiary | VariableID:37a0ea94f1ce202132cbe3637999ca8e1f0ca566/3639:895 | REMOTE |
| font/family/base | VariableID:5b6478e0ce1305efedeaf4a605843e3af57a32ca/8394:2 | REMOTE |
| font/letter-spacing/normal | VariableID:79fe3a30a9b92bac34cd254ab77fd25797247666/3639:879 | REMOTE |
| font/line-height/sm | VariableID:b8aed2fc3d0787610a1d9514cbe56ea42ee5b1e1/3639:871 | REMOTE |
| font/line-height/xs | VariableID:5a156743257bea0783f4d33628bd3a8262bc35e2/3639:870 | REMOTE |
| Font/Primary | VariableID:15006:75178 | LOCAL |
| font/size/sm | VariableID:127a590c83af7e9167ebd4daaca4658d7e6ca288/3639:862 | REMOTE |
| font/size/xs | VariableID:44a21f9f8d118524aceb4bab4db4c656140a3b4a/3639:861 | REMOTE |
| font/weight/bold | VariableID:68953aef437f5350d545fc4a9000b6ca1328f7b2/4655:15 | REMOTE |
| font/weight/regular | VariableID:d9723f3635e7a39d3366f43f0c4fcbb13cfb1dea/8394:4 | REMOTE |
| icons/xsm-icon-size | VariableID:7b6bf4f6145d8f0aa9bf8e84a38d58241bcd9e2e/4360:12 | REMOTE |
| message-Actions/state-ThumbsDown | VariableID:82efcf196fbfb0f0c2e8be695dac10be0a1df6f9/209:239 | REMOTE |
| message-Actions/state-ThumbsUp | VariableID:d43cad09980477881a87d883bce79829e4c6c90c/209:238 | REMOTE |
| radius/full | VariableID:07f844cfd865a18cfad54385444f42b10f605123/3639:804 | REMOTE |
| radius/md | VariableID:31c39dae3354372bf695953f2b7d26172742bdeb/3639:799 | REMOTE |
| radius/sm | VariableID:3ae4611e96f2ce2dea9afff292184554b70766d0/3639:798 | REMOTE |
| size/2xl | VariableID:a4b3df7778347a55c5e9581d2b4b147977d87876/8871:9 | REMOTE |
| size/3xl | VariableID:a8d2e43425dd224dd65342e23db51560c586bf22/8871:7 | REMOTE |
| Size/Font/Body/Base | VariableID:15006:75542 | LOCAL |
| Size/Font/Subheading/md | VariableID:15006:75540 | LOCAL |
| size/lg | VariableID:151918309e07e9c091e8dd43f6230aba54e7ef5b/5401:17 | REMOTE |
| size/sm | VariableID:6529b09a82c73a4ddc0033e45730ffe49d15c109/3639:813 | REMOTE |
| spacing/lg | VariableID:078efa311580f51425cc2454d702721e2acad78f/5401:36 | REMOTE |
| spacing/md | VariableID:03c59fefa1fd346bf03d4abc099396fa9ae5bb92/5504:1 | REMOTE |
| spacing/none | VariableID:4f36a89ff3f1560665805305d5132f9b73d4b2ad/3639:849 | REMOTE |
| spacing/sm | VariableID:634220d13f50e842b56b814d7b2f7d8049cc0c95/3639:806 | REMOTE |
| spacing/xs | VariableID:90435138fcc3da9fb6d745fd768eea1072696e3e/3639:805 | REMOTE |
| stroke/xs | VariableID:09bf0f399feb2dd1331a55f613f3fec11642c615/3639:793 | REMOTE |

## 11. Content

Los20 textos de ejemplo están en YAML: solicitud de facturas, respuestas BENI/NAVI, etiquetas de agente, preview de tabla, Crear indicador/Agregar a dashboard, disclaimer y placeholder. Son contenido de demostración; no requisitos fiscales, límite de longitud, capacidades reales ni una política de agentes.

## 12. Interactions

FIGMA_DEFINED, alcance parcial: **15 reacciones en12 nodos anidados**. Incluyen animación del personaje por timeout, hover de botones, condiciones al pulsar valoración y cambio visual de Copy. Hay acciones de clic vacías.
Requires definition: ramas completas de las condiciones, destinos de animación y comportamiento de enviar, adjuntar, audio, persistencia de valoración y copia real al portapapeles. La presencia del icono no demuestra esas funciones.

## 13. Accessibility

REQUIRES_DEFINITION. Sin certificación de teclado, nombres accesibles, anuncios, foco ni contraste en modos del destino. No se confunde render Figma con una implementación web accesible.

## 14. External Dependencies

18 principales REMOTE;43 variables REMOTE y un estilo REMOTE. Metadatos de biblioteca, archivo de origen remoto y versión: NOT_EXPOSED_BY_FIGMA_MCP. Los IDs resueltos en Anticipa no son IDs de AI Design System.

## 15. Unresolved Information

- ComponentProperties getter failed: Component set for node has existing errors; active instance properties/overrides and owning-set definitions not completely inspected.
- ValuesByMode preserve source aliases; terminal alias resolution and current theme parity not checked.
- Paints/effects captured for 37 containers; detailed text/vector paints and styled segments remain pending.
- Conditional reactions summarized only; branch expressions/actions and destination components not inspected.
- No destination inventory, token mapping, normative contract, build, QA implementation or library publication in this intake.

Las llamadas demasiado grandes se repitieron por lotes; no se usaron respuestas truncadas como evidencia completa. Todos los scripts fueron de lectura.

## 16. Implementation Notes

No se construyó ni se modificó Figma. No se alteró el JSON canónico. Este documento no autoriza copiar dependencias remotas ni adoptar variables internas de Anticipa.
P-SLOTS: REQUIRED para respuesta compuesta, previews y acciones variables. Se observaron siete Slots, pero no se probaron operaciones en instancias consumidoras. La cardinalidad de la muestra no establece límites.

## 17. Evidence / Confidence

FIGMA_DIRECT: snapshot de identidad, árbol,37 layouts, textos,47 instancias/21 principales,51 referencias/definiciones de variables, tres estilos y resumen de reacciones.
DERIVED: agrupaciones y conteos.
REQUIRES_DEFINITION: contrato normativo destino, roles/asignaciones canónicas, alcance de personajes y comportamiento no demostrado.
Confianza MEDIUM: árbol completo, resolución de propiedades/dependencias parcial. Snapshot SHA-256 `f02bf89ff7c06a101d372fe62fdf34b335155f5a94be9a225582573477632193`.

