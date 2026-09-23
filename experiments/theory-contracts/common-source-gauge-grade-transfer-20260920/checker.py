"""Replay the delivered bounded algebra, with fixed input pins and OO parity.

Requires Python, numpy and sympy plus the declared local TFPT input snapshots.
No paper, ledger, graph or original source is changed by this checker.
"""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
JOBS = [
    ("gauge", "joint/check_gauge_section.py", "joint/gauge_section.json"),
    ("single_background", "joint/check_one_background.py", "joint/one_background.json"),
    ("transfer", "transfer/checker.py", "transfer/results.json"),
    ("flavor", "flavor/checker.py", "flavor/certificate.json"),
    ("phase", "phase_operator/checker.py", "phase_operator/result.json"),
]


def write_json(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def verify_inputs():
    manifest = json.loads((HERE / "source_manifest.json").read_text())
    entries = [(Path(e["path"]), e["sha256"]) for e in manifest["original_files"]]
    entries += [(HERE / e["path"], e["sha256"]) for e in manifest["package_dependencies"]]
    for path, wanted in entries:
        actual = sha256(path.read_bytes()).hexdigest() if path.is_file() else None
        if actual != wanted:
            raise RuntimeError("Input drift: " + str(path))
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=manifest["repository"], text=True).strip()
    if head != manifest["repository_head"]:
        raise RuntimeError("Repository HEAD drift; inspect before repinning")
    return len(manifest["original_files"]), len(manifest["package_dependencies"])


def checked_count(name, result):
    if name in ("gauge", "single_background"):
        if result["passed"] != result["total"] or not all(result["checks"].values()):
            raise RuntimeError(name + " failed an identity")
        return result["passed"]
    if name == "transfer":
        if result["status"] != "PASS_EXACT_TWO_SOURCE_TRANSFER_SEPARATION":
            raise RuntimeError("Transfer verdict changed")
        if result["event_gap"]["uniform_positive_gap_above_joint_kernel"] != "2 - sqrt(3)":
            raise RuntimeError("Transfer gap changed")
        return result["checks_passed"]
    if name == "flavor":
        if result["status"] != "PASS_EXACT_BOUNDED" or result["complete_TFPT_solution"]:
            raise RuntimeError("Flavor certificate failed or exceeded scope")
        if result["physical_gates_closed"]:
            raise RuntimeError("Flavor physical gate promotion is unauthorized")
        return result["checks"]
    if not result["status"].startswith("PASS"):
        raise RuntimeError("Phase certificate failed")
    if result["finite_spectral_trace_test"]["full_two_source_mu8_trace_coefficient_difference"] != "10080":
        raise RuntimeError("Phase trace coefficient changed")
    return result["checks_passed"]


def main():
    start = time.monotonic()
    original_count, own_count = verify_inputs()
    records, certificates = [], {}
    for name, script, output in JOBS:
        mode_hashes = []
        for mode in ("normal", "optimized"):
            command = [sys.executable, "-B"]
            if mode == "optimized":
                command.append("-OO")
            completed = subprocess.run(command + [str(HERE / script)], cwd=HERE,
                                       capture_output=True, text=True, timeout=120)
            if completed.returncode:
                raise RuntimeError(name + "/" + mode + ": " + completed.stdout + completed.stderr)
            data = (HERE / output).read_bytes()
            result = json.loads(data)
            count = checked_count(name, result)
            digest = sha256(data).hexdigest()
            mode_hashes.append(digest)
            records.append({"lane": name, "mode": mode, "exit_code": 0,
                            "checks": count, "certificate_sha256": digest})
            certificates[name] = result
        if mode_hashes[0] != mode_hashes[1]:
            raise RuntimeError(name + " normal and OO certificates differ")
    verify_inputs()
    counts = {name: checked_count(name, data) for name, data in certificates.items()}
    result = {
        "research_id": "TFPT.SOURCE.COMMON_LIFT.20260920",
        "execution": "PASS", "research_verdict": "PARTIAL",
        "original_inputs_verified": original_count,
        "package_dependency_pins_verified": own_count,
        "checks_per_lane": counts,
        "check_count_note": "Mechanical checks include pin/typing/negative controls and overlap; this is not a count of independent physical evidence.",
        "normal_optimized_byte_identity": True,
        "gauge": {"auxiliary_pair_hypercharges": [-1, 1], "full_10D_clock_lifts_changed": True,
                  "fixed_hypercharge_preserved": False, "source_selection": "OPEN"},
        "flavor": {"marked_complete_coefficient_symmetric": True,
                   "S_is_CAR_parity_or_all_left_v252_gamma": False,
                   "single_family_rank_bound": 2, "physical_current_to_fermion_descent": "OPEN",
                   "restricted_quadratic_pair_mixing": "QHP=0"},
        "single_background": {"result": "F(h)=f(norm(h)^2) epsilon*h",
                              "premises": "One nonzero vector, exact SU3 covariance in bar3 tensor bar3, U1 degree +1, no other oriented tensor input",
                              "analyticity_required": False, "full_TFPT_no_go": False},
        "transfer": {"joint_event_gap": "2-sqrt(3)", "QVP": "0", "QLP": "nonzero",
                     "leakage_branch_norm_squared": "1/7200",
                     "common_W_condition": "J(2-sqrt(3))-4kappa-2mu>2kappa",
                     "scope": "Two sources only; actual H spectral projector; coupling choice not derived"},
        "phase": {"common_phase_H_response": "exactly zero",
                  "relative_diagnostic_first_nonconstant_full_label_moment": 8,
                  "all_observables_blind_through_7": False,
                  "label_trace_difference": "315/2", "full_mu8_coefficient_difference": "10080",
                  "a0_to_delta_map": "OPEN"},
        "same_source_identification_between_compiler_QWZ_E8_edge": "OPEN",
        "closed_gate_ids": [], "T1_T8_closed": [], "complete_physical_solution": False,
    }
    write_json("results.json", result)
    write_json("validation.json", {"execution": "PASS", "runs": records,
        "original_inputs_verified_before_and_after": original_count,
        "own_pins_verified_before_and_after": own_count,
        "normal_optimized_byte_identity_all_five_lanes": True,
        "elapsed_seconds": round(time.monotonic()-start, 3),
        "scope": "Bounded algebra replay and input integrity, not a full suite or physical proof."})
    print(json.dumps({"execution": "PASS", "research_verdict": "PARTIAL",
                      "checks_per_lane": counts, "byte_identity_all": True,
                      "original_inputs_verified": original_count}))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failure = {"execution": "FAIL", "reason": str(exc), "complete_physical_solution": False}
        write_json("validation.json", failure)
        write_json("results.json", failure)
        raise
