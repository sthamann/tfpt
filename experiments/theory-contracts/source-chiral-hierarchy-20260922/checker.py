#!/usr/bin/env python3
"""Exact finite algebra checks. General theorems are proved in PROOF.md.

No source selection, 4D matter construction, or physical mass prediction.
Fixtures are diagnostics of theorem scope, not proposed TFPT models.
"""
import argparse
import ast
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

u = s.Symbol('u', real=True)
checks = []


def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)


def zero(expr):
    if isinstance(expr, s.MatrixBase):
        return all(s.simplify(v) == 0 for v in expr)
    return s.simplify(expr) == 0


def skew(h):
    x, y, z = h
    return s.Matrix([[0, z, -y], [-z, 0, x], [y, -x, 0]])


def vertex(c, h):
    a = skew(h)
    return c.T * a - a * c


def order(poly):
    poly = s.cancel(poly)
    if poly == 0:
        return s.oo
    num, den = s.fraction(poly)
    return min(p[0] for p, _ in s.Poly(num, u).terms()) - min(
        p[0] for p, _ in s.Poly(den, u).terms())


def valuations(y):
    result = []
    for k in range(1, y.rows + 1):
        result.append(min(order(y.extract(ii, jj).det())
                          for ii in itertools.combinations(range(y.rows), k)
                          for jj in itertools.combinations(range(y.cols), k)))
    return result


def read_decl(path, name):
    tree = ast.parse(path.read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return eval(compile(ast.Expression(node.value), str(path), 'eval'),
                        {'__builtins__': {}, 'sp': s, 'II': s.I})
    raise RuntimeError('Missing original declaration: ' + name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', type=Path,
                        default=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4'))
    args = parser.parse_args()
    source = args.repo / 'verification/v117_monodromy_weyl_a3.py'
    m = read_decl(source, 'M0_EXACT')
    deck = read_decl(source, 'U_EXACT')
    require(zero(m.H*m - s.eye(3)), 'original_M_unitary')
    require(zero(deck.H*deck - s.eye(3)), 'original_U_unitary')
    require(zero(m**3-s.eye(3)), 'original_M_order_divides_3')
    require(zero(deck**4-s.eye(3)), 'original_U_order_divides_4')
    ms = [deck**k*m*deck**(-k) for k in range(4)]
    prod = s.eye(3)
    for mk in ms:
        prod = prod * mk
    require(zero(prod-s.eye(3)), 'original_four_puncture_product')
    aor = s.simplify(sum((mk-mk.H for mk in ms), s.zeros(3))/(4*s.I))
    require(aor == s.diag(0, -1, 1), 'attachment_oriented_operator')

    # Full complex offdiagonal identity, not a numerical sample.
    ar, ai, br, bi, cr, ci = s.symbols('ar ai br bi cr ci', real=True)
    a, b, c = ar+s.I*ai, br+s.I*bi, cr+s.I*ci
    yy = s.Matrix([[0,a,b],[a,0,c],[b,c,0]])
    hh = yy.H*yy
    require(s.expand(2*s.trace(hh*hh)-s.trace(hh)**2) == 0,
            'general_complex_zero_diagonal_Heron_identity')
    x, y, z = s.symbols('x y z', real=True)
    heron = (x+y+z)*(-x+y+z)*(x-y+z)*(x+y-z)
    require(s.expand(heron - (2*(x*x*y*y+x*x*z*z+y*y*z*z)
                                 -(x**4+y**4+z**4))) == 0,
            'ordered_singular_value_triangle_factorization')

    h = s.Matrix(s.symbols('h0:3'))
    lam = s.symbols('l0:3')
    diagonal_vertex = vertex(s.diag(*lam), h)
    require(diagonal_vertex == diagonal_vertex.T,
            'diagonal_clock_vertex_symmetric')
    require(all(diagonal_vertex[i,i] == 0 for i in range(3)),
            'diagonal_clock_vertex_zero_diagonal')
    require(any(v != 0 for v in diagonal_vertex), 'vertex_is_not_trivially_zero')
    require(zero(diagonal_vertex.det()-2*s.det(s.Matrix.hstack(
        h, s.diag(*lam)*h, s.diag(*lam)**2*h))),
        'known_cyclicity_identity_in_eigenbasis')

    # Original generators at general complex h; exact identity after expansion.
    hv = s.Matrix([ar+s.I*ai,br+s.I*bi,cr+s.I*ci])
    for name, cl in [('M',m),('U',deck),('MU',m*deck)]:
        vv = vertex(cl,hv)
        gram = vv.H*vv
        require(s.expand(2*s.trace(gram*gram)-s.trace(gram)**2) == 0,
                'original_'+name+'_all_complex_h_triangle')

    # One analytic original-clock response: orders (2,2,5), NOT (2,3,5).
    clock_fixture = u**2*vertex(deck,s.Matrix([1,u**3,1]))
    require(valuations(clock_fixture) == [2,4,9],
            'original_clock_analytic_orders_2_2_5')
    target = s.diag(s.Rational(7,6)*u**2,s.Rational(4,3)*u**3,
                    s.Rational(16,7)*u**5)
    require(valuations(target) == [2,5,10], 'target_minor_orders')
    require(not zero(2*s.trace((target.H*target)**2)
                     -s.trace(target.H*target)**2),
            'target_rejected_by_triangle_identity')

    # Do not overextend to all C: nonnormal varying matrices escape.
    cn = s.Matrix([[0,u**3/2,u**4],[-u**2/2,0,0],[0,0,0]])
    yn = vertex(cn,s.Matrix([0,0,1]))
    require(yn == s.Matrix([[u**2,0,0],[0,u**3,u**4],[0,u**4,0]]),
            'nonnormal_scope_control_vertex')
    require(valuations(yn) == [2,5,10], 'nonnormal_scope_control_orders')
    require(not zero(cn.H*cn-cn*cn.H), 'nonnormal_control_really_nonnormal')
    fixed_q = s.Matrix([[3,1,0],[3,2,0],[3,2,1]])
    sig = s.diag(1,-1,-1)
    discriminants = {}
    for name, cl in [('Q',fixed_q),('Qplus',(fixed_q+sig*fixed_q*sig)/2),
                     ('Qminus',(fixed_q-sig*fixed_q*sig)/2)]:
        cp = cl.charpoly()
        disc = s.discriminant(cp.as_expr(),cp.gen)
        require(disc != 0, name+'_simple_spectrum')
        discriminants[name] = str(disc)

    # Exact regular changes of fields preserve minors' orders.
    left = s.Matrix([[1,u,0],[0,1,u],[0,0,1]])
    right = s.Matrix([[1,0,0],[u,1,0],[0,u,1]])
    require(left.det() == right.det() == 1, 'regular_fixture_invertible')
    require(valuations(left*target*right) == [2,5,10],
            'regular_mixed_target_preserves_orders')
    require(valuations(left*clock_fixture*right) == [2,4,9],
            'regular_mixed_clock_cannot_acquire_target_orders')
    # These positive factors are exactly inverse square roots of analytic Z.
    pos_l = s.diag(1+u,1,1)
    pos_r = s.diag(1,1+2*u,1)
    require(valuations(pos_l*target*pos_r) == [2,5,10],
            'positive_regular_kinetic_factors_preserve_orders')

    # General coefficient algebra of the two-step Schur test.
    aa, a1 = s.symbols('aa a1', nonzero=True)
    r1=s.Matrix(1,2,s.symbols('r1_0:2')); r2=s.Matrix(1,2,s.symbols('r2_0:2'))
    c1=s.Matrix(2,1,s.symbols('c1_0:2')); c2=s.Matrix(2,1,s.symbols('c2_0:2'))
    d1=s.Matrix(2,2,s.symbols('d1_0:4'))
    d2=s.Matrix(2,2,s.symbols('d2_0:4'))
    d3=s.Matrix(2,2,s.symbols('d3_0:4'))
    exact=u*d1+u**2*d2+u**3*d3-(u*c1+u**2*c2)*(u*r1+u**2*r2)/(aa+u*a1)
    rhat2=d2-c1*r1/aa
    rhat3=d3-(c1*r2+c2*r1)/aa+a1*c1*r1/aa**2
    truncated=exact.applyfunc(lambda v:s.series(v,u,0,4).removeO())
    require(zero(truncated-(u*d1+u**2*rhat2+u**3*rhat3)),
            'general_first_Schur_coefficients_through_order3')
    bb, t11,t12,t21,t22,k11,k12,k21,k22=s.symbols('bb t11 t12 t21 t22 k11 k12 k21 k22')
    rr=u*s.diag(bb,0)+u**2*s.Matrix([[t11,t12],[t21,t22]])+u**3*s.Matrix([[k11,k12],[k21,k22]])
    light=rr[1,1]-rr[1,0]*rr[0,1]/rr[0,0]
    light3=s.series(light,u,0,4).removeO()
    require(zero(light3-(u**2*t22+u**3*(k22-t21*t12/bb))),
            'general_second_Schur_light_coefficient')
    # Meaningful failure controls: a forbidden u4 term or missing third opening.
    early=target+s.diag(0,0,u**4)
    absent=s.diag(s.Rational(7,6)*u**2,s.Rational(4,3)*u**3,0)
    require(valuations(early) == [2,5,9], 'early_light_direction_fails_target')
    require(valuations(absent) == [2,5,s.oo], 'missing_light_direction_fails_target')

    # Same actual marked Aor, different covariant analytic couplings: only
    # counterexamples to selection from covariance, NOT full P1/P2 models.
    p0=s.eye(3)-aor*aor; pp=(aor*aor+aor)/2; pm=(aor*aor-aor)/2
    cov=s.Rational(7,6)*u**2*pp+s.Rational(4,3)*u**3*pm+s.Rational(16,7)*u**5*p0
    require(valuations(cov) == [2,5,10], 'covariance_target_can_be_inserted')
    require(valuations(cov+u**4*p0) == [2,5,9],
            'same_marks_covariance_do_not_select_orders')

    phi=1/(6*s.pi)+3/(256*s.pi**4)
    rmu=8*phi/7; re=96*phi**3/49
    require(0 < float((rmu+re).evalf()) < 1,
            'finite_target_fails_bare_normal_clock_sum')
    pins=[
        'verification/v117_monodromy_weyl_a3.py',
        'tfpt_2_standard_model.tex',
        'experiments/theory-contracts/source-native-clock-flavor-bridge-20260922/PROOF.md',
        'experiments/theory-contracts/source-native-retarded-selection-20260922/PROOF.md',
        'experiments/theory-contracts/rr-three-family-state-20260921/HERLEITUNG.md',
        'experiments/theory-contracts/source-variation-origin-gate-20260922/PROOF.md',
        '_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex',
        '_archive/tfpt-45/source_extracts/02_carrier_source.tex']
    result={
        'research_id':'UR.SOURCE.CHIRAL_HIERARCHY.01',
        'verdict':'PARTIAL', 'finite_algebra_checks':'PASS',
        'complete_TFPT_solution':False, 'physical_gates_closed':[],
        'count':len(checks),'checks':checks,
        'new_scoped_theorem':'For any normal 3x3 C and complex h: s1=s2+s3 for C^T A(h)-A(h) C; analytic orders alpha1=alpha2 remain under regular normalization.',
        'target_minor_orders':[2,5,10],
        'original_clock_fixture_minor_orders':[2,4,9],
        'nonnormal_scope_control_minor_orders':[2,5,10],
        'simple_spectrum_discriminants':discriminants,
        'phi0':str(s.N(phi,25)),
        'target_mu_plus_e_over_tau':str(s.N(rmu+re,25)),
        'necessary_sqrt_kinetic_condition_product_for_finite_fit':str(s.N(1/(2*rmu),25)),
        'source_hashes':{p:hashlib.sha256((args.repo/p).read_bytes()).hexdigest() for p in pins},
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python_dependency':{'sympy':s.__version__},
        'scope':'General proofs in PROOF.md; fixtures are not physical models. No native gap replay; no source/field selection; no finite-u normalization exclusion without bounds.'}
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
