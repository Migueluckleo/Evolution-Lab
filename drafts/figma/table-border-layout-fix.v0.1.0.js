const ids=["548:895","548:408","548:726","548:853","546:257","546:292"];for(const id of ids){const n=await figma.getNodeByIdAsync(id);n.strokesIncludedInLayout=false;}return {mutatedNodeIds:ids};
