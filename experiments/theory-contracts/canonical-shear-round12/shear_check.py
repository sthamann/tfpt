"""Exact canonical-shear audit, with a nonzero actual Ward/TT vertex.

No finite CCR matrices, floating eigenvalues, repository edits or spectral
truncation claims. The generic differential tests are separate from the
actual-source vertex witness. Run with the TFPT SymPy environment.
"""
import json
from itertools import product
from pathlib import Path
import runpy
import sympy as s


def exact_zero(expression):
    assert s.expand(expression) == 0


def actual_vertex():
    source = Path(__file__).resolve().parent.parent / 'free-scalar-3d/free_scalar_ward.py'
    module = runpy.run_path(str(source))
    fields = module['Fields']()
    ward = module['WardComplex'](fields)
    local_plus = s.expand(ward.tau(0, 0, (0, 0, 0)) - ward.tau(1, 1, (0, 0, 0)))
    local_cross = ward.tau(0, 1, (0, 0, 0))
    sites = list(product(range(3), repeat=3))
    index = {x: j for j, x in enumerate(sites)}
    phi = s.symbols('phi0:27', real=True)
    cosine = [s.Integer(1), -s.Rational(1, 2), -s.Rational(1, 2)]
    norm = s.sqrt(2 * sum(cosine[x[2]]**2 for x in sites))
    assert norm == 3*s.sqrt(3)
    weights = {x: cosine[x[2]] / norm for x in sites}
    polarizations = [s.diag(1, -1, 0), s.Matrix([[0,1,0],[1,0,0],[0,0,0]])]
    for polarization in polarizations:
        assert s.trace(polarization) == 0
        assert polarization*s.Matrix([0,0,s.sqrt(3)]) == s.zeros(3,1)
        assert s.simplify(sum(w*w for w in weights.values())
                          *s.trace(polarization.T*polarization)) == 1
    assert sum(weights.values()) == 0

    def specialize(expression, at):
        replace = {ward.a: 1}
        for symbol in expression.free_symbols:
            if symbol not in fields.reverse:
                continue
            kind, offset = fields.reverse[symbol]
            assert kind == 'phi', 'TT source must cancel the momentum terms'
            shifted = tuple((at[j] + offset[j]) % 3 for j in range(3))
            replace[symbol] = phi[index[shifted]]
        return s.expand(expression.subs(replace, simultaneous=True))

    TT = [s.expand(sum(weights[x]*specialize(local_plus, x) for x in sites)),
          s.expand(sum(2*weights[x]*specialize(local_cross, x) for x in sites))]
    ell = s.Integer(3)  # k=(0,0,2*pi/3), both normalized real TT polarizations.
    F = [T/ell for T in TT]
    profile, amplitude = [1, -1, 0], [1, 2, -1]
    background = {phi[index[x]]: profile[x[0]]*amplitude[x[2]] for x in sites}
    for T, FF in zip(TT, F):
        assert T != 0
        assert s.Poly(T, *phi).total_degree() == 2
        exact_zero(sum(p*s.diff(FF, p) for p in phi) - 2*FF)
        exact_zero(sum(s.diff(FF, p, 2) for p in phi))
        exact_zero(sum(s.diff(FF, p) for p in phi))
    values = [s.simplify(T.subs(background)) for T in TT]
    assert values[0] != 0

    # In the FULL model set all Q=0, all P except the actual first TT mode
    # to zero, P_1=1, and pi=phi_background. No other mode is discarded:
    # it simply contributes zero to this mixed-momentum first-vertex test.
    mixed = s.expand(-sum(phi[j]*s.diff(F[0], phi[j]) for j in range(27)))
    exact_zero(mixed + 2*F[0])
    witness = s.simplify(mixed.subs(background))
    assert witness != 0
    quadratic_witness = s.simplify(sum(s.diff(F[0], variable).subs(background)**2
                                      for variable in phi)/2)
    assert quadratic_witness > 0

    # A concrete scalar site shift changes an actual TT oscillator shift.
    a = s.symbols('a', real=True)
    for site in sites:
        variable = phi[index[site]]
        delta = s.expand(F[0].subs(variable, variable+a) - F[0])
        if delta != 0:
            exact_zero(delta - a*s.diff(F[0], variable) - a*a*s.diff(F[0], variable, 2)/2)
            shift_site = site
            break
    else:
        raise AssertionError('The actual shear cannot be constant')
    return {'lattice': [3, 3, 3], 'TT_eigenvalue': str(ell),
            'TT_values_on_background': [str(v) for v in values],
            'background': 'phi(x,y,z)=(1,-1,0)[x]*(1,2,-1)[z]',
            'full_model_old_first_vertex_at_Q_zero': '0',
            'full_model_new_first_vertex_P1_one_pi_phi': str(witness),
            'full_model_difference_at_pi_zero_coefficient_g_squared': str(quadratic_witness),
            'actual_scalar_shift_site_changing_TT': shift_site,
            'TT_homogeneous_quadratic_and_configuration_harmonic': True}


def canonical_and_quantum():
    x, y, q, r, px, py, p, t, g, a, b = s.symbols(
        'x y q r px py p t g a b', real=True)
    fields, tensors = [x, y], [q, r]
    scalar_p, tensor_p = [px, py], [p, t]
    FF = s.Matrix([x*x-y*y, 2*x*y])
    J = FF.jacobian(fields)
    avec = J.T*s.Matrix(tensor_p)
    coordinates = fields + tensors
    momenta = scalar_p + tensor_p
    newq = fields + list(s.Matrix(tensors)+g*FF)
    newp = list(s.Matrix(scalar_p)-g*avec) + tensor_p

    def pb(f, h):
        return s.expand(sum(s.diff(f, z)*s.diff(h, pp)-s.diff(f, pp)*s.diff(h, z)
                            for z, pp in zip(coordinates, momenta)))

    for i, j in product(range(4), repeat=2):
        assert pb(newq[i], newq[j]) == 0
        assert pb(newp[i], newp[j]) == 0
        assert pb(newq[i], newp[j]) == int(i == j)

    def shift(expression, sign):
        return s.expand(expression.subs({q:q+sign*g*FF[0], r:r+sign*g*FF[1]}, simultaneous=True))

    # U psi(phi,q)=psi(phi,q-gF); its inverse uses the opposite sign.
    test = x*x*q*r + y*q*q + x*r + x*y*y + r*r
    exact_zero(shift(shift(test, 1), -1)-test)
    def momentum(z, expression):
        return -s.I*s.diff(expression, z)
    def A(j, expression):
        return sum(J[k, j]*momentum(tensors[k], expression) for k in range(2))
    for j, z in enumerate(fields):
        transformed = shift(momentum(z, shift(test, 1)), -1)
        exact_zero(transformed - momentum(z, test) - g*A(j, test))
    for z in tensors:
        exact_zero(shift(momentum(z, shift(test, 1)), -1)-momentum(z, test))

    def Hplus(expression):
        kinetic = -sum(s.diff(expression, z, 2) for z in coordinates)/2
        matter = (x*x+2*y*y)*expression/2
        shifted = ((q+g*FF[0])**2 + 3*(r+g*FF[1])**2)*expression/2
        return s.expand(kinetic+matter+shifted)
    transformed = shift(Hplus(shift(test, 1)), -1)
    covariant_kinetic = 0
    for j, z in enumerate(fields):
        inner = momentum(z, test)+g*A(j, test)
        covariant_kinetic += (momentum(z, inner)+g*A(j, inner))/2
    expected = (covariant_kinetic-sum(s.diff(test, z, 2) for z in tensors)/2
                +(x*x+2*y*y+q*q+3*r*r)*test/2)
    exact_zero(transformed-expected)
    free = -sum(s.diff(test, z, 2) for z in coordinates)/2+(x*x+2*y*y+q*q+3*r*r)*test/2
    assert s.expand(transformed-free) != 0

    # Exact finite pullback Weyl translation, including the quadratic term.
    def scalar_shift(expression):
        return s.expand(expression.subs({x:x+a, y:y+b}, simultaneous=True))
    lhs = shift(scalar_shift(shift(test, 1)), -1)
    delta = s.Matrix([scalar_shift(FF[k])-FF[k] for k in range(2)])
    rhs = test.subs({x:x+a, y:y+b, q:q+g*delta[0], r:r+g*delta[1]}, simultaneous=True)
    exact_zero(lhs-rhs)

    # H_iso is the FULL conjugate, not just the shifted potential.
    def Hzero(expression):
        return s.expand(-sum(s.diff(expression, z, 2) for z in coordinates)/2
                        +(x*x+2*y*y+q*q+3*r*r)*expression/2)
    Hiso_test = shift(Hzero(shift(test, -1)), 1)
    difference = 0
    for j, z in enumerate(fields):
        difference += -g*(momentum(z, A(j, test))+A(j, momentum(z, test)))/2
        difference += g*g*A(j, A(j, test))/2
    exact_zero(Hiso_test-Hplus(test)-difference)
    assert s.expand(difference).coeff(g, 1) != 0
    return {'canonical_bracket_checks': 48,
            'exact_unitary_chain_rule_and_both_Hamiltonians': True,
            'exact_finite_Weyl_shift': True,
            'missing_linear_kinetic_vertex_mutant_rejected': True,
            'generic_test_role': 'Differential/ordering identities only; actual source witness is separate.'}


if __name__ == '__main__':
    print(json.dumps({'status':'PASS', 'actual_source_vertex':actual_vertex(),
                      'canonical_quantum_algebra':canonical_and_quantum(),
                      'scope':'Finite-volume exact algebra. PROOF.md supplies Hilbert-domain and transported-net statements; ordinary scattering-limit existence is not proved.'}, indent=2))
