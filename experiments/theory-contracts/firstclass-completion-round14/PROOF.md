# Constructive first-class quantum completion with an explicit off-shell change

2026-09-06. Finite, non-RH construction. The completion below is a declared
choice of Hamiltonian modulo the first-class constraint ideal. It is not
the unchanged off-shell Hamiltonian studied in Rounds 12--14.

## 1. Result and the precise permitted change

For the actual finite free-scalar/TT input, this note constructs a unique
self-adjoint Hamiltonian on the unreduced retained-gravity Hilbert space,
proves its strong constraint-spectral covariance, and computes a positive
physical inner product with exactly the previously proved interacting
reduced Hamiltonian. No interacting nonautonomous fiber propagator is
assumed. Gravity dressing transports all these statements exactly.

Fix a connected periodic finite cubic lattice of side L>=2, spacing a>0, scalar mass m>=0,
and real coupling g. Retain all scalar coordinates, including their mean,
and delete homogeneous gravity exactly as in the existing Darboux chart.
Write N=n-1, c=(r,v) in R^(4N), z=(Q,P,phi,pi), and {X,c}=I. The actual
identities in `covariant-domain-round13/README.md`, equations (1),(4),(5),
and `mixed-constraints-round11/README.md`, equation (4), give

    A_c = [[0,b],[0,0]],  b=(D_1^-,D_2^-,D_3^-),
    A_c^2=0,  tr A_c=0,  rank b=N,
    K_c = -X_H^T b v + k(c),
    k(c)=r^T B_H r/2+v^T B_v v/2,
    H_f=H_m+H_TT+K_c,
    H_sr=H_f+g[Q^T T+r^T Bcal-v^T B_v J_v]+g^2 R,
    R=sum_alpha T_alpha(phi)^2/(2 r_alpha^2).                 (1)

Here B_H and B_v are the verified real symmetric free matrices; each
T_alpha is the actual configuration-only homogeneous quadratic TT stress,
and r_alpha>0 is its free oscillator frequency. The vector Bcal and J_v
are the prescribed unprojected quadratic matter sources, not adjustable
parameters. The symbol B_H=-1/(2 ell) on a nonzero mode is negative.

Declare the new symbol

    H_first = H_+(z;g)+K_c,
    H_+ = H_m + sum_alpha [P_alpha^2/2
                +r_alpha^2 (Q_alpha+g T_alpha/r_alpha^2)^2/2]. (2)

Its exact difference from the old eliminated symbol is

    H_first-H_sr = -g r^T Bcal+g v^T B_v J_v.                 (3)

This is linear in the first-class constraints with matter coefficients
that commute with c and X. It vanishes on c=0. Thus (2) keeps the entire
free H_f, including its nontrivial constraint propagation, and keeps the
entire chosen positive reduced Hamiltonian, not just its first vertex.
It changes the prescribed first off-shell vertex by a generally nonzero
constraint-ideal term. Equation (3) is part of the definition, not a claim
that the original operator had the same domain or dynamics.

Classically the two vector fields differ on c=0 only by first-class gauge
directions: for Delta=c_a F_a(z), X_Delta restricted to c=0 is F_a X_c_a.
Their physical reduced flow therefore agrees, while their off-surface and
gauge-coordinate trajectories need not agree. Both obey {c,H}=A_c c.

## 2. Actual positive factor and the constraint-sector group

Let H_p=L2(R^(2N+n),dQ dphi). The actual T_alpha contain no pi dependence:
the common isotropic kinetic/mass trace is killed by each TT tensor. Hence
the physical expression is -Delta_(Q,phi)/2+V_g with V_g a smooth,
nonnegative polynomial of degree at most four. The cutoff deficiency
proof in `local-positive-auxiliary/QUANTUM_DOMAIN.md`, section 2, establishes
essential self-adjointness on C_c^infinity and on Schwartz space for every
fixed g and m>=0. Denote that unique closure by A_+(g). This is an actual
already proved infinite-dimensional operator, not a finite spectral cutoff.

For clarity, the only properties needed here are: A_+ is self-adjoint,
nonnegative, has Schwartz as an operator core, and acts there by (2).
We do NOT assume its unitary group preserves physical Schwartz space.

Fourier transform X with c as the multiplication variable; then
X=i partial_c. Weyl quantization of K_c on S(R^(4N)) is

    K_min=-i (b v).partial_r+k(c).                            (4)

There is no extra half-divergence term because tr A_c=0. Put d=bv and

    I_t(c)=integral_0^t k(e^(-s A_c)c) ds
          =t k(c)-t^2 r^T B_H d/2+t^3 d^T B_H d/6.
    (G_t u)(c)=exp(-i I_t(c)) u(e^(-t A_c)c).                 (5)

These formulas apply to every c, including bv=0. They give a strongly
continuous unitary group for every real t: det e^(t A_c)=1, the phase
has modulus one, and

    I_(t+u)(c)=I_t(c)+I_u(e^(-t A_c)c).                       (6)

The phase is quadratic in c and the pullback is linear. Consequently
G_t preserves S, continuously in Schwartz seminorms on compact t sets.
Differentiation gives i partial_t G_t u=K_min G_t u there; equivalently
partial_t I_t+(bv).partial_r I_t=k(c). Its Stone generator K is a
self-adjoint extension of (4).

Here is a direct core argument, to exclude hidden extension choices.
For a compactly supported smooth time mollifier a, the map
T_a f=integral a(t)G_t f dt obeys

    K T_a f=-i integral a'(t)G_t f dt.

Time mollification of a vector in Dom K approaches it in the graph norm.
For fixed a, approximate the input in Hilbert norm by Schwartz vectors;
the two displayed integrals converge in graph norm. The mollified
Schwartz vectors remain Schwartz, by compact-time seminorm continuity.
Thus S is a core of K. In particular (4) is essentially self-adjoint;
(5) is its unique unitary group. No deficiency-space boundary selection
and no nonautonomous interacting existence theorem are used.

## 3. Unique full self-adjoint Hamiltonian and its exact domain

Use H=H_c tensor H_p with H_c=L2(R^(4N),dc). Let E_K and E_+ be the
separate spectral measures. Define their joint spectral sum

    H_first = K tensor I + I tensor A_+,
    Dom H_first = {psi: integral |lambda+E|^2
                    d<psi,(E_K tensor E_+) psi> < infinity}.
                                                               (7)

Equation (7), not a naive assertion that the domain equals the intersection
of the two summand domains, defines a self-adjoint operator. K is not
semibounded and spectral cancellations can enlarge the domain.
Its exact strongly continuous unitary group is

    (U_t psi)(c)=exp(-i I_t(c))
                   e^(-it A_+) psi(e^(-t A_c)c).             (8)

The algebraic tensor product of a core of K and a core of A_+ is a core
of (7). One proof first truncates both spectral variables to |lambda|,
|E|<=L. For any vector in (7) these bounded rectangles converge in its
sum graph norm by dominated convergence. On each rectangle approximate
by finite sums of elementary tensors; then approximate the two factors
in their individual graph norms by their respective cores. A diagonal
choice gives convergence in the sum graph norm.

In particular S(c) algebraic-tensor S(Q,phi) is an operator core. Every
full joint Schwartz function belongs to both separate summand domains:
the corresponding polynomial differential expressions are square
integrable, and the separate self-adjoint maximal realizations give
membership by testing and Fubini. Thus

    S(c) tensor_alg S(Q,phi) subset S(c,Q,phi) subset Dom H_first.

On full joint S, (7) acts by precisely the Weyl expression (2). Since this
domain contains a core, that full joint Schwartz expression is essentially
self-adjoint and has (7) as its UNIQUE self-adjoint closure. This is a
theorem about the declared new off-shell expression. It does not select
an extension of the different old H_sr.

No common full operator domain as g varies, graph differentiability in g,
or Schwartz invariance under the interacting group is needed or asserted.

## 4. Strong constraint covariance, including spectral domains

The c_a are the ordinary strongly commuting self-adjoint multiplication
operators on their maximal domains. Formula (8) proves for every bounded
Borel function F on R^(4N), without a formal-domain limitation,

    U_t^* F(c) U_t = F(e^(t A_c)c).                          (9)

In particular the joint spectral measures are covariant, and the
self-adjoint unbounded identities U_t^* c_a U_t=(e^(t A_c)c)_a include
the correct transported maximal domains. This proves the strong property
that the unchanged-H_sr analyses left open, for the new Hamiltonian (2).

The kinematic operator is not positive. On the full-measure regular set
bv!=0, take s=(bv).r/|bv|^2 and r_perp=r-s bv. The measure is
dr=|bv| ds dr_perp, with a time-independent half-density. In each label
fiber K becomes P_s+q(s), where q is real quadratic. If F'=q,
M_F=e^(-iF(s)) obeys M_F P_s M_F^*=P_s+q(s). Moreover multiplication by
e^(-is A_+) conjugates P_s to P_s+A_+ in the joint spectral sense. These
two unitary gauges identify H_first with P_s tensor identity on this
regular full-measure space. The phases are measurable even when their
coefficients grow near bv=0. It follows that the full kinematic spectrum
is R and purely absolutely continuous, in agreement with (9).
The positive physical reduction below is a rigging-map quotient at c=0,
not a nonzero kinematic spectral subspace supported on that null set.

## 5. Explicit physical norm and interacting physical evolution

Take the dense test space

    E = S(R^(4N)_c) tensor_alg H_p.                          (10)

Physical factors in (10) are arbitrary Hilbert vectors. This is deliberate:
(8) preserves (10) without an unproved physical Schwartz-invariance claim.
The constraint group is R(a)=exp(i a.c). For psi,phi in E, its matrix
element is the Fourier transform of a scalar Schwartz function of c.
Therefore its normalized Haar average is absolutely convergent and

    q_phys(psi,phi)
       =integral da/(2pi)^(4N) <psi,R(a)phi>
       =<psi(0),phi(0)>_(H_p).                              (11)

The positive semidefinite form has null space exactly the tests with
value zero at c=0. Its quotient completes to H_p, because u(0)=1 with
u in S realizes every physical vector. The simultaneous kinematic L2
kernel of c is zero; it is not substituted for this rigging construction.

Since e^(-t A_c)0=0, k(0)=0, and tr A_c=0, equation (8) gives

    (U_t psi)(0)=e^(-it A_+) psi(0).                         (12)

Thus (11) is preserved and the induced strongly continuous physical group
is EXACTLY e^(-it A_+), with its previously proved self-adjoint domain
and positive norm. On S(c) tensor_alg Dom A_+, evaluating the generator
also gives (H_first psi)(0)=A_+ psi(0). This is not inferred merely from
a classical constraint-surface substitution.

The zero trace matters: a general non-volume-preserving linear transport
would introduce a nontrivial half-density at c=0, so this particular
unmodified Haar norm would not automatically be preserved. Actual
nilpotent A_c has exactly the needed determinant one.

The averaging interpretation follows the framework of
[Marolf, Refined Algebraic Quantization](https://arxiv.org/abs/gr-qc/9508015);
the norm and its absolute convergence here are computed directly in (11).

## 6. Exact gravity dressing and first-order comparison

Return to the X representation by the fixed Fourier transform. The actual
homogeneous quadratic currents define the established unitary

    D_g(X)=exp(-ig X^a J_a),
    C_a=D_g c_a D_g^*,
    H_first,dressed=D_g H_first D_g^*.                       (13)

For each X the matter generator is a real homogeneous Weyl quadratic;
the corresponding global metaplectic flow defines a measurable unitary
family for every real g. The primary quadratic input is
[Combescure--Robert, sections 3--5](https://arxiv.org/html/math-ph/0509027v1).
No claim is made that the complete interacting Hamiltonian is quadratic.

All domains and a core are transported by the same D_g. In particular
H_first,dressed is self-adjoint with core D_g S(full), and the C_a strongly
commute. Conjugating (9) proves the full strong dressed spectral covariance

    U_dressed(t)^* F(C) U_dressed(t)=F(e^(t A_c) C).           (14)

Transport the test space (10) as well. Its group average is (11) applied
to D_g^*psi,D_g^*phi. Consequently the physical norm and group remain the
same H_p and e^(-it A_+). This is an exact unitary construction; there is
no need for a common full Schwartz domain in the original X coordinates.

The price in the original dressed vertex can be stated exactly. Put
S=-X.J and D a={a,S}. The old first Ward identity is
W=V_1-DH_f=Q.T+r.Bcal-v.B_v J_v. Hence the first coupling jet of (13) is

    [g] H_first,dressed = D H_f+Q.T
                         = V_1-r.Bcal+v.B_v J_v.             (15)

The free symbol is exactly H_f. Because H_f is quadratic, its commutator
with S has no higher Moyal correction; (15) is the exact first Weyl jet.
One can take this jet on compact-X, Schwartz-physical tests, which are
preserved by the parameter-dependent metaplectic dressing and its local
parameter derivatives. No claim of an analytic operator family follows.
The full quantum ordering at nonzero g is defined by (13), not by an
unproved full cubic-generator Egorov equality.

## 7. Scope, auxiliary interface, and exact controls

This closes strong self-adjoint first-class propagation AND a positive
physical norm/time evolution for one explicitly declared finite completion.
It removes the prior domain obstruction by changing exactly (3), not by
proving a false estimate for the old operator. The actual scalar/TT
interaction, its positive g^2 term, and every free gravity block remain.

For the separate auxiliary construction, A in the joint-domain formula
may now be this uniquely defined H_first. The matter/auxiliary unitary
V(eta)=exp(-i eta.f), f=-K_aux^-1 gB tau, commutes with every bare c and X.
Thus the auxiliary completed total and its separately declared gauge-
unfixed Hamiltonian inherit (9) by unitary transport. The combined
auxiliary norm requires that declared gauge-unfixing; imposing all real
second-class constraints as a common quantum kernel is still invalid.
The separate combined contract spells out this prescription. No new
covariant-extension hypothesis about the old H_sr is required here.

The checker independently reconstructs the actual L2 Ward source and
free Darboux matrices, checks the NONZERO removed vertex, exact physical
agreement, full free agreement, first Ward/vertex signs, and quantum
transport identities on arbitrary functions. It also checks all-volume
structural identities at L=2,3. The all-finite-volume Hilbert-space proofs
are above; no finite matrix CCR approximation supplies them. The source
witness uses one actual retained tensor mode and all eight scalar sites;
the theorem keeps every TT mode through the established finite A_+.

Reproduce with `python3 firstclass_completion_check.py` from this folder.
The verified result is **35/35 exact check groups, zero floating-point
checks**. The first-class ideal change takes the exact nonzero value
`-3 sqrt(2)/128` on the declared retained-mode datum. The source frontend
path is printed with the results so its actual-repository provenance is
auditable. No numerical propagator or deficiency-index cutoff is used.

Not supplied: selection of (3) by TFPT, locality of the completion or its
dressing, a restored homogeneous gravity receiver, continuum or volume
limits, or equivalence to the unchanged off-shell Hamiltonian. These are
distinct from the finite quantum existence and physical-norm result just
proved. No RH or complete-TOE assertion is made.
