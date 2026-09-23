#!/usr/bin/env python3
"""Exact conditional F(E8) dressed-operator comparison; see PROOF.md."""
from pathlib import Path
from itertools import combinations, product
from collections import Counter
import argparse
import hashlib
import json
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
CHECKS = []

def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS.append(label)

def pins():
    files = json.loads((HERE/'source_manifest.json').read_text())['files']
    for rel, digest in files.items():
        need(hashlib.sha256((REPO/rel).read_bytes()).hexdigest() == digest,
             'source pin: '+rel)
    return files

def solve(rows):
    basis = {}
    for mask, rhs in rows:
        while mask:
            j = mask.bit_length()-1
            if j in basis:
                mask ^= basis[j][0]
                rhs ^= basis[j][1]
            else:
                basis[j] = (mask, rhs)
                break
        if not mask and rhs:
            raise ValueError('inconsistent sign equations')
    sol = 0
    for j, (mask, rhs) in sorted(basis.items()):
        if rhs ^ ((mask & sol).bit_count() % 2):
            sol |= 1 << j
    need(all(((mask & sol).bit_count() % 2) == rhs for mask, rhs in rows),
         'all '+str(len(rows))+' sign equations solved exactly')
    return sol, len(basis)

def census(counter):
    return [{'data': list(k) if isinstance(k,tuple) else k, 'count':v}
            for k,v in sorted(counter.items())]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='certificate.json')
    args=parser.parse_args()
    files=pins()
    path=REPO/'experiments/theory-contracts/universalraum-keyD-native-instruments-20260915/native_source.py'
    prefix, marker, _=path.read_text().partition('# --- Root-opposite boson pairing')
    need(bool(marker),'native prefix boundary')
    ns={'__file__':str(path),'__name__':'native_source_prefix'}
    exec(compile(prefix,str(path),'exec',optimize=0),ns)
    need(len(ns['checks'])==6,'all six original native prefix guards retained')
    fw,bw,W,PAIRS=[ns[k] for k in ['FW','BW','W','PAIRS']]
    a=np.array([1,1,1,-1,-1,-1,-1,-1],dtype=np.int64)
    k=np.array([1]*9+[-1],dtype=np.int64)
    K=np.diag(k)
    er=np.array([0]*8+[-1,0],dtype=np.int64)
    n=np.array(list(a)+[-1,3],dtype=np.int64)
    m=n-er
    g=k*n
    y6=np.array([-2,-2,-2,3,3,0,0,0,6,6],dtype=np.int64)
    Vaux=K+2*np.outer(k*m,k*m)

    def F2(r2):
        ar2=int(a@r2)
        num=np.r_[2*r2-ar2*a,0,-2*ar2]
        if np.any(num%4):
            raise RuntimeError('nonintegral F(E8) image')
        return num//4

    def eps(x,y):
        return (-1)**int(sum(x[i]*sum(y[:i]) for i in range(10))%2)

    P=np.array([F2(r)+er for r in fw])
    B=np.array([F2(r)+2*er for r in bw])
    need(np.array_equal(Vaux@K@Vaux,K),'selected generalized metric identity')
    need(all(sp.Matrix(Vaux[:j,:j]).det()>0 for j in range(1,11)),
         'Vaux positive definite by ten exact leading principal minors')
    need(int(er@(k*er))==1 and int(m@(k*m))==-1 and er@(k*m)==0,
         'actual orthogonal pair has signature (1,1)')
    need(np.all(P@g==1) and np.all(B@g==2),'odd and pair field gauge weights 1 and 2')
    need(all(x@(k*x)==3 and x@Vaux@x==3 for x in P),'all dressed fermion vectors chiral norm three')
    need(all(x@(k*x)==6 and x@Vaux@x==6 for x in B),'all dressed mediator vectors chiral norm six')
    need(all(2*sum(P[i])==sum(fw[i])-2 for i in range(64)), 'q_odd=q_E8-1')
    need(all(2*(P[i]@y6)==fw[i]@y6[:8]-12 for i in range(64)), 'Y_odd=Y_E8-1')
    need(all(2*sum(B[i])==sum(bw[i])-4 for i in range(60)), 'q_pair=q_E8-2')
    need(all(2*(B[i]@y6)==bw[i]@y6[:8]-24 for i in range(60)), 'Y_pair=Y_E8-2')
    need(all(eps(x,y)*eps(y,x)==(-1)**int((x@(k*y)+(x@(k*x))*(y@(k*y)))%2)
             for x in P for y in P),'graded cocycle commutator on all 4096 field pairs')

    # One phase per field/current, never one fit per tensor entry.
    eq=[]
    raw=np.zeros_like(W)
    blook={tuple(x):i for i,x in enumerate(B)}
    exponents=Counter()
    for c,(i,j) in enumerate(PAIRS):
        lam=int(P[i]@(k*P[j]));exponents[lam]+=1
        if lam==0:
            A=blook.get(tuple(P[i]+P[j]))
            need(A is not None,'regular pair has a native mediator label')
            raw[A,c]=eps(P[i],P[j])
    need(np.array_equal(raw!=0,W!=0),'all 120960 source/native tensor supports, including zeros')
    need(exponents=={0:480,1:1120,2:416},'whole pair exponent census')
    for A,c in zip(*np.nonzero(W)):
        i,j=PAIRS[c]
        eq.append(((1<<i)^(1<<j)^(1<<(64+int(A))),int(raw[A,c]!=W[A,c])))
    _,pairrank=solve(eq)
    need(pairrank==115,'native tensor phase equation rank')
    bad=eq.copy();bad[0]=(bad[0][0],bad[0][1]^1)
    try:
        solve(bad)
    except ValueError:
        pass
    else:
        raise RuntimeError('one wrong relative W sign escaped negative control')
    need(True,'one relative W sign cannot be removed by field rephasing')

    # The complete non-Cartan D5+D3 action from original JW operators.
    fwlook={tuple(w):i for i,w in enumerate(fw)}
    bwlook={tuple(w):i for i,w in enumerate(bw)}
    native_ops=[]
    for dim,offset in [(5,0),(3,5)]:
        ann=ns['_jw'](dim)
        ev=[j for j in range(2**dim) if j.bit_count()%2==0]
        for i,j in combinations(range(dim),2):
            for si,sj in product((1,-1),repeat=2):
                root2=np.zeros(8,dtype=np.int64)
                root2[offset+i]=2*si;root2[offset+j]=2*sj
                op=(ann[i] if si==1 else ann[i].T)@(ann[j] if sj==1 else ann[j].T)
                small=op[np.ix_(ev,ev)]
                op=np.kron(small,np.eye(4,dtype=np.int64)) if dim==5 else np.kron(np.eye(16,dtype=np.int64),small)
                native_ops.append((root2,op))
    need(len(native_ops)==52,'all 40+12 product-group roots included')
    for ell,(root2,op) in enumerate(native_ops):
        root=F2(root2)
        need(all(2*(root@(k*P[i]))==root2@fw[i]//2 for i in range(64)),
             'Cartan action on dressed fermions '+str(ell))
        src=np.zeros((64,64),dtype=np.int64)
        for i,r in enumerate(fw):
            j=fwlook.get(tuple(r+root2))
            if j is not None:
                need(root@(k*P[i])==-1,'fermion current action is an actual simple pole')
                src[j,i]=eps(root,P[i])
        need(np.array_equal(src!=0,op!=0),'complete fermion root action support '+str(ell))
        for j,i in zip(*np.nonzero(op)):
            eq.append(((1<<int(i))^(1<<int(j))^(1<<(124+ell)),int(src[j,i]!=op[j,i])))

        WR2=np.zeros_like(W)
        for c,(i,j) in enumerate(PAIRS):
            for h in np.flatnonzero(op[:,i]):
                if h!=j:
                    ab=tuple(sorted((int(h),j)))
                    WR2[:,c]+=int(op[h,i])*(1 if h<j else -1)*W[:,ns['PAIR_INDEX'][ab]]
            for h in np.flatnonzero(op[:,j]):
                if i!=h:
                    ab=tuple(sorted((i,int(h))))
                    WR2[:,c]+=int(op[h,j])*(1 if i<h else -1)*W[:,ns['PAIR_INDEX'][ab]]
        rawb=WR2@W.T
        need(not np.any(rawb%8),'integral native mediator action '+str(ell))
        bos=rawb//8
        need(np.array_equal(bos@W,WR2),'native tensor full root covariance '+str(ell))
        srcb=np.zeros((60,60),dtype=np.int64)
        for i,r in enumerate(bw):
            j=bwlook.get(tuple(r+root2))
            if j is not None:
                need(root@(k*B[i])==-1,'mediator current action is an actual simple pole')
                srcb[j,i]=eps(root,B[i])
        need(np.array_equal(srcb!=0,bos!=0),'complete mediator root action support '+str(ell))
        for j,i in zip(*np.nonzero(bos)):
            eq.append(((1<<(64+int(i)))^(1<<(64+int(j)))^(1<<(124+ell)),int(srcb[j,i]!=bos[j,i])))
    phase,rank=solve(eq)
    need((len(eq),rank)==(2032,167),'one compatible phase choice for W and both full group actions')
    signs=np.array([-1 if (phase>>i)&1 else 1 for i in range(176)],dtype=np.int64)
    transformed=raw.copy()
    for c,(i,j) in enumerate(PAIRS):
        transformed[:,c]*=signs[i]*signs[j]*signs[64:124]
    need(np.array_equal(transformed,W),'entire native W equals the dressed OPE tensor')

    # Faithful exterior-product jets, antisymmetrized at fixed positions.
    fibers={}
    for c,(i,j) in enumerate(PAIRS):
        key=tuple(map(int,P[i]+P[j]))
        fibers.setdefault(key,[]).append((c,i,j,int(P[i]@(k*P[j]))))
    jet_census=Counter();grade_ranks=[0,0,0];grade5rank=0
    for key,vals in fibers.items():
        lam=vals[0][3]
        need(all(v[3]==lam for v in vals),'equal-momentum pair fiber has fixed exponent')
        rows=[]
        for c,i,j,l in vals:
            x,y=P[i],P[j];sgn=(-1)**lam
            rows.append([1+sgn]+list(map(int,x+sgn*y))+
                        [int(x[u]*x[v]+sgn*y[u]*y[v]) for u in range(10) for v in range(u,10)])
        mat=sp.Matrix(rows)
        ranks=(mat[:,:1].rank(),mat[:,:11].rank(),mat.rank())
        jet_census[(lam,len(vals),*ranks)]+=1
        for j in range(3):
            if j>=lam:
                grade_ranks[j]+=ranks[j-lam]
        # Homogeneous total t^2 coefficient: both a_-2 and a_-1^2 at lambda=0.
        idx=2-lam
        homogeneous=mat[:,1:] if idx==2 else (mat[:,1:11] if idx==1 else mat[:,:1])
        hrank=homogeneous.rank()
        need(hrank==len(vals),'homogeneous weight-five coefficient injective on momentum fiber')
        grade5rank+=hrank
    need(jet_census=={(0,8,1,1,8):60,(1,2,0,2,2):480,(1,4,0,4,4):40,(2,1,1,1,1):416},
         'complete antisymmetric jet rank census')
    need(grade_ranks==[60,60,2016] and grade5rank==2016,'all pair directions recovered at weight five, not weight four')
    need(np.array_equal(W@W.T,8*np.eye(60,dtype=np.int64)),'source pair quotient rank sixty')
    need(2016-60==1956,'native dark kernel dimension')
    need(sp.Matrix([[8,sp.sqrt(8)],[sp.sqrt(8),1]]).det()==0,'source bright-pair/mediator Gram is rank one')

    deltaP=Counter(str(sp.Rational(int(x@x),2)) for x in P)
    deltaB=Counter(str(sp.Rational(int(x@x),2)) for x in B)
    mismatch=Counter(int(P[i]@P[j]) for A,c in zip(*np.nonzero(W)) for i,j in [PAIRS[c]])
    need(deltaP=={'5/2':56,'21/2':8} and deltaB=={'3':30,'7':30},'original V0 dimensions differ from Vaux')
    need(mismatch=={-18:15,-6:90,-2:225,2:150},'all original-time mediator/pair offsets nonzero')
    need(all(P[i]@Vaux@P[j]==0 for A,c in zip(*np.nonzero(W)) for i,j in [PAIRS[c]]),
         'selected Vaux restores pair scaling resonance only')
    need(all(sum(P[i]+P[j])==sum(B[A]) for A,c in zip(*np.nonzero(W)) for i,j in [PAIRS[c]]),
         'original quarter-charge term cancels from every pair energy difference')
    witness=next((i,j) for i,j in PAIRS if P[i]@(k*P[j])==2)
    need(not np.array_equal(P[witness[0]],P[witness[1]]),'noncentral mixed adjoint double-pole witness')
    # The infinite odd-dressing bound is proved analytically, not by this census.
    t=sp.symbols('t',positive=True)
    u,v=sp.symbols('u v',integer=True)
    pair_energy=((u+v)**2*t**2+(u-v)**2/t**2)/4
    need(sp.expand(4*pair_energy-(u+v)**2*t**2-(u-v)**2/t**2)==0,'boost-family exact positive-square energy formula')
    pins()
    record={'research_id':'UR.SOURCE.DRESSED_NATIVE.01','verdict':'PARTIAL',
            'mathematical_verdict':'EXACT_EQUIVARIANT_DRESSED_W; EXTERIOR_JET_INJECTION; DIRECT_NATIVE_CAR_CCR_TIME_IDENTIFICATION_FAILS',
            'source_pins':files,'checks':CHECKS,'check_count':len(CHECKS),
            'phase_equations':{'equations':2032,'rank':rank,'variables':176,'phases':signs.tolist(),
                               'root_order_doubled':[r.tolist() for r,_ in native_ops]},
            'pair_tensor':{'shape':[60,2016],'nonzero':480,'gram':'8 I60','kernel':1956,
                           'pair_exponents':census(exponents)},
            'operator_jets':{'census':census(jet_census),'cumulative_ranks_at_weights_3_4_5':grade_ranks,
                             'homogeneous_weight5_rank':grade5rank,'new_dark_directions_at_weight5':1956},
            'time':{'V0_fermion_dimensions':census(deltaP),'V0_mediator_dimensions':census(deltaB),
                    'V0_delta_b_minus_delta_i_minus_delta_j':census(mismatch),
                    'Vaux_fermion_dimension':'3/2','Vaux_mediator_dimension':'3',
                    'quarter_charge_shift_changes_pair_offsets':False,
                    'Vaux_is_source_derived':False},
            'charges':{'fermion_g':1,'mediator_g':2,'q':'q_E8-g','Y':'Y_E8-g'},
            'CAR_gate':{'same_field_adjoint_pole_order':3,'mixed_double_pole_indices':list(witness),
                        'native_bright_pair_and_mediator_independent_in_source':False},
            'physical_gates_closed':[],'complete_TFPT_solution':False,'independent_review':False}
    Path(args.output).write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'verdict':record['verdict'],'checks':len(CHECKS),'jet_ranks':grade_ranks,'output':args.output}))

if __name__=='__main__':
    main()
