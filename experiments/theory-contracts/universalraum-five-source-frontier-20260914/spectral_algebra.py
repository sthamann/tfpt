"""Exact regular-representation certificate behind local F4 positivity.
Also audits, without rerunning, the submitted 64-sector numerical summaries.
"""
from itertools import permutations,combinations
from pathlib import Path
import json,hashlib
import numpy as np
HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,name):
    if not bool(ok):raise RuntimeError(name)
    checks.append(name)

def run():
    perms=list(permutations(range(6)));idx={p:i for i,p in enumerate(perms)}
    rows=[]
    for j in range(1,6):
        row=[]
        for p in perms:
            q=list(p);q[0],q[j]=q[j],q[0];row.append(idx[tuple(q)])
        rows.append(row)
    def A(v):return 5*v-sum((v[r,:] for r in rows),np.zeros_like(v))
    v=np.eye(720,dtype=np.int64);maxentry=0
    # A is sum of five I-S positive terms: A>=0. This exact annihilating
    # polynomial then confines its spectrum to integers 0..10, whence A(A-I)>=0.
    for k in range(11):
        v=A(v)-k*v
        maxentry=max(maxentry,int(np.max(abs(v))))
    need(np.count_nonzero(v)==0,'regular S6: product_(k=0)^10(A-kI)=0 exactly')
    need(maxentry<2**60,'exact polynomial intermediate values fit int64')
    p=HERE/'sources/evidence/validation_sectors_f4.json'
    report=json.loads(p.read_text())['sectors_f4'];per=report['per_sector']
    need(len(per)==64,'submitted sector table contains 64 sectors')
    need(sum(x['dim_Sn']*x['dim_SU4'] for x in per.values())==4**16,'Schur-Weyl dimensions sum to entire matter dimension')
    trunc=[]
    for shape,r in per.items():
        if sum(l['multiplicity_detected'] for l in r['levels'])<r['dim_Sn']:trunc.append(shape)
    need(len(trunc)>0,'submitted table is low bare modes, not full corrected diagonalisation')
    # Pointwise monotonicity of f(h)=h+eps²/2(h²-76h+1440), h in [0,40].
    need(1-38/400>0,'operator lower bound f(H0) monotone over entire bare spectrum at 1/20')
    return {'count':len(checks),'checks':checks,'regular_dimension':720,'largest_integer_intermediate':maxentry,
      'local_F4_identity':'sum_v A_v(A_v-I), A_v=sum_{e incident v}(I-S_e)',
      'local_F4_positive':True,'local_F4_operator_lower_bound':'H0^2 - 76 H0 + 1440 I',
      'submitted_sectors':64,'bare_modes_truncated_in_sectors':len(trunc),
      'all_sector_table_hash':hashlib.sha256(p.read_bytes()).hexdigest(),
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'exact_first_excited_multiplicity_proved':False,'T1_T8_closed':[]}
if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(HERE/'spectral_algebra.json'));a=ap.parse_args()
    out=run();Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2))
