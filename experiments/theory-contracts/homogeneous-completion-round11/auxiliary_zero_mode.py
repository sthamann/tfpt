#!/usr/bin/env python3
"""Exact finite regressions for the global auxiliary theorem; no TOE claim."""
import json
import sympy as s

checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def zero(matrix):
    return all(s.simplify(x) == 0 for x in matrix)


t = s.Matrix([1, 1, 1, 0, 0, 0])
B = s.Matrix.hstack(s.Matrix([1, -1, 0, 0, 0, 0])/s.sqrt(2),
                    s.Matrix([1, 1, -2, 0, 0, 0])/s.sqrt(6),
                    *[s.eye(6)[:, j] for j in range(3, 6)])
N = t.row_join(B)
check("traceless orthonormal columns", zero(t.T*B) and B.T*B == s.eye(5))
check("constant source map Gram", N.T*N == s.diag(3, 1, 1, 1, 1, 1))
check("constant source map determinant", s.simplify(N.det()**2) == 3)
K = s.diag(s.eye(18), s.zeros(12))
K[18:24, 24:30] = N.T
K[24:30, 18:24] = N
Ki = s.diag(s.eye(18), s.zeros(12))
Ki[18:24, 24:30] = N.inv()
Ki[24:30, 18:24] = N.T.inv()
check("full 30-dimensional K inverse", zero(K*Ki-s.eye(30)) and zero(Ki*K-s.eye(30)))
check("constant K determinant", s.simplify(K.det()) == 3)
eigs = K.eigenvals()
check("constant K inertia", sum(v for e, v in eigs.items() if e.is_positive) == 24
      and sum(v for e, v in eigs.items() if e.is_negative) == 6
      and sum(eigs.values()) == 30)
g = s.Symbol("g", real=True)
tau = s.Matrix(s.symbols("tau:6", real=True))
source = s.zeros(24, 1).col_join(g*tau)
ystar = -Ki*source
expected_u = s.Matrix([-g*(t.T*tau)[0]/3]).col_join(-g*B.T*tau)
check("stationary constant graph", zero(K*ystar+source)
      and zero(ystar[:18, :]) and zero(ystar[24:, :]) and zero(ystar[18:24, :]-expected_u))
check("arbitrary constant source absorbed", zero(N*expected_u+g*tau))
check("no constant energy response", s.simplify((source.T*Ki*source)[0]) == 0)

# A nonzero antisymmetric source bracket tests the F term, not F=0 alone.
F = s.zeros(30)
F[24, 25] = 2
F[25, 24] = -2
C = s.BlockMatrix([[s.zeros(30), -K], [K, F]]).as_explicit()
Ci = s.BlockMatrix([[Ki*F*Ki, Ki], [-Ki, s.zeros(30)]]).as_explicit()
check("60-dimensional Dirac inverse with F nonzero", zero(C*Ci-s.eye(60)) and zero(Ci*C-s.eye(60)))
check("seed bracket correction lower block zero", Ci[30:, 30:] == s.zeros(30))
wrong = s.BlockMatrix([[s.zeros(30), Ki], [-Ki, s.zeros(30)]]).as_explicit()
check("dropping F is detected", not zero(C*wrong-s.eye(60)))
# These are exact null witnesses, not slow numerical near-singularity checks.
oldK = s.diag(s.eye(18), s.zeros(7))
oldK[18:19, 19:25] = t.T
oldK[19:25, 18:19] = t
oldnull = s.zeros(19, 5).col_join(B)
check("without five slacks old K has exactly five nulls", zero(oldK*oldnull)
      and oldK.rank() == 20 and oldnull.rank() == 5)
redundant = s.diag(K, s.zeros(3))
check("retaining three constant v coordinates is singular", redundant.rank() == 30
      and redundant.shape == (33, 33))
n = s.Symbol("n", integer=True, positive=True)
m = 3*(n-1)+n+5
check("all n dimension and inertia identities", s.expand(18*n+m+6*n-(28*n+2)) == 0
      and s.expand(18*n+m-(22*n+2)) == 0
      and s.expand(m+2*(n-1)-6*n) == 0)
check("all n complete second-class pair removal", s.expand(2*(28*n+2)-(56*n+4)) == 0
      and s.expand(6*n-m-2*(n-1)) == 0)
print(json.dumps({"status": "PASS", "exact_check_groups": len(checks), "checks": checks,
                  "scope": "Auxiliary zero-mode completion only; no homogeneous gravity receiver."}, indent=2))
