# Round35: a standalone 20-state time-local auxiliary model

**NON-RH, unpromoted theory contract.** Verdict:
`CERTIFIED_20_STATE_TIME_LOCAL_AUXILIARY_REALIZATION`.
This is a controlled numerical reduction of the inherited prepared cycle,
not a low-energy spectral EFT or a physical T1-T8 closure.

## Concrete result

The same four matter/gauge readouts now run with **20 evolving auxiliary
components instead of 488 full-cutoff components**, with no memory history
and no full/high-state reconstruction during online evaluation. The certified
extra vector error from the reduction is <3.32e-19 on 0<=t<=1.
At t=1, including every excluded electric flux, the absolute observable error
is <9.309e-14. All four reported intervals are identical to Round33/Round34:

| Observable | Certified t=1 interval |
|---|---|
| High occupation at site 0 | [0.00071934464413, 0.00071934464432] |
| Probability E0=0 | [0.99928328547964, 0.99928328547983] |
| Onsite low/high coherence | [-0.00404633584758, -0.00404633584738] |
| Real cycle Wilson loop | [0.00000021720204, 0.00000021720223] |

The initial bare-filled zero-flux state, U(1) Gauss sector and parameters
a=1/12, beta=1/4, eta=1/2, kappa=1/100, M=4, Vmag=0 remain unchanged. No
experimental data or fitted reference values enter construction. The geometry
is a three-site cycle, not a three-dimensional lattice.

## Why this is different from the previous memory reformulation

The auxiliary basis is generated from psi0, H psi0, H^2 psi0, ... using exact
orthogonal integer representatives. Its Hamiltonian is a small Hermitian
tridiagonal matrix. All four physical measurement operators are compressed
with the same embedding before online execution. Their source corrections
are retained, including the Wilson contribution whose omission previously
gave the wrong sign.

The second auxiliary basis vector is entirely in the bare-high sector. Thus
the model includes high-state information; it does **not** claim an effective
Hamiltonian on the old bare-low subspace. It cannot establish spectral mirror
decoupling, a selected physical vacuum, or spatial locality.

The error is certified from the exact full-parent residual and a nonnegative
path-series bound on reaching its last auxiliary coordinate. The residual
operator is not assumed small: its last column has norm about 3.52, but the
integrated amplitude reaching it is below 9.426e-20 on the declared interval.
This yields the small error without assuming decay of the old memory kernel.

Krylov model reduction and residual bounds are established methods, not new
TFPT principles; see [Jawecki, Auzinger and Koch](https://arxiv.org/html/1809.03369v2).
The parent-specific derivation, exact-arithmetic certification and limitations
are in [AUXILIARY_REDUCTION.md](AUXILIARY_REDUCTION.md).

## Standalone use and full verification

Run the compiled artifact without loading the parent model:

```bash
python3 experiments/theory-contracts/auxiliary-dynamics-round35/checker.py --model experiments/theory-contracts/auxiliary-dynamics-round35/compiled_model.json
python3 experiments/theory-contracts/auxiliary-dynamics-round35/checker.py --model experiments/theory-contracts/auxiliary-dynamics-round35/compiled_model.json --time 1/2
```

The standalone path uses only the standard library. The time domain is [0,1];
different initial states and times outside this interval are not certified.
The artifact contains 58 Hamiltonian integers and 1,600 source integers, common
denominators and error budgets. It contains no 488-state basis, parent matrix,
high-state vectors, memory kernels or benchmark values. Its current serialized
size is 109,937 bytes.

For independent reconstruction and validation against the pinned repository:

```bash
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/auxiliary-dynamics-round35/checker.py --output experiments/theory-contracts/auxiliary-dynamics-round35/validation.json --write-model experiments/theory-contracts/auxiliary-dynamics-round35/compiled_model.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/auxiliary-dynamics-round35 -p test_checker.py
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/auxiliary-dynamics-round35 -p test_checker.py
```

The standalone calculation **uses** certified budgets; reading an arbitrary
modified JSON is not a proof that its budgets are valid. The build and exact
replay verify those budgets and bind the compiled model by SHA256. Source pins
are rechecked even on cached certification. Tests independently compare the
full embedded vector, the physical sources, t=0 and t=1/2, and standalone
execution with a nonexistent parent path. Mutants exercise missing sources,
changed Hamiltonians, initial preparation, provenance and invalid time domains.

The tested 12- and 16-state candidates have wider but overlapping certificates;
20 states reproduce the frozen intervals. No minimal-dimension claim is made.

## Costs and remaining work

Offline compilation still uses the full 488-state parent, builds 9,760 integer
basis entries for m20 (up to 3,969 bits each), verifies orthogonality, residuals
and sources, and stores additional working arrays. The smaller online model
does not eliminate those setup costs.

Online evolution makes 9,280 real sparse coefficient visits at degree 80 instead
of 629,120 in the full-state calculation, but its denominator is 10^30 rather
than 14400 and its integer operands are larger. Four dense source contractions
also cost O(4m^2). **No end-to-end runtime speedup is claimed.**

The solved subtask is an independently runnable, certified finite-time auxiliary
realization of the existing prepared cycle. The outstanding theory task is a
physically local, preparation-family/volume-uniform description, or a genuinely
low-energy spectral reduction with controlled initial/source corrections.
Auxiliary-index locality is not spatial locality. T1-T8, continuum/gravity and
physical parameter/state selection remain unpromoted. Under the experiment
workflow, paper, website, ledger, verification suite and scorecard are unchanged.
