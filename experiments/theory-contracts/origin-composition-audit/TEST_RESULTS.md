# Verification record — 2026-09-08

Current source checkout: b803b7e5, with the named pre-existing uncommitted
research artifacts. No commit, push, paper/site update or marker promotion.

| Test folder under experiments/theory-contracts | Normal | Python -OO |
| --- | ---: | ---: |
| origin-composition-audit | 10 pass | 10 pass |
| neutral-pair-composition | 13 pass | 13 pass |
| compiler-clifford-bridge | 18 pass | 18 pass |
| charged-cocycle-lift | 20 pass | 20 pass |
| half-twist-grade-carry | 23 pass | 23 pass |
| gaussian-vacuum-filter | 21 pass | 21 pass |
| Total per mode | **105 pass** | **105 pass** |

Commands: `python3 [-OO] -m unittest discover -s <folder> -p test_checker.py`.
The two new checker CLIs generated validation.json and diagnostics.json.
Source-pin chains and unchanged theory-file status were checked.

Exact algebraic/finite-series record is separate from floating N=8,16,32,64
diagnostics. Green tests are not proofs of a field limit, physical parent
selection, gauge-equivalent carrier marking, continuum TOE or RH.

The initial optimized-mode import failure and final metadata-only adapter
are described in README.md. The legacy census and charged source hashes
remain unchanged. No assertion-based mathematical check was replaced by
a success constant; new deciding guards use explicit exceptions.

Current SHA256:

- Structural checker: `81a92db3092f6fe03a7b25901a46e540063a4b549ab34ba81fce007110b836a2`
- Structural validation: `1b9c8abc6b834e6f33392dd4338cfc6c93d0fe41f3821bb5cbf3e60548b16721`
- Neutral checker: `95e9c38fd176681160ff5dae5764cf53acee70832a6f4a92ef6fcbf13305bca4`
- Neutral diagnostics: `7a31d7e62724dafd53f80c0f4a5596831eef9c3299984fcb8332119d799064cb`

The validation hash is checked again at final handoff because adding an
exact certificate changes the recorded checker hash and output.
