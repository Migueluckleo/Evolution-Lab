// HISTORICAL FAILED ATTEMPT — NOT A VALIDATED MIGRATION SCRIPT.
// Reassigning styles can propagate the last style across existing variants.
// Immediate per-node checks below did not detect the final shared-property drift.
// Do not replay on live components. See qa/implementations/typography/Figma-blocker.md
// and the independent census/readback reports before developing a safe replacement.
const page=await figma.getNodeByIdAsync(PAGE_ID);await figma.setCurrentPageAsync(page);figma.skipInvisibleInstanceChildren=false;
const catalog=CATALOG;
const styleMap=STYLE_MAP;
const phase=PHASE;
const nodeMapping=NODE_MAPPING;
const rangeStart=RANGE_START,rangeEnd=RANGE_END;
const fields=['fontName','fontSize','fontWeight','lineHeight','letterSpacing','textStyleId','textStyleOverrides','boundVariables','textCase','textDecoration','fills','hyperlink','paragraphSpacing','paragraphIndent'];
const clean=x=>JSON.parse(JSON.stringify(x,(_,v)=>typeof v==='symbol'?'MIXED':v));
const encode=(m,k)=>m.unit==='AUTO'?'AUTO':m.value===0&&k==='tracking'?'0':m.unit+':'+(m.unit==='PERCENT'&&k==='line'?Math.fround(m.value/100)*100:Math.fround(m.value));
const key=s=>JSON.stringify([s.fontName?s.fontName.style:s.fontStyle,s.fontSize,encode(s.lineHeight,'line'),encode(s.letterSpacing,'tracking')]);
const byKey=new Map(catalog.map(s=>[key(s),s]));
const nonmetric=s=>clean({characters:s.characters,start:s.start,end:s.end,textCase:s.textCase,textDecoration:s.textDecoration,fills:s.fills,hyperlink:s.hyperlink,paragraphSpacing:s.paragraphSpacing,paragraphIndent:s.paragraphIndent});
const texts=page.findAllWithCriteria({types:['TEXT','TEXT_PATH']});let uiCount=0,docCount=0,checked=0,skipped=0;const mutated=[],errors=[],scaled=[];
for(const n of texts.slice(rangeStart,rangeEnd)){
 let p=n.parent,isUI=false,scale=1;
 while(p&&p.type!=='PAGE'){if(p.type==='INSTANCE'||p.type==='COMPONENT')isUI=true;if(p.type==='INSTANCE'&&scale===1&&p.scaleFactor!==1)scale=p.scaleFactor;p=p.parent;}
 if(!isUI){docCount++;continue;}uiCount++;
 if(phase==='masters'&&n.id.startsWith('I')){skipped++;continue;}
 const before=clean(n.getStyledTextSegments(fields));const dims=[n.width,n.height];const props=JSON.stringify(n.componentPropertyReferences);const oldNonmetric=JSON.stringify(before.map(nonmetric));
 const chosen=before.map((s,i)=>{const mapped=nodeMapping[n.id]?.[i];if(!mapped)return null;const spec=catalog.find(d=>d.id===mapped[0]);return spec?{spec,scale:mapped[1]}:null;});
 if(chosen.some(s=>!s)){errors.push({id:n.id,kind:'UNMAPPED_RECIPE',recipes:before.map(key),scale});continue;}
 if(chosen.some(x=>x.scale!==1)){scaled.push({id:n.id,scale,styleId:before[0].textStyleId,expected:styleMap[chosen[0].spec.id]});if(before.some((s,i)=>s.textStyleId!==styleMap[chosen[i].spec.id]))errors.push({id:n.id,kind:'SCALED_STYLE_NOT_INHERITED'});checked++;continue;}
 const needs=before.some((s,i)=>s.textStyleId!==styleMap[chosen[i].spec.id]||(s.textStyleOverrides||[]).some(k=>['fontName','fontSize','lineHeight','letterSpacing','fontWeight','fontStyle'].includes(k)));
 if(!needs){checked++;continue;}
 const fonts=new Map(before.map(s=>[JSON.stringify(s.fontName),s.fontName]));for(const f of fonts.values())await figma.loadFontAsync(f);
 for(const f of ['fontFamily','fontStyle','fontWeight','fontSize','lineHeight','letterSpacing'])if(n.boundVariables&&n.boundVariables[f])n.setBoundVariable(f,null);
 if(chosen.every(x=>x.spec.id===chosen[0].spec.id))await n.setTextStyleIdAsync(styleMap[chosen[0].spec.id]);
 else for(let i=0;i<before.length;i++)await n.setRangeTextStyleIdAsync(before[i].start,before[i].end,styleMap[chosen[i].spec.id]);
 // Only restore actual differences. Reassigning even an unchanged textCase/paragraph
 // value detaches the shared TextStyle in Figma. Decoration is a supported semantic override.
 for(const s of before){if(s.end<=s.start)continue;for(const [field,getter,setter] of [['textCase','getRangeTextCase','setRangeTextCase'],['textDecoration','getRangeTextDecoration','setRangeTextDecoration'],['fills','getRangeFills','setRangeFills'],['hyperlink','getRangeHyperlink','setRangeHyperlink'],['paragraphSpacing','getRangeParagraphSpacing','setRangeParagraphSpacing'],['paragraphIndent','getRangeParagraphIndent','setRangeParagraphIndent']]){if(JSON.stringify(clean(n[getter](s.start,s.end)))!==JSON.stringify(s[field])){if(before.length===1)n[field]=s[field];else n[setter](s.start,s.end,s[field]);}}}
 const after=clean(n.getStyledTextSegments(fields));
 if(JSON.stringify(after.map(nonmetric))!==oldNonmetric)errors.push({id:n.id,kind:'NON_TYPOGRAPHIC_CHANGE'});
 if(n.width!==dims[0]||n.height!==dims[1])errors.push({id:n.id,kind:'GEOMETRY_CHANGE',before:dims,after:[n.width,n.height]});
 if(JSON.stringify(n.componentPropertyReferences)!==props)errors.push({id:n.id,kind:'COMPONENT_PROPERTY_CHANGE'});
 for(let i=0;i<after.length;i++)if(key(after[i])!==key(before[i])||after[i].textStyleId!==styleMap[chosen[i].spec.id])errors.push({id:n.id,kind:'STYLE_MISMATCH',before:key(before[i]),after:key(after[i]),style:after[i].textStyleId,expected:styleMap[chosen[i].spec.id]});
 mutated.push(n.id);checked++;
}
return {pageId:page.id,pageName:page.name,phase,textCount:texts.length,uiCount,documentationCount:docCount,checked,skipped,mutatedNodeIds:mutated,scaled,errors};

