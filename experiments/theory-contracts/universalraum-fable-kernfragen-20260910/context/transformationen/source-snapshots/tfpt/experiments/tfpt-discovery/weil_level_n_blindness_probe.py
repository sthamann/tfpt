#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weil_level_n_blindness_probe -- r640  ARITH.LEVELN.BLIND.01

Negative / equivalence register (experiments only).  Question of the day
(2026-09-03, RSA-260 factored by E. Lu): can the TFPT objects -- the E8
lattice, the Weil-measure detector (W1/W3), the mu4 / Coxeter clocks, or a
dissipative energy relaxation in the Hylaean sense -- be pointed at an
arbitrary modulus N = p q and read the factors off as a "delta"?

Every candidate is reduced to a measurable statement on two test moduli
(N_SMALL, enumerable; N_BIG, 40 digits) and one real one (RSA-260 bit sizes):

  S1  PRINCIPAL-CHARACTER BLINDNESS.  Twisting the Weil atom comb by
      chi_0 mod N (remove the primes dividing N) changes NOTHING below
      log min(p,q): Lambda*chi_0 == Lambda for every n < min(p,q), exactly.
      Any window with support below log p sees zero delta; a window above
      it has enumerated the primes up to p (trial division).
  S2  DELTA == SOLUTION.  The delta P(s) = L(s,chi_0)/zeta(s)
      = 1 - p^-s - q^-s + N^-s is the factorisation: P(1) = phi(N)/N gives
      p+q; the E8 shell count r_8(N) = 240 sigma_3(N) gives p^3+q^3.  Both
      inversions are one line -- and reading phi(N) off the coprime density
      needs X > 8N samples (measured), the shell has ~N^3 points, and
      |P(1/2+it) - 1| ~ 2 p^-1/2 needs (bits of p)/2 bits of precision.
  S3  QUADRATIC CHARACTER / CLASS NUMBER.  The Jacobi symbol (n/N) is a
      primitive character of conductor N, computable per term without the
      factors, and by reciprocity (n/N) below p depends only on N mod n.
      Its delta at s=1 is Dirichlet's class number h(-4N).  Measured:
      (a) the ambiguous classes of disc -4N ARE the factorisations;
      (b) with h known, g^(h/2^k) lands on an ambiguous form -> factor
          (poly-time given h; success rate over all reduced forms);
      (c) pinning h from partial sums of L(1,chi) needs X ~ N terms.
  S4  DISSIPATIVE ENERGY (Hylaean-type) RELAXATION.  E = (u+v-log N)^2 on
      the log-manifold plus an integrality penalty: the product manifold is
      reached from 100 % of starts (unique admissible sector); the integer
      factor pair at a rate consistent with basin counting ~2/sqrt(N)
      (Poisson p-value reported) -- an optimisation/mixing failure of this
      concrete solver, not an information-theoretic no-go.
  S5  PRE-REGISTRATION for E8.THETA.MODCRT.01 (composite-index modular
      coefficient a_N(E_4) = 240 sigma_3(N) mod ell without divisor search):
      the ell = 3 residue is ambiguous for N = 1 mod 3 and equals the
      quadratic-residuosity question "is -3 a square mod p" -- i.e. the
      first residue of that lane is already the QR problem for -3 mod N.

Imports nothing from verification/.  Deterministic.  Runs in seconds.

Decision: NO_SHORTCUT_FOUND (in the four implemented readouts no factor
path cheaper than the known routes; exact invariants phi(N), sigma_3(N)
factor N by explicit reduction -- BMS86 -- but nothing here is a lower
bound for all TFPT constructions) / PARTIAL / LEAK (some sub-check finds
factor information below cost sqrt(N) -- would be news).

What this probe does NOT show: a universal dichotomy "factor-blind or
factoring-equivalent" for every N-dependent readout.  Sub-exponential
routes built from many cheap, individually weak relations (QS/NFS
smoothness relations, ECM non-invertible coordinates, class-group
relation sieves, Shor's coherent modular powers) are a third kind that
this probe does not test.  Cardinalities (shell size) and partial-sum
term counts quoted here are costs of the implemented readouts, not lower
bounds.

Claim boundary: experiments only.  Not a ledger row.  Not a paper claim.
Fence: no RH claim; no factoring claim; no cryptographic statement beyond
the reductions checked here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from math import gcd
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROUND = 640
SEED = 640202609
CONTRACT = "ARITH.LEVELN.BLIND.01"
FENCE = "Exploration; no RH claim; no factoring claim"
TAG = "r640"
RESULT_JSON = HERE / "weil_level_n_blindness_result.json"

# --- test moduli -----------------------------------------------------------
P_SMALL, Q_SMALL = 1009, 1013                      # both = 1 mod 4 -> split in Z[i]
N_SMALL = P_SMALL * Q_SMALL                        # 1_022_117, enumerable
P_BIG = 1_000_000_000_000_000_000_117              # 22-digit primes (re-checked by gate S2-test-primes)
Q_BIG = 1_000_000_000_000_000_005_203
N_BIG = P_BIG * Q_BIG                              # 43 digits
RSA260_BITS, RSA260_FACTOR_BITS = 862, 431         # E. Lu, 2026-09-03 (Wikipedia RSA numbers)

# --- tolerances / budgets --------------------------------------------------
COPRIME_DENSITY_X_FACTORS = (0.5, 0.75, 1.0, 2.0, 8.0)   # X = factor * N in units of N^1 (0.5,0.75 as exponents)
L1_PARTIAL_X_GRID = (10**3, 10**4, 10**5, 10**6, 4 * 10**6)
RELAX_STARTS = 1000
RELAX_STEPS = 400
RELAX_LR = 0.05
INTEGER_PENALTY = 0.35

DECISIONS = ("NO_SHORTCUT_FOUND", "PARTIAL", "LEAK")
SEMIPRIME_SCAN_LIMIT = 400          # S5: p < q < limit, all semiprimes N = 1 mod 3
CHECKS: list[tuple[str, bool]] = []
LINES: list[str] = []


def emit(s: str = "") -> None:
    LINES.append(s)
    print(s)


def section(title: str) -> None:
    emit("")
    emit("== " + title)


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    emit("  [%s] %s%s" % ("PASS" if ok else "FAIL", name, ("  -- " + detail) if detail else ""))
    return bool(ok)


def fmt(x: float, nd: int = 4) -> str:
    return "nan" if not math.isfinite(x) else ("%%.%dg" % nd) % x


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def payload_sha(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


# --- elementary number theory (self-contained, exact) ---------------------
def is_prime(n: int) -> bool:
    """Deterministic Miller-Rabin for n < 3.3e24 (bases 2..41), probabilistic above."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def jacobi(a: int, n: int) -> int:
    """Jacobi symbol (a/n), n odd positive.  Poly-time; never touches factors of n."""
    assert n > 0 and n % 2 == 1
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def mangoldt_table(limit: int) -> np.ndarray:
    """Lambda(n) for 0..limit as float array (exact primes via sieve)."""
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i * i:: i] = False
    lam = np.zeros(limit + 1)
    for p in np.nonzero(sieve)[0]:
        pk = int(p)
        while pk <= limit:
            lam[pk] = math.log(int(p))
            pk *= int(p)
    return lam


def isqrt_exact(n: int) -> tuple[int, bool]:
    r = math.isqrt(n)
    return r, r * r == n


def icbrt_exact(n: int) -> tuple[int, bool]:
    r = round(n ** (1.0 / 3.0)) if n < 2**200 else int(round(math.exp(math.log(n) / 3.0)))
    for c in (r - 1, r, r + 1):
        if c >= 0 and c**3 == n:
            return c, True
    lo, hi = 0, 1 << ((n.bit_length() + 2) // 3 + 1)
    while lo < hi:
        mid = (lo + hi) // 2
        if mid**3 < n:
            lo = mid + 1
        else:
            hi = mid
    return lo, lo**3 == n


def factor_from_sum_and_product(s: int, prod: int) -> tuple[int, int] | None:
    """x,y with x+y=s, xy=prod, or None."""
    disc = s * s - 4 * prod
    if disc < 0:
        return None
    d, ok = isqrt_exact(disc)
    if not ok or (s + d) % 2:
        return None
    return (s - d) // 2, (s + d) // 2


# --- binary quadratic forms of discriminant D < 0 (Cohen Alg. 5.4.2 / 5.4.7) -
def bqf_reduce(f: tuple[int, int, int]) -> tuple[int, int, int]:
    """Reduced representative (-a < b <= a <= c, b >= 0 if a == c) of a positive definite form."""
    a, b, c = f
    D = b * b - 4 * a * c
    assert D < 0 and a > 0
    while True:
        if not (-a < b <= a):
            k = (a - b) // (2 * a)          # b + 2ka in (-a, a]
            b = b + 2 * k * a
            c = (b * b - D) // (4 * a)      # exact: discriminant preserved
        if a > c:
            a, b, c = c, -b, a
            continue
        if a == c and b < 0:
            b = -b
        return a, b, c


def bqf_compose(f1: tuple[int, int, int], f2: tuple[int, int, int]) -> tuple[int, int, int]:
    """Gauss/Dirichlet composition of primitive forms of equal discriminant (Cohen 5.4.7)."""
    a1, b1, c1 = f1
    a2, b2, c2 = f2
    if a1 > a2:
        a1, b1, c1, a2, b2, c2 = a2, b2, c2, a1, b1, c1
    s = (b1 + b2) // 2
    n = b2 - s

    def xgcd(x: int, y: int) -> tuple[int, int, int]:
        if y == 0:
            return x, 1, 0
        g, u, v = xgcd(y, x % y)
        return g, v, u - (x // y) * v

    if a2 % a1 == 0:
        y1, d = 0, a1
    else:
        d, u, _v = xgcd(a2, a1)   # u*a2 + v*a1 = d
        y1 = u
    if s % d == 0:
        y2, x2, d1 = -1, 0, d
    else:
        d1, u2, v2 = xgcd(s, d)   # u2*s + v2*d = d1
        x2, y2 = u2, -v2
    v1 = a1 // d1
    v2_ = a2 // d1
    r = (y1 * y2 * n - x2 * c2) % v1
    b3 = b2 + 2 * v2_ * r
    a3 = v1 * v2_
    c3 = (c2 * d1 + r * (b2 + v2_ * r)) // v1
    return bqf_reduce((a3, b3, c3))


def bqf_identity(D: int) -> tuple[int, int, int]:
    b = D % 2
    return bqf_reduce((1, b, (b * b - D) // 4))


def bqf_pow(f: tuple[int, int, int], e: int, D: int) -> tuple[int, int, int]:
    result = bqf_identity(D)
    base = f
    while e:
        if e & 1:
            result = bqf_compose(result, base)
        base = bqf_compose(base, base)
        e >>= 1
    return result


def reduced_forms(D: int) -> list[tuple[int, int, int]]:
    """All primitive reduced forms of discriminant D < 0."""
    out = []
    a_max = math.isqrt(abs(D) // 3)
    for a in range(1, a_max + 1):
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a or (c == a and b < 0):
                continue
            if gcd(gcd(a, abs(b)), c) != 1:
                continue
            out.append((a, b, c))
    return out


def is_ambiguous(f: tuple[int, int, int]) -> bool:
    a, b, c = f
    return b == 0 or a == b or a == c


# --- sections ---------------------------------------------------------------
def s1_principal_blindness() -> dict:
    section("S1  principal character chi_0 mod N: the twisted Weil atom comb below log min(p,q)")
    p, q, N = P_SMALL, Q_SMALL, N_SMALL
    limit = 4 * N_SMALL // 1000 + 2 * p          # comfortably above min(p,q)
    lam = mangoldt_table(limit)
    n = np.arange(limit + 1)
    coprime = np.array([gcd(int(k), N) == 1 for k in n])
    twisted = lam * coprime
    below = slice(0, min(p, q))
    identical_below = bool(np.array_equal(lam[below], twisted[below]))
    first_dev = int(np.nonzero(lam != twisted)[0][0])
    check("S1a-atoms-identical-below-min(p,q)", identical_below,
          "Lambda*chi_0 == Lambda for all n < %d; first deviation at n = %d (= p)" % (min(p, q), first_dev))
    check("S1b-first-deviation-is-a-factor", first_dev in (p, q) and N % first_dev == 0)

    # window read: prime-side sum with a tent of support [0, L]; L below/above log p
    def prime_side(L: float, table: np.ndarray) -> float:
        x = np.log(np.maximum(n, 1))
        f = np.clip(1.0 - np.abs(x - L / 2) / (L / 2), 0.0, None)   # tent on [0, L]
        return float(np.sum(table * f / np.sqrt(np.maximum(n, 1))))

    L_below, L_above = math.log(p) - 0.05, math.log(p) + 0.05
    d_below = prime_side(L_below, lam) - prime_side(L_below, twisted)
    d_above = prime_side(L_above, lam) - prime_side(L_above, twisted)
    check("S1c-window-delta-zero-below-log-p", d_below == 0.0, "delta(L=log p - 0.05) = %s" % fmt(d_below))
    check("S1d-window-delta-nonzero-above-log-p", d_above > 0.0,
          "delta(L=log p + 0.05) = %s = log p * f(log p)/sqrt(p) (one atom = trial division reached p)" % fmt(d_above))
    return {"first_deviation": first_dev, "delta_below": d_below, "delta_above": d_above,
            "log_p_rsa260": RSA260_FACTOR_BITS * math.log(2)}


def s2_delta_is_solution() -> dict:
    section("S2  the delta P(s)=L(s,chi_0)/zeta(s) and the E8 shell r_8(N) ARE the factorisation")
    p, q, N = P_BIG, Q_BIG, N_BIG
    check("S2-test-primes", is_prime(p) and is_prime(q) and p != q, "N_BIG has %d digits" % len(str(N)))
    phi = (p - 1) * (q - 1)                    # what P(1) = phi/N would hand us
    rec = factor_from_sum_and_product(N + 1 - phi, N)
    check("S2a-phi(N)-inverts-to-factors", rec == (min(p, q), max(p, q)), "p+q = N+1-phi(N), one quadratic")
    sigma3 = (1 + p**3) * (1 + q**3)           # r_8(N)/240 = sigma_3(N)
    rec3 = factor_from_sum_and_product(sigma3 - 1 - N**3, N**3)
    ok3 = False
    if rec3:
        a, aok = icbrt_exact(rec3[0])
        b, bok = icbrt_exact(rec3[1])
        ok3 = aok and bok and {a, b} == {p, q}
    check("S2b-E8-shell-r8(N)=240sigma3(N)-inverts-to-factors", ok3,
          "shell cardinality ~10^%d (a count, NOT a cost bound: sigma_3(N) <-> factoring is a reduction, BMS86)"
          % len(str(240 * sigma3)))
    check("S2c-r8-small-shells-are-E8", [240 * sum(d**3 for d in range(1, k + 1) if k % d == 0) for k in (1, 2, 3)] == [240, 2160, 6720])

    # precision needed on the critical line
    bits_small = 0.5 * math.log2(min(P_SMALL, Q_SMALL))
    bits_big = 0.5 * math.log2(min(p, q))
    bits_rsa = 0.5 * RSA260_FACTOR_BITS
    emit("  |P(1/2+it)-1| ~ 2 p^-1/2: precision needed  N_SMALL %.1f bits  N_BIG %.1f bits  RSA-260 %.1f bits"
         % (bits_small, bits_big, bits_rsa))

    # reading phi(N)/N off the coprime density: how many samples X ?
    Ns = N_SMALL
    phi_s = (P_SMALL - 1) * (Q_SMALL - 1)
    recovered = {}
    for fac in COPRIME_DENSITY_X_FACTORS:
        X = int(Ns**fac) if fac < 1.0 else int(fac * Ns)
        ks = np.arange(1, X + 1, dtype=np.int64)
        cnt = int(np.count_nonzero(np.gcd(ks, Ns) == 1))
        est = cnt * Ns / X
        recovered[fac] = int(round(est)) == phi_s
        emit("  X = %-9s  #coprime = %-8d  phi_est = %.3f  phi = %d  exact: %s"
             % (("N^%.2f" % fac) if fac < 1.0 else ("%gN" % fac), cnt, est, phi_s, recovered[fac]))
    check("S2d-coprime-density-fails-for-sublinear-X", not any(recovered[f] for f in COPRIME_DENSITY_X_FACTORS if f < 1.0),
          "count(X) - phi X/N = -sum_{d|N} mu(d){X/d}, so |phi_est - phi| <= 2N/X: needs X >= 4N to be guaranteed, X ~ N in practice")
    check("S2e-coprime-density-recovers-at-X=8N", recovered[8.0], "guaranteed regime (error <= 1/4)")
    return {"bits_needed": {"N_SMALL": bits_small, "N_BIG": bits_big, "RSA260": bits_rsa},
            "coprime_density_exact": {str(k): v for k, v in recovered.items()}}


def s3_quadratic_character_class_number() -> dict:
    section("S3  quadratic character (n/N) and Dirichlet's class number h(-4N)")
    p, q, N = P_SMALL, Q_SMALL, N_SMALL
    # (a) per-term computable without factors; reciprocity: (n/N) depends only on N mod n below p
    ok_rec = True
    for n in range(3, min(p, q), 2):
        lhs = jacobi(n, N)
        sign = -1 if (n % 4 == 3 and N % 4 == 3) else 1
        rhs = sign * jacobi(N % n, n)
        if lhs != rhs:
            ok_rec = False
            break
    check("S3a-reciprocity-(n/N)=f(N mod n)-below-p", ok_rec, "odd n < %d" % min(p, q))
    # non-splittability witness: (n/N)=+1 with (n/p)=(n/q)=-1 exist (QR problem)
    liars = [n for n in range(2, 2000) if jacobi(n, N) == 1 and jacobi(n, p) == -1]
    check("S3b-jacobi-plus-one-hides-non-residues", len(liars) > 0, "first: n=%d" % (liars[0] if liars else -1))

    # (b) class group of discriminant -4N
    D = -4 * N
    forms = reduced_forms(D)
    h = len(forms)
    one = bqf_identity(D)
    amb = [f for f in forms if is_ambiguous(f)]
    amb_factors = set()
    for a, b, c in amb:
        for g in (gcd(a, N), gcd(c, N), gcd(a + c + b, N) if b else 1):
            if 1 < g < N:
                amb_factors.add(g)
    check("S3c-ambiguous-classes-count-2^(t-1)", len(amb) == 4, "h(-4N) = %d, ambiguous = %d (t = 3 primes 2,p,q)" % (h, len(amb)))
    check("S3d-ambiguous-forms-ARE-the-factorisation", amb_factors == {p, q}, "gcds with N: %s" % sorted(amb_factors))
    # Lagrange: g^h = 1 for every class (validates composition and h simultaneously)
    lagrange_ok = all(bqf_pow(f, h, D) == one for f in forms)
    check("S3e-lagrange-g^h=1-all-classes", lagrange_ok, "composition + h consistent")
    # with h known: g^(h / 2^k) hits an ambiguous class -> factor
    v2 = 0
    hh = h
    while hh % 2 == 0:
        hh //= 2
        v2 += 1
    successes = 0
    for f in forms:
        g = bqf_pow(f, hh, D)                       # odd part killed: g in 2-power torsion
        found = False
        for _ in range(v2 + 1):
            if g != one and is_ambiguous(g):
                a, b, c = g
                if any(1 < gcd(x, N) < N for x in (a, c, a + b + c)):
                    found = True
                    break
            g = bqf_compose(g, g)
        successes += found
    rate = successes / h
    check("S3f-h-known-implies-poly-time-factor", rate >= 0.25,
          "success over all %d classes: %.3f  (v2(h)=%d; constant fraction => poly-time with h known)" % (h, rate, v2))

    # (c) pinning h from partial sums of L(1, chi_{-4N}) = pi h / sqrt(4N)  (w = 2)
    target = math.pi * h / math.sqrt(4 * N)
    chi_vals = None
    pinned = {}
    Xmax = max(L1_PARTIAL_X_GRID)
    ks = np.arange(1, Xmax + 1)
    # chi_{-4N}(n) = (D/n) Kronecker; for odd n equals jacobi(-4N mod n, n) ... use jacobi(N, n)*(-1/n)*(4/n)
    chi = np.zeros(Xmax + 1)
    for k in range(1, Xmax + 1, 2):
        if gcd(k, N) == 1:
            chi[k] = jacobi(N, k) * (-1 if k % 4 == 3 else 1)   # (-4N/k) = (-1/k)(N/k)
    partial = np.cumsum(chi[1:] / ks)
    h_est_all = partial * math.sqrt(4 * N) / math.pi
    rounds_to_h = np.rint(h_est_all) == h
    first_coincidence = int(np.nonzero(rounds_to_h)[0][0]) + 1
    wrong = np.nonzero(~rounds_to_h)[0]
    stable_from = int(wrong[-1]) + 2 if len(wrong) else 1          # round(h_est(X)) == h for all X >= stable_from
    for X in L1_PARTIAL_X_GRID:
        est_h = float(h_est_all[X - 1])
        pinned[X] = (int(round(est_h)) == h, est_h)
        emit("  X = %-8d  L_X(1,chi) = %.6f  target %.6f  h_est = %.3f  h = %d  rounds to h: %s"
             % (X, partial[X - 1], target, est_h, h, pinned[X][0]))
    emit("  rounding coincides with h first at X = %d (fluctuation, %.1f %% of X <= 2e4 do); stable for all X >= %d = %.2f N"
         % (first_coincidence, 100 * float(np.mean(rounds_to_h[:20000])), stable_from, stable_from / N))
    check("S3g-L(1,chi)-partial-sum-readout-not-certified-below-sqrt(N)", stable_from > math.isqrt(N),
          "one readout algorithm (raw Dirichlet partial sums), not a lower bound: Hafner-McCurley gives h in L[1/2]; "
          "coincidental roundings below sqrt(N) are uncertified")
    return {"h": h, "ambiguous": len(amb), "factor_rate_given_h": rate, "v2_h": v2,
            "pinned": {str(k): v[0] for k, v in pinned.items()},
            "first_coincidence_X": first_coincidence, "stable_from_X": stable_from}


def s4_dissipative_relaxation() -> dict:
    section("S4  Hylaean-type dissipative relaxation: E = (u+v-log N)^2 + lambda*[sin^2(pi e^u)+sin^2(pi e^v)]")
    N = N_SMALL
    rng = np.random.default_rng(SEED)
    logN = math.log(N)
    # starts: u in [0, log N/2], v = logN - u + noise  (typical: not on the manifold)
    u = rng.uniform(0.0, logN / 2, RELAX_STARTS)
    v = logN - u + rng.normal(0.0, 0.5, RELAX_STARTS)

    def rough_grad_and_curv(w, lam):
        """d/dw and d^2/dw^2 of lam*sin^2(pi e^w)  (the integrality well)."""
        ew = np.exp(w)
        s, c = np.sin(math.pi * ew), np.cos(math.pi * ew)
        g = lam * 2.0 * s * c * math.pi * ew
        curv = lam * (2.0 * (math.pi * ew) ** 2 * (c * c - s * s) + 2.0 * s * c * math.pi * ew)
        return g, np.maximum(np.abs(curv), 1e-9)

    def relax(uu, vv, lam, steps):
        # flat term: plain dissipative step; rough term: exponential-integrator style step
        # c(curv) = (1 - exp(-dbeta*curv)) / curv  (Newton-fast where steep, bounded where flat)
        for _ in range(steps):
            r = uu + vv - logN
            uu = uu - RELAX_LR * 2.0 * r
            vv = vv - RELAX_LR * 2.0 * r
            if lam:
                for arr in (uu, vv):
                    g, curv = rough_grad_and_curv(arr, lam)
                    step = (1.0 - np.exp(-3.0 * curv)) / curv
                    arr -= np.clip(step * g, -0.5, 0.5)
        return uu, vv

    results = {}
    for lam in (0.0, INTEGER_PENALTY):
        uu, vv = relax(u.copy(), v.copy(), 0.0, RELAX_STEPS)          # phase A: fall onto the product manifold
        if lam:
            uu, vv = relax(uu, vv, lam, RELAX_STEPS // 2)              # phase B: integrality wells switched on
        r = np.abs(uu + vv - logN)
        on_manifold = float(np.mean(r < 1e-3))
        x, y = np.exp(uu), np.exp(vv)
        xi, yi = np.rint(x), np.rint(y)
        integer_pt = (np.abs(x - xi) < 0.05) & (np.abs(y - yi) < 0.05)
        factor_pair = (xi * yi == N) & (xi > 1) & (yi > 1) & (np.abs(x - xi) < 0.5) & (np.abs(y - yi) < 0.5)
        results[lam] = {"on_manifold": on_manifold, "integer_points": float(np.mean(integer_pt)),
                        "factor_pairs": float(np.mean(factor_pair)), "n_factor": int(np.sum(factor_pair))}
        emit("  lambda = %-5s  on product manifold: %.3f  settled at integer points: %.3f  exact factor pair: %.4f (%d/%d)"
             % (lam, on_manifold, results[lam]["integer_points"], results[lam]["factor_pairs"],
                results[lam]["n_factor"], RELAX_STARTS))
    basin_expect = 2.0 / math.sqrt(N)   # two zero-energy integer points (p,q),(q,p) among ~sqrt(N) basins per branch
    expected_hits = basin_expect * RELAX_STARTS
    n_hits = results[INTEGER_PENALTY]["n_factor"]
    # Poisson probability of observing <= n_hits under the basin null
    p_null = sum(math.exp(-expected_hits) * expected_hits**k / math.factorial(k) for k in range(n_hits + 1))
    check("S4a-unique-admissible-sector-reached", results[0.0]["on_manifold"] >= 0.99,
          "unique attractor manifold u+v=log N (gapped, Perron-like) reached from %.1f %% of starts" % (100 * results[0.0]["on_manifold"]))
    check("S4b-sector-attractor-is-not-the-factor", results[0.0]["factor_pairs"] == 0.0,
          "zero-energy manifold is a continuum; the factor pairs ARE global zero minima but are never hit without integrality term")
    check("S4c-consistent-with-basin-counting", results[INTEGER_PENALTY]["factor_pairs"] <= 10 * basin_expect + 0.01,
          "hits %d/%d vs basin null 2/sqrt(N)*starts = %.2f (Poisson P(<=%d) = %.3f): this solver behaves like basin "
          "counting; an optimisation/mixing failure of THIS solver, not an information no-go"
          % (n_hits, RELAX_STARTS, expected_hits, n_hits, p_null))
    return {str(k): v for k, v in results.items()} | {"basin_expect": basin_expect, "poisson_p_null": p_null}


def s5_modcrt_preregistration() -> dict:
    section("S5  pre-registration E8.THETA.MODCRT.01: a_N(E_4) = 240 sigma_3(N) mod ell for composite N")
    # ell = 3: sigma_3(N) = (1+p^3)(1+q^3) = (1+p)(1+q) mod 3.  Which residues occur for a given N mod 3 ?
    from itertools import combinations
    primes = [n for n in range(5, SEMIPRIME_SCAN_LIMIT) if is_prime(n)]
    by_residue: dict[int, set[int]] = {}
    qr_consistent = True
    n_pairs = 0
    for p, q in combinations(primes, 2):
        N = p * q
        s3 = (1 + p**3) * (1 + q**3)
        by_residue.setdefault(N % 3, set()).add(s3 % 3)
        if N % 3 == 1:
            # sigma_3(N) = 1 mod 3  <=>  p = q = 1 mod 3  <=>  -3 is a square mod p  (and mod q)
            minus3_is_square_mod_p = pow(-3 % p, (p - 1) // 2, p) == 1
            if (s3 % 3 == 1) != minus3_is_square_mod_p:
                qr_consistent = False
        n_pairs += 1
    emit("  sigma_3(N) mod 3 by N mod 3 over %d semiprimes p<q<%d: %s"
         % (n_pairs, SEMIPRIME_SCAN_LIMIT, {k: sorted(v) for k, v in sorted(by_residue.items())}))
    check("S5a-residue-mod-3-ambiguous-for-N=1-mod-3", by_residue.get(1) == {0, 1} and by_residue.get(2) == {0},
          "N = 2 mod 3 forces 0; N = 1 mod 3 leaves {0,1}: one bit of factor information not determined by N mod 3")
    check("S5b-that-bit-is-QR(-3,N)", qr_consistent,
          "sigma_3(N) = 1 mod 3  <=>  -3 is a quadratic residue mod p  (Jacobi (-3/N) = +1 in both cases): "
          "the ell = 3 residue of the lane IS the quadratic-residuosity problem for -3 mod N")
    jac_uninformative = all(jacobi(-3 % (p * q), p * q) == 1 for p, q in combinations(primes[:40], 2) if (p * q) % 3 == 1)
    check("S5c-jacobi-cannot-split-it", jac_uninformative, "(-3/N) = +1 for every N = 1 mod 3 in the scan")
    emit("  stop sign for the lane: any composite-index a_N mod ell readout in poly(log N) without divisor search would decide")
    emit("  QR(-3, N) (ell = 3) and, by CRT over many ell, recover sigma_3(N) -> factor N; Couveignes-Edixhoven is prime-index only.")
    return {"by_residue": {str(k): sorted(v) for k, v in by_residue.items()}, "qr_consistent": qr_consistent, "n_pairs": n_pairs}


def decide(sections: dict) -> tuple[str, str]:
    leak = []
    if sections["s1"]["delta_below"] != 0.0:
        leak.append("S1 window delta below log p")
    if any(sections["s2"]["coprime_density_exact"][k] for k in ("0.5", "0.75")):
        leak.append("S2 phi(N) from sublinear samples")
    if sections["s3"]["stable_from_X"] <= math.isqrt(N_SMALL):
        leak.append("S3 h stably readable from o(sqrt N) partial-sum terms")
    if sections["s4"][str(INTEGER_PENALTY)]["factor_pairs"] > 10 * sections["s4"]["basin_expect"] + 0.01:
        leak.append("S4 relaxation beats basin counting")
    if leak:
        return "LEAK", "; ".join(leak)
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    if n_fail:
        return "PARTIAL", "%d gate(s) failed" % n_fail
    return "NO_SHORTCUT_FOUND", ("in the four implemented readouts no factor path cheaper than the known routes; "
                                 "exact phi(N) / sigma_3(N) factor N by explicit reduction, h(-4N) given exactly factors N "
                                 "with class-group arithmetic; no universal dichotomy and no lower bound for other "
                                 "TFPT constructions is claimed (weak-relation routes untested)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true", help="fewer relaxation starts")
    args = ap.parse_args()
    global RELAX_STARTS
    if args.smoke:
        RELAX_STARTS = 200
    wall0 = time.time()
    emit("%s  %s  round %d  fence: %s" % (TAG, CONTRACT, ROUND, FENCE))
    emit("N_SMALL = %d = %d * %d   N_BIG = %d digits   RSA-260 = %d bits (factors %d bits)"
         % (N_SMALL, P_SMALL, Q_SMALL, len(str(N_BIG)), RSA260_BITS, RSA260_FACTOR_BITS))
    sections = {"s1": s1_principal_blindness(), "s2": s2_delta_is_solution(),
                "s3": s3_quadratic_character_class_number(), "s4": s4_dissipative_relaxation(),
                "s5": s5_modcrt_preregistration()}
    verdict, why = decide(sections)
    check("G-verdict-enum", verdict in DECISIONS, verdict)
    payload = {"contract": CONTRACT, "tag": TAG, "round": ROUND, "fence": FENCE, "verdict": verdict, "why": why,
               "moduli": {"N_SMALL": N_SMALL, "N_BIG_digits": len(str(N_BIG)), "RSA260_bits": RSA260_BITS},
               "sections": json.loads(json.dumps(sections, default=float)),
               "gates": {name: ok for name, ok in CHECKS}}
    payload["result_sha"] = payload_sha(payload)
    payload["file_sha256"] = file_sha256()
    RESULT_JSON.write_text(json.dumps(payload, indent=1, sort_keys=True) + "\n")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    emit("")
    emit("VERDICT %s" % verdict)
    emit("WHY %s" % why)
    emit("GATES %d/%d" % (n_pass, len(CHECKS)))
    emit("FILE_SHA256 %s" % payload["file_sha256"])
    emit("RESULT_SHA %s" % payload["result_sha"])
    emit("WALL_S %s" % fmt(time.time() - wall0, 4))
    emit("ALL CHECKS PASSED" if n_pass == len(CHECKS) else
         "GATE_FAILURES " + ",".join(n for n, ok in CHECKS if not ok))
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
