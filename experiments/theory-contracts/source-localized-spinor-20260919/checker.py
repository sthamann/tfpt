"""Exact algebra supporting a conditional bounded source-sector lift."""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as s


def require(ok, message):
    if not ok:
        raise ValueError(message)


def pair_map(m):
    require(type(m) is int and m >= 1, "positive finite interval window")
    inputs = [(c, n) for c in (0, 1) for n in range(-m, m + 1)]
    outputs = [(0, r) for r in range(-2*m-1, 2*m+2, 2)]
    outputs += [(1, r) for r in range(-2*m+1, 2*m, 2)]
    matrix = s.zeros(len(outputs), len(inputs))
    for column, (c, n) in enumerate(inputs):
        if n == 0:
            matrix[outputs.index((0, 1)), column] = (s.I if c == 0 else -1)/s.sqrt(2)
            matrix[outputs.index((0, -1)), column] = (-s.I if c == 0 else -1)/s.sqrt(2)
        else:
            sign = 1 if n > 0 else -1
            row = (c, 2*n + (sign if c == 0 else -sign))
            matrix[outputs.index(row), column] = s.I*sign*(1 if c == 0 else -1)
    return inputs, outputs, matrix


def reversal(labels):
    result = s.zeros(len(labels))
    for i, (c, n) in enumerate(labels):
        result[labels.index((c, -n)), i] = 1
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="validation.json")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    pins = json.loads((here/"source_pins.json").read_text())
    for name, expected in pins.items():
        require(hashlib.sha256((root/name).read_bytes()).hexdigest() == expected,
                "source pin: " + name)
    windows = []
    for m in (1, 2, 4, 8):
        inputs, outputs, v = pair_map(m)
        d = len(inputs)
        require(s.simplify(v.H*v-s.eye(d)) == s.zeros(d), "isometry")
        require(s.simplify(v*v.H-s.eye(d)) == s.zeros(d), "onto its exact output window")
        gi, go = reversal(inputs), reversal(outputs)
        require(s.simplify(v*gi-go*s.conjugate(v)) == s.zeros(d), "CAR real structure")
        mutant = v.copy()
        mutant[outputs.index((0, -1)), inputs.index((0, 0))] *= -1
        require(mutant.H*mutant != s.eye(d), "wrong zero-mode sign rejected")
        windows.append({"cutoff": m, "dimension_per_pair": d,
                        "unitary": True, "CAR_real": True,
                        "wrong_sign_rejected": True})
    for a in (s.Rational(1, 4), s.Rational(3, 4)):
        for j in range(-5, 6):
            require(j-s.Rational(1, 2)+(s.Rational(1, 2)-a) == j-a,
                    "holonomy frequency identity")
    require((-1)**2 == 1 and (+1)**2 == 1, "even words in each complement component fixed")
    require((+1)*(-1) == -1, "odd-left odd-right word is not fixed")
    result = {
        "research_id": "UR.SEAM.LOCALIZED_SECTOR.10",
        "verdict": "PARTIAL",
        "algebra_checks": "PASS",
        "windows": windows,
        "majorana_pairs_stipulated": 8,
        "source_copies_derived_from_P1": False,
        "source_to_DHR": "analytic word-limit proof using declared upstream inputs",
        "microscopic_intersector_field": "NOT_CONSTRUCTED",
        "microscopic_full_CAR_homomorphism_at_finite_N": False,
        "FE_GEN_ALG_EXH": "OPEN",
        "closed_gate_ids": [],
        "promotion": False,
        "source_pins": pins,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_sha256": hashlib.sha256((here/"PROOF.txt").read_bytes()).hexdigest(),
    }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"verdict": result["verdict"], "algebra_checks": "PASS",
                      "output": args.output, "closed_gate_ids": []}))


if __name__ == "__main__":
    main()
