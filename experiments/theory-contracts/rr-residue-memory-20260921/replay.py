from pathlib import Path
import hashlib, importlib.util, json, subprocess, sys
BASE=Path(__file__).resolve().parent

def worker(kind):
    spec=importlib.util.spec_from_file_location('current_check',BASE/(kind+'_checker.py'))
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    m.TENSOR=BASE/'native_tensor.npz'
    if kind=='hodge':
        sources=json.loads((BASE/'source_snapshots.json').read_text())
        m.PINS={BASE/name:item['sha256'] for name,item in sources.items()}
    return m.exact_run()

if len(sys.argv)>1:
    print(json.dumps(worker(sys.argv[1]),indent=2,sort_keys=True))
else:
    receipts={}
    for kind in ('residue','hodge'):
        normal=subprocess.check_output([sys.executable,'-B',str(BASE/'replay.py'),kind])
        optimized=subprocess.check_output([sys.executable,'-OO','-B',str(BASE/'replay.py'),kind])
        if normal!=optimized: raise RuntimeError(kind+': normal/optimized mismatch')
        data=json.loads(normal)
        if data['status']!='PASS_EXACT_SCOPED': raise RuntimeError(kind+': failed')
        (BASE/(kind+'_certificate.json')).write_bytes(normal)
        receipts[kind]={'status':data['status'],'normal_optimized_byte_identical':True,'checks':len(data['checks'])}
    (BASE/'replay_receipt.json').write_text(json.dumps(receipts,indent=2)+'\n')
    print(json.dumps(receipts,indent=2))
