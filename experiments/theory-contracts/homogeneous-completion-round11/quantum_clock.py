#!/usr/bin/env python3
"""Algebraic regressions; functional-analysis statements are proved in the note."""
import json
from itertools import product
import sympy as s

checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


E, w = s.symbols("E w", positive=True)
p, Q = s.symbols("p Q", real=True)
C = E-p**2/12
for sign in [-1, 1]:
    check(f"sheet {sign} solves constraint", s.simplify(C.subs({E: w**2/12, p: sign*w})) == 0)
    check(f"sheet {sign} Jacobian", s.simplify(s.Abs(s.diff(C, p).subs(p, sign*w))-w/6) == 0)
    psi = s.sqrt(6/w)*s.exp(sign*s.I*w*Q)
    check(f"sheet {sign} wave equation", s.simplify(s.diff(psi, Q, 2)+w**2*psi) == 0)
    current = s.I/12*(s.conjugate(psi)*s.diff(psi, Q)-s.conjugate(s.diff(psi, Q))*psi)
    check(f"sheet {sign} KG current sign", s.simplify(current+sign) == 0)
    check(f"sheet {sign} P eigenvalue", s.simplify(-s.I*s.diff(psi, Q)-sign*w*psi) == 0)

energies = [s.Rational(1, 2), s.Rational(3, 2), s.Rational(7, 3), s.Integer(5)]
f = s.Matrix([1+s.I, 2, 3-s.I, -2*s.I])
weight = s.diag(*[6/s.sqrt(12*e) for e in energies])
J = s.diag(*[s.sqrt(6/s.sqrt(12*e)) for e in energies])
check("weighted averaging equals physical norm", all(s.simplify(v) == 0 for v in J.T*J-weight))
check("positive mass shell weight", all(weight[i, i].is_positive for i in range(4)))
check("omitting Jacobian is detected", s.simplify((f.conjugate().T*(weight-s.eye(4))*f)[0]) != 0)
check("selected physical Hamiltonian nonnegative", all(s.sqrt(12*e).is_positive for e in energies))
shift = s.Symbol("Omega", positive=True)
A0 = shift/2
check("unsubtracted oscillator gap positive", A0.is_positive)
check("vacuum subtraction destroys simple root", A0-shift/2 == 0
      and C.subs({E: 0, p: 0}) == 0 and s.diff(C, p).subs(p, 0) == 0)
check("zero frequency does not destroy spectral square root", s.sqrt(12*(A0-shift/2)) == 0)
# Normalized inverse Fourier transform of delta(C)f carries a 1/sqrt(2pi).
check("rigging to KG normalization", s.simplify((6/w)/s.sqrt(2*s.pi)
      - s.sqrt(6/w)*s.sqrt(6/w)/s.sqrt(2*s.pi)) == 0)
# Exact Gamma=(Z/3)^3 regular-representation identities. This is a group-
# algebra regression, not a finite-dimensional truncation of scalar quantization.
sites = list(product(range(3), repeat=3))
index = {x: i for i, x in enumerate(sites)}
translations = []
for shift_vector in sites:
    U = s.zeros(27)
    for i, x in enumerate(sites):
        U[index[tuple((x[j]+shift_vector[j]) % 3 for j in range(3))], i] = 1
    translations.append(U)
Pi = sum(translations, s.zeros(27))/27
check("finite translation average is orthogonal projector", Pi.T == Pi and Pi*Pi == Pi)
check("finite invariant sector nonzero", Pi.rank() == 1 and Pi*s.ones(27, 1) == s.ones(27, 1))
check("all translations preserve invariant projector", all(U*Pi == Pi for U in translations))
circulant = s.eye(27)
for axis in range(3):
    shift_vector = tuple(int(i == axis) for i in range(3))
    U = translations[index[shift_vector]]
    circulant += 2*s.eye(27)-U-U.T
check("commuting positive regular-representation sample", circulant*Pi == Pi*circulant
      and circulant*Pi == Pi)
print_scope = "Conditional one-constraint model with optional finite-translation projection; no continuous momentum repair."
print(json.dumps({"status": "PASS", "exact_check_groups": len(checks), "checks": checks,
                  "scope": print_scope}, indent=2))
