"""Dressed microscopic 4-star vs the ideal 8-point filter (Konsolidierte_Fortsetzung sec. 7).

Quantifies the mismatch between the ideal star filter (designed for H = J*G)
and the exact microscopic dressed spectrum, and constructs the corrected
filter polynomial in H_eff.

Checks:
 1. ideal star spectrum {0,1/2,1,3/2,2,5/2,3}*J with multiplicities
    {1,30,45,40,15,90,35} (exact, 256-dim)
 2. dressed levels E(g) = (Delta - sqrt(Delta^2 + 4 t^2 (6-2g)))/2, ground g=0
 3. exact gap = (sqrt(D^2+24t^2)-sqrt(D^2+20t^2))/2 = 0.00243396875137...
    at Delta=1, t=0.05  (NOT the bare J/2 = 0.0025)
 4. dressed ground bare-matter weight = (1 + D/sqrt(D^2+24t^2))/2
    = 0.9856429311786321
 5. dressed level spacings are incommensurate with the bare J/2 grid
    (no exact rephasing time; max phase error at the bare filter time)
 6. corrected filter: p(x) = prod_{g>0} (x - E(g))/(E(0) - E(g)) applied to
    H_eff projects onto the dressed ground exactly (residual < 1e-12)

Scope: effective 256-dim matter space via M^dag M = 6I - 2G; the 67 dark
directions of the full 544-dim block stay at Delta and are never excited
from P. Numerical (double precision), not interval-certified.
"""
import numpy as np
from itertools import product
from fractions import Fraction
import json, time, hashlib
from pathlib import Path

start = time.time()
CHECKS = []

def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(name)
    print("PASS:", name, flush=True)

# ---- ideal star parent operator G = sum_e P_e^+ on 4 carriers, star edges ----
def swap4(a, b):
    S = np.zeros((16, 16))
    for x in range(4):
        for y in range(4):
            S[4 * y + x, 4 * x + y] = 1
    return S

I4 = np.eye(4)
def embed2(op2, i, j):
    # two-site operator on sites i,j of 4 (order 0..3), rest identity
    ops = [I4] * 4
    out = None
    # build via kronecker with care: place S on (i,j)
    # simpler: full 256 index map
    return None

def two_site_on(i, j):
    S2 = swap4(0, 1)
    idx = list(range(4))
    # permutation to bring (i,j) to front
    rest = [k for k in idx if k not in (i, j)]
    perm = [i, j] + rest
    P = np.zeros((256, 256))
    for state in product(range(4), repeat=4):
        src = sum(state[k] * 4**(3 - k) for k in range(4))
        permuted = [state[perm[m]] for m in range(4)]
        dst = sum(permuted[m] * 4**(3 - m) for m in range(4))
        P[dst, src] = 1.0
    S_front = np.kron(S2, I4)
    S_front = np.kron(S_front, I4)
    return P.T @ S_front @ P

star_edges = [(0, 1), (0, 2), (0, 3)]
G = sum(((np.eye(256) + two_site_on(i, j)) / 2 for (i, j) in star_edges),
        np.zeros((256, 256)))
G = 0.5 * (G + G.T)
ev, V = np.linalg.eigh(G)

# ---- 1. exact spectrum check ----
expect_mult = {Fraction(0): 1, Fraction(1, 2): 30, Fraction(1): 45,
               Fraction(3, 2): 40, Fraction(2): 15, Fraction(5, 2): 90,
               Fraction(3): 35}
for g, m in expect_mult.items():
    n = int(np.sum(np.abs(ev - float(g)) < 1e-10))
    require(n == m, f"1: star level g={g} has multiplicity {m}")
require(int(np.sum(np.abs(ev) < 1e-12)) == 1, "1b: unique bare ground (Omega)")

# ---- 2./3./4. dressed spectrum ----
Delta, t = 1.0, 0.05
J = 2 * t**2 / Delta
def E(g):
    return (Delta - np.sqrt(Delta**2 + 4 * t**2 * (6 - 2 * g))) / 2
levels = sorted(expect_mult.keys())
dressed = {float(g): E(float(g)) for g in levels}
ground_d = E(0.0)
first_d = E(0.5)
gap = first_d - ground_d
gap_formula = (np.sqrt(Delta**2 + 24 * t**2) - np.sqrt(Delta**2 + 20 * t**2)) / 2
require(abs(gap - gap_formula) < 1e-16, "2: dressed gap formula")
require(abs(gap - 0.0024339687513700303) < 1e-15,
        "3: dressed gap = 0.00243396875137... (not bare J/2 = 0.0025)")
w_bare = 0.5 * (1 + Delta / np.sqrt(Delta**2 + 24 * t**2))
require(abs(w_bare - 0.9856429311786321) < 1e-15,
        "4: dressed ground bare-matter weight = 0.9856429311786321")

# matrix-function cross-check: H_eff = (D I - sqrt(D^2 I + 4 t^2 (6I - 2G)))/2
# build in G's own eigenbasis V (eigenvalues ev), keeping the assignment
M2_ev = Delta**2 + 4 * t**2 * (6 - 2 * ev)
sq = V @ np.diag(np.sqrt(M2_ev)) @ V.T
H_eff = 0.5 * (Delta * np.eye(256) - sq)
ev_eff = np.sort(np.linalg.eigvalsh(H_eff))
expect_eff = sorted(E(float(g)) for g, m in expect_mult.items() for _ in range(m))
require(np.max(np.abs(ev_eff - np.array(expect_eff))) < 1e-12,
        "2b: H_eff matrix-function spectrum matches E(g) with multiplicities")

# ---- 5. incommensurability / rephasing error ----
# bare levels rephase exactly at tau* = 4 pi / J (all gaps multiples of J/2)
tau_star = 4 * np.pi / J
phases = {g: (E(g) * tau_star) % (2 * np.pi) for g in dressed}
# best common reference phase: minimize max circular distance
refs = np.linspace(0, 2 * np.pi, 20001)
def maxerr(ref):
    return max(min(abs(ph - ref), 2 * np.pi - abs(ph - ref)) for ph in phases.values())
best = min(refs, key=maxerr)
max_phase_err = maxerr(best)
require(max_phase_err > 1e-6,
        "5: dressed levels do NOT rephase at the bare filter time "
        f"(residual phase error {max_phase_err:.6f} rad)")
# bare case control: phases all multiples of 2 pi at tau*
bare_phases = [(float(g) * J * tau_star) % (2 * np.pi) for g in dressed]
require(max(min(p, 2 * np.pi - p) for p in bare_phases) < 1e-9,
        "5b: control - bare levels DO rephase at tau* (filter design assumption)")
# spacing ratios in units of the gap: bare are integers, dressed are not
bare_ratios = [(float(g) * J - 0) / (J / 2) for g in levels]
dressed_ratios = [(E(float(g)) - ground_d) / gap for g in levels]
irr = {str(g): r for g, r in zip(levels, dressed_ratios)
       if abs(r - round(r)) > 1e-12}
require(len(irr) >= 5, "5c: dressed spacing ratios are non-integer (incommensurate)")

# ---- 6. corrected filter polynomial ----
# p(x) = prod_{g>0} (x - E(g)) / (E(0) - E(g)); apply to H_eff
Pproj = np.eye(256)
for g in levels:
    if float(g) == 0.0:
        continue
    Pproj = Pproj @ (H_eff - E(float(g)) * np.eye(256)) / (ground_d - E(float(g)))
Omega = V[:, int(np.argmin(np.abs(ev)))]
Omega = Omega / np.linalg.norm(Omega)
err = np.max(np.abs(Pproj - np.outer(Omega, Omega)))
print(f"info: corrected-filter projector error = {err:.3e}", flush=True)
require(err < 1e-9,
        "6: corrected degree-7 filter in H_eff projects onto dressed ground "
        f"(projector error {err:.3e})")

result = {
    "checks": CHECKS,
    "count": len(CHECKS),
    "dressed_levels": {str(g): dressed[float(g)] for g in levels},
    "gap_dressed": gap,
    "gap_bare": J / 2,
    "bare_weight_dressed_ground": w_bare,
    "rephase_error_at_bare_filter_time_rad": max_phase_err,
    "dressed_spacing_ratios_in_gap_units": {str(g): r for g, r in zip(levels, dressed_ratios)},
    "corrected_filter_projector_error": float(err),
    "scope": ["effective matter-space model via M^dag M = 6I - 2G",
              "numerical double precision; star isolation remains a control access"],
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "seconds": time.time() - start,
}
Path(__file__).with_name("dressed_star.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"count": len(CHECKS), "gap_dressed": gap,
                  "rephase_error_rad": max_phase_err,
                  "filter_error": float(err)}, indent=2))
