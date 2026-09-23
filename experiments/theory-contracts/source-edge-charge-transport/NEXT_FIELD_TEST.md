# Next test: measure the actual half-transfer, not just its endpoints

This file specifies the next experiment; it does NOT report an executed
intersector-field construction.

The new charge operators provide an independent acceptance measurement
for the existing microscopic disorder/filtered-twist candidates. Keep
their original source, preparation, filter and normalization provenance.
Do not define a new transport by assigning arbitrary eigenvector labels.

## 1. First source background to second

For a proposed renormalized smeared field `V_(3<-1),N(F)`, test on each
fixed particle/hole core, including the actual filled vacuum,

```
[Ctop_(N,3) V_(3<-1),N(F)
 - V_(3<-1),N(F) Ctop_(N,1)
 - (1/2) V_(3<-1),N(F)] psi_N -> 0.
```

The bottom equation has -1/2 in place of +1/2. Total charge must be
preserved. The same test for the adjoint has reversed backgrounds and
opposite charge. Use the actual common-reference regional operators,
not an imposed abstract half-charge register.

The limit must have a nonzero smeared norm. A vanishing candidate would
pass the displayed homogeneous Ward residual vacuously. The norm of the
output, its H graph norm, and both adjoint matrix elements must therefore
be reported alongside it. Mean charge alone is insufficient; its variance
and off-vacuum action must also be controlled.

The currently available original Gaussian microscopic twist is a concrete
first candidate to measure. A finite Slater covariance calculation can
reject it early: for its one-body unitary U and initial sea P1, compute
`D=U P1 U*`, then `Tr(D A3)-Tr(P1 T)` and
`Tr[D A3 (I-D) A3]`. These are full-sea charge mean and variance. Passing
this finite test would still not prove the renormalized smeared limit.

## 2. Second forward half step is not the adjoint

On the target source-charge dictionary the forward step after r=3 must
return to the r=1 background with `(q_top,q_bottom)` increased by `(1,-1)`.
Thus a two-step forward composition must carry an actual integer edge
excitation. A map sending each ground state to the other and then back
to itself is merely a two-state flip and fails this test.

The inverse/adjoint of the first step decreases charge; it must not be
mistaken for the second forward step. Require the corresponding source
current and cocycle composition, including on excited states.

## 3. Physical limitations that this test does not waive

- The present r backgrounds are externally specified. A microscopic
  source-selection argument is still needed before treating their direct
  sum as the chosen TFPT system.
- A Kato/spectral ground-space transporter alone need not be local and
  would not establish a field with the required source support.
- If a continuous flux-insertion route is pursued, both its spatial
  support and its N-dependent time/gap budget must be controlled. The
  full-cycle level crossing cannot be replaced by instantaneous vacuum
  reselection without losing the required integer carry.
- No half-field test here identifies the eight E8 channels, the Clock
  marking or the interacting rotor parent automatically.
