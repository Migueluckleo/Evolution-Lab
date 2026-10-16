# QA de implementación · Stepper Item 0.1.0

Estado histórico: `STALE` solo para color tras la instrucción posterior de tema de marca. La estructura y tipografía verificadas aquí permanecen como evidencia; el [QA 0.1.1](stepper.v0.1.1.figma.review.md) es vigente para alias, scope y bindings. Auditoría humana `PENDING`, biblioteca `UNPUBLISHED`. Inspección original: 2026-09-24.

## Estructura y propiedades

Página `Steppers` (`347:122`), set público `Stepper Item` (`350:347`) de 18 variantes y `Stepper Connector` (`348:138`) de ocho. Las medidas de Start/Middle/End coinciden con las seis medidas de la fuente. Cada ítem anida una instancia de icono Phosphor y una o dos instancias locales de conector, sin depender del set `container` de la Librería antigua. Los extremos de conectores se redondean junto al círculo; la salida vertical de Start se recorta a 21 px. El set público ofrece tres textos, dos booleanas y un swap de icono, además de sus tres ejes de variantes; los seis controles se vincularon en las 18 variantes. Se probó el cambio de texto, ocultar/mostrar Step y Caption, y sustituir el icono en una instancia temporal, que fue retirada tras la prueba.

La comparación visual detectó que el texto `Step details` se partía en dos líneas: la fuente emplea tracking de −2 % y el destino arrancó en 0 %. Se restauró el valor fuente en los 54 textos; la captura posterior muestra de nuevo el título en una línea. La fuente usa interlineado 15/21 px y el destino vincula los tokens existentes 16/20 px; los bloques públicos y su colocación mantienen las medidas de la fuente. El tracking −2 % permanece literal, porque el token tipográfico `tight` disponible resuelve a −0.01 px y no reproduce esta composición. No se creó una primitiva tipográfica por esa diferencia.

## Tokens y readback

Los ocho roles del [JSON de extensión](../../drafts/foundations/ai-design-system.stepper-colors.v0.1.0.json) existen en la colección local `semantic`, con nombres, descripciones, scopes y aliases coincidentes en los cuatro modos. Todos los colores de la familia resuelven al RGB fuente; ninguna primitiva nueva. La lectura recursiva de los dos sets encontró **122/122 pinturas visibles con binding**, cero pinturas sin variable y cero cruces entre `background`, `shape`, `icon` y `text`. Los 54 textos tienen sus cuatro propiedades de familia, peso, tamaño e interlineado vinculadas: 216/216 bindings tipográficos previstos. Los 54 trackings −2 % son la excepción literal documentada. No hay reacciones añadidas.

## Límites

La etiqueta `Caption` conserva neutral/400 original y su contraste sobre blanco queda marcado `*` para revisión interna; no se oscureció. La biblioteca Figma no implementa navegación, paso actual calculado, accesibilidad de teclado ni anuncios de estado. `Default` se mantiene como nombre fuente sin afirmar que siempre signifique “paso actual”. Este QA no sustituye auditoría humana.
