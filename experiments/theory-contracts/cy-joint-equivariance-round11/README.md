# Round11: simultaneous elliptic clock and inversion

[The complete proof](JOINT_EQUIVARIANCE.md) constructs the joint C4 x C2
linearization of the rank-four orbit bundle. There are exactly two choices,
with explicitly necessary eighth-root phases. The two descended lines on
the free degree-two quotient have order eight, while their pullbacks have
order four. Both choices have determinant character (-1,+1), and both fail
ordinary coarse Kummer descent; stack/orbifold data cannot be discarded.

The same construction refines the previous flat boundary operator: resolving
both symmetries splits the momentum-parity subsets. One holonomy orbit has
squared-frequency gaps 1/16 and 9/16, while the other has equal 5/16 gaps and
an exact all-spectrum parity bijection. The original four clock-character
spectra remain equal before this additional resolution. No particle mass,
family count, chirality or physical projection is selected by this result.

`test_joint_equivariance.py` supplies six unittest groups covering the exact
finite torsion data, both lift choices and their relations, determinant and
descent checks, and spectral regressions. The geometric and all-mode proofs
are in the note, not inferred from a finite sample. Use `../run_round11.py`
for the bounded combined run and source-hashed evidence.

This construction continues [Round10](../cy-seam-round10/README.md), without
identifying the boundary bundle with the separately chosen matter/gravity
completion. No full T1-T8 closure or RH claim.
