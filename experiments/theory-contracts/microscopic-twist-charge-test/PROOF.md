# A source-defined global carrier and a better charged-operator candidate

9 September 2026. NON-RH, unpromoted mathematical research. Written
derivations and reproducible finite controls, not a formal proof certificate,
independent mathematical review, a local charged-field reconstruction, or
T1–T8 closure.

## 1. Fixed source and exact question

Retain the original QWZ cylinder at transverse width W=8 and mass m=1.
Its one-body space has dimension 16N, with complete negative projector
P_r of rank 8N at background r=1,3. The original hopping, both edges and
all massive modes remain present. The rescaled many-body generator is

```
s_N=N/(2 pi),
H_r=dGamma(s_N h_r)-Tr(P_r s_N h_r).
```

Use the source-derived charge of
[source-edge-charge-transport](../source-edge-charge-transport/PROOF.md):
T is the identity on both spin components of the upper four rows,
A_r=Phi_(delta_N,h_r)(T), delta_N=4 N^(-3/4), and

```
C_r=dGamma(A_r)-Tr(P_1 T).
```

Phi is the original Gaussian time average. Its energy-basis multiplier is
exp[-(lambda_a-lambda_b)^2/(2 delta_N^2)]. The same reference constant is
used in both sectors. The prior derivation gives the full-sea difference
Tr[(P_3-P_1)T] -> 1/2 and vanishing filtered-charge fluctuations, including
their energy graph norm. These statements are for this fixed source.

The original microscopic candidate from
[gaussian-vacuum-filter](../gaussian-vacuum-filter/README.md) is

```
G_N(x)=exp(-i pi x/N),
F_a=Phi_(delta_N,h_1)(pi A_arc,a + R),   R(x)=pi x/N,
U_a=G_N exp(i F_a).
```

A_arc,a is the original top-two-row arc multiplication operator. The
executed point comparison retains the original half-circumference arc.
The code validates both predecessor checker hashes and their transitive
source checks. This note changes a candidate operator, not this Hamiltonian,
filter, charge, or microscopic Hilbert space.

## 2. The filled-sea Ward error has an exact finite formula

Let U be any finite one-body unitary, P a source sea, and a the proposed
charge increment. Let Gamma(U) denote its canonical exterior-power lift,
fixing the empty vacuum, including its complex determinants. Put

```
B=U* A_destination U-A_source.
```

Second quantization gives

```
Gamma(U)* (C_destination Gamma(U)-Gamma(U) C_source-a Gamma(U))
    =dGamma(B)-a.
```

The common charge subtraction cancels. The Slater mean and variance
identities therefore prove exactly

```
||(C_destination Gamma(U)-Gamma(U) C_source-a Gamma(U)) Omega_P||^2
 = (Tr(P B)-a)^2 + ||(1-P) B P||_HS^2.                 (1)
```

This is stronger than checking the expectation of the transported charge:
it retains source fluctuations and their interference. For the adjoint
test, reverse source and destination, replace U by U*, and use a=-1/2.
An independent four-mode full-Fock implementation checks (1), complex
phases, Gamma(VU)=Gamma(V)Gamma(U), and Gamma(U*)=Gamma(U)*.

For the original U_a, the forward squared errors at N=16,32,64 are
0.00710805, 0.00274998, 0.00119246. They decrease but do not prove a
limit. The bare ramp G performs almost identically on this charge test.
Identity and the undressed top string fail the same test. This suggests
separating the global sector transport from the endpoint-dependent part.

## 3. The existing ramp already knows the integer carry

Original momenta are p_(r,j)=2 pi(j-r/4)/N. Exactly,

```
G exp(i p_(r,j) x)=exp(i p_(r+2,j) x).
```

The first step r=1 to r=3 crosses no zero mode. The second step is r=3
to r=5, not the adjoint of the first. Although h_5=h_1 in the physical
coordinates, its Fourier label is j-1 in the r=1 convention:

```
j-5/4=(j-1)-1/4.
```

In the second step, only j=1 crosses p=0. Continue the actual occupied
top edge line across this crossing and keep the bottom edge line empty.
The target projector is then

```
Q_5^flow=P_5+|u_top,j=1><u_top,j=1|-|u_bottom,j=1><u_bottom,j=1|.  (2)
```

These are exact eigenlines selected by their overlap with the original
geometric edge quasimodes, not added states. In the r=1 labels, (2) adds
one top j=0 particle and removes one bottom j=0 particle. Resetting the
second target to P_5 would erase this integer carry. Total particle number
remains 8N throughout. Bare G twice already approaches this charge transfer
numerically; exact sea transport needs the next correction.

## 4. Canonical polar correction on the complete original sea

For source P, bare-ramp-translated source projection P'=G P G*, and desired
target Q, form

```
b=Q P'+(1-Q)(1-P'),
b* b=1-(P'-Q)^2,
R=b (b* b)^(-1/2),
W=R G.                                                       (3)
```

When ||P'-Q||<1, these expressions give W*W=1 and W P W*=Q. Equivalently,
W is the unitary polar part of Q G P+(1-Q)G(1-P). The intertwining follows
from bP'=Qb and the fact that b*b commutes with P'. In Fourier coordinates,
G identifies the labels, and the calculation uses only 16-by-16 matrices.
No filled mode is deleted by this blockwise computation.

For the first step use Q=P_3; for the second use the continued projector
(2). Thus Gamma(W_31) takes the complete first sea exactly to the complete
third sea, up to its canonical filled-sea determinant phase. The second
map takes this sea exactly to (2). The first output is a target ground
state, with target normal-ordered energy and H graph norm exactly zero.
The second output is an exact eigenstate with one particle and one hole.

### Existence for sufficiently large N, not just the executed samples

For fixed W=8,m=1, the negative projector is smooth on the punctured
momentum circle, with bounded one-sided derivative at zero. Near zero,
the geometrically marked edge lines continue smoothly through the
crossing, as established in the predecessor's source-specific strip
analysis. On the second crossing block, (2) uses that smooth continuation.
Every step has length pi/N. Compactness away from zero and the continued
local branch give a uniform constant K with

```
||P'-Q|| <= K/N
```

for the two specified steps. Consequently (3) exists for all sufficiently
large N. This argument does not give a numerically enclosed threshold K.
The finite replay separately checks N=16,32,64,128,256; its minimum Gram
eigenvalue ranges from 0.9903699 to 0.9999622. Complete-sea intertwining
errors are below 1e-12 in those floating-point controls.

### Fixed low modes and their energy graph

At each fixed physical Fourier label, rho=1-cos(p)=O(N^-2). The original
normalized geometric edge mode differs from its edge-row vector by
O(rho), and the exact eigenline differs from that quasimode by
O(rho^8/|sin p|). Therefore both endpoint eigenvectors differ from the
same edge-row vector by O(N^-2). Occupations agree along the continued
branch, so (P'-Q) on these vectors is also O(N^-2).

From b-1=(Q-P')(2P'-1) and the analytic inverse square root in (3),

```
||(R-1)u|| <= K' ||(P'-Q)u|| = O(N^-2).
```

After consistent eigenvector phase alignment, W maps a fixed edge mode
to its target edge mode with error O(N^-2). The rescaled one-body norm
is O(N), hence the target generator defect on that mode is O(N^-1).
The difference between its exact eigenvalue and the limiting chiral
eigenvalue also vanishes. Exterior powers extend this comparison to each
fixed finite particle/hole product over the transported sea. This is not
an estimate uniform in a growing number of modes or excitations.

The two-forward sea energy tends to 1/2: after relabeling the two
excitations each have rescaled energy tending to 1/4. Executed values
are 0.4991972 at N=16 and 0.4999969 at N=256. Inverses are the actual
unitary adjoints. Acting with the inverse second step on the identified
r=1 vacuum gives the opposite half charge and energy tending to 1/2.

For comparison, the bare ramp's particle/hole leakage tends downward in
the replay, but its rescaled energy variance rises from 23.86 at N=16 to
384.52 at N=256. Mere sea-vector proximity is not energy-graph control.
The polar correction removes that full-sea defect exactly on the first
transported vacuum. The observed variance trend is not itself an all-N
divergence proof.

### Phase and source-selection boundary

Canonical finite Gamma retains composition phases exactly. Comparing
filled-sea vectors and limiting intersector embeddings still requires a
consistent phase convention; the mode-alignment norm estimates above do
not derive an E8 cocycle or the marked Clock lift. A family of maps between
externally specified flux backgrounds is not yet one autonomous,
TFPT-selected intersector generator. Nor is W known to be localized.

## 5. A concrete improvement that leaves source-side neutral pairs intact

Replace only the common left factor:

```
U'_a=W_31 exp(i F_a).                                        (4)
```

Since the carrier is unitary and independent of a,

```
(U'_a)* U'_b=exp(-i F_a)exp(i F_b)=U_a* U_b.                  (5)
```

This is an exact finite operator identity, not a fitted correlation.
Canonical second quantization preserves it, including determinants and
phases. Products of these source-side alternating pairs, and their
expectations in the unchanged source sea, are also unchanged. This does
not assert that U'_a(U'_b)* equals U_a U_b* in an unchanged target state;
those target-side operators are conjugated by the changed carrier.

| N | Original forward Ward norm squared | New forward Ward norm squared | New adjoint Ward norm squared | New rescaled point energy |
|---|---:|---:|---:|---:|
| 16 | 7.10805e-3 | 6.92171e-6 | 1.64296e-5 | 0.328814 |
| 32 | 2.74998e-3 | 2.52437e-7 | 6.89510e-7 | 0.426605 |
| 64 | 1.19246e-3 | 2.36646e-10 | 6.00910e-10 | 0.550207 |

The independent full-matrix control of (5), using the half arc and the
empty-arc reference, has residual below 6e-13. The displayed Ward numbers
are **squared norms**, not norms or bounds on the whole Fock space. The
new point energy still increases over the three tested sizes. These
results do not establish bounded limiting energy, a normalization, or a
nonzero field limit.

## 6. The next proof is specific

Write E_a=exp(iF_a) and D=W_31* A_3 W_31-A_1. The new Ward operator has
the exact one-body decomposition

```
B'_a=E_a* D E_a + (E_a* A_1 E_a-A_1).                        (6)
```

Controlling D only on the vacuum is insufficient because E_a creates
excitations. The next acceptance gate is a uniform estimate for (6) on
the actual growing current window, in both directions, together with a
source-derived normalization and a nonzero spacetime-smeared field limit
in the relevant energy graph norm. The carrier's locality/exchange law
must be proved or a source-preserving localized replacement constructed.

Eight marked chiral channels, their E8/Clock phase dictionary, the physical
choice of flux dynamics, and a common 3+1D parent remain additional
obligations. Neither the exact global carrier nor improved finite point
data closes them.
