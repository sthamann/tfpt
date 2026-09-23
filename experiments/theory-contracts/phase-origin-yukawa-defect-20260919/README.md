# Phase-origin Yukawa defect — scoped experiment contract

This `experiments` contract records exact anomaly algebra and a conditional
rank/period calculation around the existing Yukawa determinant exponents
`(6,9,10)`. It does not promote a physical axial field, photon coupling,
complex source, QCD response, or domain-wall index.

Run the copied checker with:

```bash
python3 -B check_phase_origin.py
```

Expected result: `38/38` checks pass and the copied result remains
`PARTIAL_SOURCE_SELECTION_OPEN`.

The contract keeps three layers separate. The all-left-handed block traces
are exact rephasing traces; the `(12,15)` three-component torus statement is
conditional on those columns being complete non-cancelled responses of
independent physical fields with an independently assumed compact torus; and
the written PLB EFT plus an independent complex seed gives the separate
conditional row `(0,15)`, with 15 components. A derivative-only torsion
coupling with fixed masses has its constant QCD response cancelled by the
mass/Jacobian Ward identity.

The source manifest pins the primary repository locations and the final
checker/result bytes. Positive real mass exponents are recorded as real source
data; they are not presented as a complex field. `HERLEITUNG.md` is not pinned
here because it is still a source report rather than the primary input for
this contract.
