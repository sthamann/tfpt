# Source pair response and controlled state/time transfer

**UR.SOURCE.PAIR_TRANSFER.01 — PARTIAL.**

Read [the German result](ERGEBNIS.md) and [the proof](PROOF.md).
The all-order pair response is derived from the actual previously defined
odd F(E8) composite fields. No new Hamiltonian, energy matrix or mediator
is chosen. The fixed boundary, Vaux and vacuum are still conditional inputs.

Reproduce with Python, NumPy, SciPy and SymPy:

```sh
python3 -B checker.py --output certificate.json
python3 -B -OO checker.py --output certificate_optimized.json
```

Certificates must agree byte for byte. Ten source files are pinned before
and after the calculation. The native source prefix retains its six
original guards. Only that prefix is executed; the large native suite is
not claimed to have been rerun. All new checking uses explicit exceptions.

The finite checker verifies the nine rational-function types covering all
6816 same-momentum cells, the other zero entries by momentum support,
generating-function identities, exact transfer counterexamples, uniform
tail-bound identities, and the unchanged native two-level binding block.
Infinite-order and all-time statements use the written analytic proofs;
they are not extrapolations from finitely many sampled times.

`sector_lane_replay.json` reproduces the new sector-reconstruction lane's
32-control certificate byte for byte. This is not a derivation of that
lane's physical premises. No independent agent review is claimed here.

Experiments firewall: no paper, verification, ledger or empirical scorecard
promotion; no physical T1-T8 closure or complete TFPT solution.
