"""Exact conditional charge adapter and full-potential slow-roll consistency.

No native half-charge vertex or cosmological likelihood is inferred. Symbolic
identities and finite numerical diagnostics are explicitly distinguished.
"""
from pathlib import Path
import argparse, hashlib, json, math
import numpy as np
import sympy as s
from scipy.optimize import brentq

CHECKS=[]
def need(ok,name):
    if not bool(ok): raise RuntimeError(name)
    CHECKS.append(name)

def relative_charge():
    k,l=s.symbols('k l',integer=True)
    energy=(k*k+l*l)/4
    shifted=((k+1)**2+(l-1)**2)/4
    need(s.expand((k+1+l-1)/2-(k+l)/2)==0,'opposite half-charge shifts conserve total charge')
    need(s.simplify(2*energy+1-shifted-((k-1)**2+(l+1)**2)/4)==0,
         'energy bound E_shift <= 2 E + 1 is an exact sum of squares')
    # Finite cutoffs are partial shifts, NOT bilateral unitaries. The infinite
    # unitary/adjoint assertion follows from the bijection (k,l)->(k+1,l-1).
    boundary=[]
    for cutoff in [1,2,4,8]:
        labels=[(a,b) for a in range(-cutoff,cutoff+1) for b in range(-cutoff,cutoff+1)]
        ids={x:i for i,x in enumerate(labels)};d=len(labels)
        J=np.zeros((d,d),dtype=int)
        for x,i in ids.items():
            target=(x[0]+1,x[1]-1)
            if target in ids:J[ids[target],i]=1
        q=np.diag([a+b for a,b in labels])
        ps=np.diag([(-1)**a for a,b in labels]);pt=np.diag([(-1)**(a+b) for a,b in labels])
        need(np.array_equal(q@J,J@q),'total charge commutator vanishes cutoff '+str(cutoff))
        need(np.array_equal(ps@J,-J@ps),'system parity flips cutoff '+str(cutoff))
        need(np.array_equal(pt@J,J@pt),'total parity conserved cutoff '+str(cutoff))
        need(not np.array_equal(J.T@J,np.eye(d,dtype=int)),'finite cutoff boundary is not silently called unitary '+str(cutoff))
        e=np.array([(a*a+b*b)/4 for a,b in labels])
        # Columns have one or zero nonzero entries: exact inequality entrywise.
        ep=np.sum((J*J)*e[:,None],axis=0)
        need(np.all(ep<=2*e+1),'finite partial shift satisfies energy form bound '+str(cutoff))
        boundary.append({'cutoff':cutoff,'dimension':d,'dropped_boundary_inputs':int(d-np.sum(J))})
    return {'infinite_carrier':'l2(Z) system tensor l2(Z) reference',
            'J':'|k,l> -> |k+1,l-1>', 'system_charge_unit':'k/2',
            'norm':1,'adjoint':'|k,l> -> |k-1,l+1>',
            'energy_domain_bound':'H0 J bounded by (2 H0 + I) on D(H0), H0=(k^2+l^2)/4',
            'forbidden_with_separately_even_operations':True,
            'extra_resource':'an odd-system times odd-reference interaction, not obtainable from separately parity-even accesses',
            'native_half_charge_field_constructed':False,'cutoff_controls':boundary}

def full_potential():
    y,M=s.symbols('y M',positive=True)
    # Planck units, y=exp(sqrt(2/3)*phi). Differentiate the full potential.
    V=s.Rational(3,4)*M**2*(1-1/y)**2
    diff_phi=lambda f:s.sqrt(s.Rational(2,3))*y*s.diff(f,y)
    eps=s.simplify((diff_phi(V)/V)**2/2)
    eta=s.simplify(diff_phi(diff_phi(V))/V)
    tilt=s.factor(6*eps-2*eta)
    As=s.factor(V/(24*s.pi**2*eps))
    need(s.simplify(eps-4/(3*(y-1)**2))==0,'full Starobinsky potential epsilon identity')
    need(s.simplify(eta-s.Rational(4,3)*(2-y)/(y-1)**2)==0,'full potential eta identity')
    need(s.simplify(tilt-s.Rational(8,3)*(y+1)/(y-1)**2)==0,'first-order slow-roll tilt, without large-N truncation')
    need(s.simplify(As-3*M**2*(y-1)**4/(128*s.pi**2*y**2))==0,'full potential first-order slow-roll scalar amplitude')
    need(s.factor(As*tilt**2-M**2/(6*s.pi**2)*(1+1/y)**2)==0,
         'exact full-potential As*(1-ns)^2 identity within first-order slow roll')
    need(s.factor(As*tilt**2-M**2/(6*s.pi**2))==M**2*(2*y+1)/(6*s.pi**2*y**2),
         'finite-field correction has strictly positive sign for y>1')
    c3=1/(8*math.pi);m2=c3**7
    observed_As=math.exp(3.062)*1e-10;observed_ns=.9752
    amp=lambda v:3*m2*(v-1)**4/(128*math.pi**2*v*v)
    ns=lambda v:1-(8/3)*(v+1)/(v-1)**2
    yend=1+2/math.sqrt(3)
    N=lambda v:.75*(v-yend-math.log(v/yend))
    ya=brentq(lambda v:amp(v)-observed_As,yend,1000,xtol=1e-12)
    yn=brentq(lambda v:ns(v)-observed_ns,yend,1000,xtol=1e-12)
    ratio=observed_As*(1-observed_ns)**2/(m2/(6*math.pi**2))
    need(ratio<.5,'selected ACT central combination is below the strict full-potential lower bound')
    need(abs(amp(ya)/observed_As-1)<1e-13,'numerical amplitude match verified')
    need(abs(ns(yn)-observed_ns)<1e-14,'numerical tilt match verified')
    need(ns(ya)<1-2/math.sqrt(24*math.pi**2*observed_As/m2),
         'full finite-field correction does not repair the previous large-N tilt mismatch')
    return {'approximation':'full Starobinsky potential; first-order potential slow-roll, not exact mode evolution',
            'mass_rule':'M^2/Mp^2=(1/(8*pi))^7',
            'ACT_column':'P-ACT-LB2, table 5, arXiv:2503.14452v2',
            'observed_As':observed_As,'observed_ns':observed_ns,
            'central_invariant_over_strict_lower_bound':ratio,
            'fit_As':{'y':ya,'N_slow_roll':N(ya),'ns':ns(ya),'r':64/(3*(ya-1)**2)},
            'fit_ns':{'y':yn,'N_slow_roll':N(yn),'As':amp(yn),'As_over_observed':amp(yn)/observed_As},
            'mass_squared_needed_over_compiler_mass_squared':observed_As/amp(yn),
            'central_values_simultaneously_fit':False,
            'joint_likelihood_or_exclusion_sigma_computed':False,
            'all_orders_or_general_TFPT_exclusion':False}

def run():
    out={'charge':relative_charge(),'matching':full_potential(),'count':len(CHECKS),'checks':CHECKS,
         'T1_T8_closed':[],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default=str(Path(__file__).with_suffix('.json')));a=p.parse_args()
    out=run();Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print(json.dumps(out,indent=2))
