"""Exact one-leaf information loss under a fixed tree of Bell ground encodings.

This is a conditional encoding, not microscopic time evolution or a derived
holographic boundary. No full exponentially large tree is constructed.
General proofs and the global/local distinction are recorded in README.md.
"""
import itertools
import json
import sympy as s


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    results = []
    for d in (2, 3, 4):
        phi = s.Matrix([s.Rational(int(i//d == i % d), 1)/s.sqrt(d)
                        for i in range(d*d)])
        v = s.kronecker_product(phi, s.eye(d))
        w = s.kronecker_product(s.eye(d), phi)
        z = (v+w)/s.sqrt(2*(1+s.Rational(1, d)))
        require(z.T*z == s.eye(d), 'entire encoder remains isometric')
        a = s.Rational(d+2, 2*(d+1))
        for row, col in itertools.product(range(d), repeat=2):
            unit = s.zeros(d)
            unit[row, col] = 1
            expected = a*unit+(1-a)*s.trace(unit)*s.eye(d)/d
            require(s.simplify(z.T*s.kronecker_product(unit, s.eye(d*d))*z)
                    == expected, 'all matrix units: outer leaf is depolarizing')
        # Choi partial transpose has antisymmetric eigenvalue below; its
        # zero marks the exact EB threshold, with separable Haar construction
        # giving sufficiency (not PPT alone in dimensions d>2).
        first = next(k for k in range(1, 30) if a**k <= s.Rational(1, d+1))
        threshold = s.Rational(1, d+1)
        antisymmetric = lambda lam: (1-(d+1)*lam)/d**2
        require(antisymmetric(a**(first-1)) < 0
                and antisymmetric(a**first) >= 0, 'first exact threshold crossing')
        # Explicit convex decomposition of the normalized Choi matrix.
        pair = phi*phi.T
        mixed = s.eye(d*d)/d**2
        threshold_choi = (s.eye(d*d)+d*pair)/(d*(d+1))
        lam = a**first
        weight = (d+1)*lam
        require(0 <= weight <= 1, 'separable mixture coefficient')
        require(lam*pair+(1-lam)*mixed
                == weight*threshold_choi+(1-weight)*mixed,
                'EB sufficiency uses separable decomposition, not PPT equivalence')
        require(lam > 0, 'EB does not mean constant channel or loss of all classical information')
        # Deliberately false claim must be rejected.
        require(a != 1 and a**2 != a, 'negative control: a single leaf is not a perfect record')
        results.append({'d': d, 'outer_leaf_multiplier': str(a),
            'first_entanglement_breaking_depth': first,
            'multiplier_at_threshold_crossing': str(lam)})
    print(json.dumps({'scope': 'fixed-tree encoding; only all-outer-child leaf paths',
        'cases': results, 'global_encoding_isometric': True,
        'all_leaves_or_boundary_regions_classified': False,
        'physical_holography_derived': False, 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
