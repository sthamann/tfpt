"""Normal/optimized replay plus narrowly targeted in-memory negative controls."""
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'check_extension.py'


def main():
    outputs=[]
    for flags in (['-B'],['-B','-OO']):
        run=subprocess.run([sys.executable,*flags,str(SOURCE)],capture_output=True,text=True,
                           timeout=60,check=True)
        if run.stderr:
            raise ValueError(run.stderr)
        outputs.append(run.stdout)
    if outputs[0]!=outputs[1]:
        raise ValueError('normal and optimized output mismatch')
    raw=SOURCE.read_text()
    mutations=[
        ('(C.T*B*C+F.T*F)/28','(C.T*B*C+F.T*F)/27','source transition factorization'),
        ('s.Rational(1,5)*s.Rational(3,7)**(n-1)','s.Rational(1,5)**n',
         'independent first preparation then retained context formula'),
        ('H2=6*eye+sum(swaps)','H2=6*eye-sum(swaps)','tetramer exact full spectrum'),
        ('sign=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))',
         'sign=1','unique zero energy vector'),
        ('sign=(-1)**((state & ((1<<mode)-1)).bit_count())','sign=1','canonical CAR'),
        ('fixed_dimension==23076','fixed_dimension==1','unitary fixed-operator algebra is highly nonunique'),
    ]
    rejected=[]
    for old,new,guard in mutations:
        if raw.count(old)!=1:
            raise ValueError('not unique mutation: '+old)
        code='__file__='+repr(str(SOURCE))+'\n'+raw.replace(old,new)
        run=subprocess.run([sys.executable,'-B','-OO','-c',code],capture_output=True,text=True,timeout=60)
        if run.returncode==0 or guard not in run.stderr:
            raise ValueError('negative control did not fire correctly: '+guard+'\n'+run.stderr)
        rejected.append(guard)
    (HERE/'verification.json').write_text(outputs[0])
    report={'normal_OO_byte_identical':True,'checks_per_mode':json.loads(outputs[0])['checks'],
            'rejected_mutations':rejected,'T1_T8_closed':[]}
    (HERE/'replay.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
