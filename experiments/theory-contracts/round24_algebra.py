"""Exact source firewall and finite-block tools for NON-RH Round24."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys
import sympy as s

PINS = {
    'round23_algebra.py':'b177207b0da98eea863b8298dcd9e77b6adf90068b06f6efc774b4d37838fa58',
    'run_round23.py':'c26c9ccbc5b3f88002dd2308092ae7a3257f84ec9911d3bf626d98ee6d9260b0',
    'soft-sector-round23/PROOF.md':'88a5407a001d6f34d528689b7ebe780889c5f81dd38240c60bad5a03dc57d7c6',
    'soft-sector-round23/checker.py':'bf146477185851681cba482eea8aa411b0c680838a26d933aac807d3de7076af',
    'translation-locality-round23/PROOF.md':'6c5a575bc42242e0a3b96e104fc127161d2afabad6ad76437ab538809e5f1145',
    'round22_algebra.py':'133a11d7d873062960e685e15ce0d55dcf9baf16b59199de5846e2e27711ae5c',
    'positive-hopping-band-round22/PROOF.md':'f04800b05e2f09098211ada037e8392e598526b6620e4e2232b62219abbbc93d',
    'translation-completion-round22/PROOF.md':'248c46bf6bf7dfdc3611e6355bf58f9f99482cac52c1001f8ec37c8e113b64ac',
    'local-charge-transport-round20/PROOF.md':'6d7059cc75108be2b7262f030b83e2c14c774a950d2f1ccd0f9c5c1b3b5afb5c',
    'local-charge-transport-round20/checker.py':'e5b56b53e3fbb079947d8f420aa45cfd0190e9ac3ccca9fd42f8797a7438d234',
    'scalar-charge-energy-round20/PROOF.md':'f54190fffdf3ccc110c5a66d6da0575c7b8ad96a5a880fcb4b6c01f930ccb7b5',
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
    out=[]
    for label,name in [('r24_e8','round22_algebra.py'),('r24_osc','round23_algebra.py'),('r24_ward','free-scalar-3d/free_scalar_ward.py')]:
        spec=importlib.util.spec_from_file_location(label,root/name)
        module=importlib.util.module_from_spec(spec); sys.modules[label]=module
        spec.loader.exec_module(module); out.append(module)
    return tuple(out)


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


def neutral_bounds(count,eps=s.Rational(1,32)):
    eta=2*eps/(1-2*eps)
    mean=2*eps*(2*eta+eta**2)
    return {'J_max':eps/(24*count**2),'eps':eps,'eta':eta,
            'energy_norm':4*eps,'energy_mean':mean}


def shifted_mass2(mass2,coupling,background_energy,count):
    return mass2+2*coupling*background_energy


def source_fourth(z,w,c,v):
    return w+2*z*c+c**2+4*z*v+2*v**2


def wick(labels,cov):
    if not labels:
        return s.Integer(1)
    if len(labels)%2:
        return s.Integer(0)
    return sum(cov[labels[0],labels[j]]*wick(labels[1:j]+labels[j+1:],cov) for j in range(1,len(labels)))


def density_coefficients(number,count,mass):
    z=(2*number+1)/(2*count*mass)
    w=(6*number**2+6*number+3)/(4*count**2*mass**2)
    return z,w,w+z/mass+1/(4*mass**2),2*z/mass+1/(2*mass**2)


def spatial_stiffness(size,mass2,potential=None):
    sites=list(product(range(size),repeat=3)); index={x:i for i,x in enumerate(sites)}
    result=s.zeros(len(sites)); potential=potential or {}
    for x,i in index.items():
        result[i,i]=mass2+6+potential.get(x,0)
        for axis in range(3):
            for step in (-1,1):
                y=list(x); y[axis]=(y[axis]+step)%size
                result[i,index[tuple(y)]]-=1
    return sites,result


def gaussian_weight(determinant):
    return 1/s.sqrt(determinant)


def schur_static(A,B,C):
    inverse=B.inv()
    K=A-C*inverse*C.T
    Z=s.eye(A.rows)+C*inverse**2*C.T
    return K,Z
