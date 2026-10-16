#!/usr/bin/env python3
"""Resolve a verified GitHub data release into a new execution folder. Stdlib only."""
from __future__ import annotations
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import tarfile
import tempfile
import urllib.request

BASE = 'https://raw.githubusercontent.com/Migueluckleo/Evolution-Lab/main/'
HEX = re.compile(r'[a-f0-9]{64}\Z')
MAX_JSON = 16 * 1024 * 1024
MAX_BUNDLE = 100 * 1024 * 1024
MAX_EXPANDED = 512 * 1024 * 1024

def sha(data):
    return hashlib.sha256(data).hexdigest()

def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()

def unique_json(data):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('Duplicate JSON key')
            result[key] = value
        return result
    value = json.loads(data, object_pairs_hook=pairs)
    if not isinstance(value, dict):
        raise ValueError('Expected a JSON object')
    return value

def relative(name):
    if not isinstance(name, str) or not name or '\\' in name or '\x00' in name:
        raise ValueError('Invalid data path')
    p = PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or str(p) != name or ':' in name:
        raise ValueError('Unsafe data path')
    return name

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('Unexpected redirect; official origin required')

def fetch(name, limit):
    relative(name)
    req = urllib.request.Request(BASE + name, headers={'User-Agent': 'Evolution-Lab-Skill/1', 'Cache-Control': 'no-cache'})
    with urllib.request.build_opener(NoRedirect).open(req, timeout=45) as response:
        data = response.read(limit + 1)
    if len(data) > limit:
        raise ValueError('Remote object exceeds size limit')
    return data

def checked(name, expected, limit, cache, transport):
    if not isinstance(expected, str) or not HEX.fullmatch(expected):
        raise ValueError('Invalid content hash')
    target = cache / expected
    if target.is_symlink():
        raise ValueError('Cache symlink rejected')
    if target.is_file() and target.stat().st_size <= limit:
        data = target.read_bytes()
        if sha(data) == expected:
            return data
    data = transport(name, limit)
    if len(data) > limit or sha(data) != expected:
        raise ValueError('Remote integrity failure: ' + name)
    with tempfile.NamedTemporaryFile(dir=cache, delete=False) as temp:
        temp.write(data)
        tmp = Path(temp.name)
    tmp.replace(target)
    return data

def extract(bundle, manifest, target):
    files = manifest['files']
    if not isinstance(files, dict) or not files or len(files) > 20000:
        raise ValueError('Invalid file manifest')
    for name, expected in files.items():
        relative(name)
        if not isinstance(expected, str) or not HEX.fullmatch(expected):
            raise ValueError('Invalid file hash')
    if sha(canonical(files)) != manifest['ds_digest']:
        raise ValueError('DS digest mismatch')
    seen = set()
    total = 0
    with tarfile.open(fileobj=io.BytesIO(bundle), mode='r:gz') as archive:
        for member in archive:
            name = relative(member.name)
            total += member.size
            if not member.isfile() or name in seen or name not in files or total > MAX_EXPANDED:
                raise ValueError('Unsafe or unexpected archive member')
            data = archive.extractfile(member).read()
            if sha(data) != files[name]:
                raise ValueError('File hash mismatch: ' + name)
            dest = target / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            seen.add(name)
    if seen != set(files):
        raise ValueError('Incomplete data bundle')

def resolve(engine, output, cache, transport=fetch):
    engine = Path(engine).resolve()
    output = Path(output).absolute()
    if output.exists() or output.is_symlink() or output.resolve().is_relative_to(engine):
        raise ValueError('Execution folder must be new and outside the installed skill')
    info = unique_json((engine / 'assets/engine.json').read_bytes())
    if info.get('engine_protocol') != 1 or info.get('repository') != 'Migueluckleo/Evolution-Lab' or info.get('branch') != 'main':
        raise ValueError('Unsupported engine configuration')
    # Always perform a fresh pointer request. An offline cache is never freshness evidence.
    pointer_bytes = transport('catalog/current.json', MAX_JSON)
    if len(pointer_bytes) > MAX_JSON:
        raise ValueError('Catalog too large')
    pointer = unique_json(pointer_bytes)
    if pointer.get('schema_version') != 1 or pointer.get('engine_protocol') != 1:
        raise ValueError('Catalog requires an unsupported engine; update skill')
    identity = pointer.get('manifest_sha256', '')
    if not isinstance(identity, str) or not HEX.fullmatch(identity):
        raise ValueError('Invalid catalog identity')
    if pointer.get('manifest') != f'catalog/releases/{identity}/manifest.json' or pointer.get('bundle') != f'catalog/releases/{identity}/data.tar.gz':
        raise ValueError('Unexpected catalog paths')
    cache = Path(cache).absolute()
    if cache.is_symlink():
        raise ValueError('Cache must not be a symlink')
    cache = cache.resolve()
    cache.mkdir(parents=True, exist_ok=True)
    data = checked(pointer['manifest'], identity, MAX_JSON, cache, transport)
    manifest = unique_json(data)
    if manifest.get('schema_version') != 1 or manifest.get('ds_digest') != pointer.get('ds_digest') or not isinstance(manifest.get('components'), list):
        raise ValueError('Unsupported or inconsistent manifest')
    bundle = checked(pointer['bundle'], pointer['bundle_sha256'], MAX_BUNDLE, cache, transport)
    if len(bundle) != pointer.get('bundle_bytes'):
        raise ValueError('Bundle length mismatch')
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.evolution-', dir=output.parent))
    try:
        # Copy trusted installed tools; remote data never replaces engine instructions or scripts.
        for src in engine.rglob('*'):
            rel = src.relative_to(engine)
            if src.is_symlink():
                raise ValueError('Engine symlink rejected')
            if src.is_file() and '__pycache__' not in rel.parts and src.name != '.ds-managed-install.json':
                dst = staging / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)
        snapshot = staging / 'assets/design-system'
        extract(bundle, manifest, snapshot)
        (staging / 'assets/snapshot-manifest.json').write_bytes(data)
        (staging / 'references').mkdir(exist_ok=True)
        (staging / 'references/components.json').write_bytes(encoded(manifest['components']))
        release = {**info, 'version': manifest['package_version'], 'engine_version': info['version'],
                   'ds_digest': manifest['ds_digest'], 'manifest_sha256': identity,
                   'catalog_url': BASE + 'catalog/current.json'}
        (staging / 'assets/release.json').write_bytes(encoded(release))
        (staging / 'assets/remote-receipt.json').write_bytes(encoded(pointer))
        if output.exists():
            raise ValueError('Execution folder appeared during download')
        staging.rename(output)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return {'status': 'PASS', 'runtime': str(output), 'engine_version': info['version'],
            'ds_version': manifest['package_version'], 'ds_digest': manifest['ds_digest'],
            'manifest_sha256': identity, 'files': len(manifest['files'])}

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', required=True, type=Path)
    p.add_argument('--cache', type=Path)
    args = p.parse_args()
    try:
        result = resolve(Path(__file__).resolve().parents[1], args.output,
                         args.cache or args.output.absolute().parent / '.evolution-cache')
    except (OSError, ValueError, KeyError, TypeError, tarfile.TarError) as error:
        print(json.dumps({'status': 'BLOCKED', 'error': str(error), 'offline_fallback': False}, ensure_ascii=False))
        raise SystemExit(1)
    print(json.dumps(result, ensure_ascii=False))
