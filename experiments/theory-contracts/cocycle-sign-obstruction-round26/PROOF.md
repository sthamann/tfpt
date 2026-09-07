# Round26: actual negative charge loop and the precise gauge obstruction

2026-09-07. NON-RH. This uses the original E8 lattice/cocycle and ALL
hopping terms. It is not a no-go theorem for every representation,
grouping of histories, auxiliary-field method or simulation algorithm.

## 1. A negative closed loop in the actual neutral carrier

On three distinct adjacent sites x,y,z choose p=e2 and r=e3, with
p^T G r=1. Let A=W_xy,p and B=W_yz,r. Round20's exact full-cocycle
identity gives AB=-BA. Applying the chronological word

    A, B, A*, B*

therefore returns EVERY initial charge profile with multiplier -1.
For the all-zero initial profile the four successive steps have phases
(-1,+1,-1,-1), hence product -1. The intermediate total diagonal site
energies sum e(n_x) are (2,3,2,0). Every state has total charge zero.

The word exists on an actual L3 torus (N=27) with the other 24 sites
unchanged. None of the intermediate states is wrapped or removed. Its
four successive charge transitions are distinct genuine matrix elements
of H_hop; for L>=3 each receives -J times its cocycle sign. Other
channels and charge-diagonal terms cannot cancel those matrix elements.

## 2. Rephasing cannot turn this Hamiltonian stoquastic in that basis

For any diagonal unitary F|n>=f(n)|n>, |f(n)|=1, each transition gains
f(n_next)/f(n_current) (or the conjugate convention). Around a closed
loop these factors telescope to one, so the loop multiplier stays -1.
Four nonpositive real off-diagonal Hamiltonian entries would have
nonnegative product, whereas these four have product -J^4 for J>0.
Thus no diagonal rephasing of the FULL configuration basis can make
all off-diagonal entries nonpositive in the neutral sector.

This is stronger than failure of an on-site rephasing, but it is only a
diagonal-basis-change statement. It does not exclude non-diagonal changes,
enlarged descriptions with a proved equivalence, or regrouping negative
words into positive blocks. In particular non-stoquasticity alone must
not be equated with an intrinsic sign problem in every representation.

## 3. The sign survives scalar integration in the actual word expansion

At T=4 time slices choose precisely one of the displayed hops in each
factor exp(delta J A_sign), and start/end in the zero charge state.
For nu=0 and beta=4delta the term in the full scalar-integrated expansion is

    -exp(-beta kappa) (delta J)^4 exp(-7delta/N) Z_phi[n],
    kappa=48NJ, Z_phi[n]>0.                         (1)

All scalar coordinates are kept when establishing this positivity.
For u>=0,m>0, the full 4N-coordinate matrix
delta^-1 L_time tensor I+delta blockdiag[-Delta_a+m^2+2u e(n(j))]
is strictly positive. The checker builds the original N=27, T=4 matrix
with 108 scalar coordinates and verifies its physical diagonal dominance
and nonnegative added potential. Gaussian integration cannot reverse or
erase this individual word's negative multiplier.

The four-hop term is a SUBCONTRIBUTION, not an invariant finite Hamiltonian
or the complete partition function. Resummed transfer entries can combine
many words; this test does not claim their signs for every delta. Nor does
one negative term quantify the actual average sign in a large system.

The [summed-history contract](../history-sum-control-round26/PROOF.md)
retains these phases and proves a finite cancellation/error budget rather
than deleting them. Its bounds may be computationally very expensive.

For primary-source context on basis-dependent cycle criteria and the
distinction from universal simulation impossibility, see
[Hen](https://arxiv.org/abs/2012.02022). The particular E8 loop, sign,
energies and scalar normalization here are derived from the repository's
actual hopping operator; no broad no-go theorem is imported from that paper.
No T1-T8/TOE/RH or empirical promotion.
