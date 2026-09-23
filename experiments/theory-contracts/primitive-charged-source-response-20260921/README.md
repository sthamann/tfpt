# Primitive charged source response

**UR.SOURCE.PRIMITIVE_CHARGED_RESPONSE.01 — PARTIAL — 2026-09-21.**

Read ERGEBNIS.md for the outcome, SOURCE_PROVENANCE.md for the primitive-source audit, and CORRELATORS.md for the explicit charged response of the already defined QWZ realization. This realization is not derived from P1/P2 here. No Gamma=I(9,1), Vaux or desired RR Hamiltonian enters the new calculation.

Reproduce the narrow companion checker (Python 3 and SymPy):

```sh
python3 -B checker.py --output certificate.json
python3 -B -OO checker.py --output certificate_optimized.json
cmp certificate.json certificate_optimized.json
```

Use --repo /absolute/path/to/tfpt-theoryv4 if the original source repository is elsewhere. Source pins are checked before the calculation. The inherited source checker output is archived separately; finite checks do not prove the continuum theorem. The existing continuum field theorem dates to September 9 and is not counted as newly derived.

The review corrected the finite-width sine dispersion to a controlled quasimode statement, distinguished unproved operator homomorphism from disproved homomorphism, and retained the first P1-selection gap before the candidate comparison. The old projector/time ambiguity is only a negative control; its alternate generator keeps the same negative projector.

Experiments firewall: no paper, ledger, empirical scorecard or T1–T8 promotion. Energies 3,4,5 are specific to the existing boundary candidate and are not requirements on every TFPT completion.
