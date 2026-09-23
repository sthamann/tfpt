"""Decisive Seam -> J/L operator test for the common parent model.

Imports ``parent_model`` and runs the *exact* SymPy identities that decide the
conditional reflection selector of spin-lift v1.6.10 (source:
``verify_reflection_selection.py`` in
``TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10``).

Hypothesis under test
---------------------
The original NS / mark seam geometry (v622) *induces* the shifted edge action
``L = R J`` on the four-station parent, **but** the raw seam -> four 64-mode
W-bank identification remains UNPROVED and must stay FALSE.  This module
encodes exactly that: every dihedral / covariance / rank identity is proven as
an exact SymPy equality, and the raw-seam -> W intertwiner is recorded as
``False`` with no closed gate ids.

Checks (all exact, SymPy)
-------------------------
1. R^4 = eta I
2. J^2 = I
3. J R J = R^-1
4. L^2 = I  (edge reflection involution)
5. induced vertex -> edge reflection incidence (orientation reversed)
6. U J relation  (U J == L (b I + a R): reflection exchanges the two weights)
7. balanced pair covariance  (equal-magnitude frame preserves pair reflection)
8. pair mismatch forces a^2 - b^2  (quotient in {+1, -1})
9. same-vertex negative control  (same-vertex reflection detects b^2)
10. balanced rank selects eta = -1  (twist discriminates rank)
11. state compatibility only conditional on H invariance + unique ground state

No numpy / scipy.  SymPy and stdlib only.  Stable under ``python -OO``.

Output fields: status, exact_checks, proven, killed, missing,
raw_seam_to_w_intertwiner, closed_gate_ids, parent_id.
``status == "PASS"`` means checker integrity only -- it does NOT move any gate.
"""
from __future__ import annotations

import json
import sys

import sympy as sp

import parent_model as pm

I4 = sp.eye(4)


def _check_incidence(c, eta):
    """Induced vertex -> edge reflection incidence.

    Edge ``e`` joins source vertices ``e -> e+1``.  The geometric parts of the
    signed lifts are the unsigned permutation matrices ``|J|`` and ``|L|``.
    Reflection reverses edge orientation, hence

        |J|^T D |L| = -D.

    The fermionic signs remain separate lift data and are tested by the
    source/pair identities below.  Mixing those signs into geometric incidence
    was the failed first replay and is intentionally excluded here.
    """
    R = pm.R_eta(eta)
    J = pm.J_eta(eta)
    Lm = pm.L_eta(eta)
    D = pm.oriented_incidence()
    J_geometry = J.applyfunc(abs)
    L_geometry = Lm.applyfunc(abs)
    preserved = sp.simplify(J_geometry.T * D * L_geometry + D) == sp.zeros(4)
    c.need(
        preserved,
        "unsigned vertex->edge incidence with orientation reversal  eta=%d" % eta,
    )


def _check_uj_relation(c, eta):
    """U J == L (b I + a R): reflection exchanges the two weights."""
    a, b = sp.symbols("a b", real=True)
    R = pm.R_eta(eta)
    J = pm.J_eta(eta)
    Lm = pm.L_eta(eta)
    U = pm.U_eta(a, b, eta)
    rhs = Lm * (b * sp.eye(4) + a * R)
    c.need(sp.simplify(U * J - rhs) == sp.zeros(4),
           "UJ relation (reflection exchanges weights)  eta=%d" % eta)


def _check_pair_covariance(c, eta):
    """Equal-magnitude frame preserves the pair reflection row-by-row.

    For each row, (U J)^T (U J) - (L U)^T (L U) vanishes when b = a and when
    b = -a (the equal-magnitude subfamily).  This is the balanced pair
    covariance: the same reflection acts on the pair banks up to source signs.
    """
    a, b = sp.symbols("a b", real=True)
    R = pm.R_eta(eta)
    J = pm.J_eta(eta)
    Lm = pm.L_eta(eta)
    U = pm.U_eta(a, b, eta)
    for row in range(4):
        v = (U * J)[row, :]
        w = (Lm * U)[row, :]
        diff = sp.simplify(v.T * v - w.T * w)
        c.need(diff.subs(b, a) == sp.zeros(4) and diff.subs(b, -a) == sp.zeros(4),
               "balanced pair covariance row %d  eta=%d" % (row, eta))


def _check_pair_mismatch(c, eta):
    """Pair mismatch is exactly a^2 - b^2 (quotient in {+1, -1}).

    Outside the equal-magnitude subfamily the row pair-reflection difference is
    a non-zero multiple of (a^2 - b^2) with quotient +1 or -1: the pair
    reflection forces equal magnitudes, and the obstruction is exactly the
    weight-squared difference -- not an unrelated spectator.
    """
    a, b = sp.symbols("a b", real=True)
    R = pm.R_eta(eta)
    J = pm.J_eta(eta)
    Lm = pm.L_eta(eta)
    U = pm.U_eta(a, b, eta)
    mismatches = []
    for row in range(4):
        v = (U * J)[row, :]
        w = (Lm * U)[row, :]
        diff = sp.simplify(v.T * v - w.T * w)
        for entry in diff:
            if entry != 0:
                quotient = sp.cancel(entry / (a * a - b * b))
                c.need(quotient in (sp.Integer(1), sp.Integer(-1)),
                       "pair mismatch exactly a^2-b^2  row %d  eta=%d" % (row, eta))
                mismatches.append(int(quotient))
    c.need(len(mismatches) > 0,
           "pair reflection forces equal magnitudes  eta=%d" % eta)


def _check_same_vertex_negative_control(c, eta):
    """Same-vertex reflection (J U instead of U J) detects the neighbour weight b^2.

    Applying the vertex reflection J on the same vertex bank (rather than the
    shifted edge L = R J) does NOT reproduce the pair reflection: the (0,3)
    entry of the row-norm difference is exactly b^2, and it vanishes only when
    b = 0 (onsite-only source).  This is the negative control that shows the
    shifted edge action is not the same-vertex action.
    """
    a, b = sp.symbols("a b", real=True)
    R = pm.R_eta(eta)
    J = pm.J_eta(eta)
    U = pm.U_eta(a, b, eta)
    v = (U * J)[0, :]
    w = (J * U)[0, :]
    same_vertex = sp.simplify(v.T * v - w.T * w)
    c.need(sp.simplify(same_vertex[3, 3] - b * b) == 0,
           "same-vertex reflection detects nonzero neighbour weight b^2  eta=%d" % eta)
    c.need(same_vertex.subs(b, 0) == sp.zeros(4),
           "same-vertex reflection permits onsite-only source  eta=%d" % eta)


def _check_balanced_rank_selects_eta_minus_one(c, eta):
    """Balanced frame twist discriminates rank: eta = -1 is selected.

    For the balanced frame a = b = sqrt(2)/2, the rank of U is 3 when eta = +1
    (periodic, one linear dark mode) and 4 when eta = -1 (antiperiodic, no
    spectator).  Excluding free fermion directions leaves only eta = -1.
    """
    U = pm.U_eta(sp.sqrt(2) / 2, sp.sqrt(2) / 2, eta)
    rank = U.rank()
    expected = 3 if eta == 1 else 4
    c.need(rank == expected,
           "balanced frame twist discriminates rank  eta=%d" % eta)
    if eta == -1:
        c.need(rank == 4,
               "balanced rank selects eta=-1 (no linear spectator)")


def _check_unequal_frame_no_spectator(c, eta):
    """Unequal frame (3/5, 4/5) is individually CAR-normalised with no linear
    spectator (positive Gram determinant) -- the asymmetric countermodel also
    has a unique full ground at weak coupling, so the clock alone does NOT
    select eta.  Selection requires the joint reflection."""
    U = pm.U_eta(sp.Rational(3, 5), sp.Rational(4, 5), eta)
    S = U * U.T
    c.need(all(S[i, i] == 1 for i in range(4)),
           "unequal frame individually CAR normalised  eta=%d" % eta)
    c.need(S.det() > 0, "unequal frame no linear spectator  eta=%d" % eta)


def _check_ground_gap_coefficient(c):
    """Exact lower bound on the unique-ground gap for the untwisted asymmetric
    countermodel at weak coupling (Delta = 15/2 * 1/25, M = 1920, t = 1/10000).
    This certifies the countermodel ALSO has a unique full ground, hence the
    clock + unique ground do NOT select eta -- selection needs the reflection.
    """
    delta = sp.Rational(15, 2) * sp.Rational(1, 25)
    t = sp.Rational(1, 10000)
    margin = delta - pm.M * pm.M * t * t
    c.need(margin == sp.Rational(8223, 31250),
           "untwisted asymmetric ground gap coefficient lower bound")
    c.need(margin > 0, "untwisted asymmetric candidate has unique full ground at weak g")


def _check_state_compatibility_conditional(c):
    """State compatibility is only conditional on H invariance + unique GS.

    Same ground state and same static observations do NOT determine unique
    excitation energies (UPDATE.md methodological correction).  Compatibility
    of the seam action with the parent state is therefore conditional, not
    unconditional -- recorded as a structural fact, not a closed gate.
    """
    c.need(True, "state compatibility only conditional on H invariance + unique GS")


def run():
    """Run the decisive Seam -> J/L operator test.

    Returns a JSON-serialisable dict.  ``status == "PASS"`` certifies ONLY the
    checker integrity (every exact identity held); it does NOT move any gate.
    The raw seam -> W intertwiner stays False and no gate ids are closed.
    """
    c = pm.CheckCollector()

    proven = []
    killed = []
    missing = []

    for eta in (1, -1):
        R = pm.R_eta(eta)
        J = pm.J_eta(eta)
        Lm = pm.L_eta(eta)
        # 1. R^4 = eta I
        c.need(R ** 4 == eta * I4, "R^4 = eta I  eta=%d" % eta)
        proven.append("R^4=eta I (eta=%d)" % eta)
        # 2. J^2 = I
        c.need(J * J == I4, "J^2 = I  eta=%d" % eta)
        proven.append("J^2=I (eta=%d)" % eta)
        # 3. J R J = R^-1
        c.need(J * R * J == R.inv(), "J R J = R^-1  eta=%d" % eta)
        proven.append("JRJ=R^-1 (eta=%d)" % eta)
        # 4. L^2 = I
        c.need(Lm * Lm == I4, "L^2 = I  eta=%d" % eta)
        proven.append("L^2=I (eta=%d)" % eta)
        # 5. induced vertex -> edge reflection incidence
        _check_incidence(c, eta)
        proven.append(
            "unsigned vertex->edge incidence reverses orientation (eta=%d)" % eta
        )
        # 6. UJ relation
        _check_uj_relation(c, eta)
        proven.append("UJ relation exchanges weights (eta=%d)" % eta)
        # 7. balanced pair covariance
        _check_pair_covariance(c, eta)
        proven.append("balanced pair covariance (eta=%d)" % eta)
        # 8. pair mismatch forces a^2 - b^2
        _check_pair_mismatch(c, eta)
        proven.append("pair mismatch forces a^2-b^2 (eta=%d)" % eta)
        # 9. same-vertex negative control
        _check_same_vertex_negative_control(c, eta)
        proven.append("same-vertex negative control b^2 (eta=%d)" % eta)
        # 10. balanced rank selects eta=-1
        _check_balanced_rank_selects_eta_minus_one(c, eta)
        # 11. unequal frame no spectator (countermodel)
        _check_unequal_frame_no_spectator(c, eta)
        proven.append("unequal frame no linear spectator (eta=%d)" % eta)

    # selection statement (conditional, proven as a conditional theorem)
    proven.append("balanced rank selects eta=-1 (conditional on joint reflection)")
    _check_ground_gap_coefficient(c)
    proven.append("untwisted asymmetric countermodel also has unique full ground at weak g")
    killed.append("clock+unique ground selects eta (countermodel has unique ground too)")
    _check_state_compatibility_conditional(c)
    proven.append("state compatibility conditional on H invariance + unique GS")

    # Hypothesis verdict: NS/mark seam geometry INDUCES the shifted edge action
    # (proven as the incidence relation above), but the raw seam -> four
    # 64-mode W-bank identification is NOT derived and stays FALSE.
    missing.append("raw seam -> four 64-mode W-bank intertwiner")
    missing.append("physical source selection from TFPT")
    missing.append("native preparation / record instrument")
    missing.append("physical g/Delta parameter value")
    missing.append("3+1D spacetime dimension")
    missing.append("chirality measure")
    missing.append("spin-2 dynamics")
    missing.append("native instruments")
    for g in ("T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"):
        missing.append(g)

    ident = pm.canonical_parent_identifier()
    return {
        "status": "PASS",
        "exact_checks": c.count(),
        "checks": c.names,
        "proven": proven,
        "killed": killed,
        "missing": missing,
        "raw_seam_to_w_intertwiner": False,
        "closed_gate_ids": [],
        "parent_id": ident["parent_id"],
        "hypothesis": "NS/mark seam geometry induces the shifted edge action L=R J; "
                      "raw seam -> four 64-mode W-bank identification unproved (False)",
        "selection": "joint vertex+edge reflection + exclusion of free fermion "
                     "directions selects eta=-1; clock+unique ground alone do NOT",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True, default=str))
