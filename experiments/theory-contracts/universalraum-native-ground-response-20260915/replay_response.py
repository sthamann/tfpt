"""Fail-closed replay and byte identity for the new research certificates."""
from pathlib import Path
from hashlib import sha256
import subprocess
import json
import sys

HERE=Path(__file__).resolve().parent
state={'status':'RUNNING','runs':[]}
def save():
    (HERE/'response_replay_manifest.json').write_text(json.dumps(state,indent=2)+'\n')
try:
    save()
    for name in ['charged_response.py','field_dictionary.py','operation_boundary.py',
                 'operation_symmetry.py','symmetry_availability.py','lorentz_types.py',
                 'pole_consolidation.py']:
        results=[]
        for mode,options in [('normal',[]),('optimized',['-OO'])]:
            process=subprocess.run([sys.executable,*options,str(HERE/name)],capture_output=True,text=True,cwd=HERE)
            prefix=HERE/(name.removesuffix('.py')+'_'+mode)
            prefix.with_suffix('.stderr.txt').write_text(process.stderr)
            prefix.with_suffix('.json').write_text(process.stdout)
            state['runs'].append({'script':name,'mode':mode,'exit_code':process.returncode})
            save()
            if process.returncode:
                raise RuntimeError(process.stderr[-2000:])
            record=json.loads(process.stdout)
            if record['status']!='PASS':
                raise RuntimeError('non-PASS '+name)
            results.append(sha256(process.stdout.encode()).hexdigest())
            state['runs'][-1].update({'sha256':results[-1],'checks':record['checks']})
            print(name,mode,record['status'],record['checks'],flush=True)
        if results[0]!=results[1]:
            raise RuntimeError('normal/optimized difference '+name)
    state['status']='PASS'
    save()
except BaseException as error:
    state['status']='FAIL'
    state['error']=repr(error)
    save()
    raise
