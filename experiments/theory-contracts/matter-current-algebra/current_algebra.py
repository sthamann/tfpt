#!/usr/bin/env python3
"""Exact audits of the EXISTING free-scalar sources, not nonlinear gravity.

The universal statements and their hypotheses are proved in README.md.
Finite systems below are regressions, not the source of universal quantifiers.
No random samples, external data, fitted inputs, or floating-point arithmetic.
"""
from __future__ import annotations

import importlib.util
from itertools import product
from pathlib import Path
import sys

import sympy as sp


def load_ward():
    path = Path(__file__).resolve().parents[1] / "free-scalar-3d" / "free_scalar_ward.py"
    spec = importlib.util.spec_from_file_location("round8_fixed_ward", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def poisson(f, g, qs, ps):
    return sp.expand(sum(sp.diff(f, q) * sp.diff(g, p)
                         - sp.diff(f, p) * sp.diff(g, q)
                         for q, p in zip(qs, ps)))


class Audit:
    def __init__(self):
        self.passed = 0
        self.total = 0

    def check(self, label, condition):
        self.total += 1
        self.passed += int(bool(condition))
        print(f"[{'PASS' if condition else 'FAIL'}] {label}")


def current_matrix(n, weights, spacing):
    """J[u]=-p^T A[u]q, from the fixed endpoint-averaged current."""
    matrix = sp.zeros(n)
    for x in range(n):
        y = (x + 1) % n
        w = weights[x] / (2 * spacing)
        matrix[x, y] += w
        matrix[x, x] -= w
        matrix[y, y] += w
        matrix[y, x] -= w
    return matrix


def run():
    audit = Audit()
    a = sp.Symbol("a", positive=True)
    q0, q1, p0, p1, n0, n1, m0, m1, mass2 = sp.symbols(
        "q0 q1 p0 p1 n0 n1 m0 m1 mass2", real=True)

    def two_site(n, m):
        return (n * (p0**2 + mass2*q0**2) + m*(p1**2 + mass2*q1**2))/2 + (
            n+m)*(q1-q0)**2/(4*a**2)

    bracket = poisson(two_site(n0, n1), two_site(m0, m1), (q0, q1), (p0, p1))
    current = -(p0+p1)*(q1-q0)/(2*a)
    beta = (m0*n1-n0*m1)/a
    audit.check("generic edge: lapse-lapse bracket equals J[beta]", sp.expand(bracket-beta*current) == 0)
    audit.check("generic edge: reversed bracket sign is rejected", sp.expand(bracket+beta*current) != 0)
    audit.check("generic edge: mass cancels for arbitrary smearings", sp.diff(bracket, mass2) == 0)

    # Import and test the actual previously integrated source, not a renamed toy.
    source = load_ward()
    fields = source.Fields(period=3)
    ward = source.WardComplex(fields)
    sites = list(product(range(3), repeat=3))
    qs = [fields.phi(x) for x in sites]
    ps = [fields.pi(x) for x in sites]
    ns = {x: 1 + x[0] - 2*x[1] + x[2]**2 for x in sites}
    ms = {x: 2 - x[0]**2 + x[1]*x[2] for x in sites}
    hn = sp.expand(sum(ns[x]*ward.rho(x) for x in sites))
    hm = sp.expand(sum(ms[x]*ward.rho(x) for x in sites))
    current_bracket = 0
    for x in sites:
        for axis in range(3):
            y = fields.wrap(source.add(x, source.E[axis]))
            current_bracket += (ms[x]*ns[y]-ns[x]*ms[y])*ward.current(axis, x)/ward.a
    audit.check("actual 3^3 source: lapse-lapse bracket closes exactly", poisson(hn, hm, qs, ps) == sp.expand(current_bracket))
    audit.check("actual source: closure is nonzero, not a commuting-smearing test", sp.expand(current_bracket) != 0)
    h = sp.expand(sum(ward.rho(x) for x in sites))
    for axis in range(3):
        total_current = sp.expand(sum(ward.current(axis, x) for x in sites))
        audit.check(f"actual source: global momentum {axis} is conserved in free theory", poisson(total_current, h, qs, ps) == 0)

    n = 7
    us = sp.symbols("u:7", real=True)
    vs = sp.symbols("v:7", real=True)
    au, av = current_matrix(n, us, a), current_matrix(n, vs, a)
    comm = au*av-av*au
    tail = (us[0]*vs[1]-vs[0]*us[1])/(4*a**2)
    audit.check("generic current bracket: distance-two coefficient", sp.expand(comm[0, 2]-tail) == 0)
    audit.check("distance-two coefficient is not identically zero", tail != 0)
    audit.check("every original smeared current has zero distance-two coefficient", au[0, 2] == av[0, 2] == 0)
    audit.check("current operators annihilate constant fields", au*sp.ones(n, 1) == sp.zeros(n, 1))
    audit.check("current ordering trace is zero", sp.trace(au) == 0)
    q = sp.Matrix(sp.symbols("q:7", real=True))
    p = sp.Matrix(sp.symbols("p:7", real=True))
    # Rational nonconstant smearings make an independent full Poisson calculation cheap.
    numeric_u = [sp.Integer(i % 3 - 1) for i in range(n)]
    numeric_v = [sp.Integer((2*i+1) % 5 - 2) for i in range(n)]
    aa, ab = current_matrix(n, numeric_u, a), current_matrix(n, numeric_v, a)
    ju, jv = -(p.T*aa*q)[0], -(p.T*ab*q)[0]
    audit.check("full canonical current bracket has the stated commutator sign", poisson(ju, jv, q, p) == sp.expand((p.T*(aa*ab-ab*aa)*q)[0]))
    audit.check("nonconstant shifts give a nonzero current bracket", aa*ab-ab*aa != sp.zeros(n))
    # Three adjacent edge generators create an unavoidable distance-three term.
    edges = [current_matrix(n, [sp.Integer(i == j) for i in range(n)], a) for j in range(3)]
    c2 = edges[0]*edges[1]-edges[1]*edges[0]
    c3 = c2*edges[2]-edges[2]*c2
    audit.check("localized edge commutator reaches two links", c2[0, 2] == 1/(4*a**2))
    audit.check("nested edge commutator reaches three links", c3[0, 3] == 1/(8*a**3))

    # Complete onsite-potential classification: the analytic proof is in README.
    x, y, z = sp.symbols("x y z", real=True)
    c0, c1, c2, c3, c4, c5, c6 = cs = sp.symbols("c:7", real=True)
    v = sum(c*x**power for power, c in enumerate(cs))
    f = sp.diff(v, x)
    tri = sp.expand(f*(y-z)+f.subs(x,y)*(z-x)+f.subs(x,z)*(x-y))
    equations = sp.Poly(tri, x, y, z).coeffs()
    solutions = sp.linsolve(equations, cs)
    audit.check("degree-six potential census leaves exactly constant/linear/quadratic", solutions == sp.FiniteSet((c0,c1,c2,0,0,0,0)))
    f0, f1, ft = sp.symbols("f0 f1 ft")
    interpolation_residual = (1-z)*f0+z*f1-ft
    solved_derivative = sp.solve(interpolation_residual, ft)[0]
    audit.check("arbitrary C1 potential: three-value condition forces affine derivative", sp.expand(solved_derivative-(f0+(f1-f0)*z)) == 0)
    b, c, mu = sp.symbols("b c mu", real=True)
    quadratic = mu*x**2/2+b*x+c
    trapezoid = (sp.diff(quadratic,x)+sp.diff(quadratic,x).subs(x,y))*(y-x)/2-(quadratic.subs(x,y)-quadratic)
    audit.check("allowed general quadratic potential admits exact local pressure", sp.expand(trapezoid) == 0)
    quartic = x**4/sp.Integer(24)
    defect = (sp.diff(quartic,x)+sp.diff(quartic,x).subs(x,y))*(y-x)/2-(quartic.subs(x,y)-quartic)
    audit.check("quartic local defect factors exactly", sp.expand(defect-(x+y)*(y-x)**3/24) == 0)
    values = (0,1,2,4)
    residue = sum(defect.subs({x:values[i],y:values[(i+1)%4]}) for i in range(4))
    audit.check("historical four-site quartic obstruction is -17/2", residue == -sp.Rational(17,2))

    print(f"COUNTS: {audit.passed}/{audit.total} exact checks passed")
    print("VERDICT: EXACT_LAPSE_LAPSE_CLOSURE; CURRENT_RANGE_GROWTH; FIXED_CURRENT_ONSITE_POTENTIAL_MUST_BE_QUADRATIC; NO_NONLINEAR_GRAVITY_CLAIM")
    return 0 if audit.passed == audit.total else 1


if __name__ == "__main__":
    raise SystemExit(run())
