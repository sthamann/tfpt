"""Exact C6 census; exterior square is a comparison, not a physical Fock claim."""
import argparse
from collections import Counter
import hashlib
import importlib.util
from itertools import combinations
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def construct():
    spec = importlib.util.spec_from_file_location("clock_type_source", HERE / "checker.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    source = module.exact_source_prefix()
    clock = sp.zeros(16)
    for i, j in enumerate(source["img"]):
        clock[j, i] = 1
    boundary = sp.diag(*([0] * 10 + [1] * 6))
    return clock, boundary, source["provenance"]


def exterior_square(matrix):
    pairs = list(combinations(range(matrix.rows), 2))
    return sp.Matrix(len(pairs), len(pairs), lambda i, j:
                     matrix[pairs[i][0], pairs[j][0]] * matrix[pairs[i][1], pairs[j][1]]
                     - matrix[pairs[i][0], pairs[j][1]] * matrix[pairs[i][1], pairs[j][0]])


def record():
    clock, boundary, provenance = construct()
    z = sp.Symbol("z")
    polynomial = (z - 1)**10 * (z + 1)**2 * (z*z + z + 1)**2
    if sp.expand(clock.charpoly(z).as_expr() - polynomial) != 0:
        raise ValueError("source clock character polynomial")
    if clock**6 != sp.eye(16) or clock * boundary != boundary:
        raise ValueError("source clock or boundary identity")
    grades = {0: 10, 2: 2, 3: 2, 4: 2}
    weights = [k for k, count in grades.items() for _ in range(count)]
    pairs = Counter((a + b) % 6 for a, b in combinations(weights, 2))
    return {
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "source": provenance,
        "character_polynomial": str(polynomial),
        "one_coordinate_grades": grades,
        "exterior_square_grades": dict(sorted(pairs.items())),
        "boundary_fixed": True,
        "scope": {
            "primitive_C6_grades_absent_on_one_coordinate_space": True,
            "primitive_C6_grades_present_on_exterior_square": True,
            "physical_Fock_polarization_or_charged_TFPT_lift_derived": False,
            "Majorana_coordinates_identified_with_creation_modes": False,
            "TOE_or_RH_proved": False,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(record(), indent=2) + "\n"
    if args.output:
        args.output.write_text(result)
    else:
        print(result, end="")
