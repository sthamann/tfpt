"""Normal / -OO replay and in-memory mutants for c16_parallel_closure.py."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
CHECKER = HERE / "c16_parallel_closure.py"
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
    for opt, out in [([], "validation.json"), (["-OO"], "validation_optimized.json")]:
        elapsed += run_py(opt, out)
    if (HERE / "validation.json").read_bytes() != (HERE / "validation_optimized.json").read_bytes():
        raise RuntimeError("normal/optimized divergence")
    if CHECKER.read_bytes() != ORIGINAL:
        raise RuntimeError("checker changed while running")

    text = ORIGINAL.decode()
    mutations = [
        ("Schur ratio", "Fraction(160, 1) * t_over_D", "Fraction(200, 1) * t_over_D"),
        ("F4 overlap norm", "160 * 8 + 60 * 8", "160 * 4 + 60 * 8"),
        ("competition margin", "margin > 0", "margin > 1e6"),
        ("singlet dimension", "d == 24024", "d == 24023"),
        ("baseline count", 'baseline["count"] == 891', 'baseline["count"] == 890'),
        ("Aut order", "AUT_ORDER = 1920", "AUT_ORDER = 1921"),
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

    val = json.loads((HERE / "validation.json").read_text())
    payload = {
        "normal_OO_byte_identical": True,
        "checker_sha256": hashlib.sha256(ORIGINAL).hexdigest(),
        "mutants_caught": caught,
        "own_checks": val["count"],
        "flags": val["flags"],
        "seconds": round(elapsed, 2),
        "T1_T8_closed": [],
    }
    (HERE / "replay.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
