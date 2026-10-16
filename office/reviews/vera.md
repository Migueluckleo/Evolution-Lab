# Vera · revisión de mis directrices

Fecha: 2026-10-16. Rol: Verificadora; ejecución `/root/review_governance`. Nombre confirmado por mí en este encargo. Alcance solicitado: revisar mis directrices y proponer mejoras desde verificación. Estado: **PROPUESTAS**, no cambios adoptados en configuración ni protocolos. No modifiqué `office/config.json` ni protocolos del DS.

## Qué comprobé y qué ya está implementado

Revisé mi perfil en [config.json](../config.json), las reglas comunes y el [protocolo de oficina](../OPERATING-PROTOCOL.md), junto con [P06](../../protocols/06-QA-AND-VALIDATION.md) y [DEC-AI-TECHNICAL-CLOSURE-001](../../registry/DEC-AI-TECHNICAL-CLOSURE-001.md). Las tres directrices actuales cubren contraste, reproducción y revalidación; el protocolo ya exige independencia para cambios de flujo, evidencia y cierre técnico sin espera humana.

Implementación comprobada de esta misión: [24 pruebas de oficina](../../tests/office/test_office.py), todas PASS, sin skips; [salida](../../output/qa/office/tests.txt) y [revisión independiente](../../output/qa/office/independent-review.md). Se revalidaron el gate de evidencia de todos los resultados PASS/COMPLETED, fallos antes/después del append, estado/HTML, chat HTTP con red simulada y serialización de render frente a registros concurrentes. La documentación corregida con Atlas distingue archivos de evidencia de referencias declaradas y chat de registros frente a presencia o transmisión de tokens. Estas correcciones pertenecen al cierre de la oficina; no son todavía cambios de mis directrices.

## 1. Seleccionar comprobaciones por impacto y reutilizar evidencia válida

**Observación:** P06 §4 ya limita la repetición a controles afectados y dependientes. Mi perfil no explicita cómo decidir qué evidencia reutilizar antes de lanzar pruebas. En la revisión remota se inició un build PO adicional que se interrumpió porque el cambio solo afectaba la entrada remota; init y regresiones cubrían ese alcance. [Registro de esa prueba](../../output/qa/remote-consumption/po-build.txt). Esto identifica una oportunidad, no demuestra un ahorro cuantificado.

**Directiva propuesta para Vera:** “Antes de probar, relaciona cada requisito modificado y sus dependencias con los controles necesarios. Reutiliza evidencia solo cuando coincidan versión o hashes, configuración, entorno relevante y alcance; explica exclusiones. Amplía pruebas si cambia una dependencia, aparece un fallo o queda una incertidumbre concreta.”

**Criterio de verificación:** usar dos cambios de referencia: una corrección documental sin efecto en ejecución y un cambio de validación con efectos en persistencia. La primera no dispara build/Figma sin un criterio afectado; la segunda ejecuta controles positivos, negativos y de persistencia dependientes. Todos los controles obligatorios del alcance quedan asociados a evidencia actual o límite explícito. Comparar controles repetidos, duración y tokens solo si están medidos; no omitir controles obligatorios para mejorar una cifra.

**Medición:** ahorro y comparación de tokens **UNAVAILABLE**. Las duraciones de tests existentes son observaciones de ejecución, no una comparación de alternativas. El piloto propuesto aún no se ejecutó como experimento separado.

## 2. Mantener el ciclo defecto–corrección–revalidación acotado

**Observación:** el fallo de render posterior al guardado se reprodujo en temporal; con una plantilla ausente el llamador recibía error aunque el evento ya existía. La corrección tiene dos ramas que deben distinguirse: fallo previo sin append y fallo del panel posterior con ID persistido/aviso y recuperación por render. Las pruebas `test_invalid_template_prevents_append` y `test_panel_write_failure_returns_committed_id_and_render_recovers` cubren esas consecuencias, no solo detalles de implementación.

**Directiva propuesta para Vera:** “Por cada defecto, conserva entrada mínima, resultado esperado, resultado observado y alcance. Comunícalo directamente al responsable con una copia resumida a Eva. Tras la corrección, repite el caso y los dependientes que puedan cambiar; registra resuelto, abierto o limitado sin borrar la evidencia anterior ni repetir suites sin causa nueva.”

**Criterio de verificación:** un defecto no cambia a resuelto solo por mensaje del autor; debe tener reproducción o inspección suficiente, revisión del cambio y evidencia posterior del mismo comportamiento. Para persistencia, comprobar ausencia de escritura cuando falla antes del commit y ausencia de duplicación cuando falla después. La corrección de esta misión pasó ambos casos; eso demuestra viabilidad del mecanismo, no una reducción medida de coste.

**Medición:** defectos reproducidos/revalidados pueden contarse en cada lote; ahorro y coste total de coordinación **UNAVAILABLE**. El informe debe incluir límites cuando la reproducción no sea posible.

## 3. Cerrar por evidencia técnica sin convertir auditoría humana en trabajo pendiente

**Observación:** P06 DOC-15/§6 y la decisión de cierre ya gobiernan esto. El perfil de Vera dice “sin simular una revisión humana”, pero puede expresar más claramente que no debe solicitarla como gate rutinario. El nuevo test de decisiones PASS/COMPLETED verifica evidencia estructural, no aceptación humana ni conformidad semántica del documento enlazado.

**Directiva propuesta para Vera:** “Cierra el alcance autorizado cuando sus controles obligatorios y entregables aplicables tengan evidencia suficiente. Distingue PASS técnico, estado documental y aprobación humana explícita; conserva FAIL/BLOCKED/NOT_RUN/STALE donde corresponda. No bloquees por una auditoría humana opcional ni por un PENDING histórico aislado. Un defecto posterior reabre solo el alcance afectado.”

**Criterio de verificación:** escenario con solicitud concreta y QA suficiente cierra sin pedir confirmación humana; escenario con requisito obligatorio fallido permanece limitado aunque no haya revisión humana. Ningún escenario cambia DELEGATED_FOR_BUILD a APPROVED por silencio o equipara archivo existente con resultado comprobado. Los nuevos registros de cierre mantienen `user_audit: NOT_REQUIRED` y `human_review_policy: OPTIONAL_NON_BLOCKING`.

**Medición:** conteo de gates humanos rutinarios injustificados en los escenarios: objetivo cero; el conjunto de escenarios y sus evidencias debe fijarse antes de medir. Línea base de demoras o ahorro de tokens **UNAVAILABLE**. No se presenta una mejora cuantitativa aún.

## Propuesta de adopción y límites

Las tres frases anteriores pueden concretar las directrices del perfil Vera sin crear un nuevo protocolo ni duplicar el contenido normativo de P06. Su adopción corresponde a la integración autorizada de Eva; este archivo no altera configuración ni requisitos DS. Mantener referencias a las reglas canónicas y el registro de pruebas, en lugar de copiar listas completas en varios sitios.

No propongo nuevos monitores, servicios, revisión humana obligatoria ni ejecución de cinco agentes por defecto. La verificación independiente sigue aplicándose cuando el cambio de flujo o impacto lo exige. La revisión visual de UI y la ejecución externa continúan siendo controles separados cuando el alcance los requiera.

## Fuentes por hash

Los hashes identifican el corte leído; no son aprobación ni medición de ahorro.

```json
{
  "office/config.json": "7f44bb4fd561a999fe05eb14d25681aa020ce4026187340910b00dc3b1886baa",
  "office/OPERATING-PROTOCOL.md": "3a8f2acabbe590f808f3b1aeab6f33f38c4cb21c47d602ca019003a240927e16",
  "protocols/06-QA-AND-VALIDATION.md": "f0f0de88bc3f7f18d91eb5c60428c3fe3c1e6ccdd80ce8e5004ef3e57af8bd83",
  "registry/DEC-AI-TECHNICAL-CLOSURE-001.md": "39e61ad4424a01d6328000dae50676e30521e9d3d096754585451494a800b0cf",
  "tests/office/test_office.py": "18d90fd92de1b2aebad47f12e4c60d0a9a3535491e23b280239d6828580790ac",
  "output/qa/office/tests.txt": "a32bf53477fedad7f24e2c91a8bf8374ca3387c2111a6f222ef090d2cddf45c8",
  "output/qa/remote-consumption/po-build.txt": "a856596df9159f16f7d2e1681a737cd60cdde107bd4f8911efb962b0dadf3632"
}
```
