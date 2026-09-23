"""Execute the new checker twice without changing any prior research report."""
from pathlib import Path
from hashlib import sha256
import subprocess
import sys
import json
here=Path(__file__).resolve().parent
runs=[]
totals={'guards':0,'exact_guards':0,'numerical_guards':0}
manifest_path=here/'replay_manifest.json'
def progress(status,**extra):
    manifest_path.write_text(json.dumps({'status':status,'runs':runs,**extra},indent=2)+'\n')
progress('RUNNING')
for checker,prefix in [('verify_hole.py',''),('addition_response.py','addition_'),
                       ('external_synthesis.py','external_'),
                       ('minimal_interfaces.py','interfaces_')]:
    outputs=[]
    for mode,flags in [('normal',[]),('optimized',['-OO'])]:
        p=subprocess.run([sys.executable,*flags,str(here/checker)],capture_output=True,cwd=here)
        (here/f'{prefix}{mode}.json').write_bytes(p.stdout)
        (here/f'{prefix}{mode}.stderr.txt').write_bytes(p.stderr)
        if p.returncode:
            runs.append({'checker':checker,'mode':mode,'exit_code':p.returncode})
            progress('FAIL',reason='checker returned a nonzero exit code')
            print(p.stderr.decode(),file=sys.stderr)
            raise SystemExit(p.returncode)
        try:
            data=json.loads(p.stdout)
        except (ValueError,TypeError):
            progress('FAIL',reason='invalid checker JSON',checker=checker,mode=mode)
            raise
        if data['status']!='PASS':
            progress('FAIL',reason='checker status is not PASS',checker=checker,mode=mode)
            raise RuntimeError('checker did not pass')
        digest=sha256(p.stdout).hexdigest(); outputs.append(digest)
        runs.append({'checker':checker,'mode':mode,'exit_code':p.returncode,'sha256':digest})
    if outputs[0]!=outputs[1]:
        progress('FAIL',reason='normal and optimized output differ',checker=checker)
        raise RuntimeError('normal and optimized output differ')
    for key in totals:
        totals[key]+=data[key]
manifest={'status':'PASS','runs':runs,**totals,
          'scope':'counts are guards, not independent new theorems or physical closure'}
(here/'replay_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
