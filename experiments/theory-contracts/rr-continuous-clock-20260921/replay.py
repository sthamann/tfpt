from pathlib import Path
import json, subprocess, sys
base=Path(__file__).resolve().parent
code="import importlib.util,pathlib,json; p=pathlib.Path.cwd(); s=importlib.util.spec_from_file_location('rrclock',p/'checker.py'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); m.TENSOR=p/'native_tensor.npz'; print(json.dumps(m.main(),indent=2,sort_keys=True))"
normal=subprocess.check_output([sys.executable,'-B','-c',code],cwd=base)
optimized=subprocess.check_output([sys.executable,'-OO','-B','-c',code],cwd=base)
if normal!=optimized: raise RuntimeError('normal/optimized mismatch')
data=json.loads(normal)
if data['status']!='PASS': raise RuntimeError('certificate not PASS')
(base/'certificate.json').write_bytes(normal)
receipt={'status':'PASS','normal_optimized_byte_identical':True,'exact_checks':data['exact_checks'],'total_intertwining_mismatches':data['intertwining']['total_mismatches']}
(base/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
