"""Exact actual-source sharp stability check; no spectral or field cutoff.

Uses the original Ward frontend and the independently reconstructed full
14-TT source from Round 14. Scratch use requires --contracts-root PATH.
All assertions are explicit fail-closed checks even under python -OO.
"""

import argparse
import hashlib
import json
from pathlib import Path
import runpy

import sympy as s


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contracts-root", type=Path,
                        default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    base = args.contracts_root.resolve()
    ward_path = base / "free-scalar-3d" / "free_scalar_ward.py"
    escape_path = base / "escape-round14" / "escape_check.py"
    for path in (ward_path, escape_path):
        if not path.is_file():
            parser.error(f"Required actual source not found: {path}")
    checks = []

    def check(label, condition):
        if not condition:
            raise AssertionError(label)
        checks.append(label)

    def clean(expression):
        return s.simplify(s.expand(expression))

    actual = runpy.run_path(str(escape_path))
    phi, pi, hm, labels, sources, eigenvalues = actual["actual_sources"]()
    sites = actual["SITES"]
    original = runpy.run_path(str(ward_path))
    fields = original["Fields"](period=2)
    ward = original["WardComplex"](fields)
    subs = {ward.a: 1, ward.mass2: 2}
    subs.update({fields.phi(x): phi[i] for i, x in enumerate(sites)})
    subs.update({fields.pi(x): pi[i] for i, x in enumerate(sites)})
    original_hm = sum(ward.rho(x) for x in sites)
    check("full matter Hamiltonian equals original Ward source",
          clean(original_hm.subs(subs) - hm) == 0)
    stresses = {
        x: s.Matrix([ward.tau(i, i, x) for i in range(3)]
                    + [s.sqrt(2) * ward.tau(i, j, x)
                       for i, j in ((1, 2), (0, 2), (0, 1))])
        for x in sites
    }
    for index, (momentum, polarization) in enumerate(labels):
        vector = actual["tt_frame"](momentum)[0][polarization]
        source = sum(
            s.Integer(-1) ** sum(k * x for k, x in zip(momentum, site))
            * (vector.T * stresses[site])[0] / s.sqrt(8)
            for site in sites
        )
        check(f"original Ward TT source {momentum}/{polarization}",
              clean(source.subs(subs) - sources[index]) == 0)
    check("every physical TT oscillator and scalar is retained",
          len(phi) == 8 and len(sources) == 14 and len(eigenvalues) == 14)
    check("all actual TT stiffnesses are strictly positive",
          all(ell > 0 for ell in eigenvalues))
    check("all actual TT stresses are configuration-only homogeneous quadratics",
          all(not (set(pi) & T.free_symbols)
              and clean(sum(x * s.diff(T, x) for x in phi) - 2*T) == 0
              for T in sources))
    laplace = lambda expression, variables: s.expand(sum(s.diff(expression, x, 2)
                                                        for x in variables))
    check("every actual nonzero-momentum TT stress has zero Gaussian trace",
          all(laplace(T, phi) == 0 for T in sources))
    R = s.expand(sum(T*T / (2*ell) for T, ell in zip(sources, eigenvalues)))
    delta = dict.fromkeys(phi, 0)
    delta[phi[0]] = 1
    DR = laplace(R, phi)
    DDR = laplace(DR, phi)
    vm = s.expand(hm - sum(p*p for p in pi)/2)
    check("actual nonvacuous minimal quartic at delta profile",
          R.subs(delta) == s.Rational(3, 256))
    check("actual first Gaussian quartic contraction",
          DR.subs(delta) == s.Rational(43, 144))
    check("actual second Gaussian quartic contraction",
          DDR == s.Rational(43, 9))
    check("actual matter energy at delta profile", vm.subs(delta) == 4)
    check("minimal correction is homogeneous quartic",
          clean(sum(x*s.diff(R, x) for x in phi)-4*R) == 0)
    shift = s.symbols("shift", real=True)
    check("minimal correction preserves the actual uniform scalar shift",
          clean(R.subs({x: x+shift for x in phi}, simultaneous=True)-R) == 0)
    direct_DR = sum(sum(s.diff(T, x)**2 for x in phi)/ell
                    for T, ell in zip(sources, eigenvalues))
    direct_DDR = 2*sum(sum(s.diff(T, x, y)**2 for x in phi for y in phi)/ell
                      for T, ell in zip(sources, eigenvalues))
    check("independent source-gradient contraction reproduces Delta R",
          clean(DR-direct_DR) == 0)
    check("independent source-Hessian contraction reproduces Delta squared R",
          clean(DDR-direct_DDR) == 0)

    q = s.symbols("Q0:14", real=True)
    g, kappa = s.symbols("g kappa", real=True)
    radius = s.symbols("t", positive=True)
    variables = phi + q
    V = s.expand(vm + sum(ell*Q*Q/2+g*Q*T
                          for Q, T, ell in zip(q, sources, eigenvalues)) + g*g*kappa*R)
    square = vm + sum(ell*(Q+g*T/ell)**2/2
                      for Q, T, ell in zip(q, sources, eigenvalues)) + g*g*(kappa-1)*R
    check("full fourteen-mode exact square completion", clean(V-square) == 0)
    centers = {x: radius*delta[x] for x in phi}
    centers.update({Q: -g*radius**2*T.subs(delta)/ell
                    for Q, T, ell in zip(q, sources, eigenvalues)})
    classical = clean(V.subs(centers, simultaneous=True))
    check("full exact classical sharp-threshold trajectory",
          clean(classical - 4*radius**2
                - s.Rational(3, 256)*g*g*(kappa-1)*radius**4) == 0)
    DV, DDV = laplace(V, variables), laplace(laplace(V, variables), variables)
    gaussian = clean(s.Rational(len(variables), 4)
                     + (V+DV/4+DDV/32).subs(centers, simultaneous=True))
    expected = (s.Rational(3, 256)*g*g*(kappa-1)*radius**4
                + (4+s.Rational(43, 576)*kappa*g*g)*radius**2
                + s.Rational(91, 2)+s.Rational(43, 288)*kappa*g*g)
    check("complete genuine Gaussian expectation equals exact formula",
          clean(gaussian-expected) == 0)
    free_hessian_trace = s.trace(s.hessian(vm, phi)) + sum(eigenvalues)
    check("all twenty-two Gaussian kinetic and oscillator zero-point terms",
          free_hessian_trace == 160
          and (len(variables)+free_hessian_trace)/4 == s.Rational(91, 2))
    independent_gaussian = (classical+s.Rational(91, 2)
                            + kappa*g*g*(radius**2*DR.subs(delta)/4+DDR/32))
    check("independent quartic contractions reproduce full Gaussian expectation",
          clean(gaussian-independent_gaussian) == 0)
    for coefficient in (s.Integer(-1), s.Integer(0), s.Rational(1, 2),
                        s.Rational(99, 100)):
        check(f"coefficient {coefficient} fails quantum lower boundedness",
              s.limit(gaussian.subs({g: 1, kappa: coefficient}), radius, s.oo) == -s.oo)
    check("sharp endpoint removes exactly the negative quartic term",
          s.Poly(gaussian.subs(kappa, 1), radius).degree() == 2
          and clean(s.expand(gaussian).coeff(radius, 4)
                    - s.Rational(3, 256)*g*g*(kappa-1)) == 0)
    check("above-endpoint negative-control coefficient stabilizes this ray",
          s.limit(gaussian.subs({g: 1, kappa: 2}), radius, s.oo) == s.oo)
    check("zero-coupling degeneracy is explicit",
          s.diff(gaussian.subs(g, 0), kappa) == 0)

    # Positive corrections are an infinite family, not a unique stable theory.
    eps = s.symbols("epsilon", nonnegative=True)
    W = eps*(phi[0]-phi[1])**4
    check("larger shift-invariant quartic family is genuinely distinct",
          W.subs(delta) == eps
          and clean(W.subs({x: x+shift for x in phi}, simultaneous=True)-W) == 0)
    check("negative actual-source matrix direction can be invisible",
          sum(T == 0 for T in sources) == 9)
    invisible = next(i for i, T in enumerate(sources) if T == 0)
    Amutant = s.diag(*[1/ell for ell in eigenvalues])
    Amutant[invisible, invisible] -= 2
    vectorT = s.Matrix(sources)
    check("actual invisible-direction mutation keeps the same unique scalar function",
          clean((vectorT.T*Amutant*vectorT)[0]/2-R) == 0
          and Amutant[invisible, invisible]-1/eigenvalues[invisible] == -2)
    x, y = s.symbols("x y", real=True)
    Adiff = s.Matrix([[0, 1], [1, 0]])
    modelT = s.Matrix([x*x, y*y])
    check("source-image positivity does not imply full matrix positivity",
          Adiff.det() == -1 and (modelT.T*Adiff*modelT)[0] == 2*x*x*y*y)

    # General fixed-coupling compensation is not covered by quartic homogeneity.
    matter_compensated = s.expand(V.subs({g: 1, kappa: 1}) - vm/2)
    matter_square = vm/2 + sum(ell*(Q+T/ell)**2/2
                               for Q, T, ell in zip(q, sources, eigenvalues))
    check("fixed-coupling matter compensation is an exact positive counterexample",
          clean(matter_compensated-matter_square) == 0
          and (R-vm/2).subs(delta) < R.subs(delta))
    ett = clean(sum(s.sqrt(ell) for ell in eigenvalues)/2)
    check("actual shifted TT oscillator lower bound includes all retained modes",
          ett == 6+6*s.sqrt(2)+2*s.sqrt(3) and ett > 0)
    check("constant negative correction has negative classical vacuum",
          (V.subs({g: 1, kappa: 1})-ett/2).subs(dict.fromkeys(variables, 0)) == -ett/2)
    check("the same constant stays below the rigorous quantum zero-point bound",
          clean(ett-ett/2) == ett/2 and ett/2 > 0)
    z = s.symbols("z", nonnegative=True)
    check("sextic compensation changes the degree and is bounded below",
          s.expand(z**3-z+(s.Rational(2, 3)/s.sqrt(3)))
          == s.expand((z-1/s.sqrt(3))**2*(z+2/s.sqrt(3))))

    # Independent-source square/Schur identity; no hidden fitted coefficient.
    Q1, Q2, j1, j2, a11, a12, a22 = s.symbols("Q1 Q2 j1 j2 a11 a12 a22", real=True)
    ls = s.diag(2, 3)
    aa = s.Matrix([[a11, a12], [a12, a22]])
    qq, jj = s.Matrix([Q1, Q2]), s.Matrix([j1, j2])
    coupled = (qq.T*ls*qq)[0]/2+(qq.T*jj)[0]+(jj.T*aa*jj)[0]/2
    shifted = qq+ls.inv()*jj
    remainder = (shifted.T*ls*shifted)[0]/2+(jj.T*(aa-ls.inv())*jj)[0]/2
    check("independent-source sharp Schur remainder identity",
          clean(coupled-remainder) == 0)

    print(json.dumps({
        "status": "PASS", "exact_check_count": len(checks),
        "checked_groups": checks,
        "source_sha256": {str(path.relative_to(base)): hashlib.sha256(path.read_bytes()).hexdigest()
                          for path in (ward_path, escape_path)},
        "actual_scalar_coordinates": len(phi), "retained_TT_coordinates": len(sources),
        "identically_zero_TT_source_count": sum(T == 0 for T in sources),
        "minimal_R_at_delta": str(R.subs(delta)),
        "Delta_R_at_delta": str(DR.subs(delta)), "Delta_squared_R": str(DDR),
        "exact_Gaussian_expectation": str(s.expand(expected)),
        "sharp_scalar_coefficient_threshold": "kappa >= 1 for every fixed g != 0",
        "scope": "Fixed finite actual free-scalar/TT source. Unique least homogeneous-quartic stabilizer, not uniqueness of all stable theories or microscopic TFPT selection. No T-gate, continuum, locality, or RH conclusion.",
    }, indent=2))


if __name__ == "__main__":
    main()
