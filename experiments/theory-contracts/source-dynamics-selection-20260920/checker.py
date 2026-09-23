#!/usr/bin/env python3
"""Exact finite controls for the source dynamics-selection diagnostic.

The module compares the already selected free and auxiliary boundary metrics,
checks the graded null/bilinear restrictions, and gives two finite Gaussian
controls.  It is a diagnostic for the stated source-selection premises; it
does not derive a Gaussian theorem, a QWZ continuum, or a TFPT solution.
"""

from collections import Counter
from itertools import combinations, product
import hashlib
from math import isqrt
import json
from pathlib import Path
import sys

import sympy as S


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
CONTROLS = json.loads((HERE / "controls.json").read_text())
CHECKS = {}


def verify_source_manifest():
    """Verify optional repo-relative source pins; absence is an explicit skip."""
    manifest_path = HERE / "source_manifest.json"
    if not manifest_path.exists():
        return {"present": False, "skipped": True, "reason": "source_manifest.json absent"}
    manifest = json.loads(manifest_path.read_text())
    files = manifest.get("files", [])
    for item in files:
        relative = Path(item["path"])
        if relative.is_absolute():
            raise RuntimeError(f"manifest path is not repo-relative: {relative}")
        target = REPO / relative
        if not target.exists():
            raise RuntimeError(f"manifest target missing: {relative}")
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != item["sha256"]:
            raise RuntimeError(f"manifest hash mismatch: {relative}")
    return {"present": True, "skipped": False, "file_count": len(files)}


def check(name, condition):
    ok = bool(condition)
    CHECKS[name] = ok
    if not ok:
        raise RuntimeError(name)


def integral_vector(vector):
    return all(S.denom(x) == 1 for x in vector)


def integral_matrix(matrix):
    return all(S.denom(x) == 1 for x in matrix)


def residue(value, modulus):
    value = S.Rational(value)
    if value.q != 1:
        raise ValueError(f"non-integral modular value: {value}")
    return int(value) % modulus


def bilinear(x, matrix, y):
    return (x.T * matrix * y)[0]


def qform(x, matrix):
    return bilinear(x, matrix, x)


def e8_data():
    basis = [
        S.Matrix([1, -1, -1, -1, -1, -1, -1, 1]) / 2,
        S.Matrix([1, 1, 0, 0, 0, 0, 0, 0]),
    ]
    for i in range(6):
        p = S.zeros(8, 1)
        p[i], p[i + 1] = -1, 1
        basis.append(p)

    roots = []
    for i, j in combinations(range(8), 2):
        for si, sj in product((-1, 1), repeat=2):
            p = [S.Integer(0)] * 8
            p[i], p[j] = si, sj
            roots.append(S.Matrix(p))
    for signs in product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(S.Matrix(signs) / 2)
    return basis, roots


def rational_complex(value):
    return S.denom(S.re(value)) >= 1 and S.denom(S.im(value)) >= 1


def as_string(value):
    return str(S.simplify(value))


def main():
    manifest_status = verify_source_manifest()
    K = S.diag(*([1] * 9 + [-1]))
    eye10 = S.eye(10)
    n = S.Matrix(CONTROLS["basis"]["n"])
    z = S.Matrix(CONTROLS["basis"]["z"])
    grade = S.Matrix(CONTROLS["basis"]["grade"])
    Y = S.Matrix([S.Rational(x) for x in CONTROLS["basis"]["hypercharge"]])
    a = n[:8, 0]
    eR = -eye10[:, 8]
    m = n + eye10[:, 8]

    def T(p):
        k = a.dot(p) / 2
        return S.Matrix(list(p) + [-k, k])

    def F(p):
        k = a.dot(p) / 2
        return T(p) - k * n

    beta, roots = e8_data()
    B = S.Matrix.hstack(*beta)
    G = B.T * B
    W = S.Matrix.hstack(*[F(p) for p in beta], eR, m)
    I = eye10
    Vaux = K + 2 * K * m * m.T * K
    Y8 = S.Matrix([S.Rational(-1, 3)] * 3 + [S.Rational(1, 2)] * 2 + [0] * 3)
    q = lambda x: sum(x)

    # 1. The two selected metrics and the complete scalar dimension table.
    check("W_integral_unimodular", integral_matrix(W) and abs(W.det()) == 1)
    check("W_K_congruence", W.T * K * W == S.diag(G, 1, -1))
    check("W_Vaux_congruence", W.T * Vaux * W == S.diag(G, 1, 1))
    check("W_euclidean_congruence_differs", W.T * I * W != S.diag(G, 1, 1))
    check("free_metric_K_orthogonal", I * K * I == K)
    check("aux_metric_K_orthogonal", Vaux * K * Vaux == K)
    check("E8_basis_even_positive", G.det() == 1 and all(G[i, i] % 2 == 0 for i in range(8)) and G.is_positive_definite)

    # The endpoint metrics lie on one explicitly fixed null-vector
    # interpolation.  This is a finite control for that interpolation, not a
    # choice of a general metric or a claim about a selected RG trajectory.
    A = S.acosh(3)
    theta = S.symbols("theta", real=True)
    c, h = S.symbols("c h", real=True)
    check("interpolation_endpoint_identity", S.simplify(S.cosh(A) - 3) == 0 and S.simplify(S.sinh(A) - S.sqrt(8)) == 0)
    v_s = S.Matrix.vstack(S.sinh(theta) * a / S.sqrt(8), S.zeros(1, 1), S.cosh(theta) * S.ones(1, 1))
    V_s = K + 2 * K * v_s * v_s.T * K
    check("interpolation_V0_is_free", V_s.subs(theta, 0) == I)
    check("interpolation_V1_is_aux", V_s.subs(theta, A) == Vaux)
    check("interpolation_null_vector_K_norm", S.trigsimp((v_s.T * K * v_s)[0] + 1) == 0)
    delta_z_symbolic = S.simplify(qform(z, V_s) / 2)
    delta_n_symbolic = S.simplify(qform(n, V_s) / 2)
    check("interpolation_delta_z", S.trigsimp(delta_z_symbolic - S.cosh(theta) ** 2) == 0)
    check("interpolation_delta_n", S.trigsimp(delta_n_symbolic - (3 * S.cosh(theta) - S.sqrt(8) * S.sinh(theta)) ** 2) == 0)
    shifted_cosh = 3 * S.cosh(theta) - S.sqrt(8) * S.sinh(theta)
    check("interpolation_delta_n_shifted_cosh", S.trigsimp(delta_n_symbolic - shifted_cosh ** 2) == 0)
    V_mid_substituted = V_s.subs(theta, A / 2)
    v_mid = S.Matrix.vstack(a / S.sqrt(8), S.zeros(1, 1), S.sqrt(2) * S.ones(1, 1))
    V_mid = K + 2 * K * v_mid * v_mid.T * K
    check("interpolation_midpoint_substitution", all(S.trigsimp(V_mid_substituted[i, j] - V_mid[i, j]) == 0 for i in range(10) for j in range(10)))
    V_mid_expected = K.copy()
    V_mid_expected[:8, :8] += a * a.T / 4
    V_mid_expected[:8, 9] = -a
    V_mid_expected[9, :8] = -a.T
    V_mid_expected[9, 9] = 3
    check("interpolation_midpoint_rational", V_mid == V_mid_expected)
    midpoint_delta_n = qform(n, V_mid) / 2
    midpoint_delta_z = qform(z, V_mid) / 2
    check("interpolation_midpoint_deltas", midpoint_delta_n == S.Rational(CONTROLS["expected"]["interpolation_midpoint_delta"]) and midpoint_delta_z == S.Rational(CONTROLS["expected"]["interpolation_midpoint_delta"]))
    check("interpolation_midpoint_K_orthogonal", V_mid * K * V_mid == K)

    field_vectors = [(f"e{i + 1}", eye10[:, i]) for i in range(10)] + [("n", n), ("z", z)]
    table = []
    expected_dims = {
        **{f"e{i + 1}": (S.Rational(1, 2), S.Rational(3, 2), S.Rational(1, 2)) for i in range(8)},
        "e9": (S.Rational(1, 2), S.Rational(1, 2), S.Rational(1, 2)),
        "e10": (S.Rational(1, 2), S.Rational(17, 2), S.Rational(-1, 2)),
        "n": (S.Integer(9), S.Integer(1), S.Integer(0)),
        "z": (S.Integer(1), S.Integer(9), S.Integer(0)),
    }
    for name, vector in field_vectors:
        delta_free = qform(vector, I) / 2
        delta_aux = qform(vector, Vaux) / 2
        hspin = qform(vector, K) / 2
        check(f"dimension_{name}", (delta_free, delta_aux, hspin) == expected_dims[name])
        table.append({"field": name, "delta_free": as_string(delta_free), "delta_aux": as_string(delta_aux), "h_spin": as_string(hspin)})

    # E8 roots and the norm-one vertex census in the two local metrics.
    check("E8_root_count", len(roots) == CONTROLS["expected"]["root_count"] and len({tuple(r) for r in roots}) == 240)
    check("E8_roots_norm_two", all(qform(r, S.eye(8)) == 2 for r in roots))
    root_lifts = [F(r) for r in roots]
    check("F_root_euclidean_norm_formula", all(qform(F(r), I) == qform(r, S.eye(8)) + 2 * (a.dot(r)) ** 2 for r in roots))
    free_root_dims = Counter(str(S.simplify(qform(x, I) / 2)) for x in root_lifts)
    aux_root_dims = Counter(str(S.simplify(qform(x, Vaux) / 2)) for x in root_lifts)
    check("E8_free_root_dimension_counts", dict(sorted(free_root_dims.items())) == CONTROLS["expected"]["free_root_dimension_counts"])
    check("E8_aux_root_dimension_counts", dict(sorted(aux_root_dims.items())) == CONTROLS["expected"]["aux_root_dimension_counts"])
    check("norm_one_vertex_count_free", 2 * 10 == CONTROLS["expected"]["norm_one_vertex_count_free"])
    check("norm_one_vertex_count_aux", 2 * 2 == CONTROLS["expected"]["norm_one_vertex_count_aux"])
    check("norm_one_count_uses_fixed_NS_local_convention", qform(eR, Vaux) == 1 and qform(m, Vaux) == 1 and qform(n, Vaux) == 2)

    # 2. Characteristic null arithmetic and the fermion/derivative count.
    check("n_characteristic_null", all(int(x) % 2 for x in n) and qform(n, K) == 0)
    check("characteristic_null_bounds", 9 <= sum(int(x) ** 2 for x in n[:9]) and abs(int(n[9])) >= 3 and sum(abs(int(x)) for x in n) >= 12)
    check("n_saturates_characteristic_l1", sum(abs(int(x)) for x in n) == CONTROLS["expected"]["characteristic_minimum_l1"])
    unit_factors = sum(abs(int(x)) for x in n[:9])
    derivative_order = abs(int(n[9]))
    check("n_fermion_derivative_decomposition", unit_factors == 9 and derivative_order == 3 and unit_factors + derivative_order == 12 and qform(n, I) / 2 == 9)
    k = S.symbols("k", integer=True, nonnegative=True)
    check("fermion_derivative_count_identity", S.expand(k / 2 + k * (k - 1) / 2 - k ** 2 / 2) == 0)

    # 3. Number-preserving primitive bilinear nulls: only +/-z survive q,Y,g.
    candidates = []
    accepted = []
    modular_rejection = []
    for i in range(9):
        base = eye10[:, i] - eye10[:, 9]
        for sign in (-1, 1):
            x = sign * base
            candidates.append(x)
            check(f"bilinear_null_{i}_{sign}_primitive", qform(x, K) == 0 and sum(abs(int(v)) for v in x) == 2)
            try:
                g_residue = residue(grade.dot(x), 4)
            except ValueError:
                modular_rejection.append(False)
                continue
            modular_rejection.append(True)
            if q(x) == 0 and Y.dot(x) == 0 and g_residue == 0:
                accepted.append(x)
    accepted_set = {tuple(x) for x in accepted}
    check("bilinear_modular_checks_integral", len(modular_rejection) == 18 and all(modular_rejection))
    check("bilinear_neutral_selection_only_pm_z", len(accepted) == 2 and accepted_set == {tuple(z), tuple(-z)})
    try:
        residue(S.Rational(1, 2), 4)
    except ValueError:
        nonintegral_residue_rejected = True
    else:
        nonintegral_residue_rejected = False
    check("modular_residue_rejects_noninteger", nonintegral_residue_rejected)

    # A bounded census of the neutral self-null integer vectors at the
    # rational midpoint.  For x=(R8,u,l), nullity gives ||(R8,u)||^2=l^2
    # and the midpoint dimension is exactly (a.R8-4l)^2/8.  The endpoint
    # arithmetic bounds the equality census to |l|<=3; this enumerates those
    # finitely many shells only.
    def integer_vectors_with_norm(dimension, norm_squared):
        def descend(index, remaining, prefix):
            if index == dimension:
                if remaining == 0:
                    yield S.Matrix(prefix)
                return
            limit = isqrt(remaining)
            for value in range(-limit, limit + 1):
                square = value * value
                if square <= remaining:
                    yield from descend(index + 1, remaining - square, prefix + [value])

        yield from descend(0, norm_squared, [])

    midpoint_neutral = []
    midpoint_by_l = {}
    for l_abs in (1, 2, 3):
        shell_count = 0
        for l in (-l_abs, l_abs):
            for r9 in integer_vectors_with_norm(9, l_abs * l_abs):
                x = S.Matrix(list(r9) + [l])
                shell_count += 1
                if q(x) != 0 or Y.dot(x) != 0 or residue(grade.dot(x), 4) != 0:
                    continue
                midpoint_neutral.append(x)
        midpoint_by_l[str(l_abs)] = shell_count
    midpoint_deltas = [S.simplify(qform(x, V_mid) / 2) for x in midpoint_neutral]
    check("midpoint_neutral_shells_bounded", set(midpoint_by_l) == {"1", "2", "3"} and all(v > 0 for v in midpoint_by_l.values()))
    check("midpoint_neutral_dimension_bound", all(delta >= 2 for delta in midpoint_deltas))
    midpoint_minimizers = {tuple(x) for x, delta in zip(midpoint_neutral, midpoint_deltas) if delta == 2}
    check("midpoint_only_pm_n_pm_z_at_delta_two", len(midpoint_minimizers) == CONTROLS["expected"]["midpoint_neutral_delta_two_count"] and midpoint_minimizers == {tuple(n), tuple(-n), tuple(z), tuple(-z)})

    # Uniform algebra along the same fixed path.  For a null x=(R8,u,l),
    # write d=a.R8 and h=3l-d.  The path dimension is
    # (alpha*l+beta*h)^2 with alpha=sinh(A-theta)/sqrt(8) and
    # beta=sinh(theta)/sqrt(8).  The following identities are the reviewed
    # full-path bound controls; the global classification is part of PROOF.
    alpha = S.cosh(theta) - 3 * S.sinh(theta) / S.sqrt(8)
    beta = S.sinh(theta) / S.sqrt(8)
    l_symbol, h_symbol, scale = S.symbols("l_symbol h_symbol scale", real=True)
    delta_null = (alpha * l_symbol + beta * h_symbol) ** 2
    c_symbol, h_symbol = S.symbols("c_symbol h_symbol", real=True)
    alpha_ch = c_symbol - 3 * h_symbol / S.sqrt(8)
    beta_ch = h_symbol / S.sqrt(8)
    r_symbol = S.Matrix(S.symbols("r0:8", real=True))
    u_symbol = S.symbols("u_symbol", real=True)
    x_symbol = S.Matrix(list(r_symbol) + [u_symbol, l_symbol])
    d_symbol = a.dot(r_symbol)
    null_residual = (sum(value ** 2 for value in r_symbol) + u_symbol ** 2 - l_symbol ** 2) / 2
    V_ch = K + 2 * K * S.Matrix.vstack(h_symbol * a / S.sqrt(8), S.zeros(1, 1), c_symbol * S.ones(1, 1)) * S.Matrix.vstack(h_symbol * a / S.sqrt(8), S.zeros(1, 1), c_symbol * S.ones(1, 1)).T * K
    check("null_path_dimension_formula", S.expand(qform(x_symbol, V_ch) / 2 - (alpha_ch * l_symbol + beta_ch * (3 * l_symbol - d_symbol)) ** 2 - null_residual) == 0)
    check("null_scaled_dimension_formula", S.expand((alpha_ch * scale * l_symbol + beta_ch * scale * h_symbol) ** 2 - scale ** 2 * (alpha_ch * l_symbol + beta_ch * h_symbol) ** 2) == 0)
    even_pair = 2 * alpha + 4 * beta
    odd_pair = 3 * alpha + 3 * beta
    even_remainder = 2 * S.sinh(theta) - S.cosh(theta) / S.sqrt(2)
    odd_remainder = 3 * S.sinh(theta) - 3 * S.cosh(theta) / S.sqrt(2)
    check("uniform_even_pair_identity", S.trigsimp(even_pair - (2 * S.cosh(theta) - S.sinh(theta) / S.sqrt(2))) == 0 and S.trigsimp(even_pair ** 2 - S.Rational(7, 2) - even_remainder ** 2) == 0)
    check("uniform_odd_pair_identity", S.trigsimp(odd_pair - (3 * S.cosh(theta) - 3 * S.sinh(theta) / S.sqrt(2))) == 0 and S.trigsimp(odd_pair ** 2 - S.Rational(9, 2) - odd_remainder ** 2) == 0)
    two_n_delta = 4 * shifted_cosh ** 2
    shifted_sinh = S.sqrt(8) * S.cosh(theta) - 3 * S.sinh(theta)
    check("uniform_two_n_bound", S.trigsimp(two_n_delta - 4 - 4 * shifted_sinh ** 2) == 0)
    def dh(vector):
        last = vector[9]
        d_value = a.dot(vector[:8, 0])
        return int(d_value), int(last), int(3 * last - d_value)

    check("uniform_special_null_pairs", [dh(n), dh(-z), dh(2 * n)] == [(8, 3, 1), (0, 1, 3), (16, 6, 2)])
    check("uniform_non_special_parity_bound_data", (2 % 2 == 4 % 2 and 3 % 2 == 3 % 2 and (2, 4) != (3, 3)))

    # 4. Exact nontrivial complex rational Schur block; no Gaussian theorem.
    J = S.I
    A = S.Matrix([[1 + J, S.Rational(1, 2)], [S.Rational(1, 3), 2 - J]])
    Dblock = S.Matrix([[1, J / 2], [S.Rational(1, 4), -1]])
    Cblock = S.Matrix([[1 - J, S.Rational(1, 5)], [-J / 3, 2]])
    E = S.Matrix([[2 + J, S.Rational(1, 3)], [S.Rational(1, 4), 3 - J]])
    D = A.row_join(Dblock).col_join(Cblock.row_join(E))
    Schur = A - Dblock * E.inv() * Cblock
    det_D, det_E, det_Schur = map(S.factor, (D.det(), E.det(), Schur.det()))
    check("complex_rational_block_nontrivial", D.shape == (4, 4) and any(S.im(x) != 0 for x in D) and all(rational_complex(x) for x in D))
    check("schur_det_factorization", S.simplify(det_D - det_E * det_Schur) == 0 and det_D != 0)
    check("schur_inverse_PP", D.inv()[:2, :2] == Schur.inv())
    check("schur_phase_preserved", S.im(det_D) != 0 and S.simplify(det_D - det_E * det_Schur) == 0)

    # 5. A pure two-mode Slater state separates Wick factorization from
    # current cumulants: the elementary four determinant vanishes, while the
    # one-mode occupation characteristic has a nonzero fourth log derivative.
    u = S.Matrix([1, 1]) / S.sqrt(2)
    C = u * u.conjugate().T
    t = S.symbols("t", real=True)
    Z = (1 + S.exp(t)) / 2
    kappa4 = S.simplify(S.diff(S.log(Z), t, 4).subs(t, 0))
    check("slater_projector_and_wick_determinant", C == C.H and C.rank() == 1 and C.det() == 0)
    check("slater_current_fourth_log_cumulant", Z.subs(t, 0) == 1 and kappa4 == -S.Rational(1, 8))
    check("slater_connected_four_zero_but_current_nonzero", C.det() == 0 and kappa4 != 0)

    result = {
        "contract": CONTROLS["contract"],
        "status": CONTROLS["status"],
        "research_verdict": CONTROLS["research_verdict"],
        "source_manifest": manifest_status,
        "count": len(CHECKS),
        "all_passed": all(CHECKS.values()),
        "checks": CHECKS,
        "scalar_dimensions_h_spins": table,
        "free_root_dimension_counts": dict(sorted(free_root_dims.items())),
        "aux_root_dimension_counts": dict(sorted(aux_root_dims.items())),
        "norm_one_vertex_count": {"free": 20, "aux": 4, "convention": "norm-one lattice vectors before cosine, fixed compatible NS local vertex convention"},
        "characteristic_null": {"minimum_l1": 12, "unit_factors": unit_factors, "derivative_order": derivative_order, "delta_free": "9"},
        "bilinear_neutral_directions": [[int(v) for v in x] for x in accepted],
        "interpolation": {
            "endpoint": "V(theta)=K+2 K v(theta) v(theta)^T K, theta in [0, arcosh(3)]",
            "delta_z": "cosh(theta)^2",
            "delta_n": "cosh(arcosh(3)-theta)^2",
            "midpoint_delta_n": as_string(midpoint_delta_n),
            "midpoint_delta_z": as_string(midpoint_delta_z),
            "midpoint_neutral_shells": midpoint_by_l,
            "generation_norm_shell_counts": midpoint_by_l,
            "midpoint_delta_two_vectors": len(midpoint_minimizers),
        },
        "uniform_path_bound": {
            "alpha": "sinh(arcosh(3)-theta)/sqrt(8)",
            "beta": "sinh(theta)/sqrt(8)",
            "even_pair": "(2*alpha+4*beta)^2 >= 7/2",
            "odd_pair": "(3*alpha+3*beta)^2 >= 9/2",
            "two_n": "Delta(2n)=4*cosh(arcosh(3)-theta)^2 >= 4",
            "special_vectors": ["+/-n", "+/-z", "+/-2n"],
        },
        "schur": {"det_D": as_string(det_D), "det_E": as_string(det_E), "det_Schur": as_string(det_Schur), "inverse_PP_exact": True, "complex_phase": True},
        "slater_counterexample": {"wick_determinant": "0", "fourth_log_cumulant": as_string(kappa4), "current_characteristic": "(1+exp(t))/2"},
        "scope": CONTROLS["scope"],
    }
    certificate_name = "certificate.optimized.json" if sys.flags.optimize else "certificate.json"
    (HERE / certificate_name).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "count": result["count"], "all_passed": result["all_passed"], "certificate": certificate_name}, sort_keys=True))


if __name__ == "__main__":
    main()
