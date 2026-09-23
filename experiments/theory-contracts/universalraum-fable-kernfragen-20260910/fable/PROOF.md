# Fable round, 10 September 2026 — final corrected state (after LL2, Theorem-1, μ_s, Arithmetik, Dynamik and Zusatz reviews)

Declared source: uncut compact-U(1) rotor / CAR parent (ground-state-loop-response, observable-
dynamics; Q047 §1), H = (κ/2)ΣE_e² + l*(aA_U + βa²A_U²)l + M d*d + b(d*A_U l + l*A_U d), a = 1/12,
β = 1/4 (c = βa² = 1/576), b = 1/24, M = 4, κ = 1/100, ε_L = 1/96 (backtracks). Gauss law
q_x + div_x E = 0, q = n_L + n_H − 1. Ω_0 = all-low, zero flux. Plaquette loop W = U^p (div p = 0),
Z = e^{iπE_e/2} on a link with p_e = 1, S = W(I−P_3) + W^{−3}P_3.

Machine evidence: `checks.py` → `checks.json`, `cap_dynamics.py` → `cap_dynamics.json` (normal and
`-OO` byte-identical). Each JSON carries `evidence_classes`: **exact Fraction** = theorem on the
stated finite graph; **numpy** (allclose/eig/rank) and **mpmath** = numerical controls of formulas
proved in the text; **model values** = properties of auxiliary matrices, not of the parent.
The two-link term l*A_U²l is implemented as the direct endpoint bilinear c†_{L,z}c_{L,x}U_{xy}U_{yz}
(review witness: mask 75, flux 0, path 0→1→2 → (78, (1,1,0,0)) with amplitude −1/576; a sequential
two-hop mutant gives 0). The first dressing stage was independently confirmed by Codex with 85 exact
controls.

Scope boundary: finite graphs (one ring, two disjoint rings) and exact operator identities only.
No RH statement, no factoring speedup, no TOE/T1–T8 closure, no derivation of the parent, of the
wall premise, of a physical state selection or of a time identification from P1/P2. No volume
threshold, no all-order dressing statement, no minimality claim.

---

## Theorem 1 (leak of all-low flux codes) — exact

Let J be a finite isometry into the all-low sector (every L occupied, every H empty; range in
Dom H), P = JJ*, N_dir the number of directed links, Γ = (I − P)HJ. Then

    Γ*Γ = J*H_diag(I − P)H_diag J + b² N_dir I  ≥  b² N_dir I,                            (1.1)

with equality iff (I − P)H_diag J = 0, e.g. for codes spanned by flux basis vectors (the 16-dim cap
code: N_dir = 6N ⇒ N/96). Proof: on all-low states H_LL, H_LL2 (endpoint bilinear, needs an empty
L) and H_HL vanish; H_diag keeps the all-low sector; each directed LH term b d*_y U l_x produces a
normalized one-H/one-hole state, and distinct ordered pairs give orthogonal Fock patterns for
arbitrary (also overlapping) flux wave functions, so J*T*TJ = N_dir I; the diagonal and LH pieces lie
in orthogonal sectors (zero vs one H). ∎
Exact controls: ring N_dir = 8 → 1/72 (two flux-basis codes); two rings N_dir = 16 → 1/36; ring
superposition |flux 0⟩ + |flux 1⟩ → 1/72 + (4e)²/4 = 1259/90000. Codex's L = 5 witness
(Ω_0 + WΩ_0)/√2 → 125/96 + 1/10000 = 78131/60000 has the same structure.

Corollary 1.1 (restricted). No finite all-low flux code is H-invariant; its leak is ≥ b² N_dir,
extensive in the volume for this pattern. For a fixed Fock occupation basis state on the connected
cubic torus non-invariance holds as well (some occupied→empty NN edge exists, contributing ≥ b²),
but the leak need not be extensive: half-filled/half-empty block patterns leak only through a
boundary layer, O(L²) rather than O(L³). Fixed entangled matter vectors, other graphs and dressed
codes are not covered.

Corollary 1.2 (marks are not a symmetry; exact). [H_E, S]Ω_0 = 4κ·SΩ_0 = (1/50)SΩ_0, and with
plaquette orientation Ad_{e^{−itH_E}}(W) = W exp[−itκ(Σ_e p_eE_e + 2)]. Fixed marks are not
stationary; co-moving marks S(t) = U(t)*SU(t) (Q057) are an available exact construction, and
larger invariant spaces with their own marks are not excluded.

## Theorem 2 (source dressing on the ring) — exact rationals, finite observation

Recursion on an exactly re-orthogonalized family F_k: v ↦ v − Σ_h ⟨h|H|v⟩/(E_h − E_v)|h⟩, h over the
components of Hv orthogonal to F_k, E_h the diagonal energy of h, E_v := ⟨v,Hv⟩/‖v‖² (Rayleigh value
of the current vector). Only H enters. Ring results (per-vector leak ⟨v,H(I−P_k)Hv⟩/‖v‖²):

    order 0: 1/72 = 1.3889·10⁻²               (support 1)
    order 1: 3.32212·10⁻⁵ … 3.32258·10⁻⁵     (support 9; exact rationals; factor 418.07; confirmed by Codex, 85 controls)
    order 2: 8.7130·10⁻⁸                        (support 54; exact rational, 2036-digit denominator; factor 381.3; not independently certified)

Off-diagonal leak entries 1.5·10⁻⁶ (order 1) and 4.0·10⁻⁹ (order 2): from order 2 the dressed flux
sectors mix. Order-1 high admixture weight 8.70·10⁻⁴; residual census at order 1: 1.81·10⁻⁵ one-H
states (hole hopping with a = 1/12, energy mismatch), 1.51·10⁻⁵ two-H states, 9·10⁻¹² flux-only.

Uniform Duhamel contract (corrected). With R = HV − Vh after orthogonalization,
‖(e^{−itH}V − Ve^{−ith})v‖ ≤ |t|·‖R‖ for every unit code vector, and ‖R‖² ≤ max_a Σ_b |(R*R)_ab|
from the full exact leak matrix: ring coefficients 0.1179, 6.02·10⁻³, 3.08·10⁻⁴ for orders 0, 1, 2.
A single initial column value is not a trajectory bound (exact 3×3 counterexample of the Zusatz
review reproduced: Rv = 0 but Rhv = e_3, error ~ t²/2, distance √2 at t = π/√2).

Limits. Two observed reduction factors prove no expansion parameter, no convergence radius and no
all-order statement; no minimality is claimed. The dressing is controlled only on the tested flux
window: the hop detuning Δ(E) = M − ε_L + (2σE+1)/200 = (9587 + 24σE)/2400 equals 11/2400 at
σE = −399 (|b/Δ| = 100/11) and changes sign at σE = −400, both reachable in Gauss-neutral loop-flux
states. The dressing describes the H mode as a bookkeeping mode dressed onto the mobile L band; it
does not derive it.

## Theorem 2b (consolidation with the exact Krylov block, ERWEITERUNG.md) — exact on the ring

Codex keeps the preparation (ψ,0) and adds the leaked direction as an isometric block: V_1 = (J, η),
η = Γ/g, V_1*HV_1 = [[h_0, gI],[gI, h_1]] (a 32-dim compression, not an invariant two-level space:
R_1 = (I − V_1V_1*)Hη ≠ 0 with R_1*R_1 ≥ I/24 + G_2). Ring reproduction (exact): ‖ΓJ_a‖² = g² = 1/72,
J*η = 0, coupling block with squared entries 1/72, h_0 = diag(1/24, 37/600, 73/600, 133/600),
h_1 = h_0 + (57497/14400)I − (1/1152)·(neighbour-sector coupling) (torus analogue 57397/14400 and
−K/108000; constants are geometry dependent), moments J*H^kJ = E_0*(V_1*HV_1)^kE_0 exact for
k = 0..3, H⁴ defect = g²R*R as a full 4×4 identity (R*R diagonal ≈ 0.0382…0.0391), onsite-exchange
channel ⟨Σ_x d*_x l_x J, HΓJ⟩ = −deg·a·b·N (ring −1/36; torus −6ab√N/g = −1/√24 after normalization).
Relation: the Krylov block is an exact response-preserving enlargement of the representation
(Feshbach form kept); the dressing is a source-bound approximation that changes the prepared family.
Neither closes the dynamics.

## Theorem 3 (two-plaquette cap) — exact

For Ψ_cap = ½Σ_a S_1^a S_2^{−a}Ω_0 on two disjoint rings: energy increase 14κ = 7/50, electric
variance 68κ² = 17/2500, full variance 68κ² + 16b² = 389/11250, ‖P_AllLow[H,T_bal]Ψ_cap‖² = 208κ² =
13/625 (T_bal = S_1S_2^{−1}, ⟨Ψ,T_balΨ⟩ = 1) — the WILSON-CAP §5 values on an independent geometry.
Under H_E alone ⟨Ψ(t),T_balΨ(t)⟩ = ½[cos(20κt) + cos(4κt)] = ½[cos(t/5) + cos(t/25)], first common
revival t = π/(2κ) = 50π (confirmed by the Zusatz review). Under the separately defined norm flow
λ_t(U) = U, λ_t(S_m) = m^{it}S_m the whole marked M_4 algebra is pointwise fixed, hence every state
restricted to it has unchanged responses; this says nothing about the cap vector in the rotor
representation or about a common physical time. λ_t is not Ad(e^{it log N}) on the positive charge
basis (the latter moves U).

## Theorem 4 (auxiliary two-level model) — model values only

For the matrix [[0,g],[g,Δ]] with Δ = 9587/2400 and g² = N_dir b²: eigenvector high weight
½(1 − Δ/√(Δ²+4g²)) and normalized first-order-vector weight g²/(Δ²+g²) — ring 8.7·10⁻⁴ / 8.7·10⁻⁴,
N = 125: 6.5858 % / 7.5445 %. These are properties of the auxiliary matrix. They are not weights of
the parent (the first block is not invariant, R_1 ≠ 0), no volume threshold and no orthogonality
catastrophe is asserted. What is proved: the exact first coupling of the global all-low preparation
grows like √(N_dir)·b = √(N/96) on the torus.

## Theorem 5 (loop clock: invariant state; restricted coincidences) — exact rank, exact formulas, mpmath

(a) On M_4 = C*(Z,S) the unique Ad(S), Ad(Z)-invariant state is the normalized trace τ (null space
dimension 1). (b) The two-loop cap restricted to one loop clock is τ (exact, flux pattern (a,−a)).
(c) The critical ax+b state (KRITISCHER-GRENZZUSTAND: weak* limit of the ζ density operators on the
concrete affine C*-algebra, 1-KMS for λ_t) restricted to residues mod 4 is uniform. (d) The ζ-Gibbs
residue laws ω_β of H_log converge to uniform as β → 1⁺ per fixed modulus: ω_β(0) = 4^{−β},
ω_β(2) = 2^{−β}(1−2^{−β}), ω_β(1,3) = ½[(1−2^{−β}) ± L(β,χ_4)/ζ(β)]; deviations 0.40 … 5.7·10⁻⁵ at
β = 2 … 1.0001 (mpmath; the ζ-pole argument is exact). Corrections: ω_β is NOT the unit-invariant
report family μ_s at finite β — they share the divisibility/gcd moments Pr(n|X) = n^{−β}, but
ω_β(1) − ω_β(3) = L(β,χ_4)/ζ(β) > 0 (0.557 at β = 2, 0.0760 at 1.1, 7.9·10⁻⁴ at 1.001) whereas
μ_β(1) = μ_β(3) = (1−2^{−β})/2; the exact repair is μ_β = ∫_{Ẑ^×} u_*ω_β du. Convergence is per fixed
modulus / weak*, never uniform: d_TV(ω_β, Haar) = 1 and sup_m d_TV(ω_β mod m, Unif_m) = 1 for every
β > 1. The electric energy of ω_β is (κ/2)ζ(β−2)/ζ(β), finite only for β > 3 and divergent for
1 < β ≤ 3, so the ζ path is not a finite-electric-energy preparation. (e) Electric Gibbs states
e^{−βκE²/2}/Θ give residue weights uniform up to |w_r − 1/4| ≤ 2Σ_{k≥1}e^{−π²k²/(8βκ)}: β = 1: <
6·10⁻⁵⁴ (deviation 0 to 40 digits), β = 10: 2.2·10⁻⁶, β = 100: 0.149, β = 1000: 0.737 → δ_0.

Scope. (a) is about M_4; (b)–(e) are statements about the residue (diagonal) algebra and, for (b),
one loop's M_4. Nothing identifies the full pure two-loop cap with the full critical/Haar state
(I_4/4 and |+⟩⟨+| share the diagonal but differ on the shift); H_log acts trivially on the diagonal
algebra, so KMS there selects no temperature. The Frobenius weights are selected on the loop clock
by invariance under the two marked operations, are the common restricted limit of two different
thermal roads, and are never the electric ground state (β → ∞ gives (1,0,0,0)); the cap must be
prepared (WILSON-CAP §3: F_1, C are allowed field operations) and transported.

Finite-energy alternative (KRITISCHER-GRENZZUSTAND §5, reproduced exactly): σ_K uniform on −K…K has
residue error ≤ 1/(2K+1) per affine monomial (ring checks: worst 4/105 ≤ 1/21 at K = 10) and electric
energy κK(K+1)/6 per rotor (2κK(K+1)/3 on a neutral plaquette); the local covering
S_m^{(p)}|E⟩ = |E + (m−1)E_e p⟩ is injective on the full flux space, Gauss-preserving for every
matter configuration, with image E_e ≡ 0 mod m and S_m^{(p)}W = W^mS_m^{(p)} (exact on a sampled
flux box). This gives a finite energy/error contract for approximating the critical residue
responses by actual neutral rotor states; physical selection, controllability and time identity
remain open.

## Theorem 6 (radix layer with carry) — exact

n = 4q + r, E = 4Q + R, E² = 16Q² + 8QR + R², L = U(I−P_3) + U^{−3}P_3 = I⊗X, ZL = iLZ, and
Ad_{e^{−itκE²/2}}(L) = L·exp(−itκ(2Eδ(E) + δ(E)²)/2), δ ∈ {1, −3}. The carry is
C = U⁴P_0 + (I − P_0) (P_0 the residue-0 projection after the step), U = CL exactly; C and L are
two-term shift/diagonal operators, i.e. they lie in the finite normal form Σ_k U^k g_k(E).
Closures: W*(L, ℓ^∞(E)) ≅ ℓ^∞(Z; M_4) (bounded product of q-blocks, not the c_0 sum), invariant
blockwise under the electric flow; adding U the commutant is scalar and the von Neumann closure is
B(ℓ²(Z)); the norm closure has finite bandwidth and does not contain S_m (m > 1).

## Theorem 7 (coverings and finite clocks) — exact identities, numpy controls

S_m|n⟩ = |mn⟩: S_mU = U^mS_m, ES_m = mS_mE, E²S_m = m²S_mE², S_mS_k = S_{mk}, T_r = U^rS_4 Cuntz
(numpy controls on truncation-free cores; identities hold on the electric core). On the pure loop
sector E = Φp the electric energy 2κΦ² scales by m² under Φ ↦ mΦ (output energy, not an
implementation cost); on charged backgrounds E = np + ξ the difference is
(κ/2)[(m²−1)n²‖p‖² + 2(m−1)n⟨ξ,p⟩] — no global m² scaling. Primes are the indecomposable degrees
(known: round17 audit, Cuntz Q_N). A true S_m (m > 1) is a non-surjective isometry and cannot equal
any e^{−itH}; this excludes nothing about controls, ancillas or instruments. On Z_N, U_a|x⟩ =
|ax mod N⟩ (gcd(a,N) = 1) is a separately constructed permutation with the covering composition
law; F_NU_aF_N* = U_{a^{−1}}, ord_91(2) = 12, cycles {1,3,12}; its shift/diagonal normal form has
N/gcd(a−1,N) = 91 labels — a format complexity, not a gate lower bound. The label map
|n⟩ → |n mod N⟩ is not a bounded Hilbert-space transfer (norm amplification √K). Three distinct
cases — carry (finite normal form), finite U_a (in the shift/diagonal algebra of C^N), unbounded
S_m (outside every finite normal form) — must not be merged into one excluded class; whether a
native H or an admissible control protocol realizes a given transformation at favourable cost
follows from none of this bookkeeping.

---

## What is settled, what is open

Settled (exact, stated graphs / operator identities): (1.1) with the H_diag term and its witnesses;
non-stationarity of fixed marks; ring dressing orders 0–2 with exact residuals and the uniform
Duhamel coefficients; the ring reproduction of the Krylov block, its moments and H⁴ defect; the
two-plaquette cap energetics and its electric breathing; the unique marked-invariant state on M_4
and the restricted residue coincidences with their per-modulus limits; the radix/carry identities
with closures; the covering identities and the finite-clock permutation facts; the σ_K box
approximation and the local Gauss-preserving covering.

Open: physical preparation/retention mechanism of the Frobenius cap; a source-side reason for the
β = 1 norm time (electric time and norm time are functions of the same charge with incompatible
Gibbs states and different cap responses); an invariant extension with a commuting marked action
(excluded for all-low flux codes only); native flux-controlled loop operations at controlled cost;
the onsite/wall premise from P1/P2 (`det-wall-hh-rule`, equivalent to positivity + budget in
`TFPT-Globaler-Quellabschluss`); RH (odd-window infimum ≤ 10⁻¹² for L ≥ 9/4 and the constant-floor
shell gate refuted in `odd-window-direct-infimum-20260910/LOAD_BOUND.md`; no positivity source here).

## Sources

BRIEFING.md, UPDATE-1.md, UPDATE-2.md; context/aktuelle-runde: tfpt/WILSON-CAP-BEWEIS.md,
tfpt/ERWEITERUNG.md, ROTOR-BAUSTEIN.md, KRITISCHER-GRENZZUSTAND.md, primzahlen/PRIMZAHLEN-
PROZESSMODELL.md, transformationen/TRANSFORMATION.md, REVIEW-FABLE-LL2.md, REVIEW-FABLE-DYNAMIK.md,
REVIEW-FABLE-ARITHMETIK.md, REVIEW-FABLE-ZUSATZ.md (all corrections adopted); context:
TFPT-Globaler-Quellabschluss.md, TFPT-Markierter-Ursprung-der-Kopplung.md, Universalraum-Cap-und-
physische-Dynamik.md, Universalraum-Masterprogramm-Pruefung.md; verification/v1027 (hash-pinned);
det-wall-hh-rule/PROOF.md; odd-window-direct-infimum-20260910/LOAD_BOUND.md. Hashes: `QUELLEN.json`.
