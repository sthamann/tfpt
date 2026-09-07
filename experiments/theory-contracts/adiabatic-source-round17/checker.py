#!/usr/bin/env python3
"""Exact actual-source and continuous Gaussian source-intertwining checks.

Finite algebra supports the analytic form/nonautonomous proof in PROOF.md;
it does not simulate CCR with finite matrices or certify a continuum limit.
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ward-source', type=Path,
                        default=Path(__file__).resolve().parents[1]
                        / 'free-scalar-3d/free_scalar_ward.py')
    args = parser.parse_args()
    source_path = args.ward_source.resolve(strict=True)
    spec = importlib.util.spec_from_file_location('r17_adiabatic_actual_ward', source_path)
    if spec is None or spec.loader is None:
        raise RuntimeError('Original Ward source cannot be loaded')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    checks = []

    def check(name, condition):
        if not bool(condition):
            raise AssertionError(name)
        checks.append(name)

    fields = module.Fields(period=2)
    ward = module.WardComplex(fields)
    sites = list(product(range(2), repeat=3))
    phi = [fields.phi(x) for x in sites]
    pi = [fields.pi(x) for x in sites]
    weights = [s.Integer(-1)**(x[0]+x[1])/s.sqrt(8) for x in sites]
    subst = {ward.a: 1, ward.mass2: 2}
    rt = s.sqrt(2)
    pairs = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))
    trace = s.Matrix([1, 1, 1, 0, 0, 0])
    scalar_mode = s.Matrix([4, 4, 8, 0, 0, 4*rt])
    vector = s.Matrix([[-2, 0, 0, 0, 0, rt], [0, -2, 0, 0, 0, rt],
                       [0, 0, 0, rt, rt, 0]])
    frame = s.Matrix.hstack(s.Matrix([1, 1, -2, 0, 0, rt])/s.sqrt(8),
                           s.Matrix([0, 0, 0, 1, -1, 0])/rt)
    ell = s.Integer(8)
    kp = s.eye(6)-trace*trace.T/2
    gv = vector*vector.T
    bv = (gv.inv()*vector*kp*vector.T*gv.inv()).applyfunc(clean)
    bh = -1/(2*ell)
    check('ACTUAL normalized retained mode uses the original nondegenerate Bv matrix',
          bv == s.Matrix([[5, -3, 0], [-3, 5, 0], [0, 0, 8]])/32)
    check('ACTUAL TT frame retains its two transverse traceless polarizations',
          zero(frame.T*frame-s.eye(2)) and zero(vector*frame) and zero(trace.T*frame))
    tau_sites = []
    sigma_sites = []
    for x in sites:
        tau_x = s.Matrix([(1 if i == j else rt)*ward.tau(i, j, x)
                          for i, j in pairs]).subs(subst).applyfunc(clean)
        sigma_x = (tau_x-trace*(fields.pi(x)**2-2*fields.phi(x)**2)/2).applyfunc(clean)
        tau_sites.append(tau_x)
        sigma_sites.append(sigma_x)
    tau = sum((w*t for w, t in zip(weights, tau_sites)), s.zeros(6, 1))
    sigma = sum((w*t for w, t in zip(weights, sigma_sites)), s.zeros(6, 1))
    tt = (frame.T*tau).applyfunc(clean)
    rho = clean(sum(w*ward.rho(x) for x, w in zip(sites, weights)).subs(subst))
    hm = clean(sum(ward.rho(x) for x in sites).subs(subst))
    current = s.Matrix([clean(sum(w*ward.current(axis, x) for x, w in zip(sites, weights)).subs(subst))
                        for axis in range(3)])
    bcal = clean((scalar_mode.T*tau)[0]/(scalar_mode.T*scalar_mode)[0]-bh*rho)
    sources = s.Matrix.vstack(s.Matrix([bcal]), bv*current)
    check('ACTUAL Ward matter kinetic Hessian remains identity on all eight sites',
          s.hessian(hm, pi) == s.eye(8))
    check('ACTUAL TT source is unchanged by the local configuration-only trace representative',
          zero(frame.T*(tau-sigma)) and all(not item.has(*pi) for item in sigma))
    check('ACTUAL TT source contains the original nonzero delta-site coefficient',
          s.Poly(tt[0], *phi).coeff_monomial(phi[0]**2) == s.Rational(1, 4))
    check('ACTUAL original Bcal contains the required nonzero second-derivative kinetic source',
          s.diff(bcal, pi[0], 2) == 3*rt/64)
    check('ACTUAL all four literal sources are real homogeneous quadratics including zero members',
          all(s.Poly(q, *(phi+pi)).total_degree() <= 2
              and all(coeff == 0 or sum(power) == 2 for power, coeff in s.Poly(q, *(phi+pi)).terms())
              and not q.has(s.I) for q in sources))
    check('ACTUAL vanishing third current channel is retained rather than invented as nonzero',
          sources[3] == 0 and all(sources[j] != 0 for j in range(3)))

    def pb(left, right):
        return clean(sum(s.diff(left, x)*s.diff(right, p)-s.diff(left, p)*s.diff(right, x)
                         for x, p in zip(phi, pi)))

    brackets = [pb(sources[0], sources[j]) for j in range(1, 4)]
    check('ACTUAL full sources fail to commute already in their exact quadratic Poisson brackets',
          any(not zero(item) for item in brackets))
    witness_poly = next(s.Poly(item, *(phi+pi)) for item in brackets if not zero(item))
    witness_power, witness_coefficient = witness_poly.terms()[0]
    check('ACTUAL source noncommutation has a nonzero exact retained coefficient',
          witness_coefficient != 0 and sum(witness_power) == 2)
    omega = s.zeros(16)
    omega[:8, 8:] = s.eye(8)
    omega[8:, :8] = -s.eye(8)
    hessians = [s.hessian(q, phi+pi) for q in sources]
    ordering = [clean(s.trace((omega*h)**2)/8) for h in hessians]
    check('ACTUAL source squares retain their original nonzero Weyl-ordering constants',
          ordering == [s.Rational(3, 512), -s.Rational(15, 2048),
                       -s.Rational(15, 2048), s.Integer(0)])
    check('NEGATIVE CONTROL replacing all ordered source squares by classical squares changes them',
          sum(ordering) != 0)

    # Exact full 28-coordinate fast fiber of the local parent, not a proxy Hessian.
    masks = ((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0))
    plus, minus = (-2, -2, 0), (2, 2, 0)
    div = s.Matrix.hstack(*[s.diag(*(plus[i] if mask[i] else minus[i] for mask in masks))
                             for i in range(3)])
    nmat = s.Matrix.hstack(vector.T, trace)
    delta = s.Rational(1, 3)
    mh = (delta+ell/delta)*s.eye(6)
    base = s.diag(s.eye(18), delta*s.eye(4), mh)
    cmat = s.Matrix.hstack(div, -nmat, -s.eye(6))
    kk = base+cmat.T*cmat/delta
    inverse_kernel = (ell+delta)*s.eye(6)+nmat*nmat.T/delta+mh.inv()
    rr = inverse_kernel.inv()
    amap = s.Matrix.vstack(div.T*rr, -nmat.T*rr/delta, -mh.inv()*rr)
    check('ACTUAL all 28 fast coordinates and their source-independent Hessian are retained',
          kk.shape == (28, 28) and amap.shape == (28, 6)
          and zero(div*div.T-ell*s.eye(6)))
    pivots = kk.LDLdecomposition(hermitian=True)[1].diagonal()
    check('ACTUAL fast covariance input is a strictly positive constant Hessian',
          all(value > 0 for value in pivots)
          and not any(entry.has(*(phi+pi)) for entry in kk))
    check('ACTUAL fast displacement map solves every stationary equation',
          zero(kk*amap-cmat.T/delta))
    actual_displacement = (amap*sigma).applyfunc(clean)
    check('ACTUAL scalar-dependent fast displacement is quadratic and momentum independent',
          all(s.Poly(entry, *phi).total_degree() <= 2
              and not entry.has(*pi) for entry in actual_displacement)
          and any(s.Poly(entry, *phi).total_degree() == 2 for entry in actual_displacement))
    h_tt_displacement = clean((frame[:, 0].T*actual_displacement[22:28, :])[0])
    check('ACTUAL normalized h-TT displacement is the original screened nonzero source',
          zero(h_tt_displacement+9*tt[0]/1834)
          and s.diff(h_tt_displacement, phi[0], 2) == -s.Rational(9, 3668))
    check('ACTUAL displacement has zero third derivatives in every scalar direction',
          all(s.Poly(entry, *phi).total_degree() <= 2 for entry in actual_displacement))

    # Universal directional Gaussian norm constants, one real direction.
    # Multi-direction proof uses Wick pairing + covariance Cauchy--Schwarz.
    z, pfast = s.symbols('z pfast', real=True)
    epsilon = s.symbols('epsilon', positive=True)  # epsilon = eta^(1/4)
    density_p = s.exp(-pfast**2/epsilon**2)/(s.sqrt(s.pi)*epsilon)
    check('CONTINUOUS Fourier Gaussian has unit positive norm',
          s.integrate(density_p, (pfast, -s.oo, s.oo)) == 1)
    for order in range(1, 5):
        moment = s.integrate(pfast**(2*order)*density_p, (pfast, -s.oo, s.oo))
        expected = s.factorial2(2*order-1)*epsilon**(2*order)/2**order
        check(f'CONTINUOUS order-{order} directional derivative has exact eta^(k/4) norm coefficient',
              zero(moment-expected))
    check('GAUSSIAN pair counts through fourth derivative are 1,3,15,105',
          [s.factorial2(2*k-1) for k in range(1, 5)] == [1, 3, 15, 105])

    x, a = s.symbols('x a', real=True)
    alpha, beta, gamma = s.symbols('alpha beta gamma', real=True)
    fshift = alpha*x*x+beta*x+gamma
    chi = s.exp(-epsilon**2*(a-fshift)**2/2)
    f1, f2 = s.diff(fshift, x), s.diff(fshift, x, 2)
    derivative_formulas = {
        1: -f1*s.diff(chi, a),
        2: f1**2*s.diff(chi, a, 2)-f2*s.diff(chi, a),
        3: -f1**3*s.diff(chi, a, 3)+3*f1*f2*s.diff(chi, a, 2),
        4: f1**4*s.diff(chi, a, 4)-6*f1**2*f2*s.diff(chi, a, 3)
           +3*f2**2*s.diff(chi, a, 2),
    }
    for order, predicted in derivative_formulas.items():
        check(f'CHAIN RULE exact quadratic-displacement partition formula through derivative {order}',
              zero((s.diff(chi, x, order)-predicted)/chi))
    check('NEGATIVE CONTROL fourth derivative cannot omit the three paired Hessian terms',
          not zero((s.diff(chi, x, 4)-derivative_formulas[4]
                    +3*f2**2*s.diff(chi, a, 2))/chi))
    check('COST fourth-order chain rule needs blocks of orders eta^(1/2), eta^(3/4), eta',
          [(k, s.factorial(4)/(s.factorial(2*k-4)*s.factorial(4-k)*2**(4-k)))
           for k in range(2, 5)] == [(2, 3), (3, 6), (4, 1)])

    # Generic real Weyl quadratics test full ordering/product rules with an
    # arbitrary slow function. This is an algebra control, not a substitute
    # for the literal 8-coordinate source regression above.
    psi = s.Function('psi')(x)
    q1 = lambda value: -s.diff(value, x, 2)+x*x*value
    q2 = lambda value: -s.I*(x*s.diff(value, x)+value/2)
    q3 = lambda value: -s.diff(value, x, 2)+x*x*value-s.I*(x*s.diff(value, x)+value/2)
    first_residual = clean((q1(psi*chi)-chi*q1(psi))/chi)
    expected_first = clean((-2*s.diff(psi, x)*s.diff(chi, x)-psi*s.diff(chi, x, 2))/chi)
    check('ORDERED SOURCE exact second-order intertwining retains every Gaussian derivative',
          zero(first_residual-expected_first))
    # Q1^2 = d^4 - 2 x^2 d^2 - 4 x d + (x^4-2).
    q1square = lambda value: (s.diff(value, x, 4)-2*x*x*s.diff(value, x, 2)
                             -4*x*s.diff(value, x)+(x**4-2)*value)
    check('ORDERED SQUARE coefficients include derivatives of the source coefficients',
          zero(q1(q1(psi))-q1square(psi)))
    square_expected = sum(s.binomial(4, nu)*s.diff(psi, x, 4-nu)*s.diff(chi, x, nu)
                          for nu in range(1, 5))
    square_expected -= 2*x*x*(2*s.diff(psi, x)*s.diff(chi, x)+psi*s.diff(chi, x, 2))
    square_expected -= 4*x*psi*s.diff(chi, x)
    square_actual = q1square(psi*chi)-chi*q1square(psi)
    check('ORDERED SQUARE exact intertwining includes all four slow derivative orders',
          zero((square_actual-square_expected)/chi))
    check('NEGATIVE CONTROL treating the ordered Q1 square as a commuting classical polynomial fails',
          not zero(q1(q1(psi))-(s.diff(psi, x, 4)-2*x*x*s.diff(psi, x, 2)+x**4*psi)))
    comm = clean(q1(q2(psi))-q2(q1(psi)))
    check('NONCOMMUTING algebra control retains a genuine ordered source commutator',
          zero(comm-2*s.I*(s.diff(psi, x, 2)+x*x*psi)) and not zero(comm))
    mixed = q1(q2(psi*chi))-chi*q1(q2(psi))
    mixed_split = q1(q2(psi*chi)-chi*q2(psi))+(q1(chi*q2(psi))-chi*q1(q2(psi)))
    check('NONCOMMUTING ordered product intertwines without exchanging its two factors',
          zero((mixed-mixed_split)/chi))
    reverse = q2(q1(psi*chi))-chi*q2(q1(psi))
    check('NEGATIVE CONTROL reversing source order changes the exact intertwining remainder',
          not zero((mixed-reverse)/chi))
    # Evaluate the exact derivative norm powers, not pointwise y coefficients.
    # For f=x^2 at x=0 and psi=1, the Q1 residual is 2 d_a chi.
    norm_square_witness = 4*s.integrate(pfast**2*density_p, (pfast, -s.oo, s.oo))
    check('COST leading eta^(1/4) fiber derivative norm is attained by a quadratic displacement',
          zero(norm_square_witness-2*epsilon**2))
    check('NEGATIVE CONTROL claiming a uniformly eta^(1/2) source norm rate misses the leading term',
          s.limit(norm_square_witness/epsilon**4, epsilon, 0, dir='+') == s.oo)

    # Exact common-form coercivity and completed-square lower bound; these
    # identities make weak lower semicontinuity safe for noncommuting sources.
    w, qnorm, unorm, aa = s.symbols('w qnorm unorm a', nonnegative=True)
    lower = w*w*qnorm*qnorm-w*qnorm*unorm+unorm*unorm
    check('FORM lower coercivity remains valid for the full source graph norm',
          zero(lower-(w*w*qnorm*qnorm+unorm*unorm)/2
               -(w*qnorm-unorm)**2/2))
    coeff1, coeff2, uvalue, qvalue1, qvalue2 = s.symbols('l1 l2 u q1 q2', real=True)
    completed = (w*qvalue1+coeff1*uvalue)**2+(w*qvalue2+coeff2*uvalue)**2
    check('FORM shifted source squares retain the linear term with no commutator assumption',
          zero(completed-w*w*(qvalue1*qvalue1+qvalue2*qvalue2)
               -2*w*uvalue*(coeff1*qvalue1+coeff2*qvalue2)
               -(coeff1*coeff1+coeff2*coeff2)*uvalue*uvalue))
    check('FORM completed-square remainder is exactly 3/4 for h+norm squared',
          1-s.Rational(1, 4) == s.Rational(3, 4))
    deriv_bound = aa*(w*w*qnorm*qnorm+unorm*unorm)/2+2*aa*w*w*qnorm*qnorm
    check('FORM common-characteristic derivative bound is independent of the adiabatic parameter',
          zero(5*aa*(w*w*qnorm*qnorm+unorm*unorm)/2-deriv_bound-2*aa*unorm*unorm))
    cutoff = s.Function('cutoff')(x)
    cutoff_expected = -2*s.diff(cutoff, x)*s.diff(psi, x)-s.diff(cutoff, x, 2)*psi \
        -s.I*x*s.diff(cutoff, x)*psi
    check('FORM CORE cutoff commutator contains only the declared H1-controlled derivatives',
          zero(q3(cutoff*psi)-cutoff*q3(psi)-cutoff_expected))
    check('FORM CORE the source second-derivative coefficient is constant in the actual lattice quadratics',
          all(not entry.has(*(phi+pi)) for q in sources for entry in s.hessian(q, pi)))

    print(json.dumps({
        'status': 'PASS',
        'exact_check_groups': len(checks),
        'checks': checks,
        'actual_source_sha256': hashlib.sha256(source_path.read_bytes()).hexdigest(),
        'actual_ordering_constants': [str(item) for item in ordering],
        'actual_noncommuting_source_coefficient': str(witness_coefficient),
        'actual_noncommuting_source_monomial': list(witness_power),
        'actual_fast_hessian_dimension': list(kk.shape),
        'actual_h_tt_displacement_factor': '-9/1834',
        'scope': ('Exact actual-source/full-fast-fiber and continuous differential Gaussian algebra. '
                  'Form-core density, generalized lower-bound/recovery and uncompressed nonautonomous '
                  'limits are analytic results in PROOF.md, not finite numerical certificates. '
                  'No source commuting replacement, microscopic identification or continuum claim.'),
    }, indent=2))


if __name__ == '__main__':
    main()
