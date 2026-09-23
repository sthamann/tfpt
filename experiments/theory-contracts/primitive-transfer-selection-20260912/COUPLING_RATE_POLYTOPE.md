# The complete coupling-rate region at fixed local compiler dynamics

2026-09-12. NON-RH. Conditional finite-dimensional theorem, not physical
selection of a TFPT generator. Extends [MINIMAL_COVARIANT_PROCESS.md](MINIMAL_COVARIANT_PROCESS.md).

## 1. Contract, provenance and classification

Keep its actual four-dimensional compiler frame, Hermitian Pauli factors
A_mu and B_nu, and the explicit covariance contract under a,f,u_j,w. Now
require a norm-continuous, time-homogeneous CPTP semigroup on this finite
space. Every channel is Pauli diagonal with the family-related error weights
equal. Differentiating its nonidentity Pauli weights at zero gives nonnegative
jump rates. Conversely any such rates define a CPTP semigroup by Poisson
mixtures and composition of the commuting Pauli conjugation channels.
Therefore ALL generators in this contract are

    L = sum_(mu=1..3) x_mu (Ad_A_mu-id)
      + sum_(mu=0..3) (y_mu/3) sum_(j=1..3)(Ad_(A_mu B_j)-id),
    x_mu>=0, y_mu>=0.

Identity-event rates are omitted: they have no effect on the generator.
No nontrivial Hamiltonian term survives covariance under all Pauli
conjugations. The premise that all those conjugations are physical symmetries
is still additional; this classification cannot be imposed on arbitrary TFPT.

`coupling_rate_polytope.py` pins the previous checker to
`1c853b49041aaa61e772ad331e22d9e5400c3192c81d69fead873396db6a9109`,
checks the original frame source through its existing pin and verifies its
eight declared upstream file hashes. The original suites are not rerun.

## 2. Exact remaining region after fixing both local generators

Let the first-factor Pauli jump rates be a_1,a_2,a_3 and the second-factor
isotropic total jump rate be b. Then

    a_mu=x_mu+y_mu,   b=y_0+y_1+y_2+y_3.

Thus the full remaining freedom is exactly

    0<=y_i<=a_i (i=1,2,3),    y_1+y_2+y_3<=b,
    x_i=a_i-y_i,    y_0=b-sum_i y_i.

This is a box cut by one plane, generically three-dimensional. It is not
an unlimited unspecified search space, and it is not a uniquely selected
coupling either. When b=0 or some a_i vanish, its dimension may decrease.
Independence means y_1=y_2=y_3=0, an allowed point but not a forced one.

## 3. Joint responses and exact inverse

First-factor decay rates are d_i=2(sum a-a_i); second-factor decay is 4b/3.
The three family-distinct joint decay rates are

    kappa_i=d_i+4b/3-(8/3)sum_(mu != i) y_mu.

For Delta_i=(3/8)(d_i+4b/3-kappa_i), inversion is

    y_i=(Delta_j+Delta_k-Delta_i)/2,   {i,j,k}={1,2,3}.

The checker derives every rate directly on all sixteen actual compiler Pauli
directions and verifies the inverse symbolically for arbitrary a,b,y. A set
of proposed observed rates is admissible in this class exactly when the
reconstructed y satisfies the inequalities above (and the local rates are
nonnegative). Measurement uncertainty would require interval/error treatment;
no laboratory measurement or sampling-cost guarantee is supplied here.

## 4. Stronger simplicity conditions still do not select the coupling

Set a_1=a_2=a_3=1 and b=3, merely as a diagnostic normalization. The remaining
region is the full unit cube 0<=y_i<=1. Every point has local decay rates 4
on both factors, and joint rates between 8/3 and 8. Hence the only stationary
operator direction is I, giving the unique physical stationary state I/4.

Each generator is Hilbert–Schmidt selfadjoint, because the jump conjugations
are selfadjoint involutions. This is detailed balance relative to the tracial
state, not a separately derived thermal temperature. The negative generator
is positive semidefinite. For every positive finite time the transfer is a
strictly positive selfadjoint operator on operator Hilbert space, with unique
largest eigenvalue one. This last use of "positive" is operator positivity;
complete positivity of its action is additionally supplied by the channel
construction. Neither identifies the transfer with a physical unitary flow.

Even the fastest possible spectral relaxation does not select a unique point.
The fixed local eigenvalues bound the spectral gap by 4. All y with
y_j+y_k<=3/2 for each pair attain this maximal gap.

Two explicit interior choices are:

| Quantity | Model A | Model B |
| --- | --- | --- |
| (y_1,y_2,y_3) | (1/2,1/2,1/2) | (3/4,1/2,1/4) |
| Local decay rates | all 4 | all 4 |
| Unique stationary state | I/4 | I/4 |
| Spectral gap, maximal at fixed locals | 4 | 4 |
| Total jump intensity | 9/2 | 9/2 |
| Superoperator trace | -72 | -72 |
| Joint decay rates | (16/3,16/3,16/3) | (6,16/3,14/3) |

All seven nontrivial grouped jump rates are strictly positive in both models.
The examples have the same local dynamics, positivity, symmetry, stationary
state, detailed balance, total event intensity and maximal spectral gap, yet
different full spectra and joint responses. The distinction cannot be removed
by a common change of time units because the local rates already agree.

The examples were constructed as counterexamples during this audit. They are
not blind predictions or two asserted physical universes. Their rates are not
derived constants. They disprove uniqueness under the LISTED premises, not
under all possible original TFPT conditions.

## 5. What this resolves and what it cannot resolve

The complete conditional finite generator family, positivity region, marginal
constraints, joint response law and inverse are now explicit. This stops
repeated searches for uniqueness from the same tested assumptions. Symmetry,
positive transfer, unique stationary state, Markov composition and maximal
relaxation gap do not close the three coupling freedoms in this model class.

A missing constraint must therefore be genuinely independent: for example a
source-derived coupling support or a primitive event measure. Locality or
independence cannot simply be named after the fact to choose a favorable
point. A different, physically derived covariance or state contract is also
a different problem, not a contradiction of this result.

The compiler's matrix multiplication allows joint monomials algebraically.
It does not assign them Poisson rates. The source assembly-loop audit already
excludes identifying its repeated matrix writes with those rates. Hence this
calculation does not manufacture the absent physical selection rule.

## Verification and implementation note

Normal and -OO executions use explicit exceptions and exact SymPy arithmetic.
The first implementation run stopped on a native integer zero lacking `.subs`.
A minimal reproduction isolated that type mismatch; changing only that zero
to `S.Integer(0)` corrected it. No mathematical acceptance condition was relaxed.
The systematic-debugging skill guided this repair; the requested test-driven
subskill was unavailable, so the one-off reproducer and full replay were used.

The written semigroup completeness, detailed-balance and gap arguments carry
the general quantifiers. Finite cube-vertex tests supplement the affine rate
bounds; they do not substitute for the proofs. No TOE/RH/P-versus-NP result,
paper/status promotion, commit, push or external export is claimed.

Final extended checker: 151 exact controls passed in normal and -OO modes,
with byte-identical JSON. This includes the narrower constructive hypothesis
in [FOUR_PRIMITIVE_PROCESS.md](FOUR_PRIMITIVE_PROCESS.md), not just the
general rate-region classification. The initial pre-extension replay passed
114 controls; only the final 151-control version is the current count.
