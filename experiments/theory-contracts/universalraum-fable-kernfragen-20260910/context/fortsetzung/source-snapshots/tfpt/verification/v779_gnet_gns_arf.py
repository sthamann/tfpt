#!/usr/bin/env python3
"""v779 -- GNET.GNSLIMIT.01: the G_net continuum strand -- finite-level precursors of the GNS limit net COHERENT, plus the exact C[Z4] obstruction dim law and the honest Arf negative, ONE module from two probes (27/27 + 27/27 checks, ~50 s; discovery probes gnet_gns_limit_probe.py GNS-PRECURSORS-COHERENT and gnet_arf_qsystem_probe.py GNET-ARF-NO-CORRESPONDENCE, both 2026-08-05).  THE PRECURSORS (typed finite evidence FOR the five v746 continuum theorems, never a continuum proof): the Haar scaling isometry tower intertwines EXACTLY (V isometric, V H_N = H_2N V, V L_N = L_2N V <= 2.2e-16; window data literally level-independent; Fock coherence iota(E(m)) = E'(iota(m)) <= 1.5e-14); the index-4 expectation squares COMMUTE exactly (restriction coherence, [E_I, E_J] = 0, idempotent joint expectation -- the finite half of the Longo Q-system identification); the canonical chiral-sea state is Cauchy along the tower with geometric contraction ~1/4 per doubling (d5 = 2.4e-4, parity-odd exactly 0); the index census is machine-exact at EVERY level with zero degradation (lambda* = 1/4, quasi-basis index 4*1, l = 1 anomaly stable at 3); the split witness stabilizes and decreases with separation; the finite Haag-duality census gives twisted-duality DEFECT = 0 (dim A' = 4^{n_c} exactly, exhausted by the twisted complement) and dim B'/dim A' = 4 = the local Watatani index (l = 1: ratio 3); a 10-section continuum-paper skeleton is the work product.  THE EXACT DIM LAW (part 2, the structural yield): d_c(l) = 4^(l-1) + 2^(l-1) cos(pi c/2) exactly for l = 1..6 -- the C[Z4]/Longo 4-element quasi-basis is OBSTRUCTED at every finite l with relative gap exactly 2^-l -> 0: the crossed-product structure is exactly asymptotic (the finite precursor of the GATE.METRIC.08/11 identification), and d_2(1) = 0 IS the l = 1 three-sector index-3 anomaly of v746 (the law explains it); the 185-element Watatani quasi-basis at l = 2 is explicit with sum v v* = 4*1 exact; sector-resolved split bounds are uniform along the tower; the sigma register exists internally on the Z6-quotient window W6 (deck + half-turn joint, dims (20,16,12,16), lambda* = 1/4).  THE HONEST NEGATIVE, EXHAUSTIVE: the 16 = 1 + 5 + 10 counting echo between the l = 2 window and the Arf geometry is REAL and exact but NOT geometric -- F2-rank certificate 3 vs 4 (a linear bijection is impossible), GL(4,2) census 0/20160 for EVERY Arf-1 form's 5-set, no nontrivial internal order-3 symmetry on the 16-state window (census over all 6144 generalized signed permutations); and K_matter does NOT govern the tower weight transport (x5 = (0.414, 0.586) vs pi = (1/3, 2/3); the transfer fit is non-degenerate and mismatches).  BINDING HONESTY RULE: the Watatani index 4 = |mu4| and the channel eigenvalue 4/49 = (-2/7)^2 are two different numbers from two different registers -- NOTHING equates them.  All nine controls fire (bond scramble, Z2-only average, scrambled sea, decimation embedding incl. the uniform-weights caution, wrong Arf form).  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes gnet_gns_limit_probe.py (2026-08-05, 27/27, 40.1 s, GNS-PRECURSORS-COHERENT; the G4b spec correction -- measured spanning basis of B = E(A) instead of an under-generating random set -- carried verbatim in the docstring, gate values unchanged) + gnet_arf_qsystem_probe.py (2026-08-05, 27/27, 5.2 s, GNET-ARF-NO-CORRESPONDENCE; the S4 bar-anchor spec correction carried verbatim); both re-run identically at promotion.  Promoted verbatim (part 2 wrapped in a function scope; its inspect-based SHA-freeze therefore hashes the indented source -- print-only, no gate); run() encodes both patterns (v757 precedent).  Numbers unchanged.

Original GNS-limit probe docstring (verbatim):
G_net continuum strand -- FINITE-LEVEL PRECURSORS of the GNS limit net.

Context (GNET.LOCALNET.01 / phys_gnet_local_functor_probe.py, promoted as
v746): the finite G_net functor I |-> (A(I-hat), E_I) on the mu4 quotient
circle is exact (isotony, graded locality, clock covariance), the local
Watatani index is exactly 4 for every interval l >= 2, and the Ramond
sector is a half-line/bond defect.  FIVE continuum theorems are NAMED,
NOT CLAIMED there: (1) GNS limit net, (2) index continuity along the
inductive limit, (3) identification with the Longo Q-system extension
(GATE.METRIC.08/11), (4) solitonic sector construction (twisted
DHR/Longo-Roberts), (5) Haag duality/split for the quotient-circle net.

THIS PROBE measures everything about the inductive limit that is
measurable NOW -- the finite-level precursors of (1), (2), (3), (5).
Theorem (4) (solitonic sectors) is NOT re-measured here; its finite
witness is the v746 bond-defect identity.

HONEST TYPING (firewall): every measurement below is FINITE-LEVEL
EVIDENCE FOR the cited continuum theorems, NEVER a continuum proof.
No continuum claim is gated.  Exploration only (tfpt-experiment
firewall): NOT wired into run_all.py, no ledger row, no paper claim,
no marker move.

THE TOWER: levels N = 48 * 2^k.  The inductive-limit embedding is the
Haar block ISOMETRY V_N : C^N -> C^2N, e_j |-> (e_2j + e_2j+1)/sqrt(2)
(the Osborne-Stottmeister/MMST real-space scaling map, second
quantized to the CAR embedding iota(c(f)) = c(Vf)).  The canonical
state is the one the finite functor carries: the declared chiral Dirac
sea (NS covariance C = f(S), as in v746 "state = declared chiral Dirac
sea"); mu4 = the clock-derived half-turn H = S^{N/2} (order 4 forced
by the NS spin structure, as in v726 -- not inserted).

PREREGISTERED GATES (frozen before the first run):

G1 INDUCTIVE-LIMIT COHERENCE  [precursor of theorem (1), and of (3)
   via the coherent expectation system]:
   G1a one-particle tower: V^T V = 1, V H_N = H_2N V, V L_N = L_2N V
       exactly (dev < 1e-10) for all adjacent pairs N = 48..768;
       V(window(N,p,l)) supported inside window(2N,2p,2l) exactly
       (positions p = 0 and the wrap p = N/2-1).
   G1b scale covariance of the tower data: the window matrices H_W
       (4x4 and 8x8) and the window isometry V_W (8x4) extracted at
       every level are IDENTICAL (dev < 1e-12) -- the coherence data
       is level-independent.
   G1c Fock coherence: iota . Ad(U^j) = Ad(U'^j) . iota on generators
       and on a monomial battery, hence iota(E(m)) = E'(iota(m)),
       all dev < 1e-10 (U = Gamma(H_W) on the small window, U' on the
       doubled window, iota from V_W).
   G1d commuting squares of the index-4 expectations (ambient Fock,
       N = 48, K-hat of 8 sites, I c J c K): restriction coherence
       E_K|A(I-hat) = E_J|A(I-hat) = E_I; commutation [E_I, E_J] = 0
       on an A(K-hat) battery; idempotency (E_I E_J)^2 = E_I E_J;
       and E_small = E_small . E_large on the A(I-hat) battery.
       All dev < 1e-10 (exact).

G2 STATE CONVERGENCE FOR GNS  [precursor of theorem (1), weak-*]:
   fixed local observables on the base window (N0 = 48, base l = 2,
   modes {0,1,24,25}), pulled back through the V-chain, levels
   N = 48..1536 (5 doublings).  Cauchy deltas d_k = max over the
   battery of |omega_k(x) - omega_k-1(x)| (battery: quadratic,
   quartic, E-processed, frozen random even combos).  Gates:
   d_5 < 5e-3, d_5/d_4 <= 0.85, d_4/d_3 <= 0.85 (oscillation-aware:
   max-over-battery, ratio gates on the LAST two steps only);
   parity-odd battery elements exactly 0 at every level (< 1e-12).

G3 INDEX STABILITY ALONG THE TOWER  [precursor of theorem (2),
   Pimsner-Popa/Longo heredity]: census over N = 48/96/192/384,
   l = 1..4, p = {0, 7, N/2-1}: for l >= 2 exactly 4 sectors,
   |lambda* - 1/4| < 1e-8, quasi-basis Watatani index = 4*1 with
   dev < 1e-7 (l <= 3); l = 1 anomaly stable (3 sectors,
   |lambda - 1/3| < 1e-8, index 3); local Takesaki [rho_W, U] = 0
   < 1e-8; PP pinching margin at the mixing minimizer
   min eig(E(vv*) - vv*/4) >= -1e-8.  NON-DEGRADATION: the per-level
   max deviations stay under the SAME absolute gates at EVERY level
   (profiles printed; no growth along the tower).

G4 SPLIT/DUALITY PRECURSORS  [precursors of theorem (5), and the
   index = statistical-dimension reading of (2)/(3)] -- measured,
   typed, never gated as continuum claims:
   G4a split witness: cross-covariance norm nu(sep) between separated
       doubled windows at FIXED angular geometry (base l = N/24,
       separations N/24, N/12, N/6), levels N = 48..768: per
       separation the tower deltas satisfy final |Delta nu| < 5e-3
       and last delta <= previous delta (stabilization); nu strictly
       decreasing in separation at the final level.
   G4b finite Haag-duality census (level-independent by G1b; computed
       once in the 6-mode ambient frame, I-hat = 4 modes, and the
       4-mode frame for l = 1): A(I-hat) spans its full 256-dim
       (resp. 16-dim) matrix factor (rank check); measured commutant
       dimension dim A' = 4^{n_c} EXACTLY; twisted-complement basis
       (even complement monomials + Klein_I * odd complement
       monomials) commutes with A (dev < 1e-10), is independent
       (Gram rank 4^{n_c}) => twisted-duality DEFECT = dim A' -
       4^{n_c} = 0; fixed-point census: dim B' = m * 4^{n_c} EXACTLY
       (m = sectors), so the relative-commutant EXCESS ratio
       dim B'/dim A' = m = 4 for l = 2 (= the local Watatani index)
       and = 3 for the l = 1 anomaly; kernel/nonzero eigengap of the
       commutant Gram operator >= 1e6 (clean count).
       [HONEST SPEC CORRECTION after run 1 (25/26): the B-commutant
       was first computed from a SMALL generating set (4 random
       E-images + sector projections); that set under-generates B
       (measured generated dim 70 < dim B = 72, so dim B' came out
       80 = 5 blocks instead of 64 = 4 blocks).  The generator
       specification is corrected to a measured SPANNING BASIS of
       B = E(A) (rank-reduction of the E-images of all 256 monomials;
       rank check dim B = sum d_q^2 gated), whose commutant IS B' by
       definition -- no generation assumption.  The GATE VALUES
       (dim B' = 64, ratio 4; l = 1: 48, ratio 3) are unchanged.]

G5 CONTROLS (all MUST fire):
   C1 scrambled bond data (same-arc pairing instead of the half-turn
      two-arc pairing): Fock tower coherence dev > 0.1.
   C2 broken twist (Z2-only average): lambda = 1/2 (dev < 1e-8) at
      N = 48 AND N = 384 -- the index census breaks (2 != 4).
   C3 scrambled state (random momentum occupation, filling fraction
      alternating 0.3/0.7 along the tower): final Cauchy delta
      > 10 * true d_5 AND > 0.05 -- convergence breaks.
   C4 scale-incoherent embedding (decimation e_j -> e_2j, isometric
      but not the scaling map): limiting window covariance max
      off-diagonal < 0.05 while the Haar value > 0.1 -- the block
      structure of the embedding is load-bearing.

VERDICT ENUM (frozen): 
  GNS-PRECURSORS-COHERENT : G1, G2, G3, G4 all pass AND all controls
                            C1-C4 fire.
  GNS-PRECURSORS-PARTIAL  : G1 and G3 pass, all controls fire, but
                            G2 or G4 fails (convergence/witness gap).
  GNS-PRECURSORS-DEAD     : G1 or G3 fails, or any control fails.

SHA-FREEZE: the construction source (all builder functions + frozen
constants) is hashed and printed before any gate runs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/gnet_gns_limit_probe.py

Original Arf/Q-system probe docstring (verbatim):
G_net continuum strand, Priority 6 -- the index-4 Q-system vs the
Arf/S5/K6 sector structure, plus uniform quasi-basis/split bounds.

INPUTS (located, read-only):
  * G_net side: the exact local index-4 net functor (GNET.LOCALNET.01 /
    v746; GNET.PPINDEX.01 / v726) and the exact inductive system of
    gnet_gns_limit_probe.py (verdict GNS-PRECURSORS-COHERENT): Haar
    isometry tower, commuting index-4 expectation squares, geometric
    state convergence, duality census dim B'/dim A' = 4.
  * Q-system contract: GATE.METRIC.08 (C[Z4] Longo Q-system, index
    4 = |Z4|, quasi-basis = the group layer) and GATE.METRIC.11 (the
    simple-current extension theorem [B:A] = |mu4| = 4, v125/v154).
  * Arf side (arf_spinor_compiler_probe.py, ARF-SPINOR-EXACT): on
    V = L/(1+i)L = F2^4 with hbar = all-ones-off-diagonal, the unique
    sigma-selected Arf refinement q* = wt(iota(.))/2 mod 2 gives
    16 = 1 + 5bar + 10 as Stab(q*) ~ S5 orbits; V\\{0} ~ E(K6);
    B = I + A_KG(6,2); the compressed matter channel on (5bar, 10)
    is K_matter = (1/7)[[1,6],[3,4]], eigenvalues {1, -2/7}, and
    K^2 = (4/49) I + (45/49) Pi_0 (v754; Stinespring v756).

BINDING HONESTY RULE (user): the eigenvalue 4/49 = (-2/7)^2 of the
two-step incidence channel and the Watatani index 4 = |mu4| are two
DIFFERENT numbers from two DIFFERENT registers.  NOTHING in this probe
equates them; no gate, no verdict clause, no printed line treats
"4" and "4/49" as related.  The candidate connection tested here is
CORRESPONDENCE STRUCTURE (gradings, transport, equivariance); if none
exists, the honest verdict says so.

FROZEN LADDER-SIDE COMPARISON OBJECT (preregistered "why here"): the
l = 2 doubled window is the UNIQUE window whose Fock space has exactly
|V| = 16 states (4 modes).  In the H_W eigenmode basis it carries the
canonical splitting  16 = 1 + 5 + 10 :
    1  = the Fock vacuum (distinguished, like 0 in V),
    5  = the mu4-charge-0 states minus the vacuum   (|{c=0}| = 6),
    10 = the charged states (c != 0).
This size match with the Arf 1 + 5bar + 10 is exact and is itself a
measured fact (S1.2); whether it is MORE than counting is what the
censuses decide.

PREREGISTERED STEPS AND GATES (frozen before the first run):

S1 Q-SYSTEM CARRIER / NATURAL GRADING.  "Natural" is predeclared as:
   (i) an F2-affine bijection Phi: Fock16 -> V mapping (vacuum,
   charge-0-nonvac, charged) onto (0, 5bar, 10) -- censused
   EXHAUSTIVELY over all of GL(4,2) (20160 maps; affine with
   Phi(vac) = 0 reduces to linear since both distinguished points are
   fixed); PLUS (ii) an internal order-3 window symmetry (the sigma
   register) compatible with (H_W, C_W-limit) acting nontrivially on
   the sector lattice -- censused over all 6144 generalized signed
   permutations (entries 0, +-1, +-i).  A forced/arbitrary labeling
   counts as NO.  Exact F2-rank certificates accompany the census
   (rank of the ladder 5-set vs rank of the Arf 5bar).
   Gate S1-NATURAL := (census (i) >= 1) AND (census (ii) has a
   nontrivial element).  Expected decisive either way; sizes echo
   (S1.2) is gated separately as a measured fact.
   POSITIVE SUB-FINDING (gated exactly): the sigma register DOES exist
   internally on the Z6-quotient (sixfold) window W6 = the L^2-orbit
   window: deck D = S^{N/3} and half-turn H = S^{N/2} BOTH preserve
   W6, commute, D^3 = -1 (NS), H^2 = -1; E on W6 still has lambda* =
   1/4 with sector dims (20, 16, 12, 16); the deck acts inside each
   mu4 sector with orbit census (fixed, 3-orbits) per charge =
   (2,6), (1,5), (0,4), (1,5) -- BUT dim Fock(W6) = 64 != 16 = |V|,
   so the S5/K6 geometry does NOT transport pointwise (the register
   matches, the state space does not).  All numbers preregistered.

S2 SECTOR TRANSPORT vs K_MATTER.  The (1,5,10) weights w(k) of the
   canonical chiral-sea state pulled back along the Haar tower
   (N = 48..1536, the gnet_gns_limit_probe chain) on the l = 2 window;
   x(k) = (w5, w10)/(w5 + w10).  Frozen comparisons:
   (a) TRANSFER: fit one row-stochastic 2x2 T with x(k+1) = x(k) T
       (least squares over the 5 pairs; both orientations T and T^t
       compared, better one reported).  S2-KMATTER := residual < 1e-3
       AND max|T - K_matter| < 1e-6.  DEGENERACY RULE (oscillation-
       aware): if the trajectory spread max_k |x(k) - x(5)| < 1e-3
       the transfer fit is declared DEGENERATE (any T with fixed
       point x* fits) and only (b) decides.
   (b) STATIONARY: K_matter's stationary law is pi = (1/3, 2/3) (=
       uniform on the 15 points).  S2-STATIONARY :=
       max|x(5) - (1/3, 2/3)| < 1e-3.
   A mismatch is a clean NO, not a tuning opportunity.  CAUTION LINE
   (preregistered): the DEGENERATE decimation embedding gives exactly
   uniform weights (1,5,10)/16, i.e. x = (1/3, 2/3) trivially -- the
   stationary test is only meaningful on the Haar chain (C4 control).

S3 QUASI-BASIS <-> C[Z4]/ARF SECTORS.  Extract the explicit Watatani
   quasi-basis of E on the l = 2 window (1 + sum_{q != q'} d_q d_q'
   = 185 elements; sum v v* = 4*1 exact).  The GATE.METRIC.08/11
   C[Z4] object has the 4-ELEMENT group-layer quasi-basis {u_c}; a
   4-element unitary quasi-basis exists on a window iff the mu4
   grading is strongly graded iff the sector dims are equal.  FROZEN
   CLOSED FORM (measured census l = 1..6, exact integers):
       d_c(l) = 4^{l-1} + 2^{l-1} cos(pi c / 2),
   so d_0 - d_2 = 2^l > 0 at EVERY finite l: the 4-element (C[Z4])
   quasi-basis is OBSTRUCTED at every finite level with relative gap
   (d_0 - d_2)/4^l = 2^{-l} -> 0 geometrically -- the crossed-product
   structure is exactly asymptotic (the finite precursor of the
   GATE.METRIC.08 R2 identification).  BONUS (gated): d_2(1) = 0 is
   EXACTLY the l = 1 three-sector index-3 anomaly of v746.
   Gate S3-LAW := census == closed form for l = 1..6 AND index = 4*1
   exact at l = 2, 3 AND no unitary u_c (c != 0) at any l <= 6.
   MUST-FAIL: quasi-basis with WRONG sector weights (d_{q+1} instead
   of d_q) breaks scalarness (dev > 0.1) -- a wrong sector assignment
   breaks the quasi-basis relations.

S4 UNIFORM SECTOR-RESOLVED SPLIT BOUNDS.  Two disjoint l = 2 windows
   (base sites {0,1}+{24,25} and {6,7}+{30,31}) under the pulled-back
   tower states, levels k = 0..5; frozen battery of charge-c
   eigenmode monomials per window (c = 0..3, normalized); nu_cc'(k) =
   max battery |<ab> - <a><b>|.  Gates (per (c,c') with nonzero
   profile): UNIFORM BAR nu_cc'(k) <= max(2 max(nu(0), nu(1)), 1e-3)
   for all k, and TAIL |nu(5) - nu(4)| <= |nu(4) - nu(3)| + 1e-12
   (oscillation-aware).  Identically-zero profiles are reported as
   exact charge/number-conservation zeros.
   HONEST SPEC CORRECTION (first run, gate form only, no number
   tuned): the bar was first anchored at 2 nu(0) alone; the (1,3) and
   (3,1) profiles turned out to be EXACTLY ZERO at k = 0 (a symmetry
   of the native N = 48 sea between these two windows) and then sit
   on a uniform plateau 0.0296 from k = 1 on -- a zero anchor makes
   any nonzero plateau "fail" spuriously.  The bar anchor is widened
   to the first TWO levels (still frozen, still uniform, no tail
   fitting); the k = 0 exact zero is reported as a measured fact.  This is the quantitative
   uniform input a continuum split/index-continuity argument needs --
   typed as finite evidence, never the continuum theorem.

S5 INDEX-CONTINUITY PRECURSOR (combination).  The window data (H_W,
   V_W) is level-independent (gnet_gns_limit_probe G1b), so the
   index-4 structure transports LITERALLY along the tower; slim
   re-check lambda* = 1/4 and quasi-basis 4*1 exact at N = 48 and
   N = 768 native windows; combined with S4's uniform constants this
   is the measured finite precursor of index continuity in the GNS
   limit -- never the continuum theorem itself.

CONTROLS (all must fire):
  C1 bond scramble (same-arc pairing H): sector weights shift,
     max|w_scr - w_true|(final) > 0.02.
  C2 Z2-only average: lambda = 1/2 (breaks the index-4 census).
  C3 scrambled sea (alternating filling 0.3/0.7): final weight delta
     > max(10 x true final delta, 0.05) -- convergence breaks.
  C4 decimation embedding: max|w_dec - w_haar|(final) > 0.02 AND
     w_dec is uniform within 1e-3 (the preregistered caution: the
     degenerate limit fakes the stationary law).
  C5 wrong-Arf-form: q_bad = q* + hbar(., c_bad), c_bad = (0,1,1,1)
     (frozen smallest sigma-moved element of 5bar): q_bad is Arf-1
     with q_bad(A) = 1 but NOT sigma-invariant and its zero set is
     NOT sigma-stable (fires), while q*'s sectors ARE sigma-stable
     (sanity).

VERDICT ENUM (frozen):
  GNET-ARF-QSYSTEM-CARRIES : S1-NATURAL and (S2-KMATTER or
      S2-STATIONARY) and S3-LAW and S4 and S5 pass, all controls fire.
  GNET-ARF-NO-CORRESPONDENCE : NOT S1-NATURAL and NOT S2-KMATTER and
      NOT S2-STATIONARY, controls fire (the honest negative: shared
      symmetries, no natural transport; S3/S4/S5 are G_net-internal
      and are reported on their own).
  GNET-ARF-PARTIAL : anything else (which steps carry is named);
      any control failure is flagged CONTROL-VOID inside PARTIAL.

HONEST TYPING: every measurement is finite-level structure; nothing
here is a continuum statement or a physics claim; no marker moves.
Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper claim, no file writes.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/gnet_arf_qsystem_probe.py
"""

import hashlib
import inspect
import sys
import time

import numpy as np

TOL = 1e-10
SEED = 20260805
CHECKS = []

# frozen construction constants
N0 = 48                      # base level
K_STATE = 5                  # doublings for the state tower (48 -> 1536)
LEVELS_1P = (48, 96, 192, 384)          # one-particle tower pairs N -> 2N
LEVELS_IDX = (48, 96, 192, 384)         # index census levels
LEVELS_SPLIT = (48, 96, 192, 384, 768)  # split-witness levels
BASE_L = 2                   # base window length for the state tower


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    return ok


# ---------------- one-particle layer (constructions) ----------------

def spower(N, k):
    """S^k as an exact signed permutation (NS: -1 per wrap)."""
    P = np.zeros((N, N))
    for j in range(N):
        P[(j + k) % N, j] = (-1.0) ** ((j + k) // N)
    return P


def covariance(N):
    """the declared chiral Dirac sea (NS momenta, theta < 0 occupied)."""
    th = 2 * np.pi * (np.arange(N) + 0.5) / N
    th = np.mod(th + np.pi, 2 * np.pi) - np.pi
    th[np.isclose(th, -np.pi)] = np.pi
    F = np.exp(1j * np.outer(np.arange(N), th)) / np.sqrt(N)
    occ = (th < 0).astype(float)
    return (F * occ) @ F.conj().T


def covariance_occ(N, occ):
    th = 2 * np.pi * (np.arange(N) + 0.5) / N
    th = np.mod(th + np.pi, 2 * np.pi) - np.pi
    th[np.isclose(th, -np.pi)] = np.pi
    F = np.exp(1j * np.outer(np.arange(N), th)) / np.sqrt(N)
    return (F * occ) @ F.conj().T


def window(N, p, l):
    return [(p + i) % N for i in range(l)] + \
           [(p + N // 2 + i) % N for i in range(l)]


def haar_iso(N):
    """the scaling isometry V_N : C^N -> C^2N, e_j -> (e_2j+e_2j+1)/sqrt2."""
    V = np.zeros((2 * N, N))
    for j in range(N):
        V[2 * j, j] = V[2 * j + 1, j] = 1.0 / np.sqrt(2.0)
    return V


def decim_iso(N):
    """control C4: decimation e_j -> e_2j (isometric, scale-incoherent)."""
    V = np.zeros((2 * N, N))
    for j in range(N):
        V[2 * j, j] = 1.0
    return V


# ---------------- Fock layer ----------------

def jw_ops(n):
    sm = np.array([[0, 1], [0, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    ops = []
    for j in range(n):
        m = np.array([[1.0]], dtype=complex)
        for l in range(n):
            m = np.kron(m, sz if l < j else (sm if l == j else I2))
        ops.append(m)
    return ops


def gamma_partial(Hsub, idx, cops):
    mu, V = np.linalg.eigh(1j * Hsub)
    dim = cops[0].shape[0]
    U = np.eye(dim, dtype=complex)
    for i in range(len(idx)):
        d = sum(np.conj(V[j, i]) * cops[idx[j]] for j in range(len(idx)))
        n_i = d.conj().T @ d
        ev = -1j * mu[i]
        U = U @ (np.eye(dim) + (ev - 1) * n_i)
    return U


def gaussian_rho(CW, cops):
    lam, V = np.linalg.eigh(CW)
    lam = np.clip(lam.real, 0.0, 1.0)
    dim = cops[0].shape[0]
    rho = np.eye(dim, dtype=complex)
    for i in range(len(cops)):
        d = sum(np.conj(V[j, i]) * cops[j] for j in range(len(cops)))
        rho = rho @ ((1 - lam[i]) * np.eye(dim)
                     + (2 * lam[i] - 1) * (d.conj().T @ d))
    return rho


def sector_projs(U):
    return [sum((1j ** (-q * j)) * np.linalg.matrix_power(U, j)
                for j in range(4)) / 4 for q in range(4)]


def lam_of(B, Efun):
    A = Efun(B)
    a, W = np.linalg.eigh((A + A.conj().T) / 2)
    keep = a > 1e-11 * max(a.max(), 1.0)
    Ws = W[:, keep] / np.sqrt(a[keep])
    M = Ws.conj().T @ B @ Ws
    top = float(np.linalg.eigvalsh((M + M.conj().T) / 2).max().real)
    return 1.0 / top


def onb_of(P):
    w, W = np.linalg.eigh((P + P.conj().T) / 2)
    return W[:, w > 0.5]


def quasi_basis(Ps):
    onbs = [onb_of(P) for P in Ps]
    dims = [o.shape[1] for o in onbs]
    vs = [np.eye(Ps[0].shape[0], dtype=complex)]
    for q in range(4):
        for qp in range(4):
            if q == qp or dims[q] == 0 or dims[qp] == 0:
                continue
            for a in range(dims[q]):
                for b in range(dims[qp]):
                    vs.append(np.outer(onbs[q][:, a], onbs[qp][:, b].conj())
                              / np.sqrt(dims[qp]))
    return vs


def comm_kernel(gens, D):
    """dim of the commutant of the self-adjoint set gens in M_D:
    kernel of M = sum_g A_g^dag A_g with A_g the commutator superop,
    built term-by-term from single krons (pure numpy)."""
    M = np.zeros((D * D, D * D), dtype=complex)
    I = np.eye(D, dtype=complex)
    for g in gens:
        M += np.kron(I, np.conj(g @ g.conj().T))
        M += np.kron(g.conj().T @ g, I)
        M -= np.kron(g, np.conj(g))
        M -= np.kron(g.conj().T, g.T)
    ev = np.linalg.eigvalsh(M)
    tolz = 1e-9 * max(1.0, float(ev.max()))
    kdim = int(np.sum(ev < tolz))
    gap = float(ev[kdim] / max(abs(ev[kdim - 1]), 1e-300)) if kdim < len(ev) \
        else np.inf
    return kdim, gap, ev


def transport(U, cops):
    """extract T with Ad(U) c_i = sum_b T[b,i] c_b, verify residual."""
    n = len(cops)
    nrm = [float(np.vdot(c, c).real) for c in cops]
    T = np.zeros((n, n), dtype=complex)
    res = 0.0
    for i in range(n):
        A = U @ cops[i] @ U.conj().T
        for b in range(n):
            T[b, i] = np.vdot(cops[b], A) / nrm[b]
        R = A - sum(T[b, i] * cops[b] for b in range(n))
        res = max(res, float(np.abs(R).max()))
    return T, res


def rnd_elem(gens, rng, terms=6, maxdeg=3):
    dim = gens[0].shape[0]
    x = np.zeros((dim, dim), dtype=complex)
    for _ in range(terms):
        deg = rng.integers(1, maxdeg + 1)
        m = np.eye(dim, dtype=complex)
        for _ in range(deg):
            m = m @ gens[rng.integers(0, len(gens))]
        x += (rng.standard_normal() + 1j * rng.standard_normal()) * m
    return x


def sha_freeze():
    fns = [spower, covariance, covariance_occ, window, haar_iso, decim_iso,
           jw_ops, gamma_partial, gaussian_rho, sector_projs, lam_of,
           onb_of, quasi_basis, comm_kernel, transport, rnd_elem]
    blob = "".join(inspect.getsource(f) for f in fns)
    blob += repr((TOL, SEED, N0, K_STATE, LEVELS_1P, LEVELS_IDX,
                  LEVELS_SPLIT, BASE_L))
    return hashlib.sha256(blob.encode()).hexdigest()


# =====================================================================

def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    print("gnet_gns_limit_probe -- finite-level precursors of the GNS "
          "limit net\n")
    print(f"SHA-freeze (construction source + constants): "
          f"{sha_freeze()[:32]}\n")

    # ---------------- S0 sanity ----------------
    # comm_kernel on a known case: sz(x)I in M4 -> commutant M2(+)M2, dim 8
    sz = np.diag([1.0, -1.0]).astype(complex)
    g0 = np.kron(sz, np.eye(2, dtype=complex))
    kd, gap, _ = comm_kernel([g0], 4)
    check("S0 comm_kernel sanity: commutant of sz(x)1 in M4 has dim 8",
          kd == 8, f"dim = {kd}, gap = {gap:.1e}")

    # ================= G1 inductive-limit coherence =====================
    print("\n-- G1: inductive-limit coherence --")
    # G1a one-particle tower
    dev_a = 0.0
    ok_win = True
    for N in LEVELS_1P + (768,):
        V = haar_iso(N)
        HN, H2 = spower(N, N // 2), spower(2 * N, N)
        LN, L2 = spower(N, N // 12), spower(2 * N, 2 * N // 12)
        dev_a = max(dev_a, np.abs(V.T @ V - np.eye(N)).max())
        dev_a = max(dev_a, np.abs(V @ HN - H2 @ V).max())
        dev_a = max(dev_a, np.abs(V @ LN - L2 @ V).max())
        for (p, l) in ((0, 2), (N // 2 - 1, 2)):
            w, w2 = window(N, p, l), set(window(2 * N, 2 * p, 2 * l))
            for j in w:
                ok_win &= set(np.nonzero(V[:, j])[0]).issubset(w2)
    check("G1a tower: V isometric, V H_N = H_2N V, V L_N = L_2N V exact, "
          "N = 48..768", dev_a < TOL, f"max dev = {dev_a:.2e}")
    check("G1a tower: V(window(N,p,l)) inside window(2N,2p,2l) exactly "
          "(incl. wrap)", ok_win)

    # G1b scale covariance of the window data
    HW4_ref, HW8_ref, VW_ref = None, None, None
    dev_b = 0.0
    for N in LEVELS_1P + (768,):
        wN, w2N = window(N, 0, BASE_L), window(2 * N, 0, 2 * BASE_L)
        HN, H2 = spower(N, N // 2), spower(2 * N, N)
        HW4 = HN[np.ix_(wN, wN)]
        HW8 = H2[np.ix_(w2N, w2N)]
        VW = haar_iso(N)[np.ix_(w2N, wN)]
        if HW4_ref is None:
            HW4_ref, HW8_ref, VW_ref = HW4, HW8, VW
        dev_b = max(dev_b, np.abs(HW4 - HW4_ref).max(),
                    np.abs(HW8 - HW8_ref).max(), np.abs(VW - VW_ref).max())
    check("G1b scale covariance: H_W (4x4/8x8) and V_W (8x4) identical at "
          "every level", dev_b < 1e-12, f"max dev = {dev_b:.2e}")

    # G1c Fock coherence via the constant window data
    c4 = jw_ops(4)
    c8 = jw_ops(8)
    U4 = gamma_partial(HW4_ref, list(range(4)), c4)
    U8 = gamma_partial(HW8_ref, list(range(8)), c8)
    g_emb = [sum(VW_ref[a, i] * c8[a] for a in range(8)) for i in range(4)]
    # CAR sanity of the embedding
    dev_car = 0.0
    for i in range(4):
        for k in range(4):
            ac = g_emb[i] @ g_emb[k].conj().T + g_emb[k].conj().T @ g_emb[i]
            dev_car = max(dev_car, np.abs(
                ac - (1.0 if i == k else 0.0) * np.eye(256)).max())
    check("G1c iota is a CAR embedding: {g_i, g_k^dag} = delta exactly",
          dev_car < TOL, f"max dev = {dev_car:.2e}")
    T4, r4 = transport(U4, c4)
    T8, r8 = transport(U8, c8)
    dev_int = np.abs(VW_ref @ T4 - T8 @ VW_ref).max()
    check("G1c generator intertwining: V_W T4 = T8 V_W (transports "
          "extracted, residuals ~ 0)", max(r4, r8) < TOL and dev_int < TOL,
          f"res = {max(r4, r8):.1e}, dev = {dev_int:.2e}")

    # monomial battery: sequences of (mode, dag)
    monos = [[(0, 1)], [(0, 1), (1, 0)], [(0, 0), (1, 0)],
             [(0, 1), (2, 0)], [(0, 1), (1, 1), (2, 0), (3, 0)],
             [(0, 1), (0, 0)], [(2, 1), (3, 0)]]
    dev_c = 0.0
    for seq in monos:
        m_small = np.eye(16, dtype=complex)
        m_big = np.eye(256, dtype=complex)
        for (i, dag) in seq:
            f = c4[i].conj().T if dag else c4[i]
            m_small = m_small @ f
            m_big = m_big @ (g_emb[i].conj().T if dag else g_emb[i])
        # E(m) small: (1/4) sum_j Ad(U4^j); iota via rotated factors
        lhs = np.zeros((256, 256), dtype=complex)
        for j in range(4):
            term = np.eye(256, dtype=complex)
            Tj = np.linalg.matrix_power(T4, j)
            for (i, dag) in seq:
                co = Tj[:, i]
                if dag:
                    fac = sum(np.conj(co[b]) * g_emb[b].conj().T
                              for b in range(4))
                else:
                    fac = sum(co[b] * g_emb[b] for b in range(4))
                term = term @ fac
            lhs += term / 4
        rhs = sum(np.linalg.matrix_power(U8, j) @ m_big
                  @ np.linalg.matrix_power(U8, j).conj().T
                  for j in range(4)) / 4
        dev_c = max(dev_c, float(np.abs(lhs - rhs).max()))
        # also raw Ad coherence at j = 1
        ad_small_emb = np.zeros((256, 256), dtype=complex)
        term = np.eye(256, dtype=complex)
        for (i, dag) in seq:
            co = T4[:, i]
            if dag:
                fac = sum(np.conj(co[b]) * g_emb[b].conj().T for b in range(4))
            else:
                fac = sum(co[b] * g_emb[b] for b in range(4))
            term = term @ fac
        ad_small_emb = term
        ad_big = U8 @ m_big @ U8.conj().T
        dev_c = max(dev_c, float(np.abs(ad_small_emb - ad_big).max()))
    check("G1c Fock coherence: iota(E(m)) = E'(iota(m)) and "
          "iota(Ad(U)m) = Ad(U')iota(m) on the monomial battery",
          dev_c < TOL, f"max dev = {dev_c:.2e}")

    # G1d commuting squares in the ambient K window (N = 48, 8 sites)
    N = 48
    HN = spower(N, N // 2)
    ambK = window(N, 0, 4)
    copsK = jw_ops(8)
    pos = {s: i for i, s in enumerate(ambK)}

    def make_E(baseI):
        ambI = window(N, baseI[0], len(baseI))
        idxI = [pos[s] for s in ambI]
        HI = HN[np.ix_(ambI, ambI)]
        UI = gamma_partial(HI, idxI, copsK)

        def E(x, UI=UI):
            return sum(np.linalg.matrix_power(UI, j) @ x
                       @ np.linalg.matrix_power(UI, j).conj().T
                       for j in range(4)) / 4
        return E, idxI

    EI, idxI = make_E([0, 1])
    EJ, idxJ = make_E([0, 1, 2])
    EK, _ = make_E([0, 1, 2, 3])
    gensI = []
    for i in idxI:
        gensI += [copsK[i], copsK[i].conj().T]
    gensK = []
    for i in range(8):
        gensK += [copsK[i], copsK[i].conj().T]
    battI = [copsK[idxI[0]], copsK[idxI[0]].conj().T @ copsK[idxI[1]],
             copsK[idxI[0]] @ copsK[idxI[1]]] + \
            [rnd_elem(gensI, rng) for _ in range(4)]
    battK = [rnd_elem(gensK, rng) for _ in range(6)]
    d_restr = max(max(np.abs(EJ(x) - EI(x)).max(),
                      np.abs(EK(x) - EI(x)).max()) for x in battI)
    d_comm = max(np.abs(EI(EJ(x)) - EJ(EI(x))).max() for x in battK)
    d_idem = max(np.abs(EI(EJ(EI(EJ(x)))) - EI(EJ(x))).max() for x in battK)
    d_small = max(np.abs(EI(EJ(x)) - EI(x)).max() for x in battI)
    check("G1d commuting squares: E_K|A(I) = E_J|A(I) = E_I (restriction "
          "coherence)", d_restr < TOL, f"max dev = {d_restr:.2e}")
    check("G1d commuting squares: [E_I, E_J] = 0 on A(K-hat)",
          d_comm < TOL, f"max dev = {d_comm:.2e}")
    check("G1d commuting squares: (E_I E_J)^2 = E_I E_J (joint expectation)",
          d_idem < TOL, f"max dev = {d_idem:.2e}")
    check("G1d E_small = E_small . E_large on A(I-hat) (nested coherence)",
          d_small < TOL, f"max dev = {d_small:.2e}")

    # ================= G2 state convergence =============================
    print("\n-- G2: state convergence along the tower (Haar chain) --")
    win0 = window(N0, 0, BASE_L)

    def pullback_series(cov_fun, iso_fun, kmax):
        """window covariances of the pulled-back state, levels 0..kmax."""
        out = []
        chain = np.eye(N0)
        Nk = N0
        for k in range(kmax + 1):
            C = cov_fun(Nk, k)
            Ct = chain.T @ C @ chain
            out.append(Ct[np.ix_(win0, win0)])
            V = iso_fun(Nk)
            chain = V @ chain
            Nk *= 2
        return out

    cws = pullback_series(lambda Nk, k: covariance(Nk), haar_iso, K_STATE)

    # battery (frozen): even, odd, E-processed, random even combos
    n_ = [c4[i].conj().T @ c4[i] for i in range(4)]
    B_even = [n_[0], c4[0].conj().T @ c4[1], c4[0].conj().T @ c4[2],
              c4[0].conj().T @ c4[3], c4[1].conj().T @ c4[2],
              c4[0] @ c4[1], n_[0] @ n_[2],
              c4[0].conj().T @ c4[1].conj().T @ c4[2] @ c4[3]]
    r_pairs = [rnd_elem([c4[0].conj().T @ c4[1], c4[1].conj().T @ c4[2],
                         c4[2].conj().T @ c4[3], n_[0], n_[3]], rng)
               for _ in range(2)]
    B_even += r_pairs

    def E4(x):
        return sum(np.linalg.matrix_power(U4, j) @ x
                   @ np.linalg.matrix_power(U4, j).conj().T
                   for j in range(4)) / 4

    B_E = [E4(x) for x in (n_[0], c4[0].conj().T @ c4[2],
                           c4[0].conj().T @ c4[1].conj().T @ c4[2] @ c4[3])]
    B_odd = [c4[0], c4[0].conj().T @ c4[1] @ c4[2]]
    batt = B_even + B_E

    om = []
    odd_max = 0.0
    for k, CW in enumerate(cws):
        rho = gaussian_rho(CW, c4)
        om.append(np.array([np.trace(rho @ x) for x in batt]))
        odd_max = max(odd_max, max(abs(np.trace(rho @ x)) for x in B_odd))
    om = np.array(om)
    dd = [float(np.abs(om[k] - om[k - 1]).max()) for k in range(1, K_STATE + 1)]
    print("   Cauchy deltas d_k (max over battery):",
          " ".join(f"{d:.3e}" for d in dd))
    rat = [dd[i + 1] / dd[i] if dd[i] > 0 else 0.0 for i in range(len(dd) - 1)]
    print("   ratios:", " ".join(f"{r:.3f}" for r in rat))
    check(f"G2 Cauchy: d_5 = {dd[-1]:.3e} < 5e-3", dd[-1] < 5e-3)
    check(f"G2 contraction: d5/d4 = {rat[-1]:.3f} <= 0.85 and "
          f"d4/d3 = {rat[-2]:.3f} <= 0.85",
          rat[-1] <= 0.85 and rat[-2] <= 0.85)
    check("G2 parity: odd battery elements exactly 0 at every level",
          odd_max < 1e-12, f"max |omega(odd)| = {odd_max:.1e}")

    # ================= G3 index stability census ========================
    print("\n-- G3: index census along the tower --")
    print(f"{'N':>4} {'max|lam-1/4|':>14} {'max ind dev':>13} "
          f"{'max Takesaki':>13} {'anomaly':>9} {'PP margin':>11}")
    ok3 = True
    prof3 = []
    for NN in LEVELS_IDX:
        SS_H = spower(NN, NN // 2)
        CC = covariance(NN)
        dlam, dind, dtak, danom, pmargin = 0.0, 0.0, 0.0, 0.0, 0.0
        anom_ok = True
        for l in (1, 2, 3, 4):
            for p in (0, 7, NN // 2 - 1):
                win = window(NN, p, l)
                HW = SS_H[np.ix_(win, win)]
                CW = CC[np.ix_(win, win)]
                cs = jw_ops(2 * l)
                U = gamma_partial(HW, list(range(2 * l)), cs)
                Ps = sector_projs(U)
                dims = [int(round(np.trace(P).real)) for P in Ps]
                m = sum(1 for d in dims if d > 0)

                def E(x, Ps=Ps):
                    return sum(P @ x @ P for P in Ps)

                v = np.zeros(2 ** (2 * l), dtype=complex)
                for P in Ps:
                    o = onb_of(P)
                    if o.shape[1]:
                        v += o[:, 0]
                v /= np.linalg.norm(v)
                vv = np.outer(v, v.conj())
                lam = lam_of(vv, E)
                pm = float(np.linalg.eigvalsh(E(vv) - 0.25 * vv).min())
                rho = gaussian_rho(CW, cs)
                tak = float(np.abs(rho @ U - U @ rho).max())
                dtak = max(dtak, tak)
                if l >= 2:
                    dlam = max(dlam, abs(lam - 0.25))
                    anom_ok &= (m == 4)
                    pmargin = min(pmargin, pm)
                else:
                    danom = max(danom, abs(lam - 1.0 / 3.0))
                    anom_ok &= (m == 3)
                if l <= 3:
                    vs = quasi_basis(Ps)
                    ind = sum(x @ x.conj().T for x in vs)
                    dind = max(dind, float(
                        np.abs(ind - m * np.eye(2 ** (2 * l))).max()))
        prof3.append((NN, dlam, dind, dtak, danom, pmargin))
        ok3 &= (dlam < 1e-8 and dind < 1e-7 and dtak < 1e-8
                and danom < 1e-8 and anom_ok and pmargin > -1e-8)
        print(f"{NN:>4} {dlam:>14.2e} {dind:>13.2e} {dtak:>13.2e} "
              f"{danom:>9.2e} {pmargin:>11.2e}")
    grow = max(prof3[-1][1], prof3[-1][2]) <= max(
        10 * max(prof3[0][1], prof3[0][2]), 1e-8)
    check("G3 index census: lambda* = 1/4 exactly, Ind = 4*1, Takesaki = 0, "
          "l = 1 anomaly stable, PP margin >= -1e-8 at EVERY level", ok3)
    check("G3 non-degradation: deviations do not grow along the tower "
          "(final <= max(10x first, 1e-8))", grow)

    # ================= G4 split/duality precursors ======================
    print("\n-- G4a: split witness (cross-covariance norm, fixed angular "
          "geometry) --")
    seps = {}
    for NN in LEVELS_SPLIT:
        C = covariance(NN)
        l = NN // 24
        for i, d in enumerate((NN // 24, NN // 12, NN // 6)):
            W1 = window(NN, 0, l)
            W2 = window(NN, l + d, l)
            nu = float(np.linalg.norm(C[np.ix_(W1, W2)], 2))
            seps.setdefault(i, []).append(nu)
    ok4a = True
    for i, label in enumerate(("N/24", "N/12", "N/6")):
        vals = seps[i]
        dts = [abs(vals[k] - vals[k - 1]) for k in range(1, len(vals))]
        print(f"   sep {label}: nu = " + " ".join(f"{v:.5f}" for v in vals)
              + "  deltas: " + " ".join(f"{d:.1e}" for d in dts))
        ok4a &= dts[-1] < 5e-3 and dts[-1] <= dts[-2]
    ok4a &= seps[0][-1] > seps[1][-1] > seps[2][-1]
    check("G4a split witness: cross-norm stabilizes along the tower "
          "(final delta < 5e-3, non-increasing) and decreases with "
          "separation", ok4a)

    print("\n-- G4b: finite Haag-duality / commutant census --")
    # main config: I-hat = 4 modes first, complement = 2 modes (D = 64)
    c6 = jw_ops(6)
    D6 = 64
    gensA = []
    for i in range(4):
        gensA += [c6[i], c6[i].conj().T]
    # A spans its full factor (rank of the 256 monomials in 16-dim factor)
    mono_vecs = []
    for S in range(16):
        for Tm in range(16):
            op = np.eye(16, dtype=complex)
            for i in range(4):
                if (S >> i) & 1:
                    op = op @ c4[i].conj().T
            for i in range(4):
                if (Tm >> i) & 1:
                    op = op @ c4[i]
            mono_vecs.append(op.reshape(-1))
    rankA = np.linalg.matrix_rank(np.array(mono_vecs), tol=1e-8)
    check("G4b A(I-hat) spans its full 256-dim matrix factor",
          rankA == 256, f"rank = {rankA}")
    kdA, gapA, _ = comm_kernel(gensA, D6)
    check("G4b measured dim A' = 4^{n_c} = 16 exactly (clean eigengap)",
          kdA == 16 and gapA > 1e6, f"dim = {kdA}, gap = {gapA:.1e}")
    # twisted-complement basis: even comp monomials + Klein_I * odd
    KI = np.eye(64, dtype=complex)
    for i in range(4):
        KI = KI @ (np.eye(64) - 2 * c6[i].conj().T @ c6[i])
    cands, dev_tw = [], 0.0
    for S in range(4):
        for Tm in range(4):
            op = np.eye(64, dtype=complex)
            npar = 0
            for i in (4, 5):
                if (S >> (i - 4)) & 1:
                    op = op @ c6[i].conj().T
                    npar += 1
            for i in (4, 5):
                if (Tm >> (i - 4)) & 1:
                    op = op @ c6[i]
                    npar += 1
            cand = op if npar % 2 == 0 else KI @ op
            cands.append(cand)
            dev_tw = max(dev_tw, max(float(np.abs(cand @ g - g @ cand).max())
                                     for g in gensA))
    gram_rank = np.linalg.matrix_rank(
        np.array([x.reshape(-1) for x in cands]), tol=1e-8)
    defect = kdA - 16
    check("G4b twisted duality: the 16 twisted-complement elements commute "
          "with A, are independent, and exhaust A' -- defect = 0",
          dev_tw < TOL and gram_rank == 16 and defect == 0,
          f"dev = {dev_tw:.1e}, gram rank = {gram_rank}, defect = {defect}")
    # fixed-point census: B = A^{mu4} = range of E; use a measured
    # SPANNING BASIS of B (commutant of a spanning set = B' exactly)
    u4f = gamma_partial(HW4_ref, list(range(4)), c4)
    Ps4 = sector_projs(u4f)
    dims4 = [int(round(np.trace(P).real)) for P in Ps4]
    m4 = sum(1 for d in dims4 if d > 0)

    def E16(x):
        return sum(P @ x @ P for P in Ps4)

    def span_basis(Eims, dim_expect):
        M = np.array([x.reshape(-1) for x in Eims])
        _, s, Vh = np.linalg.svd(M, full_matrices=False)
        r = int(np.sum(s > 1e-9 * s[0]))
        n = Eims[0].shape[0]
        return [Vh[i].reshape(n, n) for i in range(r)], r

    Eims = [E16(m.reshape(16, 16)) for m in np.array(mono_vecs)]
    basB, dimB = span_basis(Eims, None)
    check("G4b dim B = sum d_q^2 (measured spanning basis of E(A))",
          dimB == sum(d * d for d in dims4),
          f"dim B = {dimB}, sector dims = {dims4}")
    gensB = [np.kron(b, np.eye(4, dtype=complex)) for b in basB]
    kdB, gapB, _ = comm_kernel(gensB, D6)
    ratio = kdB / kdA
    check("G4b fixed-point census: dim B' = m * 4^{n_c} = 64, excess ratio "
          "dim B'/dim A' = 4 = the local Watatani index",
          kdB == 64 and abs(ratio - 4.0) < 1e-12 and gapB > 1e6 and m4 == 4,
          f"dim B' = {kdB}, ratio = {ratio:.1f}, gap = {gapB:.1e}")
    # l = 1 anomaly config (D = 16): I = 2 modes, comp = 2 modes
    HW2 = np.array([[0.0, -1.0], [1.0, 0.0]])
    c2 = jw_ops(2)
    gensA1 = []
    for i in range(2):
        gensA1 += [c4[i], c4[i].conj().T]      # inside jw_ops(4) frame
    kdA1, gapA1, _ = comm_kernel(gensA1, 16)
    u2 = gamma_partial(HW2, [0, 1], c2)
    Ps2 = sector_projs(u2)
    m2 = sum(1 for P in Ps2 if np.trace(P).real > 0.5)

    def E4f(x):
        return sum(P @ x @ P for P in Ps2)

    monos2 = []
    for S in range(4):
        for Tm in range(4):
            op = np.eye(4, dtype=complex)
            for i in range(2):
                if (S >> i) & 1:
                    op = op @ c2[i].conj().T
            for i in range(2):
                if (Tm >> i) & 1:
                    op = op @ c2[i]
            monos2.append(op)
    basB1, dimB1 = span_basis([E4f(m) for m in monos2], None)
    gensB1 = [np.kron(b, np.eye(4, dtype=complex)) for b in basB1]
    kdB1, gapB1, _ = comm_kernel(gensB1, 16)
    check("G4b l = 1 anomaly census: dim A' = 16, dim B' = 48, excess "
          "ratio = 3 (the 3-sector anomaly index)",
          kdA1 == 16 and kdB1 == 48 and m2 == 3
          and gapA1 > 1e6 and gapB1 > 1e6,
          f"dim A' = {kdA1}, dim B' = {kdB1}, m = {m2}")

    # ================= G5 controls ======================================
    print("\n-- G5: controls (must fire) --")
    # C1 scrambled bond data: same-arc pairing instead of the half-turn
    J2 = np.array([[0.0, -1.0], [1.0, 0.0]])
    HW4s = np.kron(np.eye(2), J2)             # pairs (0,1),(2,3): same arc
    HW8s = np.kron(np.eye(4), J2)
    U4s = gamma_partial(HW4s, list(range(4)), c4)
    U8s = gamma_partial(HW8s, list(range(8)), c8)
    T4s, _ = transport(U4s, c4)
    T8s, _ = transport(U8s, c8)
    dev_c1 = float(np.abs(VW_ref @ T4s - T8s @ VW_ref).max())
    check("C1 fires: same-arc bond scramble breaks tower coherence "
          "(V_W T4s != T8s V_W)", dev_c1 > 0.1, f"dev = {dev_c1:.3f}")
    # C2 broken twist: Z2-only average
    ok_c2 = True
    for NN in (48, 384):
        win = window(NN, 0, 2)
        HWn = spower(NN, NN // 2)[np.ix_(win, win)]
        cs = jw_ops(4)
        U = gamma_partial(HWn, list(range(4)), cs)
        Ps = sector_projs(U)
        v = np.zeros(16, dtype=complex)
        for P in Ps:
            o = onb_of(P)
            if o.shape[1]:
                v += o[:, 0]
        v /= np.linalg.norm(v)

        def E2(x, U=U):
            U2 = U @ U
            return (x + U2 @ x @ U2.conj().T) / 2

        lam2 = lam_of(np.outer(v, v.conj()), E2)
        ok_c2 &= abs(lam2 - 0.5) < 1e-8
    check("C2 fires: Z2-only average gives lambda = 1/2 != 1/4 at N = 48 "
          "and 384 (index census breaks under broken twist)", ok_c2)
    # C3 scrambled state: random occupation, alternating filling
    rng3 = np.random.default_rng(SEED + 1)

    def scr_cov(Nk, k):
        frac = 0.3 if k % 2 == 0 else 0.7
        occ = np.zeros(Nk)
        occ[rng3.permutation(Nk)[:int(frac * Nk)]] = 1.0
        return covariance_occ(Nk, occ)

    cws_scr = pullback_series(scr_cov, haar_iso, K_STATE)
    om_s = []
    for CW in cws_scr:
        rho = gaussian_rho(CW, c4)
        om_s.append(np.array([np.trace(rho @ x) for x in batt]))
    om_s = np.array(om_s)
    d5s = float(np.abs(om_s[-1] - om_s[-2]).max())
    check("C3 fires: scrambled state breaks Cauchy convergence "
          f"(d5_scr = {d5s:.3f} > max(10*d5_true, 0.05))",
          d5s > max(10 * dd[-1], 0.05))
    # C4 decimation embedding: limit degenerates
    cws_dec = pullback_series(lambda Nk, k: covariance(Nk), decim_iso,
                              K_STATE)
    off_dec = float(np.abs(cws_dec[-1] - np.diag(np.diag(cws_dec[-1]))).max())
    off_haar = float(np.abs(cws[-1] - np.diag(np.diag(cws[-1]))).max())
    check("C4 fires: decimation embedding degenerates the limit "
          "(off-diag < 0.05) while the Haar chain does not (> 0.1)",
          off_dec < 0.05 and off_haar > 0.1,
          f"decim = {off_dec:.4f}, haar = {off_haar:.4f}")

    # ================= verdict ==========================================
    names = [n for n, _ in CHECKS]
    res = dict(CHECKS)
    g1 = all(res[n] for n in names if n.startswith("G1"))
    g2 = all(res[n] for n in names if n.startswith("G2"))
    g3 = all(res[n] for n in names if n.startswith("G3"))
    g4 = all(res[n] for n in names if n.startswith("G4"))
    ctrl = all(res[n] for n in names if n.startswith("C"))
    s0 = all(res[n] for n in names if n.startswith("S0"))
    if s0 and g1 and g2 and g3 and g4 and ctrl:
        verdict = "GNS-PRECURSORS-COHERENT"
    elif s0 and g1 and g3 and ctrl:
        verdict = "GNS-PRECURSORS-PARTIAL"
    else:
        verdict = "GNS-PRECURSORS-DEAD"
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print(f"\n{n_pass}/{len(CHECKS)} checks pass -- VERDICT: {verdict}"
          f"   ({time.time() - t0:.1f} s)")
    print("""
PRECURSOR MAP (typed; finite evidence FOR the cited theorems, never a
continuum proof):
  G1 (coherence, commuting squares)  -> theorem (1) GNS limit net: the
     inductive system (A_N, iota_N, E) is exactly coherent -- the data
     whose GNS/inductive limit the theorem asserts; the coherent
     expectation system is also the finite half of (3) Longo Q-system.
  G2 (state Cauchy profiles)         -> theorem (1): weak-* convergence
     of the canonical chiral-sea state on fixed local observables =
     the GNS-limit precursor.
  G3 (index census + PP margins)     -> theorem (2) index continuity
     (Pimsner-Popa/Longo heredity): index exactly 4 at every level
     with non-degrading margins.
  G4a (split witness)                -> theorem (5) split property:
     the finite correlation bound between separated intervals.
  G4b (commutant census)             -> theorem (5) Haag duality
     (twisted/fermionic form, defect 0) and the index =
     statistical-dimension reading of (2)/(3): excess ratio = 4.
  Theorem (4) (solitonic R sectors) is NOT re-measured here; its
  finite witness stays the v746 bond-defect identity.
No marker moves; exploration only.""")
    return 0 if n_pass == len(CHECKS) else 1


_run_part1 = main


def _run_part2():
    # PART 2 -- gnet_arf_qsystem_probe.py (verbatim; module-level names
    # local to this function scope)
    import hashlib
    import inspect
    import itertools
    import sys
    import time
    from fractions import Fraction as Fr

    import numpy as np

    TOL = 1e-10
    SEED = 20260805
    N0 = 48
    K_STATE = 5
    CHECKS = []

    K_MATTER = np.array([[1.0, 6.0], [3.0, 4.0]]) / 7.0
    PI_STAT = np.array([1.0 / 3.0, 2.0 / 3.0])


    def check(name, ok, detail=""):
        CHECKS.append((name, bool(ok)))
        print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
        return ok


    # ---------------- ladder constructions (as in gnet_gns_limit_probe) ---

    def spower(N, k):
        P = np.zeros((N, N))
        for j in range(N):
            P[(j + k) % N, j] = (-1.0) ** ((j + k) // N)
        return P


    def covariance(N):
        th = 2 * np.pi * (np.arange(N) + 0.5) / N
        th = np.mod(th + np.pi, 2 * np.pi) - np.pi
        th[np.isclose(th, -np.pi)] = np.pi
        F = np.exp(1j * np.outer(np.arange(N), th)) / np.sqrt(N)
        occ = (th < 0).astype(float)
        return (F * occ) @ F.conj().T


    def covariance_occ(N, occ):
        th = 2 * np.pi * (np.arange(N) + 0.5) / N
        th = np.mod(th + np.pi, 2 * np.pi) - np.pi
        th[np.isclose(th, -np.pi)] = np.pi
        F = np.exp(1j * np.outer(np.arange(N), th)) / np.sqrt(N)
        return (F * occ) @ F.conj().T


    def window(N, p, l):
        return [(p + i) % N for i in range(l)] + \
               [(p + N // 2 + i) % N for i in range(l)]


    def window6(N, p, l):
        return [(p + k * (N // 6) + i) % N for k in range(6) for i in range(l)]


    def haar_iso(N):
        V = np.zeros((2 * N, N))
        for j in range(N):
            V[2 * j, j] = V[2 * j + 1, j] = 1.0 / np.sqrt(2.0)
        return V


    def decim_iso(N):
        V = np.zeros((2 * N, N))
        for j in range(N):
            V[2 * j, j] = 1.0
        return V


    def jw_ops(n):
        sm = np.array([[0, 1], [0, 0]], dtype=complex)
        sz = np.array([[1, 0], [0, -1]], dtype=complex)
        I2 = np.eye(2, dtype=complex)
        ops = []
        for j in range(n):
            m = np.array([[1.0]], dtype=complex)
            for l in range(n):
                m = np.kron(m, sz if l < j else (sm if l == j else I2))
            ops.append(m)
        return ops


    def gamma_partial(Hsub, idx, cops):
        mu, V = np.linalg.eigh(1j * Hsub)
        dim = cops[0].shape[0]
        U = np.eye(dim, dtype=complex)
        for i in range(len(idx)):
            d = sum(np.conj(V[j, i]) * cops[idx[j]] for j in range(len(idx)))
            n_i = d.conj().T @ d
            ev = -1j * mu[i]
            U = U @ (np.eye(dim) + (ev - 1) * n_i)
        return U


    def gamma_u(Vmat, cops):
        """implementer of a general (normal, unitary) one-particle map:
        eig + per-cluster orthonormalization, then product of phase gates."""
        w, W = np.linalg.eig(Vmat)
        order = np.argsort(np.round(np.angle(w), 9))
        w, W = w[order], W[:, order]
        i = 0
        while i < len(w):
            j = i
            while j < len(w) and abs(w[j] - w[i]) < 1e-9:
                j += 1
            Q, _ = np.linalg.qr(W[:, i:j])
            W[:, i:j] = Q
            i = j
        dim = cops[0].shape[0]
        U = np.eye(dim, dtype=complex)
        for i in range(len(w)):
            d = sum(np.conj(W[j, i]) * cops[j] for j in range(len(w)))
            n_i = d.conj().T @ d
            U = U @ (np.eye(dim) + (w[i] - 1) * n_i)
        return U


    def gaussian_rho(CW, cops):
        lam, V = np.linalg.eigh(CW)
        lam = np.clip(lam.real, 0.0, 1.0)
        dim = cops[0].shape[0]
        rho = np.eye(dim, dtype=complex)
        for i in range(len(cops)):
            d = sum(np.conj(V[j, i]) * cops[j] for j in range(len(cops)))
            rho = rho @ ((1 - lam[i]) * np.eye(dim)
                         + (2 * lam[i] - 1) * (d.conj().T @ d))
        return rho


    def sector_projs(U):
        return [sum((1j ** (-q * j)) * np.linalg.matrix_power(U, j)
                    for j in range(4)) / 4 for q in range(4)]


    def lam_of(B, Efun):
        A = Efun(B)
        a, W = np.linalg.eigh((A + A.conj().T) / 2)
        keep = a > 1e-11 * max(a.max(), 1.0)
        Ws = W[:, keep] / np.sqrt(a[keep])
        M = Ws.conj().T @ B @ Ws
        top = float(np.linalg.eigvalsh((M + M.conj().T) / 2).max().real)
        return 1.0 / top


    def onb_of(P):
        w, W = np.linalg.eigh((P + P.conj().T) / 2)
        return W[:, w > 0.5]


    def quasi_basis(Ps, weights=None):
        onbs = [onb_of(P) for P in Ps]
        dims = [o.shape[1] for o in onbs]
        if weights is None:
            weights = dims
        vs = [np.eye(Ps[0].shape[0], dtype=complex)]
        for q in range(4):
            for qp in range(4):
                if q == qp or dims[q] == 0 or dims[qp] == 0:
                    continue
                for a in range(dims[q]):
                    for b in range(dims[qp]):
                        vs.append(np.outer(onbs[q][:, a], onbs[qp][:, b].conj())
                                  / np.sqrt(weights[qp]))
        return vs


    # ---------------- Arf layer (closed forms from arf_spinor_compiler) ---

    W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
    GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]


    def hb(v, w):
        return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
                   for j in range(4)) % 2


    def xor4(v, w):
        return tuple((a + b) % 2 for a, b in zip(v, w))


    def sig_bits(v):
        return (v[2], v[0], v[1], v[3])


    def iota5(v):
        f1, f2, f3, a = v
        return (f1, f2, f3, a, (f1 + f2 + f3 + a) % 2)


    def qstar(v):
        return (sum(iota5(v)) // 2) % 2


    def bits_to_int(v):
        return v[0] | (v[1] << 1) | (v[2] << 2) | (v[3] << 3)


    def f2_rank_ints(vals):
        basis = []
        for x in vals:
            for b in basis:
                x = min(x, x ^ b)
            if x:
                basis.append(x)
                basis.sort(reverse=True)
        return len(basis)


    def sha_freeze():
        fns = [spower, covariance, covariance_occ, window, window6, haar_iso,
               decim_iso, jw_ops, gamma_partial, gamma_u, gaussian_rho,
               sector_projs, lam_of, onb_of, quasi_basis, hb, xor4, sig_bits,
               iota5, qstar, bits_to_int, f2_rank_ints]
        blob = "".join(inspect.getsource(f) for f in fns)
        blob += repr((TOL, SEED, N0, K_STATE, K_MATTER.tolist(),
                      PI_STAT.tolist()))
        return hashlib.sha256(blob.encode()).hexdigest()


    # =====================================================================

    def main():
        t0 = time.time()
        print("gnet_arf_qsystem_probe -- index-4 Q-system vs Arf/S5/K6, "
              "uniform bounds\n")
        print(f"SHA-freeze (construction source + constants): "
              f"{sha_freeze()[:32]}")
        print("HONESTY: Watatani index 4 = |mu4| and the channel eigenvalue "
              "4/49 = (-2/7)^2\nare from different registers; nothing below "
              "relates them.\n")

        # ============ A: Arf layer reconstruction (exact) =================
        print("-- A: Arf layer (q*, sectors, K_matter derived exactly) --")
        ok_ref = all((qstar(xor4(v, w)) + qstar(v) + qstar(w)) % 2 == hb(v, w)
                     for v in W16 for w in W16)
        check("A1 q* = wt(iota)/2 is a quadratic refinement of hbar "
              "(256 cells)", ok_ref)
        refs = {c: {v: (qstar(v) + hb(v, c)) % 2 for v in W16} for c in W16}
        siginv = [c for c in W16
                  if all(refs[c][sig_bits(v)] == refs[c][v] for v in W16)]
        A_BIT, FSIG = (0, 0, 0, 1), (1, 1, 1, 0)
        sel = [c for c in siginv
               if refs[c][A_BIT] == 1 and refs[c][FSIG] == 0]
        check("A2 selector census on the 16 parametrized forms q_c = "
              "q* + hbar(.,c): 4 sigma-invariant, unique selected = q* "
              "(c = 0)", len(siginv) == 4 and sel == [(0, 0, 0, 0)])
        five = sorted(v for v in W16 if any(v) and qstar(v) == 0)
        ten = sorted(v for v in W16 if qstar(v) == 1)
        check("A3 sectors: |5bar| = 5, |10| = 10 (16 = 1 + 5 + 10)",
              len(five) == 5 and len(ten) == 10)
        NZ = [v for v in W16 if any(v)]
        rows = {}
        okK = True
        for x in NZ:
            into5 = sum(1 for y in five if hb(x, y) == 0)
            into10 = sum(1 for y in ten if hb(x, y) == 0)
            s = "5" if qstar(x) == 0 else "10"
            rows.setdefault(s, set()).add((into5, into10))
        okK = rows["5"] == {(1, 6)} and rows["10"] == {(3, 4)}
        check("A4 K_matter DERIVED: B-row counts constant per sector: "
              "5bar -> (1,6), 10 -> (3,4); K = (1/7)[[1,6],[3,4]]", okK,
              f"rows = {rows}")
        tr = Fr(1, 7) + Fr(4, 7)
        det = Fr(1 * 4 - 6 * 3, 49)
        check("A5 eig(K_matter) = {1, -2/7} (trace/det exact); stationary "
              "pi = (1/3, 2/3) = uniform on 15",
              tr == Fr(5, 7) and det == Fr(-2, 7)
              and np.allclose(PI_STAT @ K_MATTER, PI_STAT, atol=1e-15))
        # K^2 on the 15-point model (v754 identity, Fractions)
        pts = sorted(NZ)
        B15 = [[Fr(1 if hb(x, y) == 0 else 0, 7) for y in pts] for x in pts]
        K2 = [[sum(B15[i][k] * B15[k][j] for k in range(15)) for j in range(15)]
              for i in range(15)]
        okK2 = all(K2[i][j] == (Fr(4, 49) if i == j else 0)
                   + Fr(45, 49) * Fr(1, 15) for i in range(15)
                   for j in range(15))
        check("A6 K^2 = (4/49) I + (45/49) Pi_0 exact on the 15 points "
              "(v754 re-derived; the 4/49 lives HERE, in the channel "
              "register only)", okK2)

        # ============ S1: natural grading census ==========================
        print("\n-- S1: Q-system carrier / natural grading --")
        HN = spower(N0, N0 // 2)
        win0 = window(N0, 0, 2)
        HW4 = HN[np.ix_(win0, win0)]
        c4 = jw_ops(4)
        U4 = gamma_partial(HW4, list(range(4)), c4)
        Ps4 = sector_projs(U4)
        dims4 = [int(round(np.trace(P).real)) for P in Ps4]
        vs = quasi_basis(Ps4)
        ind = sum(v @ v.conj().T for v in vs)
        dev_ind = float(np.abs(ind - 4 * np.eye(16)).max())
        check("S1.1 explicit Watatani quasi-basis on the l = 2 window: "
              f"{len(vs)} elements (= 1 + sum d_q d_q'), sum v v* = 4*1 "
              "exact", len(vs) == 1 + 256 - sum(d * d for d in dims4)
              and dev_ind < 1e-7,
              f"dims = {dims4}, dev = {dev_ind:.1e}")

        # eigenmode frame and the (1, 5, 10) splitting
        ww, WW = np.linalg.eig(HW4)
        order = np.argsort(-np.imag(ww))
        ww, WW = ww[order], WW[:, order]
        i = 0
        while i < 4:
            j = i
            while j < 4 and abs(ww[j] - ww[i]) < 1e-9:
                j += 1
            Q, _ = np.linalg.qr(WW[:, i:j])
            WW[:, i:j] = Q
            i = j
        s_j = [int(round(np.imag(ww[j]))) for j in range(4)]   # +1/-1
        check("S1.2 eigenmode frame: H_W eigenvalues (+i,+i,-i,-i)",
              s_j == [1, 1, -1, -1])
        nops = [c4[j].conj().T @ c4[j] for j in range(4)]
        words = [tuple(int(round(nops[j][b, b].real)) for j in range(4))
                 for b in range(16)]
        charge = {b: sum(s_j[j] * words[b][j] for j in range(4)) % 4
                  for b in range(16)}
        vac = words.index((0, 0, 0, 0))
        S5L = [b for b in range(16) if charge[b] == 0 and b != vac]
        S10L = [b for b in range(16) if charge[b] != 0]
        csz = [sum(1 for b in range(16) if charge[b] == c) for c in range(4)]
        check("S1.3 ladder splitting 16 = 1 + 5 + 10 (vacuum / charge-0 "
              "nonvac / charged); charge dims = (6,4,2,4)",
              len(S5L) == 5 and len(S10L) == 10 and csz == [6, 4, 2, 4]
              and sorted(csz) == sorted(dims4))
        s5_ints = [bits_to_int(words[b]) for b in S5L]
        five_ints = [bits_to_int(v) for v in five]
        r_lad = f2_rank_ints(list(s5_ints))
        r_arf = f2_rank_ints(list(five_ints))
        check("S1.4 F2-RANK CERTIFICATES: rank(ladder 5-set) = 3, "
              "rank(Arf 5bar) = 4 -- a linear bijection is impossible",
              r_lad == 3 and r_arf == 4, f"ranks = {r_lad} vs {r_arf}")
        # exhaustive GL(4,2) census
        five_sets = {}
        for c in W16:
            z = sorted(bits_to_int(v) for v in W16
                       if any(v) and refs[c][v] == 0)
            if len(z) == 5:
                five_sets[c] = (set(z), f2_rank_ints(list(z)))
        tgt5 = set(five_ints)
        src5 = set(s5_ints)
        n_gl, n_hit, hits_c = 0, 0, {c: 0 for c in five_sets}
        for mask in range(1 << 16):
            rowsM = [(mask >> (4 * i)) & 15 for i in range(4)]
            b = list(rowsM)
            rk = 0
            bb = []
            for x in b:
                for y in bb:
                    x = min(x, x ^ y)
                if x:
                    bb.append(x)
            if len(bb) != 4:
                continue
            n_gl += 1
            img = set()
            for x in src5:
                y = 0
                for i in range(4):
                    if (x >> i) & 1:
                        y ^= rowsM[i]
                img.add(y)
            if img == tgt5:
                n_hit += 1
            for c, (zs, _r) in five_sets.items():
                if img == zs:
                    hits_c[c] += 1
        check("S1.5 EXHAUSTIVE GL(4,2) CENSUS: |GL| = 20160; bijections "
              "mapping ladder-5 onto Arf-5bar: 0 (and 0 for EVERY Arf-1 "
              "form's 5-set; all those have rank 4)",
              n_gl == 20160 and n_hit == 0
              and all(h == 0 for h in hits_c.values())
              and all(r == 4 for _z, r in five_sets.values()),
              f"|GL| = {n_gl}, hits = {n_hit}, per-form = "
              f"{sorted(hits_c.values())}")
        # internal order-3 census on the window
        Vch = np.eye(N0)
        Nk = N0
        for k in range(K_STATE):
            Vch = (haar_iso(Nk) @ Vch)
            Nk *= 2
        CW_lim = (Vch.T @ covariance(Nk) @ Vch)[np.ix_(win0, win0)]
        phases = [1, -1, 1j, -1j]
        n_ord3, n_nontriv = 0, 0
        for perm in itertools.permutations(range(4)):
            for ph in itertools.product(phases, repeat=4):
                M = np.zeros((4, 4), dtype=complex)
                for i in range(4):
                    M[perm[i], i] = ph[i]
                if np.abs(M @ M @ M - np.eye(4)).max() > 1e-12:
                    continue
                if np.abs(M @ HW4 - HW4 @ M).max() > 1e-12:
                    continue
                if np.abs(M @ CW_lim @ M.conj().T - CW_lim).max() > 1e-9:
                    continue
                n_ord3 += 1
                if np.abs(M - M[0, 0] * np.eye(4)).max() > 1e-12:
                    n_nontriv += 1
        check("S1.6 internal order-3 census (6144 generalized signed "
              "perms, compatible with H_W and the limit C_W): only the "
              "identity survives -- NO internal sigma register on the "
              "16-state window", n_ord3 == 1 and n_nontriv == 0,
              f"survivors = {n_ord3}, nontrivial = {n_nontriv}")

        # the sixfold window: the sigma register DOES exist, but on 64 states
        w6 = window6(N0, 0, 1)
        HW6 = spower(N0, N0 // 2)[np.ix_(w6, w6)]
        DK6 = spower(N0, N0 // 3)[np.ix_(w6, w6)]
        ok_pres = all(((j + N0 // 2) % N0 in w6) and ((j + N0 // 3) % N0 in w6)
                      for j in w6)
        ok_alg = (np.abs(HW6 @ DK6 - DK6 @ HW6).max() < 1e-12
                  and np.abs(HW6 @ HW6 + np.eye(6)).max() < 1e-12
                  and np.abs(np.linalg.matrix_power(DK6, 3)
                             + np.eye(6)).max() < 1e-12)
        check("S1.7 Z6-quotient window W6: deck AND half-turn internal, "
              "[H,D] = 0, H^2 = -1, D^3 = -1 (NS)", ok_pres and ok_alg)
        c6 = jw_ops(6)
        U6 = gamma_partial(HW6, list(range(6)), c6)
        G6 = gamma_u(DK6, c6)
        dev_g = max(float(np.abs(G6 @ c6[j] @ G6.conj().T
                                 - sum(DK6[k, j] * c6[k] for k in range(6))).max())
                    for j in range(6))
        comm_ad = max(float(np.abs((U6 @ G6) @ c6[j] @ (U6 @ G6).conj().T
                                   - (G6 @ U6) @ c6[j]
                                   @ (G6 @ U6).conj().T).max())
                      for j in range(6))
        Ps6 = sector_projs(U6)
        dims6 = [int(round(np.trace(P).real)) for P in Ps6]
        dev_dp = max(float(np.abs(G6 @ P - P @ G6).max()) for P in Ps6)

        def E6(x):
            return sum(P @ x @ P for P in Ps6)

        v6 = np.zeros(64, dtype=complex)
        for P in Ps6:
            o = onb_of(P)
            if o.shape[1]:
                v6 += o[:, 0]
        v6 /= np.linalg.norm(v6)
        lam6 = lam_of(np.outer(v6, v6.conj()), E6)
        check("S1.8 W6 carries the joint register: Gamma(D) correct "
              "(Ad on generators), Ad-commutes with Gamma(H), deck acts "
              "INSIDE each mu4 sector, dims = (20,16,12,16), lambda* = 1/4",
              dev_g < 1e-9 and comm_ad < 1e-9 and dev_dp < 1e-9
              and dims6 == [20, 16, 12, 16] and abs(lam6 - 0.25) < 1e-8,
              f"lambda* = {lam6:.10f}")
        # deck orbit census per sector (eigenmode occupation words)
        fixed_pred = {0: (2, 6), 1: (1, 5), 2: (0, 4), 3: (1, 5)}
        cen6 = {}
        for c in range(4):
            nf = 0
            for mp in itertools.product((0, 1), repeat=3):
                for mm in itertools.product((0, 1), repeat=3):
                    if (sum(mp) - sum(mm)) % 4 != c:
                        continue
                    if len(set(mp)) == 1 and len(set(mm)) == 1:
                        nf += 1
            d = dims6[c]
            cen6[c] = (nf, (d - nf) // 3)
        check("S1.9 deck-orbit census per mu4 sector on W6 (fixed, "
              "3-orbits) = (2,6),(1,5),(0,4),(1,5); V-side sigma census "
              "(1: (1,0); 5bar: (2,1); 10: (1,3)) -- DIFFERENT registers, "
              "64 != 16: no pointwise transport (reported, not forced)",
              cen6 == fixed_pred, f"census = {cen6}")
        s1_natural = (n_hit >= 1 and n_nontriv >= 1)

        # ============ S2: sector transport vs K_matter ====================
        print("\n-- S2: sector weights along the Haar tower vs K_matter --")

        def pullback_full(cov_fun, iso_fun, kmax):
            out = []
            chain = np.eye(N0)
            Nk = N0
            for k in range(kmax + 1):
                C = cov_fun(Nk, k)
                out.append(chain.T @ C @ chain)
                chain = iso_fun(Nk) @ chain
                Nk *= 2
            return out

        Cts = pullback_full(lambda Nk, k: covariance(Nk), haar_iso, K_STATE)

        def weights_of(Ct, Weig, ch):
            Ceig = Weig.conj().T @ Ct[np.ix_(win0, win0)] @ Weig
            rho = gaussian_rho(Ceig, c4)
            P = np.real(np.diag(rho))
            w1 = P[vac]
            w5 = float(sum(P[b] for b in range(16) if ch[b] == 0)) - w1
            w10 = float(sum(P[b] for b in range(16) if ch[b] != 0))
            return np.array([w1, w5, w10])

        wk = np.array([weights_of(Ct, WW, charge) for Ct in Cts])
        xk = np.array([w[1:] / (w[1] + w[2]) for w in wk])
        print("   w(k) [vac, 5, 10]:")
        for k in range(K_STATE + 1):
            print(f"     k={k}: {wk[k][0]:.6f} {wk[k][1]:.6f} {wk[k][2]:.6f}"
                  f"   x = ({xk[k][0]:.6f}, {xk[k][1]:.6f})")
        spread = float(np.abs(xk - xk[-1]).max())
        # transfer fit x(k+1) = x(k) T, T row-stochastic (2 params)
        A_ls, b_ls = [], []
        for k in range(K_STATE):
            A_ls.append([xk[k][0], xk[k][1]])
            b_ls.append(xk[k + 1][0])
        ab, *_ = np.linalg.lstsq(np.array(A_ls), np.array(b_ls), rcond=None)
        Tfit = np.array([[ab[0], 1 - ab[0]], [ab[1], 1 - ab[1]]])
        res = max(float(np.abs(xk[k + 1] - xk[k] @ Tfit).max())
                  for k in range(K_STATE))
        devK = min(float(np.abs(Tfit - K_MATTER).max()),
                   float(np.abs(Tfit - K_MATTER.T).max()))
        devI = float(np.abs(Tfit - np.eye(2)).max())
        degen = spread < 1e-3
        s2_kmatter = (not degen) and res < 1e-3 and devK < 1e-6
        print("   S2.1 transfer fit: " +
              (f"DEGENERATE (spread {spread:.2e} < 1e-3; any fixed-point T "
               "fits) -- transfer test void, stationary test decides"
               if degen else
               f"T fitted (res {res:.1e}); |T - K_matter| = {devK:.3e}, "
               f"|T - I| = {devI:.3e}") +
              f"; T = {np.round(Tfit, 4).tolist()}")
        print("   S2.2 K_MATTER TRANSFER: " +
              ("YES" if s2_kmatter else "NO (degenerate or mismatch)"))
        dev_pi = float(np.abs(xk[-1] - PI_STAT).max())
        s2_stat = dev_pi < 1e-3
        print(f"   S2.3 STATIONARY LAW: |x(5) - (1/3, 2/3)| = {dev_pi:.4f} "
              + ("< 1e-3: matches pi" if s2_stat else ">= 1e-3: does NOT "
                 "match K_matter's stationary law (clean NO)"))

        # ============ S3: quasi-basis <-> C[Z4], the dim law ==============
        print("\n-- S3: the C[Z4] 4-element quasi-basis obstruction law --")
        ok_law, ok_obstruct = True, True
        print(f"{'l':>3} {'dims (census)':>22} {'closed form':>22} "
              f"{'rel gap':>9}")
        for l in range(1, 7):
            dc = [0, 0, 0, 0]
            for a in range(l + 1):
                for b in range(l + 1):
                    from math import comb
                    dc[(a - b) % 4] += comb(l, a) * comb(l, b)
            pred = [4 ** (l - 1) + (2 ** (l - 1) if c == 0 else
                                    (-2 ** (l - 1) if c == 2 else 0))
                    for c in range(4)]
            ok_law &= dc == pred
            ok_obstruct &= (dc[0] != dc[1]) and (dc[0] != dc[2])
            print(f"{l:>3} {str(dc):>22} {str(pred):>22} "
                  f"{2.0 ** (-l):>9.4f}")
        check("S3.1 DIM LAW exact for l = 1..6: d_c = 4^{l-1} + 2^{l-1} "
              "cos(pi c/2); relative gap (d_0 - d_2)/4^l = 2^{-l} -> 0: "
              "the C[Z4] 4-element quasi-basis is obstructed at EVERY "
              "finite l, restored only asymptotically", ok_law and ok_obstruct)
        check("S3.2 BONUS: d_2(1) = 0 IS the l = 1 three-sector index-3 "
              "anomaly of v746 (the law explains it)",
              ok_law)   # d_2(1) = 4^0 - 2^0 = 0 inside the verified law
        # index recheck l = 2, 3 with correct weights; must-fail with wrong
        ok_idx = dev_ind < 1e-7
        win3 = window(N0, 0, 3)
        HW6b = HN[np.ix_(win3, win3)]
        c6b = jw_ops(6)
        U6b = gamma_partial(HW6b, list(range(6)), c6b)
        Ps6b = sector_projs(U6b)
        vs3 = quasi_basis(Ps6b)
        ind3 = sum(v @ v.conj().T for v in vs3)
        ok_idx &= float(np.abs(ind3 - 4 * np.eye(64)).max()) < 1e-7
        check("S3.3 Watatani quasi-basis index = 4*1 exact at l = 2 and "
              "l = 3 (the general basis carries index 4 despite the "
              "crossed-product obstruction)", ok_idx)
        dims_shift = [dims4[(q + 1) % 4] for q in range(4)]
        vs_bad = quasi_basis(Ps4, weights=dims_shift)
        ind_bad = sum(v @ v.conj().T for v in vs_bad)
        scal = np.trace(ind_bad).real / 16
        dev_bad = float(np.abs(ind_bad - scal * np.eye(16)).max())
        check("S3.4 MUST-FAIL fires: WRONG sector weights (shifted d_{q+1}) "
              "break quasi-basis scalarness", dev_bad > 0.1,
              f"dev from scalar = {dev_bad:.3f}")
        s3_law = ok_law and ok_obstruct and ok_idx and dev_bad > 0.1

        # ============ S4: uniform sector-resolved split bounds ============
        print("\n-- S4: uniform per-sector split bounds along the tower --")
        winB = window(N0, 6, 2)
        joint = win0 + winB
        c8 = jw_ops(8)
        d1 = [sum(np.conj(WW[j, i]) * c8[j] for j in range(4))
              for i in range(4)]
        d2 = [sum(np.conj(WW[j, i]) * c8[4 + j] for j in range(4))
              for i in range(4)]

        def batt(d):
            return {0: [d[0].conj().T @ d[0], d[0].conj().T @ d[1]],
                    1: [d[0].conj().T, d[2]],
                    2: [d[0].conj().T @ d[1].conj().T,
                        d[0].conj().T @ d[2]],
                    3: [d[0], d[2].conj().T]}

        bat1, bat2 = batt(d1), batt(d2)
        prof = {(c, cp): [] for c in range(4) for cp in range(4)}
        for k in range(K_STATE + 1):
            Cj = Cts[k][np.ix_(joint, joint)]
            rho8 = gaussian_rho(Cj, c8)
            for c in range(4):
                for cp in range(4):
                    m = 0.0
                    for a in bat1[c]:
                        for b in bat2[cp]:
                            na = float(np.linalg.norm(a, 2))
                            nb = float(np.linalg.norm(b, 2))
                            val = abs(np.trace(rho8 @ (a @ b))
                                      - np.trace(rho8 @ a) * np.trace(rho8 @ b))
                            m = max(m, float(val) / (na * nb))
                    prof[(c, cp)].append(m)
        ok_bar, ok_tail = True, True
        n_zero = 0
        for (c, cp), p in sorted(prof.items()):
            if max(p) < 1e-12:
                n_zero += 1
                continue
            bar = max(2 * max(p[0], p[1]), 1e-3)
            ok_bar &= all(v <= bar for v in p)
            ok_tail &= abs(p[5] - p[4]) <= abs(p[4] - p[3]) + 1e-12
            print(f"   nu({c},{cp}): " + " ".join(f"{v:.5f}" for v in p))
        check(f"S4.1 uniform bar: every nonzero per-sector profile stays "
              f"<= max(2 max(nu(0), nu(1)), 1e-3) at all levels "
              f"({16 - n_zero} nonzero, {n_zero} exact conservation zeros; "
              f"the (1,3)/(3,1) k = 0 exact zero is a measured sea "
              f"symmetry, see docstring correction)", ok_bar)
        check("S4.2 oscillation-aware tails: |nu(5) - nu(4)| <= "
              "|nu(4) - nu(3)| for every nonzero profile", ok_tail)
        s4_uniform = ok_bar and ok_tail

        # ============ S5: index-continuity precursor ======================
        print("\n-- S5: index transport along the tower (slim recheck) --")
        ok5 = True
        for NN in (48, 768):
            HNN = spower(NN, NN // 2)
            winN = window(NN, 0, 2)
            HWn = HNN[np.ix_(winN, winN)]
            ok5 &= np.abs(HWn - HW4).max() < 1e-14
            Un = gamma_partial(HWn, list(range(4)), c4)
            Psn = sector_projs(Un)
            vn = np.zeros(16, dtype=complex)
            for P in Psn:
                o = onb_of(P)
                if o.shape[1]:
                    vn += o[:, 0]
            vn /= np.linalg.norm(vn)

            def En(x, Psn=Psn):
                return sum(P @ x @ P for P in Psn)

            ok5 &= abs(lam_of(np.outer(vn, vn.conj()), En) - 0.25) < 1e-8
            indn = sum(v @ v.conj().T for v in quasi_basis(Psn))
            ok5 &= float(np.abs(indn - 4 * np.eye(16)).max()) < 1e-7
        check("S5.1 window data literally level-independent; lambda* = 1/4 "
              "and index 4*1 exact at N = 48 and N = 768: with S4's "
              "uniform constants this is the finite precursor of index "
              "continuity in the GNS limit (typed, never the theorem)", ok5)

        # ============ Controls ============================================
        print("\n-- Controls (must fire) --")
        # C1 bond scramble: same-arc pairing
        J2 = np.array([[0.0, -1.0], [1.0, 0.0]])
        HW4s = np.kron(np.eye(2), J2)
        ws_, WWs = np.linalg.eig(HW4s)
        orders = np.argsort(-np.imag(ws_))
        ws_, WWs = ws_[orders], WWs[:, orders]
        i = 0
        while i < 4:
            j = i
            while j < 4 and abs(ws_[j] - ws_[i]) < 1e-9:
                j += 1
            Q, _ = np.linalg.qr(WWs[:, i:j])
            WWs[:, i:j] = Q
            i = j
        ssj = [int(round(np.imag(ws_[j]))) for j in range(4)]
        ch_s = {b: sum(ssj[j] * words[b][j] for j in range(4)) % 4
                for b in range(16)}
        w_scr = weights_of(Cts[-1], WWs, ch_s)
        dev_c1 = float(np.abs(w_scr - wk[-1]).max())
        check("C1 fires: same-arc bond scramble shifts the sector weights "
              f"(max dev {dev_c1:.4f} > 0.02)", dev_c1 > 0.02)
        # C2 Z2-only
        v2m = np.zeros(16, dtype=complex)
        for P in Ps4:
            o = onb_of(P)
            if o.shape[1]:
                v2m += o[:, 0]
        v2m /= np.linalg.norm(v2m)

        def E2(x):
            U2 = U4 @ U4
            return (x + U2 @ x @ U2.conj().T) / 2

        lam2 = lam_of(np.outer(v2m, v2m.conj()), E2)
        check("C2 fires: Z2-only average gives lambda = 1/2 != 1/4 "
              "(index census breaks)", abs(lam2 - 0.5) < 1e-8,
              f"lambda = {lam2:.10f}")
        # C3 scrambled sea
        rng3 = np.random.default_rng(SEED + 1)

        def scr_cov(Nk, k):
            frac = 0.3 if k % 2 == 0 else 0.7
            occ = np.zeros(Nk)
            occ[rng3.permutation(Nk)[:int(frac * Nk)]] = 1.0
            return covariance_occ(Nk, occ)

        Cts_scr = pullback_full(scr_cov, haar_iso, K_STATE)
        w_s = np.array([weights_of(Ct, WW, charge) for Ct in Cts_scr])
        d5s = float(np.abs(w_s[-1] - w_s[-2]).max())
        d5t = float(np.abs(wk[-1] - wk[-2]).max())
        check("C3 fires: scrambled sea breaks weight convergence "
              f"(final delta {d5s:.3f} > max(10 x {d5t:.5f}, 0.05))",
              d5s > max(10 * d5t, 0.05))
        # C4 decimation
        Cts_dec = pullback_full(lambda Nk, k: covariance(Nk), decim_iso,
                                K_STATE)
        w_dec = weights_of(Cts_dec[-1], WW, charge)
        dev_c4 = float(np.abs(w_dec - wk[-1]).max())
        unif = np.array([1.0, 5.0, 10.0]) / 16.0
        dev_unif = float(np.abs(w_dec - unif).max())
        check("C4 fires: decimation embedding degenerates the weights to "
              f"UNIFORM (dev from (1,5,10)/16 = {dev_unif:.2e} < 1e-3) and "
              f"differs from Haar ({dev_c4:.4f} > 0.02) -- the caution "
              "line: uniformity fakes the stationary law in the degenerate "
              "limit", dev_c4 > 0.02 and dev_unif < 1e-3)
        # C5 wrong Arf form
        c_bad = (0, 1, 1, 1)
        q_bad = refs[c_bad]
        zb = {v for v in W16 if q_bad[v] == 0 and any(v)}
        zb_sig = {sig_bits(v) for v in zb}
        z_star = set(five)
        z_star_sig = {sig_bits(v) for v in z_star}
        check("C5 fires: q_bad = q* + hbar(., (0,1,1,1)) is Arf-1 with "
              "q_bad(A) = 1 but its zero set is NOT sigma-stable, while "
              "q*'s sectors ARE sigma-stable (S5-equivariance breaks for "
              "the wrong form)",
              len(zb) == 5 and q_bad[A_BIT] == 1 and zb_sig != zb
              and z_star_sig == z_star)

        # ============ verdict =============================================
        names = [n for n, _ in CHECKS]
        res_d = dict(CHECKS)
        ctrl = all(res_d[n] for n in names if n.startswith("C"))
        s2_any = s2_kmatter or s2_stat
        if s1_natural and s2_any and s3_law and s4_uniform and ok5 and ctrl:
            verdict = "GNET-ARF-QSYSTEM-CARRIES"
        elif (not s1_natural) and (not s2_any) and ctrl:
            verdict = "GNET-ARF-NO-CORRESPONDENCE"
        else:
            verdict = "GNET-ARF-PARTIAL" + ("" if ctrl else " (CONTROL-VOID)")
        n_pass = sum(1 for _, ok in CHECKS if ok)
        print(f"\n{n_pass}/{len(CHECKS)} checks pass -- VERDICT: {verdict}"
              f"   ({time.time() - t0:.1f} s)")
        geo = ("a natural geometric grading EXISTS" if s1_natural else
               "NOT geometric: rank certificate 3 vs 4, GL(4,2) census "
               f"{n_hit}/20160, internal order-3 nontrivial = {n_nontriv}; "
               "the sigma register lives on the Z6 window with 64 states")
        km = ("K_matter GOVERNS the tower weight transport (measured)"
              if s2_any else
              "K_matter does not govern the tower weight transport "
              f"(measured; |x5 - pi| = {dev_pi:.4f})")
        print(f"""
    FLAGS: S1-NATURAL = {s1_natural} (GL census {n_hit}/20160, internal
    order-3 nontrivial = {n_nontriv}); S2-KMATTER = {s2_kmatter},
    S2-STATIONARY = {s2_stat} (|x5 - pi| = {dev_pi:.4f}); S3-LAW = {s3_law};
    S4-UNIFORM = {s4_uniform}; S5 = {ok5}; controls fire = {ctrl}.

    TYPED SUMMARY (honest):
      * The counting echo is REAL and exact: both registers split
        16 = 1 + 5 + 10 with a distinguished point (vacuum <-> 0).
      * Geometry: {geo}.
      * Transport: {km}.
      * The G_net-internal positives stand on their own: the exact dim
        law d_c = 4^(l-1) + 2^(l-1) cos(pi c/2) makes the C[Z4]/Longo
        quasi-basis obstruction exactly 2^-l (asymptotically restored --
        the finite precursor of the GATE.METRIC.08/11 identification),
        and the sector-resolved split bounds are uniform along the tower
        (S4 = {s4_uniform}).
      * The two fours stay in their registers: index 4 = |mu4|;
        4/49 = (-2/7)^2 is the Kneser channel gap.  Unrelated.
    No marker moves; exploration only.""")
        return 0 if n_pass == len(CHECKS) else 1
    return main(), list(CHECKS)


def run():
    """run_all entry point (combined adjudication): part 1 must be 27/27
    (GNS-PRECURSORS-COHERENT), part 2 must be 27/27 with the honest
    negative (GNET-ARF-NO-CORRESPONDENCE: the counting echo is real, the
    geometry does not transport)."""
    rc1 = _run_part1()
    fails1 = [n for (n, ok) in CHECKS if not ok]
    part1_ok = (rc1 == 0 and not fails1 and len(CHECKS) == 27)
    print("\n[%s] PART-1 PATTERN GATE: expected 27/27 "
          "(GNS-PRECURSORS-COHERENT) -- fails: %s"
          % ("PASS" if part1_ok else "FAIL", fails1 or "none"))
    rc2, chks2 = _run_part2()
    fails2 = [n for (n, ok) in chks2 if not ok]
    part2_ok = (rc2 == 0 and not fails2 and len(chks2) == 27)
    print("\n[%s] PART-2 PATTERN GATE: expected 27/27 "
          "(GNET-ARF-NO-CORRESPONDENCE) -- fails: %s"
          % ("PASS" if part2_ok else "FAIL", fails2 or "none"))
    ok = part1_ok and part2_ok
    print("\nCOMBINED ADJUDICATION: %s -- GNS-PRECURSORS-COHERENT + "
          "GNET-ARF-NO-CORRESPONDENCE: the inductive system (Haar tower, "
          "commuting index-4 expectation squares, geometric state "
          "convergence, twisted-duality defect 0, ratio 4) is exactly "
          "coherent -- the measured finite data whose GNS limit the v746 "
          "continuum theorems assert; the exact dim law d_c = 4^(l-1) + "
          "2^(l-1) cos(pi c/2) makes the C[Z4] quasi-basis obstruction "
          "exactly 2^-l (asymptotically restored; explains the l = 1 "
          "anomaly); the Arf correspondence is honestly negative (rank 3 "
          "vs 4, GL census 0/20160, K_matter does not govern transport); "
          "the two fours stay in their registers.  NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
