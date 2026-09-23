"""Verify exact certificate is optimization-independent, excluding timing."""
from pathlib import Path
import json,subprocess,sys,os
HERE=Path(__file__).resolve().parent
before=json.loads((HERE/'verification.json').read_text())
proc=subprocess.run([sys.executable,'-OO',str(HERE/'checker.py'),'--exact'],
                    text=True,capture_output=True,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'})
if proc.returncode:raise RuntimeError(proc.stdout+proc.stderr)
after=json.loads((HERE/'verification.json').read_text())
before.pop('elapsed_seconds');after.pop('elapsed_seconds')
if before!=after:raise RuntimeError('semantic certificate differs under -OO')
out={'status':'PASS','optimized_process_exit_code':proc.returncode,
     'exact_certificate_identical_except_elapsed_seconds':True,'check_count':after['check_count']}
(HERE/'optimized_comparison.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2))
