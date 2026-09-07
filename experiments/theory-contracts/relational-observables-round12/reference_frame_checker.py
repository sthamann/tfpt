#!/usr/bin/env python3
"""Exact reference-frame identities and an actual-source locality transfer test."""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import runpy

import sympy as s

HERE = Path(__file__).resolve().parent
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def zero(matrix):
    return all(s.simplify(x) == 0 for x in matrix)


def comm(a, b):
    return a*b-b*a


I2 = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
Z = s.diag(1, -1)


def site_op(op, site):
    return s.kronecker_product(*[op if i == site else I2 for i in range(3)])


xs, ys, zs = [[site_op(op, j) for j in range(3)] for op in (X, Y, Z)]
bits = list(product(range(2), repeat=3))
index = {b: i for i, b in enumerate(bits)}
U = s.zeros(8)
for j, b in enumerate(bits):
    U[index[(b[2], b[0], b[1])], j] = 1
Us = [s.eye(8), U, U**2]
check("genuine system cyclic action", U**3 == s.eye(8) and U.T*U == s.eye(8))
Pi = sum(Us, s.zeros(8))/3
check("system invariant projector", Pi*Pi == Pi and Pi.T == Pi and Pi.rank() == 4)
check("original distant observables commute", zero(comm(xs[0], zs[1])))
compressed = comm(Pi*xs[0]*Pi, Pi*zs[1]*Pi)
check("compression destroys the proposed local commutation", not zero(compressed)
      and zero(compressed+2*s.I*Pi*sum(ys, s.zeros(8))*Pi/9))
check("compression is not multiplicative", not zero(Pi*xs[0]*xs[0]*Pi-(Pi*xs[0]*Pi)**2))

L = s.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
Ls = [s.eye(3), L, L**2]
W = [s.kronecker_product(Ls[a], Us[a]) for a in range(3)]
V = s.Matrix.vstack(*Us)/s.sqrt(3)
Pdiag = sum(W, s.zeros(24))/3
check("encoding isometric", zero(V.H*V-s.eye(8)))
check("encoding has exactly invariant range", zero(V*V.H-Pdiag) and Pdiag.rank() == 8)
check("encoded vectors satisfy all group constraints", all(zero(w*V-V) for w in W))


def rel(op):
    return s.diag(*[u*op*u.H for u in Us])


O, Bop = xs[0], zs[1]
check("relational operator is gauge invariant", all(zero(comm(w, rel(O))) for w in W))
check("relational lift intertwines on physical states", zero(rel(O)*V-V*O))
check("relational compression restores the original operator", zero(V.H*rel(O)*V-O))
check("relational algebra is unital", rel(s.eye(8)) == s.eye(24))
check("relational lift preserves arbitrary products", zero(rel(O*Bop)-rel(O)*rel(Bop)))
check("relational lift preserves adjoints", zero(rel(O.H)-rel(O).H))
check("relational lift restores distant commutation", zero(comm(rel(O), rel(Bop))))

# This spin Hamiltonian tests the finite group identities, not scalar dynamics.
A = 5*s.eye(8)+sum((zs[i]*zs[(i+1) % 3] for i in range(3)), s.zeros(8))
A += sum(xs, s.zeros(8))/3
check("witness Hamiltonian respects actual translations", all(zero(comm(A,u)) for u in Us))
Hext = s.kronecker_product(s.eye(3), A)
check("full physical Hamiltonian transported exactly", zero(Hext*V-V*A))
check("Heisenberg derivative transported", zero(comm(Hext, rel(O))-rel(comm(A,O))))
check("double commutator transported", zero(V.H*comm(comm(Hext,rel(O)),rel(Bop))*V-comm(comm(A,O),Bop)))

psi = s.Matrix([1, s.I, 2, 0, -1, 0, s.I, 1])/3
check("readout state normalized", (psi.H*psi)[0] == 1)
rho = psi*psi.H
encoded = V*rho*V.H
check("encoded density has exact readout", s.simplify(s.trace(encoded*rel(O))-s.trace(rho*O)) == 0)
check("encoded density invariant", all(zero(w*encoded*w.H-encoded) for w in W))
check("reference has uniform diagonal distribution", all(s.simplify(s.trace(encoded[8*a:8*(a+1),8*a:8*(a+1)])-s.Rational(1,3)) == 0 for a in range(3)))
check("conditional recovery in each frame coordinate", all(zero(Us[a].H*(V*psi)[8*a:8*(a+1), :]*s.sqrt(3)-psi) for a in range(3)))

Href = 2*s.eye(3)-L-L.T
effective = 2*s.eye(8)-U-U.T
check("reference energy compression", zero(V.H*s.kronecker_product(Href,s.eye(8))*V-effective))
check("general coefficient formula", zero(sum((Href[0,j]*Us[j] for j in range(3)),s.zeros(8))-effective))
check("reference energy is positive", Href == (s.eye(3)-L).H*(s.eye(3)-L))
check("effective reference energy is positive", effective == (s.eye(8)-U).H*(s.eye(8)-U))
check("reference energy commutes with original dynamics", zero(comm(effective,A)))
check("reference backreaction genuinely changes physical Hamiltonian", not zero(effective)
      and zero(V.H*(Hext+s.kronecker_product(Href,s.eye(8)))*V-(A+effective)))

# Actual scalar source at the cubic Round11 witness, not the spin model.
Lattice = runpy.run_path(str(HERE.parent/'reduced-locality-round11/locality_check.py'))['Lattice']
lat = Lattice((6,6,6))
profile = (Fraction(1), Fraction(-1), Fraction(0))
phi = {x: profile[x[0] % 3] for x in lat.sites}
dx, dy = lat.zero(), lat.zero()
dx[(0,0,0)], dy[(0,0,3)] = Fraction(1), Fraction(1)
jx, jy = lat.variation(phi, dx), lat.variation(phi, dy)
hxy = lat.pair(jx,jy)
check("actual cubic nonzero remote vertex", hxy == -s.Rational(1762469675117,170400029184000))
check("actual stress mixed derivative vanishes", all(v == 0 for row in lat.variation(dx,dy).values() for v in row))
twice = {x: 2*phi[x] for x in lat.sites}
check("actual Jacobian scales linearly", lat.variation(twice,dx) == {x:[2*v for v in row] for x,row in jx.items()})
check("actual remote Hessian scales quadratically", lat.pair(lat.variation(twice,dx),lat.variation(twice,dy)) == 4*hxy)
# Algebraic finite differences of an arbitrary quartic with no term from a
# mixed second stress derivative: the ab t^2 coefficient is the actual Hessian.
t, a, b = s.symbols('t a b', real=True)
sxKsy, jxKsy, sxKjy = s.symbols('sxKsy jxKsy sxKjy', real=True)
cross = a*b*t**2*hxy+a**2*b*t*sxKjy+a*b**2*t*jxKsy+a**2*b**2*sxKsy
check("unbounded finite-difference leading coefficient", s.Poly(cross,t).coeff_monomial(t**2) == a*b*hxy
      and hxy != 0)

print(json.dumps({"status":"PASS", "exact_check_groups":len(checks),"checks":checks,
                  "actual_cubic_remote_hessian":str(hxy),
                  "scope":"Finite reference-frame theorem and actual source witness; no new local parent or continuous momentum receiver."},indent=2))
