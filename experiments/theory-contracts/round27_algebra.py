"""Full-reference finite-regulator error budgets; exact integers/rationals only."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

PINS = {
    "round25_algebra.py": "8c2424ebd59fc83b29d08b1eecc9683316aaff573e5040f5e268b234680d9d7e",
    "run_round25.py": "3d593df1203b2e8cb4505b70c9db2c7d9d8db0ec995b942f5f7eb1c7fe809136",
    "moving-history-memory-round25/PROOF.md": "a9e11a04aa359c37e38a93b00b638aa114dec4a30f6556722018543a36468375",
    "moving-history-memory-round25/checker.py": "77e5552cbd0eebbdbb9e158179245751500c3f4c8efd6f4f9e680a12f2573370",
    "history-determinant-solver-round25/PROOF.md": "721af33babf3d85a4648b7f4bad91a3b2d5944ec162f29c91c0c7bbb5bced43f",
    "history-determinant-solver-round25/checker.py": "94106706e77118227b99349904d7eb1b2a04e81a50bf8cfe2d18fea584993762",
    "round22_algebra.py": "133a11d7d873062960e685e15ce0d55dcf9baf16b59199de5846e2e27711ae5c",
    "round24_algebra.py": "74ce2b8e7f4b880e383c9d05e864d43bec1d51482b2af7d26c73f002c9ea2d9b",
    "local-charge-transport-round20/PROOF.md": "6d7059cc75108be2b7262f030b83e2c14c774a950d2f1ccd0f9c5c1b3b5afb5c",
    "local-charge-transport-round20/checker.py": "e5b56b53e3fbb079947d8f420aa45cfd0190e9ac3ccca9fd42f8797a7438d234",
    "scalar-charge-energy-round20/PROOF.md": "f54190fffdf3ccc110c5a66d6da0575c7b8ad96a5a880fcb4b6c01f930ccb7b5",
    "free-scalar-3d/free_scalar_ward.py": "6a07fde8b3c5336abac603e1979326784d9a2c451e5a5c68b4f03f9c7aed4d81",
    "round26_algebra.py": "616f8b40697f92b0f8494730c035cf708d2768348aabf99774f521112a980e53",
    "run_round26.py": "ab3a1a917f6f819d68e9474d04093da7390d315ac53090c9b4b7ae2150327ef5",
    "history-sum-control-round26/PROOF.md": "cd1ea78abaeabd0073fa20e290aebe4599d4a1895552f23d9ef3843064cb6647",
    "history-sum-control-round26/checker.py": "771396595f191df187072cf239d733116f8268d78d020d25195f1a1f348ce653",
    "cocycle-sign-obstruction-round26/PROOF.md": "bfdb5885f6b96889e84d80fcd60e77ee49460761a7616e116f82c31299d90e4b",
    "cocycle-sign-obstruction-round26/checker.py": "3b5859539374581d3eebc09d47dab0dd9324ad73e66d78368d412c78ac568d2a"
}

def inputs():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input-root',type=Path,default=Path(__file__).resolve().parent)
    root=parser.parse_args().input_root
    for name,expected in PINS.items():
        path=root/name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
            raise ValueError('pinned input missing or changed: '+name)
    loaded=[]
    for label,name in [('r27_previous','round26_algebra.py'),('r27_e8','round22_algebra.py')]:
        spec=importlib.util.spec_from_file_location(label,root/name)
        module=importlib.util.module_from_spec(spec); sys.modules[label]=module
        spec.loader.exec_module(module); loaded.append(module)
    return tuple(loaded)

class Certificate:
    def __init__(self): self.checks=[]; self.witnesses={}
    def check(self,label,condition):
        if not bool(condition): raise AssertionError(label)
        self.checks.append(label)
    def emit(self,scope):
        print(json.dumps({'status':'PASS','exact_check_groups':len(self.checks),
            'provenance_checks':len(PINS),'checks':self.checks,'witnesses':self.witnesses,
            'pinned_inputs':PINS,'scope':scope},indent=2))

def ceil_root(value,degree):
    if type(value) is not int or value<0 or type(degree) is not int or degree<1:
        raise ValueError('nonnegative integer and positive integer degree required')
    lo,hi=0,1 << ((value.bit_length()+degree-1)//degree)
    while lo<hi:
        mid=(lo+hi)//2
        if mid**degree>=value: hi=mid
        else: lo=mid+1
    return lo

def first_true(predicate):
    lo,hi=0,1
    while not predicate(hi): lo,hi=hi,2*hi
    if predicate(0): return 0
    while lo+1<hi:
        mid=(lo+hi)//2
        if predicate(mid): hi=mid
        else: lo=mid
    return hi

def pinch(matrix,block_size):
    return matrix.applyfunc(lambda _: 0).__class__(matrix.rows,matrix.cols,
        lambda i,j: matrix[i,j] if i//block_size==j//block_size else 0)

def word_trace(C,words,projector=None):
    result=C**0
    for j,U in enumerate(words):
        result=result*U*(projector if j==0 and projector is not None else C**0)*C
    return result.trace()

def theta_upper(time,count):
    inv=1/(F(time)*F(1,62*count))
    k=math.isqrt(inv.numerator//inv.denominator)
    k+=int(k*k<inv)
    return (1+2*k)**(8*count)

def relative_hop_tail(theta,order):
    theta=F(theta)
    if theta<0 or type(order) is not int or order<0 or order+2<=theta:
        raise ValueError('theta>=0, P>=0 and P+2>theta required')
    return theta**(order+1)/math.factorial(order+1)/(1-theta/(order+2))

def relative_charge_tail(beta,slices,count,J,cutoff):
    beta,J=F(beta),F(J); delta=beta/slices
    theta=beta*48*count*J
    root=ceil_root(theta_upper(beta/2,count),slices)
    decay=delta*F(1,62*count)*(cutoff+1)**2/2
    return F(3**math.ceil(theta)*slices*root,2**math.floor(decay))

def memory_relative_error(B,theta):
    B,theta=F(B),F(theta)
    if not 0<=B<1 or theta<0:
        raise ValueError('0<=B<1 and theta>=0 required')
    return 3**math.ceil(theta)*B/(1-B)

def error_plan(count=27,slices=3,beta=F(1),J=F(1,10),tolerance=F(1,100),memory_error=F(0)):
    beta,J,tolerance,memory_error=map(F,(beta,J,tolerance,memory_error))
    if (type(count) is not int or count<1 or type(slices) is not int or slices<3
        or beta<=0 or J<0 or not 0<=memory_error<tolerance<1):
        raise ValueError('finite positive regulator and memory_error<tolerance<1 required')
    theta=beta*48*count*J; allowance=(tolerance-memory_error)/2
    K=first_true(lambda k: relative_charge_tail(beta,slices,count,J,k)<=allowance)
    P=first_true(lambda p: p+2>theta and relative_hop_tail(theta,p)<=allowance)
    charge=relative_charge_tail(beta,slices,count,J,K); hops=relative_hop_tail(theta,P)
    candidates=(2*K+1)**(8*count)*sum((48*count)**r*math.comb(slices+r-1,r) for r in range(P+1))
    return {'K':K,'P':P,'theta':theta,'charge_error':charge,'hop_error':hops,
            'memory_error':memory_error,'total_error':charge+hops+memory_error,
            'tolerance':tolerance,'tail_allowance':allowance,
            'candidate_decimal_digits_upper':1+(candidates.bit_length()*30103)//100000,
            'full_memory':memory_error==0,'partition_sum_executed':False}

def memory_witness(radius):
    if type(radius) is not int or not 0<=radius<=16:
        raise ValueError('integer radius in [0,16] required')
    delta=F(3,4); slices=33; count=729; retained=513
    q=F(1,4); qm=F(1,2); mass2=F(1); theta=F(1)
    sinh=(1/q-q)/2
    tail=F(0) if radius==slices//2 else delta*q**(radius+1)/(sinh*(1-q)*(1-q**slices))
    epsilon=delta**2*36*tail
    eta=epsilon/(delta*mass2)
    gm=delta/(1/qm-qm)*(1+qm**slices)/(1-qm**slices)
    B=epsilon*retained*slices*gm/(2*(1-eta)) if eta<1 else None
    relative=memory_relative_error(B,theta) if B is not None and B<1 else None
    return {'L':9,'N':count,'ell':3,'retained':retained,'T':slices,
            'delta':delta,'beta':delta*slices,'J':1/(delta*slices*48*count),
            'm_squared':mass2,'cell_gap':F(4),'q_gap':q,'q_mass_lower':qm,
            'R':radius,'epsilon':epsilon,'eta':eta,'B':B,'memory_error':relative,
            'exact_fast_determinant_retained':True}
