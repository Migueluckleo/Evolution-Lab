# Changelog del paquete de protocolos

## 0.5.0 · cierre técnico delegado · 2026-10-16

[DEC-AI-TECHNICAL-CLOSURE-001](registry/DEC-AI-TECHNICAL-CLOSURE-001.md) elimina la aprobación/revisión humana rutinaria como gate del trabajo de IA solicitado. QA documental permite delegación técnica; QA de implementación y entregables aplicables permiten cierre. Los agentes mantienen documentación y evidencia, y las observaciones posteriores abren correcciones. `APPROVED` sigue requiriendo decisión humana real; los estados y evidencias históricos se conservan. No modifica diseño, permisos ni publicaciones externas. P08 mantiene el mecanismo de paquetes existente hasta implementar el consumo remoto propuesto.

## 0.4.0 · skills de consumo versionadas · 2026-10-14

Por [DEC-DS-SKILLS-001](registry/DEC-DS-SKILLS-001.md), se incorpora [P08](protocols/08-SKILLS-AND-RELEASES.md). Cada alta o modificación del DS entrega las dos nuevas skills, `contpaqi-figma-screens` y `contpaqi-po-prototypes`, desde el mismo corte de fuentes. P05/P06/P07 incorporan trazabilidad y controles de vigencia. Los paquetes son inmutables por versión y los generadores detectan cambios, ausencias o alteraciones; no se editan snapshots a mano.

La primera skill construye pantallas Figma con componentes del DS y composiciones locales documentadas. La segunda genera HTML autónomo desde React/TypeScript/Tailwind/Next.js y un Markdown de traspaso con identidad, medidas y evidencia del render. No modifica las dos skills anteriores ni promueve componentes locales al DS. Las verificaciones e instalaciones efectivas se registran en [skills](registry/skills.md), separadas de una ejecución Figma o publicación remota.

## 0.3.0 · componentes web · 2026-10-13

Por solicitud explícita se incorpora P07 y el destino React + TypeScript + Tailwind + Next.js. Biblioteca local de 43 familias con API, ejemplos, fichas regenerables y catálogo con pantalla de muestra sin backend. Versiones estables compatibles fijadas en package.json/lockfile. Cobertura documental obligatoria para altas y modificaciones, con verificación de fuentes y ejemplos. [Guía](implementations/web/README.md), [decisiones técnicas y límites](implementations/web/docs/WEB-ADAPTATION.md), [QA](qa/implementations/web.v0.1.0.review.md).

La autorización sustituye la previsión Vite para este destino; no modifica datos canónicos, aprobaciones visuales o Figma. 64/72 assets Logos disponibles; ocho pendientes por límite de consultas Figma. No hay backend ni publicación. Se conservan los cambios previos de retención y el cierre estructural/semántico de P05.

## 0.2.4 · sincronización continua y herramientas locales

La decisión del 2026-10-08 DEC-GRAPH-CONTINUOUS-SYNC-001 y P05 0.2.4 exigen cierre local estructural y semántico, cobertura, hashes y outputs concordantes. Esta entrada y README se concilian el 2026-10-13 con la versión ya declarada en AGENTS; no aprueban contratos de diseño.

Por solicitud «Dale empieza con las Altas» del 2026-10-13 se implementan el punto de entrada `scripts/ds`, configuración de corpus y controles, vista derivada por familia y QA documental determinista. El cierre Graphify conserva respaldo, valida semántica y genera en staging antes de publicar. [Operación y límites](references/PROJECT-TOOLING.md). No modifica contratos, datos canónicos, Figma ni hooks globales; la retención de derivados queda fuera de este lote.

En un lote posterior del 2026-10-13, autorizado con «Dale» tras proponer la reducción de peso Git, se aplica la [retención de artefactos](references/ARTIFACT-RETENTION.md): cachés, intermedios y copias completas locales quedan excluidos; 673 derivados se retiran del índice con respaldo y recuperación verificados. Se conservan fuentes, evidencia, entregables, grafo activo e historial.

## Modal · Librería raíz · 2026-10-01

Sin cambio de protocolos. PáginaModal565:122 con6variantesBasic,Media ySideBySide; contrato promovido aspecs. SlotsBody/Side content/Actions, imágenes originales y34 tokens existentes.25pruebas,123paints,53textos,136 aliases y392comparaciones por tema. Excepciones documentadas; bibliotecasinpublicar. [Continuación](registry/SESSION-HANDOFF-2026-10-01-MODAL.md).

## Table · Anticipa · 2026-10-01

Sin cambio de versión de protocolos. FuenteTable reemplazada explícitamente porAnticipa15006:84823. Reconstrucción enpáginaTable546:122/main548:895 y contratoen specs; Slots0..n, textoseditables y tokenssemánticoslocales.27checks,899paints,36tokens/144aliases;0variables nuevas. Excepciones documentadas; biblioteca nopublicada. [Continuación](registry/SESSION-HANDOFF-2026-10-01-TABLE.md).

## Header · 2026-10-01

Sin cambio de versión del paquete: Header construido en página propia, contrato promovido a specs, Slot Actions validado y tres roles semánticos nuevos sin primitivas. JSON/Figma/contrato sincronizados; contraste y límites Desktop documentados. No publicación de biblioteca, frontend ni nuevos logos. Estado y continuación: registry/SESSION-HANDOFF-2026-10-01-HEADER.md.

## Mantenimiento documental · 2026-10-01

Sin cambio de versión del paquete ni de requisitos: estado consolidado de migración en MIGRATION-TRACEABILITY-STATUS, enlaces de continuidad en README y anotación de temporalidad en el descubrimiento de Header. Select y las seis composiciones Slots no vuelven a la cola por frases históricas. Actualización Graphify autorizada por lotes; resultado operativo y cobertura en registry/environment.md. No cambia Figma, JSON canónico ni aprobaciones.

## 0.2.3 · 2026-09-29

Se incorpora P-SLOTS0.1.0 por DEC-SLOTS-REVIEW-001: revisión obligatoria de aplicabilidad antes de construir/modificar cada familia; Slots para contenido variable cuando corresponda, con definición contractual, verificación de capacidad real, operaciones desde instancias consumidoras y nueve controles de QA. Se integra en AGENTS, P03/P04/P05/P06, README y plantilla de componente. No constituye implementación en Figma ni aprobación de contratos futuros. Select queda primero en la cola de adopción; sus cinco opciones son una muestra, no un máximo. Se conserva el QA histórico y se marca pendiente el requisito nuevo. Graphify sigue STALE, sin regeneración.

## 0.2.2 · 2026-09-23

Se añadió una excepción de decisión delegada, limitada a la migración desde la Librería Figma anterior hacia `AI-Design-System`, por solicitud explícita de construir y pedir auditoría humana después. `DELEGATED_FOR_BUILD` exige inspección, contrato versionado, QA documental y mapeo al JSON aprobado, sin afirmar aprobación humana. El QA de implementación y la auditoría del usuario se registran por separado; conflictos materiales, tokens faltantes y operaciones destructivas no se autorizan por la delegación.

## 0.2.1 · 2026-09-23

Por solicitud del usuario, P03/P04/P06 y la plantilla de componente incorporan el nombre semántico exacto de una página por familia, su creación/reutilización con verificación previa y lectura posterior, y un mapeo explícito de color y tipografía a variables locales de `AI-Design-System`. P05 registra nombre e ID reales de la página y el mapa de variables. El inventario JSON aprobado de variables es la fuente canónica de nombres, tipos, modos, valores, aliases y `description`; el Figma de destino aporta los IDs reales. No se modificaron contratos ya aprobados ni componentes existentes. La nueva regla no aprueba automáticamente contratos futuros.

## 0.2.0 · 2026-09-22

### Añadido

P03 de construcción de contratos Markdown desde JSON, nodo Figma y fuentes combinadas. Incluye clasificación de evidencia, requisitos candidatos, cobertura, reporte, revisión documental y aprobación humana de versión/alcance.

Plantillas diferenciadas para componentes y foundations, más reporte de síntesis. La de componentes conserva las 21 secciones del ejemplo educativo, pero no importa sus valores ni reglas como verdad del proyecto.

Prompts separados para integrar la actualización y para sintetizar contratos cuando se entreguen fuentes reales. Documento de migración, manifiesto de integridad y verificación del paquete.

### Renumerado

Construcción Figma pasa de P03 a P04; autodocumentación de P04 a P05; QA de P05 a P06. Se actualizan sus enlaces activos.

### Cambios de gobernanza declarados

La ingesta ya no conduce directamente a construcción. Un contrato sintetizado debe pasar por DRAFT/IN_REVIEW y aprobación humana antes de P04.

Se separan el estado documental del contrato, la preparación por destino y el estado de implementación. Una excepción aceptada se muestra como `VALIDATED_WITH_EXCEPTIONS`, sin ocultar la diferencia.

Se precisa la autoridad por responsabilidad: el MD aprobado gobierna las reglas y el JSON aprobado los campos delegados. Esto sustituye la simplificación anterior de que el formato Markdown siempre ganaba a un JSON. Una contradicción debe resolverse, no sobreescribirse por formato.

Las enmiendas aprobadas son sustituciones acotadas por entidad, versión y requisito; no quedan inútilmente subordinadas a una versión anterior ni adquieren autoridad global por fecha.

### Ampliado

Trazabilidad para fuentes, borradores, requisitos, decisiones y digests. QA documental separado de QA de implementación. Gestión de cobertura parcial, unidades desconocidas, estados simultáneos, mapeos por plataforma e identidad origen/destino.

La lectura de un nodo Figma en P03 se diferencia de la escritura de P04. Graphify y sus bloques/configuración existentes se preservan durante la migración.

### Conservado

Repositorio como fuente de especificación; una sola `description` por token; aliases y bindings; originales intactos; destino Figma acordado; una página por familia de componente; React + TypeScript + Vite como pila prevista, no instalada por esta entrega.

## Paquete anterior, identificado como 0.1 durante la conversación

Cinco protocolos: entorno, ingesta, construcción Figma, autodocumentación y QA. Sin fase formal de síntesis de contratos antes de construir. Su estado se conserva en los respaldos del proyecto al migrar; no se incluye como una segunda versión activa en este paquete.
