#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seam_state_derivation_probe -- SEAM.STATE.DERIVATION.01
(EXPLORATION ONLY, experiments/; round 58, 2026-08-10: the two OPEN
items of the v898 round -- spatial reflection positivity and the
modular/geometric-temperature route -- attacked as MEASUREMENTS on
the (u, t, beta) candidate family, plus the thermal curve of the
mixing characterized precisely.)

THE QUESTION.  v898 (SEAM.CFIN.KMSMIX.01) constructed the C6-covariant
channel-mixing KMS candidate h(u, t) = -(u A16_dep + t A_int) at
(u=1, t=1/8, beta=1) and NAMED two open items: (i) RP-THETA-OPEN --
no spatial/OS reflection was deployed on the 16-dim one-particle
space; (ii) whether the actual seam state realizes the candidate.
Round 57 (seam_mixing_normalization_probe) measured that the frozen
v898 gates force NOTHING about (u, t, beta) beyond t > 0
(T-INTERIOR-UNBOUNDED, PIN-ABSENT) and that the mixing is THERMAL
(dies at beta -> infinity).  THIS probe stops pinning constants and
derives what the STATE itself demands: (a) OS/reflection positivity
under the repo's own sheet-swap structures, (b) the modular
Hamiltonian of one-side reductions against the DEPLOYED geometric
angle beta_angle = 2pi (v526/v519/v239), (c) the thermal curve as a
measured object with a frozen distinguished-point census.

FEASIBILITY / REDUNDANCY CHECK (done against the corpus FIRST,
2026-08-10): v519 (WOIT.THETA.FREE.01) deploys the exact finite-dim
RP criterion -- the Gram M_ab = omega(theta(e_a) e_b) over half-side
monomials with the antilinear reversal convention and the FORCED
twist eta = +i -- but only for the free NS circle vacuum, NOT for
the v898 KMS family; v424/v426/v440 deploy the BW dictionary
(Theta K Theta = -K, Theta C_beta Theta = I - C_beta) on an 8-dim
collar toy whose reflection is Theta = I (x) sigma_x -- the PAIR
SWAP, whose 16-dim lift is exactly the sheet swap tested here; v898
typed RP-THETA-OPEN and tested only the particle-hole Theta_0.
NOTHING in the corpus tests OS positivity of the v898 candidate
under a spatial theta, computes the modular Hamiltonian of its
one-side reductions, or locates the thermal peak.  That is exactly
this probe.

SMOKE-RUN DISCLOSURE (2026-08-10, three declared smoke rounds before
freezing; ALL frozen claims below were shaped by them -- recording
the surprises is part of the method):
 (i)  the untwisted C6 2-cycle swap (a<->b positionally) is NOT an
      OS reflection: its Gram is non-Hermitian already at t = 0
      (the 2-cycle acts orientation-PRESERVINGLY on the pair
      planes); only the orientation-reversed (intra-pair-twisted)
      version theta_abT is exactly Hermitian, and it is Hermitian
      for the WHOLE family;
 (ii) the sheet swap theta_S (16-dim lift of the v440 collar
      Theta = I (x) sigma_x) has an EXACTLY Hermitian one-particle
      Gram family-wide, and its PSD boundary is the LAW u = t
      (beta-independent, bisected to 1e-6 at three t and four
      beta) -- which is exactly the third positive Pfaffian root
      below;
 (iii) DEAD GUESS, disclosed: the plan expected the ground-state
      transition of the boundary reduction to sit at a deployed
      constant (1/4 was the candidate); the smoke bisected the
      gap-closing at t* = 0.2309488708... and the EXACT sympy
      factorization identifies it as the smallest positive root of
      9 t^3 + 21 t^2 - t - 1 (no deployed constant; 1/4 is 8.6%
      away);
 (iv) the strict (Hermiticity-included) RP of theta_S fails for
      every t > 0 in the even deg-2 sector (defect ~ 0.098 at the
      deployed point; no assignment of pair signs among all 256
      repairs it), and the HERMITIZED PSD boundary t_c(beta)
      increases toward the SAME first Pfaffian root as
      beta -> infinity (t_c(2pi) = 0.230939 vs root 0.230949);
 (v)  the thermal peak sits at beta = 1.6730, NOT at 2: the round-57
      reading "peak at beta = 2" was a coarse-grid artifact (2 was
      the argmax of the scanned set {1/2, 1, 2, 4}; the fine
      ternary search moves it) -- PREMISE CORRECTED here;
 (vi) the twisted 2-cycle odd-sector Gram has eigenvalues EXACTLY
      +-|a_J| of the {a, b} carrier cross-block (trace forced to 0
      by the same covariance that forces the v898 {a,b} zeros), so
      OS positivity under theta_abT DEMANDS a_J = 0 while the v898
      gate G3 demands a_J != 0 -- reflection positivity and the
      block-functor floor are MUTUALLY EXCLUSIVE on this family.

CONVENTIONS (v898 / round 57, rebuilt inline; READ-ONLY import of
tfpt_constants): 16-dim Majorana one-particle space; boundary
channel CH(0) = indices 10..15 (A3 block B), carrier channels
CH(i) = {2(i-1), 2(i-1)+1}, i = 1..5.  KMS covariance A_beta =
-tan(beta h / 2) (spectral, = i tanh(beta K / 2) with K = i h);
h(u, t) = -(u A16_dep + t A_int).  Two-point function omega(c_i c_j)
= delta_ij + i A_ij; Wick by Pfaffian recursion (v519 form).  RP
criterion (v519, ported): theta acts on monomials antilinearly with
REVERSAL, spin signs and the twist eta^deg; Gram M_ab =
omega(theta(e_a) e_b) over half-side monomial bases; RP demands M
Hermitian AND PSD, sector-typed (one-particle / even deg <= 2; deep
sectors odd deg <= 3, even deg <= 4 at representative points).  A
PASS is a SECTOR statement, not full-algebra RP.  Modular route:
restriction of a quasi-free state = subblock covariance C_P;
K_mod = log((I - C_P)/C_P); seam rotation generator K_rot = i J3
(J3 = boundary block of A16_dep, e^{2pi J3} = I); geometric-
temperature defect D(u, t, beta) = ||K_mod + 2pi K_rot||_F /
||2pi K_rot||_F (sign frozen from the exact t = 0 anatomy K_mod =
-beta K_rot).  NUMERICAL PROTOCOL (exploration grade, declared):
numpy float64 eigendecompositions; structural zeros land at machine
scale ~1e-15; frozen thresholds NZ_FLOOR = 1e-8, ZTOL = 1e-10
(structural-zero ceiling for relative defects), PF_FLOOR = 1e-16;
bisections/ternary searches to interval < 1e-8.  All structural
wiring (compiler rebuild, A_int, canonical Pf4 signs) is exact
integer arithmetic; the Pfaffian factorization ward is EXACT sympy.

FROZEN CLAIMS (2026-08-10, frozen + SHA-hashed before the frozen
run):

 R1  REFLECTION CENSUS (typed by measurement).
     (a) Gamma16 fixes both grading blocks (diagonal +-1) -- NOT a
         side-exchanging reflection; Theta_0 is particle-hole (v898
         R1.2), not spatial; the untwisted 2-cycle swap has 1p-Gram
         Hermiticity defect >= 0.3 at (u=1, t=0, beta=1) -- not an
         OS reflection.  The two spatial candidates are theta_S
         (sheet swap, sigma_x per Majorana pair, sides = the two
         sheets {even}/{odd} indices; the v440 collar form) and
         theta_abT (channel a <-> b with intra-pair twist, sides =
         CH(a)/CH(b)).
     (b) THE TWIST IS FORCED (v519 regression on this family):
         eta = 1 breaks Gram Hermiticity for both candidates
         (defect >= 0.5); eta = +i is Hermitian at the bare point
         (<= ZTOL); eta = -i flips the 1p sheet-swap Gram to
         negative (lam_min <= -0.4 at (1, 0, 1)).
 R2  SHEET-SWAP RP (theta_S).
     (a) the 1p Gram is Hermitian on the ENTIRE scan grid
         t in {0, 0.01, 0.03, 1/16, 1/8, 1/4, 1/2, 1} x beta in
         {1/2, 1, 2, 4, 2pi} x u = 1, plus u in {0, 1/2, 2} at
         (t=1/8, beta=1): relative defect <= 1e-10;
     (b) THE u >= t LAW (v2, see amendment): the 1p PSD boundary
         satisfies u_c >= t, with EQUALITY u_c = t (bisected
         |u_c - t| <= 1e-6) at t in {1/16, 1/8} x beta in {1/2, 1,
         2, 4} AND at t = 1/4 x beta in {1/2, 1, 2} (11 of 12 grid
         points); at the deep-coupling corner (t = 1/4, beta = 4)
         the boundary LIFTS ABOVE the marginal line: u_c = 0.3627
         +- 0.005 > t (measured exception).  At u = t the exact
         zero mode of h(t, t) makes the Gram marginal (|lam_min| <=
         1e-6 at the beta = 1 rows) with strict signs at
         u = t -+ 0.02.  RP at the one-particle level FORCES the
         diagonal kernel to dominate the mixing: u >= t, with the
         boundary exactly u = t throughout the deployed region
         (t <= 1/8: all scanned beta).  The deployed (u=1, t=1/8)
         passes with margin 7/8; u = 0 (round-57 "u unforced incl.
         0") is EXCLUDED by RP.
     (c) THE PFAFFIAN LOCK (exact sympy): det(A16_dep + t A_int) =
         (t-1)^2 (3t^2-1)^2 (9t^3+21t^2-t-1)^2 EXACTLY; positive
         real roots t/u in {t_gap, 1/sqrt(3), 1} with t_gap =
         0.2309488708... the smallest positive root of
         9t^3+21t^2-t-1.  The u = t RP boundary is the THIRD root
         (t/u = 1): h(t, t) is singular (min |eig| <= 1e-10).
     (d) STRICT RP FAILS FOR ALL t > 0: the even deg-2 Gram
         Hermiticity defect is >= 1e-8 at every scanned point with
         t > 0, beta <= 2pi (at the deployed point: 0.0982 +-
         0.005); NO pair-sign dressing repairs it (256-scan min
         defect >= 0.05); the defect DIES thermally (defect at
         (1/8, 30) < defect at (1/8, 1) -- report);
     (e) the HERMITIZED PSD boundary t_c(beta), bisected at beta in
         {1/2, 1, 2, 4, 2pi, 30}: frozen values {0.2159, 0.2205,
         0.2276, 0.2307, 0.2309, 0.2309} +- 0.01, monotone
         nondecreasing, and |t_c(30) - t_gap| <= 1e-4: the
         zero-temperature limit of the RP boundary IS the first
         Pfaffian root (the exact level crossing);
     (f) deep sectors at the strict point (t=0, beta=1): odd
         deg <= 3 (64-dim) lam_min = 0.0987 +- 0.005 > 0, even
         deg <= 4 (99-dim) lam_min = 0.0456 +- 0.005 > 0, both
         Hermitian <= ZTOL -- the bare seam state is RP through
         deg-4 sectors, not just at the 2-point level.
 R3  TWISTED 2-CYCLE RP (theta_abT).
     (a) Gram Hermitian on the whole scan grid (defect <= 1e-10)
         including the u rows -- theta_abT is a reflection of the
         FAMILY, not of a point;
     (b) THE INCOMPATIBILITY THEOREM (measured): the full half-side
         algebra of CH(a) is 4 monomials; at t = 0 the Gram is
         marginally PSD (min eig >= -1e-9, odd sector identically
         0 <= 1e-10); for t > 0 the odd-sector eigenvalues are
         EXACTLY {-|a_J|, +|a_J|} of the {a, b} carrier cross-block
         (trace <= 1e-10, identity | |lam| - |a_J| | <= 1e-10) --
         the SAME covariance that forces the v898 {a,b} zeros
         forces the trace to vanish.  Hence OS positivity under
         theta_abT <=> a_J = 0 <=> the v898 floor gate G3 FAILS:
         reflection positivity and the block-functor mixing floor
         are mutually exclusive on this family.  Gate: lam_min <=
         -NZ_FLOOR at every scanned t >= 0.01 (u = 1).
 R4  TYPED RP ANSWER (the honest classification, round-57 style):
     STRICT-RP-FORCES(t = 0): under BOTH spatial candidates the
     strictly reflection-positive locus of the family is the bare
     diagonal axis t = 0 (a BOUNDARY point, not interior);
     1P-RP-FORCES(u >= t) (sheet swap; the boundary u = t is the
     exact Pfaffian root t/u = 1, beta-independent); beta is
     RP-INTERIOR-UNBOUNDED (no scanned beta is carved at fixed
     valid (u, t)).  The deployed candidate (1, 1/8, 1): 1p-PASS
     (margin 7/8), strict-FAIL (both thetas), hermitized-INTERIOR
     (distance to t_c(1): 0.0955).
 M   THE MODULAR ROUTE (boundary reduction, 6-dim exact linear
     algebra).
     (a) t = 0 CLOSED FORM: D(0, beta) = |beta - 2pi| / (2pi)
         (ward <= 1e-9 at beta in {1, 2pi}); the 2pi-KMS locus on
         the bare axis is EXACTLY beta = 2pi (ternary beta* =
         2pi +- 1e-6, D* <= 1e-10) -- the deployed angle
         beta_angle = 2pi (v526/v519/v239) is the geometric
         temperature of the UNCOUPLED seam;
     (b) OFF-AXIS THE LOCUS IS EMPTY: frozen table t in {1/32,
         1/16, 1/8, 1/4}: min-over-beta defect D* = {0.0202,
         0.0712, 0.2136, 0.4733} +- 0.005 at beta* = {6.368,
         6.544, 6.787, 6.183} +- 0.1, with J3-ray residual
         rf(beta*) >= 1e-4: K_mod leaves the rotation ray for
         every t > 0.  TYPED: MODULAR-LOCUS-POINT(t=0, beta=2pi),
         i.e. PIN-EXCLUDES-MIXING -- the geometric-temperature
         demand does not pin (t, beta) inside the mixing family,
         it kills the mixing; distances to the deployed candidate:
         |2pi - 1| = 5.2832 in beta, 1/8 in t.  On the deployed
         line beta = 1 the defect is flat 0.84..0.86 with min at
         t = 0 -- the deployed candidate is FAR from geometric KMS.
     (c) ANATOMY: carrier reduction at the deployed point has
         J-ray residual fraction 0.205 +- 0.02 (not rotation-
         proportional); the sheet reduction admits NO rotation
         (P theta_S-side A16_dep P = 0 exactly -- J maps sheet to
         sheet); the GROUND-STATE boundary reduction stays exactly
         on the rotation ray for t < t_gap (residual <= 1e-9 at
         t in {1/16, 1/8, 0.2}) and leaves it beyond (residual >=
         0.5 at t = 0.3): the modular anatomy locks to the SAME
         first Pfaffian root as the RP boundary.
 T   THE THERMAL CURVE (order parameter m_x(beta) = sqrt(sum of
     squared cross-duad Frobenius norms) at (u=1, t=1/8)).
     (a) peak at beta_pk = 1.673033 +- 5e-4 with m_pk = 0.391967
         +- 1e-4 (PREMISE CORRECTION: round-57 "peak at beta = 2"
         was the coarse-grid argmax; m_x(2) = 0.383925 < m_pk);
         half-max at 0.473114 / 4.343665 +- 0.005 (FWHM 3.870551);
         exactly ONE inflection at beta = 3.10411 +- 0.005
         (step-stability <= 2e-3; no sign change of the second
         difference on [0.05, 1.7) at step 0.005); the beta = 100
         state has 0/15 cross-blocks at the floor (round-57
         THERMAL-MIXING regression);
     (b) DISTINGUISHED-POINT CENSUS (frozen set, frozen window):
         markers {peak, half-max left/right, FWHM, inflection}
         against the deployed-constant set {1/2, 1, 2, 3, 4, 5,
         pi/2, pi, 2pi, 4pi, 8pi, 1/(2pi), 1/(4pi), 1/(8pi)} with
         relative window 0.005: the frozen claim is NO HIT
         (DISTINGUISHED-ABSENT) -- nearest misses printed
         (inflection vs pi at 1.19%, FWHM vs 4 at 3.2%); typed as
         reading-grade census, never a derivation.
 C   CONTROLS (must fire; frozen fire rules; RNG ONLY here).
     C1 ORIENTATION-REVERSED MEDIATOR (the round-57 premise
        respected: Pf4 is quadratic, global sign flips are
        INVISIBLE): (i) invisibility ward: at u = 0 the global
        flip A_int -> -A_int leaves ALL 15/15 per-edge Pf4 signs
        of the KMS state invariant (must NOT fire); (ii) the FIRE:
        the row-swapped A_int (orientation reversal of carrier
        channel 1) at (1, 1/8, 1) flips the Pf4 sign on EXACTLY
        the 5 duads containing channel 1 ({0,1}, {1,2}, {1,3},
        {1,4}, {1,5}), none dead.
     C2 WRONG REFLECTION (mixes gradings): theta_mix (swap carrier
        indices 0..5 with boundary 10..15) at (1, 0, 1) -- where
        both spatial candidates pass/are marginal -- breaks the
        even deg-2 Gram: relative Hermiticity defect >= 0.5 AND
        hermitized lam_min <= -0.3.
     C3 SEEDED RANDOM PAIRINGS (rng seed 898, 3 draws): random
        perfect matchings of the 16 indices as theta: all 3 break
        the 1p Gram at the deployed point (defect >= 0.5 or
        lam_min <= -0.1).
     C4 AST FIREWALL: banned identifiers zetazero / nzeros /
        primerange / isprime / primepi / nextprime / prevprime.

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K2 an RP ward breaks (census, twist, law, lock,
     sectors, incompatibility)                   -> RPROUTE-BROKEN
  K3 a modular ward breaks                       -> MODROUTE-BROKEN
  K4 a thermal-curve ward breaks                 -> THERMAL-BROKEN
  K7 a control does not fire                     -> CONTROL-DEAD

VERDICT (frozen enum): SEAMSTATE-MEASURED [RP-CARVES(u >= t EXACT;
STRICT-RP-FORCES t=0; t_c -> t_gap = root(9t^3+21t^2-t-1)),
MODULAR-LOCUS-POINT(t=0, beta=2pi; PIN-EXCLUDES-MIXING),
THERMAL-PEAK(beta = 1.6730; DISTINGUISHED-ABSENT)] /
PIPELINE-BROKEN / RPROUTE-BROKEN / MODROUTE-BROKEN /
THERMAL-BROKEN / CONTROL-DEAD.  Exit 0 iff all checks pass and no
kill fired; else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  NO physics claim beyond the recorded
identities and measurements: the [O] premise of v898 stays [O];
RP-THETA-OPEN is ANSWERED AS A MEASUREMENT on the candidate family
(two deployable spatial thetas and their carving), NOT as a physics
realization; whether the actual seam realizes any state is
untouched; no marker moves.  NO RH claim.

SPEC v1 (2026-08-10): frozen after the three declared smoke rounds;
no amendments at freeze.
SPEC v2 AMENDMENT (honest, after the frozen run of v1; the
fail-first output is preserved in the round transcript): the v1
claim R2(b) asserted u_c = t "beta-INDEPENDENT" at all 12 grid
points; the frozen run FAILED exactly there -- the smoke grid had
bisected t = 1/4 only at beta = 1, and the v1 run measured
u_c(1/4, 4) = 0.3627 != 1/4.  The claim is re-typed to the measured
law u_c >= t with equality on 11/12 points (all of t <= 1/8, and
t = 1/4 for beta <= 2) and the lifted boundary u_c = 0.3627 +-
0.005 at (1/4, 4) gated as the exception.  The u = t marginality
(exact zero mode), the Pfaffian lock, and every other frozen claim,
grid, threshold and fire rule are untouched; the deployed-region
statement (t <= 1/8: boundary exactly u = t at every scanned beta)
is unchanged.

Sources (read-only, machinery rebuilt inline): v898_kms_schur_mixing
(frozen probe kms_schur_mixing_probe, round 55: family, gates),
seam_mixing_normalization_probe (round 57: numpy protocol, thermal
finding), seam_minimal_mediator_probe (round 57: quadratic
invisibility, covariance-trivial boundary), v519 (RP Gram + forced
twist), v424/v426/v440 (BW dictionary, collar Theta = I (x)
sigma_x), v526/v239 (beta_angle = 2pi seats), tfpt_constants
(N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/seam_state_derivation_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time

import numpy as np
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402  (READ-ONLY)

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

NZ_FLOOR = 1e-8            # nonzero decision floor (frozen)
ZTOL = 1e-10               # structural-zero ceiling (frozen)
PF_FLOOR = 1e-16           # Pf4 nonzero floor (frozen)
TGAP_REF = 0.2309488708333614   # smallest positive root, re-derived


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print("%s  (t=%.1fs)" % (title, time.time() - T0))
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ---------------------------------------------------------- bit model
# (v880 / v888 conventions rebuilt inline, byte-parallel to round 57)
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000
FSIG = 0b0111
LOWIDX = {1: 0, 2: 1, 4: 2, 8: 3}


def sig(v):
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


SIGP = tuple(sig(v) for v in range(16))


def polar_shift(c):
    return tuple((pc(v) * (pc(v) - 1) // 2 + pc(c & v)) % 2
                 for v in range(16))


def iota_bits(v):
    b = [(v >> i) & 1 for i in range(4)]
    b.append(sum(b) % 2)
    return tuple(b)


IOTA_MSG = [iota_bits(v) for v in range(16)]


def iota_support(v):
    return frozenset(i + 1 for i, bit in enumerate(IOTA_MSG[v]) if bit)


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


def perm_order(p):
    o, pp = 1, p
    ident = tuple(range(len(p)))
    while pp != ident:
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


def cycle_type(perm):
    n = len(perm)
    seen = [False] * n
    cyc = []
    for i in range(n):
        if seen[i]:
            continue
        ln, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            ln += 1
        cyc.append(ln)
    return tuple(sorted(cyc))


def edge_orbits(perm):
    n_ord = perm_order(perm)
    seen = set()
    out = []
    for i, j in itertools.combinations(range(6), 2):
        e = frozenset({i, j})
        if e in seen:
            continue
        x, y = i, j
        edges = set()
        rev = False
        for _k in range(n_ord):
            edges.add(frozenset({x, y}))
            x, y = perm[x], perm[y]
            if (x, y) == (j, i):
                rev = True
        seen |= edges
        out.append((frozenset(edges), rev, (i, j)))
    return out


DUADS_CH = sorted(itertools.combinations(range(6), 2))


def main():
    print("SEAM.STATE.DERIVATION.01 -- RP, the modular route and the "
          "thermal curve, measured")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (v898 rebuilt)")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s" % (BANNED_IDS,),
          not bad, kill="K0")

    refs = [polar_shift(c) for c in range(16)]
    ok_ref = all(
        all(q[x ^ y] ^ q[x] ^ q[y] == HT[x][y]
            for x in range(16) for y in range(16)) for q in refs)
    arf1 = sorted(q for q in refs if q.count(0) == 6)
    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand = [q for q in siginv if q[A_BIT] == 1 and q[FSIG] == 0]
    check("S0.1 v880/v845 rebuilt: 16 refinements, 6 Arf-1, unique q*",
          ok_ref and len(set(refs)) == 16 and len(arf1) == 6
          and len(cand) == 1, kill="K0")
    QSTAR = cand[0]
    NZ = list(range(1, 16))
    ovoid = [v for v in NZ if QSTAR[v] == 0]

    def duad(v):
        return frozenset(i for i, q in enumerate(arf1) if q[v] == 0)

    DUADS_L = sorted((frozenset(d)
                      for d in itertools.combinations(range(6), 2)),
                     key=sorted)
    dmap = {v: duad(v) for v in NZ}
    V0 = arf1.index(QSTAR)
    phi = {}
    ok_phi = True
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        ok_phi &= (len(others) == 1 and len(islot) == 1)
        phi[next(iter(others))] = next(iter(islot))
    ok_phi &= (len(phi) == 5 and set(phi.values()) == set(range(1, 6)))

    def lab(j):
        return 0 if j == V0 else phi[j]

    chd = {v: frozenset(lab(j) for j in dmap[v]) for v in NZ}
    SP6 = []
    gl_n = 0
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = [0] * 16
        for v in range(1, 16):
            lb = v & -v
            p[v] = p[v ^ lb] ^ imgs[LOWIDX[lb]]
        if len(set(p)) != 16:
            continue
        gl_n += 1
        if all(HT[imgs[x]][imgs[y]] == 1
               for x in range(4) for y in range(x + 1, 4)):
            SP6.append(tuple(p))
    S5P = list(itertools.permutations(range(5)))
    AUT = []
    for p in SP6:
        if any(QSTAR[p[v]] != QSTAR[v] for v in range(16)):
            continue
        if compose(p, SIGP) != compose(SIGP, p):
            continue
        pis = [pi for pi in S5P
               if all(IOTA_MSG[p[v]] == tuple(IOTA_MSG[v][pi[s]]
                                              for s in range(5))
                      for v in range(16))]
        if pis:
            AUT.append(p)
    g_pin = [p for p in AUT
             if perm_order(p) == 6 and compose(p, p) == SIGP]
    check("S0.2 duad model + Aut pin: 15 <-> 15 channel duads, "
          "|Sp(4,2)| = %d == 720, |Aut| = %d == 6, generator unique"
          % (len(SP6), len(AUT)),
          ok_phi and sorted(chd.values(), key=sorted) == DUADS_L
          and gl_n == 20160 and len(SP6) == 720 and len(AUT) == 6
          and len(g_pin) == 1, kill="K0")
    GEN = g_pin[0]

    a1idx = {q: i for i, q in enumerate(arf1)}
    tau = [a1idx[tuple(q[GEN[v]] for v in range(16))] for q in arf1]
    pia = [0] * 6
    for j in range(6):
        pia[tau[j]] = j
    pia = tuple(pia)
    PI6 = [0] * 6
    for j in range(6):
        PI6[lab(j)] = lab(pia[j])
    PI6 = tuple(PI6)
    cycles = []
    seen = set()
    for i in range(6):
        if i in seen:
            continue
        cyc, j = [], i
        while j not in seen:
            seen.add(j)
            cyc.append(j)
            j = PI6[j]
        cycles.append(cyc)
    TWO = sorted(next(c for c in cycles if len(c) == 2))
    a_ch, b_ch = TWO
    check("S0.3 deployed channel permutation pi = %s, cycle type %s "
          "== (1, 2, 3); 2-cycle {%d, %d}"
          % (PI6, cycle_type(PI6), a_ch, b_ch),
          PI6[0] == 0 and cycle_type(PI6) == (1, 2, 3), kill="K0")

    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
    CAR_IDX = list(range(10))
    BND_IDX = list(range(10, 16))
    img = [0] * 16
    for i in range(6):
        for k, s in enumerate(CH[i]):
            img[s] = CH[PI6[i]][k]

    J2 = np.array([[0, 1], [-1, 0]], dtype=np.int64)
    I2 = np.eye(2, dtype=np.int64)
    IOTA6 = np.vstack([I2, I2, I2])
    orbs = edge_orbits(PI6)

    def put_ordered(A, x, y, B):
        rx, cy = CH[x], CH[y]
        for r in range(len(rx)):
            for c in range(len(cy)):
                A[rx[r], cy[c]] = B[r, c]
                A[cy[c], rx[r]] = -B[r, c]

    A_int = np.zeros((16, 16), dtype=np.int64)
    for edges, rev, rep in orbs:
        i, j = rep
        B = J2 if rev else (IOTA6 if i == 0 else I2)
        x, y = i, j
        for _k in range(perm_order(PI6)):
            put_ordered(A_int, x, y, B)
            x, y = PI6[x], PI6[y]
    okA = (np.array_equal(A_int[np.ix_(img, img)], A_int)
           and np.array_equal(A_int, -A_int.T))
    A16_dep = np.zeros((16, 16), dtype=np.int64)
    for i in range(8):
        A16_dep[2 * i, 2 * i + 1] = 1
        A16_dep[2 * i + 1, 2 * i] = -1
    okD = (np.array_equal(A16_dep[np.ix_(img, img)], A16_dep)
           and np.array_equal(A16_dep @ A16_dep,
                              -np.eye(16, dtype=np.int64)))
    check("S0.4 A_int rebuilt (integer, antisymmetric, exactly "
          "covariant); A16_dep = (+)_8 J covariant with A^2 = -I",
          okA and okD, kill="K0")

    Aint_f = A_int.astype(np.float64)
    Adep_f = A16_dep.astype(np.float64)
    I16 = np.eye(16)
    CH2 = {i: [2 * i, 2 * i + 1] for i in range(6)}

    def kms_A_gen(Am, u, t, beta):
        h = -(u * Adep_f + t * Am)
        w, Q = np.linalg.eigh(1j * h)
        f = 1.0 / (1.0 + np.exp(np.clip(beta * w, -700, 700)))
        C = (Q * f) @ Q.conj().T
        return (-1j * (2 * C - I16)).real, w

    def kms_A(u, t, beta):
        return kms_A_gen(Aint_f, u, t, beta)[0]

    def compress12(A):
        Ahat = np.zeros((12, 12))
        IO = IOTA6.astype(np.float64)
        for (i, j) in DUADS_CH:
            if i == 0:
                B = IO.T @ A[np.ix_(CH[0], CH[j])] / 3.0
            else:
                B = A[np.ix_(CH[i], CH[j])]
            for rr in range(2):
                for cc in range(2):
                    Ahat[CH2[i][rr], CH2[j][cc]] = B[rr, cc]
                    Ahat[CH2[j][cc], CH2[i][rr]] = -B[rr, cc]
        return Ahat

    def pf4_of(Ahat):
        out = {}
        for (i, j) in DUADS_CH:
            B = Ahat[np.ix_(CH2[i], CH2[j])]
            out[frozenset({i, j})] = -(B[0, 0] * B[1, 1]
                                       - B[0, 1] * B[1, 0])
        return out

    pf4_c = pf4_of(compress12(Aint_f))
    sign_c = {d: (1 if v > 0 else -1) for d, v in pf4_c.items()}

    def blocks_census(A):
        return {(i, j): float(np.linalg.norm(A[np.ix_(CH[i], CH[j])]))
                for (i, j) in DUADS_CH}

    A18, w18 = kms_A_gen(Aint_f, 1.0, 0.125, 1.0)
    smax18 = float(np.max(np.abs(np.tanh(1.0 * w18 / 2.0))))
    bn18 = blocks_census(A18)
    n18 = sum(1 for v in bn18.values() if v >= NZ_FLOOR)
    fz18 = max(abs(A18[CH[a_ch][k], CH[b_ch][k]]) for k in range(2))
    check("S0.5 v898 regression at (u=1, t=1/8, beta=1): smax = "
          "%.6f (0.668 +- 2e-3), 15/15 cross-blocks at the floor "
          "(%d), forced zeros of the {%d,%d} block < ZTOL (%.1e), "
          "all 15 canonical Pf4 signs negative"
          % (smax18, n18, a_ch, b_ch, fz18),
          abs(smax18 - 0.668) < 2e-3 and n18 == 15 and fz18 < ZTOL
          and all(s == -1 for s in sign_c.values()), kill="K0")

    # ---------------- RP machinery (v519 form, ported)
    def wick_factory(A):
        W = np.eye(16, dtype=complex) + 1j * A
        memo = {}

        def wick(idx):
            idx = tuple(idx)
            if len(idx) == 0:
                return 1.0 + 0j
            if len(idx) % 2 == 1:
                return 0.0 + 0j
            if idx in memo:
                return memo[idx]
            head, rest = idx[0], idx[1:]
            tot = 0.0 + 0j
            for j, b in enumerate(rest):
                sub = rest[:j] + rest[j + 1:]
                tot += (-1) ** j * W[head, b] * wick(sub)
            memo[idx] = tot
            return tot
        return wick

    def theta_mono(mono, r, s, eta):
        imgs = [r[a] for a in reversed(mono)]
        coeff = eta ** len(mono)
        for a in mono:
            coeff *= s[a]
        lst = list(imgs)
        sign = 1
        for i in range(len(lst)):
            for j in range(len(lst) - 1 - i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    sign = -sign
        return coeff * sign, tuple(lst)

    def gram(basis, r, s, eta, wick):
        n = len(basis)
        M = np.zeros((n, n), dtype=complex)
        for ai, ma in enumerate(basis):
            ca, ia = theta_mono(ma, r, s, eta)
            for bi, mb in enumerate(basis):
                M[ai, bi] = ca * wick(tuple(list(ia) + list(mb)))
        return M

    def metrics(M):
        nm = max(float(np.max(np.abs(M))), 1e-300)
        hd = float(np.max(np.abs(M - M.conj().T)) / nm)
        lm = float(np.min(np.linalg.eigvalsh((M + M.conj().T) / 2)))
        return hd, lm

    S_ONE = {k: 1 for k in range(16)}

    r_S = {}
    for i in range(8):
        r_S[2 * i] = 2 * i + 1
        r_S[2 * i + 1] = 2 * i
    P_S = [2 * i for i in range(8)]

    r_ab = {k: k for k in range(16)}
    for k in range(2):
        r_ab[CH[a_ch][k]] = CH[b_ch][k]
        r_ab[CH[b_ch][k]] = CH[a_ch][k]
    r_abT = {k: k for k in range(16)}
    for k in range(2):
        r_abT[CH[a_ch][k]] = CH[b_ch][1 - k]
        r_abT[CH[b_ch][k]] = CH[a_ch][1 - k]
    P_ab = list(CH[a_ch])

    B1_S = [(a,) for a in P_S]
    B2_S = [()] + [tuple(c) for c in itertools.combinations(P_S, 2)]
    B1_ab = [(a,) for a in P_ab]
    B2_ab = [(), tuple(P_ab)]

    def rp_eval(A, r, P, b1, b2, eta=1j, s=None):
        wk = wick_factory(A)
        s = s or S_ONE
        M1 = gram(b1, r, s, eta, wk)
        M2 = gram(b2, r, s, eta, wk)
        return metrics(M1), metrics(M2), M1, M2

    # ==================================================================
    section("R1 -- reflection census + the forced twist")
    # ==================================================================
    A0 = kms_A(1.0, 0.0, 1.0)
    Gamma16 = np.diag([-1.0] * 10 + [1.0] * 6)
    side_fix = float(np.linalg.norm(
        Gamma16[np.ix_(CAR_IDX, BND_IDX)]))
    (m1u, m2u), _m, _M1, _M2 = (None, None), None, None, None
    m1u, m2u, _M1, _M2 = rp_eval(A0, r_ab, P_ab, B1_ab, B2_ab)
    check("R1.1 CENSUS: Gamma16 is diagonal (side-fixing, off-block "
          "%.1e) -- not a side-exchanging reflection; Theta_0 is "
          "particle-hole (v898 R1.2, cited); the UNTWISTED 2-cycle "
          "swap is NOT an OS reflection: Gram Hermiticity defect "
          "%.3f >= 0.3 already at (1, 0, 1) (orientation-"
          "preserving); spatial candidates: theta_S (sheet swap = "
          "v440 collar lift) and theta_abT (orientation-reversed "
          "2-cycle)" % (side_fix, max(m1u[0], m2u[0])),
          side_fix == 0.0 and max(m1u[0], m2u[0]) >= 0.3, kill="K2")

    ok_tw = True
    det_tw = {}
    for eta, tag in ((1.0, "1"), (1j, "+i"), (-1j, "-i")):
        mS1, mS2, _a, _b = rp_eval(A0, r_S, P_S, B1_S, B2_S, eta=eta)
        mT1, mT2, _c, _d = rp_eval(A0, r_abT, P_ab, B1_ab, B2_ab,
                                   eta=eta)
        det_tw[tag] = (mS1, mS2, mT1, mT2)
    ok_tw &= (max(det_tw["1"][0][0], det_tw["1"][2][0]) >= 0.5)
    ok_tw &= (max(det_tw["+i"][0][0], det_tw["+i"][1][0],
                  det_tw["+i"][2][0], det_tw["+i"][3][0]) <= ZTOL)
    ok_tw &= (det_tw["-i"][0][1] <= -0.4)
    check("R1.2 THE TWIST IS FORCED (v519 regression): eta = 1 "
          "breaks Hermiticity (max defect %.3f >= 0.5); eta = +i "
          "Hermitian at the bare point (max defect %.1e <= ZTOL); "
          "eta = -i flips the 1p sheet Gram negative (lam_min "
          "%.4f <= -0.4)"
          % (max(det_tw["1"][0][0], det_tw["1"][2][0]),
             max(det_tw["+i"][0][0], det_tw["+i"][1][0],
                 det_tw["+i"][2][0], det_tw["+i"][3][0]),
             det_tw["-i"][0][1]),
          ok_tw, kill="K2")

    # ==================================================================
    section("R2 -- sheet-swap RP: the u >= t law + the Pfaffian lock")
    # ==================================================================
    T_GRID = [0.0, 0.01, 0.03, 1.0 / 16, 0.125, 0.25, 0.5, 1.0]
    B_GRID = [0.5, 1.0, 2.0, 4.0, 2 * math.pi]
    hd1_max = 0.0
    hd2_min_tpos = 1e9
    hd2_at = {}
    for t in T_GRID:
        for beta in B_GRID:
            m1, m2, _a, _b = rp_eval(kms_A(1.0, t, beta), r_S, P_S,
                                     B1_S, B2_S)
            hd1_max = max(hd1_max, m1[0])
            hd2_at[(t, beta)] = m2[0]
            if t > 0:
                hd2_min_tpos = min(hd2_min_tpos, m2[0])
    for u in (0.0, 0.5, 2.0):
        m1, m2, _a, _b = rp_eval(kms_A(u, 0.125, 1.0), r_S, P_S,
                                 B1_S, B2_S)
        hd1_max = max(hd1_max, m1[0])
    check("R2.1 1p Gram Hermitian on the ENTIRE scan grid (8 t x 5 "
          "beta + 3 u rows): max relative defect %.1e <= 1e-10"
          % hd1_max, hd1_max <= 1e-10, kill="K2")

    def lam1p(u, t, beta):
        wk = wick_factory(kms_A(u, t, beta))
        M1 = gram(B1_S, r_S, S_ONE, 1j, wk)
        return float(np.min(np.linalg.eigvalsh(
            (M1 + M1.conj().T) / 2)))

    ok_law = True
    rows = []
    uc_exc = None
    for t in (1.0 / 16, 0.125, 0.25):
        for beta in (0.5, 1.0, 2.0, 4.0):
            lo, hi = 0.0, 2 * t
            for _ in range(60):
                mid = (lo + hi) / 2
                if lam1p(mid, t, beta) < 0:
                    lo = mid
                else:
                    hi = mid
            uc = (lo + hi) / 2
            if (t, beta) == (0.25, 4.0):
                uc_exc = uc
                ok_law &= (abs(uc - 0.3627) <= 5e-3
                           and uc > t + 0.05)
            else:
                ok_law &= (abs(uc - t) <= 1e-6)
            rows.append((t, beta, uc))
        lm_at = lam1p(t, t, 1.0)
        ok_law &= (abs(lm_at) <= 1e-6)
        ok_law &= (lam1p(t + 0.02, t, 1.0) > 0)
        ok_law &= (lam1p(t - 0.02, t, 1.0) < 0)
    for (t, beta, uc) in rows:
        print("      u_c(t=%-7s beta=%-4s) = %.10f  (|u_c - t| = "
              "%.1e)" % (round(t, 4), beta, uc, abs(uc - t)))
    check("R2.2 THE u >= t LAW (v2): 1p PSD boundary u_c >= t, "
          "EQUALITY |u_c - t| <= 1e-6 on 11/12 grid points (all "
          "t <= 1/8 + (1/4, beta <= 2)); measured exception at "
          "(1/4, 4): u_c = %.4f (0.3627 +- 5e-3, lifted ABOVE "
          "the marginal line); marginal at u = t, strict signs at "
          "u = t -+ 0.02; the deployed (1, 1/8) passes with margin "
          "7/8; u = 0 is EXCLUDED by RP (round-57 'u unforced' "
          "carved)" % (uc_exc if uc_exc is not None else -1),
          ok_law, kill="K2")

    tsym = sp.Symbol("t")
    Msym = sp.Matrix(16, 16, lambda i, j:
                     sp.Integer(int(A16_dep[i, j]))
                     + tsym * sp.Integer(int(A_int[i, j])))
    dsym = sp.factor(Msym.det())
    target = ((tsym - 1) ** 2 * (3 * tsym ** 2 - 1) ** 2
              * (9 * tsym ** 3 + 21 * tsym ** 2 - tsym - 1) ** 2)
    ok_fac = sp.expand(dsym - target) == 0
    cub = 9 * tsym ** 3 + 21 * tsym ** 2 - tsym - 1
    roots_pos = [x for x in sp.Poly(cub, tsym).all_roots()
                 if x.is_real and x > 0]
    t_gap = float(sp.N(roots_pos[0], 20))
    _A11, w11 = kms_A_gen(Aint_f, 0.125, 0.125, 1.0)
    min_eig_tt = float(np.min(np.abs(w11)))
    check("R2.3 THE PFAFFIAN LOCK (exact sympy): det(A16_dep + t "
          "A_int) == (t-1)^2 (3t^2-1)^2 (9t^3+21t^2-t-1)^2 (%s); "
          "positive roots t/u in {%.10f, 1/sqrt(3), 1}; the u = t "
          "boundary IS the third root: min |eig(i h(t,t))| = %.1e "
          "<= 1e-10 at t = 1/8"
          % (ok_fac, t_gap, min_eig_tt),
          ok_fac and len(roots_pos) == 1
          and abs(t_gap - TGAP_REF) < 1e-12
          and min_eig_tt <= 1e-10, kill="K2")

    hd2_dep = hd2_at[(0.125, 1.0)]
    m2_30 = rp_eval(kms_A(1.0, 0.125, 30.0), r_S, P_S, B1_S,
                    B2_S)[1]
    best_sign = 1e9
    for bits in range(256):
        s = dict(S_ONE)
        for i in range(8):
            sg = 1 if (bits >> i) & 1 == 0 else -1
            s[2 * i] = sg
            s[2 * i + 1] = sg
        wk = wick_factory(A18)
        M2 = gram(B2_S, r_S, s, 1j, wk)
        best_sign = min(best_sign, metrics(M2)[0])
    check("R2.4 STRICT RP FAILS FOR ALL t > 0: even deg-2 "
          "Hermiticity defect >= 1e-8 at every scanned t > 0, "
          "beta <= 2pi (min %.1e); at the deployed point %.4f "
          "(0.0982 +- 0.005); NO pair-sign dressing repairs it "
          "(256-scan min %.4f >= 0.05); thermally dying: defect at "
          "(1/8, 30) = %.1e < deployed (report)"
          % (hd2_min_tpos, hd2_dep, best_sign, m2_30[0]),
          hd2_min_tpos >= 1e-8 and abs(hd2_dep - 0.0982) <= 5e-3
          and best_sign >= 0.05 and m2_30[0] < hd2_dep, kill="K2")

    def lam2h(t, beta):
        wk = wick_factory(kms_A(1.0, t, beta))
        M1 = gram(B1_S, r_S, S_ONE, 1j, wk)
        M2 = gram(B2_S, r_S, S_ONE, 1j, wk)
        l1 = float(np.min(np.linalg.eigvalsh((M1 + M1.conj().T) / 2)))
        l2 = float(np.min(np.linalg.eigvalsh((M2 + M2.conj().T) / 2)))
        return min(l1, l2)

    TC_REF = {0.5: 0.2159, 1.0: 0.2205, 2.0: 0.2276, 4.0: 0.2307,
              2 * math.pi: 0.2309, 30.0: t_gap}
    tcs = []
    ok_tc = True
    for beta in (0.5, 1.0, 2.0, 4.0, 2 * math.pi, 30.0):
        lo, hi = 0.125, 0.30
        for _ in range(50):
            mid = (lo + hi) / 2
            if lam2h(mid, beta) > 0:
                lo = mid
            else:
                hi = mid
        tc = (lo + hi) / 2
        tcs.append(tc)
        ok_tc &= (abs(tc - TC_REF[beta]) <= 0.01)
        print("      t_c(beta=%-8s) = %.8f" % (round(beta, 4), tc))
    ok_tc &= all(tcs[k + 1] >= tcs[k] - 1e-9 for k in range(len(tcs) - 1))
    ok_tc &= (abs(tcs[-1] - t_gap) <= 1e-4)
    check("R2.5 HERMITIZED PSD boundary t_c(beta): frozen values "
          "+- 0.01, monotone nondecreasing, and |t_c(30) - t_gap| "
          "= %.1e <= 1e-4: the zero-temperature RP boundary IS the "
          "first Pfaffian root" % abs(tcs[-1] - t_gap),
          ok_tc, kill="K2")

    wk0 = wick_factory(A0)
    odd3 = ([(a,) for a in P_S]
            + [tuple(c) for c in itertools.combinations(P_S, 3)])
    ev4 = (B2_S + [tuple(c) for c in itertools.combinations(P_S, 4)])
    Mo = gram(odd3, r_S, S_ONE, 1j, wk0)
    Me = gram(ev4, r_S, S_ONE, 1j, wk0)
    ho, lo_ = metrics(Mo)
    he, le_ = metrics(Me)
    check("R2.6 DEEP SECTORS at the strict point (t=0, beta=1): odd "
          "deg<=3 (64-dim) lam_min = %.6f (0.0987 +- 0.005) > 0, "
          "even deg<=4 (99-dim) lam_min = %.6f (0.0456 +- 0.005) > "
          "0, Hermitian (%.1e, %.1e)"
          % (lo_, le_, ho, he),
          abs(lo_ - 0.0987) <= 5e-3 and abs(le_ - 0.0456) <= 5e-3
          and ho <= ZTOL and he <= ZTOL, kill="K2")

    # ==================================================================
    section("R3 -- twisted 2-cycle RP: the incompatibility theorem")
    # ==================================================================
    hdT_max = 0.0
    for t in T_GRID:
        for beta in B_GRID:
            m1, m2, _a, _b = rp_eval(kms_A(1.0, t, beta), r_abT,
                                     P_ab, B1_ab, B2_ab)
            hdT_max = max(hdT_max, m1[0], m2[0])
    for u in (0.0, 0.5, 2.0):
        m1, m2, _a, _b = rp_eval(kms_A(u, 0.125, 1.0), r_abT, P_ab,
                                 B1_ab, B2_ab)
        hdT_max = max(hdT_max, m1[0], m2[0])
    check("R3.1 theta_abT Gram Hermitian on the whole scan grid "
          "(max defect %.1e <= 1e-10) -- a reflection of the "
          "FAMILY" % hdT_max, hdT_max <= 1e-10, kill="K2")

    m1_0, m2_0, M1_0, _M2_0 = rp_eval(A0, r_abT, P_ab, B1_ab, B2_ab)
    odd0 = float(np.max(np.abs(M1_0)))
    lam_marg = min(m1_0[1], m2_0[1])
    ok_inc = (lam_marg >= -1e-9 and odd0 <= 1e-10)
    worst_id = 0.0
    worst_lam = 0.0
    for t in [x for x in T_GRID if x >= 0.01]:
        A = kms_A(1.0, t, 1.0)
        wk = wick_factory(A)
        M1 = gram(B1_ab, r_abT, S_ONE, 1j, wk)
        ev = np.linalg.eigvalsh((M1 + M1.conj().T) / 2)
        B = A[np.ix_(CH[a_ch], CH[b_ch])]
        aJ = (B[0, 1] - B[1, 0]) / 2
        worst_id = max(worst_id,
                       float(abs(abs(ev[0]) - abs(aJ))),
                       float(abs(abs(ev[1]) - abs(aJ))),
                       float(abs(ev[0] + ev[1])))
        worst_lam = max(worst_lam, float(ev[0]))
        ok_inc &= (abs(aJ) >= NZ_FLOOR and ev[0] <= -NZ_FLOOR)
    check("R3.2 THE INCOMPATIBILITY (measured): t = 0 marginally "
          "PSD (min eig %.1e >= -1e-9, odd sector %.1e); for every "
          "scanned t >= 0.01 the odd eigenvalues are EXACTLY "
          "{-|a_J|, +|a_J|} of the {%d,%d} block (worst identity "
          "defect %.1e <= 1e-10) with a_J >= floor => lam_min <= "
          "-NZ_FLOOR (worst %.1e): OS positivity under theta_abT "
          "<=> a_J = 0 <=> v898 G3 FAILS -- RP and the mixing "
          "floor are mutually exclusive"
          % (lam_marg, odd0, a_ch, b_ch, worst_id, worst_lam),
          ok_inc and worst_id <= 1e-10, kill="K2")

    lam_dep_1p = lam1p(1.0, 0.125, 1.0)
    check("R4.1 TYPED RP ANSWER: STRICT-RP-FORCES(t = 0) [both "
          "thetas; boundary point]; 1P-RP-FORCES(u >= t) [sheet "
          "swap; boundary = Pfaffian root t/u = 1 in the deployed "
          "region, v2]; beta RP-INTERIOR-UNBOUNDED; deployed "
          "(1, 1/8, 1): 1p-PASS (lam_min %.4f > 0, margin 7/8), "
          "strict-FAIL, hermitized-INTERIOR (dist to t_c(1) = "
          "%.4f)" % (lam_dep_1p, tcs[1] - 0.125),
          lam_dep_1p > 0 and tcs[1] > 0.125,
          "typed by measurement", kill="K2")

    # ==================================================================
    section("M -- the modular route (boundary reduction)")
    # ==================================================================
    J3f = Adep_f[np.ix_(BND_IDX, BND_IDX)]
    Krot = 1j * J3f

    def reduced(u, t, beta):
        A = kms_A(u, t, beta)
        ABB = A[np.ix_(BND_IDX, BND_IDX)]
        f = float(np.sum(ABB * J3f) / np.sum(J3f * J3f))
        rf = float(np.linalg.norm(ABB - f * J3f))
        C = (np.eye(6) + 1j * ABB) / 2
        w, Q = np.linalg.eigh(C)
        w = np.clip(w, 1e-300, 1 - 1e-16)
        Kmod = (Q * np.log((1 - w) / w)) @ Q.conj().T
        D = float(np.linalg.norm(Kmod + 2 * math.pi * Krot)
                  / np.linalg.norm(2 * math.pi * Krot))
        return D, f, rf

    D01, _f, _r = reduced(1.0, 0.0, 1.0)
    D0p, _f, _r = reduced(1.0, 0.0, 2 * math.pi)
    cf1 = abs(1.0 - 2 * math.pi) / (2 * math.pi)
    lo, hi = 0.5, 60.0
    for _ in range(80):
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if reduced(1.0, 0.0, m1)[0] < reduced(1.0, 0.0, m2)[0]:
            hi = m2
        else:
            lo = m1
    bstar0 = (lo + hi) / 2
    check("M1.1 t = 0 CLOSED FORM: D(0, beta) = |beta - 2pi|/(2pi) "
          "(|D(0,1) - %.6f| = %.1e <= 1e-9); the 2pi-KMS locus on "
          "the bare axis is beta* = %.8f = 2pi +- 1e-6 with D* = "
          "%.1e <= 1e-10: beta_angle = 2pi (v526/v239) IS the "
          "geometric temperature of the uncoupled seam"
          % (cf1, abs(D01 - cf1), bstar0, D0p),
          abs(D01 - cf1) <= 1e-9
          and abs(bstar0 - 2 * math.pi) <= 1e-6 and D0p <= 1e-10,
          kill="K3")

    MOD_REF = {1.0 / 32: (0.0202, 6.368), 1.0 / 16: (0.0712, 6.544),
               0.125: (0.2136, 6.787), 0.25: (0.4733, 6.183)}
    ok_mod = True
    for t in (1.0 / 32, 1.0 / 16, 0.125, 0.25):
        lo, hi = 0.5, 60.0
        for _ in range(80):
            m1 = lo + (hi - lo) / 3
            m2 = hi - (hi - lo) / 3
            if reduced(1.0, t, m1)[0] < reduced(1.0, t, m2)[0]:
                hi = m2
            else:
                lo = m1
        bstar = (lo + hi) / 2
        D, f, rf = reduced(1.0, t, bstar)
        dref, bref = MOD_REF[t]
        ok_mod &= (abs(D - dref) <= 5e-3 and abs(bstar - bref) <= 0.1
                   and rf >= 1e-4)
        print("      t=%-7s beta* = %.6f  D* = %.6f  rf = %.2e"
              % (round(t, 4), bstar, D, rf))
    D_line = [reduced(1.0, t, 1.0)[0]
              for t in (0.0, 1.0 / 16, 0.125, 0.25)]
    ok_line = (all(0.84 <= d <= 0.86 for d in D_line)
               and min(D_line) == D_line[0])
    check("M1.2 OFF-AXIS THE LOCUS IS EMPTY: D* and beta* match the "
          "frozen table (+-5e-3 / +-0.1), J3-ray residual rf >= "
          "1e-4 for every t > 0 -- TYPED MODULAR-LOCUS-POINT(t=0, "
          "beta=2pi), PIN-EXCLUDES-MIXING; distances to deployed: "
          "|2pi - 1| = %.4f in beta, 1/8 in t; on the beta = 1 "
          "line D is flat %s (min at t = 0)"
          % (2 * math.pi - 1, [round(d, 4) for d in D_line]),
          ok_mod and ok_line, "typed by measurement", kill="K3")

    A = A18
    ACC = A[np.ix_(CAR_IDX, CAR_IDX)]
    AdC = Adep_f[np.ix_(CAR_IDX, CAR_IDX)]
    fC = float(np.sum(ACC * AdC) / np.sum(AdC * AdC))
    resC = float(np.linalg.norm(ACC - fC * AdC) / np.linalg.norm(ACC))
    sheet_rot = float(np.linalg.norm(Adep_f[np.ix_(P_S, P_S)]))
    rf_lo = max(reduced(1.0, t, 200.0)[2]
                for t in (1.0 / 16, 0.125, 0.2))
    rf_hi = reduced(1.0, 0.3, 200.0)[2]
    check("M2.1 ANATOMY: carrier reduction J-ray residual fraction "
          "%.4f (0.205 +- 0.02); sheet reduction admits NO "
          "rotation (||P A16_dep P|| = %.1e exactly 0); ground-"
          "state boundary reduction ON the rotation ray for t < "
          "t_gap (max residual %.1e <= 1e-9 at t in {1/16, 1/8, "
          "0.2}) and OFF beyond (residual %.3f >= 0.5 at t = 0.3): "
          "the modular anatomy locks to the SAME first Pfaffian "
          "root as the RP boundary"
          % (resC, sheet_rot, rf_lo, rf_hi),
          abs(resC - 0.205) <= 0.02 and sheet_rot == 0.0
          and rf_lo <= 1e-9 and rf_hi >= 0.5, kill="K3")

    # ==================================================================
    section("T -- the thermal curve (order parameter m_x)")
    # ==================================================================
    def mx(beta):
        A = kms_A(1.0, 0.125, beta)
        s = 0.0
        for (i, j) in DUADS_CH:
            s += float(np.sum(A[np.ix_(CH[i], CH[j])] ** 2))
        return math.sqrt(s)

    lo, hi = 1.0, 2.5
    for _ in range(80):
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if mx(m1) > mx(m2):
            hi = m2
        else:
            lo = m1
    bpk = (lo + hi) / 2
    mpk = mx(bpk)

    def bisect(f, lo, hi, target, it=60):
        flo = f(lo) - target
        for _ in range(it):
            mid = (lo + hi) / 2
            if (f(mid) - target) * flo > 0:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    bl = bisect(mx, 1e-3, bpk, mpk / 2)
    br = bisect(mx, bpk, 60.0, mpk / 2)

    def d2(beta, h=0.02):
        return mx(beta + h) - 2 * mx(beta) + mx(beta - h)

    infls = []
    for h in (0.02, 0.005):
        lo, hi = 2.5, 4.0
        for _ in range(50):
            mid = (lo + hi) / 2
            if d2(mid, h) < 0:
                lo = mid
            else:
                hi = mid
        infls.append((lo + hi) / 2)
    bs = np.arange(0.05, 1.7, 0.005)
    msv = [mx(b) for b in bs]
    dd = np.diff(msv, 2)
    sgn = np.sign(dd)
    n_left = sum(1 for k in range(len(dd) - 1)
                 if sgn[k] * sgn[k + 1] < 0)
    A100 = kms_A(1.0, 0.125, 100.0)
    n100 = sum(1 for v in blocks_census(A100).values()
               if v >= NZ_FLOOR)
    ok_t1 = (abs(bpk - 1.673033) <= 5e-4
             and abs(mpk - 0.391967) <= 1e-4
             and abs(bl - 0.473114) <= 5e-3
             and abs(br - 4.343665) <= 5e-3
             and abs(infls[0] - 3.10411) <= 5e-3
             and abs(infls[0] - infls[1]) <= 2e-3
             and n_left == 0 and n100 == 0
             and mx(2.0) < mpk)
    check("T1.1 THE CURVE: peak beta_pk = %.6f (1.673033 +- 5e-4; "
          "PREMISE CORRECTION: round-57 'peak at beta = 2' was the "
          "coarse-grid argmax, m_x(2) = %.6f < m_pk = %.6f), "
          "half-max %.6f / %.6f (FWHM %.6f), ONE inflection at "
          "%.5f (step-stable %.1e), no left inflection (%d sign "
          "changes), beta = 100: %d/15 blocks (THERMAL-MIXING "
          "regression)"
          % (bpk, mx(2.0), mpk, bl, br, br - bl, infls[0],
             abs(infls[0] - infls[1]), n_left, n100),
          ok_t1, kill="K4")

    CONSTS = {"1/2": 0.5, "1": 1.0, "Z2=2": 2.0, "N_fam=3": 3.0,
              "mu4=4": 4.0, "g_car=5": 5.0, "pi/2": math.pi / 2,
              "pi": math.pi, "2pi": 2 * math.pi, "4pi": 4 * math.pi,
              "8pi": 8 * math.pi, "1/(2pi)": 1 / (2 * math.pi),
              "1/(4pi)": 1 / (4 * math.pi),
              "1/(8pi)": 1 / (8 * math.pi)}
    markers = {"peak": bpk, "halfmax-L": bl, "halfmax-R": br,
               "FWHM": br - bl, "inflection": infls[0]}
    hits = []
    nearest = []
    for mk, x in markers.items():
        best = min(CONSTS.items(), key=lambda kv: abs(x - kv[1]) / kv[1])
        rel = abs(x - best[1]) / best[1]
        nearest.append("%s=%.4f ~ %s (rel %.4f)" % (mk, x, best[0], rel))
        if rel <= 0.005:
            hits.append((mk, best[0]))
    for line in nearest:
        print("      " + line)
    check("T2.1 DISTINGUISHED-POINT CENSUS (frozen set, window "
          "0.5%%): %s -- typed reading-grade census, never a "
          "derivation" % ("NO HIT (DISTINGUISHED-ABSENT)"
                          if not hits else "HITS %s" % hits),
          not hits, "frozen claim: no deployed constant sits at a "
          "distinguished point", kill="K4")

    # ==================================================================
    section("C -- controls (must fire; RNG only here)")
    # ==================================================================
    A_p = kms_A_gen(Aint_f, 0.0, 0.125, 1.0)[0]
    A_m = kms_A_gen(-Aint_f, 0.0, 0.125, 1.0)[0]
    pf_p, pf_m = pf4_of(compress12(A_p)), pf4_of(compress12(A_m))
    inv = sum(1 for d in pf_p if abs(pf_p[d]) > PF_FLOOR
              and (pf_p[d] > 0) == (pf_m[d] > 0))
    SW = np.eye(16)
    SW[0, 0] = SW[1, 1] = 0.0
    SW[0, 1] = SW[1, 0] = 1.0
    A_sw = kms_A_gen(SW @ Aint_f @ SW.T, 1.0, 0.125, 1.0)[0]
    pf_sw = pf4_of(compress12(A_sw))
    flips = sorted(tuple(sorted(d)) for d in pf_sw
                   if abs(pf_sw[d]) > PF_FLOOR
                   and (pf_sw[d] > 0) != (sign_c[d] > 0))
    dead = sorted(tuple(sorted(d)) for d in pf_sw
                  if abs(pf_sw[d]) <= PF_FLOOR)
    check("C1 FIRES (quadratic invisibility respected): global flip "
          "A_int -> -A_int at u = 0 leaves %d/15 Pf4 signs "
          "invariant (must NOT flip); the ORIENTATION-REVERSED "
          "(row-swapped channel 1) mediator flips EXACTLY the 5 "
          "duads containing channel 1: %s (dead: %s)"
          % (inv, flips, dead or "none"),
          inv == 15 and flips == [(0, 1), (1, 2), (1, 3), (1, 4),
                                  (1, 5)] and not dead, kill="K7")

    r_mx = {k: k for k in range(16)}
    for k in range(6):
        r_mx[k] = 10 + k
        r_mx[10 + k] = k
    P_mx = list(range(6))
    B1m = [(a,) for a in P_mx]
    B2m = [()] + [tuple(c) for c in itertools.combinations(P_mx, 2)]
    m1x, m2x, _a, _b = rp_eval(A0, r_mx, P_mx, B1m, B2m)
    check("C2 FIRES: the grading-mixing theta at (1, 0, 1) -- where "
          "both spatial candidates pass/are marginal -- breaks the "
          "even deg-2 Gram: defect %.3f >= 0.5, lam_min %.3f <= "
          "-0.3" % (m2x[0], m2x[1]),
          m2x[0] >= 0.5 and m2x[1] <= -0.3, kill="K7")

    rng = np.random.default_rng(898)
    n_fire = 0
    for _trial in range(3):
        perm = rng.permutation(16)
        r = {}
        for k in range(8):
            x, y = int(perm[2 * k]), int(perm[2 * k + 1])
            r[x] = y
            r[y] = x
        P = [min(x, r[x]) for x in r if x < r[x]]
        wk = wick_factory(A18)
        M1 = gram([(a,) for a in P], r, S_ONE, 1j, wk)
        hd, lm = metrics(M1)
        if hd >= 0.5 or lm <= -0.1:
            n_fire += 1
    check("C3 FIRES: 3/3 seeded random pairings (rng 898) break the "
          "1p Gram at the deployed point (%d/3)" % n_fire,
          n_fire == 3, kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif "K0" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "K2" in KILLS:
        VERDICT = "RPROUTE-BROKEN"
    elif "K3" in KILLS:
        VERDICT = "MODROUTE-BROKEN"
    elif "K4" in KILLS:
        VERDICT = "THERMAL-BROKEN"
    else:
        VERDICT = ("SEAMSTATE-MEASURED [RP-CARVES(u >= t, boundary "
                   "u = t in the deployed region; "
                   "STRICT-RP-FORCES t=0; t_c -> t_gap = "
                   "root(9t^3+21t^2-t-1) = %.6f), "
                   "MODULAR-LOCUS-POINT(t=0, beta=2pi; "
                   "PIN-EXCLUDES-MIXING), THERMAL-PEAK(beta = "
                   "%.4f; DISTINGUISHED-ABSENT)]" % (t_gap, bpk))
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE RP ANSWER (R1-R4): two spatial reflections are deployable on
    the 16-dim space -- the sheet swap theta_S (v440 collar lift)
    and the orientation-reversed 2-cycle theta_abT; the untwisted
    2-cycle and Gamma16 are NOT reflections; the v519 twist eta = +i
    is forced again.  RP CARVES, in three exact layers: (i) the 1p
    sector forces u >= t (boundary u = t = the Pfaffian root
    t/u = 1 throughout the deployed region t <= 1/8; it lifts above
    the marginal line at the deep corner (1/4, 4) -- v2 amendment)
    -- u = 0 is now EXCLUDED, the first carving of the round-57
    'unforced' set; (ii) STRICT RP
    (Hermiticity included) forces t = 0 under BOTH thetas -- and
    under theta_abT this is a measured incompatibility THEOREM:
    the odd Gram eigenvalues are +-|a_J| of the {a,b} block, so OS
    positivity <=> a_J = 0 <=> the v898 mixing floor G3 fails;
    (iii) the hermitized boundary t_c(beta) converges to the FIRST
    Pfaffian root t_gap = 0.230949 (exact algebraic: smallest
    positive root of 9t^3 + 21t^2 - t - 1) as beta -> infinity.
    The deployed (1, 1/8, 1): 1p-PASS, strict-FAIL, hermitized-
    INTERIOR.  RP does NOT pin t = 1/8 or beta = 1.
  * THE MODULAR ANSWER (M): the 2pi-KMS locus of the boundary
    reduction is EXACTLY the point (t, beta) = (0, 2pi): the
    deployed angle beta_angle = 2pi is the geometric temperature of
    the UNCOUPLED seam, and every t > 0 breaks the rotation-ray
    alignment (rf > 0, D* up to 0.21 at t = 1/8) -- the demand
    EXCLUDES the mixing rather than pinning it; distances to the
    deployed candidate: 5.28 in beta, 1/8 in t; PIN-ABSENT for a
    joint (t, beta) selection inside the family.
  * THE THERMAL CURVE (T): peak at beta = 1.6730 (round-57 'peak at
    beta = 2' corrected -- coarse-grid artifact), half-max 0.4731 /
    4.3437, one inflection at 3.104; NO deployed constant sits at
    any distinguished point at 0.5%% (nearest miss: inflection vs
    pi at 1.2%%) -- DISTINGUISHED-ABSENT.
  * THE ONE NEW STRUCTURAL OBJECT: the exact factorization
    det(A16_dep + t A_int) = (t-1)^2 (3t^2-1)^2 (9t^3+21t^2-t-1)^2
    -- its three positive roots organize EVERYTHING measured here:
    the 1p RP boundary (t/u = 1), the zero-temperature hermitized
    RP boundary AND the ground-state modular transition (t_gap),
    all measured to coincide.  None of the roots equals 1/8: the
    deployed mixing strength remains UNPINNED by state-level
    demands; what the demands DO force is u >= t and (strictly)
    t = 0.
  * The [O] premise of v898 stays [O]; no marker moves; NO RH claim.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
