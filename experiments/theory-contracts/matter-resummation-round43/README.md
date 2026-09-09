# Round43: all-order matter row, an evaluated loop, and a canonicality boundary

2026-09-07. **NON-RH / unpromoted same-parent research.**
The matter sector is now represented to all orders and actually evaluated
on an edge, a six-leaf star and a closed four-site loop. This is NOT the
full electric many-body dynamics or a solution of T1-T8.

## What is new

The matter hierarchy has the exact rotor/one-particle representation
F(t)=exp(i H_E t) e_H^T exp(-i(H_E I+h)t). It preserves all earlier-prefix
electric phases. On a homogeneous translation-covariant graph, TWO evolved
auxiliary columns determine the entire source row, with a volume-free
error bound on the declared E0, exactly-one-fermion/site initial family.
The existing electric ME, MEM and MME terms are retained separately.

The new analytic cubic-source remainder at t=1 is below
**0.000034638931076**, about 79.23% below Round42. This removes the finite
matter truncation but ADDS all later first-electric budgets. It is not a
bound obtained by simply dropping the old dominant term.

**The resummed full-3D bulk readout has NOT been evaluated.** The new
finite-time numerical results here belong to the specified edge, star
and four-cycle. The cycle retains arbitrary integer winding flux; an
explicit Dyson/Duhamel tail controls the computational winding cutoff.
Two auxiliary columns use a 200-state matrix; the separate full physical
check uses 2310 states and a vector tail below 3.767e-15. The reconstructed
cycle source numerical error is below 4.124e-18.

At t=1 on the four-cycle, for the original bare-low input:

| Calculation | Certified high-root occupation interval |
|---|---|
| Resummed matter plus retained electric sources and all remainders | [0.00072348740629, 0.00072473021731] |
| Independent full physical parent, including all winding tails | [0.00072410866669, 0.00072410866672] |

The deterministic record also includes coherent Bell inputs on the cycle
and edge and the complete star benchmark. The same response matrix handles
different patch states without a fit. No cycle result is substituted for
a full cubic-lattice result or an experimental measurement.

There is also a precise negative result that prevents a false shortcut:
the matter row satisfies FF^dagger=I, yet on the same bare edge input
the expectation of its fermionic anticommutator is
**1 - (383/33177600)t^4 + O(t^5)**. Thus the auxiliary evolution alone is
not a canonical full-Fock transformation. The nonlinear electric terms
cannot be omitted on the strength of row unitarity. An independent symbolic
derivation gives the general edge coefficient **-kappa*g^2*(M-d)/6**, with
g=eta*a: electric coupling and the mass difference explain the obstruction.

See [MATTER_RESUMMATION.md](MATTER_RESUMMATION.md) for the exact identities,
the complete Gauss parameterization, the winding and reconstruction error
proofs, the canonicality witness, and the executed/unevaluated distinction.

## Reproduce

From the repository root, using the existing shared environment:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/matter-resummation-round43/checker.py --output experiments/theory-contracts/matter-resummation-round43/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/matter-resummation-round43 -p 'test_*.py' -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/matter-resummation-round43 -p 'test_*.py' -v
```

The record pins Round42 and its transitive parents and hashes this checker,
tests and both documents. Sixteen regression tests cover all matter jets
through fourth order on edge/cycle, the indispensable left electric phase,
two-column translation versus eight independent columns, complete Gauss
parameterization, winding tails and cutoff stability, source covariance,
the bare one-particle probability identity, exact CAR defect, improved
electric remainder accounting, independent full-cycle readouts, common
mixed/entangled patch responses, time reversal, domain/pin mutation guards
and deterministic replay. No observational dataset is used.

Record verdict:
`EXACT_MATTER_ROW_REPRESENTATION_WITH_EVALUATED_TREE_AND_CYCLE_HYBRIDS`.
The record explicitly sets `bulk_resummed_readout_executed` to false.

Verified on 2026-09-07: **16 new plus 338 predecessor tests** from
Rounds30-42 pass in normal and optimized Python, **354 tests per mode**.
The predecessor sources and their pinned records are unchanged.

## Remaining work

The next executable target is the full-cubic two-column rotor calculation
with independent loop fluxes and proved spatial and electric tails. The
analytic source bound is ready, but its improved bulk readout is not.
Multiple electric branches and further compatible physical observables
remain open, as do the selection of physical parameters and state, chiral
continuum dynamics, a universal spin-two sector and the other T1-T8 gates.

Matrix sizes here compare different intermediate problems, not equivalent
exact solvers: no total speedup is claimed. The experiment skill keeps this
as local research and catalog/notes only. No paper, website, verification
ledger, empirical scorecard, commit or push is changed by this round.
