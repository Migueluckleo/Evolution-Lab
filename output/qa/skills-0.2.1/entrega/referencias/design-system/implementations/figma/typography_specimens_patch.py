#!/usr/bin/env python3
"""Generate a minimal, guarded Figma documentation patch locally. Never calls Figma."""
from pathlib import Path
import argparse, hashlib, json
ROOT=Path(__file__).resolve().parents[2]
CANON='specs/tokens/ai-design-system.typography.v0.1.1.json'
OLD='specs/tokens/ai-design-system.typography.v0.1.0.json'
STATE='implementations/figma/typography.v0.1.1.catalog.state.json'
MAPPING='implementations/figma/typography.v0.1.1.mapping.json'
BUILDER='implementations/figma/typography.v0.1.0.specimens.build.js'
RUNTIME='implementations/figma/typography_specimens_patch.runtime.js'
PINS={CANON:'26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd',STATE:'de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0',MAPPING:'4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads((ROOT/p).read_text())
def fmt(x):return 'Auto' if x['unit']=='AUTO' else f"{x['value']}{'%' if x['unit']=='PERCENT' else ' px'}"
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output-dir',type=Path,default=ROOT/'implementations/figma');args=ap.parse_args()
    for name,pin in PINS.items():
        if sha(ROOT/name)!=pin:raise ValueError('Source changed; review patch before regeneration: '+name)
    current=load(CANON);old=load(OLD);state=load(STATE);mapping=load(MAPPING)
    styles={s['id']:s for s in current['styles']};oldstyles={s['id']:s for s in old['styles']}
    assert len(styles)==79 and sum(s['category']=='base' for s in styles.values())==18
    assert set(styles)==set(state['styleMap']) and len(oldstyles)==75
    assert mapping['summary']['applicationBlockedSegments']==103
    base_ids=[('ui-action-label-medium','1006:602'),('ui-action-label-small','1006:542'),('ui-action-label-normal','1006:607'),('ui-upload-action-feedback','1006:522')]
    editorial=['body-regular','body-semibold','heading-3-semibold','subheading-1-semibold']
    selected=[];cards=[]
    for sid,cardid in base_ids:
        s=styles[sid+'-underline'];base=styles[sid]
        assert s['derivedFormattingFrom']['baseStyleId']==sid and s['textDecoration']=='UNDERLINE'
        assert s['description'] and base['description']!=oldstyles[sid]['description']
        for key in ['fontFamily','fontStyle','fontSize','fontWeight','lineHeight','letterSpacing','tokenRefs']:
            assert s[key]==base[key],(sid,key)
        selected.extend([sid,s['id']]);cards.append({'cardId':cardid,'baseStyleId':sid,'newStyleId':s['id'],'oldDescription':oldstyles[sid]['description'],'description':base['description'],'sample':'La información clara facilita cada decisión.','values':f"{s['fontFamily']} {s['fontStyle']} · Peso {s['fontWeight']} · {s['fontSize']} px · Interlínea {fmt(s['lineHeight'])} · Tracking {fmt(s['letterSpacing'])} · Decoración UNDERLINE\n{s['id']}"})
    boards=[{'id':'1006:292','name':'01 · Base · 18 estilos','originalCount':18},{'id':'1006:387','name':'02 · Compatibilidad · 1 de 3','originalCount':19},{'id':'1006:487','name':'03 · Compatibilidad · 2 de 3','originalCount':19},{'id':'1006:587','name':'04 · Compatibilidad · 3 de 3','originalCount':19}]
    ids=[('1006:294','1006:296'),('1006:389','1006:391'),('1006:489','1006:491'),('1006:589','1006:591')]
    updates=[]
    for board,(status_id,ref_id) in zip(boards,ids):
        updates.extend([{'nodeId':status_id,'boardId':board['id'],'name':'Estado','styleId':'body-semibold','before':'Estilos listos · Migración de componentes pendiente','after':'Catálogo 0.1.1 · 18 base + 61 complementarios · Consultar QA por consumidor'},
        {'nodeId':ref_id,'boardId':board['id'],'name':'Referencia','styleId':'body-regular','before':'La migración de componentes existentes sigue pendiente. Registro: qa/implementations/typography/Figma-blocker.md','after':'Consumo y QA por familia: registry/implementations.md. El mapping 0.1.1 registra 103 rangos escalados sin vínculo resuelto; el catálogo no acredita validación global.'}])
    suffix='La escala principal para nuevas pantallas y documentación. Elige el nivel por su función y conserva sus métricas.'
    updates.extend([{'nodeId':'1006:295','boardId':'1006:292','name':'Introducción','styleId':'body-regular','before':'Manrope · 75 estilos: 18 base y 57 de compatibilidad, incluidos tres derivados para composiciones existentes. '+suffix,'after':'Manrope · 79 estilos: 18 base y 61 de compatibilidad, incluidos tres derivados de escala y cuatro complementos de formato para consumidores existentes. '+suffix},
    {'nodeId':'1006:588','boardId':'1006:587','name':'Título','styleId':'heading-3-semibold','before':'Compatibilidad 3 de 3 · 19 estilos','after':'Compatibilidad 3 de 3 · 23 estilos'}])
    tokens=[['color/text/primary','VariableID:13:27','COLOR','TEXT_FILL'],['color/text/secondary','VariableID:13:28','COLOR','TEXT_FILL'],['color/background/default','VariableID:13:35','COLOR','FRAME_FILL'],['color/background/subtle','VariableID:13:36','COLOR','FRAME_FILL'],['spacing/lg','VariableID:12:32','FLOAT','GAP'],['spacing/xl','VariableID:12:33','FLOAT','GAP'],['spacing/2xl','VariableID:12:34','FLOAT','GAP'],['radius/md','VariableID:13:6','FLOAT','CORNER_RADIUS']]
    selected+=editorial
    required=['id','name','category','fontFamily','fontStyle','fontSize','fontWeight','lineHeight','letterSpacing','textDecoration','description','tokenRefs']
    source={name:{'path':name,'sha256':sha(ROOT/name)} for name in [CANON,OLD,STATE,MAPPING,BUILDER,RUNTIME,'implementations/figma/typography_specimens_patch.py','implementations/figma/foundations-tokens.state.json','sources/inventories/tokens.inventory.json']}
    plan={'fileKey':'tj3WIBEZDGLVs7MJWKCwgf','pageId':'1003:412','layoutProvenance':'Parent reported live IDs; runtime must verify every identity and expected text before any mutation. Not an independent Figma readback.','source':source,'styleCount':79,'applicationBlockedSegments':103,'styles':[{**{k:styles[sid][k] for k in required},'styleId':state['styleMap'][sid]} for sid in selected],'baseCards':cards,'boards':boards,'updates':updates,'cardRoles':['Nombre','Muestra','Valores','Descripción'],'newStyleIds':[x['newStyleId'] for x in cards],'oldStyleIds':list(oldstyles),'lastOriginalCardId':'1006:682','collection':{'id':'VariableCollectionId:6:2','modeId':'6:0'},'tokens':tokens}
    runtime=(ROOT/RUNTIME).read_text();args.output_dir.mkdir(parents=True,exist_ok=True);results={}
    for mode,apply in [('preflight',False),('patch',True)]:
        p=args.output_dir/f'typography.v0.1.1.specimens.{mode}.js'
        p.write_text(runtime.replace('__APPLY__',str(apply).lower()).replace('__PLAN__',json.dumps(plan,ensure_ascii=False,separators=(',',':'))))
        results[str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p)]={'sha256':sha(p),'mode':mode}
    result={'status':'PREPARED_NOT_RUN_IN_FIGMA','sourceChecks':'PASS','source':source,'outputs':results,'newCards':4,'existingTextTargets':14,'originalCards':75,'expectedFinalCards':79,'expectedFinalTextNodes':332,'expectedFinalFrames':83,'consumerQA':'NOT_RUN','visualQA':'NOT_RUN'}
    (args.output_dir/'typography.v0.1.1.specimens.patch.plan.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
