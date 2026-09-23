"""Shared c3 transfer audit, no per-observable retune or likelihood claim."""
from pathlib import Path
import argparse, json, hashlib
import mpmath as m

HERE=Path(__file__).resolve().parent
m.mp.dps=70
checks=[]
def need(test,name):
    if not test: raise RuntimeError(name)
    checks.append(name)

def phi(alpha,c):
    q=48*c**4*m.exp(-2*alpha)
    return 1/(6*m.pi)+q*(1-q)**(-m.mpf(5)/4)

def equation(alpha,c):
    return alpha**3-2*c**3*alpha**2-m.mpf(164)/5*c**6*m.log(1/phi(alpha,c))

def alpha(c):
    a=m.findroot(lambda a:equation(a,c), (m.mpf('.005'),m.mpf('.009')))
    need(a>0 and abs(equation(a,c))<m.mpf('1e-65'),'positive electromagnetic root with tiny residual')
    return a

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=HERE/'parameter_transfer.json');args=p.parse_args()
    c=1/(8*m.pi);As=m.exp(m.mpf('3.062'))*m.mpf('1e-10');ns=m.mpf('.9752')
    cfit=(6*m.pi**2*As*(1-ns)**2)**(m.mpf(1)/7)
    a0=alpha(c);a1=alpha(cfit)
    need(abs(1/a0-m.mpf('137.0359992168407125'))<m.mpf('1e-16'),'source baseline alpha reproduced')
    need(abs(1/a1-m.mpf('167.8032986296328993'))<m.mpf('1e-16'),'cosmology retune alpha consequence reproduced')
    da_dc=-m.diff(lambda cc:equation(a0,cc),c)/m.diff(lambda aa:equation(aa,c),a0)
    sensitivity=-c*da_dc/a0
    eps=m.mpf('1e-8')
    checkfd=m.log(alpha(c*(1-eps))/alpha(c*(1+eps)))/(m.log(1+eps)-m.log(1-eps))
    need(abs(checkfd-sensitivity)<m.mpf('1e-14'),'implicit logarithmic sensitivity agrees with independent finite difference')
    y=m.findroot(lambda y:1-8*(y+1)/(3*(y-1)**2)-ns,110)
    fullpotential_cfit=(6*m.pi**2*As*(1-ns)**2/(1+1/y)**2)**(m.mpf(1)/7)
    afull=alpha(fullpotential_cfit)
    need(fullpotential_cfit<cfit<c and 1/afull>1/a1>1/a0,'full-potential first-SR shift worsens shared-c3 electromagnetic mismatch')
    out={'scope':'high precision implicit equations; not interval arithmetic, not an empirical exclusion',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'c3_fixed':str(c),'As_target':str(As),'ns_target':str(ns),
         'leading_retune':{'c3':str(cfit),'fractional_change':str(cfit/c-1),'alpha_inverse':str(1/a1)},
         'baseline_alpha_inverse':str(1/a0),'dlog_alpha_inverse_dlog_c3':str(sensitivity),
         'full_potential_first_SR_retune':{'y':str(y),'c3':str(fullpotential_cfit),'alpha_inverse':str(1/afull)},
         'ACT_dataset':'arXiv:2503.14452v2 Table5 P-ACT-LB2; not a universal model-independent measurement',
         'checks':checks,'check_count':len(checks)}
    args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
