#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v774 -- ARF.SPINORCOMPILER.01: the Arf/spinor compiler on V = L/(1+i)L = F2^4 -- Priority 1 of the Arf compiler programme, the exact finite-algebra layer (46/46 checks, ~2 s; discovery probe arf_spinor_compiler_probe.py, 2026-08-05, verdict ARF-SPINOR-EXACT, zero kills, both must-fail controls fire).  THE COMPILER, EXACT END TO END: hbar rebuilt from the concrete v752 lattice (Gram J - I in the family/anchor basis, census 240 = 15 x 16, sigma symplectic; standard-doubled-model cross-check with chi coefficients (0,0,0,1) and y0 = FSUM); brute force over all 2^16 functions gives EXACTLY 16 quadratic refinements; Arf census 6 + 10 with |Sp(4,2)| = 720 by full 65536-matrix census and a faithful+surjective S6 action on the six Arf-1 forms; the frozen selector (sigma-invariance census 4 -> q(A) = 1: 2 -> q(F_Sigma) = 0: 1) picks a UNIQUE refinement q*; the parity lift iota: V ~ C_even(5) satisfies beta(v,w) = iota(v).iota(w) = hbar(v,w) in all 256 cells (crosslink 1), and the weight form q_wt = wt(iota)/2 IS q* (offset 0; the 16 refinements are q* + hbar(., c) bijectively over all 16 c); Stab(q*) of order 120 acts as S5 with orbits {1, 5, 10} on refinements AND words: 16 = 1 + 5bar + 10 as Arf geometry; the K6 duad model v <-> D(v) = {q Arf-1 : q(v) = 0} is a bijection onto E(K6), Sp(4,2)- and sigma-equivariant, vertex split 15 = 5 + 10 at q*; B = I + A_KG(6,2) ENTRYWISE in all 225 cells, charpoly (x-7)(x-2)^9(x+2)^5, ovoid eigenvector B(1_O - (1/3)1) = -2(1_O - (1/3)1) EXACT (Fraction arithmetic; the six ovoid indicators span the (-2)-eigenspace, rank 5); all 6 fully isotropic spreads of PG(3,2) carry q*-signature (1 of 5bar, 2 of 10) per block; the hypercharge table X = (-2,-2,-2,3,3) (primitive, traceless) reproduces the v310/v14 dictionary with values AND multiplicities; the code polynomial P_X has Euler moments (16, 0, 120, 0) with the chain 120/3 = 40, +1 = 41 = 10 b1 (tfpt_constants), 2*120 = 240, +8 = 248 (the v2 master moment Tr_{S+} X^2 = 120 = 5! = |R+(E8)|); Pati--Salam splits 16 = 8 + 8 = (4,2,1) + (4bar,1,2) with the A bit as isospin index and B-L = 1 - 2 n_c/3 exact; chi_NSR(v) = hbar(v, F_Sigma) = the anchor bit a on all 16 words, re-derived in the standard doubled model.  SEMANTIC SEPARATION (naming discipline, no physics claim): sigma acts on the family bits (F1,F2,F3) as the family 3-cycle A3^Fam AND on the five carrier slots of iota as the 3+2 slot split A3^PS -- the SAME group element in two different registers (message bits vs carrier slots), never to be conflated.  HONESTY FENCE: this module is finite exact algebra reproducing corpus objects (v752 incidence, v2/v310 carrier + hypercharge + master moment, v753 canonical form); the PHYSICAL code->matter reading is NOT claimed here -- it is KILLED at root level by v775 (ROOTCLASS-MIXED), and the 'empty mailbox = right-handed neutrino' reading is fenced with it.  Companion Lean module: experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean (23 kernel theorems, decide/norm_num, no sorry, no native_decide, lake build green).  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe arf_spinor_compiler_probe.py (2026-08-05, 46/46, 2.3 s, ARF-SPINOR-EXACT; re-run identical at promotion).  Promoted verbatim; the only transforms: sys.path points at verification/ (the corpus imports v310_carrier_sm_anomaly / tfpt_constants are siblings here) and run() encodes the all-pass pattern (v757 precedent).  Numbers unchanged.

Original probe docstring (verbatim):
arf_spinor_compiler_probe -- ARF.SPINORCOMPILER.01 (Arf compiler
programme, Priority 1): the Arf/spinor compiler on V = L/(1+i)L = F2^4.

THEOREM CANDIDATE (preregistered, twelve+ steps).  The symplectic
four-bit Gaussian quotient (V, hbar) of the unimodular hermitian E8
lattice (v752, basis (F1, F2, F3, A), Gram = all-ones-off-diagonal)
carries a CANONICAL quadratic refinement q* (the parity lift into the
even-weight code C_even(5) on the five carrier slots), and the whole
finite geometry of q* reproduces, in exact integer/F2 arithmetic, the
carrier decomposition S+_{D5} = Lambda^even C^5 = 1 + 5bar + 10
(v2/v310, CAR.SM.01), the projective Hamming incidence of v752 as
I + A_{KG(6,2)} (Kneser on the K6 duads of the six odd theta
characteristics), the hypercharge code polynomial with master moment
Tr_{S+} X^2 = 120 (v2), the Pati--Salam split, and the NS/R parity as
the fourth information bit (v752 P5.3).

THE STEPS (all exact; kill criteria frozen below):
 S1  hbar reconstructed from the CONCRETE lattice exactly as v752
     builds it (same C* placement, same family/anchor recipe); Gram
     in (F1,F2,F3,A) == the all-ones-off-diagonal 4x4; census
     240 = 15 x 16, zero class empty; sigma = family 3-cycle
     F1->F2->F3 fixing A, symplectic; cross-check in the standard
     doubled model incl. chi_NSR coefficients (0,0,0,1), y0 = FSUM.
 S2  ALL quadratic refinements q: V -> F2 with
     q(v+w)+q(v)+q(w) = hbar(v,w), by brute force over all 2^16
     functions: exactly 16.
 S3  ARF CENSUS: 6 refinements of Arf type 1 (6 zeros) + 10 of Arf
     type 0 (10 zeros); |Sp(4,2)| = 720 by full 65536-matrix census;
     Sp orbits on the 16 refinements = {6} u {10}; the action on the
     6 Arf-1 forms is FAITHFUL and SURJECTIVE onto S6 (720 distinct
     permutations): Sp(4,2) ~ S6.
 S4  SELECTOR: sigma-invariance + q(A) = 1 + q(F_Sigma) = 0 selects
     a UNIQUE refinement q* (full sigma-invariance census reported).
 S5  PARITY LIFT: iota(v) = (f1,f2,f3,a,f1+f2+f3+a) in F2^5;
     iota(V) = C_even(5) (the 16 even-weight words);
     beta(v,w) = iota(v).iota(w) mod 2 == hbar (all 256 pairs) --
     crosslink 1, exact matrix identity.
 S6  q_wt(v) = wt(iota(v))/2 mod 2 is a refinement and IS q*
     (identification reported exactly, offset census printed).
 S7  DECOMPOSITION 16 = 1 + 5bar + 10: Stab_{Sp}(q*) has order 120,
     acts on the 16 refinements with orbits {q*} u {5 Arf-1} u
     {10 Arf-0}, faithful+surjective onto S5 on the five; on words:
     {q*=0}\{0} has 5 elements, {q*=1} has 10.
 S8  K6 DUAD MODEL: D(v) = {q Arf-1 : q(v) = 0} is a 2-set for every
     v != 0, D(v) = {q, q + hbar(v,.)}, v <-> D(v) is a BIJECTION
     onto E(K6); Sp(4,2)- (hence sigma-) equivariant; with q* as
     distinguished vertex: 15 = 5 (edges at q*) + 10 (inner edges).
 S9  INCIDENCE EXPLAINED: B = I + A_{KG(6,2)} ENTRYWISE; charpoly
     (x-7)(x-2)^9(x+2)^5; OVOID EIGENVECTOR: for O = {v!=0 :
     q*(v)=0}: B(1_O - (1/3) 1) = -2 (1_O - (1/3) 1) exactly
     (Fraction arithmetic, residual must be zero); the six ovoid
     indicators span the (-2)-eigenspace (exact rank 5 = nullity of
     B + 2I).
 S10 SPREAD TEST: census over all 56 PG(3,2) spreads; every
     ISOTROPIC spread block contains exactly 1 point of the 5bar and
     2 points of the 10 (q*-signature (1,2) per block).
 S11 HYPERCHARGE TABLE: X = (-2,-2,-2,3,3) primitive + traceless;
     the frozen assignment 0->nu^c(0), A->e^c(6), F_i->Q_up(1),
     F_i+A->Q_dn(1), F_i+F_j->u^c(-4), F_i+F_j+A->d^c(2),
     F_Sigma->nu_L(-3), F_Sigma+A->e_L(-3); Y = X/6 reproduces the
     dual-root dictionary values (1/6,-2/3,1/3,-1/2,1,0) with the
     v310/v14 multiplicities (cross-checked against v310.GEN,
     read-only import).
 S12 CODE POLYNOMIAL: P_X(z) = 1 + 3z^-4 + 2z^-3 + 6z + 3z^2 + z^6;
     Euler-derivative moments P(1)=16, DP(1)=0, D^2P(1)=120,
     D^3P(1)=0; chain 120/3 = 40, +1 = 41 = 10*b1 (tfpt_constants),
     2*120 = 240, +8 = 248; master moment Tr_{S+} X^2 = 120 = 5! =
     |R+(E8)| is v2_carrier_pascal's ledger fact.
 S13 PATI--SALAM: p_F = f1+f2+f3 splits 16 = 8 + 8 = (4,2,1) +
     (4bar,1,2) with A as the isospin index on each side;
     B-L = 1 - 2 n_c/3 exact per class; sigma acts on the FIVE
     carrier slots of iota as the 3+2 split (slots {1,2,3} cycled,
     slots {4,5} fixed).
 S14 NS/R CROSSLINK: chi_NSR(v) = hbar(v, F_Sigma) = a (the fourth
     information bit), exact in the v752 basis AND re-derived in the
     standard doubled model; the four A-pairings nu^c<->e^c,
     u^c<->d^c, Q_up<->Q_dn, nu_L<->e_L each carry chi = (0, 1).
 C   MUST-FAIL CONTROLS: (C1) the non-alternating dot form admits
     ZERO quadratic refinements (the identity forces alternation);
     (C2) the mutated charge X' = (-2,-2,-2,3,2) breaks
     tracelessness AND the master moment 120.

KILLS (frozen, any one fires => ARF-SPINOR-KILLED):
  K1  Gram of hbar in (F1,F2,F3,A) != all-ones-off-diagonal, or the
      v752 census/sigma structure breaks, or the standard-model
      cross-check (chi coefficients, y0 = FSUM) deviates.
  K2  number of quadratic refinements != 16.
  K3  Arf census != (6 of type 1, 10 of type 0), or |Sp(4,2)| != 720,
      or the S6 action is not faithful+surjective, or the Sp orbits
      on the refinements are not {6} u {10}.
  K4  the frozen selector does not pick a UNIQUE form.
  K5  iota(V) != C_even(5), or beta != hbar in ANY of the 256 cells.
  K6  the parity-lift q_wt is not a refinement or is NOT q*.
  K7  Stab(q*) orbit sizes != {1, 5, 10}, or the word decomposition
      != 1 + 5 + 10.
  K8  the duad map is not bijective onto E(K6) or not
      Sp/sigma-equivariant, or the vertex split != 5 + 10.
  K9  B != I + A_{KG(6,2)} in a single cell, or the spectrum
      multiplicities != (1, 9, 5), or the ovoid eigenvector has a
      nonzero residual, or the six ovoid indicators do not span the
      (-2)-eigenspace.
  K10 an isotropic spread block with q*-signature != (1 of 5bar,
      2 of 10).
  K11 X not primitive/traceless, or the frozen assignment table
      deviates, or Y = X/6 does not reproduce the v310 dictionary
      (values AND multiplicities).
  K12 any moment of P_X deviates from (16, 0, 120, 0), or the chain
      40/41/240/248 breaks.
  K13 the Pati--Salam split is not 8+8 with the A-doublet structure,
      or B-L = 1 - 2 n_c/3 deviates, or sigma does not act as the
      3+2 slot split.
  K14 chi_NSR != a on any of the 16 words (either model), or an
      A-pairing fails.
VERDICTS (frozen): ARF-SPINOR-EXACT / ARF-SPINOR-KILLED / TEST-VOID
(a must-fail control does not fire).

SEMANTIC SEPARATION (user's correction, naming discipline, no physics
claim): sigma acts on the FAMILY bits (F1,F2,F3) of V as the family
3-cycle A3^Fam; the SAME sigma acts on the five CARRIER slots of
iota(V) as the 3+2 split (three cycled slots + two fixed slots).
The 3+2 slot split is the Pati--Salam-style colour+weak partition
A3^PS of the carrier legs and must NOT be conflated with the family
cycle: same group element, two different registers (message bits vs
carrier slots).  This is a naming discipline, not a physics claim.

HONESTY FENCE: this probe proves finite exact algebra and reproduces
corpus objects (v752 incidence, v2/v310 carrier + hypercharge + master
moment, v753 canonical form).  The PHYSICAL reading -- that q*/Arf is
a matter classifier -- is NOT claimed here; that reading is Priority
2's preregistered kill test (separate worker).  Nothing in this file
moves a status marker.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface
beruehrt.  Exakte Ganzzahl/Fraction/F2-Arithmetik durchgehend; sympy
nur fuer das charakteristische Polynom (gated); keine Floats, kein
RNG, kein Fit, kein freier Parameter.

Quellen (read-only): verification/v752_projective_hamming_incidence.py
(hbar, Basis, Inzidenz, chi_NSR), verification/v753_ramified_polarity.py
(Kanonizitaet der Form), verification/v2_carrier_pascal.py (Pascal
1+5+10, Tr X^2 = 120), verification/v310_carrier_sm_anomaly.py (GEN:
die SM-Generation mit Y-Werten), verification/v14_carrier_uniqueness.py
(3+2 split), note_e8_gaussian_code.tex (Code-Layer-Konventionen).

Lean-Gegenstueck: experiments/lean4-carrier-rigidity/TfptCarrier/
ArfSpinorCompiler.lean (kernel decide / norm_num, kein sorry, kein
native_decide).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/arf_spinor_compiler_probe.py
"""

import itertools
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr
from math import gcd

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

T0 = time.time()
CHECKS = []
KILLS = []


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ======================================================================
# v752 machinery, copied VERBATIM (P0/P1/P5 recipe; deterministic)
# ======================================================================
G_NAIVE = [(1, 0, 0, 0, 0, 1, 1, 1),
           (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1),
           (0, 0, 0, 1, 1, 1, 1, 0)]
C_NAIVE = frozenset(tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
                          for j in range(8))
                    for m in itertools.product((0, 1), repeat=4))
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)
CSTAR_SUPPORTS_EXPECTED = [
    (0, 1, 2, 3), (0, 1, 4, 5), (0, 1, 6, 7), (0, 2, 4, 6), (0, 2, 5, 7),
    (0, 3, 4, 7), (0, 3, 5, 6), (1, 2, 4, 7), (1, 2, 5, 6), (1, 3, 4, 6),
    (1, 3, 5, 7), (2, 3, 4, 5), (2, 3, 6, 7), (4, 5, 6, 7)]


def apply_perm(c, p):
    return tuple(c[p[k]] for k in range(8))


def code_image(code, p):
    return frozenset(apply_perm(c, p) for c in code)


def supports_w4(code):
    return sorted(tuple(i for i in range(8) if w[i])
                  for w in code if sum(w) == 4)


def mat_det_inv(rows):
    n = len(rows)
    A = [[Fr(v) for v in r] for r in rows]
    I = [[Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]
    det = Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] != 0), None)
        if piv is None:
            return Fr(0), None
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            I[col], I[piv] = I[piv], I[col]
            det = -det
        det *= A[col][col]
        inv = 1 / A[col][col]
        A[col] = [a * inv for a in A[col]]
        I[col] = [a * inv for a in I[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [a - f * b for a, b in zip(A[r], A[col])]
                I[r] = [a - f * b for a, b in zip(I[r], I[col])]
    return det, I


def vec_mat(x, M):
    n = len(M)
    return tuple(sum(x[i] * M[i][j] for i in range(n)) for j in range(n))


def row_hnf(rows):
    M = [list(map(int, r)) for r in rows]
    m = len(M)
    for col in range(m):
        piv = next(r for r in range(col, m) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        for r in range(col + 1, m):
            while M[r][col] != 0:
                q = M[col][col] // M[r][col]
                M[col] = [a - q * b for a, b in zip(M[col], M[r])]
                M[col], M[r] = M[r], M[col]
        if M[col][col] < 0:
            M[col] = [-a for a in M[col]]
    return M


def hnf_reduce(c, H):
    c = list(c)
    for i in range(len(H)):
        q = c[i] // H[i][i]
        if q:
            c = [a - q * b for a, b in zip(c, H[i])]
    return tuple(c)


def J_vec(x):
    out = []
    for k in range(0, 8, 2):
        out += [-x[k + 1], x[k]]
    return tuple(out)


def sig_vec(x):
    return (x[4], x[5], x[0], x[1], x[2], x[3], x[6], x[7])


def add_vec(x, y):
    return tuple(a + b for a, b in zip(x, y))


def ip(x, y):
    return sum(a * b for a, b in zip(x, y))


def f2_rref(words):
    rows = [list(w) for w in sorted(words, reverse=True) if any(w)]
    basis, pivots = [], []
    for r in rows:
        r = r[:]
        for b, pv in zip(basis, pivots):
            if r[pv]:
                r = [(a + c) % 2 for a, c in zip(r, b)]
        if any(r):
            basis.append(r)
            pivots.append(next(i for i, a in enumerate(r) if a))
    return basis, pivots


def make_lattice(in_lat, basis_rows):
    det, Binv = mat_det_inv(basis_rows)
    lat = {"in": in_lat, "B": basis_rows, "det": det, "Binv": Binv}

    def coords(x):
        c = vec_mat(x, Binv)
        assert all(v.denominator == 1 for v in c), "kein Gittervektor"
        return tuple(int(v) for v in c)

    A = [coords(add_vec(b, J_vec(b))) for b in basis_rows]
    H = row_hnf(A)
    lat["coords"] = coords
    lat["A"] = A
    lat["H"] = H
    lat["label"] = lambda x: hnf_reduce(coords(x), H)
    return lat


def constrA_lattice(code):
    cb, pivots = f2_rref(code)
    rows = [tuple(r) for r in cb]
    rows += [tuple(2 if i == j else 0 for i in range(8))
             for j in range(8) if j not in pivots]
    return make_lattice(lambda x: tuple(v % 2 for v in x) in code, rows)


def constrA_roots(code):
    return [x for x in itertools.product(range(-2, 3), repeat=8)
            if sum(v * v for v in x) == 4
            and tuple(v % 2 for v in x) in code]


def label_group(lat):
    reps = {hnf_reduce((0,) * 8, lat["H"]): (0,) * 8}
    frontier = [(0,) * 8]
    while frontier:
        v = frontier.pop()
        for b in lat["B"]:
            w = add_vec(v, b)
            l = lat["label"](w)
            if l not in reps:
                reps[l] = w
                frontier.append(w)
    return reps


def family_anchor_basis(lat, reps, zero_label, sig_label_fn):
    """v689-I2.6-Rezept: (F1, F2, F3, ANC)-Basis + Bit-Koordinaten."""
    fixed_labels = [lb for lb in reps if sig_label_fn(lb) == lb]
    fam_basis = None
    for lb in reps:
        if lb == zero_label or sig_label_fn(lb) == lb:
            continue
        o1 = lb
        o2 = sig_label_fn(lb)
        o3 = sig_label_fn(o2)
        s = lat["label"](add_vec(add_vec(reps[o1], reps[o2]), reps[o3]))
        if s == zero_label:
            continue
        span3 = set()
        for bits in itertools.product((0, 1), repeat=3):
            w = (0,) * 8
            for bit, l2 in zip(bits, (o1, o2, o3)):
                if bit:
                    w = add_vec(w, reps[l2])
            span3.add(lat["label"](w))
        if len(span3) != 8:
            continue
        anchor = next(l2 for l2 in fixed_labels
                      if l2 != zero_label and l2 not in span3)
        fam_basis = (o1, o2, o3, anchor, s)
        break
    assert fam_basis is not None
    o1, o2, o3, anc, fsum = fam_basis
    bits_of = {}
    for bits in itertools.product((0, 1), repeat=4):
        v = (0,) * 8
        for bit, l2 in zip(bits, (o1, o2, o3, anc)):
            if bit:
                v = add_vec(v, reps[l2])
        bits_of[lat["label"](v)] = bits
    return fam_basis, bits_of


def herm(x, y):
    """h(x,y) = (<x,y> + i <x,Jy>)/2 als Paar (Re, Im) in Z[i]."""
    re2, im2 = ip(x, y), ip(x, J_vec(y))
    assert re2 % 2 == 0 and im2 % 2 == 0, "h nicht Z[i]-wertig"
    return (re2 // 2, im2 // 2)


def hbar_vec(x, y):
    h = herm(x, y)
    return (h[0] + h[1]) % 2


# ======================================================================
# abstract F2^4 layer in the family/anchor coordinates (f1, f2, f3, a)
# ======================================================================
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}
GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]  # J - I


def hb(v, w):
    return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
               for j in range(4)) % 2


def xor(v, w):
    return tuple((a + b) % 2 for a, b in zip(v, w))


ADD = [[WIDX[xor(v, w)] for w in W16] for v in W16]
HTAB = [[hb(v, w) for w in W16] for v in W16]
NZ15 = [w for w in W16 if any(w)]
A_BIT = (0, 0, 0, 1)
FSIG = (1, 1, 1, 0)


def sig_bits(v):
    """sigma in family coordinates: F1->F2->F3->F1, A fixed."""
    return (v[2], v[0], v[1], v[3])


def iota(v):
    f1, f2, f3, a = v
    return (f1, f2, f3, a, (f1 + f2 + f3 + a) % 2)


def frac_rank(rows):
    """exact rank over Q (Fraction elimination, no floats)."""
    M = [[Fr(x) for x in r] for r in rows]
    rank, col = 0, 0
    nrows, ncols = len(M), len(M[0]) if M else 0
    for col in range(ncols):
        piv = next((r for r in range(rank, nrows) if M[r][col] != 0), None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = 1 / M[rank][col]
        M[rank] = [x * inv for x in M[rank]]
        for r in range(nrows):
            if r != rank and M[r][col] != 0:
                f = M[r][col]
                M[r] = [x - f * y for x, y in zip(M[r], M[rank])]
        rank += 1
        if rank == nrows:
            break
    return rank


# ======================================================================
# S1 -- hbar from the concrete lattice, exactly as v752 builds it
# ======================================================================
def s1_lattice():
    section("S1: hbar rekonstruiert wie v752 (C*, Gitter, Familienbasis)")
    all_placements = set()
    for p in itertools.permutations(range(8)):
        all_placements.add(code_image(C_NAIVE, p))
    both_inv = [c for c in sorted(all_placements, key=lambda c: sorted(c))
                if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
    W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
    CSTAR = [c for c in both_inv if W0246 in c][0]
    ROOTS = constrA_roots(CSTAR)
    LAT = constrA_lattice(CSTAR)
    REPS = label_group(LAT)
    ZERO = LAT["label"]((0,) * 8)
    census = Counter(LAT["label"](r) for r in ROOTS)
    check("S1.1 C* deterministisch (v638-Rezept), 240 Wurzeln, 16 Klassen,"
          " Zensus 15 x 16, Nullklasse leer",
          supports_w4(CSTAR) == CSTAR_SUPPORTS_EXPECTED and len(ROOTS) == 240
          and len(REPS) == 16 and len(census) == 15
          and sorted(census.values()) == [16] * 15 and ZERO not in census,
          kill="K1")

    def sig_label(lb):
        return LAT["label"](sig_vec(REPS[lb]))

    fixed_nz = [lb for lb in REPS if lb != ZERO and sig_label(lb) == lb]
    check("S1.2 sigma^3 = id auf den Labels, 3 fixe nichttriviale Klassen",
          all(sig_label(sig_label(sig_label(lb))) == lb for lb in REPS)
          and len(fixed_nz) == 3, kill="K1")

    FAM, BITS = family_anchor_basis(LAT, REPS, ZERO, sig_label)
    F1L, F2L, F3L, ANCL, FSUML = FAM
    FAM_VECS = [REPS[F1L], REPS[F2L], REPS[F3L], REPS[ANCL]]
    GFAM = [[hbar_vec(FAM_VECS[i], FAM_VECS[j]) for j in range(4)]
            for i in range(4)]
    print("    GFAM (F1,F2,F3,A) = %s" % GFAM)
    check("S1.3 Gram von hbar in (F1,F2,F3,A) == all-ones-off-diagonal "
          "(J - I)", GFAM == GJI, kill="K1")

    ok_repr = all(hbar_vec(REPS[lx], REPS[ly]) == hb(BITS[lx], BITS[ly])
                  for lx in REPS for ly in REPS)
    check("S1.4 hbar == Bit-Form auf allen 256 Label-Paaren "
          "(abstrakte Schicht = Gitterschicht)", ok_repr, kill="K1")

    ok_sig_bits = all(BITS[sig_label(lb)] == sig_bits(BITS[lb])
                      for lb in REPS)
    ok_sig_h = all(hb(sig_bits(v), sig_bits(w)) == hb(v, w)
                   for v in W16 for w in W16)
    check("S1.5 sigma in Bits = Familien-3-Zyklus (f1,f2,f3,a) -> "
          "(f3,f1,f2,a), fixiert A; symplektisch (256 Paare)",
          ok_sig_bits and ok_sig_h, kill="K1")

    check("S1.6 F_Sigma = F1+F2+F3 ist das Koordinaten-Label (FSUM), "
          "sigma-fix; BITS[FSUM] = (1,1,1,0), BITS[ANC] = (0,0,0,1)",
          BITS[FSUML] == FSIG and BITS[ANCL] == A_BIT
          and sig_label(FSUML) == FSUML, kill="K1")

    # standard doubled model: chi_NSR cross-check (v752 P5 recipe)
    def in_E8_std(x):
        par = {v % 2 for v in x}
        return len(par) == 1 and sum(x) % 4 == 0

    B_STD = [(4, 0, 0, 0, 0, 0, 0, 0), (-2, 2, 0, 0, 0, 0, 0, 0),
             (0, -2, 2, 0, 0, 0, 0, 0), (0, 0, -2, 2, 0, 0, 0, 0),
             (0, 0, 0, -2, 2, 0, 0, 0), (0, 0, 0, 0, -2, 2, 0, 0),
             (0, 0, 0, 0, 0, -2, 2, 0), (1, 1, 1, 1, 1, 1, 1, 1)]
    LATS = make_lattice(in_E8_std, list(B_STD))
    ZEROS = LATS["label"]((0,) * 8)
    roots_std = []
    for v in itertools.product(range(-1, 2), repeat=8):
        if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
            roots_std.append(tuple(2 * a for a in v))
    for y in itertools.product((0, -1), repeat=8):
        v = tuple(2 * a + 1 for a in y)
        if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
            roots_std.append(v)
    REPS_S = label_group(LATS)
    census_s = Counter(LATS["label"](r) for r in roots_std)

    def parity(w):
        return w[0] % 2

    chi = {lb: parity(REPS_S[lb]) % 2 for lb in REPS_S}
    class_par = {}
    pure = True
    for r in roots_std:
        lb = LATS["label"](r)
        p = parity(r)
        if lb in class_par and class_par[lb] != p:
            pure = False
        class_par[lb] = p

    def sig_label_s(lb):
        return LATS["label"](sig_vec(REPS_S[lb]))

    FAM_S, BITS_S = family_anchor_basis(LATS, REPS_S, ZEROS, sig_label_s)
    F1S, F2S, F3S, ANCS, FSUMS = FAM_S
    FAM_VECS_S = [REPS_S[F1S], REPS_S[F2S], REPS_S[F3S], REPS_S[ANCS]]

    def herm_std(w, v):
        re4, im4 = ip(w, v), ip(w, J_vec(v))
        assert re4 % 4 == 0 and im4 % 4 == 0
        return (re4 // 4, im4 // 4)

    def hbar_std(w, v):
        h = herm_std(w, v)
        return (h[0] + h[1]) % 2

    GFAM_S = [[hbar_std(FAM_VECS_S[i], FAM_VECS_S[j]) for j in range(4)]
              for i in range(4)]
    chi_coeff = tuple(chi[lb] for lb in (F1S, F2S, F3S, ANCS))
    y0 = [lb for lb in REPS_S if lb != ZEROS
          and all(hbar_std(REPS_S[lx], REPS_S[lb]) == chi[lx]
                  for lx in REPS_S)]
    check("S1.7 STANDARDMODELL-KREUZCHECK: Zensus 15 x 16, NS/R-Puritaet,"
          " GFAM == J - I auch dort, chi-Koeffizienten (F1,F2,F3,A) = "
          "%s == (0,0,0,1), y0 = FSUM (eindeutig)" % (chi_coeff,),
          len(census_s) == 15 and sorted(census_s.values()) == [16] * 15
          and ZEROS not in census_s and pure
          and GFAM_S == GJI and chi_coeff == (0, 0, 0, 1)
          and y0 == [FSUMS], kill="K1")
    return dict(BITS=BITS, REPS=REPS, ZERO=ZERO)


# ======================================================================
# S2 -- all quadratic refinements by brute force over 2^16 functions
# ======================================================================
def s2_refinements():
    section("S2: ALLE quadratischen Verfeinerungen (Brute force 2^16)")
    refs = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for i in range(16):
            hrow = HTAB[i]
            arow = ADD[i]
            qi = q[i]
            for j in range(16):
                if q[arow[j]] ^ qi ^ q[j] != hrow[j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            refs.append(tuple(q))
    check("S2.1 GENAU 16 Verfeinerungen q mit q(v+w)+q(v)+q(w) = "
          "hbar(v,w) (Brute force ueber alle 65536 Funktionen); alle "
          "mit q(0) = 0",
          len(refs) == 16 and all(q[WIDX[(0, 0, 0, 0)]] == 0
                                  for q in refs),
          "gefunden: %d" % len(refs), kill="K2")
    return refs


# ======================================================================
# S3 -- Arf census + Sp(4,2) = S6
# ======================================================================
def mat_apply(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(4)) % 2
                 for i in range(4))


def s3_arf_sp(refs):
    section("S3: Arf-Zensus 6 + 10 und Sp(4,2) ~ S6")
    zeros = {q: sum(1 for i in range(16) if q[i] == 0) for q in refs}
    cen = Counter(zeros.values())
    arf1 = sorted(q for q in refs if zeros[q] == 6)
    arf0 = sorted(q for q in refs if zeros[q] == 10)
    check("S3.1 ARF-ZENSUS: 6 Formen mit 6 Nullstellen (Arf 1) + 10 mit "
          "10 Nullstellen (Arf 0): %s" % dict(sorted(cen.items())),
          cen == Counter({6: 6, 10: 10}), kill="K3")

    sp = []
    for bits in range(1 << 16):
        M = [[(bits >> (4 * i + j)) & 1 for j in range(4)]
             for i in range(4)]
        ok = True
        for i in range(4):
            ei = tuple(1 if k == i else 0 for k in range(4))
            for j in range(4):
                ej = tuple(1 if k == j else 0 for k in range(4))
                if hb(mat_apply(M, ei), mat_apply(M, ej)) != GJI[i][j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            sp.append(M)
    perms = []
    ok_bij = True
    for M in sp:
        p = [WIDX[mat_apply(M, w)] for w in W16]
        if len(set(p)) != 16:
            ok_bij = False
        perms.append(tuple(p))
    check("S3.2 |Sp(4,2)| = %d == 720 (voller 65536-Matrix-Zensus); "
          "alle Elemente bijektiv auf V" % len(sp),
          len(sp) == 720 and ok_bij and len(set(perms)) == 720,
          kill="K3")

    inv_perms = []
    for p in perms:
        q = [0] * 16
        for i, pi in enumerate(p):
            q[pi] = i
        inv_perms.append(tuple(q))

    refset = set(refs)

    def act(q, ipm):
        return tuple(q[ipm[i]] for i in range(16))

    ok_closed = all(act(q, ipm) in refset for q in refs
                    for ipm in inv_perms[:8])
    # orbits of the full group on the 16 refinements
    orbits = []
    seen = set()
    for q in refs:
        if q in seen:
            continue
        orb = {act(q, ipm) for ipm in inv_perms}
        seen |= orb
        orbits.append(orb)
    osizes = sorted(len(o) for o in orbits)
    check("S3.3 Sp-Orbits auf den 16 Verfeinerungen = {6} u {10} "
          "(Arf ist die einzige Invariante): %s" % osizes,
          osizes == [6, 10] and ok_closed
          and set(map(len, orbits)) == {6, 10}
          and all((zeros[next(iter(o))] == 6) == (len(o) == 6)
                  for o in orbits), kill="K3")

    s6_perms = set()
    faithful = True
    for ipm in inv_perms:
        pp = tuple(arf1.index(act(q, ipm)) for q in arf1)
        if pp in s6_perms:
            faithful = False
        s6_perms.add(pp)
    check("S3.4 Wirkung auf den 6 Arf-1-Formen: TREU (720 verschiedene "
          "Permutationen) und SURJEKTIV auf S6 (720 = |S6|): "
          "Sp(4,2) ~ S6", faithful and len(s6_perms) == 720, kill="K3")
    return dict(arf1=arf1, arf0=arf0, zeros=zeros, sp=sp, perms=perms,
                inv_perms=inv_perms, act=act)


# ======================================================================
# S4 -- the frozen selector
# ======================================================================
def s4_selector(refs, ctx3):
    section("S4: der eingefrorene Selektor (sigma-invariant, q(A)=1, "
            "q(F_Sigma)=0)")
    sig_perm = [WIDX[sig_bits(w)] for w in W16]
    sig_inv = all(sig_perm[sig_perm[sig_perm[i]]] == i for i in range(16))
    assert sig_inv
    siginv = [q for q in refs
              if all(q[sig_perm[i]] == q[i] for i in range(16))]
    cand_a = [q for q in siginv if q[WIDX[A_BIT]] == 1]
    cand = [q for q in cand_a if q[WIDX[FSIG]] == 0]
    arf_of = {q: (1 if ctx3["zeros"][q] == 6 else 0) for q in refs}
    print("    sigma-invariante Verfeinerungen: %d (Arf-Typen %s); "
          "davon q(A)=1: %d; davon zusaetzlich q(F_Sigma)=0: %d"
          % (len(siginv), sorted(arf_of[q] for q in siginv),
             len(cand_a), len(cand)))
    check("S4.1 SELEKTOR EINDEUTIG: sigma-Invarianz-Zensus 4, mit "
          "q(A) = 1: 2, mit q(F_Sigma) = 0: GENAU 1 Form q*",
          len(siginv) == 4 and len(cand_a) == 2 and len(cand) == 1,
          kill="K4")
    qstar = cand[0]
    check("S4.2 q* hat Arf-Typ 1 (6 Nullstellen)",
          ctx3["zeros"][qstar] == 6, kill="K4")
    return qstar


# ======================================================================
# S5 -- parity lift and beta = hbar
# ======================================================================
def s5_parity_lift():
    section("S5: Paritaets-Lift iota und beta == hbar (Crosslink 1)")
    img = {iota(v) for v in W16}
    ceven = {w for w in itertools.product((0, 1), repeat=5)
             if sum(w) % 2 == 0}
    check("S5.1 iota(V) == C_even(5): 16 Worte gerader Laenge-5-Gewichte,"
          " iota injektiv",
          img == ceven and len(img) == 16, kill="K5")
    ok_beta = all(sum(x * y for x, y in zip(iota(v), iota(w))) % 2
                  == hb(v, w) for v in W16 for w in W16)
    check("S5.2 beta(v,w) = iota(v).iota(w) mod 2 == hbar(v,w) EXAKT in "
          "allen 256 Zellen", ok_beta, kill="K5")


# ======================================================================
# S6 -- the weight refinement IS q*
# ======================================================================
def s6_weight_form(refs, qstar):
    section("S6: q_wt = wt(iota)/2 mod 2 -- Identifikation mit q*")
    qwt = tuple((sum(iota(w)) // 2) % 2 for w in W16)
    check("S6.1 q_wt ist eine der 16 Verfeinerungen", qwt in set(refs),
          kill="K6")
    # offset census: every refinement is q* + hbar(., c) for unique c
    offs = {}
    for q in refs:
        cs = [c for c in W16
              if all(q[i] == (qstar[i] + HTAB[i][WIDX[c]]) % 2
                     for i in range(16))]
        offs[q] = cs
    ok_param = all(len(cs) == 1 for cs in offs.values())
    print("    Offset-Zensus: jede Verfeinerung = q* + hbar(., c) mit "
          "eindeutigem c; Offsets = alle 16 Vektoren: %s"
          % (sorted(offs[q][0] for q in refs) == sorted(W16)))
    check("S6.2 q_wt IST q* (Offset c = 0); Parametrisierung "
          "q_c = q* + hbar(., c) bijektiv ueber alle 16 c",
          qwt == qstar and ok_param
          and sorted(offs[q][0] for q in refs) == sorted(W16),
          "offset(q_wt) = %s" % (offs[qwt],), kill="K6")
    return offs


# ======================================================================
# S7 -- the 1 + 5bar + 10 decomposition
# ======================================================================
def s7_decomposition(refs, qstar, ctx3):
    section("S7: 16 = 1 + 5bar + 10 (Stab(q*)-Orbits und Worte)")
    act, inv_perms, perms = ctx3["act"], ctx3["inv_perms"], ctx3["perms"]
    stab_idx = [k for k in range(720)
                if act(qstar, inv_perms[k]) == qstar]
    check("S7.1 |Stab_Sp(q*)| = %d == 120" % len(stab_idx),
          len(stab_idx) == 120, kill="K7")
    orbits = []
    seen = set()
    for q in refs:
        if q in seen:
            continue
        orb = {act(q, inv_perms[k]) for k in stab_idx}
        seen |= orb
        orbits.append(orb)
    osz = sorted(len(o) for o in orbits)
    arf1_rest = [q for q in ctx3["arf1"] if q != qstar]
    ok_types = any(o == {qstar} for o in orbits) \
        and any(o == set(arf1_rest) for o in orbits) \
        and any(o == set(ctx3["arf0"]) for o in orbits)
    check("S7.2 Stab(q*)-Orbits auf den 16 Verfeinerungen: Groessen %s "
          "== [1, 5, 10], und zwar {q*} u {5 restliche Arf-1} u "
          "{10 Arf-0}" % osz, osz == [1, 5, 10] and ok_types, kill="K7")

    s5_perms = set()
    for k in stab_idx:
        pp = tuple(arf1_rest.index(act(q, inv_perms[k]))
                   for q in arf1_rest)
        s5_perms.add(pp)
    check("S7.3 Stab(q*) auf den 5 restlichen Arf-1-Formen: treu + "
          "surjektiv auf S5 (120 Permutationen)",
          len(s5_perms) == 120, kill="K7")

    five = [w for w in NZ15 if qstar[WIDX[w]] == 0]
    ten = [w for w in W16 if qstar[WIDX[w]] == 1]
    check("S7.4 WORTE: {q*=0}\\{0} hat 5 Elemente (5bar), {q*=1} hat 10 "
          "(10); 1 + 5 + 10 = 16",
          len(five) == 5 and len(ten) == 10, kill="K7")
    return dict(five=five, ten=ten, stab_idx=stab_idx)


# ======================================================================
# S8 -- the K6 duad model
# ======================================================================
def s8_duads(qstar, ctx3, ctx7):
    section("S8: das K6-Duaden-Modell V\\{0} ~ E(K6)")
    arf1 = ctx3["arf1"]
    duad = {}
    ok_pair = True
    for v in NZ15:
        dv = [q for q in arf1 if q[WIDX[v]] == 0]
        if len(dv) != 2:
            ok_pair = False
        else:
            q0, q1 = dv
            shifted = tuple((q0[i] + HTAB[i][WIDX[v]]) % 2
                            for i in range(16))
            if shifted != q1:
                ok_pair = False
        duad[v] = frozenset(dv)
    check("S8.1 KANONISCHE REGEL: D(v) = {q Arf-1 : q(v) = 0} ist fuer "
          "jedes v != 0 ein 2-SET, und D(v) = {q, q + hbar(v,.)}",
          ok_pair, kill="K8")
    check("S8.2 BIJEKTION: v <-> D(v) trifft alle C(6,2) = 15 Duaden",
          len(set(duad.values())) == 15
          and all(len(d) == 2 for d in duad.values()), kill="K8")

    act, inv_perms, perms = ctx3["act"], ctx3["inv_perms"], ctx3["perms"]
    ok_equi = True
    for k in range(720):
        p, ipm = perms[k], inv_perms[k]
        for v in NZ15:
            gv = W16[p[WIDX[v]]]
            if duad[gv] != frozenset(act(q, ipm) for q in duad[v]):
                ok_equi = False
                break
        if not ok_equi:
            break
    sig_perm = [WIDX[sig_bits(w)] for w in W16]
    sig_in_sp = tuple(sig_perm) in set(perms)
    check("S8.3 Sp(4,2)-AEQUIVARIANZ: D(g v) = g . D(v) fuer alle 720 g "
          "und alle 15 v; sigma in Sp(4,2) (also sigma-aequivariant)",
          ok_equi and sig_in_sp, kill="K8")

    edges_at = [v for v in NZ15 if qstar in duad[v]]
    inner = [v for v in NZ15 if qstar not in duad[v]]
    check("S8.4 q* als ausgezeichneter Knoten: 15 = 5 (Kanten an q*) + "
          "10 (innere Kanten); Kanten an q* == 5bar-Worte, innere == "
          "10-Worte",
          sorted(edges_at) == sorted(ctx7["five"])
          and sorted(inner) == sorted(ctx7["ten"]), kill="K8")
    return duad


# ======================================================================
# S9 -- incidence = I + Kneser, spectrum, ovoid eigenvectors
# ======================================================================
def s9_incidence(qstar, ctx3, duad):
    section("S9: B = I + A_KG(6,2), Spektrum 7/2^9/(-2)^5, "
            "Ovoid-Eigenvektoren")
    pts = sorted(NZ15)
    n = 15
    B = [[1 if hb(x, y) == 0 else 0 for y in pts] for x in pts]
    ok_kneser = True
    for i in range(n):
        for j in range(n):
            if i == j:
                want = 1
            else:
                want = 1 if not (duad[pts[i]] & duad[pts[j]]) else 0
            if B[i][j] != want:
                ok_kneser = False
    check("S9.1 B == I + A_{KG(6,2)} ENTRYWISE (Diagonale 1; x != y "
          "benachbart gdw. Duaden disjunkt) -- alle 225 Zellen",
          ok_kneser, kill="K9")

    BBt = [[sum(B[i][k] * B[j][k] for k in range(n)) for j in range(n)]
           for i in range(n)]
    ok_bbt = all(BBt[i][j] == (7 if i == j else 3)
                 for i in range(n) for j in range(n))
    from sympy import Matrix, symbols, expand   # gated: charpoly only
    xs = symbols("x")
    cp = Matrix(B).charpoly(xs).as_expr()
    cp_t = expand((xs - 7) * (xs - 2) ** 9 * (xs + 2) ** 5)
    check("S9.2 B B^T = 4I + 3J exakt; char. Polynom = "
          "(x-7)(x-2)^9(x+2)^5 (Kneser-Theorie: KG(6,2)-Eigenwerte "
          "6/1/-3 + I => 7/2/-2 mit Multiplizitaeten 1/9/5)",
          ok_bbt and expand(cp - cp_t) == 0, kill="K9")

    O = set(v for v in NZ15 if qstar[WIDX[v]] == 0)
    u = [Fr(1) if pts[i] in O else Fr(0) for i in range(n)]
    third = Fr(1, 3)
    vec = [u[i] - third for i in range(n)]
    Bv = [sum(Fr(B[i][j]) * vec[j] for j in range(n)) for i in range(n)]
    resid = [Bv[i] + 2 * vec[i] for i in range(n)]
    check("S9.3 OVOID-EIGENVEKTOR: B(1_O - (1/3) 1) = -2 (1_O - (1/3) 1) "
          "EXAKT (Fraction; Residuum identisch 0)",
          all(r == 0 for r in resid), kill="K9")

    rows6 = []
    for q in ctx3["arf1"]:
        Oq = set(v for v in NZ15 if q[WIDX[v]] == 0)
        rows6.append([3 * (1 if pts[i] in Oq else 0) - 1
                      for i in range(n)])
    ok_eig6 = True
    for r in rows6:
        br = [sum(B[i][j] * r[j] for j in range(n)) for i in range(n)]
        if any(br[i] != -2 * r[i] for i in range(n)):
            ok_eig6 = False
    rk6 = frac_rank(rows6)
    Bp2 = [[B[i][j] + (2 if i == j else 0) for j in range(n)]
           for i in range(n)]
    rkB2 = frac_rank(Bp2)
    check("S9.4 die 6 Ovoid-Indikatoren (3 1_Oq - 1) sind (-2)-"
          "Eigenvektoren; Rang %d == 5 == 15 - Rang(B + 2I) = 15 - %d: "
          "sie SPANNEN den (-2)-Eigenraum" % (rk6, rkB2),
          ok_eig6 and rk6 == 5 and rkB2 == 10, kill="K9")


# ======================================================================
# S10 -- the spread test
# ======================================================================
def s10_spreads(qstar):
    section("S10: Spreads -- q*-Signatur (1, 2) pro isotropem Block")
    pts = sorted(NZ15)
    lines = set()
    for a, b in itertools.combinations(pts, 2):
        c = xor(a, b)
        lines.add(frozenset({a, b, c}))
    by_pt = {}
    for L in lines:
        for p in L:
            by_pt.setdefault(p, []).append(L)

    def find_spreads(covered, used):
        if len(covered) == 15:
            return [frozenset(used)]
        p = next(x for x in pts if x not in covered)
        out = []
        for L in by_pt[p]:
            if covered & L:
                continue
            out += find_spreads(covered | L, used + [L])
        return out

    spreads = set(find_spreads(frozenset(), []))
    iso_line = {L: all(hb(a, b) == 0 for a in L for b in L)
                for L in lines}
    iso_spreads = [S for S in spreads if all(iso_line[L] for L in S)]
    n_iso_lines = sum(1 for L in lines if iso_line[L])
    check("S10.1 56 PG(3,2)-Spreads; %d isotrope Geraden (GQ(2,2)); "
          "%d vollstaendig isotrope Spreads"
          % (n_iso_lines, len(iso_spreads)),
          len(spreads) == 56 and n_iso_lines == 15
          and len(iso_spreads) >= 1)

    ok_sig = True
    sigs = Counter()
    for S in iso_spreads:
        for L in S:
            n0 = sum(1 for v in L if qstar[WIDX[v]] == 0)
            n1 = sum(1 for v in L if qstar[WIDX[v]] == 1)
            sigs[(n0, n1)] += 1
            if (n0, n1) != (1, 2):
                ok_sig = False
    check("S10.2 SPREAD-TEST: JEDER Block jedes isotropen Spreads hat "
          "q*-Signatur genau (1 Punkt der 5bar, 2 Punkte der 10): %s"
          % dict(sigs), ok_sig, kill="K10")

    ok_all_lines = all(sum(1 for v in L if qstar[WIDX[v]] == 0) == 1
                       for L in lines if iso_line[L])
    check("S10.3 staerker (Ovoid-Eigenschaft): ALLE 15 isotropen "
          "Geraden treffen die 5bar in genau 1 Punkt", ok_all_lines)


# ======================================================================
# S11 -- the hypercharge table
# ======================================================================
X5 = (-2, -2, -2, 3, 3)


def xval(v):
    return sum(x * b for x, b in zip(X5, iota(v)))


def class_of(v):
    n_c = v[0] + v[1] + v[2]
    a = v[3]
    return {(0, 0): "nu_c", (0, 1): "e_c", (1, 0): "Q_up",
            (1, 1): "Q_dn", (2, 0): "u_c", (2, 1): "d_c",
            (3, 0): "nu_L", (3, 1): "e_L"}[(n_c, a)]


def s11_hypercharge():
    section("S11: die Hyperladungs-Tafel X = (-2,-2,-2,3,3), Y = X/6")
    g = 0
    for x in X5:
        g = gcd(g, abs(x))
    check("S11.1 X primitiv (gcd = %d) und spurfrei (Summe = %d)"
          % (g, sum(X5)), g == 1 and sum(X5) == 0, kill="K11")

    FROZEN = {"nu_c": 0, "e_c": 6, "Q_up": 1, "Q_dn": 1, "u_c": -4,
              "d_c": 2, "nu_L": -3, "e_L": -3}
    MULT = {"nu_c": 1, "e_c": 1, "Q_up": 3, "Q_dn": 3, "u_c": 3,
            "d_c": 3, "nu_L": 1, "e_L": 1}
    tab = Counter()
    ok_x = True
    for v in W16:
        cl = class_of(v)
        tab[cl] += 1
        if xval(v) != FROZEN[cl]:
            ok_x = False
    check("S11.2 EINGEFRORENE ZUORDNUNG exakt: 0->nu_c(0), A->e_c(6), "
          "F_i->Q_up(1), F_i+A->Q_dn(1), F_iF_j->u_c(-4), "
          "F_iF_jA->d_c(2), F_Sig->nu_L(-3), F_SigA->e_L(-3); "
          "Multiplizitaeten %s" % dict(tab),
          ok_x and dict(tab) == MULT, kill="K11")

    from v310_carrier_sm_anomaly import GEN   # read-only corpus import
    ours = Counter()
    for v in W16:
        ours[Fr(xval(v), 6)] += 1
    v310 = Counter()
    for _name, m, Y in GEN:
        v310[Fr(Y)] += m
    check("S11.3 Y = X/6 reproduziert das v310-Woerterbuch (Werte UND "
          "Multiplizitaeten): {1/6:6, -2/3:3, 1/3:3, -1/2:2, 1:1, 0:1}",
          ours == v310,
          "unsere %s" % dict(sorted(ours.items())), kill="K11")


# ======================================================================
# S12 -- the code polynomial and its moments
# ======================================================================
def s12_polynomial():
    section("S12: P_X(z) und die Euler-Momente (Master-Moment 120)")
    coef = Counter(xval(v) for v in W16)
    P_EXPECT = {0: 1, -4: 3, -3: 2, 1: 6, 2: 3, 6: 1}
    check("S12.1 P_X(z) = 1 + 3z^-4 + 2z^-3 + 6z + 3z^2 + z^6 "
          "(Koeffizienten-Zensus %s)" % dict(sorted(coef.items())),
          dict(coef) == P_EXPECT, kill="K12")
    m0 = sum(coef.values())
    m1 = sum(x * c for x, c in coef.items())
    m2 = sum(x * x * c for x, c in coef.items())
    m3 = sum(x ** 3 * c for x, c in coef.items())
    check("S12.2 MOMENTE: P(1) = %d == 16, DP(1) = %d == 0, D^2P(1) = "
          "%d == 120, D^3P(1) = %d == 0 (D = z d/dz)"
          % (m0, m1, m2, m3),
          (m0, m1, m2, m3) == (16, 0, 120, 0), kill="K12")

    from tfpt_constants import b1   # read-only corpus import
    chain = (m2 // 3 == 40 and m2 // 3 + 1 == 41
             and 2 * m2 == 240 and 2 * m2 + 8 == 248
             and int(10 * b1) == 41)
    check("S12.3 KETTE: 120/3 = 40, +1 = 41 = 10 b1 (tfpt_constants), "
          "2*120 = 240, +8 = 248; Master-Moment Tr_{S+} X^2 = 120 = 5! "
          "= |R+(E8)| == v2_carrier_pascal-Fakt", chain, kill="K12")


# ======================================================================
# S13 -- Pati--Salam split and B-L
# ======================================================================
def s13_pati_salam():
    section("S13: Pati--Salam 16 = (4,2,1) + (4bar,1,2), B-L, "
            "3+2-Slot-Split")
    left = [v for v in W16 if (v[0] + v[1] + v[2]) % 2 == 1]
    right = [v for v in W16 if (v[0] + v[1] + v[2]) % 2 == 0]
    ok_doublets = True
    for side, names in ((left, {"Q_up", "Q_dn", "nu_L", "e_L"}),
                        (right, {"nu_c", "e_c", "u_c", "d_c"})):
        for v in side:
            w = xor(v, A_BIT)
            if w not in side:
                ok_doublets = False
            if class_of(v) not in names:
                ok_doublets = False
    check("S13.1 p_F = f1+f2+f3 splittet 16 = 8 (links: Q, L) + 8 "
          "(rechts: nu_c, e_c, u_c, d_c); A-Bit = Isospin-Index "
          "(Dubletts (v, v+A) bleiben je Seite)",
          len(left) == 8 and len(right) == 8 and ok_doublets,
          kill="K13")

    BL = {"nu_c": Fr(1), "e_c": Fr(1), "Q_up": Fr(1, 3),
          "Q_dn": Fr(1, 3), "u_c": Fr(-1, 3), "d_c": Fr(-1, 3),
          "nu_L": Fr(-1), "e_L": Fr(-1)}
    ok_bl = all(Fr(1) - Fr(2 * (v[0] + v[1] + v[2]), 3)
                == BL[class_of(v)] for v in W16)
    check("S13.2 B-L = 1 - 2 n_c/3 exakt fuer alle 16 Worte "
          "(n_c = f1+f2+f3 als Zahl)", ok_bl, kill="K13")

    ok_slots = all(iota(sig_bits(v))
                   == tuple(iota(v)[k] for k in (2, 0, 1, 3, 4))
                   for v in W16)
    check("S13.3 SLOT-SPLIT: sigma wirkt auf den 5 Traeger-Slots von "
          "iota als 3-Zyklus auf {1,2,3} + Fixpunkte {4,5} -- der "
          "3+2-Split (A3^PS-Register), NICHT der Familienzyklus "
          "(A3^Fam-Register); Namensdisziplin, kein Physik-Claim",
          ok_slots, kill="K13")


# ======================================================================
# S14 -- NS/R crosslink
# ======================================================================
def s14_nsr():
    section("S14: chi_NSR(v) = hbar(v, F_Sigma) = a -- das vierte "
            "Informationsbit")
    ok_chi = all(hb(v, FSIG) == v[3] for v in W16)
    check("S14.1 chi_NSR = hbar(., F_Sigma) == Anker-Bit a auf allen 16 "
          "Worten (v752-Basis; Standardmodell-Kreuzcheck in S1.7)",
          ok_chi, kill="K14")
    PAIRS = [("nu_c", "e_c"), ("u_c", "d_c"), ("Q_up", "Q_dn"),
             ("nu_L", "e_L")]
    ok_pairs = True
    for v in W16:
        w = xor(v, A_BIT)
        cv, cw = class_of(v), class_of(w)
        if v[3] == 0:
            if (cv, cw) not in PAIRS:
                ok_pairs = False
            if not (hb(v, FSIG) == 0 and hb(w, FSIG) == 1):
                ok_pairs = False
    check("S14.2 die vier A-Paarungen nu_c<->e_c, u_c<->d_c, "
          "Q_up<->Q_dn, nu_L<->e_L: chi = (0, 1) auf jedem Paar",
          ok_pairs, kill="K14")


# ======================================================================
# C -- must-fail controls
# ======================================================================
def c_controls():
    section("C: Must-fail-Kontrollen")
    # C1: the non-alternating dot form admits NO refinement
    dot = [[sum(a * b for a, b in zip(v, w)) % 2 for w in W16]
           for v in W16]
    n_bad = 0
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for i in range(16):
            for j in range(16):
                if q[ADD[i][j]] ^ q[i] ^ q[j] != dot[i][j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            n_bad += 1
    check("C1 KONTROLLE FEUERT: die nicht-alternierende Punktform laesst"
          " GENAU 0 quadratische Verfeinerungen zu (Alternierung ist "
          "notwendig)", n_bad == 0, "gefunden: %d" % n_bad)

    Xbad = (-2, -2, -2, 3, 2)
    m2_bad = sum(sum(x * b for x, b in zip(Xbad, iota(v))) ** 2
                 for v in W16)
    check("C2 KONTROLLE FEUERT: X' = (-2,-2,-2,3,2) ist nicht spurfrei "
          "(Summe %d != 0) und bricht das Master-Moment (D^2P = %d != "
          "120)" % (sum(Xbad), m2_bad),
          sum(Xbad) != 0 and m2_bad != 120)


# ======================================================================
def main():
    print("=" * 78)
    print("ARF.SPINORCOMPILER.01 -- Priority 1: der Arf/Spinor-Compiler "
          "auf V = L/(1+i)L")
    print("=" * 78, flush=True)
    s1_lattice()
    refs = s2_refinements()
    ctx3 = s3_arf_sp(refs)
    qstar = s4_selector(refs, ctx3)
    s5_parity_lift()
    s6_weight_form(refs, qstar)
    ctx7 = s7_decomposition(refs, qstar, ctx3)
    duad = s8_duads(qstar, ctx3, ctx7)
    s9_incidence(qstar, ctx3, duad)
    s10_spreads(qstar)
    s11_hypercharge()
    s12_polynomial()
    s13_pati_salam()
    s14_nsr()
    c_controls()

    section("ZUSAMMENFASSUNG / VERDIKT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    print("%d/%d Checks bestanden" % (n_pass, n_all))
    if KILLS:
        verdict = "ARF-SPINOR-KILLED"
        print("VERDIKT: ARF-SPINOR-KILLED -- Kills gefeuert: %s"
              % sorted(set(KILLS)))
    elif not controls_ok:
        verdict = "TEST-VOID"
        print("VERDIKT: TEST-VOID -- eine Must-fail-Kontrolle feuert "
              "nicht; der Test misst nichts.")
    elif n_pass == n_all:
        verdict = "ARF-SPINOR-EXACT"
        print("VERDIKT: ARF-SPINOR-EXACT -- q* kanonisch (Selektor "
              "eindeutig), Paritaets-Lift = q*, 16 = 1 + 5bar + 10 als "
              "Arf-Geometrie, B = I + A_KG(6,2), Ovoid-Eigenvektoren "
              "spannen den (-2)-Raum, Hyperladungs-Tafel + Momente "
              "(16, 0, 120, 0) exakt, Pati--Salam-Split + B-L exakt, "
              "chi_NSR = das vierte Informationsbit.")
    else:
        verdict = "ARF-SPINOR-KILLED"
        print("VERDIKT: ARF-SPINOR-KILLED -- Nicht-Kill-Check "
              "gescheitert; siehe FAIL-Zeilen.")
    print("Verdikt-Enum: %s" % verdict)
    print("Laufzeit: %.1f s" % (time.time() - T0))
    print("ALLE CHECKS BESTANDEN" if n_pass == n_all
          else "CHECKS FEHLGESCHLAGEN")
    return 0 if n_pass == n_all else 1


_run_probe = main


def run():
    """run_all entry point (v757 precedent): the preregistered pattern is
    ALL-PASS -- 46/46 checks, zero kills, both must-fail controls fire,
    verdict ARF-SPINOR-EXACT."""
    rc = _run_probe()
    fails = [n for (n, ok) in CHECKS if not ok]
    ok = (rc == 0 and len(CHECKS) == 46 and not fails and not KILLS)
    print("\n[%s] PATTERN GATE: expected ARF-SPINOR-EXACT (46/46, zero "
          "kills, controls fire) -- failing checks: %s, kills: %s"
          % ("PASS" if ok else "FAIL", fails or "none",
             sorted(set(KILLS)) or "none"))
    print("\nADJUDICATION: %s -- ARF-SPINOR-EXACT: the sigma-selected Arf "
          "refinement q* is canonical (selector census 4 -> 2 -> 1), the "
          "parity lift iota: V ~ C_even(5) carries beta = hbar exactly, "
          "16 = 1 + 5bar + 10 is the Arf geometry (Stab(q*) ~ S5), "
          "B = I + A_KG(6,2) with exact ovoid eigenvectors, hypercharge "
          "table + moments (16, 0, 120, 0) + Pati--Salam + chi_NSR = anchor "
          "bit all exact.  The code->matter reading stays FENCED (killed at "
          "root level by v775).  NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
