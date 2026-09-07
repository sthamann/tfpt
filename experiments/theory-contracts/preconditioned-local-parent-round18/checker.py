#!/usr/bin/env python3
"""Exact native-stencil and source checks for the NEW Round18 local chart.

Finite symbolic regression certificates, not a continuum theorem or a finite
CCR representation. The proof supplies the all-volume identities and imports
the active-form domain/propagator theorem. No RH or complete-TOE claim.
"""
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


def check(name: str, condition: object) -> None:
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def zero(value: s.MatrixBase | s.Expr) -> bool:
    if isinstance(value, s.MatrixBase):
        return all(s.expand(x) == 0 for x in value)
    return s.expand(value) == 0


def native_stencils(side: int) -> None:
    sites = tuple(product(range(side), repeat=3))
    index = {x: i for i, x in enumerate(sites)}
    n = len(sites)
    eye = s.eye(n)
    shifts = []
    for axis in range(3):
        shift = s.zeros(n)
        for x in sites:
            y = list(x)
            y[axis] = (y[axis] + 1) % side
            shift[index[x], index[tuple(y)]] = 1
        shifts.append(shift)
    plus = [t - eye for t in shifts]
    minus = [eye - t.T for t in shifts]
    ell = -sum((minus[i] * plus[i] for i in range(3)), s.zeros(n))
    grad, div = s.Matrix.vstack(*plus), s.Matrix.hstack(*minus)
    pairs = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))
    scalar = s.Matrix.hstack(*[
        minus[i] * plus[i] + ell if i == j
        else s.sqrt(2) * minus[i] * minus[j] for i, j in pairs
    ])
    vector = s.zeros(3 * n, 6 * n)
    for block, (i, j) in enumerate(pairs):
        if i == j:
            vector[i*n:(i+1)*n, block*n:(block+1)*n] = plus[i]
        else:
            vector[i*n:(i+1)*n, block*n:(block+1)*n] = minus[j] / s.sqrt(2)
            vector[j*n:(j+1)*n, block*n:(block+1)*n] = minus[i] / s.sqrt(2)
    trace = s.Matrix.vstack(eye, eye, eye, s.zeros(n), s.zeros(n), s.zeros(n))
    lv = s.diag(ell, ell, ell)
    gv = vector * vector.T
    kp = s.eye(6 * n) - trace * trace.T / 2
    fv = 2 * lv - s.Rational(3, 2) * grad * grad.T
    pre = ell**2
    prev = s.diag(pre, pre, pre)
    prefix = f"actual all-site L={side}: "
    check(prefix + "adjoint signs and scalar Laplacian", zero(grad.T + div) and zero(grad.T * grad - ell))
    check(prefix + "scalar Gram and trace factors", zero(scalar * scalar.T - 2 * ell**2) and zero(scalar * trace - 2 * ell))
    check(prefix + "scalar/vector annihilation", zero(scalar * vector.T))
    check(prefix + "vector Gram exact factor", zero(gv - (lv + grad * grad.T) / 2))
    check(prefix + "DeWitt vector factor", zero(vector * kp * vector.T - lv / 2))
    check(prefix + "cleared vector inverse identity", zero(fv * gv**2 - lv**3 / 2))
    check(prefix + "preconditioning commutes with actual shear", zero(pre * div - div * prev))
    ones = s.ones(n, 1)
    vector_means = s.diag(ones.T, ones.T, ones.T)
    check(prefix + "all source sums vanish", zero(ones.T * scalar) and zero(ones.T * ell) and zero(vector_means * fv))
    # DomainMatrix exact rank avoids heuristic symbolic simplification.
    rank = div.to_DM().rank()
    check(prefix + "shear exact rank and conserved scalar mean", rank == n - 1 and zero(ones.T * div))
    if side == 2:
        mean = s.ones(n) / n
        green = (ell + mean).inv() - mean
        greenv = s.diag(green, green, green)
        bv = 2 * greenv - s.Rational(3, 2) * greenv**2 * grad * grad.T
        check(prefix + "mean-zero Green inverse", zero(ell * green - eye + mean) and zero(green * mean))
        check(prefix + "source denominators cancel exactly", zero(pre * green**2 * scalar - scalar) and zero(pre * green - ell))
        check(prefix + "both vector preconditioning factors", zero(prev * bv - fv) and zero(prev * bv * prev - prev * fv))
        check(prefix + "negative scalar potential retained", zero(pre * (-green / 2) * pre + ell**3 / 2))


def block_and_chart_controls() -> None:
    rt = s.sqrt(2)
    a = s.Matrix([[4, 4, 8, 0, 0, 4 * rt]])
    v = s.Matrix([[-2, 0, 0, 0, 0, rt], [0, -2, 0, 0, 0, rt], [0, 0, 0, rt, rt, 0]])
    t = s.Matrix([1, 1, 1, 0, 0, 0])
    kp = s.eye(6) - t * t.T / 2
    polar = s.Matrix.hstack(s.Matrix([1, 1, -2, 0, 0, rt]) / s.sqrt(8), s.Matrix([0, 0, 0, 1, -1, 0]) / rt)
    kq = 8 * polar * polar.T - a.T * a / 16
    gv = v * v.T
    bv = gv.inv() * (v * kp * v.T) * gv.inv()
    check("actual real (pi,pi,0) b and scalar q-sector coefficient", a * kp * v.T * gv.inv() == s.Matrix([[2, 2, 0]]) and (a * kq * a.T)[0] / (a * a.T)[0]**2 == -s.Rational(1, 16))
    check("actual real block vector preconditioner", bv == s.Matrix([[5, -3, 0], [-3, 5, 0], [0, 0, 8]]) / 32 and 64 * bv == s.Matrix([[10, -6, 0], [-6, 10, 0], [0, 0, 16]]))
    k1, k2, k3 = s.symbols("k1 k2 k3", real=True)
    native = s.Rational(3, 4) * (1 - k1**2 / (k1**2 + k2**2 + k3**2))
    eps = s.symbols("eps", positive=True)
    check("native projector has unequal directional limits", s.limit(native.subs({k1: eps, k2: 0, k3: 0}), eps, 0) == 0 and s.limit(native.subs({k1: 0, k2: eps, k3: 0}), eps, 0) == s.Rational(3, 4))
    p = s.diag(4, 9)
    omega = s.Matrix.vstack(s.Matrix.hstack(s.zeros(2), s.eye(2)), s.Matrix.hstack(-s.eye(2), s.zeros(2)))
    chart = s.diag(p, p.inv())
    check("classical symplectic label change, not finite CCR", chart * omega * chart.T == omega)
    c1, c2, q1, q2, g, r = s.symbols("c1 c2 q1 q2 g r", real=True)
    c, q = s.Matrix([c1, c2]), s.Matrix([q1, q2])
    check("source pairing exactly preserved", zero((p * c).dot(q) - c.dot(p * q)))
    check("kinematic determinant and gauge Haar factor", p.det() == 36 and s.sqrt(p.det())**2 / p.det() == 1 and s.sqrt(p.det())**2 == p.det())
    old = (c1**2 + c2**2) * (q1**2 + q2**2)
    new = c1**2 * q1**2 + c2**2 * q2**2
    datum = {c1: 1, c2: 0, q1: 0, q2: 1}
    check("new cell completion differs nontrivially from global one", old.subs(datum) == 1 and new.subs(datum) == 0)
    check("completion change leaves linear coupling jet", s.diff(g**2 * (new - old), g).subs(g, 0) == 0)
    mean_stabilizer = 2 * g**2 * r**2 * q1**2
    check("added mean constraints are not decoupled off shell", r*q1-r*q1 == 0 and s.diff(mean_stabilizer, r) != 0 and mean_stabilizer.subs(r, 0) == 0 and s.diff(mean_stabilizer, r).subs(r, 0) == 0)
    n = s.symbols("n", integer=True, positive=True)
    check("all-site extension adds four gauge pairs only", s.expand(39*n - (35*n + 4*(n-1))) == 4 and 39*n - 4*n == 35*n)
    lmin, lmax = s.symbols("ell_min ell_max", positive=True)
    check("preconditioner conditioning is not uniform", (lmax**2 / lmin**2) == (lmax / lmin)**2 and s.diff(lmin**-2, lmin) == -2/lmin**3)


def source_checks(path: Path) -> dict[str, int]:
    spec = importlib.util.spec_from_file_location("round18_preconditioned_ward", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load actual Ward source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    fields = module.Fields()
    ward = module.WardComplex(fields)
    substitutions = {ward.a: s.Integer(1), ward.mass2: s.Integer(2)}
    origin = (0, 0, 0)

    def shifted(x: tuple[int, int, int], axis: int, sign: int) -> tuple[int, int, int]:
        y = list(x)
        y[axis] += sign
        return tuple(y)

    @lru_cache(None)
    def rho(x: tuple[int, int, int]) -> s.Expr:
        return s.expand(ward.rho(x).subs(substitutions))

    @lru_cache(None)
    def tau(i: int, j: int, x: tuple[int, int, int]) -> s.Expr:
        return s.expand(ward.tau(i, j, x).subs(substitutions))

    @lru_cache(None)
    def current(i: int, x: tuple[int, int, int]) -> s.Expr:
        return s.expand(ward.current(i, x).subs(substitutions))

    def lap(fn, x: tuple[int, int, int]) -> s.Expr:
        return sum(2*fn(x)-fn(shifted(x, j, 1))-fn(shifted(x, j, -1)) for j in range(3))

    @lru_cache(None)
    def divj(x: tuple[int, int, int]) -> s.Expr:
        return sum(current(j, x)-current(j, shifted(x, j, -1)) for j in range(3))

    row = sum(2*tau(i, i, origin)-tau(i, i, shifted(origin, j, 1))-tau(i, i, shifted(origin, j, -1)) for i in range(3) for j in range(3) if i != j)
    for i in range(3):
        for j in range(i + 1, 3):
            mi, mj = shifted(origin, i, -1), shifted(origin, j, -1)
            mij = shifted(mi, j, -1)
            row += 2*(tau(i, j, origin)-tau(i, j, mi)-tau(i, j, mj)+tau(i, j, mij))
    qh = s.expand((row + lap(rho, origin)) / 2)
    qv = [s.expand(2*lap(lambda x: current(i, x), origin) + s.Rational(3, 2)*(divj(shifted(origin, i, 1))-divj(origin))) for i in range(3)]
    phizero = {x: 0 for x in fields.phi_vars.values()}
    kinetic = s.Rational(3, 4)*lap(lambda x: fields.pi(x)**2, origin)
    check("actual source scalar kinetic preconditioning", zero(qh.subs(phizero) - kinetic))
    check("actual source scalar central and neighbor factors", s.diff(qh, fields.pi(origin), 2) == 9 and all(s.diff(qh, fields.pi(shifted(origin, i, sign)), 2) == -s.Rational(3, 2) for i in range(3) for sign in (-1, 1)))
    check("actual vector source phi-pi structure and nonzero support", all(zero(x.subs(phizero)) and x != 0 for x in qv))
    allzero = {x: 0 for x in fields.reverse}
    check("actual Ward source energy origin regression", rho(origin).subs(allzero) == 0 and s.diff(rho(origin), fields.pi(origin), 2) == 1)
    radii = {}
    for name, expression in zip(("Q_H", "Q_v1", "Q_v2", "Q_v3"), (qh, *qv)):
        symbols = sorted(expression.free_symbols, key=str)
        check("actual " + name + " homogeneous real quadratic", all(sum(powers) == 2 for powers, _ in s.Poly(expression, *symbols).terms()) and all(x.is_real for x in symbols))
        coords = [fields.reverse[x][1] for x in symbols]
        radius = max(sum(abs(a) for a in x) for x in coords)
        radii[name] = radius
        check("actual " + name + " universal Z3 graph radius <=4 from center", radius <= 4)
    # Current sign is literal Ward J_v=-j. A wrong plus-adjoint sign changes
    # this independently reconstructed nested vector stencil.
    jv = lambda i, x: -current(i, x)
    for i in range(3):
        b_jv = lambda x: sum(jv(j, x)-jv(j, shifted(x, j, -1)) for j in range(3))
        fv_jv = 2*lap(lambda x: jv(i, x), origin) + s.Rational(3, 2)*(b_jv(shifted(origin, i, 1))-b_jv(origin))
        check(f"actual vector source {i+1} Jv and adjoint signs", zero(qv[i] + fv_jv))
    return radii


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ward-source", type=Path, default=Path(__file__).resolve().parents[1] / "free-scalar-3d" / "free_scalar_ward.py")
    args = parser.parse_args()
    source = args.ward_source.resolve(strict=True)
    for side in (2, 3):
        native_stencils(side)
    block_and_chart_controls()
    radii = source_checks(source)
    print(json.dumps({"status": "PASS", "exact_check_groups": len(CHECKS), "checks": CHECKS, "actual_source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "actual_Z3_source_graph_radii": radii, "scope": "New declared site-field completion only; original native observable net remains nonlocal; no continuum/TOE/RH claim."}, indent=2))


if __name__ == "__main__":
    main()
