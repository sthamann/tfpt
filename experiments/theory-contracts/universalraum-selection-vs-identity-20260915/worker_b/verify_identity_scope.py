#!/usr/bin/env python3
"""Exact finite checks accompanying a conditional affine-current uniqueness proof.

This checks algebraic instances, not the analytic uniqueness theorem or the
raw-seam/VOA identification. It writes no files and imports no repository code.
"""
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[4]
SOURCES = [
    "origin_theory.tex", "docs/THEORY.md", "docs/OPEN_PROBLEMS.md",
    "verification/v154_simple_current_theorem.py",
    "verification/v463_seam_c8_holomorphic_uniqueness.py",
    "verification/v469_seam_crossedproduct_route.py",
    "verification/v973_seam_route_narrowing.py",
    "experiments/theory-contracts/universalraum-native-exterior-reset-20260915/RESULTS.md",
    "experiments/theory-contracts/universalraum-five-reports-native-clock-20260915/RESULTS.md",
    "experiments/theory-contracts/universalraum-primitive-source-audit-20260915/RESULTS.md",
    "experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/native_tensor.npz",
]


def main():
    hashes_before = {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in SOURCES}
    checks = []

    def check(name, predicate):
        passed = bool(predicate)
        checks.append({"name": name, "pass": passed})
        if not passed:
            raise RuntimeError(name)

    raw_w = np.load(ROOT / SOURCES[-1])["W"]
    check("source_W_real_integer", np.all(raw_w.imag == 0)
          and np.all(raw_w.real == np.round(raw_w.real)))
    w = raw_w.real.astype(np.int64)
    check("source_W_shape", w.shape == (60, 2016))
    check("source_W_nonzero_count", np.count_nonzero(w) == 480)
    check("source_W_Wtranspose", np.array_equal(w @ w.T, 8 * np.eye(60, dtype=np.int64)))

    k = sp.symbols("k")
    check("c8_and_affine_Sugawara_force_k1", sp.solve(sp.Eq(248*k/(k+30), 8), k) == [1])
    check("glue_current_integer_weight_1", Fraction(5, 8) + Fraction(3, 8) == 1)
    check("glue_current_integer_weight_2", Fraction(1, 2) + Fraction(1, 2) == 1)

    # Existing (16,4) root sector: even minus parity separately on 5 and 3 coordinates.
    alpha = sp.Matrix([sp.Rational(1, 2)] * 8)
    beta = sp.Matrix([sp.Rational(i, 2) for i in [-1, -1, -1, -1, 1, -1, -1, 1]])
    gamma = alpha + beta
    check("root_pair_in_existing_sector", all(sum(bool(x < 0) for x in v[:5]) % 2 == 0
          and sum(bool(x < 0) for x in v[5:]) % 2 == 0 for v in (alpha, beta)))
    check("root_pair_inner_products", alpha.dot(alpha) == beta.dot(beta) == gamma.dot(gamma) == 2
          and alpha.dot(beta) == -1)
    # Lattice VOA formula: u=epsilon alpha(-1)e^gamma, v=-epsilon beta(-1)e^gamma.
    gram = sp.Matrix([[alpha.dot(alpha), -alpha.dot(beta)],
                      [-beta.dot(alpha), beta.dot(beta)]])
    check("four_current_Gram", gram == sp.Matrix([[2, 1], [1, 2]]))
    check("current_commutator_descendant_norm", (sp.Matrix([1, -1]).T*gram*sp.Matrix([1, -1]))[0] == 2)
    check("symmetric_current_pair_norm", (sp.Matrix([1, 1]).T*gram*sp.Matrix([1, 1]))[0] == 6)

    # Same E8 Hilbert space, algebra, vacuum, internal symmetries and quarter clock.
    n = sp.symbols("n", integer=True, nonnegative=True)
    f = n + 4*n*(n-1)
    check("counter_generator_polynomial_identity", sp.expand(f - n - 4*n*(n-1)) == 0)
    check("counter_generator_positivity_formula", sp.factor(f) == n*(4*n-3))
    check("counter_same_full_quarter_clock", sp.simplify(sp.exp(-sp.I*sp.pi*(f-n)/2)) == 1)
    check("counter_same_vacuum_and_first_level", f.subs(n, 0) == 0 and f.subs(n, 1) == 1)
    check("counter_distinct_dimensionless_second_gap", f.subs(n, 2) == 10)
    ratio = sp.simplify(sp.exp(-sp.I*sp.pi*f.subs(n, 2)/8) / sp.exp(-sp.I*sp.pi*2/8))
    check("counter_mode2_halfstep_phase_is_minus", ratio == -1)
    check("counter_fails_geometric_rotation_contract", f.subs(n, 2) - f.subs(n, 0) != 2)

    hashes_after = {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in SOURCES}
    check("all_source_hashes_unchanged", hashes_before == hashes_after)
    print(json.dumps({
        "status": "PASS_FINITE_ALGEBRA_ONLY",
        "analytic_uniqueness": "proved_in_RESULTS_md_on_declared_affine_vacuum_domain",
        "raw_seam_equals_E8_VOA": "NOT_PROVED",
        "primitive_physical_decisions_eliminated": "NOT_ESTABLISHED",
        "independent_TFPT_holdout": "NONE",
        "source_hashes": hashes_before,
        "checks": checks,
        "checks_passed": len(checks),
        "four_current_gram": [[2, 1], [1, 2]],
        "same_clock_generators_energy_levels_0_1_2": [[0, 1, 2], [0, 1, 10]],
        "phase_ratio_at_pi_over_8": -1,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
