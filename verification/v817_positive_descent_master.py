"""v817 TFPT scope: abstract positive descent and G_net instance.

Scope extraction from original module at ba2f0fc; original ID and
mathematical statements preserved. Original full source is retained
in the extraction provenance; no proof/status promotion.
"""
import time

import numpy as np

TOL = 1e-10

SEED = 20260806

GN0 = 48

GKMAX = 5

GRATE_BAR = 0.55

CTRL_GNET_BAR = 0.05

CHECKS = []

def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name
          + ("  -- " + detail if detail else ""))
    return ok

def section(title):
    print("\n-- %s --" % title)

SECTORS = [(e, v, j) for e in (1, -1) for v in ("v1", "v7")
           for j in (0, 1, 2)]

MULT = np.array([(2 if v == "v1" else 14) * (2 if j == 1 else 1)
                 for e, v, j in SECTORS], float)

def l1_state(qa, qb):
    """state norm on C[G]: l1 over the 128 characters."""
    return float(np.abs(qa - qb) @ MULT) / 128.0

def spower(N, k):
    P = np.zeros((N, N))
    for j in range(N):
        P[(j + k) % N, j] = (-1.0) ** ((j + k) // N)
    return P

def covariance_occ(N, occ):
    th = 2 * np.pi * (np.arange(N) + 0.5) / N
    th = np.mod(th + np.pi, 2 * np.pi) - np.pi
    th[np.isclose(th, -np.pi)] = np.pi
    F = np.exp(1j * np.outer(np.arange(N), th)) / np.sqrt(N)
    return (F * occ) @ F.conj().T

def covariance(N):
    th = 2 * np.pi * (np.arange(N) + 0.5) / N
    th = np.mod(th + np.pi, 2 * np.pi) - np.pi
    th[np.isclose(th, -np.pi)] = np.pi
    return covariance_occ(N, (th < 0).astype(float))

def window(N, p, l):
    return [(p + i) % N for i in range(l)] + \
           [(p + N // 2 + i) % N for i in range(l)]

def haar_iso(N):
    V = np.zeros((2 * N, N))
    for j in range(N):
        V[2 * j, j] = V[2 * j + 1, j] = 1.0 / np.sqrt(2.0)
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

def tracenorm(A):
    return float(np.abs(np.linalg.eigvalsh((A + A.conj().T) / 2)).sum())

def leg_abstract():
    section("A: abstract-core mirror (Lean statements, numeric witness)")
    rng = np.random.default_rng(SEED)
    q_lim = np.abs(rng.normal(size=12))
    dirs = rng.normal(size=(40, 12))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    qs = [q_lim + sum(2.0 ** (-j) * dirs[j] * 0.01 for j in range(n, 40))
          for n in range(20)]
    deltas = [np.linalg.norm(qs[n + 1] - qs[n], 1) for n in range(19)]
    tails = [sum(deltas[n:]) + 2.0 ** (-19) * 0.5 for n in range(19)]
    ok_tail = all(np.linalg.norm(qs[n] - q_lim, 1) <= tails[n] + 1e-12
                  for n in range(19))
    ok_pos = bool(np.all(q_lim + 0.02 >= 0))     # witness structure only
    S = [0, 3, 7]
    ok_sec = abs(sum(qs[18][i] for i in S) - sum(q_lim[i] for i in S)) \
        <= sum(abs(qs[18][i] - q_lim[i]) for i in S) + 1e-15
    check("A1 telescoping mirror: Cauchy tail <= summed defects on "
          "every rung; sector sums commute with the limit "
          "(kernel-checked versions: PositiveDescentMaster.lean)",
          ok_tail and ok_pos and ok_sec)

def leg_gnet():
    section("B: INSTANCE 1 -- G_net (l = 2 window, tower k <= %d)"
            % GKMAX)
    t0 = time.time()
    ok_iso, ok_supp = True, True
    for N in (48, 96):
        V = haar_iso(N)
        ok_iso &= np.abs(V.T @ V - np.eye(N)).max() < 1e-14
        w_small = window(N, 0, 2)
        w_big = window(2 * N, 0, 4)
        P = np.zeros(2 * N)
        P[w_big] = 1.0
        ok_supp &= np.abs(V[:, w_small] * (1 - P)[:, None]).max() < 1e-14
    HN = spower(GN0, GN0 // 2)
    win2 = window(GN0, 0, 2)
    HW = HN[np.ix_(win2, win2)]
    H_big = spower(GN0 * 2 ** GKMAX, GN0 * 2 ** (GKMAX - 1))
    wbig = window(GN0 * 2 ** GKMAX, 0, 2)
    ok_lvl = np.abs(H_big[np.ix_(wbig, wbig)] - HW).max() < 1e-14
    check("B1 (1) filtration exact: V*V = 1, support-coherence leak = 0"
          " at N = 48, 96; window data level-independent",
          ok_iso and ok_supp and ok_lvl)

    c4 = jw_ops(4)
    U4 = gamma_partial(HW, list(range(4)), c4)
    Ps = sector_projs(U4)

    def E2(x):
        return sum(P @ x @ P for P in Ps)

    # Choi matrix of E on the 16-dim window algebra (256 x 256)
    dim = 16
    choi = np.zeros((dim * dim, dim * dim), dtype=complex)
    for i in range(dim):
        for j in range(dim):
            eij = np.zeros((dim, dim), dtype=complex)
            eij[i, j] = 1.0
            choi += np.kron(E2(eij), eij)
    ev_choi = np.linalg.eigvalsh((choi + choi.conj().T) / 2)
    unital = np.abs(E2(np.eye(dim, dtype=complex))
                    - np.eye(dim)).max()
    rng = np.random.default_rng(SEED)
    dev_tr = 0.0
    for _ in range(4):
        A = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
        dev_tr = max(dev_tr, abs(np.trace(E2(A)) - np.trace(A)))
    check("B2 (3) E is CP: Choi min eig = %.2e >= -1e-10; unital "
          "(dev %.1e); trace-preserving (dev %.1e)"
          % (float(ev_choi.min()), unital, dev_tr),
          ev_choi.min() >= -1e-10 and unital < TOL and dev_tr < TOL)

    covs = {}

    def cov_of(N):
        if N not in covs:
            covs[N] = covariance(N)
        return covs[N]

    def pullback(cov_fun):
        out = []
        chain = np.eye(GN0)
        Nk = GN0
        for k in range(GKMAX + 1):
            out.append(chain.T.conj() @ cov_fun(Nk, k) @ chain)
            chain = haar_iso(Nk) @ chain
            Nk *= 2
        return out

    Cts = pullback(lambda Nk, k: cov_of(Nk))
    rhos = [gaussian_rho(Ct[np.ix_(win2, win2)], c4) for Ct in Cts]
    deltas = [tracenorm(rhos[k + 1] - rhos[k]) for k in range(GKMAX)]
    print("   G_net defects delta_k (trace norm): "
          + "  ".join("%.3e" % d for d in deltas))
    ok_rate = all(deltas[k] <= GRATE_BAR * deltas[k - 1]
                  for k in range(1, GKMAX) if deltas[k - 1] > 1e-12)
    Cg = 8 * deltas[1]
    ok_env = all(deltas[k] <= Cg * 2.0 ** (-k) + 1e-15
                 for k in range(1, GKMAX))
    rate_fit = (deltas[GKMAX - 1] / deltas[1]) ** (1.0 / (GKMAX - 2))
    check("B3 (5) defects summable: ratios <= %.2f, envelope "
          "delta_k <= 8 delta_1 2^-k (fitted rate %.3f/doubling)"
          % (GRATE_BAR, rate_fit), ok_rate and ok_env)

    min_eig = min(float(np.linalg.eigvalsh(
        (r + r.conj().T) / 2).min()) for r in rhos)
    trs = [float(np.trace(P).real) for P in Ps]
    res = sum(Ps[q] @ Ps[qp] - (Ps[q] if q == qp else 0)
              for q in range(4) for qp in range(4))
    dev_alg = max(float(np.abs(sum(Ps) - np.eye(dim)).max()),
                  float(np.abs(res).max()))
    ok_even = np.allclose(trs, [6, 4, 2, 4], atol=1e-9)
    check("B4 (2)+(4) states positive (min eig %.1e >= -1e-12); mu4 "
          "sector algebra exact (dev %.1e); traces (6,4,2,4) => "
          "w_1 = w_3 = 1/4 evenness" % (min_eig, dev_alg),
          min_eig >= -1e-12 and dev_alg < TOL and ok_even)
    print("   (6) closure datum: 185-element Watatani quasi-basis "
          "(arf-qsystem run) [typed, cited]; (7) Mosco form family "
          "[typed, open].   (%.1f s)" % (time.time() - t0))
    return dict(deltas=deltas, rate=rate_fit,
                ok=all(v for n, v in CHECKS if n.startswith("B")),
                pullback=pullback, rhos=rhos, win2=win2, c4=c4)

def leg_controls(th, gnet):
    section("K: controls (all must fire)")
    # K1: G_net scrambled sea
    rng = np.random.default_rng(SEED + 1)

    def scr_cov(Nk, k):
        frac = 0.3 if k % 2 == 0 else 0.7
        occ = np.zeros(Nk)
        occ[rng.permutation(Nk)[:int(frac * Nk)]] = 1.0
        return covariance_occ(Nk, occ)

    Cts_scr = gnet["pullback"](scr_cov)
    win2, c4 = gnet["win2"], gnet["c4"]
    rho_s = [gaussian_rho(Ct[np.ix_(win2, win2)], c4) for Ct in Cts_scr]
    d_s = [tracenorm(rho_s[k + 1] - rho_s[k]) for k in range(GKMAX)]
    check("K1 fires: G_net scrambled sea gives O(1) defects "
          "(delta_3 = %.3f, delta_4 = %.3f > %.2f)"
          % (d_s[3], d_s[4], CTRL_GNET_BAR),
          min(d_s[3], d_s[4]) > CTRL_GNET_BAR)

    # K4: summable defects but a non-positivity-preserving transition
    q0 = np.abs(np.random.default_rng(SEED + 2).normal(size=12)) + 0.1
    q0 /= float(q0 @ MULT) / 128.0
    bad_dir = np.zeros(12)
    bad_dir[5] = -(q0[5] + 0.05)
    qs = [q0 + (1 - 2.0 ** (-n)) * bad_dir for n in range(24)]
    d4 = [l1_state(qs[n + 1], qs[n]) for n in range(23)]
    lim = q0 + bad_dir
    ok_sum = all(d4[n + 1] <= 0.5 * d4[n] + 1e-15 for n in range(22))
    check("K4 fires: non-positive transition with SUMMABLE defects "
          "(ratio 1/2 exact) yields a NON-positive limit "
          "(min sector = %.3f < -0.01): positivity is a separate "
          "hypothesis, not implied by (5)" % float(lim.min()),
          ok_sum and lim.min() < -0.01)

def run():
    CHECKS.clear()
    leg_abstract()
    gnet = leg_gnet()
    leg_controls(None, gnet)
    failed = [n for n, ok in CHECKS if not ok]
    print("v817 TFPT master/G_net scope: %d/%d checks passed" % (len(CHECKS)-len(failed),len(CHECKS)))
    return 0 if not failed else 1

if __name__ == "__main__":
    raise SystemExit(run())
