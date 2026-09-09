# Verification record — 2026-09-08

Source checkout: b803b7e5 with preserved pre-existing uncommitted research
artifacts. This round adds the two named contracts and prepends the
experiments index/next-step log. No commit, push, paper/site modification
or completion-marker promotion.

| Folder under experiments/theory-contracts | Normal | Python -OO |
| --- | ---: | ---: |
| neutral-current-limit | 13 pass | 13 pass |
| carrier-module-conjugation | 9 pass | 9 pass |
| origin-composition-audit | 10 pass | 10 pass |
| neutral-pair-composition | 13 pass | 13 pass |
| compiler-clifford-bridge | 18 pass | 18 pass |
| charged-cocycle-lift | 20 pass | 20 pass |
| half-twist-grade-carry | 23 pass | 23 pass |
| gaussian-vacuum-filter | 21 pass | 21 pass |
| Total per mode, all rerun this round | **127 pass** | **127 pass** |

Commands: python3 [-OO] -m unittest discover -s <folder> -p test_checker.py.
The two new checker CLIs regenerated diagnostics.json and validation.json.
The source comparison includes the complete N=128 occupied determinant,
N=64 filter coefficients 2 and 6, and nine finite source Schur factorizations
at N=16,32,64. Saved tests verify the producing checker hashes.

Independent parallel review checked the current normalization, sign,
positive coefficient recursion, L1/distributional limit and Schur/phase
proofs. Its clarifications about the logarithm branch and the oscillator
factor versus a complete charged field are included in README.md.
The carrier construction was developed in a separate parallel line and
replayed against the pinned source in the main checkout. A final independent
review also reran all nine carrier tests in both modes and checked the
zero-mode covariance classification; its covariance-versus-density-matrix
qualification is included in the carrier README.

Tests are finite algebra and floating diagnostics, not a microscopic
scaling-limit theorem, all-n-point reconstruction, physical parent
selection, complete T1–T8 evidence, TOE or RH proof.

SHA256 of the producing code and final saved records:

- Current checker: 2e4a03cbacc3bc0ed4835facd85e8abce2f2585d717abc56fc2dc57f6b67c136
- Current diagnostics: 60296741a383705f723c915d77e510f115fc0ac83b8796bb90f36b1eacb7b9f6
- Carrier checker: 87cd67ca2588a41aec5b1237250e45cca69f40ff7701c9a38206c6a0d29af1e7
- Carrier validation: 4797d2ffe136d96094bad97e7a293c0eafc07cccde78e30c39d8a1f78b339151

The finite Gaussian series has a proved truncation bound. This does not
certify all floating-point errors in the dense microscopic calculation.
