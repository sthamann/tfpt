"""Exact original-source firewall and conservative finite-history error planner."""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import sympy as s

PINS = {
    'round25_algebra.py':'8c2424ebd59fc83b29d08b1eecc9683316aaff573e5040f5e268b234680d9d7e',
    'run_round25.py':'3d593df1203b2e8cb4505b70c9db2c7d9d8db0ec995b942f5f7eb1c7fe809136',
    'moving-history-memory-round25/PROOF.md':'a9e11a04aa359c37e38a93b00b638aa114dec4a30f6556722018543a36468375',
    'moving-history-memory-round25/checker.py':'77e5552cbd0eebbdbb9e158179245751500c3f4c8efd6f4f9e680a12f2573370',
    'history-determinant-solver-round25/PROOF.md':'721af33babf3d85a4648b7f4bad91a3b2d5944ec162f29c91c0c7bbb5bced43f',
    'history-determinant-solver-round25/checker.py':'94106706e77118227b99349904d7eb1b2a04e81a50bf8cfe2d18fea584993762',
    'round22_algebra.py':'133a11d7d873062960e685e15ce0d55dcf9baf16b59199de5846e2e27711ae5c',
    'round24_algebra.py':'74ce2b8e7f4b880e383c9d05e864d43bec1d51482b2af7d26c73f002c9ea2d9b',
    'local-charge-transport-round20/PROOF.md':'6d7059cc75108be2b7262f030b83e2c14c774a950d2f1ccd0f9c5c1b3b5afb5c',
    'local-charge-transport-round20/checker.py':'e5b56b53e3fbb079947d8f420aa45cfd0190e9ac3ccca9fd42f8797a7438d234',
    'scalar-charge-energy-round20/PROOF.md':'f54190fffdf3ccc110c5a66d6da0575c7b8ad96a5a880fcb4b6c01f930ccb7b5',
    'free-scalar-3d/free_scalar_ward.py':'6a07fde8b3c5336abac603e1979326784d9a2c451e5a5c68b4f03f9c7aed4d81',
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
    for label,name in [('r26_e8','round22_algebra.py'),('r26_scalar','round24_algebra.py'),('r26_memory','round25_algebra.py')]:
        spec=importlib.util.spec_from_file_location(label,root/name)
        module=importlib.util.module_from_spec(spec); sys.modules[label]=module
        spec.loader.exec_module(module); modules.append(module)
    return tuple(modules)


class Certificate:
    def __init__(self): self.checks=[]; self.witnesses={}
    def check(self,label,condition):
        if not bool(condition): raise AssertionError(label)
        self.checks.append(label)
    def emit(self,scope):
        print(json.dumps({'status':'PASS','exact_check_groups':len(self.checks),
            'provenance_checks':len(PINS),'checks':self.checks,'witnesses':self.witnesses,
            'pinned_inputs':PINS,'scope':scope},indent=2))


def ceil_sqrt(value):
    value=Fraction(value)
    k=math.isqrt(value.numerator//value.denominator)
    return k+int(k*k*value.denominator<value.numerator)


def charge_coercivity(count):
    return Fraction(1,62*count)


def theta_upper(time,count):
    return (1+2*ceil_sqrt(1/(Fraction(time)*charge_coercivity(count))))**(8*count)


def relative_hop_tail(theta,order,theta_bound):
    theta=Fraction(theta)
    if order<0 or order+2<=theta: raise ValueError('P>=0 and P+2>theta required')
    return theta_bound*theta**(order+1)/math.factorial(order+1)/(1-theta/(order+2))


def relative_charge_tail(beta,slices,count,J,cutoff):
    beta,J=Fraction(beta),Fraction(J); delta=beta/slices
    theta=beta*48*count*J
    exp_upper=3**math.ceil(theta)
    decay=delta*charge_coercivity(count)*(cutoff+1)**2/2
    return Fraction(exp_upper*slices*theta_upper(beta-delta/2,count),2**math.floor(decay))


def error_plan(count=27,slices=3,beta=Fraction(1),J=Fraction(1,10),tolerance=Fraction(1,100)):
    beta,J,tolerance=Fraction(beta),Fraction(J),Fraction(tolerance)
    if type(count) is not int or count<1 or type(slices) is not int or slices<3 or beta<=0 or J<0 or not 0<tolerance<1:
        raise ValueError('finite positive regulator and 0<tolerance<1 required')
    theta=beta*48*count*J; bound=theta_upper(beta,count)
    cutoff=1
    while relative_charge_tail(beta,slices,count,J,cutoff)>tolerance/2:
        cutoff*=2
    order=max(0,math.ceil(theta))
    while relative_hop_tail(theta,order,bound)>tolerance/2:
        order+=64
    charge=relative_charge_tail(beta,slices,count,J,cutoff)
    hops=relative_hop_tail(theta,order,bound)
    candidates=(2*cutoff+1)**(8*count)*sum((48*count)**r*math.comb(slices+r-1,r) for r in range(order+1))
    return {'K':cutoff,'P':order,'theta':theta,'charge_error':charge,'hop_error':hops,
            'total_error':charge+hops,'tolerance':tolerance,
            'candidate_decimal_digits_upper':1+(candidates.bit_length()*30103)//100000,
            'full_memory':True,'partition_sum_executed':False}


def relative_observable_error(rho):
    return 2*rho/(1-rho)


def trace_log_bound(epsilon,retained,slices,diagonal_green,eta):
    return epsilon*retained*slices*diagonal_green/(2*(1-eta))


def cycle_laplacian(count):
    L=2*s.eye(count)
    for j in range(count):
        L[j,(j+1)%count]-=1; L[(j+1)%count,j]-=1
    return L


def negative_word(old):
    p,r=old.UNITS[1],old.UNITS[2]
    word=[(0,1,p),(1,2,r),(1,0,p),(2,1,r)]
    initial=(old.ZERO,)*3; current=initial; phase=1; states=[]; signs=[]
    for edge in word:
        current,sign=old.move(current,edge)
        phase*=sign; signs.append(sign); states.append(current)
    return initial,word,states,signs,phase
