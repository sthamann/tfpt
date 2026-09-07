# Round15 internal review record

2026-09-06. This records agent-assisted independent derivation/checking and
root integration review. It is not external peer review, a formal proof
certificate, an empirical test, or a T-gate status change. Reproducible
execution evidence is stored separately by run_round15.py.

- Minimal stability: independently read in full by the matter/geometry
  lane and by root. Quantum negative-quartic scaling, compact-core passage,
  classical completeness, source-image limitation and uniform-in-g argument
  were checked. Independent normal/optimized checker runs passed 49 groups.
- Vertex-preserving forms: independently read in full by the stability
  lane, including the primary common-form theorem hypotheses. The uniform
  energy bound, zero-fiber continuity, regularized norm and first jet were
  checked. Root added the explicit integral difference-quotient bound for
  the full generator. Independent optimized execution passed 35 groups.
- Local parent: root read the whole proof and checker. Exact fast Hessian,
  signs, zero modes, Gaussian derivative constants, core residual and
  uncompressed unitary convergence were checked. The author ran 50 groups
  normally and under optimization; root re-executes the integrated artifact.
- Eight-channel construction: the local-parent lane and root read the
  entire proof/checker. The lattice isometry, GSO, cocycle, finite code and
  different fourth powers were checked. Review corrected a locality phrase:
  the defect spans the whole far transverse cut, not one point. Root added
  a source-matrix negative control for the single-transverse-bond mutant.
  The integrated count is 29 exact and five floating source-matrix groups.

The systematic-debugging workflow was used for source/claim mismatches:
the literal QWZ matrix loop contains every transverse y bond, whereas an
earlier phrase suggested one bond. The proof now states the full support;
the regression computes a nonzero error for the point-supported mutant.
This changes the documented claim, not the hopping Hamiltonian.

The four outputs are not identified with one another beyond their stated
interfaces. In particular the vertex-preserving Hamiltonian is not the
separated Round14 joint clock operator; the local parent retains extra free
energy; and the finite charged transporter is not the lattice vertex field.
No old proof, ledger, paper or website claim was promoted during review.
