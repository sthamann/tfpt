"""Record explicit visual acceptance, verify source snapshots and copy deliverables."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import sys

HERE=Path(__file__).resolve().parent
DOCUMENTS=Path('/Users/stefanhamann/Documents')
EXTERNAL=Path('/var/folders/nb/qnm6znn55875vj2nhcz5vjhc0000gn/T/tfpt-gemeinsame-quelle-audit-8xpd0zxm/work/composition/replay/report.json')


def accept():
    qa=json.loads((HERE/'PDF_QA.json').read_text())
    qa['status']='PASS'
    qa['visual_review']={
        'all_new_front_pages_and_both_short_documents_reviewed_as_raster':True,
        'key_proof_and_modular_pages_reviewed_at_full_raster_size':True,
        'historical_visual_sampling_pages':[70,120,qa['documents']['Hauptdokument']['pages']],
        'all_historical_and_new_pages_individually_visually_reviewed':False,
        'observations':'No clipped equations or text, no overlapping blocks in inspected pages. Complete prior Markdown is retained; all PDF pages passed text and page-boundary checks.'}
    (HERE/'PDF_QA.json').write_text(json.dumps(qa,indent=2)+'\n')
    external=json.loads(EXTERNAL.read_text())
    if external['status']!='PASS' or external['conditions']!=614:raise RuntimeError('external replay differs')
    external['fresh_replay_report_path']=str(EXTERNAL)
    external['fresh_replay_report_sha256']=sha256(EXTERNAL.read_bytes()).hexdigest()
    (HERE/'EXTERNAL_REPLAY.json').write_text(json.dumps(external,indent=2)+'\n')
    pins=json.loads((HERE/'frozen_sources.json').read_text())
    pins.update(json.loads((HERE/'late_aspects_normal.json').read_text())['source_hashes'])
    audit={}
    for original,record in pins.items():
        frozen=HERE/record['local']
        if sha256(frozen.read_bytes()).hexdigest()!=record['sha256']:raise RuntimeError('frozen source drift')
        src=Path(original)
        audit[original]={'frozen_sha256':record['sha256'],
                         'original_still_matches_snapshot':src.exists() and sha256(src.read_bytes()).hexdigest()==record['sha256']}
    (HERE/'SOURCE_SNAPSHOT_AUDIT.json').write_text(json.dumps(audit,indent=2)+'\n')
    print('Visual acceptance recorded; frozen sources valid; '+str(sum(not x['original_still_matches_snapshot'] for x in audit.values()))+' originals differ at delivery')


def deliver():
    if json.loads((HERE/'PDF_QA.json').read_text())['status']!='PASS':raise RuntimeError('QA not accepted')
    portable=json.loads((HERE/'PORTABLE_REPLAY.json').read_text())
    archive=HERE/'TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10.zip'
    if portable['status']!='PASS' or portable['archive_sha256']!=sha256(archive.read_bytes()).hexdigest():raise RuntimeError('portable replay missing or different archive')
    manifest=json.loads((HERE/'documents_manifest.json').read_text())
    sources=[]
    for kind in ('Hauptdokument','Update','Einfach'):
        for field in ('markdown','pdf'):
            source=HERE/manifest[kind][field]
            expected=manifest[kind]['md_sha256' if field=='markdown' else 'pdf_sha256']
            if sha256(source.read_bytes()).hexdigest()!=expected:raise RuntimeError('changed document')
            sources.append(source)
    sources.append(HERE/'TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10.zip')
    for source in sources:
        target=DOCUMENTS/source.name
        if target.exists() and target.read_bytes()!=source.read_bytes():raise RuntimeError('refuse to overwrite existing different '+str(target))
    result={}
    for source in sources:
        target=DOCUMENTS/source.name
        shutil.copy2(source,target)
        digest=sha256(source.read_bytes()).hexdigest()
        if sha256(target.read_bytes()).hexdigest()!=digest:raise RuntimeError('copy mismatch')
        result[str(target)]={'sha256':digest,'bytes':target.stat().st_size}
    (HERE/'DELIVERY.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    if sys.argv[1:]==['accept-visual']:accept()
    elif sys.argv[1:]==['deliver']:deliver()
    else:raise SystemExit('accept-visual or deliver required')
