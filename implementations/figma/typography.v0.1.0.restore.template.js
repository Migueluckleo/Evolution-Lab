const page=await figma.getNodeByIdAsync(PAGE_ID);await figma.setCurrentPageAsync(page);figma.skipInvisibleInstanceChildren=false;
const data=DATA;const ids=[],errors=[];const clean=x=>JSON.parse(JSON.stringify(x,(_,v)=>typeof v==='symbol'?'MIXED':v));
for(const row of data.nodes){
 const n=await figma.getNodeByIdAsync(row.id);if(!n||n.type!=='TEXT')throw Error('Missing original text '+row.id);
 const segs=row.segments.map(([start,end,r])=>({start,end,...data.recipes[r]}));
 for(const s of n.getStyledTextSegments(['fontName']))await figma.loadFontAsync(s.fontName);
 for(const s of segs)await figma.loadFontAsync(s.fontName);
 for(const f of ['fontFamily','fontStyle','fontWeight','fontSize','lineHeight','letterSpacing'])if(n.boundVariables?.[f])n.setBoundVariable(f,null);
 for(const s of segs){
  if(segs.length===1){n.fontName=s.fontName;n.fontSize=s.fontSize;n.lineHeight=s.lineHeight;n.letterSpacing=s.letterSpacing;n.textDecoration=s.textDecoration;n.textCase=s.textCase;n.paragraphSpacing=s.paragraphSpacing;n.paragraphIndent=s.paragraphIndent;}
  else {n.setRangeFontName(s.start,s.end,s.fontName);n.setRangeFontSize(s.start,s.end,s.fontSize);n.setRangeLineHeight(s.start,s.end,s.lineHeight);n.setRangeLetterSpacing(s.start,s.end,s.letterSpacing);n.setRangeTextDecoration(s.start,s.end,s.textDecoration);n.setRangeTextCase(s.start,s.end,s.textCase);n.setRangeParagraphSpacing(s.start,s.end,s.paragraphSpacing);n.setRangeParagraphIndent(s.start,s.end,s.paragraphIndent);}
  if(s.textStyleId){if(segs.length===1)await n.setTextStyleIdAsync(s.textStyleId);else await n.setRangeTextStyleIdAsync(s.start,s.end,s.textStyleId);}
  for(const [field,alias]of Object.entries(s.boundVariables||{})){if(!['fontFamily','fontStyle','fontWeight','fontSize','lineHeight','letterSpacing'].includes(field))continue;if(alias?.type!=='VARIABLE_ALIAS')continue;const v=await figma.variables.getVariableByIdAsync(alias.id);if(segs.length===1)n.setBoundVariable(field,v);else n.setRangeBoundVariable(s.start,s.end,field,v);}
 }
 ids.push(n.id);
}
for(const row of data.nodes){const n=await figma.getNodeByIdAsync(row.id),after=n.getStyledTextSegments(['fontName','fontSize','lineHeight','letterSpacing','textStyleId','textDecoration','textCase','boundVariables']);if(n.width!==row.width||n.height!==row.height)errors.push({id:n.id,field:'geometry',expected:[row.width,row.height],actual:[n.width,n.height]});for(let i=0;i<row.segments.length;i++){const s=data.recipes[row.segments[i][2]],a=after.find(a=>a.start<=row.segments[i][0]&&a.end>=row.segments[i][1]);if(!a){errors.push({id:n.id,field:'segments'});continue;}for(const f of ['fontSize','lineHeight','letterSpacing','textStyleId','textDecoration','textCase'])if(JSON.stringify(clean(a[f]))!==JSON.stringify(s[f]))errors.push({id:n.id,field:f,expected:s[f],actual:a[f]});if(a.fontName.style!==s.fontName.style)errors.push({id:n.id,field:'fontName'});}}
return{pageId:page.id,mutatedNodeIds:ids,errors};

