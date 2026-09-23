# Source Clifford grading and nonlinear spinor seed

Research contract **UR.SOURCE.CLIFFORD_GRADE.01**, 2026-09-20.
Verdict **PARTIAL**. Start with [the German result](ERGEBNIS.md) and
[the mathematical proof](PROOF.md).

This experiment tests the previously identified precompression Clifford
route against the actual operator algebra, grading and source time. It
then identifies an explicit nonlinear source-field orbit within the
already existing conditional Gamma boundary theory. It does not derive
that boundary theory or its selected critical energy from P1/P2.

Reproduce from this directory, with Python, NumPy, SciPy and SymPy:

```sh
python3 -B checker.py --output certificate.json
python3 -B -OO checker.py --output certificate_optimized.json
```

The two certificates must agree byte for byte. Fourteen original repository
files are checked against frozen SHA-256 digests before and after the
calculation. The original seam constructor hashes its own docstring, so
its unchanged definitions and five prefix guards are compiled with
`optimize=0` in both runs; our checking logic uses explicit exceptions
and remains active under `-OO`. No upstream full numerical suite is
claimed to have been rerun. The native W/FW/BW prefix retains its six
original guards and avoids unrelated large cubic-array construction.

The new other-lane contract `UR.SOURCE.FLUX_INDEX.01` was read and its
40-predicate algebra checker replayed into `flux_lane_replay.json`, without
editing that lane. This replay must agree with its pinned source certificate.
It is not a replay of the analytical index theorem or physical gauge dynamics.

Finite counts are exact integer/rational calculations. The full-algebra
and extension statements are written proofs, not results inferred by
extrapolating finite samples. No independent agent review is claimed.

Firewall: experiments only; not empirical evidence, not promoted into
verification/ledger/papers. No physical T1–T8 gate is closed, no 3+1D
chirality/gravity or complete TFPT solution is claimed. Original source
files and other lanes are not edited.
