#!/usr/bin/env python3
"""Exact counterexample contract for the sign-covariance implication.

The v199 covariance is C = (I + sgn(H))/2.  This checker keeps the sign
projector fixed while changing the positive magnitudes of H, and also gives a
four-dimensional witness with [rho,C] = 0 but [rho,H] != 0.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
V199 = ROOT / "verification/v199_seam_state_invariance.py"
V258 = ROOT / "verification/v258_dirac_covariance_induction.py"
LEDGER = ROOT / "verification/status_ledger.csv"

PINS = {
    "verification/v199_seam_state_invariance.py":
        "566ea460d3d4198e6437c528f96f921d0b857abb167ad37216e9fee9c38dab0e",
    "verification/v258_dirac_covariance_induction.py":
        "16c60e831dceba773f3629466895f1009654827286e5b760ae01bd755fd5c0b1",
}
LEDGER_ROW_SHA256 = "0c43b723c8109cdabc65d8b149e979906e573d126cc5f606c366761d569b404c"


class Certificate:
    def __init__(self) -> None:
        self.checks: list[dict[str, object]] = []

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        self.checks.append({
            "name": name,
            "status": "PASS" if condition else "FAIL",
            "detail": detail,
        })

    @property
    def failed(self) -> list[dict[str, object]]:
        return [c for c in self.checks if c["status"] != "PASS"]


def frobenius_squared(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(sum(sp.conjugate(x) * x for x in matrix))


def gamma(j0: sp.Matrix, matrix: sp.Matrix) -> sp.Matrix:
    """Antiunitary Gamma(X) = J0 conjugate(X) J0, represented exactly."""
    return j0 * matrix.conjugate() * j0


def sign_projector(matrix: sp.Matrix) -> sp.Matrix:
    # The witness is diagonal with no zero eigenvalue; this is sgn(H) exactly.
    signs = [1 if value > 0 else -1 for value in matrix.diagonal()]
    return sp.diag(*[(sp.Integer(1) + value) / sp.Integer(2)
                     for value in signs])


def source_pins(cert: Certificate) -> dict[str, object]:
    actual: dict[str, str] = {}
    for relative, expected in PINS.items():
        digest = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        actual[relative] = digest
        cert.check(
            f"SOURCE PIN {relative}",
            digest == expected,
            f"expected={expected}, actual={digest}",
        )

    rows = [line for line in LEDGER.read_text().splitlines()
            if line.startswith("QGEO.STATE.01,")]
    row = rows[0] if len(rows) == 1 else ""
    row_digest = hashlib.sha256(row.encode()).hexdigest() if row else ""
    cert.check(
        "LEDGER PIN QGEO.STATE.01",
        len(rows) == 1 and row_digest == LEDGER_ROW_SHA256,
        f"rows={len(rows)}, sha256={row_digest}, length={len(row)}",
    )
    return {
        "source_sha256": actual,
        "ledger_row": {
            "id": "QGEO.STATE.01",
            "sha256": row_digest,
            "length": len(row),
        },
    }


def exact_counterexample(cert: Certificate) -> dict[str, object]:
    I = sp.I
    I2 = sp.eye(2)
    Z2 = sp.zeros(2)
    S = sp.Matrix([[0, 1], [1, 0]])
    A = sp.diag(1, 2)
    H = sp.diag(1, 2, -1, -2)
    rho = sp.diag(I * S, -I * S)
    C = sp.diag(1, 1, 0, 0)
    J0 = sp.Matrix.vstack(sp.Matrix.hstack(Z2, I2), sp.Matrix.hstack(I2, Z2))
    identity = sp.eye(4)
    zero = sp.zeros(4)
    comm_rho_c = rho * C - C * rho
    comm_rho_h = rho * H - H * rho
    sign_h = 2 * C - identity
    abs_h = sign_h * H

    cert.check("H is Hermitian", H.H == H)
    cert.check("H is gapped", all(value != 0 for value in H.diagonal()))
    cert.check("rho is unitary", rho.H * rho == identity)
    cert.check("rho has exact order four", rho**4 == identity and rho**2 != identity)
    cert.check("C is the sign projector", C == sign_projector(H))
    cert.check("rho commutes with C", comm_rho_c == zero)
    cert.check("rho commutes with sgn(H)", rho * sign_h - sign_h * rho == zero)
    cert.check("Gamma is antiunitary particle-hole conjugation",
               gamma(J0, H) == -H and gamma(J0, C) == identity - C)
    cert.check("Gamma commutes with rho", gamma(J0, rho) == rho)
    cert.check("reverse implication fails", comm_rho_h != zero)
    cert.check("exact Frobenius witness is four",
               frobenius_squared(comm_rho_h) == 4,
               f"||[rho,H]||_F^2={frobenius_squared(comm_rho_h)}")
    cert.check("lost datum is |H|",
               abs_h == sp.diag(1, 2, 1, 2)
               and frobenius_squared(rho * abs_h - abs_h * rho) == 4)
    cert.check("sharp repair witness equivalence",
               (rho * H - H * rho == zero)
               == (rho * abs_h - abs_h * rho == zero),
               "this witness has [rho,sgn(H)]=0; the general identity is H=sgn(H)|H|")
    return {
        "H": [[str(x) for x in H.row(i)] for i in range(4)],
        "rho": [[str(x) for x in rho.row(i)] for i in range(4)],
        "C": [[str(x) for x in C.row(i)] for i in range(4)],
        "commutator_frobenius_squared": str(frobenius_squared(comm_rho_h)),
        "sign_H": [[str(x) for x in sign_h.row(i)] for i in range(4)],
        "abs_H": [[str(x) for x in abs_h.row(i)] for i in range(4)],
    }


def magnitude_family(cert: Certificate) -> dict[str, object]:
    I = sp.I
    rho0 = sp.diag(I, -I, -I, I)
    C = sp.diag(1, 1, 0, 0)
    values: dict[str, object] = {}
    matrices: list[sp.Matrix] = []
    for a in (sp.Integer(2), sp.Integer(3)):
        H_a = sp.diag(1, a, -1, -a)
        matrices.append(H_a)
        C_a = sign_projector(H_a)
        cert.check(f"H_a={a} is Hermitian and gapped",
                   H_a.H == H_a and all(value != 0 for value in H_a.diagonal()))
        cert.check(f"H_a={a} has the same sign state", C_a == C)
        cert.check(f"H_a={a} has the same rho/C invariance", rho0 * C == C * rho0)
        cert.check(f"H_a={a} commutes with fixed rho0", rho0 * H_a == H_a * rho0)
        values[str(a)] = {
            "energy_ratio_H2_over_H1": str(H_a[1, 1] / H_a[0, 0]),
            "H": [str(x) for x in H_a.diagonal()],
        }
    cert.check("same C and rho do not fix magnitudes",
               matrices[0] != matrices[1]
               and values["2"]["energy_ratio_H2_over_H1"] !=
               values["3"]["energy_ratio_H2_over_H1"])
    return {
        "rho0": [str(x) for x in rho0.diagonal()],
        "C": [str(x) for x in C.diagonal()],
        "a_values": values,
    }


def main() -> int:
    cert = Certificate()
    pins = source_pins(cert)
    witness = exact_counterexample(cert)
    family = magnitude_family(cert)
    passed = len(cert.failed) == 0
    result = {
        "status": "PASS" if passed else "FAIL",
        "verdict": "PARTIAL" if passed else "KERNEL_VIOLATION",
        "reverse_implication": "REFUTED" if passed else "NOT_CERTIFIED",
        "question": "Does [rho,C]=0 for C=(I+sgn(H))/2 imply [rho,H]=0?",
        "exact_checks": len(cert.checks),
        "failed_checks": len(cert.failed),
        "checks": cert.checks,
        "counterexample": witness,
        "magnitude_family": family,
        "source_replay_observed_separately": {
            "source": "verification/v199_seam_state_invariance.py",
            "command": "python3 -B verification/v199_seam_state_invariance.py",
            "exit_code": 0,
            "output_sha256": "a44873d1094c3045d33475e366f5fab76310cc714eca744ab7fc3d01edfe1cde",
            "output_bytes": 1406,
            "observed_summary": "4 passed, 0 failed",
            "scope": "v199 verifies only the character-block criterion and leaves the bounded sub-principal residual open",
            "executed_by_checker": False,
        },
        "scope": {
            "proves": "The sign-projector covariance is not injective in H; state invariance alone loses |H|.",
            "does_not_prove": [
                "No refutation of modular uniqueness for a fixed standard pair.",
                "No refutation of a full TFPT source or continuum construction.",
                "No claim that v201 mark-local => state invariance is false.",
            ],
        },
        "pins": pins,
        "closed_gate_ids": [],
        "promotion": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
