"""Common parent model -- exact, dependency-light mathematical core slice.

Encodes the *shared* algebraic backbone of the TFPT/Universalraum spin-lift
round v1.6.10 (sources: ``verify_reflection_selection.py`` with 45 PASS checks
and ``verify_spin_lift.py`` in
``TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10``).

This module is deliberately *narrow*: it only carries the exact SymPy
identities for the four-station clock/reflection parent and the integer
constants that pin the native W-bank composition.  It does NOT derive the
physical source from TFPT, it does NOT construct a native preparation or
record instrument, and it does NOT identify the raw seam with the four 64-mode
W-banks -- that identification is explicitly left FALSE (see ``parent_spec.json``
and ``seam_lift.py``).

No numpy / scipy.  SymPy and stdlib only.  Stable under ``python -OO``.

Public surface
--------------
Constants:
    L, INNER_FERMION_DIM, PAIR_MODES, PAIR_NORM, M, SEAM_SITES,
    FOUR_BANK_TOTAL_CHARGE, Q_LOCAL_BOUND

Operators (SymPy matrices, exact):
    R_eta(eta)            -- four-station clock, R^4 = eta I
    J_eta(eta)            -- signed vertex reflection, J^2 = I, J R J = R^-1
    L_eta(eta)            -- induced edge reflection L = R J, L^2 = I
    U_eta(a, b, eta)      -- two-weight source frame U = a I + b R

Identifiers:
    canonical_parent_identifier() -- stable dict naming the parent

Helpers:
    CheckCollector         -- accumulates exact-check names, raises on failure
    oriented_incidence()   -- oriented vertex/edge incidence of the 4-cycle
    source_frame_norm_sq() -- U U^T diagonal structure (pair covariance witness)

Entry point:
    run() -- returns a JSON-serializable dict; CLI prints sorted/indented JSON.
"""
from __future__ import annotations

import json
import sys

import sympy as sp

# ---------------------------------------------------------------- constants
# Four-station (bank) source cycle.
L = 4
# Inner fermion modes per bank (the native W acts on 64 Majorana modes).
INNER_FERMION_DIM = 64
# Number of independent pair channels of the native W tensor (shape (60, 2016)).
PAIR_MODES = 60
# Pair Gram norm: W W^T = PAIR_NORM * I_{PAIR_MODES}  (exact integer).
PAIR_NORM = 8
# Filled-state quartic Q eigenvalue on the full four-bank Fock space
# (single-bank filled Q = 480; four banks => 4 * 480 = 1920).  This is the
# ``M`` used by the non-perturbative Feshbach bounds in verify_spin_lift.py.
M = 1920
# Seam geometry (v622_seam_identification.py): 16 Majorana NS sites on the
# unit circle, marks at the four mu4 bond midpoints.
SEAM_SITES = 16
# Zeroth-order total charge of the four-bank filled state.
FOUR_BANK_TOTAL_CHARGE = 4 * INNER_FERMION_DIM  # 256
# Local Casimir bound coefficient: Q <= (15/2) N <= 480 I per bank.
Q_LOCAL_BOUND = sp.Rational(15, 2)


def _eta_sym(eta):
    """Normalise an eta selector to a SymPy integer in {1, -1}."""
    e = sp.Integer(eta)
    if e not in (sp.Integer(1), sp.Integer(-1)):
        raise ValueError("eta must be +1 or -1, got %r" % (eta,))
    return e


# ---------------------------------------------------------------- operators
def R_eta(eta):
    """Four-station clock matrix with R^4 = eta I.

    Permutation cycle (0 1 2 3) with the eta sign carried by the wrap edge,
    exactly as in ``verify_reflection_selection.py``.
    """
    e = _eta_sym(eta)
    return sp.Matrix([[0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1],
                      [e, 0, 0, 0]])


def J_eta(eta):
    """Signed vertex reflection with J^2 = I and J R J = R^-1.

    Fixes stations 0 and 2 and swaps 1 <-> 3 with an eta sign, matching the
    dihedral relation of ``verify_reflection_selection.py``.
    """
    e = _eta_sym(eta)
    return sp.Matrix([[1, 0, 0, 0],
                      [0, 0, 0, e],
                      [0, 0, e, 0],
                      [0, e, 0, 0]])


def L_eta(eta):
    """Induced edge reflection L = R J  (L^2 = I).

    With the source labelling ``edge e connects vertex e -> vertex (e+1) mod
    4``, the unsigned permutation carried by L is exactly the edge permutation
    induced by the unsigned vertex reflection.  Fermionic lift signs are not
    geometric incidence signs; see ``seam_lift._check_incidence``.
    """
    return R_eta(eta) * J_eta(eta)


def U_eta(a, b, eta):
    """Two-weight source frame U = a I + b R  (commutes with the clock R)."""
    a = sp.sympify(a)
    b = sp.sympify(b)
    return a * sp.eye(4) + b * R_eta(eta)


# ---------------------------------------------------------------- helpers
def oriented_incidence():
    """Oriented vertex/edge incidence matrix D of the 4-cycle.

    ``D[v, e] = -1`` at the tail ``v=e`` and ``+1`` at the head
    ``v=(e+1) mod 4``.  This is the source-frame convention
    ``q_e = a f_e + b f_{e+1}``.  A reflection reverses orientation, so the
    geometric relation is ``|J|^T D |L| = -D``.
    """
    D = sp.zeros(4, 4)
    for e in range(4):
        tail = e
        head = (e + 1) % 4
        D[head, e] = sp.Integer(1)
        D[tail, e] = sp.Integer(-1)
    return D


def source_frame_norm_sq(a, b, eta):
    """Diagonal structure of U U^T as a SymPy matrix (pair-covariance witness).

    Returns the 4x4 matrix ``U U^T``; its diagonal entries are ``a^2 + b^2``
    for every station (individual CAR normalisation when a^2 + b^2 = 1), and
    the off-diagonal structure encodes the neighbour weights whose mismatch
    is exactly ``a^2 - b^2`` (see ``seam_lift.check_pair_mismatch``).
    """
    U = U_eta(a, b, eta)
    return sp.simplify(U * U.T)


def canonical_parent_identifier():
    """Stable, JSON-serialisable identifier of this common parent model.

    The identifier is a content hash of the exact operator definitions and
    constants, so any change to the load-bearing algebra changes the id.
    """
    import hashlib

    e1 = sp.Integer(1)
    em1 = sp.Integer(-1)
    payload = {
        "L": L,
        "inner_fermion_dim": INNER_FERMION_DIM,
        "pair_modes": PAIR_MODES,
        "pair_norm": PAIR_NORM,
        "M": M,
        "seam_sites": SEAM_SITES,
        "R_eta_plus": R_eta(e1).tolist(),
        "R_eta_minus": R_eta(em1).tolist(),
        "J_eta_plus": J_eta(e1).tolist(),
        "J_eta_minus": J_eta(em1).tolist(),
        "L_eta_plus": L_eta(e1).tolist(),
        "L_eta_minus": L_eta(em1).tolist(),
        "oriented_incidence": oriented_incidence().tolist(),
    }
    blob = json.dumps(payload, sort_keys=True, default=str)
    digest = hashlib.sha256(blob.encode("utf-8")).hexdigest()
    return {
        "parent_id": "tfpt-universalraum-common-parent-t1-t8-20260915:"
                     + digest[:16],
        "digest_sha256": digest,
        "constants": {
            "L": L,
            "inner_fermion_dim": INNER_FERMION_DIM,
            "pair_modes": PAIR_MODES,
            "pair_norm": PAIR_NORM,
            "M": M,
            "seam_sites": SEAM_SITES,
            "four_bank_total_charge": FOUR_BANK_TOTAL_CHARGE,
            "q_local_bound_coefficient": str(Q_LOCAL_BOUND),
        },
        "operators": {
            "R_eta": "clock, R^4 = eta I",
            "J_eta": "signed vertex reflection, J^2 = I, J R J = R^-1",
            "L_eta": "induced edge reflection L = R J, L^2 = I",
            "U_eta": "two-weight source frame a I + b R",
        },
    }


# ---------------------------------------------------------------- stable exports
# Module-level stable identifiers, derived once from the canonical function so
# every consumer (seam_lift, gates_t1_t4, gates_t5_t8, cross_gate) reads the
# SAME parent_id and constants without re-computing or falling back to a
# described contract.  These are JSON-safe (plain str / int / dict).
_CANONICAL = canonical_parent_identifier()
PARENT_ID: str = _CANONICAL["parent_id"]
#: Stable content digest of the parent's load-bearing algebra (full sha256).
PARENT_DIGEST_SHA256: str = _CANONICAL["digest_sha256"]
#: JSON-safe constants dict (integers and a rational-as-string coefficient).
CONSTANTS: dict = _CANONICAL["constants"]
#: JSON-safe operator-name -> short-description map.
OPERATORS: dict = _CANONICAL["operators"]


class CheckCollector:
    """Accumulate exact-check names; raise on the first failure.

    Mirrors the ``need``/``checks`` pattern of the source verifiers but is
    reusable across modules.  A check passes iff its condition is truthy
    under ``bool(...)`` (SymPy equalities are made explicit by the caller via
    ``== 0`` or ``is True`` before being passed in).
    """

    def __init__(self):
        self.names = []

    def need(self, condition, name):
        if not bool(condition):
            raise RuntimeError("CHECK FAILED: " + name)
        self.names.append(name)

    def count(self):
        return len(self.names)


def run():
    """Return a JSON-serialisable summary of the parent-model core slice.

    ``status == "PASS"`` here only certifies the internal self-checks of this
    module (operator shapes, constants, identifier stability); it does NOT
    certify the seam->W intertwiner or any T1-T8 gate -- those are reserved
    for ``seam_lift.py`` and are explicitly FALSE/absent.
    """
    c = CheckCollector()
    a, b = sp.symbols("a b", real=True)
    for eta in (1, -1):
        R = R_eta(eta)
        J = J_eta(eta)
        Lm = L_eta(eta)
        c.need(R ** 4 == eta * sp.eye(4), "R^4 = eta I  eta=%d" % eta)
        c.need(J * J == sp.eye(4), "J^2 = I  eta=%d" % eta)
        c.need(J * R * J == R.inv(), "J R J = R^-1  eta=%d" % eta)
        c.need(Lm * Lm == sp.eye(4), "L^2 = I  eta=%d" % eta)
        U = U_eta(a, b, eta)
        c.need(U * R == R * U, "U commutes with R  eta=%d" % eta)
    ident = canonical_parent_identifier()
    return {
        "status": "PASS",
        "exact_checks": c.count(),
        "checks": c.names,
        "parent_id": ident["parent_id"],
        "constants": ident["constants"],
        "operators": ident["operators"],
        "raw_seam_to_w_intertwiner": False,
        "closed_gate_ids": [],
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True, default=str))
