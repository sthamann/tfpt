# Round11: actual-source locality and momentum preservation

[The proof and model boundary](PROOF.md) establish two obstructions for the
**chosen** positive reduced Hamiltonian, not an impossibility theorem for TFPT.

* The actual scalar stress gives a nonzero first-time-order response between
  separated bounded scalar operations. An all-size cubic argument has a
  nonzero 3/(4 ell_z) pole in the normalized plane Hessian, ruling out one
  fixed finite interaction range on this same scalar observable algebra.
  A local static auxiliary representation alone does not resolve this.
* The old centered-difference total momentum is not conserved at order g^2,
  even at a point with all old momentum constraints zero. A directly checked
  cubic 6^3 witness gives {J_z,R}=-568433/21952. The Hamiltonian still respects
  actual discrete lattice translations; these are different symmetry claims.

The checker uses exact actual stresses and complete staggered Fourier kernels,
with trace/longitudinal annihilation, real TT normalization, independent
four-energy Hessian and discrete-translation controls. Both rectangular and
strict cubic witnesses are checked. No floating tolerance or truncated CCR
matrix is used. Independent source/kernel review is recorded in the round
overview; see `locality_check.py` and the combined `../run_round11.py`.

`redteam_source_projector.py` separately imports the original Ward formulas,
compares 648 stress components, three total-current signs and 162 Hamilton-flow
coefficients, and reconstructs the weighted TT projector from its nullspace at
all 53 nonzero modes of the 3x3x6 witness. It therefore cross-checks the actual
repository inputs, rather than relying on the standalone checker alone.

These obstructions preserve important alternatives: another relational or
gauge-dressed local observable algebra, a different interacting parent, and
a controlled continuum limit are not ruled out. The exact finite-translation
invariant restriction in
[the conditional quantum clock](../homogeneous-completion-round11/QUANTUM_CLOCK.md)
is consistent, but its allowed local operations must be specified anew.
No generic Coulomb-gauge acausality claim or blanket Lieb--Robinson no-go is made.
