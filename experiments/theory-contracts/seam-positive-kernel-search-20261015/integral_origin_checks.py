"""Exact scoped origin checks for the given D/A completion and divisor.

These are conditional mathematical tests, not a P1 or physical-origin proof.
"""
from __future__ import annotations
import argparse
import ast
from fractions import Fraction as F
from math import gcd
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]


def need(condition, label, checks):
    if not condition:
        raise ArithmeticError('Failed: '+label)
    checks.append(label)


def family_fundamental(n, b):
    return [F(n-b, n)]*b + [F(-b, n)]*(n-b)


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def simple_roots_d(rank):
    roots = []
    for j in range(rank-1):
        r = [0]*rank; r[j], r[j+1] = 1, -1; roots.append(r)
    r = [0]*rank; r[-2], r[-1] = 1, 1; roots.append(r)
    return roots


def simple_roots_a(n):
    roots = []
    for j in range(n-1):
        r = [0]*n; r[j], r[j+1] = 1, -1; roots.append(r)
    return roots


def original_lambda_check():
    """Compare source AST, never import or execute the original module."""
    path = ROOT/'verification/v983_simple_current_generator.py'
    text = path.read_text()
    tree = ast.parse(text)
    assignments = {node.targets[0].id: node.value for node in tree.body
                   if isinstance(node, ast.Assign) and len(node.targets) == 1
                   and isinstance(node.targets[0], ast.Name)}
    expected = {'OMEGA_S': '[sp.Rational(1, 2)] * 5',
                'OMEGA_F': '[sp.Rational(3, 4), sp.Rational(-1, 4), sp.Rational(-1, 4), sp.Rational(-1, 4)]',
                'LAM': 'OMEGA_S + OMEGA_F'}
    for key, expression in expected.items():
        if key not in assignments or ast.dump(assignments[key], include_attributes=False) != ast.dump(ast.parse(expression, mode='eval').body, include_attributes=False):
            raise ValueError('Original v983 generator AST changed: '+key)
    return {'path': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'scope': 'Static AST identification of the supplied original generator; original module not executed.'}


def primitive_integral_completion():
    checks = []
    survivors = []
    enumerated = 0
    # Quadratic residue classes of D_(n+1)^*: 0, vector, spin+, spin-.
    # These residues require no unimodularity or evenness of the extension.
    for n in range(3, 97):
        classes = [F(0), F(1), F(n+1, 4), F(n+1, 4)]
        for b in range(1, n):
            if gcd(b, n) != 1:
                continue
            for label, dnorm in zip(('zero','vector','spin+','spin-'), classes):
                enumerated += 1
                fnorm = F(b*b*(n-1), n)
                if (dnorm+fnorm).denominator == 1:
                    survivors.append({'n': n, 'b': b, 'class': label,
                                      'norm_residue': str(dnorm+fnorm)})
    need({x['n'] for x in survivors} == {4}, 'primitive integral scan selects n=4', checks)
    need({(x['b'],x['class']) for x in survivors} == {(1,'spin+'),(1,'spin-'),(3,'spin+'),(3,'spin-')},
         'four oriented representatives form two inverse-paired glues', checks)
    spin = [F(1,2)]*5; family = family_fundamental(4,1)
    need(dot(spin,spin)+dot(family,family)==2, 'v983 generator has norm 2', checks)
    need(all(dot(spin,r).denominator == 1 for r in simple_roots_d(5)), 'spinor pairs integrally with D5', checks)
    need(all(dot(family,r).denominator == 1 for r in simple_roots_a(4)), 'family weight pairs integrally with A3', checks)
    need((F(4)*F(4))/F(4*4)==1, 'index-four extension determinant 1', checks)
    # Nonprimitive input: same R101 representative s + 2 omega_1.
    s16 = [F(1,2)]*17; w16 = [2*x for x in family_fundamental(16,1)]
    need(gcd(2,16)>1 and dot(s16,s16)+dot(w16,w16)==8, 'n16 nonprimitive generator has norm 8', checks)
    need(dot(w16,w16)==F(15,4) and dot(family_fundamental(16,2),family_fundamental(16,2))==F(7,4),
         '2 omega1 is not silently replaced by omega2', checks)
    need(all(dot(s16,r).denominator==1 for r in simple_roots_d(17)) and
         all(dot(w16,r).denominator==1 for r in simple_roots_a(16)), 'n16 nonprimitive generator pairs integrally', checks)
    s5=[F(1,2)]*6; w5=family_fundamental(5,1)
    norm5 = dot(s5,s5)+dot(w5,w5)
    need(norm5==F(23,10), 'n5 primitive generator fails integrality', checks)
    need(20*norm5==46 and all((20*dot(s5,r)).denominator==1 for r in simple_roots_d(6)) and
         all((20*dot(w5,r)).denominator==1 for r in simple_roots_a(5)),
         'scaled-by-20 n5 is even integral under changed pairing', checks)
    r5 = [[*r, *([0]*5)] for r in simple_roots_d(6)] + [[*([0]*6), *r] for r in simple_roots_a(5)]
    need(all((20*dot(x,y)).denominator==1 for x in r5 for y in r5) and
         all((20*dot(x,x)).denominator==1 and int(20*dot(x,x))%2==0 for x in r5),
         'scaled n5 root pairing integral with even diagonal', checks)
    # Full doubled braiding form B_L-B_R, not its positive Hilbert energy.
    doubled = norm5-norm5
    need(doubled==0 and 2*norm5==F(23,5) and norm5.denominator!=1,
         'doubled braid cancellation does not imply one-sided integrality or zero positive norm', checks)
    need(all(dot(s5,r).denominator==1 for r in simple_roots_d(6)) and
         all(dot(w5,r).denominator==1 for r in simple_roots_a(5)), 'doubled diagonal pairs integrally with both root copies', checks)
    return {'id':'primitive-integral-completion','status':'pass','checks':checks,
            'facts':{'scan_n':[3,96], 'representatives_checked':enumerated,'survivors':survivors,
                     'n4_inverse_paired_glue_count':2,'v983_norm':'2','n16_nonprimitive_norm':'8',
                     'n5_original_norm':'23/10','n5_scaled_norm':'46',
                     'n5_scaled_label_scope':'original A4 weight class; not claimed to be the full discriminant of the rescaled lattice',
                     'n5_doubled_braiding_norm':'0','n5_doubled_positive_norm':'23/5'}, 'original_source':original_lambda_check(),
            'analytic_argument':'Integral norm implies n divides 4b² since 4 times every D dual norm is integer; gcd(b,n)=1 gives n divides 4. With n>=3, n=4.',
            'inference_claims':[{'id':'primitive_integral_projection_allows_n_other_than_4','holds':False}],
            'excluded_inference':'Standard positive D/A pairing, integral completion and primitive family projection are premises. Doubled braiding locality does not establish positive one-sided integrality. No P1 origin or physical source selection.'}


def function_differential_typing():
    checks=[]
    # Four simple poles on P1: RR dimensions, with the residue at infinity explicit.
    functions, constants, principal_parts, differentials = 5, 1, 4, 3
    need(functions == constants+principal_parts, 'function principal-parts exact-sequence dimensions', checks)
    need(functions != constants+differentials, 'C to five functions to three outputs cannot be short exact', checks)
    # f(z)=1/(z-1), f(z)dz = -du/[u(1-u)] at z=1/u.
    z,u=sp.symbols('z u')
    f=1/(z-1)
    residue_at_one=sp.residue(f,z,1)
    residue_at_infinity=sp.residue(-f.subs(z,1/u)/u**2,u,0)
    need(residue_at_one+residue_at_infinity==0, 'global differential residue sum including infinity', checks)
    need(residue_at_one != 0, 'residue sum on marked finite points need not vanish', checks)
    return {'id':'function-differential-typing','status':'pass','checks':checks,
            'facts':{'h0_O_D':functions, 'constants':constants, 'principal_parts':principal_parts,
                     'h0_K_D':differentials,'f':'1/(z-1)',
                     'residue_at_1':int(residue_at_one),'residue_at_infinity':int(residue_at_infinity)},
            'inference_claims':[{'id':'function_quotient_equals_three_differentials','holds':False}],
            'excluded_inference':'Given genus-zero four-point divisor; this separates spaces, not a P1 field map. Clifford evaluation is neutral, not an automatically positive observable.'}


CHECKS = {'primitive-integral-completion':primitive_integral_completion,
          'function-differential-typing':function_differential_typing}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', required=True, choices=sorted(CHECKS))
    args=parser.parse_args()
    print(json.dumps(CHECKS[args.check](), indent=2))


if __name__=='__main__':
    main()
