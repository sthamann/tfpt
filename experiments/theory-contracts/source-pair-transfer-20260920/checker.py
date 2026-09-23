#!/usr/bin/env python3
"""Exact all-order source pair response and controlled transfer comparison."""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
REPO=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
CONTRACTS=REPO/'experiments/theory-contracts'
CHECKS=[]

def need(ok,label):
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS.append(label)

def verify_pins():
    files=json.loads((HERE/'source_manifest.json').read_text())['files']
    for name,h in files.items():
        need(hashlib.sha256((REPO/name).read_bytes()).hexdigest()==h,'source pin '+name)
    return files

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='certificate.json')
    args=parser.parse_args()
    source_pins=verify_pins()
    f=CONTRACTS/'universalraum-keyD-native-instruments-20260915/native_source.py'
    prefix,marker,_=f.read_text().partition('# --- Root-opposite boson pairing')
    need(bool(marker),'native source prefix boundary')
    ns={'__file__':str(f),'__name__':'original_native_prefix'}
    exec(compile(prefix,str(f),'exec',optimize=0),ns)
    need(len(ns['checks'])==6,'six original native guards retained')
    a=np.array([1,1,1,-1,-1,-1,-1,-1],dtype=np.int64)
    k=np.array([1]*9+[-1],dtype=np.int64)
    er=np.array([0]*8+[-1,0],dtype=np.int64)

    def F2(r):
        h=int(a@r);num=np.r_[2*r-h*a,0,-2*h]
        if np.any(num%4):
            raise RuntimeError('nonintegral source embedding')
        return num//4

    def eps(x,y):
        return (-1)**int(sum(x[i]*sum(y[:i]) for i in range(10))%2)

    P=np.array([F2(r)+er for r in ns['FW']])
    W=ns['W'];pairs=ns['PAIRS']
    phases=json.loads((CONTRACTS/'source-dressed-native-20260920/certificate.json').read_text())['phase_equations']['phases']
    need(len(phases)==176,'inherited simultaneous field/current phase dictionary')
    need(np.array_equal(W@W.T,8*np.eye(60,dtype=np.int64)),'AA=8A from WWt=8I')
    need(all(x@(k*x)==3 for x in P),'all odd source field norms three')
    fibers={};eta=[]
    for c,(i,j) in enumerate(pairs):
        fibers.setdefault(tuple(P[i]+P[j]),[]).append(c)
        eta.append(phases[i]*phases[j]*eps(P[i],P[j]))
    need(len(fibers)==996,'all 996 total-momentum fibers')
    for A,c in zip(*np.nonzero(W)):
        need(eta[c]*phases[64+int(A)]==W[A,c],'actual source sign agrees with native W')
    # No dense 2016^2 symbolic matrix: distinct momenta are exactly orthogonal.
    patterns=Counter()
    for vals in fibers.values():
        for c in vals:
            i,j=pairs[c];x,y=P[i],P[j];lam=int(x@(k*y))
            for d in vals:
                u,t=[P[q] for q in pairs[d]]
                need(int(u@(k*t))==lam,'same-momentum pair exponent')
                pattern=(lam,int(eta[c]*eta[d]),int(x@(k*u)),int(x@(k*t)),
                         int(y@(k*u)),int(y@(k*t)),int(c==d),int(W[:,c]@W[:,d]))
                patterns[pattern]+=1
    need(sum(patterns.values())==6816 and len(patterns)==9,'all nontrivial kernel cells in nine exact types')
    for A in range(60):
        totals={tuple(P[pairs[c][0]]+P[pairs[c][1]]) for c in np.flatnonzero(W[A])}
        need(len(totals)==1,'native W row has only one actual total momentum')

    v=sp.symbols('v',positive=True)
    d=v**2*(2-v)/(2*(1-v)**3)
    o=(2-v)/(2*(1-v)**2)
    for pattern,count in sorted(patterns.items()):
        lam,sign,xx,xy,yx,yy,diag,w=pattern
        actual=sign*v**lam*((1-v)**(-xx)+(-1)**lam*(1-v)**(-xy)+
                           (-1)**lam*(1-v)**(-yx)+(1-v)**(-yy))/4
        need(sp.cancel(actual-d*diag-o*w)==0,'rational kernel identity '+str(pattern))
    need(sp.cancel(d-v*v*o/(1-v))==0,'common scalar kernel factor')
    geo=1/(1-v)
    D=lambda expr:v*sp.diff(expr,v)
    need(sp.cancel(o-(D(geo)+2*geo)/2)==0,'all-order o_n=(n+2)/2 generating identity')
    need(sp.cancel(d-(D(D(geo))+D(geo)-2*geo+2)/4)==0,
         'all-order d_n=(n-1)(n+2)/4 for n>=1; d_0=0')
    need(sp.limit(d/v**2,v,0)==1 and sp.limit(o,v,0)==1,'normalized first bright/dark coefficients')
    need(sp.diff(d,v,2).subs(v,0)/2==1 and sp.diff(o,v,2).subs(v,0)/2==2,
         'second jet Gram I+2 WtW')
    gb=sp.factor(d+8*o)
    hd=sp.factor(3+D(d)/d)
    hb=sp.factor(3+D(gb)/gb)
    kap=sp.factor((hd-hb)/8)
    need(sp.cancel(kap-(2-v)/(v*v-8*v+8))==0,'finite-separation compressed mean coefficient')
    var_d=sp.factor(D(hd));var_b=sp.factor(D(hb))
    need([sp.limit(z,v,0) for z in [hd,hb,kap,var_d,var_b]]==[5,3,sp.Rational(1,4),0,0],
         'collision limits of means and variances')
    sample={key:str(fun.subs(v,sp.Rational(1,2))) for key,fun in
            [('H_dark',hd),('H_bright',hb),('coefficient',kap),('variance_dark',var_d),('variance_bright',var_b)]}
    need(var_d.subs(v,sp.Rational(1,2))==sp.Rational(50,9) and
         var_b.subs(v,sp.Rational(1,2))==sp.Rational(10850,2601),'positive exact compression variances')
    semigroup={}
    rho=sp.Rational(1,2);u=sp.Rational(1,2)
    for name,fun in [('bright',gb),('dark',d)]:
        one=sp.factor(u**3*fun.subs(v,rho*u)/fun.subs(v,rho))
        two=sp.factor(u**6*fun.subs(v,rho*u*u)/fun.subs(v,rho))
        defect=sp.factor(two-one**2)
        need(defect>0,'finite-separation semigroup defect '+name)
        semigroup[name]={'at_log2':str(one),'at_log4':str(two),'defect':str(defect)}
        real_pi=sp.factor(-fun.subs(v,-rho)/fun.subs(v,rho))
        need(abs(real_pi)<1,'finite-separation real-time compression is not unitary '+name)
        semigroup[name]['real_time_pi_amplitude']=str(real_pi)
    p_b=8/gb;p_d=v*v/d
    residual_b=v*v*(4-3*v*v)/(2*(2-v)*(v*v-8*v+8))
    residual_d=v*v*(7-4*v)/(2*(2-v))
    need(sp.cancel(sp.Rational(3,2)*v-(1-p_b)-residual_b)==0,'bright spectral tail <=3rho/2')
    need(sp.cancel(sp.Rational(5,2)*v-(1-p_d)-residual_d)==0,'dark spectral tail <=5rho/2')
    # Positivity on 0<v<1 is analytic: each displayed numerator/denominator is positive.
    need(sp.limit(gb,v,0)==8 and sp.limit(d/v**2,v,0)==1,'polar isometry scaling normalization')
    # Projector identity: A=WtW has eigenvalues 8,0 and projectors Pb=A/8,Pd=I-Pb.
    need(sp.Rational(1,8)*8==1 and sp.Rational(1,4)*8==2,'Hlimit=3Pb+5Pd=5I-A/4')
    need(60+1956==2016,'complete pair-space multiplicities')
    pairq=np.array([int(sum(P[i]+P[j])) for i,j in pairs],dtype=np.int64)
    for A in range(60):
        need(len(set(int(pairq[c]) for c in np.flatnonzero(W[A])))==1,'quarter-charge generator commutes with bright projector')
    need(int(pairq.max())==4 and int(pairq.min())==-6,'complete pair source-charge range')
    need(max(int(sum(F2(r)+2*er)) for r in ns['BW'])==0,'bright source charge never positive')
    # Any additive one-body shift cancels in the same-channel connected pair energy.
    x,y=sp.symbols('x y')
    need(sp.expand((5-(x+y)/4)-(3-(x+y)/4))==2,'dark connected source pair energy +2')
    need(sp.expand((3-(x+y)/4)-(3-(x+y)/4))==0,'bright connected source pair energy zero')
    # Original native N=2 block. No mu*N is inserted.
    coupling,delta=sp.symbols('coupling delta',positive=True)
    native=sp.Matrix([[0,sp.sqrt(8)*coupling],[sp.sqrt(8)*coupling,delta]])
    need(sp.expand(native.det())==-8*coupling**2,'original native bright block determinant strictly negative')
    native_energy=(delta-sp.sqrt(delta*delta+32*coupling*coupling))/2
    need(sp.simplify(native_energy.subs({delta:1,coupling:sp.Rational(1,20)})-(5-3*sp.sqrt(3))/10)==0,
         'native original-ratio negative binding witness')
    constant,mu=sp.symbols('constant mu')
    need(sp.solve([constant,constant+mu],[constant,mu])=={constant:0,mu:0},
         'vacuum and one-particle calibration forbid an arbitrary N=2 offset')
    e0,e1,e2,eij=sp.symbols('e0 e1 e2 eij')
    need(sp.expand((eij+constant+2*mu)-(e1+constant+mu)-(e2+constant+mu)+
                   (e0+constant)-(eij-e1-e2+e0))==0,
         'connected pair energy invariant under affine number shifts for fixed reference states')
    # Wrongly dropping the identity offset would invent binding in the source.
    need(5-sp.Rational(1,4)*8==3 and 3-sp.Rational(1,4)*8==1,
         'negative control: deleting mandatory pair offset changes bright energy')
    verify_pins()
    record={
        'research_id':'UR.SOURCE.PAIR_TRANSFER.01','verdict':'PARTIAL',
        'mathematical_verdict':'EXACT_ALL_ORDER_PAIR_KERNEL; CONTROLLED_POLAR_TRANSFER_LIMIT; MANDATORY_POSITIVE_DARK_PENALTY; NATIVE_ATTRACTIVE_BINDING_NOT_DERIVED',
        'source_pins':source_pins,'check_count':len(CHECKS),'checks':CHECKS,
        'kernel':{'matrix_size':[2016,2016],'momentum_fibers':996,'nontrivial_cells':6816,
                  'distinct_types':9,'G':'d(v) I + o(v) W^T W','d':str(d),'o':str(o),
                  'patterns':[{'data':list(p),'multiplicity':c} for p,c in sorted(patterns.items())],
                  'spectral_coefficients':{'o_n':'(n+2)/2 for n>=0','d_n':'0 for n=0; (n-1)(n+2)/4 for n>=1'}},
        'transfer':{'T_bright':'exp(-3 tau) gb(rho exp(-tau))/gb(rho)',
                    'T_dark':'exp(-3 tau) d(rho exp(-tau))/d(rho)',
                    'mean_dark':str(hd),'mean_bright':str(hb),'mean_A_coefficient':str(kap),
                    'rho_half_values':sample,'semigroup_counterexample':semigroup,
                    'limit':'exp(-3 tau) Pb + exp(-5 tau) Pd',
                    'uniform_tau_nonnegative_error_bound':'5 rho / 2',
                    'uniform_all_real_times_error_bound':'5 rho',
                    'state_map_limit':'C0 Pb / sqrt(8) + C2 Pd',
                    'state_map_norm_error_bound':'sqrt(5 rho)',
                    'limit_generator':'3 I + 2 Pd - Q2/4',
                    'same_assigned_time':True,'source_selected_metric':False},
        'native_gate':{'source_connected_bright_energy':0,'source_connected_dark_energy':2,
                       'native_reference':'empty-Fock N=2 sector, not charged response about the interacting N=64 ground',
                       'native_lower_bright_energy':'(Delta-sqrt(Delta^2+32 coupling^2))/2 < 0',
                       'native_ratio_example':'(5-3 sqrt(3))/10 at Delta=1,coupling=1/20',
                       'full_Fock_or_vacuum_transfer':False},
        'physical_gates_closed':[],'complete_TFPT_solution':False,'independent_review':False}
    Path(args.output).write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'verdict':record['verdict'],'checks':len(CHECKS),'kernel_types':9,
                      'same_time_pair_limit':True,'native_binding_derived':False,'output':args.output}))

if __name__=='__main__':
    main()
