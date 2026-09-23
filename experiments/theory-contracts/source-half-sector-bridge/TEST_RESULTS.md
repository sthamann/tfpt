# Verification, 9 September 2026

Local, after `66b91e40`; neither this branch nor the preceding
`half-charge-energy-bridge` is part of that publication.

- Python 3.14.3, ordinary mode: **16 tests passed**, 0.776 seconds.
- Optimized `-OO` mode: **16 tests passed**, 0.790 seconds.
- Direct source checker: completed successfully. Full output in
  [validation.json](validation.json).
- Full cylinder covariance/energy diagnostics: N=16,32,64, sectors 1 and 3,
  both edges; matrices of dimensions 256,512,1024 and original sea ranks
  128,256,512. The largest polarization residual was 1.38e-14.
- Fixed-regulator covariance comparison at z=0.7, t=0.4: for sector 3's
  top edge, errors were approximately 0.26310, 0.005149 and 0.00001714
  at N=64,256,1024, all within the written analytic cap. These are floating
  diagnostics, not interval arithmetic or a uniform cutoff-removal proof.
- Exact rational tests include arbitrary integer-charge energy formulas,
  compensated half charges, noncyclic transfer and its inverse/adjoint,
  and finite excitation energies above charge minima.
- Independent symbolic covariance calculation confirms the opposite
  half shifts and the noncommutation of cutoff removal and coincidence.
- Negative controls reject mutated source pins, half-integer input to the
  integer source charge function, wrong sectors/windows and a cyclic flip.

The all-charge and scaling claims depend on the written proofs and their
explicit hypotheses in `README.md`. These tests are not independent
mathematical review, construction of the local intersector field or
closure of any T1–T8 gate. The selected physical current prescription,
opposite-edge factorization and E8 realization remain open.
