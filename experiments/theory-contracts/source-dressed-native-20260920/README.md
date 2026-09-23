# Dressed native tensor and pair-state/time audit

**UR.SOURCE.DRESSED_NATIVE.01 — PARTIAL.**

Start with [the German result](ERGEBNIS.md) and [the proof](PROOF.md).
This checks the existing F(E8) plus fermion-pair boundary dictionary against
the actual native W, group action, pair states and both existing energies.
No new physical model, metric, Hamiltonian or coupling is chosen.

Reproduce with Python, NumPy, SciPy and SymPy:

```sh
python3 -B checker.py --output certificate.json
python3 -B -OO checker.py --output certificate_optimized.json
```

Both certificates must be byte-identical. Eleven upstream files are frozen
by SHA-256 before and after the calculation. The unchanged native prefix
retains its six original guards; the original full large-array native suite
is not claimed to have been rerun. All new checks use explicit exceptions.

The new charged-lift lane's 33-control checker was replayed to
`charged_lift_lane_replay.json`, byte-identical to its original certificate.
This is an algebra replay, not a proof of its physical premises. No
independent reviewer or formal proof assistant is claimed for this contract.

The check includes negative control on a single relative tensor sign,
full product-group action, actual antisymmetrization at fixed positions,
all pair-momentum fibers, original-versus-selected energy, and the native
bright-pair/mediator Gram rank. An ordered pair at different positions is
not silently used as a covariant exterior-square map.

Experiments firewall: no empirical scorecard, paper, ledger or verification
promotion; no T1-T8 physical closure or complete TFPT solution.
