"""Normal/optimized replay of the64D-bounded collision contract and mutants."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE=Path(__file__).resolve().parent
PYTHON='/opt/homebrew/bin/python3'
rows=[]


def need(ok,message):
    if not ok:raise RuntimeError(message)


for flags,name in [([],'verification.json'),(['-OO'],'verification_optimized.json')]:
    p=subprocess.run([PYTHON,*flags,str(HERE/'probe.py'),'--out',name],capture_output=True,text=True)
    need(p.returncode==0,'positive collision replay failed: '+p.stderr)
    rows.append({'flags':flags,'returncode':p.returncode})
need((HERE/'verification.json').read_bytes()==(HERE/'verification_optimized.json').read_bytes(),
     'normal and optimized collision outputs differ')
for mutant in ['reuse_equals_fresh','sign_invisible_with_filters','pure_environment_dimension4']:
    p=subprocess.run([PYTHON,'-OO',str(HERE/'probe.py'),'--mutant',mutant,'--out','must_not_exist.json'],capture_output=True,text=True)
    need(p.returncode!=0 and 'MUTANT:' in p.stderr,'collision mutant escaped: '+mutant)
    rows.append({'mutant':mutant,'returncode':p.returncode,'diagnostic':p.stderr.splitlines()[-1]})
positive=json.loads((HERE/'verification.json').read_text())
out={'status':'PASS','collision_checks':positive['check_count'],'source_decode_prefix_checks':positive['source_prefix_checks'],
     'normal_optimized_byte_identical':True,'mutants_rejected':3,
     'probe_sha256':hashlib.sha256((HERE/'probe.py').read_bytes()).hexdigest(),'runs':rows}
(HERE/'replay.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
