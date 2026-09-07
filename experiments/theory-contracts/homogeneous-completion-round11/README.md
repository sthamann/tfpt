# Round11: two different constant-mode problems

The two results in this folder must not be conflated.

1. [Auxiliary zero modes](AUXILIARY_ZERO_MODE.md): five constant traceless
   slacks and explicit deletion of three redundant auxiliary coordinates
   give an invertible global saddle matrix. All introduced pairs are removed
   by regular second-class constraints, including the constant block. This
   is an exact representation of the existing **zero-mean reduced** model,
   with zero energy response to constant sources. It is not a gravitational
   energy or momentum receiver.
2. [Quantum trace clock](QUANTUM_CLOCK.md): for the **postulated** single
   global constraint C=A-P^2/12 with A>=epsilon>0, convergent group averaging
   constructs the positive physical norm, the physical Hilbert completion and
   unitary intrinsic-time evolution. The actual unsubtracted finite positive
   model satisfies the gap assumption for m>0, or m=0 with n>1. The absolute
   energy reference and time orientation remain choices. A finite-translation
   invariant sector is a consistent optional joint restriction, not a proof
   of the old continuous momentum constraints.

Reproduce with `auxiliary_zero_mode.py` and `quantum_clock.py`, or use the
combined `../run_round11.py`. Exact finite regression groups supplement the
general proofs. Independent review checked the global auxiliary block and
the quantum-clock domain, normalization, gap and finite-translation argument.

The actual old-momentum preservation failure and reduced-algebra locality
boundary are established in [the separate audit](../reduced-locality-round11/PROOF.md).
The compatibility of the auxiliary construction with the finite dressed
first-class constraints is established in
[the mixed-system theorem](../mixed-constraints-round11/README.md).

All results are unpromoted research contracts. They neither close a full
T1-T8 gate nor derive a common microscopic TFPT model or continuum limit.
