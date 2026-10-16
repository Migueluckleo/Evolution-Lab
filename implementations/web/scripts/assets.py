"""Assets locales derivados de snapshots, conservando procedencia y geometría."""
import base64, hashlib, json, shutil, re
from pathlib import Path
from tokens import ROOT, WEB

def build():
    result={}; path='sources/figma-snapshots/characters.ecosistema.2026-10-08.json';nodes=json.loads((ROOT/path).read_text())['frames']
    identities=[]
    for p in ['specs/tokens/ai-design-system.character-identity.v0.1.0.json','specs/tokens/ai-design-system.character-shadow.v0.1.0.json']:
        for v in json.loads((ROOT/p).read_text())['variables']:
            identities.append((v['name'],v['valuesByMode']['Value']))
    def local_transform(parent, child):
        # Los ojos del snapshot tienen relativeTransform referido al componente,
        # incluso bajo GROUP. Derivar el sistema local SVG desde las matrices
        # absolutas evita aplicar dos veces el desplazamiento del grupo.
        a,c,e=parent[0];b,d,f=parent[1];det=a*d-b*c
        assert det != 0, 'Transformación fuente no invertible'
        inverse=[[d/det,-c/det,(c*f-d*e)/det],[-b/det,a/det,(b*e-a*f)/det]]
        return [[sum(inverse[i][k]*child[k][j] for k in range(2))+(inverse[i][2] if j==2 else 0) for j in range(3)] for i in range(2)]
    def node(n, parent=None):
        out={'id':n['id'],'opacity':n.get('opacity',1),'visible':n.get('visible',True)}
        if parent is not None: out['transform']=local_transform(parent['absoluteTransform'],n['absoluteTransform'])
        paths=[]
        for paint in n.get('fills',[]):
            if not paint.get('visible',True):continue
            assert paint['type']=='SOLID',f'Pintura no soportada {n["id"]}'
            color=paint['color'];matches=[name for name,c in identities if max(abs(color[k]-c[k]) for k in 'rgb')<0.000001]
            assert len(matches)==1,(n['id'],color,matches)
            for p in n.get('vectorPaths',[]):paths.append({'d':p['data'],'fillRule':'evenodd' if p['windingRule']=='EVENODD' else 'nonzero','token':matches[0],'opacity':paint.get('opacity',1)})
        assert not n.get('strokes'),f'Stroke no convertido {n["id"]}'
        out['paths']=paths;out['children']=[node(c,n) for c in n.get('children',[])];return out
    frames={'beni':[node(n) for n in nodes[:6]],'navi':[node(n) for n in nodes[6:]]}
    result['src/generated/characters.json']=json.dumps({'source':path,'sha256':hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),'width':nodes[0]['width'],'height':nodes[0]['height'],'frames':frames},ensure_ascii=False)+'\n'
    glyph_source='implementations/figma/conversation.v0.1.0.build.js'
    glyphs=json.loads(re.search(r'const ART=(.*);',(ROOT/glyph_source).read_text()).group(1))
    glyph_paints=json.loads((ROOT/'sources/figma-snapshots/conversation.characters.original.2026-10-08.json').read_text())
    for glyph, observed in zip(glyphs,glyph_paints):
        assert glyph['id']==observed['id']
        for vector in glyph['nodes']:
            paths=[]
            for paint in vector['fills']:
                if not paint.get('visible',True):continue
                assert paint in next(v['fills'] for v in observed['paints'] if v['id']==vector['id'])
                matches=[name for name,c in identities if max(abs(paint['color'][k]-c[k]) for k in 'rgb')<0.000001]
                assert len(matches)==1
                paths.extend({'d':p['data'],'token':matches[0]} for p in vector['vectorPaths'])
            vector['paths']=paths
            for key in ['fills','effects','vectorPaths']:vector.pop(key,None)
    result['src/generated/conversation-glyphs.json']=json.dumps({'source':glyph_source,'sha256':hashlib.sha256((ROOT/glyph_source).read_bytes()).hexdigest(),'glyphs':glyphs},ensure_ascii=False)+'\n'
    welcome_source='implementations/figma/chat-section.v0.1.0.build.js'
    welcome=json.loads(re.search(r'const HERO=(.*);',(ROOT/welcome_source).read_text()).group(1))
    for vector in welcome['vectors']:
        matches=[name for name,c in identities if max(abs(vector['fills'][0]['color'][k]-c[k]) for k in 'rgb')<0.000001]
        assert len(matches)==1
        vector['token']=matches[0]
        vector.pop('fills')
    result['src/generated/chat-welcome.json']=json.dumps({'source':welcome_source,'sha256':hashlib.sha256((ROOT/welcome_source).read_bytes()).hexdigest(),**welcome},ensure_ascii=False)+'\n'
    manifest=ROOT/'sources/assets/web/logos.manifest.json'
    if manifest.exists():
        assets=json.loads(manifest.read_text())['assets']
        result['src/generated/logos.json']=json.dumps([{**x,'src':'/assets/logos/'+Path(x['file']).name} for x in assets],ensure_ascii=False,indent=2)+'\n'
        for x in assets:
            raw=(ROOT/x['file']).read_bytes();assert hashlib.sha256(raw).hexdigest()==x['sha256']
            result['public/assets/logos/'+Path(x['file']).name]=raw
    for asset in json.loads((ROOT/'sources/assets/web/modal.manifest.json').read_text())['assets']:
        raw=(ROOT/asset['file']).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==asset['sha256'] and hashlib.sha1(raw).hexdigest()==asset['hash']
        result['public/assets/'+Path(asset['file']).name]=raw
    avatar=ROOT/'sources/figma-snapshots/avatar-source-face-48.png.base64'
    result['public/assets/avatar.png']=base64.b64decode(avatar.read_text())
    result['src/generated/gauge.json']=(ROOT/'sources/figma-snapshots/chart-donut.vector-paths.json').read_text()
    art={}
    roles=json.loads((ROOT/'drafts/foundations/ai-design-system.empty-states.v0.1.0.json').read_text())['variables']
    palette={attribute:{'#'+''.join(f'{c:02X}' for c in v['source_rgb']):'var(--ds-'+v['name'].replace('/','-')+')' for v in roles if (v['name'].startswith('color/border/'))==(attribute=='stroke')} for attribute in ['fill','stroke']}
    for svg in (ROOT/'sources/figma-snapshots').glob('empty-states-*.svg'):
        content=svg.read_text()
        # El blanco de máscaras/clipPaths es geometría, preservado por REQ-ES-05.
        for attribute,colors in palette.items():
            for color,role in colors.items():
                content=content.replace(attribute+'="'+color+'"',attribute+'="'+role+'"')
        for identifier in re.findall(r'id="([^"]+)"',content):
            content=content.replace('id="'+identifier+'"','id="IDPREFIX'+identifier+'"').replace('url(#'+identifier+')','url(#IDPREFIX'+identifier+')')
        art[svg.stem.split('-')[-1]]=content
    result['src/generated/illustrations.json']=json.dumps(art,ensure_ascii=False)+'\n'
    source='sources/figma-snapshots/sidebar.v0.1.0.source.json'
    observed='sources/figma-snapshots/sidebar.web-fidelity.2026-10-13.json'
    sidebar=json.loads((ROOT/source).read_text())['nodes']
    recipes=json.loads((ROOT/observed).read_text())['variants']
    for recipe in recipes:
        original=next(n for n in sidebar if n['type']=='COMPONENT' and n['name']==recipe['name'])
        recipe['sourceId']=original['id']
        recipe['properties']=dict(part.split('=') for part in recipe['name'].split(', '))
        if recipe['union']:
            union=recipe['union']
            if union['svg']:
                union['paths']=re.findall(r'<path d="([^"]+)"',union.pop('svg'))
                union['viewBox']='0 0 222 48'
            else:
                vector=next(n for n in sidebar if n.get('parent')==original['id'] and n['name']=='Union')
                union['paths']=[p['data'] for p in vector['vectorPaths']]
                union['viewBox']=f"0 0 {vector['width']} {vector['height']}"
                union.pop('svg')
    release=next(n for n in sidebar if n['id']=='7268:1065')
    a,c,e=release['fills'][0]['gradientTransform'][0];b,d,f=release['fills'][0]['gradientTransform'][1];det=a*d-b*c
    gradient=f'matrix({d/det} {-b/det} {-c/det} {a/det} {(c*f-d*e)/det} {(b*e-a*f)/det})'
    caret_source='sources/figma-snapshots/header.company-caret.source.svg'
    result['src/generated/header-caret.json']=json.dumps({'source':caret_source,'sha256':hashlib.sha256((ROOT/caret_source).read_bytes()).hexdigest(),'path':re.search(r'<path d="([^"]+)"',(ROOT/caret_source).read_text()).group(1),'profileSource':'sources/figma-snapshots/header.profile-caret.web-fidelity.2026-10-13.svg','profileSha256':hashlib.sha256((ROOT/'sources/figma-snapshots/header.profile-caret.web-fidelity.2026-10-13.svg').read_bytes()).hexdigest(),'profilePath':re.search(r'<path d="([^"]+)"',(ROOT/'sources/figma-snapshots/header.profile-caret.web-fidelity.2026-10-13.svg').read_text()).group(1)})+'\n'
    result['src/generated/sidebar.json']=json.dumps({'releaseGradient':gradient,'sources':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [source,observed]},'variants':recipes},ensure_ascii=False,indent=2)+'\n'
    arrow_source='drafts/contracts/tooltip.contract.v0.1.0.yaml'
    arrow=re.search(r'      path: "([^"\n]+)"',(ROOT/arrow_source).read_text()).group(1)
    result['src/generated/tooltip-arrow.json']=json.dumps({'source':arrow_source,'sha256':hashlib.sha256((ROOT/arrow_source).read_bytes()).hexdigest(),'path':arrow})+'\n'
    loader_source='sources/figma-snapshots/loader-header.web-fidelity.2026-10-13.json'
    loader=json.loads((ROOT/loader_source).read_text())['nodes'][0]['children'][0]['children']
    result['src/generated/loader.json']=json.dumps({'source':loader_source,'sha256':hashlib.sha256((ROOT/loader_source).read_bytes()).hexdigest(),'ring':loader[0],'cap':loader[1]})+'\n'
    table_source='sources/figma-snapshots/table-icons.web-contract-audit.2026-10-13.json'
    result['src/generated/table-icons.json']=json.dumps({'source':table_source,'sha256':hashlib.sha256((ROOT/table_source).read_bytes()).hexdigest(),**json.loads((ROOT/table_source).read_text())})+'\n'
    return result
if __name__=='__main__':
    for path,content in build().items():
        p=WEB/path;p.parent.mkdir(parents=True,exist_ok=True)
        if isinstance(content,bytes):p.write_bytes(content)
        else:p.write_text(content)
    print('Assets generados desde fuentes locales.')
