"""Freeze only scoped inputs; run exact audit with and without optimization."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
INPUTS={
 'native_tensor.npz':'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz',
 'tfpt_1_architecture_e8.tex':'tfpt_1_architecture_e8.tex',
 'THEORY.md':'docs/THEORY.md',
 'v177_seam_marking_kernel.py':'verification/v177_seam_marking_kernel.py',
 'v469_seam_crossedproduct_route.py':'verification/v469_seam_crossedproduct_route.py',
 'v506_seam_clock_rigidity.py':'verification/v506_seam_clock_rigidity.py',
 'v510_seam_bit_freedom.py':'verification/v510_seam_bit_freedom.py',
 'previous_spinlift_RESULTS.md':'experiments/theory-contracts/universalraum-spin-lift-basics-20260915/RESULTS.md',
 'native_ground_RESULTS.md':'experiments/theory-contracts/universalraum-native-ground-response-20260915/RESULTS.md',
}

def main():
    (HERE/'sources').mkdir(exist_ok=True)
    manifest={}
    for name,relative in INPUTS.items():
        source=ROOT/relative;target=HERE/'sources'/name
        if not target.exists():shutil.copy2(source,target)
        manifest[name]={'original':str(source),'sha256':sha256(target.read_bytes()).hexdigest(),
                        'current_source_matches_snapshot':source.read_bytes()==target.read_bytes()}
    (HERE/'sources_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    runs=[]
    for name,flags in [('normal',[]),('optimized',['-OO'])]:
        result=subprocess.run([sys.executable,*flags,str(HERE/'verify_native_reset.py')],
                              capture_output=True,text=True,cwd=HERE)
        (HERE/(name+'.stderr.txt')).write_text(result.stderr)
        if result.returncode:raise RuntimeError(name+': '+result.stderr)
        data=json.loads(result.stdout)
        if data['status']!='PASS':raise RuntimeError('non-PASS '+name)
        (HERE/(name+'.json')).write_text(result.stdout)
        runs.append({'variant':name,'exit_code':result.returncode,
                     'sha256':sha256(result.stdout.encode()).hexdigest(),'exact_checks':data['exact_checks']})
    if runs[0]['sha256']!=runs[1]['sha256']:raise RuntimeError('optimized output mismatch')
    ground=json.loads((HERE/'ground_replay_manifest.json').read_text())
    if ground['status']!='PASS':raise RuntimeError('native ground replay did not pass')
    report={'status':'PASS','runs':runs,'normal_optimized_byte_identical':True,
            'native_ground_replayed':True,'ground_certificate_scope':ground['scope'],
            'ground_commands':len(ground['commands']),
            'proof_boundary':'finite exact audit plus analytical arguments in RESULTS.md; no TOE closure'}
    (HERE/'replay.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
