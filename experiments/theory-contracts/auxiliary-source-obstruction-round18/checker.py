#!/usr/bin/env python3
"""Actual-source noise obstruction and exact coherent-state polynomial checks."""
import argparse
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

import sympy as s


def zero(value):
    values = list(value) if isinstance(value, s.MatrixBase) else [value]
    return all(s.simplify(s.expand(item)) == 0 for item in values)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ward-source', type=Path,
                        default=Path(__file__).resolve().parents[1]
                        / 'free-scalar-3d/free_scalar_ward.py')
    args = parser.parse_args()
    path = args.ward_source.resolve(strict=True)
    spec = importlib.util.spec_from_file_location('r18_noise_actual_ward', path)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load actual Ward source')
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
    z = phi + pi
    weights = [s.Integer(-1)**(x[0]+x[1])/s.sqrt(8) for x in sites]
    sub = {ward.a: 1, ward.mass2: 2}
    rt = s.sqrt(2)
    pairs = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))
    tau = s.Matrix([sum(w*(1 if i == j else rt)*ward.tau(i, j, x)
                        for w, x in zip(weights, sites)).subs(sub) for i, j in pairs])
    scalar = s.Matrix([4, 4, 8, 0, 0, 4*rt])
    rho = sum(w*ward.rho(x) for w, x in zip(weights, sites)).subs(sub)
    current = s.Matrix([sum(w*ward.current(i, x) for w, x in zip(weights, sites)).subs(sub)
                        for i in range(3)])
    bv = s.Matrix([[5, -3, 0], [-3, 5, 0], [0, 0, 8]])/32
    sources = [s.expand((scalar.T*tau)[0]/(scalar.T*scalar)[0]+rho/16)]
    sources += list((bv*current).applyfunc(s.expand))
    check('ACTUAL import retains the registered dataclass source module',
          sys.modules[spec.name] is module and fields.period == 2)
    check('ACTUAL normalized Fourier weights retain all eight sites',
          len(sites) == 8 and sum(w*w for w in weights) == 1 and sum(weights) == 0)
    check('ACTUAL scalar kinetic source coefficient is unchanged',
          s.diff(sources[0], pi[0], 2) == 3*rt/64)
    check('ACTUAL one exactly zero source is retained',
          sources[3] == 0 and all(sources[a] != 0 for a in range(3)))
    omega = s.zeros(16)
    omega[:8, 8:] = s.eye(8)
    omega[8:, :8] = -s.eye(8)
    hs = [s.hessian(q, z) for q in sources]
    check('ACTUAL source symbols are exactly their symmetric quadratic Hessians',
          all(zero(q-(s.Matrix(z).T*h*s.Matrix(z))[0]/2) for q, h in zip(sources, hs)))
    bracket = s.expand(sum(s.diff(sources[0], x)*s.diff(sources[1], p)
                          -s.diff(sources[0], p)*s.diff(sources[1], x)
                          for x, p in zip(phi, pi)))
    check('ACTUAL noncommuting-source coefficient is retained',
          s.Poly(bracket, *z).coeff_monomial(phi[0]**2) == -s.Rational(1, 1024))
    vacuum = s.simplify(s.trace(s.hessian(bracket, z))/4)
    check('ACTUAL centered normalized Gaussian already detects noncommutation',
          vacuum == -s.Rational(5, 512))
    t = s.symbols('t', real=True)
    mean = dict.fromkeys(z, 0)
    mean[phi[0]] = t
    witness = s.simplify(bracket.subs(mean)+vacuum)
    check('ACTUAL displaced Gaussian detects the exact unbounded witness',
          witness == -(t*t+10)/1024)
    check('ACTUAL no finite constant can equal the source-readout lower defect',
          s.diff(-witness, t, 2) == s.Rational(1, 512))
    ordering = [s.simplify(s.trace((omega*h)**2)/8) for h in hs]
    check('ACTUAL all original source-square ordering constants survive',
          ordering == [s.Rational(3, 512), -s.Rational(15, 2048),
                       -s.Rational(15, 2048), 0])

    def lap(poly):
        return s.expand(sum(s.diff(poly, x, 2) for x in z))

    def heat4(poly):
        return s.expand(poly+lap(poly)/4+lap(lap(poly))/32)

    noise_coefficients = []
    for a, (q, h, order) in enumerate(zip(sources, hs, ordering)):
        f = q-s.trace(h)/4
        check(f'ACTUAL source {a} coherent readout has exactly the target first moment',
              zero(heat4(f)-q))
        noise = s.expand((s.Matrix(z).T*h*h*s.Matrix(z))[0]/2
                         +(s.trace(h*h)-s.trace((omega*h)**2))/8)
        check(f'ACTUAL source {a} squared readout has the full exact excess',
              zero(heat4(f*f)-(q*q+order)-noise))
        constant = s.simplify((s.trace(h*h)-s.trace((omega*h)**2))/8)
        check(f'ACTUAL source {a} excess constant is nonnegative', constant >= 0)
        check(f'ACTUAL source {a} noise Hessian is the positive square H squared',
              zero(s.hessian(noise, z)-h*h))
        expect = s.simplify(noise.subs(mean)+s.trace(h*h)/4)
        noise_coefficients.append(expect)
    check('ACTUAL nonzero sources have nonconstant coherent-readout noise',
          all(h*h != s.zeros(16) for h in hs[:3]))
    check('ACTUAL zero source has zero coherent-readout noise', noise_coefficients[3] == 0)
    sum_gap = s.Poly(s.expand(noise_coefficients[0]+noise_coefficients[1]+witness), t)
    check('ACTUAL explicit positive dilation satisfies the two-source noise bound',
          all(c >= 0 and sum(power) % 2 == 0 for power, c in sum_gap.terms()))

    # Finite commuting-readout model: exact compression, not a CCR simulation.
    j = s.Matrix([[1, 0], [0, 1], [1, 0], [0, 1]])/s.sqrt(2)
    # Rotate the two-dimensional target range to produce noncommuting compressions.
    u = s.Matrix([[1, 0, 0, 0], [0, 1/s.sqrt(2), 1/s.sqrt(2), 0],
                  [0, -1/s.sqrt(2), 1/s.sqrt(2), 0], [0, 0, 0, 1]])
    j = u*j
    ra, rb = s.diag(0, 1, 2, 3), s.diag(3, 1, 4, 0)
    qa, qb = j.T*ra*j, j.T*rb*j
    p = j*j.T
    la, lb = (s.eye(4)-p)*ra*j, (s.eye(4)-p)*rb*j
    check('MODEL commuting registers compress to genuinely noncommuting targets',
          zero(ra*rb-rb*ra) and not zero(qa*qb-qb*qa))
    check('MODEL compression isometry is exact', zero(j.T*j-s.eye(2)))
    check('MODEL squared-source defect is precisely positive range leakage',
          zero(j.T*ra*ra*j-qa*qa-la.T*la))
    check('MODEL target commutator is precisely the antisymmetric leakage term',
          zero(qa*qb-qb*qa+la.T*lb-lb.T*la))
    psi = s.Matrix([1, s.I])/s.sqrt(2)
    na = (psi.conjugate().T*la.T*la*psi)[0]
    nb = (psi.conjugate().T*lb.T*lb*psi)[0]
    comm = (psi.conjugate().T*(qa*qb-qb*qa)*psi)[0]
    check('MODEL complex target state has a nonzero commutator witness', comm != 0)
    check('MODEL leakage uncertainty bound retains its factor two',
          s.simplify(4*na*nb-s.Abs(comm)**2) >= 0)
    check('MODEL noiseless energy mutation contradicts actual squared compression',
          not zero(j.T*(ra*ra+rb*rb)*j-(qa*qa+qb*qb)))

    k = s.Matrix([[2, 1], [1, 3]])
    ll = s.Matrix([[1, 2], [-1, 1]])
    c = ll.T*k.inv()*ll+s.eye(2)
    aa = s.Matrix(s.symbols('a0:2', real=True))
    jj = s.Matrix(s.symbols('j0:2', real=True))
    original = (aa.T*k*aa)[0]/2+(aa.T*ll*jj)[0]+(jj.T*c*jj)[0]/2
    shifted = aa+k.inv()*ll*jj
    check('STATIC full positive auxiliary square has the exact Schur complement',
          zero(original-(shifted.T*k*shifted)[0]/2-(jj.T*jj)[0]/2))
    check('STATIC no bare contact gives a negative induced source form',
          (ll.T*k.inv()*ll).det() > 0 and (ll.T*k.inv()*ll)[0, 0] > 0)
    check('STATIC required bare source contact is nonzero', c != s.zeros(2))
    check('COPY undressed commuting registers cannot remove the actual source curvature',
          bracket != 0)

    print(json.dumps(dict(status='PASS', exact_check_groups=len(checks), checks=checks,
                         actual_source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                         actual_coherent_commutator_over_i=str(witness),
                         actual_coherent_noise=[str(x) for x in noise_coefficients],
                         scope='Actual Ward quadratics, exact coherent-state polynomial identities, '
                               'and separately labelled finite dilation/static controls. '
                               'No general local-parent no-go, dynamical dilation, continuum or TOE claim.'),
                     indent=2))


if __name__ == '__main__':
    main()
