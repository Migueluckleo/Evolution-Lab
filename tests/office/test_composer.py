"""Independent composer behavior tests; fake DOM/network, never invoke a model."""
import json
import shutil
import subprocess
import unittest

import test_office as fixtures


HARNESS = r"""
const vm=require('node:vm'),fs=require('node:fs');
const input=JSON.parse(fs.readFileSync(0,'utf8')),all=[],timers=[],requests=[];
class Element {
 constructor(tag){this.tag=tag;this.children=[];this.dataset={};this.style={setProperty(){}};this.value='';this._text='';this.scrollTop=0;this.scrollHeight=0;this.clientHeight=0;this.disabled=tag==='send';all.push(this)}
 set textContent(v){this._text=String(v)} get textContent(){return this._text}
 set innerHTML(v){throw Error('Unsafe HTML sink')}
 append(...v){this.children.push(...v)} replaceChildren(...v){this.children=v}
 querySelector(tag){return this.summary??=new Element(tag)} setAttribute(){}
 requestSubmit(){return this.onsubmit({preventDefault(){}})}
}
const ids={},document={hidden:false,getElementById(id){return ids[id]??=new Element(id)},createElement(tag){return new Element(tag)}};
document.getElementById('data').textContent=JSON.stringify(input.data);
let uuid=0,posts=0,mode='normal',jobStatus='running',sessionToken='session-token',active=input.scenario==='busy'?{id:'active-job',status:'running'}:null;
let stream=input.scenario.startsWith('stream'),lastJob=null;
if(stream){active={id:'stream-job',status:'running',updates:[],started_at:new Date(Date.now()-65000).toISOString(),last_activity_at:new Date(Date.now()-65000).toISOString(),activity:'Esperando el primer evento de Codex'};}
if(input.scenario==='stream_reload'){lastJob={...active,status:'completed',updates:[{id:'public-1',actor:'eva',kind:'message',message:'Avance público conservado',timestamp:new Date().toISOString()}]};active=null;}
const jobs=new Map();
function response(body,status=200){return {ok:status<400,status,json:async()=>JSON.parse(JSON.stringify(body))}}
const context={document,window:{},location:{protocol:'http:'},AbortController,crypto:{randomUUID(){return 'request-'+(++uuid)}},
 setTimeout(fn,delay){timers.push({fn,delay});return timers.length},clearTimeout(){},
 async fetch(url,opts={}){
  requests.push({url,opts});
  if(url==='./state.json')return response(input.data);
  if(url==='/api/session')return response({token:sessionToken,active_job:active,last_job:lastJob});
  if(url.startsWith('/api/jobs/')){if(mode==='offline')throw Error('Offline');return response({job:stream?active:{id:url.split('/').pop(),status:jobStatus,error:jobStatus==='failed'?'Fallo verificado':null}});}
  if(url==='/api/messages'){
   posts++;assert(opts.method==='POST','No POST');assert(opts.headers['X-Office-Token']===sessionToken,'Token missing or stale');
   const p=JSON.parse(opts.body);if(mode==='busy'){active={id:'other-job',status:'running'};return response({error:'Hay una ejecución activa'},409)}
   if(mode==='expired'){sessionToken='fresh-token';mode='normal';return response({error:'Sesión inválida; recarga la oficina'},403)}
   if(!jobs.has(p.request_id))jobs.set(p.request_id,{id:p.request_id,status:'running'});
   if(mode==='lost'){mode='normal';throw Error('Response lost after acceptance')}
   return response({job:jobs.get(p.request_id)},202);
  }
  throw Error('Unexpected endpoint '+url);
 }};
function assert(ok,message){if(!ok)throw Error(message)}
function texts(node){return [node.textContent,...node.children.flatMap(texts)]}
const tick=()=>new Promise(setImmediate);
async function submit(text){ids.message.value=text;await ids.composer.requestSubmit();await tick()}
(async()=>{
 vm.createContext(context);vm.runInContext(input.script,context,{timeout:1000});await tick();
 if(input.scenario==='retry'){
  assert(!ids.send.disabled,'Ready composer disabled');mode='lost';await submit('Solicitud de prueba');
  assert(ids.message.value==='Solicitud de prueba','Text lost on uncertain delivery');
  assert(!ids.send.disabled,'Retry disabled');assert(ids['send-status'].textContent.includes('No se confirmó'),'Uncertain status hidden');
  await submit('Solicitud de prueba');assert(posts===2,'Retry not submitted');assert(jobs.size===1&&uuid===1,'Retry creates duplicate job');
  const bodies=requests.filter(r=>r.url==='/api/messages').map(r=>r.opts.body);assert(bodies[0]===bodies[1],'Retry changed payload');
  assert(ids.message.value===''&&ids.send.disabled,'Accepted job did not clear text/block submit');
  assert(!ids.feed.children.some(e=>e.className==='event'),'UI invented message before ledger confirmation');
  jobStatus='completed';await vm.runInContext('watchJob()',context);assert(!ids.send.disabled,'Completed job remains busy');
  assert(ids['send-status'].textContent.includes('Eva respondió'),'Completion not visible');
 }else if(input.scenario==='busy'){
  assert(ids.send.disabled,'Existing job did not disable composer');await submit('Another request');assert(posts===0,'Busy UI dispatched');
  jobStatus='failed';await vm.runInContext('watchJob()',context);assert(!ids.send.disabled,'Failed job remains busy');
  assert(ids['send-status'].textContent==='Fallo verificado','Failure hidden');
 }else if(input.scenario==='conflict'){
  mode='busy';await submit('Keep this text');await tick();assert(ids.message.value==='Keep this text','409 lost input');
  assert(ids.send.disabled,'409 did not reload active job');assert(posts===1,'409 auto-retried command');
 }else if(input.scenario==='expired'){
  mode='expired';await submit('Preserve after restart');await tick();
  assert(ids.message.value==='Preserve after restart','Session expiry lost input');
  assert(posts===1,'Session refresh automatically resubmitted command');
  assert(requests.filter(r=>r.url==='/api/session').length===2,'403 did not refresh session');
  await submit('Preserve after restart');assert(jobs.size===1&&uuid===1,'Recovery changed idempotency key or failed');
 }else if(input.scenario==='user'){
  assert(ids.feed.children.length===2,'User request/response missing');
  assert(all.some(e=>e.tag==='strong'&&e.textContent==='Tú'),'User identity not rendered');
  assert(all.some(e=>e.className==='reply'&&e.textContent.startsWith('Tú: ')),'User correlation quote missing');
  assert(all.some(e=>e.tag==='p'&&e.textContent===input.attack),'User payload was not text');assert(!context.pwned,'Payload executed');
 }else if(input.scenario==='stream_reload'){
  assert(texts(ids.feed).includes('Avance público conservado'),'Reload lost persisted updates');
  assert(!ids.send.disabled,'Reload of completed job claims still busy');assert(posts===0,'Reload resubmitted job');
 }else if(input.scenario==='streaming'){
  assert(ids['send-status'].textContent.includes('Sin novedades'),'Silent process presented as progress');
  assert(!ids.feed.children.some(e=>e.className==='event'),'Process start invented a message');
  const stamp=new Date().toISOString();active.updates=[
   {id:'private',actor:'eva',kind:'reasoning',message:'PRIVATE REASONING',timestamp:stamp},
   {id:'activity',actor:'eva',kind:'activity',message:'PRIVATE COMMAND',timestamp:stamp},
   {id:'public-1',actor:'eva',kind:'message',message:'Avance público parcial',timestamp:stamp}];
  active.last_activity_at=stamp;active.activity='Mensaje público recibido';await vm.runInContext('watchJob()',context);
  assert(texts(ids.feed).includes('Avance público parcial'),'Public update not shown before completion');
  assert(!texts(ids.feed).includes('PRIVATE REASONING')&&!texts(ids.feed).includes('PRIVATE COMMAND'),'Nonpublic updates rendered');
  assert(ids.send.disabled,'Streaming incorrectly finished job');
  active.updates[2].message='Avance público actualizado';await vm.runInContext('watchJob()',context);
  assert(!texts(ids.feed).includes('Avance público parcial'),'Updated item duplicated stale text');
  assert(texts(ids.feed).filter(t=>t==='Avance público actualizado').length===1,'Public update duplicated');
  mode='offline';await vm.runInContext('watchJob()',context);
  assert(ids['send-status'].textContent.includes('Se perdió'),'Offline status hidden');
  assert(texts(ids.feed).includes('Avance público actualizado')&&posts===0,'Offline discarded/reposted progress');
  mode='normal';active.updates.push({id:'final',actor:'eva',kind:'message',message:'Respuesta final pública',timestamp:stamp});
  active.status='completed';await vm.runInContext('watchJob()',context);
  input.data.events=[{id:'terminal',from:'eva',to:'user',kind:'response',message:'Respuesta final pública',timestamp:stamp,status:'RECORDED',evidence:[],tool_ref:'codex-exec:stream-job',why:'Fixture',scope:'Fixture',deliverable:'Fixture',objective:input.data.config.objectives[0].id}];input.data.revision+='-final';
  await vm.runInContext('sync()',context);
  assert(texts(ids.feed).filter(t=>t==='Respuesta final pública').length===1,'Final response duplicated between progress and ledger');
  assert(texts(ids.feed).includes('Avance público actualizado'),'Finalization discarded progress');
  assert(texts(ids.feed).indexOf('Avance público actualizado')<texts(ids.feed).indexOf('Respuesta final pública'),'Earlier progress appears after final response');
  assert(!ids.send.disabled,'Final response leaves busy');
 }else if(input.scenario==='stream_error'){
  active.updates=[{id:'public-1',actor:'eva',kind:'message',message:'Avance antes del fallo',timestamp:new Date().toISOString()}];
  active.status='failed';active.error='Fallo real de la ejecución';await vm.runInContext('watchJob()',context);
  assert(texts(ids.feed).includes('Avance antes del fallo'),'Failure discarded observed update');
  assert(ids['send-status'].textContent==='Fallo real de la ejecución'&&!ids.send.disabled,'Failure hidden or composer stuck');
  assert(posts===0,'Failure auto-retried command');
 }else if(input.scenario==='keyboard'){
  ids.message.value='Keyboard request';ids.message.onkeydown({key:'Enter',ctrlKey:true,preventDefault(){}});await tick();
  assert(posts===1&&ids.send.disabled,'Ctrl Enter did not submit exactly once');
 }
 console.log('PASS '+input.scenario);
})().catch(e=>{console.error(e);process.exitCode=1});
"""


class ComposerTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.OfficeTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def execute(self, scenario, attack=None):
        from test_office import office
        office.render(self.fixture.root)
        parser = fixtures.Scripts()
        parser.feed((self.fixture.root / "office/dist/index.html").read_text())
        node = shutil.which("node")
        if not node:
            self.skipTest("Node required for isolated composer execution")
        result = subprocess.run([node, "-e", HARNESS], input=json.dumps({
            "scenario": scenario, "data": json.loads(parser.blocks[0]["data"]),
            "script": parser.blocks[1]["data"], "attack": attack,
        }), capture_output=True, text=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_uncertain_ack_retry_reuses_id_and_completion_unlocks(self):
        self.execute("retry")

    def test_existing_busy_job_blocks_submit_and_failed_job_unlocks(self):
        self.execute("busy")

    def test_conflict_preserves_text_and_refreshes_active_job(self):
        self.execute("conflict")

    def test_keyboard_shortcut_submits_once(self):
        self.execute("keyboard")

    def test_expired_session_refreshes_without_losing_text_or_resubmitting(self):
        self.execute("expired")

    def test_public_streaming_before_exit_silence_disconnect_and_final_dedup(self):
        self.execute("streaming")

    def test_reload_recovers_completed_public_updates_without_resubmitting(self):
        self.execute("stream_reload")

    def test_stream_failure_preserves_updates_and_shows_error(self):
        self.execute("stream_error")

    def test_user_messages_render_as_inert_text_with_correlated_reply(self):
        attack = '</script><img src=x onerror="globalThis.pwned=true">'
        request = self.fixture.record(self.fixture.payload("request", **{"from": "user", "to": "eva"}, message=attack))
        self.fixture.record(self.fixture.payload("response", **{"from": "eva", "to": "user"}, reply_to=request, message="Respuesta comprobada"))
        self.execute("user", attack)


if __name__ == "__main__":
    unittest.main()
