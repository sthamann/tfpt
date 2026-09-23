"""F4 modular period readout lane — native modmul compiler audit (NON-RH, unpromoted).

Separates ORACLE_SPECIFICATION of modular multiplication from compilation through
pinned audited U/F4 primitives. Toys N=15 and N=35; asymptotic guards vs poly(b).
No factoring/RH/P=NP claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

MANIFEST = HERE / "source_manifest.json"
CHECKS: list[dict] = []

VERDICTS = (
    "NATIVE_POLYLOG_MODMUL_FOUND",
    "SHOR_IMPLEMENTATION_ONLY",
    "BLOCKED_MISSING_NATIVE_COMPILER",
    "BLOCKED_ORACLE_ONLY",
)

# Audited dimensions from paired-release verification (pinned hash).
AUDITED_DIMS = {
    "matter_Hmat": 256,
    "microscopic_star_block": 544,
    "local_F4_full_columns": 832,
    "common_carrier_with_one_mediator": 832,
    "clocked_record_macro": 6656,
}

# Declared primitive surface (no mod-N parameterization in pinned check.py).
AUDITED_PRIMITIVE_SURFACE = [
    "four_carrier_F4_word_evaluation",
    "microscopic_boson_exchange_paths",
    "22D_U0_involution_and_record_macro",
    "256D_matter_sector",
    "544D_closed_star_Gram_block",
    "832D_common_carrier_edge_embedding",
    "E8_quadratic_Fourier_output_law_on_fixed_small_moduli",
    "amplification_two_step_phase_polynomial",
    "classical_factor_blind_gcd_moment_roundtrip",
]

DEAD_ROUTES = [
    "quadratic_E8_FFT_uniform_at_coprime_ticks",
    "E8_tree_contraction_O_N3_readout",
]


def require(ok: bool, name: str, kind: str = "exact") -> None:
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append({"name": name, "kind": kind})


def pin_sources() -> dict:
    manifest = json.loads(MANIFEST.read_text())
    pins = {}
    for row in manifest["sources"]:
        rel = row["path"]
        digest = row["sha256"]
        data = (ROOT / rel).read_bytes()
        got = hashlib.sha256(data).hexdigest()
        require(got == digest, "source pin " + rel)
        pins[rel] = digest
    return pins


def load_r647() -> dict:
    path = ROOT / "experiments/tfpt-discovery/e8_composite_gauss_result.json"
    data = json.loads(path.read_text())
    require(data.get("verdict") == "E8_COUNT_FACTOR_EQUIVALENT_NO_FAST_READOUT", "r647 verdict pinned")
    require(data["checks"]["G3 tree sums equal N^4*gcd(t,N)^4"], "r647 G3")
    require(data["checks"]["G7 tree contraction is cubic with generic bond N"], "r647 G7")  # MUTANT_ANCHOR_R647_G7
    require(data["checks"]["G8 rare nonunit sampling is sqrt(N), amplitude N^(1/4)"], "r647 G8")
    return data


def load_audit_snapshot() -> dict:
    path = ROOT / "experiments/theory-contracts/universalraum-paired-release-20260914/new-input-audit/verification.json"
    data = json.loads(path.read_text())
    require(data["local_F4_full_columns"] == AUDITED_DIMS["local_F4_full_columns"], "audit 832 columns")
    require("closed microscopic star block 544" in {c["name"] for c in data["checks"]}, "audit 544 block check present")
    return {
        "local_F4_full_columns": data["local_F4_full_columns"],
        "F4_scope": data["F4_scope"],
        "factor_graph_configured_path": False,
    }


def multiplicative_order(a: int, n: int) -> tuple[int | None, int]:
    g = gcd(a, n)
    if g != 1:
        return None, g
    x = 1
    for r in range(1, n + 1):
        x = (x * a) % n
        if x == 1:
            return r, 1
    raise RuntimeError("order not found")


def factors_from_period(a: int, n: int, r: int) -> list[int]:
    z = pow(a, r // 2, n)
    if z == n - 1:
        return []
    out = []
    for t in (z - 1, z + 1):
        g = gcd(t, n)
        if 1 < g < n:
            out.append(g)
    return sorted(set(out))


def oracle_modmul_specification(n: int, a: int) -> dict:
    """Direct permutation from y -> a*y mod N; explicitly not native compilation."""
    require(gcd(a, n) == 1, "oracle modmul base is coprime N=" + str(n))
    rows = []
    for y in range(n):
        target = (a * y) % n
        rows.append({"y": y, "image": target})
    require(len({row["image"] for row in rows}) == n, "oracle table is permutation N=" + str(n))
    return {
        "label": "ORACLE_SPECIFICATION",
        "modulus": n,
        "base": a,
        "permutation_rows": n,
        "dense_one_hot_table_bits_if_materialized": n * n,
        "compact_arithmetic_description": "(N,a): y -> a*y mod N",
        "compiled_primitive_count_from_audit": 0,
        "native_compilation": False,
        "rows": rows,
    }


def arithmetic_specification_cost(n: int) -> dict:
    b = n.bit_length()
    return {
        "modulus": n,
        "bit_length": b,
        "dense_one_hot_table_bits_if_materialized": n * n,
        "classical_orbit_enumeration_ops": n,  # worst-case order <= n
        "gcd_moment_acquisition_ops": n,  # r647: sum over t mod N
    }


def search_native_modmul_compiler(n: int) -> dict:
    """Scan declared audited interface for (N,a)-parameterized modmul — none found."""
    b = n.bit_length()
    matter = AUDITED_DIMS["matter_Hmat"]
    obstruction = [
        "pinned_interface_has_fixed_256D_matter_sector_and_no_N_indexed_scaling_family"
    ]
    if n > matter:
        obstruction.append("full_Z_N_regular_representation_requires_dim>=N_but_audited_matter=256")
    # Even for n<=256, pinned interface has no modulus register or controlled multiply API.
    missing = [
        "controlled_modular_multiply_U_a_on_Z_N_register",
        "scalable_QFT_on_exponent_register",
        "parameterized_semiprime_factor_graph_compiler",
    ]
    found = [p for p in AUDITED_PRIMITIVE_SURFACE if "mod" in p.lower() and str(n) in p]
    require(len(found) == 0, "no accidental mod-N primitive name")
    return {
        "modulus": n,
        "bit_length": b,
        "audited_primitive_surface": list(AUDITED_PRIMITIVE_SURFACE),
        "missing_native_apis": missing,
        "fixed_dimension_obstruction": obstruction,
        "evidence_scope": "declared pinned interface inventory; not a universal circuit lower bound",
        "native_modmul_compiler": False,
        "factor_graph_configured_path": False,
    }


def shor_reference_cost(n: int) -> dict:
    b = max(2, n.bit_length())
    # Standard counting model: b^2 qubits, b controlled modmuls, poly(b) per modmul assumed.
    return {
        "bit_length": b,
        "reference": "Shor 1995 circuit model (conditional on native modmul+QFT)",
        "exponent_register_qubits_theta_b_squared": b * b,
        "controlled_modmul_repetitions": b,
        "intended_total_quantum_gates_theta_b_cubed": b ** 3,
        "classical_postprocess_theta_b_cubed": b ** 3,
        "requires_oracle_if_modmul_not_native": True,
    }


def asymptotic_guards(r647: dict) -> dict:
    sampling = r647.get("sampling", {})
    cost_rows = {row["N"]: row for row in r647.get("cost_rows", [])}
    guards = []
    for n in (15, 35):
        b = n.bit_length()
        row = cost_rows.get(n)
        require(row is not None, "r647 cost row N=" + str(n))
        tree_ops = row["tree_ops"]
        guards.append(
            {
                "modulus": n,
                "bit_length": b,
                "negative_O_N_moment_ops": n,
                "negative_tree_ops_O_N3": tree_ops,
                "tree_ops_over_n_cubed": tree_ops / (n ** 3),
                "polylog_target_ops_theta_b_cubed": b ** 3,
                "tree_beats_polylog": tree_ops > (b ** 3) * 100,
                "oracle_perm_bits_n_squared": n * n,
                "direct_perm_synthesis_blocked_without_oracle": True,
            }
        )
    amp = float(sampling.get("amplitude_queries", 0))
    classical = float(sampling.get("classical_queries", 0))
    if classical > 0:
        ratio = amp / classical
        guards.append(
            {
                "r647_sampling_amplitude_over_classical": ratio,
                "expected_N_quarter_scaling_class": "N^(1/4) useful tick amplification",
                "polylog_incompatible": ratio > 0.01,
            }
        )
    guards.append({"dead_route": DEAD_ROUTES[0], "status": "do_not_retry"})
    return {"guards": guards, "dead_routes": DEAD_ROUTES}


def run_toy(n: int, a: int, *, coprime_fallback: int | None = None) -> dict:
    g = gcd(a, n)
    period_info: dict
    if g == 1:
        period_base = a
        immediate_factor = None
    else:
        fb = coprime_fallback
        require(fb is not None and gcd(fb, n) == 1, "coprime fallback for N=" + str(n))
        period_base = fb
        immediate_factor = g
    spec = oracle_modmul_specification(n, period_base)
    arith = arithmetic_specification_cost(n)
    native = search_native_modmul_compiler(n)
    r, _ = multiplicative_order(period_base, n)
    fac = factors_from_period(period_base, n, r)
    if immediate_factor is None:
        period_info = {
            "base": period_base,
            "order": r,
            "gcd": 1,
            "nontrivial_factors_from_period": fac,
        }
    else:
        period_info = {
            "requested_base": a,
            "requested_gcd": immediate_factor,
            "requested_base_already_reveals_factor": True,
            "period_base_used": period_base,
            "order": r,
            "nontrivial_factors_from_period": fac,
        }
    require(spec["label"] == "ORACLE_SPECIFICATION", "oracle label toy N=" + str(n))  # MUTANT_ANCHOR_ORACLE
    require(not native["native_modmul_compiler"], "native compiler absent N=" + str(n))
    return {
        "modulus": n,
        "oracle_modmul": spec,
        "arithmetic_specification_cost": arith,
        "native_compiler_search": native,
        "period_readout": period_info,
        "compiled_primitive_count": 0,
        "dense_one_hot_table_bits_if_materialized": spec["dense_one_hot_table_bits_if_materialized"],
    }


def decide_verdict(toys: list[dict], native_global: bool) -> str:
    if native_global:
        return "NATIVE_POLYLOG_MODMUL_FOUND"
    any_oracle = all(t["oracle_modmul"]["label"] == "ORACLE_SPECIFICATION" for t in toys)
    if any_oracle:
        # Period extraction works classically/oracle-only; Shor stack not native.
        return "BLOCKED_MISSING_NATIVE_COMPILER"
    return "BLOCKED_ORACLE_ONLY"


def record() -> dict:
    global CHECKS
    CHECKS = []
    pins = pin_sources()
    r647 = load_r647()
    audit = load_audit_snapshot()
    toys = [
        run_toy(15, 7),
        run_toy(35, 7, coprime_fallback=3),
    ]
    require(toys[0]["period_readout"]["order"] == 4, "N=15 a=7 order 4")  # MUTANT_ANCHOR_TOY15_ORDER
    require(toys[0]["period_readout"]["nontrivial_factors_from_period"] == [3, 5], "N=15 factors")
    require(toys[1]["period_readout"]["order"] == 12, "N=35 a=3 order 12")
    require(set(toys[1]["period_readout"]["nontrivial_factors_from_period"]) == {5, 7}, "N=35 factors")
    require(toys[1]["oracle_modmul"]["base"] == 3, "N=35 oracle table uses coprime period base")
    scaling = asymptotic_guards(r647)
    for g in scaling["guards"]:
        if "tree_beats_polylog" in g:
            require(g["tree_beats_polylog"], "O(N^3) tree not polylog N=" + str(g["modulus"]))
    native_global = all(t["native_compiler_search"]["native_modmul_compiler"] for t in toys)
    require(not native_global, "global native compiler must stay false")  # MUTANT_ANCHOR_NATIVE_FALSE
    verdict = decide_verdict(toys, native_global)
    require(verdict in VERDICTS, "verdict enum")
    require(verdict == "BLOCKED_MISSING_NATIVE_COMPILER", "expected blocked verdict")  # MUTANT_ANCHOR_VERDICT
    shor = {str(n): shor_reference_cost(n) for n in (15, 35)}
    return {
        "contract": "F4.MODULAR.PERIOD.READOUT.20260914",
        "fence": "Experiments only; no factoring breakthrough; no RH; no P=NP",
        "verdict": verdict,
        "native_modmul_compiler": False,
        "audited_dimensions": AUDITED_DIMS,
        "audit_snapshot": audit,
        "r647_cross_checks": {
            "verdict": r647["verdict"],
            "G7_cubic": True,
            "G8_N_quarter": True,
        },
        "toys": toys,
        "asymptotic_guards": scaling,
        "shor_reference_cost": shor,
        "pins": pins,
        "claims_not_made": [
            "no polylog factoring breakthrough",
            "no RH or P=NP statement",
            "no ledger or paper promotion",
        ],
        "checks": CHECKS,
        "count": len(CHECKS),
    }


def run_replay() -> None:
    checker = HERE / "checker.py"
    original = checker.read_bytes()
    env = {"OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1"}

    def run_py(args: list[str]) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, *args],
            cwd=HERE,
            capture_output=True,
            text=True,
            env={**dict(__import__("os").environ), **env},
            timeout=120,
        )

    out_n = run_py(["-B", str(checker), "--output", str(HERE / "validation.json")])
    out_o = run_py(["-B", "-OO", str(checker), "--output", str(HERE / "validation_optimized.json")])
    if out_n.returncode or out_o.returncode:
        raise RuntimeError(out_n.stderr + out_o.stderr)
    if (HERE / "validation.json").read_bytes() != (HERE / "validation_optimized.json").read_bytes():
        raise ValueError("normal and -OO validation differ")
    text = original.decode()
    mutations = [
        ("N=15 a=7 order 4", "MUTANT_ANCHOR_TOY15_ORDER", "== 4,", "== 5,"),
        ("native compiler must stay false", "MUTANT_ANCHOR_NATIVE_FALSE", "not native_global", "native_global"),
        (
            "oracle label toy",
            "MUTANT_ANCHOR_ORACLE",
            "ORACLE_SPECIFICATION",
            "NATIVE_COMPILATION",
        ),
        (
            "r647 G7 cubic",
            "MUTANT_ANCHOR_R647_G7",
            'require(data["checks"]["G7 tree contraction is cubic with generic bond N"], "r647 G7")',
            'require(False, "r647 G7")',
        ),
        (
            "expected blocked verdict",
            "MUTANT_ANCHOR_VERDICT",
            '"BLOCKED_MISSING_NATIVE_COMPILER"',
            '"NATIVE_POLYLOG_MODMUL_FOUND"',
        ),
    ]
    caught = []
    for name, anchor, old, new in mutations:
        if anchor:
            idx = text.index(anchor)
            line_start = text.rfind("\n", 0, idx) + 1
            line_end = text.find("\n", idx)
            line = text[line_start:line_end]
            if old not in line:
                raise ValueError("mutation anchor miss: " + name)
            changed = text[:line_start] + line.replace(old, new, 1) + text[line_end:]
        else:
            if text.count(old) != 1:
                raise ValueError("mutation not unique: " + name)
            changed = text.replace(old, new, 1)
        code = (
            "_path = "
            + repr(str(checker))
            + "\n_ns = {'__file__': _path, '__name__': 'mutation_probe'}\nexec(compile("
            + repr(changed)
            + ", _path, 'exec'), _ns)\n_ns['record']()\n"
        )
        proc = run_py(["-B", "-c", code])
        err = proc.stderr + proc.stdout
        if proc.returncode == 0:
            raise ValueError("mutant survived: " + name)
        if "RuntimeError" not in err:
            raise ValueError("mutant wrong failure for " + name + ":\n" + err)
        caught.append({"mutation": name, "stderr_tail": err.strip().splitlines()[-1:]})
    digest = hashlib.sha256(original).hexdigest()
    replay = {
        "normal_OO_byte_identical": True,
        "checker_sha256": digest,
        "mutants_caught": caught,
        "own_checks": json.loads((HERE / "validation.json").read_text())["count"],
        "verdict": json.loads((HERE / "validation.json").read_text())["verdict"],
        "T1_T8_closed": [],
    }
    (HERE / "replay.json").write_text(json.dumps(replay, indent=2) + "\n")
    print(json.dumps(replay, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="write validation JSON")
    parser.add_argument("--replay", action="store_true", help="run validation + mutants")
    args = parser.parse_args()
    if args.replay:
        run_replay()
        return
    result = record()
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    payload = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload)
    slim = {k: v for k, v in result.items() if k not in ("checks", "toys")}
    slim["toy_summary"] = [
        {
            "modulus": t["modulus"],
            "order": t["period_readout"].get("order"),
            "factors": t["period_readout"].get("nontrivial_factors_from_period"),
            "dense_one_hot_bits_if_materialized": t["dense_one_hot_table_bits_if_materialized"],
        }
        for t in result["toys"]
    ]
    print(json.dumps(slim, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
