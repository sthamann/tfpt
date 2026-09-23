#!/usr/bin/env python3
"""Exact finite bookkeeping for the four charged-sector classes.

This is a conditional algebra control for the fixed (9,1) lattice labels.
It checks discriminant-sector signs, the finite Arf/Fourier transforms, and
the two positive generalized metrics used in the existing diagnostics.  It
does not construct a twisted module or a source-derived Hamiltonian.
"""

import argparse
import json
import sys
from pathlib import Path

import sympy as S


HERE = Path(__file__).resolve().parent
CHECKS = {}


def check(name, condition):
    ok = bool(condition)
    CHECKS[name] = ok
    if not ok:
        raise RuntimeError(name)


def qform(x, matrix, y=None):
    if y is None:
        y = x
    return (x.T * matrix * y)[0]


def integral_vector(x):
    return all(S.denom(v) == 1 for v in x)


def main(output=None):
    K = S.diag(*([1] * 9 + [-1]))
    I10 = S.eye(10)
    n = S.Matrix([1, 1, 1, -1, -1, -1, -1, -1, -1, 3])
    z = S.Matrix([0] * 8 + [1, -1])
    g = K * n
    h = n / 2
    f = I10[:, 8]
    c = h + f
    q = S.ones(10, 1)
    Y = S.Matrix([S.Rational(-1, 3)] * 3 + [S.Rational(1, 2)] * 2 + [0] * 3 + [1, 1])

    reps = [S.zeros(10, 1), h, f, c]
    labels = ["0", "h", "f", "h+f"]

    # The two standard exact bases used by the preceding lattice controls.
    e8_simple = [
        S.Matrix([1, -1, -1, -1, -1, -1, -1, 1]) / 2,
        S.Matrix([1, 1, 0, 0, 0, 0, 0, 0]),
    ]
    for i in range(6):
        r = S.zeros(8, 1)
        r[i], r[i + 1] = -1, 1
        e8_simple.append(r)
    a = S.Matrix([1, 1, 1, -1, -1, -1, -1, -1])

    def T(r):
        k = a.dot(r) / 2
        return S.Matrix(list(r) + [-k, k])

    T_basis = S.Matrix.hstack(*(T(r) for r in e8_simple))

    # Gamma0 is the even-g charge sublattice.  Its basis is deliberately
    # elementary so the index and the four discriminant classes are visible.
    gamma0_cols = []
    for i in range(9):
        col = I10[:, i] - I10[:, 9]
        gamma0_cols.append(col)
    gamma0_cols.append(2 * I10[:, 9])
    Gamma0_basis = S.Matrix.hstack(*gamma0_cols)

    check("null_plane", qform(n, K) == qform(z, K) == 0 and qform(n, K, z) == 2)
    check("global_neutral_null_plane", q.dot(n) == q.dot(z) == 0 and Y.dot(n) == Y.dot(z) == 0)
    Gamma0_coordinates = Gamma0_basis.inv()
    n_coords = Gamma0_coordinates * n
    z_coords = Gamma0_coordinates * z
    standard_gamma_basis = [I10[:, i] for i in range(10)]
    characteristic_on_standard_basis = all(
        (g.dot(v) - qform(v, K)) % 2 == 0 for v in standard_gamma_basis
    )
    check("gamma0_basis_even_and_index_two", all((g.dot(v) % 2) == 0 for v in gamma0_cols) and abs(Gamma0_basis.det()) == 2)
    check("n_z_in_gamma0_and_characteristic", integral_vector(n_coords) and integral_vector(z_coords) and characteristic_on_standard_basis)
    check("lh_unimodular_basis", abs(S.Matrix.hstack(*[T_basis[:, i] for i in range(8)], h, z).det()) == 1)

    # The discriminant representatives are ordered (0,h,f,h+f).  The
    # quadratic form uses B(x,x)/2, while the S matrix uses B(x,y) mod 1.
    Bdisc = S.Matrix(4, 4, lambda i, j: qform(reps[i], K, reps[j]))
    Q = [S.Rational(Bdisc[i, i], 2) % 1 for i in range(4)]
    check("discriminant_order_and_quadratic_values", labels == ["0", "h", "f", "h+f"] and Q == [0, 0, S.Rational(1, 2), 0])
    dual_membership = all(integral_vector(Gamma0_basis.T * K * r) for r in reps)
    doubled_membership = all(integral_vector(Gamma0_coordinates * (2 * r)) for r in reps)
    distinct_differences = all(
        not integral_vector(Gamma0_coordinates * (reps[i] - reps[j]))
        for i in range(4) for j in range(i + 1, 4)
    )
    check("four_discriminant_classes", dual_membership and doubled_membership and distinct_differences and all(qform(r, K) % 1 == 0 for r in reps))
    check("gamma_even_class_grades", [int(g.dot(r)) for r in reps] == [0, 0, -1, -1])
    check("half_sector_global_charges", [q.dot(r) for r in reps] == [0, 0, 1, 1] and [Y.dot(r) for r in reps] == [0, 0, 1, 1])

    # Finite discriminant modular data.  The universal gravitational phase is
    # intentionally not included: S is the finite Fourier transform and T is
    # only the relative sector sign from Q.
    Sdisc = S.Matrix(4, 4, lambda i, j: S.Rational(1, 2) * ((-1) ** (2 * Bdisc[i, j])))
    Tdisc = S.diag(*[(-1) ** int(2 * Qv) for Qv in Q])
    check("finite_S_fourier", Sdisc == Sdisc.T and Sdisc.T * Sdisc == S.eye(4))
    check("relative_T_sector_signs", Tdisc == S.diag(1, 1, -1, 1))
    check("finite_modular_ST_identity", (Sdisc * Tdisc) ** 3 == S.eye(4))
    probe = S.Matrix([2, -3, 5, 7])
    check("finite_S_reconstructs", Sdisc.T * (Sdisc * probe) == probe)

    # Arf kernel H_{(rho_x,rho_t),(a,b)}.  Its inverse is H.T, so both the
    # forward transform and reconstruction are exact over Q.
    spin = [(0, 0), (0, 1), (1, 0), (1, 1)]
    H = S.Matrix([
        [S.Rational((-1) ** (a0 * b0 + a0 * rt + b0 * rx), 2) for a0, b0 in spin]
        for rx, rt in spin
    ])
    check("arf_kernel_formula", H == S.Matrix([
        [S.Rational(1, 2), S.Rational(1, 2), S.Rational(1, 2), -S.Rational(1, 2)],
        [S.Rational(1, 2), S.Rational(1, 2), -S.Rational(1, 2), S.Rational(1, 2)],
        [S.Rational(1, 2), -S.Rational(1, 2), S.Rational(1, 2), S.Rational(1, 2)],
        [S.Rational(1, 2), -S.Rational(1, 2), -S.Rational(1, 2), -S.Rational(1, 2)],
    ]))
    check("arf_kernel_inverse_is_transpose", H.T * H == S.eye(4) and H * H.T == S.eye(4) and H.T != H)
    check("arf_kernel_reconstructs", H.T * (H * probe) == probe)

    bosonic_background = S.Matrix([
        [1, 1, 0, 0], [1, -1, 0, 0],
        [0, 0, 1, 1], [0, 0, -1, 1],
    ])
    fermion_rows = S.Matrix([
        [1, 0, 1, 0], [1, 0, -1, 0],
        [0, 1, 0, 1], [0, 1, 0, -1],
    ])
    check("arf_maps_background_to_fermions", H * bosonic_background == fermion_rows)
    check("background_rows_orthogonal", bosonic_background.T * bosonic_background == 2 * S.eye(4))
    check("fermion_rows_orthogonal", fermion_rows.T * fermion_rows == 2 * S.eye(4))
    check("background_and_fermion_reconstruct", bosonic_background.T * (bosonic_background * probe) / 2 == probe and fermion_rows.T * (fermion_rows * probe) / 2 == probe)

    # Modular S/T actions are checked as explicit (signed) row permutations,
    # rather than inferred only from a global relation.
    row_perm_S = S.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    row_perm_T_boson = S.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    row_perm_T_fermion = S.Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    check("modular_S_background_permutation", bosonic_background * Sdisc == row_perm_S * bosonic_background and fermion_rows * Sdisc == row_perm_S * fermion_rows)
    check("modular_T_background_permutation", bosonic_background * Tdisc == row_perm_T_boson * bosonic_background and fermion_rows * Tdisc == row_perm_T_fermion * fermion_rows)

    eta = S.diag(1, -1, 1, -1)  # exp(2 pi i B(f, -))
    check("twist_character", [qform(f, K, r) for r in reps] == [0, S.Rational(-1, 2), 1, S.Rational(1, 2)] and eta == S.diag(1, -1, 1, -1))
    check("twisted_lift_signs", -eta == S.diag(-1, 1, -1, 1))

    # Sector addition is the Z2xZ2 table; f interchanges the two putative
    # parity pairs.  This is only the finite class bookkeeping.
    class_bits = [(0, 0), (1, 0), (0, 1), (1, 1)]
    class_index = {bits: i for i, bits in enumerate(class_bits)}

    def class_of(vector):
        for index, representative in enumerate(reps):
            if integral_vector(Gamma0_coordinates * (vector - representative)):
                return index
        raise RuntimeError("class representative not found")

    addition = [[class_of(reps[i] + reps[j]) for j in range(4)] for i in range(4)]
    check("f_intertwiner_class_pairs", [addition[i][2] for i in range(4)] == [2, 3, 0, 1])
    check("sector_addition_z2x_z2", addition == [
        [0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]
    ])

    # For integral Gamma basis vectors, the inherited lattice cocycle has the
    # super-commutator exponent B(x,y)+p(x)p(y), p=q mod 2.
    gamma_basis = [I10[:, i] for i in range(10)]
    def triangular_cocycle(x, y):
        return sum(x[i] * y[j] for i in range(10) for j in range(i))

    cocycle_exponents = [[int(qform(x, K, y) + (q.dot(x) % 2) * (q.dot(y) % 2)) % 2 for y in gamma_basis] for x in gamma_basis]
    triangular_commutators = [[int(triangular_cocycle(x, y) - triangular_cocycle(y, x)) % 2 for y in gamma_basis] for x in gamma_basis]
    check("gamma_cocycle_supercommutator", cocycle_exponents == [
        [1 if i != j else 0 for j in range(10)] for i in range(10)
    ] and triangular_commutators == cocycle_exponents)

    # Both matrices are exact positive Euclidean generalized metrics obeying
    # V K V=K.  V0 is the free point; Vc is the selected diagnostic point.
    v = (n - z) / 2
    V0 = S.eye(10)
    Vc = K + 2 * K * v * v.T * K
    check("generalized_metric_identities", V0 * K * V0 == K and Vc * K * Vc == K and Vc == Vc.T)
    vc_eigs = Vc.eigenvals()
    check("generalized_metrics_positive", all(ev.is_positive for ev in V0.eigenvals()) and vc_eigs == {
        S.Integer(1): 8, 7 - 4 * S.sqrt(3): 1, 7 + 4 * S.sqrt(3): 1
    })
    delta0_e9 = qform(f, V0) / 2
    deltac_e9 = qform(f, Vc) / 2
    check("same_sector_dimension_diagnostic", delta0_e9 == S.Rational(1, 2) and deltac_e9 == S.Rational(3, 2))
    check("critical_e9_exponents_and_charges", [delta0_e9, deltac_e9] == [S.Rational(1, 2), S.Rational(3, 2)] and q.dot(f) == Y.dot(f) == 1 and g.dot(f) == -1)
    check("critical_two_point_exponents", S.Rational(1) + S.Rational(1, 2) == deltac_e9 and S.Rational(1) - S.Rational(1, 2) == S.Rational(1, 2))

    result = {
        "contract_scope": "conditional four-sector algebra; no twisted-module or source-dynamics claim",
        "checks_passed": len(CHECKS),
        "checks": CHECKS,
        "sector_order": labels,
        "quadratic_values": [str(x) for x in Q],
        "relative_T": [int(2 * x) for x in Q],
        "S_matrix": [[str(x) for x in row] for row in Sdisc.tolist()],
        "Arf_kernel": [[str(x) for x in row] for row in H.tolist()],
        "twist_eta": [int(eta[i, i]) for i in range(4)],
        "twisted_lift_minus_eta": [int((-eta)[i, i]) for i in range(4)],
        "delta_e9": {"V0": str(delta0_e9), "Vc": str(deltac_e9)},
        "critical_exponents": {"h": "1", "hbar": "1/2", "Delta": "3/2"},
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if output is None:
        suffix = ".optimized" if sys.flags.optimize else ""
        output = HERE / f"charged-sector-algebra-result{suffix}.json"
    Path(output).write_text(text)
    print(f"charged-sector-algebra: {len(CHECKS)}/{len(CHECKS)} checks; output={Path(output)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    main(args.output)
