# The complete weighted-grade-seven source on the original edge

2026-09-08. **NON-RH / finite conditional same-parent algebra.**

This companion experiment is independent of the unfinished Round50 bulk
calculation. It uses the pinned Round49 original Hamiltonian and adds all
twelve electric event words with #M+2#E=7, while retaining all earlier
families and the independently resummed pure-matter source:

```
MEEE    MEEMM   MEMEM   MEMME   MEMMMM   MMEEM
MMEME   MMEMMM  MMMEE   MMMEMM  MMMMEM   MMMMME
```

The three pMM words are the same formal second-matter family considered
in Round50. The remaining nine are obtained by complete original M
derivations, one more first-E depth, and a general third-E phase difference.
No Round50 probability or validation is read or assumed.

## The new finite phase-difference construction

For an existing literal source with prefixes r_i and signed branches
(f_b,s_b), enumerate ALL original hopping-force monomials (a,b,p,w)
meeting any prefix. Prepend the literal pair c_a^* c_b, form final current
r+p, and append its full original onsite/current energy as the last
frequency. Keep both the unshifted branch and its shift

  delta = (0,24 r_1 dot p,...,24 r_n dot p,0),

with opposite signs. Thus each new E event doubles the branch count and
adds a genuine phase difference; none of the old branch pairings is lost.
The old difference vectors gain one trailing zero, and the new vector is
(r_1 dot p,...,r_n dot p,0). This follows from the finite shift commutator
F(E)-F(E+p) and the original left bilinear multiplication. It is not
projection onto initially allowed words.

The implementation reproduces the pinned MEE, MEME and MMEE formulas as
exact signed literal/frequency dictionaries. The extended first-E formula
also reproduces all four older depths before using depth five. Seven-leg
words from MEEE are acted on as complete ordered CAR products; repeated
modes are not pruned merely because of the initial state.

## Independent physical check

Use the entire original 6-state neutral and 4-state charged sectors, not
an isolated two-level surrogate. Compare the source against the exact
matrix coefficients of exp(i H_Q t) c_H,0 exp(-i H_N t). After removing
the common i^j factor, its order-j coefficient is

  sum_(k=0..j) (-1)^k H_Q^(j-k) c_H,0 H_N^k / ((j-k)! k!).

All four E0 input columns are checked, including coherent matrix elements.
The new complete source agrees at orders 0 through 7 and fails at 8.
The source with only the second-M addition fails at 7. Every one of the
twelve families has a nonzero physical coefficient at 7: removing any
single family breaks equality there. The generated record contains all
exact rational matrix entries and individual contributions, not only
Boolean conclusions. There are 12392 new raw edge paths in total.

## Reproduction and scope

From the repository root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/seventh-frontier-edge/checker.py --output experiments/theory-contracts/seventh-frontier-edge/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/seventh-frontier-edge -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/seventh-frontier-edge -p 'test_*.py'
```

Success verdict: `COMPLETE_WEIGHTED_GRADE_SEVEN_SOURCE_ON_ORIGINAL_EDGE_ONLY`.
The frozen parent and all local source files are checked by hashes.

This closes a **finite source-coefficient construction**, not the full
electric dynamics, an infinite-volume theorem, or a new cubic error
certificate. It supplies no new bulk probability, interval, configuration
bound or universal O(t8) claim. In particular, the full cubic raw census,
all new M/E boundary estimates and a changed common bulk column are still
required. The original parameters and preparation remain assumed; T1-T8,
chirality and universal spin-two emergence remain open.

Experiment firewall: local theory-contract work only, outside the evidence
scorecard. No paper, website, verification, ledger, commit, push, empirical
or proof-assistant promotion is included.
