#!/usr/bin/env python3
"""Exact actual-source/local-parent algebra and continuous Gaussian controls.

No finite CCR matrices, floating tolerances, continuum or full-TOE claim.
The operator convergence theorem is proved in PROOF.md, not numerically fitted.
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
    return all(clean(item) == 0 for item in values)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ward-source', type=Path,
                        default=Path(__file__).resolve().parents[1]
                        / 'free-scalar-3d/free_scalar_ward.py')
    args = parser.parse_args()
    source = args.ward_source.resolve(strict=True)
    spec = importlib.util.spec_from_file_location('round15_local_actual_ward', source)
    ward_module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = ward_module
    spec.loader.exec_module(ward_module)
    checks = []

    def check(name, condition):
        if not bool(condition):
            raise AssertionError(name)
        checks.append(name)

    fields = ward_module.Fields(period=2)
    ward = ward_module.WardComplex(fields)
    sites = list(product(range(2), repeat=3))
    phi = [fields.phi(x) for x in sites]
    pi = [fields.pi(x) for x in sites]
    pairs = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))
    rt = s.sqrt(2)
    trace = s.Matrix([1, 1, 1, 0, 0, 0])
    subst = {ward.a: 1, ward.mass2: 2}
    tau_sites, sigma_sites = [], []
    for x in sites:
        tau = s.Matrix([(1 if i == j else rt)*ward.tau(i, j, x)
                        for i, j in pairs]).subs(subst).applyfunc(clean)
        scalar_trace = (fields.pi(x)**2-2*fields.phi(x)**2)/2
        sigma = (tau-trace*scalar_trace).applyfunc(clean)
        check(f'ACTUAL source at {x}: all six components have the declared trace decomposition',
              zero(tau-sigma-trace*scalar_trace) and
              all(not entry.has(*pi) for entry in sigma))
        check(f'ACTUAL source at {x}: the retained source is quadratic in configuration',
              max(s.Poly(entry, *phi).total_degree() for entry in sigma) == 2)
        tau_sites.append(tau)
        sigma_sites.append(sigma)

    # Actual L2 (pi,pi,0) staggered raw-phase matrices. D link signs depend
    # on the tensor mask; this is not an unrelated continuum D symbol.
    masks = ((0, 0, 0), (0, 0, 0), (0, 0, 0),
             (0, 1, 1), (1, 0, 1), (1, 1, 0))
    plus, minus = (-2, -2, 0), (2, 2, 0)
    div = s.Matrix.hstack(*[s.diag(*(plus[i] if mask[i] else minus[i]
                                    for mask in masks)) for i in range(3)])
    vec = s.Matrix([[-2, 0, 0, 0, 0, rt],
                    [0, -2, 0, 0, 0, rt],
                    [0, 0, 0, rt, rt, 0]])
    nmat = s.Matrix.hstack(vec.T, trace)
    ell = s.Integer(8)
    frame = s.Matrix.hstack(s.Matrix([1, 1, -2, 0, 0, rt])/s.sqrt(8),
                           s.Matrix([0, 0, 0, 1, -1, 0])/rt)
    proj = frame*frame.T
    check('ACTUAL oriented link divergence has the exact ell=8 Gram',
          zero(div*div.T-ell*s.eye(6)))
    check('ACTUAL full local complement has rank four and stated determinant',
          nmat.rank() == 4 and (nmat.T*nmat).det() == ell**3/2)
    check('ACTUAL real TT frame is orthonormal, transverse, and traceless',
          zero(frame.T*frame-s.eye(2)) and zero(nmat.T*frame))
    check('ACTUAL TT projector equals elimination of the local complement',
          zero(proj-s.eye(6)+nmat*(nmat.T*nmat).inv()*nmat.T))
    weights = [s.Integer(-1)**(x[0]+x[1])/s.sqrt(8) for x in sites]
    tau = sum((w*tau for w, tau in zip(weights, tau_sites)), s.zeros(6, 1))
    sigma = sum((w*sig for w, sig in zip(weights, sigma_sites)), s.zeros(6, 1))
    tt = (frame.T*tau).applyfunc(clean)
    check('ACTUAL normalized TT source is unchanged by the local trace representative',
          zero(frame.T*(tau-sigma)))
    check('ACTUAL normalized TT source is genuinely nonzero, not a degenerate axial witness',
          not zero(tt) and s.Poly(tt[0], *phi).coeff_monomial(phi[0]**2) == s.Rational(1, 4))

    # Full 28-fast-coordinate exact Hessian at a rational stiffness.
    delta = s.Rational(1, 3)
    mh = (delta+ell/delta)*s.eye(6)
    base = s.diag(s.eye(18), delta*s.eye(4), mh)
    cmat = s.Matrix.hstack(div, -nmat, -s.eye(6))
    kk = base+cmat.T*cmat/delta
    lmat = (ell+delta)*s.eye(6)+nmat*nmat.T/delta+mh.inv()
    rr = lmat.inv()
    amap = s.Matrix.vstack(div.T*rr, -nmat.T*rr/delta, -mh.inv()*rr)
    check('ACTUAL parent retains all 28 fast coordinates with correct kinetic size',
          kk.shape == (28, 28) and cmat.shape == (6, 28))
    ld, dd = kk.LDLdecomposition(hermitian=True)
    check('ACTUAL fast Hessian is strictly positive, with all 28 exact positive LDL pivots',
          zero(ld*dd*ld.T-kk) and all(dd[i, i] > 0 for i in range(28)))
    check('ACTUAL proposed minimum has exactly the softened residual -delta R j',
          zero(cmat*amap-s.eye(6)+delta*rr))
    check('ACTUAL all 28 stationary equations hold for an independent six-component source',
          zero(kk*amap-cmat.T/delta))
    check('ACTUAL independent-source minimum is exactly the positive R kernel',
          zero(amap.T*base*amap+delta*rr.T*rr-rr))
    check('ACTUAL Hessian shift gives the same Schur kernel by a separate contraction',
          zero(s.eye(6)/delta-cmat*amap/delta-rr))
    check('ACTUAL finite-delta source kernel is strictly positive',
          all(value > 0 for value in rr.LDLdecomposition(hermitian=True)[1].diagonal()))
    check('ACTUAL finite-delta kernel is not falsely equal to target TT kernel',
          not zero(rr-proj/ell) and rr.rank() == 6 and proj.rank() == 2)

    q = s.Matrix(s.symbols('q0:6', real=True))
    src = s.Matrix(s.symbols('s0:6', real=True))
    g = s.symbols('g', real=True)
    target = ((ell*q+g*src).T*(proj/ell)*(ell*q+g*src))[0]/2
    expanded = ell*(q.T*proj*q)[0]/2+g*(q.T*proj*src)[0]+g*g*(src.T*proj*src)[0]/(2*ell)
    check('ACTUAL target retains the entire q-quadratic, cubic and source-quartic square',
          zero(target-expanded))
    source_square = ((sigma.T*proj*sigma)[0]/(2*ell)).applyfunc(clean) if isinstance((sigma.T*proj*sigma)[0], s.MatrixBase) else clean((sigma.T*proj*sigma)[0]/(2*ell))
    check('ACTUAL source quartic equals the old normalized TT sum and is nonzero',
          zero(source_square-(tt.T*tt)[0]/(2*ell)) and not zero(source_square))

    # Universal eigenchannel formulas, not fits of the rational matrix above.
    ddelt, ll, mu = s.symbols('delta l mu', positive=True)
    ad = ll+ddelt+ddelt/(ddelt**2+ll)
    check('UNIVERSAL TT eigenvalue converges to positive inverse Laplacian',
          s.limit(1/ad, ddelt, 0, dir='+') == 1/ll)
    check('UNIVERSAL all four complement eigenchannels disappear',
          s.limit(1/(ad+mu/ddelt), ddelt, 0, dir='+') == 0)
    check('UNIVERSAL TT convergence difference and O(delta) upper bound have correct signs',
          zero(1/ll-1/ad-(ad-ll)/(ll*ad)) and
          s.factor((1+1/ll)/ll**2-(1/ll-1/ad)/ddelt).is_positive is True)
    nzero = s.Matrix.hstack(s.zeros(6, 3), trace)
    rzero = ((ddelt+1/ddelt)*s.eye(6)+nzero*nzero.T/ddelt).inv()
    ptr = trace*trace.T/3
    pfree = s.eye(6)-ptr
    check('HOMOGENEOUS all five traceless source means have the declared screened eigenvalue',
          zero(rzero*pfree-ddelt*pfree/(ddelt**2+1)))
    check('HOMOGENEOUS trace source has its distinct screened eigenvalue',
          zero(rzero*ptr-ddelt*ptr/(ddelt**2+4)))
    check('HOMOGENEOUS every source mean disappears in the limit, without inversion of ell zero',
          zero(rzero.applyfunc(lambda val: s.limit(val, ddelt, 0, dir='+'))))
    rzero_without_h = (ddelt*s.eye(6)+nzero*nzero.T/ddelt).inv()
    check('NEGATIVE CONTROL omitting the new h field leaves divergent traceless means',
          zero(rzero_without_h*pfree-pfree/ddelt))
    nsites = s.symbols('n', integer=True, positive=True)
    check('MODE COUNT: seven slow plus 28 fast pairs per site, with 4n+2 extra slow limit modes',
          7*nsites+28*nsites == 35*nsites and
          6*nsites-2*(nsites-1) == 4*nsites+2)

    # Healthy-source-sign control: a divergent contact really is present.
    a, j = s.symbols('a j', real=True)
    kk0, cc0 = s.symbols('k c', positive=True)
    bare = kk0*a*a/2+(cc0*a-j)**2/(2*ddelt)
    amin = cc0*j/(ddelt*kk0+cc0**2)
    induced = s.factor(bare.subs(a, amin))
    check('SIGN CONTROL positive net response comes from explicit positive source contact',
          zero(induced-j*j/(2*(ddelt+cc0**2/kk0))))
    no_contact = bare-j*j/(2*ddelt)
    check('NEGATIVE CONTROL deleting bare contact restores the negative Schur response',
          zero(no_contact.subs(a, amin)+cc0**2*j*j/(2*ddelt*(ddelt*kk0+cc0**2))))

    # Continuous Gaussian operator check; MODEL K=4, f(x)=g*x^2, eta=r^4.
    # It verifies universal derivative constants using actual quadratic-source degree,
    # but does not replace the actual 28n-dimensional K with a finite quantum matrix.
    x, y, b = s.symbols('x y b', real=True)
    r = s.symbols('r', positive=True)
    psi, psi1 = s.symbols('psi psi1', real=True)
    f = g*x*x
    chi = (2*r*r/s.pi)**s.Rational(1, 4)*s.exp(-r*r*(y-f)**2)
    density = s.sqrt(2*r*r/s.pi)*s.exp(-2*r*r*b*b)
    check('CONTINUOUS Gaussian encoding has exactly unit positive norm',
          s.integrate(density, (b, -s.oo, s.oo)) == 1)
    fast_image = -s.diff(chi, y, 2)/(2*r**4)+2*(y-f)**2*chi
    check('CONTINUOUS fast zero-point energy is exactly 1/r^2 for K=4 and eta=r^4',
          zero(s.simplify(fast_image/chi)-1/r**2))
    derivative1 = s.simplify(s.diff(chi, x)/chi).subs(y, b+f)
    derivative2 = s.simplify(s.diff(chi, x, 2)/chi).subs(y, b+f)
    residual = clean(-psi1*derivative1-psi*derivative2/2)
    moments = {2*i: s.factorial2(2*i-1)/(4*r*r)**i for i in range(1, 5)}
    moments[0] = 1

    def average(polynomial):
        pol = s.Poly(s.expand(polynomial), b)
        return clean(sum(coeff*(moments.get(power[0], 0))
                         for power, coeff in pol.terms()))

    check('CONTINUOUS first derivative has zero Berry connection', average(derivative1) == 0)
    check('CONTINUOUS Gaussian derivative metric has the exact eta^(1/2) coefficient',
          zero(average(derivative1**2)-4*g*g*x*x*r*r))
    check('CONTINUOUS finite-mass compression has a nonzero positive correction',
          zero(average(residual)-2*g*g*x*x*r*r*psi))
    check('CONTINUOUS full operator residual squared is O(eta^(1/2))+O(eta)',
          zero(average(residual**2)-g*g*r*r*(2*x*psi1+psi)**2
               -12*g**4*x**4*r**4*psi**2))
    check('NEGATIVE CONTROL claiming exact finite-mass intertwining fails',
          average(residual).subs({g: 1, x: 1, r: 1, psi: 1}) == 2)
    shift = s.symbols('shift', real=True)
    delta_f = s.expand(f.subs(x, x+shift)-f)
    overlap = s.exp(-r*r*delta_f**2/2)
    check('CONTINUOUS encoded Weyl compression loses isometry at finite parameters',
          overlap.subs({g: 1, x: 0, shift: 1, r: 1}) == s.exp(-s.Rational(1, 2)))

    print(json.dumps({
        'status': 'PASS',
        'exact_check_groups': len(checks),
        'checks': checks,
        'actual_source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'actual_source_witness': 'All six stress components at all 8 L2 sites; actual nonzero (pi,pi,0) TT mode and all 28 fast fiber coordinates',
        'canonical_pairs_per_site': 35,
        'added_fast_pairs_per_site': 28,
        'quantum_residual': 'C(delta,psi)*eta^(1/4)+D(delta,psi)*eta^(1/2) on the compact smooth slow core',
        'scope': 'New local positive dynamical family; sequential fixed-lattice quantum limit with explicit energy subtraction and extra free modes. Not finite-parameter equivalence, causal continuum, TFPT selection, or complete TOE.'
    }, indent=2))


if __name__ == '__main__':
    main()
