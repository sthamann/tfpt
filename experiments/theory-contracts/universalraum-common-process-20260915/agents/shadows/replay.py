"""Portable replay: Python3.10+ and NumPy; no source contract is modified."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent

def main():
    sources=json.loads((HERE/'sources_manifest.json').read_text())['files']
    for name,digest in sources.items():
        if sha256((HERE/name).read_bytes()).hexdigest()!=digest:
            raise RuntimeError('source pin failed: '+name)
    outputs=[]
    for name,flags in [('normal',[]),('optimized',['-OO'])]:
        run=subprocess.run([sys.executable,'-B','-W','error',*flags,str(HERE/'verify.py')],
                           cwd=HERE,capture_output=True,check=False)
        if run.returncode!=0 or run.stderr:
            raise RuntimeError(name+' failed: '+run.stderr.decode())
        outputs.append(run.stdout)
        (HERE/('results.'+name+'.json')).write_bytes(run.stdout)
    if outputs[0]!=outputs[1]:
        raise RuntimeError('normal and optimized outputs differ')
    result=json.loads(outputs[0])
    manifest={'status':'PASS','input_pins':len(sources),'normal_optimized_byte_identical':True,
              'exact_checks_per_mode':result['exact_checks'],'numerical_checks_per_mode':result['numerical_checks'],
              'verify_sha256':sha256((HERE/'verify.py').read_bytes()).hexdigest(),
              'results_sha256':sha256(outputs[0]).hexdigest(),
              'dependency':'Python3.10+ and NumPy; no network or absolute source path'}
    (HERE/'replay_manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
    print(json.dumps(manifest,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
