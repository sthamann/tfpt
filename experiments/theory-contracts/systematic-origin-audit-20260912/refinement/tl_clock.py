"""Exact conditional Bell/TL checks; spectral parameter is not physical time.

NON-RH. Does not derive the physical tensor factors, graph, active U(d),
Hamiltonian selection, or any T1--T8 acceptance. General proofs: README.md.
"""
import json
import sympy as s


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    cases = []
    for d in (2, 3, 4):
        eye = s.eye(d**3)
        phi = s.Matrix([s.Rational(int(i//d == i % d), 1)/s.sqrt(d)
                        for i in range(d*d)])
        pair = phi*phi.T
        e = d*s.kronecker_product(pair, s.eye(d))
        f = d*s.kronecker_product(s.eye(d), pair)
        require(e*e == d*e and f*f == d*f, 'quadratic TL relations')
        require(e*f*e == e and f*e*f == f, 'adjacent TL relations')
        require(e != f, 'nondegenerate representation for YB coefficient comparison')
        x, y = s.Rational(1, 10), s.Rational(1, 7)
        z = (x+y+d*x*y)/(1-x*y)
        require((eye+x*e)*(eye+z*f)*(eye+y*e)
                == (eye+y*f)*(eye+z*e)*(eye+x*f), 'exact rational Yang-Baxter control')
        wrong_z = x+y+d*x*y
        require((eye+x*e)*(eye+wrong_z*f)*(eye+y*e)
                != (eye+y*f)*(eye+wrong_z*e)*(eye+x*f),
                'negative control: group addition is not YB spectral addition')
        # Four-site distant contractions act on disjoint factors.
        distant_left = d*s.kronecker_product(pair, s.eye(d*d))
        distant_right = d*s.kronecker_product(s.eye(d*d), pair)
        require(distant_left*distant_right == distant_right*distant_left,
                'distant TL generators commute')
        cases.append({'d': d, 'TL_and_YB': True, 'wrong_group_law_rejected': True})
    # Positive unitary control at d=4 on imaginary spectral contour,
    # tan(theta)=1/2, eta=arcosh(2). Only two eigenvalues are necessary.
    x = (-1+s.I*s.sqrt(3))/8
    parallel = 1+4*x
    require(s.simplify(parallel*s.conjugate(parallel)) == 1,
            'Baxterized gate is unitary on this spectral contour')
    twice_x = (2*x+4*x*x)/(1-x*x)
    require(s.simplify((1+4*twice_x)*s.conjugate(1+4*twice_x)) == 1,
            'doubled spectral parameter remains unitary')
    require(s.simplify(1+4*twice_x-parallel**2) != 0,
            'two unitary gates do not compose by adding the spectral parameter')
    # Hyperbolic solution is checked in rational exponential coordinates.
    # q=e^eta, r=e^(cu), t=e^(cv), d=q+1/q.
    q, r, t = s.symbols('q r t', nonzero=True)
    fun = lambda z: q*(z*z-1)/(q*q-z*z)
    delta = q+1/q
    require(s.factor(fun(r*t)*(1-fun(r)*fun(t))
                     -fun(r)-fun(t)-delta*fun(r)*fun(t)) == 0,
            'general hyperbolic YB family')
    print(json.dumps({'scope': 'NON-RH conditional finite Bell model',
        'cases': cases, 'd4_unitary_spectral_family_not_additive_time_group': True,
        'general_family': 'f(u)=sinh(c*u)/sinh(eta-c*u), d=2*cosh(eta)',
        'unselected_scale': 'c', 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
