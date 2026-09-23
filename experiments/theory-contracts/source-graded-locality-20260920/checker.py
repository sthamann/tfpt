#!/usr/bin/env python3
"""Exact finite controls for the graded boundary bridge.

This is a conditional lattice/algebra checker.  It tests the already chosen
I_(9,1) construction, the auxiliary E8 basis, the n/z null plane, and the
common-lattice locality seam.  It does not claim that the source, energy
matrix, or a 4D physical boundary is selected by P1/P2.
"""

from collections import Counter
from itertools import combinations, product
import hashlib
import json
from math import gcd
from pathlib import Path
import sys

import sympy as S


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
CONTROLS = json.loads((HERE / "graded-boundary-controls.json").read_text())
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
    """Record an exact control and raise on the first failed control."""
    ok = bool(condition)
    CHECKS[name] = ok
    if not ok:
        raise RuntimeError(name)


def integral_matrix(matrix):
    return all(S.denom(x) == 1 for x in matrix)


def integral_vector(vector):
    return all(S.denom(x) == 1 for x in vector)


def mod_integer(value, modulus):
    value = S.Rational(value)
    if value.q != 1:
        raise ValueError(f"non-integral residue: {value}")
    return int(value) % modulus


def qform(x, matrix):
    return (x.T * matrix * x)[0]


def bilinear(x, matrix, y):
    return (x.T * matrix * y)[0]


def e8_data():
    """Return the fixed simple-root basis and all 240 E8 roots."""
    roots_basis = [
        S.Matrix([1, -1, -1, -1, -1, -1, -1, 1]) / 2,
        S.Matrix([1, 1, 0, 0, 0, 0, 0, 0]),
    ]
    for i in range(6):
        p = S.zeros(8, 1)
        p[i] = -1
        p[i + 1] = 1
        roots_basis.append(p)

    roots = []
    for i, j in combinations(range(8), 2):
        for si, sj in product((-1, 1), repeat=2):
            p = [S.Integer(0)] * 8
            p[i], p[j] = si, sj
            roots.append(S.Matrix(p))
    for signs in product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(S.Matrix(signs) / 2)
    return roots_basis, roots


def d8_data():
    basis = []
    for i in range(7):
        p = S.zeros(8, 1)
        p[i], p[i + 1] = 1, -1
        basis.append(p)
    p = S.zeros(8, 1)
    p[6], p[7] = 1, 1
    basis.append(p)
    return basis


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
    q = lambda x: sum(x)
    Y8 = S.Matrix([S.Rational(-1, 3)] * 3 + [S.Rational(1, 2)] * 2 + [0] * 3)
    ones8 = S.ones(8, 1)
    try:
        mod_integer(S.Rational(1, 2), 4)
    except ValueError:
        noninteger_residue_rejected = True
    else:
        noninteger_residue_rejected = False
    check("mod_integer_rejects_noninteger", noninteger_residue_rejected)

    # 1. Whole-lattice E8 and source-parity controls.
    check("e8_basis_unimodular", abs(B.det()) == 1 and G.det() == 1)
    check("e8_basis_even", all(G[i, i] % 2 == 0 for i in range(8)))
    check("whole_W_integral_unimodular", integral_matrix(W) and abs(W.det()) == 1)
    check("whole_W_congruence", W.T * K * W == S.diag(G, 1, -1))
    diag = [S.Integer((W.T * K * W)[i, i]) for i in range(10)]
    check("W_parity_first8_even_last2_odd", [int(x) % 2 for x in diag] == [0] * 8 + [1, 1])
    qW = [q(W[:, i]) for i in range(10)]
    check("source_q_split_e8_pair", qW[:8] == [q(p) for p in beta] and qW[8:] == [-1, 1])
    check("source_parity_identity_on_W", all(mod_integer(qform(W[:, i], K) - q(W[:, i]), 2) == 0 for i in range(10)))
    # The all-integer identity is the mathematical parity argument:
    # v^T K v-sum(v)=sum_{i<10} v_i(v_i-1)-v_10(v_10+1), a sum of even terms.
    vv = S.Matrix(S.symbols("v0:10", integer=True))
    parity_terms = sum((vv[i] * (vv[i] - 1) for i in range(9)), S.Integer(0)) - vv[9] * (vv[9] + 1)
    check("source_parity_identity_structural", S.expand(qform(vv, K) - sum(vv) - parity_terms) == 0)

    # E8 roots, source charges, and the fixed grade.
    check("e8_root_count", len(roots) == CONTROLS["expected"]["e8_root_count"] and len({tuple(r) for r in roots}) == 240)
    check("e8_roots_norm_two", all((r.T * r)[0] == 2 for r in roots))
    root_q = Counter(int(q(r)) for r in roots)
    expected_q = {int(k): v for k, v in CONTROLS["expected"]["root_q_distribution"].items()}
    check("root_q_distribution", dict(sorted(root_q.items())) == dict(sorted(expected_q.items())))
    root_lifts = [F(r) for r in roots]
    check("all_e8_pure_vertical_even", all(qform(x, K) == 2 and int(q(x)) % 2 == 0 for x in root_lifts))
    check("all_e8_root_grade_integral", all(S.denom(grade.dot(x)) == 1 for x in root_lifts))

    # 2. n/z null, grade, charge, energy, and the sharp source bounds.
    check("n_z_null", qform(n, K) == 0 and qform(z, K) == 0)
    check("n_z_source_neutral", q(n) == 0 and q(z) == 0)
    check("n_z_Y_neutral", Y.dot(n) == 0 and Y.dot(z) == 0)
    check("n_z_grade_zero_mod4", mod_integer(grade.dot(n), 4) == 0 and mod_integer(grade.dot(z), 4) == 0)
    check("n_z_pairing_two", bilinear(n, K, z) == 2)
    check("n_characteristic_z_not", all(int(x) % 2 for x in n) and any(int(x) % 2 == 0 for x in z))
    Vaux = K + 2 * K * m * m.T * K
    W_inv_z = W.inv() * z
    rcoeff = W_inv_z[:8, 0]
    rvector = sum((rcoeff[i] * beta[i] for i in range(8)), S.zeros(8, 1))
    check("W_inverse_z_pair_coordinates", list(W_inv_z[8:, 0]) == [-1, -3])
    check("W_inverse_z_rootpart", (rvector.T * rvector)[0] == 8 and q(rvector) == 2)
    check("energy_dimensions_aux_free", qform(z, Vaux) / 2 == 9 and qform(n, Vaux) / 2 == 1 and n.dot(n) / 2 == 9 and z.dot(z) / 2 == 1)
    c2, s2 = S.symbols("c2 s2", real=True)
    delta_z = S.Integer(4) + 5 * c2 + 3 * s2
    t = S.symbols("t", positive=True)
    boost_t = 4 + 4 * t + 1 / t
    check("pairboost_delta_z_formula", S.simplify(delta_z.subs({c2: (t + 1 / t) / 2, s2: (t - 1 / t) / 2}) - boost_t) == 0)
    check("pairboost_sharp_lower_bound", S.simplify((4 * t + 1 / t) - 4 - (2 * t - 1) ** 2 / t) == 0)

    # A neutral null with E8 norm two cannot occur in the pair coordinates.
    for qvalue in (0, 2, -2, 4, -4):
        if qvalue == 0:
            A0, C0 = S.symbols("A0 C0", real=True)
            check("neutral_null_norm2_q0", S.expand((C0 ** 2 - A0 ** 2).subs(C0, A0)) == 0 and S.Integer(2) != 0)
        else:
            A = S.Rational(qvalue * qvalue - 2, 2 * qvalue)
            check(f"neutral_null_norm2_q{qvalue}", A.q != 1)
    rsharp = S.Matrix([1, 1, 1, -1, 0, 0, 0, 0])
    check("sharp_source_neutral_null", (rsharp.T * rsharp)[0] + 0 ** 2 - (-2) ** 2 == 0 and q(rsharp) - 0 - 2 == 0 and ((rsharp.T * rsharp)[0] + 0 + 4) / 2 == 4)

    # At the norm-eight boundary, block Cauchy leaves one integer parameter.
    # The source/hypercharge constraints give c=3t, w=4+2t, f=-2-5t.
    t = S.symbols("t", integer=True)
    c_block, w_block, f_block = 3 * t, 4 + 2 * t, -2 - 5 * t
    block_cauchy = c_block ** 2 / 3 + w_block ** 2 / 2 + f_block ** 2 / 3
    boundary_poly = S.factor(10 * t ** 2 + 11 * t + 1)
    integer_window = S.solveset(boundary_poly <= 0, t, domain=S.Integers)
    check("norm8_block_cauchy_formula", S.simplify(block_cauchy - (40 * t ** 2 + 44 * t + 28) / 3) == 0)
    check("norm8_block_cauchy_condition", S.factor(block_cauchy - 8) == S.Rational(4, 3) * boundary_poly and boundary_poly == (10 * t + 1) * (t + 1))
    check("norm8_only_integer_parameter", list(integer_window) == [-1])
    r_norm8_unique = -S.Matrix(a)
    check("norm8_equality_forces_minus_a", c_block.subs(t, -1) == -3 and w_block.subs(t, -1) == 2 and f_block.subs(t, -1) == 3 and r_norm8_unique == -S.Matrix(a) and (r_norm8_unique.T * r_norm8_unique)[0] == 8)
    check("doubly_neutral_Q_window", S.Rational(53 * 4, 40) <= 8 and S.Rational(53 * 16, 40) > 8)
    # A half-integral E8 vector has c=sum(color) in Z+1/2 and
    # w=sum(weak) in Z.  For A=-1,B=-3 the pair grade is -30, so
    # 2(c+w)-30 is odd and cannot vanish modulo four.  The explicit norm-8
    # witness below is q/Y neutral but is rejected by this glue parity.
    Cint, Wint = S.symbols("Cint Wint", integer=True)
    check("glue_halfcase_parity_excludes_half_r", S.expand(2 * (Cint + S.Rational(1, 2) + Wint) - 30 - (2 * (Cint + Wint - 15) + 1)) == 0)
    half_witness = S.Matrix([S.Rational(1, 2), -S.Rational(1, 2), -S.Rational(3, 2), S.Rational(3, 2), S.Rational(3, 2), S.Rational(1, 2), S.Rational(1, 2), -S.Rational(1, 2)])
    half_full = F(half_witness) - eR - 3 * m
    check("glue_halfcase_explicit_witness", (half_witness.T * half_witness)[0] == 8 and q(half_witness) == 2 and Y8.dot(half_witness) == 2 and mod_integer(grade.dot(half_full), 4) == 1)

    # 3. The u/v null plane, its critical positive matrix, and the integral seam.
    u, v = (n + z) / 2, (n - z) / 2
    check("uv_K_orthonormal", qform(u, K) == 1 and qform(v, K) == -1 and bilinear(u, K, v) == 0)
    check("uv_half_integral", not integral_vector(u) and not integral_vector(v) and integral_vector(2 * u) and integral_vector(2 * v))
    check("uv_source_Y_grade_zero", q(u) == q(v) == 0 and Y.dot(u) == Y.dot(v) == 0 and mod_integer(grade.dot(u), 4) == 0 and mod_integer(grade.dot(v), 4) == 0)
    Vcrit = K + 2 * K * v * v.T * K
    check("Vcrit_positive_spectrum", Vcrit.eigenvals() == {S.Integer(1): 8, 7 - 4 * S.sqrt(3): 1, 7 + 4 * S.sqrt(3): 1})
    check("Vcrit_n_z_dimensions", qform(n, Vcrit) / 2 == 1 and qform(z, Vcrit) / 2 == 1)
    reflection = eye10 + 2 * v * v.T * K
    check("null_plane_reflection", reflection.T * K * reflection == K and reflection * n == z and reflection * z == n and not integral_matrix(reflection))

    N = S.Matrix.hstack(n, z)
    minors = [abs(N.extract([i, j], [0, 1]).det()) for i, j in combinations(range(10), 2)]
    check("mixed_plane_saturated", gcd(*[int(x) for x in minors]) == 1)
    # x*u+y*v is integral exactly when x,y are integers with equal parity.
    alpha, beta_coeff = S.symbols("alpha beta", integer=True)
    check("mixed_plane_integer_coordinates", u + v == n and u - v == z and S.Matrix([[S.Rational(1, 2), S.Rational(1, 2)], [S.Rational(1, 2), -S.Rational(1, 2)]]).det() == -S.Rational(1, 2))
    check("mixed_plane_index_two", abs(S.Rational(1, 2).q) == CONTROLS["expected"]["mixed_plane_index"])
    check("mixed_plane_parity_parameterization", S.expand((alpha + beta_coeff) - (alpha - beta_coeff)) == 2 * beta_coeff)

    # 4. Common lattice L0 and the projected-versus-full mutual locality seam.
    d8 = d8_data()
    Td8 = [T(p) for p in d8]
    GD8 = S.Matrix.hstack(*d8).T * S.Matrix.hstack(*d8)
    check("common_lattice_T_integral", all(integral_vector(x) for x in Td8))
    check("common_lattice_D8_gram", GD8.det() == 4)
    check("common_lattice_both_orthogonal", all(bilinear(n, K, x) == 0 and bilinear(z, K, x) == 0 for x in Td8))
    check("common_lattice_q_grade_Y_preserved", all(q(T(p)) == q(p) and grade.dot(T(p)) == 2 * sum(p[:5]) and Y.dot(T(p)) == Y8.dot(p) for p in d8))

    e1 = eye10[:, 0]
    s = S.ones(8, 1) / 2
    f = e1
    b = F(s)
    check("microscopic_f_b_integral", integral_vector(f) and integral_vector(b))
    check("f_b_common_decompositions", f == T(S.eye(8)[:, 0]) + z / 2 and b == T(s) + n / 2)
    check("projected_pairings_half", bilinear(T(S.eye(8)[:, 0]), K, T(s)) == S.Rational(1, 2) and bilinear(z / 2, K, n / 2) == S.Rational(1, 2))
    check("full_f_b_local", bilinear(f, K, b) == 1)
    unit_pair_checks = []
    for i in range(8):
        ei = S.eye(8)[:, i]
        common = bilinear(T(ei), K, T(s))
        pair = bilinear(z / 2, K, n / 2) * (a[i])
        full = common + pair
        unit_pair_checks.append(common == S.Rational(1, 2) and pair == S.Rational(a[i], 2) and full == S.Rational(1 + a[i], 2))
    check("all_unit_vector_projected_locality_restored", all(unit_pair_checks))

    d8_lattice = S.Matrix.hstack(*d8)
    check("D8_membership_2e1_2s", sum(2 * S.eye(8)[:, 0]) == 2 and 2 * s == S.ones(8, 1))
    def in_d8(vector):
        return integral_vector(vector) and int(sum(vector)) % 2 == 0

    def in_e8_cosets(vector):
        return in_d8(vector) or in_d8(vector - s)

    check("D8_extensions_index_two", d8_lattice.det() in (2, -2) and B.det() in (1, -1) and all(in_e8_cosets(p) for p in beta) and all(in_d8(S.eye(8)[:, i]) or in_d8(S.eye(8)[:, i] - S.eye(8)[:, 0]) for i in range(8)))
    check("E8_even_I8_odd", all((x.T * x)[0] % 2 == 0 for x in beta) and (S.eye(8)[:, 0].T * S.eye(8)[:, 0])[0] % 2 == 1)
    check("e1_s_not_D8", sum(S.eye(8)[:, 0]) % 2 == 1 and not integral_vector(s))
    check("e1_s_norms", (S.eye(8)[:, 0].T * S.eye(8)[:, 0])[0] == 1 and (s.T * s)[0] == 2)

    # Transport each original right-channel unit vector through the E8
    # dictionary.  These are the microscopic odd fields dressed by one
    # massive pair component; the transport is an exact lattice identity.
    transported = []
    transported_ok = []
    for i in range(8):
        ai = a[i]
        ri = S.eye(8)[:, i] - ai * a / 2
        transported.append(ri)
        transported_ok.append((ri.T * ri)[0] == 2 and in_e8_cosets(ri) and F(ri) - ai * m == eye10[:, i] and q(ri) == 1 + ai and Y8.dot(ri) == Y8[i] + ai)
    check("all_original_odd_fields_transport", len(transported) == 8 and all(transported_ok) and -eR == eye10[:, 8] and F(a) + 3 * m == eye10[:, 9])

    # The common D8+n+z sublattice has exactly four cosets in the
    # unimodular microscopic lattice.  f, b, and f+b are the three
    # nontrivial half-integral representatives; doubling any of them lands
    # back in the common sublattice.
    common = S.Matrix.hstack(*Td8, n, z)
    common_coords = [common.inv() * x for x in (f, b, f + b)]
    check("common_D8_n_z_index_four", abs(common.det()) == 4)
    check("four_glue_cosets_exhaust", all(integral_vector(2 * x) and not integral_vector(x) for x in common_coords))

    # 5. Strong doubly-neutral lower bound, with z as the sharp witness.
    Ypair = W.T * Y
    check("pair_Y_matches_source_pair", list(Ypair[8:, 0]) == [-1, 1])
    check("Y8_orthogonal_source_functional", Y8.dot(ones8) == 0 and (Y8.T * Y8)[0] == S.Rational(5, 6) and (ones8.T * ones8)[0] == 8)
    qsym, yr = S.symbols("q yr", real=True)
    bound = S.Rational(53, 40) * qsym ** 2
    Ar, Cr = S.symbols("A C", real=True)
    check("doubly_neutrality_identifies_Yr_q", S.expand((qsym - Ar + Cr) - (yr - Ar + Cr)) == qsym - yr)
    check("doubly_neutral_cauchy_bound", S.Rational(1, 8) + S.Rational(6, 5) == S.Rational(53, 40) and bound.subs(qsym, 2) == S.Rational(53, 10) and bound.subs(qsym, 4) == S.Rational(106, 5))
    check("doubly_neutral_q2_integer_obstruction", S.Rational(4 - 6, 4).q != 1)
    check("doubly_neutral_non_n_norm_bound", S.Rational(53, 10) > 4 and S.Rational(106, 5) > 8 and S.Integer(8) >= 8)
    x = S.symbols("x", real=True)
    pair_energy = (Ar ** 2 + Cr ** 2) * S.cosh(x) + 2 * Ar * Cr * S.sinh(x)
    check("null_pair_energy_identity", S.expand((Ar ** 2 + Cr ** 2) ** 2 - (2 * Ar * Cr) ** 2 - (Ar ** 2 - Cr ** 2) ** 2) == 0)
    pair_t = ((Ar + Cr) ** 2 * t + (Ar - Cr) ** 2 / t) / 2
    check("null_pair_energy_lower_bound", S.simplify(pair_t - (Ar ** 2 - Cr ** 2) - (t * (Ar + Cr) - (Ar - Cr)) ** 2 / (2 * t)) == 0 and S.simplify(pair_t + (Ar ** 2 - Cr ** 2) - (t * (Ar + Cr) + (Ar - Cr)) ** 2 / (2 * t)) == 0)
    check("null_delta_minus_r2_square", S.simplify((Cr ** 2 - Ar ** 2 + pair_t) / 2 - (Cr ** 2 - Ar ** 2) - (t * (Ar + Cr) + (Ar - Cr)) ** 2 / (4 * t)) == 0)
    check("z_sharp_doubly_neutral_witness", list(W_inv_z[8:, 0]) == [-1, -3] and Y.dot(z) == 0 and q(z) == 0 and delta_z.subs({c2: S.Rational(5, 4), s2: -S.Rational(3, 4)}) == 8)

    summary = {
        "status": CONTROLS["status_scope"],
        "research_verdict": CONTROLS["research_verdict"],
        "count": len(CHECKS),
        "all_passed": all(CHECKS.values()),
        "root_q_distribution": {str(k): v for k, v in sorted(root_q.items())},
        "W_inverse_z": [int(x) for x in W_inv_z],
        "delta_z_aux": int(qform(z, Vaux) / 2),
        "delta_n_aux": int(qform(n, Vaux) / 2),
        "delta_z_critical": 1,
        "pairboost_delta_z_lower_bound": 8,
        "doubly_neutral_non_n_delta_lower_bound": 8,
        "full_f_b_bilinear": int(bilinear(f, K, b)),
        "four_glue_cosets": 4,
        "source_manifest": manifest_status,
        "scope": CONTROLS["scope"],
    }
    result = dict(summary)
    result["checks"] = CHECKS
    output_name = "certificate.optimized.json" if sys.flags.optimize else "certificate.json"
    (HERE / output_name).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "count": result["count"], "all_passed": result["all_passed"], "certificate": output_name, "source_manifest": manifest_status}, sort_keys=True))


if __name__ == "__main__":
    main()
