"""Independent normal/-OO reproduction and targeted mathematical mutants."""
from pathlib import Path
import json
import subprocess
import sys

here = Path(__file__).resolve().parent
rows = []
for optimized, mutant in [(False, None), (True, None),
                           (False, "conditioned_as_raw"), (False, "understate_bridge_norm")]:
    output = "coupled_and_instrument_optimized.json" if optimized else "coupled_and_instrument.json"
    command = [sys.executable]+(["-OO"] if optimized else [])
    command += [str(here/"coupled_and_instrument.py"), "--out", output]
    if mutant:
        command += ["--mutant", mutant]
    completed = subprocess.run(command, cwd=here, capture_output=True, text=True)
    good = completed.returncode != 0 if mutant else completed.returncode == 0
    if not good:
        raise RuntimeError(f"Unexpected subprocess result: {command}\n{completed.stdout}\n{completed.stderr}")
    rows.append({"optimized": optimized, "mutant": mutant, "returncode": completed.returncode,
                 "last_line": (completed.stderr or completed.stdout).strip().splitlines()[-1]})
equal = (here/"coupled_and_instrument.json").read_bytes() == (here/"coupled_and_instrument_optimized.json").read_bytes()
if not equal:
    raise RuntimeError("Normal and -OO outputs differ")
result = {"normal_optimized_byte_identical": equal, "all_mutants_detected": True, "runs": rows}
(here/"replay_coupled.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
print(json.dumps(result, indent=2))
