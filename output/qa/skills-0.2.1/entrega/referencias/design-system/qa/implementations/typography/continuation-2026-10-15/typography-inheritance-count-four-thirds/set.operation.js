const mutatedNodeIds=[];
try{
 assert(STATE?.baseline,'Require literal persisted successful setup state');const ctx=await sourceContext();const c=await copies(ctx,STATE);const obs=await observation(ctx,c,STATE);assert(equal(obs.sourceGuard,STATE.baseline.sourceGuard),'Original guard changed');
 assert(hash(obs.mainControl)===STATE.baseline.mainControlHash&&hash(obs.instanceControl)===STATE.baseline.instanceControlHash,'Owner control changed');
 assert(hash(obs.instanceOverrides)===STATE.baseline.instanceOverridesHash,'Instance overrides changed');
 const target=CFG.writeTarget,style=await verifyStyle(target),current=c.actor.getRangeTextStyleId(0,c.actor.characters.length);
 if(current===style.id)return{status:'ALREADY_REQUESTED_STYLE_REQUIRE_INDEPENDENT_READ',createdNodeIds:[],mutatedNodeIds,state:STATE};
 if(target==='B')assert(obs.ownerHash===STATE.baseline.ownerHash&&obs.mainHash===STATE.baseline.mainHash&&obs.instanceHash===STATE.baseline.instanceHash,'RecipeB precondition is not exact baselineA');
 else assert(current===CFG.styles.B.id,'Restore only permits the known recipeB on copied actor');
 await loadFonts(c.owner);await figma.loadFontAsync({family:style.fontName.family,style:style.fontName.style});
 mutatedNodeIds.push(c.actor.id,c.instanceActor.id);
 await c.actor.setRangeTextStyleIdAsync(0,c.actor.characters.length,style.id);
 assert(equal(await originalGuard(ctx),STATE.baseline.sourceGuard),'Original guard changed during pilot write');
 return{status:'WRITE_COMPLETED_REQUIRE_INDEPENDENT_READ',target,createdNodeIds:[],mutatedNodeIds,affectedCopyRootIds:[c.owner.id,c.root.id],state:STATE,validation:'NOT_VALIDATED_IN_WRITE_CALL'};
}catch(error){return{status:'INCONCLUSIVE',createdNodeIds:[],mutatedNodeIds,message:String(error),state:STATE};}
