"""Exact discriminating checks for the Fable kernel-question round (10 Sep 2026).

All statements are finite/exact model checks supporting the written proofs in
PROOF.md.  They are research documentation: no RH, factoring-speedup, TOE or
T1-T8 claim.  Only the Python standard library, numpy and mpmath are used; no
TFPT module is imported and no sealed artefact is modified.

Sections
  1. leak theorem for flux-only codes on the uncut rotor/CAR ring (candidate B)
  2. Z4 layer of the rotor with carry: exact conjugation law (candidate A)
  3. covering isometries, Cuntz radix, energy scaling (candidate C)
  4. zeta-Gibbs residue masses -> uniform Frobenius state at beta -> 1+ (C)
  5. modular multiplication as reduced covering; controlled-shift cost (D)
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import sys

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
SOURCES = [
    "../BRIEFING.md",
    "../context/TFPT-Globaler-Quellabschluss.md",
    "../context/TFPT-Markierter-Ursprung-der-Kopplung.md",
    "../context/Universalraum-Cap-und-physische-Dynamik.md",
    "../context/Universalraum-Masterprogramm-Pruefung.md",
    "../../det-wall-hh-rule/PROOF.md",
    "../../../../verification/v1027_signed_det_car_wall.py",
]

# Native ring couplings (Q047 section 1 / ground-state-loop-response).
A_LL, B_LH, C_LL2, EPS_L, M_H, E_EL = F(1, 12), F(1, 24), F(1, 576), F(1, 96), F(4), F(1, 200)
SITES = 4


def require(ok, message):
    if not ok:
        raise ValueError(message)


# --------------------------------------------------------------------------
# 1. Uncut rotor/CAR ring: exact sparse action and the leak theorem
# --------------------------------------------------------------------------
def fermion(mask, i, create):
    """Apply c_i (create=False) or c_i^dagger (create=True) with Jordan-Wigner sign."""
    occupied = (mask >> i) & 1
    if create == bool(occupied):
        return None, 0
    sign = -1 if bin(mask & ((1 << i) - 1)).count("1") % 2 else 1
    return mask ^ (1 << i), sign


def hop(state, amp, x, y, s_from, s_to):
    """c^dagger_{s_to,y} c_{s_from,x} U^{+-} on basis state (mask, E); ring links e_x: x->x+1."""
    mask, E = state
    i, j = x + SITES * s_from, y + SITES * s_to
    mask1, sgn1 = fermion(mask, i, False)
    if mask1 is None:
        return None
    mask2, sgn2 = fermion(mask1, j, True)
    if mask2 is None:
        return None
    E = list(E)
    if y == (x + 1) % SITES:
        E[x] += 1
    elif y == (x - 1) % SITES:
        E[y] -= 1
    else:
        raise ValueError("not a ring link")
    return (mask2, tuple(E)), amp * sgn1 * sgn2


def add(vec, key, amp):
    if amp == 0:
        return
    vec[key] = vec.get(key, 0) + amp
    if vec[key] == 0:
        del vec[key]


def gauss_ok(state):
    mask, E = state
    for x in range(SITES):
        q = ((mask >> x) & 1) + ((mask >> (x + SITES)) & 1) - 1
        if q + E[x] - E[(x - 1) % SITES] != 0:
            return False
    return True


def apply_H(vec):
    out = {}
    for state, amp in vec.items():
        mask, E = state
        nL = [(mask >> x) & 1 for x in range(SITES)]
        nH = [(mask >> (x + SITES)) & 1 for x in range(SITES)]
        diag = EPS_L * sum(nL) + M_H * sum(nH) + E_EL * sum(e * e for e in E)
        add(out, state, amp * diag)
        for x in range(SITES):
            for y in ((x + 1) % SITES, (x - 1) % SITES):
                for (sf, st, coef) in ((0, 0, A_LL), (0, 1, B_LH), (1, 0, B_LH)):
                    res = hop(state, amp * coef, x, y, sf, st)
                    if res:
                        add(out, *res)
                # two-link LL paths x -> y -> z (non-backtracking), both directions covered by x, y
                z = (2 * y - x) % SITES
                mid = hop(state, amp * C_LL2, x, y, 0, 0)
                if mid:
                    res = hop(mid[0], mid[1], y, z, 0, 0)
                    if res:
                        add(out, *res)
    return out


def inner(u, v):
    return sum(a * v[k] for k, a in u.items() if k in v)


def plaquette_S(state, power=1):
    """S = W(I-P3) + W^{-3}P3 with W = U_0U_1U_2U_3 (all four link fluxes +1), P3 keyed on link 0."""
    mask, E = state
    for _ in range(power % 4):
        shift = -3 if E[0] % 4 == 3 else 1
        E = tuple(e + shift for e in E)
    return (mask, E)


def leak_theorem():
    omega0 = (0b1111, (0, 0, 0, 0))  # all low occupied, zero flux
    require(gauss_ok(omega0), "Omega0 satisfies Gauss law")
    code = [{plaquette_S(omega0, a): F(1)} for a in range(4)]
    for a in range(4):
        require(gauss_ok(next(iter(code[a]))), "code state respects Gauss law")
        require(plaquette_S(next(iter(code[a])), 4) == next(iter(code[a])), "S^4 = I on code")
    # Z S = i S Z with Z = exp(i pi E_0 / 2): S raises E_0 by +1 mod 4.
    require(all((plaquette_S(next(iter(code[a])))[1][0] - next(iter(code[a]))[1][0]) % 4 == 1
                for a in range(4)), "S raises E_0 by one mod 4 (clock-shift relation)")
    HJ = [apply_H(v) for v in code]
    for w in HJ:
        require(all(gauss_ok(s) for s in w), "H preserves Gauss law")
    JHJ = [[inner(code[a], HJ[b]) for b in range(4)] for a in range(4)]
    JH2J = [[inner(HJ[a], HJ[b]) for b in range(4)] for a in range(4)]
    gamma = [[JH2J[a][b] - sum(JHJ[a][k] * JHJ[k][b] for k in range(4)) for b in range(4)]
             for a in range(4)]
    n_dir = 2 * SITES  # directed links of the ring
    expected = n_dir * B_LH * B_LH
    require(all(gamma[a][b] == (expected if a == b else 0) for a in range(4) for b in range(4)),
            "Gamma^dagger Gamma = N_dir b^2 I on the flux-only code")
    require(all(JHJ[a][b] == 0 for a in range(4) for b in range(4) if a != b),
            "compressed H is diagonal on the flux code")
    # Independence of flux content: a second flux-only code with other (Gauss-compatible,
    # hence uniform on the ring) loop fluxes.
    other = [{(0b1111, (k,) * SITES): F(1)} for k in (-7, 2, 5, 10)]
    require(all(gauss_ok(next(iter(v))) for v in other), "second code Gauss law")
    HO = [apply_H(v) for v in other]
    g2 = [[inner(HO[a], HO[b]) - sum(inner(other[a], HO[k]) * inner(other[k], HO[b]) for k in range(4))
           for b in range(4)] for a in range(4)]
    require(all(g2[a][b] == (expected if a == b else 0) for a in range(4) for b in range(4)),
            "leak is independent of the flux content")
    # Which terms leak: only L->H hops (Pauli blocks LL, no H for HL).
    leaked = {s for w in HJ for s in w if s not in {next(iter(v)) for v in code}}
    require(len(leaked) == 4 * n_dir and all(bin(s[0] >> SITES).count("1") == 1 for s in leaked),
            "leaked states carry exactly one high fermion, one per directed link and code vector")
    # Electric generator does not commute with S: compare H_E S Omega0 and S H_E Omega0.
    def electric(state):
        return E_EL * sum(e * e for e in state[1])
    s1 = plaquette_S(omega0)
    commutator = electric(s1) - electric(omega0)
    require(commutator == E_EL * 4, "[H_E, S] Omega0 = 4 e S Omega0 != 0")
    return {"N_directed_links": n_dir, "gamma_dagger_gamma_diagonal": str(expected),
            "cubic_torus_formula": "6 N b^2 = N/96 for N sites (N_dir = 6N)",
            "compressed_H_diagonal": [str(JHJ[a][a]) for a in range(4)],
            "electric_commutator_on_Omega0": str(commutator),
            "dressed_code": dressed_code(code, HJ, JHJ, expected)}


def scale(vec, factor):
    return {k: a * factor for k, a in vec.items()}


def axpy(out, vec, factor):
    for k, a in vec.items():
        add(out, k, a * factor)


def diagonal_energy(state):
    mask, E = state
    nL = sum((mask >> x) & 1 for x in range(SITES))
    nH = sum((mask >> (x + SITES)) & 1 for x in range(SITES))
    return EPS_L * nL + M_H * nH + E_EL * sum(e * e for e in E)


def leak_matrix(codevecs):
    """<d_a, H(I-P)H d_b> for an ORTHOGONAL (not necessarily normalized) family, exact.

    P = sum_k |d_k><d_k| / ||d_k||^2.  For normalized vectors this is Gamma^dagger Gamma.
    """
    HJ = [apply_H(v) for v in codevecs]
    n = len(codevecs)
    norms2 = [inner(v, v) for v in codevecs]
    JHJ = [[inner(codevecs[a], HJ[b]) for b in range(n)] for a in range(n)]
    JH2J = [[inner(HJ[a], HJ[b]) for b in range(n)] for a in range(n)]
    return [[JH2J[a][b] - sum(JHJ[k][a] * JHJ[k][b] / norms2[k] for k in range(n)) for b in range(n)]
            for a in range(n)]


def dressed_code(code, HJ, JHJ, bare_leak):
    """First-order Schrieffer-Wolff dressing of the flux code by the SOURCE Hamiltonian.

    J~_a = J_a - sum_h  <h|H|J_a> / (E_h - E_a) |h>,  h the leaked one-high states; then the
    exact residual leak Gamma~^dagger Gamma~ is computed on the (orthogonalized) dressed
    family.  Nothing about the desired response is inserted: only H and its diagonal energies.
    """
    dressed = []
    for a, v in enumerate(code):
        base = next(iter(v))
        Ea = JHJ[a][a]
        w = dict(v)
        for h, amp in HJ[a].items():
            if h == base:
                continue
            Eh = diagonal_energy(h)
            require(Eh != Ea, "nonresonant leak")
            add(w, h, -amp / (Eh - Ea))
        dressed.append(w)
    # Gram-Schmidt (exact) -- distinct flux sectors keep the family orthogonal, but verify.
    gram = [[inner(dressed[a], dressed[b]) for b in range(4)] for a in range(4)]
    require(all(gram[a][b] == 0 for a in range(4) for b in range(4) if a != b), "dressed vectors stay orthogonal")
    norms2 = [gram[a][a] for a in range(4)]
    # Leak of the unnormalized vectors, then normalize: Gamma~^dagger Gamma~ scaled by 1/(norm_a norm_b).
    leak = leak_matrix(dressed)
    diag_ratio = [leak[a][a] / norms2[a] for a in range(4)]
    require(all(0 < r < bare_leak / 100 for r in diag_ratio), "dressing reduces the leak by more than 1e2")
    high_weight = [sum(amp * amp for s, amp in dressed[a].items() if bin(s[0] >> SITES).count("1") == 1) / norms2[a]
                   for a in range(4)]
    # Where the residual leak lives: matter pattern census of H d_0 minus its code projection.
    Hd = apply_H(dressed[0])
    residual = dict(Hd)
    for k in range(4):
        axpy(residual, dressed[k], -inner(dressed[k], Hd) / norms2[k])
    census = {}
    for s, amp in residual.items():
        key = f"high={bin(s[0] >> SITES).count('1')},low={bin(s[0] & ((1 << SITES) - 1)).count('1')}"
        census[key] = census.get(key, F(0)) + amp * amp
    census = {k: float(v / norms2[0]) for k, v in census.items()}
    return {"bare_leak": str(bare_leak),
            "dressed_leak_diagonal": [str(r) for r in diag_ratio],
            "dressed_leak_float": [float(r) for r in diag_ratio],
            "reduction_factor": [float(bare_leak / r) for r in diag_ratio],
            "high_admixture_weight": [float(w) for w in high_weight],
            "residual_leak_census_a0": census,
            "note": "first-order source dressing by H itself; the residual leak is dominated by the LL hop (coefficient a) of the hole created by the LH admixture, i.e. by mobile dressed excitations; still extensive in volume"}


# --------------------------------------------------------------------------
# 2. Rotor Z4 layer with carry (candidate A)
# --------------------------------------------------------------------------
def rotor_layer(kappa=F(1, 100), t=F(3, 7), n_range=range(-9, 10)):
    """L|n> = |n+delta(n)>, delta = 1 (n mod 4 < 3), -3 (n mod 4 = 3).  Exact conjugation law:
    e^{-it k E^2/2} L e^{it k E^2/2} = L exp(-i t k (2 E delta(E) + delta(E)^2)/2)."""
    def delta(n):
        return -3 if n % 4 == 3 else 1
    for n in n_range:
        lhs_phase = F(n * n, 2) - F((n + delta(n)) ** 2, 2)      # exponent/(i t kappa) of LHS
        rhs_phase = -F(2 * n * delta(n) + delta(n) ** 2, 2)
        require(lhs_phase == rhs_phase, "conjugation law for L")
        # U = C L with C the controlled q-shift: U|n> = |n+1>; check n = 4q+r bookkeeping.
        q, r = divmod(n, 4)
        q2, r2 = divmod(n + 1, 4)
        require((q2 - q, r2) == ((1, 0) if r == 3 else (0, r + 1)), "carry bookkeeping")
        require(n * n == 16 * q * q + 8 * q * r + r * r, "E^2 = 16Q^2 + 8QR + R^2")
    require(all(((n + delta(n)) % 4 - (n + 1) % 4) % 4 == 0 for n in n_range), "L = Z4 shift on r")
    return {"conjugation_law": "Ad_{exp(-it kE^2/2)}(L) = L * f_t(E), f_t(E) = exp(-itk(2E delta(E)+delta(E)^2)/2)",
            "closed_algebra": "Alg(L, E) = direct sum over q of M_4 with q-dependent phases; U = C L, C = controlled q-shift",
            "coupling_term": "8QR"}


# --------------------------------------------------------------------------
# 3. Covering isometries and Cuntz radix (candidate C)
# --------------------------------------------------------------------------
def coverings(n_max=40):
    idx = {n: k for k, n in enumerate(range(-n_max, n_max + 1))}
    dim = len(idx)

    def op(f):
        M = np.zeros((dim, dim))
        for n in idx:
            m = f(n)
            if m in idx:
                M[idx[m], idx[n]] = 1
        return M
    U = op(lambda n: n + 1)
    E = np.diag([float(n) for n in idx])
    inner_vec = np.zeros(dim)
    for n in range(-5, 6):
        inner_vec[idx[n]] = 1 / math.sqrt(11)
    results = {}
    for m in (2, 3, 5, 6):
        S = op(lambda n, m=m: m * n)
        require(np.allclose((S @ U - np.linalg.matrix_power(U, m) @ S) @ inner_vec, 0), "S_m U = U^m S_m")
        require(np.allclose((E @ S - m * S @ E) @ inner_vec, 0), "E S_m = m S_m E")
        require(np.allclose((E @ E @ S - m * m * S @ E @ E) @ inner_vec, 0), "E^2 S_m = m^2 S_m E^2")
        core = [idx[n] for n in idx if abs(m * n) <= n_max]  # truncation-free columns
        require(np.allclose((S.T @ S)[np.ix_(core, core)], np.eye(len(core))), "S_m isometric")
    S2, S3, S6 = (op(lambda n, m=m: m * n) for m in (2, 3, 6))
    require(np.allclose((S2 @ S3 - S6) @ inner_vec, 0), "S_2 S_3 = S_6 (degree monoid)")
    # Cuntz radix: T_r = U^r S_4, r = 0..3, sum T_r T_r^* = I on the interior.
    T = [np.linalg.matrix_power(U, r) @ op(lambda n: 4 * n) for r in range(4)]
    P = sum(t @ t.T for t in T)
    interior = [idx[n] for n in range(-8, 9)]
    require(np.allclose(P[np.ix_(interior, interior)], np.eye(len(interior))), "Cuntz completeness on interior")
    core = [idx[n] for n in idx if abs(4 * n) + 3 <= n_max]
    require(all(np.allclose((T[r].T @ T[s])[np.ix_(core, core)], np.eye(len(core)) if r == s else 0)
                for r in range(4) for s in range(4)), "Cuntz orthogonality T_r^* T_s = delta_rs")
    results["relations"] = ["S_m U = U^m S_m", "E S_m = m S_m E", "E^2 S_m = m^2 S_m E^2",
                            "S_m S_k = S_mk", "T_r = U^r S_4 Cuntz"]
    results["energy_scaling"] = "degree-m covering multiplies the electric energy kappa E^2/2 by m^2"
    return results


# --------------------------------------------------------------------------
# 4. zeta-Gibbs residue masses and the beta -> 1+ limit (candidate C, report 7.1)
# --------------------------------------------------------------------------
def gibbs_residues():
    mp.mp.dps = 30
    chi4 = [0, 1, 0, -1]
    rows = []
    for beta in (mp.mpf(2), mp.mpf("1.5"), mp.mpf("1.1"), mp.mpf("1.01"), mp.mpf("1.001"), mp.mpf("1.0001")):
        z = mp.zeta(beta)
        L4 = mp.dirichlet(beta, chi4)
        m0 = 4 ** (-beta)
        m2 = 2 ** (-beta) * (1 - 2 ** (-beta))
        m1 = ((1 - 2 ** (-beta)) + L4 / z) / 2
        m3 = ((1 - 2 ** (-beta)) - L4 / z) / 2
        require(abs(m0 + m1 + m2 + m3 - 1) < mp.mpf(10) ** -25, "residue masses sum to one")
        # direct partial-sum control at beta = 2
        if beta == 2:
            direct = [mp.nsum(lambda k, r=r: (4 * k + r) ** (-beta), [1 if r == 0 else 0, mp.inf]) / z for r in range(4)]
            require(all(abs(direct[r] - [m0, m1, m2, m3][r]) < mp.mpf(10) ** -20 for r in range(4)),
                    "closed forms agree with direct sums")
        rows.append({"beta": str(beta), "mass_mod4": [mp.nstr(x, 12) for x in (m0, m1, m2, m3)],
                     "max_deviation_from_quarter": mp.nstr(max(abs(x - mp.mpf(1) / 4) for x in (m0, m1, m2, m3)), 6)})
    devs = [mp.mpf(r["max_deviation_from_quarter"]) for r in rows]
    require(all(devs[i + 1] < devs[i] for i in range(len(devs) - 1)), "deviation from 1/4 decreases toward beta=1")
    require(devs[-1] < mp.mpf("1e-3"), "uniform Z4 state recovered at the critical point")
    # Divisibility moments: Pr_beta(n | X) = n^{-beta} for every n (report 7.1 family mu_s with s = beta).
    for n in (2, 3, 4, 6):
        require(abs(mp.nsum(lambda k, n=n: (n * k) ** (-mp.mpf(2)), [1, mp.inf]) / mp.zeta(2) - n ** (-mp.mpf(2))) < mp.mpf(10) ** -25,
                "divisibility moment n^{-beta}")
    return {"rows": rows, "identification": "zeta-Gibbs residue law = report family mu_s at s=beta; beta->1+ gives Haar on Z-hat, i.e. the equal-weight Z4 Frobenius state",
            "H_log_vs_H_E": "on the loop sector H_E = (kappa/2) exp(2 H_log) on |E|>0: same eigenbasis, incompatible Gibbs states"}


# --------------------------------------------------------------------------
# 5. Modular multiplication as reduced covering (candidate D)
# --------------------------------------------------------------------------
def modular_covering(N=91, a=2):
    require(math.gcd(a, N) == 1, "unit multiplier")
    Ua = np.zeros((N, N), dtype=complex)
    for x in range(N):
        Ua[(a * x) % N, x] = 1
    Fm = np.array([[np.exp(-2j * np.pi * j * k / N) for k in range(N)] for j in range(N)]) / np.sqrt(N)
    ainv = pow(a, -1, N)
    Uinv = np.zeros((N, N), dtype=complex)
    for x in range(N):
        Uinv[(ainv * x) % N, x] = 1
    require(np.allclose(Fm @ Ua @ Fm.conj().T, Uinv), "F_N U_a F_N^* = U_{a^{-1}}")
    order = 1
    while pow(a, order, N) != 1:
        order += 1
    require(order == 12, "order of 2 mod 91 is 12")
    # cycle structure of x -> a x mod N and controlled-shift decomposition U_a = sum_k W^k 1_{(a-1)x = k}
    seen, cycles = set(), []
    for x in range(N):
        if x in seen:
            continue
        cyc, y = [], x
        while y not in seen:
            seen.add(y); cyc.append(y); y = (a * y) % N
        cycles.append(len(cyc))
    shifts = {((a - 1) * x) % N for x in range(N)}
    require(len(shifts) == N // math.gcd(a - 1, N), "number of distinct controlled shifts")
    eig = np.linalg.eigvals(Ua)
    require(np.allclose(np.sort_complex(eig ** 12), 1), "spectrum of U_2 on Z_91 consists of 12th roots of unity")
    return {"N": N, "a": a, "order": order, "cycle_lengths": sorted(set(cycles)),
            "controlled_shifts_needed": len(shifts),
            "identification": "U_a = S_a mod N: the degree-a covering reduced to the Z_N clock; a flux-controlled loop operation sum_k W^k 1_{(a-1)x=k}(E)",
            "cost_note": "N/gcd(a-1,N) distinct controlled loop powers, or O(log N) controlled multiplications with an extra register (repeated squaring); no speedup over standard order finding"}


def manifest():
    out = {}
    for rel in SOURCES:
        p = (HERE / rel).resolve()
        out[str(p.relative_to(HERE.parents[3]))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def record():
    return {
        "status": "FABLE_KERNFRAGEN_EXACT_CHECKS",
        "claims_not_made": ["no RH statement", "no factoring speedup", "no TOE/T1-T8 closure",
                            "no derivation of the wall premise or of P1/P2 consequences"],
        "leak_theorem": leak_theorem(),
        "rotor_layer": rotor_layer(),
        "coverings": coverings(),
        "gibbs_residues": gibbs_residues(),
        "modular_covering": modular_covering(),
        "sources_sha256": manifest(),
    }


if __name__ == "__main__":
    out = record()
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "checks.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
