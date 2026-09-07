"""Original-Ward/full-14-TT independent source and displacement audit.

Integrated layout: the original Ward frontend is the neighboring
free-scalar-3d/free_scalar_ward.py. Scratch use requires --ward-source.
No personal paths, fallback repository guesses, or repository writes.
"""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import runpy
import sympy as sp


HERE = Path(__file__).resolve().parent


def load_escape_checker():
    source = HERE / "escape_check.py"
    spec = importlib.util.spec_from_file_location("round14_full_source_escape", source)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load the sibling escape_check.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ward-source", type=Path,
                        default=HERE.parent / "free-scalar-3d" / "free_scalar_ward.py")
    args = parser.parse_args()
    ward_source = args.ward_source.resolve()
    if not ward_source.is_file():
        parser.error("Ward frontend not found; scratch invocation requires --ward-source PATH")
    escape = load_escape_checker()
    checked = []

    def check(label, condition):
        if not condition:
            raise AssertionError(label)
        checked.append(label)

    clean = escape.clean
    phi, pi, hm, labels, sources, eigenvalues = escape.actual_sources()
    original = runpy.run_path(str(ward_source))
    fields = original["Fields"](period=2)
    ward = original["WardComplex"](fields)
    substitutions = {ward.a: 1, ward.mass2: 2}
    substitutions.update({fields.phi(x): phi[i] for i, x in enumerate(escape.SITES)})
    substitutions.update({fields.pi(x): pi[i] for i, x in enumerate(escape.SITES)})
    original_hm = sum(ward.rho(x) for x in escape.SITES)
    check("full scalar Hamiltonian equals original Ward frontend",
          clean(original_hm.subs(substitutions) - hm) == 0)
    original_stresses = {
        x: sp.Matrix([ward.tau(j, j, x) for j in range(3)]
                     + [sp.sqrt(2) * ward.tau(i, j, x)
                        for i, j in ((1, 2), (0, 2), (0, 1))])
        for x in escape.SITES
    }
    for index, (momentum, polarization) in enumerate(labels):
        vector = escape.tt_frame(momentum)[0][polarization]
        source = sum(
            sp.Integer(-1) ** sum(k * y for k, y in zip(momentum, x))
            * (vector.T * original_stresses[x])[0] / sp.sqrt(8)
            for x in escape.SITES
        )
        check(f"original Ward source equals TT {momentum}/{polarization}",
              clean(source.subs(substitutions) - sources[index]) == 0)

    # The characteristic coefficient and current are read from the ORIGINAL
    # Ward frontend, whereas the full physical Hamiltonian uses the separately
    # reconstructed fourteen-mode source just checked above.
    weights = [sp.Integer(-1) ** (x[0] + x[1]) / sp.sqrt(8) for x in escape.SITES]
    rho = clean(sum(weight * ward.rho(x) for weight, x in zip(weights, escape.SITES))
                .subs(substitutions))
    tau = sum((weight * original_stresses[x] for weight, x in zip(weights, escape.SITES)),
              sp.zeros(6, 1)).subs(substitutions).applyfunc(clean)
    current = sp.Matrix([
        clean(sum(weight * ward.current(axis, x) for weight, x in zip(weights, escape.SITES))
              .subs(substitutions))
        for axis in range(3)
    ])
    scalar = sp.Matrix([4, 4, 8, 0, 0, 4 * sp.sqrt(2)])
    coefficient = clean((scalar.T * tau)[0] / 128 + rho / 16)
    check("original characteristic B has actual kinetic Hessian",
          (sp.hessian(coefficient, pi) - 3 * sp.diag(*weights) / 16).applyfunc(clean) == sp.zeros(8))
    q = sp.symbols("Q0:14", real=True)
    p = sp.symbols("P0:14", real=True)
    g = sp.symbols("g", real=True, nonzero=True)
    time = sp.symbols("time", real=True)
    radius = sp.symbols("R", positive=True)
    bv = sp.Matrix([[5, -3, 0], [-3, 5, 0], [0, 0, 8]]) / 32
    cv = sp.Matrix([sp.Rational(1, 2), 0, 0])
    free_tt = sum(pp ** 2 + ell * qq ** 2 for pp, ell, qq in zip(p, eigenvalues, q)) / 2
    full_cubic = g * sum(qq * source for qq, source in zip(q, sources))
    htime = sp.expand(free_tt + hm + full_cubic + g * (cv.T * bv * current)[0]
                      + (cv.T * bv * cv)[0] / 2 + g * time * coefficient - time ** 2 / 32)
    selected = labels.index((escape.SELECTED, 0))
    delta = dict.fromkeys(phi, 0)
    delta[phi[0]] = 1
    check("simpler scalar delta-profile has the actual selected source 1/4",
          clean(sources[selected].subs(delta)) == sp.Rational(1, 4))
    variables = phi + pi + q + p
    branch_results = []
    for tag, site, sign in (("plus", 0, 1), ("minus", 2, -1)):
        c = 1 + 3 * g * time * weights[site] / 16
        center = dict.fromkeys(variables, sp.Integer(0))
        center.update({phi[0]: radius ** 2, pi[site]: radius ** 3,
                       q[selected]: -2 * c * radius ** 2 / g})
        displaced = {z: z + center[z] for z in variables}
        moved_h = sp.expand(htime.subs(displaced, simultaneous=True))
        moved_b = sp.expand(coefficient.subs(displaced, simultaneous=True))
        check(f"{tag}: complete 14-TT operator-valued R^6 coefficient vanishes",
              clean(moved_h.coeff(radius, 6)) == 0)
        degree_h = sp.Poly(moved_h, radius).degree()
        check(f"{tag}: complete displaced Hamiltonian degree at most five", degree_h <= 5)
        beta = clean(moved_b.coeff(radius, 6))
        expected_beta = sign * 3 / (32 * sp.sqrt(8))
        check(f"{tag}: original B has nonzero R^6 coefficient 3w/32",
              clean(beta - expected_beta) == 0 and beta != 0)
        check(f"{tag}: B remainder degree at most four",
              sp.Poly(sp.expand(moved_b - beta * radius ** 6), radius).degree() <= 4)
        aligned_product = sp.symbols("aligned_product", nonnegative=True)
        check(f"{tag}: selected kinetic direction is positive at arbitrary real time",
              clean(c.subs(time, sign * aligned_product / g)
                    - 1 - 3 * aligned_product / (16 * sp.sqrt(8))) == 0)
        spectator_max_degree = 0
        for index, (qq, source) in enumerate(zip(q, sources)):
            if index == selected:
                continue
            moved_vertex = sp.expand((g * qq * source).subs(displaced, simultaneous=True))
            degree = sp.Poly(moved_vertex, radius).degree()
            check(f"{tag}: actual undisplaced TT spectator {labels[index]} degree at most four",
                  degree <= 4)
            if degree != sp.S.NegativeInfinity:
                spectator_max_degree = max(spectator_max_degree, int(degree))
        check(f"{tag}: at least one actual spectator reaches degree four", spectator_max_degree == 4)
        mutated = sp.expand((htime - full_cubic).subs(displaced, simultaneous=True))
        check(f"{tag}: removing the actual cubic destroys the degree improvement",
              clean(mutated.coeff(radius, 6) - c / 2) == 0)
        branch_results.append({"branch": tag, "full_operator_displacement_degree": int(degree_h),
                               "B_leading_R6": str(beta),
                               "actual_TT_spectators_checked": 13,
                               "spectator_max_displacement_degree": spectator_max_degree})

    print(json.dumps({
        "status": "PASS", "exact_check_count": len(checked),
        "original_Ward_source_sha256": hashlib.sha256(ward_source.read_bytes()).hexdigest(),
        "sibling_escape_checker_sha256": hashlib.sha256((HERE / "escape_check.py").read_bytes()).hexdigest(),
        "original_Ward_TT_sources_compared": len(sources),
        "all_physical_scalar_coordinates": len(phi), "all_physical_TT_coordinates": len(q),
        "independent_displacement": "phi=R^2 delta_000; pi_i=R^3; Q_plus=-2 C_i(t) R^2/g",
        "branches": branch_results,
        "scope": (
            "Exact comparison with the original full Ward frontend and full 14-TT "
            "operator-valued displacement certificate. Supports the stated fixed "
            "operator/absolute-form-domain obstruction only through its separate "
            "closed-graph proof. No moving-domain, propagator-existence, essential "
            "self-adjointness, continuum, gravitational or RH conclusion."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
