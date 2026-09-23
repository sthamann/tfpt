# Two marked rates: nonuniqueness beyond a choice of clock units

2026-09-14. This is an exact nonuniqueness statement under named algebraic and
channel requirements, **not a physically source-derived dynamics**. It stays
within the existing C4 word algebra and its16D operator representation.

## Correction to the one-rate argument

For T_gamma(t)=P0+exp(-gamma t)(I-P0), every strictly positive gamma can be
absorbed into the time unit. Full unmarked Clifford covariance strongly
restricts a Pauli-diagonal process to this depolarizing form. A freely chosen
positive gamma alone is therefore not evidence for inequivalent dimensionless
physics. The static gamma=0 case is separately degenerate.

## The actual marked source permits two sectors

The original v774 defines the even-five-slot map iota and quadratic refinement
qstar=wt(iota)/2 mod2. Its nonzero word orbits are O5={qstar=0} minus zero and
O10={qstar=1}; see `verification/v774_arf_spinor_compiler.py:743-777`,
`:784-822`. The bridge pins this source and independently reproduces the
selector and actual cocycle at `compiler-clifford-bridge/checker.py:60-104`.

Use its actual unitary word matrices P_v and set

    L = gamma5 sum_(v in O5)(Ad_Pv-I)
      + gamma10 sum_(v in O10)(Ad_Pv-I),   gamma5,gamma10>=0.

No additional physical carrier has been introduced. A word and its overall
phase give the same conjugation, but lift signs have not been discarded when
checking the symmetry action.

Every term is a unitary-jump channel generator. More elementarily, with
Gamma=5gamma5+10gamma10>0 and
Phi=[gamma5 sum_O5 Ad_P + gamma10 sum_O10 Ad_P]/Gamma,

    exp(tL)=exp(-Gamma t) sum_(n>=0) (Gamma t)^n/n! Phi^n.

This is a convex Poisson mixture of CPTP maps for every t>=0. At Gamma=0 it is
the identity. Thus the whole family is CPTP, unital and trace-preserving; this
does not rely on confusing Hilbert-space positivity with complete positivity.

## Exact counting, rates and signed covariance

P_v P_w=(-1)^b(v,w) P_w P_v. The source bilinear-form counts are

| Observed word w | Anticommuting O5 words | Anticommuting O10 words |
|---|---:|---:|
| w in O5 | 4 | 4 |
| w in O10 | 2 | 6 |

Each anticommuting jump contributes minus2 to the observed mode. Therefore

    r5=8(gamma5+gamma10),
    r10=4gamma5+12gamma10,
    exp(tL)=P0+exp(-r5 t)P5+exp(-r10 t)P10.

Here P0,P5,P10 are orthogonal **process** projectors of ranks1,5,10. The same
formula is a positive self-adjoint GNS transfer and obeys exact semigroup
gluing.

For the full marked S5 action, order the five Hermitian qstar-zero Clifford
words Gamma_j by the missing slot in their four-of-five parity vector. The
four adjacent permutations have explicit unitary lifts

    U_j=(Gamma_j+Gamma_(j+1))/sqrt2.

They exchange the two indicated Gamma words and negate the other three.
All64 generator/word images were checked with their actual signs, as were the
S5 Coxeter relations and all120 source slot permutations. There are16 negative
signs among these64 word transports. The generator L commutes exactly with
each lifted conjugation, because it is uniform within the two preserved
orbits.

This is the source-marked word action. It does not identify its sigma lift
with the distinct original Gaussian-coordinate sigma representation.

## The ratio is dimensionless and cannot be rescaled away

Two valid endpoints give

    (gamma5,gamma10)=(1,0): (r5,r10)=(8,4),  r5/r10=2;
    (gamma5,gamma10)=(0,1): (r5,r10)=(8,12), r5/r10=2/3.

A rescaling of time multiplies both rates together and cannot change either
ratio. To eliminate clock units completely, compare the two modes when the
O10 correlation has decayed to1/8. The O5 correlation is then **1/64** in the
first model and **1/4** in the second. The normalized trace, marked symmetry,
positivity and gluing rules are the same, but this dimensionless relation is
different.

The existence of these channels is not a derivation that either is executed by
TFPT. It proves only that the stated marked algebraic requirements do not
uniquely select that relative evolution.

## Complete positivity imposes an additional rate cone

The inverse coordinates are

    gamma5=(3r5-2r10)/16,
    gamma10=(2r10-r5)/16.

Consequently the CPTP semigroup cone in this two-projector family is

    r5/2 <= r10 <= 3r5/2,
    equivalently 2/3 <= r5/r10 <= 2

for nonzero rates. Arbitrary positive r5,r10 give a positive GNS transfer but
need not give a CP channel. With lambda5=exp(-r5 t) and
lambda10=exp(-r10 t), its normalized Choi eigenvalues are exactly

    (1+5lambda5+10lambda10)/16             multiplicity1,
    (1-3lambda5+2lambda10)/16              multiplicity5,
    (1+lambda5-2lambda10)/16               multiplicity10.

Their derivatives at t=0 in the nonidentity sectors are gamma5 and gamma10,
so nonnegative jump rates are also necessary for this semigroup to be CP at
arbitrarily short times. As a finite exact counterexample, the strictly
positive process operator with lambda5=3/4, lambda10=9/16 has Choi eigenvalue
**-1/128**. It is not CP.

## What changes under the full unmarked compiler symmetry

The exact Clifford witness U=(I+i Gamma_0)/sqrt2 normalizes every word but
mixes O5 and O10. The two-rate generator commutes with it only when the rates
coincide, hence gamma5=gamma10. On that line

    r5=r10=16gamma,
    L=-16gamma(I-P0).

Thus the earlier full-symmetry result is a genuine strong restriction: within
this family it leaves only depolarization and an overall positive time scale.
The new dimensionless freedom is specifically present under the actual
qstar-marked S5 requirements. One must not retain that freedom while also
claiming unchanged full unmarked G31/Clifford covariance.

## Verification

`two_rate.py` verifies the original eight bridge source pins, recomputes its
finite selector, and checks the source words, all anticommutator counts,
signed covariance, exact process and Choi decompositions and dimensionless
controls. `replay_two_rate.py` requires normal/-OO byte-identical JSON and
rejects three mutants: removal of lift signs, identification of the two rate
ratios, and inference of CP from positive process eigenvalues alone.

Counts and source hashes are in `two_rate_verification.json` and
`two_rate_replay.json`. Only this existing redteam directory was changed.
