const createdNodeIds=[],createdRootIds=[];
let state=STATE;
try{
 const ctx=await sourceContext();
 await verifyStyle('A');await verifyStyle('B');
 if(state){const c=await copies(ctx,state);const obs=await observation(ctx,c,state);assert(equal(obs.sourceGuard,state.baseline.sourceGuard),'Original source guard changed');return{status:'EXISTING_PILOT_READ_ONLY',createdNodeIds,mutatedNodeIds:[],state,observation:obs};}
 assert(!ctx.page.children.some(n=>n.name===CFG.rootNames.owner||n.name===CFG.rootNames.instance),'Pilot names already exist; recover concrete IDs before retry, do not duplicate');
 const guard=await originalGuard(ctx),sourceSnapshot=await snapshot(ctx.root);
 assert(at(ctx.instance,ctx.actorPath).getRangeTextStyleId(0,at(ctx.instance,ctx.actorPath).characters.length)==='','This pilot requires observed blank instance style ID');
 assert(ctx.instance.scaleFactor===Math.fround(4/3),'Unexpected effective source instance scale');
 for(const n of[ctx.actor])assert(n.getRangeTextStyleId(0,n.characters.length)===CFG.styles.A.id,'Original principal is not linked to recipeA');
 await loadFonts(ctx.owner);await loadFonts(ctx.root);
 const x=ctx.page.children.reduce((m,n)=>Math.max(m,'x'in n?n.x+n.width:0),0)+400;
 const owner=ctx.owner.clone();createdRootIds.push(owner.id);owner.name=CFG.rootNames.owner;owner.x=x;owner.y=0;
 createdNodeIds.push(...walk(owner).map(r=>r.node.id));
 const variants=owner.children.filter(n=>n.type==='COMPONENT'&&equal(n.variantProperties,ctx.main.variantProperties));assert(variants.length===1,'Copied exact variant is ambiguous');const main=variants[0];
 const prop=propertyMap(ctx.owner,owner),ownerAliases=aliasesFrom(ctx.owner,owner);
 assert(equal(await snapshot(ctx.owner),await snapshot(owner,ownerAliases,prop.map)),'Owner clone changed geometry, relationships, refs or API');
 const root=ctx.root.clone();createdRootIds.push(root.id);root.name=CFG.rootNames.instance;root.x=x+owner.width+400;root.y=0;const instance=at(root,ctx.instancePath);
 createdNodeIds.push(...walk(root).map(r=>r.node.id));
 const preAliases=aliasesFrom(ctx.root,root);
 assert(equal(sourceSnapshot,await snapshot(root,preAliases)),'Instance clone already differs from original');
 instance.swapComponent(main);
 const aliases={...ownerAliases,...aliasesFrom(ctx.root,root)};
 createdNodeIds.push(...walk(root).map(r=>r.node.id));
 assert((await instance.getMainComponentAsync())?.id===main.id,'Swapped copy does not point to actual copied variant');
 assert(equal(sourceSnapshot,await snapshot(root,aliases,prop.map)),'Swap changed metrics, geometry, properties, refs or overrides; INCONCLUSIVE');
 assert(equal(guard,await originalGuard(ctx)),'Original guard changed');
 state={schema_version:1,styles:CFG.styles,runTag:CFG.runTag,pageId:ctx.page.id,sourceOwnerId:ctx.owner.id,sourceMainId:ctx.main.id,sourceInstanceId:ctx.instance.id,sourceRootId:ctx.root.id,copyRootId:root.id,instancePath:ctx.instancePath,copyOwnerId:owner.id,copyMainId:main.id,copyInstanceId:instance.id,createdRootIds,rootNames:CFG.rootNames,variantProperties:clean(ctx.main.variantProperties),actorPath:ctx.actorPath,controlPath:ctx.controlPath,propertyMap:prop.map};
 const c=await copies(ctx,state),obs=await observation(ctx,c,state);
 state.baseline={sourceGuard:guard,scale:obs.scale,ownerHash:obs.ownerHash,mainHash:obs.mainHash,instanceHash:obs.instanceHash,mainControlHash:hash(obs.mainControl),instanceControlHash:hash(obs.instanceControl),instanceOverridesHash:hash(obs.instanceOverrides)};
 return{status:'READY_FOR_INDEPENDENT_A_READ',createdNodeIds:[...new Set(createdNodeIds)],mutatedNodeIds:[],state,setupIsNotCausalProof:true};
}catch(error){return{status:'INCONCLUSIVE',message:String(error),createdNodeIds:[...new Set(createdNodeIds)],mutatedNodeIds:[],recovery:{createdRootIds,rootNames:CFG.rootNames,sourceInstanceId:CFG.sourceInstanceId},state};}
