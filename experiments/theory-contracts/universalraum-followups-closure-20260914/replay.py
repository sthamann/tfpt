"""Replay the follow-up checkers, compare -OO, and reject scoped mutants.

The lightweight modules run by default.  The heavy numerical ones need several
minutes per pass and only run when named explicitly with --only; their
conditions are counted the same way once they do.
"""
from pathlib import Path
import subprocess, sys, json, hashlib

HERE = Path(__file__).resolve().parent
MODULES = ["architecture", "primitives", "native_family", "matching_joint", "coupled_cells"]
HEAVY = ["quartet_cert"]
MUTANTS = [
    ("architecture", "run", "bond = tuple(x + y for x, y in zip(s, t))",
     "bond = tuple(x - y for x, y in zip(s, t))", "bond label read off the wrong combination"),
    ("architecture", "run", "(min(4, n + 1) if per_bond else 1)", "(min(2, n + 1) if per_bond else 1)",
     "shared bank Schur norm weakened"),
    ("primitives", "record_sector", "tuple(2 * x for x in e)", "tuple(4 * x for x in e)",
     "wrong normalisation of the vector weights of the record sector"),
    ("primitives", "record_reduction", "R = np.kron(Pp, np.eye(2)) + np.kron(Pm, X)",
     "R = np.kron(Pm, np.eye(2)) + np.kron(Pp, X)", "record heralds the wrong sector"),
    ("native_family", "common_cone_and_chirality", "V_CHAIN = pi / 4", "V_CHAIN = pi / 3",
     "second velocity on the same chain"),
    ("native_family", "graviton_polarisations", "/ (d - 1)", "/ d",
     "transverse traceless filter is no longer a projector"),
    ("coupled_cells", "anchors", "return (v + v[PERM_AB]) / 2.0", "return (v - v[PERM_AB]) / 2.0",
     "bridge built as the antisymmetric instead of the symmetric half-sum"),
    ("coupled_cells", "clock_budget", "mult = np.array([1, 30, 45, 40, 15, 90, 35])",
     "mult = np.array([1, 30, 45, 40, 15, 80, 35])", "star level multiplicities no longer exhaust the 256 sector"),
    ("matching_joint", "joint_fit_block",
     'N_from_As = float(np.sqrt(24 * PI ** 2 * (np.exp(val("lnAs")) * 1e-10) / C3 ** 7))',
     'N_from_As = float(np.sqrt(24 * PI ** 2 * (np.exp(val("lnAs")) * 1e-10) / C3 ** 6))',
     "wrong power of c3 in the amplitude matching relation"),
    ("matching_joint", "joint_fit_block", 'N_from_ns = float(2.0 / (1.0 - val("ns")))',
     'N_from_ns = float(3.0 / (1.0 - val("ns")))', "wrong tilt matching relation"),
    ("quartet_cert", "label_block_bound", "-8.0 * regular_sum", "-6.0 * regular_sum",
     "wrong swap coefficient in the shared-bank label block"),
    ("quartet_cert", "operator_bound_certificate", "edge_coefficients[1] + 12",
     "edge_coefficients[1] - 12", "cross term added to the edge bound with the wrong sign"),
]


def main(only=None):
    selected = [m for m in MODULES if only is None or m in only]
    selected += [m for m in HEAVY if only is not None and m in only]
    report = {"replays": {}, "mutants": [], "T1_T8_closed": []}
    for name in selected:
        path = HERE / (name + ".py")
        if not path.exists():
            continue
        for optimized, suffix in [(False, ""), (True, "_optimized")]:
            cmd = [sys.executable] + (["-OO"] if optimized else []) + \
                  [str(path), "--output", str(HERE / (name + suffix + ".json"))]
            p = subprocess.run(cmd, cwd=HERE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if p.returncode:
                raise RuntimeError(p.stdout.decode())
        a = (HERE / (name + ".json")).read_bytes()
        b = (HERE / (name + "_optimized.json")).read_bytes()
        if a != b:
            raise RuntimeError(name + " normal/OO mismatch")
        report["replays"][name] = {"byte_identical": True, "count": json.loads(a)["count"],
                                   "output_sha256": hashlib.sha256(a).hexdigest()}
    for name, fn, old, new, label in MUTANTS:
        path = HERE / (name + ".py")
        if not path.exists() or name not in selected:
            continue
        src = path.read_text()
        if src.count(old) != 1:
            raise RuntimeError("mutation target not unique: " + label)
        ns = {"__name__": "mutant", "__file__": str(path)}
        exec(compile(src.replace(old, new), str(path), "exec"), ns)
        try:
            ns[fn]()
        except RuntimeError as e:
            report["mutants"].append({"label": label, "caught_by": str(e)})
        else:
            raise RuntimeError("surviving mutant " + label)
    report["total_conditions"] = sum(x["count"] for x in report["replays"].values())
    (HERE / "replay.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", default=None, choices=MODULES + HEAVY)
    main(ap.parse_args().only)
