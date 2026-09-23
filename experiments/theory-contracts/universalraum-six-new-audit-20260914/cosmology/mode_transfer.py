"""Fixed-mass exact-background and linear scalar/tensor perturbation transfer.

Numerical convergence, not interval certification or a joint data likelihood.
Equations: arXiv:2510.18656v1 Appendix C; amplitudes evaluated after freeze-out.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
C3 = 1/(8*math.pi)
M2 = C3**7
B = math.sqrt(2/3)
AS_TARGET = math.exp(3.062)*1e-10
NS_TARGET = .9752
CHECKS=[]


def need(value,label):
    if not bool(value):
        raise RuntimeError(label)
    CHECKS.append(label)


def potential(phi):
    z=math.exp(-B*phi)
    V=.75*M2*(1-z)**2
    vp=1.5*M2*B*z*(1-z)
    vpp=1.5*M2*B*B*(-z+2*z*z)
    return V,vp,vpp


class Background:
    def __init__(self,phi_initial=6.5,velocity_factor=1.,rtol=2e-12,atol=2e-14):
        V,vp,_=potential(phi_initial)
        def rhs(n,y):
            phi,p=y
            V,vp,_=potential(phi)
            return [p,-(3-p*p/2)*(p+vp/V)]
        def end(n,y):
            return y[1]**2/2-1
        end.terminal=True
        end.direction=1
        sol=solve_ivp(rhs,[0,300],[phi_initial,-velocity_factor*vp/V],
                      events=end,dense_output=True,method='DOP853',rtol=rtol,atol=atol,max_step=.1)
        need(sol.success and len(sol.t_events[0])==1,'background reaches epsilon_H=1 '+str((phi_initial,velocity_factor)))
        self.sol=sol
        self.end=float(sol.t_events[0][0])
        self.initial=phi_initial
        self.factor=velocity_factor
        self.options={'rtol':rtol,'atol':atol}

    def at(self,n):
        phi,p=self.sol.sol(n)
        phi=float(phi);p=float(p)
        V,vp,vpp=potential(phi)
        eps=p*p/2
        H=math.sqrt(V/(3-eps))
        F=-(3-eps)*(p+vp/V)
        m=vpp/H**2-p**4/2+2*p*vp/H**2+3*p*p
        return phi,p,eps,H,F,m


def mode(bg,Nstar,lnkratio=0.,start_ratio=300.,rtol=2e-10,atol=2e-12,
         freeze_efolds=12.,independent_curvature=False):
    pivot=bg.end-Nstar
    ph,p,ep,Hstar,_,_=bg.at(pivot)
    k=Hstar*math.exp(lnkratio)
    def ratio(n):
        return k*math.exp(pivot-n)/bg.at(n)[3]
    n0=brentq(lambda n:math.log(ratio(n)/start_ratio),pivot-15,pivot+1,xtol=1e-12)
    nend=pivot+freeze_efolds
    if n0<10 or nend>=bg.end:
        raise RuntimeError('mode outside settled inflationary background')
    a0=math.exp(n0-pivot)
    _,p0,eps0,H0,F0,_=bg.at(n0)
    # q=a_start*sqrt(2k)*Q; irrelevant common phase set to one.
    initial=[1+0j,-1-1j*start_ratio,1+0j,-1-1j*start_ratio]
    if independent_curvature:
        initial += [1/p0,(-1-1j*start_ratio)/p0-F0/p0**2]
    def rhs(n,y):
        _,p,eps,H,F,m=bg.at(n)
        x=k*math.exp(pivot-n)/H
        out=[y[1],-(3-eps)*y[1]-(x*x+m)*y[0],
             y[3],-(3-eps)*y[3]-x*x*y[2]]
        if independent_curvature:
            out += [y[5],-(3-eps+2*F/p)*y[5]-x*x*y[4]]
        return out
    sol=solve_ivp(rhs,[n0,nend],np.array(initial,dtype=complex),method='DOP853',
                  dense_output=True,rtol=rtol,atol=atol,max_step=.1)
    if not sol.success:
        raise RuntimeError(sol.message)
    def spectra(n):
        yy=sol.sol(n)
        p=bg.at(n)[1]
        pref=k*k/(4*math.pi**2*a0*a0)
        As=pref*abs(yy[0]/p)**2
        Pt=8*pref*abs(yy[2])**2
        return float(As),float(Pt),float(Pt/As)
    As,Pt,r=spectra(nend)
    As10,Pt10,_=spectra(pivot+10)
    yc=sol.sol(pivot)
    W=yc[0]*yc[1].conjugate()-yc[0].conjugate()*yc[1]
    Wtarget=2j*start_ratio*math.exp(-3*(pivot-n0))*H0/Hstar
    out={'Nstar':float(Nstar),'ln_k_ratio':lnkratio,'phi_star':ph,'epsilon_H_star':ep,
         'Hstar':Hstar,'As':As,'Pt':Pt,'r':r,'BD_k_over_aH':start_ratio,
         'background_burn_in_efolds':n0,'mode_start_before_pivot_efolds':pivot-n0,
         'rtol':rtol,'atol':atol,'nfev':sol.nfev,
         'scalar_freeze_relative_10_to_12':As/As10-1,
         'tensor_freeze_relative_10_to_12':Pt/Pt10-1,
         'scalar_wronskian_relative_at_pivot':float(abs(W/Wtarget-1)),
         'scalar_horizon_amplitude_over_final':spectra(pivot)[0]/As,
         'curvature_equation_relative_difference':None}
    if independent_curvature:
        pref=k*k/(4*math.pi**2*a0*a0)
        AR=float(pref*abs(sol.y[4,-1])**2)
        out['curvature_equation_relative_difference']=AR/As-1
    return out


def observables(bg,Nstar,dk=.02,**options):
    ms=[mode(bg,Nstar,x,**options) for x in [-dk,0.,dk]]
    ns=1+(math.log(ms[2]['As'])-math.log(ms[0]['As']))/(2*dk)
    return {'Nstar':float(Nstar),'As':ms[1]['As'],'ns':ns,'r':ms[1]['r'],
            'log_k_derivative_step':dk,'central_mode':ms[1],'adjacent_modes':[ms[0],ms[2]]}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=HERE/'verification.json')
    ap.add_argument('--quick',action='store_true')
    args=ap.parse_args()
    bg=Background()
    baseline={'start_ratio':300.,'rtol':2e-10,'atol':2e-12}
    Nfit=brentq(lambda N:math.log(mode(bg,N,**baseline)['As']/AS_TARGET),45,65,xtol=2e-7)
    amp=observables(bg,Nfit,**baseline)
    print('Amplitude-matched preliminary:',json.dumps({k:amp[k] for k in ['Nstar','As','ns','r']}),flush=True)
    tests={}
    tests['earlier_BD_1000']=observables(bg,Nfit,start_ratio=1000.,rtol=2e-10,atol=2e-12)
    tests['tighter_tolerance']=observables(bg,Nfit,start_ratio=300.,rtol=2e-12,atol=2e-14)
    tests['earlier_BD_and_tighter']=observables(bg,Nfit,start_ratio=1000.,rtol=2e-12,atol=2e-14)
    tests['earlier_BD_3000']=observables(bg,Nfit,start_ratio=3000.,rtol=2e-12,atol=2e-14)
    print('Independent BD/tolerance runs complete',flush=True)
    accurate={'start_ratio':3000.,'rtol':2e-12,'atol':2e-14}
    # Refine amplitude pivot only; the fixed mass is never varied.
    Nprec=brentq(lambda N:math.log(mode(bg,N,**accurate)['As']/AS_TARGET),Nfit-.02,Nfit+.02,xtol=2e-8)
    amp_prec=observables(bg,Nprec,**accurate)
    tests['half_derivative_step']=observables(bg,Nprec,dk=.01,**accurate)
    curvature=mode(bg,Nprec,independent_curvature=True,**accurate)
    # Earlier background and deliberately changed initial velocity: same attractor.
    bg2=Background(phi_initial=6.7,velocity_factor=.5,rtol=2e-13,atol=2e-15)
    tests['earlier_background_different_velocity']=observables(bg2,Nprec,**accurate)
    tilt=None
    if not args.quick:
        Nt=brentq(lambda N:observables(bg,N,**baseline)['ns']-NS_TARGET,65,95,xtol=3e-5)
        tilt=observables(bg,Nt,**accurate)
        tilt['As_over_target']=tilt['As']/AS_TARGET
        print('Tilt-matched:',json.dumps({k:tilt[k] for k in ['Nstar','As','ns','r','As_over_target']}),flush=True)
    need(abs(amp_prec['As']/AS_TARGET-1)<1e-8,'fixed-mass amplitude pivot meets target numerically')
    need(amp_prec['ns']<NS_TARGET-.009,'full mode transfer does not close target tilt discrepancy')
    need(abs(curvature['curvature_equation_relative_difference'])<2e-8,'Q and independent curvature equations agree')
    for label,result in [('final',amp_prec)]+list(tests.items()):
        c=result['central_mode']
        need(abs(c['scalar_freeze_relative_10_to_12'])<1e-7,'scalar freezes beyond horizon '+label)
        need(abs(c['tensor_freeze_relative_10_to_12'])<1e-7,'tensor freezes beyond horizon '+label)
        need(c['scalar_wronskian_relative_at_pivot']<3e-6,'canonical scalar Wronskian preserved '+label)
    out={'status':'NUMERICAL_FULL_BACKGROUND_AND_LINEAR_MODE_TRANSFER',
         'model':{'V':'3M^2(1-exp(-sqrt(2/3)*phi))^2/4','c3':C3,'M2':M2,'M':math.sqrt(M2),
                  'units':'reduced Mp=hbar=1','mass_fitted':False},
         'data_target':{'As':AS_TARGET,'ns':NS_TARGET,'ACT_column':'table 5 P-ACT-LB2',
                        'url':'https://arxiv.org/pdf/2503.14452v2'},
         'background':{'end_N_from_initial':bg.end,'end_phi':bg.at(bg.end)[0],
                       'end_epsilon_H':bg.at(bg.end)[2],'phi_initial':bg.initial,
                       'velocity_factor':bg.factor,'settings':bg.options},
         'amplitude_match_baseline':amp,'amplitude_match_refined':amp_prec,
         'convergence_at_reported_pivots':tests,'independent_curvature_check':curvature,
         'tilt_match':tilt,'checks':CHECKS,'count':len(CHECKS),
         'scope':{'exact_background_equations':True,'linear_modes_numerically_integrated':True,
                  'potential_slow_roll_used_for_observables':False,'BD_infinite_past_certified':False,
                  'interval_certificate':False,'likelihood_computed':False,'reheating_matched_to_observed_k':False,
                  'loop_or_nonlinear_perturbation_corrections_included':False,'T1_T8_closed':[]},
         'primary_method_reference':'https://arxiv.org/html/2510.18656v1#A3',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'Nstar':Nprec,'As':amp_prec['As'],'ns':amp_prec['ns'],'r':amp_prec['r'],'checks':len(CHECKS)},indent=2))


if __name__=='__main__':
    main()
