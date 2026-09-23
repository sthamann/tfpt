# Core-covariant processes: complete finite classification and joint reconstruction

2026-09-12. NON-RH. Conditional mathematical classification on the existing
compiler representations. No claim of a complete physical TFPT solution.

## 0. Scope and source provenance

The previous seam model was not the earliest compiler core. This audit returns
to its algebraic two- and four-dimensional representations. It reads ONLY
the reviewed pure `data`, `generators` and `frame` functions from:

- `compiler-cone-object-audit/checker.py`, SHA
  `1a23ba58f9ca9eec3d51425e9dd6f200c2e22cd89cfd88a8f123dcbe489c4304`;
- `compiler-clifford-bridge/checker.py`, SHA
  `bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d`.

It verifies all eight upstream pins declared by the latter and rechecks all
64 products identifying its anchor commutant with the small representation.
Those upstream suites are not fully rerun. The scalar relationships in
`verification/v53_compiler_core.py` were also read: that file expressly calls
them readings/syntheses of already specified atoms, not new physical inputs.

The NEW CONDITIONAL contract is a linear completely positive trace-preserving
(CPTP) map on one stated finite Hilbert space, covariant under EACH of the
specified inner compiler symmetries. These covariance requirements are stronger
than merely belonging to the compiler algebra or preserving the family cycle.
Neither this physical channel interpretation nor covariance under every unit
has been derived from TFPT's original physical premises. Changing that contract
can change the classification.

## 1. Complete classification on the two-dimensional commutant representation

Let I,u_1,u_2,u_3 be the documented quaternion matrices and
w=(I+u_1+u_2+u_3)/2. With Hermitian Pauli basis sigma_j=-i u_j,
conjugation by u_j fixes axis j and negates the other two axes; conjugation by
w cycles the three axes. A general Hermiticity-preserving trace-preserving
qubit map is affine on Bloch vectors: r -> M r + b.

Covariance under the three sign flips forces b=0 and M diagonal. Covariance
under the cycle forces the three diagonal entries equal. Therefore ALL maps
in the declared class have form

    D_lambda(X)=lambda X+(1-lambda)Tr(X) I/2.

The unnormalized Choi eigenvalues are (1+3 lambda)/2 once and (1-lambda)/2
three times. Complete positivity is exactly -1/3 <= lambda <= 1. The checker
also solves the full superoperator commutation constraints: dimension two
before trace preservation, leaving one parameter after it.

This extends the older [RELATIONAL_RESULT.md](RELATIONAL_RESULT.md), which
obtained depolarization from a particular quadratic comparison energy. Here
no choice of that energy ansatz is required. It is still a standard finite
symmetry/channel classification, not a new general quantum-information law.
For channel and Choi conventions see
[IBM Quantum channel basics](https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/quantum-channels/quantum-channel-basics).

If a continuous time-homogeneous semigroup is additionally required, continuity
at zero and lambda(t+s)=lambda(t)lambda(s) imply lambda(t)=exp(-gamma t),
gamma>=0. To see positivity, lambda(t)=lambda(t/2)^2>=0; a finite-time zero
would contradict continuity at zero by repeated halving. The logarithm is
continuous and additive. The rate gamma is not fixed by symmetry.

For gamma>0 the unique stationary density matrix is I/2, NOT a pure vacuum.
For gamma=0 every state is stationary. The only unitary channel in this class
is the identity: preservation of pure-state purity needs lambda^2=1, while
complete positivity rules out lambda=-1. Thus demanding a nontrivial unitary
time evolution AND covariance of each fixed channel under all these units
would be too restrictive. A covariant FAMILY with transforming additional
data is a different contract.

## 2. Link to the positive cone, without confusing it with spacetime dynamics

For X=tI+x sigma_1+y sigma_2+z sigma_3, det X=t^2-x^2-y^2-z^2. But

    det D_lambda(X)-det X=(1-lambda^2)(x^2+y^2+z^2).

The depolarizing process preserves the positive state cone while generally
changing this determinant. It is not a Lorentz isometry merely because the
same matrices represent a Lorentz cone. For a nontrivial channel, a normalized
pure state moves into the interior. The shared representation is real; the
identification of information relaxation with relativistic motion is not.
Both polynomial identities are checked on the actual small compiler matrices.

## 3. Keep the full core: seven parameters remain

The four-dimensional compiler frame also contains f with f^2=I,
a^2=-I, af=-fa, and commuting quaternion units u_j. Define Pauli factors

    A=(I, f, i a, a f),    B=(I, i u_1, i u_2, i u_3).

They commute between factors, and their sixteen products are an orthonormal
Hermitian Pauli basis. This is an algebraic factorization, not a newly derived
spatial tensor-product decomposition. Require channel covariance under a,f,u_j
and w=(I+u_1+u_2+u_3)/2 on THIS space.

The Pauli conjugations give sixteen distinct sign characters, forcing any
covariant superoperator to be diagonal in A_mu B_nu. Family covariance groups
nu=1,2,3 for each fixed mu, leaving eight diagonal values and, after trace
preservation, SEVEN parameters. This is not the one-parameter qubit answer.

Equivalently every such CPTP channel is a Pauli mixture with probabilities

    weight(A_mu)=p_mu-q_mu,
    weight(A_mu B_j)=q_mu/3,  j=1,2,3,

where sum p_mu=1 and 0<=q_mu<=p_mu. Necessity of nonnegative weights follows
from the mutually orthogonal Pauli Bell eigenvectors of the Choi matrix;
sufficiency is the displayed random-unitary Kraus mixture. The orthogonality
and invertible Pauli sign transform are checked. All parameter dimensions
refer to the interior; boundary channels may have fewer free coordinates.

The first-factor marginal channel determines the distribution p_mu (three
parameters). The second-factor depolarizing channel determines
s=sum q_mu (one parameter). Fixing both marginals therefore leaves

    0<=q_mu<=p_mu,   sum q_mu=s,

a generically THREE-dimensional convex polytope. Choosing independence,
q_mu=s p_mu, selects one point but is an extra assumption, not a symmetry result.

## 4. Same complete local dynamics, different joint answer

Let Z=A_1, and let C_j=B_j, j=1,2,3. Consider

    E_corr(rho)=rho/2 + (1/6)sum_j Z C_j rho C_j Z,
    E_ind= (1/2)(id+Ad_Z) composed with
           ((1/2)id+(1/6)sum_j Ad_Cj).

Both are CPTP and satisfy every specified covariance. Their complete reduced
output maps agree on both factors for EVERY input operator, including inputs
with correlations. This equality is checked on the full sixteen-element basis.
It is not merely an agreement on a few local expectation values.

For J=A_2 B_1, rho=(I+J)/4 and measurement effect E=(I+J)/2:

    Tr(E E_corr(rho))=5/6,
    Tr(E E_ind(rho))=1/2.

The checker verifies positivity, normalization, the projector measurement and
both exact probabilities. The half weights are a diagnostic choice, not
derived constants. This is not an external measurement or a claim of physical
access to the two factors. It shows what information local descriptions omit.

## 5. Positive closure: three joint readouts reconstruct the whole channel

Define the 4x4 sign matrix

    H_i,mu=Tr(A_i A_mu A_i A_mu)/4,    H H^T=4I.

From known marginal p define eta_i=(H p)_i. The eigenvalue c_i of the
joint observable A_i B_1, for i=1,2,3, satisfies

    c_i = eta_i - (4/3)(H q)_i.

Family covariance makes the choice of B_1 versus B_2 or B_3 immaterial for
this coefficient. Therefore

    q = (1/4) H^T [s, (3/4)(eta_1-c_1),
                      (3/4)(eta_2-c_2), (3/4)(eta_3-c_3)]^T.

This is an explicit unique inverse. It is symbolically verified for arbitrary
p_mu and q_mu and compared with the actual compiler-matrix channel action.
Each c_i can in principle be obtained from input rho_i=(I+A_i B_1)/4 and
effect E_i=(I+A_i B_1)/2: the probability is (1+c_i)/2. The three tests use
separate preparations; no simultaneous measurement of incompatible observables
is assumed. Preparation and joint readout availability remain physical obligations.

Accept a reconstructed channel only when sum p_mu=1 and 0<=q_mu<=p_mu within
appropriately propagated uncertainty. If p and s are exact and each c_i has
absolute error at most epsilon, the inverse formula gives
|delta q_mu|<=9 epsilon/16. This algebraic conditioning bound is not a sample-
complexity or physical-noise guarantee. One should also test the predicted
B_2/B_3 responses as consistency checks rather than silently assuming covariance.

Thus the finite identification problem in this precisely specified class is
closed GIVEN the two marginal maps and three joint response coefficients.
It does not select their values from the compiler and does not solve a TOE.

## 6. Concrete consequence for the universal-object search

### A composition-law countercheck: the ambiguity survives Markov evolution

With gamma>=0 define two time-homogeneous generators

    L_corr = gamma [(1/3)sum_j Ad_(Z C_j)-id],
    L_ind  = gamma (Ad_Z-id)+gamma [(1/3)sum_j Ad_Cj-id].

Each generates CPTP semigroup evolution: for any channel F,
exp(t gamma(F-id))=exp(-gamma t) sum_n (gamma t)^n F^n/n!, a convex
Poisson mixture. The two summands of L_ind commute here, so their semigroups
compose to give a CPTP semigroup as well. They obey the specified covariances.

Their complete local generators agree, and each Pauli direction is an
eigenoperator. Thus their local maps agree for every time, not just to first
order. Yet the joint witness J obeys

    L_corr(J)=-(2 gamma/3)J,   L_ind(J)=-(10 gamma/3)J.

The same rho and effect as above give time-dependent probabilities
(1+exp(-2 gamma t/3))/2 and (1+exp(-10 gamma t/3))/2. The generator identities
and closure on each Pauli direction are checked exactly; the exponential
formula follows analytically. No empirical rate or physical clock is derived.

Therefore continuous homogeneous iteration and no temporal memory do NOT by
themselves determine joint dynamics. Our earlier emphasis on history needs
this qualification: even memoryless processes can carry different simultaneous
joint-event correlations with identical local histories. Markov composition
alone does not choose the missing coupling law.

Do not infer uniqueness of a full process from a simple one-factor shadow.
The missing information in this audited class is neither an unspecified huge
space nor another isolated integer: it is three joint process correlations.
Local inputs leave those three free. Joint responses determine them uniquely.

This supplies a bounded forward/inverse test for a proposed source rule:
derive p,q without choosing them to match outputs; compute all local and joint
responses; reserve at least one not-used response before fitting or choosing
the candidate. The present symbolic calculation is not such a blind prediction.
None of the source files read here derives the displayed event probabilities.

## Verification

`minimal_covariant_process.py` uses explicit checks surviving -OO. All source
hashes, the small/full product map, covariance dimensions, Choi polynomial,
cone identities, full marginal equality, joint witness and symbolic inverse
are tested. General semigroup and Choi-classification arguments are written
above; no full continuum construction or experiment is performed.

Final extended version executed on 2026-09-12: 203 exact checks passed in
normal and -OO modes with byte-identical JSON, including the Markov
countercheck. Many checks concern source algebra and provenance, not
independent physical predictions. `git diff --check` also passed. No commit,
push, paper/status promotion or external export was made.
