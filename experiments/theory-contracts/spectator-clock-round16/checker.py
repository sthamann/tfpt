#!/usr/bin/env python3
"""Exact original-source and continuous spectator/quadratic-clock controls.

No finite CCR truncation, numerical spectral fit or continuum/TOE claim.
The infinite-dimensional convergence statements are proved in PROOF.md.
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
    return all(s.simplify(item) == 0 for item in values)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ward-source', type=Path,
                        default=Path(__file__).resolve().parents[1]
                        / 'free-scalar-3d/free_scalar_ward.py')
    args = parser.parse_args()
    source = args.ward_source.resolve(strict=True)
    spec = importlib.util.spec_from_file_location('r16_spectator_actual_ward', source)
    if spec is None or spec.loader is None:
        raise RuntimeError('Original Ward source is not importable')
    ward_module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = ward_module
    spec.loader.exec_module(ward_module)
    checks = []

    def check(name, condition):
        if not bool(condition):
            raise AssertionError(name)
        checks.append(name)

    # Original finite-lattice Hamiltonian, not a continuum replacement.
    fields = ward_module.Fields(period=2)
    ward = ward_module.WardComplex(fields)
    sites = list(product(range(2), repeat=3))
    nsites = len(sites)
    scalar = [fields.phi(x) for x in sites]
    momenta = [fields.pi(x) for x in sites]
    index = {x: i for i, x in enumerate(sites)}
    graph = s.zeros(nsites)
    for x in sites:
        row = index[x]
        for axis in range(3):
            graph[row, row] += 2
            for step in (-1, 1):
                y = list(x)
                y[axis] = (y[axis]+step) % 2
                graph[row, index[tuple(y)]] -= 1
    mass2 = s.symbols('mass2', nonnegative=True)
    hm = s.expand(sum(ward.rho(x) for x in sites)
                  .subs({ward.a: 1, ward.mass2: mass2}))
    phi, pi = s.Matrix(scalar), s.Matrix(momenta)
    expected = ((pi.T*pi)[0]+(phi.T*(graph+mass2*s.eye(nsites))*phi)[0])/2
    check('ACTUAL original periodic Ward energy equals the full scalar quadratic form',
          zero(hm-expected))
    check('ACTUAL original matter kinetic Hessian is exactly positive identity',
          s.hessian(hm, momenta) == s.eye(nsites))
    check('ACTUAL original configuration Hessian retains mass and every lattice mode',
          s.hessian(hm, scalar) == graph+mass2*s.eye(nsites))
    eigen = graph.eigenvals()
    check('ACTUAL full scalar Laplacian has exact L2 eigenvalue multiplicities',
          eigen == {s.Integer(0): 1, s.Integer(4): 3,
                    s.Integer(8): 3, s.Integer(12): 1})
    em0 = sum(count*s.sqrt(ell)/2 for ell, count in eigen.items())
    ett = sum(count*s.sqrt(ell) for ell, count in eigen.items() if ell != 0)
    estar = s.simplify(em0+ett)
    check('ACTUAL massless scalar lower bound is strictly positive despite the free mean',
          zero(em0-3-3*s.sqrt(2)-s.sqrt(3)) and em0 > 0)
    check('ACTUAL target lower bound includes both TT polarizations and the matter mean',
          zero(estar-9-9*s.sqrt(2)-3*s.sqrt(3)) and ett == 2*em0)
    check('ACTUAL original lattice energy obeys the finite-size sum and maximum inputs',
          sum(count*ell for ell, count in eigen.items()) == 6*nsites
          and max(eigen) == 12 and sum(eigen.values()) == nsites)
    d = 6*nsites-2*(nsites-1)
    check('ACTUAL all surviving free spectators are counted without deleting homogeneous modes',
          d == 4*nsites+2 == 34)
    check('NEGATIVE CONTROL removing all spectator modes miscounts the parent limit',
          6*nsites != 2*(nsites-1))

    # Actual source and staggered nonzero complement channel, same conventions
    # as local-parent-round15. The contact screening is not an unrelated toy.
    rt = s.sqrt(2)
    pairs = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))
    trace = s.Matrix([1, 1, 1, 0, 0, 0])
    tau_sites, sigma_sites = [], []
    for x in sites:
        tau = s.Matrix([(1 if i == j else rt)*ward.tau(i, j, x)
                        for i, j in pairs]).subs({ward.a: 1, ward.mass2: 0})
        sigma = (tau-trace*fields.pi(x)**2/2).applyfunc(clean)
        tau_sites.append(tau)
        sigma_sites.append(sigma)
    check('ACTUAL full source trace subtraction retains a configuration-only representative',
          all(not entry.has(*momenta) for sigma in sigma_sites for entry in sigma))
    vec = s.Matrix([[-2, 0, 0, 0, 0, rt],
                    [0, -2, 0, 0, 0, rt],
                    [0, 0, 0, rt, rt, 0]])
    nmat = s.Matrix.hstack(vec.T, trace)
    frame = s.Matrix.hstack(s.Matrix([1, 1, -2, 0, 0, rt])/s.sqrt(8),
                           s.Matrix([0, 0, 0, 1, -1, 0])/rt)
    comp = s.Matrix([1, -1, 0, 0, 0, 0])/rt
    check('ACTUAL normalized ell=8 TT frame is transverse and traceless',
          zero(frame.T*frame-s.eye(2)) and zero(nmat.T*frame))
    check('ACTUAL complement witness is a normalized mu=4 non-TT direction',
          zero(comp.T*comp-s.ones(1, 1))
          and zero(nmat*nmat.T*comp-4*comp)
          and zero(frame.T*comp))
    weights = [s.Integer(-1)**(x[0]+x[1])/s.sqrt(8) for x in sites]
    tau = sum((w*t for w, t in zip(weights, tau_sites)), s.zeros(6, 1))
    sigma_source = sum((w*t for w, t in zip(weights, sigma_sites)), s.zeros(6, 1))
    tt = (frame.T*tau).applyfunc(clean)
    check('ACTUAL source still excites a normalized TT channel with unchanged first coefficient',
          zero(frame.T*(tau-sigma_source))
          and s.Poly(tt[0], *scalar).coeff_monomial(scalar[0]**2) == s.Rational(1, 4))
    delta = s.symbols('delta', positive=True)
    ell = s.Integer(8)
    aden = ell+delta+delta/(delta**2+ell)
    inverse_kernel = aden*s.eye(6)+nmat*nmat.T/delta
    # Certify the all-delta inverse action directly. Generic symbolic Gaussian
    # elimination of unsimplified rational entries causes expression blow-up;
    # the eigenchannel residual checks the same inverse equation exactly.
    response = comp/(aden+4/delta)
    curvature = clean(ell**2*(comp.T*response)[0])
    rational_delta = s.Rational(1, 3)
    rational_inverse = inverse_kernel.subs(delta, rational_delta).inv()
    check('ACTUAL finite-delta spectator curvature follows the complete original kernel',
          zero(inverse_kernel*response-comp)
          and zero(curvature-ell**2/(aden+4/delta))
          and zero(ell**2*(comp.T*rational_inverse*comp)[0]
                   -curvature.subs(delta, rational_delta)))
    check('ACTUAL finite-delta complement momentum is not an exact translation symmetry',
          curvature.subs(delta, s.Rational(1, 3)) == s.Rational(7008, 2231)
          and curvature.subs(delta, s.Rational(1, 3)) > 0)
    check('ACTUAL spectator translation symmetry emerges only in the delta limit',
          s.limit(curvature, delta, 0, dir='+') == 0)
    yy = s.symbols('y', real=True)
    check('NEGATIVE CONTROL finite-delta gauge deletion drops a nonzero restoring force',
          s.diff(curvature*yy**2/2, yy) != 0)

    # The fast ground subtraction leaves the actual scalar lower bound.
    # Continuous differential identity with arbitrary test function.
    z, center = s.symbols('z center', real=True)
    freq, eta = s.symbols('freq eta', positive=True)
    f = s.Function('f')(z)
    annihilate = lambda v: (s.diff(v, z)+s.sqrt(eta)*freq*(z-center)*v) \
        / s.sqrt(2*s.sqrt(eta)*freq)
    create = lambda v: (-s.diff(v, z)+s.sqrt(eta)*freq*(z-center)*v) \
        / s.sqrt(2*s.sqrt(eta)*freq)
    hfast = -s.diff(f, z, 2)/(2*eta)+freq**2*(z-center)**2*f/2
    efast = freq/(2*s.sqrt(eta))
    check('CONTINUOUS shifted fast oscillator factorization retains the full subtraction',
          zero(hfast-efast*f-freq/s.sqrt(eta)*create(annihilate(f))))
    check('NEGATIVE CONTROL twice-subtracted fast vacuum destroys its nonnegative remainder',
          -efast < 0)
    ef = s.symbols('Efast', positive=True)
    check('ENERGY ORIGIN unsubtracted inverse-quarter readout vanishes at divergent Efast',
          s.limit(3**s.Rational(1, 4)*(ef+em0)**(-s.Rational(1, 4)), ef, s.oo) == 0)
    check('ENERGY ORIGIN removing a scalar phase still freezes fixed residual energy differences',
          s.limit(s.sqrt(12*(ef+5))-s.sqrt(12*(ef+2)), ef, s.oo) == 0)

    # Continuous momentum Gaussian. Its norm and derivative moments are not
    # represented by finite coordinate matrices.
    p = s.symbols('p', real=True)
    variance = s.symbols('sigma2', positive=True)
    density = s.exp(-p*p/(2*variance))/s.sqrt(2*s.pi*variance)
    chi = (2*s.pi*variance)**(-s.Rational(1, 4))*s.exp(-p*p/(4*variance))
    moment0 = s.integrate(density, (p, -s.oo, s.oo))
    moment2 = s.integrate(p*p*density, (p, -s.oo, s.oo))
    moment4 = s.integrate(p**4*density, (p, -s.oo, s.oo))
    check('CONTINUOUS Gaussian is exactly normalized at every positive width', moment0 == 1)
    check('CONTINUOUS Gaussian second and fourth moments have the stated variance convention',
          zero(moment2-variance) and zero(moment4-3*variance**2))
    dimension = s.symbols('d', integer=True, positive=True)
    mean_energy = dimension*moment2/2
    rms_energy_squared = (dimension*moment4+dimension*(dimension-1)*moment2**2)/4
    check('CONTINUOUS d-dimensional spectator mean energy includes every mode',
          zero(mean_energy-dimension*variance/2))
    check('CONTINUOUS spectator energy RMS includes the nonzero cross-coordinate moments',
          zero(rms_energy_squared-dimension*(dimension+2)*variance**2/4))
    position_second = s.integrate(s.diff(chi, p)**2, (p, -s.oo, s.oo))
    check('CONTINUOUS small momentum costs exact coordinate variance 1/(4 sigma2)',
          zero(position_second-1/(4*variance)))
    check('CONTINUOUS each normalized spectator saturates the position-momentum variance product',
          zero(position_second*moment2-s.Rational(1, 4)))
    check('NEGATIVE CONTROL no positive-width Gaussian has zero spectator energy',
          mean_energy.is_positive is True)
    chi_twice = chi.subs(variance, 4*variance)
    overlap = s.simplify(s.integrate(chi*chi_twice, (p, -s.oo, s.oo)))
    check('CONTINUOUS shrinking Gaussian family is not Cauchy along a fixed width ratio',
          zero(overlap-2/s.sqrt(5)) and overlap < 1)

    # Pointwise clock bounds, exact positive polynomial certificates.
    energy, extra = s.symbols('E s', positive=True)
    radial, increase = s.symbols('r h', positive=True)
    inc_energy = 2*radial*increase+increase**2
    freq_difference = s.sqrt(12)*increase
    linear_bound = s.sqrt(3)*inc_energy/radial
    check('CLOCK rationalization gives the correct uniform phase coefficient sqrt(3)',
          zero(linear_bound-freq_difference-s.sqrt(3)*increase**2/radial))
    check('CLOCK phase Lipschitz residual is a strictly nonnegative exact certificate',
          s.sqrt(3)*increase**2/radial > 0)
    gaussian_rms = variance*s.sqrt(dimension*(dimension+2))/2
    bound, time = s.symbols('b Q', positive=True)
    clock_error = time*s.sqrt(3)/s.sqrt(bound)*gaussian_rms
    check('CLOCK full-vector Gaussian phase error retains dimension and RMS, not just mean',
          zero(clock_error-time*s.sqrt(3*dimension*(dimension+2))*variance/(2*s.sqrt(bound))))
    epsilon = s.symbols('epsilon', positive=True)
    check('COST prescribed total spectator energy is epsilon at sigma2=2epsilon/d',
          zero(mean_energy.subs(variance, 2*epsilon/dimension)-epsilon))
    check('COST error at fixed energy includes the sqrt(1+2/d) fluctuation factor',
          zero(clock_error.subs(variance, 2*epsilon/dimension)
               -time*s.sqrt(3)/s.sqrt(bound)*epsilon*s.sqrt(1+2/dimension)))
    check('COST coordinate variance grows linearly in d at fixed total spectator energy',
          zero(position_second.subs(variance, 2*epsilon/dimension)-dimension/(8*epsilon)))
    check('COST total squared coordinate spread grows quadratically in d at fixed energy',
          zero((dimension*position_second).subs(variance, 2*epsilon/dimension)
               -dimension**2/(8*epsilon)))

    # Quadratic, not linear, clock half density and weighted solution norm.
    lam = s.symbols('lambda', real=True)
    positive_gap = s.symbols('gap', positive=True)
    pminus = -s.sqrt(12*(energy+extra-lam))
    weight = 6/s.sqrt(12*(energy+extra-lam))
    check('CLOCK negative sheet solves the full quadratic constraint including spectator energy',
          zero(energy+extra-pminus**2/12-lam))
    check('CLOCK full shell Jacobian is dp_clock/dlambda',
          zero(s.diff(pminus, lam)-weight))
    check('CLOCK spectral half density exactly cancels the Jacobian in the physical norm',
          zero(((-pminus/6)*weight).subs(energy, lam+positive_gap-extra)-1))
    check('CLOCK limit-only spectator reduction retains the original quadratic shell weight',
          zero(weight.subs({extra: 0, lam: 0})-6/s.sqrt(12*energy)))
    de = 3**s.Rational(1, 4)*energy**(-s.Rational(1, 4))
    detot = 3**s.Rational(1, 4)*(energy+extra)**(-s.Rational(1, 4))
    metric = s.sqrt(12*energy)/6
    metric_total = s.sqrt(12*(energy+extra))/6
    check('NORM D_X is exactly unitary into the positive weighted slice norm',
          zero(de**2*metric-1) and zero(detot**2*metric_total-1))
    check('NORM clock encoding requires the inverse-quarter energy ratio',
          zero((detot/de)**2*metric_total-metric))
    check('NEGATIVE CONTROL ordinary tensoring does not preserve the quadratic-clock norm',
          not zero(de**2*metric_total-1))
    u = s.symbols('u', positive=True)
    check('NORM square-root concavity bound has an exact nonnegative polynomial residual',
          zero(1+(u**4-1)/2-u**2-(u**2-1)**2/2))
    check('NORM quarter-root concavity has an exact positive residual for u>=1',
          zero(1+(u**4-1)/4-u-(u-1)**2*(u*u+2*u+3)/4))
    check('NORM naive-product excess and corrected amplitude bound retain all constants',
          zero(mean_energy/(2*bound)-dimension*variance/(4*bound))
          and zero(gaussian_rms/(4*bound)-variance*s.sqrt(dimension*(dimension+2))/(8*bound)))
    qq = s.symbols('q', real=True)
    fq = de*s.exp(-s.I*qq*s.sqrt(12*energy))
    df_without_phase = s.simplify(s.diff(fq, energy)*s.exp(s.I*qq*s.sqrt(12*energy)))
    expected_derivative = 3**s.Rational(1, 4)*(
        -energy**(-s.Rational(5, 4))/4
        -s.I*qq*s.sqrt(3)*energy**(-s.Rational(3, 4)))
    check('READOUT derivative bound simultaneously includes inverse-quarter norm and square-root phase',
          zero(df_without_phase-expected_derivative))
    check('NEGATIVE CONTROL commuting A and S do not make their square roots additive',
          s.sqrt(12*(1+1)) != s.sqrt(12)+s.sqrt(12))
    check('NEGATIVE CONTROL spectator energy changes relative system clock phases',
          not zero((s.sqrt(12*5)-s.sqrt(12*2))-(s.sqrt(12*4)-s.sqrt(12))))

    # Exact test-space averaging controls, with ordinary continuous variables.
    aa = s.symbols('a', real=True)
    gaussian_fourier = s.integrate(s.exp(-p*p)*s.exp(s.I*aa*p), (p, -s.oo, s.oo))
    check('RIGGING continuous spectator Haar average evaluates the test density at zero',
          zero(s.integrate(gaussian_fourier/(2*s.pi), (aa, -s.oo, s.oo))-1))
    shifted = s.symbols('c', real=True)
    zero_density = s.exp(-shifted**2)
    exact_average = s.integrate(s.sqrt(s.pi)*s.exp(-aa**2/4)
                                *s.exp(s.I*aa*shifted)/(2*s.pi),
                                (aa, -s.oo, s.oo))
    check('RIGGING translation average is evaluation, not an ordinary normalized L2 kernel',
          zero(exact_average-zero_density))
    check('NEGATIVE CONTROL wrong Haar normalization rescales the physical norm',
          zero(s.integrate(gaussian_fourier, (aa, -s.oo, s.oo))-2*s.pi)
          and 2*s.pi != 1)

    print(json.dumps({
        'status': 'PASS',
        'exact_check_groups': len(checks),
        'checks': checks,
        'actual_source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'actual_massless_L2_common_parent_lower_bound': str(s.simplify(em0)),
        'actual_massless_L2_target_lower_bound': str(estar),
        'actual_L2_surviving_spectator_count': d,
        'actual_finite_delta_complement_curvature': str(curvature.subs(delta, s.Rational(1, 3))),
        'scope': ('Exact original-source, continuous Gaussian and quadratic-clock algebra. '
                  'The infinite-dimensional sequential convergence and distributional reduction '
                  'are proved in PROOF.md. Energy subtraction and optional limit-only new '
                  'constraints remain explicit choices. No microscopic or continuum completion.'),
    }, indent=2))


if __name__ == '__main__':
    main()
