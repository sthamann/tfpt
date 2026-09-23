# Local follow-up verification — 9 September 2026

Base publication: `66b91e40e245569f06ab440ead80f446c9be0ee5`.
This directory was added **after** that commit and is not part of its
published papers, website, manifest or CI inventory.

Using the repository's Python 3.14.3 environment, from this directory:

```sh
../../tfpt-discovery/.venv/bin/python -B -m unittest -v test_checker
../../tfpt-discovery/.venv/bin/python -B -OO -m unittest -v test_checker
../../tfpt-discovery/.venv/bin/python -B checker.py
```

- Ordinary mode: **12 tests passed**, 0.316 seconds reported by unittest.
- Optimized mode: **12 tests passed**, 0.317 seconds reported by unittest.
- Direct checker: successful, status `CONDITIONAL_TARGET_ENERGY_DOMAIN_BRIDGE`.
- All 256 quarter-holonomy sign assignments checked on all 240 E8 roots.
- An additional 1,000 deterministically sampled higher-charge/oscillator
  states satisfy the exact rational comparison inequalities.
- The pinned microscopic source still rejects half-integer charge.
- Source-pin mutation is rejected; no upstream pinned source was edited.

The finite calculations check the algebra and regressions. The all-charge
positivity, kernel and energy-domain statements rely on the written proof
and explicitly assumed target Hilbert space in `README.md`; finite tests
are not a proof of an infinite microscopic limit. There is no independent
mathematical review or promotion of a T1–T8 closure claim.

The next missing object is still the source-derived renormalized
half-charge inter-sector field, including a justified choice of relative
channel holonomies and a compatible physical charge sector.
