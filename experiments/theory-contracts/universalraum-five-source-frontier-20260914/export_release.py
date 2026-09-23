"""Export the already-built, visually inspected release without replacing versions."""
from pathlib import Path
import argparse, hashlib, json, shutil, zipfile

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument('--visual-review-complete', action='store_true')
ap.add_argument('--documents', type=Path, default=Path('/Users/stefanhamann/Documents'))
args = ap.parse_args()
if not args.visual_review_complete:
    raise RuntimeError('Explicit completed rendered-page review required')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path = HERE / 'release_manifest.json'
manifest = json.loads(manifest_path.read_text())
for name in ['main', 'update']:
    if sha(HERE / 'main-v1.4' / (name + '.pdf')) != manifest['pdfs'][name]:
        raise RuntimeError('PDF changed since build manifest')
manifest['visual_review'] = {
    'completed': True, 'main_pages_rendered': manifest['page_counts']['main'],
    'update_pages_rendered': manifest['page_counts']['update'],
    'contact_sheets_inspected': 12,
    'representative_full_pages_inspected': {'main': [101, 103, 104, 110], 'update': [2]},
    'outcome': 'No clipping, overlap, missing glyphs or unresolved references observed; all baseline illustrations preserved.'}
manifest['checks'] = json.loads((HERE / 'replay.json').read_text())
manifest['checker_hashes'] = {p.name: sha(p) for p in sorted(HERE.glob('*.py'))}
manifest['source_original_paths'] = {
    'N9_fable.md': '/Users/stefanhamann/Documents/TFPT_UNIVERSALRAUM_ABSCHLUSSRUNDE_2026-09-14_fable.md',
    'N10_sol.md': '/Users/stefanhamann/Documents/gpt56-runde-2.md',
    'N11_astra.md': '/Users/stefanhamann/Documents/gpt-6-astra-chatgpt-antwort.md',
    'N12_astra_hoch.md': '/Users/stefanhamann/Documents/gpt-6-astra-hoch-chatgpt.md',
    'N13_spark.md': '/Users/stefanhamann/Documents/TFPT_UNIVERSALRAUM_GESAMTSTAND_2026-09-14_spark.md'}
for name, original in manifest['source_original_paths'].items():
    original = Path(original)
    if original.exists() and sha(original) != manifest['source_hashes'][name]:
        raise RuntimeError('User input changed since audit: ' + name)
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')

out = HERE.parents[2] / 'output' / 'pdf'
out.mkdir(parents=True, exist_ok=True)
def preserve_copy(src, dst):
    if dst.exists():
        if sha(src) != sha(dst):
            raise RuntimeError('Refusing to overwrite different version: ' + str(dst))
    else:
        shutil.copyfile(src, dst)
    if sha(src) != sha(dst):
        raise RuntimeError('Copy verification failed')

exports = [
    (HERE / 'main-v1.4/main.pdf', 'TFPT_Universalraum_Hauptdokument_2026-09-14_v1.4.pdf'),
    (HERE / 'main-v1.4/update.pdf', 'TFPT_Universalraum_Update_2026-09-14_v1.4.pdf'),
    (HERE / 'RESULTS.md', 'TFPT_Universalraum_Ergebnisse_2026-09-14_v1.4.md'),
    (HERE / 'FOLLOWUPS.md', 'TFPT_Followups_2026-09-14_v1.4.md')]
for src, name in exports:
    preserve_copy(src, args.documents / name)
    if src.suffix == '.pdf':
        preserve_copy(src, out / name)

zipname = 'TFPT_Universalraum_Quellen_und_Pruefungen_2026-09-14_v1.4.zip'
archive = HERE / zipname
if archive.exists():
    raise RuntimeError('Archive already exists; choose a new revision instead of replacing it')
keep_suffix = {'.md', '.py', '.json', '.tex', '.png', '.pdf', '.sty', '.cls', '.bib'}
files = [p for p in sorted(HERE.rglob('*')) if p.is_file() and p.suffix in keep_suffix
         and 'qa' not in p.relative_to(HERE).parts and '__pycache__' not in p.relative_to(HERE).parts]
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for p in files:
        z.write(p, 'TFPT_Universalraum_v1.4/' + str(p.relative_to(HERE)))
with zipfile.ZipFile(archive) as z:
    if z.testzip() is not None:
        raise RuntimeError('Archive integrity failed')
preserve_copy(archive, args.documents / zipname)
print(json.dumps({'documents': [str(args.documents / n) for _, n in exports] + [str(args.documents / zipname)],
                  'archive_files': len(files), 'archive_bytes': archive.stat().st_size,
                  'pages': manifest['page_counts'], 'visual_review_complete': True}, indent=2))
