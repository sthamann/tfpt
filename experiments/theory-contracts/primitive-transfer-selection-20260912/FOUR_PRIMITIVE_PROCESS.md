# A constructive narrower candidate: four inherited generators, two event rates

2026-09-12. NON-RH. Conditional forward model with fully explicit predictions.
It is not yet the physical compiler process or a complete TOE solution.

## The extra hypothesis is stated first

Use the original four Clifford generators g_1,...,g_4 of the audited frame.
Assume ONLY these are elementary independent Poisson jump operations on the
four-dimensional Hilbert space. Products are sequentially possible but are
not separate elementary jumps. Treat family covariance as a symmetry of
this process. Neither the independent-Poisson interpretation nor this support
restriction is derived from the original physical premises. Naming matrices
"generators" establishes algebraic generation, not stochastic primitivity.

With rates c for each of g_1,g_2,g_3 and e for g_4, c,e>0, define

    L(rho)=c sum_(i=1..3)(g_i rho g_i†-rho)
          +e(g_4 rho g_4†-rho).

This is an explicit CPTP semigroup generator, not unitary closed-system
dynamics. The family cycles the first three generators and fixes the fourth,
so it equates the three c rates but does not equate c with e.

## Why this is a real coupling candidate, not an independent-factor ansatz

In the existing compiler frame,

    g_1=-f u_2,   g_2=-f u_3,   g_3=-f u_1,   g_4=a.

The first three original generators are JOINT operations in the two-factor
description. With the notation of [COUPLING_RATE_POLYTOPE.md](COUPLING_RATE_POLYTOPE.md),
the support hypothesis forces

    local rates (a_1,a_2,a_3)=(3c,e,0),   b=3c,
    joint rates (y_1,y_2,y_3)=(3c,0,0),   y_0=0,
    first-only rates (x_1,x_2,x_3)=(0,e,0).

Thus the coupling is fixed GIVEN this support and the local rates. It is not
a third free choice after c and e. This does not contradict the larger
three-parameter region: the support assumption selects a boundary point.
In particular, the earlier diagnostic local rates (1,1,1), b=3 cannot come
from this four-generator-only hypothesis because it predicts a_3=0.

## Complete rate predictions

The local A-factor decay rates are (2e,6c,6c+2e). The B-factor decay rate is
4c on all three directions. The joint decay rates are

    (4c+2e, 2c, 2c+2e),

each repeated for the three family-related B directions. Hence the local
rates alone predict all joint rates, conditional on the primitive support.
Relations such as d_A3=d_A1+d_A2 and d_A2=(3/2)d_B are rejection tests.
For a real predictive test, infer c,e from two independently available local
measurements and reserve the other local and joint responses before selecting
the model. No such external experiment was carried out here.

The unique stationary state for c,e>0 is I/4; this is not a pure vacuum.
The spectral gap is 2 min(c,e). The total elementary jump intensity is
R=3c+e. Maximizing this gap at fixed R uniquely gives c=e=R/4: if c<=e,
the gap is 2c and c<=R/4; if e<=c it is 2e and e<=R/4. This is a separate
optimization principle and does not follow from the generator relations.
The previous nonuniqueness at maximal gap concerned a larger support with
fixed local dynamics; these are different optimization domains.

## The simplest equal-rate shadow

At c=e=r the negative generator, acting on the SIXTEEN-dimensional operator
space, has eigenvalues and multiplicities

    0, 2r, 4r, 6r, 8r
    1,  4,  6,  4,  1.

This is the binomial spectrum of four commuting conjugation flips. The
g_i anticommute as spinor operators, but their conjugation superoperators
commute because their central minus signs cancel. Their sixteen sign
characters exhaust all patterns, yielding the binomial multiplicities.
It is the same spectral pattern as a four-bit hypercube diffusion, not a
derivation that physical spacetime has four dimensions. Operator dimension
16 is not Hilbert dimension 16, and common spectra do not identify marked
processes, as [ASSEMBLY_NOT_HISTORY.md](ASSEMBLY_NOT_HISTORY.md) demonstrates.

The mathematical simplification is constructive: the same inherited primitive
operations can look locally simple while imposing nontrivial joint relations.
The outstanding premise is whether these are truly the physical elementary
events and why this event measure, state interpretation and time scale apply.
Without that derivation this remains a candidate, not the universal solution.

## Verification

The extended `coupling_rate_polytope.py` checks the four identities against
the pinned source frame, all sixteen generator actions, its embedding into
the general rate region, the three joint-rate formulas, total intensity and
the equal-rate binomial spectrum. The spectral-gap optimization is the
analytic two-case proof above. No fit to H70 or empirical constants is used.

Final combined replay: 151 exact controls per normal/-OO mode, byte-identical
outputs. This count includes the larger rate-region audit and source-frame
checks; it is not 151 independent tests of physical realization.
