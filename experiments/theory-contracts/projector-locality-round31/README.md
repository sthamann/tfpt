# Round31: projector geometry gives local, full-Fock and density control

2026-09-07. **NON-RH / unpromoted theory experiment.**
Verdict: `CONDITIONAL_LOCAL_GEOMETRIC_CONTROL`.
No physical T1-T8 gate is declared solved; no new empirical prediction.

[GEOMETRIC_CONTROL.md](GEOMETRIC_CONTROL.md) gives the actual arguments,
including domains, constants, connected examples and counterexamples.
The input is Round30's declared dynamical compact-rotor signed-wall family,
not a new geometry attached without a common Hamiltonian.

## New constructive result

For a smooth low spectral projector P, S_a=(1-P)(X_a P)P measures its
change toward the high sector. Its squared magnitude is exactly the
positive Born-Huang correction found in Round30. The differentiated
spectral equation gives a convergent Sylvester integral and

    ||S_a||_p <= ||X_a h||_p/delta, p=1,2,infinity,

where delta is a uniformly ordered **fiber** band separation. Crucially,
on the whole fermion Fock space the off-band connection norm is
||S_a||_1, not the total number of modes times ||S_a||. A local derivative
therefore gives a volume-independent full-Fock bound per link. A weighted
resolvent argument separately proves spatially decaying projector and
link-derivative kernels, with explicit hypotheses and constants.

For the full electric Hamiltonian, the high-number commutator yields

    |d nu_H/dt| <= g sqrt(2 kappa c_E ebar),

where nu_H is expected high occupation per site, g bounds the per-link
full-Fock current, c_E bounds electric directions per site, and ebar bounds
electric energy per site. No electric flux cutoff is taken. This is a
finite-time **density** estimate, not a spectral mirror gap or a bound on
all local-observable errors of a low-only effective theory.
Round30 already implied the static density bound nu_H<=ebar/M; it is
retained, not claimed as a newly discovered theorem. What is new is the
local full-Fock estimate, spatial projector control, finite-time rate,
and the explicit Gauss-state construction supplying uniform energy below.

## Explicit connected-lattice and physical-state realization

Connected U(1) chains with hopping 1/4, beta=1/4, eta=1/2, M>=4 have
L=1/2, delta=M-9/16 and local derivative costs D1<=9/8, D2^2<=33/128,
independent of length. At M=4 the full-Fock off-band norm per link is at
most 18/55 and geometric energy at most 33 kappa/3025. The projector
has a valid spatial decay exponent mu=1/16 at fixed lattice spacing.

There is an explicit Gauss state with all low modes filled, no high modes,
constant rotated Haar wave, and declared external charge q_x=1 at every
vertex. Its total energy per site is bounded by
1/32+33 kappa/(256 delta^2). This construction supplies the energy premise
and proves high-density suppression uniformly over all chain lengths for
bounded times as M grows. It is a chosen state, not a cosmological selection.

For kappa=1/100 the following rational enclosures hold:

| Declared high parameter M | Bound on expected high occupation per site |
|---|---|
| 4 | nu_H(t) <= min(0.133, 0.034 abs(t)) |
| 40 | nu_H(t) <= min(0.0133, 0.003 abs(t)) |
| 400 | nu_H(t) <= min(0.00133, 0.0003 abs(t)) |

Time and energy use the declared model units with hbar=1. These are
conservative upper bounds, not measured transition probabilities. Neither
M nor kappa is selected by TFPT here. The chain is not a physical 3+1D SM.

The same construction is now also explicit on **three-dimensional cubic
boxes**, with hopping 1/12, one low/high pair per site and the same stated
Gauss backgrounds. No physical dimension-selection claim is made. Here
D1<=3/8 and D2^2<=11/384; the full physical rotor space contains unbounded
plaquette circulation even after Gauss reduction. For every finite box size:

| Declared M, kappa=1/100 | Cubic-box high occupation per site |
|---|---|
| 4 | nu_H(t) <= min(0.128, 0.0192 abs(t)) |
| 40 | nu_H(t) <= min(0.0128, 0.0017 abs(t)) |
| 400 | nu_H(t) <= min(0.00128, 0.00017 abs(t)) |

This is a declared three-space-dimensional lattice gauge/matter model with
continuous time and V_mag=0, not the chirally correct physical SM, a
Lorentz continuum or a derived vacuum. Every table entry is an exact upper
enclosure of the analytic bound, not a sampled dynamical measurement.

## Exact boundaries retained

- Small projector derivatives do not imply a bounded electric perturbation:
  Round30's unrestricted rotor transition norm is exactly
  3 kappa(2 abs(k)+1)/20 on the stated Fourier-input subspace. It diverges
  with flux despite a fixed fiber gap. This is not the fixed-charge finite
  Gauss sector, whose fluxes are forced by its constraints.
- Small local leakage does not imply uniform all-low many-body overlap:
  independent copies of the actual Round30 Gauss cell have all-low
  probability (1-p(t))^N, while high density is just p(t).
- A flat full moving-frame connection can have curved projections. This
  does not produce spacetime curvature or the T7 graviton.
- No uniform interacting mirror spectral gap, chiral determinant measure,
  connected-graph low-effective-dynamics comparison or T5 continuum exists
  in this result. T1/T2/T6/T7/T8 are not closed either.

## Reproduce and verify

From repository root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/projector-locality-round31/checker.py
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/projector-locality-round31 -p 'test_*.py' -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/projector-locality-round31 -p 'test_*.py' -v
```

Use `--output experiments/theory-contracts/projector-locality-round31/validation.json`
to regenerate the saved record. Four Round30 inputs and their transitive
verification/Round29 pins are checked before reuse. All four new sources
are hashed in the result. No verification module is imported or changed.

Twenty-eight tests include independent projector formulas, sign mutants,
full-Fock occupation costs, flat-versus-projected curvature, all link
positions on several chains, block-versus-scalar row norms, exact rational
decay/rate bounds, large positive/negative fluxes, product-state obstruction,
three-dimensional boxes and arbitrary integer physical plaquette flux,
source-pin mutants and byte-exact result replay. All acceptance arithmetic
is exact; no floating eigenvalue tolerance is used.

Finite checks reach 32 chain sites (64 one-particle dimensions), 27 cubic
sites (54 one-particle dimensions) and all
16 Fock states of the inherited rotor. General uniformity follows from
the written analytic estimates, not this finite sample. Generic Fock
enumeration remains exponential; no efficient arbitrary-volume solver is
claimed. The proof is not proof-assistant or externally peer-review certified.

Only experiments and their catalog/research notes change. Round28-30,
verification, ledger, papers, website and scorecard remain untouched.
No commit or push is part of this research continuation.

Next concrete obligation: retain virtual high-sector corrections and
compare gauge-invariant **local** readouts of the full and reduced
connected-graph dynamics at fixed finite energy density, with constants
uniform in graph size and the actual original couplings retained.
