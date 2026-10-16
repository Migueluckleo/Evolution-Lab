# Preparación del release 0.2.1

Estado: PREPARED, no publicado ni instalado. Las órdenes siguientes se ejecutan solo después de que root libere el corte de fuentes y termine o registre expresamente el QA aplicable por destino. Figma sigue IN_PROGRESS y los 103 rangos escalados siguen BLOCKED. Publicar el paquete no convierte ese consumo en VALIDATED. Ninguna orden de este plan modifica Figma ni ejecuta Graphify.

La versión actual leída es 0.2.0. El comando de publicación exacto es `scripts/ds skills sync --bump patch --json`; la CLI no tiene `--version`. Con fuentes cambiadas produce 0.2.1. Antes se comprueba que current siga en 0.2.0, que no exista 0.2.1 y que el fingerprint corresponda al candidato probado. Si esas condiciones cambian, detenerse; no borrar ni sobreescribir releases históricos.

## Resultado de la preparación

- Auditoría independiente: 43 familias, 44 MD de consumo, 79 estilos, 360 filas, 3351 nodos/3353 rangos UI, 528 enlaces y 226 hashes: PASS documental. 103 rangos conservan su bloqueo, cuatro familias N/A justificadas.
- Los 15 archivos del freeze anterior siguen idénticos.
- Único archivo fuente adicional corregido: `skills/contpaqi-po-prototypes/scripts/verify-offline.mjs`. La comprobación final exige el catálogo 0.1.1, base foundation, enmienda de formato, transversal y las enmiendas de las cinco familias del fixture.
- Verificación enfocada del código real de esa comprobación: 13 casos sintéticos PASS. No son build ni evidencia de navegador/Figma.
- Los únicos 0.1.0 restantes encontrados en scripts son referencias históricas conservadas o fixtures negativos; el generador web y los defaults del QA actual ya apuntan a 0.1.1.

## 1. Preflight después de liberar el corte

Desde la raíz del repositorio:

```bash
set -euo pipefail
export PATH="/Users/miguel.leo/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin:$PATH"
export PYTHONDONTWRITEBYTECODE=1
mkdir -p qa/skills/release-0.2.1
python3 /tmp/typography-release-0.2.1-preflight.py "$PWD" > qa/skills/release-0.2.1/documentary-preflight.json
scripts/ds check --docs-only --json --report qa/skills/release-0.2.1/docs-only.json
NODE_BINARY="$(command -v node)" PYTHONPATH=tests python3 -m unittest test_ds_skills.HandoffTypographyTests -v > qa/skills/release-0.2.1/handoff-unit.log 2>&1
node --check skills/contpaqi-po-prototypes/scripts/verify-offline.mjs
node /tmp/verify-offline-source-gate-0.2.1.mjs "$PWD" > qa/skills/release-0.2.1/offline-gate-unit.json
```

El preflight tiene un control del freeze anterior: si root cambió posteriormente alguno de esos 15 archivos, informa la diferencia y revisa ese cambio antes de usarlo como evidencia. No elimines el control ni alteres hashes para fabricar PASS.

## 2. Candidato temporal de ambas skills y pruebas reales

Se usa el generador de paquetes existente para construir ambas carpetas/ZIP en `/tmp` con versión candidata 0.2.1. No toca current ni el historial. El candidato todavía no es un release publicado.

```bash
SKILLS_QA_ROOT="$(mktemp -d /tmp/contpaqi-skills-0.2.1-XXXXXX)"
export SKILLS_QA_ROOT
python3 - <<'PY'
from pathlib import Path
import os, sys, json
sys.path.insert(0, 'scripts')
import ds_skills as ds
state=ds.inputs()
current=ds.current_record(state)
assert current['version']=='0.2.0', current
assert not Path('output/skills/0.2.1').exists(), 'Historical release collision'
assert current['input_digest']!=state['input_digest'], 'No changed inputs: do not invent a bump'
expected,manifest=ds.expected_release(state,'0.2.1')
base=Path(os.environ['SKILLS_QA_ROOT'])/'0.2.1'
base.mkdir()
for relative,value in expected.items():
    target=base/relative
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(ds.content(value))
assert not ds.inspect_tree(base,expected)
assert ds.inputs()['input_digest']==state['input_digest'], 'Sources changed during candidate creation'
Path('qa/skills/release-0.2.1/candidate-location.json').write_text(json.dumps({'directory':str(base),'input_digest':state['input_digest'],'ds_digest':state['ds_digest'],'status':'CANDIDATE_NOT_PUBLISHED'},indent=2)+'\n')
PY
python3 "$SKILLS_QA_ROOT/0.2.1/contpaqi-figma-screens/scripts/verify_snapshot.py" > qa/skills/release-0.2.1/snapshot-validation.log
node "$SKILLS_QA_ROOT/0.2.1/contpaqi-po-prototypes/scripts/test-inline-export.mjs" > qa/skills/release-0.2.1/inline-export.log
PLAYWRIGHT_CHANNEL=chrome node "$SKILLS_QA_ROOT/0.2.1/contpaqi-po-prototypes/scripts/verify-offline.mjs" "$SKILLS_QA_ROOT/0.2.1/contpaqi-po-prototypes" "$PWD/implementations/web/node_modules" "$SKILLS_QA_ROOT/offline" > qa/skills/release-0.2.1/offline.log 2>&1
```

El directorio offline debe ser nuevo. Reutiliza las dependencias existentes compatibles; no instala paquetes ni navegador. Si el sandbox impide abrir Chrome, registrar la limitación real y usar únicamente la escalación disponible y autorizada; no convertirla en PASS. No iniciar un servidor como sustituto de file://.

Resultado exigido: 14 estados/viewports, diez instancias, apertura del HTML movido y renombrado, recursos condicionales, Enter/Escape, regreso y edición; cero HTTP(S), errores, imágenes rotas o texto sin identificar. El MD debe conservar bloque JSON autosuficiente, medidas y fuentes con hashes. El fixture comprueba cinco familias; no valida visualmente las 43 ni consume en navegador los cuatro nuevos IDs UNDERLINE. Esos cuatro IDs tienen pruebas unitarias de handoff y el QA de recetas web por separado.

Inspeccionar las capturas pertinentes y el MD; registrar el alcance real de esa inspección. No copiar los PASS visuales del release anterior. Completar `brief.json` del candidato con estados y limitaciones reales —futura pantalla Figma NOT_RUN; bloqueo solo de consumidores afectados— y repetir `capture`/`handoff` cuando cambie ese brief:

```bash
(cd "$SKILLS_QA_ROOT/offline" && PLAYWRIGHT_CHANNEL=chrome node scripts/capture.mjs && node scripts/handoff.mjs)
```

Conservar la entrega completa en `output/qa/skills-0.2.1/` o en un ZIP verificable; si QA contiene un índice al MD, enlazar la entrega completa. No copiar aisladamente el Markdown con enlaces relativos a carpetas ausentes. El snapshot duplicado puede omitirse solo si se documenta su recuperación exacta del release por digest. Registro y QA de skills están excluidos del fingerprint; otros archivos de QA de implementación no lo están.

## 3. Publicación exacta después del candidato satisfactorio

```bash
python3 - <<'PY'
import os, sys, json
from pathlib import Path
sys.path.insert(0,'scripts')
import ds_skills as ds
manifest=json.loads((Path(os.environ['SKILLS_QA_ROOT'])/'0.2.1/manifest.json').read_text())
state=ds.inputs()
assert ds.current_record(state)['version']=='0.2.0'
assert not Path('output/skills/0.2.1').exists()
assert state['input_digest']==manifest['input_digest'], 'Candidate no longer matches final sources'
PY
scripts/ds skills sync --bump patch --json > qa/skills/release-0.2.1/sync.json
cmp "$SKILLS_QA_ROOT/0.2.1/manifest.json" output/skills/0.2.1/manifest.json
scripts/ds skills check --json > qa/skills/release-0.2.1/check.json
scripts/ds skills export --bump patch --json > qa/skills/release-0.2.1/export.json
python3 - <<'PY'
import json
from pathlib import Path
sync=json.loads(Path('qa/skills/release-0.2.1/sync.json').read_text())
export=json.loads(Path('qa/skills/release-0.2.1/export.json').read_text())
assert sync['version']=='0.2.1' and sync['operation']=='CREATED', sync
assert export['version']=='0.2.1' and export['operation']=='UNCHANGED', export
PY
```

Las salidas serán `output/skills/0.2.1/contpaqi-figma-screens`, `contpaqi-po-prototypes`, ambos ZIP `*-0.2.1.zip`, `manifest.json` y el pointer `output/skills/current.json`. El `cmp` exige el mismo manifiesto del candidato probado. Si aparece cualquier diferencia, conservar ambos cortes y registrar el problema; nunca modificar una versión histórica para hacerla coincidir.

## 4. Instalación gestionada y registro, tras liberar el corte y completar el QA del paquete

```bash
scripts/ds skills install --skills-dir /Users/miguel.leo/.codex/skills --json > qa/skills/release-0.2.1/install.json
scripts/ds skills check-installed --skills-dir /Users/miguel.leo/.codex/skills --json > qa/skills/release-0.2.1/installed-check.json
scripts/ds skills check --json > qa/skills/release-0.2.1/check-after.json
```

Si una copia gestionada fue editada, el instalador debe rechazarla y preservarla; no sobrescribirla ni cambiar a una copia manual. Las skills antiguas quedan intactas. Registrar versión/digest, ZIP, pruebas reales, hashes, instalación y límites en `registry/skills.md` y `qa/skills/release-0.2.1/`. Root cerrará Graphify por separado; este plan no afirma CURRENT del grafo ni validación Figma.
