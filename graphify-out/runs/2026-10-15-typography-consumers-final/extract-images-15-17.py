import json,re,hashlib
from pathlib import Path
ROOT=Path('/Users/miguel.leo/Desktop/CONTPAQi-designSystem-Optimizado');run=ROOT/'graphify-out/runs/2026-10-15-typography-consumers-final'
plan=json.loads((run/'source-plan.json').read_text())['source_sha256']
norm=lambda s:re.sub('[^a-z0-9]','_',s.lower())
def make(num,items,links):
 source=json.loads((run/f'chunk-{num:02}.files.json').read_text())[0];p=Path(source);rel=p.relative_to(ROOT).as_posix();assert hashlib.sha256(p.read_bytes()).hexdigest()==plan[rel]
 stem=norm(str(Path(rel).with_suffix('')));ids=[stem+'_'+norm(label) for label,typ,attrs in items]
 nodes=[dict(id=i,label=label,file_type=typ,source_file=source,source_location=None,source_url=None,captured_at=None,author=None,contributor=None,**attrs) for i,(label,typ,attrs) in zip(ids,items)]
 edges=[dict(source=ids[a],target=ids[b],relation=relation,confidence=confidence,confidence_score=score,source_file=source,source_location=None,weight=1.0) for a,b,relation,confidence,score in links]
 out={'nodes':nodes,'edges':edges,'hyperedges':[],'input_tokens':0,'output_tokens':0,'usage_status':'UNAVAILABLE','usage_note':'Provider token counts unavailable; legacy schema numeric fields are placeholders, not measured usage.','extraction_method':'Direct vision via view_image of each exact source; no OCR-only extraction and no behavior/Figma validation inferred.','source_sha256':{source:plan[rel]}}
 (run/f'chunk-{num:02}.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(num,len(nodes),len(edges))
make(15,[
 ('File Upload default state','image',{'description':'Rendered upload-control specimen on white background; visible default caption, outlined container, dashed drop area, upload icon, instruction and helper text.','image_size':[534,218],'evidence_scope':'Static appearance only; upload behavior not executed.'}),
 ('Upload drop area','concept',{'description':'Dashed rounded rectangle inside a larger thin-bordered container; centered cloud-and-up-arrow icon above the instruction.'}),
 ('Underlined upload action','concept',{'text':'subir tu archivo','description':'Purple underlined phrase embedded between “Haz clic para” and “o arrástralo aquí”; distinguishes the upload action visually from surrounding copy.'}),
 ('Sample format helper','concept',{'text':'Formatos de muestra','description':'Muted supporting text centered below upload instruction.'}),
 ('External helper text','concept',{'text':'Helper text','description':'Muted text below the dashed area, inside outer control.'})
],[(0,1,'references','EXTRACTED',1.0),(1,2,'references','EXTRACTED',1.0),(1,3,'references','EXTRACTED',1.0),(0,4,'references','EXTRACTED',1.0),(2,1,'conceptually_related_to','INFERRED',0.85)])
make(16,[
 ('Modal Media desktop screenshot','image',{'image_size':[1440,900],'description':'Centered white dialog over a dimmed product-prototype page; purple geometric media occupies upper dialog area, centered title and message below.','evidence_scope':'Static rendered screenshot; not proof of bindings, click handling or Figma implementation.'}),
 ('Media dialog composition','concept',{'description':'Vertically arranged image region and white text region; rounded outer corners and drop shadow.'}),
 ('Purple media artwork','concept',{'description':'Lavender abstract geometric artwork with diagonal motifs in the upper region; preserved as visible image content.'}),
 ('Editable intent title and local instruction','concept',{'title_text':'Detalle portable','message_text':'Presiona M para ver el detalle con contenido variable.','description':'Centered title and explanatory sentence in white dialog body; editability and keyboard behavior cannot be determined from pixels.'}),
 ('Close icon affordance','concept',{'description':'Small X at the upper right of the media region; visible affordance only.'}),
 ('Dimmed prototype background','concept',{'description':'Background shows Prueba portable CONTPAQi heading, Buscar required input, Abrir detalle button and Consulta: vacía feedback under gray scrim.'})
],[(0,1,'references','EXTRACTED',1.0),(1,2,'references','EXTRACTED',1.0),(1,3,'references','EXTRACTED',1.0),(1,4,'references','EXTRACTED',1.0),(0,5,'references','EXTRACTED',1.0),(4,1,'conceptually_related_to','INFERRED',0.85)])
make(17,[
 ('Modal SideBySide narrow screenshot','image',{'image_size':[1000,760],'description':'Wide modal centered over dimmed prototype, white content on left and lavender artwork on right; title, avatar, branded logo and return button are visible.','evidence_scope':'Static appearance only; no live Figma, bindings or interaction validation.'}),
 ('SideBySide modal composition','concept',{'description':'Two adjacent regions: left white content stack, right abstract purple image; rounded outer dialog and lower white space.'}),
 ('Visible content stack','concept',{'title_text':'Detalle portable','description':'Left region vertically arranges title, circular photo avatar with green presence dot, CONTPAQi Contabilidad logo and blue action button.'}),
 ('Return action affordance','concept',{'text':'Volver al medio','description':'Blue rounded button with white text below logo; no click behavior inferred.'}),
 ('Focused close affordance','concept',{'description':'X in upper-right with visible blue rectangular outline; appearance is consistent with focus, but focus state is inferred from outline only.'}),
 ('Official brand appearance','concept',{'text':'CONTPAQi Contabilidad','description':'Blue icon and blue/gray wordmark as a visible asset; screenshot alone does not prove canonical asset hashes.'}),
 ('Dimmed background retained','concept',{'description':'Heading, required input, opening action and feedback remain partly visible behind overlay.'})
],[(0,1,'references','EXTRACTED',1.0),(1,2,'references','EXTRACTED',1.0),(2,3,'references','EXTRACTED',1.0),(1,4,'references','EXTRACTED',1.0),(2,5,'references','EXTRACTED',1.0),(0,6,'references','EXTRACTED',1.0),(3,1,'conceptually_related_to','INFERRED',0.85)])
