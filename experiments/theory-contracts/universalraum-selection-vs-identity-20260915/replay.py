"""Independently rerun both requested workers and the causal controls.

All output stays in this research branch. No publication or claim promotion.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    sources=[HERE/'worker_a/checker.py',HERE/'worker_b/verify_identity_scope.py',
             HERE/'causal_record_checker.py',ROOT/'origin_theory.tex',
             ROOT/'verification/v973_seam_route_narrowing.py',
             Path('/Users/stefanhamann/.codex/attachments/b3a502d5-9938-4c56-9cf2-f0c80f004db6/pasted-text.txt')]
    before={str(p):digest(p) for p in sources}
    jobs=[('selection',HERE/'worker_a/checker.py',True),
          ('identity',HERE/'worker_b/verify_identity_scope.py',False),
          ('causal',HERE/'causal_record_checker.py',True)]
    runs=[]
    success=True
    for name,script,uses_output in jobs:
        blobs=[]
        counts=[]
        for optimized in (False,True):
            tag='optimized' if optimized else 'normal'
            output=script.parent/f'parent_replay_{tag}.json'
            command=[sys.executable,'-B']+(['-OO'] if optimized else [])+[str(script)]
            if uses_output:
                command += ['--output',str(output)]
            proc=subprocess.run(command,cwd=ROOT,capture_output=True,timeout=90)
            (HERE/f'{name}_{tag}.stdout.txt').write_bytes(proc.stdout)
            (HERE/f'{name}_{tag}.stderr.txt').write_bytes(proc.stderr)
            row={'job':name,'mode':tag,'exit_code':proc.returncode}
            if proc.returncode==0:
                data=output.read_bytes() if uses_output else proc.stdout
                if not uses_output:
                    output.write_bytes(data)
                parsed=json.loads(data)
                count=parsed.get('checks_count',parsed.get('checks_passed',parsed.get('exact_checks')))
                row.update({'status':parsed['status'],'checks':count,'json':str(output),
                            'sha256':hashlib.sha256(data).hexdigest()})
                blobs.append(data)
                counts.append(count)
            else:
                success=False
            runs.append(row)
        identical=len(blobs)==2 and blobs[0]==blobs[1]
        success=success and identical
        runs.append({'job':name,'byte_identical':identical,
                     'counted_once':counts[0] if identical else None})
    after={str(p):digest(p) for p in sources}
    success=success and before==after
    count=sum(row['counted_once'] for row in runs if row.get('counted_once') is not None)
    result={'status':'PASS_SCOPED_REPLAY' if success else 'FAIL',
            'component_conditions_counted_once':count,'runs':runs,
            'input_sha256_before':before,'input_sha256_after':after,
            'scope':'Finite worker checks and source hashes only; written general proofs are separate. No primitive physical selection or TOE closure.'}
    (HERE/'REPLAY.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'component_conditions_counted_once':count}))
    raise SystemExit(0 if success else 1)


if __name__=='__main__':
    main()
