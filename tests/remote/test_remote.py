import importlib.util
import io
import json
from pathlib import Path
import tarfile
import tempfile
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('loader', ROOT/'skills/contpaqi-figma-screens/scripts/resolve_ds.py')
loader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(loader)

class RemoteTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.engine = self.root/'engine'
        (self.engine/'assets').mkdir(parents=True)
        (self.engine/'assets/engine.json').write_bytes(loader.encoded({'version':'0.3.0','engine_protocol':1,'skill_name':'contpaqi-figma-screens','companion_skill':'contpaqi-po-prototypes','repository':'Migueluckleo/Evolution-Lab','branch':'main'}))
        (self.engine/'skill.md').write_text('installed engine')
        self.cache = self.root/'cache'
        self.calls = []
        self.publish({'specs/button.md': b'first version'})

    def publish(self, files, unsafe=None):
        hashes = {p:loader.sha(b) for p,b in files.items()}
        self.manifest = {'schema_version':1,'package_version':'0.0.0+test','ds_digest':loader.sha(loader.canonical(hashes)),'files':hashes,'components':[]}
        data = loader.encoded(self.manifest)
        identity = loader.sha(data)
        stream = io.BytesIO()
        with tarfile.open(fileobj=stream, mode='w:gz') as archive:
            for name, value in files.items():
                item = tarfile.TarInfo(name); item.size = len(value)
                archive.addfile(item,io.BytesIO(value))
            if unsafe:
                item = tarfile.TarInfo(unsafe);item.type = tarfile.SYMTYPE;item.linkname = '/etc/passwd';archive.addfile(item)
        bundle = stream.getvalue()
        self.pointer = {'schema_version':1,'engine_protocol':1,'manifest':f'catalog/releases/{identity}/manifest.json','manifest_sha256':identity,'bundle':f'catalog/releases/{identity}/data.tar.gz','bundle_sha256':loader.sha(bundle),'bundle_bytes':len(bundle),'ds_digest':self.manifest['ds_digest']}
        self.objects = {'catalog/current.json':loader.encoded(self.pointer), self.pointer['manifest']:data,self.pointer['bundle']:bundle}

    def fetch(self, name, limit):
        self.calls.append(name)
        return self.objects[name]

    def resolve(self, name='run', transport=None):
        return loader.resolve(self.engine,self.root/name,self.cache,transport or self.fetch)

    def test_same_engine_reads_new_release_and_preserves_existing_run(self):
        a = self.resolve('a')
        self.publish({'specs/button.md':b'second version','specs/new-component.md':b'new'})
        b = self.resolve('b')
        self.assertNotEqual(a['ds_digest'],b['ds_digest'])
        self.assertEqual((self.root/'a/assets/design-system/specs/button.md').read_bytes(),b'first version')
        self.assertEqual((self.root/'b/assets/design-system/specs/button.md').read_bytes(),b'second version')
        self.assertEqual((self.engine/'skill.md').read_text(),'installed engine')
        self.assertFalse((self.engine/'assets/design-system').exists())

    def test_cache_still_checks_current_pointer(self):
        self.resolve('a'); self.calls.clear(); self.resolve('b')
        self.assertEqual(self.calls,['catalog/current.json'])

    def test_offline_blocks_even_with_valid_cache(self):
        self.resolve('a')
        def offline(*args): raise OSError('offline')
        with self.assertRaises(OSError): self.resolve('b',offline)
        self.assertFalse((self.root/'b').exists())

    def test_modified_download_rejected(self):
        self.objects[self.pointer['bundle']] += b'bad'
        with self.assertRaisesRegex(ValueError,'integrity'): self.resolve()
        self.assertFalse((self.root/'run').exists())

    def test_corrupt_cache_refetched(self):
        self.resolve('a'); (self.cache/self.pointer['bundle_sha256']).write_bytes(b'broken');self.calls.clear()
        self.resolve('b');self.assertIn(self.pointer['bundle'],self.calls)

    def test_traversal_and_symlink_rejected(self):
        self.publish({'../outside':b'bad'})
        with self.assertRaises(ValueError): self.resolve()
        self.publish({'specs/safe.md':b'good'},unsafe='specs/link')
        with self.assertRaises(ValueError): self.resolve('second')
        self.assertFalse((self.root/'outside').exists())

    def test_incompatible_protocol_rejected(self):
        self.pointer['engine_protocol'] = 2;self.objects['catalog/current.json'] = loader.encoded(self.pointer)
        with self.assertRaisesRegex(ValueError,'unsupported'): self.resolve()

    def test_external_catalog_paths_rejected(self):
        self.pointer['bundle'] = 'https://elsewhere.test/file';self.objects['catalog/current.json'] = loader.encoded(self.pointer)
        with self.assertRaises(ValueError): self.resolve()

    def test_existing_output_preserved(self):
        self.resolve()
        with self.assertRaises(ValueError): self.resolve()
        self.assertTrue((self.root/'run/skill.md').is_file())

    def test_non_object_catalog_is_structured_error(self):
        for value in [[], None, 'bad']:
            self.objects['catalog/current.json'] = loader.encoded(value)
            with self.assertRaisesRegex(ValueError, 'JSON object'): self.resolve()

    def test_yaml_bridge_parses_current_contract_metadata(self):
        rows = [{'path':'contract.md','text':'contract_id: BUTTON-001\nstatus: DELEGATED_FOR_BUILD\ndate: 2026-10-16\n'}]
        result = subprocess.run(['ruby',str(ROOT/'scripts/ds_yaml.rb')],input=json.dumps(rows),capture_output=True,text=True,check=True)
        parsed = json.loads(result.stdout)[0]
        self.assertEqual(parsed['errors'],[])
        self.assertEqual(parsed['value']['contract_id'],'BUTTON-001')
        self.assertEqual(parsed['value']['date'],'2026-10-16')

    def test_both_engines_share_loader_bytes(self):
        self.assertEqual((ROOT/'skills/contpaqi-figma-screens/scripts/resolve_ds.py').read_bytes(),(ROOT/'skills/contpaqi-po-prototypes/scripts/resolve_ds.py').read_bytes())

if __name__ == '__main__': unittest.main()
