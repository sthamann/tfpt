from seam_extension import *
# Source v146 inversion fixes character 2 and exchanges characters 1 and 3.
# Native family mode M sends e5 -> -e5, e6 -> e7, e7 -> e6; det M = +1.
# Compose its spin lift with the D8 dual involution. On even-family states:
# vacuum -> -vacuum, B0 -> B0, B1 <-> B2, exactly the selected inversion action.
rdict=parent['results']['native'];spinorder=[tuple(v) for v in rdict['spinor_root_order']];basisphase=dict(zip(spinorder,rdict['basis_phases']))
def p(v):return v[:6]+(v[7],v[6])
P=s.eye(8);P[6,6]=P[7,7]=0;P[6,7]=P[7,6]=1
T=Ri*P*R;B=s.zeros(8);gram=R.T*R
for i in range(8):
 B[i,i]=1
 for j in range(i):B[i,j]=gram[i,j]
delta=T.T*B*T-B
basephase={v:(-1)**sum(int(delta[i,j])*int(coords[v][i])*int(coords[v][j]) for i in range(8) for j in range(i+1,8)) for v in roots}
desired={}
for v in spinorder:
 n5,n6,n7=[int(x==1) for x in v[5:]]
 desired[v]=basisphase[v]*basisphase[p(v)]*(-1)**(1+n5+n6*n7)
solutions=[]
for bits in itertools.product([0,1],repeat=8):
 if all(basephase[v]*(-1)**sum(bits[i]*int(coords[v][i]) for i in range(8))==desired[v] for v in spinorder):solutions.append(bits)
ck(len(solutions)==1,'unique inversion sign extension from the native spinor action')
bits=solutions[0];f={v:basephase[v]*(-1)**sum(bits[i]*int(coords[v][i]) for i in range(8)) for v in roots}
for a,b in itertools.product(roots,repeat=2):
 out=lie.bracket(lie.ridx[a],lie.ridx[b]);po=lie.bracket(lie.ridx[p(a)],lie.ridx[p(b)])
 if add(a,b) in rs:
  v=add(a,b);ck(out[lie.ridx[v]]*f[v]==f[a]*f[b]*po[lie.ridx[p(v)]],'inversion preserves every source root-sum bracket')
 elif b==neg(a):ck(f[a]*f[b]==1,'inversion preserves opposite-root bracket under P Cartan action')
 else:ck(not out and not po,'inversion preserves zero root bracket')
for v in roots:
 ck(f[v]*f[p(v)]==1,'inversion squares to identity')
 ck((exponents[p(v)]+exponents[v])%4==0,'inversion conjugates deck to inverse')
for j,b in enumerate(blocks):
 for v in b:
  if q(v)!=1:continue
  target=blocks[[0,2,1][j]];ck(p(v) in target,'inversion acts on correct family block')
  ck(basisphase[v]*f[v]*basisphase[p(v)]==1,'all 48 native carrier basis states have unphased source inversion')
ck(all(basisphase[v]*f[v]*basisphase[p(v)]==-1 for v in fourth),'remaining singlet carrier inversion is minus one')
# Check joint D4 character of the four family slots; no invariant line exists.
F4=s.Matrix([[-1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
T4=s.diag(-1,-1,-s.I,s.I)
# Re-evaluate the original geometric pullback rule from v146 in the selected order.
Z,W=s.symbols('z w');env={'sp':s,'Z':Z,'W':W}
source_tree=ast.parse((ROOT/'verification/v146_moebius_d4.py').read_text())
omega_assign=next(n for n in source_tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='OMEGA' for t in n.targets))
exec(compile(ast.Module(body=[omega_assign],type_ignores=[]),'source_omega','exec'),env)
pullback=select('verification/v146_moebius_d4.py','pullback',env)
cohT=s.Matrix([pullback(k,s.I*W,s.I) for k in [1,2,3]]).T
cohF=s.Matrix([pullback(k,1/W,-1/W**2) for k in [1,2,3]]).T
order=[1,2,0]
ck(cohT.extract(order,order)==T4[1:,1:] and cohF.extract(order,order)==F4[1:,1:],'original geometric deck and inversion match the native three-family action exactly')
ck(F4**2==s.eye(4) and T4**4==s.eye(4) and F4*T4*F4==T4.inv(),'full marked four-slot D4 relations')
ck(s.Matrix.vstack(T4-s.eye(4),F4-s.eye(4)).rank()==4,'four-slot extension contains no trivial D4 submodule')
ck(all(p(v)==v and f[v]==1 for v in d5),'full inversion fixes the original D5 root generators pointwise')
from sympy import kronecker_product as kron
constraints=s.Matrix.vstack(kron(s.eye(4),T4)-kron(T4.T,s.eye(4)),kron(s.eye(4),F4)-kron(F4.T,s.eye(4)))
ck(16-constraints.rank()==3,'D4 family commutant has dimension three')
# An allowed, source-explicit projector separates the native singlet from the selected three.
# On eigenvalue -1 of T4, F4 distinguishes the singlet (-) and first family (+).
PT=(s.eye(4)-T4+T4**2-T4**3)/4;PF=(s.eye(4)-F4)/2;Psing=PT*PF
ck(Psing==s.diag(1,0,0,0),'joint D4 projector recovers the family singlet without a new continuous coefficient')
# Determinant completion is forced by SU4, not by a free singlet character.
Vdeck=T4[1:,1:];Vinv=F4[1:,1:]
ck(T4[0,0]==1/Vdeck.det() and F4[0,0]==1/Vinv.det(),'fourth character is the dual determinant line of the source H1 module')
ck(T4.det()==1 and F4.det()==1,'full family action lies in SU4')
ck(Psing*T4==T4*Psing and Psing*F4==F4*Psing,'isotypic family projector respects the full seam D4 action')
result={'verdict' :'EXACT_D4_EXTENSION_ON_FULL_E8_AND_JOINT_FAMILY_PROJECTOR','determinant_completion':'W = det(V)^* directsum V; V is the source three-dimensional seam D4 module','source_phase_bits':bits,'inversion_root_order':roots,'inversion_root_signs':[f[v] for v in roots],'family_deck':[[str(x) for x in row] for row in T4.tolist()],'family_inversion':[[str(x) for x in row] for row in F4.tolist()],'singlet_D4_character':{'deck':-1,'inversion':-1},'triplet_D4_action':'diag(-1,-i,i) and unphased swap of the last two; v141/v146 order','singlet_projector':'(I-T+T^2-T^3)/4 times (I-F)/2 on the four-slot family module','family_invariant_state_simplex':'rho = a*P_singlet + b*P_character2_even + c*P_doublet/2; a,b,c >= 0, a+b+c=1','family_commutant_dimension':3,'total_checks':len(checks),'scope':'Exact extension after identifying the marked native triplet with the original seam D4 module. The resulting projector is algebraic; no physical measurement instrument, state or dynamics is derived.'}
(OUT/'d4.json').write_text(json.dumps(result,indent=2)+'\n')
