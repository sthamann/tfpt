"""Versioned research delivery, including a fresh replay of the packed snapshot."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile

HERE = Path(__file__).resolve().parent
OUT = HERE / 'deliverables'
DEST = Path('/Users/stefanhamann/Documents')
BASE = 'TFPT_Universalraum_Zwei_Banken_'
VERSION = '_2026-09-15_v1.6.5'
ROOT = 'TFPT_Zwei_Banken_v1.6.5'
OUT.mkdir(exist_ok=True)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


status = {'status': 'RUNNING', 'scope': 'Markdown research continuation plus reproducible package; no full-main-PDF update',
          'delivered': []}


def save():
    (HERE / 'delivery_manifest.json').write_text(json.dumps(status, indent=2) + '\n')


def main():
    save()
    replay = json.loads((HERE / 'replay_manifest.json').read_text())
    if replay['status'] != 'PASS' or len(replay['reports']) != 5:
        raise RuntimeError('Current complete replay missing')
    if sum(r['checks'] for r in replay['reports'].values()) != 6490:
        raise RuntimeError('Documented check count stale')
    for label, record in replay['reports'].items():
        for variant in ('normal', 'optimized'):
            if digest(HERE / (label+'_'+variant+'.json')) != record['sha256']:
                raise RuntimeError('Changed result: ' + label)
    full = (HERE / 'RESULTS.md').read_text() + '\n\n---\n\n' + (HERE / 'LATE_AUDIT.md').read_text()
    full += '\n\n---\n\n# Historischer Beweisanhang: vollständiger nativer Herleitungsstand v1.6.4\n\n'
    full += ('Dieser Anhang bewahrt die frühere Herleitung vollständig. Seine damaligen '
             'Statussätze werden durch die aktuelle Konsolidierung und den Nachtrag oben '
             'ergänzt; er ist kein ungeprüft übernommener neuer Gesamtstatus. '
             'Die externe laufende Symmetrieergänzung wurde separat geprüft und ist '
             'nicht unbemerkt in diesen eingefrorenen Anhang eingegangen.\n\n')
    full += (HERE / 'sources/native_RESULTS.md').read_text()
    documents = {
        BASE+'Konsolidierung'+VERSION+'.md': full,
        BASE+'Update'+VERSION+'.md': (HERE / 'UPDATE.md').read_text(),
        BASE+'Einfach'+VERSION+'.md': (HERE / 'EINFACH.md').read_text(),
    }
    for name, body in documents.items():
        if '“+zu' in body:
            raise RuntimeError('Formatting artifact remains')
        (OUT / name).write_text(body)
    archive = OUT / (BASE+'Pruefpaket'+VERSION+'.zip')
    members = []
    for path in sorted(HERE.rglob('*')):
        if not path.is_file() or '__pycache__' in path.parts or path.suffix == '.pyc':
            continue
        if path == archive or path.name == 'delivery_manifest.json':
            continue
        if OUT in path.parents and path.name not in documents:
            continue
        members.append(path)
    package_files = {str(p.relative_to(HERE)): digest(p) for p in members}
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for path in members:
            zf.write(path, ROOT+'/'+str(path.relative_to(HERE)))
        zf.writestr(ROOT+'/PACKAGE_FILES.json', json.dumps(package_files, indent=2)+'\n')
    with zipfile.ZipFile(archive) as zf:
        if zf.testzip() is not None:
            raise RuntimeError('Archive checksum failure')
        for name, sha in package_files.items():
            if sha256(zf.read(ROOT+'/'+name)).hexdigest() != sha:
                raise RuntimeError('Archive content mismatch: '+name)
        # The temporary directory is created and owned by this process.
        with tempfile.TemporaryDirectory(prefix='tfpt-two-bank-package-') as temp:
            zf.extractall(temp)
            unpacked = Path(temp)/ROOT
            proc = subprocess.run([sys.executable, '-B', 'replay.py', '--frozen-only'],
                                  cwd=unpacked, text=True, capture_output=True)
            if proc.returncode:
                raise RuntimeError('Packed replay failed: '+proc.stderr[-3000:])
            packed = json.loads((unpacked/'replay_manifest.json').read_text())
            if packed['status'] != 'PASS':
                raise RuntimeError('Packed replay not PASS')
            for label in replay['reports']:
                if packed['reports'][label]['sha256'] != replay['reports'][label]['sha256']:
                    raise RuntimeError('Packed replay changed result: '+label)
            status['packed_replay'] = {'status': 'PASS', 'all_five_results_byte_identical': True,
                                       'checks_per_variant': 6490}
    # Refuse to replace a different user-owned file under an existing version.
    for path in [OUT/name for name in documents]+[archive]:
        target = DEST/path.name
        if target.exists() and digest(target) != digest(path):
            raise RuntimeError('Existing version differs; not overwriting '+str(target))
    for path in [OUT/name for name in documents]+[archive]:
        target = DEST/path.name
        if not target.exists():
            shutil.copy2(path, target)
        if digest(path) != digest(target):
            raise RuntimeError('Delivery bytes differ: '+str(target))
        status['delivered'].append({'path': str(target), 'sha256': digest(target),
                                    'bytes': target.stat().st_size})
    status['source_state'] = replay['validation_scope']
    status['live_originals_unchanged'] = replay['originals_unchanged']
    status['status'] = 'PASS'
    save()
    print(json.dumps(status, indent=2))


if __name__ == '__main__':
    try:
        main()
    except BaseException as error:
        status['status'] = 'FAIL'
        status['error'] = repr(error)
        save()
        raise
