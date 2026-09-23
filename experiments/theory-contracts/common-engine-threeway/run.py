"""Run all three bounded research paths; write only an explicitly requested output."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform

import numpy as np
import scipy
import sympy as sp

import cell
import reverse
from source_adapter import HERE, PINS, verify_pins


def encode(value):
    if isinstance(value, (Fraction, sp.Basic)):
        return str(value)
    if isinstance(value, dict):
        return {str(key): encode(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(item) for item in value]
    return value


def run():
    verify_pins()
    return encode({
        "scope": "three bounded investigations; common TFPT-selected engine NOT constructed",
        "source_baseline_commit": "66b91e40e245569f06ab440ead80f446c9be0ee5",
        "source_pins": PINS,
        "runtime": {"python": platform.python_version(), "numpy": np.__version__,
                    "scipy": scipy.__version__, "sympy": sp.__version__},
        "forward": {"exact_electric_reduction": cell.hodge_record(),
                    "executed_plaquette": cell.run_cell(10)},
        "reverse": reverse.run_reverse(),
        "robustness": cell.robustness_record(),
        "all_T1_T8_remain_open": True,
        "same_source_plaquette_to_E8_intertwiner": "NOT_CONSTRUCTED",
        "own_code_sha256": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                            for name in ("source_adapter.py", "cell.py", "reverse.py", "run.py", "test_engine.py")},
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    content = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
