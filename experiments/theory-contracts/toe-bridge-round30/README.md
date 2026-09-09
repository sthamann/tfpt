# Round30: targeted T1-T8 work, quantum gauge dynamics and flavor/state selection

2026-09-07. **NON-RH, local unpromoted research.** No physical T1-T8 gate
is declared solved. This round addresses two actual missing bridges in
the existing corpus and states the other six requirements explicitly.
It does not extend Round29's scalar model into a chiral SM by fiat.

## Constructive quantum-gauge result (T3/T4)

[QUANTUM_GAUGE.md](QUANTUM_GAUGE.md) extends the v1027 signed-wall family
to a declared compact-rotor gauge Hamiltonian. There is a global pointwise
band rotation and an exact unitary on the **entire** fermion Fock space
and infinite gauge Hilbert space. The complete transformed Hamiltonian is

    H'=(kappa/2) sum_a (E_a+B_a)^2 + V_mag
                                  +dGamma(diag(h_low,h_high)).

The connection B_a is derived, not fitted or dropped. The construction
preserves the CAR, Gauss sectors, domains and real-time unitarity. It
applies to commuting group-coordinate multiplication entries, **not**
arbitrary noncommuting quantum-link matrices. The prior CAR counterexample
therefore remains intact.

An exact U(1) rotor example has four fermion modes, all 16 Fock states,
no electric cutoff, and a differential identity verified for an arbitrary
integer Fourier label. In the empty-high Fock compression the positive
geometric term is 9 N_low/100; its contribution to H is 9 N_low/200.
Two exact Gauss sectors (one and two fermions, with stated external charges)
show squared Hamiltonian errors 1/10 and 9/50 if the electric connection
is omitted. The one-fermion characteristic polynomial changes by 31/256.
This is actual dynamical backreaction, not merely a changed basis label.

The one-fermion Gauss sector also has a controlled Feshbach elimination:
for electric coefficient kappa/2 with kappa=1/100, the two compressed low
energies each differ from the exact full energies by at most
27/13000000 (<2.1x10^-6 in declared energy units). Exact rational Sturm
intervals check every root. The corresponding dynamical norm error is
bounded by 0.0015 |t|. This is an additional weak-electric finite-sector
case, not a volume-independent mirror theorem.

The proof also gives a bounded-interaction propagation estimate for the
original compact-gauge family at fixed lattice spacing, an energy bound
on dressed high occupation, and a finite-regulator common source functional.
The high sector still couples through B_a: no full interacting mirror gap,
bare-mirror response gap, chiral measure or physical SM is obtained.

## Flavor and state have a shared selection rule (T6/T8)

[FLAVOR_STATE.md](FLAVOR_STATE.md) starts from the actual six-mode lift
C_f, not the ordinary representation on its pair quotient. Its residual
K=C_f^4=(-1)^(N_1+N_3) enforces the exact Majorana block form

    [m11  0   m13]
    [ 0  m22   0 ]
    [m13  0   m33].

Arbitrary ordinary-seam operators and K-preserving reductions cannot fill
the (1,2) and (2,3) cells. This is an all-coefficient symmetry statement,
not a scan of a few mass ansatze. The existing spin-singlet composite
B12=nu1_up nu2_down-nu1_down nu2_up has the needed K-odd character;
no new elementary field is needed just for this algebraic ingredient.

However, any unique symmetric finite-volume ground ray, or invariant
Gibbs state, has <B12>=0. A genuine flavor mechanism using this composite
must therefore establish a physical symmetry-breaking state and its
selection. Neither condensation nor its coupling, scale or cosmological
branch has been derived. The Majorana-block restriction alone is not
a complete claim about observable PMNS mixing.

## T1-T8 acceptance and the current result

The authoritative requirement is `TFPT.TOE.COMPLETE.01` in
`verification/status_ledger.csv`; the checker records its current text hash.

| Gate | Concrete obligation still required | Contribution of this round |
|---|---|---|
| T1 | Structure postulate must derive P1/P2, dimension and compiler choices without additional selection data. | No new derivation. The graph construction is dimension-agnostic and its couplings remain declared. |
| T2 | Identify the actual charged microscopic seam operator algebra and its scaling limit with (E8)_1; preserve charge, cocycle and full source response. | No new seam identification. The gauge-band unitary is not this missing dictionary. |
| T3 | One TFPT-selected local/quasilocal unitary 3+1D parent, compatible with all downstream sectors. | Constructed conditional compact-gauge extension of the existing signed-wall family, with exact domains, Gauss and electric backreaction. Not a uniquely selected TFPT parent. |
| T4 | Chiral SM, local gauge-invariant Weyl measure, anomaly/index control and uniform mirror decoupling. | Removes the fixed-background restriction for the full representation theorem; interband gauge dynamics remains and must be controlled. |
| T5 | Uniform 3+1D continuum, Lorentz restoration, confinement, clustering and nontrivial scattering. | Fixed-spacing bounded-interaction propagation bound only; no continuum or scattering proof. |
| T6 | All three gauge couplings and complete neutrino texture/scale internally fixed. | Exact residual flavor rule and an existing candidate odd composite; no coupling fixpoint or mass prediction. |
| T7 | Emergent massless quantum spin-two mode, two helicities and universal coupling from the same parent. | No new graviton construction. The internal connection is not spacetime gravity. |
| T8 | Derived unique physical initial state and one source functional for all readouts. | Same-model finite-regulator source construction plus the exact incompatibility of a symmetric unique finite cap with the required odd condensate. No selected cosmological state. |

Two immediate, falsifiable continuation targets follow from the actual
new operators: bound the B_a-induced interband transitions uniformly in
the physical gauge regime; derive and solve an invariant interaction of
the existing K-odd composite orbit, including the state/limit that selects
its order. Completing either requires new dynamical work, not another
symmetry label or an inserted desired parameter value.

## Reproduction, tests, cost and scope

From repository root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/toe-bridge-round30/checker.py
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/toe-bridge-round30 -p 'test_*.py' -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/toe-bridge-round30 -p 'test_*.py' -v
```

Add `--output experiments/theory-contracts/toe-bridge-round30/validation.json`
to regenerate the local record. It hashes all five research sources and
pins the three inherited verification sources and two Round29 sources.
The checkers do not import or rewrite the verification suite.

Twenty-three tests cover exact CAR/exterior functoriality, all Fock occupations,
arbitrary-flux differential identities and independent large-flux examples,
Gauss orientation mutants, full compressed occupation factors, physical
spectral changes, the original noncommuting-entry counterexample, the
actual projective phases, spin singlet, all ordinary seam matrix units,
symmetry-preserving Feshbach reduction, positive self-energy bounds,
complete Sturm root enclosures, source pins and complete replay.

All acceptance comparisons are exact rational/symbolic identities; no
floating eigenvalue threshold is used. Matrices are at most 64x64 for the
actual six-fermion flavor algebra. The gauge differential calculation uses
degree-bounded Laurent matrices, not an enumeration of integer flux. The
general proof keeps the full compact-group Hilbert space. These small
regressions are not proof-assistant or external peer-review certification.
Generic full Fock assembly still grows as 2^(2d), and no polynomial-cost
solver, thermodynamic mirror theorem or continuum resource bound is claimed.

Only experiments are changed. Round28/29 sources are preserved. No ledger
promotion, empirical scorecard update, paper/website modification, commit
or push is part of this local research round.
