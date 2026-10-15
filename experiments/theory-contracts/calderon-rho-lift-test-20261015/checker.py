"""Does the original seam / Calderon operator lift rho(p) = P p + r0 ?

Exact (sympy) plus finite Fock checks; no promotion.  Scope: PROOF.md.

R  rho algebra on the stipulated E8 zero modes: rho^2 = id, Q rho = Q,
   K rho = K, rho(0) = r0, rho(-delta) = -delta, rho swaps D8 and D8+s,
   T = tau_s rho = rho tau_s, T^2 = tau_q; r0 is an E8 root with K(r0) = 0.
N  native CAR: K on Z^8 has the unique zero p = 0, and rho(Z^8) is disjoint
   from Z^8; hence no operator on the native CAR Fock space lifts rho.
C  original Calderon formula P_C = (1+R_tau)/2, iota_C = R_tau
   (01_boundary_kernel_source.tex:105-135, 159-170): for an involution R on a
   finite Cauchy space, the Fock lift Gamma(R) satisfies Gamma a^dag(f) Gamma^dag
   = a^dag(R f), preserves bilinears covariantly, commutes with Q, fixes the
   P_C quasi-free vacuum up to sign, and Gamma dGamma(D) Gamma^dag =
   dGamma(D_ref - D_rel) with D_ref, D_rel as in 01:120-124.
S  source pins (seed, B_Sigma, U_Sigma family, sheet operation, no orbifold).
"""
from pathlib import Path
import json
import random
import itertools
import numpy as np
import sympy as sp

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

ROOT = Path(__file__).resolve().parents[3]
bk = (ROOT / "_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex").read_text()
t42 = (ROOT / "_archive/paper-latex/tfpt-42.tex").read_text()
car = (ROOT / "_archive/tfpt-45/source_extracts/02_carrier_source.tex").read_text()
flat = lambda t: " ".join(t.split())

# ---------------- S: source pins ----------------
require("S1_calderon_is_deck_reflection", "\\iC=R_{\\taudbl}." in bk and "P_C=\\frac{1+R_{\\taudbl}}{2}," in bk)
require("S2_seam_fixed_set", "\\Seam=\\mathrm{Fix}(\\taudbl)," in bk)
require("S3_ref_rel_split", "D_{\\mathrm{ref}}:=\\frac12\\bigl(D+\\taudbl^{\\ast}D\\taudbl^{\\ast}\\bigr)," in bk
        and "D_{\\mathrm{rel}}:=\\frac12\\bigl(D-\\taudbl^{\\ast}D\\taudbl^{\\ast}\\bigr);" in bk)
require("S4_collar_normal_form", "D_+=\\gamma_n(\\partial_n+B_\\Sigma)" in bk)
require("S5_seed", "\\mathfrak S=(\\mathfrak A_{\\mathrm{loc}},\\tau_t,\\Theta,\\omega,[u_\\Sigma],\\mathcal D_{\\mathrm{coll}})" in bk)
require("S6_B_from_Dcoll", "The first-order elliptic collar generator determines the boundary operator $B_\\Sigma$," in flat(bk))
require("S7_SF_corner", "|\\SF(U_\\Sigma)|=1\\quad\\Rightarrow\\quad N_{\\rm corner}=4." in bk)
require("S8_U_Sigma_family", "\\widehat U_\\Sigma(\\rho):=U_\\Sigma(\\lambda_\\Sigma\\sqrt{\\rho})," in t42
        and "\\widehat L_\\Sigma(\\rho):=-\\log\\det\\nolimits_{\\mathrm{adm}}(1-\\widehat U_\\Sigma(\\rho))," in t42)
require("S9_sheet_operation_reverses_Q", "\\mathcal C_\\Sigma\\,Q\\,\\mathcal C_\\Sigma^{-1}=-Q," in t42)
require("S10_calderon_upgrade_same_class", "lies in the same admissible elliptic class as $\\APSdomprov$" in flat(car))
require("S12_no_confusion_corollary", "No later theorem may identify these three operators literally; only the displayed restriction and transport maps are allowed." in flat(bk))
for word in ("orbifold", "twisted sector", "Ramond"):
    require(f"S11_no_{word.replace(' ', '_')}_in_boundary_kernel", word not in bk.lower())

# ---------------- R: rho algebra ----------------
al = sp.symbols("alpha")
p = sp.Matrix(sp.symbols("p0:8"))
half = sp.Rational(1, 2)
q = sp.Matrix([1] * 8); s = q / 2
r0 = sp.Matrix([half] * 4 + [-half] * 4)
P = sp.zeros(8)
for k in range(8):
    P[k, (k + 4) % 8] = 1
delta = sp.Matrix([(k + al) / 8 - half for k in range(8)])
K = lambda v: v.dot(v) / 2 + delta.dot(v)
rho = lambda v: P * v + r0
T = lambda v: P * v + s + r0
zero = lambda e: sp.simplify(sp.expand(e)) == 0
require("R1_involution", all(zero(e) for e in (rho(rho(p)) - p)))
require("R2_Q_invariant", zero(q.dot(rho(p)) - q.dot(p)))
require("R3_K_invariant", zero(K(rho(p)) - K(p)))
require("R4_rho0_r0", rho(sp.zeros(8, 1)) == r0)
require("R5_fixes_K_centre", all(zero(e) for e in (rho(-delta) + delta)))
require("R6_T_factorises", all(zero(e) for e in (T(p) - (rho(p) + s))))
require("R6_factors_commute", all(zero(e) for e in (rho(p + s) - (rho(p) + s))))
require("R7_T_squared", all(zero(e) for e in (T(T(p)) - p - q)))
require("R8_r0_E8_root_K_null", r0.dot(r0) == 2 and zero(K(r0)))
require("R8_r0_half_charged_per_channel_total_neutral", all(abs(x) == half for x in r0) and sum(r0) == 0)
# linear part P = product of the four D8 reflections in e_k - e_{k+4}
refl = sp.eye(8)
for k in range(4):
    a_ = sp.zeros(8, 1); a_[k] = 1; a_[k + 4] = -1
    refl = refl * (sp.eye(8) - a_ * a_.T)
require("R9_P_in_W(D8)", refl == P)
def in_D8(v): return all(x.is_integer for x in v) and sum(v) % 2 == 0
def in_D8s(v): return in_D8(v - s)
rng = random.Random(5)
for t in range(300):
    v = sp.Matrix([rng.randint(-3, 3) for _ in range(8)])
    if sum(v) % 2:
        v[0] += 1
    require(f"R10_swaps_D8_to_spinor_{t}", in_D8(v) and in_D8s(rho(v)) and in_D8(rho(v + s)))

# ---------------- N: no native CAR lift ----------------
for alv in (sp.Rational(1, 4), sp.Rational(3, 4)):
    dl = [d.subs(al, alv) for d in delta]
    require(f"N1_|delta|<1/2_{alv}", all(abs(d) < half for d in dl))
    for k in range(8):
        for n in range(-4, 5):
            term = sp.Rational(n * n, 2) + dl[k] * n
            require(f"N1_term_{alv}_{k}_{n}", term > 0 if n else term == 0)
for t in range(300):
    v = sp.Matrix([rng.randint(-4, 4) for _ in range(8)])
    require(f"N2_rho_leaves_Z8_{t}", not all(x.is_integer for x in rho(v)))

# ---------------- C: Calderon involution on a finite Cauchy space ----------------
d = 5
rs = np.random.default_rng(15)
def rand_unitary(n):
    z = rs.normal(size=(n, n)) + 1j * rs.normal(size=(n, n))
    qq, rr = np.linalg.qr(z)
    return qq * (np.diag(rr) / abs(np.diag(rr)))
U = rand_unitary(d)
for npos in (2, 3):
    R = U @ np.diag([1.0] * npos + [-1.0] * (d - npos)) @ U.conj().T
    PC = (np.eye(d) + R) / 2
    require(f"C0_projector_{npos}", np.allclose(PC @ PC, PC) and np.allclose(2 * PC - np.eye(d), R))
    # Jordan-Wigner Fock space
    Z = np.diag([1, -1]).astype(complex); Lo = np.array([[0, 1], [0, 0]], complex); I2 = np.eye(2)
    cs = []
    for i in range(d):
        ops = [Z] * i + [Lo] + [I2] * (d - i - 1)
        m = ops[0]
        for o in ops[1:]:
            m = np.kron(m, o)
        cs.append(m)
    adag = lambda f: sum(f[i] * cs[i].conj().T for i in range(d))
    dG = lambda h: sum(h[i, j] * cs[i].conj().T @ cs[j] for i in range(d) for j in range(d))
    w_, V_ = np.linalg.eigh(dG((np.eye(d) - R) / 2))
    G = V_ @ np.diag(np.exp(1j * np.pi * np.round(w_))) @ V_.conj().T
    Qop = dG(np.eye(d))
    # P_C quasi-free vacuum: fill Ran P_C
    vac = np.zeros(2 ** d, complex); vac[0] = 1
    ev, eV = np.linalg.eigh(PC)
    occ = [eV[:, i] for i in range(d) if ev[i] > 0.5]
    Om = vac
    for f in occ:
        Om = adag(f) @ Om
    Om = Om / np.linalg.norm(Om)
    require(f"C1_vacuum_fixed_up_to_sign_{npos}", min(np.linalg.norm(G @ Om - Om), np.linalg.norm(G @ Om + Om)) < 1e-10)
    require(f"C2_commutes_Q_{npos}", np.allclose(G @ Qop, Qop @ G))
    for t in range(4):
        f = rs.normal(size=d) + 1j * rs.normal(size=d)
        g = rs.normal(size=d) + 1j * rs.normal(size=d)
        require(f"C3_fermion_generator_{npos}_{t}", np.allclose(G @ adag(f) @ G.conj().T, adag(R @ f)))
        require(f"C4_boson_bilinear_{npos}_{t}",
                np.allclose(G @ adag(f) @ adag(g).conj().T @ G.conj().T, adag(R @ f) @ adag(R @ g).conj().T))
    Hm = rs.normal(size=(d, d)) + 1j * rs.normal(size=(d, d)); Dm = Hm + Hm.conj().T
    Dref = (Dm + R @ Dm @ R) / 2; Drel = (Dm - R @ Dm @ R) / 2
    require(f"C5_time_action_{npos}", np.allclose(G @ dG(Dm) @ G.conj().T, dG(Dref - Drel)))
    require(f"C6_symmetry_iff_Drel_zero_{npos}",
            np.allclose(G @ dG(Dref) @ G.conj().T, dG(Dref)) and not np.allclose(G @ dG(Dm) @ G.conj().T, dG(Dm)))
    # every Q-commuting unitary that commutes with P_C (Gamma(u), [u,P_C]=0) fixes Omega up to phase
    u = U @ np.diag(np.exp(1j * rs.normal(size=d))) @ U.conj().T
    wu, Vu = np.linalg.eig(u)
    hu = Vu @ np.diag(np.angle(wu)) @ np.linalg.inv(Vu)
    hu = (hu + hu.conj().T) / 2
    from scipy.linalg import expm
    Gu = expm(1j * dG(hu))
    require(f"C7_P_C_commuting_lifts_fix_vacuum_{npos}", abs(abs(np.vdot(Om, Gu @ Om)) - 1) < 1e-8)

res = {"contract": "calderon-rho-lift-test-20261015", "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(res, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
