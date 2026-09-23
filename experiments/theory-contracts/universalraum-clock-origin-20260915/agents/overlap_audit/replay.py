"""Pin the supplied text unchanged and reproduce the isolated overlap audit."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent
SOURCE=Path('/Users/stefanhamann/.codex/attachments/59dc0059-8914-48ca-953d-85933f66e00b/pasted-text.txt')
PIN='1a75e84b28868dd682e4b2337d6546f275f49321e489b3b23af4754a844d1ac4'
def digest(path):
    return sha256(path.read_bytes()).hexdigest()
if digest(SOURCE)!=PIN:
    raise RuntimeError('User source differs from the inspected version')
shutil.copy2(SOURCE,HERE/'attachment.txt')
if digest(HERE/'attachment.txt')!=PIN:
    raise RuntimeError('Attachment copy differs')
results=[]
for mode,flags in [('normal',['-B']),('optimized',['-B','-OO'])]:
    process=subprocess.run([sys.executable,*flags,str(HERE/'check_overlap.py')],
                           stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
    if process.stderr:
        raise RuntimeError(process.stderr.decode())
    (HERE/f'check_overlap_{mode}.json').write_bytes(process.stdout)
    results.append(process.stdout)
if results[0]!=results[1]:
    raise RuntimeError('Normal and optimized results differ')
if digest(SOURCE)!=PIN:
    raise RuntimeError('Source changed during audit')
receipt={'status':'PASS','source':str(SOURCE),'source_sha256':PIN,
         'source_unchanged':True,'attachment_copy_sha256':digest(HERE/'attachment.txt'),
         'checker_sha256':digest(HERE/'check_overlap.py'),
         'normal_optimized_identical':True,
         'result_sha256':sha256(results[0]).hexdigest(),
         'checks':json.loads(results[0])['checks']}
(HERE/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
