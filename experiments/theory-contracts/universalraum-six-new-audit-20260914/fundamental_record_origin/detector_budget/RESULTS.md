# Detector color-information budget for the complete Q-free experiment

2026-09-14. Conditional finite-instrument result, not a physical detector-origin
or foundational closure claim. All probabilities below are per started trial.

## The important result

The complete available classical record does not separately identify
preparation coherence and end-detector coherence. In this model it identifies
only their product. A perfectly prepared Omega with a completely
color-dephasing end detector and a fidelity-1/6 preparation with an ideal end
detector produce exactly the same classical histogram, for the same middle
detector. This includes **all final eight-bit strings**, not just the accepted
all-zero event.

Moreover, if the intermediate detector is ideal, the recorded/retained ratio
remains exactly **17/32**, however bad the preparation and end detectors are.
An ideal contrast quotient alone therefore does not certify good preparation.

## Complete instrument, without renormalized branches

For an addressed edge let P- be its antisymmetric projector and
B_c=W†|c><c|W the six mutually orthogonal color projectors, including the
identity on unaffected spectators. Thus sum_c B_c=P-. The actual A/readout/A
instrument on bare matter is

    I0(rho) = P+ rho P+,
    I1,eta(rho) = eta P- rho P- + (1-eta) sum_c B_c rho B_c.

These are completely positive outcome maps and their traces sum to tr(rho).
Here eta is the weight of the ideal color-blind detector, not its error rate.
Preparation selects occupied outcome1 on edge03. The retained echo has no
intermediate measurement; the recorded echo sums both outcome maps on edge01.
The end test again selects edge03 outcome1, applies the inverse xi circuit and
accepts its eight-zero result. Every hidden color history retains its raw
weight throughout the calculation.

Use a, b, c for the ideal weights of preparation, intermediate and end
detectors. Distinct detector applications are assumed independent, with no
unmodeled shared environment memory. This is a memoryless-instrument premise,
not a claim that physical reset is free. A common numerical eta means
a=b=c=eta **with independent applications**, not one common Bernoulli choice
for the entire trial.

## Exact probabilities

    p_prep = 3/8,
    F_prep = (1+5a)/6,

    p_retained = 3(1+5ac)/128,
    p_recorded = 3(19abc+66ac+3b+14)/4096.

For the recorded experiment additional raw flag probabilities are

    p_echo_occupied = 9/64,
    p_end_occupied = 3(b+10)/128,
    p_success_and_echo0 = 75(1+5ac)/8192,
    p_success_and_echo1 = 3(38abc+7ac+6b+3)/8192.

Preparation rejection is always5/8. The end failure after successful
preparation has raw weight3/8-p_success. The complete flag accounting sums to
one; no failure or hidden-color outcome has been silently discarded.

At common independent eta,

    p_retained = 3(1+5eta²)/128,
    p_recorded = 3(19eta³+66eta²+3eta+14)/4096,
    gap = 3(18-3eta+94eta²-19eta³)/4096.

| Common eta | Prep fidelity | Retained raw | Recorded raw | Ratio |
|---|---:|---:|---:|---:|
| 1 | 1 | 9/64 | 153/2048 | 17/32 |
| 0 | 1/6 | 3/128 | 21/2048 | 7/16 |

Complete color loss still leaves a positive raw contrast27/2048. The existence
of a contrast alone is therefore not a high-fidelity witness. Within the
strict common-eta model its ratio equals17/32 only at eta=1, since

    ratio - 17/32 = (eta-1)(19eta²+3) / [32(5eta²+1)].

If instead a single hidden detector condition is perfectly correlated across
the trial, the retained raw rate is3(1+5eta)/128, not the independent-use
quadratic. The replay rejects this substitution as a negative control.

## End measurement changes its meaning, not only its efficiency

Let |psi_c> be the six normalized, mutually orthogonal Schmidt components of
Omega across edge03 and its spectators, and Q6=sum_c |psi_c><psi_c|. The actual
noisy end effect on the full bare256D matter space is

    E_c = (3c/8) P_Omega + (1-c) Q6/16.

Its eigenvalue on Omega is(1+5c)/16; the five orthogonal directions within Q6
are accepted with probability(1-c)/16; the remaining250 directions have zero
acceptance. Thus the end detector can accept states orthogonal to Omega. It is
incorrect to treat it as an otherwise ideal projector with smaller efficiency.

This effect and the prepared state

    rho_prep = a P_Omega + (1-a)Q6/6

immediately reproduce p_retained above. The recorded polynomial was derived
from the full intermediate instrument and checked independently by rational
density-matrix propagation, not by replacing the echo with eta raised to a
power or by assuming an ideal end effect.

## What the classical data do and do not determine

Writing x=ac, the retained raw rate determines

    x = (128 p_retained/3 - 1)/5.

The recorded end-occupation flag determines

    b = 128 p_end_occupied/3 - 10.

They do not split x into a and c. This is true of the entire accessible
histogram, including all final bit strings. For each endpoint b=0,1 the exact
histograms obey H00=H10=H01, where indices denote a,c; multilinearity then gives
H(a,b,c)=H00(b)+ac[H11(b)-H00(b)] for every allowed a,b,c.

The minimum extra information needed within this model is an independent
coherence calibration of one boundary instrument, a or c. Knowledge of both
boundary calibrations is not obtained from the observed path probabilities.
Assuming a=c is itself additional calibration information; under that
assumption eta=sqrt(x) and the preparation fidelity follows.

Absolute rates nevertheless give a model-conditional lower bound because
0<=c<=1 implies a>=x:

    F_prep >= (1+5x)/6 = 64 p_retained/9.

Thus nearly maximal absolute retained success can certify nearly ideal
preparation within this specified noise model. Low rates are ambiguous:
preparation, end readout, or both may be responsible. Neither these bounds nor
the exact parameter inversion apply unchanged to arbitrary detector faults.

## General environment Gram matrix and permitted color leakage

For color-preserving coupling |c> -> |c>|e_c>, normalized environment vectors
define G_cd=<e_c|e_d>, G positive semidefinite with diagonal1. The prepared
Omega fidelity after the environment is discarded is

    F_Omega = (1/36) 1† G 1,
    1-F_Omega = (1/36) sum_(c<d) ||e_c-e_d||².

Known Schmidt signs are absorbed into the definitions of |psi_c>. Complex
environment overlap phases are included; they can disturb coherence even
without directly distinguishable classical color populations.

The present detector model has G=eta 11†+(1-eta)I, giving
F=(1+5eta)/6. To keep preparation infidelity at most epsilon requires exactly

    1-eta <= 6epsilon/5.

For epsilon=10^-6 the full-color-dephasing weight may be at most1.2e-6. In the
general Gram description the total pairwise squared environment separation
must be at most36epsilon. This is an operational coherence budget; it is not a
derivation of a detector or a universal classical information-capacity bound.

Successive use would multiply corresponding Gram entries only for the same
color decomposition with fresh independent environments and no intervening
mixing. The present clock and changed edge do mix these decompositions, which
is why the complete protocol was calculated explicitly.

## Verification

775 always-on exact guards; normal and optimized Python outputs are required
to be byte-identical. The implementation calculates all12 endpoint ensembles,
interpolates exact multilinear polynomials, checks independent full-density
propagation at five rational parameter triples, and verifies the complete
classical histogram identities. Three mutants must fail: idealizing the end
detector, correlating supposedly independent detector choices, and separately
normalizing hidden color histories.

`detector_probe.py`, `verification.json`, `verification_optimized.json`,
`replay.py` and `replay.json` are confined to this new directory. The xi/tick
source hash is preserved in the output. No parent artifact was changed.
