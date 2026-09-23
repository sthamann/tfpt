# A small discriminating test: a mean operator is not an event process

2026-09-12. NON-RH. This extends the existing covariant-edge comparison with
an exact operator-variance identity and a bounded refinement argument. It is
not a new discovery of ensemble averaging, nor a derived TFPT event law.

## Fixed inputs and provenance

The original finite candidate matrices are reconstructed using the source pin
`5e54c416be72a125a8ce6e235b4300f9f9c2344b3ada796d2dc4c7e2ea01482b`
and the previously deployed permutation. From the existing carrier edge E14
we form its six Clock conjugates K_j on the eight complex one-particle modes.
These are the same stipulated operations as in [COVARIANT_EDGE_CHANNEL.md](COVARIANT_EDGE_CHANNEL.md).
No new coupling is inserted into the source. Individual physical accessibility,
equal-probability event sampling, pulse angles and preparation remain additional
assumptions. The original source Hamiltonian is not being diagnosed as erroneous.

Let P be the accessible rank-five projector, Q=I-P, rho=Q/3 and

    Kbar = (1/6) sum_j K_j,   delta_j=K_j-Kbar.

Compare exactly two specified processes with the SAME first derivative:

    Psi_theta(rho)=exp(-i theta Kbar) rho exp(i theta Kbar),
    Phi_theta(rho)=(1/6) sum_j exp(-i theta K_j) rho exp(i theta K_j).

Equal first moments are not equality of the physical processes. Standard
ensemble-averaged dynamics treats precisely such distinctions:
[Kropf–Gneiting–Buchleitner](https://arxiv.org/abs/1511.08764).

## 1. The missing second moment

Taylor expansion, in finite dimension, gives

    Phi_theta(rho)-Psi_theta(rho)
       = -(theta^2/12) sum_j [delta_j,[delta_j,rho]] + O(theta^3).

The coefficient identity is verified as a full 64-by-64 superoperator equality,
not only on one selected state. The positive operator variance is

    V=(1/6) sum_j delta_j^2 = (1/6) sum_j K_j^2-Kbar^2,
    spectrum(V)={0,0,0,1/6,1/3,1/3,1/3,1/2}.

Positivity follows directly from Hermiticity: <x,Vx> is the average squared
norm of delta_j x. V alone does not specify the channel: the sandwich terms
delta_j rho delta_j matter as well. Even first and second moments together
do not generally determine a full process or its temporal correlations.

## 2. Three linked outputs from the same fixed construction

1. Kbar commutes with P, so the mean evolution leaves rho=Q/3 unchanged.
2. The event mixture instead gives

       Tr(P Phi_theta(Q/3)) = theta^2/6 + O(theta^4).

   Its known exact all-angle expression is
   (35-34 cos(theta)-cos(theta)^2)/108. Its second derivative agrees with
   the independently computed double-commutator coefficient.
3. Let h be the ORIGINAL source generator I+B_complex/8 and R_B the literal
   three-mode boundary projector. Following the pulse by original evolution,
   the coefficient of theta^2 tau^2 in

       Tr(R_B exp(-i tau h) Phi_theta(Q/3) exp(i tau h))

   is 7/384. This is a bivariate Taylor coefficient, not a claim that this
   expression is an exact probability at finite angles or times. The pulse
   acts only in carrier coordinates, so the literal boundary population and
   its first tau derivative vanish at tau=0. The quadratic coefficient is
   obtained from Tr(R_B h Phi_theta(rho) h).

All these quantities follow from the same matrices, weights and specified
state; they are not separately fitted. However the all-angle formula was
known beforehand and the new coefficient was computed during exploration:
this is a consistency/cross-output test, NOT a blind held-out prediction and
NOT a comparison with external experimental data.

## 3. Repetition does not automatically preserve the extra dynamics

Here every ||K_j||<=1 and ||Kbar||<=1. Write ad_K=[K, .]. The diamond norm
of ad_K is at most 2||K||, including ancillary systems. The exponential
Taylor remainder beyond first order is bounded by 2 theta^2 exp(2|theta|)
for each of the two channels above. Their first-order terms coincide, hence

    ||Phi_delta-Psi_delta||_diamond <= 4 delta^2 exp(2|delta|).

Quantum channels have diamond norm one, so telescoping products gives

    ||(Phi_(t/n))^n-Psi_t||_diamond
       <= 4 t^2 exp(2|t|/n)/n -> 0.

This is an analytic finite-dimensional bound, not a numerical extrapolation.
It applies to INDEPENDENT resampling after each short step at fixed total t.
For the chosen hidden witness, the final accessible signal therefore tends
to zero in this limit. The original finite-angle signal is not a proof of
a nonzero continuous-time dissipative term under this scaling.

Choosing j once and retaining it over all steps is a DIFFERENT process:
the average remains Phi_t, not (Phi_(t/n))^n. Thus temporal memory of the
event label can change the limit without changing the one-step ensemble.
Alternatively, centered signed fluctuations of size sqrt(delta) can yield
a diffusion term, but their signs, scaling and rate are EXTRA stochastic
inputs, not consequences of the compiler matrices. We do not install them.

## 4. What may be missing, stated without overclaim

The narrowly supported simplification is: distinguish an operation, a
distribution of operations, and an ordered/history-dependent process of
operations. A mean matrix, a spectrum and a count can be compatible with
different observable histories. They are incomplete views of a process.

This does not establish that TFPT has accidentally averaged away its true
physics. The earlier work already recognized the mean/channel distinction.
The present extension locates its second moment and shows exactly why a
naive infinitesimal iteration can erase the additional effect again.

The decisive source audit is now: Does the compiler define only a sum of
couplings, or separately realized events? If events, what specifies their
joint history, duration and state preparation? Derive that rule before
promoting the event model to a physical origin. A simple law would be valuable;
its simplicity is not evidence of its truth or uniqueness.

## Verification

`process_moment_audit.py` passed 21 exact checks in normal and -OO modes with
byte-identical JSON outputs. It replays the pinned source split, compares the
full second-order superoperators, and checks variance spectrum and both
response coefficients. The general norm bound above is a written proof, not
a separately executed continuum simulation. No TOE/RH/factoring/P-versus-NP
result is claimed; no paper, website, iCloud export or status ledger promoted.
