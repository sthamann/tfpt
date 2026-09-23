# Charged ground-state source comparison

**UR.SOURCE.GROUND_RESPONSE.01 · PARTIAL · 2026-09-20**

The existing nonlinear dressed boundary fields fail to reproduce the
unchanged native interacting ground response even when every actual source
ground state is admitted. A block of 35 fields has addition/removal threshold
ratio 7/5 for all these states; the native ratio is strictly greater than
8.43495 at its fixed test point. A positive common time calibration cannot
repair this mismatch. Integrated weights can nevertheless be fitted; an
explicit first-moment contradiction prevents mistaking that fit for a
state-and-time identification.

- [German explanation](ERGEBNIS.md)
- [Analytic derivation and exact scope](PROOF.md)
- [Test specification, not an external preregistration](SPEC.txt)
- [Finite exact certificate](certificate.json)
- [Pinned upstream sources](source_manifest.json)
- [Replay and delivery validation](validation.json)

Run with Python 3, NumPy and SymPy:

```sh
python3 -B checker.py --output certificate.json
python3 -OO -B checker.py --output certificate_optimized.json
```

The checker reads its pinned original source files from the declared local
TFPT repository. It is not a self-contained archive of every upstream file.
The output folder includes normal and optimized replays of the existing
native moment and pole checks and the new other-lane static-register check.
The full historical ground enumeration was not repeated.

**Firewall:** this is an experiments/theory-contracts result. Fixed massless
Vaux, original quarter charge, original vertices and an adjoint-preserving
heat readout are assumptions. The native no-mu Hamiltonian is unchanged.
No source interaction is introduced, no T1-T8 gate is closed, no empirical
scorecard, verification module, paper or ledger is promoted. The analytic
argument and exact finite controls are distinguished; neither formal proof
assistant verification nor independent review is claimed.
