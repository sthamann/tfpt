"""Both independent finite redteam checks, optimized replay and mutants."""
from pathlib import Path
import subprocess
import hashlib
import json

HERE=Path(__file__).resolve().parent
PYTHON='/opt/homebrew/bin/python3'
rows=[]


def need(ok,message):
    if not ok:raise RuntimeError(message)


for script,prefix in [('probe.py','verification'),('sigma_sources.py','sigma_verification')]:
    for flags,name in [([],prefix+'.json'),(['-OO'],prefix+'_optimized.json')]:
        p=subprocess.run([PYTHON,*flags,str(HERE/script),'--out',name],capture_output=True,text=True)
        need(p.returncode==0,'positive replay failed: '+p.stderr)
        rows.append({'script':script,'flags':flags,'returncode':p.returncode})
    need((HERE/(prefix+'.json')).read_bytes()==(HERE/(prefix+'_optimized.json')).read_bytes(),'optimized mismatch '+script)
for mutant in ['clock12_observable','same_sigma_chart','gluing_selects_rate']:
    p=subprocess.run([PYTHON,'-OO',str(HERE/'probe.py'),'--mutant',mutant,'--out','must_not_exist.json'],capture_output=True,text=True)
    need(p.returncode!=0 and 'MUTANT:' in p.stderr,'mutant escaped '+mutant)
    rows.append({'mutant':mutant,'returncode':p.returncode,'error':p.stderr.splitlines()[-1]})
result={'status':'PASS','trace_GNS_checks':json.loads((HERE/'verification.json').read_text())['check_count'],
        'source_sigma_checks':json.loads((HERE/'sigma_verification.json').read_text())['check_count'],
        'normal_optimized_byte_identical':True,'mutants_rejected':3,'runs':rows,
        'script_hashes':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in ['probe.py','sigma_sources.py']}}
(HERE/'replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
