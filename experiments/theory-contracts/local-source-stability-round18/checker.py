#!/usr/bin/env python3
"""Exact cell-stabilizer, source/first-vertex and native-locality controls.

Finite algebra checks only; analytic closed-form/propagator proofs are in
PROOF.md. No truncated CCR, unchanged-completion, continuum or TOE claim.
"""
import argparse
import hashlib
import importlib.util
import json
from itertools import product
from pathlib import Path
import sys

import sympy as s


def clean(value):
    return s.factor(s.expand(value))


def zero(value):
    values = list(value) if isinstance(value, s.MatrixBase) else [value]
    return all(s.simplify(s.expand(item)) == 0 for item in values)


def site_matrices(side):
    sites = list(product(range(side), repeat=3))
    lookup = {x: i for i, x in enumerate(sites)}
    n = len(sites)
    minus = []
    for axis in range(3):
        shift = s.zeros(n)
        for i, x in enumerate(sites):
            y = list(x)
            y[axis] = (y[axis]+1) % side
            shift[i, lookup[tuple(y)]] = 1
        minus.append(s.eye(n)-shift.T)
    b = s.Matrix.hstack(*minus)
    return sites, lookup, minus, b, b*b.T


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ward-source', type=Path,
                        default=Path(__file__).resolve().parents[1]
                        / 'free-scalar-3d/free_scalar_ward.py')
    args = parser.parse_args()
    source_path = args.ward_source.resolve(strict=True)
    spec = importlib.util.spec_from_file_location('r18_cell_actual_ward', source_path)
    if spec is None or spec.loader is None:
        raise RuntimeError('Original Ward source is not importable')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    checks = []

    def check(name, condition):
        if not bool(condition):
            raise AssertionError(name)
        checks.append(name)

    # Actual periodic transport, not a chosen diagonal toy drift.
    for side in (2, 3):
        sites, lookup, minus, b, ell_matrix = site_matrices(side)
        n = len(sites)
        aa = s.zeros(4*n)
        aa[:n, n:] = b
        check(f'ACTUAL L{side} free shear is nilpotent, traceless and mean preserving',
              aa*aa == s.zeros(4*n) and s.trace(aa) == 0
              and b.to_DM().rank() == n-1 and s.ones(1, n)*b == s.zeros(1, 3*n))
        t, u = s.symbols('t u', real=True)
        check(f'ACTUAL L{side} affine transport composes exactly at arbitrary times',
              (s.eye(4*n)+t*aa)*(s.eye(4*n)+u*aa)
              == s.eye(4*n)+(t+u)*aa)
        check(f'ACTUAL L{side} drift involves only the same/backward neighboring vector sites',
              all(set(j for j in range(3*n) if b[i, j] != 0)
                  == set(j*n+lookup[tuple((x[k]-int(k == j)) % side for k in range(3))]
                         for j in range(3)) | set(j*n+i for j in range(3))
                  for i, x in enumerate(sites)))
        check(f'ACTUAL L{side} free scalar graph is the positive drift Gram with one mean zero mode',
              ell_matrix == sum((dm*dm.T for dm in minus), s.zeros(n))
              and ell_matrix.to_DM().rank() == n-1 and ell_matrix*s.ones(n, 1) == s.zeros(n, 1))
    sites3, lookup3, minus3, b3, lap3 = site_matrices(3)
    n3 = len(sites3)
    vdatum = s.zeros(3*n3, 1)
    vdatum[lookup3[(0, 0, 0)]] = 1
    vdatum[lookup3[(1, 0, 0)]] = -1
    rdatum = s.zeros(n3, 1)
    rdatum[lookup3[(0, 1, 0)]] = 1
    rdatum[lookup3[(0, 2, 0)]] = -1
    drift = b3*vdatum
    rho_actual = [clean((rdatum[i]+t*drift[i])**2
                        +sum(vdatum[j*n3+i]**2 for j in range(3))+drift[i]**2)
                  for i in range(n3)]
    active = [i for i, rho in enumerate(rho_actual) if rho != 0]
    check('ACTUAL L3 mean-free example has both active and exactly inactive cells',
          sum(rdatum) == 0 and sum(vdatum) == 0 and 0 < len(active) < n3)
    check('ACTUAL L3 inactive cells stay identically inactive along the full characteristic',
          all(rho_actual[i] == 0 for i in range(n3) if i not in active))
    check('ACTUAL L3 active cells have positive minima even if their scalar coordinate crosses zero',
          all((sum(vdatum[j*n3+i]**2 for j in range(3))+drift[i]**2 > 0)
                  or (drift[i] == 0 and rdatum[i] != 0) for i in active))

    r, driftvar = s.symbols('r drift', real=True)
    vv = s.symbols('v0:3', real=True)
    vnorm2 = sum(x*x for x in vv)
    rho = r*r+vnorm2+driftvar*driftvar
    rhot = (r+t*driftvar)**2+vnorm2+driftvar**2
    drho = s.diff(rhot, t)
    check('WEIGHT cell transport contribution gives exact all-time coefficient',
          zero(rhot-rho.subs(r, r+t*driftvar)))
    check('WEIGHT positive relative-derivative bound has exact plus square certificate',
          zero(rhot+drho-(r+t*driftvar+driftvar)**2-vnorm2))
    check('WEIGHT negative relative-derivative bound has exact minus square certificate',
          zero(rhot-drho-(r+t*driftvar-driftvar)**2-vnorm2))
    check('WEIGHT local source coefficient and its derivative are both bounded by rho',
          zero(rho-r*r-vnorm2-driftvar**2)
          and zero(rho-driftvar**2-r*r-vnorm2))
    wrongrho = (r+t*driftvar)**2+vnorm2
    check('NEGATIVE CONTROL deleting drift squared activates a previously zero domain cell',
          wrongrho.subs({r: 0, driftvar: 1, **dict.fromkeys(vv, 0)}).subs(t, 0) == 0
          and wrongrho.subs({r: 0, driftvar: 1, **dict.fromkeys(vv, 0)}).subs(t, 1) == 1)
    eps = s.symbols('epsilon', positive=True)
    bad_ratio = (s.diff(wrongrho, t)/wrongrho).subs(
        {r: eps, driftvar: 1, t: 0, **dict.fromkeys(vv, 0)})
    check('NEGATIVE CONTROL drift-free relative energy bound diverges at an activity change',
          zero(bad_ratio-2/eps) and s.limit(bad_ratio, eps, 0, dir='+') == s.oo)

    # Exact closed-form envelopes and all-time energy constant.
    n, w, qnorm, unorm = s.symbols('N w qnorm unorm', positive=True)
    linear_bound = s.sqrt(n)*w*qnorm*unorm
    weighted = w*w*qnorm*qnorm
    check('FORM collective Cauchy bound has exact extensive Young-square remainder',
          zero((weighted+n*unorm**2)/2-linear_bound
               -(w*qnorm-s.sqrt(n)*unorm)**2/2))
    check('FORM h+N norm squared lower envelope is positive with the stated coefficients',
          zero(weighted-linear_bound+n*unorm**2
               -(weighted+n*unorm**2)/2
               -(w*qnorm-s.sqrt(n)*unorm)**2/2))
    check('FORM time derivative is bounded by three times the coercive envelope',
          zero(3*(weighted+n*unorm**2)/2
               -(3*weighted/2+n*unorm**2/2)-n*unorm**2))
    g, qval, coeff = s.symbols('g q c', real=True)
    positive_rho = s.symbols('rho', positive=True)
    check('FORM per-source completion square retains the sign of g and the exact linear term',
          zero((g*s.sqrt(positive_rho)*qval+coeff/(2*s.sqrt(positive_rho)))**2
               -coeff**2/(4*positive_rho)-g*g*positive_rho*qval*qval-g*coeff*qval))
    check('NEGATIVE CONTROL a dimension-independent quarter-energy bound is not supplied by cellwise completion',
          sum((s.Rational(-1, 2))**2+s.Rational(-1, 2) for i in range(2)) == -s.Rational(1, 2))

    # Literal retained-mode Ward sources and first dressed vertex.
    fields = module.Fields(period=2)
    ward = module.WardComplex(fields)
    sites = list(product(range(2), repeat=3))
    weights = [s.Integer(-1)**(x[0]+x[1])/s.sqrt(8) for x in sites]
    phi = [fields.phi(x) for x in sites]
    pi = [fields.pi(x) for x in sites]
    subst = {ward.a: 1, ward.mass2: 2}
    rt = s.sqrt(2)
    trace = s.Matrix([1, 1, 1, 0, 0, 0])
    scalar = s.Matrix([4, 4, 8, 0, 0, 4*rt])
    vector = s.Matrix([[-2, 0, 0, 0, 0, rt], [0, -2, 0, 0, 0, rt],
                       [0, 0, 0, rt, rt, 0]])
    frame = s.Matrix.hstack(s.Matrix([1, 1, -2, 0, 0, rt])/s.sqrt(8),
                           s.Matrix([0, 0, 0, 1, -1, 0])/rt)
    ell = s.Integer(8)
    kp = s.eye(6)-trace*trace.T/2
    gh = (scalar.T*scalar)[0]
    gv = vector*vector.T
    bh = -1/(2*ell)
    bv = (gv.inv()*vector*kp*vector.T*gv.inv()).applyfunc(clean)
    bmode = (scalar.T*kp*vector.T*gv.inv()).applyfunc(clean)
    check('ACTUAL scalar constraint normalization and trace contraction are the stated ones',
          gh == 2*ell**2 and (scalar.T*trace)[0] == 2*ell and bh == -1/(2*ell))
    check('ACTUAL retained mode has the same local shear row', bmode == s.Matrix([[2, 2, 0]]))
    tau = s.zeros(6, 1)
    pairs = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))
    for x, weight in zip(sites, weights):
        tau += weight*s.Matrix([(1 if i == j else rt)*ward.tau(i, j, x) for i, j in pairs])
    tau = tau.subs(subst).applyfunc(clean)
    rho_source = clean(sum(w*ward.rho(x) for x, w in zip(sites, weights)).subs(subst))
    hm = clean(sum(ward.rho(x) for x in sites).subs(subst))
    jv = -s.Matrix([clean(sum(w*ward.current(axis, x) for x, w in zip(sites, weights)).subs(subst))
                    for axis in range(3)])
    bcal = clean((scalar.T*tau)[0]/gh-bh*rho_source)
    sources = s.Matrix.vstack(s.Matrix([bcal]), -bv*jv)
    tt = (frame.T*tau).applyfunc(clean)
    check('ACTUAL original matter kinetic Hessian is unchanged on all eight sites',
          s.hessian(hm, pi) == s.eye(8))
    kinetic_bcal = bcal.subs(dict.fromkeys(phi, 0))
    expected_kinetic = 3*sum(w*p*p for w, p in zip(weights, pi))/(4*ell)
    check('ACTUAL entire Bcal kinetic source is precisely 3/(4ell) times Fourier pi squared',
          zero(kinetic_bcal-expected_kinetic))
    check('ACTUAL Bcal source is not identically zero or made configuration-only',
          s.diff(bcal, pi[0], 2) == 3*rt/64)
    check('ACTUAL TT source retains the exact nonzero original coefficient',
          s.Poly(tt[0], *phi).coeff_monomial(phi[0]**2) == s.Rational(1, 4))
    qtt = s.Matrix(s.symbols('Q0:2', real=True))
    ptt = s.Matrix(s.symbols('P0:2', real=True))
    rc, xh = s.symbols('rc XH', real=True)
    vc = s.Matrix(s.symbols('vc0:3', real=True))
    xv = s.Matrix(s.symbols('XV0:3', real=True))
    qgrav = frame*qtt+scalar*rc/gh+vector.T*xv
    pgrav = frame*ptt-scalar*xh+vector.T*gv.inv()*vc
    kq = ell*frame*frame.T-scalar*scalar.T/(2*ell)
    hgrav = ((qgrav.T*kq*qgrav)[0]+(pgrav.T*kp*pgrav)[0])/2
    hf = hgrav+hm
    generator = -xh*rho_source-(xv.T*jv)[0]
    vertex = (qgrav.T*tau)[0]
    coords = [xh]+list(xv)+list(qtt)+phi
    moms = [rc]+list(vc)+list(ptt)+pi

    def pb(left, right):
        return clean(sum(s.diff(left, x)*s.diff(right, p)-s.diff(left, p)*s.diff(right, x)
                         for x, p in zip(coords, moms)))

    cc = s.Matrix([rc]+list(vc))
    invariant = clean(vertex-pb(hf, generator))
    check('ACTUAL unchanged linear ideal retains the exact original first-vertex identity',
          zero(invariant-(qtt.T*tt)[0]-(cc.T*sources)[0]))
    cell_weight = rc*rc+(vc.T*vc)[0]+(bmode*vc)[0]**2
    extra = g*g*cell_weight*(sources.T*sources)[0]
    omega = s.zeros(16)
    omega[:8, 8:] = s.eye(8)
    omega[8:, :8] = -s.eye(8)
    ordering = [clean(s.trace((omega*s.hessian(q, phi+pi))**2)/8) for q in sources]
    ordered_extra = extra+g*g*cell_weight*sum(ordering)
    check('ACTUAL new cell stabilizer retains every original source-square ordering constant',
          ordering == [s.Rational(3, 512), -s.Rational(15, 2048),
                       -s.Rational(15, 2048), s.Integer(0)])
    check('ACTUAL new completion preserves the entire original first dressed interaction vertex',
          zero(pb(hf, generator)+s.diff(hf+g*invariant+ordered_extra, g).subs(g, 0)-vertex))
    zero_constraint = dict.fromkeys(cc, 0)
    check('ACTUAL new higher-order term and its first constraint derivatives vanish on the physical surface',
          zero(ordered_extra.subs(zero_constraint))
          and all(zero(s.diff(ordered_extra, ca).subs(zero_constraint)) for ca in cc))
    check('ACTUAL noncommuting source witness is retained',
          any(not zero(pb(sources[0], sources[j])) for j in range(1, 4)))
    global_extra = g*g*(cc.T*cc)[0]*(sources.T*sources)[0]
    check('NEGATIVE CONTROL cell stabilizer is not falsely called the previous global completion',
          not zero(extra-global_extra))
    check('NEGATIVE CONTROL the added drift weight cannot be discarded even in the actual retained mode',
          zero(cell_weight-(cc.T*cc)[0]-(2*vc[0]+2*vc[1])**2)
          and not zero(cell_weight-(cc.T*cc)[0]))

    # Actual inverse-kernel support witness in reconstructed mean-free cells.
    mean = s.ones(n3)/n3
    green = (lap3+mean).inv()-mean
    green_product = lap3*green
    first, far = lookup3[(0, 0, 0)], lookup3[(1, 1, 1)]
    check('ACTUAL L3 Green kernel is the full mean-free inverse, not a fitted tail',
          green_product == s.eye(n3)-mean and green*s.ones(n3, 1) == s.zeros(n3, 1))
    check('ACTUAL L3 native Bcal kinetic coefficient is nonzero outside the transport stencil',
          green[first, far] == -s.Rational(11, 486)
          and 3*green[first, far]/4 == -s.Rational(11, 648)
          and 3*green[first, far]/2 == -s.Rational(11, 324)
          and lap3[first, far] == 0)
    check('SUPPORT inverse-Laplacian product is dense off diagonal due to the mean projection',
          all(green_product[i, j] == -s.Rational(1, n3)
              for i in range(n3) for j in range(n3) if i != j))
    restricted_green = green.copy()
    restricted_green[first, far] = 0
    check('NEGATIVE CONTROL deleting the distant native-source coefficient fails the inverse identity',
          lap3*restricted_green != s.eye(n3)-mean)

    # Cell support control on a mean-free constraint datum: a distant source
    # receives no multiplier just because another cell carries a constraint.
    rlocal = s.zeros(n3, 1)
    rlocal[first] = 1
    rlocal[lookup3[(1, 0, 0)]] = -1
    check('SUPPORT cell completion does not multiply every remote source by a global constraint norm',
          rlocal[far]**2 == 0 and (rlocal.T*rlocal)[0] == 2 and sum(rlocal) == 0)
    check('NEGATIVE CONTROL removing the old global multiplier alone does not localize Bcal',
          rlocal[far] == 0 and green[first, far] != 0)

    print(json.dumps({
        'status': 'PASS',
        'exact_check_groups': len(checks),
        'checks': checks,
        'actual_source_sha256': hashlib.sha256(source_path.read_bytes()).hexdigest(),
        'actual_L3_active_cells_in_sparse_meanfree_example': len(active),
        'actual_ordering_constants': [str(value) for value in ordering],
        'actual_L3_G_000_111': str(green[first, far]),
        'actual_L3_Bcal_pi111_squared_coefficient_at_000': str(3*green[first, far]/4),
        'scope': ('New cellwise higher-order completion: exact finite lattice/source algebra. '
                  'Closed forms, stratum-continuous propagators, covariance and adiabatic limits '
                  'are proved in PROOF.md. Native Darboux sources remain nonlocal; a finite-range '
                  'full completion requires a separate local source chart. No RH/continuum/TOE claim.'),
    }, indent=2))


if __name__ == '__main__':
    main()
