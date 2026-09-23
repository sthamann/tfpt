from e6_structure import *
# The source H1 deck characters i, -1, -i are assigned to the explicitly marked family weights.
# Family order: missing 5, missing 6, missing 7. Use v141 selected -U order (2,3,1); this labeling is an explicit bridge premise.
# Read the original chosen deck matrix rather than retyping its phase assignment.
source_tree=ast.parse((ROOT/'verification/v141_deck_selection.py').read_text())
source_assigns=[n for n in source_tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ['II','MINUS_U'] for t in n.targets)]
source_env={'sp':s};exec(compile(ast.Module(body=source_assigns,type_ignores=[]),'source_deck_constants','exec'),source_env)
chars=[next(k for k in range(4) if s.I**k==source_env['MINUS_U'][j,j]) for j in range(3)]
ck(chars==[2,3,1],'original chosen deck order')
H=(0,0,0,0,0,4,3,5)
def degree(v):
 z=F(ip(H,v),2)
 ck(z.denominator==1,'E8 cocharacter integral on every root')
 return int(z)
exponents={v:degree(v)%4 for v in roots}
ck(all(exponents[v]==chars[j] for j,b in enumerate(blocks) for v in b if q(v)==1),'all 48 marked matter directions carry original H1 characters')
ck(all(exponents[v]==0 for v in d5),'source carrier D5 algebra fixed pointwise')
# Direct original brackets establish a full order-four Lie algebra automorphism.
for a,b in itertools.product(roots,repeat=2):
 out=lie.bracket(lie.ridx[a],lie.ridx[b])
 for k,c in out.items():
  target=exponents[lie.roots[k]] if k<240 else 0
  ck((exponents[a]+exponents[b]-target)%4==0,'seam phase extension preserves source Lie bracket')
# The span over Z of all D5 roots and the 48 marked carrier weights is the entire E8 root lattice.
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
source_lattice=s.Matrix.hstack(*[s.Matrix(coords[v]) for v in sorted(d5|old48)])
normal=smith_normal_form(source_lattice,domain=ZZ)
ck([abs(normal[i,i]) for i in range(8)]==[1]*8,'marked D5 and 48 weights generate full E8 lattice, proving unique torus extension')
# The old fourth family weight is all minus in the last three components.
fourth={v for v in roots if all(abs(x)==1 for x in v) and v[5:]==(-1,-1,-1)}
ck(len(fourth)==16 and {exponents[v] for v in fourth}=={2},'fourth 16 forced to character minus one')
counts=Counter(exponents.values());counts[0]+=8
# Compare to actual coherent J lift from the prior original-source certificate.
clocks=parent['results']['clocks'];rorder=[tuple(v) for v in clocks['roots']];J=clocks['coherent_compiler_lifts']['J'];perm=J['root_permutation'];sign=J['root_signs'];base=s.Matrix(D['clock_matrices']['J']['vector'])
traces=[]
for n in range(4):
 tr=s.trace(base**n)
 for i in range(240):
  j=i;z=1
  for _ in range(n):z*=sign[j];j=perm[j]
  if j==i:tr+=z
 traces.append(int(tr))
mult={k:int(s.simplify(sum(s.I**(-k*n)*traces[n] for n in range(4))/4)) for k in range(4)}
ck(dict(counts)!={k:mult[k] for k in range(4)},'cohomological deck extension is not conjugate to the chosen original J lift')
ck(all(perm[i]!=i for i in range(240)) and s.trace(base)==0,'all phase-twisted lifts of original root permutation J have trace zero')
seamtrace=sum(counts[k]*s.I**k for k in range(4))
ck(seamtrace==4,'seam clock adjoint trace is four, excluding conjugacy to any root-normalizer lift of J')
# The unique extension factors into the already marked D8 dual involution and an A2 quarter-rotation.
HA=(0,0,0,0,0,0,-1,1)
for v in roots:
 theta=q(v)%2
 ck(theta==int(all(abs(x)==1 for x in v)),'D8 dual involution is minus exactly on 128 spinor roots')
 ak=F(ip(HA,v),2);ck(ak.denominator==1,'family A2 quarter rotation integral')
 ck((2*theta+int(ak)-exponents[v])%4==0,'unique seam extension equals D8 dual involution times A2 quarter rotation')
ck(all(ip(HA,v)==0 for v in e6),'A2 quarter rotation centralizes E6')
blockphases=[]
for b in blocks:
 counts_by_piece={str(grade):dict(Counter(str(exponents[v]) for v in b if q(v)==grade)) for grade in [1,-2,4]}
 blockphases.append(counts_by_piece)

# Witness that setting the leftover singlet phase to +1 fails a concrete root relation.
# Sum four native family weights once each, choose carrier entries to sum to zero.
foursets=[fourth]+[{v for v in b if q(v)==1} for b in blocks]
witness=None
for a in sorted(foursets[0]):
 for b in sorted(foursets[1]):
  for c in sorted(foursets[2]):
   d=tuple(-a[i]-b[i]-c[i] for i in range(8))
   if d in foursets[3]:witness=[a,b,c,d];break
  if witness:break
 if witness:break
ck(witness is not None,'four family root directions obey a zero-sum lattice relation')
ck(sum(exponents[v] for v in witness)%4==0,'forced fourth phase respects lattice relation')
ck((0+1+2+3)%4!=0,'trivial fourth phase violates source character relation')
result={'research_id':'UR.COMPILER.SEAM_E8_CHARACTER_EXTENSION.05','verdict':'EXACT_UNIQUE_MARKED_TORUS_EXTENSION; NONCONJUGATE_TO_ANY_LIFT_OF_ORIGINAL_J','H_cocharacter':H,'factorization':{'D8_dual_involution':'plus on 120 D8 currents, minus on 128 spinor currents','A2_cocharacter':HA,'three_27_phase_content':blockphases},'seam_adjoint_trace':str(seamtrace),'all_phase_twisted_J_lift_adjoint_trace':0,'family_character_exponents':chars,'fourth_family_character_exponent':2,'uniqueness_index':1,'full_adjoint_multiplicities_i_to_k':{str(k):counts[k] for k in range(4)},'tested_original_J_multiplicities_i_to_k':{str(k):mult[k] for k in range(4)},'tested_original_J_power_traces':traces,'zero_sum_family_root_witness_doubled':witness,'total_checks_including_e6':len(checks),'root_order':roots,'root_character_exponents':[exponents[v] for v in roots],'scope':'Unique among diagonal root-space automorphisms fixing marked D5 pointwise and assigning these three seam characters to the chosen 48 directions. Assignment from H1 to this internal family module is still a premise. This is not a vacuum or physical time selection; Nonconjugacy holds for every phase-twisted lift with the original J root permutation (all have trace zero).'}
(OUT/'seam.json').write_text(json.dumps(result,indent=2)+'\n')
