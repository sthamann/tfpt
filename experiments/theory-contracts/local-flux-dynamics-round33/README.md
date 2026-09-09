# Round33: local electric control and fully evaluated cycle readouts

2026-09-07. **NON-RH / unpromoted theory experiment.**
Verdict: `LOCAL_ELECTRIC_CONTROL_AND_CERTIFIED_FULL_ROTOR_READOUTS`.
No physical T1-T8 gate closure, empirical evidence or RH claim.

## What is new

1. [LOCAL_FLUX.md](LOCAL_FLUX.md) supplies the missing local electric
   premise for Round31's actual dressed filled-low cubic preparation.
   The full parent gives a per-link force norm <=53/288 and
   <E_l^2(t)> <= (sqrt(11/384)/(M-9/16)+(53/288)|t|)^2.
   Both the initial moment and its propagation are independent of total
   volume, including open boundaries. A subsequent partial electric
   truncation has an explicit state, normalization and readout error budget.
2. [CYCLE_DYNAMICS.md](CYCLE_DYNAMICS.md) actually evaluates four matter
   and gauge readouts of the full three-site cycle with its infinite
   physical electric sector. Gauss leaves 20 matter masks times arbitrary
   integer cycle flux. A Dyson-tail bound accounts for every omitted
   sector, and exact integer real-time arithmetic supplies finite-matrix
   errors. At t=1 the K=12 full-rotor readout error is <=9.3081e-14.
3. The same parent generates a leading U(1) plaquette potential in its
   filled-band compression: g_square(1-Re W_square), up to a constant,
   with g_square=a^4(M+3)/(2M^3)>0. At a=1/12,M=4 it is 7/2654208.
   This is an exact leading hopping coefficient, not an independently
   added magnetic action. Higher orders and eliminated-channel dynamics
   are not discarded or claimed controlled by this coefficient alone.

## Actual full-cycle outputs

All parameters are declared model choices: a=1/12, beta=1/4, eta=1/2,
kappa=1/100, M=4, V_mag=0. Time is in model units, hbar=1. The normalized
initial cycle state has three **bare** low fermions and zero electric
flux. It is NOT Round31's gauge-dependent dressed filled-Haar state.

| Bounded gauge-invariant readout at t=1 | Certified interval |
|---|---|
| Bare high occupation, site 0 | [0.00071934464413, 0.00071934464432] |
| Probability electric flux E0=0 | [0.99928328547964, 0.99928328547983] |
| Onsite low/high coherence | [-0.00404633584758, -0.00404633584738] |
| Real Wilson cycle | [0.00000021720204, 0.00000021720223] |

These are absolute enclosures of an actual full-rotor evolution, not
upper limits on unspecified populations or measured experimental data.
The Wilson interval excludes zero. The three-site cycle is not a 3D
cubic calculation. All six fermion modes, including high fermions,
remain in the calculation: electric regularization is not high-sector
elimination. A bare-low frozen comparison would miss all four changes.

## Preserve the parent under regularization

The electric compression is P_K H P_K. In particular, the code expands
the parent's A^2 before projecting; replacing it by (P_K A P_K)^2 loses
the positive term P_K A(1-P_K)A P_K. An exact physical one-edge witness
loses energy 1/576 under that incorrect replacement. The test suite also
rejects treating truncated link shifts as exact rotor unitaries.

The rigorous-error strategy is contextualized by [Tong et al., Quantum
6, 816 (2022)](https://arxiv.org/abs/2110.06942). The simple bounded-
interaction Dyson estimate, concrete parent expansion and all constants
are derived in this experiment; the established general truncation idea
is not claimed as a new result.

## Reproduce and limits

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/local-flux-dynamics-round33/checker.py
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/local-flux-dynamics-round33 -p 'test_*.py' -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/local-flux-dynamics-round33 -p 'test_*.py' -v
```

Use `--output experiments/theory-contracts/local-flux-dynamics-round33/validation.json`
to regenerate the deterministic record. Three Round32 sources and the
transitive Round31/30 provenance are checked; five new sources are hashed.
Twenty-five tests cover independent Laurent-parent expansion and fermion
signs, arbitrary Gauss flux, a repeatable physical cycle, exact basis
counts, bounded hopping norms, cutoff order, independent polynomial
coefficients, two electric cutoffs, two Taylor orders, nontrivial readouts,
local current budgets, induced loop coefficients, source mutations and replay.

The largest numerical problem is 488 physical states and 3932 matrix
entries, evolved with 80 sparse Gaussian-integer polynomial steps. No
floating-point acceptance tolerance is used. Costs remain exponential
for general graphs with many matter modes and independent cycles. This
does not solve arbitrary-volume many-body dynamics or supply an efficient
full-TOE solver. The analytic arguments are not proof-assistant or externally
peer-review certified.

Next: use this full matter-and-gauge reference to validate an independently
closed low-only evolution with consistent virtual terms and preparation;
extend the comparison locally on the same cubic parent with controlled
spatial and electric remainders. T3/T4 physical chirality and mirror-gap
claims, T1/T2 selection, T5 continuum, T6 flavor, T7 graviton and T8 state
selection remain open. An induced U(1) coefficient is not the physical SM.

Experiment firewall: no paper, website, ledger, scorecard or verification
changes; no promotion, commit or push is part of this local research round.
