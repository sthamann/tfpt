"""v807: TFPT physical addendum to E8.ONEOBJECT.01.
Original S1 RR/Serre/null-spinor identities only, extracted unchanged
from v807_lorentz_nullselector at ba2f0fc. Dedicated PRIME.LORENTZ.SPINOR.01
window dynamics and conditional seam-family tests live in Prime Front.
The algebra is conditional on the stated functor/rank-one assignment.
"""
import sympy as sp
import tfpt_constants as tc
from tfpt_constants import check, reset, summary

def M_of(t, x, y):
    return sp.Matrix([[t + x, y], [y, t - x]])

def run():
    reset()
    D_RANGE = range(1,13)
    ABS_MU4 = 4
    ABS_Z2 = 2
    d_ = sp.Symbol("d", positive=True)
    g_, N_, gl_ = d_ + 1, d_ - 1, d_
    norm = sp.expand(g_**2 - N_**2 - gl_**2)
    Md_sym = M_of(g_, -N_, gl_)
    detMd = sp.expand(Md_sym.det())
    check("S1.1 [E neu] |v_d|^2_L = (d+1)^2 - (d-1)^2 - d^2 = %s = "
          "d(4-d) IDENTICALLY, and M(v_d) = [[2, d],[d, 2d]] "
          "(entries %s) with det M_d = %s = the same d(4-d) -- the "
          "null condition and the rank-one condition are ONE equation"
          % (norm, tuple(Md_sym), detMd),
          sp.simplify(norm - d_ * (4 - d_)) == 0
          and sp.simplify(detMd - d_ * (4 - d_)) == 0
          and Md_sym[0, 0] == 2 and Md_sym[0, 1] == d_
          and Md_sym[1, 1] == 2 * d_)

    print("\n    the d-table (exact integers):")
    print("    %3s %6s %6s %6s | %8s %10s | %6s %6s"
          % ("d", "g=d+1", "N=d-1", "glue", "|v|^2_L", "type",
             "detM_d", "rankM"))
    tab_ok = True
    null_set = []
    for d in D_RANGE:
        nm = (d + 1)**2 - (d - 1)**2 - d**2
        Md = sp.Matrix([[2, d], [d, 2 * d]])
        dM = int(Md.det())
        rk = Md.rank()
        typ = ("TIMELIKE" if nm > 0 else
               ("NULL" if nm == 0 else "SPACELIKE"))
        if nm == 0:
            null_set.append(d)
        expect_typ = ("TIMELIKE" if d < 4 else
                      ("NULL" if d == 4 else "SPACELIKE"))
        expect_rk = 1 if d == 4 else 2
        tab_ok = tab_ok and nm == d * (4 - d) and dM == nm \
            and typ == expect_typ and rk == expect_rk
        print("    %3d %6d %6d %6d | %8d %10s | %6d %6d"
              % (d, d + 1, d - 1, d, nm, typ, dM, rk))
    check("S1.2 the d-table is exact: |v_d|^2 = d(4-d) with d < 4 "
          "TIMELIKE, d = 4 NULL, d > 4 SPACELIKE on d = 1..12; the "
          "null set is %s = {4} EXACTLY" % null_set,
          tab_ok and null_set == [4])

    M4 = sp.Matrix([[2, 4], [4, 8]])
    spin = sp.Matrix([1, 2])
    fac = sp.simplify(M4 - 2 * spin * spin.T)
    check("S1.3 rank census: rank M_d = 2 for every d in 1..12 except "
          "d = 4 (rank 1, det = 0), where the factorization M_4 = "
          "2 (1,2)^T (1,2) is exact (residual %s) -- the rank-one "
          "square root at the null point is EXACTLY the parent "
          "probe's certified spinor square" % fac,
          fac == sp.zeros(2, 2))

    def h0_P1(deg):
        return deg + 1 if deg >= 0 else 0

    def h1_P1(deg):                     # Serre: h^1(O(k)) = h^0(O(-k-2))
        return h0_P1(-deg - 2)

    coh_ok = all(h0_P1(d) == d + 1 and h1_P1(-d) == d - 1
                 for d in D_RANGE)
    check("S1.4 the functor content is honest cohomology arithmetic: "
          "g = h^0(P^1, O(d)) = d+1 (RR) and N = h^1(P^1, O(-d)) = "
          "h^0(O(d-2)) = d-1 (Serre) as exact integer functions on "
          "d = 1..12; at d = 4: (g, N) = (5, 3) = (g_car, N_fam) -- "
          "the v499/Deligne reading (chi(O(d)) = d+1, anchor degree "
          "-4, h^1(O(-a_i)) = a_i - 1)",
          coh_ok and h0_P1(4) == int(tc.g_car)
          and h1_P1(-4) == int(tc.N_fam))

    a_anchor = (1, 1, 2)
    e1 = sum(a_anchor)
    e2 = (a_anchor[0] * a_anchor[1] + a_anchor[0] * a_anchor[2]
          + a_anchor[1] * a_anchor[2])
    e3 = a_anchor[0] * a_anchor[1] * a_anchor[2]
    i_s, j_s = 1, 2                      # the spinor = anchor support
    t_ = sp.Symbol("t")
    chi_a = sp.expand((t_ - 1)**2 * (t_ - 2))
    chi_ref = t_**3 - e1 * t_**2 + e2 * t_ - e3
    check("S1.5 anchor identification: a = (1,1,2) has e_k(a) = "
          "(%d, %d, %d) = (|mu4|, g_car, |Z2|) (v23/origin_theory "
          "convention; chi_a = (t-1)^2(t-2) = %s); the spinor (1,2) "
          "is the SUPPORT (distinct values) of the anchor multiset, "
          "and EXACTLY: i+j = %d = N_fam, i*j = %d = e3 = |Z2|, "
          "i^2+j^2 = %d = e2 = g_car, 2ij = %d = e1 = |mu4| -- "
          "'(1,2) is the nontrivial anchor content' is these four "
          "exact identities"
          % (e1, e2, e3, chi_a, i_s + j_s, i_s * j_s,
             i_s**2 + j_s**2, 2 * i_s * j_s),
          (e1, e2, e3) == (ABS_MU4, int(tc.g_car), ABS_Z2)
          and sp.simplify(chi_a - chi_ref) == 0
          and sorted(set(a_anchor)) == [1, 2]
          and i_s + j_s == int(tc.N_fam)
          and i_s * j_s == ABS_Z2
          and i_s**2 + j_s**2 == int(tc.g_car)
          and 2 * i_s * j_s == ABS_MU4)

    return summary("v807 RR/Serre/null-spinor physical addendum")

if __name__ == "__main__":
    raise SystemExit(run())
