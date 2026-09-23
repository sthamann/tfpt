"""Freeze the requested evidence and replay only inspected read-only checkers."""
from pathlib import Path
import hashlib, json, subprocess, sys, shutil
from concurrent.futures import ThreadPoolExecutor

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PY='/opt/homebrew/bin/python3'
SOURCES={
 'input_matrix.txt':'/Users/stefanhamann/.codex/attachments/ec82946e-d1bd-46b9-9219-af86076f6c0e/pasted-text.txt',
 'input_space.txt':'/Users/stefanhamann/.codex/attachments/cd37b745-3bb4-47e3-8822-5c526f48ba18/pasted-text.txt',
 'input_worker.txt':'/Users/stefanhamann/.codex/attachments/a41372d2-0b8f-44a2-b085-09898298a6ea/pasted-text.txt',
 'preliminary_core_v16.md':'/Users/stefanhamann/Documents/TFPT_Universalraum_Kernprobleme_2026-09-14_v1.6.md',
 'preliminary_audit_v16.md':'/Users/stefanhamann/Documents/TFPT_Universalraum_Quellenpruefung_2026-09-14_v1.6.md',
 'preliminary_update_v16.md':'/Users/stefanhamann/Documents/TFPT_Universalraum_Kurzupdate_2026-09-14_v1.6.md',
 'native_tensor.npz':'/Users/stefanhamann/Documents/Codex/2026-09-14/scha-3/outputs/simple_core/spinor_tensors.npz',
}
for name,rel in {
 'order_proof.md':'compiler-cone-object-audit/ORDER_PROOF.md',
 'marked_bridge.md':'compiler-cone-object-audit/MARKED_BRIDGE.md',
 'session_results.md':'session-reorientation-20260914/RESULTS.md',
 'native_results.md':'session-reorientation-20260914/native/RESULTS.md',
 'weyl_results.md':'session-reorientation-20260914/weyl/RESULTS.md',
 'compatibility_results.md':'session-reorientation-20260914/compatibility/RESULTS.md',
}.items():
    SOURCES[name]=str(HERE.parent/rel)
(HERE/'sources').mkdir(exist_ok=True)
manifest=[]
for name,path in SOURCES.items():
    p=Path(path); dst=HERE/'sources'/name
    if dst.exists() and dst.read_bytes()!=p.read_bytes():
        raise RuntimeError('Frozen source changed: '+path)
    shutil.copy2(p,dst)
    manifest.append({'path':path,'snapshot':name,'sha256':hashlib.sha256(dst.read_bytes()).hexdigest()})
(HERE/'sources.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
jobs={
 'new_checks':HERE/'verify_v16.py',
 'order':HERE.parent/'compiler-cone-object-audit/checker.py',
 'native':HERE.parent/'session-reorientation-20260914/check_native.py',
 'weyl':HERE.parent/'session-reorientation-20260914/weyl/check_weyl.py',
 'compatibility':HERE.parent/'session-reorientation-20260914/compatibility/checker.py',
}
def run(item):
    name,path=item
    outputs=[]
    for flags in [[],['-OO']]:
        command=[PY,*flags,str(path)]
        if name=='compatibility':
            command=[PY,*flags,str(HERE/'read_only_compatibility.py'),str(path)]
        result=subprocess.run(command,cwd=ROOT,capture_output=True)
        if result.returncode:
            raise RuntimeError(name+': '+result.stderr.decode()+result.stdout.decode())
        outputs.append(result.stdout)
    if outputs[0]!=outputs[1]:
        raise RuntimeError('Optimized run differs: '+name)
    data=json.loads(outputs[0])
    (HERE/(name+'.json')).write_bytes(outputs[0])
    print(name,'PASS; normal and -OO identical',flush=True)
    return name,{'script':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'normal_and_optimized_equal':True,'exit_code':0}
with ThreadPoolExecutor(max_workers=3) as pool:
    results=dict(pool.map(run,jobs.items()))
(HERE/'replay_manifest.json').write_text(json.dumps(results,indent=2)+'\n')
