#!/usr/bin/env python3
"""Exact source/bandwidth controls and separate cubic-boundary MODEL.

No finite CCR assertion, floating tolerance, or interacting limit claim.
The infinite-basis ladder action has finite support for every checked vector.
"""
from __future__ import annotations

import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

import sympy as sp


def main():
    checks = []

    def check(label, condition):
        if not bool(condition):
            raise RuntimeError(label)
        checks.append(label)

    def clean(x):
        return sp.simplify(sp.expand(x))

    ward_path = Path(__file__).resolve().parent.parent / "free-scalar-3d/free_scalar_ward.py"
    spec = importlib.util.spec_from_file_location("r14_actual_ward", ward_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    fields = module.Fields(period=2)
    ward = module.WardComplex(fields)
    sites = list(product(range(2), repeat=3))
    phi = [fields.phi(x) for x in sites]
    pi = [fields.pi(x) for x in sites]
    tau = sp.zeros(6, 1)
    pairs = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
    for x in sites:
        weight = sp.Integer(-1)**(x[0]+x[1])/sp.sqrt(8)
        for j, (left, right) in enumerate(pairs):
            tau[j] += weight * (1 if left == right else sp.sqrt(2)) * ward.tau(left, right, x)
    tau = tau.subs({ward.a: 1, ward.mass2: 2}).applyfunc(clean)
    polar = sp.Matrix.hstack(sp.Matrix([1,1,-2,0,0,sp.sqrt(2)])/sp.sqrt(8),
                            sp.Matrix([0,0,0,1,-1,0])/sp.sqrt(2))
    stress = (polar.T*tau).applyfunc(clean)
    Q0, Q1 = sp.symbols("Q0 Q1", real=True)
    coordinates = [Q0, Q1] + phi
    cubic = sp.Poly(sp.expand(Q0*stress[0]+Q1*stress[1]), *coordinates)
    check("ACTUAL retained-mode cubic has degree three", cubic.total_degree() == 3)
    check("ACTUAL TT stress contains no matter momenta", all(not v.has(*pi) for v in stress))
    check("ACTUAL TT delta-site source coefficient is one quarter",
          sp.Poly(stress[0], *phi).coeff_monomial(phi[0]**2) == sp.Rational(1,4))

    # Independent common-domain witness, using a single-site delta instead
    # of the other proof's eight nonzero displacement entries.
    weights = [sp.Integer(-1)**(x[0]+x[1])/sp.sqrt(8) for x in sites]
    substitutions = {ward.a: 1, ward.mass2: 2}
    rho = clean(sum(w*ward.rho(x) for w,x in zip(weights,sites)).subs(substitutions))
    matter = clean(sum(ward.rho(x) for x in sites).subs(substitutions))
    current = sp.Matrix([clean(sum(w*ward.current(j,x) for w,x in zip(weights,sites)).subs(substitutions)) for j in range(3)])
    scalar_row = sp.Matrix([4,4,8,0,0,4*sp.sqrt(2)])
    B = clean((scalar_row.T*tau)[0]/128+rho/16)
    coupling = sp.symbols("coupling", real=True, nonzero=True)
    time, amplitude = sp.symbols("time amplitude", real=True)
    P0, P1 = sp.symbols("P0 P1", real=True)
    cv = sp.Matrix([sp.Rational(1,2),0,0])
    bv = sp.Matrix([[5,-3,0],[-3,5,0],[0,0,8]])/32
    fiber = (P0**2+P1**2)/2+4*(Q0**2+Q1**2)+matter+coupling*cubic.as_expr()
    fiber += coupling*time*B+coupling*(cv.T*bv*current)[0]-time**2/32+sp.Rational(5,256)
    coefficient = 1+3*coupling*time*weights[0]/16
    displacement = {phi[0]:phi[0]+amplitude**2, pi[0]:pi[0]+amplitude**3,
                    Q0:Q0-2*coefficient*amplitude**2/coupling}
    moved_h = sp.Poly(sp.expand(fiber.subs(displacement, simultaneous=True)), amplitude)
    moved_B = sp.Poly(sp.expand(B.subs(displacement, simultaneous=True)), amplitude)
    check("ACTUAL independent delta packet cancels the entire degree-six Hamiltonian coefficient",
          moved_h.degree() <= 5)
    check("ACTUAL independent delta packet retains a nonzero B degree-six coefficient",
          clean(moved_B.coeff_monomial(amplitude**6)) == 3*sp.sqrt(2)/128)
    check("ACTUAL independent delta packet B remainder has degree at most four",
          sp.Poly(moved_B.as_expr()-3*sp.sqrt(2)*amplitude**6/128, amplitude).degree() <= 4)

    dimension = len(coordinates)
    vacuum = (0,)*dimension

    def coordinate_action(state, index):
        answer = {}
        for occupation, value in state.items():
            for change in (-1, 1):
                number = occupation[index]
                if change < 0 and number == 0:
                    continue
                shifted = list(occupation)
                shifted[index] += change
                key = tuple(shifted)
                factor = sp.sqrt(sp.Rational(number if change < 0 else number+1, 2))
                answer[key] = answer.get(key, 0) + value*factor
        return {key: clean(value) for key, value in answer.items() if clean(value) != 0}

    def apply_cubic(state):
        answer = {}
        for powers, coefficient in cubic.terms():
            term = state
            for index, number in enumerate(powers):
                for _ in range(number):
                    term = coordinate_action(term, index)
            for occupation, value in term.items():
                answer[occupation] = answer.get(occupation, 0) + coefficient*value
        return {key: clean(value) for key, value in answer.items() if clean(value) != 0}

    def projection(state, cutoff):
        return {key: value for key, value in state.items() if sum(key) <= cutoff}

    def difference(a, b):
        return {key: clean(a.get(key, 0)-b.get(key, 0)) for key in set(a)|set(b)
                if clean(a.get(key, 0)-b.get(key, 0)) != 0}

    ground_output = apply_cubic({vacuum: sp.Integer(1)})
    target = list(vacuum)
    target[0], target[2] = 1, 2
    check("ACTUAL vacuum to degree-three amplitude is exactly one eighth",
          ground_output[tuple(target)] == sp.Rational(1,8))
    check("ACTUAL two-shell residual mutant loses a nonzero amplitude",
          projection(ground_output, 2).get(tuple(target), 0) != ground_output[tuple(target)])
    norm2 = clean(sum(sp.conjugate(a)*a for a in ground_output.values()))
    check("ACTUAL cubic vacuum residual norm is strictly nonzero", norm2 > 0)

    for cutoff in range(4):
        state = {vacuum: sp.Integer(1)}
        if cutoff:
            mode = list(vacuum)
            mode[2] = cutoff
            state[tuple(mode)] = sp.Rational(1,3)
        out = apply_cubic(state)
        residual = difference(out, projection(out, cutoff))
        shell = difference(projection(state, cutoff), projection(state, cutoff-3))
        shell_out = apply_cubic(shell)
        shell_residual = difference(projection(shell_out, cutoff+3), projection(shell_out, cutoff))
        check(f"ACTUAL exact external three-shell identity at cutoff {cutoff}",
              difference(residual, shell_residual) == {})
        check(f"ACTUAL no output above cutoff plus three at {cutoff}",
              projection(out, cutoff+3) == out)

    # Finite 2-channel algebra checks the sign and the external-residual role
    # of Duhamel. It is not a truncation of the TFPT canonical algebra.
    t, z = sp.symbols("t z", real=True)
    matrix = sp.Matrix([[0, 1], [1, 0]])
    retained = sp.diag(1, 0)
    seed = sp.Matrix([1, 0])
    unitary = lambda time: sp.eye(2)*sp.cos(time)-sp.I*matrix*sp.sin(time)
    residual = (sp.eye(2)-retained)*matrix*seed
    integral = sp.I*sp.integrate(unitary(t-z)*residual, (z, 0, t))
    check("MODEL Duhamel residual sign agrees exactly", all(clean(x) == 0 for x in seed-unitary(t)*seed-integral))
    check("MODEL projected residual can vanish while external residual does not",
          retained*residual == sp.zeros(2, 1) and residual != sp.zeros(2, 1))
    check("MODEL wrong Duhamel sign is rejected", any(clean(x) != 0 for x in seed-unitary(t)*seed+integral))

    # Independently soluble cubic transport; not the actual Hamiltonian.
    y, s, beta, theta = sp.symbols("y s beta theta", real=True)
    v = sp.Function("v")(y)
    inverse = sp.cos(y)*v
    transformed = sp.simplify((-sp.I*(sp.diff(inverse,y)+sp.tan(y)*inverse))/sp.cos(y))
    check("MODEL cubic half-density conjugates exactly to interval momentum",
          sp.simplify(transformed+sp.I*sp.diff(v,y)) == 0)
    check("MODEL Jacobian equals half-density squared",
          sp.simplify(sp.diff(sp.tan(y),y)-1/sp.cos(y)**2) == 0)
    packet = sp.Function("F")(s,y)
    operator = lambda a: -sp.I*(sp.diff(a,s)+sp.diff(a,y))
    modulation = sp.exp(sp.I*beta*s)
    check("MODEL exact formal characteristic Weyl relation",
          sp.simplify(operator(modulation*packet)-modulation*(operator(packet)+beta*packet)) == 0)
    endpoint = sp.symbols("endpoint", complex=True)
    left, right = endpoint, sp.exp(sp.I*theta)*endpoint
    check("MODEL reflection-conjugation preserves each boundary phase",
          sp.simplify(sp.conjugate(left)-sp.exp(sp.I*theta)*sp.conjugate(right)) == 0)
    n = sp.symbols("n", integer=True)
    eigenvalue = 2*n+theta/sp.pi
    check("MODEL eigenvalues obey full interval boundary condition",
          sp.simplify(sp.exp(sp.I*eigenvalue*sp.pi)-sp.exp(sp.I*theta)) == 0)
    periodic = sp.Matrix([1,1])/sp.sqrt(2)
    antiperiodic = sp.Matrix([-1,1])/sp.sqrt(2)
    check("MODEL one-wrapped-component phases give orthogonal states",
          (periodic.H*antiperiodic)[0] == 0 and (periodic.H*periodic)[0] == 1)
    check("MODEL a common overall phase would not explain orthogonality",
          periodic*periodic.H != antiperiodic*antiperiodic.H)
    for cutoff in range(4):
        ranks = sum(sp.binomial(k+dimension-1, dimension-1) for k in range(cutoff+1))
        check(f"exact physical cutoff rank at {cutoff}", ranks == sp.binomial(cutoff+dimension, dimension))

    print(json.dumps({"status":"PASS", "exact_check_groups":len(checks), "checks":checks,
                      "actual_physical_oscillators_in_source_witness":dimension,
                      "actual_cubic_vacuum_norm_squared":str(norm2),
                      "actual_three_creation_amplitude":"1/8",
                      "scope":"Exact actual retained-mode source and infinite-basis finite-support ladder controls; separate solvable cubic MODEL. No actual propagator convergence, certified time integral, essential self-adjointness or full TFPT completion."}, indent=2))


if __name__ == "__main__":
    main()
