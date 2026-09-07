# Complete canonical shear of the actual reduced positive Hamiltonian

Date: 2026-09-06. Finite-volume theorem and explicit source witness.
Integrated as an unpromoted research contract. No continuum, local-parent, scattering,
TFPT-origin, or complete-TOE theorem is asserted.

## 1. The model being transformed

Use the actual free scalar and the chosen positive reduced completion in
`experiments/theory-contracts/constraint-dressing/README.md`, section 10,
and its strengthened domain theorem in
`experiments/theory-contracts/local-positive-auxiliary/QUANTUM_DOMAIN.md`.
There are n scalar coordinates phi and M=2(n-1) real orthonormal TT pairs
(Q,P). Homogeneous gravity is excluded, so every TT eigenvalue ell_alpha
is positive. The scalar uniform coordinate is not silently removed.

The actual Ward stress has the same scalar kinetic/mass term on each
diagonal component. TT smearing cancels it exactly. Thus

    T_alpha(phi) = <w_alpha, sigma(D phi)>

is a real homogeneous quadratic polynomial in scalar coordinates only,
not a momentum-dependent quadratic operator. Write

    L = diag(ell_alpha),       F = L^-1 T,
    V_m(phi) = (||D phi||^2 + m^2 ||phi||^2)/2,
    H_0 = (||pi||^2 + ||P||^2)/2 + V_m + Q^T L Q/2,
    H_+ = (||pi||^2 + ||P||^2)/2 + V_m
          + (Q+gF)^T L (Q+gF)/2.                         (1)

In particular its prescribed first vertex is W_+=Q dot T. Its quartic
completion is g^2 R with R=T^T L^-1 T/2. This note does not replace (1)
with a different stress or an arbitrary one-mode toy Hamiltonian.

An additional useful exact property is

    Delta_phi F_alpha = 0.                                (2)

Indeed the configuration Laplacian of a translation-covariant quadratic
local stress is a configuration-independent tensor, constant over the
periodic spatial lattice. Its projection onto every nonzero Fourier mode
vanishes. All TT modes used here are nonzero modes. This argument does
not confuse the spatial Laplacian with Delta_phi. The checker also tests
(2) directly for two nonzero actual normalized TT polynomials.

## 2. Classical transformation: the momentum shift cannot be dropped

Let J(phi)=DF(phi), an M by n matrix, and define

    q = Q+gF(phi),   p=P,   varphi=phi,
    rho = pi-g J(phi)^T P.                                (3)

This is a globally invertible canonical transformation. The inverse is
Q=q-gF, P=p, phi=varphi, pi=rho+gJ^T p. A direct proof is the equality
of canonical one-forms

    pi dot dphi + P dot dQ = rho dot dphi + p dot dq.

Equivalently its canonical Poisson brackets are standard, including
{rho_x,rho_y}=0 by symmetry of the second derivatives of F.
Writing A_x(phi,p)=sum_alpha (partial_x F_alpha) p_alpha, the ACTUAL
Hamiltonian in the new coordinates is

    H_tilde,+ = H_0(phi,q,rho,p)
                + g sum_x rho_x A_x + g^2 sum_x A_x^2/2.   (4)

Thus the oscillator potential is unshifted, but the mixed kinetic terms
remain. The cotangent lift of a nonlinear shear transforms the Euclidean
kinetic metric; deleting the induced metric terms is a Hamiltonian change.
Formula (4) proves neither a failure nor a success of every conceivable
local parent: it only evaluates this explicit proposed transformation.

## 3. Exact quantum unitary and its domains

Work in H=L2(R^(n+M),dphi dQ), hbar=1. Define the fixed-coupling map

    (U_g psi)(phi,q) = psi(phi,q-gF(phi)).                  (5)

The configuration shear is a global polynomial diffeomorphism with
polynomial inverse and determinant one. Fubini and a translation in q at
each phi prove ||U_g psi||=||psi||, and U_-g is its inverse. It is therefore
an everywhere-defined unitary, not merely a formal exponential.
It is strongly continuous in g by its action on compactly supported
continuous functions and density. The general Jacobian-weighted unitary
pullback convention appears in Duca--Joly--Turaev, section 2.1,
[equations (2.1)--(2.2)](https://arxiv.org/pdf/2203.00486); its Jacobian
weight is exactly one here. Their moving-domain evolution theorem is not
being imported for this unbounded polynomial shear.

For completeness an exact generator is available. After Fourier transform
only in Q, B=F(phi) dot P is multiplication by the real function F(phi) dot p.
It has the maximal self-adjoint multiplication domain

    Dom B = {psi: (F(phi) dot p) psi_hat(phi,p) is in L2}.

Consequently U_g=exp(-ig B). This construction avoids any unsupported
functional calculus for noncommuting F components: they are multiplication
operators in this actual model.

Both U_g and its inverse preserve Cc_infinity and Schwartz space. For the
latter, the chain rule supplies polynomial derivative factors, and both
the shear and its inverse have polynomial growth. These bounds transfer
every weighted Schwartz seminorm to finitely many such seminorms. This
statement concerns the shear, not invariance under the time evolution.

On these invariant test spaces the chain rule gives

    U_g Q U_g^-1 = q-gF,          U_g P U_g^-1 = p,
    U_g phi U_g^-1 = phi,        U_g pi_x U_g^-1 = rho_x+gA_x.  (6)

Here rho=-i partial_phi and p=-i partial_q in the new representation.
The exact operator formula is therefore

    H_tilde,+ = U_g H_+ U_g^-1
       = H_0 + (g/2) sum_x (rho_x A_x + A_x rho_x)
              + (g^2/2) sum_x A_x^2.                     (7)

If expanded with momenta to the right, the linear term includes
-ig(Delta_phi F) dot p/2. It vanishes after summation in this particular
model by (2). The anticommutator/square formula (7) is preferable: it
remains exact without relying on that simplification. No scalar ordering
constant or Jacobian-induced potential has been omitted.

The previously proved nonnegative self-adjoint H_+ has Cc_infinity and
Schwartz operator cores. Its transform is rigorously defined by

    Dom H_tilde,+ = U_g Dom H_+,
    Dom q_tilde,+ = U_g Dom q_+,
    q_tilde,+[psi] = q_+[U_g^-1 psi].                    (8)

Equivalently its nonnegative form is the sum of the squared norms of
(rho_x+gA_x)psi, p_alpha psi, sqrt(2V_m)psi and
sqrt(ell_alpha) q_alpha psi, each with coefficient 1/2. The domain is the
intersection of their maximal graph domains. The differential expressions
are understood weakly there. The covariant momentum is the self-adjoint
conjugate of pi_x, with domain U_g Dom pi_x. On the test core it equals
the displayed polynomial differential expression.

The sum form is closed and densely defined; equivalently closedness is
already immediate from (8). Its unique representing operator is precisely
the conjugate operator, by the uniqueness of the closed-form representation
([Sebestyen--Tarcsay, Corollary 2.7](https://arxiv.org/html/2505.09588v1)).
Both test spaces remain operator cores because U_g preserves them.
There is no assertion of a coupling-independent full operator domain,
that Dom H_tilde,+ equals Dom H_0, or that exp(-itH_+) preserves Schwartz.

## 4. Bounded local scalar operations: the complete formula

Fix the original scalar net

    A_sc(Lambda) = B(L2(R^Lambda)) tensor I

inside the scalar tensor-product Hilbert space, also acting as the identity
on all TT variables. It can equivalently be generated as a von Neumann
algebra by the scalar Weyl operators supported in Lambda. For real f,h
with that support, use

    W(f,h)=exp(i(f dot phi+h dot pi)),
    (W(f,h)psi)(phi,Q)=exp(i f dot (phi+h/2)) psi(phi+h,Q).

Direct composition with (5), without a truncated BCH series, yields

    (U_g W(f,h) U_g^-1 psi)(phi,q)
       = exp(i f dot (phi+h/2))
         psi(phi+h, q+g[F(phi+h)-F(phi)]).                (9)

The phase-only operators h=0 stay unchanged. A scalar translation h!=0
acquires a field-dependent TT translation. Since F is quadratic its shift
is exactly DF(phi)h+D2F[h,h]/2, not merely its linearization. These bounded
unitaries are defined on all of H; no momentum-domain assumption is needed.

The transported physical net is A_tilde_sc(Lambda)=U_g A_sc(Lambda) U_g^-1.
Its disjoint algebras still commute, by unitarity. This fact by itself is
not a dynamical locality theorem. For every bounded A,B and every t,

    [exp(it H_tilde,+)(U_g A U_g^-1)exp(-it H_tilde,+), U_g B U_g^-1]
       = U_g [exp(itH_+) A exp(-itH_+), B] U_g^-1.        (10)

Thus the previously verified nonzero first-order remote response in this
net is preserved exactly, in norm and in transported state matrix elements.
There is no new infinite-volume assumption in this equality.

Declaring the naive new scalar algebra generated by phi,rho to be physical
instead is a different operational identification. Pulled back to the old
representation, exp(i h dot rho) shifts

    (phi,Q) -> (phi+h, Q-g[F(phi+h)-F(phi)]),              (11)

and its generator is h dot (pi-g DF^T P). These are not the original
scalar-factor operations. Inverse spatial ell and TT projection also enter
F. Even before resolving every spatial-support question for reduced TT
variables, (9) and the explicit nonzero TT shift witness already disprove
identification with the original scalar-only site operation.

This is a concrete description of the available changed observable net,
not a theorem that every alternative physical net or every local parent
is impossible. Relational preparations or extra gauge-invariant fields
require their own explicit observable map and complete response calculation.

## 5. The genuinely isospectral free completion is a different model

One CAN construct the exact self-adjoint Hamiltonian

    H_iso = U_g^-1 H_0 U_g,
    Dom H_iso = U_g^-1 Dom H_0.                          (12)

It is positive and exactly isospectral to H_0, with multiplicities and
spectral type preserved. Its complete old-coordinate expression is

    H_iso = ||pi-g DF^T P||^2/2 + ||P||^2/2 + V_m
             + (Q+gF)^T L (Q+gF)/2,

    H_iso-H_+ = -(g/2) sum_x (pi_x A_x+A_x pi_x)
                  +(g^2/2) sum_x A_x^2.                 (13)

Products in (13) have the displayed operator ordering. The classical
version is the same formula with ordinary products. Its first vertex is

    W_iso = Q dot T - pi dot (DF)^T P,                   (14)

so it fails the original first-stress-vertex matching. The mixed term is
cubic since DF is linear, and cannot be declared merely a higher-order
completion ambiguity. The second kinetic term is an additional quartic.

### Actual nonzero source witness, not a toy oscillator

On the 3^3 cubic lattice at a=1 take k=(0,0,2*pi/3) and the real normalized
TT mode

    w_xx(x,y,z)=cos(2*pi*z/3)/(3 sqrt(3)),
    w_yy=-w_xx, all other components zero, ell=3.

Trace and divergence vanish; its tensor norm is one. Its diagonal source
has no hidden staggered phase since kx=ky=0. Evaluate the ORIGINAL Ward
stress at

    phi_0(x,y,z)=(1,-1,0)[x]*(1,2,-1)[z].

The exact result is T_1(phi_0)=-3 sqrt(3)/4. In the full model choose
Q=0, P_1=1 and all other TT momenta zero, and pi=phi_0. Homogeneity gives

    pi dot DF_1(phi_0)=2 F_1(phi_0)=-sqrt(3)/2,
    W_+=0,       W_iso=sqrt(3)/2 != 0.                  (15)

No other oscillator was removed: its momentum and coordinate are simply
zero at this full phase-space point. This proves a nonzero coefficient of
the actual mixed differential operator, so an ordering convention cannot
make the two first vertices identical. The checker additionally computes
the positive coefficient ||DF_1(phi_0)||^2/2: with pi=0 the classical
difference is this coefficient times g^2, nonzero for every g!=0.
In fact that coefficient is exactly 1/16. Thus at the second full-model
point pi=0, P_1=1, Q=0, phi=phi_0, the difference is g^2/16.

For comparison the already audited full-TT Round-11 configuration also
works: set P=T(phi_0), pi=phi_0 and Q=0 on 3x3x6. Then the added first
vertex is -4R(phi_0)=-115645/6174. The new cubic witness (15) does not depend
on importing that earlier inverse-projector calculation.

## 6. What is free, and what has NOT been shown about scattering

The pair (H_iso, U_g^-1 A_0(Lambda) U_g), with correspondingly transported
states, is exactly the free theory in changed coordinates. In particular,
for the free scalar local net A_0, every dynamics/correlation statement is
transported from H_0; the independent free TT factor does not create a new
scalar interaction. Nonlinear expressions in the original variables can
have complicated correlations, which is not evidence of new dynamics.

This does not construct scattering for the original H_+. In finite massive
volume the operators have discrete spectra, so an ordinary spatial
many-particle scattering theory is not furnished here. In any meaningful
two-Hilbert-space comparison with identification I_g=U_g^-1 one has exactly

    exp(it H_iso) I_g exp(-it H_0)=I_g for every t.

Thus the transported comparison has identity scattering wherever that
notion applies (after restriction to the relevant continuous subspaces).
One must NOT infer existence or identity of ordinary wave operators with
the identity identification instead: U_g need not be asymptotically trivial,
and no infinite-volume implementation or asymptotic completeness was proved.

The constructive conclusion is therefore precise: the actual H_+ admits
an exact canonical/unitary shear and an explicit transported net, but its
kinetic interaction survives. A completely free conjugate can be built,
yet it changes the already specified first vertex and, under its free
physical identification, adds no genuine interacting dynamics. Neither
operation repairs locality of the original Hamiltonian on the same net
by relabeling, and neither is a blanket no-go for other constructions.
The unequal expressions establish failure of this proposed free conjugacy,
not the absence of every other possible unitary or canonical equivalence.

## 7. Verification

`shear_check.py` independently imports the original Ward source frontend
read-only and constructs two actual normalized nonzero TT polynomials.
It checks degree, uniform-shift invariance, configuration harmonicity,
the nonzero full-model first-vertex witness and a nonzero finite scalar
operation's TT shift. Separate generic polynomial tests verify all 48
canonical bracket identities, the exact quantum chain rule, both complete
Hamiltonian conjugations, anticommutator ordering and finite Weyl pullback.
The generic two-field/two-oscillator identity tests are not advertised as a
TT-mode truncation of the actual model. All arithmetic is exact SymPy.
Operator domains and physical-net conclusions are proved above, not inferred
from finite CCR matrices or a numerical spectrum.
