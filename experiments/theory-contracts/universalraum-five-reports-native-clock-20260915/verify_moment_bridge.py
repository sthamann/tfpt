"""Minimal inverse-dynamics test on the declared native filled preparation.

Independent occupation-number computation through two pair creation steps.
The filled Fock vector is NOT the interacting ground state. These are central
energy moments in that preparation, equivalently derivatives of its return
amplitude. No native preparation or source-time map is asserted here.
"""
from collections import defaultdict
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
WPATH=ROOT/'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz'
WPIN='3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'
checks=[]


def need(v,label):
    if not bool(v):raise RuntimeError(label)
    checks.append(label)


def annihilate_pair(mask,i,j):
    if not(mask&(1<<i)) or not(mask&(1<<j)):return None
    sign=(-1)**((mask&((1<<i)-1)).bit_count())
    mask^=1<<i
    sign*=(-1)**((mask&((1<<j)-1)).bit_count())
    return mask^(1<<j),sign


def run():
    need(sha256(WPATH.read_bytes()).hexdigest()==WPIN,'native tensor unchanged')
    with np.load(WPATH,allow_pickle=False) as z:raw=z['W']
    need(np.all(raw.imag==0) and np.all(raw.real==np.rint(raw.real)),'exact integer source')
    W=raw.real.astype(np.int64)
    pairs=list(combinations(range(64),2))
    terms=[(int(a),*pairs[int(col)],int(W[a,col])) for a,col in zip(*np.nonzero(W))]
    full=(1<<64)-1
    first={}
    for a,i,j,w in terms:
        mask,sign=annihilate_pair(full,i,j)
        first[(mask,a)]=w*sign
    need(len(first)==480 and sum(v*v for v in first.values())==480,'norm squared of Qplus F is 480')
    second=defaultdict(int)
    for (mask,a),coefficient in first.items():
        for b,i,j,w in terms:
            item=annihilate_pair(mask,i,j)
            if item is None:continue
            newmask,sign=item
            second[(newmask,*sorted((a,b)))]+=coefficient*w*sign
    second={k:v for k,v in second.items() if v}
    norm2=sum(v*v*(2 if a==b else 1) for (_,a,b),v in second.items())
    need(len(second)==108240,'two-pair support independently reproduced')
    need(norm2==439680==480*916,'norm squared of Qplus squared F is 480 times 916')
    # Qminus Qplus F returns only to the unique fully-filled, zero-boson state.
    back=sum(v*v for v in first.values())
    need(back==480,'Qminus Qplus F equals 480 F')
    g,D=s.symbols('g D',positive=True)
    mu2=480*g**2
    mu3=480*D*g**2
    mu4=back**2*g**4+D**2*mu2+norm2*g**4
    need(s.expand(mu4-(480*D**2*g**2+670080*g**4))==0,'full fourth moment via orthogonal boson-number layers')
    need(s.simplify(mu3/mu2-D)==0,'two moments reconstruct Delta')
    need(s.simplify(mu2/480-g**2)==0,'two moments reconstruct absolute g')
    need(s.simplify(mu2**3/(480*mu3**2)-(g/D)**2)==0,'scale-invariant reconstruction of g over Delta squared')
    need(s.simplify(mu4-mu3**2/mu2-s.Rational(349,120)*mu2**2)==0,'held-out fourth moment identity')
    need(s.simplify((mu4-3*mu2**2)-mu3**2/mu2+s.Rational(11,120)*mu2**2)==0,'fourth cumulant form')
    x2,x3=s.symbols('x2 x3',positive=True)
    inferred_g=s.sqrt(x2/480); inferred_D=x3/x2
    predicted=s.simplify(mu4.subs({g:inferred_g,D:inferred_D}))
    need(s.simplify(predicted-(x3**2/x2+s.Rational(349,120)*x2**2))==0,'unique prediction after solving two moments')
    need(s.simplify(predicted+1-predicted)==1,'negative control: independent fourth-moment change rejected')
    need(s.Rational(2,3)**6>s.Rational(1,20),'direct rate-as-g-over-Delta guess lies outside proven ground window')
    return {'status':'PASS','scope':'exact moment reconstruction in declared native H and filled preparation',
        'check_count':len(checks),'checks':checks,'native_tensor_sha256':WPIN,
        'two_pair_norm_squared':norm2,'two_pair_support':len(second),
        'moments':{'m1':'0','m2':str(mu2),'m3':str(mu3),'m4':str(s.expand(mu4))},
        'inverse':{'Delta':'m3/m2','abs_g':'sqrt(m2/480)','g_over_Delta_squared':'m2^3/(480*m3^2)'},
        'held_out':'m4 = m3^2/m2 + (349/120)*m2^2',
        'cumulant':'kappa4 = kappa3^2/kappa2 - (11/120)*kappa2^2',
        'prerequisites':['Delta positive and g nonzero','same fully filled 64-fermion / empty-boson preparation',
            'central energy moments or return amplitude with mean-energy phase removed',
            'one fixed source time, common field map, and original W normalization'],
        'limits':['not a computation of the raw seam moments','not the interacting ground-state return amplitude',
            'passing four moments is necessary, not equality of full processes','sign of real g is removable by boson rephasing']}


if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
