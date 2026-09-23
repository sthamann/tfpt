"""Build and validate versioned Markdown research delivery without replacing old files."""
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile

HERE = Path(__file__).resolve().parent
OUT = HERE/'deliverables'
DEST = Path('/Users/stefanhamann/Documents')
PREFIX = 'TFPT_Universalraum_Clock_Gemeinsame_Quelle_'
VERSION = '_2026-09-15_v1.6.6'
ARCHIVE_ROOT = 'TFPT_Clock_Gemeinsame_Quelle_v1.6.6'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    replay = json.loads((HERE/'replay_manifest.json').read_text())
    if replay['status'] != 'PASS' or replay['checks_per_variant'] != 2205 or len(replay['reports']) != 8:
        raise RuntimeError('Complete current replay absent')
    for label, report in replay['reports'].items():
        for variant in ('normal','optimized'):
            if digest(HERE/'replay_outputs'/f'{label}_{variant}.json') != report['sha256']:
                raise RuntimeError('Replay output changed: '+label)
    OUT.mkdir(exist_ok=True)
    full = (HERE/'RESULTS.md').read_text()
    for title, path in [
        ('Anhang A: Quellenprüfung Symmetrie und Verfügbarkeit','agents/symmetry_audit/AUDIT.md'),
        ('Anhang B: unabhängige Krylov- und Feldprüfung','agents/ground_field_audit/REPORT.md'),
        ('Anhang C: minimaler Transfer und seine Quellen-Grenze','agents/minimal_origin/RESULTS.md'),
        ('Anhang D: vollständiger Überlappungs-Audit','agents/overlap_audit/AUDIT.md'),
        ('Anhang E: arithmetischer Schleifenvorschlag','RH_LOOP_AUDIT.md'),
    ]:
        full += '\n\n---\n\n# '+title+'\n\n'+(HERE/path).read_text()
    full += '\n\n---\n\n# Historischer vollständiger Herleitungsstand v1.6.5 einschließlich v1.6.4\n\n'
    full += ('Der folgende Text wird unverändert bewahrt. Neue Gesamtstatusaussagen und '
             'Reichweitenkorrekturen stehen in der vorangestellten Revision v1.6.6. '
             'Historische Arbeitsaufträge oder Verfügbarkeitsannahmen werden dadurch '
             'nicht erneut zu aktuellen Beweisen erklärt.\n\n')
    full += (HERE/'sources/historical_v1.6.5.md').read_text()
    docs = {PREFIX+'Konsolidierung'+VERSION+'.md':full,
            PREFIX+'Update'+VERSION+'.md':(HERE/'UPDATE.md').read_text(),
            PREFIX+'Einfach'+VERSION+'.md':(HERE/'EINFACH.md').read_text()}
    for name, body in docs.items():
        if body.count('```') % 2:
            raise RuntimeError('Unbalanced code fence: '+name)
        (OUT/name).write_text(body)
    # Keep full historical derivation, not only a shorter replacement summary.
    if (HERE/'sources/historical_v1.6.5.md').read_text() not in full:
        raise RuntimeError('Historical derivation lost')
    archive = OUT/(PREFIX+'Pruefpaket'+VERSION+'.zip')
    members = []
    for path in sorted(HERE.rglob('*')):
        if not path.is_file() or '__pycache__' in path.parts or path.suffix == '.pyc':
            continue
        if path.name in ('contracted_krylov','delivery_manifest.json') or path == archive:
            continue
        if OUT in path.parents and path.name not in docs:
            continue
        members.append(path)
    hashes = {str(path.relative_to(HERE)):digest(path) for path in members}
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for path in members:
            z.write(path,ARCHIVE_ROOT+'/'+str(path.relative_to(HERE)))
        z.writestr(ARCHIVE_ROOT+'/PACKAGE_FILES.json',json.dumps(hashes,indent=2)+'\n')
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:
            raise RuntimeError('Archive checksum failure')
        for name, sha in hashes.items():
            if sha256(z.read(ARCHIVE_ROOT+'/'+name)).hexdigest() != sha:
                raise RuntimeError('Archive member mismatch: '+name)
        with tempfile.TemporaryDirectory(prefix='tfpt-clock-package-') as temp:
            z.extractall(temp)
            extracted = Path(temp)/ARCHIVE_ROOT
            proc = subprocess.run([sys.executable,'-B','replay.py'],cwd=extracted,
                                  capture_output=True,timeout=300)
            if proc.returncode:
                raise RuntimeError('Fresh packed replay failed: '+proc.stderr.decode()[-4000:])
            check = json.loads((extracted/'replay_manifest.json').read_text())
            if check != replay:
                raise RuntimeError('Fresh packed replay does not match original replay')
    live = []
    for name in ('sources_manifest.json','late_sources_manifest.json'):
        for relative, record in json.loads((HERE/name).read_text()).items():
            source = Path(record['source'])
            live.append({'source':str(source),'unchanged':source.exists() and digest(source)==record['sha256']})
    delivered = []
    for path in [OUT/name for name in docs]+[archive]:
        target = DEST/path.name
        if target.exists() and digest(target) != digest(path):
            raise RuntimeError('Existing version differs; not overwriting '+str(target))
    for path in [OUT/name for name in docs]+[archive]:
        target = DEST/path.name
        if not target.exists():
            shutil.copy2(path,target)
        if digest(target) != digest(path):
            raise RuntimeError('Documents copy differs')
        delivered.append({'path':str(target),'sha256':digest(target),'bytes':target.stat().st_size})
    result = {'status':'PASS','version':'1.6.6','format':'Markdown and reproducible ZIP',
              'full_historical_v1_6_5_preserved':True,
              'fresh_extraction_all_eight_replays_identical':True,
              'checks_per_variant':2205,'sources_current_at_delivery':live,
              'PDF_updated':False,'website_updated':False,'committed_or_pushed':False,
              'delivered':delivered}
    (HERE/'delivery_manifest.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
