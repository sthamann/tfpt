# Provenance validation — 2026-09-08

## Executed final checks

| Check | Result |
| --- | --- |
| Normal `python3 -B -m unittest discover -s experiments/theory-contracts/clock-interaction-provenance -p test_checker.py` | 7 tests passed, 4.639 s |
| Same invocation with `-OO` after `-B` | 7 tests passed, 4.679 s |
| `python3 -B experiments/theory-contracts/clock-interaction-provenance/checker.py` | Successful; complete output stored in `validation.json` |

There were no failed mathematical checks or code fixes in this experiment.
The unchanged upstream ResourceWarning at `seam_state_derivation_probe.py:366`
appears when the original prefix is loaded. It is not suppressed. Its pinned
legacy adapter retains source assertions through optimize=0 compilation;
this is not a claim of legacy-source OO hardening. New checks use explicit
exceptions and unittest assertions.

The bounded exact checks comprise:

- All 14400 ordered quadratic Majorana basis brackets; 3360 nonzero,
  all degree two, none degree four.
- Exact rank-two abelian Lie span of the actual source matrices A0 and B.
- Original-source six-coordinate Grassmann integration and logarithm:
  raw quartic coefficient 61/64, connected quartic coefficient zero,
  exact Schur exponent.
- Actual compact-parent low-link double commutator on all 16 original
  L0,L1,H0,H1 Fock masks and arbitrary symbolic integer flux E.
- Full original two-site hopping list projection onto q_L0 q_L1 retains
  coefficient -1/7200, including all other Low/High link terms.
- The grade-three occupation parity implements O cubed on all 16 original
  Clock Majorana generators.
- A direction in the already classified invariant quartic space is not
  occupation diagonal; full generatedness is not asserted.
- Source-pin mutation and explicit no-promotion guards.

No Grassmann, rotor, CAR or operator identity here relies on floating-point
eigenvalues. No infinite flux cutoff, fitted coefficient, selected new
Hamiltonian term or externally imposed response was used.

## Source verification

The code checks the SHA-256 of the four direct source files recorded in
`validation.json`; the Clock source adapter and compact parent also check
their original transitive pins. The original sixteen-Majorana source remains
at `5e54c416be72a125a8ce6e235b4300f9f9c2344b3ada796d2dc4c7e2ea01482b`.

Final experiment hashes:

    checker.py
    f1bc93d39c8f84f76bff55da901908dcd2ba97975753992464484279ebef3506

    test_checker.py
    bcb6bb4750b3617405252cc7b2f04333bd197377cc2f69b70f516671995ceec3

Graph-first discovery was attempted using the codebase-memory skill. The
project listing and search both confirmed TFPT is not indexed; targeted
source-file fallback was used. No index was built and no foreign active
research files were edited.

The electric/rotor result belongs to the existing compact lattice parent,
not automatically to the sixteen-Majorana Clock. Its physical dictionary,
effective-action derivation and TFPT parameter selection remain open.
Only this experiment folder was written. No old source, index, paper,
website, commit, push or TOE/RH completion marker changed.
