"""Native variable-background control; the accompanying proof owns the limit."""
from pathlib import Path
import sys,json,hashlib
import numpy as np
from scipy.linalg import expm
from scipy.special import expit

REPO=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
sys.path.insert(0,str(REPO/'verification'))
import v252_full_finite_triple as original

checks={}
def need(name,value):
    checks[name]=bool(value)
    if not value:raise RuntimeError(name)
def small(a,tol=1e-8):return np.linalg.norm(a)<tol
rng=np.random.default_rng(252)
ys=[rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)) for _ in range(4)]
mr=rng.normal(size=(3,3));D=original.full_D(*ys,mr+mr.T)
gamma=original.grading();K=original.Kswap()
Q=[np.array([[0,1],[-1,0]],complex),np.array([[0,1j],[1j,0]],complex),np.eye(2),np.diag([-1j,1j])]
bp=original.rep(1,np.zeros((2,2)),np.zeros((3,3)))
V=[]
for q in Q:
    a=original.rep(0,q,np.zeros((3,3)));om=a@(D@bp-bp@D)
    sa=om+om.conj().T;V.append(sa+K@sa.conj()@K)
ix=[i for i,f in enumerate(original.P) if f[0] in ('u','d')]
sub=lambda a:a[np.ix_(ix,ix)]
g=sub(gamma);T=[-1j*g@sub(a) for a in V]
need('full96_original_has_reducing_quark36',len(ix)==36 and all(small(a[np.ix_(ix,[j for j in range(96) if j not in ix])]) for a in [D,*V]))
need('original_four_derivatives_are_Hermitian_and_odd',all(small(a-a.conj().T) and small(a@g+g@a) for a in T))
need('original_constant_radial_background_is_preserved',small(-1j*g@sub(D)-T[2]))

# Real, nonconstant coefficients of the SAME original four Higgs directions.
potential={0:T[2],1:.065*T[0]-.045j*T[1],-1:.065*T[0]+.045j*T[1],2:.035*T[3],-2:.035*T[3]}
probe={0:.02*T[2],1:.002*T[2]-.0015j*T[3],-1:.002*T[2]+.0015j*T[3]}
def add(d,k,a):d[k]=d.get(k,np.zeros((36,36),complex))+a
B={k:k*g@a for k,a in probe.items()}
for j,v in potential.items():
    for k,t in probe.items():add(B,j+k,v@t+t@v)
def mult(coeff,ns):
    return np.block([[coeff.get(int(n-m),np.zeros((36,36),complex)) for m in ns] for n in ns])
def source(c,a,b):
    U=expm(1j*a)@expm(1j*b);L=a+b;I=np.eye(len(c))
    X=c[:,None]*(U-I)
    sign,logabs=np.linalg.slogdet(I+X)
    direct=sign*np.exp(logabs-1j*np.sum(c*np.diag(L)))
    det2=sign*np.exp(logabs-np.trace(X))
    corrected=det2*np.exp(np.sum(c*np.diag(U-I-1j*L)))
    return direct,corrected
rows=[]
for alpha in [.25,.75]:
    for ncut in [2,4,8]:
        ns=np.arange(-ncut,ncut);size=36*len(ns)
        Vn=mult(potential,ns);Fn=mult(probe,ns)
        h=np.kron(np.diag(ns+alpha),g)+Vn
        Bn=mult(B,ns);anti=h@Fn+Fn@h
        inner=np.arange(36*2,size-36*2)
        if len(inner):
            need(f'weak_anticommutator_interior_alpha{alpha}_N{ncut}',small((anti-Bn)[np.ix_(inner,inner)]))
            bare=Bn-mult({k:k*g@a for k,a in probe.items()},ns)
            need(f'spatial_derivative_is_required_alpha{alpha}_N{ncut}',np.linalg.norm((anti-bare)[np.ix_(inner,inner)])>1e-3)
        e,u=np.linalg.eigh(h);delta=e[:,None]-e[None,:]
        fe=u.conj().T@Fn@u
        A=fe*np.exp(-.07*delta**2/2)
        # g'(t) Fourier transform is -i*w*g_hat(w).
        derivative=-1j*delta*A
        timeidentity=(e[:,None]+e[None,:])*A+1j*derivative-2*e[:,None]*A
        need(f'time_and_anticommutator_identity_alpha{alpha}_N{ncut}',small(timeidentity))
        need(f'actual_variable_h_is_not_momentum_diagonal_alpha{alpha}_N{ncut}',np.linalg.norm(Vn-np.kron(np.eye(len(ns)),T[2]))>1)
        need(f'selfadjoint_source_alpha{alpha}_N{ncut}',small(A-A.conj().T))
        c=expit(2*e);variance=float(np.sum(c[:,None]*(1-c)[None,:]*abs(A)**2))
        norm=float(np.linalg.norm(A,2));hs2=float(np.linalg.norm(A)**2)
        Btest=fe*np.exp(-.09*delta**2/2+1j*.3*delta)
        direct,corrected=source(c,A,Btest)
        need(f'exact_ordered_det2_correction_alpha{alpha}_N{ncut}',abs(direct-corrected)<1e-10)
        mg=[]
        ae=np.linalg.eigvalsh(A)
        for s in [-.7,.7]:
            # Similar positive matrix avoids a complex log determinant.
            rootc=np.sqrt(c);X=rootc[:,None]*(expm(s*A)-np.eye(size))*rootc[None,:]
            z=np.linalg.eigvalsh(np.eye(size)+(X+X.conj().T)/2)
            need(f'positive_MGF_matrix_alpha{alpha}_N{ncut}_s{s}',min(z)>0)
            logmgf=float(np.sum(np.log(z))-s*np.sum(c*np.diag(A)).real)
            bound=s*s/2*np.exp(abs(s)*norm)*hs2
            need(f'uniform_exponential_moment_bound_alpha{alpha}_N{ncut}_s{s}',logmgf<=bound+1e-9)
            mg.append({'s':s,'log_MGF':logmgf,'analytic_upper_bound':float(bound)})
        rows.append({'alpha':alpha,'N':ncut,'dimension':size,'HS_squared':hs2,'operator_norm':norm,'variance':variance,'ordered_source':[float(direct.real),float(direct.imag)],'moment_bounds':mg})

result={'result_id':'L20261102D','all_passed':all(checks.values()),'checks':checks,'rows':rows,'original_builder':str(REPO/'verification/v252_full_finite_triple.py'),'builder_sha256':hashlib.sha256((REPO/'verification/v252_full_finite_triple.py').read_bytes()).hexdigest(),'scope':'Original given circle and variable smooth Higgs coefficient; native seed252 diagnostics. The continuum theorem is analytical. No primitive field/state selection, H probability, 3+1 physics, absolute normalization or ledger promotion.'}
Path(__file__).with_name('variable-background-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_passed':result['all_passed'],'checks':len(checks),'rows':rows},indent=2))
