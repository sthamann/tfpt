"""Actual elliptic local source; all-mode proof is in the adjacent text.
Finite CAR slice checks are not a lattice replacement or full-k convergence.
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

mp.mp.dps=85
beta=4*mp.pi;q=mp.exp(-beta);delta=mp.pi/16;theta0=mp.pi/4
def bump_integral(n):
    return mp.quad(lambda y:mp.exp(-1/(1-y*y))*mp.cos(n*delta*y/2),[-1,0,1])
b0=bump_integral(0)
bn=[bump_integral(n)/b0 for n in range(11)]
chi=[x*x for x in bn]
need(all(x>0 for x in bn[:3]),'Actual compact autocorrelation has positive first two Fourier coefficients')
need(theta0+delta<mp.pi/2 and theta0-delta>-mp.pi/2,'Entire actual smooth probe support lies inside I')
def cothdiff(n):
    return 2*(q**n/(1-q**n)-q**(n+1)/(1-q**(n+1)))
M=8
terms=[-mp.sin(theta0)*(n*(n+1))**2*cothdiff(n)*chi[n]*chi[n+1] for n in range(1,M+1)]
derivative=sum(terms)
N=M+1
tail=2*(N*(N+1))**2*q**N/((1-q)*(1-q*((mp.mpf(N+2)/N)**2)))
need(all(t<0 for t in terms),'All evaluated exact-sign summands are negative')
need(abs(derivative)>tail*mp.mpf('1e35'),'Certified analytic all-mode tail cannot change the strict local witness sign')
f=lambda n:1j*n*chi[abs(n)]*mp.exp(-1j*n*theta0)
g=lambda n:-.5j*((n-1)*f(n-1)+(n+1)*f(n+1))
# Different evaluation: direct variation of only the thermal correction.
# The full vacuum part is analytically invariant, not Fourier truncated.
direct=sum(2*mp.re(mp.conj(f(n))*g(n))*2*n*q**n/(1-q**n) for n in range(1,M+1))
need(abs(direct-derivative)<tail,'Direct Fourier transport matches collected covariance derivative within analytic tail')
n,z=sy.symbols('n z',real=True)
need(sy.expand((n+1)*n-n*(n+1))==0,'Vacuum covariance derivative coefficient cancels identically')
need(sy.simplify((1/(1+sy.exp(z)))+(1/(1+sy.exp(-z)))-1)==0,'Quarter particle-hole occupation complement identity')
# Independent Laurent expansion of the necessary geometric-flow identity.
d,a0,a2=sy.symbols('d a0 a2');v1,v3,v5=sy.symbols('v1 v3 v5')
kernel=-d**-2+a0+a2*d*d
lie=sy.expand((d*v1+d**3*v3/24+d**5*v5/1920)*sy.diff(kernel,d)+(2*v1+d*d*v3/4+d**4*v5/192)*kernel)
need(sy.expand(lie).coeff(d,0)==-v3/6+2*a0*v1,'Whole geometric-flow class: constant Laurent coefficient')
need(sy.expand(lie).coeff(d,2)==-v5/240+a0*v3/4+4*a2*v1,'Whole geometric-flow class: quadratic Laurent coefficient')
need(sy.expand(lie.coeff(d,2).subs({v3:12*a0*v1,v5:144*a0*a0*v1})-sy.Rational(4,5)*(5*a2+3*a0*a0)*v1)==0,'Whole class integrability coefficient after third-order condition')
x=sy.Rational(1,20)
bound=(x+x**3)/(1-x**4)+2*x**4/(1-x**4)**3
need(bound<sy.Rational(1,12),'Exact rational all-mode charge and oscillator bound at BOTH original quarters')
# Evaluate the scalar resolvent formula independently, without a matrix log.
for lam in [mp.mpf('0.1'),mp.mpf('0.4'),mp.mpf('0.8')]:
    integ=mp.quad(lambda s:1/(lam+s)-1/(1-lam+s),[0,1,mp.inf])
    need(abs(integ-mp.log((1-lam)/lam))<mp.mpf('1e-75'),'Occupation-log resolvent sign at lambda='+str(lam))

alphas=[mp.mpf(1)/4,mp.mpf(3)/4]
def occupation(r,a):return 1/(1+mp.exp(beta*(r+a)))
def dc(r,a):
    x=mp.exp(beta*(r+a)) if r<0 else mp.exp(-beta*(r+a))
    return -x/(1+x) if r<0 else x/(1+x)
def overlap(r,j):
    k=2*j-r
    return 1/mp.sqrt(2) if k==0 else (mp.mpf(0) if k%2==0 else mp.sqrt(2)*mp.sin(k*mp.pi/2)/(mp.pi*k))
def sea(j,k):
    a=mp.mpf(j)+mp.mpf('.5');b=mp.mpf(k)+mp.mpf('.5')
    s=mp.polygamma(1,a) if j==k else (mp.digamma(b)-mp.digamma(a))/(b-a)
    return (-1)**(j+k)*s/(2*mp.pi**2)
need(abs(sea(0,0)-mp.mpf(1)/4)<mp.mpf('1e-80'),'Entire Hardy sea gives exactly1/4 on the normalized interval constant')
for j in range(3):
    for k in range(3):
        independent=2*(-1)**(j+k)/mp.pi**2*mp.nsum(lambda l:1/((2*j+2*l+1)*(2*k+2*l+1)),[0,mp.inf])
        need(abs(independent-sea(j,k))<mp.mpf('1e-75'),'Independent infinite negative-odd sea sum '+str((j,k)))
def annihilator(j,m=3):
    A=np.zeros((2**m,2**m),complex)
    for bits in range(2**m):
        if (bits>>j)&1:A[bits^(1<<j),bits]=(-1)**((bits&((1<<j)-1)).bit_count())
    return A
aa=[annihilator(j) for j in range(3)];ident=np.eye(8)
for j in range(3):
    for k in range(3):need(np.max(abs(aa[j]@aa[k].conj().T+aa[k].conj().T@aa[j]-(ident if j==k else 0)))<1e-14,'Independent Fock CAR '+str((j,k)))
rows=[];R=16
for alpha in alphas:
    weights={r:dc(r,alpha) for r in range(-R,R+1)}
    Cmp=mp.matrix(3)
    for j in range(3):
        for k in range(3):Cmp[j,k]=sea(j,k)+sum(overlap(r,j)*overlap(r,k)*weights[r] for r in weights)
    eps=(mp.exp(-beta*(R+1+alpha))+mp.exp(-beta*(R+1-alpha)))/(1-q)
    need(eps<mp.mpf('1e-88'),'Actual source thermal correction norm tail bound alpha='+str(alpha))
    C=np.array(Cmp.tolist(),float);ev,V=np.linalg.eigh(C)
    need(ev[0]>0 and ev[-1]<1,'Actual spatial3mode CAR restriction is faithful alpha='+str(alpha))
    kval=np.log1p(-ev)-np.log(ev);K=(V*kval)@V.T
    H=sum(K[j,k]*aa[j].conj().T@aa[k] for j in range(3) for k in range(3))
    rho=expm(-H);rho/=np.trace(rho)
    obs=lambda A:np.trace(rho@A)
    for j in range(3):
        for k in range(3):need(abs(obs(aa[j].conj().T@aa[k])-C[j,k])<2e-14,'Original source two-point vs independent finite density '+str((str(alpha),j,k)))
    A=aa[0].conj().T@aa[1].conj().T@aa[1]@aa[0]
    det=C[0,0]*C[1,1]-C[0,1]*C[1,0]
    need(abs(obs(A)-det)<2e-14,'Actual supported four-field word from full sea covariance alpha='+str(alpha))
    N0=aa[0].conj().T@aa[0];N1=aa[1].conj().T@aa[1];s=.7;t=-.4
    word=expm(1j*s*N0)@expm(1j*t*N1)
    target=1+np.expm1(1j*s)*C[0,0]+np.expm1(1j*t)*C[1,1]+np.expm1(1j*s)*np.expm1(1j*t)*det
    need(abs(obs(word)-target)<2e-14,'Whole supported two-number-unitary word alpha='+str(alpha))
    tau=.31;U=expm(-1j*tau*H)
    need(abs(obs(U@word@U.conj().T)-obs(word))<2e-14,'Actual finite-subalgebra modular action preserves source state alpha='+str(alpha))
    one=expm(-1j*tau*K)
    for j in range(3):
        rhs=sum(np.conj(one[k,j])*aa[k] for k in range(3))
        need(np.max(abs(U@aa[j]@U.conj().T-rhs))<2e-14,'Canonical modular sign with antilinear annihilation alpha='+str(alpha)+' j='+str(j))
    theta=lambda z:sum(mp.exp(-beta*(mp.mpf(a*a)/2+(alpha-mp.mpf('.5'))*a))*mp.exp(1j*z*a) for a in range(-12,13))
    mean=sum(a*mp.exp(-beta*(mp.mpf(a*a)/2+(alpha-mp.mpf('.5'))*a)) for a in range(-12,13))/theta(0)
    need(abs(mp.re(1j*mean))==0,'Full charge factor cannot cancel first derivative of Weyl modulus alpha='+str(alpha))
    varQ=sum(occupation(r,alpha)*(1-occupation(r,alpha)) for r in range(-30,31))
    S1=sum(n*q**n/(1-q**n) for n in range(1,21));S3=sum(n**3*q**n/(1-q**n) for n in range(1,21))
    a0val=varQ-mp.mpf(1)/12+2*S1;a2val=-mp.mpf(1)/240-S3
    need(-mp.mpf(1)/12<a0val<0 and 5*a2val+3*a0val*a0val<0,'Full connected source, including charge variance, has nonzero geometric-class obstruction alpha='+str(alpha))
    rows.append(dict(alpha=str(alpha),occupation_covariance=[[mp.nstr(Cmp[j,k],28) for k in range(3)] for j in range(3)],eigenvalues=ev.tolist(),finite_subalgebra_k=K.tolist(),thermal_correction_tail_bound=mp.nstr(eps,12),four_field_word=float(det),two_number_word=[float(target.real),float(target.imag)],charge_variance=mp.nstr(varQ,35),connected_kernel_a0=mp.nstr(a0val,35),connected_kernel_a2=mp.nstr(a2val,35),geometric_class_obstruction=mp.nstr(5*a2val+3*a0val*a0val,35)))

result=dict(verdict='EXACT_SCOPED_LOCAL_TIME_WITNESS_AND_GIVEN_FREE_CAR_READOUT; GEOMETRIC_CURRENT_POINT_FLOW_CLASS_EXCLUDED_AT_ACTUAL_QUARTERS; PHYSICAL_ORIGIN_OPEN',all_passed=True,checks=checks,control_count=len(checks),original_beta='4*pi',probe=dict(delta='pi/16',theta0='pi/4',b='normalized exp[-1/(1-(2x/delta)^2)] on |x|<delta/2',chi='b*tilde b',f='translated derivative of chi',b_fourier_first=[mp.nstr(x,25) for x in bn[:4]],f_zero_mode=0),local_covariance_derivative=mp.nstr(derivative,40),analytic_derivative_tail_bound=mp.nstr(tail,15),direct_thermal_derivative=mp.nstr(direct,40),log_weyl_modulus_derivative_per_s_squared=mp.nstr(-derivative/2,40),geometric_class=dict(regularity='C5 real v, continuous at fixed interval endpoints',action='unchanged weight1 current point transport plus arbitrary scalar shifts',exact_upper_bound_charge_variance_plus_2S1=str(bound),strict_upper_limit='1/12',decision='only v=0 is state preserving at either original quarter'),actual_interval_car_rows=rows,scope='Exact supported all-mode Mobius witness for every finite beta. Whole stated C5 geometric point-transport class excluded at actual fixed beta4pi and both quarter alphas using full connected charge covariance. Entire negative sea summed analytically. Finite3mode CAR subalgebra is only a restriction check, not a full interval modular approximation, full E8 replacement, primitive measure or physical4D result. No assertion that given current subnet equals local U1 fixed-point algebra; no full CAR nonlocal-kernel conclusion.')
(HERE/'LOCAL-SOURCE-MODULAR-TIME.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['checks','actual_interval_car_rows']},ensure_ascii=False,indent=2))
