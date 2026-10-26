"""Compare a graph query with verified raw reading of exactly the same documents."""
import argparse
import json
from pathlib import Path
import time
from consumer_graph import Reader, canonical, safe, sha


def benchmark(runtime, component='BUTTON-001'):
    engine=Reader(runtime)
    fallback=Reader(runtime)
    fallback.index=None
    fallback.reason='BENCHMARK_NO_INDEX'
    rows=[]
    for intent in ['component','dependencies','evidence','variants','states','tokens']:
        query=engine.query({'schema_version':1,'component':component,'intent':intent})
        fallback_query=fallback.query({'schema_version':1,'component':component,'intent':intent})
        start=time.perf_counter();documents=[];total=0
        for item in query['documents']:
            raw=safe(engine.snapshot,item['path']).read_bytes()
            if sha(raw) != item['sha256']:raise ValueError('Snapshot changed during benchmark')
            total+=len(raw);documents.append({'path':item['path'],'text':raw.decode()})
        rows.append({'intent':intent,'status':query['status'],'mode':query['mode'],'reason':query['reason'],
                     'graph':query['metrics'],'selective_control':{'files_read':len(documents),'bytes_read':total,
                     'context_bytes':len(canonical(documents)),'duration_ms':round((time.perf_counter()-start)*1000,3)},
                     'fallback':{'status':fallback_query['status'],'coverage':fallback_query.get('coverage'),
                                 'metrics':fallback_query['metrics'],'paths':[d['path'] for d in fallback_query['documents']]},
                     'paths':[d['path'] for d in documents], 'tokens_returned':len(query.get('tokens',[]))})
    return {'schema_version':1,'snapshot':engine.identity,'component':component,
            'method':'Selective control reads full originals of exactly the graph-selected set. Additional fallback disables the index only in memory and reads contract/amendments, with narrower coverage. No claim of baseline discovery cost or network savings. Timings depend on local cache.',
            'rows':rows}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--runtime',type=Path,required=True)
    parser.add_argument('--output',type=Path);parser.add_argument('--component',default='BUTTON-001');args=parser.parse_args()
    result=benchmark(args.runtime,args.component)
    text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text)
