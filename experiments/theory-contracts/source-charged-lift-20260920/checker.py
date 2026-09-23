#!/usr/bin/env python3
"""Exact finite algebra for charged E8 lifts and the minimal local repair.

This is conditional lattice algebra for the fixed ten-channel dictionary.  It
does not add a source interaction, a gauge field, or an IR identification.
"""

from itertools import combinations, product
import argparse
import hashlib
import json
from pathlib import Path

import sympy as S


HERE = Path(__file__).resolve().parent
DEFAULT_ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
EXPECTED_SHA256 = {
    "source_flux_index": "55ad6f18bf4f69d8d194e74dff29d6679e4cd6fca4568aafaaf7d127ac7d4bef",
    "source_clifford_grade": "7cfda722c50e6c7d17caccf038e0ffd42d326935f4301ecf466dd9dae2760276",
    "source_graded_locality": "669309ea7f240397b2eb49c61e02b5224d4b9d1c15d50aeca30668fa97fa41bb",
}
CHECKS = {}


def check(name, condition):
    ok = bool(condition)
    CHECKS[name] = ok
    if not ok:
        raise RuntimeError(name)


def source_files(root):
    root = Path(root).resolve()
    return {
        "source_flux_index": root / "experiments/theory-contracts/source-flux-index-20260920/PROOF.txt",
        "source_clifford_grade": root / "experiments/theory-contracts/source-clifford-grade-20260920/PROOF.md",
        "source_graded_locality": root / "experiments/theory-contracts/source-graded-locality-20260920/PROOF.txt",
    }


def e8_roots():
    roots = []
    for i, j in combinations(range(8), 2):
        for si, sj in product((-1, 1), repeat=2):
            v = [S.Integer(0)] * 8
            v[i], v[j] = si, sj
            roots.append(S.Matrix(v))
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
        v = S.zeros(8, 1)
        v[i], v[i + 1] = -1, 1
        basis.append(v)
    return basis


def d8_basis():
    basis = []
    for i in range(7):
        v = S.zeros(8, 1)
        v[i], v[i + 1] = 1, -1
        basis.append(v)
    v = S.zeros(8, 1)
    v[7 - 1], v[7] = 1, 1
    basis.append(v)
    return basis


def all_integral(matrix):
    return all(S.denom(value) == 1 for value in matrix)


def main(output=None, root=DEFAULT_ROOT):
    files = source_files(root)
    source_sha256 = {name: hashlib.sha256(path.read_bytes()).hexdigest()
                     for name, path in files.items()}
    check("source_pins_enforced", source_sha256 == EXPECTED_SHA256)

    K = S.diag(*([1] * 9 + [-1]))
    a = S.Matrix([1, 1, 1, -1, -1, -1, -1, -1])
    n = S.Matrix(list(a) + [-1, 3])
    z = S.Matrix([0] * 8 + [1, -1])
    g = K * n
    e9 = S.eye(10)[:, 8]
    q = S.ones(10, 1)
    Y = S.Matrix([S.Rational(-1, 3)] * 3 + [S.Rational(1, 2)] * 2 + [0] * 3 + [1, 1])

    def F(r):
        k = a.dot(r) / 2
        return S.Matrix(list(r - k * a) + [0, -2 * k])

    def T(r):
        k = a.dot(r) / 2
        return S.Matrix(list(r) + [-k, k])

    roots = e8_roots()
    simple = simple_e8_basis()
    simple_matrix = S.Matrix.hstack(*simple)
    F_basis = S.Matrix.hstack(*(F(r) for r in simple))
    T_basis = S.Matrix.hstack(*(T(r) for r in simple))
    G_E8 = simple_matrix.T * simple_matrix
    d8 = d8_basis()
    d8_matrix = S.Matrix.hstack(*d8)
    d8_roots = [r for r in roots if all(S.denom(value) == 1 for value in r)]

    check("fixed_dictionary", K * n == g and g.dot(n) == 0)
    check("source_markings_neutral", q.dot(n) == 0 and q.dot(z) == 0 and Y.dot(n) == 0 and Y.dot(z) == 0)
    check("F_E8_integral_and_neutral", all_integral(S.Matrix.hstack(*(F(r) for r in roots))) and all(g.dot(F(r)) == 0 for r in roots))
    check("E8_simple_gram_unimodular", G_E8.det() == 1 and all_integral(G_E8.inv()))
    check("F_isometric", F_basis.T * K * F_basis == G_E8)
    check("T_minus_F_formula", all(T(r) - F(r) == (a.dot(r) / 2) * n for r in roots))
    check("e9_charged_pairing", g.dot(e9) == -1 and (n.T * K * e9)[0] == -1)

    # Every integral additive section differs by an integral linear functional
    # times the null generator n.  E8 self-duality represents that functional
    # as lambda dot r with lambda in E8.
    ell = S.Matrix(S.symbols("ell0:8", integer=True))
    section = F_basis + n * ell.T
    lambda_coordinates = G_E8.inv() * ell
    check("all_section_difference_is_null_shift", (section.T * K * section - G_E8).applyfunc(S.simplify) == S.zeros(8))
    check("E8_self_duality_represents_all_integral_functionals", all_integral(G_E8.inv()) and G_E8 * lambda_coordinates == ell)
    lambda_vector = simple_matrix * lambda_coordinates
    check("section_functional_is_lambda_dot", simple_matrix.T * lambda_vector == ell)

    # D8 is the integral-root subgroup of E8.  T is integral on it, but the
    # desired T restriction forces lambda=a/2, which is outside E8.
    required_lambda = a / 2
    d8_delta = T_basis[:, :]
    d8_T = S.Matrix.hstack(*(T(r) for r in d8))
    d8_F = S.Matrix.hstack(*(F(r) for r in d8))
    required_values = S.Matrix([a.dot(r) / 2 for r in d8])
    check("D8_is_index_two_root_subgroup", len(d8_roots) == 112 and abs(d8_matrix.det()) == 2)
    check("T_integral_on_D8", all_integral(d8_T))
    check("T_restriction_forces_a_over_two", d8_T - d8_F == n * required_values.T and d8_matrix.T * required_lambda == required_values)
    check("a_over_two_not_E8", not all_integral(required_lambda) and sum(1 if value < 0 else 0 for value in required_lambda) % 2 == 1)
    check("T_nonintegral_on_all_E8_half_roots", sum(not all_integral(T(r)) for r in roots) == 128)
    check("T_half_roots_half_pairing_with_e9", sum(S.denom((T(r).T * K * e9)[0]) == 2 for r in roots if any(S.denom(value) == 2 for value in r)) == 128)

    # Minimal positive repair: the even-charge sublattice plus n/2.
    even_basis = []
    for i in range(9):
        v = S.zeros(10, 1)
        v[i], v[9] = 1, -1
        even_basis.append(v)
    twice_last = S.zeros(10, 1)
    twice_last[9] = 2
    even_basis.append(twice_last)
    even_matrix = S.Matrix.hstack(*even_basis)
    h = n / 2
    f = e9
    check("Gamma_even_basis", abs(even_matrix.det()) == 2 and all((g.dot(v) % 2) == 0 for v in even_basis))
    check("Gamma_even_is_even_norm_kernel", all((g.dot(v) - (v.T * K * v)[0]) % 2 == 0 for v in even_basis))

    # The two even unimodular neighbors are retained explicitly.  The h coset
    # is selected only because it contains the desired T(E8) lift.
    neighbor_h_basis = S.Matrix.hstack(*even_basis[1:], h)
    neighbor_hf_basis = S.Matrix.hstack(*even_basis[1:], h + f)
    check("neighbor_h_basis_unimodular", abs(neighbor_h_basis.det()) == 1 and all_integral(neighbor_h_basis.inv() * even_matrix) and all_integral(neighbor_h_basis.T * K * neighbor_h_basis))
    check("neighbor_hf_basis_unimodular", abs(neighbor_hf_basis.det()) == 1 and all_integral(neighbor_hf_basis.inv() * even_matrix) and all_integral(neighbor_hf_basis.T * K * neighbor_hf_basis))
    even_inverse = even_matrix.inv()
    check("Gamma_even_four_cosets", all(all_integral(even_inverse * (2 * v)) for v in [f, h, h + f]) and
          all(not all_integral(even_inverse * v) for v in [f, h, h + f]) and
          (h.T * K * h)[0] == 0 and (f.T * K * f)[0] == 1 and
          (h + f).T * K * (h + f) == S.Matrix([[0]]) and (h.T * K * f)[0] == S.Rational(-1, 2))

    W_B = S.Matrix.hstack(*[T(r) for r in simple], h, z)
    expected_WB_gram = S.zeros(10)
    expected_WB_gram[:8, :8] = G_E8
    expected_WB_gram[8, 9] = expected_WB_gram[9, 8] = 1
    check("WB_gram_E8_plus_U", abs(W_B.det()) == 1 and W_B.T * K * W_B == expected_WB_gram)
    check("L_generators_in_WB", all_integral(W_B.inv() * even_matrix) and all_integral(W_B.inv() * h))
    check("WB_generators_in_L", all_integral(neighbor_h_basis.inv() * W_B))
    check("L_equals_T_E8_plus_h_plus_z", all_integral(neighbor_h_basis.inv() * W_B) and all_integral(W_B.inv() * neighbor_h_basis))
    check("all_T_E8_roots_local_in_L", all_integral(neighbor_h_basis.inv() * S.Matrix.hstack(*(T(r) for r in roots))))
    check("missing_halfroots_not_in_Gamma", sum(not all_integral(T(r)) for r in roots) == 128)
    check("e9_excluded_from_L", not all_integral(neighbor_h_basis.inv() * e9))
    check("all_L_vectors_even", all(entry % 2 == 0 for entry in (W_B.T * K * W_B).diagonal()))

    # Optional constructive spectator: an Eichler transvection realizes one
    # nontrivial lambda section by an integral K-isometry fixing the markings.
    lambda_eichler = S.Matrix([1, -1, 0, 0, 0, 0, 0, 0])
    F_lambda = F(lambda_eichler)
    L_eichler = (S.eye(10) - F_lambda * g.T + n * (K * F_lambda).T
                 - (lambda_eichler.dot(lambda_eichler) / 2) * n * g.T)
    check("Eichler_is_integral_unimodular_K_isometry", all_integral(L_eichler) and L_eichler.det() == 1 and L_eichler.T * K * L_eichler == K)
    check("Eichler_fixes_n_g_q_Y", L_eichler * n == n and g.T * L_eichler == g.T and q.T * L_eichler == q.T and Y.T * L_eichler == Y.T)
    check("Eichler_realizes_lambda_section", L_eichler * F_basis == F_basis + n * (lambda_eichler.T * simple_matrix) and L_eichler != S.eye(10))

    result = {
        "status": "PASS_EXACT_FINITE_CONTROLS_ONLY",
        "research_verdict": "PARTIAL",
        "count": len(CHECKS),
        "all_passed": all(CHECKS.values()),
        "checks": CHECKS,
        "source_pins": {name: {"path": str(path), "sha256": source_sha256[name]} for name, path in files.items()},
        "section_theorem": {"section_form": "F_lambda(r)=F(r)+(lambda.r)n", "lambda_lattice": "E8 via E8 self-duality",
                            "D8_restriction": "lambda=a/2", "a_over_two_in_E8": False,
                            "D8_root_count": 112, "E8_half_root_count": 128,
                            "e9_charge": -1, "B_n_e9": -1},
        "minimal_repair": {"even_kernel": "Gamma_even={x:g.x even}", "basis": "T(E8) plus Z(n/2) plus Zz",
                           "gram": "G_E8 plus U", "signature": "(9,1)", "determinant_abs": 1,
                           "T_roots_local": 240, "half_roots_missing_from_Gamma": 128,
                           "e9_in_repair": False, "even_neighbors": 2,
                           "T_selects_neighbor": "Gamma_even+Z(n/2)"},
        "eichler_spectator": {"lambda": [1, -1, 0, 0, 0, 0, 0, 0], "is_physical_claim": False},
        "scope": {"conditional_lattice_algebra_only": True, "source_origin_derived": False,
                   "new_dynamics_added": False, "gauge_field_added": False, "ir_identification_claimed": False},
    }
    output = Path(output) if output is not None else HERE / "charged_lift_algebra.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "count": result["count"], "all_passed": result["all_passed"], "result": output.name}, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    main(args.output, args.root)
