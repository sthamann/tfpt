"""Floating finite-Fock vacuum kill test; NOT an asymptotic theorem."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("half_vacuum_source", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def run():
    _, source, _, _, _ = r.inherited()
    rows = []
    for n in (8, 16, 32):
        h = source.qwz_cylinder(n, 8, 1, 1)
        hn = source.qwz_cylinder(n, 8, 1, 3)
        values, vectors = np.linalg.eigh(h)
        destination = np.linalg.eigvalsh(hn)
        r.require(min(abs(values)) > 0.04, "diagnostic avoids ambiguous zero-mode occupation")
        occupied = vectors[:, values < 0]
        row = {"N": n, "unscaled_one_particle_gap": float(min(abs(values)))}
        for width in (2, 8):
            phase = r.phase_vector(n, 8, n//2-1, width)
            transformed = phase[:, None]*occupied
            excess = float(np.trace(transformed.conj().T@hn@transformed).real-sum(destination[destination < 0]))
            r.require(excess >= -1e-10, "transformed state is not below ground energy")
            row[f"width_{width}_unscaled_vacuum_energy_excess_one_copy"] = excess
        rows.append(row)
    return {"scope": "floating diagnostic, one copy, finite filled Fermi sea; no extrapolation theorem",
            "diagnostic_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "checker_sha256": hashlib.sha256((HERE/"checker.py").read_bytes()).hexdigest(),
            "source_sectors": [1, 3], "ny": 8, "rows": rows,
            "one_particle_low_mode_bounds_imply_vacuum_control": False,
            "raw_string_renormalization_or_smeared_field_limit_established": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(run(), sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.write_text(result)
    print(result)
