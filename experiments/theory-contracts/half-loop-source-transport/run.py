"""Replay source half-loop construction and its open dynamical acceptance tests."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np
import sympy as sp

import checker
import energy_matching


def encode(value):
    if isinstance(value, (Fraction, sp.Basic)):
        return str(value)
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def run():
    checker.verify_pins()
    return encode({
        "scope": "source-supported candidate on the declared physical plaquette, NOT the E8 half-charge field",
        "baseline_commit": "66b91e40e245569f06ab440ead80f446c9be0ee5",
        "source_pins": checker.PINS,
        "matter_assisted_root": checker.root_certificate(),
        "actual_dynamics_test": checker.dynamical_test(),
        "diagonal_charge_test": checker.diagonal_charge_test(),
        "scalar_root_comparison": checker.scalar_root_test(),
        "executed_same_source_sequence": checker.numerical_transport(),
        "full_energy_matching": energy_matching.energy_gate(),
        "source_holonomy_pair_check": energy_matching.sourced_pair_check(),
        "all_T1_T8_remain_open": True,
        "source_selected_half_charge_field": "NOT_CONSTRUCTED",
        "local_code_sha256": {name: hashlib.sha256((checker.HERE / name).read_bytes()).hexdigest()
                              for name in ("checker.py", "energy_matching.py", "run.py", "test_checker.py")},
    })


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(run(), sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(result)
    else:
        print(result, end="")
