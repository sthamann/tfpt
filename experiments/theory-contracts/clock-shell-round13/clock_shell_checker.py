#!/usr/bin/env python3
"""Exact actual-energy and clock-shell controls, not a finite CCR model."""
from itertools import product
import json
from pathlib import Path
import runpy

import sympy as s


def main():
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    def zero(value):
        if isinstance(value, s.MatrixBase):
            return all(s.simplify(x) == 0 for x in value)
        return s.simplify(value) == 0

    # Original Ward energy, not a reconstructed continuum density.
    source = Path(__file__).resolve().parent.parent/'free-scalar-3d/free_scalar_ward.py'
    module = runpy.run_path(str(source))
    fields = module['Fields'](period=3)
    ward = module['WardComplex'](fields)
    sites = list(product(range(3), repeat=3))
    scalar = [fields.phi(x) for x in sites]
    momenta = [fields.pi(x) for x in sites]
    Hm = s.expand(sum(ward.rho(x) for x in sites).subs({ward.a:1, ward.mass2:1}))
    graph = s.zeros(27)
    index = {x:i for i,x in enumerate(sites)}
    for i,x in enumerate(sites):
        for axis in range(3):
            graph[i,i] += 2
            for step in (-1,1):
                y = list(x)
                y[axis] = (y[axis]+step) % 3
                graph[i,index[tuple(y)]] -= 1
    phi, pi = s.Matrix(scalar), s.Matrix(momenta)
    expected = ((pi.T*pi)[0]+(phi.T*(graph+s.eye(27))*phi)[0])/2
    check('actual original periodic matter energy equals oscillator quadratic form', zero(Hm-expected))
    check('actual scalar graph exact eigenvalue multiplicities', graph.eigenvals()=={0:1,3:6,6:12,9:8})
    check('actual matter kinetic Hessian is identity', s.hessian(Hm,momenta)==s.eye(27))
    check('actual matter configuration Hessian is graph plus mass', s.hessian(Hm,scalar)==graph+s.eye(27))
    em = sum(count*s.sqrt(1+ell)/2 for ell,count in graph.eigenvals().items())
    ett = sum(count*s.sqrt(ell) for ell,count in graph.eigenvals().items() if ell)
    check('actual massive scalar zero-point lower bound', zero(em-(s.Rational(13,2)+6*s.sqrt(7)+4*s.sqrt(10))))
    check('two real TT polarizations have correct frequency count', 2*sum(count for ell,count in graph.eigenvals().items() if ell)==52)
    check('actual TT zero-point lower bound', zero(ett-(24+6*s.sqrt(3)+12*s.sqrt(6))))
    em0 = sum(count*s.sqrt(ell)/2 for ell,count in graph.eigenvals().items())
    check('massless uniform mode contributes zero but total lower bound positive', zero(em0+ett-(36+9*s.sqrt(3)+18*s.sqrt(6))) and em0+ett>0)

    # Continuous-coordinate oscillator factorization, arbitrary test function.
    x, shift = s.symbols('x shift', real=True)
    freq = s.symbols('freq', positive=True)
    f = s.Function('f')(x)
    annihilate = lambda v:(s.diff(v,x)+freq*(x+shift)*v)/s.sqrt(2*freq)
    create = lambda v:(-s.diff(v,x)+freq*(x+shift)*v)/s.sqrt(2*freq)
    oscillator = (-s.diff(f,x,2)+freq**2*(x+shift)**2*f)/2
    check('shifted oscillator factorization gives same zero-point term', zero(oscillator-freq*create(annihilate(f))-freq*f/2))
    check('omitting zero-point factor is detected', not zero(oscillator-freq*create(annihilate(f))))

    # Exact classical relational-flow identity in an explicitly solvable model.
    # This is an algebra control, not the actual interacting scalar/TT flow.
    q, p, z, r, z2, r2, g = s.symbols('q p z r z2 r2 g', real=True, nonzero=True)
    coords, moms = (q,z,z2),(p,r,r2)
    def pb(left,right):
        return s.simplify(sum(s.diff(left,a)*s.diff(right,b)-s.diff(left,b)*s.diff(right,a) for a,b in zip(coords,moms)))
    T = -6*q/p
    H = (r**2+g**2*z**2+r2**2+4*g**2*z2**2)/2
    C = H-p**2/12
    K = r*s.cos(g*T)+g*z*s.sin(g*T)
    K2 = r2*s.cos(2*g*T)+2*g*z2*s.sin(2*g*T)
    check('classical reference parameter is exactly conjugate to unchanged clock constraint', pb(T,C)==1)
    check('first relational charge commutes with unchanged quadratic clock', zero(pb(K,C)))
    check('second relational charge commutes with unchanged quadratic clock', zero(pb(K2,C)))
    check('clock-dependent charges still mutually commute', zero(pb(K,K2)))
    check('free limit retains the prescribed seed charge', zero(s.limit(K,g,0)-r))
    check('clock origin retains original charge at every coupling', zero(K.subs(q,0)-r))
    check('clock-origin translation is not falsely preserved', not zero(pb(p,K)))
    wrongT = 6*q/p
    wrongK = r*s.cos(g*wrongT)+g*z*s.sin(g*wrongT)
    check('wrong clock-flow sign is rejected', not zero(pb(wrongK,C)))

    # Quantum spectral-shell chart. p is an ordinary continuous coordinate;
    # finite energy labels below test channels, never a truncated clock CCR.
    E, lam = s.symbols('E lam', real=True)
    d = s.symbols('d', positive=True)
    pminus = -s.sqrt(12*(E-lam))
    weight = 6/s.sqrt(12*(E-lam))
    check('negative-sheet inverse solves actual quadratic constraint', zero(E-pminus**2/12-lam))
    check('Jacobian is dp/dlambda not its reciprocal', zero(s.diff(pminus,lam)-weight))
    check('inverse Jacobian product is one', zero(((-pminus/6)*weight).subs(E,lam+d)-1))
    check('shell weight matches previous quadratic RAQ', zero(weight.subs(lam,0)-6/s.sqrt(12*E)))
    check('linear-clock unit weight is not substituted', not zero(weight.subs(lam,0)-1))

    # Two arbitrary continuous-clock functions and a self-adjoint energy swap.
    # It changes energy, so leaving p fixed must fail to preserve C.
    energies = [s.Integer(2),s.Integer(5)]
    pp = s.symbols('pp', negative=True)
    values = [s.Function('u')(pp),s.Function('v')(pp)]
    def transport_to_channel(output_index, input_index, expr):
        targetp = -s.sqrt(pp**2+12*(energies[input_index]-energies[output_index]))
        # Restricted spectral tube ensures the square root is positive.
        factor = s.sqrt((-pp)/s.sqrt(pp**2+12*(energies[input_index]-energies[output_index])))
        return factor*expr.subs(pp,targetp,simultaneous=True)

    for out,inp in ((0,1),(1,0)):
        transported = transport_to_channel(out,inp,values[inp])
        lhs = (energies[out]-pp**2/12)*transported
        rhs = transport_to_channel(out,inp,(energies[inp]-pp**2/12)*values[inp])
        check(f'energy-changing channel {inp} to {out} preserves exact constraint eigenvalue', zero(lhs-rhs))
        check(f'uncompensated momentum in channel {inp} to {out} is rejected', not zero((energies[out]-energies[inp])*values[inp]))

    # In lambda coordinates the half densities and swap form an exact
    # Hermitian involution; evaluate with E_i-lambda>0 symbolic positive gaps.
    d0,d1 = s.symbols('d0 d1',positive=True)
    w0,w1 = s.sqrt(3)/s.sqrt(d0),s.sqrt(3)/s.sqrt(d1)
    half = s.diag(s.sqrt(w0),s.sqrt(w1))
    J = s.Matrix([[0,1],[1,0]])
    raw = half.inv()*J*half
    metric = s.diag(w0,w1)
    check('channel half-density transform is invertible', zero(half*half.inv()-s.eye(2)))
    check('transported channel involution squares to identity', zero(raw*raw-s.eye(2)))
    check('channel transformation has correct weighted self-adjointness', zero(raw.T*metric-metric*raw))
    check('wrong reciprocal half-density violates the measure identity', not zero((half*J*half.inv()).T*metric-metric*(half*J*half.inv())))
    check('transported constraints commute with scalar shell multiplier', zero(raw*(lam*s.eye(2))-(lam*s.eye(2))*raw))
    kernel = (s.eye(2)+J)/2
    Achannel = s.diag(2,5)
    check('zero-charge projector exists after shifting the generator', zero((J-s.eye(2))*kernel) and zero(kernel*kernel-kernel))
    check('physical initial-data subspace need not be A-invariant', not zero(Achannel*kernel-kernel*Achannel))
    rigging = half*kernel*half
    check('joint averaging keeps both half-density factors in the right order', zero(rigging-(kernel*half).T*(kernel*half)))
    check('commuting energy weight past physical projection is rejected', not zero(metric*kernel-(metric*kernel).T))

    print(json.dumps({'status':'PASS','exact_check_groups':len(checks),'checks':checks,
                      'actual_massive_L3_free_energy_bound':str(s.simplify(em+ett)),
                      'actual_massless_L3_free_energy_bound':str(s.simplify(em0+ett)),
                      'scope':'Actual oscillator-energy inputs plus exact continuous-clock and channel controls. Full spectral domains and joint averaging are proved in README.md. No microscopic clock, original spatial constraints, locality or efficient interacting spectrum is derived.'},indent=2))


if __name__ == '__main__':
    main()
