"""Positive trace comparison at u>0, plus exact Noether/geometric controls.

Unpromoted NON-RH research. No physical T1-T8 closure. The base partition
is re-executed from pinned Round28 sources, never replaced by a finite carrier.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as s

PINS = {
    "poisson-charge-round28/checker.py": "6b1ad08c38433f71a8c353cf8bbd535eae91c7ea064e36de9b6062eda644cb22",
    "poisson-charge-round28/PROOF.md": "bcab65c05a8bca2bab10fc6fa4d9e46ad99f9199529138eefc587fa8645b69ae",
    "poisson-charge-round28/README.md": "cfb824135a22c92d1921ac3d4fff057c431becf431fb9f48279ce6179b18d82e",
    "poisson-charge-round28/test_checker.py": "31ce05ca4386699e779cd19b46823cfa8472d817f3fe428fa670f62f69307f76",
    "poisson-charge-round28/validation.json": "23a2491e2d3d0370883e085bf65dde3c72a1cb0048a905d4429627c337514c2b",
    "round22_algebra.py": "133a11d7d873062960e685e15ce0d55dcf9baf16b59199de5846e2e27711ae5c",
    "full-reference-control-round27/PROOF.md": "fa672c87b5a3d952e9294e78ecf922905a6c48d750cdbe8d1507ab63953ac691",
    "local-charge-transport-round20/PROOF.md": "6d7059cc75108be2b7262f030b83e2c14c774a950d2f1ccd0f9c5c1b3b5afb5c",
    "scalar-charge-energy-round20/PROOF.md": "f54190fffdf3ccc110c5a66d6da0575c7b8ad96a5a880fcb4b6c01f930ccb7b5",
}


def require(condition, label):
    if not bool(condition):
        raise ValueError(label)


def inputs(root):
    for name, expected in PINS.items():
        path = root/name
        require(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                "pinned input missing or changed: " + name)
    spec = importlib.util.spec_from_file_location("r29_previous", root/"poisson-charge-round28/checker.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def log_bounds(x, terms=32):
    """Positive atanh series with a rational geometric remainder."""
    x = F(x)
    require(1 <= x <= 2 and type(terms) is int and terms >= 1, "log enclosure domain")
    z = (x-1)/(x+1)
    lo = 2*sum((z**(2*k+1)/(2*k+1) for k in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return lo, lo+tail


def scalar_variance():
    # Diagonal covariance of the SAME primitive T3 Gaussian, not its continuum limit.
    return sum((count*(F(1, lam)+F(2, lam+27))
                for lam, count in [(1, 1), (4, 6), (7, 12), (10, 8)]), F(0))/27


def interaction_moment_upper(eta, r=F(9, 10)):
    eta, r = F(eta), F(r)
    require(0 <= eta < 1 and F(1, 2) <= r < 1, "moment comparison domain")
    log_upper = log_bounds(1/r)[1]
    # beta <W> <= N v_phi [theta + (d/2) log(1/r) + log(1+eta)]/(1-r).
    # d/2 = 4(N-1) =104; log(1+eta)<=eta. beta=1 at the declared regulator.
    return 27*scalar_variance()*(F(1, 2)+104*log_upper+eta)/(1-r)


def coupled_enclosure(base, previous, u, tolerance):
    u, tolerance = F(u), F(tolerance)
    require(u >= 0 and 0 < tolerance < 1, "nonnegative coupling and relative tolerance")
    require(base["parameters"]["u"] == 0 and base["parameters"]["beta"] == "1",
            "comparison must start at the declared uncoupled reference")
    require(base["parameters"]["N"] == 27 and base["parameters"]["T"] == 3,
            "N27 T3 covariance and entropy specialization")
    require(base["parameters"]["L"] == 3 and base["parameters"]["delta"] == "1/3"
            and base["parameters"]["sector"] == "total charge zero"
            and base["parameters"]["theta"] == "1/2", "lattice slicing, sector and trace comparison")
    require(base["parameters"]["J"] == "1/2592" and base["parameters"]["m"] == 1
            and base["parameters"]["a"] == 1 and base["parameters"]["g"] == 0
            and base["parameters"]["nu"] in ("0", "1/486"), "full reference parameter guard")
    moment = interaction_moment_upper(base["dual_relative_error_upper"])
    exponent = u*moment
    require(exponent <= 1, "numeric exp envelope needs u*M<=1; analytic theorem is not so restricted")
    lower_ratio = previous.exp_minus(exponent)[0]
    lo = F(base["full_partition_interval"]["lower"])*lower_ratio
    hi = F(base["full_partition_interval"]["upper"])
    require(0 < lo <= hi, "positive complete partition interval")
    # Include the outward interval display before certifying the displayed estimate.
    lo, hi = F(previous.outward(lo)), F(previous.outward(hi, True))
    # The harmonic center minimizes the worst relative, not absolute, error.
    center = 2*lo*hi/(lo+hi)
    displayed = F(previous.outward(center))
    rho = max(displayed/lo-1, 1-displayed/hi)
    require(rho < tolerance, "requested relative enclosure target")
    parameters = dict(base["parameters"])
    parameters["u"] = str(u)
    return {
        "parameters": parameters,
        "reference_u": 0,
        "partition_interval": previous.interval_json((lo, hi)),
        "reported_relative_minimax_estimate": previous.outward(center),
        "relative_error_upper": previous.outward(rho, True),
        "tolerance": str(tolerance),
        "beta_interaction_moment_upper": previous.outward(moment, True),
        "comparison_exponent_upper": previous.outward(exponent, True) if exponent else "0",
        "partition_ratio_lower": previous.outward(lower_ratio),
        "partition_ratio_upper": "1",
        "scalar_charge_coupling_nonzero": u > 0,
        "all_integer_charges_retained": True,
        "scalar_amplitude_cutoff": None,
        "all_signed_hop_orders_retained_by_reference_bound": True,
        "evaluation_method": "analytic positive-trace sandwich around re-executed Round28 interval",
    }


def matrix_controls():
    A = s.Matrix([[3, 1, -1], [1, 3, 1], [-1, 1, 3]])
    require(all(A[:i, :i].det() > 0 for i in range(1, 4)), "positive noncommuting control")
    require(A[0, 1]*A[1, 2]*A[2, 0] < 0, "positive trace is not a positive path measure")
    D = [s.diag(1, t, t*t) for t in (s.Integer(1), s.Rational(1, 2), s.Rational(1, 4))]
    traces = [((d*A*d)**3).trace() for d in D]
    require(traces[1]**2 <= traces[0]*traces[2], "noncommuting logarithmic midpoint convexity")
    require(traces[0] > traces[1] > traces[2], "decreasing trace powers")
    W = s.diag(0, 1, 2)
    t = s.symbols("t", real=True)
    E = s.diag(1, s.exp(-t/2), s.exp(-t))
    derivative = s.diff(((E*A*E)**3).trace(), t).subs(t, 0)
    require(derivative == -3*(W*A**3).trace(), "beta factor in logarithmic derivative")
    B = s.Matrix([[2, 1], [1, 2]])
    C = s.diag(1, s.Rational(1, 2))
    require((B-C*B*C).det() < 0, "reject false sandwich operator monotonicity")
    return {"trace_samples": [str(v) for v in traces], "derivative_at_zero": str(derivative),
            "false_operator_order_minor": str((B-C*B*C).det()),
            "evidence_type": "finite regression, not replacement for the infinite-carrier proof"}


def geometry_control():
    x, a, u = s.symbols("x a u", positive=True)
    c = a+u*x*x
    d = 8
    drift = -d*s.diff(c, x)/(2*c)
    quantum = s.simplify(s.diff(drift, x)/4+drift**2/8)
    curvature = s.simplify(d*s.diff(c, x, 2)/c-d*(d+5)*s.diff(c, x)**2/(4*c*c))
    expected = -2*u/c+12*u*u*x*x/(c*c)
    require(s.simplify(quantum-expected) == 0, "warped torus measure potential")
    psi = s.Function("psi")(x)
    curved_psi = c**2*psi  # inverse of U=c^-2, the unitary to flat measure.
    conjugated = s.simplify(-c**-2*(s.diff(curved_psi, x, 2)+drift*s.diff(curved_psi, x))/2)
    require(s.simplify(conjugated+s.diff(psi, x, 2)/2-quantum*psi) == 0,
            "full unitary conjugation including the volume measure")
    xi = s.symbols("xi")
    require(s.solve([-1+4*xi, 3-13*xi], [xi]) == [],
            "no constant curvature ordering cancels both independent structures")
    require(s.simplify((quantum+curvature/8)+s.diff(c, x)**2/(4*c*c)) == 0,
            "xi=1/4 cancels only one structure")
    require(s.simplify(curvature.subs(x, 0)-16*u/a) == 0,
            "nonzero curvature rules out a Ricci-flat configuration metric at u>0")
    curvature_second = s.simplify(s.diff(curvature, x, 2).subs(x, 0))
    require(curvature_second == -240*u*u/(a*a),
            "quadratic positive coupling has nonconstant scalar curvature")
    return {"dual_fiber_dimension": 8, "physical_spacetime_dimension_claim": False,
            "warping": "c(phi)=a+u phi^2",
            "volume_density": "c(phi)^(-4)", "unitary_to_flat_measure": "c(phi)^(-2)",
            "forced_flat_measure_potential": str(s.factor(quantum)),
            "scalar_curvature": str(s.factor(curvature)),
            "curvature_second_derivative_at_origin": str(curvature_second),
            "ricci_flat_at_positive_u": False, "constant_scalar_curvature_at_positive_u": False,
            "naive_laplace_beltrami_equals_original": False,
            "constant_xi_R_cancellation": False,
            "u_selected_by_geometrization": False}


def noether_control(e8):
    fields = s.symbols("phi0:3", real=True)
    u, J = s.symbols("u J", positive=True)
    checks = 0
    for p in e8.UNITS:
        start = (p, e8.ZERO, tuple(-value for value in p))
        finish, phase = e8.move(start, (0, 1, p))
        require(tuple(map(sum, zip(*start))) == e8.ZERO
                and tuple(map(sum, zip(*finish))) == e8.ZERO, "neutral current control sector")
        before = sum(e8.energy(n)*fields[x]**2 for x, n in enumerate(start))
        after = sum(e8.energy(n)*fields[x]**2 for x, n in enumerate(finish))
        exchange = s.expand(-s.I*J*phase*(before-after))
        require(exchange != 0, "interacting matter/hop energy exchange is not absent")
        for component in range(8):
            for site in range(3):
                # Adding u W changes the diagonal energy, but not [H,n_x^a].
                diagonal_commutator = u*before*start[site][component]-start[site][component]*u*before
                current = -s.I*J*phase*(start[site][component]-finish[site][component])
                sign = -1 if site == 0 else 1 if site == 1 else 0
                require(diagonal_commutator == 0 and current == sign*s.I*J*phase*p[component],
                        "same exact charge current for every nonnegative u")
                checks += 1
    return {"exact_charge_current_components": checks,
            "u_changes_current_operator": False, "u_changes_state_and_evolution": True,
            "energy_exchange_nonzero_in_each_channel": True,
            "coupling_selected_by_charge_conservation": False}


def run(root):
    previous = inputs(root)
    reference = previous.run(root)
    saved = json.loads((root/"poisson-charge-round28/validation.json").read_text())
    saved.pop("artifact_sources")
    require(reference == saved, "Round28 executed result must match its pinned saved record")
    cases = []
    for base in (reference, reference["spatial_charge_coupled_case"]):
        for u, tolerance in ((F(1, 65536), F(1, 100)), (F(1, 4096), F(1, 10))):
            cases.append(coupled_enclosure(base, previous, u, tolerance))
    require(scalar_variance() == F(167106, 682465), "exact boundary scalar covariance")
    return {
        "status": "PASS", "verdict": "NONZERO_U_PARTITION_ENCLOSED_AND_GEOMETRIC_SELECTION_BOUNDARY",
        "prerequisite_round28_reexecuted": True, "pinned_inputs": PINS,
        "scalar_variance_exact": str(scalar_variance()), "charge_entropy_exponent": 104,
        "cases": cases, "matrix_controls": matrix_controls(),
        "geometry": geometry_control(), "noether": noether_control(previous.inputs(root)),
        "scope": "Original signed g=0 finite regulator with u>0; no charge/scalar cutoff. Comparison intervals, not direct quadrature or a continuum result. No selected microscopic parent, chirality, graviton, T1-T8, TOE, RH or empirical promotion. Written proof, not proof-assistant certified.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.input_root)
    result["artifact_sources"] = {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                  for name in ("checker.py", "PROOF.md", "COMPILER.md", "README.md", "test_checker.py")}
    payload = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
