"""Portable exact replay for the source-composition field strand."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess
import sys
HERE=Path(__file__).resolve().parent
def main():
 outputs=[]
 for name,flags in [('normal',[]),('optimized',['-OO'])]:
  run=subprocess.run([sys.executable,'-B','-W','error',*flags,str(HERE/'verify.py')],cwd=HERE,capture_output=True,check=False)
  if run.returncode or run.stderr:raise RuntimeError(name+': '+run.stderr.decode())
  outputs.append(run.stdout);(HERE/('results.'+name+'.json')).write_bytes(run.stdout)
 if outputs[0]!=outputs[1]:raise RuntimeError('normal and optimized outputs differ')
 data=json.loads(outputs[0]);manifest={'status':'PASS','normal_optimized_byte_identical':True,
  'exact_checks_per_mode':data['exact_checks'],'numerical_checks_per_mode':0,'input_pins':data['pins'],
  'verify_sha256':sha256((HERE/'verify.py').read_bytes()).hexdigest(),'results_sha256':sha256(outputs[0]).hexdigest(),
  'dependencies':'Python and SymPy; no network or absolute paths'}
 (HERE/'replay_manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
 print(json.dumps(manifest,indent=2,sort_keys=True))
if __name__=='__main__':main()
