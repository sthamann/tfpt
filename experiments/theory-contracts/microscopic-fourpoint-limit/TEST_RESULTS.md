# Verification record: microscopic neutral four-point continuation

2026-09-09. Repository HEAD `b803b7e5d0e4ac20c0a1ce7bffee0f91326dcff4`.
All reported tests were actually rerun in this continuation, in separate
processes per suite and optimization mode. The full transcripts, counts,
return codes, runtime version and UTC timestamp are in [verification.json](verification.json).

## Verified suites

| Suite | Normal | Optimized (-OO) |
|---|---:|---:|
| Previous microscopic neutral limit | 11 | 11 |
| Exact source/current symbol | 9 | 9 |
| Microscopic energy linearization | 10 | 10 |
| Current truncation/Galerkin bridge | 13 | 13 |
| Full reference histories | 11 | 11 |
| Polarization/vacuum histories | 14 | 14 |
| Clock interaction provenance | 7 | 7 |
| New ordered Current four-point limit | 15 | 15 |
| New microscopic four-point comparison | 12 | 12 |
| New local Clock/rotor charge classification | 10 | 10 |
| Total in the recorded run | **112** | **112** |

Every listed suite passed. These counts are regression coverage, not
independent physical predictions, external reviews or TOE evidence.
The inherited frozen Clock source emits its preexisting ResourceWarning
about an unclosed read handle. It remains visible in the transcript; no
upstream source was changed or warning silently suppressed.

## What was independently checked

The new tests include an independent fixed-number CAR implementation of the
four-point word, rather than comparing two calls to the same BCH formula.
They check exact integer windows, source polarization, the new symbol and
energy bounds, normal phase, the full original 16N source, complete four-leg
histories, pair-Gram reversal and a control where replacing a nonalternating
physical U word by a signed F word is demonstrably wrong.

The Current suite separately tests sequential coherent Weyl composition,
the one-oscillator product, all six neutral four-leg CAR determinants,
complex phase, ordered branches and a false Wick-sum control. The L1
theorem is the written analytic proof, not these finite samples.

The new Clock suite checks the original permutation/characteristic polynomial,
all 7776 single-edge phase assignments, all 1296 square site-grade assignments,
the full two-step list, exact symbolic Gauss identity, full H matrix elements
at both signs of large electric flux, noncontractible torus holonomy and the
nondegenerate onsite U(2) commutant. The key three-link/Gauss/spectral proof
was independently derived in the parallel branch; the root then checked the
source and implemented the reproducible artifacts. Clock diagnostics are in
`../clock-rotor-joint-charge/diagnostics.json`.

The complete new source README/checker/tests and their decisive inherited
estimates received an independent read-only mathematical review, with no
load-bearing gap found. That reviewer independently reran 12 tests in both
modes. The general-L Galerkin exponent and the placement of the normal
phase at the Fock-vector level were clarified. The root independently read
the complete Current README and checker, including BCH, full-torus Lp/Vitali
and Gram positivity. Neither review is external peer review or formal verification.

## Reproduced implementation failure and regression

The systematic-debugging workflow was applied to a large-N numerical-output
failure: `numpy.sqrt(16*N)` selects object dtype once a Python integer exceeds
the machine integer range, raising an AttributeError/TypeError. A minimal
reproduction and a failing test at N=2^96 established the cause before the fix.
The fix converts only the dimension argument used in floating majorant
evaluation to float. Lattice sizes and cutoffs remain exact integers.
The new regression passes normally and with -OO. It does not change any
analytic bound or turn the evaluated bounds into interval enclosures.

## Source diagnostics

[diagnostics.json](diagnostics.json) was regenerated after the final pin update.
It contains full microscopic words at N=8,16,32 and the held-out unsymmetrical
word (1,5,13,21)/24. The largest common-rest amplitude identity residual is
2.32e-13. Both analytic windows are evaluated at large N without constructing
enormous matrices. Some coarse bounds are huge before their asymptotic regime;
the output retains them rather than silently replacing them by observed errors.

The checker transitively validates the previous microscopic source chain and
also pins the independent Current four-point checker and proof document.
The final hashes of the new core files are:

```
checker.py
976f8a82d00f312a2bc63c29c3a182efb54fe248370eb7d9568b37705464672f
test_checker.py
dbef31b6c46f95103e6f9384b15da96c69c52b10563a50fb317c200f207021a6
README.md
037599f5778d2697b8f03cd1b288144edd8582e023dda11ed6dfcfd81eef9ab2
diagnostics.json
a7d1a7310ddaf9e33878e3510e70f3ed5c02db63f0840a3f3a8ab82debbc1e05
```

## Reproduction

From this directory, `python3 checker.py --output diagnostics.json` regenerates
the floating source diagnostics. `python3 -m unittest -v test_checker` and
`python3 -OO -m unittest -v test_checker` rerun this suite. The sibling
Current checker prints its own diagnostic JSON. `run_verification.py` runs
each declared suite in an isolated process and records its full transcript.

Only new research artifacts and additive research-index entries are in scope.
No historical checker, physical source, paper, website or status ledger was
modified. No commit or push was performed.
