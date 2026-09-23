# Validation record — 9 September 2026

Repository baseline: `66b91e40e245569f06ab440ead80f446c9be0ee5`, with the
pre-existing dirty checkout and source pins explicitly retained. No original
research source, paper, website, global ledger or other task's edits changed.

## Executed exact checks

- Original supplied program: all 44 checks pass; recomputed JSON is exactly
  equal to its archived result. All ten direct source hashes and ten archived
  source copies match; transitive guards execute. Replayed independently by
  an algebra-audit agent and by the integrating checker.
- New unit suite: **16 passed**, normal Python, 9.662 seconds.
- Same new suite: **16 passed**, Python `-OO`, 10.276 seconds.
- Both complete replays, including the original 44 checks, finish successfully.
  `validation.json` and `validation_optimized.json` are byte-for-byte equal.
- The two new Python-file fingerprints in the record were independently
  recalculated and match the final code at validation time.

The original program is inspected before execution. Its AST is cut immediately
before its fixed output-writing tail at line 167. No original output or archived
source copy is overwritten. Its source hash and its expected source-manifest
guards remain active. The original result is compared as structured JSON;
the two new full reports are additionally compared as bytes.

## Independent mathematical controls

The maximal-order calculation uses a separate 2x2 representation and checks
all 64 multiplication cells against the actual compiler commutant. It verifies
closure, inherited adjoints, indices, residual F4 generator, quarter-turn
membership, and the explicit Hermitian-lattice formula. Local maximal-order
uniqueness is a written proof in ORDER_PROOF.md, not a finite census alone.

The E8 calculation checks an integral even Gram matrix, determinant one,
positive leading minors, and an explicit unimodular simple-root basis with
the E8 Cartan graph. All 5^8 possible bounded norm-two coordinates are tested
using exact bounded integer arithmetic, yielding 240 roots. The coordinate
bound follows from the diagonal of the inverse Gram matrix; it is not an
arbitrary search cutoff. The 96/144 determinant split is then computed exactly.

The marked-source comparison independently constructs the actual v774
Construction-A row basis and all 240 source roots. It checks a unimodular
matrix identity for the entire lattice, both Gaussian and family intertwiners,
the actual anchor representative, and the inherited binary polar form. These
checks are stronger than matching a root count or abstract lattice name.

Process controls retain the real Clock spectrum, its invariant active triple,
nontrivial cross-transfer composition, source-point empty active vacuum,
positive as well as negative tensor-normalizer controls, a nonunique state
family, normalized instrument probabilities, and a finite-charge counterexample.

## Debugging history and limitations

The first new suite had one failed assertion and three errors: it compared
raw symbolic expression forms, including `(1-I)*(1+I)` against `2`, instead of
simplifying their difference. A minimal reproduction showed zero residuals.
Following the systematic-debugging skill, the comparator was corrected to
exact symbolic zero checks and a dedicated false-equality regression was added.
No floating tolerance, theorem assumption or original source was relaxed.
The independent source-map audit encountered and resolved the same expression
normalization issue in a redundant rootwise check.

The original pinned `seam_state_derivation_probe.py:366` emits a ResourceWarning
for an unclosed read handle in its import-time source guard. It does not fail
the suite. That upstream file was not modified or its warning suppressed.

These runs do not constitute external mathematical peer review or proof-assistant
verification. No complete repository suite, paper build, website build, physical
simulation of the proposed instruments, marked Half-Charge field map, RH proof,
factorization benchmark, or Hylæan evaluation was performed.

## Reproduction

From this directory, with the existing Python 3.14.3 environment:

```
/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/tfpt-discovery/.venv/bin/python -B -m unittest -v
/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/tfpt-discovery/.venv/bin/python -OO -B -m unittest -v
/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/tfpt-discovery/.venv/bin/python -B checker.py --replay-original --output validation.json
/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/tfpt-discovery/.venv/bin/python -OO -B checker.py --replay-original --output validation_optimized.json
```

The output options intentionally write the named report. `--replay-original`
requires the explicitly pinned local attachment artifact directory; the new
tests and computations otherwise use repository-relative pinned sources.
The supplied program is not portable as an unmodified import: it has a fixed
output path, and creating a fresh output directory would also require its
`quellen` subdirectory. The read-only replay avoids those side effects.
