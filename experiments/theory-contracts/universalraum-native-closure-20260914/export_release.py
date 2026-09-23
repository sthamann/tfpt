"""Export one new paired release only after visual inspection, without overwrite."""
from pathlib import Path
import argparse,hashlib,json,shutil,zipfile

HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--visual-review-complete',action='store_true');args=p.parse_args()
if not args.visual_review_complete:raise RuntimeError('Render inspection is required before export')
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
manifest_path=HERE/'release_manifest.json';manifest=json.loads(manifest_path.read_text())
for name in ['main','update']:
    if sha(HERE/'main-v1.5'/(name+'.pdf'))!=manifest['pdfs'][name]:raise RuntimeError('PDF changed after build')
manifest['evidence_audit']=json.loads((HERE/'evidence_audit.json').read_text())
manifest['visual_review']={'completed':True,'all_pages_rendered':manifest['page_counts'],
                          'contact_sheets_inspected':'all main and update contact sheets',
                          'full_page_inspection':'new formulas, new T1-T8 table, update pages',
                          'outcome':'No clipping, missing glyphs or unresolved references observed.'}
manifest['all_scientific_source_hashes']={str(f.relative_to(HERE)):sha(f) for f in sorted(HERE.rglob('*.py'))
                                         if '__pycache__' not in f.parts}
manifest['document_source_hashes']={str(f.relative_to(HERE)):sha(f) for f in sorted((HERE/'main-v1.5').rglob('*.tex'))}
manifest['source_original_paths']={
    'N14_Fortsetzung.md':'/Users/stefanhamann/Documents/TFPT_Universalraum_Fortsetzung_2026-09-14NEU.md',
    'N15_Ergebnisse.md':'/Users/stefanhamann/Documents/TFPT_UNIVERSALRAUM_ERGEBNISSE_2026-09-14.md'}
for name,original in manifest['source_original_paths'].items():
    if sha(Path(original))!=sha(HERE/'sources'/name):raise RuntimeError('User source changed')
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')

dest=Path('/Users/stefanhamann/Documents');out=HERE.parents[2]/'output/pdf';out.mkdir(parents=True,exist_ok=True)
def preserve(src,dst):
    if dst.exists():
        if sha(src)!=sha(dst):raise RuntimeError('Refusing version overwrite: '+str(dst))
    else:shutil.copyfile(src,dst)
    if sha(src)!=sha(dst):raise RuntimeError('Copy hash mismatch')
exports=[('main-v1.5/main.pdf','TFPT_Universalraum_Hauptdokument_2026-09-14_v1.5.pdf'),
         ('main-v1.5/update.pdf','TFPT_Universalraum_Update_2026-09-14_v1.5.pdf'),
         ('RESULTS.md','TFPT_Universalraum_Ergebnisse_2026-09-14_v1.5.md'),
         ('FOLLOWUPS.md','TFPT_Followups_2026-09-14_v1.5.md')]
for source,name in exports:
    preserve(HERE/source,dest/name)
    if name.endswith('.pdf'):preserve(HERE/source,out/name)
archive=HERE/'TFPT_Universalraum_Quellen_und_Pruefungen_2026-09-14_v1.5.zip'
if archive.exists():raise RuntimeError('Archive exists; use a new version instead of overwrite')
suffixes={'.md','.py','.json','.tex','.png','.pdf','.sty','.cls','.bib','.npz'}
files=[f for f in sorted(HERE.rglob('*')) if f.is_file() and f.suffix in suffixes
       and 'qa' not in f.relative_to(HERE).parts and '__pycache__' not in f.relative_to(HERE).parts]
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for f in files:z.write(f,'TFPT_Universalraum_v1.5/'+str(f.relative_to(HERE)))
with zipfile.ZipFile(archive) as z:
    if z.testzip() is not None:raise RuntimeError('Archive integrity failure')
preserve(archive,dest/archive.name)
print(json.dumps({'pages':manifest['page_counts'],'exports':[str(dest/n) for _,n in exports]+[str(dest/archive.name)],
                  'archive_files':len(files),'archive_bytes':archive.stat().st_size},indent=2))
