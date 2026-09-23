"""Replay the owned bounded consequences, without mutating source contracts."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
REPO=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest=json.loads((HERE/'source_manifest.json').read_text())
for item in manifest['files']:
    path=Path(item['path'])
    if not path.is_absolute():
        path=REPO/path
    if sha(path)!=item['sha256']:
        raise RuntimeError('source pin mismatch: '+str(path))

jobs=[
 ('flavor_delta/checker.py','flavor_delta/certificate.json'),
 ('local_modules/check_local_modules.py','local_modules/certificate.json'),
 ('critical_review/check_weights.py',None),
 ('local_modules/check_ir_glue.py','local_modules/ir_glue_certificate.json'),
 ('flavor_delta/check_critical_flavor.py','flavor_delta/critical_flavor_certificate.json'),
 ('clock_gate/checker.py','clock_gate/certificate.json'),
 ('energy_bridge/checker.py','energy_bridge/certificate.json'),
]
records=[]
for script,output in jobs:
    hashes=[]
    payload=None
    for options in [[],['-OO']]:
        run=subprocess.run([sys.executable,*options,str(HERE/script)],cwd=HERE/script.split('/')[0],capture_output=True,text=True)
        if run.returncode:
            raise RuntimeError(script+' '+repr(options)+'\n'+run.stdout+'\n'+run.stderr)
        if output:
            hashes.append(sha(HERE/output))
            payload=json.loads((HERE/output).read_text())
        else:
            payload=json.loads(run.stdout)
            normalized=json.dumps(payload,sort_keys=True,indent=2)+'\n'
            hashes.append(hashlib.sha256(normalized.encode()).hexdigest())
            (HERE/'critical_review/replay_certificate.json').write_text(normalized)
    if hashes[0]!=hashes[1]:
        raise RuntimeError('normal/optimized result mismatch: '+script)
    records.append({'checker':script,'normal_optimized_identical':True,
                    'certificate_sha256':hashes[0],
                    'mathematical_scope':'See associated proof; replay is not physical gate closure.'})

result={
 'research_id':'UR.SOURCE.CRITICAL_FIELDS.01','verdict':'PARTIAL',
 'all_owned_replays_passed':True,'normal_optimized_identical':True,
 'replays':records,'pinned_original_files':len(manifest['files']),
 'physical_gates_closed':[],'complete_TFPT_solution':False,
 'scope':'Exact local lattice fields, conditional Ising and flavor consequences, fixed-clock tests, direct source-energy comparison. No derived common interacting source or full IR projector.'}
(HERE/'validation.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps({'verdict':'PARTIAL','owned_replays':len(records),
                  'all_passed':True,'source_files':len(manifest['files']),
                  'complete_TFPT_solution':False}))
