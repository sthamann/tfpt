# Fable round, 10 September 2026: exact statements on candidates A–D

All statements are proved for the declared source (uncut rotor/CAR parent with
couplings a=1/12, b=1/24, c=1/576, epsilon_L=1/96, M=4, e=1/200; Q047 §1,
`ground-state-loop-response`). Exact finite controls: `checks.py` → `checks.json`.
NO RH claim, no factoring speedup, no TOE/T1–T8 closure. Nothing here derives the
source or its couplings from P1/P2.

Notation. Sites x, oriented links e_x: x→x+1 (ring) or the cubic-torus links; link
shifts U_e (E_e ↦ E_e+1); Gauss law q_x + div E(x) = 0 with q = n_L + n_H − 1;
Ω_0 = all-low, zero-flux state. Plaquette loop W = U^p (div p = 0), Z = e^{iπE_e/2}
on a positively oriented link of the plaquette, S = W(I−P_3) + W^{−3}P_3.

---

## Theorem 1 (leak of every flux-only code; candidate B)

Let J: C^d → H_phys be an isometry whose range is spanned by states of the form
(all-low matter pattern, arbitrary Gauss-compatible fluxes) — in particular the
16-dimensional cap code J(e_a⊗e_b) = S_1^a S_2^b Ω_0. Let N_dir be the number of
directed links of the graph. Then, with Γ = (I − JJ*)HJ,

    Γ*Γ = b² N_dir · I_d,                                                  (1.1)

independently of the flux content of the code. On a cubic torus with N sites
N_dir = 6N, so Γ*Γ = 6N b² I = (N/96) I, as found by the parallel Codex run.

Proof. Write H = H_diag + H_LL + H_LH + H_HL + H_LL2. On an all-low state every L
mode is occupied and every H mode is empty, so H_LL (c†_L c_L), H_LL2 and H_HL
(c†_L c_H) annihilate it (Pauli blocking / no H). H_diag is diagonal in the
(matter, flux) basis, hence maps the code into itself (J*H_diag J is diagonal and
(I−JJ*)H_diag J = 0). H_LH consists of the N_dir terms b c†_{H,y} c_{L,x} U_{xy}^{±},
one per directed link; on a code basis state each produces a normalized state with
exactly one H fermion at y, one L hole at x and the link flux (x,y) changed by one.
These N_dir states are mutually orthogonal (different (x,y) give different matter
patterns), orthogonal to the code (one H fermion) and, for different code basis
states, orthogonal to each other (two code states differ on at least the four
links of a plaquette, one hop changes one link). Hence (I−JJ*)HJ e = Σ_links b|h⟩
with orthonormal |h⟩ and Γ*Γ = b² N_dir I. ∎

Exact control (`checks.json` → `leak_theorem`): on the 4-ring N_dir = 8 and
Γ*Γ = 8b² = 1/72 for the S-code and for a second uniform-flux code; the leaked
states carry exactly one H fermion, one per directed link and code vector.

Corollary 1.1 (no finite fixed-matter code is dynamically closed). Any code whose
range has a fixed Gauss-admissible matter pattern leaks: the all-low pattern by
(1.1); the fully filled and empty patterns are Gauss-forbidden on a torus (total
charge ±N ≠ 0); mixed patterns admit LL hops onto holes and LH hops, so the leak
is again a positive multiple of the identity plus a positive operator. Since the
leak is extensive in the volume, the cap code cannot be made "approximately
invariant" by increasing the system.

Corollary 1.2 (the marked algebra is not a symmetry). [H_E, S] ≠ 0 exactly:
H_E S Ω_0 − S H_E Ω_0 = e Σ_{e∈p}((E_e+1)² − E_e²) S Ω_0 = 4e S Ω_0 = (1/50) S Ω_0.
More generally Ad_{e^{−itH_E}}(W) = W e^{−it e Σ_{e∈p}(2E_e+1)}: under the free
electric dynamics the marked operators stay local (same plaquette) but acquire
flux-dependent phases; under hopping they spread. The finite Z_4×Z_4 algebra is a
preparation/readout structure, and the only exact "closure" available is the
Heisenberg transport S(t) = U(t)*SU(t) of Q057 (carried marks), whose cost is the
support growth of S(t).

## Theorem 2 (the next-larger construction: source-dressed flux code)

Define the first-order Schrieffer–Wolff dressing by the source Hamiltonian itself,

    J̃ e_a = J e_a − Σ_h  ⟨h|H|J e_a⟩ / (E_h − E_a) |h⟩,                    (2.1)

h ranging over the leaked one-high states, E the diagonal energies (nonresonant:
E_h − E_a = M − ε_L + e(±2E+1) ≈ 4). Then on the 4-ring the dressed family is
exactly orthogonal, has high admixture weight 8.70·10⁻⁴ per vector, and its
residual leak is

    ⟨J̃_a, H(I−P̃)H J̃_a⟩/‖J̃_a‖² = 3.3227·10⁻⁵ … 3.3231·10⁻⁵   (exact rationals in checks.json),

i.e. a reduction of the bare leak 1/72 by the factor 418.0 for every a. The
residual is split 1.81·10⁻⁵ (one-high states: the L hole created by the LH
admixture hops with the large coefficient a = 1/12, and diagonal-energy
mismatch) and 1.51·10⁻⁵ (two-high states, second LH hop); the flux-only
component is 9·10⁻¹².

Interpretation. The cap can be carried into the dynamics only as a *dressed*
object; the dressing is fixed by the source (no response value is inserted) and
reproduces the DET-wall picture: the H species is a bookkeeping mode dressed onto
the mobile L band. The residual is dominated by the mobility of the hole — the
dressed excitation is not localized — so no finite-order dressing gives an exactly
invariant finite code. Exact invariant finite subspaces exist (finite-volume
eigenvectors) but they are not flux-only, not products, and carry no commuting
marked Z_4 action. This is the corrected constructive answer to candidate B: the
smallest dynamically consistent extension is the dressed code plus transported
marks, with the exact residual above as its error contract.

## Theorem 3 (rotor Z_4 layer with carry; candidate A)

On ℓ²(Z) with n = 4q + r, V|n⟩ = |q⟩⊗|r⟩ is unitary, E = 4Q + R, E² = 16Q² + 8QR + R²,
and L = U(I−P_3) + U^{−3}P_3 = I ⊗ X (X the Z_4 cyclic shift), Z = i^R, ZL = iLZ.
The physical shift is U = C L with the carry C = T_q^{P_0} (shift q iff r = 0 after
the step). Exact conjugation law:

    e^{−itκE²/2} L e^{itκE²/2} = L · exp(−itκ(2E δ(E) + δ(E)²)/2),   δ = 1 (R<3), −3 (R=3).   (3.1)

Hence Alg(L, E) = ⊕_q M_4(q) (functions of E and the internal shift) is invariant
under the free electric dynamics, with q-dependent phases: the Z_4 clock is not
autonomous, its frequency depends on the carry register through 8QR. Adding the
carry C (i.e. U) generates the full rotor algebra. Discarding 8QR is not
dynamics-preserving; keeping it makes the Z_4 layer a fibered, not a tensor,
factor of the dynamics. (`checks.json` → `rotor_layer`.)

## Theorem 4 (coverings as transformation building blocks; candidate C)

On the Fourier basis S_m|n⟩ = |mn⟩ (m ≥ 1) is an isometry with

    S_m U = U^m S_m,   E S_m = m S_m E,   E² S_m = m² S_m E²,   S_m S_k = S_{mk},   (4.1)

and T_r = U^r S_4 (r = 0..3) are four Cuntz isometries (Σ T_r T_r* = I, T_r*T_s = δ_rs)
realizing the radix decomposition of Theorem 3. The degree monoid (N_{>0}, ·) is
generated by the primes: primes are the indecomposable coverings. On a plaquette
loop sector (divergence-free flux Φ) the dilation Φ ↦ mΦ preserves Gauss law, so
S_m is a gauge-invariant isometry there, and it multiplies the electric energy by
m² (a degree-m covering costs m² in energy — energy is quadratic in charge). On the
full link space S_m violates Gauss law unless matter charges are scaled too.
S_m are isometries, not unitaries, and are not generated by the native H
(which contains only fixed-coefficient shifts W^{±1} and functions of E; see
Theorem 6). (`checks.json` → `coverings`.)

## Theorem 5 (the equal-weight Frobenius state is the critical Bost–Connes state)

Let ω_β be the ζ-Gibbs state on ℓ²(N_{>0}) with H_log|n⟩ = log n |n⟩, β > 1. Its
residue masses mod 4 are exactly

    ω_β(0 mod 4) = 4^{−β},   ω_β(2 mod 4) = 2^{−β}(1 − 2^{−β}),
    ω_β(1 mod 4) = ½[(1−2^{−β}) + L(β,χ_4)/ζ(β)],   ω_β(3 mod 4) = ½[(1−2^{−β}) − L(β,χ_4)/ζ(β)],

and, since ζ(β) → ∞ while L(β,χ_4) stays finite,  ω_β(r mod 4) → 1/4 for every r
as β → 1⁺ (numerically: max deviation 0.40, 0.24, 0.055, 0.0056, 0.00057, 0.000057
at β = 2, 1.5, 1.1, 1.01, 1.001, 1.0001). For general m the same argument
(principal character carries ζ, non-principal L-values stay bounded) gives 1/m.
Moreover Pr_β(n | X) = n^{−β} for all n, i.e. ω_β restricted to Ẑ is exactly the
report's profinite family μ_s at s = β (report §7.1), and its β → 1⁺ limit is Haar
measure on Ẑ = μ_1.

Consequence for candidate C. The observed mismatch "4^{−β} ≠ 1/4" is the finite-
temperature deviation of the Bost–Connes system; the native equal-weight Z_4
Frobenius/cap state is its critical (β = 1⁺, Haar) limit, uniformly for all moduli.
The arithmetic time H_log and the electric time are functions of the same charge
operator on the loop sector, H_E = (κ/2) e^{2H_log} on |E| > 0: same eigenbasis,
commuting flows, but incompatible Gibbs states (n^{−β} versus Gaussian e^{−βκn²/2}),
so neither a scalar clock reparametrization nor a change of β identifies the two
times — consistent with report §7.3. A common source would have to select the
critical point β = 1 dynamically; that selection is not supplied here.
(`checks.json` → `gibbs_residues`.)

## Theorem 6 (modular multiplication is the reduced covering; candidate D)

On the Z_N clock, U_a|x⟩ = |ax mod N⟩ (gcd(a,N)=1) is the reduction of S_a; it is
unitary, U_a U_b = U_{ab}, and the additive Fourier transform conjugates it to
U_{a^{−1}} (F_N U_a F_N* = U_{a^{−1}}; checked for N = 91, a = 2), so F_N does not
diagonalize it; its spectrum consists of roots of unity of orders dividing the
cycle lengths (for N = 91, a = 2: cycles of length 1, 3, 12; ord_91(2) = 12).
In the native operation vocabulary,

    U_a = Σ_k W^k · 1_{(a−1)x ≡ k (N)}(E),                                   (6.1)

a **flux-controlled loop operation** Γ_f = Σ_Φ |f(Φ)⟩⟨Φ|. The same class contains
the radix carry of Theorem 3 (f = controlled q-shift) and the coverings of
Theorem 4 (f = m·). So A, C and D are one operation class, and it is exactly the
class the native generator does not contain: the *-algebra generated by {W^{±1},
g(E)} consists of finite sums Σ_k W^k g_k(E); Γ_f belongs to it only when
f(Φ) − Φ takes finitely many values — false for unbounded coverings, and for U_a
it requires N/gcd(a−1, N) distinct controlled powers (91 for N = 91, a = 2), or
O(log N) controlled multiplications with an additional register (repeated
squaring). Order finding on the Z_N clock is therefore Shor's algorithm in TFPT
vocabulary, with identical resource accounting and no speedup; a native clock
with C^4 = I supplies none of these controlled operations for free.
(`checks.json` → `modular_covering`.)

---

## What this settles and what remains

Settled (exactly, in the declared source):
- The 16-dimensional physical cap is not H-invariant and leaks extensively (1.1);
  the minimal consistent continuation is the source-dressed code with residual
  3.32·10⁻⁵ per vector on the ring (factor 418 below the bare leak), plus
  Heisenberg-transported marks (Theorem 2, Corollary 1.2).
- The Z_4 layer of the rotor is a fibered factor with carry-dependent frequency (3.1).
- Coverings are gauge-invariant isometric transformation blocks on loop sectors,
  prime-generated, with energy scaling m² (4.1); the equal-weight cap state is the
  critical Bost–Connes/Haar state (Theorem 5); modular multiplication is the
  reduced covering and all of A, C, D are flux-controlled loop operations (6.1).

Not settled (named remaining premises):
1. A dynamical selection of β = 1 (the critical point) from the source; without it
   the identification cap ↔ Bost–Connes is kinematic.
2. A native mechanism producing flux-controlled loop operations Γ_f with controlled
   cost; without it no arithmetic reader beyond standard order finding exists.
3. An exact invariant extension of the cap carrying a commuting marked action:
   excluded for fixed-matter codes (Cor. 1.1); open for time-dependent or
   enlarged source constructions.
4. RH: none of the above supplies a positivity source; the odd-window infimum is
   ≤ 10⁻¹² for L ≥ 9/4 and the constant-floor shell gate is refuted
   (`odd-window-direct-infimum-20260910/LOAD_BOUND.md`); the full comparison (14)
   remains equivalent to window positivity.
