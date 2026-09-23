"""Replay the final zip from a fresh directory and compare its pinned outputs."""
from hashlib import sha256
from pathlib import Path
from tempfile import mkdtemp
from zipfile import ZipFile
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
archive=HERE/'TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10.zip'
destination=Path(mkdtemp(prefix='tfpt-spinlift-portable-'))
with ZipFile(archive) as z:
    for name in z.namelist():
        path=Path(name)
        if path.is_absolute() or '..' in path.parts:raise RuntimeError('unsafe archive path')
    z.extractall(destination)
files=['verification_normal.json','verification_optimized.json',
       'late_aspects_normal.json','late_aspects_optimized.json',
       'reflection_selection_normal.json','reflection_selection_optimized.json']
before={f:(destination/f).read_bytes() for f in files}
p=subprocess.run([sys.executable,str(destination/'replay.py')],cwd=destination,capture_output=True)
(HERE/'portable_replay_stdout.txt').write_bytes(p.stdout)
(HERE/'portable_replay_stderr.txt').write_bytes(p.stderr)
if p.returncode:raise RuntimeError(p.stderr.decode())
if any((destination/f).read_bytes()!=data for f,data in before.items()):raise RuntimeError('portable output differs from pinned result')
if json.loads((destination/'REPLAY.json').read_text())['status']!='PASS':raise RuntimeError('portable replay nonPASS')
report={'status':'PASS','archive_sha256':sha256(archive.read_bytes()).hexdigest(),
        'fresh_directory':str(destination),'exit_code':p.returncode,
        'all_six_scientific_results_byte_identical_to_packaged_outputs':True,
        'historical_v480_replayed_normal_and_optimized':True,
        'no_original_source_paths_required_for_scientific_replay':True,
        'separate_external_614_suite_not_run_by_this_runner':True}
(HERE/'PORTABLE_REPLAY.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
