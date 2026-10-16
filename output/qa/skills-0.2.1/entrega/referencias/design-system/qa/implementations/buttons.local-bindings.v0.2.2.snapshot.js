// Read-only regression fingerprint. FNV-1a UTF-16 is a change detector, not a cryptographic file hash.
function stable(v){if(v===figma.mixed)return "__MIXED__";if(v===undefined)return null;if(Array.isArray(v))return v.map(stable);if(v&&typeof v==="object")return Object.fromEntries(Object.keys(v).sort().map(k=>[k,stable(v[k])]));return v;}
function fingerprint(v){const s=JSON.stringify(stable(v));let h=2166136261;for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return (h>>>0).toString(16).padStart(8,"0")+":"+s.length;}
async function snapshot(rootIds,buttonVariantIds){
 figma.skipInvisibleInstanceChildren=false;
 const result=[];
 for(const id of rootIds){
  const root=await figma.getNodeByIdAsync(id);if(!root)throw Error("Missing "+id);
  const nodes=[root,...root.findAll(()=>true)],groups={identity:[],geometry:[],paint:[],text:[],api:[],reactions:[],bindings:[],overrides:[]},refs={},buttonInstances=[],textFonts={};
  const geometryFields=["x","y","width","height","rotation","relativeTransform","visible","opacity","layoutMode","layoutSizingHorizontal","layoutSizingVertical","primaryAxisSizingMode","counterAxisSizingMode","primaryAxisAlignItems","counterAxisAlignItems","itemSpacing","counterAxisSpacing","paddingTop","paddingBottom","paddingLeft","paddingRight","topLeftRadius","topRightRadius","bottomLeftRadius","bottomRightRadius","strokeWeight","strokeTopWeight","strokeBottomWeight","strokeLeftWeight","strokeRightWeight","strokeAlign","constraints","clipsContent","layoutPositioning"];
  for(const n of nodes){
   groups.identity.push([n.id,n.name,n.type,n.parent?.id,"children" in n?n.children.map(x=>x.id):[]]);
   groups.geometry.push([n.id,Object.fromEntries(geometryFields.filter(k=>k in n).map(k=>[k,n[k]]))]);
   groups.paint.push([n.id,Object.fromEntries(["fills","strokes","effects","blendMode","fillStyleId","strokeStyleId","effectStyleId"].filter(k=>k in n).map(k=>[k,n[k]]))]);
   groups.api.push([n.id,Object.fromEntries(["componentPropertyDefinitions","componentPropertyReferences","componentProperties","variantProperties","description","documentationLinks"].filter(k=>k in n && !(k==="componentPropertyDefinitions" && n.type==="COMPONENT" && n.parent?.type==="COMPONENT_SET")).map(k=>[k,n[k]]))]);
   if("reactions" in n)groups.reactions.push([n.id,n.reactions]);
   groups.bindings.push([n.id,n.boundVariables||{}]);
   for(const [field,a]of Object.entries(n.boundVariables||{}))for(const v of Array.isArray(a)?a:[a])if(v?.id)refs[v.id]=(refs[v.id]||0)+1;
   if(n.type==="TEXT"){groups.text.push([n.id,n.characters,n.fontName,n.fontSize,n.lineHeight,n.letterSpacing,n.textAutoResize,n.textAlignHorizontal,n.textAlignVertical,n.getStyledTextSegments(["fontName","fontSize","lineHeight","letterSpacing","fills","textStyleId"])]);const key=JSON.stringify(n.fontName);textFonts[key]=(textFonts[key]||0)+1;}
   if(n.type==="INSTANCE"){const main=await n.getMainComponentAsync();groups.identity.push([n.id,main?.id,main?.key]);groups.overrides.push([n.id,n.overrides]);if(buttonVariantIds.includes(main?.id))buttonInstances.push({id:n.id,mainId:main.id,w:n.width,h:n.height,propertiesFingerprint:fingerprint(n.componentProperties)});}
  }
  result.push({id:root.id,name:root.name,nodeCount:nodes.length,types:nodes.reduce((a,n)=>(a[n.type]=(a[n.type]||0)+1,a),{}),fingerprints:Object.fromEntries(Object.entries(groups).map(([k,v])=>[k,fingerprint(v)])),refs,buttonInstances,textFonts,variantGeometry:root.type==="COMPONENT_SET"?root.children.map(n=>[n.id,n.name,n.width,n.height]):null});
 }
 return result;
}
