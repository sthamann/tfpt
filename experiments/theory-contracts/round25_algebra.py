"""Pinned original-model inputs and exact finite-history Gaussian algorithms."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import sympy as s

PINS = {
    'round24_algebra.py':'74ce2b8e7f4b880e383c9d05e864d43bec1d51482b2af7d26c73f002c9ea2d9b',
    'run_round24.py':'153e1302b883ef3c97e5380d028c4a89eff68737888d2e2169064e822bb39eae',
    'local-gaussian-elimination-round24/PROOF.md':'7f2fecf8f6aee19baa1bdd0aab812690041bc22d793550fe418ec9d4a46a5b8e',
    'local-gaussian-elimination-round24/checker.py':'11611f1e3429158b1dcdb6c65807626324709551b5ec69e2b609c264ce57ba3d',
    'finite-density-background-round24/PROOF.md':'0e1ab3d75772d1a92bd432450b44478216a50245282ed3934d2783532e63d72e',
    'finite-density-background-round24/checker.py':'72dcb16d3f4c9a256a513d7d41df9cf95064d0b38a708fe60e22d7f7c2d8614d',
    'round22_algebra.py':'133a11d7d873062960e685e15ce0d55dcf9baf16b59199de5846e2e27711ae5c',
    'local-charge-transport-round20/PROOF.md':'6d7059cc75108be2b7262f030b83e2c14c774a950d2f1ccd0f9c5c1b3b5afb5c',
    'free-scalar-3d/free_scalar_ward.py':'6a07fde8b3c5336abac603e1979326784d9a2c451e5a5c68b4f03f9c7aed4d81',
    'local-parent-round15/PROOF.md':'e5264468f3f3c87ab35f37205cc65370f3639e0c2d34b73399b82cb50b0cccbb',
}


def inputs():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input-root',type=Path,default=Path(__file__).resolve().parent)
    root=parser.parse_args().input_root
    for name,expected in PINS.items():
        path=root/name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
            raise ValueError('pinned input missing or changed: '+name)
    modules=[]
    for label,name in [('r25_e8','round22_algebra.py'),('r25_local','round24_algebra.py')]:
        spec=importlib.util.spec_from_file_location(label,root/name)
        module=importlib.util.module_from_spec(spec); sys.modules[label]=module
        spec.loader.exec_module(module); modules.append(module)
    return tuple(modules)


class Certificate:
    def __init__(self):
        self.checks=[]; self.witnesses={}
    def check(self,label,condition):
        if not bool(condition):
            raise AssertionError(label)
        self.checks.append(label)
    def emit(self,scope):
        print(json.dumps({'status':'PASS','exact_check_groups':len(self.checks),
            'provenance_checks':len(PINS),'checks':self.checks,'witnesses':self.witnesses,
            'pinned_inputs':PINS,'scope':scope},indent=2))


def temporal_green(q,delta,count,separation):
    r=separation % count
    sinh=(1/q-q)/2
    return delta*(q**r+q**(count-r))/(2*sinh*(1-q**count))


def memory_tail(q,delta,count,radius):
    if type(count) is not int or count<3 or type(radius) is not int or radius<0:
        raise ValueError('T>=3 and integer R>=0 required')
    if radius>=count//2:
        return s.Integer(0)
    sinh=(1/q-q)/2
    return delta*q**(radius+1)/(sinh*(1-q)*(1-q**count))


def kernel_error(delta,coupling_norm,tail):
    return delta**2*coupling_norm**2*tail


def mixed_logdet_response(inverse,i,k,delta):
    return -delta**2*inverse[i,k]*inverse[k,i]


def memory_mask(G,block_size,count,radius):
    out=G.copy()
    for j in range(count):
        for k in range(count):
            distance=min(abs(j-k),count-abs(j-k))
            if distance>radius:
                out[j*block_size:(j+1)*block_size,k*block_size:(k+1)*block_size]=s.zeros(block_size)
    return out


def physical_blocks(old,local,count):
    """An actual root hop, with neutral compensator on a retained site."""
    sites,full=local.spatial_stiffness(3,s.Integer(1))
    F=[i for i,x in enumerate(sites) if all(a!=0 for a in x)]
    S=[i for i in range(27) if i not in F]
    base=full.extract(F,F); C=full.extract(S,F)
    p=old.UNITS[1]; two=tuple(2*a for a in p)
    initial=(two,old.ZERO,tuple(-a for a in two))
    moved,phase=old.move(initial,(0,1,p))
    blocks=[]
    for j in range(count):
        profile=initial if j%2==0 else moved
        block=base.copy()
        block[0,0]+=2*old.energy(profile[0])
        block[4,4]+=2*old.energy(profile[1])
        blocks.append(block)
    return blocks,C,initial,moved,phase


class CycleSolver:
    """Exact block LDL plus rank-2d periodic correction; B_j must be positive."""
    def __init__(self,blocks,delta):
        self.delta=s.sympify(delta)
        if len(blocks)<3 or self.delta.is_positive is not True:
            raise ValueError('positive delta and at least three time slices required')
        self.count=len(blocks); self.width=blocks[0].rows
        d=self.width; self.t=1/self.delta
        if d<1 or any(B.shape!=(d,d) or B!=B.T for B in blocks):
            raise ValueError('equal-size real symmetric spatial blocks required')
        self.pivots=[]; self.inverses=[]
        for B in blocks:
            pivot=2*self.t*s.eye(d)+self.delta*B
            if self.inverses:
                pivot-=self.t**2*self.inverses[-1]
            self.pivots.append(pivot); self.inverses.append(pivot.inv())
        self.U=s.zeros(self.count*d,2*d)
        self.U[:d,:d]=s.eye(d); self.U[-d:,d:]=s.eye(d)
        self.R=s.zeros(2*d)
        self.R[:d,d:]=-self.t*s.eye(d); self.R[d:,:d]=-self.t*s.eye(d)
        self.F=self.open_solve(self.U)
        self.H=s.eye(2*d)+self.R*self.U.T*self.F
        self.H_inverse=self.H.inv()
        self.determinant=s.prod(P.det() for P in self.pivots)*self.H.det()

    def open_solve(self,rhs):
        d=self.width
        if rhs.rows!=self.count*d:
            raise ValueError('right-hand-side row count does not match history')
        y=[]
        for j in range(self.count):
            part=rhs[j*d:(j+1)*d,:]
            if j:
                part+=self.t*self.inverses[j-1]*y[-1]
            y.append(part)
        x=[self.inverses[j]*y[j] for j in range(self.count)]
        for j in reversed(range(self.count-1)):
            x[j]+=self.t*self.inverses[j]*x[j+1]
        return s.Matrix.vstack(*x)

    def solve(self,rhs):
        open_result=self.open_solve(rhs)
        return open_result-self.F*self.H_inverse*self.R*self.U.T*open_result

    def update_ratio(self,coordinates,diagonal_changes):
        if len(coordinates)!=len(diagonal_changes) or len(set(coordinates))!=len(coordinates):
            raise ValueError('one signed update for each distinct coordinate required')
        E=s.zeros(self.count*self.width,len(coordinates))
        for j,coordinate in enumerate(coordinates):
            E[coordinate,j]=1
        V=s.diag(*diagonal_changes)
        return (s.eye(len(coordinates))+V*E.T*self.solve(E)).det()
