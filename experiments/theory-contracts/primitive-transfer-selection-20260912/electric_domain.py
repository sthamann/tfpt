"""Domain compatibility and a declared quadratic-electric collar alternative.

No TFPT selection claim. Fraction identities and numerical finite controls
are reported separately from the all-cutoff proof in ELECTRIC_DOMAIN.md.
"""
from fractions import Fraction as F
import json
import numpy as np
checks=[]
def check(name,condition):
    if not condition: raise RuntimeError(name)
    checks.append(name)

records=[]
for kap in [F(1),F(2),F(5)]:
    for N in [4,16,64]:
        Z=1/kap**2+2*sum((1/(4*n+kap)**2 for n in range(1,N+1)),F(0))
        E2=2*sum(((4*n)**2/(4*n+kap)**2 for n in range(1,N+1)),F(0))
        Zupper=1/kap**2+F(1,4) # sum n^-2 <=2
        n0=max(1,(kap.numerator+4*kap.denominator-1)//(4*kap.denominator))
        lower=F(max(0,N-n0+1),2)/Zupper
        check(f'norm_upper_{kap}_{N}',Z<=Zupper)
        check(f'electric_divergence_lower_{kap}_{N}',E2/Z>=lower)
        records.append({'kappa':str(kap),'N':N,'electric_second_moment':float(E2/Z),'diverging_lower_bound':float(lower)})

for eta in [F(1,200),F(1,2),F(2)]:
    for M in [8,16]:
        k=np.arange(-M,M+1)
        eta_f=float(eta); eps=0.4
        a=abs(k)+eta_f*k*k
        V=np.exp(-1j*k[:,None]*(np.arange(4)*np.pi/2)[None,:])
        B=np.diag(a)+eps*V@V.conj().T
        R=np.diag(1/(a+1))
        G=V.conj().T@R@V
        inverse=R-R@V@np.linalg.solve(np.eye(4)/eps+G,V.conj().T@R)
        check(f'positive_energy_{eta}_{M}',np.linalg.eigvalsh(B)[0]>0)
        check(f'electric_source_resolvent_{eta}_{M}',np.max(abs(inverse-np.linalg.inv(B+np.eye(len(k)))))<1e-11)
        clock=np.diag(1j**k)
        check(f'four_clock_preserved_{eta}_{M}',np.max(abs(clock@B-B@clock))<1e-10)

# Explicit all-tail comparison bounds; a finer cutoff is only a control.
for eta in [F(1,2),F(2)]:
    for M in [4,16,64]:
        gt=4*sum((2/(eta*k*k+k+1) for k in range(M+1,2*M+1)),F(0))
        bt=4*sum((2/(eta*k*k+k+1)**2 for k in range(M+1,2*M+1)),F(0))
        check(f'Gram_tail_bound_{eta}_{M}',gt<8/(eta*M))
        check(f'vector_tail_bound_{eta}_{M}',bt<8/(3*eta**2*M**3))

print(json.dumps({'status':'DIRECT_FLUX_MAP_REJECTED_QUADRATIC_FORM_ALTERNATIVE_WELL_DEFINED',
 'checks_passed':len(checks),'checks':checks,'energy_records':records,
 'quadratic_collar_derived_from_TFPT':False,
 'native_rotor_and_collar_intertwiner_constructed':False,
 'any_kappa_has_finite_bare_electric_energy':False},sort_keys=True,indent=2))
