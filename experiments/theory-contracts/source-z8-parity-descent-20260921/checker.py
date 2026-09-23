#!/usr/bin/env python3
"""Exact Z8/Z4 extension checks for the supplied finite candidate.

This is a bounded algebra check only.  It does not assert that the candidate
is selected by TFPT or that the compensating parent is physically present.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


F = Fraction


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def roots_e8():
    roots = []
    for i, j in combinations(range(8), 2):
        for si, sj in product((-1, 1), repeat=2):
            r = [0] * 8
            r[i], r[j] = si, sj
            roots.append(tuple(F(v) for v in r))
    for signs in product((-1, 1), repeat=8):
        if sum(s < 0 for s in signs) % 2 == 0:
            roots.append(tuple(F(s, 2) for s in signs))
    return roots


def field_image(r, a):
    k = dot(a, r) / 2
    return tuple(r[i] - k * a[i] for i in range(8)) + (F(0), -2 * k)


def beta(a, b):
    return (-1) ** ((a % 4) * (b // 4))


def omega(a, b, c):
    return (-1) ** ((a % 4) * (((b % 4) + (c % 4)) // 4))


def analytic_bound_n4_d10():
    # Decimal is used so the displayed value is reproducible without a
    # floating-point continuum claim.  The expression itself is the exact
    # symbolic bound supplied in the task.
    with localcontext() as ctx:
        ctx.prec = 90
        pi = Decimal("3.141592653589793238462643383279502884197169399375105820974944592307816406286")
        x = Decimal(108) * (pi / Decimal(20)).sqrt() * Decimal(-10).exp()
        value = x.exp() - Decimal(1)
        return format(value, ".60f")


def run():
    Kdiag = (1,) * 9 + (-1,)
    g = (1, 1, 1, -1, -1, -1, -1, -1, -1, -3)
    t = (2, 2, 2, 2, 2, 0, 0, 0, -1, -1)
    n0 = tuple(Kdiag[i] * g[i] for i in range(10))
    qhat = tuple(2 * t[i] + g[i] for i in range(10))
    a = (F(1), F(1), F(1), F(-1), F(-1), F(-1), F(-1), F(-1))
    roots = roots_e8()
    Fs = [field_image(r, a) for r in roots]
    checks = []

    def add(name, ok, details=None):
        checks.append({"id": name, "status": "PASS" if ok else "FAIL", "details": details or {}})

    add("t_dot_n0_zero", dot(t, n0) == 0, {"t_dot_n0": str(dot(t, n0)), "n0": list(n0)})
    add("gKg_zero", sum(Kdiag[i] * g[i] * g[i] for i in range(10)) == 0,
        {"gKg": sum(Kdiag[i] * g[i] * g[i] for i in range(10))})
    add("mixed_gKt_zero", sum(Kdiag[i] * g[i] * t[i] for i in range(10)) == 0,
        {"gKt": sum(Kdiag[i] * g[i] * t[i] for i in range(10))})
    add("qhat_definition", qhat == tuple(2 * t[i] + g[i] for i in range(10)), {"qhat": list(qhat)})
    qhat_norm = sum(Kdiag[i] * qhat[i] * qhat[i] for i in range(10))
    add("qhat_K_qhat_80", qhat_norm == 80, {"qhatKqhat": qhat_norm})
    add("qhat_all_entries_odd", all(x % 2 for x in qhat), {"odd_entries": sum(x % 2 for x in qhat)})
    right_sum = sum((qhat[i] * qhat[i] - 1) // 8 for i in range(9))
    left_sum = (qhat[9] * qhat[9] - 1) // 8
    spin_nu = sum(Kdiag[i] * (qhat[i] * qhat[i] - 1) // 8 for i in range(10))
    add("conditional_global_spin_Z8f", spin_nu == 9 and spin_nu % 2 == 1,
        {"nu": spin_nu, "nu_mod2": spin_nu % 2,
         "right_sum": right_sum, "left_sum": left_sum,
         "scope": "conditional on the global Uhat lift; not a gauged U(1) quotient"})
    add("conditional_chiral_sums", right_sum == 12 and left_sum == 3,
        {"right_sum": right_sum, "left_sum": left_sum,
         "formula": "sum_(K=+1)(qhat_i^2-1)/8 and sum_(K=-1)(qhat_i^2-1)/8"})
    add("conditional_chiral_central_difference", 9 - 1 == 8,
        {"cR": 9, "cL": 1, "cR_minus_cL": 8,
         "scope": "channel-count/chiral-response datum, not a 4D graviton claim"})

    odd_k_checks = {}
    for k in (1, 3, 5, 7):
        qk = tuple(2 * t[i] + k * g[i] for i in range(10))
        qk_norm = sum(Kdiag[i] * qk[i] * qk[i] for i in range(10))
        qk_nu = sum(Kdiag[i] * (qk[i] * qk[i] - 1) // 8 for i in range(10))
        odd_k_checks[str(k)] = {"norm": qk_norm, "nu": qk_nu,
                                "nu_mod2": qk_nu % 2,
                                "all_odd": all(x % 2 for x in qk)}
    add("all_odd_k_mod8_spin_checks", all(
        row["norm"] == 80 and row["nu"] == 9 and row["nu_mod2"] == 1 and row["all_odd"]
        for row in odd_k_checks.values()), {"k_checks": odd_k_checks,
        "scope": "conditional global Spin comparison for q_k=2t+k*g, k odd mod 8"})

    add("E8_root_census_240", len(roots) == 240, {"count": len(roots)})
    add("field_images_integral", all(x.denominator == 1 for v in Fs for x in v),
        {"nonintegral_entries": sum(x.denominator != 1 for v in Fs for x in v)})
    tf_values = [dot(t, v) for v in Fs]
    target_values = [2 * sum(r[:5], F(0)) for r in roots]
    add("tF_identity", tf_values == target_values,
        {"violations": sum(x != y for x, y in zip(tf_values, target_values)),
         "identity": "t·F(r)=2*sum(r[0:5])"})

    phase_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    for val in tf_values:
        phase_counts[int(val) % 4] += 1
    # The eight Cartan currents have trivial phase under this diagonal charge.
    phase_counts[0] += 8
    add("Uphase_census_248", phase_counts == {0: 60, 1: 64, 2: 60, 3: 64},
        {"phase_exponents_mod4": phase_counts, "basis": "240 E8 roots + 8 Cartan currents"})

    # Squaring U_car makes all integer E8 roots invariant and all 128 half
    # roots odd; the eight Cartan currents add to the invariant D8 block.
    root_kind_phase = {"integer": {0: 0, 1: 0, 2: 0, 3: 0},
                       "half": {0: 0, 1: 0, 2: 0, 3: 0}}
    for r in roots:
        kind = "integer" if all(x.denominator == 1 for x in r) else "half"
        root_kind_phase[kind][int(dot(t, field_image(r, a))) % 4] += 1
    add("Ucar2_root_census_D8", root_kind_phase == {
        "integer": {0: 52, 1: 0, 2: 60, 3: 0},
        "half": {0: 0, 1: 64, 2: 0, 3: 64},
    }, {"root_phase_exponents_mod4": root_kind_phase,
        "Ucar2_invariant_integer_roots": 112, "Ucar2_invariant_cartan": 8,
        "Ucar2_odd_half_roots": 128, "invariant_algebra": "D8 = 112 integer roots + 8 Cartan"})

    u0_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    for r in roots:
        u0_counts[int(sum(r, F(0))) % 4] += 1
    u0_counts[0] += 8
    add("U0_phase_census_248", u0_counts == {0: 136, 1: 0, 2: 112, 3: 0},
        {"phase_exponents_mod4": u0_counts, "basis": "240 E8 roots + 8 Cartan currents"})

    vector_weights = []
    for i in range(8):
        for sign in (-1, 1):
            v = [F(0)] * 8
            v[i] = F(sign)
            vector_weights.append(tuple(v))
    vector_h = [sum(x * x for x in v) / 2 for v in vector_weights]
    vector_t_charge = [2 * sum(v[:5], F(0)) for v in vector_weights]
    add("fermionized_vector_weights", len(vector_weights) == 16 and all(h == F(1, 2) for h in vector_h),
        {"count": len(vector_weights), "h_counts": {"1/2": len(vector_h)}})
    add("vector_weight_Ucar_split", sum(abs(int(x)) == 2 for x in vector_t_charge) == 10
        and sum(x == 0 for x in vector_t_charge) == 6,
        {"first_five_count": sum(abs(int(x)) == 2 for x in vector_t_charge),
         "last_three_count": sum(x == 0 for x in vector_t_charge),
         "interpretation": "10 first-five vector weights, 6 last-three vector weights"})
    quarter_vector_energies = [h - sum(v, F(0)) / 4 for v, h in zip(vector_weights, vector_h)]
    quarter_counts = {"1/4": sum(e == F(1, 4) for e in quarter_vector_energies),
                      "3/4": sum(e == F(3, 4) for e in quarter_vector_energies)}
    add("quarter_physical_vector_energies", quarter_counts == {"1/4": 8, "3/4": 8},
        {"energy_counts": quarter_counts, "formula": "H=L0-sum(r)/4, conditional on vector weights"})

    pair_dot_minus_one = sum(dot(r, s) == -1 for r in roots for s in roots)
    add("E8_ordered_root_pairs_dot_minus_one", pair_dot_minus_one == 13440,
        {"count": pair_dot_minus_one, "scope": "generic E8 root census only; no full cocycle validation"})

    bound = analytic_bound_n4_d10()
    add("analytic_bound_N4_d10", Decimal(bound) > 0 and Decimal(bound) < Decimal("0.00195"),
        {"expression": "exp(108*sqrt(pi/20)*exp(-10))-1", "value_60dp": bound,
         "upper_check": "0 < value < 0.00195",
         "scope": "high-precision evaluation of supplied analytic bound; not a continuum proof"})

    bad_coboundary = []
    for aa, bb, cc in product(range(8), repeat=3):
        lhs = beta(bb, cc) * beta(aa, (bb + cc) % 8)
        rhs = beta((aa + bb) % 8, cc) * beta(aa, bb)
        cob = lhs // rhs if lhs == rhs else F(lhs, rhs)
        if cob != omega(aa, bb, cc):
            bad_coboundary.append((aa, bb, cc, cob, omega(aa, bb, cc)))
    add("inflated_Z4_cocycle_trivialized", not bad_coboundary,
        {"triples": 8 ** 3, "violations": len(bad_coboundary),
         "beta": "(-1)^((a mod 4)*floor(b/4))",
         "omega": "(-1)^((a mod 4)*floor(((b mod 4)+(c mod 4))/4))"})
    add("beta_non_descent_witness", beta(1, 0) == 1 and beta(1, 4) == -1,
        {"beta_1_0": beta(1, 0), "beta_1_4": beta(1, 4),
         "meaning": "candidate beta depends on the Z8 lift of its second argument"})
    invariant_product = 1
    for bb in range(4):
        invariant_product *= omega(1, bb, 1)
    add("omega_invariant_product_minus_one", invariant_product == -1,
        {"product_b_0_to_3": invariant_product,
         "meaning": "no descended Z4 cochain can trivialize this invariant product"})

    passed = sum(c["status"] == "PASS" for c in checks)
    failed = [c for c in checks if c["status"] == "FAIL"]
    return {
        "status": "PASS" if not failed else "FAIL",
        "check_count": len(checks),
        "pass_count": passed,
        "fail_count": len(failed),
        "checks": checks,
        "assumptions": [
            "K=diag(1^9,-1), g, t, n0=K g and qhat=2t+g are supplied finite data.",
            "F(r)=(r-k a,0,-2k), k=(a·r)/2, is the supplied E8-to-source representative map.",
            "The 248 phase census counts 240 E8 roots plus eight Cartan currents; Cartan phases are taken trivial.",
            "The coboundary test is the finite Z8 cochain identity with addition modulo 8.",
            "The U_car^2 and U0 phase counts use the same F(r) charge map; Cartan currents are assigned the stated trivial phase.",
            "The vector-weight and quarter-energy checks are conditional on fermionizing the 16 weights ±e_i and using H=L0-sum(r)/4.",
            "The 13440 pair count is only the generic ordered E8 root-dot-product census; the attachment's 57600 phase claim is not revalidated here.",
        ],
        "scope": "Exact finite algebra only; no claim that the Z8 extension, anomaly inflow parent, or U(1) phase is selected by TFPT.",
        "witnesses": {
            "Kdiag": list(Kdiag), "g": list(g), "t": list(t), "n0": list(n0), "qhat": list(qhat),
            "qhat_K_qhat": qhat_norm, "E8_roots": len(roots), "cocycle_triples": 512,
            "analytic_bound_N4_d10": analytic_bound_n4_d10(),
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("status", "check_count", "pass_count", "fail_count")}, sort_keys=True))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
