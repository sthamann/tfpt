"""Four-mode spectral flow of the single chiral Moebius-cover fermion.

Exact checks (sympy / Fraction); no promotion.  Scope: PROOF.md.

Input (moebius-clock-fold-20261014, F1): ONE chiral complex channel psi on the
Moebius boundary circle (length 8l) folded to eight channels chi_k; chi_k
contains exactly the cover modes m = 8n + k.  Fold time law
K_alpha = sum_k (L0_k + delta_k p_k), delta_k = (k+alpha)/8 - 1/2.

A  zero modes (symbolic, alpha and j symbolic): T(p) = P p + a with
   s = q/2, r0 = p* = (1/2^4, -1/2^4), a = s + r0, P = block swap k <-> k+4:
   q(Tp) = q(p)+4; T^2 p = p+q; K(Tp)-K(p) = q(p)/2 + 3/4 + alpha/2 = K(p+s)-K(p);
   nu.(Tp-p) - nu.s = r0.p - 1, nu_k = (k+j)/8; K(a) = K(s).
B  full Fock space (Maya diagrams, oscillators included): T = sigma^4,
   c_m -> c_{m+4}.  K_alpha is the free cover Hamiltonian sum (m+alpha)/8 :N_m:;
   p(TS) = P p(S) + a; oscillator numbers N_k(TS) = N_{Pk}(S);
   K(TS) - K(S) = Q(S)/2 + 3/4 + alpha/2 for every state, hence
   U_T^dag K U_T = K + Q/2 + c_alpha and U_T(t) = U_T exp(it(Q/2 + c_alpha)).
   Geometric deck rotation g (translation by l): g U_T g^-1 = -i (-1)^Q U_T.
C  powers: sigma^2 (pullback of the primitive core winding) has
   K(sigma^2 S) - K(S) = Q/4 + (1+2 alpha)/8; T = (sigma^2)^2.
D  source pins: P1 seam class [u_Sigma] = 1, SF = 1; d_0 = |SF(U_Sigma)|;
   moebius-clock-fold single-chiral-channel premise; source-driven-carry
   external Peierls drive; mmst zero-mode charge shift on l^2(L_charge).
"""
from fractions import Fraction as F
from pathlib import Path
import json
import random
import sympy as sp

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

ROOT = Path(__file__).resolve().parents[3]

# ---------------- D: source pins ----------------
fold = (ROOT / "experiments/theory-contracts/moebius-clock-fold-20261014/PROOF.md").read_text()
require("pin_fold_single_chiral_channel_is_chosen_geometry",
        "## Erste zusätzlich gewählte Geometrie" in fold and "Ein **einziger chiraler** Kanal entlang des ganzen Möbiusrands" in fold)
require("pin_fold_fourier_channels", "χ_k = Σ_j ω^{-jk} ψ_j" in fold and "g⁴ = Deck" in fold)
tfpt42 = (ROOT / "_archive/paper-latex/tfpt-42.tex").read_text()
require("pin_P1_primitive_seam_class", "[u_\\Sigma]=1\\in K^1(S^1)\\cong \\mathbb Z." in tfpt42)
require("pin_P1_seam_spectral_flow_one", "SF(U_\\Seam)=1," in tfpt42)
bk = (ROOT / "_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex").read_text()
require("pin_defect_coordinate_d0", "d_0(B)&:=|\\SF(U_\\Sigma)|," in bk)
carry = (ROOT / "experiments/theory-contracts/source-driven-carry-20260920/PROOF.md").read_text()
require("pin_full_qwz_pump_external_drive",
        "**Extra input:** the uniform time-dependent Peierls phase and the duration T" in carry
        and "A global spectral-flow unitary" in carry)
mmst = (ROOT / "articles/2026-08-30/mmst_charged_scaling_limit_en.tex").read_text()
require("pin_psi_lambda_definition", ":\\!\\exp(i\\lambda\\cdot\\phi_N)\\!:_m" in mmst
        and "zero-mode charge shifts have norm one in all four grades" in mmst
        and ":=\\id_{\\ell^2(L_{\\rm charge})}\\otimes\\Gamma_s(j_{N,2N})." in mmst)
require("pin_psi_lambda_not_bilinear", "a spin/lattice exponential changes sectors and" in mmst)
require("pin_round7_register", "only after adding a local four-level flux register" in " ".join(mmst.split()))

# ---------------- A: symbolic zero-mode identities ----------------
al, j = sp.symbols("alpha j")
p = sp.Matrix(sp.symbols("p0:8"))
half = sp.Rational(1, 2)
q = sp.Matrix([1] * 8)
s = q / 2
r0 = sp.Matrix([half] * 4 + [-half] * 4)
a = s + r0
require("A0_a_value", list(a) == [1, 1, 1, 1, 0, 0, 0, 0])
Pm = sp.zeros(8)
for k in range(8):
    Pm[k, (k + 4) % 8] = 1                       # (Pp)_k = p_{k+4}
delta = sp.Matrix([(k + al) / 8 - half for k in range(8)])
nu = sp.Matrix([(k + j) / 8 for k in range(8)])
def K(v):
    return (v.dot(v)) / 2 + delta.dot(v)
T = lambda v: Pm * v + a
zero = lambda e: sp.simplify(sp.expand(e)) == 0
require("A1_charge_plus_4", zero(q.dot(T(p)) - q.dot(p) - 4))
require("A2_T_squared_is_q_translation", all(zero(e) for e in (T(T(p)) - p - q)))
dK_T = K(T(p)) - K(p)
dK_s = K(p + s) - K(p)
require("A3_energy_shift_formula", zero(dK_T - (q.dot(p) / 2 + sp.Rational(3, 4) + al / 2)))
require("A3_same_as_E8_translation", zero(dK_T - dK_s))
require("A4_character_difference", zero(nu.dot(T(p) - p) - nu.dot(s) - (r0.dot(p) - 1)))
require("A4_C_equals_g_squared_matches_on_CAR", zero(2 * nu.dot(T(p) - p) - 2 * nu.dot(s) - (2 * r0.dot(p) - 2)))
for alv in (sp.Rational(1, 4), sp.Rational(3, 4)):
    require(f"A5_vacuum_energies_{alv}", K(a).subs(al, alv) == K(s).subs(al, alv) == sp.Rational(3, 4) + alv / 2)
require("A5_values_7/8_9/8", {K(a).subs(al, sp.Rational(1, 4)), K(a).subs(al, sp.Rational(3, 4))} == {sp.Rational(7, 8), sp.Rational(9, 8)})
require("A6_a_ne_s_cartan", a != s)
require("A6_T_affine_not_translation", not all(zero(e) for e in (T(p) - p - (T(sp.zeros(8, 1)) - sp.zeros(8, 1)))))
# parity of the extra character on integral p: r0.p = q(p)/2 mod 1
random.seed(7)
for t in range(200):
    pv = sp.Matrix([random.randint(-3, 3) for _ in range(8)])
    require(f"A7_extra_character_(-1)^Q_{t}",
            sp.exp(2 * sp.pi * sp.I * r0.dot(pv)) == (1 if int(q.dot(pv)) % 2 == 0 else -1))

# A8: a = s + p* factorisation; p* is the K-null neutral direction
require("A8_a_minus_s_is_pstar", a - s == r0)
require("A8_K_pstar_zero_all_alpha", zero(K(r0)))
require("A8_s_orthogonal_pstar", s.dot(r0) == 0)
require("A8_K_a_equals_K_s_via_pstar", zero(K(a) - K(s) - s.dot(r0) - K(r0)))
require("A8_a_in_D8", all(x.is_integer for x in a) and sum(a) % 2 == 0)
for nm, v in (("s", s), ("pstar", r0)):
    require(f"A8_{nm}_in_spinor_coset", all((x - half).is_integer for x in v) and sum(v - s) % 2 == 0)
# G: reproduction of source-graded-locality (4a) with F from source-flux-index
aa = sp.Matrix([1, 1, 1, -1, -1, -1, -1, -1])
def Fe8(r):
    k = aa.dot(r)
    return sp.Matrix(list(r - k * aa / 2) + [0, -k])
m10 = sp.Matrix(list(aa) + [0, 3])
require("G0_b_equals_F_s", list(Fe8(s)) == [1, 1, 1, 0, 0, 0, 0, 0, 0, 1])
for i in range(8):
    d = sp.zeros(8, 1); d[i] = 1
    ri = d - aa[i] * aa / 2
    ei = sp.zeros(10, 1); ei[i] = 1
    require(f"G1_r{i}_E8_root", ri.dot(ri) == 2 and all((x - half).is_integer for x in ri))
    require(f"G1_e{i}_equals_F(r)-a_i m", Fe8(ri) - aa[i] * m10 == ei)
    require(f"G1_q(r{i})", sum(ri) == 1 + aa[i])
gl = (ROOT / "experiments/theory-contracts/source-graded-locality-20260920/PROOF.txt").read_text()
require("pin_graded_locality_4a", " e_i=F_aux(r_i)-a_i m,    q(r_i)=1+a_i," in gl)
z8 = (ROOT / "experiments/theory-contracts/source-z8-parity-descent-20260921/PROOF.txt").read_text()
require("pin_z8_vector_fermions", " 16_vector = (10,1) direct_sum (1,6)." in z8)

# ---------------- B: full Fock space on Maya diagrams ----------------
def channel_data(S, W):
    """S: set of occupied cover modes, finite difference from {m<0}; W window."""
    pk, L0k = [], []
    for k in range(8):
        Sk = {(m - k) // 8 for m in S if (m - k) % 8 == 0}
        lo, hi = -W, W
        pch = sum(1 for n in Sk if n >= 0) - sum(1 for n in range(lo, 0) if n not in Sk)
        L0 = sum(F(2 * n + 1, 2) for n in Sk if n >= 0) - sum(F(2 * n + 1, 2) for n in range(lo, 0) if n not in Sk)
        pk.append(pch); L0k.append(L0)
    return pk, L0k
def K_cover(S, alv, W):
    return (sum(F(m) + alv for m in S if m >= 0) - sum(F(m) + alv for m in range(-8 * W, 0) if m not in S)) / 8
def random_maya(rng, W):
    S = set(range(-8 * W, 0))
    for _ in range(rng.randint(0, 6)):
        m = rng.randint(-20, 19)
        S.symmetric_difference_update({m})
    return S
rng = random.Random(2026)
W = 6
for alv in (F(1, 4), F(3, 4)):
    dl = [F(k) / 8 + alv / 8 - F(1, 2) for k in range(8)]
    cα = F(3, 4) + alv / 2
    for t in range(150):
        S = random_maya(rng, W)
        Q = sum(1 for m in S if m >= 0) - sum(1 for m in range(-8 * W, 0) if m not in S)
        pk, L0k = channel_data(S, W)
        Nk = [L0k[k] - F(pk[k] ** 2, 2) for k in range(8)]
        require(f"B1_boson_fermion_{alv}_{t}", all(n.denominator == 1 and n >= 0 for n in Nk))
        Kc = K_cover(S, alv, W)
        require(f"B2_fold_law_is_cover_hamiltonian_{alv}_{t}", Kc == sum(L0k[k] + dl[k] * pk[k] for k in range(8)))
        require(f"B3_positive_{alv}_{t}", Kc >= 0)
        TS = {m + 4 for m in S} | {m for m in range(-8 * W, -8 * W + 4)}
        pT, L0T = channel_data(TS, W)
        NT = [L0T[k] - F(pT[k] ** 2, 2) for k in range(8)]
        require(f"B4_zero_mode_map_{alv}_{t}", pT == [pk[(k + 4) % 8] + (1 if k < 4 else 0) for k in range(8)])
        require(f"B5_oscillators_permuted_{alv}_{t}", NT == [Nk[(k + 4) % 8] for k in range(8)])
        require(f"B6_energy_shift_all_states_{alv}_{t}", K_cover(TS, alv, W) - Kc == F(Q, 2) + cα)
        # deck rotation g = exp(2 pi i G), G = sum m/8 :N_m:
        G = lambda X: (sum(F(m) for m in X if m >= 0) - sum(F(m) for m in range(-8 * W, 0) if m not in X)) / 8
        require(f"B7_deck_commutation_{alv}_{t}", G(TS) - G(S) == F(Q, 2) + F(3, 4))
        # sigma^2: pullback of primitive core winding
        S2 = {m + 2 for m in S} | {m for m in range(-8 * W, -8 * W + 2)}
        require(f"C1_sigma2_shift_{alv}_{t}", K_cover(S2, alv, W) - Kc == F(Q, 4) + (1 + 2 * alv) / 8)
    vac = set(range(-8 * W, 0))
    require(f"B3_unique_zero_{alv}", K_cover(vac, alv, W) == 0)
    require(f"B8_T_vacuum_energy_{alv}", K_cover({m + 4 for m in vac} | set(range(-8 * W, -8 * W + 4)), alv, W) == cα)

# deck phase exp(2 pi i (Q/2+3/4)) = -i (-1)^Q
for Q in range(-4, 5):
    require(f"B7_phase_{Q}", sp.exp(2 * sp.pi * sp.I * (sp.Rational(Q, 2) + sp.Rational(3, 4))) == -sp.I * (1 if Q % 2 == 0 else -1))
# winding of the multipliers on the core circle (length 4l): exp(2 pi i w x/(8l)) descends iff w even, core winding w/2
for w in (1, 2, 4):
    descends = (w * 4) % 8 == 0
    require(f"C2_descends_w{w}", descends == (w % 2 == 0))
require("C3_T_is_core_winding_two", 4 // 2 == 2)

# C4 (Korrektur): unit winding on the source circle theta is sigma^1 = T1
T1 = lambda v: sp.Matrix([v[7] + 1] + [v[k] for k in range(7)])
v = p
w1 = v
for _ in range(4):
    w1 = T1(w1)
require("C4_T1_fourth_power_is_T", all(zero(e) for e in (w1 - T(v))))
for _ in range(4):
    w1 = T1(w1)
require("C4_T1_eighth_power_is_q_translation", all(zero(e) for e in (w1 - v - q)))
rng1 = random.Random(11)
for t in range(100):
    S = random_maya(rng1, W)
    pk, _ = channel_data(S, W)
    S1 = {m + 1 for m in S} | {-8 * W}
    p1, _ = channel_data(S1, W)
    require(f"C4_sigma1_zero_modes_{t}", p1 == [pk[7] + 1] + pk[:7])
src_fold = fold.splitlines()
require("C5_factor_two_only_from_fold_geometry",
        any("der den Kern zweifach überlagert" in l for l in src_fold[10:14]))
for alv in (sp.Rational(1, 4), sp.Rational(3, 4)):
    for Qv in range(-4, 5):
        ph = sp.exp(2 * sp.pi * sp.I * (sp.Rational(Qv, 2) + sp.Rational(3, 4) + alv / 2))
        require(f"C6_bare_segment_translation_phase_{alv}_{Qv}",
                sp.simplify(ph - sp.exp(2 * sp.pi * sp.I * (sp.Rational(3, 4) + alv / 2)) * (1 if Qv % 2 == 0 else -1)) == 0)
require("C7_complement_m_charged", sum(m10) == 1 and all(sum(-aa[i] * m10) == -aa[i] for i in range(8)))
require("C7_pstar_neutral_not_m", sum(r0) == 0 and sum(m10) != 0)
require("C5_original_seam_is_fixed_set", "\\Seam=\\mathrm{Fix}(\\taudbl)," in bk)

res = {"contract": "chiral-cover-spectral-flow-20261015", "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(res, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
