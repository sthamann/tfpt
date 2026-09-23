#!/usr/bin/env python3
"""Exact charge-sector check for the 24 current directions in process gate .20.

The doubled coordinates are signs in {+1,-1}; division by two gives an E8
half-root of norm two.  The class convention is the corrected v148 census:
an odd/even number of minus signs in the D5 or D3 block gives class 3/1.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def signs(length: int, minus_count: int):
    for minus_positions in itertools.combinations(range(length), minus_count):
        minus_positions = set(minus_positions)
        yield tuple(-1 if i in minus_positions else 1 for i in range(length))


def odd_class(block: tuple[int, ...]) -> int:
    """v148 half-root class: even minus count -> 1, odd -> 3."""
    return 1 if block.count(-1) % 2 == 0 else 3


def charge_class(root: tuple[int, ...]) -> tuple[int, int]:
    return odd_class(root[:5]), odd_class(root[5:])


def record() -> dict:
    family = tuple(
        signs3
        for count in (1, 3)
        for signs3 in signs(3, count)
    )
    w20 = tuple(d5 + d3 for d5 in signs(5, 1) for d3 in family)
    w4 = tuple(d5 + d3 for d5 in signs(5, 5) for d3 in family)
    source24 = w20 + w4
    adjoints = tuple(tuple(-x for x in root) for root in source24)

    require(len(family) == 4, "four last-three odd-minus weights")
    require(len(w20) == 20 and len(w4) == 4, "W20 plus W4 census")
    require(len(set(source24)) == 24, "24 distinct source directions")
    require(all(sum(x * x for x in root) == 8 for root in source24),
            "all doubled roots have true norm two")
    require({charge_class(root) for root in source24} == {(3, 3)},
            "all source directions lie in Ramond class (3,3)")
    require({charge_class(root) for root in adjoints} == {(1, 1)},
            "all adjoints lie in conjugate Ramond class (1,1)")
    require(all(any(x % 2 for x in root) for root in source24),
            "no source direction is an integral/bilinear D8 root")

    ns_classes = {(0, 0), (2, 0), (0, 2), (2, 2)}
    ramond_classes = {(1, 1), (1, 3), (3, 1), (3, 3)}
    glue_a = {(0, 0), (1, 1), (2, 2), (3, 3)}
    glue_b = {(0, 0), (1, 3), (2, 2), (3, 1)}
    common_ns = glue_a & ns_classes
    require(common_ns == glue_b & ns_classes == {(0, 0), (2, 2)},
            "the two Lagrangian glues have identical NS restriction")
    require(glue_a & ramond_classes == {(1, 1), (3, 3)},
            "source24 and adjoints select glue A only after Ramond data")
    require(glue_b & ramond_classes == {(1, 3), (3, 1)},
            "the competing glue has the other Ramond sheet")

    return {
        "status": "PASS",
        "source24": {
            "W20": len(w20),
            "W4": len(w4),
            "total": len(source24),
            "charge_classes": sorted(map(list, {charge_class(r) for r in source24})),
            "integral_D8_roots": 0,
        },
        "adjoints": {
            "total": len(adjoints),
            "charge_classes": sorted(map(list, {charge_class(r) for r in adjoints})),
        },
        "glue_selection": {
            "glue_a": sorted(map(list, glue_a)),
            "glue_b": sorted(map(list, glue_b)),
            "common_NS_restriction": sorted(map(list, common_ns)),
            "glue_a_Ramond": sorted(map(list, glue_a & ramond_classes)),
            "glue_b_Ramond": sorted(map(list, glue_b & ramond_classes)),
            "NS_vacuum_data_alone_distinguishes_glue": False,
            "first_distinguishing_data": "a nonzero source operator/sector response in (3,3) or (1,1)",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    payload = json.dumps(record(), indent=2, sort_keys=True) + "\n"
    if args.out:
        args.out.write_text(payload)
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
