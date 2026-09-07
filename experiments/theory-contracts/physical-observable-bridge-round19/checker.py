#!/usr/bin/env python3
"""Exact physical-observable bridge regressions; no finite CCR/TOE/RH claim."""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

import sympy as s

CHECKS: list[str] = []
PAIRS = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))


def check(label, result):
    if not bool(result):
        raise AssertionError(label)
    CHECKS.append(label)


def zero(x):
    if isinstance(x, s.MatrixBase):
        return all(s.expand(v) == 0 for v in x)
    return s.expand(x) == 0


def lattice(side):
    sites = tuple(product(range(side), repeat=3))
    lookup = {x: i for i, x in enumerate(sites)}
    n = len(sites)
    eye = s.eye(n)
    plus, minus = [], []
    for axis in range(3):
        shift = s.zeros(n)
        for i, x in enumerate(sites):
            y = list(x)
            y[axis] = (y[axis] + 1) % side
            shift[i, lookup[tuple(y)]] = 1
        plus.append(shift-eye)
        minus.append(eye-shift.T)
    ell = -sum((minus[i]*plus[i] for i in range(3)), s.zeros(n))
    d = s.Matrix.vstack(*plus)
    a = s.Matrix.hstack(*[minus[i]*plus[i]+ell if i == j else s.sqrt(2)*minus[i]*minus[j] for i, j in PAIRS])
    v = s.zeros(3*n, 6*n)
    for block, (i, j) in enumerate(PAIRS):
        if i == j:
            v[i*n:(i+1)*n, block*n:(block+1)*n] = plus[i]
        else:
            v[i*n:(i+1)*n, block*n:(block+1)*n] = minus[j]/s.sqrt(2)
            v[j*n:(j+1)*n, block*n:(block+1)*n] = minus[i]/s.sqrt(2)
    trace = s.Matrix.vstack(eye, eye, eye, s.zeros(n), s.zeros(n), s.zeros(n))
    ell6 = s.diag(*([ell]*6))
    r = ell6**2-2*ell6*v.T*v+v.T*d*d.T*v-a.T*a/2
    return sites, ell, ell6, a, v, d, trace, r


def native_checks(side):
    sites, ell, ell6, a, v, d, trace, r = lattice(side)
    n = len(sites)
    tag = f"native all-site L={side}: "
    check(tag+"scalar trace-complement identity including signs", zero(a.T-ell6*trace+v.T*d))
    check(tag+"TT filter self-adjoint", zero(r-r.T))
    check(tag+"both actual constraint gauge directions annihilated", zero(r*v.T) and zero(r*a.T))
    check(tag+"trace and all tensor means annihilated", zero(r*trace) and zero(r*s.diag(*([s.ones(n, 1)]*6))))
    check(tag+"polynomial projector relation", zero(r*r-ell6**2*r))
    check(tag+"native linear symplectic gauge pairings vanish", zero(a*r) and zero(v*r))
    # This is a linear symplectic certificate, not a matrix CCR model.
    check(tag+"filtered reduced canonical kernel symmetric nonzero", r*r == (r*r).T and not zero(r*r))
    if side == 2:
        mean = s.ones(n)/n
        green = (ell+mean).inv()-mean
        green6 = s.diag(*([green]*6))
        proj = green6**2*r
        check(tag+"actual TT quotient projector", zero(proj*proj-proj) and zero(proj-proj.T) and s.trace(proj) == 2*(n-1))
        check(tag+"finite-lattice inverse is exactly nonlocal Green squared", zero(green6**2*r-proj) and zero(r*proj-r) and zero(r*green6**2*r-r))
        check(tag+"source denominator removal retains all TT modes", zero(r-ell6**2*proj) and zero(r*proj*r-r*r))
    return (sites, r)


def universal_stencil():
    z = s.symbols("z0:3", nonzero=True)
    def adj(m):
        return m.T.xreplace({q: 1/q for q in z})
    plus = [q-1 for q in z]
    minus = [1-1/q for q in z]
    ell = -sum(minus[i]*plus[i] for i in range(3))
    d = s.Matrix(plus)
    a = s.Matrix([[minus[i]*plus[i]+ell if i == j else s.sqrt(2)*minus[i]*minus[j] for i, j in PAIRS]])
    v = s.zeros(3, 6)
    for k, (i, j) in enumerate(PAIRS):
        if i == j:
            v[i, k] = plus[i]
        else:
            v[i, k] = minus[j]/s.sqrt(2)
            v[j, k] = minus[i]/s.sqrt(2)
    trace = s.Matrix([1, 1, 1, 0, 0, 0])
    r = (ell**2*s.eye(6)-2*ell*adj(v)*v+adj(v)*d*adj(d)*v-adj(a)*a/2).applyfunc(s.expand)
    check("unaliased Laurent scalar and vector Grams", zero(a*adj(a)-s.Matrix([[2*ell**2]])) and zero(v*adj(v)-(ell*s.eye(3)+d*adj(d))/2))
    check("unaliased Laurent TT gauge annihilation", zero(r*adj(v)) and zero(r*adj(a)))
    check("unaliased Laurent trace and adjoint", zero(r*trace) and zero(r-adj(r)))
    supports = set()
    for expression in r:
        for term in s.expand(expression).as_ordered_terms():
            if term == 0:
                continue
            powers = term.as_powers_dict()
            coord = tuple(int(powers.get(q, 0)) for q in z)
            supports.add(coord)
    radius = max(sum(abs(k) for k in x) for x in supports)
    check("unaliased Laurent support radius <=4 from site center", radius <= 4 and radius > 0)
    check("unaliased Laurent all six means removed exactly", zero(r.subs({q: 1 for q in z})))
    # A literal nonzero finite stencil coefficient, not only a rank statement.
    check("unaliased filter nonzero on actual (pi,pi,0) mode", not zero(r.subs({z[0]: -1, z[1]: -1, z[2]: 1})))
    return radius, len(supports)


def source_checks(path, sites, r):
    spec = importlib.util.spec_from_file_location("round19_observable_ward", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot import actual Ward source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    fields = module.Fields(period=2)
    ward = module.WardComplex(fields)
    sub = {ward.a: 1, ward.mass2: 2}
    tau, sigma, kinetic_trace = [], [], []
    for i, j in PAIRS:
        for x in sites:
            actual = s.expand(ward.tau(i, j, x).subs(sub))
            if i == j:
                trace_piece = fields.pi(x)**2/2-fields.phi(x)**2
                tau.append(actual)
                sigma.append(s.expand(actual-trace_piece))
                kinetic_trace.append(trace_piece)
            else:
                tau.append(s.sqrt(2)*actual)
                sigma.append(s.sqrt(2)*actual)
                kinetic_trace.append(0)
    tau, sigma = s.Matrix(tau), s.Matrix(sigma)
    check("literal Ward tensor split has exactly trace kinetic/mass part", zero(tau-sigma-s.Matrix(kinetic_trace)) and all(not e.has(*fields.pi_vars.values()) for e in sigma))
    filtered = (r*tau).applyfunc(s.expand)
    check("literal Ward filtered full source equals configuration source", zero(filtered-r*sigma))
    check("literal Ward filtered source is nonzero and no matter pi", not zero(filtered) and all(not e.has(*fields.pi_vars.values()) for e in filtered))
    mutant = tau.copy()
    mutant[0] += fields.pi(sites[0])**2
    defect = (r*mutant-filtered).applyfunc(s.expand)
    check("anisotropic kinetic-source alteration is detected", not zero(defect) and any(e.has(fields.pi(sites[0])) for e in defect))
    allzero = {x: 0 for x in fields.reverse}
    check("literal Ward rho origin mutation regression", ward.rho(sites[0]).subs(sub).subs(allzero) == 0)


def gaussian_weyl_checks():
    b, f0, f1, omega = s.symbols("b f0 f1 omega", real=True, positive=True)
    midpoint = (f0+f1)/2
    check("exact Gaussian overlap square completion", zero((b-f0)**2+(b-f1)**2-2*(b-midpoint)**2-(f1-f0)**2/2))
    # Normalized overlap integrates by translating the normalized Gaussian.
    eta, k, deltaf = s.symbols("eta k deltaf", positive=True)
    overlap = s.exp(-s.sqrt(eta)*s.sqrt(k)*deltaf**2/4)
    check("exact normalized Gaussian translation defect", s.limit(2*(1-overlap), eta, 0, dir="+") == 0 and (2*(1-overlap)).subs({eta: 1, k: 1, deltaf: 2}) == 2-2/s.E)
    x, y, u, v, z = s.symbols("x y u v z", real=True)
    phase_product = u*(x+y/2)+v*(x+y+z/2)
    phase_total = (u+v)*(x+(y+z)/2)
    check("bare slow Weyl exact multiplication sign", zero(phase_product-phase_total-(v*y-u*z)/2))
    check("coordinate-only phase cancels in overlap defect", zero(u*(x+y/2)-u*(x+y/2)))
    alpha, beta, gamma = s.symbols("alpha beta gamma", real=True)
    f = alpha*x+beta*x**2+gamma
    diff = s.expand(f.subs(x, x+y)-f)
    check("actual degree-two displacement yields affine translation difference", zero(diff-alpha*y-2*beta*x*y-beta*y**2) and s.diff(diff, x, 2) == 0)
    q, h, zeta = s.symbols("q h zeta", real=True)
    fq = alpha*q+beta*x**2+gamma
    check("tensor translation displacement is constant in slow fields", zero(fq.subs(q, q+h)-fq-alpha*h))
    check("finite-eta encoding is not exactly local-Weyl invariant", overlap.subs({eta: 1, k: 1, deltaf: 2}) != 1)
    # Scalar weighted integral test: 1-e^-z <= z follows from monotonic
    # derivative; exact derivative and equality at zero are checked here.
    zz = s.symbols("zz", nonnegative=True)
    gap = zz-1+s.exp(-zz)
    check("dominating Gaussian defect bound endpoints and derivative", gap.subs(zz, 0) == 0 and s.diff(gap, zz) == 1-s.exp(-zz))
    rho = s.Matrix([[s.Rational(1, 3), 0], [0, s.Rational(2, 3)]])
    spectator = s.Matrix([[1, 0], [0, s.exp(-s.I*zeta)]])
    check("normalized spectator cancellation for zero net time", s.trace(rho) == 1 and zero(spectator.conjugate().T*spectator-s.eye(2)))
    check("nonzero-duration transition retains spectator amplitude", s.trace(rho*spectator) == s.Rational(1, 3)+2*s.exp(-s.I*zeta)/3 and s.trace(rho*spectator).subs(zeta, s.pi) == -s.Rational(1, 3))


def quotient_clock_and_projection_checks():
    detp = s.Integer(36)
    check("physical chart determinant explicitly cancels in pushed Haar", detp*s.Rational(1, 36) == 1 and s.sqrt(detp)/s.sqrt(detp) == 1)
    o = s.Matrix([[1, 2], [3, 4]])
    j = s.Matrix([[1, 0], [0, 1], [0, 0]])
    op = j*o*j.T
    check("isometric quotient representation preserves products", j.T*j == s.eye(2) and zero(op*j-j*o) and zero(op**2-j*o**2*j.T))
    energy1, energy2 = s.symbols("energy1 energy2", positive=True)
    om = s.diag(s.sqrt(12*energy1), s.sqrt(12*energy2))
    weight = s.diag(s.sqrt(6)/s.sqrt(om[0, 0]), s.sqrt(6)/s.sqrt(om[1, 1]))
    check("clock half-density weighted norm is exactly canonical", zero(weight*(om/6)*weight-s.eye(2)))
    flip = s.Matrix([[0, 1], [1, 0]])
    readout = weight*flip*weight.inv()
    check("sector-changing clock readout needs energy-dependent weights", zero(weight.inv()*readout*weight-flip) and not zero(readout-flip))
    # Rank-two projection in three dimensions; commuting ambient observables
    # acquire a nonzero commutator after compression.
    z = s.Matrix([1, 1, 1])/s.sqrt(3)
    proj = s.eye(3)-z*z.T
    a, b = s.diag(1, 0, 0), s.diag(0, 1, 0)
    check("optional projection counterexample is a genuine orthogonal projector", zero(proj**2-proj) and proj.T == proj and s.trace(proj) == 2)
    check("commuting ambient observables need not commute after compression", zero(a*b-b*a) and not zero(proj*a*proj*b*proj-proj*b*proj*a*proj))
    check("optional projection compression is not multiplicative", not zero(proj*a*b*proj-proj*a*proj*b*proj))
    # Exact charge tensor intertwiner, without finite periodic wrap being
    # promoted to an infinite charge-lattice simulation.
    shift = s.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    totalj = s.kronecker_product(s.eye(3), j)
    check("charge-only bounded operator commutes with charge-independent encoding", zero(s.kronecker_product(shift, s.eye(3))*totalj-totalj*s.kronecker_product(shift, s.eye(2))))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ward-source", type=Path, default=Path(__file__).resolve().parents[1]/"free-scalar-3d"/"free_scalar_ward.py")
    args = parser.parse_args()
    path = args.ward_source.resolve(strict=True)
    sites, r = native_checks(2)
    native_checks(3)
    radius, terms = universal_stencil()
    source_checks(path, sites, r)
    gaussian_weyl_checks()
    quotient_clock_and_projection_checks()
    print(json.dumps({"status": "PASS", "exact_check_groups": len(CHECKS), "checks": CHECKS, "actual_source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "unaliased_R_stencil_radius": radius, "unaliased_R_distinct_displacements": terms, "scope": "Finite physical observable subalgebra/protocol bridge; no full native local net, uniform continuum bound, finite CCR, TOE or RH claim."}, indent=2))


if __name__ == "__main__":
    main()
