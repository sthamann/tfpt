# v1.6.7: correct Hamilton chain and explicit singlet projections

The active German report is `RESULTS.md` plus `BIG_PICTURE.md`, the short delta is `UPDATE.md`,
and the accessible explanation is `EINFACH.md`. The delivered full main
also includes the entire historical v1.6.6 and all six user source texts.

## Scientific replay

From this directory, with Python, NumPy, SciPy, SymPy and a C++17 compiler:

```sh
python3 -B replay.py
```

This verifies 24 frozen input digests, runs the six new Python verifiers
normally and with `-OO` and warnings-as-errors, and compares the outputs
byte for byte. There are 822 exact conditions per variant. It also freshly
compiles and executes the preserved C++ contraction and compares every
reported integer with the historical result.

The four-boson norm nu4 is an explicitly retained prior exact input. The
entire older source checker suites and the full native ground-state archive
are not rerun here. A fresh replay of the extracted package must reproduce
the new replay manifest. No assertions disappear under optimization.

## What is actually new

- Independent Schur/Weyl proof that the k=2 singlet multiplicity is four.
- Fresh native construction of all four directions and their squared
  couplings 36,16,504,360; complete six-dimensional compression through k=2.
- Correct full-H Lanczos prefix through five vectors, ten exact F energy
  moments, strict Ritz upper bound and slightly improved removal-energy floor.
- Full inner decomposition of End(16 tensor 4), resolving the 4035 remainder.
- Independent small-graph proof of the conditional full S2/S3 sector algebra;
  availability and Lie controllability are NOT inferred.
- Correct scalar-zero and symmetric-spinor channel norms; correction of the
  supplied value 24 versus squared norm 192.
- A dimensionless moment witness proving nonuniqueness of dynamics if only
  W, symmetries and the finite Clock are specified.
- Exact source pair-graph connectivity, 9 versus 8 diagonal Noether charges,
  invariant quadratic and cubic extensions, their availability still open.
- An explicit CAR/Lie-bracket obstruction to the literal primitive mapping.
- A real Bogoliubov-equivalence criterion preventing basis artifacts from
  being called genuinely new dynamics or fundamental number breaking.
- A time-varying cross correlation with zero initial value and no signalling.
- Source-derived 60-to-2016 isometry, exact single-mode information leak on
  all 64 modes, and small native N2 conversion; no physical boundary claim.
- Complementary and insufficient shadow examples, incompatible pairwise
  gluing and invisibility of an appended decoupled sector.

No native spatial transfer, complete relativistic dictionary, common 3+1D
parent, T1-T8 closure, RH, factoring breakthrough or P-versus-NP result is
claimed. No source worker, central acceptance marker or website was changed.

## Input audit

The ground probe completed during the inspection. Its frozen final JSON
has 382 guards (379 exact, 3 numerical), matching checker and dependency
hashes, and independently finds mult2=4. Its weaker sector estimates do not
contradict the prior stronger native ground-state theorem.

The operations JSON reports 306 guards rather than 307 and its embedded
checker hash differs from the frozen source. This is a snapshot mismatch;
we independently verified the material conditional conclusions instead of
calling this a whole-program replay. The field result has matching source
hashes but contains the mathematical norm/interpretation corrections.

## Documents

`build_documents.py` builds the Markdown and PDF trio. The local build uses
Pandoc 3.x from pypandoc-binary 1.17 and system XeLaTeX, with font paths
configured explicitly. Formula-heavy papers use TeX rather than image math.
The editable header and Lua formatting filter are retained. The Pandoc
binary and transient build directories are deliberately not in the archive.
To rebuild elsewhere, supply Pandoc and adjust the runtime/font paths.

PDF extraction/geometry checks use the Codex bundled Python runtime.
The mathematical replay has no dependency on that runtime, PDF tools,
the original absolute input locations, or network access.
