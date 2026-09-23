"""Replay own checks, reject two false-origin mutants, and review root protocol."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
PYTHON = "/opt/homebrew/bin/python3"


def run(arguments):
    result = subprocess.run([PYTHON, *arguments], cwd=HERE, capture_output=True, text=True)
    return {"argv": arguments, "returncode": result.returncode,
            "stdout_tail": result.stdout[-1200:], "stderr_tail": result.stderr[-1200:]}


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


rows = []
for flags, output in [([], "origin_verification.json"), (["-OO"], "origin_verification_optimized.json")]:
    result = run([*flags, str(HERE/"origin_probe.py"), "--out", output])
    need(result["returncode"] == 0, "own origin replay failed")
    rows.append(result)
need((HERE/"origin_verification.json").read_bytes() == (HERE/"origin_verification_optimized.json").read_bytes(),
     "own origin normal/-OO outputs differ")
for mutant in ["local_controls_make_Q", "spectators_unchanged"]:
    result = run([str(HERE/"origin_probe.py"), "--mutant", mutant, "--out", "must_not_exist.json"])
    need(result["returncode"] != 0 and "MUTANT:" in result["stderr_tail"], "false resource mutant escaped")
    rows.append(result)
root_probe = HERE.parent/"fundamental_record_execution/mediator_record.py"
root_sha = hashlib.sha256(root_probe.read_bytes()).hexdigest()
for flags, output in [([], "root_mediator_replay.json"), (["-OO"], "root_mediator_replay_optimized.json")]:
    result = run([*flags, str(root_probe), "--output", str(HERE/output)])
    need(result["returncode"] == 0, "root mediator replay failed")
    rows.append(result)
need(root_sha == hashlib.sha256(root_probe.read_bytes()).hexdigest(), "root source changed during replay")
need((HERE/"root_mediator_replay.json").read_bytes() == (HERE/"root_mediator_replay_optimized.json").read_bytes(),
     "root mediator normal/-OO outputs differ")
report = {"status": "PASS", "own_check_count": json.loads((HERE/"origin_verification.json").read_text())["check_count"],
          "normal_optimized_byte_identical": True, "mutants_rejected": 2,
          "root_mediator_check_count": json.loads((HERE/"root_mediator_replay.json").read_text())["check_count"],
          "root_mediator_sha256": root_sha, "runs": rows}
(HERE/"replay.json").write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps({k:v for k,v in report.items() if k != "runs"}, indent=2))
