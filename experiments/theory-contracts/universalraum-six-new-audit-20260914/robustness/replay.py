"""Run normal/optimized probes and require four deliberate mutations to fail."""
from pathlib import Path
import json
import subprocess
import sys

here = Path(__file__).resolve().parent
reports = []
commands = [([], "verification.json", None), (["-OO"], "verification_optimized.json", None)]
commands += [([], "unused.json", name) for name in
             ("pretend_invariant", "omit_phase_repair", "ignore_conditioning", "combine_sigma_F9")]
for flags, output, mutation in commands:
    command = [sys.executable]+flags+[str(here/"probe.py"), "--out", output]
    if mutation:
        command += ["--mutant", mutation]
    run = subprocess.run(command, cwd=here, text=True, capture_output=True)
    expected = run.returncode != 0 if mutation else run.returncode == 0
    if not expected:
        raise RuntimeError(f"unexpected status {run.returncode}: {command}\n{run.stdout}\n{run.stderr}")
    reports.append({"mutation": mutation, "optimized": bool(flags), "returncode": run.returncode,
                    "last_line": (run.stderr or run.stdout).strip().splitlines()[-1]})
same = (here/"verification.json").read_bytes() == (here/"verification_optimized.json").read_bytes()
if not same:
    raise RuntimeError("normal and -OO outputs differ")
result = {"normal_optimized_byte_identical": same, "runs": reports,
          "all_mutations_detected": True}
(here/"replay.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
print(json.dumps(result, indent=2))
