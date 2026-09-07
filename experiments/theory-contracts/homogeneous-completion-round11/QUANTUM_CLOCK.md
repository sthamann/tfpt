# Conditional quantum trace clock: physical inner product and its limits

This closes an explicitly stated gap in the **one-constraint conditional
model** of `../homogeneous-receiver/README.md`: it constructs the physical
Hilbert space and norm by group averaging, rather than only applying a square
root to a presumed rest Hamiltonian. It does not derive that constraint from
TFPT or make the remaining constraints commute with it.

## 1. Assumptions and the actual finite scalar model

Let A be a self-adjoint operator on a separable Hilbert space H with
A >= epsilon I for some epsilon>0. Postulate, on L^2(R_Q) tensor H,

    P=-i partial_Q, C=A-P^2/12, omega=(12A)^(1/2).          (1)

A and P strongly commute because they act on different factors. C is the
self-adjoint joint spectral multiplication operator with domain
integral |E-p^2/12|^2 ||f(E,p)||^2 dmu(E) dp < infinity. Its domain need not
equal D(A) intersection D(P^2); cancellation in this joint multiplier is
allowed. The negative-momentum sheet P<0 is an additional orientation choice.

For the **unsubtracted, chosen finite** scalar/TT Hamiltonian of
`../local-positive-auxiliary/QUANTUM_DOMAIN.md`, the positive lower bound follows:

* If m>0, the nonnegative potential is proper and A has compact resolvent.
  Its lowest eigenvalue exists. Were it zero, its quadratic form would force
  every configuration derivative of its eigenfunction to vanish. A constant
  function on the noncompact configuration space is not a nonzero L^2 vector.
  Thus E0>0.
* If m=0 and n>1, the uniform scalar coordinate factors as a free particle.
  The remaining confining operator Aperp has the same strict-positive-ground
  argument. Hence A=P_uniform^2/2 + Aperp >= Eperp>0, even though the full
  operator has no normalizable ground state.
* The degenerate n=1,m=0 pure-free case has threshold zero and is excluded
  from this strict-gap corollary.

These are fixed-volume statements. They provide neither a volume-uniform
epsilon nor a TFPT selection of the potential, energy zero or global lapse.

## 2. A convergent test space and the averaging formula

Use the direct-integral representation H=integral H_E dmu(E), including any
discrete spectrum and multiplicities. Take finite sums of sections smooth
and compactly supported in p<0, supported away from p=0, with compact A-spectral
support and bounded L^2_H norms of all p derivatives. This is a dense invariant
test space in the negative-momentum kinematical sector. Tensor-product smooth
clock tests and compact-spectral H vectors already give such a dense space.

Define the sesquilinear form using inner products conjugate-linear in the
first entry and Haar normalization ds/(2pi):

    eta_-(f,h) = integral_R ds/(2pi) <f, exp(isC) h>.       (2)

It is an actual convergent matrix-element integral on this test space. Twice
integrating by parts in p in exp(-is p^2/12), using p bounded away from zero,
gives an O(|s|^-2) bound uniform in the compact energy support. Cauchy--Schwarz
controls the H-valued amplitudes and their derivatives; exp(isA) is unitary.
The bounded s interval is harmless. Equivalently one may first insert a
Gaussian regulator exp(-delta s^2) and pass to the limit by dominated
convergence. The latter calculation evaluates the familiar delta distribution
without assuming absolute convergence of its pointwise energy integrand.

At fixed E>0 the roots are simple. Since |partial_p C|=|p|/6,

    delta(E-p^2/12) = (6/omega(E))
                     [delta(p-omega(E))+delta(p+omega(E))]. (3)

Only the negative root is in the chosen test sector. Therefore

    eta_-(f,h) = integral (6/omega(E))
       <f(E,-omega(E)),h(E,-omega(E))>_E dmu(E).           (4)

The values in (4) are defined by the smooth p representative; trace evaluation
is controlled on each compact energy interval. Equation (4) proves positivity
for this model, rather than assuming a general group-averaging positivity
theorem.

## 3. The physical completion and intrinsic-time evolution

The null quotient of (4) has the isometry

    J_- f(E) = sqrt(6/omega(E)) f(E,-omega(E)).             (5)

Its range is dense in H. To obtain any compact-spectral vector v, choose a
smooth negative-p bump equal to one on its compact mass-shell interval and
multiply v by sqrt(omega/6). These are allowed test functions and map to v.
Thus the completed physical Hilbert space is unitarily isomorphic to H.

These are generalized solutions: the kinematical L^2 kernel of C is zero.
Indeed for every E the allowed p set has Lebesgue measure zero, so Fubini
excludes a nonzero joint L^2 vector supported there. Confusing that kernel
with the physical space would erase all states.

The physical time generator is the positive self-adjoint omega with domain
D(A^(1/2)); exp(-i omega Q) is a unitary group on H. Use the following
Klein--Gordon-normalized realization of a compact-spectral physical vector v:

    Psi_v(Q) = sqrt(6) omega^(-1/2) exp(-i omega Q) v.      (6)

With the unitary Fourier convention, (6) is sqrt(2pi) times the inverse Fourier
transform of delta(C)f when v=J_-f. This rescales the solution realization,
not the previously fixed kinematical Fourier transform or Haar measure.

It obeys (partial_Q^2+12A)Psi=0 and i partial_Q Psi=omega Psi, equivalently
P Psi=-omega Psi. Its conserved Klein--Gordon pairing is

    (i/12) [<Psi_v,partial_Q Psi_w>
            - <partial_Q Psi_v,Psi_w>] = <v,w>.           (7)

First prove (7) on compact energy support, where all derivatives exist, then
extend the norm by completion. It is not an assertion that every physical
vector lies in every derivative domain. The gap ensures omega^(-1/2) is
bounded, but omega itself is generally unbounded.

If both momentum sheets are retained, group averaging instead yields the
**positive direct sum H plus H**. The unmodified Klein--Gordon current has
opposite signs on the two sheets and is not that positive direct-sum norm.
There is no spontaneous selection of the chosen time orientation in (1).

## 4. Why this does not solve the vacuum or joint-constraint problem

The energy reference in (1) is physical input, not a harmless convention once
energy sources a constraint. For A=Omega(N+1/2), Omega>0, the unsubtracted
operator has the required positive gap. Replacing it by A-Omega/2 introduces
a zero eigenvalue. On that eigenspace the mass-shell equation has the double
root p=0, the simple-root weight 6/omega diverges and the test-space construction
above omits that sector. Formula (4) must not be extended there by assertion.
The spectral square root nevertheless remains self-adjoint; the failure is
this claimed equivalence/normalization at the degenerate shell, not spectral
calculus. The classical vacuum irregularity of the earlier proof is unchanged.

In addition, simultaneous physical constraints J_i require their own domain
and preservation theorem, e.g. strong commutation with A for this abelian
construction. The old centered-difference free scalar momentum does not
automatically have that property after the chosen positive interaction is
added. Round11's actual-source test in `../reduced-locality-round11/` finds a
nonzero bracket. Therefore the present result is **one conditional clock**,
not a joint solution of homogeneous energy and momentum constraints, much less
the local gravitational constraint algebra.

## 5. A constructive finite-translation alternative, not the old momentum constraint

There is a distinct, consistent finite-regulator alternative. Let Gamma be the
finite periodic lattice-translation group. It acts by permutations on scalar
coordinates and by real orthogonal transformations on the retained TT space;
the same transformations act on conjugate momenta. Constant and nonconstant
Fourier subspaces are translation invariant, as is the TT kernel of the
translation-covariant divergence and trace maps. No translation-invariant
choice of an individual TT basis vector is required.

Every fixed local stress formula is translation covariant. The operators ell,
ell^+ and P commute with translations. Therefore the complete potential

    Vg = Vm + 1/2 <q,ell q> + g <q,tau>
                    + g^2/2 <tau,P ell^+ tau>

is invariant under the **simultaneous** scalar and tensor translations. The
configuration kinetic Laplacian is orthogonally invariant as well. Pullback
gives a unitary representation U_a of Gamma preserving C_c^infinity and the
quadratic form. Uniqueness of the previously proved self-adjoint closure then
implies U_a A U_a^*=A, including equality of operator domains and spectral
projections. This is exact discrete symmetry, not the false identification of
centered differences with its infinitesimal generator.

The finite group average

    Pi_inv = (1/|Gamma|) sum_(a in Gamma) U_a              (8)

is an orthogonal projector which commutes strongly with A. Its range H_inv is
nonzero: a Gaussian depending only on the squared norm of all configuration
coordinates is invariant and normalizable. A_inv=A restricted to H_inv is
self-adjoint and retains the lower bound epsilon. The construction (2)-(7)
can therefore be applied verbatim with H_inv,A_inv in place of H,A.

Equivalently one can average over R times Gamma. For arbitrary clock test
vectors in the negative-momentum sector the joint form is

    eta_joint(f,h) = eta_-(f,Pi_inv h)
                  = <Pi_inv J_- f, Pi_inv J_- h>.         (9)

The finite sum and convergent time integral commute. Its completed null
quotient is exactly H_inv, and the positive intrinsic-time evolution leaves
it invariant. Thus a **zero discrete-quasimomentum sector plus the postulated
clock** is an honest joint conditional finite model. For m>0 its unique
strictly positive ground state is translation invariant; this follows from
uniqueness and positivity, not from assigning a momentum label by hand.

This is a different constraint prescription. Finite translations have no
specified Lie-algebra momentum generator; invariance under all U_a does not
imply annihilation by the old centered-difference J_i. A logarithm of U_a
would not establish that missing identity or a local Noether current. Treating
the global finite symmetry as a constraint is also an additional choice.
No homogeneous gravitational momentum has been received, and no continuum
momentum/diffeomorphism constraint follows. Equation (9) is a usable conditional
alternative, not a repair of the original J_i assertion.

## Context and reproducibility

The method is refined algebraic quantization / group averaging. Primary
context: [Marolf, Group Averaging and Refined Algebraic Quantization](https://arxiv.org/html/gr-qc/0011112)
and [Marolf, Systems with a single constraint](https://arxiv.org/abs/gr-qc/9508015).
The convergence, positive form and normalizations needed here are proved above
for (1); they are not imported as universal claims from those references.

`quantum_clock.py` checks the exact shell Jacobian, isometry, current signs,
constraint equation and energy-shift failure on finite spectral samples, plus
finite translation-projector identities in a regular representation. These
algebraic regressions do not by themselves prove the infinite-dimensional
functional-analytic statements.
