"""Exact finite-dimensional counterexample and SI thermodynamic identities.

These checks certify algebra, not black-hole physics or TFPT dynamics.
"""
from pathlib import Path
import json
import sympy as s

out = Path(__file__).resolve().parent
records = []


def check(name, statement):
    passed = bool(statement)
    records.append({"check": name, "passed": passed})
    assert passed, name


psi = s.Matrix([s.sqrt(3) / 2, 0, 0, s.Rational(1, 2)])
psi_phase = s.Matrix([s.sqrt(3) / 2, 0, 0, -s.Rational(1, 2)])
rho = psi * psi.H
rho_phase = psi_phase * psi_phase.H


def partial_b(matrix):
    return s.Matrix(2, 2, lambda i, j: sum(matrix[2*i+b, 2*j+b] for b in range(2)))


rho_a = partial_b(rho)
check("global pure and normalized", rho * rho == rho and s.trace(rho) == 1)
check("reduced state exactly diag(3/4,1/4)", rho_a == s.diag(s.Rational(3, 4), s.Rational(1, 4)))
h = s.diag(0, s.log(3))
boltzmann = (-h).exp()
check("reduced state exactly Gibbs, beta=1", rho_a == boltzmann / s.trace(boltzmann))
check("reduced state mixed and faithful", s.trace(rho_a * rho_a) == s.Rational(5, 8) and rho_a.det() > 0)
b = s.symbols("b", positive=True)
check("time-energy rescaling leaves beta H unchanged", (s.Rational(1, 1) / b) * (b * h) == h)
check("global phase change invisible to full accessible A algebra", partial_b(rho_phase) == rho_a and rho_phase != rho)
x = s.Matrix([[0, 1], [1, 0]])
xx = s.kronecker_product(x, x)
check("nonlocal XX distinguishes phase", s.simplify(s.trace(rho*xx)) == s.sqrt(3)/2 and s.simplify(s.trace(rho_phase*xx)) == -s.sqrt(3)/2)

G, c, hbar, kb, kappa, mass, area = s.symbols("G c hbar k_B kappa M A", positive=True)
temperature = hbar*kappa/(2*s.pi*c*kb)
dE_dA = kappa*c**2/(8*s.pi*G)
check("first law / Hawking temperature gives area coefficient", s.simplify(dE_dA/temperature-kb*c**3/(4*hbar*G)) == 0)
schwarzschild_kappa = c**4/(4*G*mass)
schwarzschild_area = 16*s.pi*G**2*mass**2/c**4
entropy = kb*c**3*schwarzschild_area/(4*hbar*G)
temp_mass = temperature.subs(kappa, schwarzschild_kappa)
check("Schwarzschild TdS=d(Mc^2)", s.simplify(temp_mass*s.diff(entropy, mass)-c**2) == 0)

result = {
    "scope": "exact finite quantum counterexample and dimensional-constant algebra; not a black-hole or TFPT derivation",
    "checks": records,
    "all_passed": all(r["passed"] for r in records),
    "exact_reduced_matrix": str(rho_a),
    "global_XX_expectation": str(s.trace(rho*xx)),
    "phase_flipped_XX_expectation": str(s.trace(rho_phase*xx)),
    "sympy_version": s.__version__,
}
(out / "checks.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(result, indent=2, ensure_ascii=False))
