"""Small exact witnesses for the common-source identification, not a TOE proof."""
from pathlib import Path
import importlib.util, json, hashlib
import numpy as np
import sympy as s
HERE=Path(__file__).resolve().parent
REPO=Path(__file__).resolve().parents[3]
SOURCE=REPO/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
PIN='3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593'
checks=[]
def req(ok,name):
 if not bool(ok):raise RuntimeError(name)
 checks.append(name)
req(hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN,'pinned Gaussian source')
sp=importlib.util.spec_from_file_location('native_source',SOURCE);src=importlib.util.module_from_spec(sp);sp.loader.exec_module(src)
rays=src.source_rays();refs=[np.eye(4)-np.outer(z,z.conj())/2 for z in rays]
roots=[(1j**k)*z for z in rays for k in range(4)]
def key(z):return tuple((int(a.real),int(a.imag)) for a in z)
index={key(z):i for i,z in enumerate(roots)}
actions=[]
for r in refs:
 row=[]
 for z in roots:
  w=r@z;req(np.array_equal(w.real,np.rint(w.real)) and np.array_equal(w.imag,np.rint(w.imag)),'exact Gaussian root image')
  row.append(index[key(w)])
 req(len(set(row))==240,'unitary event permutes actual240 roots')
 actions.append(row)
seen={0};todo=[0]
while todo:
 j=todo.pop()
 for row in actions:
  k=row[j]
  if k not in seen:seen.add(k);todo.append(k)
req(len(seen)==240,'native reflection group transitive on all240 roots')
coords=[next(l for l,z in enumerate(rays) if np.count_nonzero(z)==1 and z[k]!=0) for k in range(4)]
a=np.array([1,1,1,1],complex);b=np.array([1,-1,-1,-1],complex);c=a+b
req(all(key(v) in index for v in [a,b,c]),'all three bracket witnesses are native roots')
g=refs[coords[1]]@refs[coords[2]]@refs[coords[3]]
req(np.array_equal(g@a,b) and np.array_equal(g@b,a) and np.array_equal(g@c,c),'one native word swaps bracket inputs and fixes output')
req(np.vdot(a,b).real==-2 and all(np.vdot(v,v).real==4 for v in[a,b,c]),'normalized A2 root string with nonzero bracket')
x,y,z=s.symbols('f_alpha f_beta f_gamma',nonzero=True)
eta_a=y/x;eta_b=x/y;eta_c=s.Integer(1)
req(s.cancel(eta_c+eta_a*eta_b)==2,'invariance-required phases violate bracket identity by two')
# Full source root coefficients are fixed in .17; no numerical spectral work
# is needed to see that arbitrary nonzero root rephasings cannot repair Omega.
result={'research_id':'UR.COMPILER.ROOT_PHASE_LIFT.18','finite_checks':len(checks),'verdict':'EXACT_OBSTRUCTIONS_UNDER_NAMED_CURRENT_LIFT_REQUIREMENT',
 'source_sha256':PIN,'root_orbit':240,'native_word':coords[1:],
 'alpha':[1,1,1,1],'beta':[1,-1,-1,-1],'gamma':[2,0,0,0],
 'aligned_state_family':'Omega_f=sum_alpha f_alpha |alpha> tensor |psi_alpha psi_alpha>, nonzero',
 'invariance_requires':'eta_g(alpha)=f_(g alpha)/f_alpha; all coefficients nonzero by root transitivity',
 'current_bracket_requires':'eta_g(gamma)=-eta_g(alpha)*eta_g(beta) for witness word',
 'contradiction':'fixed gamma requires1, swapped pair requires product1, bracket requires -1',
 'universal_scope':'Any unitary root-monomial current-automorphism lifts of all native reflections with the unchanged paired fundamental action. All complex root rephasings included; not just a chosen sign gauge.',
 'positive_laplacian_consequence':'No nonzero aligned Omega_f belongs to ker sum_m[I-Re(Uhat_m tensor r_m tensor r_m)] with positive weights.',
 'not_excluded':['a different non-aligned joint invariant','a changed register action or larger common process','arbitrary Hilbert-space events without a current-automorphism interpretation','nonzero-energy ground states'],
 'T1_T8_closed':False}
(HERE/'origin_obstruction_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
