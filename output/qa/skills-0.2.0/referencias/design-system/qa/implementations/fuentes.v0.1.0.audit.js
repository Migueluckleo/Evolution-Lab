/**
 * validateCreation
 *
 * Verifies that a set of nodes exist and match expected structural properties.
 * Designed to run immediately after a creation script to catch partial failures
 * before proceeding to the next build phase.
 *
 * Each check specifies a node ID and any combination of expected properties.
 * A check passes when all specified expectations are met; it fails (with a
 * reason string) as soon as any expectation is violated.
 *
 * @param {Array<{
 *   nodeId: string,
 *   expectedChildCount?: number,
 *   expectedName?: string,
 *   expectedType?: NodeType
 * }>} checks
 *   - `nodeId`: The Figma node ID to look up via figma.getNodeById.
 *   - `expectedChildCount`: If set, the node must have exactly this many direct children.
 *     Applies to any node with a `children` property (frames, component sets, etc.).
 *   - `expectedName`: If set, the node's `.name` must exactly match this string.
 *   - `expectedType`: If set, the node's `.type` must exactly match this string.
 * @returns {{
 *   passed: string[],
 *   failed: Array<{nodeId: string, reason: string}>
 * }}
 *   `passed`: Array of nodeIds that passed all checks.
 *   `failed`: Array of objects with the nodeId and a human-readable reason string.
 */
async function validateCreation(checks) {
  const passed = []
  const failed = []

  for (const check of checks) {
    const node = await figma.getNodeByIdAsync(check.nodeId)

    // Node must exist
    if (!node) {
      failed.push({
        nodeId: check.nodeId,
        reason: `Node not found. It may not have been created, or was deleted.`,
      })
      continue
    }

    const reasons = []

    // Type check
    if (check.expectedType !== undefined && node.type !== check.expectedType) {
      reasons.push(`type is "${node.type}", expected "${check.expectedType}"`)
    }

    // Name check
    if (check.expectedName !== undefined && node.name !== check.expectedName) {
      reasons.push(`name is "${node.name}", expected "${check.expectedName}"`)
    }

    // Child count check
    if (check.expectedChildCount !== undefined) {
      if (!('children' in node)) {
        reasons.push(
          `node type "${node.type}" does not have children, but expectedChildCount=${check.expectedChildCount} was specified`,
        )
      } else {
        const actualCount = node.children.length
        if (actualCount !== check.expectedChildCount) {
          reasons.push(`has ${actualCount} children, expected ${check.expectedChildCount}`)
        }
      }
    }

    if (reasons.length > 0) {
      failed.push({
        nodeId: check.nodeId,
        reason: reasons.join('; '),
      })
    } else {
      passed.push(check.nodeId)
    }
  }

  return { passed, failed }
}

const page=await figma.getNodeByIdAsync("847:7");await figma.setCurrentPageAsync(page);
const structural=await validateCreation([{nodeId:"847:7",expectedName:"Fuentes",expectedType:"PAGE"},{nodeId:"848:41",expectedName:"Fuentes",expectedType:"COMPONENT_SET",expectedChildCount:2},{nodeId:"848:8",expectedType:"COMPONENT"},{nodeId:"848:19",expectedType:"SLOT",expectedChildCount:2},{nodeId:"848:33",expectedType:"SLOT",expectedChildCount:2}]);
const vars=await figma.variables.getLocalVariablesAsync();const vm=new Map(vars.map(v=>[v.id,v]));const roots=await Promise.all(["848:11","848:26","848:8"].map(id=>figma.getNodeByIdAsync(id)));
function flatten(n){return[n,...("children"in n?n.children.flatMap(flatten):[])];}
const all=roots.flatMap(flatten),paints=[],issues=[],texts=[];
for(const n of all){
for(const f of ["fills","strokes"])if(f in n&&Array.isArray(n[f]))for(const p of n[f]){if(p.type!=="SOLID"||p.visible===false)continue;const v=vm.get(p.boundVariables?.color?.id);const scope=f==="strokes"?"STROKE_COLOR":n.type==="TEXT"?"TEXT_FILL":"FRAME_FILL";paints.push({node:n.id,field:f,variable:v?.id,name:v?.name,color:p.color,scope});if(!v||v.variableCollectionId!=="VariableCollectionId:6:2"||!v.scopes.includes(scope))issues.push({node:n.id,field:f,reason:"semantic/scope"});}
if(n.type==="TEXT"){texts.push({id:n.id,name:n.name,text:n.characters,width:n.width,height:n.height,fontSize:n.fontSize,font:n.fontName,textStyleId:n.textStyleId,bindings:n.boundVariables});if(!n.id.includes("155:135")&&!["fontFamily","fontStyle","lineHeight","letterSpacing"].every(k=>n.boundVariables[k]))issues.push({node:n.id,reason:"typography"});}
}
const fixtureIds=["849:45","849:62","849:83","849:108","849:141"];
const fixtures=[];for(const id of fixtureIds){const n=await figma.getNodeByIdAsync(id);const s=flatten(n).find(n=>n.type==="SLOT");fixtures.push({id,width:n.width,height:n.height,main:(await n.getMainComponentAsync()).id,slot:{id:s.id,width:s.width,height:s.height,layoutMode:s.layoutMode,layoutWrap:s.layoutWrap,violations:s.limitViolations,children:s.children.map(c=>({id:c.id,width:c.width,height:c.height,label:c.componentProperties["Label#848:0"].value,texts:flatten(c).filter(x=>x.type==="TEXT").map(t=>({width:t.width,height:t.height,characters:t.characters}))}))}});}
const themes=[];for(const id of ["849:198","849:213","849:228","849:243"]){const n=await figma.getNodeByIdAsync(id);const location=flatten(n).find(x=>x.name==="Location");themes.push({id,modes:n.explicitVariableModes,fill:n.fills,stroke:n.strokes,brand:location.fills});}
const dot=await figma.getNodeByIdAsync("155:134");const set=await figma.getNodeByIdAsync("848:41");const newV=vm.get("VariableID:847:6");
return JSON.stringify({structural,uniquePage:figma.root.children.filter(p=>p.name==="Fuentes").length,properties:set.componentPropertyDefinitions,masters:roots.slice(0,2).map(n=>({id:n.id,width:n.width,height:n.height,minWidth:n.minWidth,maxWidth:n.maxWidth,padding:[n.paddingTop,n.paddingRight,n.paddingBottom,n.paddingLeft],gap:n.itemSpacing,radius:n.cornerRadius,strokeWeight:n.strokeWeight,strokeAlign:n.strokeAlign,strokesIncludedInLayout:n.strokesIncludedInLayout,explicitVariableModes:n.explicitVariableModes,boundFields:Object.keys(n.boundVariables)})),paints,texts:texts.map(t=>({id:t.id,name:t.name,fontSize:t.fontSize,font:t.font,boundFields:Object.keys(t.bindings)})),issues,fixtures,themes,reactions:all.filter(n=>"reactions"in n&&n.reactions.length).map(n=>n.id),dotMain:{id:dot.id,name:dot.name,width:dot.width,height:dot.height,fills:dot.fills,strokes:dot.strokes,texts:flatten(dot).filter(n=>n.type==="TEXT").map(n=>({font:n.fontName,fills:n.fills,text:n.characters}))},hoverVariable:{id:newV.id,name:newV.name,description:newV.description,scopes:newV.scopes,valuesByMode:newV.valuesByMode}});

