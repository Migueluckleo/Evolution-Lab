"""Graph consumption, malicious inputs, deterministic projection and portable packages."""
import copy
import io
import tarfile
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
import consumer_graph as reader
import ds_consumption as export
import ds_skills as skills
import ds_remote as remote
from test_remote import loader


class ConsumptionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.files = {
            'specs/button.md': b'---\ncontract_id: BUTTON-001\nversion: 1.0.0\nstatus: APPROVED\n---\n# Button\n## Variants\nprimary\n## States\ndefault\n## Tokens\n[Tokens](tokens/palette.json)\n',
            'specs/amendment.md': b'---\nversion: 1.1.0\nstatus: DELEGATED_FOR_BUILD\n---\n# Binding amendment\nApplies to [Button](button.md) only.\n',
            'specs/tokens/palette.json': b'{"variables":[{"name":"button/background","valuesByMode":{"light":"blue"}}]}',
            'registry/private.md': b'PRIVATE-SECRET-CANARY',
            'specs/unrelated.md': b'# Unrelated\n'
        }
        for path,data in self.files.items():
            target = self.root/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
        self.components = [{'id':'BUTTON-001','contract':'specs/button.md','amendments':['specs/amendment.md']}]
        hashes = {p:reader.sha(b) for p,b in self.files.items()}
        self.state = {'files':hashes,'ds_digest':reader.sha(reader.canonical(hashes)),'components':self.components}
        self.graph = {'nodes':[{'id':p,'source_file':p,'sha256':h,'label':'PRIVATE-SECRET-CANARY'} for p,h in hashes.items()]+[
            {'id':'variant','source_file':'specs/button.md','source_location':'L7'},
            {'id':'states','source_file':'specs/button.md','source_location':'L9'},
            {'id':'token','source_file':'specs/tokens/palette.json','source_location':'JSON:/variables/0','label':'button/background'}],
            'links':[{'source':'specs/button.md','target':'specs/tokens/palette.json','source_file':'specs/button.md','source_location':'L12','relation':'references','confidence':'EXTRACTED','confidence_score':1.0}]}
        self.index = export.project(self.root,self.state,self.graph,'a'*40)
        self.runtime = self.root/'runtime';self.snapshot = self.runtime/'assets/design-system'
        for p,b in self.files.items():
            dest=self.snapshot/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
        self.publish()

    def publish(self,index=True):
        self.manifest={'schema_version':1,'package_version':'0.0.0+fixture',**self.state}
        if index:
            data=reader.canonical(self.index)
            (self.runtime/'assets/consumption-graph.json').write_bytes(data)
            self.manifest['consumption_graph']={'schema_version':1,'sha256':reader.sha(data),'bytes':len(data)}
        raw=reader.canonical(self.manifest)
        (self.runtime/'assets/snapshot-manifest.json').write_bytes(raw)
        (self.runtime/'assets/remote-receipt.json').write_text(json.dumps({'manifest_sha256':reader.sha(raw),'ds_digest':self.state['ds_digest']}))

    def query(self,**extra):
        return reader.Reader(self.runtime).query({'schema_version':1,'component':'BUTTON-001','intent':'component',**extra})

    def test_directed_query_and_amendment(self):
        q=self.query();self.assertEqual(q['status'],'PASS')
        self.assertEqual({d['path'] for d in q['documents']},{'specs/button.md','specs/amendment.md','specs/tokens/palette.json'})
        self.assertEqual(q['metrics']['files_read'],3)
        self.assertEqual(next(n for n in q['nodes'] if n['id']=='specs/amendment.md')['document_status'],'DELEGATED_FOR_BUILD')

    def test_variants_states_and_token_pointer(self):
        for intent,expected in [('variants','primary'),('states','default')]:
            q=self.query(intent=intent);self.assertEqual(q['status'],'PASS');self.assertIn(expected,q['documents'][1]['text'])
        q=self.query(intent='tokens',token='button/background')
        self.assertEqual(q['status'],'PASS');self.assertEqual(q['tokens'][0]['value']['name'],'button/background')

    def test_export_deterministic_and_no_private_fields(self):
        again=export.project(self.root,self.state,self.graph,'a'*40)
        self.assertEqual(again,self.index)
        self.assertNotIn('PRIVATE-SECRET-CANARY',reader.canonical(again).decode())
        self.assertNotIn('registry/private.md',reader.canonical(again).decode())
        self.assertEqual(export.validate_sources(self.root,self.state,again),again)

    def test_stale_missing_incompatible_and_tampered_fallback(self):
        for key,value,reason in [('status','STALE','STALE'),('schema_version',999,'INCOMPATIBLE')]:
            old=self.index[key];self.index[key]=value;self.publish()
            q=self.query();self.assertEqual(q['status'],'FALLBACK');self.assertEqual(q['reason'],reason)
            self.index[key]=old
        self.publish(False);self.assertEqual(self.query()['reason'],'MISSING')
        self.publish();(self.runtime/'assets/consumption-graph.json').write_text('{}')
        self.assertEqual(self.query()['reason'],'INTEGRITY')

    def test_conflict_and_limits_never_partial_success(self):
        self.index['documents']['specs/button.md']['status']='CONFLICT';self.publish()
        q=self.query();self.assertEqual(q['reason'],'CONFLICT');self.assertEqual(q['documents'],[])
        self.index['documents']['specs/button.md']['status']='APPROVED';self.publish()
        self.assertEqual(self.query(max_documents=1)['reason'],'LIMIT_EXCEEDED')
        self.assertEqual(self.query(max_bytes=1)['documents'],[])
        self.assertEqual(self.query(component='Button')['reason'],'UNKNOWN_COMPONENT')

    def test_bad_snapshot_never_falls_back(self):
        (self.runtime/'assets/snapshot-manifest.json').write_text('{}')
        with self.assertRaises(ValueError): reader.Reader(self.runtime)

    def test_fallback_blocks_quoted_conflicts_and_obsolete_roots(self):
        original=self.files['specs/button.md']
        for scalar,reason in [('"CONFLICT"','CONFLICT'),("'CONFLICT' # reason",'CONFLICT'),
                              ('CONFLICT # reason','CONFLICT'),('"SUPERSEDED"','OBSOLETE_REFERENCE'),
                              ("'REJECTED'",'OBSOLETE_REFERENCE'),('*status_alias','STATUS_UNRESOLVED')]:
            data=original.replace(b'APPROVED',scalar.encode())
            (self.snapshot/'specs/button.md').write_bytes(data)
            self.state['files']['specs/button.md']=reader.sha(data)
            self.state['ds_digest']=reader.sha(reader.canonical(self.state['files']))
            for broken_index in [False,True]:
                self.publish(broken_index)
                if broken_index:(self.runtime/'assets/consumption-graph.json').write_text('{}')
                result=self.query()
                self.assertEqual((result['status'],result['reason']),('BLOCKED',reason))
                self.assertEqual(result['documents'],[])

    def test_status_parser_ignores_body_examples_and_rejects_ambiguity(self):
        self.assertEqual(reader.explicit_status('---\n"status": "APPROVED" # verified\n---\nstatus: CONFLICT'),'APPROVED')
        self.assertIsNone(reader.explicit_status('# Example\nstatus: CONFLICT'))
        for body in ['status: APPROVED\nstatus: CONFLICT','status: !!str CONFLICT','status: >\n  CONFLICT']:
            with self.assertRaisesRegex(ValueError,'STATUS_UNRESOLVED'):
                reader.explicit_status('---\n'+body+'\n---')

    def test_changed_source_and_symlink_block(self):
        (self.snapshot/'specs/button.md').write_text('altered')
        self.assertEqual(self.query()['status'],'BLOCKED')
        (self.snapshot/'specs/button.md').unlink();(self.snapshot/'specs/button.md').symlink_to(self.root/'registry/private.md')
        self.assertEqual(self.query()['status'],'BLOCKED')

    def test_isolation_and_unknown_fields_rejected(self):
        for path in ['../private.md','/etc/passwd','registry/private.md']:
            index=copy.deepcopy(self.index);index['documents'][path]=index['documents']['specs/button.md']
            with self.assertRaises(ValueError):reader.validate_index(index,self.manifest)
        self.index['secret']='PRIVATE-SECRET-CANARY'
        with self.assertRaises(ValueError):reader.validate_index(self.index,self.manifest)

    def test_broken_graph_and_forged_relationship_rejected(self):
        bad=copy.deepcopy(self.graph);bad['links'][0]['target']='absent'
        with self.assertRaises(ValueError):export.project(self.root,self.state,bad,'a'*40)
        self.index['relations'][0]['line']=1
        with self.assertRaises(ValueError):export.validate_sources(self.root,self.state,self.index)

    def test_coverage_gap_fallback(self):
        del self.index['documents']['specs/amendment.md'];self.index['components']['BUTTON-001']['covered']=False;self.publish()
        self.assertEqual(self.query()['reason'],'COVERAGE_GAP')

    def test_preparation_rejects_stale_graph(self):
        with patch('ds_graph.check_graph',return_value={'status':'STALE','errors':['delta']}):
            with self.assertRaisesRegex(ValueError,'CURRENT'):export.prepare(ROOT)

    def remote_objects(self):
        raw=reader.canonical(self.manifest);identity=reader.sha(raw)
        stream=io.BytesIO()
        with tarfile.open(fileobj=stream,mode='w:gz') as archive:
            for path,data in self.files.items():
                item=tarfile.TarInfo(path);item.size=len(data);archive.addfile(item,io.BytesIO(data))
        bundle=stream.getvalue()
        pointer={'schema_version':1,'engine_protocol':1,'manifest':f'catalog/releases/{identity}/manifest.json',
                 'manifest_sha256':identity,'bundle':f'catalog/releases/{identity}/data.tar.gz',
                 'bundle_sha256':reader.sha(bundle),'bundle_bytes':len(bundle),'ds_digest':self.state['ds_digest']}
        return {'catalog/current.json':reader.canonical(pointer),pointer['manifest']:raw,pointer['bundle']:bundle,
                f'catalog/releases/{identity}/consumption-graph.json':reader.canonical(self.index)}

    def test_long_inline_prose_is_not_a_file_reference(self):
        text='`'+', '.join('N'+str(i) for i in range(400))+'`'
        self.assertEqual(export.reference_targets(self.root,'specs/button.md',text),set())

    def test_historical_integer_and_unknown_locations(self):
        self.graph['nodes'][5]['source_location']=7
        self.graph['links'][0]['source_location']=12
        index=export.project(self.root,self.state,self.graph,'a'*40)
        self.assertTrue(index['relations'])
        self.graph['nodes'][5]['source_location']={'unknown':'opaque'}
        export.project(self.root,self.state,self.graph,'a'*40)

    def test_yaml_data_reference_preserved(self):
        data=b'---\ncontract_id: BUTTON-001\nversion: 1.0.0\nstatus: APPROVED\ndata_ref: specs/tokens/palette.json\n---\n# Button\n'
        (self.root/'specs/button.md').write_bytes(data)
        self.state['files']['specs/button.md']=reader.sha(data)
        self.state['ds_digest']=reader.sha(reader.canonical(self.state['files']))
        self.graph['nodes'][0]['sha256']=reader.sha(data)
        self.graph['links'][0]['source_location']='L5'
        index=export.project(self.root,self.state,self.graph,'a'*40)
        self.assertEqual(index['relations'][0]['target'],'specs/tokens/palette.json')
        export.validate_sources(self.root,self.state,index)

    def test_invalid_token_pointer_blocks_without_exception(self):
        token=self.index['tokens'].pop(next(iter(self.index['tokens'])))
        token['pointer']='/variables/99999'
        self.index['tokens'][token['source']+'#'+token['pointer']]=token
        self.publish()
        self.assertEqual(self.query(intent='tokens')['status'],'BLOCKED')

    def test_loader_invalid_optional_index_falls_back_after_valid_snapshot(self):
        engine=self.root/'engine';(engine/'assets').mkdir(parents=True)
        (engine/'assets/engine.json').write_bytes(reader.canonical({'engine_protocol':1,'repository':'Migueluckleo/Evolution-Lab','branch':'main','version':'1.0.0'}))
        objects=self.remote_objects()
        graph_path=next(p for p in objects if p.endswith('consumption-graph.json'))
        objects[graph_path]=b'altered'
        runtime=self.root/'loaded'
        result=loader.resolve(engine,runtime,self.root/'cache',lambda path,limit:objects[path])
        self.assertEqual(result['graph']['mode'],'fallback')
        query=reader.Reader(runtime).query({'schema_version':1,'component':'BUTTON-001','intent':'component'})
        self.assertEqual(query['status'],'FALLBACK')
        self.assertTrue(query['documents'])

    def test_invalid_collection_types_fall_back(self):
        for key in ['documents','tokens','relations','components']:
            original=self.index[key]
            for value in [None,42,[],{}]:
                if type(value) == type(original): continue
                self.index[key]=value;self.publish()
                self.assertEqual(self.query()['status'],'FALLBACK',(key,value))
            self.index[key]=original

    def test_explicit_publication_hold_blocks_ci(self):
        with patch.object(export,'source_inputs',return_value=self.state),patch.object(export,'prepared',return_value=b'valid'),patch.object(export,'yaml_documents',return_value={'specs/button.md':{'value':{'publication_policy':'HOLD_UNTIL_USER_REVIEW'}}}):
            with self.assertRaisesRegex(ValueError,'PUBLICATION_HOLD'):export.publication_check(self.root)

    def test_publication_failure_preserves_pointer(self):
        directory=self.root/'catalog';directory.mkdir();pointer=directory/'current.json';pointer.write_text('previous')
        with patch.object(remote,'source_inputs',return_value=self.state),patch.object(export,'prepared',side_effect=ValueError('STALE')):
            with self.assertRaises(ValueError):remote.build(self.root)
        self.assertEqual(pointer.read_text(),'previous')

    def test_prepared_payload_detects_tooling_drift(self):
        for path in export.TOOLING:
            target=self.root/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((ROOT/path).read_bytes())
        data=reader.canonical(self.index)
        proof={'schema_version':1,'status':'CURRENT','index_sha256':reader.sha(data),'ds_digest':self.state['ds_digest'],
               'source_commit':self.index['source_commit'],'source_graph_sha256':self.index['source_graph_sha256'],
               'tooling':export.tooling_hashes(self.root)}
        for path,value in [(export.PREPARED,data),(export.ATTESTATION,reader.canonical(proof))]:
            target=self.root/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(value)
        self.assertEqual(export.prepared(self.root,self.state),data)
        (self.root/'scripts/consumer_graph.py').write_text('changed')
        with self.assertRaises(ValueError):export.prepared(self.root,self.state)

    def test_both_distributed_engines_use_shared_adapter_without_checkout(self):
        shared=(ROOT/'scripts/consumer_graph.py').read_bytes()
        for name in ['contpaqi-figma-screens','contpaqi-po-prototypes']:
            state={'root':ROOT,'config':{'delivery':'github-live-v1','skills':['contpaqi-figma-screens','contpaqi-po-prototypes']},
                   'templates':{name:{'scripts/resolve_ds.py':'unused','SKILL.md':'unused'}}}
            files=skills.package_files(state,'1.0.0',name)
            archive=skills.zip_bytes(name,files)
            import io
            with zipfile.ZipFile(io.BytesIO(archive)) as z:z.extractall(self.root/'installed')
            engine=self.root/'installed'/name
            self.assertEqual((engine/'scripts/consumer_graph.py').read_bytes(),shared)
            runtime=self.root/('runtime-'+name)
            objects = self.remote_objects()
            channel = self.root/'channel'
            for path,data in objects.items():
                target=channel/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
            # Isolated process imports only the extracted engine, fetches a pinned local
            # transport fixture and invokes the real loader before querying the result.
            code = 'import sys; from pathlib import Path; sys.path.insert(0,sys.argv[1]); import resolve_ds; resolve_ds.resolve(Path(sys.argv[1]).parent,Path(sys.argv[2]),Path(sys.argv[3]),lambda name,limit:(Path(sys.argv[4])/name).read_bytes())'
            loaded=subprocess.run([sys.executable,'-B','-c',code,str(engine/'scripts'),str(runtime),str(self.root/'cache'),str(channel)],cwd=self.root,capture_output=True,text=True)
            self.assertEqual(loaded.returncode,0,loaded.stderr)

            process=subprocess.run([sys.executable,'-B',str(runtime/'scripts/consumer_graph.py'),'--component','BUTTON-001'],cwd=self.root,capture_output=True,text=True)
            self.assertEqual(process.returncode,0,process.stderr+process.stdout)
            self.assertEqual(json.loads(process.stdout)['status'],'PASS')

if __name__=='__main__':unittest.main()
