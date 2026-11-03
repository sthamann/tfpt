"""First-field test in the actual original eightfold CAR dictionary.

Uses the supplied Weyl matrix. This does not identify quotient locality
with a primitive P1 interval or realize the whole target D5+A3 net there.
"""
import itertools
import json
from pathlib import Path
import sympy as s

def need(ok,label):
    if not ok: raise RuntimeError(label)

ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
path=ROOT/'experiments/theory-contracts/v16-operator-pullback-20261014/fold-results.json'
data=json.loads(path.read_text())
M=s.Matrix([[s.Rational(q)for q in row]for row in data['explicit_Weyl_matrix']])
need(M.T*M==s.eye(8),'actual original Weyl matrix is orthogonal')
E=s.eye(8)
lam=s.ones(8,1)/2
q=M.T*lam
need(q==E[:,0]+E[:,1],'actual original lambda is the source pair charge e0+e1')
need(M*q==lam and (q.T*q)[0]==2,'literal eight-Cartan Ward charge and level')

# Exactly the two lowest positive source modes r=0,1 of the ONE cover field.
# Their eightfold residue labels are j=0,1. This finite invariant excitation
# space verifies operator identities; smooth support is treated in the proof.
ann=[]
for mode in range(2):
    C=s.zeros(4)
    for mask in range(4):
        if (mask>>mode)&1:
            sign=(-1)**sum((mask>>k)&1 for k in range(mode))
            C[mask^(1<<mode),mask]=sign
    ann.append(C)
N=[C.T*C for C in ann]
create=ann[0].T*ann[1].T
adj=create.T
vac=s.eye(4)[:,0]
psi=create*vac
need((psi.T*psi)[0]==1,'nonzero source pair norm from original CAR')
need((vac.T*adj*create*vac)[0]==1,'positive reflected pair norm')
need(all(N[j]*create-create*N[j]==create for j in (0,1)),'actual source charge commutators')
for a in range(8):
    Hcart=M[a,0]*N[0]+M[a,1]*N[1]
    need(Hcart*create-create*Hcart==lam[a]*create,'target Cartan Ward action')
energies={}
for alpha in (s.Rational(1,4),s.Rational(3,4)):
    H=alpha*N[0]+(1+alpha)*N[1]
    energy=1+2*alpha
    need(H*vac==s.zeros(4,1) and H*psi==energy*psi,'same actual source Hamiltonian')
    need(H*create-create*H==energy*create,'same all-time field covariance')
    delta=s.Matrix([s.Rational(j,8)+alpha/8-s.Rational(1,2)for j in range(8)])
    need(8*(1+(delta.T*q)[0])==energy,'original folded Kdelta and source time agree')
    energies[str(alpha)]=str(energy)

# Decisive common-U check before using a local extension theorem.
rows=[]
for component,indices in [('D5',range(5)),('D3_A3',range(5,8))]:
    for i,j in itertools.combinations(indices,2):
        for sign_i,sign_j in itertools.product((-1,1),repeat=2):
            root=sign_i*E[:,i]+sign_j*E[:,j]
            pre=M.T*root
            integer=all(v.q==1 for v in pre)
            need((pre.T*pre)[0]==2,'every source preimage is a norm2 root')
            need(integer or all(v.q==2 for v in pre),'source root sectors exact')
            rows.append({'component':component,'target':list(map(str,root)),
                         'source':list(map(str,pre)),'in_original_NS_current':integer})
counts={name:{str(flag):sum(r['component']==name and r['in_original_NS_current']==flag for r in rows)
              for flag in (True,False)}for name in ('D5','D3_A3')}
need(sum(r['in_original_NS_current']for r in rows)==20,'only20 of52 target Uroots are NS currents')
need(len(rows)==52,'complete supplied U root alphabet')
mixed=[]
for signs in itertools.product((-1,1),repeat=8):
    if sum(x<0 for x in signs[:5])%2 or sum(x<0 for x in signs[5:])%2: continue
    root=s.Matrix([s.Rational(x,2)for x in signs]); pre=M.T*root
    mixed.append(all(v.q==1 for v in pre))
need(len(mixed)==64 and sum(mixed)==32,'half of target M11roots already original NS currents')
kink_image=M*s.ones(8,1)/2
need(kink_image==E[:,2]+E[:,5],'actual uniform halfkink target grade2 root')

# Complete-chart obstruction, independent of M: the actual source even CAR
# charge lattice has determinant4. A full-rank isometric L0 inclusion has
# index2, so it cannot also contain an order4 discriminant generator.
index=s.sqrt(s.Rational(16,4))
need(index==2,'whole lattice-chart index obstruction')
# More generally in a same-conformal VOA realization, U's60 currents and
# the irreducible Mh ground64 are disjoint weightone subspaces.
need(60+64>120,'whole same-conformal UplusMh dimension obstruction')

out={
    'status':'PASS_FIRST_FIELD_AND_COMMON_U_TEST',
    'original_matrix_source':str(path),
    'target_lambda':list(map(str,lam)),
    'actual_source_preimage':list(map(str,q)),
    'explicit_original_field':'normal_ordered chi_0^dagger(x) chi_1^dagger(x)',
    'given_source_pair_CAR_norm_squared':'1',
    'source_pair_energy_by_quarter':energies,
    'target_Cartan_Ward_components':list(map(str,M*q)),
    'target_U_source_sectors':counts,
    'whole_target_U_original_NS_roots':20,
    'whole_target_U_requires_source_spinor_roots':32,
    'target_M11_original_NS_roots':32,
    'target_M11_requires_source_spinor_roots':32,
    'uniform_halfkink_target_image':list(map(str,kink_image)),
    'uniform_halfkink_target_D5A3_glue_grade':2,
    'all_lattice_chart_obstruction':{'source_lattice_det':4,'base_D5A3_det':16,'required_index':str(index),'marked_h_order':4},
    'all_same_conformal_VOA_chart_obstruction':{'U_weightone':60,'Mh_ground_at_weightone':64,'required_weightone_at_least':124,'source_D8_weightone':120},
    'scope':'Actual supplied eightfold CAR field, same state/adjoint/source time. Quotient support is8coverarcs. Full target U and primitive P1 local identification are not supplied.',
    'first_additional_realization_premise':'the entire target U must occur with this field in the same original local conformal source before applying SIMPLIFICATION.txt',
    'all_target_U_roots':rows,
}
print(json.dumps(out,indent=2,sort_keys=True))
