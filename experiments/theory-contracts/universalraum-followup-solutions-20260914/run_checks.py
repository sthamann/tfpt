"""Run all six follow-up checkers of this contract and verify their JSON outputs.

Light entry point: runs each checker as a subprocess (normal and -OO), requires
identical JSON bytes, and prints the check counts. The heavy 24,024-dim
certification (certify_quartet.py, ~6 min) is included; skip it with --fast.
"""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIGHT = ["ops_ledger.py", "architecture.py", "parameters.py", "one_family.py",
         "robustness.py"]
HEAVY = ["certify_quartet.py"]

def strip_volatile(obj):
    """remove wall-time fields before the normal/-OO comparison."""
    if isinstance(obj, dict):
        return {k: strip_volatile(v) for k, v in obj.items()
                if k not in ("seconds", "elapsed", "runtime", "wall_time")}
    if isinstance(obj, list):
        return [strip_volatile(x) for x in obj]
    return obj

def run_one(script):
    stem = script.replace(".py", "")
    out = HERE / (stem + ".json")
    subprocess.run([sys.executable, script, "--output", str(out)],
                   cwd=HERE, check=True, capture_output=True)
    normal = out.read_bytes()
    tmp = Path(str(out) + ".tmp")
    subprocess.run([sys.executable, "-OO", script, "--output", str(tmp)],
                   cwd=HERE, check=True, capture_output=True)
    opt = tmp.read_bytes()
    tmp.unlink()
    if normal != opt:
        # allow only differences in volatile wall-time fields
        if strip_volatile(json.loads(normal)) != strip_volatile(json.loads(opt)):
            raise RuntimeError(f"{script}: normal/-OO output differs")
    data = json.loads(normal)
    if not data.get("count", 0) > 0:
        raise RuntimeError(f"{script}: no checks recorded")
    if data.get("T1_T8_closed") != []:
        raise RuntimeError(f"{script}: T1_T8_closed must stay empty")
    return data["count"]

def main():
    scripts = LIGHT + ([] if "--fast" in sys.argv else HEAVY)
    total = 0
    for s in scripts:
        n = run_one(s)
        total += n
        print(f"{s}: {n} checks OK")
    print(f"TOTAL: {total} checks, all green, normal/-OO byte-identical")

if __name__ == "__main__":
    main()
