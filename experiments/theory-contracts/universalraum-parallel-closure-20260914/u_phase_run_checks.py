"""Normal / -OO replay and in-memory mutants for u_phase_audit.py."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
CHECKER = HERE / "u_phase_audit.py"
ORIGINAL = CHECKER.read_bytes()


def run_py(opt, out_name):
    t0 = time.time()
    subprocess.run(
        [sys.executable, *opt, str(CHECKER), "--output", str(HERE / out_name)],
        check=True,
        cwd=str(HERE),
    )
    return time.time() - t0


def main():
    elapsed = 0.0
    for opt, out in ([], "u_phase_validation.json"), (["-OO"], "u_phase_validation_optimized.json"):
        elapsed += run_py(opt, out)
    if (HERE / "u_phase_validation.json").read_bytes() != (
        HERE / "u_phase_validation_optimized.json"
    ).read_bytes():
        raise RuntimeError("normal/optimized divergence")
    if CHECKER.read_bytes() != ORIGINAL:
        raise RuntimeError("checker changed while running")

    text = ORIGINAL.decode()
    mutations = [
        ("ordered history rank", "require(int(L.rank()) == 12", "require(int(L.rank()) == 11"),
        ("U_W unitarity", "U_W.H * U_W - s.eye(22)) == s.zeros(22)",
         "U_W.H * U_W - s.eye(22)) == s.ones(22)"),
        ("U theta distinction", "require(overlap == 0,", "require(overlap == 1,"),
        ("phase verdict", 'require(verdict == "BLOCKED_MISSING_NATIVE_PHASE_DATA"',
         'require(verdict == "NATIVE_PHASE_COMPARATOR_OK"'),
        ("K Gram identity", "K.T * K == eye - swap", "K.T * K == eye"),
        ("tetramer degeneracy", "k4[-6] == 24", "k4[-6] == 23"),
    ]
    caught = []
    for name, old, new in mutations:
        if old not in text:
            raise RuntimeError("missing mutation anchor: " + name)
        ns = {"__name__": "mutation_probe", "__file__": str(CHECKER)}
        exec(compile(text.replace(old, new, 1), str(CHECKER), "exec"), ns)
        try:
            ns["run"]()
        except RuntimeError as e:
            caught.append({"mutation": name, "gate": str(e)})
        else:
            raise RuntimeError("surviving mutant: " + name)

    val = json.loads((HERE / "u_phase_validation.json").read_text())
    payload = {
        "lane": "History/U/non-identifiability/native-phase",
        "normal_OO_byte_identical": True,
        "checker_sha256": hashlib.sha256(ORIGINAL).hexdigest(),
        "mutants_caught": caught,
        "own_checks": val["count"],
        "phase_adapter_verdict": val["phase_adapter_verdict"],
        "CAR_native_phase_equivalence": val["CAR_native_phase_equivalence"],
        "U_theta": val["P1_P2_non_identifiability"],
        "seconds": round(elapsed, 2),
        "T1_T8_closed": [],
    }
    (HERE / "u_phase_replay.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
