# Vertex-preserving quantum completion by a quadratic constraint-ideal form

2026-09-06. NON-RH Round15. This constructs an all-time, strongly
constraint-covariant quantum realization while retaining the original first
interaction vertex. It changes second and higher orders away from the
constraint surface. It is not a realization of the unchanged old H_sr,
a microscopic derivation, or a theorem of full T1–T8 closure.

## 1. Exact input and what is changed

Fix the finite periodic scalar/TT model, L>=2, m>=0, and g in R. Retain all
scalar coordinates and all nonzero TT modes. The previous free Darboux
chart deletes homogeneous gravity. On H_p let A_+(g) be the already proved
unique nonnegative physical Hamiltonian. It has C_c^infinity and Schwartz
operator cores. Write c=(r,v), A_c=[[0,b],[0,0]], and

    K_c=-i(bv).partial_r+k(c),
    k(c)=r.B_H.r/2+v.B_v.v/2,
    H_sr=K_c+A_+(g)+g sum_a c_a Q_a.                         (1)

The ACTUAL matter source vector is Q=(Bcal,-B_v J_v), including every
retained mode. Each Q_a is the self-adjoint closure of a real homogeneous
Weyl quadratic on the matter factor; these closures exist by the quadratic
metaplectic theorem used in earlier rounds. They need not commute.

Choose the previously fixed real Euclidean constraint coordinates and
declare the additional QUANTUM form

    g^2 |c|^2 sum_a ||Q_a psi||^2.                            (2)

Its coefficient and Euclidean metric are new inputs, not canonical under
arbitrary rescaling of the constraint coordinates. A physical unit
convention is fixed here, as in the input lattice model.
At the expression level (2) is g^2|c|^2 sum Q_a^2, with operator-square
ordering. Its Weyl symbol includes the corresponding ordering constants;
it must not be confused with quantizing only the classical squares.
It is quadratic in the first-class constraint ideal and zero at c=0.
There is NO order-g change to (1). The entire free Hamiltonian and the
chosen reduced A_+ are unchanged.

## 2. Closed positive forms, without commuting-source assumptions

For fixed g!=0 and c!=0 use the common dense domain

    D=Dom(A_+^(1/2)) intersection (intersection_a Dom Q_a).

It is complete in the sum of the closed graph/form norms and contains
C_c^infinity. Define the Hermitian form (inner product anti-linear first)

    h_c[psi]=q_+[psi]+g sum_a c_a <psi,Q_a psi>
                      +g^2|c|^2 sum_a ||Q_a psi||^2.        (3)

Put w=|g||c|, S[psi]=sum_a||Q_a psi||^2. Cauchy--Schwarz gives

    |g sum_a c_a <psi,Q_a psi>| <= w sqrt(S[psi]) ||psi||.

Consequently, on D,

    q_+ +(w^2/2)S +(1/2)||psi||^2 <= h_c+||psi||^2
       <= q_+ +(3w^2/2)S +(3/2)||psi||^2.                  (4)

The positive reference norm on either side is complete. The linear term
has relative form bound at most 1/2 against q_++w^2 S. Thus h_c is closed,
bounded below by -1/2, and has one specified self-adjoint representing
operator h(c). No self-adjointness of a formal noncommuting sum Q_a^2 is
assumed. On physical Schwartz tests the representing operator acts as
A_++g sum c_a Q_a+g^2|c|^2 sum Q_a^2, because each polynomial expression
maps Schwartz to itself and integration by parts identifies the form.
For c=0 define h(0)=A_+ on its original domain. For g=0 use A_+(0) for
every c. These definitions do not incorrectly keep the larger graph
requirements of D at the zero coefficient.

## 3. Every characteristic has a controlled all-time propagator

Let c(t)=exp(t A_c)c0. If c0!=0 it never becomes zero. On any compact
time interval |c(t)| has a positive minimum, so (3) has the same D
throughout that interval. Its coefficients are polynomials in t and the
forms are C^infinity as bounded maps D to D*. Equation (4) gives uniform
equivalence of their positive form norms on the interval.

The common-form propagator theorem applies to h(c(t))+1. Precisely, use
Assumption 3.8 and Theorem 3.10 in
[Balmaseda--Lonigro--Perez-Pardo](https://arxiv.org/html/2112.11063v2).
The required dense complete common space and smooth positive inner
products have just been verified. Removing the constant phase gives a
unique unitary propagator V_c0(t,s) for h(c(t)), preserving D. Smoothness
also gives strong solutions on the corresponding operator domains.
Patching compact intervals by uniqueness defines it for all real times.
No hypothesis about a common OPERATOR domain is used.

There is a useful bound UNIFORM as c0 approaches zero. Set a=||A_c||,
e_t[psi]=h_c(t)[psi]+||psi||^2. Since |dot c|<=a|c|, (4) implies

    |partial_t e_t[psi]| <= 5 a e_t[psi].                  (5)

Indeed the differentiated linear term is bounded by
a(w sqrt(S)||psi||)<=a(w^2 S+||psi||^2)/2<=a e_t; the
differentiated square coefficient is bounded by 2a w^2 S<=4a e_t.
The usual energy identity for the smooth form evolution and density give

    e_t[V_c0(t,s)psi] <= exp(5a|t-s|) e_s[psi].             (6)

This is a source-graph energy bound for the NEW form. It is not the
oscillator-number bound disproved for the old cubic Hamiltonian.

## 4. The physical zero fiber is a continuous limit, not an arbitrary value

We prove V_c0(t,0) converges strongly to exp(-itA_+) as c0->0, uniformly
on compact t sets. Start with psi in physical C_c^infinity. Its initial
e_0 norm stays bounded as c0->0; (4),(6) bound q_+[psi_c(t)] and
w(t)^2 S[psi_c(t)] uniformly. For a fixed test z in C_c^infinity, the
weak equation has additional terms bounded by

    |g sum c_a <Q_a z,psi_c(t)>| <= C_z |c(t)|,
    |g^2|c|^2 sum <Q_a z,Q_a psi_c(t)>| <= C'_z |c(t)|.     (7)

The constants are uniform on the time interval by (6). The A_+ term is
<A_+ z,psi_c(t)>. These bounds make all scalar test amplitudes uniformly
equicontinuous. Weak compactness, a countable dense test set and a diagonal
subsequence give a weak continuous limit satisfying the A_+ Schrodinger
equation on its C_c^infinity operator core. Essential self-adjointness of
A_+ gives the unique weak solution exp(-itA_+)psi. Its norm is the same
as every approximating solution. Weak convergence plus equality of norms
therefore gives strong convergence. Uniform weak convergence on compact
time intervals and a finite-net argument along the continuous limiting
orbit make the strong convergence uniform there. Approximation of arbitrary
initial Hilbert vectors and unitarity extend the result to all H_p.

At a nonzero parameter c0, uniform common-form norms and smooth parameter
coefficients give continuous parameter dependence. This also follows by
the same energy/weak-uniqueness argument, now in the fixed common D;
on a compact parameter neighborhood the coefficient differences tend to
zero as bounded maps D to D*. Thus the propagators are strongly jointly
continuous in parameters, including the previously singular zero fiber.
This is stronger than assigning an arbitrary value on a null L2 fiber.

## 5. A genuine covariant self-adjoint full generator

Let H_kin=L2(R_c^d;H_p), d=4(n-1). With I_t(c)=integral_0^t
k(exp(-u A_c)c)du, define

    (U(t)F)(c)=exp(-i I_t(c))
              V_exp(-t A_c)c(t,0) F(exp(-t A_c)c).          (8)

The notation on V means its initial label is exp(-t A_c)c and its
characteristic runs forward from time zero to t. Uniqueness of V gives
the cocycle identity needed for U(t+s)=U(t)U(s). The constraint flow has
determinant one, so (8) is unitary; strong continuity follows by dominated
convergence on compactly supported continuous sections and density.
Stone's theorem supplies a self-adjoint full generator H_vp.

On smooth compact c sections supported away from zero, with physical
Schwartz factors, differentiating (8) gives

    H_vp=-i(bv).partial_r+k(c)+A_+(g)
                           +g c.Q+g^2|c|^2 sum_a Q_a^2.   (9)

For a fixed physical Schwartz vector psi, the common operator-domain
inclusion gives the identity

    V_c(t,0)psi-psi=-i integral_0^t V_c(t,s)h(c(s))psi ds.

The integrand norm is bounded by ||h(c(s))psi||, which is continuous
and uniformly bounded on compact c/time sets. This supplies an L2
dominating bound for the difference quotient of (8), including smooth
constraint-section coefficients. No regularity of an evolved Schwartz
vector is inferred. These expression tests are dense in H_kin. This
specifies a self-adjoint realization
of (9), not a proof that every self-adjoint extension of a full minimal
Schwartz expression must be the same. No global Schwartz invariance is
assumed. Its full operator domain can equivalently be specified by the
strong difference-quotient domain of the explicitly constructed group (8).

For every bounded Borel F, direct substitution gives the STRONG identity

    U(t)* F(c) U(t)=F(exp(t A_c)c).                         (10)

Thus both the spectral constraints and their maximal domains propagate
correctly. The full generator is not semibounded: the regular affine-orbit
Weyl relation still shifts its spectrum through all of R. Positivity in
(4) belongs to the physical fiber, and positivity below to the reduction.

## 6. Positive physical norm from a specified rigging limit

Use E=C_c(R^d;H_p), embedded as continuous representatives in L2.
It is dense. Equation (8) preserves it, by the continuity proved above.
Define the regulated constraint average

    q_epsilon(F,G)=integral da/(2pi)^d exp(-epsilon |a|^2/2)
                                      <F,exp(i a.c)G>
      =integral dc (2pi epsilon)^(-d/2) exp(-|c|^2/(2epsilon))
                                      <F(c),G(c)>.        (11)

For epsilon>0 the first integral is absolutely convergent. The positive
Gaussian approximate identity gives

    q_phys(F,G)=lim_epsilon->0 q_epsilon(F,G)=<F(0),G(0)>,
    H_phys=H_p,
    [U(t)F](0)=exp(-it A_+)F(0).                          (12)

The null quotient therefore has the same positive physical norm and
interacting dynamics as before. Every H_p vector is attained by a scalar
compact bump times that vector. No nonzero kinematic kernel at c=0 is
claimed. On tests where unregulated Haar averaging is integrable the
answer agrees with that average; unregulated absolute integrability on
the entire new E is NOT asserted. The finite-epsilon norm need not be
invariant under the shear; its limit (12) is invariant.

## 7. The original first dressed vertex really is restored

Conjugate the whole construction by the already defined gravity dressing
D_g, including its domains, constraint spectral measure and E. The actual
identity W=V1-DH_f=Q_TT.T+c.Q from the input yields

    [g] D_g H_vp D_g* = D H_f+Q_TT.T+c.Q=V1.              (13)

The new square (2) starts at g^2. As in Round14, H_f is quadratic, so
its first dressing commutator has no extra higher Moyal term. Equation
(13) is an exact first Weyl-expression jet on suitable local expression
tests, not an assertion of operator-norm analyticity in g.

This removes Round14's need to change the FIRST vertex. It pays instead
for a new constraint-quadratic, fourth-order matter operator and an
explicit closed-form quantization prescription. The old H_sr at all
orders, unique microscopic selection, local spatial current, homogeneous
gravity, continuum/Lorentz behavior and full TOE remain separate problems.
The Round14 auxiliary/clock construction is not automatically imported:
its separated Hamiltonian and transported spectral tube differ from (9).

## 8. Reproduction and resources

The companion checker reconstructs actual L2 Ward sources, verifies the
first vertex, second-ideal correction, nonzero off-shell witness and the
continuous-operator covariance. It includes exact coercivity, flow and
Gaussian-rigging controls, plus a Weyl-ordering negative control. These
bounded checks support, but do not replace, the form/propagator proofs.
No finite-dimensional canonical-commutator model is used.

There are d actual quadratic source operators. The form adds d squared
norms, no extra canonical pairs, and differential order four in matter.
The theorem gives existence and the finite-regulator energy constant (6),
not an efficient numerical propagator or a volume-uniform estimate.
