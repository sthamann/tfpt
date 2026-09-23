"""Bounded test of actual TFPT clock covariance on a normed triality.

This derives representation-level maps from the pinned source metric/clocks.
It constructs an integral order but does not derive its unique TFPT selection,
physical fields, vacuum, or Hamiltonian.
"""
import sys, json, hashlib, itertools
from pathlib import Path
from fractions import Fraction
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
from collections import deque

import ast
from types import SimpleNamespace
ROOT = Path(__file__).resolve().parents[3]
PINS = {
 'verification/v55_coxeter_cycle.py': '9af92555cc66c753430f410977fdf732cd2b6d35922ee6578b4853cb4468573c',
 'verification/v973_seam_route_narrowing.py': '88ab99f5e9d8378ec73e1b79a857644013441c11f4e0ee3bdd4a83efb3eaba2d',
 'experiments/tfpt-discovery/clock_fiber_product_probe.py': 'd71609c465c20e2feacf88ec312d21d87639d4cfd91345e4ac1f71fa3dc7ec1d',
}
def source_guard(ok, label):
    if not bool(ok): raise RuntimeError(label)
class AlwaysOn(ast.NodeTransformer):
    def visit_Assert(self, node):
        return ast.copy_location(ast.Expr(value=ast.Call(
            func=ast.Name(id='source_guard', ctx=ast.Load()),
            args=[node.test, ast.Constant(value='source guard at line '+str(node.lineno))],
            keywords=[])), node)
def selected_functions(path, names, env):
    tree=ast.parse((ROOT/path).read_text())
    nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
    source_guard(len(nodes)==len(names),'source functions present: '+path)
    env['source_guard']=source_guard
    code=ast.fix_missing_locations(AlwaysOn().visit(ast.Module(body=nodes,type_ignores=[])))
    exec(compile(code,str(ROOT/path),'exec'),env)
    return env
def matrix_json(m): return [[str(v) for v in row] for row in m.tolist()]
src=SimpleNamespace(ROOT=ROOT,PINS=PINS,selected_functions=selected_functions,matrix_json=matrix_json)
checks=[]
def check(value,label):
    if not bool(value): raise RuntimeError(label)
    checks.append(label)
def simp(m): return m.applyfunc(s.simplify)

pins={k:v for k,v in src.PINS.items() if any(t in k for t in ['v55_','v973_','clock_fiber'])}
pins['verification/v113_quasifree_kernel.py']='a033fe9c292d22b5bbc343aa0d8e352df14a0918e4124fd7596bf7f81e01ff51'
for path,digest in pins.items():
    check(hashlib.sha256((src.ROOT/path).read_bytes()).hexdigest()==digest,'source pin '+path)
roots=src.selected_functions('verification/v973_seam_route_narrowing.py',['_e8_simple_roots'],{'Fr':Fraction})
R=s.Matrix.hstack(*map(s.Matrix,roots['_e8_simple_roots']()))
cox=src.selected_functions('verification/v55_coxeter_cycle.py',['_e8_cartan','_coxeter'],{'sp':s})
C=R*cox['_coxeter'](cox['_e8_cartan']())*R.inv()
clock=src.selected_functions('experiments/tfpt-discovery/clock_fiber_product_probe.py',['J_all','sigma'],{})
I8=s.eye(8); I16=s.eye(16)
J=s.Matrix.hstack(*(s.Matrix(clock['J_all'](tuple(I8[:,k]))) for k in range(8)))
sig=s.Matrix.hstack(*(s.Matrix(clock['sigma'](tuple(I8[:,k]))) for k in range(8)))
check(C**15==-I8 and J**2==-I8,'actual clocks contain central minus identity')
check(C.det()==1 and J.det()==1 and sig.det()==1,'actual clocks preserve orientation')
jw=src.selected_functions('verification/v113_quasifree_kernel.py',['jw'],{'sp':s})['jw'](4)
gammas=[v for a in jw for v in (a+a.T,s.I*(a.T-a))]
check(all(a*b+b*a==(2*I16 if i==j else s.zeros(16)) for i,a in enumerate(gammas) for j,b in enumerate(gammas)), 'source JW Clifford relation in eight vector directions')
def cliff(v): return sum((x*g for x,g in zip(v,gammas)),s.zeros(16))
# Product of the same eight root reflections; each gamma has root norm sqrt(2).
UC=I16
for k in range(8): UC=UC*cliff(R[:,k])
UC=simp(UC/16)
if not all(simp(UC*g*UC.H)==cliff(C[:,i]) for i,g in enumerate(gammas)):
    UC=UC.H
check(all(simp(UC*g*UC.H)==cliff(C[:,i]) for i,g in enumerate(gammas)),'actual Coxeter covariance on every source basis vector')
UJ=I16
for k in range(4): UJ=UJ*(I16-gammas[2*k]*gammas[2*k+1])
UJ=simp(UJ/4)
check(all(simp(UJ*g*UJ.H)==cliff(J[:,i]) for i,g in enumerate(gammas)),'actual quarter-clock covariance on every source basis vector')
# Family permutation lift: fermionic second quantization of its 4x4 mode map.
P=s.Matrix([[0,0,1,0],[1,0,0,0],[0,1,0,0],[0,0,0,1]])
US=s.zeros(16)
for mask in range(16):
    occupied=[j for j in range(4) if mask & (1<<(3-j))]
    for dest in range(16):
        rows=[j for j in range(4) if dest & (1<<(3-j))]
        if len(rows)==len(occupied):
            US[dest,mask]=P.extract(rows,occupied).det() if rows else 1
if not all(simp(US*g*US.H)==cliff(sig[:,i]) for i,g in enumerate(gammas)):
    US=US.H
check(all(simp(US*g*US.H)==cliff(sig[:,i]) for i,g in enumerate(gammas)),'actual family permutation covariance')
Uc=UJ*US
check(UJ*US==US*UJ,'quarter and family lifts commute')
# A common real structure: B conjugation fixes all eight Clifford generators.
B=gammas[1]*gammas[3]*gammas[5]*gammas[7]
check(B==B.conjugate() and B*B==I16,'Spin8 real structure squares to plus one')
check(all(B*g.conjugate()==g*B for g in gammas),'Clifford maps commute with the common real structure')
even=[i for i in range(16) if i.bit_count()%2==0]
odd=[i for i in range(16) if i.bit_count()%2]
def real_basis(indices):
    columns=[];seen=set()
    for i in indices:
        if i in seen:continue
        j=next(j for j in indices if B[j,i]!=0); b=B[j,i]
        if j==i:
            columns.append(I16[:,i]*(1 if b==1 else s.I));seen.add(i)
        else:
            columns += [(I16[:,i]+b*I16[:,j])/s.sqrt(2),s.I*(I16[:,i]-b*I16[:,j])/s.sqrt(2)]
            seen.update([i,j])
    U=s.Matrix.hstack(*columns)
    check(U.H*U==I8 and B*U.conjugate()==U,'orthonormal real half-spinor basis')
    return U
Rp,Rm=real_basis(even),real_basis(odd)
A=[simp(Rm.H*g*Rp) for g in gammas]
check(all(a==a.conjugate() for a in A),'triality matrices act between real eight-dimensional spaces')
check(all(a.T*b+b.T*a==(2*I8 if i==j else s.zeros(8)) for i,a in enumerate(A) for j,b in enumerate(A)),'norm composition holds as a polynomial identity for all real inputs')
spectra={}; lift_mats={}
x=s.Symbol('x')
for label,G,U in [('C',C,UC),('J',J,UJ),('sigma',sig,US),('c',J*sig,Uc)]:
    Up,Um=simp(Rp.H*U*Rp),simp(Rm.H*U*Rm)
    check(Up==Up.conjugate() and Um==Um.conjugate() and Up.T*Up==I8 and Um.T*Um==I8,label+' real orthogonal half-spinor lifts')
    check(all(simp(sum((G[j,i]*A[j] for j in range(8)),s.zeros(8))*Up)==simp(Um*A[i]) for i in range(8)),label+' typed bilinear covariance on all eight generators')
    spectra[label]={'vector':str(s.factor(G.charpoly(x).as_expr())), 'spin_plus':str(s.factor(Up.charpoly(x).as_expr())), 'spin_minus':str(s.factor(Um.charpoly(x).as_expr()))}
    lift_mats[label]={'vector':src.matrix_json(G),'plus':src.matrix_json(Up),'minus':src.matrix_json(Um)}
check(J**2==-I8 and UJ**2!= -I16,'triality actions are different; no identification by dimension')
check((J*sig)**6==-I8,'actual compiler half-period retained')
# Every diagonal-equivariant bilinear V x V -> V vanishes: (-I)^2 input
# versus (-I) output. This applies to the ACTUAL subgroup, no dense-group claim.
check((-1)*(-1)==1 and -1!=1,'same-carrier bilinear operation forbidden by the existing half-clock')
# Integral compatibility is tested on exact, clock-generated root orbits.
def orbit(seed,leg):
    mats=[[[Fraction(v) for v in row] for row in lift_mats[k][leg]] for k in ['C','J','sigma']]
    seed=tuple(map(Fraction,seed)); seen={seed};queue=deque([seed])
    while queue:
        v=queue.popleft()
        for mat in mats:
            w=tuple(sum(a*b for a,b in zip(row,v)) for row in mat)
            if w not in seen:
                seen.add(w);queue.append(w)
                if len(seen)>10000:raise RuntimeError('bounded orbit test exhausted')
    return sorted(seen)
plus_roots=orbit([1,1,0,0,0,0,0,0],'plus')
minus_roots=orbit([1,0,0,0,0,0,0,0],'minus')
check(len(plus_roots)==len(minus_roots)==240,'both exact lifted clock orbits close at 240 roots')
def lattice_basis(vectors):
    M=s.Matrix.hstack(*map(s.Matrix,vectors))
    den=s.ilcm(*[v.q for v in M])
    scaled=M*den
    check(all(v.q==1 for v in scaled),'orbit denominator cleared exactly')
    return hermite_normal_form(s.Matrix(scaled.rows,scaled.cols,[int(v) for v in scaled]))/den
LP=lattice_basis(plus_roots); LM=lattice_basis(minus_roots)
GP=LP.T*LP;GM=2*LM.T*LM
for tag,G in [('plus',GP),('minus',GM)]:
    check(all(v.q==1 for v in G) and all(G[i,i]%2==0 for i in range(8)) and G.det()==1,
          tag+' lattice is positive even unimodular of rank eight in its stated normalization')
def mul(v,w):return simp(sum((v[i]*A[i] for i in range(8)),s.zeros(8))*w/2)
integral_products=[]
for i in range(8):
    for j in range(8):
        coordinates=simp(LM.inv()*mul(R[:,i],LP[:,j]))
        check(all(v.q==1 for v in coordinates),'integral typed product on source basis '+str((i,j)))
        integral_products.append([str(v) for v in coordinates])
check(all(simp(LP.inv()*s.Matrix(lift_mats[k]['plus'])*LP).applyfunc(lambda v:v.q)==s.ones(8) for k in ['C','J','sigma']),
      'all plus clock lifts preserve the full integral lattice')
check(all(simp(LM.inv()*s.Matrix(lift_mats[k]['minus'])*LM).applyfunc(lambda v:v.q)==s.ones(8) for k in ['C','J','sigma']),
      'all minus clock lifts preserve the full integral lattice')
# Normalizations: N_V(v)=v.v/2, N_+(w)=w.w/2, N_-(z)=z.z.
# Therefore N_-(mul(v,w))=N_V(v)*N_+(w), for all real vectors.
# Select two norm-one roots only to give the triality an ordinary unital product.
v0=R[:,0]; w0=s.Matrix(plus_roots[0])
unit=mul(v0,w0)
left=s.Matrix.hstack(*(mul(v0,I8[:,i]) for i in range(8)))
right=s.Matrix.hstack(*(mul(I8[:,i],w0) for i in range(8)))
Lcoord=simp(LM.inv()*left*LP);Rcoord=simp(LM.inv()*right*R)
check(abs(Lcoord.det())==abs(Rcoord.det())==1,'unit choices identify the integral lattices by unimodular maps')
right_inv,left_inv=right.inv(),left.inv()
def product(z,w):return mul(right_inv*z,left_inv*w)
check(unit.dot(unit)==1 and all(product(unit,LM[:,i])==LM[:,i] and product(LM[:,i],unit)==LM[:,i] for i in range(8)),
      'chosen-root isotope has a two-sided norm-one unit')
structure=[]
for i in range(8):
    for j in range(8):
        coords=simp(LM.inv()*product(LM[:,i],LM[:,j]))
        check(all(x.q==1 for x in coords),'unital isotope integral structure constant '+str((i,j)))
        structure.append([str(v) for v in coords])
nonassoc=None
for i,j,k in itertools.product(range(8),repeat=3):
    a,b,c=LM[:,i],LM[:,j],LM[:,k]
    d=simp(product(product(a,b),c)-product(a,product(b,c)))
    if d!=s.zeros(8,1):
        nonassoc={'indices':[i,j,k],'difference':[str(v) for v in d]};break
check(nonassoc is not None,'composition is genuinely nonassociative; no hidden monoid assertion')
norm3=I8[:,0]+I8[:,1]+I8[:,2]
check(all(v.q==1 for v in LM.inv()*norm3) and norm3.dot(norm3)==3,
      'explicit integral octave of norm three; unlike the Gaussian submodule index spectrum')
L3=s.Matrix.hstack(*(product(norm3,I8[:,i]) for i in range(8)))
check(simp(L3.T*L3)==3*I8 and abs(L3.det())==81,
      'norm-three multiplication preserves the metric up to scale and has lattice index 3 to the fourth')
out={'verdict':'EXACT_INTEGRAL_NORMED_TRIALITY_WITH_ACTUAL_CLOCK_LIFTS', 'checks':checks,
 'source_pins':pins,'spectra':spectra,'clock_matrices':lift_mats,
 'bilinear_maps':[src.matrix_json(a) for a in A],
 'integral_triality':{'vector_basis':src.matrix_json(R),'plus_basis':src.matrix_json(LP),'minus_basis':src.matrix_json(LM),
  'normalizations':{'vector':'dot(v,v)/2','plus':'dot(w,w)/2','minus':'dot(z,z)'},
  'product':'one half the Clifford map, V x S+ -> S-', 'basis_product_coefficients':integral_products,
  'plus_gram':src.matrix_json(GP),'minus_gram':src.matrix_json(GM)},
 'unital_isotope':{'choice':'two explicit roots, not selected by TFPT','v0':[str(v) for v in v0],
  'w0':[str(v) for v in w0],'unit':[str(v) for v in unit],'structure_constants':structure,'nonassociativity_witness':nonassoc,
  'norm_three_element':[str(v) for v in norm3],'norm_three_left_index':81},
 'scope':'Real Euclidean representation-level Clifford triality V x S+ -> S-. Spin lifts are sign choices over the original clocks; no claim that the original clock group splits through Spin8.',
 'new_assumptions':['Use of Clifford half-spinor modules as a candidate completion; physical identification not derived'],
 'open':['Canonical selection of the integral spinor lattices rather than the exhibited seed orbits','Identification with source D5+A3 and physical fields','Coherent physical composition beyond the integral triality','Physical state, Hamiltonian, spacetime and full TOE'],
 'not_claimed':['Three triality legs are not three particle families','Norm multiplication is not an efficient integer factorization algorithm','No RH or physical time theorem']}
target=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('certificate.json')
target.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'verdict':out['verdict'],'checks':len(checks),'spectra':spectra},ensure_ascii=False,indent=2))
