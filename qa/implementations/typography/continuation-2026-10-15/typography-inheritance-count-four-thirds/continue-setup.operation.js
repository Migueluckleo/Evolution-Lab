// Read-only continuation of the existing post-swap copies; never clones or writes styles.
let state=null;const recovery={createdRootIds:['1063:1392','1063:1414'],rootNames:CFG.rootNames,sourceInstanceId:CFG.sourceInstanceId};
try{
 const ctx=await sourceContext();await verifyStyle('A');await verifyStyle('B');
 const owner=await figma.getNodeByIdAsync('1063:1392'),root=await figma.getNodeByIdAsync('1063:1414');
 assert(owner?.type==='COMPONENT_SET'&&root?.type==='INSTANCE','Existing exact copy roots missing');
 assert(owner.name===CFG.rootNames.owner&&root.name===CFG.rootNames.instance,'Copy ownership names differ');
 assert(owner.parent?.id===ctx.page.id&&root.parent?.id===ctx.page.id,'Copy roots moved');
 const matches=owner.children.filter(n=>n.type==='COMPONENT'&&equal(n.variantProperties,ctx.main.variantProperties));assert(matches.length===1&&matches[0].id==='1063:1406','Exact copied variant differs');const main=matches[0],instance=at(root,ctx.instancePath);
 assert(instance.id==='I1063:1414;183:164'&&(await instance.getMainComponentAsync())?.id===main.id,'Actual nested Count main link differs');
 const guard=await originalGuard(ctx),prop=propertyMap(ctx.owner,owner),aliases={...aliasesFrom(ctx.owner,owner),...aliasesFrom(ctx.root,root)};
 assert(equal(await snapshot(ctx.owner),await snapshot(owner,aliases,prop.map)),'Owner differs from source');
 assert(equal(await snapshot(ctx.root),await snapshot(root,aliases,prop.map)),'Context copy differs beyond exact observed redundant name/layoutPositioning entries');
 assert(equal(guard,await originalGuard(ctx)),'Original source guard changed');
 state={schema_version:1,styles:CFG.styles,runTag:CFG.runTag,pageId:ctx.page.id,sourceOwnerId:ctx.owner.id,sourceMainId:ctx.main.id,sourceInstanceId:ctx.instance.id,sourceRootId:ctx.root.id,copyRootId:root.id,instancePath:ctx.instancePath,copyOwnerId:owner.id,copyMainId:main.id,copyInstanceId:instance.id,createdRootIds:recovery.createdRootIds,rootNames:CFG.rootNames,variantProperties:clean(ctx.main.variantProperties),actorPath:ctx.actorPath,controlPath:ctx.controlPath,propertyMap:prop.map,normalizationEvidence:'diagnose-clone-diff.result.json: only two redundant override entries, property values unchanged'};
 const c=await copies(ctx,state),obs=await observation(ctx,c,state);
 state.baseline={sourceGuard:guard,scale:obs.scale,ownerHash:obs.ownerHash,mainHash:obs.mainHash,instanceHash:obs.instanceHash,mainControlHash:hash(obs.mainControl),instanceControlHash:hash(obs.instanceControl),instanceOverridesHash:hash(obs.instanceOverrides)};
 return{status:'READY_FOR_INDEPENDENT_A_READ',createdNodeIds:[],mutatedNodeIds:[],state,recovery,setupIsNotCausalProof:true};
}catch(error){return{status:'INCONCLUSIVE',message:String(error),createdNodeIds:[],mutatedNodeIds:[],state,recovery};}
