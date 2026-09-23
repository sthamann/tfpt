"""Read-only replay of the root protocol, plus the joint raw-error contract."""
from fractions import Fraction as F
from math import sqrt, pi, log, ceil
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT_SOURCE = HERE.parent/"exact_one_record_protocol.py"
CHECKS = []


def need(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(name)


def main():
    original_sha = hashlib.sha256(ROOT_SOURCE.read_bytes()).hexdigest()
    replays = []
    for optimized, name in [(False, "root_protocol_replay.json"),
                            (True, "root_protocol_replay_optimized.json")]:
        command = [sys.executable]+(["-OO"] if optimized else [])
        command += [str(ROOT_SOURCE), "--output", str(HERE/name)]
        completed = subprocess.run(command, cwd=HERE, capture_output=True, text=True)
        need(completed.returncode == 0, f"read-only root replay succeeds optimized={optimized}")
        data = json.loads((HERE/name).read_text())
        need(data["check_count"] == 531, "all 531 exact root checks replayed")
        need(data["source_sha256"] == original_sha, "root source hash stable through replay")
        replays.append(data)
    need(replays[0] == replays[1], "normal and optimized root replay content identical")
    need((HERE/"root_protocol_replay.json").read_bytes() == (HERE/"root_protocol_replay_optimized.json").read_bytes(),
         "normal and optimized root replay byte identical")
    retained, fresh = F(9, 64), F(153, 2048)
    gap = retained-fresh
    need(gap == F(135, 2048), "unconditional ideal contrast exactly 135/2048")
    for name, p in [("retained", retained), ("fresh", fresh)]:
        row = replays[0]["protocol"][name]
        need(F(row["raw_success"]) == p, name+" exact raw event weight")
        need(F(row["preparation_failure"])+F(row["end_failure_after_successful_prep_raw"])+p == 1,
             name+" complete flag distribution has unit mass")
    root_sum = sqrt(float(retained))+sqrt(float(fresh))
    duration = 280*pi
    critical_eta = float(gap)/(2*root_sum)
    symmetric_eta = float(gap)/(sqrt(root_sum**2+2*float(gap))+root_sum)
    need(critical_eta > symmetric_eta, "asymmetric probability intervals improve the absolute-error sum")
    need(abs((sqrt(float(retained))-critical_eta)**2-(sqrt(float(fresh))+critical_eta)**2) < 1e-15,
         "critical coherent bound closes the raw probability gap")
    rows = []
    for delta, q in [(1e-6, 1e-6), (1e-5, 1e-4), (5e-5, 1e-4), (6e-5, 1e-4)]:
        eta = duration*delta
        lower = max(0., max(0., sqrt(float(retained))-eta)**2-q)
        upper = min(1., (sqrt(float(fresh))+eta)**2+q)
        margin = lower-upper
        expected = float(gap)-2*root_sum*eta-2*q
        need(abs(margin-expected) < 1e-15, "equal coherent budgets cancel eta-squared terms in raw contrast")
        rows.append({"deltaH_over_Delta": delta, "extra_full_instrument_distance_per_branch": q,
                     "eta_per_branch": eta, "retained_raw_success_lower_bound": lower,
                     "fresh_raw_success_upper_bound": upper, "guaranteed_raw_difference": margin,
                     "certifies_positive_difference": margin > 0,
                     "scope_when_nonpositive": "no separation certified by this bound; not an actual failure result"})
    need(rows[2]["certifies_positive_difference"] and not rows[3]["certifies_positive_difference"],
         "both informative and noninformative robustness regimes retained")
    # Conservative finite-sample sufficient count per branch, separate from systematic error.
    selected_margin = rows[1]["guaranteed_raw_difference"]
    confidence_failure = .01
    samples = ceil(8*log(4/confidence_failure)/selected_margin**2)+1
    need(4*sqrt(log(4/confidence_failure)/(2*samples)) < selected_margin,
         "Hoeffding estimated-gap confidence interval excludes zero under the systematic margin")
    result = {"root_source_sha256": original_sha,
              "root_source_unchanged": hashlib.sha256(ROOT_SOURCE.read_bytes()).hexdigest() == original_sha,
              "root_normal_optimized_byte_identical": True, "root_checks_per_run": 531,
              "ideal_raw_retained": str(retained), "ideal_raw_fresh": str(fresh), "ideal_raw_gap": str(gap),
              "four_macro_duration_hbar_over_Delta": duration,
              "critical_eta_q0_asymmetric": critical_eta,
              "critical_eta_q0_symmetric_absolute_errors": symmetric_eta,
              "critical_deltaH_over_Delta_q0_asymmetric": critical_eta/duration,
              "critical_extra_instrument_distance_each_at_eta0": float(gap)/2,
              "bounds": rows,
              "sampling_example": {"confidence_failure_probability": confidence_failure,
                                   "independent_started_trials_per_branch_sufficient": samples,
                                   "systematic_margin": selected_margin,
                                   "method": "two-sided Hoeffding plus union bound; with probability at least 99 percent the resulting gap confidence interval excludes zero; assumes independent trials within each arm"},
              "checks": CHECKS, "check_count": len(CHECKS),
              "scope": "single started attempt including prep rejection and every end outcome; unbounded retry-until-prep-success is a different complete instrument"}
    need(result["root_source_unchanged"], "review never changed root source")
    result["check_count"] = len(CHECKS)
    (HERE/"one_record_end_review.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"checks": len(CHECKS), "root_checks_replayed_twice": 531, "bounds": rows,
                      "sampling_example": result["sampling_example"]}, indent=2))


if __name__ == "__main__":
    main()
