# The function of the prime event log
Claim boundary: structural research map only; no claim for or against RH.

Tags: `[E]` proved in the corpus; `[N]` numerical; `[P]` corpus prose; `[T]` classical theorem; `[I]` inference.

## Q1 — Arithmetic on the physics side

The scoped search covered the eleven requested TeX files and 984 `verification/v*.py` modules after
excluding PRIME/HECKE filename families. The broad case-insensitive pattern returned 3,765 TeX hits
in 11/11 files and 25,046 verification hits in 901/984 files. These are upper bounds: most `Λ`, `θ`,
`E8`, `census`, and `ledger` hits mean cosmological constant, mixing angle, group name, or audit
vocabulary rather than prime arithmetic.

| Cluster | Broad count (TeX / v.py) | Role and evidence | Prime-dependent physics? |
|---|---:|---|---|
| E8 shells, Hecke, Euler product | 778 / 1,068 | [E] Static state census: `N(n)=240σ3(n)` and `L(E4,s)=ζ(s)ζ(s−3)`; primes enter after geometry (`tfpt_3_e8_audit_bootstrap.tex:2677-2697`; `verification/v1018_e8_directed_readout.py:27-34`). | No: exact arithmetic audit/readout, not a dynamical premise. |
| Riemann ζ | 62 / 325 | [E] Factorised shadow of the E8 theta series (`big_picture_2026-08-02_de.tex:568-581`; `tfpt_3_e8_audit_bootstrap.tex:2693-2697`). | No new prime or zero information. |
| Spectral ζ, Casimir, Quillen | 53 / 130 | [N] Heat-kernel/ζ-determinant regularisation (`tfpt_1_architecture_e8.tex:3884-3911`; `tfpt_horizon_readouts.tex:595-620`; `verification/v133_zeta_budget.py:1-14`). | No: this spectral ζ is not an Euler prime product. |
| Gaussian `χ−4` census | 32 / 99 | [E] Static signed splitting census selected by the μ4 mark (`tfpt_1_architecture_e8.tex:912-1060`; `rh/catalog/analysis/prime_story.md:10-17`). | Arithmetic channel depends on splitting, but physics predictions do not consume the prime order. |
| Coxeter primes `2·3·5=30` | 23 / 35 | [P/N] Facet labels of `h(E8)=30` (`origin_theory.tex:693-707`; `introduction.tex:786-809`). | No: finite factorisation, not the prime event stream. |
| Spectrum/state/root counts | 80 / 393 | [N] ADE/root and transition censuses (`verification/v1010_simplicity_bridge_census.py:347-368`; `verification/v782_e8_transition_bus.py:445-450`). | No. |
| Horizon/entropy | 624 / 2,247 | [N] Replica/thermal/spectral-ζ readouts (`tfpt_horizon_readouts.tex:560-620`). | No Euler-product dependence found. |
| Clock/time | 601 / 2,301 | [P/E] Finite Coxeter/μ4 clocks; finite periods cannot realise `{log p}` (`tfpt_prime_front.tex:921-951`; `rh/catalog/analysis/prime_story.md:36-37`). | Prime structure is an obstruction, not an input to physics. |
| RG/scale | 904 / 4,173 | [N/P] Ordinary QFT running and log-scale transfer (`tfpt_research_contracts.tex:14372-14462`). | No arithmetic scale action found. |
| Cosmology | 1,282 / 5,875 | [N/P] Mostly cosmological `Λ`; pattern noise for this question. | No. |
| Event log/checksum/shadow | 114 / 391 | [P/I] Consistency metaphor (`introduction.tex:62-304`; `tfpt_3_e8_audit_bootstrap.tex:2677-2704`). | No load-bearing dependency. |

[I] The arithmetic-specific material is concentrated in audit/contract layers: 2,357 of 3,765 broad
TeX hits are in `tfpt_3_e8_audit_bootstrap.tex` and `tfpt_research_contracts.tex`. [E] Source firewalls
also forbid prime-table/zero oracles in representative physics modules
(`verification/v704_chain_mass_law.py:50`; `verification/v713_l1_montage.py:191-231`).
Therefore no scoped physics prediction was found that would change under a counterfactual prime
sequence. The exact theta/Hecke identities would change, but they are static checks, not causes of
the Standard-Model, horizon, RG, or cosmological outputs.

## Q2 — Discrete → dynamic and 4D

| Mechanism | Input → operation → output | Type / generator | Arithmetic action? |
|---|---|---|---|
| Translation clock | `Z/5 × Z/6` → Coxeter synchronisation → order-30 rates | [E] discrete step; Coxeter element, hand `c^5` (`verification/v319_translation_clock.py:14-38`) | No |
| Resummed clock | transfer eigenvalue → `−6 log(1−n/Nfam)` → rate ladder | [E] discrete log ladder; hexagon size 6 (`verification/v124_resummed_clock.py:11-20`) | No |
| μ4 totative/seam clocks | element 7 or deck square root → four-cycle | [E] `Z4` step; `z↦±iz` (`verification/v223_coxeter_totative_clock.py:13`; `verification/v506_seam_clock_rigidity.py:12-22`) | No |
| Koide flow | anchor block → autonomous Riccati/Möbius ODE → time-one map | [P] continuous flow; ODE vector field, but continuous leg open (`tfpt_4_frontier.tex:457-471`) | No |
| `F_transfer` | source → threshold → RG → observables | [P/N] fibrewise RG/log-scale transfer (`tfpt_4_frontier.tex:120-121`; `verification/v777_ftransfer_clock_jets.py:84-114`) | No |
| Modular clock | RP covariance → OS transfer/GNS → modular Hamiltonian `K` | [P/E] operator flow; `K=log((1−C)C⁻¹)` (`verification/v446_seam_clock_invariance.py:31-33`) | No prime orbit theorem |
| Wick compiler | finite channel permutation + Pfaffian sign → Wick monomials | [E] finite Wick operation, not elapsed time (`tfpt_1_architecture_e8.tex:1333-1357`) | No |
| Scale lattice | three logarithmic scales → integer combinations → hierarchy factor | [E/N] additive log lattice generated by `α⁻¹,L0,Lc` (`tfpt_1_architecture_e8.tex:4167-4190`) | No |
| 4D lattice contract | local Hermitian `H` → `T=e^{-aH}` / thermodynamic limit → Lieb–Robinson cone | [P] Hamiltonian evolution; quasilocal `HΛ` (`tfpt_4_frontier.tex:809-824`) | No |
| QCA dilation | Markov collision band → unitary QCA → reduced `B^n` | [E/P] discrete unitary dilation; continuous/field limit open (`origin_theory.tex:793-796`; `tfpt_4_frontier.tex:859`) | No |
| Lorentz signature | μ4-cover Gram form → invariant Hermitian form → signature `(1,2)` | [E] algebraic 2+1 signature, not a 3+1 derivation (`tfpt_1_architecture_e8.tex:287-301`) | No |
| Horizon anchor | `c3` → thermal/Page factors | [N] static readout (`verification/v8_horizon.py:6-9`; `verification/v101_horizon_anchor.py:15-24`) | No |

Scoped absence counts are themselves findings: `foliation`, `3+1`, `emergent time`, and `scaling flow`
all returned 0; `ideles`, `Q*_+`, `integer monoid`, and a multiplicative arithmetic action returned 0.
`log p` occurred once, in a failed commensurable surrogate (`big_picture_2026-08-02_de.tex:2097-2104`).
There were 21 `unitar*` TeX hits and 42 script hits, and 19 combined self-adjoint/OS/reflection-positive
hits, but [I] these concern local QCA/modular constructions or an OS reconstruction contract—not a
corpus axiom saying that emergent TFPT time has a canonical self-adjoint generator. The continuous
`exp(t log F)` leg is explicitly open (`tfpt_4_frontier.tex:457-461`).

## Q3 — Classical templates in which primes are events

| Template | Function of the log; ζ; RH correspondence | TFPT match |
|---|---|---|
| Connes–Meyer adele-class flow | [T] Scaling on `A_Q/Q*`; primes/prime powers enter the periodic-orbit trace with lengths `log p`; the explicit formula is a trace formula and Weil positivity is the RH criterion (Connes 1999; Meyer 2005). | Has static Λ windows [E]; lacks an adele-class space, `R+`/idele action, canonical Hilbert metric, and self-adjoint TFPT generator [I]. |
| Bost–Connes | [T] C*-dynamics `σ_t`, KMS states, `Z(β)=ζ(β)`, phase transition at `β=1`; primes generate the Hecke semigroup (Bost–Connes 1995). RH has no known simple equivalence to this phase diagram. | Local/truncated KMS measurements [N], but global covariance died (`verification/v740_kms_extension_switch.py:46`; `verification/v741_kms_toeplitz_semigroup.py:9-445`). |
| Julia/Spector primon gas | [T] one-particle energies `log p`, bosonic Fock partition function `ζ(β)`, Hagedorn pole at 1; logarithmic derivative weights prime powers by Λ (Julia 1990; Spector). Fermionic variants yield reciprocal-ζ/Möbius factors. No simple RH thermodynamic criterion is known. | Seam mode counting fails the primon slope (`experiments/tfpt-discovery/seam_bc_primon_bridge_probe.py:267-283`); energies would otherwise be inserted by hand. |
| Berry–Keating `xp` | [T/I] `H=(xp+px)/2` generates dilations; regularised counting matches the smooth zero count, but a canonical boundary condition carrying the prime oscillations is missing (Berry–Keating 1999; Sierra/Connes variants). | No TFPT `xp` boundary construction found; Hilbert–Pólya truncations are different objects [I]. |
| Deninger | [T/I] conjectural foliated flow with primes as closed orbits; Lefschetz trace formula models the explicit formula; RH would follow from a Hodge-index/positivity structure on `H¹` (Deninger 1998–). | Requirements are compiled, but no arithmetic host for `Spec Z` (`experiments/tfpt-discovery/cohomspec_probe.py:122-132`; `stage1_construction_probe.py:72-85`). |
| Knauf / BC–Marcolli extensions | [T] arithmetic quantum statistical systems encode factorisation in Hamiltonians, KMS phases, symmetry breaking, and entropy; ζ/L-functions are partition functions. RH is not supplied by phase structure alone (Knauf 1990; Connes–Marcolli). | Some BC/KMS dictionaries [N/P]; no autonomous event source or global TFPT C*-system [I]. |

Every non-trivial instantiation needs: (1) a space with a canonical dilation/scale action; (2) a
multiplicative arithmetic action (`N×`, `Q*_+`, ideles, or equivalent); (3) a Hilbert/GNS space with
canonical inner product; (4) a self-adjoint generator if spectral positivity is claimed; and (5) the
archimedean place as boundary/cutoff. TFPT has finite clocks, discrete QCA dilation, modular examples,
static theta/Hecke data, and archimedean explicit-formula modules [E/N/P]. It lacks one object carrying
all five ingredients; in particular Q2 found no arithmetic group action and no transported unitarity axiom.

## Q4 — Candidate functions

1. **Constant information rate — THEOREM (PNT-level).** [T] `ψ(x)=Σ_{n≤x}Λ(n)~x` is equivalent to
   the prime number theorem. Precisely, the mean Λ-mass is one per unit of `x`; with `t=log x`, “one
   nat per unit log-time” requires the normalization `e^{-t}dψ(e^t)`, not raw event density.
2. **Minimal checksum error — RH_EQUIVALENT.** [T] Von Koch's criterion is
   `ψ(x)=x+O(√x log²x)` iff RH. This makes the checksum intuition exact: after subtracting its
   deterministic mean, cumulative weighted-prime discrepancy has square-root scale up to logarithms.
   It cannot prove RH without an independent source for the bound, because it is RH in equivalent form.
3. **Unique factorisation/no double counting — THEOREM.** [T] The numbers `{log p : p prime}` are
   Q-linearly independent: a rational relation exponentiates, after clearing denominators, to two equal
   prime factorizations. Prime powers are repetitions of their primitive prime event. [E] This is exactly
   why finite-clock periods fail (`tfpt_prime_front.tex:921-951`).
4. **Boundary between discrete and continuous — INTERPRETATION.** [T] The Euler product defines ζ
   in `Re(s)>1`; analytic continuation and the functional equation extend it to the critical strip.
   Zeros—not “singular support”—are the continuous/spectral side. [I] In this precise arithmetic sense,
   continuation is the discrete-to-analytic transition, while TFPT's proved compiler identities remain
   finite-window or Euler-region data (`rh/catalog/analysis/prime_story.md:10-19`;
   `verification/v540_amplitude_linear_carrier.py:70-87`).
5. **A privileged 4D prime mechanism — FALSE as a corpus conclusion; INTERPRETATION classically.**
   [T] Gaussian rank 2 gives `ζ_Q(i)=ζL(χ−4)`; quaternionic/D4 rank 4 theta has weight 2 and divisor
   sums of degree 1 (with a local factor at 2), while E8 rank 8 gives weight 4 and
   `ζ(s)ζ(s−3)`. D4/Hurwitz counts include `r4(n)=8Σ_{d|n,4∤d}d` and the Hurwitz normalization
   `24σ1(odd-part(n))`; E8 may be obtained by gluing `D4⊕D4`. [I] Replacing the μ4/Gaussian mark by
   a Hurwitz/quaternionic mark changes character, level, local factor, and census, but only produces
   shifted/factored ζ-functions. It does not change RH-neutrality: no new zero-location information appears.

## Q5 — Blind-spot check

The repo-wide source search excluded `node_modules`, `.lake`, and `rh/catalog`.

- [E] Finite prime-period host was tried and killed by commensurability (`tfpt_prime_front.tex:922-949`).
- [P] Connes–Consani periodic-orbit requirements remain an open Stage 1a roadmap
  (`tfpt_prime_front.tex:18312-18327`).
- [N/P] A weak functor reaches an S-local Connes subalgebra, not full adele/KMS dynamics
  (`verification/v733_strat3_gate0_census.py:36-43,302-311`).
- [N] Bost–Connes KMS extension and Toeplitz repair were carried to dead verdicts
  (`verification/v740_kms_extension_switch.py:46`; `verification/v741_kms_toeplitz_semigroup.py:9-445`).
- [N] The seam BC/primon bridge was killed: its mode count does not derive ζ
  (`experiments/tfpt-discovery/seam_bc_primon_bridge_probe.py:267-283`).
- [P/N] Deninger-style host requirements were specified; construction breakage was located, not repaired
  (`experiments/tfpt-discovery/stage1_construction_probe.py:72-85,1266`).
- [I] No Berry–Keating `xp` Hamiltonian with TFPT boundary conditions was found. “Riemann gas” had 0
  source hits; `xp` hits were coordinate names; most `Ruelle` hits were Haag–Ruelle scattering.

Thus the general direction was examined and partially killed, but no canonical TFPT scale flow with
autonomous prime orbits has been instantiated.

**Contract (extend `PRIME.STAGE1.CONSTRUCTION.01`; 8 lines).**
Object: no canonical TFPT scale generator currently exists; first freeze a source-only state space and flow.
Statement: derive primitive periods and amplitudes without reading primes, Λ, or zeros.
Pass: periods are exactly `log p`, prime powers are repetitions, and amplitudes match the explicit formula.
Metric: construct a canonical Hilbert/GNS inner product and archimedean boundary.
Positivity: identify a self-adjoint generator without assuming Weil positivity.
Kill A: periods are commensurable (finite-clock relabelling).
Kill B: multiplicative arithmetic was inserted by hand.
Kill C: the result is the standard adelic flow under TFPT names.

## Q6 — Synthesis

### In plain language
Das Ereignisprotokoll könnte drei echte dynamische Funktionen haben: als Energiespektrum
`E_p=log p` mit `Z=ζ`, als Längenspektrum primitiver geschlossener Bahnen, oder als Spur einer
Skalenwirkung. In allen drei Fällen ist ζ nicht Dekoration: Sie ist Zustandssumme oder Spurformel.
Aber die Primzahlen werden dabei nicht aus endlicher E8-Geometrie erzeugt; die Arithmetik steckt im
Wirkungsraum, in der Halbgruppe oder bereits in den Energien.

### What TFPT actually has
TFPT has exact static E8/theta/Hecke censuses, finite μ4/Coxeter clocks, discrete unitary dilations,
some modular/KMS tests, RG clocks, and archimedean explicit-formula machinery [E/N/P]. It has no
single canonical state space with an `R+`/`Q*_+`/idele action, no autonomously derived periods
`log p`, and no canonical self-adjoint generator for emergent time [I]. The corpus contains local
unitary/modular constructions and OS/reflection-positivity contracts, but no axiom whose positivity
can be transported to the required arithmetic generator. Adding that axiom without independent
physics would assume the decisive positivity and would therefore be circular for RH.

### Shortest honest path
Freeze one source-only TFPT scale flow, derive rather than import its primitive periods, and kill it
immediately if they are commensurable, hand-coded, or merely adelic relabelling. A quaternionic/4D
mark changes the rank-4 census and local Euler factors, not the zero-location problem; 8D E8 simply
shifts the divisor degree from 1 to 3. Even a perfect orbit construction gives, at best, the explicit
formula as a trace formula plus the still-open Hilbert–Pólya/Weil positivity step—unless the same
dynamics independently supplies a canonical self-adjoint generator and positive inner product.
