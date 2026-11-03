"""Direct Eq.16/56 check, not a TFPT physical source construction."""
import json
from itertools import combinations
from pathlib import Path
import numpy as np
from scipy.linalg import expm

I2=np.eye(2)
s1=np.array([[0,1],[1,0]],complex)
s2=np.array([[0,-1j],[1j,0]],complex)
s3=np.diag([1,-1])
gammas=[np.kron(s1,s) for s in (s1,s2,s3)]+[np.kron(s2,I2)]
g5=gammas[0]@gammas[1]@gammas[2]@gammas[3]
pairs=list(combinations(range(5),2))

def wedge2(U):
    return np.array([[U[i,k]*U[j,l]-U[i,l]*U[j,k]
                      for k,l in pairs] for i,j in pairs])

def dwedge2(X):
    I=np.eye(5)
    return np.array([[X[i,k]*I[j,l]+I[i,k]*X[j,l]
                      -X[i,l]*I[j,k]-I[i,l]*X[j,k]
                      for k,l in pairs] for i,j in pairs])

rng=np.random.default_rng(261009093)
def algebra():
    A=rng.normal(size=(5,5))+1j*rng.normal(size=(5,5))
    X=A-A.conj().T
    X-=np.trace(X)/5*np.eye(5)
    return X/np.linalg.norm(X,2)

As=[algebra() for _ in range(4)]
X,Y=algebra(),algebra()

def block(Us,rep,drep):
    Rs=[rep(U) for U in Us]
    n=len(Rs[0]); I=np.eye(4*n); G=np.kron(g5,np.eye(n))
    DW=sum(np.kron(g,(U-U.conj().T)/2)+np.kron(np.eye(4),np.eye(n)-(U+U.conj().T)/2)
           for g,U in zip(gammas,Rs))
    H=G@(DW-I)
    ev,V=np.linalg.eigh(H)
    S=(V*np.sign(ev))@V.conj().T
    P=(I+S)/2
    D=I+G@S
    def deriv(mu,Z):
        U=Rs[mu]; dU=drep(Z)@U
        dH=G@(np.kron(gammas[mu],(dU-dU.conj().T)/2)
               -np.kron(np.eye(4),(dU+dU.conj().T)/2))
        numer=np.sign(ev)[:,None]-np.sign(ev)[None,:]
        den=ev[:,None]-ev[None,:]
        F=np.divide(numer,den,out=np.zeros_like(den),where=abs(den)>1e-13)
        dP=.5*V@(F*(V.conj().T@dH@V))@V.conj().T
        return dP
    dP,dQ=deriv(0,X),deriv(1,Y)
    omega=1j*np.trace(P@(dP@dQ-dQ@dP))
    A=I-D/2
    hatgamma=G@(I-D)
    K=np.linalg.solve(A,D)
    Pold=(I-G)/2
    # Canonical polar intertwiner between the two close projectors.
    F=Pold@P+(I-Pold)@(I-P)
    S2=I-(Pold-P)@(Pold-P)
    le,lv=np.linalg.eigh(S2)
    V=F@((lv*(le**-.5))@lv.conj().T)
    return {
      'gap':float(min(abs(ev))), 'rank':int(round(np.trace(P).real)),
      'projector_defect':float(np.linalg.norm(P@P-P,2)),
      'GW_defect':float(np.linalg.norm(G@D+D@G-D@G@D,2)),
      'chirality_defect':float(np.linalg.norm(D@P-(I+G)/2@D,2)),
      'omega':float(omega.real),'omega_imaginary_residual':float(abs(omega.imag)),
      'eta_H':int(np.sign(ev).sum()),
      'selfadjoint_D_defect':float(np.linalg.norm(D-D.conj().T,2)),
      'cayley_chirality_defect':float(np.linalg.norm(A@hatgamma-G@A,2)),
      'cayley_action_defect':float(np.linalg.norm(K@A-D,2)),
      'preimage_antihermiticity_defect':float(np.linalg.norm(K+K.conj().T,2)),
      'preimage_oddness_defect':float(np.linalg.norm(K@G+G@K,2)),
      'cayley_min_singular_value':float(np.linalg.svd(A,compute_uv=False).min()),
      'polar_unitarity_defect':float(np.linalg.norm(V.conj().T@V-I,2)),
      'polar_projector_defect':float(np.linalg.norm(V@P@V.conj().T-Pold,2)),
      'cayley_log_abs_det':float(np.linalg.slogdet(A)[1]),
    }

rows=[]
for t in [.5,.25,.125,.0625]:
    Us=[expm(t*A) for A in As]
    b10=block(Us,wedge2,dwedge2)
    b5=block(Us,lambda U:U.conj(),lambda X:X.conj())
    plaq=max(np.linalg.norm(np.eye(5)-Us[i]@Us[j]@Us[i].conj().T@Us[j].conj().T,2)
             for i,j in combinations(range(4),2))
    rows.append({'t':t,'max_plaquette_defect':float(plaq), '10':b10,'bar5':b5,
                 'total_omega':b10['omega']+b5['omega']})
result={'scope':'One-site four-direction periodic torus. Actual Craig Eq.16/56; no claim that a finite chosen plaquette lies below his unspecified existence threshold. Numerical curvature is a witness, not an all-background proof.',
        'seed':261009093,'rows':rows,
        'generators':[[[[float(z.real),float(z.imag)] for z in row] for row in A] for A in As+[X,Y]]}
Path(__file__).with_name('overlap-results.json').write_text(json.dumps(result,indent=2))
print(json.dumps(rows,indent=2))
