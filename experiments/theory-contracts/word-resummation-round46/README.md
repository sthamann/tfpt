# Round46: fixed-word resummation with a separate electric-leakage bound

2026-09-07. **NON-RH / conditional same-parent research.**
The further matter propagation of Round45's cubic and five-factor
electric sources is now resummed, rather than stopped at the next
hopping order. The construction is evaluated on the complete edge
parent and has a volume- and flux-uniform bound for its cubic target.
The NEW bulk resummed readout has **not** yet been evaluated.

## Executed result

The signed tensor generator for a literal word is

\[
K_d=H_E I-\sum_{creator\ legs}h_l^T+\sum_{annihilator\ legs}h_l.
\]

It retains the common electric field, opposite creator transport and
all literal CAR contractions. A finite-time driven evolution resums
all later matter steps for MEMM, MMEM, MMME and MEE. Other electric
branches remain explicit in the error bound.

On the unchanged EDGE parent at t=1, the bare-low high occupation is

**[0.00036095532874, 0.00036098918920]**.

The neighboring Bell states now give separated edge results:

| Preparation | Certified edge occupation |
|---|---|
| (LL-iHH)/sqrt2 | [0.49999679150340, 0.49999805170416] |
| (LL+iHH)/sqrt2 | [0.49999850068624, 0.49999976088915] |

Their certified gap exceeds **4.489e-7**. All three intervals contain
the independent full physical Hamiltonian calculation. This is an
edge result, NOT a new three-dimensional Bell witness at t=1.

For the ideal cubic resummed target, the source bound improves from
about **1.12835e-5 to 2.67330e-6**, more than a factor of four. Its
global time order remains six because older electric branches remain
omitted. The new target must actually be compiled in the bulk before
this bound can support a new bulk occupation interval. Round45's
existing numerical center cannot simply be reused with the new bound.

## Two shortcuts that fail

- A unitary auxiliary tensor evolution does **not** give an isometric
  physical CAR reconstruction. An explicit same-initial-class family
  amplifies the coefficient l2 norm by sqrt(N-1). The new certificate
  uses an explicit coefficient l1 estimate instead.
- Words that vanish on the one-fermion/site initial class cannot be
  pruned BEFORE resummation. Later matter propagation makes some of
  them contribute. A mutant performing that pruning changes the
  physical edge response.

The independent checks compare every cubic and five-factor word to
the original full-Fock commutator, recover the old free-source limit,
and match explicitly enumerated matter suffixes through time order
seven. This is NOT seventh-order matching of the full dynamics; the
remaining electric branches still begin at order six.

See [WORD_RESUMMATION.md](WORD_RESUMMATION.md) for the derivation,
intermediate electric backgrounds, reconstruction counterexample,
volume-uniform leakage series, numerical tails and real resource costs.

## Reproduce

From the repository root, using the existing shared environment:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/word-resummation-round46/checker.py --output experiments/theory-contracts/word-resummation-round46/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/word-resummation-round46 -p 'test_*.py' -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/word-resummation-round46 -p 'test_*.py' -v
```

Twenty regression tests include algebraic, independent-enumeration,
numerical, remainder, guard and deterministic-replay checks. The record
pins Round45 and all transitive parents and hashes the checker, tests
and both documents. Its verdict is
`FIXED_WORD_SUFFIX_RESUMMED_ON_EDGE_WITH_VOLUME_UNIFORM_LEAKAGE_BOUND`.
It explicitly sets `new_bulk_resummed_readout_executed=false`,
`full_electric_dynamics_solved=false`,
`isometric_CAR_reconstruction=false` and
`initial_zero_pruning_before_resummation=false`.

## Remaining work and firewall

The next gate is the actual lifted cubic calculation with controlled
configuration exits and a safe coefficient-to-CAR reconstruction.
The older first-electric and MEME/MMEE branches remain the largest
part of the new ideal remainder. Four 64-state and six 1024-state
auxiliary evolutions are real edge costs; the physical edge sector
itself has six states, so no edge speedup is claimed.

State/parameter selection, a chiral continuum, universal spin-two
dynamics and T1-T8 remain open. This is local, conditional theory work:
no paper, website, verification, ledger, scorecard, commit or push;
no empirical, proof-assistant or peer-review promotion.
