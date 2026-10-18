"""v853 TFPT scope: exact Arf bent/CSS code identities.

Scope extraction from original module at ba2f0fc; original ID and
mathematical statements preserved. Original full source is retained
in the extraction provenance; no proof/status promotion.
"""
import contextlib

import io

import os

import re

import sys

import types

_HERE = os.path.dirname(os.path.abspath(__file__))

_SRC_BENT = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""arf_bent_css_probe -- ARF.BENT.CSS.01: the bent phase code and the
two CSS codes.  The phase vector s_q = (-1)^{q*} is a bent function
with Walsh identity s_q-hat = -4 s_q (the Gauss sum -2^{4/2} = -4 as
an eigenvalue equation), its zero set is a (16,6,2) Hadamard
difference set {0} u ovoid, the linear span A_q = <V*, q*> = [15,5,6]
is self-orthogonal inside C_iso and yields the CSS code [[15,5,3]],
the 16-slot extension A_16 = RM(1,4) + <q*> = [16,6,6] yields
[[16,4,4]] whose dual's 60 minimal words are EXACTLY the 60 isotropic
affine planes, and the Hecke difference a_3 = -4, the Gauss sum and
the Walsh eigenvalue are ONE machine-checked integer (finite-geometry
module 3 of the 2026-08-07 evening code-complex round).

FROZEN CLAIMS (2026-08-07, frozen + SHA-hashed before first run; all
statements verified over ALL objects, never samples; exact integer/F2
arithmetic; no floats, no RNG, no fits):

 S1  CARRIER: corpus form hb (J - I Gram), 16 refinements (2^16
     census), Arf 6 + 10, selector-unique q* (Arf 1); five = {q*=0}
     \{0} (the ovoid), ten = {q*=1}; s_q(x) = (-1)^{q*(x)}.

 S2  (a) THE GAUSS-SUM / WALSH IDENTITY:
     (i)  the one-line identity q*(x) + hb(a,x) = q*(x+a) + q*(a)
          holds on ALL 256 pairs (the derivation identity re-read);
     (ii) the exact integer Walsh transform obeys s_q-hat(a) =
          sum_x s_q(x) (-1)^{hb(a,x)} = -4 * s_q(a) for ALL 16 a --
          s_q is a Walsh EIGENVECTOR with eigenvalue -4 (bent,
          extremal); W^2 = 16 I for the character matrix W;
     (iii) perfect autocorrelation sum_x s_q(x+a) s_q(x+b) =
          16 delta_{a,b} on ALL 256 pairs.

 S3  (b) THE DIFFERENCE SET: D_q = {q* = 0} has 6 elements = {0} u
     the five carrier points (each of iota-weight 4 -- identified
     against the five-slot structure; the 5bar meets every doily
     line exactly once); |D_q n (D_q + a)| = 2 for ALL 15 a != 0 --
     the (16,6,2) Hadamard difference set.

 S4  (c) THE PHASE CODE A_q = C_iso^perp = <V*, q*> = [15,5,6]:
     A_q = span{hb(v,.)|_NZ} + <q*|_NZ> has dim 5, weight enumerator
     1 + 10z^6 + 15z^8 + 6z^10, min distance 6; A_q == C_iso^perp
     (set equality, C_iso = the Arf-kernel [15,10,3] of the Hamming
     code, probe-1 pencil); THE 31-WORD SEMANTIC CENSUS, each class
     identified STRUCTURALLY (set equalities, not counts): the 15
     weight-8 words ARE the linear characters hb(v,.), the 10
     weight-6 words ARE the Arf-0 (even) refinement indicators, the
     6 weight-10 words ARE the Arf-1 (odd/ovoid) refinement
     indicators.

 S5  (d1) CSS CODE ONE: A_q c A_q^perp = C_iso (self-orthogonality,
     all 32 x 32 pairs even) => [[15, 5, 3]] with k = 15 - 2*5 =
     dim C_iso - dim A_q = 5 and d = 3: the coset minimum is
     realized by the 15 explicit weight-3 isotropic-line words of
     C_iso (set equality), none of which lies in A_q (min weight 6),
     and C_iso has NO weight-1 or weight-2 word.

 S6  (d2) CSS CODE TWO: A_16 = RM(1,4) + <q*> = [16,6,6] with weight
     enumerator 1 + 16z^6 + 30z^8 + 16z^10 + z^16, SELF-ORTHOGONAL;
     dual C_16 = A_16^perp = [16,10,4] = {c in RM(2,4) : c.q* = 0}
     (set equality); the 60 minimal (weight-4) words of C_16 are
     EXACTLY the 60 isotropic affine planes = 15 through the origin
     + 45 off (SET EQUALITY -- the syndrome-table cross-link: these
     are precisely the s_Arf = 0 rows of probe 1) => [[16, 4, 4]]
     with k = 16 - 2*6 = 4 and d = 4 (weight-4 words exist in C_16
     and none lies in A_16).

 S7  (d3) THE VACUUM TRANSFORMATION [[15,5,3]] -> [[16,4,4]] typed:
     shortening A_16 at the vacuum coordinate == A_q and puncturing
     C_16 == C_iso (set equalities); one physical slot added
     (n 15 -> 16), one logical qubit paid (k 5 -> 4), distance
     bought (d 3 -> 4).

 S8  (e) THE -4 TRIPLE POINT, one machine-checked statement:
     (i)   Hecke: the per-point plane census (12 isotropic - 16
           non-isotropic off-origin planes through x, re-counted at
           ALL 15 points) gives A_3 - B_3 = -4 = a_3 (eta product
           rebuilt inline; v820 S4.2 (G3) / v535 corpus anchors);
     (ii)  Gauss: sum_x s_q(x) = 6 - 10 = -4 = -2^{4/2};
     (iii) Walsh: the eigenvalue of s_q under W is -4 (S2);
     all three integers computed independently and asserted EQUAL.
     THE 16-TRANSLATE HADAMARD BASIS vs the corpus torsor Fourier
     basis (v800, integer Gram 16 I, mutually-unbiased honest cap):
     the translates T_t = s_q(. + t) have Gram EXACTLY 16 I (an
     orthogonal Hadamard basis, same normalization as v800's rays),
     and are MUTUALLY UNBIASED against the 16 characters
     (-1)^{hb(u,.)}: ALL 256 cross inner products = +-4 = sqrt(16)
     -- the translate basis does NOT reproduce the character rays,
     it is their unbiased complement (typed REPORT, v800 cited).

 C   CONTROLS (must fire; frozen fire rules):
     C1 ARF-0 REFINEMENT q0: the Walsh identity flips sign,
        s_q0-hat = +4 s_q0 on ALL 16 (eigenvalue +4), and the zero
        set is NOT a (16,6,2) set: |{q0=0}| = 10 with all 15
        intersection sizes = 6 (the complementary (16,10,6) set --
        census printed).
     C2 DOT FORM: zero quadratic refinements (2^16 census) -- no
        bent seed exists; the direction bit is ill-defined (witness
        U = <e1,e2>); and the dot-side parity surrogate collapses:
        wt(x) mod 2 IS the linear character x1+x2+x3+x4 in RM(1,4),
        so span(RM(1,4) + <parity>) has dim 5 != 6 -- NO sixth
        generator, no [16,6,6], the self-orthogonal extension dies.

KILLS (any one fires => typed failure):
  K1 Walsh / Gauss / autocorrelation identity breaks -> WALSH-BROKEN
  K2 the (16,6,2) difference set breaks              -> DIFFSET-BROKEN
  K3 A_q census / dual / semantic identification     -> CODE-CENSUS-BROKEN
  K4 a CSS ingredient ([[15,5,3]] / [[16,4,4]])      -> CSS-BROKEN
  K5 the vacuum shorten/puncture map breaks          -> VACUUM-MAP-BROKEN
  K6 the -4 triple point / 16I / MUB check breaks    -> TRIPLE-POINT-BROKEN
  K7 a control does not fire                         -> CONTROL-DEAD

VERDICT (frozen enum): ARF-BENT-CSS-EXACT / WALSH-BROKEN /
DIFFSET-BROKEN / CODE-CENSUS-BROKEN / CSS-BROKEN / VACUUM-MAP-BROKEN /
TRIPLE-POINT-BROKEN / CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface;
no .md, no commits.  Exact integer/F2 arithmetic; no floats, no RNG,
no fits.  NO physics claim.

Sources (read-only, machinery rebuilt inline):
affine_arf_vacuum_probe.py (H / C_iso pencil, syndrome table, local
Hecke counts), finite_compiler_normal_form_probe.py +
cfin_uniqueness_probe.py (q*, selector, iota), v819 (RM landscape),
v820 S4.2 (G3) + v535 + v785 (a_3 = -4 anchors), v800 (torsor Fourier
rays, 16 I Gram, mutually-unbiased cap), v774/v752 (form +
refinements), tfpt_constants (g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/arf_bent_css_probe.py
"""
import hashlib
import itertools
import os
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "verification"))
from tfpt_constants import g_car  # noqa: E402  (read-only import)

T0 = time.time()
CHECKS = []
KILLS = []


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0), flush=True)


print("ARF.BENT.CSS.01 -- bent phase code + the two CSS codes")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

# ------------------------------------------------------- bit machinery
PTS = list(range(16))
NZ = list(range(1, 16))


def pc(v):
    return bin(v).count("1")


def hb(v, w):
    return ((pc(v) & 1) & (pc(w) & 1)) ^ (pc(v & w) & 1)


HBT = [[hb(v, w) for w in PTS] for v in PTS]
DOT = [[pc(v & w) & 1 for w in PTS] for v in PTS]


def refinements_of(tab):
    out = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for i in range(16):
            qi = q[i]
            row = tab[i]
            for j in range(16):
                if q[i ^ j] ^ qi ^ q[j] != row[j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(q))
    return out


def sig_int(v):
    b = [(v >> k) & 1 for k in range(4)]
    w = (b[2], b[0], b[1], b[3])
    return sum(w[k] << k for k in range(4))


def span_bits(gens):
    S_ = {0}
    for g in gens:
        S_ |= {s ^ g for s in S_}
    return S_


# ======================================================================
section("S1: carrier -- q*, five/ten, the phase vector s_q")
# ======================================================================
REFS = refinements_of(HBT)
ARF1 = sorted(q for q in REFS if sum(1 for i in PTS if q[i] == 0) == 6)
ARF0 = sorted(q for q in REFS if sum(1 for i in PTS if q[i] == 0) == 10)
siginv = [q for q in REFS if all(q[sig_int(v)] == q[v] for v in PTS)]
cand = [q for q in siginv if q[8] == 1 and q[7] == 0]
check("S1.1 16 refinements, Arf 6 + 10, selector-unique q* (Arf 1)",
      len(REFS) == 16 and len(ARF1) == 6 and len(ARF0) == 10
      and len(cand) == 1 and cand[0] in ARF1, kill="K1")
QS = cand[0]
FIVE = [v for v in NZ if QS[v] == 0]
TEN = [v for v in NZ if QS[v] == 1]
S = [1 - 2 * QS[x] for x in PTS]        # s_q = (-1)^{q*}
check("S1.2 five = %d = g_car carrier points, ten = %d; s_q takes "
      "value +1 on 6 and -1 on 10 slots" % (len(FIVE), len(TEN)),
      len(FIVE) == 5 == g_car and len(TEN) == 10
      and S.count(1) == 6 and S.count(-1) == 10, kill="K1")

# ======================================================================
section("S2: (a) the Gauss-sum / Walsh identity s_q-hat = -4 s_q")
# ======================================================================
check("S2.1 one-line identity q*(x) + hb(a,x) == q*(x+a) + q*(a) on "
      "ALL 256 pairs",
      all((QS[x] + HBT[a][x]) % 2 == (QS[x ^ a] + QS[a]) % 2
          for a in PTS for x in PTS), kill="K1")
WHAT = [sum(S[x] * (1 - 2 * HBT[a][x]) for x in PTS) for a in PTS]
W2 = [[sum((1 - 2 * HBT[a][x]) * (1 - 2 * HBT[x][b]) for x in PTS)
       for b in PTS] for a in PTS]
check("S2.2 WALSH EIGENVECTOR: s_q-hat(a) == -4 * s_q(a) for ALL 16 "
      "a (values %s); W^2 == 16 I (256 cells)"
      % sorted(set(WHAT)),
      all(WHAT[a] == -4 * S[a] for a in PTS)
      and all(W2[a][b] == (16 if a == b else 0)
              for a in PTS for b in PTS), kill="K1")
check("S2.3 PERFECT AUTOCORRELATION: sum_x s_q(x+a) s_q(x+b) == "
      "16 delta_{a,b} on ALL 256 pairs",
      all(sum(S[x ^ a] * S[x ^ b] for x in PTS)
          == (16 if a == b else 0) for a in PTS for b in PTS),
      kill="K1")

# ======================================================================
section("S3: (b) the (16,6,2) Hadamard difference set D_q = {q*=0}")
# ======================================================================
DQ = {v for v in PTS if QS[v] == 0}
SUBS = sorted({frozenset({0, u, v, u ^ v})
               for u, v in itertools.combinations(NZ, 2)}, key=sorted)
UBIT = {U: min(HBT[a][b] for a, b in
               itertools.combinations(sorted(U - {0}), 2))
        for U in SUBS}
ISO = [U for U in SUBS if UBIT[U] == 0]
check("S3.1 D_q = {0} u five (|D_q| = %d == 6 = g_car + 1); each of "
      "the five has iota-weight 4 (the 5bar slot structure); the "
      "5bar meets every doily line exactly once (ovoid)" % len(DQ),
      DQ == {0} | set(FIVE)
      and all(pc(v) + (pc(v) & 1) == 4 for v in FIVE)
      and all(sum(1 for x in U - {0} if x in FIVE) == 1 for U in ISO),
      kill="K2")
inter = sorted(len(DQ & {d ^ a for d in DQ}) for a in NZ)
check("S3.2 |D_q n (D_q + a)| == 2 for ALL 15 a != 0 (census %s) -- "
      "the (16,6,2) Hadamard difference set"
      % sorted(set(inter)), inter == [2] * 15, kill="K2")

# ======================================================================
section("S4: (c) A_q = C_iso^perp = <V*, q*> = [15,5,6] + census")
# ======================================================================


def xor_pts(m):
    s = 0
    while m:
        b = m & -m
        s ^= b.bit_length()
        m ^= b
    return s


def wmask(pts_set):
    return sum(1 << (x - 1) for x in pts_set)


H = [m for m in range(1 << 15) if xor_pts(m) == 0]
TENM = wmask(TEN)
CISO = [m for m in H if pc(m & TENM) % 2 == 0]
SIMP15 = {wmask({x for x in NZ if HBT[v][x] == 1}) for v in NZ}
AQ = span_bits([wmask({x for x in NZ if HBT[v][x] == 1})
                for v in (1, 2, 4, 8)] + [TENM])
weA = Counter(pc(m) for m in AQ)
check("S4.1 A_q = span{hb(v,.)} + <q*>: dim 5 (|A_q| = %d == 32), "
      "weight enumerator %s == 1 + 10z^6 + 15z^8 + 6z^10, min "
      "distance 6 -> [15,5,6]"
      % (len(AQ), dict(sorted(weA.items()))),
      len(AQ) == 32 and dict(weA) == {0: 1, 6: 10, 8: 15, 10: 6},
      kill="K3")


def bit_basis(vs):
    basis = []
    for v in vs:
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v)
            basis.sort(reverse=True)
    return basis


CB = bit_basis(CISO)
DUAL_CISO = {w for w in range(1 << 15)
             if all(pc(w & b) % 2 == 0 for b in CB)}
check("S4.2 A_q == C_iso^perp (set equality; dim 10 + dim 5 = 15)",
      DUAL_CISO == AQ and len(CB) == 10, kill="K3")

refvec = {q: wmask({x for x in NZ if q[x] == 1}) for q in REFS}
w8 = {m for m in AQ if pc(m) == 8}
w6 = {m for m in AQ if pc(m) == 6}
w10 = {m for m in AQ if pc(m) == 10}
check("S4.3 THE 31-WORD SEMANTIC CENSUS (structural set equalities): "
      "15 weight-8 words == the linear characters hb(v,.); 10 "
      "weight-6 == the Arf-0 (even) refinements; 6 weight-10 == the "
      "Arf-1 (odd/ovoid) refinements",
      w8 == SIMP15 and w6 == {refvec[q] for q in ARF0}
      and w10 == {refvec[q] for q in ARF1}, kill="K3")

# ======================================================================
section("S5: (d1) CSS one: A_q c C_iso => [[15,5,3]]")
# ======================================================================
sC = set(CISO)
ISO3 = {wmask(U - {0}) for U in ISO}
check("S5.1 SELF-ORTHOGONALITY: A_q c A_q^perp = C_iso (all 32 words "
      "in C_iso; all 32 x 32 pairs have even overlap)",
      AQ <= sC and all(pc(a & b) % 2 == 0 for a in AQ for b in AQ),
      kill="K4")
check("S5.2 [[15,5,3]]: k = 15 - 2*5 = %d == dim C_iso - dim A_q; "
      "d = 3: weight-3 words of C_iso == the 15 doily lines (set "
      "equality), NONE in A_q (min wt 6), and C_iso has NO weight-1/2 "
      "word" % (15 - 2 * 5),
      15 - 2 * 5 == 5 == 10 - 5
      and {m for m in CISO if pc(m) == 3} == ISO3
      and not (ISO3 & AQ)
      and not any(pc(m) in (1, 2) for m in CISO if m), kill="K4")

# ======================================================================
section("S6: (d2) CSS two: A_16 = RM(1,4) + <q*> => [[16,4,4]]")
# ======================================================================


def m16(pts_set):
    return sum(1 << v for v in pts_set)


QM16 = m16(set(TEN))
rm1_gens = [0xFFFF] + [m16({v for v in PTS if (v >> k) & 1})
                       for k in range(4)]
A16 = span_bits(rm1_gens + [QM16])
weA16 = Counter(pc(w) for w in A16)
gens6 = rm1_gens + [QM16]
check("S6.1 A_16 = RM(1,4) + <q*> = [16,6,6]: |A_16| = %d == 64, "
      "enumerator %s == 1 + 16z^6 + 30z^8 + 16z^10 + z^16; "
      "SELF-ORTHOGONAL (all 64 x 64 pairs even)"
      % (len(A16), dict(sorted(weA16.items()))),
      len(A16) == 64
      and dict(weA16) == {0: 1, 6: 16, 8: 30, 10: 16, 16: 1}
      and all(pc(a & b) % 2 == 0 for a in A16 for b in A16),
      kill="K4")

C16 = [w for w in range(1 << 16)
       if all(pc(w & g) % 2 == 0 for g in gens6)]
rm2_gens = rm1_gens + [m16({v for v in PTS
                            if ((v >> k) & 1) and ((v >> l) & 1)})
                       for k, l in itertools.combinations(range(4), 2)]
RM2 = span_bits(rm2_gens)
check("S6.2 C_16 = A_16^perp = [16,10,4]: |C_16| = %d == 1024, min "
      "wt %d == 4; C_16 == {c in RM(2,4) : c.q* = 0} (set equality); "
      "A_16 c C_16"
      % (len(C16), min(pc(w) for w in C16 if w)),
      len(C16) == 1024 and min(pc(w) for w in C16 if w) == 4
      and set(C16) == {c for c in RM2 if pc(c & QM16) % 2 == 0}
      and A16 <= set(C16), kill="K4")

FLAT16_ISO = set()
for U in SUBS:
    if UBIT[U] != 0:
        continue
    for cs in {frozenset(t ^ u for u in U) for t in PTS}:
        FLAT16_ISO.add(m16(cs))
w4C = {w for w in C16 if pc(w) == 4}
n_orig = sum(1 for w in FLAT16_ISO if w & 1)
check("S6.3 THE 60 MINIMAL WORDS: weight-4 words of C_16 == the 60 "
      "isotropic affine planes (SET EQUALITY; %d through origin + %d "
      "off = the s_Arf = 0 rows of the probe-1 syndrome table)"
      % (n_orig, len(FLAT16_ISO) - n_orig),
      w4C == FLAT16_ISO and len(FLAT16_ISO) == 60
      and n_orig == 15 and len(FLAT16_ISO) - n_orig == 45,
      kill="K4")
check("S6.4 [[16,4,4]]: k = 16 - 2*6 = %d; d = 4 (weight-4 words in "
      "C_16 \\ A_16: %d of them, A_16 min weight 6)"
      % (16 - 2 * 6, len(w4C - A16)),
      16 - 2 * 6 == 4 and len(w4C - A16) == 60
      and min(pc(w) for w in A16 if w) == 6, kill="K4")

# ======================================================================
section("S7: (d3) the vacuum transformation [[15,5,3]] -> [[16,4,4]]")
# ======================================================================
SHORT_A16 = {w >> 1 for w in A16 if not (w & 1)}
PUNC_C16 = {w >> 1 for w in C16}
check("S7.1 shorten(A_16) at the vacuum slot == A_q (set equality, "
      "%d words); puncture(C_16) == C_iso (set equality, %d words)"
      % (len(SHORT_A16), len(PUNC_C16)),
      SHORT_A16 == AQ and PUNC_C16 == sC and len(PUNC_C16) == 1024,
      kill="K5")
check("S7.2 typed parameters: one physical slot added (15 -> 16), "
      "one logical qubit paid (5 -> 4), distance bought (3 -> 4)",
      16 - 15 == 1 and 5 - 4 == 1 and 4 - 3 == 1
      and (15, 5, 3)[1] - 1 == (16, 4, 4)[1]
      and (15, 5, 3)[2] + 1 == (16, 4, 4)[2], kill="K5")

# ======================================================================
section("S8: (e) the -4 triple point + the 16-translate basis")
# ======================================================================
FLATS = []
for U in SUBS:
    for cs in {frozenset(t ^ u for u in U) for t in PTS}:
        FLATS.append((U, cs))
ok_pp = True
for x in NZ:
    off = [(U, cs) for U, cs in FLATS if x in cs and 0 not in cs]
    n_iso = sum(1 for U, cs in off if UBIT[U] == 0)
    if not (n_iso == 12 and len(off) - n_iso == 16):
        ok_pp = False


def eta_f8_a(n_max):
    c = [0] * (n_max + 1)
    c[0] = 1
    for step in (2, 4):
        for m in range(step, n_max + 1, step):
            for _ in range(4):
                for j in range(n_max, m - 1, -1):
                    c[j] -= c[j - m]
    a = [0] * (n_max + 2)
    for n in range(1, n_max + 2):
        if n - 1 <= n_max:
            a[n] = c[n - 1]
    return a


A3ETA = eta_f8_a(10)[3]
gauss = sum(S)
eigen = set(WHAT[a] * S[a] for a in PTS)  # {-4 * s^2} = {-4}
check("S8.1 THE -4 TRIPLE POINT (one statement, three independent "
      "computations): Hecke 12 - 16 = %d (all 15 points re-counted) "
      "== Gauss sum %d = -2^{4/2} == Walsh eigenvalue %s == a_3 = %d "
      "(eta; v820 S4.2 (G3), v535, v785 anchors)"
      % (12 - 16, gauss, sorted(eigen), A3ETA),
      ok_pp and 12 - 16 == -4 and gauss == -4
      and eigen == {-4} and A3ETA == -4 and -(2 ** 2) == -4,
      kill="K6")

T = [[S[x ^ t] for x in PTS] for t in PTS]
gramT = [[sum(T[t][x] * T[u][x] for x in PTS) for u in PTS]
         for t in PTS]
CHAR = [[1 - 2 * HBT[u][x] for x in PTS] for u in PTS]
cross = [[sum(T[t][x] * CHAR[u][x] for x in PTS) for u in PTS]
         for t in PTS]
check("S8.2 16-TRANSLATE HADAMARD BASIS: Gram(T) == 16 I EXACTLY "
      "(256 cells; v800's ray normalization reproduced); MUTUALLY "
      "UNBIASED against the 16 characters: ALL 256 cross products "
      "= +-4 = sqrt(16) (values %s) -- the translate basis "
      "complements, does NOT reproduce, the corpus character rays "
      "(v800 cited: torsor Fourier Gram 16 I, weight/character "
      "mutually unbiased)"
      % sorted({abs(cross[t][u]) for t in PTS for u in PTS}),
      all(gramT[t][u] == (16 if t == u else 0)
          for t in PTS for u in PTS)
      and all(abs(cross[t][u]) == 4 for t in PTS for u in PTS),
      kill="K6")

# ======================================================================
section("C: controls (must fire)")
# ======================================================================
Q0 = ARF0[0]
S0 = [1 - 2 * Q0[x] for x in PTS]
WH0 = [sum(S0[x] * (1 - 2 * HBT[a][x]) for x in PTS) for a in PTS]
D0 = {v for v in PTS if Q0[v] == 0}
inter0 = sorted(len(D0 & {d ^ a for d in D0}) for a in NZ)
check("C1 FIRES: Arf-0 refinement: Walsh SIGN FLIPS, s_q0-hat == "
      "+4 s_q0 on ALL 16 (eigenvalue +4 != -4); zero set |D0| = %d "
      "!= 6 with intersections %s == all-6 (the complementary "
      "(16,10,6) set) -- NO (16,6,2) set"
      % (len(D0), sorted(set(inter0))),
      all(WH0[a] == 4 * S0[a] for a in PTS) and len(D0) == 10
      and inter0 == [6] * 15, kill="K7")

refs_dot = refinements_of(DOT)
PARM = m16({v for v in PTS if pc(v) & 1})
RM1 = span_bits(rm1_gens)
check("C2 FIRES: dot form: %d == 0 refinements (no bent seed); "
      "direction bit ill-defined on U = <e1,e2> (dot pair values "
      "(%d,%d) differ); parity surrogate wt mod 2 == the character "
      "x1+x2+x3+x4 IN RM(1,4) (%s), so span(RM(1,4)+<parity>) has "
      "dim %d != 6 -- no sixth generator, the self-orthogonal "
      "[16,6,6] extension dies on the dot side"
      % (len(refs_dot), DOT[1][2], DOT[1][3],
         PARM in RM1,
         len(bit_basis(sorted(RM1 | {PARM})))),
      len(refs_dot) == 0 and (DOT[1][2], DOT[1][3]) == (0, 1)
      and PARM in RM1
      and len(bit_basis(sorted(RM1 | {PARM}))) == 5, kill="K7")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
if not controls_ok:
    VERDICT = "CONTROL-DEAD"
elif KILLS:
    VERDICT = {"K1": "WALSH-BROKEN", "K2": "DIFFSET-BROKEN",
               "K3": "CODE-CENSUS-BROKEN", "K4": "CSS-BROKEN",
               "K5": "VACUUM-MAP-BROKEN",
               "K6": "TRIPLE-POINT-BROKEN"}.get(KILLS[0],
                                                "CONTROL-DEAD")
else:
    VERDICT = "ARF-BENT-CSS-EXACT"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nCORPUS COMPRESSION REPORT (report only -- promotion separate):")
print("  * THE -4 IS ONE NUMBER: v820/v535's Hecke a_3 = -4, the "
      "bent Gauss sum")
print("    -2^{4/2} and the Walsh eigenvalue of the q* phase vector "
      "are the SAME")
print("    machine-checked integer; v785's 32 = 28 - (-4) is the "
      "gap between the")
print("    two Walsh eigenvalue lines +-4 scaled by the 16-slot "
      "register -- the")
print("    cusp projector denominator is the bent spectral gap.")
print("  * v819's RM landscape gains the PHASE layer: A_q = "
      "C_iso^perp = [15,5,6]")
print("    (simplex + q*), self-orthogonal => [[15,5,3]]; the "
      "vacuum slot upgrade")
print("    A_16 = RM(1,4)+<q*> = [16,6,6] => [[16,4,4]] whose dual "
      "minimal words")
print("    are EXACTLY the 60 isotropic planes -- the s_Arf = 0 "
      "rows of the")
print("    probe-1 syndrome table (v821/v834's 45 + the 15 doily "
      "lines).")
print("  * v800's torsor Fourier rays (Gram 16 I) get their "
      "unbiased partner: the")
print("    16 bent translates form a second 16 I frame, all cross "
      "products +-4 --")
print("    a character/bent MUB pair on the 16-slot register "
      "(reported, no upgrade).")
print("  * the (16,6,2) Hadamard difference set {0} u 5bar is the "
      "arithmetic face")
print("    of the ovoid: vacuum + five carrier slots, pairwise "
      "translate overlap 2.")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot
                       and VERDICT == "ARF-BENT-CSS-EXACT") else 1)
'''

_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)

_VD_RE = re.compile(r"VERDICT[:\]]")

def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None

def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict

def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered in sys.modules under the probe's
    canonical import name (cross-probe READ-ONLY imports resolve to
    the embedded copies); capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same

def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok

_PLAN = (("arf_bent_css_probe", _SRC_BENT, 22, (), "ARF-BENT-CSS-EXACT", 0),)

def run():
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails, exp_verdict, exp_code, gates)
    print("v853 scoped pattern gates: %d/%d passed" % (sum(gates), len(gates)))
    return 0 if all(gates) else 1

if __name__ == "__main__":
    raise SystemExit(run())
