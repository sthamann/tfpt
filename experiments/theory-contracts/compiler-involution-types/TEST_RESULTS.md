# Verification record

2026-09-08, local checkout b803b7e5 with existing research changes preserved.

- Normal process: 9 tests passed, 0.823 s.
- Optimized process (`-OO`): 9 tests passed, 0.813 s.
- Four inherited coherent K phases checked separately.
- 256 exact represented-algebra intertwining cells per phase, 1,024 total.
- Every phase has trace 8, eigenspace dimensions 12+4 and adjoint trace 64.
- Actual source A0 has A0^2=-I16 and determinant 1.
- Actual coupled A0+B/8 determinant: 29026959129/68719476736, nonzero.
- Rank-8 odd-operator and rank-12 noninvertible-intertwiner bounds have
  explicit exact witnesses.
- All three foreign source hashes were checked again and are unchanged.

The first optimized test attempt exposed an existing upstream import
assumption: `seam_state_derivation_probe.py` hashes `__doc__`, which an
ordinary `-OO` import removes. No foreign source was changed. The local
adapter compiles the exact pinned source with optimize=0, then executes
only its original construction prefix ending at line 627, before Aint_f.
The prefix hash agrees with the earlier source extractor. This retains
legacy docstrings/assertions; it does not claim to harden that legacy
source under `-OO`. Our own guards and tests run under `-OO`.

Both final test modes report a non-failing ResourceWarning from the
unchanged source's `open(...).read()` at line 366. It is not suppressed
or described as a failed mathematical check.

Artifact SHA256:

    checker.py      9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1
    test_checker.py 16c6f18d77a1b53bef8855a4fab3d0f3fb037dc8bbb110091c30b419d28fbe00
    validation.json 220ad33a08b3568434c25babd02c6f083493870a38407b6094cccf1c0c586377

Proof scope: an invertible identification of the two entire 16D linear
involution representations is excluded. No all-embedding, field,
antiunitary, Bogoliubov or RH no-go is asserted. No T1-T8 gate is closed.
Only this experiment directory was changed; no index, ledger, paper,
website, commit or push was touched.

## Later root integration: clock selection

The nine original tests were rerun together with three new clock tests:
12/12 normal (1.463 s), 12/12 optimized (1.475 s). Exact 16-coordinate
character polynomial and boundary identity; independent 120x120 exterior-
minor character polynomial; saved-record and physical-scope controls.
The original checker and validation hashes above remain unchanged.
Clock data and its additional source hash are in clock_selection_validation.json.
An independent mathematical review confirmed the Clifford embedding,
primitive grades and selection rule. The root then updated the shared
experiments index and research log, preserving their pre-existing contents.
Still no commit/push, paper/site or completion-marker change.
