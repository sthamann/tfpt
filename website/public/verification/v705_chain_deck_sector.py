"""v705 TFPT scope: original D1 physical NS-circle lift and deck sectors.
The prime arch-density/digamma application, continuum fit and controls are
maintained in Prime Front under the original v705 module identifier.
No physical selector or RH result is inferred from this finite identity.
"""
import math
import numpy as np
from tfpt_constants import check, reset, summary

def ns_shift(N):
    S = np.zeros((N, N))
    for i in range(N - 1):
        S[i, i + 1] = 1.0
    S[N - 1, 0] = -1.0
    return S

def channel(b, t):
    return np.exp(-b * t) / (1.0 - np.exp(-6.0 * t))

def run():
    reset()
    N0 = 48
    T_GRID = np.linspace(0.5, 3.0, 51)
    BAR_EXACT = 1e-12
    # ------------------------------------------------------------- D1
    print("\nD1 -- the v623 lift and its deck classes")
    S = ns_shift(N0)
    ev = np.linalg.eigvals(S)
    ph = np.sort(np.mod(np.angle(ev), 2.0 * math.pi))
    ph_ref = np.sort(np.array([(m * math.pi / N0) % (2 * math.pi)
                               for m in range(1, 2 * N0, 2)]))
    dev_ph = float(np.max(np.abs(ph - ph_ref)))
    L = np.linalg.matrix_power(S, 4)
    Dk = np.linalg.matrix_power(S, 16)
    dev_L12 = float(np.max(np.abs(
        np.linalg.matrix_power(L, 12) + np.eye(N0))))
    dev_Dk3 = float(np.max(np.abs(
        np.linalg.matrix_power(Dk, 3) + np.eye(N0))))
    # deck charge per mode m: exp(i pi m/3) -> nu = m/6 mod 1
    ms = np.arange(1, 2 * N0, 2)
    nus = np.mod(ms / 6.0, 1.0)
    cnt = {v: int(np.sum(np.isclose(nus, v)))
           for v in (1.0 / 6.0, 0.5, 5.0 / 6.0)}
    check("D1.1 [E] 48-site NS lift: eigenphases m pi/48 (m odd, dev "
          "%.1e); clock L = S^4: L^12 = -1 (dev %.1e, order 12 "
          "spin-doubled); deck Dk = L^4: Dk^3 = -1 (dev %.1e, "
          "projective mu3 = the fermion spin doubling); deck charges "
          "nu = m/6 mod 1 with counts %s == v628 twist classes "
          "{1/6, 1/2, 5/6} x 16"
          % (dev_ph, dev_L12, dev_Dk3,
             {("%d/6" % round(6 * k)): v for k, v in cnt.items()}),
          dev_ph <= 1e-12 and dev_L12 <= 1e-9 and dev_Dk3 <= 1e-9
          and all(v == 16 for v in cnt.values()))


    # ------------------------------------------------------------- D2
    print("\nD2 -- clock-character selection of the selected half-turn tower")
    t = T_GRID
    rho = np.exp(-t / 2.0) / (1.0 - np.exp(-2.0 * t))
    tow1 = sum(np.exp(-(2.0 * k + 0.5) * t) for k in range(400))
    tow3 = sum(np.exp(-(2.0 * k + 1.5) * t) for k in range(400))
    dev1 = float(np.max(np.abs(rho - tow1) / rho))
    dev3 = float(np.min(np.abs(rho - tow3) / rho))
    # half-turn eigenvalue of class m == 1 mod 4: exp(i pi m/2) = +i
    ht = set(np.round(np.mod(ms[ms % 4 == 1] * 0.5, 2.0), 9))
    check("D2.1 [E] rho(t) == the {m == 1 mod 4} half-tower (rel dev "
          "%.1e <= 1e-12); this class is EXACTLY the half-turn-"
          "eigenvalue-(+i) eigenspace (S^24 phase pi m/2, unique "
          "value %s x pi/2); the opposite class {m == 3 mod 4} "
          "misses rho by %.0f%% (min rel dev) -- the chosen half-turn convention "
          "selects ONE clock character; WHY this one = the supplied half-turn "
          "semantics, typed OPEN"
          % (dev1, sorted(ht), 100 * dev3),
          dev1 <= BAR_EXACT and dev3 > 0.3 and ht == {0.5})

    # ------------------------------------------------------------- D3
    print("\nD3 -- deck split of the selected half-turn tower == deck channel series")
    ok3 = True
    dev_max = 0.0
    scal_inf = []
    for r, b, nu in ((1, 0.5, "1/6"), (5, 2.5, "5/6"),
                     (9, 4.5, "1/2")):
        tow = sum(np.exp(-(6.0 * k + b) * t) for k in range(140))
        ch = channel(b, t)
        dev = float(np.max(np.abs(tow - ch) / ch))
        dev_max = max(dev_max, dev)
        ok3 &= dev <= BAR_EXACT
        scal_inf.append(float(tow[-1] / ch[-1]))
        print("   sector m == %d mod 12 (deck nu = %s): tower == "
              "e^{-%.1ft}/(1-e^{-6t}), rel dev %.1e" % (r, nu, b, dev))
    check("D3.1 [E] EXACT: the three deck sectors of the selected half-turn tower "
          "ARE the three deck channel series b in {1/2, 5/2, 9/2} "
          "(max rel dev %.1e <= 1e-12); global scalar forced to 1 "
          "by the t->inf asymptote (measured %s); deck charges "
          "{1/6, 5/6, 1/2} = v628 twists" % (dev_max,
          ["%.6f" % s_ for s_ in scal_inf]),
          ok3 and all(abs(s_ - 1) < 1e-9 for s_ in scal_inf))


    return summary("v705 original NS-circle deck identity")

if __name__ == "__main__":
    raise SystemExit(run())
