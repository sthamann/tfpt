"""Replay the decisive finite claims; do not equate checks with TOE closure."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

HERE=Path(__file__).resolve().parent
PYTHON=sys.executable
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
commands=[
    ['exact_one_record_protocol.py'],
    ['-OO','exact_one_record_protocol.py','--output',str(HERE/'exact_one_record_protocol.optimized.json')],
    ['core_origin_audit.py'],
    ['-OO','core_origin_audit.py','--output',str(HERE/'core_origin_audit.optimized.json')],
    ['parameter_transfer.py'],
    ['-OO','parameter_transfer.py','--output',str(HERE/'parameter_transfer.optimized.json')],
    ['matching_band.py'],
    ['-OO','matching_band.py','--output',str(HERE/'matching_band.optimized.json')],
    ['protocol_review/checker.py'],
    ['cell_coupling/source_claims.py'],
    ['spectral/nonzero_followup/checker.py','projectors'],
    ['spectral/nonzero_followup/checker.py','certify'],
    ['spectral/nonzero_followup/complete_replay.py'],
    ['-OO','spectral/nonzero_followup/complete_replay.py'],
]
records=[]
for command in commands:
    print('REPLAY', ' '.join(command),flush=True)
    run=subprocess.run([PYTHON,'-B',*command],cwd=HERE,env=env,text=True,capture_output=True)
    records.append({'argv':[PYTHON,'-B',*command],'exit_code':run.returncode,
                    'stdout':run.stdout,'stderr':run.stderr})
    if run.returncode:
        (HERE/'core_replay.json').write_text(json.dumps({'success':False,'runs':records},indent=2)+'\n')
        print(run.stdout,run.stderr)
        raise SystemExit(run.returncode)
pairs=[('exact_one_record_protocol.json','exact_one_record_protocol.optimized.json'),
       ('core_origin_audit.json','core_origin_audit.optimized.json'),
       ('parameter_transfer.json','parameter_transfer.optimized.json'),
       ('matching_band.json','matching_band.optimized.json'),
       ('seed_and_protocol.json','seed_and_protocol_optimized.json')]
comparisons={a:((HERE/a).read_bytes()==(HERE/b).read_bytes()) for a,b in pairs}
if not all(comparisons.values()):
    raise RuntimeError('Normal/optimized mismatch: '+str(comparisons))
out={'success':True,'command_count':len(records),'runs':records,
     'byte_equal_normal_and_optimized':comparisons,
     'scope':'targeted finite proof replay; no full external-suite, cosmology-rerun, or TOE-closure claim',
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'core_replay.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'success':True,'commands':len(records),'byte_equal':comparisons},indent=2))
