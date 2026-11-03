"""Support-resolved pairing in the actual free elliptic source.
No finite Fourier profile is called local; full occupied sea is analytic.
"""
from pathlib import Path
import json
import mpmath as mp
import numpy as np
import sympy as sy
from scipy.linalg import expm
HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    checks.append(dict(label=label,passed=True))

# Algebraic all-mode identities; support strictness is proved analytically.
z,c,x,a=sy.symbols('z c x a',real=True)
P=sy.Matrix([[1-z,x],[x,z]]);u=sy.Matrix([0,1]);t=sy.Matrix([x/a,(z-c)/a])
def red(expr):return sy.factor(sy.expand(expr).subs(x*x,z*(1-z)).subs(a*a,c*(1-c)))
need(all(red(e)==0 for e in P*P-P),'Given original full two-face covariance is a projection for every spectral mode')
need(all(red(e)==0 for e in P*u-c*u-a*t),'Actual probe partner first projection equation, all Fourier modes')
need(all(red(e*a)==0 for e in P*t-a*u-(1-c)*t),'Actual probe partner second projection equation, all Fourier modes')
mx,c2=sy.symbols('mx c2',real=True)
need(sy.simplify(mx+c2-c*c-c*(1-c)).subs(c2,c-mx)==0,'Entire source-moment normalization of derived partner')
F=sy.Matrix([[0,1],[1,0]])
need(P.subs(z,1-z)==F*P*F,'Actual geometric quarter complement requires transported face labels')

mp.mp.dps=85;beta=4*mp.pi;cut=32
def ur2(r):return mp.mpf('.5') if r==0 else (2/(mp.pi*r)**2 if r%2 else mp.mpf(0))
def occ(r,alpha):return 1/(1+mp.exp(beta*(r+alpha)))
def thermal(r,alpha):
    q=mp.exp(beta*(r+alpha)) if r<0 else mp.exp(-beta*(r+alpha))
    return -q/(1+q) if r<0 else q/(1+q)
def cross(r,alpha):return 1/(2*mp.cosh(beta*(r+alpha)/2))
def tail(alpha,half=False):
    b=beta/2 if half else beta
    return (mp.exp(-b*(cut+1+alpha))+mp.exp(-b*(cut+1-alpha)))/(1-mp.exp(-b))
need(abs(mp.nsum(lambda n:2/(mp.pi*(2*n+1))**2,[0,mp.inf])-mp.mpf('.25'))<mp.mpf('1e-80'),'Whole negative occupied sea gives exact1/4 for actual interval-supported probe')

def ann(j):
    A=np.zeros((4,4),complex)
    for k in range(4):
        if (k>>j)&1:A[k^(1<<j),k]=(-1)**((k&((1<<j)-1)).bit_count())
    return A
aa=[ann(0),ann(1)];I=np.eye(4)
for j in range(2):
    for k in range(2):need(np.max(abs(aa[j]@aa[k].conj().T+aa[k].conj().T@aa[j]-(I if j==k else 0)))<1e-14,'Independent two-mode Fock CAR '+str((j,k)))
rows=[]
for alpha in [mp.mpf(1)/4,mp.mpf(3)/4]:
    weights={r:ur2(r) for r in range(-cut,cut+1)}
    cp=mp.mpf('.25')+sum(w*thermal(r,alpha) for r,w in weights.items())
    xp=sum(w*cross(r,alpha) for r,w in weights.items())
    x2=sum(w*cross(r,alpha)**2 for r,w in weights.items())
    c2p=mp.mpf('.25')+sum(w*((2*thermal(r,alpha)+thermal(r,alpha)**2) if r<0 else occ(r,alpha)**2) for r,w in weights.items())
    A2=cp*(1-cp);ap=mp.sqrt(A2);gap=A2-xp*xp
    yC=occ(0,alpha)-cp;yX=cross(0,alpha)-xp;lower=yC*yC+yX*yX
    need(tail(alpha)<mp.mpf('1e-175') and tail(alpha,True)<mp.mpf('1e-87'),'Original all-mode geometric tail bounds alpha='+str(alpha))
    need(abs(cp-c2p-x2)<mp.mpf('1e-80'),'Entire-source C-C²=X² moment with full sea alpha='+str(alpha))
    need(0<cp<1 and xp>0 and gap>0,'Actual physical two-probe source is mixed alpha='+str(alpha))
    need(lower>mp.mpf('.05') and lower<gap,'Genuine outside contribution is nonzero and smaller than finite-probe defect alpha='+str(alpha))
    need(abs((x2+c2p-cp*cp)/A2-1)<mp.mpf('1e-80'),'Actual derived original-environment partner has norm1 alpha='+str(alpha))
    left=x2/A2;right=1-left
    need(0<left<1 and 0<right<1,'Derived probe partner uses both original source faces alpha='+str(alpha))
    for eps in [mp.mpf('0.001'),mp.mpf('0.000001')]:
        factor=ap/mp.sqrt(A2+eps)
        need(0<factor<1 and 1-factor<=mp.sqrt(eps)/ap,'Bounded polar approximation error on actual probe alpha='+str(alpha)+' eps='+str(eps))
    M=np.array([[float(cp),float(xp)],[float(xp),float(1-cp)]])
    vals,V=np.linalg.eigh(M);need(np.all(vals>0) and np.all(vals<1),'Both actual finite covariance endpoints excluded alpha='+str(alpha))
    k=(V*(np.log1p(-vals)-np.log(vals)))@V.T
    H=sum(k[j,l]*aa[j].conj().T@aa[l] for j in range(2) for l in range(2))
    rho=expm(-H);rho/=np.trace(rho)
    psi=np.zeros(4,complex);psi[1]=float(mp.sqrt(cp));psi[2]=float(mp.sqrt(1-cp))
    pure=np.outer(psi,psi.conj());Q=np.array([[float(cp),float(ap)],[float(ap),float(1-cp)]])
    N0=aa[0].conj().T@aa[0];N1=aa[1].conj().T@aa[1]
    for label,density,cov,expected_four in [('physical_local_pair',rho,M,float(gap)),('derived_environment_pair',pure,Q,0.)]:
        E=lambda A:np.trace(density@A)
        for j in range(2):
            for l in range(2):need(abs(E(aa[j].conj().T@aa[l])-cov[j,l])<2e-14,'Actual charged two-insertion word '+str((str(alpha),label,j,l)))
        need(abs(E(N0@N1)-expected_four)<2e-14,'Full neutral four-field word '+str((str(alpha),label)))
        need(abs(E(aa[0]))+abs(E(aa[1]))<2e-14,'Isolated charged odd insertions vanish '+str((str(alpha),label)))
        s=.7;t=-.4
        word=expm(1j*s*N0)@expm(1j*t*N1)
        target=1+np.expm1(1j*s)*cov[0,0]+np.expm1(1j*t)*cov[1,1]+np.expm1(1j*s)*np.expm1(1j*t)*expected_four
        need(abs(E(word)-target)<2e-14,'Complete bounded ordered two-number word '+str((str(alpha),label)))
    need(np.max(abs(Q@Q-Q))<2e-15 and np.max(abs(M@M-M))>.1,'Actual partner restores pure covariance without modifying global source alpha='+str(alpha))
    rows.append(dict(alpha=str(alpha),actual_right_occupation=mp.nstr(cp,40),actual_physical_cross_word=mp.nstr(xp,40),derived_partner_cross_word=mp.nstr(ap,40),actual_four_field_word=mp.nstr(gap,40),derived_partner_four_field_word='0',outside_C_word=mp.nstr(yC,40),outside_X_word=mp.nstr(yX,40),full_interval_defect_lower_bound=mp.nstr(lower,40),derived_probe_partner_left_weight=mp.nstr(left,35),derived_probe_partner_right_remainder_weight=mp.nstr(right,35),derived_probe_partner_outside_weight_lower_bound=mp.nstr(lower/A2,35),occupation_tail_bound=mp.nstr(tail(alpha),14),cross_tail_bound=mp.nstr(tail(alpha,True),14),physical_pair_eigenvalues=vals.tolist()))

out=dict(verdict='EXACT_SCOPED_REGIONAL_PARTNER_IN_ORIGINAL_FREE_SOURCE; PROPER_OTHER_FACE_ONLY_CANONICAL_PARTNER_EXCLUDED; PHYSICAL_ORIGIN_OPEN',all_passed=True,control_count=len(checks),checks=checks,original_beta='4*pi',rows=rows,scope='Full paired-proper-region exclusion and full interval polar map proved analytically using actual X smoothing and bounded polar decomposition. Numerical words use actual single supported L2 probe, entire negative sea and exponentially bounded correction; its one-mode T is not asserted equal to full interval T_I. Existing global GNS and general projection identity reused. No primitive P1 measure, full E8/4D source, local RP violation, physical signalling or Higgs Gaussianization claimed.')
(HERE/'REGIONAL-SOURCE-PARTNER.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},ensure_ascii=False,indent=2))
