try{
 assert(STATE?.baseline,'Require literal persisted successful setup state');const ctx=await sourceContext();const c=await copies(ctx,STATE);const obs=await observation(ctx,c,STATE);const issues=[];
 if(!equal(obs.sourceGuard,STATE.baseline.sourceGuard))issues.push('ORIGINAL_GUARD_CHANGED');if(obs.scale!==STATE.baseline.scale)issues.push('INSTANCE_SCALE_CHANGED');
 if(hash(obs.mainControl)!==STATE.baseline.mainControlHash||hash(obs.instanceControl)!==STATE.baseline.instanceControlHash)issues.push('OWNER_CONTROL_CHANGED');
 if(hash(obs.instanceOverrides)!==STATE.baseline.instanceOverridesHash)issues.push('COPY_INSTANCE_OVERRIDES_CHANGED');
 if(CFG.readPhase==='A'||CFG.readPhase==='RESTORED_A')if(obs.ownerHash!==STATE.baseline.ownerHash||obs.mainHash!==STATE.baseline.mainHash||obs.instanceHash!==STATE.baseline.instanceHash)issues.push('BASELINE_NOT_RESTORED');
 return{status:issues.length?'INCONCLUSIVE':'READBACK_CAPTURED',phase:CFG.readPhase,capturedAt:new Date().toISOString(),createdNodeIds:[],mutatedNodeIds:[],issues,state:STATE,observation:{...obs,geometry:{main:{rowCount:obs.geometry.main.length,fullRowsHash:hash(obs.geometry.main)},instance:{rowCount:obs.geometry.instance.length,fullRowsHash:hash(obs.geometry.instance)},policy:'Full geometry and componentProperties retained in internal snapshot/hash checks; bulky rows omitted from transport'}},validation:'NO_GLOBAL_PASS_FROM_PILOT'};
}catch(error){return{status:'INCONCLUSIVE',createdNodeIds:[],mutatedNodeIds:[],message:String(error),state:STATE};}
