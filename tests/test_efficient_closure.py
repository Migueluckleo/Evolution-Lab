import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import ds_core as core
import ds_graph as graph
import ds_incremental as inc
from ds_session import Session, cached, writer_lock


class CoordinationTests(unittest.TestCase):
    def child(self, root, body):
        code = f'import sys; sys.path.insert(0,{str(SCRIPTS)!r})\nfrom ds_session import writer_lock, Busy\n' + body
        return subprocess.run([sys.executable, '-B', '-c', code], capture_output=True, text=True, timeout=15)

    def test_second_process_blocked_and_kernel_releases_after_crash(self):
        with tempfile.TemporaryDirectory() as tmp:
            with writer_lock(tmp, 'first'):
                result = self.child(tmp, f'try:\n with writer_lock({tmp!r}, "second"): raise AssertionError("entered")\nexcept Busy: pass\n')
                self.assertEqual(result.returncode, 0, result.stderr)
            result = self.child(tmp, f'import os\nwith writer_lock({tmp!r}, "crash"): os._exit(0)\n')
            self.assertEqual(result.returncode, 0, result.stderr)
            with writer_lock(tmp, 'recovered'):
                with writer_lock(tmp, 'nested'):
                    pass
            self.assertTrue((Path(tmp) / 'output/closures/contention.jsonl').is_file())

    def test_same_source_plan_shared_without_second_backup(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); live = root / 'graphify-out'; run = live / 'runs/first'
            (run / 'before').mkdir(parents=True)
            (live / 'graph.json').write_text('{}')
            (run / 'before/graph.json').write_text('{}')
            delta = {'source_sha256': {'a.md': 'abc'}, 'config_sha256': 'cfg',
                     'new': ['a.md'], 'changed': [], 'deleted_or_excluded': [], 'semantic_required': ['a.md']}
            core.dump(run / 'source-plan.json', delta)
            core.dump(run / 'semantic-plan.json', {'chunks': [['a.md']]})
            core.dump(live / 'ds-prepared.json', {'run': 'first'})
            with patch.object(graph, 'ROOT', root), patch.object(graph, 'LIVE', live), patch.object(graph, 'plan', return_value=(delta, {})):
                result = graph.prepare({}, 'second')
            self.assertEqual(result['status'], 'PREPARED_SHARED')
            self.assertEqual(result['run'], 'first')
            self.assertFalse((live / 'runs/second').exists())


class ReuseTests(unittest.TestCase):
    def test_cache_invalidates_changes_and_detects_new_sources_at_final_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); p = root / 'source.txt'; p.write_text('old')
            calls = []
            @cached
            def inspect():
                calls.append(1)
                return {'text': p.read_text()}
            with Session(root) as session:
                inspect()['text'] = 'corrupt caller copy'
                self.assertEqual(inspect()['text'], 'old')
                self.assertEqual(len(calls), 1)
                stamp = p.stat().st_mtime_ns
                p.write_text('new'); os.utime(p, ns=(stamp, stamp))
                self.assertEqual(inspect()['text'], 'new')
                self.assertEqual(len(calls), 2)
                with self.assertRaisesRegex(ValueError, 'Fuentes cambiaron'):
                    session.verify()
            with Session(root) as session:
                (root / 'added.md').write_text('new document')
                with self.assertRaises(ValueError): session.verify()

    def test_yaml_only_parses_changed_documents_and_returns_copies(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ('a.md', 'b.md'): (root / name).write_text('---\nx: 1\n---')
            calls = []
            def parse(paths, base):
                calls.append(paths)
                return {p: {'value': {'x': 1}, 'errors': []} for p in paths}
            with Session(root), patch.object(core, '_yaml_documents_uncached', side_effect=parse):
                core.yaml_documents(['a.md', 'b.md'], root)['a.md']['value']['x'] = 99
                self.assertEqual(core.yaml_documents(['a.md'], root)['a.md']['value']['x'], 1)
                (root / 'b.md').write_text('---\nx: 2\n---')
                core.yaml_documents(['a.md', 'b.md'], root)
            self.assertEqual(calls, [['a.md', 'b.md'], ['b.md']])

    def test_yaml_reuses_across_sessions_and_rejects_corrupt_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'a.md').write_text('---\nx: 1\n---')
            result = {'a.md': {'value': {'x': 1}, 'errors': []}}
            with Session(root), patch.object(core, '_yaml_documents_uncached', return_value=result) as parse:
                core.yaml_documents(['a.md'], root)
                self.assertEqual(parse.call_count, 1)
            with Session(root) as session, patch.object(core, '_yaml_documents_uncached') as parse:
                self.assertEqual(core.yaml_documents(['a.md'], root), result)
                parse.assert_not_called()
                self.assertEqual(session.counts['yaml_files']['persisted_reused'], 1)
            cache = root / 'output/closures/yaml-cache.json'
            bad = json.loads(cache.read_text())
            bad['rows']['a.md']['result']['value']['x'] = 99
            cache.write_text(json.dumps(bad))
            with Session(root), patch.object(core, '_yaml_documents_uncached', return_value=result) as parse:
                self.assertEqual(core.yaml_documents(['a.md'], root), result)
                self.assertEqual(parse.call_count, 1)
            (root / 'a.md').write_text('---\nx: 2\n---')
            with Session(root), patch.object(core, '_yaml_documents_uncached', return_value=result) as parse:
                core.yaml_documents(['a.md'], root)
                self.assertEqual(parse.call_count, 1)


class IncrementalTests(unittest.TestCase):
    def fixture(self, root, deleted=False):
        old = root / 'graphify-out/runs/old'; run = root / 'graphify-out/runs/new'
        (run / 'before').mkdir(parents=True); old.mkdir(parents=True)
        for p in ('scripts/ds_graph_engine.py', 'scripts/ds_incremental.py', 'config/ds-project.json'):
            (root / p).parent.mkdir(exist_ok=True); (root / p).write_text('{}')
        for name in ('a.py', 'b.py', 'c.py'): (root / name).write_text('pass')
        nodes = [{'id': n, 'source_file': n + '.py', 'label': n, 'file_type': 'code'} for n in 'abc']
        edges = [{'source': 'b', 'target': 'a', 'source_file': 'b.py', 'relation': 'calls'}]
        core.dump(run / 'before/graph.json', {'nodes': nodes, 'links': edges})
        core.dump(old / 'ast.json', {'nodes': nodes, 'edges': edges})
        core.dump(old / 'structural-supplement.json', {'nodes': [], 'edges': []})
        core.dump(old / 'source-plan.json', {})
        core.dump(run / 'before/ds-closure.json', {'run': 'old', 'extraction_tool_sha256': inc.tool_digest(root),
                  'extraction_sha256': {p: inc.sha(old / p) for p in ['ast.json', 'structural-supplement.json', 'source-plan.json']}})
        paths = ['b.py', 'c.py'] if deleted else ['a.py', 'b.py', 'c.py']
        core.dump(run / 'detection.json', {'files': {'code': [str(root / p) for p in paths]}})
        core.dump(run / 'source-plan.json', {'new': [], 'changed': [] if deleted else ['a.py'],
                  'deleted_or_excluded': ['a.py'] if deleted else []})
        return run, old

    def test_external_endpoint_survives_with_unchanged_importer(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); run, old = self.fixture(root)
            data = core.read_json(old / 'ast.json')
            data['nodes'].append({'id': 'test', 'source_file': '@playwright/test', 'file_type': 'code'})
            data['edges'].append({'source': 'c', 'target': 'test', 'source_file': 'c.py', 'relation': 'dynamic_import'})
            core.dump(old / 'ast.json', data)
            proof = core.read_json(run / 'before/ds-closure.json')
            proof['extraction_sha256']['ast.json'] = inc.sha(old / 'ast.json')
            core.dump(run / 'before/ds-closure.json', proof)
            def extract(paths, **kwargs):
                return {'nodes': [{'id': p.stem, 'source_file': str(p)} for p in paths],
                        'edges': [], 'extracted_sources': list(map(str, paths)), 'failed_sources': []}
            result = inc.extract_ast(root, run, extract, lambda p: False)
            ids = {n['id'] for n in result['nodes']}
            self.assertIn('test', ids)
            self.assertTrue(all(e['source'] in ids and e['target'] in ids for e in result['edges']))

    def test_changed_callee_reextracts_callers_and_reuses_independent_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); run, old = self.fixture(root)
            observed = []
            def extract(paths, **kwargs):
                observed.extend(p.name for p in paths)
                self.assertEqual([n['id'] for n in kwargs['resolution_context_nodes']], ['c'])
                return {'nodes': [{'id': p.stem + '2', 'source_file': str(p)} for p in paths],
                        'edges': [], 'extracted_sources': list(map(str, paths)), 'failed_sources': []}
            result = inc.extract_ast(root, run, extract, lambda p: False)
            self.assertEqual(observed, ['a.py', 'b.py'])
            self.assertEqual({n['id'] for n in result['nodes']}, {'a2', 'b2', 'c'})
            self.assertEqual(result['incremental']['reused_files'], 1)
            self.assertEqual(result['edges'], [])

    def test_deleted_source_drops_old_evidence_and_invalid_cache_falls_back(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); run, old = self.fixture(root, deleted=True)
            calls = []
            def extract(paths, **kwargs):
                calls.append([p.name for p in paths])
                return {'nodes': [{'id': p.stem, 'source_file': str(p)} for p in paths],
                        'edges': [], 'extracted_sources': list(map(str, paths))}
            result = inc.extract_ast(root, run, extract, lambda p: False)
            self.assertEqual(calls, [['b.py']])
            self.assertNotIn('a', {n['id'] for n in result['nodes']})
            (old / 'ast.json').write_text('{}')
            result = inc.extract_ast(root, run, extract, lambda p: False)
            self.assertEqual(calls[-1], ['b.py', 'c.py'])
            self.assertEqual(result['incremental']['mode'], 'FULL_SAFE_FALLBACK')

    def test_failed_extraction_cannot_be_stamped_current(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); run, _ = self.fixture(root)
            with self.assertRaisesRegex(ValueError, 'incomplete'):
                inc.extract_ast(root, run, lambda *a, **k: {'failed_sources': ['a.py']}, lambda p: False)


if __name__ == '__main__':
    unittest.main()
