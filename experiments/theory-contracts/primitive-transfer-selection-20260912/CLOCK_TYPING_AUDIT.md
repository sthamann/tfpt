# Clock: covariance, gauge and retained records

Date: 2026-09-12. Finite candidate-source audit, not a TFPT closure.

## Source conclusion

`experiments/tfpt-discovery/seam_state_derivation_probe.py`, opening contract,
explicitly studies a C6-covariant KMS **candidate family**. Its actual seam-state
realization and parameters remain open. The reviewed source does not derive a
Gauss constraint requiring every physical measurement effect to commute with O.
This is absence of a derivation in the inspected sources, not a theorem that O
must be a physical global symmetry rather than gauge.

`experiments/theory-contracts/clock-marking-audit/README.md`, section
"Warum kein Markierungs-No-go folgt", already makes the gauge interpretation
conditional. Therefore `CLOCK_INVARIANT_HIDDEN.md` classifies a conditional
observable restriction, not the established full physical observable algebra.
Its matrix classification remains valid; applying it unconditionally would not.

An older warning exists in `verification/v522_woit_beta1_gso_gauge.py` and
`tfpt_research_contracts.tex` (beta1 stage, near line 12259): the NS seam's
mu4/Z8 clock was incorrectly treated as the gauge datum instead of parity/GSO.
That is a DIFFERENT clock and model. No intertwiner identifying it with this
C6 action has been derived here. Its RP results cannot be transferred.

## Explicit covariant measurement, conditional on additional access

Use the pinned source reconstruction in `boundary_access.py` and the fully
checked CAR bridge in `even_carrier_bridge.py`:

    b=e_10, v=(I-P)(e_0+e_6), ||v||^2=7/6,
    F_k=i gamma(b) gamma(O^k v)/sqrt(7/6),  k=0,...,5.

Each F_k is Hermitian, parity even, and F_k^2=I. The finite Fock lift U of O
exists here because O preserves J and acts unitarily on the eight complex
one-particle modes; second quantization gives U F_k U*=F_(k+1).
Also sum_k F_k=0. Define twelve effects

    E_(k,s)=(I+s F_k)/12, s in {-1,+1}.

Their spectra are {0,1/6}, their sum is I, and conjugation by U permutes k.
Thus this is a valid covariant POVM, although the individual effects are not
invariant. The ordinary POVM definition is positivity and normalization, not
invariance of each effect; see [IBM's measurement formulation](https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/general-measurements/formulations-of-measurements).

The two explicitly additional witness states rho_r=(I+r F_0)/256, r=+/-1,
are normalized and positive. Their outcome probabilities are

    p_r(k,s)=(1+r s g_k)/12,
    g=(1,-5/7,1/7,1/7,1/7,-5/7).

For example p_+(0,+)=1/6 while p_-(0,+)=0. They are statistically
distinguishable, not asserted perfectly distinguishable in one trial.
Forgetting k gives p_r(s)=1/2 for both states: averaging erases the distinction.
The orbit spans only three operator directions, not an informationally complete
measurement of the 256-state Fock space. The number vacuum has <F_k>=0 and
uniform outcomes 1/12; this measurement does not manufacture a vacuum signal.
The witness states and apparatus are not claimed to be source-preparable.

## Even a gauge reading permits a relational question, with an extra resource

As a purely conditional dilation, append a six-state reference |k> with cyclic
shift S|k>=|k+1>. The two joint effects

    A_s = sum_k |k><k| tensor (I+s F_k)/2

are positive, sum to I, and commute with S tensor U: both indices shift together.
For a stipulated reference |0>, their system statistics are those of F_0.
For an uncorrelated maximally mixed reference I_6/6, their effective system
effects are I/2 and all sensitivity disappears. This is the simple distinction
between a relative orientation and an erased orientation.

If the joint action really is gauge, independently assigning an absolute
reference state is not a physical preparation proof. Jointly twirling a product
state preserves the statistics of invariant A_s, but presupposes preparation of
the corresponding reference-system correlations. Neither a six-state physical
reference nor these correlations nor the coupling has been derived from TFPT.
The construction therefore relocates the question to a precise resource
obligation; it does not solve that obligation by adding a reference by hand.

## What actually changes in the search

Do not impose Clock averaging on every candidate readout without deriving the
gauge/record contract. Conversely, covariance does not create access: every F_k
crosses the exact P/Q boundary-carrier split. The boundary-only no-go remains.
The next positive result must identify, in the same source, an accessible
reference or carrier coupling and a preparation producing a nontrivial response.
If all such source operations remain in the boundary algebra, these candidate
readouts are unavailable despite being mathematically consistent.

Verification: `clock_covariant_readout.py` passes 18 exact checks in normal and
`-OO` modes. It checks source geometry, orbit and witness probabilities, with
Clifford positivity proved above; it is not another full Fock matrix test.
`even_carrier_bridge.py` was independently rerun in normal mode: 18 checks,
including the full 256-dimensional Hermiticity, parity and involution identities.
The joint-reference argument above is analytic, not a separately executed
1536-dimensional matrix test. No T1-T8 item, RH claim, or universal-object
uniqueness claim is closed. No original source, paper, or status ledger changed.
