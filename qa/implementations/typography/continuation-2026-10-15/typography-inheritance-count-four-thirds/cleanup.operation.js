const removedNodeIds=[],errors=[];
const roots=STATE?.createdRootIds||STATE?.recovery?.createdRootIds||[];
assert(roots.length>0&&roots.length<=2,'Cleanup needs concrete previously returned root IDs');
let ctx=null,guard=null;try{ctx=await sourceContext();guard=await originalGuard(ctx);}catch(error){errors.push('Source read: '+String(error));}
const names=STATE.rootNames||STATE.recovery?.rootNames;
for(const id of [...roots].reverse()){
 const n=await figma.getNodeByIdAsync(id);if(!n)continue;
 if(!['COMPONENT_SET','INSTANCE'].includes(n.type)||![names.owner,names.instance].includes(n.name)||id===CFG.sourceRootId||id===CFG.sourceInstanceId||id===CFG.sourceMainId){errors.push('Ownership mismatch; preserved '+id);continue;}
 if(n.parent?.type!=='PAGE'){errors.push('Pilot root moved; preserved '+id);continue;}
 removedNodeIds.push(...walk(n).map(r=>r.node.id));n.remove();
}
if(ctx&&guard&&!equal(guard,await originalGuard(ctx)))errors.push('Original guard changed during cleanup');
return{status:errors.length?'INCONCLUSIVE':'CLEANUP_COMPLETE',createdNodeIds:[],mutatedNodeIds:removedNodeIds,removedNodeIds,errors,validation:'NO_GLOBAL_PASS_FROM_PILOT'};
