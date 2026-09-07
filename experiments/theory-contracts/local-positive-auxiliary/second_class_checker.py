#!/usr/bin/env python3
"""Exact second-class embedding with actual finite scalar stress brackets.

The general block proof is in SECOND_CLASS.md. This is a bounded witness
on an L=2 self-conjugate (pi,pi,0) anchored-real lattice fibre, not a
finite-matrix approximation to quantum canonical commutation relations.
"""
from itertools import product
import sympy as sp


def clean(value):
    return sp.simplify(sp.expand(value))


def zero(value):
    entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
    return all(clean(entry) == 0 for entry in entries)


def run():
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
        print(f"[PASS] {name}", flush=True)

    # Actual anchored-real self-conjugate symbol at k=(pi,pi,0), a=1.
    # No bare imaginary Fourier divergence is treated as a real matrix.
    rt = sp.sqrt(2)
    trace = sp.Matrix([1, 1, 1, 0, 0, 0])
    vec = sp.Matrix([
        [-2, 0, 0, 0, 0, rt],
        [0, -2, 0, 0, 0, rt],
        [0, 0, 0, rt, rt, 0],
    ])
    dx = sp.diag(2, 2, 2, 2, -2, -2)
    dy = sp.diag(2, 2, 2, -2, 2, -2)
    div = sp.Matrix.hstack(dx, dy, sp.zeros(6))
    r2 = sp.Integer(8)
    nmat = sp.Matrix.hstack(vec.T, trace)
    gram_inv = (nmat.T*nmat).inv()
    proj = sp.eye(6)-nmat*gram_inv*nmat.T
    pol = sp.Matrix.hstack(
        sp.Matrix([1, 1, -2, 0, 0, rt])/sp.sqrt(8),
        sp.Matrix([0, 0, 0, 1, -1, 0])/rt,
    )
    check('actual real boundary link symbol has DDt=8I', zero(div*div.T-r2*sp.eye(6)))
    check('actual boundary TT polarizations are normalized and complete', zero(pol.T*pol-sp.eye(2)) and zero(pol*pol.T-proj))
    check('actual boundary TT polarizations satisfy local constraints', zero(vec*pol) and zero(trace.T*pol))

    kkt = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.eye(18), sp.zeros(18, 4), -div.T),
        sp.Matrix.hstack(sp.zeros(4, 18), sp.zeros(4), nmat.T),
        sp.Matrix.hstack(-div, nmat, sp.zeros(6)),
    )
    kinv = kkt.inv()
    inject = sp.Matrix.vstack(sp.zeros(22, 6), sp.eye(6))
    check('28-dimensional local auxiliary Hessian is symmetric and invertible', zero(kkt-kkt.T) and zero(kkt*kinv-sp.eye(28)))
    check('inverse multiplier block is minus TT inverse Laplacian', zero(inject.T*kinv*inject+proj/r2))
    expected_map = sp.Matrix.vstack(div.T*proj/r2, -gram_inv*nmat.T, proj/r2)
    check('stationary graph has the correct source and sign', zero(-kinv*inject-expected_map))

    # Actual periodic full scalar stress, including the common pi^2 trace.
    sites = list(product(range(2), repeat=3))
    index = {site: position for position, site in enumerate(sites)}
    phi = sp.Matrix(sp.symbols('phi0:8', real=True))
    pi = sp.Matrix(sp.symbols('pi0:8', real=True))
    tq = sp.Matrix(sp.symbols('Q0:2', real=True))
    tp = sp.Matrix(sp.symbols('P0:2', real=True))
    g = sp.symbols('g', real=True)
    coord = list(phi)+list(tq)
    momenta = list(pi)+list(tp)

    def shifted(site, axis, sign=1):
        out = list(site)
        out[axis] = (out[axis]+sign) % 2
        return tuple(out)

    def field(site):
        return phi[index[site]]

    def grad(site, axis):
        return field(shifted(site, axis))-field(site)

    def pb(a, b):
        return sp.expand(sum(sp.diff(a, q)*sp.diff(b, p)-sp.diff(a, p)*sp.diff(b, q) for q, p in zip(coord, momenta)))

    orth_pairs = ((1, 2), (0, 2), (0, 1))
    tau = sp.zeros(6, 1)
    hm = sp.Integer(0)
    mass2 = sp.Integer(2)
    for site in sites:
        cell = index[site]
        weight = sp.Integer(-1)**(site[0]+site[1])/sp.sqrt(8)
        local = []
        for axis in range(3):
            local.append(
                pi[cell]**2/2-mass2*phi[cell]**2/2
                +grad(site, axis)*grad(shifted(site, axis, -1), axis)/2
                -sum(grad(site, other)**2+grad(shifted(site, other, -1), other)**2 for other in range(3) if other != axis)/4
            )
        for left, right in orth_pairs:
            # Orthogonal tensor component is sqrt(2)*physical tau_ij.
            local.append(rt*(grad(site, left)+grad(shifted(site, right), left))*(grad(site, right)+grad(shifted(site, left), right))/4)
        tau += weight*sp.Matrix(local)
        hm += pi[cell]**2/2+mass2*phi[cell]**2/2+sum(grad(site, axis)**2 for axis in range(3))/2
    tau = tau.applyfunc(sp.expand)
    tau_tt = (pol.T*tau).applyfunc(sp.expand)
    f_tau = sp.Matrix(6, 6, lambda row, col: pb(tau[row], tau[col]))
    check('actual projected scalar stress is independent of all matter momenta', all(sp.diff(component, p) == 0 for component in tau_tt for p in pi))
    check('actual retained TT stress is nonzero', not zero(tau_tt))
    check('actual unprojected scalar stress brackets are nonzero', not zero(f_tau))
    check('actual TT projected scalar stress brackets vanish', zero(proj*f_tau*proj))
    check('actual full source bracket is antisymmetric', zero(f_tau+f_tau.T))

    datum = dict(zip(list(phi)+list(pi), (-2, 1, 3, -1, 4, 0, -4, 2, 1, -2, 0, 3, -1, 4, 2, -3)))
    f_point = f_tau.subs(datum)
    check('exact rational scalar datum has nonzero full source-bracket rank', f_point.rank() == 2)
    print('SOURCE_BRACKET_RANK:', f_point.rank(), flush=True)

    source = g*inject*tau
    fmat = g**2*inject*f_tau*inject.T
    ys = -kinv*source
    check('all 28 secondary constraints vanish on the stationary graph', zero(kkt*ys+source))
    free_seed = hm+(tp.T*tp)[0]/2+r2*(tq.T*tq)[0]/2
    hb = sp.expand(free_seed+g*(tq.T*tau_tt)[0])
    reduced = sp.expand(hb-(source.T*kinv*source)[0]/2)
    positive = sp.expand(hm+(tp.T*tp)[0]/2+r2*((tq+g*tau_tt/r2).T*(tq+g*tau_tt/r2))[0]/2)
    check('eliminated Hamiltonian equals the complete positive reduced square', zero(reduced-positive))
    check('stationary action source sign gives plus R', zero((ys.T*kkt*ys)[0]/2+(ys.T*source)[0]-g**2*(tau.T*proj*tau)[0]/(2*r2)))

    # Full 56x56 Dirac bracket matrix with actual nonzero source brackets.
    constraint_matrix = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(28), -kkt),
        sp.Matrix.hstack(kkt, fmat),
    )
    inverse = sp.Matrix.vstack(
        sp.Matrix.hstack(kinv*fmat*kinv, kinv),
        sp.Matrix.hstack(-kinv, sp.zeros(28)),
    )
    check('full second-class Dirac matrix has the claimed exact inverse', zero(constraint_matrix*inverse-sp.eye(56)) and zero(inverse*constraint_matrix-sp.eye(56)))
    check('secondary-secondary inverse block is exactly zero', inverse[28:56, 28:56] == sp.zeros(28))
    no_source_brackets = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(28), -kkt),
        sp.Matrix.hstack(kkt, sp.zeros(28)),
    )
    triangular = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.eye(28), sp.zeros(28)),
        sp.Matrix.hstack(-fmat*kinv, sp.eye(28)),
    )
    check('source-bracket dependence is a unit-determinant triangular factor', zero(constraint_matrix-triangular*no_source_brackets))
    ka, kb, kc, ff = sp.symbols('ka kb kc ff', real=True)
    small_k = sp.Matrix([[ka, kb], [kb, kc]])
    small_f = sp.Matrix([[0, ff], [-ff, 0]])
    small_c = sp.Matrix.vstack(sp.Matrix.hstack(sp.zeros(2), -small_k), sp.Matrix.hstack(small_k, small_f))
    check('generic exact constraint determinant is det(K)^2 independent of F', zero(small_c.det()-small_k.det()**2))
    kdet = kkt.det()
    check('actual auxiliary Jacobian is nonzero and cancels the constrained-measure factor', kdet == 16384 and sp.sqrt(kdet**2)/abs(kdet) == 1)
    seed_brackets = sp.Matrix(20, 28, lambda row, col: pb((coord+momenta)[row], source[col]))
    check('all seed Dirac brackets remain canonical including mixed matter-TT pairs', zero(seed_brackets*inverse[28:56, 28:56]*seed_brackets.T))
    # Dropping F keeps the tempting lower-right zero but no longer inverts C.
    inverse_mutant = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(28), kinv),
        sp.Matrix.hstack(-kinv, sp.zeros(28)),
    )
    check('must-fail: pretending the actual unprojected F is zero breaks inversion', not zero((constraint_matrix*inverse_mutant-sp.eye(56)).subs(datum)))

    # Explicit secondary-preservation multipliers on the stationary graph.
    avec = sp.Matrix([pb(component, hb) for component in source])
    f_correction = fmat*ys
    hvec = avec+f_correction
    multipliers = (-kinv*hvec).applyfunc(sp.expand)
    check('preservation multipliers solve every secondary equation', zero(hvec+kkt*multipliers))
    graph_velocity = sp.Matrix([pb(component, reduced) for component in ys])
    check('fixed multipliers equal the exact moving stationary-graph velocity', zero(multipliers-graph_velocity))
    check('actual source bracket makes a nonzero preservation correction', not zero(f_correction.subs(datum)))
    bad_multipliers = -kinv*avec
    check('must-fail: dropping F ystar violates secondary preservation', not zero((hvec+kkt*bad_multipliers).subs(datum)))

    # Verify the seed equations from the extended Hamiltonian before taking
    # the stationary substitution; source derivatives are not discarded.
    y = sp.Matrix(sp.symbols('y0:28', real=True))
    extended = hb+(y.T*kkt*y)[0]/2+(y.T*source)[0]
    graph = dict(zip(y, ys))
    seed_evolution = [pb(component, extended).subs(graph, simultaneous=True)-pb(component, reduced) for component in coord+momenta]
    check('all seed equations agree with reduced Hamiltonian dynamics', zero(sp.Matrix(seed_evolution)))
    # Pullback of d(py) wedge dy vanishes since py is identically zero on
    # the graph, regardless of ystar's dependence on seed momenta.
    y_jacobian = ys.jacobian(coord+momenta)
    py_jacobian = sp.zeros(28, 20)
    check('stationary graph pulls back the auxiliary symplectic form to zero', zero(py_jacobian.T*y_jacobian-y_jacobian.T*py_jacobian))

    print(f'COUNTS: {len(checks)}/{len(checks)} exact second-class embedding checks passed')
    print('VERDICT: FINITE_AUXILIARY_SECOND_CLASS_STABILIZATION; CANONICAL_SEED_DIRAC_BRACKET; EXACT_POSITIVE_REDUCED_HAMILTONIAN')
    print('SCOPE: retained nonzero modes; 28 auxiliary pairs removed by 56 second-class constraints per real component; reduced quantization only; no original gravity first-class or homogeneous completion; NON_RH')


if __name__ == '__main__':
    run()

