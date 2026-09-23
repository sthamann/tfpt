# Executed validation — 9 September 2026

Python 3.14.3 in the existing TFPT discovery environment. Repository HEAD
`66b91e40e245569f06ab440ead80f446c9be0ee5`. The checkout also contains
pre-existing changes and local predecessor research; HEAD alone does not
identify those inputs. The record includes exact source pins.

| Suite | Normal | Python -OO |
|---|---:|---:|
| microscopic-twist-charge-test | 17 passed, 5.833 s | 17 passed, 5.983 s |
| source-edge-charge-transport | 18 passed, 2.367 s | 18 passed, 2.062 s |
| gaussian-vacuum-filter | 21 passed, 4.053 s | 21 passed, 3.773 s |
| Total | 56 passed | 56 passed |

Both complete new replays finished successfully. `validation.json` and
`validation_optimized.json` compare byte-for-byte equal on this host.
All five local Python-source fingerprints in the record were independently
recomputed and match. Cross-host floating-point byte equality is not claimed.

The new suite covers:

- Original-source and transitive pin checks, including rejection of a
  deliberately incorrect pin.
- The exact filled-sea Ward norm against a separate four-mode full-Fock
  calculation, retaining complex determinants, composition and adjoints.
- Original twist, bare ramp, identity and raw-string controls.
- Two forward steps, including the distinction between continued
  occupation and resetting to the instantaneous vacuum.
- Independent polar algebra, inversion failure at orthogonal subspaces,
  full-sea intertwining and fixed-mode generator diagnostics.
- The improved candidate's source-side neutral-pair identity and its
  forward/adjoint finite Ward improvement.
- Symbolic mass-control determinants, independent numerical gap bounds,
  exact geometric compression, and declared logarithmic-width windows.
- Explicitly false local-field and completion flags.

The complete replay extends the carrier diagnostics through N=256, mass
controls through N=4096, and the proposed logarithmic width bounds through
N=65536. Original and improved full-matrix point operators are compared
at N=16,32,64. Width-window records are bounds, not large-field simulations.

Reproduce from each suite directory with the existing interpreter:

```
/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/tfpt-discovery/.venv/bin/python -m unittest -v
/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/tfpt-discovery/.venv/bin/python -OO -m unittest -v
```

From this directory, reproduce the reports with `run.py --output` followed
by the chosen report filename; use `-OO` before `run.py` for the optimized
run. The output option intentionally writes that report file.

Not executed or established: a complete repository suite, external peer
review, a formal proof-assistant certificate, interval-enclosed numerics,
a growing-width full-sea field construction, a local normalized smeared
half-charge field, E8/Clock phase identification, or T1–T8 closure. No paper
build, website build, commit or push was performed for this isolated step.
