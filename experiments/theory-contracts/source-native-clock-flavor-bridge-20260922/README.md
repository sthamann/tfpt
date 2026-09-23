# Source native clock/flavor bridge — 2026-09-22

`UR.SOURCE.NATIVE_CLOCK_FLAVOR.01` — **PARTIAL**.

Read [ERGEBNIS.md](ERGEBNIS.md) for the German research result and
[PROOF.md](PROOF.md) for formulas, premises and proof boundaries.

This contract extends the original compiler dictionary by an explicit
determinant-line twist and a common metric-preserving monodromy intertwiner.
It audits the three-family symmetric E8 source product and exhaustively
tests the native finite clock class for rank, CP and mass hierarchy.

Run `python3 checker.py --out certificate.json` and
`python3 three_family_gram.py --out three_family_gram.json` in this directory.
The same programs remain active under `python3 -OO`.

No physical charged source, unique Higgs state, 4D Yukawa vertex, common
physical time or full TFPT solution is claimed. No target mass is optimized.
Only the finite source-weight prefix is replayed; the full TFPT suite and
ODE monodromy are not rerun. Source hashes are recorded in source_pins.json.

The later user attachment is audited in [ANHANG_PRUEFUNG.md](ANHANG_PRUEFUNG.md).
Run `python3 attachment_checker.py` to reproduce its displayed-formula checks.
The original attachment tensor implementation was unavailable and is not certified.
