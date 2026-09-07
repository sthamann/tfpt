# Simultaneous auxiliary and first-class quantum reduction

2026-09-06. Round14 NON-RH appendix. This adds a constructive combination
to the frozen auxiliary `PROOF.md`; it does not amend its claims about the
unchanged old Hamiltonian. All finite lattice modes retained in the input
are included. No spectral truncation or unproved interacting fiber
propagator is used.

## 1. Precisely which Hamiltonian is now completed

Write N=n-1, h=4N, d=28N, and let c=(r,v) in R^h be the nonzero
gravitational constraints. In the Fourier-X representation c is
multiplication and X=i partial_c. The companion
`firstclass-completion-round14/PROOF.md` constructs

    A_c = [[0,b],[0,0]],       A_c^2=0, Tr A_c=0,
    K_c = -i(bv).partial_r+k(c),
    k(c)=r^T B_H r/2+v^T B_v v/2,
    H_first=K_c tensor I + I tensor A_+.                       (1)

Here A_+ is the unique self-adjoint positive actual TT/matter Hamiltonian
on H_p=L2(R^(2N+n)). Its Schwartz core and its nonnegative, smooth
polynomial potential have already been proved. K_c is the unique
self-adjoint closure of its displayed Schwartz expression. In particular

    (G_t a)(c)=exp(-i I_t(c))a(exp(-t A_c)c),
    I_t(c)=integral_0^t k(exp(-s A_c)c)ds                       (2)

is its exact group. It preserves S(c), has determinant-one transport,
and (G_t a)(0)=a(0). The full joint spectral domain, not an arbitrary
domain intersection, defines the sum (1).

The actual old eliminated symbol was

    H_sr=A_++K_c+g(r^T Bcal-v^T B_v J_v).

Thus (1) is a DECLARED first-class-ideal completion with difference

    H_first-H_sr=-g r^T Bcal+g v^T B_v J_v.                    (3)

The sources in (3) are the actual unprojected quadratic sources. This
changes the first off-surface interaction vertex, retains the entire free
gravity quadratic, and leaves the physical c=0 reduced Hamiltonian A_+
unchanged. For a term c_a F_a, its Hamiltonian vector field on c=0 is a
first-class gauge direction. This is the precise classical reduced
equivalence; it is not equality of the old and new unreduced operators.

The new input has the strong spectral covariance

    exp(it H_first) F(c) exp(-it H_first)
       =F(exp(t A_c)c)                                      (4)

for every bounded Borel F. We now exploit the established property (4),
rather than attributing it to an arbitrary old H_sr extension.

## 2. One common unitary for all the domains and constraints

Let eta=p_y in R^d and y=i partial_eta. Use

    H_ref=L2(R^h_c) tensor L2(R^d_eta) tensor H_p.

Keep the actual auxiliary KKT Hessian K_aux and source s=gB tau. As in
the frozen auxiliary proof, set

    f=-K_aux^-1 s,
    V(eta)=exp(-i eta.fhat),
    U_g(X)=exp(-ig X^a Jhat_a),
    W=U_g V.                                                (5)

Each fixed-eta generator in V is a real Weyl quadratic on the matter
factor, hence has its globally selected metaplectic propagator. The
unprojected f_i need not commute. V commutes with every bare c, X, eta,
and therefore with K_c and its unitary group. U_g commutes with y and
eta. The two factors U_g and V are NOT presumed to commute with each
other or with A_+.

All following self-adjoint operators use this same unitary transport:

    C_a=W c_a W*=U_g c_a U_g*,
    eta_j=W eta_j W*=eta_j,
    Y_g,j=W y_j W*.                                         (6)

The C_a strongly commute with one another and with every bounded
auxiliary Weyl operator; Y_g and eta form the transported canonical
auxiliary Weyl representation. In particular the Y_g,j strongly
commute with one another. Replacing Y_g by the naive y-f would destroy
that property for the actual noncommuting source.

No full common Schwartz invariance under W is asserted. The
metaplectic coefficients in V can grow exponentially in eta, and U_g
has its own parameter dependence. The exact definitions below transport
domains and cores instead of guessing a global regularity class.

## 3. Completed second-class total versus gauge-unfixed Hamiltonian

On reference space define

    H_circle=K_c+A_++q_K(y),  q_K(y)=y^T K_aux y/2,
    H_total=W H_circle W*,
    H_joint=W (K_c+A_+) W*.                                 (7)

These are self-adjoint. In the original auxiliary y representation all
three terms of H_circle act on separate factors and strongly commute.
Its exact domain is square integrability of E+kappa+q_K(y) with respect
to their product spectral measure. Indefiniteness of K_aux and K_c
does not obstruct the construction; cancellations can make this domain
larger than the intersection of the individual domains. The same rule
defines the joint sum K_c+A_+, tensor the eta identity, before transport.

For example, with D_p=S(Q,phi), the finite algebraic tensor space

    D_ref=S(c) tensor_alg C_c^infinity(eta) tensor_alg D_p      (8)

is an operator core of both reference operators in (7). The constant
coefficient quadratic q_K(i partial_eta), even when indefinite, has
C_c^infinity(eta) as a core. One direct proof first uses Fourier spectral
truncations and Schwartz approximation to obtain a Schwartz core, then
multiplies each Schwartz test by expanding smooth compact cutoffs; all
quadratic differential terms converge in its graph norm. For the tensor
sum, truncate the individual spectral variables to bounded boxes, use
density of finite tensor sums there, and approximate each factor in its
individual graph norm. Dominated convergence in the sum graph norm
handles removal of the boxes, including spectral cancellations.
Consequently W D_ref is a specified operator core of each transported
operator in (7).

The exact auxiliary propagation for H_total is

    Y_g(t)=Y_g,       eta(t)=eta-t K_aux Y_g.                  (9)

Its gravitational propagation is (4) with c replaced by C. Both
statements follow by conjugation from the separate reference factors;
in (9) the strongest formulation is the corresponding bounded Weyl
identity. Therefore H_total does NOT preserve eta=0 by itself.
It cannot be substituted for H_joint in a primary-only group average.

The separately DECLARED gauge-unfixing is

    H_joint=H_total-Y_g^T K_aux Y_g/2.                        (10)

Equation (10) means the operators defined by (7); on transported
expression tests it is the displayed subtraction. It is not a claim
that a difference of arbitrary unbounded-domain operators automatically
has the required self-adjoint closure. This prescription discards Y_g=0
as a quantum annihilation constraint, treats it as a gauge-fixing
partner, and retains only eta=0 as the auxiliary first-class list.
The original real second-class pair has no common nonzero annihilation
solution and is not replaced by an associative operator quotient.

For H_joint one obtains the simultaneous exact identities

    exp(it H_joint) F(C) exp(-it H_joint)=F(exp(t A_c)C),
    exp(it H_joint) B(eta) exp(-it H_joint)=B(eta),             (11)

for all bounded Borel F,B. Thus the full commuting constraint list
(C,eta) has an exactly covariant joint spectral measure; eta is now
constant. Equivalently H_joint and C generate the inherited semidirect
group, with auxiliary eta commuting with both. This closes strong
constraint propagation for this chosen finite model.

There are three separately disclosed changes: (3), the
primary-momentum-dependent canonical/quantum auxiliary completion, and
the secondary quadratic subtraction (10). Before U_g gravity dressing,
the eta=0 auxiliary Weyl symbol of V H_circle V* agrees with the old
H_sa plus (3), not with the old H_sa at arbitrary c. For H_total as
defined in (7), the corresponding symbol is U_g[H_sa+(3)]U_g*; both
sides must use the same dressed frame. On eta=0 and reference c=0
(transported C=0 after dressing), it retains the source graph and the
same positive physical dynamics. The operator ordering on the
full enlarged space is fixed by (5)--(7), not by a false full-space
Egorov identity for the cubic generator eta.f.

## 4. Simultaneous averaging gives exactly A_+ and its physical norm

For averaging choose a different, deliberately large dense test space

    E_ref=S(c) tensor_alg C_c^infinity(eta) tensor_alg H_p,
    E=W E_ref.                                              (12)

Only finite sums are used. Physical factors in (12) are arbitrary
Hilbert vectors; this avoids an unsupported assertion that
exp(-it A_+) preserves physical Schwartz space. The reference
constraint group exp(i(a.c+b.eta)) and the group
G_t tensor I_eta tensor exp(-it A_+) preserve (12). Therefore their
simultaneously transported groups preserve E. The averaging space
need not be a subset of the Hamiltonian domain; the operator core is
specified separately in (8).

Use Haar measure da db/(2pi)^(h+d). For F,G in E_ref, the matrix
element is a finite sum of Fourier transforms of scalar functions that
are Schwartz in c and smooth compactly supported in eta. Thus the
FULL joint matrix-element integral is absolutely convergent and

    q_phys(WF,WG)
       =integral da db/(2pi)^(h+d)
          <WF,exp(i(a.C+b.eta))WG>
       =<F(0,0),G(0,0)>_H_p.                                (13)

The null quotient completes to all of H_p: choose both scalar factors
to have value one at zero. No source determinant, extra energy
constant, or singular density is inserted. The ordinary common L2
kernel is zero because (c,eta)=0 is a null set; (13), not that zero
kernel, defines the physical space.

At the averaging point (2) gives

    [exp(-it (K_c+A_+))F](0,0)
       =exp(-it A_+)F(0,0).                                 (14)

The form (13) is preserved and the descended physical group is exactly
exp(-it A_+), with its already established self-adjoint domain and
positive norm. On S(c) tensor_alg C_c^infinity(eta) tensor_alg Dom A_+
the corresponding generator evaluation is A_+ F(0,0). This is a
quantum norm/evolution theorem, not only classical substitution.

The actual trace condition Tr A_c=0 has two roles: the transport in
(2) has no half-density factor at the zero orbit, and its action on
the c-group Haar measure has determinant one. Hence the unchanged
normalization in (13) really is covariant. For a nonzero trace neither
conclusion could be silently inherited with the same Haar convention.

The framework is compatible with
[Marolf's refined algebraic quantization](https://arxiv.org/abs/gr-qc/9508015),
but absolute convergence, normalization, positivity and the actual
descended group have been proved directly in (13)--(14). The only
quadratic/metaplectic input is the one already verified in the frozen
proof from [Combescure--Robert, sections 3--5](https://arxiv.org/html/math-ph/0509027v1).
No new general equivalence theorem for second-class quantization is
being invoked.

## 5. What has closed, and the clock interface

The former conditional auxiliary theorem becomes unconditional for
this specified H_first: domains, exact auxiliary canonical relations,
strong gravitational constraint covariance, positive joint physical
norm, and the actual positive TT/matter evolution coexist on one
explicit transported Hilbert-space construction. The already proved
massless uniform-scalar/no-ground-state boundary remains unchanged.

It does not solve the domain or covariance problem of the unchanged
old H_sr/H_sa. It does not make the indefinite completed H_total
positive, retain all real second-class constraints as annihilators,
select these off-surface changes from TFPT, establish microscopic
locality, recover deleted homogeneous gravity, or prove a continuum,
chirality or TOE statement.

For the separate trace-clock construction, apply its unitary Z ONLY
to A_+ and the clock pair, leaving c and eta untouched. The relevant
reference constraint then becomes K_c+M_lambda, not a square root of
the nonpositive H_first. If W_0=U_g V, the actual image of the old
A_+-clock tube is W_0 K_I. It is characterized by P_0<0 and

    W_0 A_+ W_0* - P_0^2/12 in I,                            (15)

not generally by the original raw A_+-clock spectral condition and
not by placing the TOTAL constraint in I. This domain distinction is
essential because W_0 need not commute with A_+. The separate joint
clock theorem supplies the further homogeneous relational constraints
and their common averaging; none is inferred from (13) alone.

## 6. Verification scope

This appendix is an analytic tensor-product/unitary-transport argument.
Its actual-source and ordering inputs are covered by the frozen
`auxiliary_domain_check.py`; its new K_c covariance, the nonzero change
(3), and the actual free/physical decomposition are covered by
`firstclass-completion-round14/firstclass_completion_check.py`.
Those exact finite checkers do not replace the all-Hilbert-space domain
and averaging proof above. Earlier-round proof artifacts are unchanged; this appendix is locally integrated research.
