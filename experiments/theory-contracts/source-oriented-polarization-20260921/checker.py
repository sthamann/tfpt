#!/usr/bin/env python3
"""Pinned bounded checks. Infinite-dimensional scope is in PROOF.md."""
from pathlib import Path
import hashlib
import json
import sys
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "verification"))
import v210_mark_local_dtn as source
from v506_seam_clock_rigidity import shift_matrix


def require(condition, message):
    if not bool(condition):
        raise RuntimeError(message)


def run():
    pins = json.loads((HERE / "source_pins.json").read_text())
    for relative, digest in pins["files"].items():
        require(hashlib.sha256((REPO / relative).read_bytes()).hexdigest() == digest,
                "Source changed: " + relative)
    modes = range(-4, 5)
    require([n for n in modes if abs(n)-n == 0] == list(range(5)), "CR orientation")
    require([n for n in modes if abs(n)+n == 0] == list(range(-4, 1)), "reverse orientation")
    for n in modes:
        require(int(n >= 0)+int(-n >= 0) == 1+int(n == 0), "periodic zero defect")
    for n in range(-4, 4):
        r = sp.Rational(2*n+1, 2)
        require(int(bool(r > 0))+int(bool(-r > 0)) == 1, "NS complement")

    A = sp.diag(*([sp.Matrix([[0, 1], [-1, 0]])] * 8))
    C0 = (sp.eye(16)+sp.I*A)/2
    require(C0*C0 == C0 and C0.H == C0, "pure zero covariance")
    require(C0+C0.conjugate() == sp.eye(16) and sp.trace(C0) == 8, "zero complement")
    mixed = sp.eye(16)/2
    require(mixed+mixed.conjugate() == sp.eye(16) and mixed*mixed != mixed,
            "invariant zero covariance is mixed")

    ns = sp.Matrix(shift_matrix(16, 8, -1))
    ramond = sp.Matrix(shift_matrix(16, 8, +1))
    quarter = sp.Matrix(shift_matrix(16, 4, -1))
    require(ns.applyfunc(abs) == ramond.applyfunc(abs), "same underlying deck")
    require(ns**2 == -sp.eye(16) and ramond**2 == sp.eye(16), "opposite lift squares")
    require(quarter**2 == ns and quarter**4 == -sp.eye(16), "quarter lift")
    q = sp.symbols("q", positive=True)
    require(sp.cancel(q/(1-q*q) - 1/(1/q-q)) == 0, "NS geometric correlator sum")

    profile = source.mark_sum([j*np.pi/2 for j in range(4)])
    theta = 2*np.pi*np.arange(source.GRID)/source.GRID
    values = sum((source.vonmises_bump(theta-j*np.pi/2) for j in range(4)),
                 start=np.zeros(source.GRID))
    rows = []
    for N in (16, 32, 64):
        Lam, n = source.dtn(profile, N)
        minimum = float(np.linalg.eigvalsh(Lam-np.diag(n))[0])
        constant = np.zeros(len(n)); constant[N] = 1
        defect = float(np.linalg.norm(Lam @ constant))
        C = source.covariance(Lam)
        gCg = C.conj()[::-1, ::-1]
        reality = float(np.linalg.norm(C-gCg, ord=2))
        complement = float(np.linalg.norm(C+gCg-np.eye(len(n)), ord=2))
        # The median sign is numerically unstable at the tiny threshold gap.
        # Exact J-evenness is proved from the real operator, not this residual.
        Lam_reality = float(np.linalg.norm(Lam-Lam.conj()[::-1, ::-1], ord=2))
        clock_error = float(np.linalg.norm(source.clock(n)@Lam-Lam@source.clock(n), ord=2))
        require(minimum >= float(np.min(values))-1e-12 and defect > 0.8,
                "actual source fails scalar CR kernel")
        require(Lam_reality < 1e-12 and clock_error < 1e-10, "original reality and clock")
        require(complement > 0.9, "scalar median fails natural selfdual complement")
        rows.append({"N": N, "CR_min_eigenvalue": minimum, "constant_defect": defect,
                     "operator_reality_error": Lam_reality,
                     "numerical_covariance_reality_error": reality,
                     "selfdual_complement_defect": complement, "clock_error": clock_error})
    cutoff = []
    for N in (7, 8, 15, 16):
        vals = sorted(abs(n) for n in range(-N, N+1))
        mu = sp.Rational(vals[N-1]+vals[N], 2)
        require(mu == sp.Rational(N, 2), "flat median")
        cutoff.append({"N": N, "mu": str(mu), "zero_mode": N % 2 == 0})
    return {"research_id": "UR.SOURCE.ORIENTED_POLARIZATION.01",
            "check_verdict": "PASS_WITH_DECLARED_SCOPE", "theory_verdict": "PARTIAL",
            "primitive_charged_source_selected": False,
            "physical_time_correlator_derived": False, "physical_gates_closed": [],
            "source_pin_count": len(pins["files"]),
            "scalar_hardy_and_CAR_identities": "FINITE_WITNESSES_OF_ANALYTIC_IDENTITIES",
            "original_spin_lifts": {"same_geometric_permutation": True,
                                    "NS_square": "-I", "R_square": "+I"},
            "profile_grid_minimum": float(np.min(values)),
            "original_v210": rows, "flat_cutoff_parity": cutoff}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
