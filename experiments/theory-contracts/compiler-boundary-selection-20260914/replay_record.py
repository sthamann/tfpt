"""Exact replay and falsification of the source record-selection calculation."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'record_selection.py'
runs=[]


def need(ok,message):
    if not ok:raise RuntimeError(message)


for flags,out in [([], 'record_selection.json'), (['-OO'], 'record_selection_optimized.json')]:
    run=subprocess.run([sys.executable,'-B',*flags,str(SOURCE),'--out',out],capture_output=True,text=True)
    need(run.returncode==0,'exact record replay failed: '+run.stderr)
    runs.append({'flags':flags,'exit_code':run.returncode})
need((HERE/'record_selection.json').read_bytes()==(HERE/'record_selection_optimized.json').read_bytes(),
     'normal versus optimized result mismatch')
for mutant in ['same_record','four_is_neutral','boundary_changes_rate']:
    run=subprocess.run([sys.executable,'-B','-OO',str(SOURCE),'--mutant',mutant,
                        '--out','mutant_must_not_exist.json'],capture_output=True,text=True)
    need(run.returncode!=0 and 'MUTANT:' in run.stderr,'false scientific claim escaped: '+mutant)
    runs.append({'mutant':mutant,'exit_code':run.returncode,'diagnostic':run.stderr.splitlines()[-1]})
certificate={'status':'PASS','check_count':json.loads((HERE/'record_selection.json').read_text())['check_count'],
    'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'normal_optimized_byte_identical':True,'mutants_rejected':3,'runs':runs}
(HERE/'record_replay.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(certificate,indent=2),flush=True)
