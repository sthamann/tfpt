"""Small independent replay of the source-marked two-rate extension."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE=Path(__file__).resolve().parent
PYTHON='/opt/homebrew/bin/python3'
rows=[]


def need(ok,message):
    if not ok:raise RuntimeError(message)


for flags,name in [([],'two_rate_verification.json'),(['-OO'],'two_rate_verification_optimized.json')]:
    p=subprocess.run([PYTHON,*flags,str(HERE/'two_rate.py'),'--out',name],capture_output=True,text=True)
    need(p.returncode==0,'positive two-rate replay failed: '+p.stderr)
    rows.append({'flags':flags,'returncode':p.returncode})
need((HERE/'two_rate_verification.json').read_bytes()==(HERE/'two_rate_verification_optimized.json').read_bytes(),
     'normal and optimized two-rate outputs differ')
for mutant in ['same_dimensionless_rate','unsigned_lift','positive_implies_CP']:
    p=subprocess.run([PYTHON,'-OO',str(HERE/'two_rate.py'),'--mutant',mutant,'--out','must_not_exist.json'],capture_output=True,text=True)
    need(p.returncode!=0 and 'MUTANT:' in p.stderr,'two-rate mutant escaped: '+mutant)
    rows.append({'mutant':mutant,'returncode':p.returncode,'diagnostic':p.stderr.splitlines()[-1]})
out={'status':'PASS','checks':json.loads((HERE/'two_rate_verification.json').read_text())['check_count'],
     'normal_optimized_byte_identical':True,'mutants_rejected':3,
     'source_sha256':hashlib.sha256((HERE/'two_rate.py').read_bytes()).hexdigest(),'runs':rows}
(HERE/'two_rate_replay.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
