#!/usr/bin/env python3
"""Finite exact algebra for the conditional flux-index interpretation of n.

This checks only the declared ten-channel lattice dictionary.  It does not
construct a flux sector, a gauge field, a cosine Hamiltonian, or a native
source map.
"""

from itertools import combinations, product
import argparse
import hashlib
import json
from math import gcd
from pathlib import Path

import sympy as S


HERE = Path(__file__).resolve().parent
SOURCE_FILES = {
    "source_dynamics_controls": Path("/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/source-dynamics-selection-20260920/controls.json"),
    "source_dynamics_proof": Path("/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/source-dynamics-selection-20260920/PROOF.txt"),
    "rotor_gauss_proof": Path("/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/source-rotor-gauss-20260920/PROOF.txt"),
}
EXPECTED_SOURCE_SHA256 = {
    "source_dynamics_controls": "08857ab6fa78673a836d04f073572c4963bdf35b3a41db4046e7f181858187f1",
    "source_dynamics_proof": "03c09468b07cc68abd31d7f8d6715dd474564728d053ccb063a67a1ca71c89d2",
    "rotor_gauss_proof": "17d351d19de8d33c346a35d8bf27ed94045eec8e8da71a62aa63b26d4276b0da",
}
CHECKS = {}


def check(name, condition):
    ok = bool(condition)
    CHECKS[name] = ok
    if not ok:
        raise RuntimeError(name)


def resolve_source_files(repo_root=None):
    if repo_root is None:
        return SOURCE_FILES
    root = Path(repo_root).resolve()
    return {
        "source_dynamics_controls": root / "experiments/theory-contracts/source-dynamics-selection-20260920/controls.json",
        "source_dynamics_proof": root / "experiments/theory-contracts/source-dynamics-selection-20260920/PROOF.txt",
        "rotor_gauss_proof": root / "experiments/theory-contracts/source-rotor-gauss-20260920/PROOF.txt",
    }


def e8_roots():
    roots = []
    for i, j in combinations(range(8), 2):
        for si, sj in product((-1, 1), repeat=2):
            vector = [S.Integer(0)] * 8
            vector[i], vector[j] = si, sj
            roots.append(S.Matrix(vector))
    for signs in product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(S.Matrix(signs) / 2)
    return roots


def simple_e8_basis():
    basis = [
        S.Matrix([1, -1, -1, -1, -1, -1, -1, 1]) / 2,
        S.Matrix([1, 1, 0, 0, 0, 0, 0, 0]),
    ]
    for i in range(6):
        vector = S.zeros(8, 1)
        vector[i], vector[i + 1] = -1, 1
        basis.append(vector)
    return basis


def main(output=None, repo_root=None):
    source_files = resolve_source_files(repo_root)
    controls = json.loads(source_files["source_dynamics_controls"].read_text())
    check("source_contract_pin", controls["contract"] == "UR.SOURCE.DYNAMICS_SELECTION.01")
    source_sha256 = {name: hashlib.sha256(path.read_bytes()).hexdigest()
                     for name, path in source_files.items()}
    check("source_pins_enforced", source_sha256 == EXPECTED_SOURCE_SHA256)

    K = S.diag(*([1] * 9 + [-1]))
    n = S.Matrix(controls["basis"]["n"])
    q = S.ones(10, 1)
    Y = S.Matrix([S.Rational(value) for value in controls["basis"]["hypercharge"]])
    a = n[:8, 0]
    eR = -S.eye(10)[:, 8]
    m = S.Matrix(list(a) + [0, 3])
    g = K * n

    def T(root):
        k = a.dot(root) / 2
        return S.Matrix(list(root) + [-k, k])

    def F(root):
        k = a.dot(root) / 2
        return T(root) - k * n

    roots = e8_roots()
    simple = simple_e8_basis()
    simple_matrix = S.Matrix.hstack(*simple)
    F_basis = S.Matrix.hstack(*(F(root) for root in simple))
    F_roots = [F(root) for root in roots]
    W_aux = S.Matrix.hstack(*[F(root) for root in simple], eR, m)
    G_E8 = simple_matrix.T * simple_matrix
    expected_W_gram = S.zeros(10)
    expected_W_gram[:8, :8] = G_E8
    expected_W_gram[8, 8] = 1
    expected_W_gram[9, 9] = -1

    check("flux_index_signed_identity", K * g == n)
    check("g_is_Kn_null", (g.T * K * g)[0] == 0)
    check("n_source_and_hypercharge_neutral", q.dot(n) == 0 and Y.dot(n) == 0)
    check("g_q_Y_mixed_bilinears", (q.T * K * g)[0] == 0 and (Y.T * K * g)[0] == 0)

    check("E8_root_count", len(roots) == 240 and len({tuple(root) for root in roots}) == 240)
    check("F_root_integrality", all(all(S.denom(value) == 1 for value in vector) for vector in F_roots))
    check("F_root_neutrality", all(g.dot(vector) == 0 for vector in F_roots))
    check("F_simple_basis_integral_lattice", all(all(S.denom(value) == 1 for value in F_basis) for _ in [0]) and F_basis.rank() == 8)
    check("F_basis_preserves_E8_simple_gram", F_basis.T * K * F_basis == G_E8 and G_E8.det() == 1)
    check("F_basis_K_orthogonal_to_complement", F_basis.T * K * eR == S.zeros(8, 1) and F_basis.T * K * m == S.zeros(8, 1))
    check("W_aux_K_gram_is_E8_plus_pair", W_aux.T * K * W_aux == expected_W_gram)
    check("complementary_pair_charges", g.dot(eR) == 1 and g.dot(m) == -1 and eR + m == n)
    check("W_aux_is_unimodular_lattice_coordinates", abs(W_aux.det()) == 1 and all(S.denom(value) == 1 for value in W_aux.inv()))

    ar, br = S.symbols("a_R b_R", integer=True)
    lattice_coords = S.Matrix(S.symbols("r0:8", integer=True))
    x = F_basis * lattice_coords + ar * eR + br * m
    check("general_lattice_charge_formula", S.expand(g.dot(x) - (ar - br)) == 0)
    check("kernel_is_E8_plus_Zn", F_basis.rank() == 8 and S.Matrix.hstack(F_basis, n).rank() == 9 and g.dot(F_basis * lattice_coords + ar * n) == 0)
    check("kernel_quotient_by_n_is_primitive_E8", S.Matrix.hstack(F_basis, n).rank() == 9 and G_E8.det() == 1)

    unit_factors = sum(abs(int(value)) for value in n[:9, 0])
    charge_three = abs(int(n[9]))
    derivative_order = charge_three * (charge_three - 1) // 2
    total_factors = unit_factors + charge_three
    free_h = S.Rational(sum(int(value) ** 2 for value in n[:9, 0]), 2)
    free_hbar = S.Rational(int(n[9]) ** 2, 2)
    free_dimension = free_h + free_hbar
    check("characteristic_n_factor_count", unit_factors == 9 and charge_three == 3 and total_factors == 12)
    check("charge_three_derivative_count", derivative_order == 3)
    check("free_chiral_weights", free_h == S.Rational(9, 2) and free_hbar == S.Rational(9, 2) and free_dimension == 9)
    check("factor_dimension_identity", S.Rational(unit_factors, 2) + S.Rational(charge_three, 2) + derivative_order == free_dimension)
    check("g_all_odd_parity", all(int(value) % 2 for value in g))

    # Select the compact-U(1) normal without assuming n-neutrality.  Every
    # integral covector annihilating the fixed F(E8) embedding has the form
    # g(v,u)=(v*a,u,-3v).  The two null branches are distinguished by the
    # already marked source charges q and Y.
    v, u = S.symbols("v u", integer=True)
    g_vu = S.Matrix(list(v * a) + [u, -3 * v])
    pure_gauge = S.factor((g_vu.T * K * g_vu)[0])
    mixed_q = S.expand((q.T * K * g_vu)[0])
    mixed_Y = S.expand((Y.T * K * g_vu)[0])
    check("neutral_covector_family_annihilates_F", all(g_vu.dot(F_basis[:, i]) == 0 for i in range(8)))
    check("normal_pure_gauge_factorization", pure_gauge == (u - v) * (u + v))
    check("normal_mixed_q_formula", mixed_q == u + v)
    check("normal_mixed_Y_formula", mixed_Y == u + v)
    check("preserved_marking_selects_u_minus_v", mixed_q.subs(u, -v) == 0 and mixed_Y.subs(u, -v) == 0)
    check("primitive_preserved_solutions", [g_vu.subs({u: -value, v: value}) for value in (-1, 1)] == [-g, g])
    check("alternative_null_branch_breaks_markings", mixed_q.subs(u, v) == 2 * v and mixed_Y.subs(u, v) == 2 * v)
    check("primitive_branch_gcd", all(gcd(abs(value), abs(value), abs(3 * value)) == 1 for value in (-1, 1)))
    check("selected_n_neutrality_is_consequence", g_vu.subs(u, -v).dot(n) == 0)

    # A compact census in the sign-flipped basis makes the low-degree quotient
    # representatives concrete.  It is a finite lattice check, not an IR
    # statement: 72 differences and 168 signed triples exhaust the 240 roots.
    sign_flip = S.diag(*[int(value) for value in g[:9, 0]] + [1])
    W_inv = W_aux.inv()
    quotient_candidates = []
    for i in range(9):
        for j in range(9):
            if i != j:
                y = [0] * 9
                y[i], y[j] = 1, -1
                quotient_candidates.append((y, 0))
    for triple in combinations(range(9), 3):
        for sign in (-1, 1):
            y = [0] * 9
            for index in triple:
                y[index] = sign
            quotient_candidates.append((y, sign))
    root_set = {tuple(root) for root in roots}
    pair_distribution = {}
    for y, k in quotient_candidates:
        y_vector = S.Matrix(y)
        projection = y_vector - S.Rational(k, 3) * S.ones(9, 1)
        check_value = projection.dot(projection)
        check("quotient_representative_neutral_grade", sum(y) == 3 * k)
        check("quotient_representative_norm", check_value == 2)
        x = sign_flip * S.Matrix(list(y) + [k])
        coordinates = W_inv * x
        check("quotient_representative_integral_W_coordinates", all(S.denom(value) == 1 for value in coordinates))
        pair_left, pair_right = coordinates[8, 0], coordinates[9, 0]
        check("quotient_representative_pair_coordinates_match", pair_left == pair_right)
        pair_distribution[str(int(pair_left))] = pair_distribution.get(str(int(pair_left)), 0) + 1
        root = simple_matrix * coordinates[:8, :]
        check("quotient_representative_is_E8_root", tuple(root) in root_set)
        check("quotient_representative_reconstructs", F_basis * coordinates[:8, :] + pair_left * n == x)
    check("quotient_representative_count", len(quotient_candidates) == 240)
    check("quotient_representative_pair_distribution", pair_distribution == {"-1": 36, "0": 168, "1": 36})

    result = {
        "status": "PASS_EXACT_FINITE_CONTROLS_ONLY",
        "research_verdict": "PARTIAL",
        "count": len(CHECKS),
        "all_passed": all(CHECKS.values()),
        "checks": CHECKS,
        "source_pins": {name: {"path": str(path), "sha256": source_sha256[name]}
                        for name, path in source_files.items()},
        "flux_index": {"K_g": [int(value) for value in n], "g": [int(value) for value in g],
                       "interpretation": "conditional unit compact-U(1) signed index in the declared lattice dictionary"},
        "lattice_quotient": {"decomposition": "x=F(r)+a_R e_R+b_R m", "g_charge": "a_R-b_R",
                            "kernel": "F(E8)+Z n", "quotient": "E8", "W_aux_determinant": int(W_aux.det())},
        "non_circular_selection": {"family": "g(v,u)=(v*a,u,-3v)", "pure_gauge": "u^2-v^2",
                                   "mixed_q": "u+v", "mixed_Y": "u+v", "selected_branch": "u=-v",
                                   "primitive_solutions": ["g", "-g"],
                                   "alternate_null_branch": "u=+v gives mixed q=Y=2v",
                                   "n_neutrality": "consequence, not selection input"},
        "quotient_root_census": {"difference_representatives": 72, "signed_triple_representatives": 168,
                                 "total": len(quotient_candidates), "all_projected_norm": "2",
                                 "pair_coordinate_distribution": pair_distribution,
                                 "scope": "finite quotient census only"},
        "n_vertex": {"unit_fermion_factors": unit_factors, "charge_three": charge_three,
                     "derivative_order": derivative_order, "total_fermion_factors": total_factors,
                     "free_h": "9/2", "free_hbar": "9/2", "free_dimension": "9"},
        "scope": {"flux_sector_constructed": False, "gauge_field_added": False, "cosine_hamiltonian_generated": False,
                   "native_source_origin_claimed": False, "conditional_algebra_only": True},
    }
    output = Path(output) if output is not None else HERE / "flux_index_algebra.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "count": result["count"], "all_passed": result["all_passed"], "result": output.name}, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--root", type=Path, default=None)
    args = parser.parse_args()
    main(args.output, args.root)
