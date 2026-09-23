"""Store generated reports, preserving failures and checking optimized replay."""
from pathlib import Path
from hashlib import sha256
import subprocess
import sys
import json

here=Path(__file__).resolve().parent
runs=[]
totals={'guards':0,'exact_guards':0,'numerical_guards':0}
for checker,prefix in [('verify_minimal.py',''),('native_three.py','native_three_'),('native_cubic.py','native_cubic_')]:
    outputs=[]
    for mode,flags in [('normal',[]),('optimized',['-OO'])]:
        cmd=[sys.executable,*flags,str(here/checker)]
        p=subprocess.run(cmd,capture_output=True,cwd=here)
        (here/f'{prefix}{mode}.stderr.txt').write_bytes(p.stderr)
        (here/f'{prefix}{mode}.json').write_bytes(p.stdout)
        digest=sha256(p.stdout).hexdigest(); outputs.append(digest)
        runs.append({'checker':checker,'mode':mode,'exit_code':p.returncode,'sha256':digest})
        if p.returncode:
            print(p.stderr.decode(),file=sys.stderr)
            raise SystemExit(p.returncode)
        data=json.loads(p.stdout)
        if data['status']!='PASS':
            raise RuntimeError('checker did not return PASS')
    if outputs[0]!=outputs[1]:
        raise RuntimeError('normal and optimized reports differ')
    for key in totals:
        totals[key]+=data[key]
manifest={'status':'PASS','runs':runs,**totals,
          'note':'Counts are guards, not independent theorems or TOE completion.'}
(here/'replay_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
