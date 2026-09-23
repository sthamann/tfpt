#!/usr/bin/env python3
"""Exact same-source instrument witness for the .20 current frame.

This checker reconstructs the 120 native source24 directions and compares
two instruments with the same effects: affine-current absorption into the
vacuum and the square-root (Lueders) update inside the one-current grade.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CHECKS: Counter[str] = Counter()
PINS = {
    "experiments/theory-contracts/compiler-spatial-response-20260919/completion24_check.py":
        "2f75bdf053e75e6a16919762ae8e8ce34471248729c336d57580fce81fece6ea",
    "experiments/theory-contracts/compiler-spatial-response-20260919/completion24_check.json":
        "df978000ae45578871ffd366e38b3acefb9256cb2b96ac3cf5f6ebfd798327bb",
    "experiments/theory-contracts/compiler-vacuum-current-cubic-20260918/PROOF.txt":
        "d65189b806facbb1eb718eec50221bb85b3a8c3417f98fb6627e01c72c98ef62",
}


def require(ok: object, label: str) -> None:
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS[label] += 1


for relpath, digest in PINS.items():
    require(hashlib.sha256((ROOT / relpath).read_bytes()).hexdigest() == digest,
            "source pin: " + relpath)

# Reuse only the exact ray loader and exact-conversion helpers from the pinned
# completion checker.  Its main routine is not executed on import.
completion_path = ROOT / next(iter(PINS))
spec = importlib.util.spec_from_file_location("instrument_completion24", completion_path)
completion = importlib.util.module_from_spec(spec)
spec.loader.exec_module(completion)
source_path = ROOT / (
    "experiments/theory-contracts/compiler-correlated-event-clock-20260919/"
    "source_channel.py"
)
source_spec = importlib.util.spec_from_file_location("instrument_source_rays", source_path)
source = importlib.util.module_from_spec(source_spec)
source_spec.loader.exec_module(source)
psis = [completion.exact_ray(z) for z in source.source_rays()]
require(len(psis) == 60, "sixty native rays")

# Reconstruct the pinned .20 F20 and its source24 frame.
words3 = list(it.product(range(4), repeat=3))
word3_index = {word: index for index, word in enumerate(words3)}
triples = list(it.combinations_with_replacement(range(4), 3))
sym3 = sp.zeros(64, 20)
for column, triple in enumerate(triples):
    perms = sorted(set(it.permutations(triple)))
    for word in perms:
        sym3[word3_index[word], column] = 1 / sp.sqrt(len(perms))
require(sym3.H * sym3 == sp.eye(20), "orthonormal symmetric-cube basis")

quartics = sp.zeros(256, 5)
for row, word in enumerate(it.product(range(4), repeat=4)):
    counts = tuple(word.count(j) for j in range(4))
    if 4 in counts:
        quartics[row, 0] = 1
    elif counts in ((2, 2, 0, 0), (0, 0, 2, 2)):
        quartics[row, 1] = 1
    elif counts in ((2, 0, 2, 0), (0, 2, 0, 2)):
        quartics[row, 2] = 1
    elif counts in ((2, 0, 0, 2), (0, 2, 2, 0)):
        quartics[row, 3] = 1
    elif counts == (1, 1, 1, 1):
        quartics[row, 4] = 1
norms = (4, 12, 12, 12, 24)
k_matrices = [quartics[:, a].reshape(4, 64) * sym3 for a in range(5)]
f20 = sp.Matrix.vstack(
    *[2 * matrix / sp.sqrt(norm) for matrix, norm in zip(k_matrices, norms)]
)
require(sp.simplify(f20.H * f20) == sp.eye(20), "pinned F20 unitary")

cubes = [sym3.H * completion.tensor_power(psi, 3) for psi in psis]
w20 = [f20 * cube.conjugate() for cube in cubes]
a = sp.sqrt(sp.Rational(5, 6))
b = sp.sqrt(sp.Rational(1, 6))
directions = [
    sp.Matrix.vstack(a * old, sign * b * psi)
    for old, psi in zip(w20, psis)
    for sign in (-1, 1)
]
require(all(sp.simplify((w.H * w)[0]) == 1 for w in directions),
        "all 120 current directions normalized")
frame = sum((w * w.H for w in directions), sp.zeros(24))
require(sp.simplify(frame) == 5 * sp.eye(24), "native source24 frame is 5 I24")

# On H_n^24 use |w,n>=i_n(w).  The affine relation
# J_n(w^dagger)i_n(v)=sqrt(n)<w,v>|Omega> makes the normalized current
# annihilator K_w exactly the rank-one vacuum bra <w|/sqrt(5).
# The square-root update M_w=|w><w|/sqrt(5) has the same effect.
for w in directions:
    effect_absorption = w * w.H / 5
    effect_lueders = (w * w.H / sp.sqrt(5)).H * (w * w.H / sp.sqrt(5))
    require(sp.simplify(effect_absorption - effect_lueders) == sp.zeros(24),
            "absorption and Lueders effects agree")
require(sp.simplify(sum((w * w.H / 5 for w in directions), sp.zeros(24))) == sp.eye(24),
        "absorption Kraus bras are complete on every one-current source24 grade")

# After absorption the state is the grade-zero vacuum.  Extending each
# positive-mode annihilator by zero on the vacuum gives K_y K_x=0.  The
# Lueders update stays at grade n and has conditional transition
# |<w_y,w_x>|^2/5.  Its probabilities sum to one for every first outcome.
gram = sp.Matrix.hstack(*directions).H * sp.Matrix.hstack(*directions)
for x in range(120):
    lueders_total = sp.simplify(sum(
        gram[y, x] * sp.conjugate(gram[y, x]) / 5 for y in range(120)
    ))
    require(lueders_total == 1, "Lueders second-event probabilities normalize")
require(sp.simplify(gram[0, 0] * sp.conjugate(gram[0, 0]) / 5) == sp.Rational(1, 5),
        "Lueders repeated-outcome probability is one fifth")
vacuum = sp.Matrix([1] + [0] * 24)
embedded_directions = [sp.Matrix.vstack(sp.zeros(1, 1), w) for w in directions]
require(all((q.H * vacuum)[0] == 0 for q in embedded_directions),
        "absorption second source event is identically zero before refresh")

# The old 20-dimensional effect POVM is recovered as an instrument as well:
# the two sign outcomes have identical vacuum output on W20 and coarse-grain
# to K_l=sqrt(1/3)|Omega><w20_l| for all inputs.
for label, old in enumerate(w20):
    coarse = sum(
        (directions[2 * label + j][:20, :] * directions[2 * label + j][:20, :].H / 5
         for j in (0, 1)),
        sp.zeros(20),
    )
    require(sp.simplify(coarse - old * old.H / 3) == sp.zeros(20),
            "sign-coarse-grained absorption recovers old source20 instrument")

result = {
    "research_id": "UR.COMPILER.CURRENT_INSTRUMENT_SOURCE_TEST.20260919",
    "verdict": "EXACT_CONDITIONAL_ABSORPTION_INSTRUMENT; MULTITIME_PROCESS_NOT_SELECTED",
    "source_pins": PINS,
    "domain": "fixed affine grade n>=1, one-current source24 image i_n(W24)",
    "absorption_kraus": "K_(l,s)=P_Omega J_n(w_(l,s)^dagger) P_(n,24)/sqrt(5n)",
    "action": "K_(l,s) i_n(v)=<w_(l,s),v> Omega/sqrt(5)",
    "effect": "K^dagger K=|i_n(w)><i_n(w)|/5",
    "completion": "sum_(l,s) K^dagger K=P_(n,24)",
    "uniqueness": "unique up to outcome phase among one-Kraus maps into the one-dimensional vacuum with these effects",
    "contrast": {
        "absorption_output": "Omega, affine grade 0; next positive-mode source event has total probability 0 without refresh",
        "lueders_output": "i_n(w_(l,s)), affine grade n",
        "lueders_conditional": "p(y|x)=|<w_y,w_x>|^2/5; sum_y p(y|x)=1; p(x|x)=1/5",
    },
    "old_source20": "forgetting sign gives K_l=sqrt(1/3)|Omega><i_n(w20_l)| for every W20 input",
    "not_selected": [
        "affine grade or incident state",
        "event occurrence times/rates",
        "refresh or retained record",
        "identification with the C60 reflection/stay-jump process",
        "raw-seam realization of the assumed E8_1 vacuum currents",
    ],
    "checks": dict(sorted(CHECKS.items())),
    "check_evaluations": sum(CHECKS.values()),
    "T1_T8_closed": [],
}
(HERE / "instrument_source_test_check.json").write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "verdict": result["verdict"],
    "checks": result["check_evaluations"],
    "directions": 120,
    "frame_bound": 5,
    "lueders_repeat_probability": "1/5",
}, sort_keys=True))
