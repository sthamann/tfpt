# Global auxiliary reduction, including constant sources

This extends the finite second-class theorem in
`../local-positive-auxiliary/SECOND_CLASS.md`. It closes the **auxiliary**
constant-mode bookkeeping, not the missing homogeneous gravitational receiver.
The seed remains the chosen zero-mean TT-plus-scalar model. No gravitational
canonical pair, global lapse constraint or momentum receiver is derived here.

## 1. Precisely specified extension

Let the connected finite periodic lattice have n sites. Use real staggered
coordinates and their Euclidean inner products. The tensor space has dimension
6n; the link auxiliary E has dimension 18n. The operators of the preceding
proof obey DD^T = ell I_6, where ell is the nonnegative scalar lattice Laplacian.
Its kernel consists of spatial constants. Let J0 embed a normalized constant
six-vector and let t=(1,1,1,0,0,0)^T.

Choose the following orthonormal basis B5 of t-perpendicular in R^6:

    (1,-1,0,0,0,0)/sqrt(2), (1,1,-2,0,0,0)/sqrt(6),
    (0,0,0,1,0,0), (0,0,0,0,1,0), (0,0,0,0,0,1).

Replace the old N=[V^T,t] by

    Ntilde(v,chi,h) = V^T v + t chi + J0 B5 h,
    mean(v)=0, chi in R^n, h in R^5.                         (1)

The three constant v coordinates have identically zero columns. They are
**deleted redundant nondynamical coordinates**, not three physical modes
declared gauge. The five h coordinates are global auxiliary slack variables.
One may describe them as spatially constant fields, but a local constraint
implementation of that description has its own reducibility to handle.
Equation (1) is the explicit finite parameterization used here.

Ntilde has m=3(n-1)+n+5=4n+2 columns. It is injective: on each nonzero real
Fourier component the previous rank-four theorem applies, and on the constant
component N0=[t,B5] is invertible, with

    N0^T N0 = diag(3,1,1,1,1,1), det(N0)^2=3.              (2)

Its orthogonal complement is precisely the old **zero-mean TT space**, of
dimension 2(n-1). Denote its projector by P. Thus P0=0 and ell is strictly
positive on ran(P). Let ell^+ be the Moore--Penrose inverse, zero on constants.
All these subspaces are invariant under ell.

## 2. Invertibility and exact reduction on all modes

For y=(E,u,lambda), u=(v,chi,h), use the same saddle Hamiltonian as before:

    Hext = Hb + 1/2 y^T K y + y^T s,
    Hb = Hseed + g <q, tau>, s=(0,0,g tau),

            [ I_18n       0          -D^T ]
    K =     [   0        0        Ntilde^T ].              (3)
            [  -D     Ntilde          0  ]

K has dimension 28n+2. Its homogeneous null equations give
E=D^T lambda, Ntilde^T lambda=0 and ell lambda=Ntilde u. Projecting the
last equation by P gives ell lambda=0, since lambda lies in ran(P).
Strict positivity there yields lambda=0, followed by E=0 and u=0.
Thus K is invertible, including the constant component.

Eliminating its positive E block, and then splitting the tensor space into
ran(Ntilde) and ran(P), gives m positive/negative saddle pairs and 2(n-1)
negative TT eigenvalues, in addition to the 18n positive E directions.
Consequently its inertia is

    (positive, negative, zero) = (22n+2, 6n, 0).            (4)

The unique stationary values are

    lambda* = g ell^+ P tau, E* = g D^T ell^+ P tau,
    u* = -g (Ntilde^T Ntilde)^(-1) Ntilde^T tau.           (5)

For the last expression, Ntilde^T ell lambda*=0 by the invariant subspace
decomposition, not by commuting arbitrary operators. Substitution gives

    Hred = Hseed + g <q,tau> + g^2/2 <tau,P ell^+ tau>.    (6)

This is **exactly the previous positive reduced Hamiltonian**, with no new
constant-source energy term. It is not a new physical interaction.

## 3. Constant block and its meaning

At zero momentum D0=0. The auxiliary block is

    K0 = I_18 direct-sum [[0,N0^T],[N0,0]].                (7)

It has dimension 30, determinant 3, and inertia (24,6,0). Its solution is

    E0*=lambda0*=0,
    chi0* = -g t^T tau0/3, h* = -g B5^T tau0.             (8)

The contribution to (6) is zero for **every** tau0. Leaving out B5 would
leave five unconstrained multiplier directions. Retaining the three mean-v
coordinates would leave three zero coordinate directions. Neither singular
description is the invertible system (3).

Equation (8) absorbs a source into nondynamical slack. It neither stores its
energy in a homogeneous gravitational degree of freedom nor receives total
momentum. In particular it does not solve the homogeneous obstruction in
`../homogeneous-receiver/README.md`. Conflating these two types of zero mode
would incorrectly turn an algebraic elimination into a physical closure.

## 4. Complete Dirac algorithm

Apply the preceding general theorem with this larger constant K. There are
28n+2 primary constraints p_y=0 and as many secondary constraints Ky+s=0.
With F={s,s}, the Poisson matrix and its inverse are exactly

    C = [[0,-K],[K,F]],
    C^-1 = [[K^-1 F K^-1,K^-1],[-K^-1,0]].                (9)

No assumption that F vanishes is needed. All 56n+4 constraints are second
class; they remove exactly the 28n+2 introduced pairs. The seed Dirac bracket
is its original canonical bracket, the unique preservation multiplier is

    mu* = -K^-1 ({s,Hb}+F y*) = {y*,Hred},

and no tertiary constraint appears. The auxiliary Liouville factor integrates
to one since sqrt(det C)=|det K| cancels the delta(Ky+s) Jacobian. In particular
the constant block removes 30 pairs through 60 second-class constraints.

Quantization is still **after** this reduction. An invertible second-class
matrix is not an anomaly-free first-class quantum gauge algebra. The extension
does not establish causal locality of the reduced observable algebra, a
continuum limit, or a common TFPT parent.

## Regression coverage

`auxiliary_zero_mode.py` checks (2), (7), (8), the zero response and determinant,
the exact inverse Dirac block with nonzero source brackets, both singular
negative controls and the all-mode dimension/inertia identities. The proof
above, not a finite list of n values, establishes the general lattice claim.
