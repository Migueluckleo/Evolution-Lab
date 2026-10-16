"""Materialize the host's reviewed semantic extraction; writes only this run."""
import copy
import difflib
import hashlib
import json
import re
from pathlib import Path

ROOT = Path.cwd()
RUN = ROOT / 'graphify-out/runs/2026-10-15-typography-final'
OLD = ROOT / 'output/skills/0.1.0/contpaqi-figma-screens/assets/design-system'
G = json.loads((RUN / 'before/graph.json').read_text())
MANIFEST = json.loads((RUN / 'before/manifest.json').read_text())
PLAN = json.loads((RUN / 'source-plan.json').read_text())
CHUNKS = [json.loads((RUN / f'chunk-{i:02}.files.json').read_text()) for i in range(4)]
TEXT = {str(Path(f).relative_to(ROOT)): Path(f).read_text() for c in CHUNKS for f in c}
PARTS = [{'nodes': [], 'edges': [], 'hyperedges': [], 'input_tokens': 0, 'output_tokens': 0,
          'usage_status': 'UNAVAILABLE', 'usage_note': 'Legacy schema zeros are placeholders, not measured usage.',
          'deep_mode': False} for _ in CHUNKS]
OWNER = {str(Path(f).relative_to(ROOT)): i for i, c in enumerate(CHUNKS) for f in c}
NODES = {}
ROOTS = {}
REUSE = []

def norm(s): return re.sub('[^a-z0-9]', '_', s.lower())
def stem(f): return norm(str(Path(f).with_suffix('')))
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rel(s): return str(Path(s).relative_to(ROOT)) if Path(s).is_absolute() else s
def loc(f, needle):
    for i, line in enumerate(TEXT[f].splitlines(), 1):
        if needle in line: return f'L{i}'
    return None
def node(f, entity, label, description='', rationale=None, file_type='concept', at=None, **attrs):
    ident = stem(f) + '_' + norm(entity)
    if ident in NODES: return ident
    n = {'id': ident, 'label': label, 'file_type': file_type, 'source_file': str(ROOT/f),
         'source_location': loc(f, at) if at else None,
         'source_url': None, 'captured_at': None, 'author': None, 'contributor': None}
    if TEXT[f].startswith('---\n'):
        header = TEXT[f].split('---', 2)[1]
        for k in ('source_url', 'captured_at', 'author', 'contributor'):
            m = re.search(r'^'+k+r':\s*(.*)$', header, re.M)
            if m and m[1].strip() not in ('null', '~', ''): n[k] = m[1].strip().strip('\"\'')
    if description: n['description'] = description
    if rationale: n['rationale'] = rationale
    n.update(attrs); NODES[ident] = n; PARTS[OWNER[f]]['nodes'].append(n)
    return ident
def edge(f, a, b, relation='references', at=None, confidence='EXTRACTED', score=1.0):
    if a == b: return
    PARTS[OWNER[f]]['edges'].append({'source': a, 'target': b, 'relation': relation,
        'confidence': confidence, 'confidence_score': score, 'source_file': str(ROOT/f),
        'source_location': loc(f, at) if at else None, 'weight': 1.0})
def concept(f, entity, label, description='', rationale=None, at=None, **attrs):
    n = node(f, entity, label, description, rationale, 'rationale' if rationale else 'concept', at, **attrs)
    edge(f, ROOTS[f], n, 'references', at); return n

# Source checks are against the final frozen plan; no source is rewritten.
for f in TEXT:
    assert digest(ROOT/f) == PLAN['source_sha256'][f], f

def reuse(f):
    q = OLD/f
    if not q.exists() and f.startswith('skills/'):
        q = ROOT/'output/skills/0.1.0'/f.removeprefix('skills/')
    if not q.exists(): return
    before = q.read_text(); current = TEXT[f]
    md5 = hashlib.md5(q.read_bytes()).hexdigest()
    assert MANIFEST[f]['semantic_hash'] == md5, ('prior graph provenance mismatch', f)
    op = difflib.SequenceMatcher(a=before.splitlines(keepends=True), b=current.splitlines(keepends=True), autojunk=False).get_opcodes()
    changes = [(t,a,b,c,d) for t,a,b,c,d in op if t != 'equal']
    append_only = all(t == 'insert' for t,*_ in changes)
    if f in ('registry/contracts.md', 'registry/implementations.md', 'registry/sources.md', 'AGENTS.md'):
        assert append_only, (f, changes)
    allowed = append_only or '/docs/components/' in f or f in (
        'implementations/web/docs/WEB-ADAPTATION.md', 'implementations/web/src/styles.css',
        'protocols/07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md') or f.startswith('skills/')
    if not allowed: return
    retained = ''.join(before.splitlines(keepends=True)[a:b][j] for t,a,b,c,d in op if t=='equal' for j in range(b-a))
    line_map = {a+j+1:c+j+1 for t,a,b,c,d in op if t=='equal' for j in range(b-a)}
    old_nodes = [n for n in G['nodes'] if rel(n.get('source_file','')) == f and n.get('_origin') != 'ast']
    ids = {n['id'] for n in old_nodes}
    for old in old_nodes:
        n = {k:copy.deepcopy(v) for k,v in old.items() if k not in ('community','community_name','_origin','norm_label','sha256')}
        n['source_file'] = str(ROOT/f)
        m = re.fullmatch(r'L(\d+)', str(n.get('source_location')))
        if m: n['source_location'] = f'L{line_map[int(m[1])]}' if int(m[1]) in line_map else None
        span = re.fullmatch(r'L(\d+)-L?(\d+)', str(n.get('source_location')))
        if span:
            start,end = map(int, span.groups())
            mapped = [line_map.get(x) for x in range(start,end+1)]
            n['historical_source_location'] = n['source_location']
            n['source_location'] = (f'L{mapped[0]}-L{mapped[-1]}'
                if all(x is not None for x in mapped) and mapped == list(range(mapped[0],mapped[-1]+1)) else None)
        n['reuse_basis'] = 'Prior semantic extraction; source snapshot hash verified; unchanged historical content or retained concepts reviewed.'
        if n['id'] == 'implementations_web_docs_web_adaptation_document': n['label'] = 'Adaptación técnica web 0.1.5'
        assert n['id'] not in NODES
        NODES[n['id']] = n; PARTS[OWNER[f]]['nodes'].append(n)
    count = 0
    for old in G.get('links', G.get('edges', [])):
        if rel(old.get('source_file','')) != f or old.get('_origin') == 'ast': continue
        if old['source'] not in ids and old['target'] not in ids: continue
        e = {k:copy.deepcopy(old[k]) for k in ('source','target','relation','confidence','confidence_score','weight') if k in old}
        e['source_file'] = str(ROOT/f); e['source_location'] = None
        m = re.fullmatch(r'L(\d+)', str(old.get('source_location')))
        if m and int(m[1]) in line_map: e['source_location'] = f'L{line_map[int(m[1])]}'
        PARTS[OWNER[f]]['edges'].append(e); count += 1
    REUSE.append({'source_file': str(ROOT/f), 'snapshot': str(q), 'snapshot_sha256': digest(q),
        'before_semantic_md5': md5, 'current_sha256': digest(ROOT/f), 'append_only': append_only,
        'equal_sections_sha256': hashlib.sha256(retained.encode()).hexdigest(),
        'old_line_count': len(before.splitlines()), 'retained_line_count': len(retained.splitlines()),
        'changes': changes, 'semantic_nodes_reused': len(old_nodes), 'semantic_edges_reused': count})

for f in TEXT:
    reuse(f)
    existing = stem(f)+'_document'
    title = next((line.removeprefix('# ').strip() for line in TEXT[f].splitlines() if line.startswith('# ')), Path(f).name)
    ROOTS[f] = existing if existing in NODES else node(f, 'document', title, file_type='document', at=title)

T = 'implementations/web/docs/TYPOGRAPHY.md'
C = 'specs/foundations/typography.contract.v0.1.0.md'
B = 'qa/implementations/typography/Figma-blocker.md'
W = 'qa/implementations/typography/web/revision-75/README.md'
S = 'qa/implementations/typography/specimens.review.md'
Q = 'qa/contracts/typography.v0.1.0.md'
D = 'registry/DEC-TYPOGRAPHY-STYLES-001.md'
R = 'qa/skills/release-0.2.0/README.md'

for f in TEXT:
    if '/docs/components/' not in f: continue
    family = re.search(r'Familia `([^`]+)`', TEXT[f])[1]
    name = TEXT[f].splitlines()[0].removeprefix('# ').split(' · ')[0]
    n = concept(f, 'recetas_tipograficas_compartidas', f'{name}: recetas tipográficas por rol y variante',
        'La ficha consume TYPOGRAPHY.md derivada del JSON único, typography.manifest.json y typographyClass(id); '
        '--ds-type-style-id permite inspeccionar identidad efectiva. No modifica API, Slots ni aprobación visual.',
        at='Las recetas de texto', component_id=family)
    edge(f,n,ROOTS[T]); edge(f,n,ROOTS[C], 'conceptually_related_to', confidence='INFERRED', score=.95)
    if name == 'AppShell':
        x=concept(f,'heading_5_semibold_en_ejemplo','AppShellExample: título local Heading 5/Semibold',
            'La composición de ejemplo usa DS.typographyClass(heading-5-semibold); no añade una propiedad al componente AppShell.',at='export function AppShellExample')
        edge(f,x,ROOTS[T])

concept('AGENTS.md','estilos_tipograficos_compartidos','Estilos explícitos por familia y rango',
    'Cada familia nueva o modificada debe registrar mapeo, propiedades resueltas y overrides por destino y cerrar P05/P06/P07/P08. '
    'JSON gobierna propiedades, unidades y única description; no altera el inventario histórico ni revalida automáticamente familias antiguas.',at='**Estilos tipográficos compartidos:**')

f='protocols/07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md'
concept(f,'catalogo_tipografico_unico','P07 0.3.0: catálogo tipográfico único',
    'FOUNDATIONS-TYPOGRAPHY-001 y DEC-TYPOGRAPHY-STYLES-001 gobiernan estilos, unidades y description; no duplicar recetas editables en CSS, fichas o código.',at='Para tipografía aplicar')
concept(f,'verificacion_de_rangos_y_overrides','Verificar identidad y propiedades de cada texto y rango',
    'Regenerar tipografía, comprobar variantes y estados, propiedades resueltas y overrides; clases o IDs aislados no acreditan conformidad.',at='2. Regenerar tokens')
concept(f,'cierre_de_skills_con_tipografia','P07/P08: sincronizar catálogo y consumidores en ambas skills',
    'Cada cambio de familia documenta mapeo y complementarios justificados, QA por destino y mismo corte versionado de las dos skills.',at='6. Actualizar catálogo')

f='implementations/web/docs/WEB-ADAPTATION.md'
concept(f,'tipografia_centralizada','Tipografía centralizada: JSON a CSS, TypeScript y documentación',
    '75 estilos generados; interlineado PERCENT relativo, tracking PERCENT en em, PIXELS en px y AUTO normal. '
    'Recetas por rol/variante, marker inspeccionable y API typographyClass/typographyIds/TypographyId.',at='## Centralización tipográfica')
concept(f,'correcciones_tipograficas_contextuales','Recetas contextuales preservan composición y semántica',
    'Tracking 0.1% de Button con contexto Modal/EmptyStates a cero; AUTO en Avatar/Dot/Header/NavigationTab/Sidebar; '
    'pesos específicos de Textarea/Pagination/Gauge/Conversation. El título AppShellExample es contenido local.',
    'No forzar la escala base por tamaño ni inferir conformidad desde un marker heredado.',at='La migración conserva cajas')
concept(f,'corte_75_independiente','Revisión 75: tres clases adicionales sin reasignar consumidores web',
    '9 tests de generador, dos pruebas Chrome, 300 recetas y 2956 textos; mediciones de consumidores idénticas al corte72. Suite61 histórica no repetida.',at='## Recetas escaladas')

canonical=concept(T,'catalogo_canonico_referenciado','Catálogo canónico tipográfico 0.1.0 referenciado',
    'La tabla generada cita el JSON único como propietario editable de nombres, métricas y descripciones; no es una segunda autoridad.',
    at='Fuente única:',reference_path='specs/tokens/ai-design-system.typography.v0.1.0.json',
    referenced_sha256='2b47811d3175b801f41e32e3bb174060697e7c265053741541bf7e602700afed')
base=concept(T,'base_18','Escala base de 18 estilos Manrope',
    'Jerarquía de texto local desde Heading1 hasta Caption; propiedades y description proceden del JSON único.',at='## Estilos base',authority='DERIVED_NOT_AUTHORITY')
extra=concept(T,'compatibilidad_57','57 estilos de compatibilidad para roles existentes',
    '54 recetas preservadas y tres derivados materializados; no elegir por coincidencia de tamaño ni extender como escala general.',at='## Estilos complementarios',authority='DERIVED_NOT_AUTHORITY')
concept(T,'conversion_css','Conversión de unidades y consumo font/tracking',
    'Cada receta exporta family/weight/size/line-height/tracking/font; font shorthand requiere tracking aparte. '
    'PERCENT de línea relativo, tracking em, PIXELS px y AUTO normal; identidad inspeccionable no prueba binding Figma.',at='Cada receta exporta')
STYLES={}
section='base'
for line in TEXT[T].splitlines():
    if line.startswith('## Estilos complementarios'): section='complementary'
    if not line.startswith('| ') or '`ds-type-' not in line: continue
    cols=[x.strip() for x in line.strip('|').split('|')]
    sid=re.search(r'`ds-type-([^`]+)`',cols[-1])[1]
    n=node(T,sid,cols[0],cols[5],file_type='concept',at=line,
        authority='DERIVED_NOT_AUTHORITY',category=section,style_id=sid,
        observed_documented_recipe={'font':cols[1],'size':cols[2],'lineHeight':cols[3],'tracking':cols[4]},
        token_references=re.findall(r'`([^`]+)`',cols[6]))
    STYLES[sid]=n;edge(T,base if section=='base' else extra,n,'references');edge(T,n,canonical,'references')
assert len(STYLES)==75
for sid in ('ui-checkbox-label-scaled-two-thirds','ui-checkbox-label-scaled-five-sixths','micro-count-small-scaled-four-thirds'):
    origin='micro-count-small' if sid.startswith('micro') else 'ui-body-compact'
    edge(T,STYLES[sid],STYLES[origin],'references',at='| '+sid+' |')
concept(T,'escala_materializada_sin_doble_aplicacion','Recetas materializadas: no aplicar de nuevo la escala',
    'Float32(base × Float32(ratio)); recipeScale=1 conserva instancia escalada y usa las métricas finales del catálogo.',at='## Recetas de escala materializada')

f='implementations/web/src/styles.css'
groups={}
for sel,body in re.findall(r'([^{}]+)\{([^{}]*)\}',TEXT[f]):
    m=re.search(r'--ds-type-style-id\s*:\s*([\w-]+)',body)
    if m:groups.setdefault(m[1],[]).append(sel.strip())
for sid,sels in groups.items():
    n=concept(f,'consumidores_'+sid,'Consumidores CSS de '+sid,
        'Selectores de rol/variante consumen font y tracking de la receta generada y declaran --ds-type-style-id.',
        at='--ds-type-style-id:'+sid,selectors=sels,style_id=sid)
    assert sid in STYLES,sid
    edge(f,n,STYLES[sid],'references')
concept(f,'line_height_cero_geometrico','Wrappers de indicadores conservan line-height:0',
    'ds-icon-count y ds-avatar-status usan cero como geometría del wrapper; no constituyen una receta tipográfica de texto.',at='.ds-icon-count')

concept(D,'delegacion_especifica','Delegación específica: 18 base y complementarios necesarios',
    'Documentar e integrar en AI-Design-System y comprobar consumidores; DELEGATED_FOR_BUILD, auditoría humana PENDING, sin publicación remota.',
    'Preservar recetas compactas cuando imponer la base cambie geometría o contrato sin necesidad.',at='El usuario solicita')
concept(D,'derivados_necesarios','Tres complementarios derivados preservan 103 rangos escalados',
    'Resolución técnica DERIVED, no aprobación humana; instanceScale y recipeScale separados; no primitivas fraccionarias.',at='## Complementarios derivados')
concept(D,'bindings_aditivos_permitidos','Adiciones canónicas verificadas a estilos reutilizados',
    '244 rangos/242 nodos/17 estilos/1202 referencias añadidas; sin pérdida, reemplazo o referencias ajenas. Preservación PASS, igualdad literal FAIL conservada.',at='## Preservación con bindings')

concept(C,'autoridad_json_y_contrato','FOUNDATIONS-TYPOGRAPHY-001: MD gobierna reglas, JSON datos',
    'Catálogo 75 con única description; 18 base para texto local nuevo, 57 complementarios compatibilityOnly para usos existentes. '
    'Contrato DELEGATED_FOR_BUILD; user_audit PENDING; Slots NOT_APPLICABLE a estilos.',at='## 2. Fuentes')
concept(C,'consumidores_explicitos','Estilo explícito y métricas resueltas por texto o rango',
    'Censo incluye variantes, contenido oculto, instancias y rangos mixtos. ID de estilo con overrides incompatibles no satisface REQ-TYP-004.',at='## 8. Integración')
concept(C,'preservacion_y_excepciones','Preservación de anatomía, contenido y geometría',
    'No normalizar tamaños/alturas por clasificación, no modificar Slots ni colores. Complementarios requieren rol, contrato, observación y motivo.',at='## 3. Cobertura')
concept(C,'codificacion_float32','Comparación exacta de codificación float32 por propiedad',
    'Interlineado Figma Math.fround(p/100)×100; tracking histórico float32 directo cuando procede. JSON y CSS canónicos no cambian; ningún epsilon posterior.',at='### Representación numérica')
concept(C,'escalas_instance_recipe','instanceScale preservada y recipeScale=1 para derivados',
    'Tres recetas materializan Float32(base×Float32(ratio)), conservan porcentajes y omiten bindings sin escalar que restablecerían métricas.',at='### Derivados necesarios')
concept(C,'bindings_244','Excepción acotada de bindings aditivos canónicos',
    '244 rangos de 242 nodos sobre 17 estilos originales: identidad, scope, aliases y cuatro modos comprobados; no exime de migración pendiente.',at='La actualización autorizada')
for line in TEXT[C].splitlines():
    if line.startswith('| REQ-TYP-') or line.startswith('| AC-TYP-'):
        cols=[x.strip() for x in line.strip('|').split('|')]
        concept(C,cols[0],cols[0]+' · '+cols[1],'; '.join(cols[2:]),at=cols[0])

scope_data=[('styles_pass','Estilos Figma PASS: 75 / 304 bindings / 1216 resoluciones',
            'Readback técnico independiente; no acredita consumo global.', 'PASS'),
           ('documentation_pass','Typography 1003:412: documentación PASS',
            '75 tarjetas, 316 textos y 79 frames; cobertura técnica separada de inspección visual.', 'PASS'),
           ('preservation_pass','Preservación acotada PASS con adiciones canónicas',
            '34 páginas, 3501 nodos y 3503 rangos; métricas/contenido/propiedades capturadas/IDs originales preservados con 244 rangos de bindings aditivos.', 'PASS'),
           ('literal_fail','Restauración literal FAIL histórico',
            '244 diferencias aditivas de boundVariables; el reporte estricto permanece sin sobrescritura.', 'FAIL'),
           ('consumer_blocked','Consumidores Figma BLOCKED',
            'Propagación observada de TextStyles entre textos con componentPropertyReferences; causa interna UNRESOLVED. Catálogo y mapping no prueban migración.', 'BLOCKED'),
           ('web_pass','Web PASS acotado: 43 familias, 75×4 recetas, 2956 textos',
            'Evidencia Chrome por destino; no valida Figma, otros motores ni composiciones arbitrarias.', 'PASS')]
for f in (C,D,Q,'qa/implementations/typography.v0.1.0.review.md','registry/implementations.md'):
    for ent,label,desc,status in scope_data:concept(f,ent,label,desc,status=status,scope='typography_0.1.0')

concept(Q,'qa_catalogo75','QA documental PASS para catálogo75 y reglas de consumo',
    '75 identidades/descripciones; 243 referencias a 68 archivos; 207 recetas citadas y 290 referencias a nodos; 304 refs y 1216 resoluciones canónicas. '
    '103 rangos derivados contrastados. Procedencia observada no es aprobación humana.',at='## Comprobaciones ejecutadas sobre los 75')
concept(Q,'base_historica18','QA base18 conservado como subconjunto histórico',
    'BASE y BASE-FIGMA retienen los hashes del corte18; el catálogo ampliado tiene su hash distinto. No valida consumidores.',at='## Readback de los 18')

concept(B,'propagacion_reproducible','Propagación reproducida entre textos con propiedades compartidas',
    'Lectura inmediata retry60 pasó; posterior conjunto mostró78 errores en39 textos. Desvincular referencias mantuvo60 estilos; revincular o propiedad común nueva dejó45 fallos.',
    'Una lectura favorable dentro del bucle no acredita estabilidad tras todas las asignaciones.',at='## Pruebas de aislamiento',status='BLOCKED')
concept(B,'reparacion_no_validada','Ninguna propuesta de sustitución de Text lista',
    'Copia con textos reemplazados falló12 verificaciones en6 de60; definiciones preservadas y originales intactos. Limpieza364+374 IDs temporales documentada.',at='El último [ensayo',status='FAIL')
concept(B,'preservacion_no_migracion','Restauración completa y diferencia aditiva explícita',
    '3501 fingerprints iguales y3503 IDs previos; preservaciónPASS con244 diferencias aditivas/1202 refs. LiteralFAIL y consumerMigrationBLOCKED permanecen.',at='## Restauración completa')
concept(B,'escala_problema_distinto','Tres derivados escalados no resuelven propagación de propiedades',
    '14 rangos a2/3,76 a5/6,13 a4/3; recipeScale=1. Herencia del Count mantuvo medidas pero textStyleId vacío.',at='## Las tres recetas')
concept(B,'revalidacion_final','Leer todo el conjunto después de una solución autorizada',
    'Comparar contenido, IDs, propiedades, overrides, bindings, rangos ocultos, métricas e instancias tras la última escritura.',at='## Decisión y condiciones')

concept(S,'readback75cards','Typography: cuatro tableros y 75 tarjetas PASS',
    'Página1003:412; tableros1006:292,387,487,587;18+19+19+19estilos;316textos79frames. DescripcionesBodyRegular14 y variables semánticas.',at='## Fuente y cobertura técnica')
concept(S,'visual_dos_muestras','Inspección visual acotada a Heading1Bold y BodyRegular',
    'Tarjetas1006:297 y1006:367 legibles sin recortes/solapes en las dos capturas inspeccionadas. No se revisaron75capturas ni cuatrotableros completos.',at='## Inspección visual realizada')
concept(S,'radios_falso_negativo','Falso negativo inicial: cuatro bindings de esquina',
    'READBACK_FAILED histórico75errores permanece. Verificador corregido para topLeft/topRight/bottomLeft/bottomRightRadius VariableID13:6=8px; readback posteriorPASS sin nueva mutación.',at='## Falso negativo')

f='qa/implementations/typography/web/README.md'
concept(f,'historical72','Corte histórico72: suite61 PASS y 288 recetas',
    '8testsPython9unitarias;20860comprobaciones43familias;2956textos;717reglas no tipográficas idénticas. SHA0c5f6cf... corresponde al corte72.',at='## Resultados',temporal_scope='historical_72_styles')
concept(f,'visual_scope','Visual web limitado a Header y Conversation',
    'Chrome con Manrope local; noFigma,otrosmotores,WCAGcompleto ni Slotsarbitrarios. Capturas disponibles no implican inspecciónmanual.',at='Inspección visual manual')
concept(W,'revision75','Revisión75 PASS en300recetas y2956mediciones',
    '18base57complementos;9testsPython2Chrome, determinismo/typecheck/build;consumidores y cincohashes idénticos al corte72. Suite61no repetida.',at='| Comprobación ejecutada')
concept(W,'exact_float32','Literales completos float32 y precisión CSS observada',
    'Generador valida Float32(base×Float32(ratio)); recetas ya resueltas sin segundaescala. getComputedStyle tiene precisión propia; literales completos probados aparte.',at='CSS conserva literalmente')

f='qa/implementations/skills.typography-handoff.v0.1.0.review.md'
concept(f,'identity_transport','PASS de captura y transporte de identidad tipográfica',
    'Fixture local con valores/placeholders; IDdesconocido rechazado; texto sinmarkerPARTIAL; esquema previoNOT_RUN. metric_validationNOT_PERFORMED.',at='## Comprobación ejecutada')
concept(f,'historical_scope','Fixture anterior72 no es release ni QA Figma',
    'No regresióncompleta14 en este informe; noexportación/instalación ni conformidadmétrica. Rutas temporales identifican ejecución sin garantizarretención.',at='## Evidencia y límites')

concept(R,'release_020_current','Skills0.2.0: paquetes e instalación CURRENT',
    '1694fuentes43familias; snapshotcomún f3d8dc4b...;syncminorcreado,checkCURRENT,exportUNCHANGED; dos skills gestionadas actualizadas.',at='**Paquetes e instalación:')
concept(R,'offline_14_pass','HTMLautónomo PASS:14estados/viewports10instancias',
    'file://aislado sinred;0requestsHTTP/errores/imágenesrotas/textos sinmapear;Manrope yassets condicionales verificados. HTML3657587bytes.',at='El HTML de')
concept(R,'identity124','124fragmentos y8IDs tipográficos IDENTIFIED',
    'Handoff preserva IDs yhashes; metric_validation no realizada por capture. No equivale a conformidadmétrica ni aplicaciónFigma.',at='`typography.status: IDENTIFIED`')
concept(R,'visual2','Dos muestras visuales inspeccionadas',
    'Media1440×900 ySideBySide1000×760;otras12capturas no inspeccionadas manualmente. PantallaFigmaNOT_RUN;consumidoresBLOCKED.',at='| Revisión visual')
concept(R,'preservation_legacy','Legacy skills, inventario e índiceGit preservados',
    '1900archivosPOC y462HTML con hashesbaselineidénticos;inventario históricointacto;673eliminaciones preparadas yhashíndiceestable.',at='El método de hash')

f='qa/skills/release-0.2.0/replicar-en-figma.md'
concept(f,'indice_qa_no_entrega','ÍndiceQA: entrega original completa preservada',
    'MDoriginal,HTML yrelativos residen output/qa/skills-0.2.0; ZIPpreserva mismosbytes,14PNG yfixture, DSduplicadorecuperable delrelease. Índiceno alteraentrega.',at='Este archivo es un índice')
concept(f,'handoff_scope','Handoff14estados124fragmentos conserva FigmaBLOCKED',
    'Entregaautosuficiente deprototipoweb; prueba no construyópantallaFigma.',at='El handoff registra')

f='registry/contracts.md'
concept(f,'foundations_typography_001','FOUNDATIONS-TYPOGRAPHY-001 registrado como DELEGATED_FOR_BUILD',
    'Contrato0.1.0+JSONcanónico+QA documental;auditoríahumanaPENDING; contratoshistóricos conservan alcance.',at='## FOUNDATIONS-TYPOGRAPHY-001')
f='registry/sources.md'
concept(f,'src_typography_reference_001','SRC-TYPOGRAPHY-REFERENCE-001: imagenoriginal18estilos',
    'SHA52053d2a...conservado; descripcionesdeuso son redaccióndelegada, no textoatribuidoalaimagen.',at='## SRC-TYPOGRAPHY-REFERENCE-001')
concept(f,'src_typography_figma_census_001','SRC-TYPOGRAPHY-FIGMA-CENSUS-001:34páginas3501textos3503rangos',
    'OBSERVED incluidostextosocultos; schema2columns/paths/names/recipes. Firmasdobles no son hashescriptográficos nicopiaFigma completa.',at='## SRC-TYPOGRAPHY-FIGMA-CENSUS-001')
f='registry/skills.md'
concept(f,'historical_release_010','Release0.1.0 histórico:1373fuentes43familias',
    'Dosnuevasskills;35tests;14capturas;FigmaNOT_RUN; anterioresconservadas. Corte2026-10-14con digest05f59b...',at='## 0.1.0',temporal_scope='historical_0.1.0')
concept(f,'release_020','Release0.2.0:1694fuentes43familias CURRENT',
    'Ambasskills exportadaseinstaladas;catálogo75+QAweb+bloqueoFigma.14estados10instancias124fragmentos;0.1.0intacto.',at='## 0.2.0')
concept(f,'release_cycle_avoided','Registro y QA excluidos del snapshot para evitar autorreferencia',
    'CierresP07/P08mismafuente; cambios efectivosotroversión;instaladorgestionadoprotegeedicionesajenas;compartirZIPnoactualizaotrasmáquinas.',at='## Mantenimiento')

# Skill instructions: extract the actual portable workflow and its safety/authority limits.
for f in [x for x in TEXT if x.startswith('skills/')]:
    concept(f,'typography_blocked_scope','Catálogo75 disponible; consumoFigmaexistenteBLOCKED',
        'Leer FOUNDATIONS-TYPOGRAPHY-001, registry/contracts y Figma-blocker antesdeconstruir; preservar limitación; QAwebnoacredita consumoFigma.',at='BLOCKED')
    concept(f,'materialized_scale','Tresderivados ya materializan laescala',
        'ui-checkbox-label-scaled-two-thirds/five-sixths y micro-count-small-scaled-four-thirds: recipeScale1; conservarinstanceScale; no dobleescala ni másderivados porparecido.',at='derivedFrom')
    if f.endswith('design-system.md'):
        concept(f,'portable_authority','Snapshotportable yautoridadporcontrato/enmienda',
            'Índiceyhasheslocalizanfamilias; MarkdownreglasJSONcamposdelegados; observacionesnoaprueban; noeditarsnapshotniarchivo maestro.',at='# ')
        concept(f,'style_roles','Baseparanuevotexto ycompatibilidadpara usosdocumentados',
            'Conservarrecetasexistentes ytokenssemánticos; no aislarmétricas; respetar unidades,aliases,BENI/NAVIfijo yassetsoriginales.',at='complementarios')
    if f.endswith('figma-workflow.md'):
        concept(f,'local_editable_workflow','Composicióneditable conmapasdeIDs yAutoLayout',
            'Inspecciónprevia, imports porclavesleídas, estilosfuentesreales,instancias/Slots,reacciones yreadbackfinal. Mutaciónsolo enprototipoautorizado.',at='## Componer pantallas')
        concept(f,'no_structural_repair','La skill no autoriza reparar maestros ni eliminar propiedades',
            'No sustituirnodosmaestros,desacoplarinstanciasni quitarpropiedadespúblicasparaeludirbloqueo. Leerconjunto afectadodespuésúltimaescritura.',at='No repares el bloqueo')
    if f.endswith('handoff-and-qa.md') or f.endswith('/handoff.md'):
        concept(f,'md_self_contained','MDautosuficiente schema1 admite copia pegadacompleta',
            'JSONembebido transporta fuentes/hash,jerarquía,parent/order,props/estados,medidas,tokens,Slots,decisionesylímites; JSONexterno/HTML/PNGopcionales.',at='Markdown')
        concept(f,'identified_not_conformant','Identidadtipográfica IDENTIFIED no es conformidadmétrica',
            'Marker efectivo --ds-type-style-id,text_runs,control-values/placeholders; IDheredadopuedeconvivir conoverride; compararrecetaymétricasantesFigma.',at='IDENTIFIED')
        concept(f,'local_content','Contenido local ycomposiciones conidentidadpropia',
            'local-content título/texto/adornos requierenmotivo,tokens,caja yorden; local-composition refierepiezasDS; no inventarfamilianiprincipal.',at='local-content')

# References are added only to nodes that exist in this extraction or the actual before graph.
old_by_file={}
for n in G['nodes']: old_by_file.setdefault(rel(n.get('source_file','')),[]).append(n)
def target_for(path):
    if path in ROOTS: return ROOTS[path]
    ns=old_by_file.get(path,[])
    if not ns:return None
    ns=sorted(ns,key=lambda n:(not n['id'].endswith('_document'),n.get('_origin')!='ast',n['id']))
    return ns[0]['id']
for f,s in TEXT.items():
    for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)',s):
        href=m[1].split('#')[0]
        if not href or '://' in href or href.startswith(('mailto:','data:')):continue
        p=(ROOT/f).parent/href
        try: p=str(p.resolve().relative_to(ROOT))
        except ValueError: continue
        t=target_for(p)
        if t:edge(f,ROOTS[f],t,'references',at=m[0])
    # Backtick paths in portable skill instructions are explicit citations, not inferred endpoints.
    if f.startswith('skills/'):
        for p in re.findall(r'`((?:specs|registry|qa|sources|implementations)/[^`]+)`',s):
            t=target_for(p)
            if t:edge(f,ROOTS[f],t,'references',at=p)

# Keep cross-destination facts connected without merging their distinct status scopes.
for f in (C,D,Q,'qa/implementations/typography.v0.1.0.review.md','registry/implementations.md'):
    for ent,target in [('consumer_blocked',B),('documentation_pass',S),('web_pass',W)]:
        edge(f,stem(f)+'_'+ent,ROOTS[target])

old_ids={n['id'] for n in G['nodes']}
all_ids=set(NODES)|old_ids
checks=[]
for i,part in enumerate(PARTS):
    # Match the schema; no merged graph statistics or prior output hashes are carried over.
    unique={}
    for e in part['edges']:
        assert e['source'] in all_ids and e['target'] in all_ids,(i,e)
        assert (e['confidence']=='EXTRACTED' and e['confidence_score']==1) or (e['confidence']=='INFERRED' and e['confidence_score'] in [.95,.85,.75,.65,.55]) or (e['confidence']=='AMBIGUOUS' and .1<=e['confidence_score']<=.3)
        k=(e['source'],e['target'],e['relation'])
        if k not in unique:unique[k]=e
    part['edges']=sorted(unique.values(),key=lambda e:(e['source'],e['target'],e['relation']))
    part['nodes'].sort(key=lambda n:n['id'])
    assert set(n['source_file'] for n in part['nodes'])==set(CHUNKS[i])
    assert len({n['id'] for n in part['nodes']})==len(part['nodes'])
    assert all(re.fullmatch('[a-z0-9_]+',n['id']) for n in part['nodes'])
    assert all(n['id'].startswith(stem(rel(n['source_file']))+'_') for n in part['nodes'])
    checks.append({'chunk':i,'files':len(CHUNKS[i]),'nodes':len(part['nodes']),'edges':len(part['edges']),'hyperedges':0,
                   'coverage':'PASS','ids':'PASS','endpoints':'PASS','confidence':'PASS','usage_status':'UNAVAILABLE'})
    (RUN/f'chunk-{i:02}.json').write_text(json.dumps(part,ensure_ascii=False,indent=2)+'\n')
(RUN/'documents-reuse-provenance.json').write_text(json.dumps({'files':REUSE,'source_plan_verified':True,'usage_status':'UNAVAILABLE'},ensure_ascii=False,indent=2)+'\n')
(RUN/'documents-extraction-checks.json').write_text(json.dumps({'chunks':checks,'unique_ids':len(NODES),'source_files':len(TEXT),'global_consumer_figma':'BLOCKED'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(checks,ensure_ascii=False))
