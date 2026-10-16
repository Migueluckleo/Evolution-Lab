"""Adaptación determinista a CSS. Los valores editables siguen en los JSON del DS."""
import hashlib, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
WEB = Path(__file__).resolve().parents[1]
BASE = 'sources/inventories/tokens.inventory.json'
BASE_SHA = 'cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474'
MODES = ['Contable','Administrativo','Servicios','Personas']
# Orden explícito de alcance: bases primero; enmiendas que sustituyen campos después.
FOUNDATIONS = ['avatar-roles.v0.1.0','breadcrumb-current-text.v0.1.0','chart-colors.v0.1.0','control-colors.v0.1.0','dot-background-colors.v0.1.0','dot-inactive-border.v0.1.0','empty-states.v0.1.0','focus-effects.v0.1.0','header-release.v0.1.0','icon-button-backgrounds.v0.1.0','linear-progress-colors.v0.1.0','metric-card-roles.v0.1.0','navigation-pagination-border.v0.1.0','navigation-tab-borders.v0.1.0','navigation-tab-colors.v0.1.0','pagination-slot-state.v0.1.0','radio-indicator-colors.v0.1.0','scrollbar-colors.v0.1.1','sidebar.v0.1.0','stepper-colors.v0.1.1','steps-colors.v0.1.1','avatar-roles.v0.1.1','control-colors.v0.1.1','dot-inactive-border.v0.1.1','feedback-icon-scopes.v0.1.0','warning-icon-contrast.v0.1.1']
SOURCES = [BASE]+['drafts/foundations/ai-design-system.'+n+'.json' for n in FOUNDATIONS]+['specs/tokens/ai-design-system.'+n+'.json' for n in ['inverse-icon.v0.1.0','six-family-color.v0.1.0','character-identity.v0.1.0','character-shadow.v0.1.0']]+['sources/inventories/ai-design-system.fuentes-hover.v0.1.0.json']
def css_name(collection, name):
    prefix = 'primitive-' if collection == 'primitive' else ''
    return '--ds-'+prefix+re.sub(r'[^a-zA-Z0-9-]', '-', name).lower()
def build():
    tokens, ids, hashes = {}, {}, {}
    mode_names = {f'6:{i}':m for i,m in enumerate(MODES)} | {m:m for m in MODES} | {'Value':'Value'}
    def add(v, collection, source):
        key=(collection,v['name'])
        v=dict(v,collection=collection,source=source)
        raw_values=v.get('valuesByMode') or {k:dict(x,type='VARIABLE_ALIAS',name=x.get('name',x.get('primitiveName'))) for k,x in v['aliasesByMode'].items()}
        v['values']={mode_names.get(k,k):x for k,x in raw_values.items()}
        tokens[key]=v
        for field in ['id','targetId']:
            if v.get(field): ids[v[field]]=key
    for source in SOURCES:
        raw=(ROOT/source).read_bytes(); hashes[source]=hashlib.sha256(raw).hexdigest();d=json.loads(raw)
        if source==BASE:
            assert hashes[source]==BASE_SHA,'El inventario canónico cambió; revisar el mapeo.'
            for c in d['collections']:
                mode_names.update({m['modeId']:m['name'] for m in c['modes']})
                for v in c['variables']: add(v,c['name'],source)
            continue
        coll=d.get('collection','semantic');coll=coll if isinstance(coll,str) else coll['name']
        for v in d.get('variables',[]): add(v,v.get('collection',coll),source)
        if 'variableName' in d:
            v=tokens['semantic',d['variableName']]
            if 'valuesByMode' in d: v['values'].update({mode_names[k]:x for k,x in d['valuesByMode'].items()})
            if 'newAlias' in d: v['values'][d['modeName']]=d['newAlias']
            if 'scopes' in d:v['scopes']=d['scopes']
            v.setdefault('amendments',[]).append(source)
        for override in d.get('scopeOverrides',[]):
            tokens['semantic',override['name']]['scopes']=override['scopes']
    def alias_key(value):
        if value.get('id') in ids:return ids[value['id']]
        name=value.get('primitive_name',value.get('name'))
        key=('primitive',name)
        if key in tokens:return key
        if value.get('targetId') in ids:return ids[value['targetId']]
        raise ValueError(f'Alias sin resolver: {value}')
    def resolve(key,mode,stack=()):
        if key in stack:raise ValueError(f'Ciclo de aliases: {stack}')
        v=tokens[key];value=v['values'].get(mode,v['values'].get('Value'))
        if value is None:raise ValueError(f'Modo ausente: {key}, {mode}')
        if isinstance(value,dict) and value.get('type')=='VARIABLE_ALIAS':
            target=alias_key(value);resolve(target,mode,stack+(key,))
            return 'var('+css_name(*target)+')'
        if v['resolvedType']=='COLOR':
            return 'rgb('+ ' '.join(f'{value[c]*255:.8f}'.rstrip('0').rstrip('.') for c in 'rgb')+' / '+str(value.get('a',1))+')'
        if v['resolvedType']=='FLOAT':
            # Las magnitudes Figma son px. Tracking se conserva como magnitud px,
            # no se interpreta como porcentaje/em sin una decisión documental.
            return f'{value:g}px'
        if v['name'].startswith('font/weight/'):
            return str({'regular':400,'medium':500,'semibold':600,'semi bold':600,'bold':700}[str(value).lower()])
        if v['name'].startswith('font/family/'):
            return '"Manrope Variable", "Manrope", sans-serif'
        return json.dumps(value,ensure_ascii=False)
    lines=['/* Generado por scripts/tokens.py. No editar; ver tokens.manifest.json. */']
    for coll in ['primitive','character-identity']:
        lines+=[':root, [data-ds-theme] {']+[f'  {css_name(*k)}: {resolve(k,"Value")};' for k in sorted(tokens) if k[0]==coll]+['}']
    for mode in MODES:
        lines+=[(':root, ' if mode==MODES[0] else '')+f'[data-ds-theme="{mode.lower()}"] {{']+[f'  {css_name(*k)}: {resolve(k,mode)};' for k in sorted(tokens) if k[0]=='semantic']+['}']
    manifest={'kind':'DERIVED_NOT_AUTHORITY','sources':hashes,'modes':MODES,'tokens':[dict(name=v['name'],collection=v['collection'],css=css_name(*k),source=v['source'],amendments=v.get('amendments',[]),description=v.get('description',''),scopes=v.get('scopes',[]),values=v['values']) for k,v in sorted(tokens.items())]}
    return {'src/generated/tokens.css':'\n'.join(lines)+'\n','src/generated/tokens.manifest.json':json.dumps(manifest,ensure_ascii=False,indent=2)+'\n'}
if __name__=='__main__':
    for path,content in build().items():
        p=WEB/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content)
    print('Tokens CSS generados desde el inventario y sus enmiendas explícitas.')
