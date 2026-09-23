"""NON-RH: source E8 glue, tetrahedral projection, and translation obstructions.

Only a small exact lattice calculation. Regular/projective translations are
typed as an added representation, not obtained from a finite Lie bracket.
"""
import argparse
import ast
from collections import Counter
from fractions import Fraction as F
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CHECKS = []


def need(ok, message):
    if not bool(ok):
        raise RuntimeError(message)
    CHECKS.append(message)


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def add(x,y):
    return tuple(a+b for a,b in zip(x,y))


def sub(x,y):
    return tuple(a-b for a,b in zip(x,y))


def gram(vs):
    return s.Matrix([[dot(v,w) for w in vs] for v in vs])


def in_D5(v):
    return all(x.denominator == 1 for x in v) and sum(v) % 2 == 0


def in_A3(v):
    return all(x.denominator == 1 for x in v) and sum(v) == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out',default='verification.json')
    args = ap.parse_args()
    path = ROOT/'verification/v128_graded_hull.py'
    tree = ast.parse(path.read_text())
    fn = next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name == 'build_roots')
    env = {'F':F,'HALF':F(1,2),'combinations':combinations,'product':product}
    exec(compile(ast.fix_missing_locations(ast.Module(body=[fn],type_ignores=[])),str(path),'exec'),env)
    roots = env['build_roots']()
    need(len(roots) == 240 and Counter(roots.values()) == Counter({0:52,1:64,2:60,3:64}), 'unchanged original E8 root builder and four grade counts')
    need(all(dot(a,a)+dot(b,b) == 2 for a,b in roots), 'all original240 roots norm squared2')
    mu = [tuple(F(int(i==a))-F(1,4) for i in range(4)) for a in range(4)]
    Gmu = gram(mu)
    need(Gmu == s.eye(4)-s.ones(4)/4, 'four defining-representation weights form tetrahedron')
    R = s.Matrix([[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])/2
    need(R*R.T == s.eye(3) and R.T*R == s.eye(4)-s.ones(4)/4, 'explicit isometry of A3 real weight hyperplane to R3')
    bcc = [tuple(R*s.Matrix(v)) for v in mu]
    need(bcc == [(s.Rational(1,2),s.Rational(1,2),s.Rational(1,2)),(s.Rational(1,2),-s.Rational(1,2),-s.Rational(1,2)),(-s.Rational(1,2),s.Rational(1,2),-s.Rational(1,2)),(-s.Rational(1,2),-s.Rational(1,2),s.Rational(1,2))], 'tetrahedral half-integer BCC steps exactly')
    p_basis = s.Matrix.hstack(*(s.Matrix(v) for v in bcc[:3]))
    q_basis = s.Matrix.hstack(*(s.Matrix(bcc[i])-s.Matrix(bcc[i+1]) for i in range(3)))
    need(abs(p_basis.det()) == s.Rational(1,2) and abs(q_basis.det()) == 2, 'BCC weight covolume onehalf and FCC root covolume2')
    need(abs(q_basis.det()/p_basis.det()) == 4, 'P(A3)/Q(A3) index4')
    need(all((p_basis.inv()*s.Matrix(e)).applyfunc(lambda x:int(x.is_integer)) == s.ones(3,1) for e in [(1,0,0),(0,1,0),(0,0,1)]), 'integer cubic lattice contained in generated weight lattice')
    # The pure fundamental A3 move fails the diagonal E8 glue condition.
    spin0 = (F(1,2),)*5
    def in_E8_glue(d,a):
        return any(in_D5(tuple(x-k*y for x,y in zip(d,spin0))) and in_A3(tuple(x-k*y for x,y in zip(a,mu[0]))) for k in range(4))
    z5 = (F(0),)*5
    need(all(not in_E8_glue(z5,m) for m in mu), 'all pure fundamental A3 shifts forbidden by original diagonal glue')
    need(all(in_E8_glue(spin0,m) for m in mu), 'all four spinor-dressed fundamental weights are allowed E8 roots')
    need(all(in_D5(tuple(-k*x for x in spin0)) == (k==0) for k in range(4)), 'fixed exact D5 coordinate forces zero discriminant grade')
    need(all(in_E8_glue(z5,sub(mu[a],mu[b])) and in_A3(sub(mu[a],mu[b])) for a,b in combinations(range(4),2)), 'pure neutral A3 differences are allowed FCC root steps')
    signs = [(1,1,1,1,1),(-1,-1,1,1,1),(1,-1,-1,-1,-1),(-1,1,-1,-1,-1)]
    spins = [tuple(F(x,2) for x in row) for row in signs]
    lam = [spins[a]+mu[a] for a in range(4)]
    need(all(row.count(-1)%2 == 0 for row in signs), 'all selected charges in same D5 spinor chirality')
    need(all((spins[a],mu[a]) in roots and roots[(spins[a],mu[a])] == 1 for a in range(4)), 'four selected lifts are actual grade1 source E8 roots')
    need(tuple(map(sum,zip(*lam))) == (0,)*9, 'spatial tetrahedral loop closes in full E8 charge as well')
    expected = s.Matrix([[2,0,-1,-1],[0,2,-1,-1],[-1,-1,2,0],[-1,-1,0,2]])
    Glam = gram(lam)
    need(Glam == expected and Glam.rank() == 3, 'full-charge Gram is affine A3 cycle and rank3')
    need(Glam[:3,:3].det() == 4, 'lifted rank3 lattice has FCC A3 root metric determinant4')
    need(Glam != Gmu, 'projection to tetrahedral BCC is not isometric in E8 metric')
    need(s.Matrix.hstack(*(s.Matrix(v) for v in spins[:3])).rank() == 3, 'closed section changes D5 charge along every nonzero displacement')
    for a,b in combinations(range(4),2):
        need(sub(spins[a],spins[b]) != z5, 'FCC difference is not exact D5-neutral for closed section '+str((a,b)))
    constant = [spin0+m for m in mu]
    need(tuple(map(sum,zip(*constant))) == (F(2),)*5+(F(0),)*4, 'constant-spinor dressing leaves residual four-spinor charge on spatially closed loop')
    need(all(sub(constant[a],constant[b]) == z5+sub(mu[a],mu[b]) for a,b in combinations(range(4),2)), 'constant dressing has exact neutral FCC differences')
    need(all(dot(add(constant[a],constant[b]),add(constant[a],constant[b])) == 6 for a,b in combinations(range(4),2)), 'constant dressing does not even supply g1g1-to-root primitive on distinct directions')
    # Explicit closed chain uses existing root-sum support; its final
    # opposite-root bracket is Cartan, not an identity translation.
    order = [0,2,1,3]
    partial = (F(0),)*9
    partials = []
    for step,a in enumerate(order):
        partial = add(partial,lam[a])
        partials.append(partial)
        if step < 3:
            need((partial[:5],partial[5:]) in roots, 'closed lift partial sum is source root at step'+str(step+1))
            need(roots[(partial[:5],partial[5:])] == (step+1)%4, 'partial root has expected Z4 grade at step'+str(step+1))
    need(partial == (0,)*9 and partials[2] == tuple(-x for x in lam[3]), 'last primitive root pair is opposite and brackets to Cartan')
    # With the standard even-lattice cocycle the commutator is
    # epsilon(l,m)/epsilon(m,l)=(-1)^(l.m). This is invariant under cochains.
    parity = Glam.applyfunc(lambda x:int(x)%2)
    need(parity == s.Matrix([[0,0,1,1],[0,0,1,1],[1,1,0,0],[1,1,0,0]]), 'pullback cocycle has nontrivial alternating mod2 pairing')
    need(dot(lam[0],lam[2]) == -1, 'explicit primitive magnetic-translation commutator is minus1')
    X,Z = s.Matrix([[0,1],[1,0]]),s.diag(1,-1)
    comps = [X,X,Z,Z]
    need(all(comps[a]*comps[b] == (-1)**(int(Glam[a,b])%2)*comps[b]*comps[a] for a in range(4) for b in range(4)), 'two-dimensional matrices realize the commutator bicharacter exactly')
    need(X*Z*X*Z == -s.eye(2), 'one-dimensional scalar compensation impossible for minus1 commutator')
    B = parity[:3,:3]
    bits = list(product(range(2),repeat=3))
    radical = [n for n in bits if all(int(x)%2 == 0 for x in B*s.Matrix(n))]
    need(radical == [(0,0,0),(1,1,0)], 'three-generator alternating pairing has GF2 rank2 and index4 radical')
    # An explicit cocycle representative with the inherited commutator.
    # Its symmetric part is a gauge choice, not the source basis convention.
    def eps(n,m):
        return (-1)**((n[2]*(m[0]+m[1]))%2)
    def rho(n):
        return X**(n[0]+n[1])*Z**n[2]
    samples = list(product(range(-1,2),repeat=3))
    need(all(rho(n)*rho(m) == eps(n,m)*rho(add(n,m)) for n in samples for m in samples), 'explicit C2 projective representation obeys chosen cocycle on 729 signed pairs')
    need(all(eps(n,m)*eps(add(n,m),k) == eps(m,k)*eps(n,add(m,k)) for n in bits for m in bits for k in bits), 'chosen bilinear cocycle satisfies all 512 binary associativity checks')
    fourth = (-1,-1,-1)
    need(rho(fourth) == Z and X*X*Z*rho(fourth) == s.eye(2), 'lambda4 minus sum of first3 has exact ordered zero-loop phase plus1 in this gauge')
    need(X*Z*X*rho(fourth) == -s.eye(2), 'interchanged zero-loop phase is minus1 in same gauge')
    # A diagonal-normalized even-lattice cocycle has epsilon(ei,ei)=-1.
    def qphase(n):
        return (-1)**(sum(x*(x-1)//2 for x in n)%2)
    def eps_diag(n,m):
        return (-1)**((sum(x*y for x,y in zip(n,m))+n[2]*(m[0]+m[1]))%2)
    def rho_diag(n):
        return qphase(n)*rho(n)
    need(all(rho_diag(n)*rho_diag(m) == eps_diag(n,m)*rho_diag(add(n,m)) for n in samples for m in samples), 'cochain-related diagonal-normalized gauge obeys exact product law on 729 signed pairs')
    need(rho_diag(fourth) == -Z and X*X*Z*rho_diag(fourth) == -s.eye(2), 'zero-loop absolute phase changes with chosen root-vector gauge but ordering ratio remains minus1')
    need(s.Matrix.hstack(*(s.Matrix(v).reshape(4,1) for v in [s.eye(2),X,Z,X*Z])).rank() == 4, 'projective fiber generates M2 and is irreducible')
    output = (HERE/args.out).resolve()
    need(output.parent == HERE, 'output confined to own native report directory')
    result = {'status':'EXACT_SMALL_GRADED_TRANSLATION_BRIDGE_AND_OBSTRUCTIONS','check_count':len(CHECKS),'checks':CHECKS,
        'source_hash':hashlib.sha256(path.read_bytes()).hexdigest(),
        'mu_weights':[[str(x) for x in row] for row in mu], 'BCC_steps':[[str(x) for x in row] for row in bcc],
        'spinor_lift_signs':signs,'weight_Gram':[[str(x) for x in row] for row in Gmu.tolist()],
        'E8_lift_Gram':Glam.tolist(),'mod2_pairing':parity.tolist(),'independent_mod2_radical':radical,'minimal_projective_irrep_dimension':2,'root_sum_loop_order_zero_based':order,
        'loop_partial_grades':[1,2,3,0],'constant_dressing_loop_residual':['2']*5+['0']*4,
        'three_way_incompatibility':'fundamental grade1 lifts + every exact D5-neutral FCC difference + zero tetrahedral loop cannot all hold for fixed additive lifts',
        'cocycle_scope':'standard even-lattice cocycle assumed as inherited phase contract; its alternating bicharacter is exact from this Gram',
        'explicit_projective_gauge':'epsilon(n,m)=(-1)^(n3*(m1+m2)); rho(n)=X^(n1+n2)*Z^n3; rho(lambda4)=Z; ordered1234loop=+I, ordered1324loop=-I',
        'diagonal_normalized_gauge':'epsilon_diag adds sum(ni*mi) to exponent; rho_diag(n)=(-1)^sum(binomial(ni,2))*rho(n); rho_diag(lambda4)=-Z; ordered1234loop=-I',
        'two_dimensional_fiber_scope':'already minimal irreducible projective fiber after a central character is chosen, not necessarily an externally added coin; spatial address interpretation and dynamics remain inputs',
        'required_extra_for_ordinary_translation':'an infinite/scaling address representation and removal/compensation of nontrivial cocycle; two-dimensional phase compensation is minimal for this rank2 mod2 pairing',
        'finite_Lie_vertex_is_regular_shift':False,'native_spatial_translation_derived':False,'Weyl_walk_derived':False,'global_TOE_no_go':False}
    output.write_text(json.dumps(result,indent=2,default=str)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2,default=str))


if __name__ == '__main__':
    main()
