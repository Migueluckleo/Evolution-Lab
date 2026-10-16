#!/usr/bin/env python3
"""P07: una familia activa necesita export, API y ejemplo documentado y ejecutable."""
import argparse, hashlib, json, re, subprocess
from pathlib import Path
import assets, tokens, typography
ROOT, WEB=tokens.ROOT,tokens.WEB

def build():
    rows=json.loads((WEB/'components.registry.json').read_text())
    status=json.loads(subprocess.check_output([str(ROOT/'scripts/ds'),'status','--json'],cwd=ROOT,text=True))
    active={f['id']:f for f in status['families'] if f['base'] and not f['id'].startswith(('FOUNDATIONS-','MIGRATION-'))}
    ids=[r['id'] for r in rows]
    assert len(ids)==len(set(ids)),'IDs de familia duplicados'
    assert set(ids)==set(active),f'Cobertura P07 pendiente: {set(active)-set(ids)}; entradas obsoletas: {set(ids)-set(active)}'
    output=tokens.build()|assets.build()
    output.update(typography.build(token_outputs=output))
    examples=(WEB/'src/examples.tsx').read_text()
    parts=re.split(r'// example: ([\w-]+)\n',examples)
    blocks={parts[i]:parts[i+1].strip() for i in range(1,len(parts),2)}
    assert set(blocks)=={r['slug'] for r in rows},'Ejemplos y familias no coinciden'
    catalogue=[]; map_lines=["'use client';", "import * as Examples from '../examples';", "import type { ComponentType } from 'react';",'export const examples: Record<string, ComponentType> = {']
    for row in rows:
        module=WEB/f'src/components/{row["module"]}.tsx';code=module.read_text()
        for name in row['exports']:assert f'export function {name}' in code or f'export const {name}' in code,f'Falta export {name}'
        assert row['base']==active[row['id']]['base']['path'],f'Base cambió: {row["id"]}'
        sources=[row['base']]+row['amendments']
        hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}
        apis={}
        for m in re.finditer(r'export (?:interface|type) (\w+)',code):
            end=code.find('\nexport ',m.end());apis[m.group(1)]=code[m.start():end if end>=0 else len(code)].strip().split('\nfunction ')[0].split('\ntype ')[0]
        needed={name+'Props' for name in row['exports']};previous=set()
        while previous!=needed:
            previous=set(needed)
            for key in apis:
                if any(re.search(r'\b'+re.escape(key)+r'\b',apis.get(n,'')) for n in needed):needed.add(key)
        api='\n\n'.join(apis[n] for n in apis if n in needed)
        assert api,'Falta API tipada '+row['name']
        block=blocks[row['slug']];function=re.search(r'export function (\w+)',block).group(1)
        map_lines.append(f'  {json.dumps(row["slug"])}: Examples.{function},')
        example=parts[0].replace("'./index'","'@/index'").strip()+'\n\n'+block+'\n'
        defaults=[]
        for name in row['exports']:
            m=re.search(r'export function '+name+r'(?:<[^\n]+?>)?\((.*?)\)\s*\{',code,re.S)
            if m:defaults.append(name+': '+m.group(1).strip())
        doc=f'''# {row['name']} · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `{row['id']}` · API local 0.1.0 · categoría {row['category']}.

## Uso sin backend

{row['notes']}

```tsx
{example.rstrip()}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [{module.name}](../../src/components/{module.name}). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
{api}
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
{chr(10).join(defaults)}
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **{row['slots']['status']}**. {row['slots']['reason'].rstrip('.') }. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

'''
        for path,digest in hashes.items(): doc+=f'- [{Path(path).name}](../../../../{path}) · SHA-256 `{digest}`.\n'
        doc+='\nLas enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.\n\n## Verificación\n\n`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../'+row.get('qa','qa/implementations/web.v0.1.0.review.md')+') identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.\n'
        output[f'docs/components/{row["slug"]}.md']=doc
        output[f'public/docs/{row["slug"]}.md']=doc
        catalogue.append(dict(row,hashes=hashes,api=api,example=example,defaults=defaults))
    map_lines.append('};\n');output['src/generated/example-map.tsx']='\n'.join(map_lines)
    output['src/generated/catalog.json']=json.dumps(catalogue,ensure_ascii=False,indent=2)+'\n'
    output['docs/components/README.md']='# Componentes web\n\nÍndice generado. Cada ficha contiene API, ejemplo ejecutable, Slots, fuentes y límites.\n\n'+'\n'.join(f'- [{r["name"]}]({r["slug"]}.md) · {r["id"]}' for r in rows)+'\n'
    return output

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args();changed=[]
    for name,content in build().items():
        path=WEB/name;raw=content if isinstance(content,bytes) else content.encode()
        if not path.exists() or path.read_bytes()!=raw:
            changed.append(name)
            if not args.check:path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)
    if args.check and changed:raise SystemExit('Derivados desactualizados: '+', '.join(changed))
    families=len(json.loads((WEB/'components.registry.json').read_text()))
    print(f'P07: {families} familias cubiertas; {len(changed)} derivados '+('desactualizados' if args.check else 'actualizados')+'.')
if __name__=='__main__':main()
