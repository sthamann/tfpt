# Symmetry with a minimal local rule: what is actually selected?

2026-09-12. NON-RH; conditional free scalar-circle theorem, not TOE closure.

## A precise simplicity theorem

Fix L2(S1,dtheta/2pi), periodic scalar functions and D=-i partial_theta.
Suppose K is a differential expression of order at most two with smooth
coefficients, symmetric on smooth periodic functions. Require invariance
under ALL rotations and the ordinary reflection f(theta)->f(-theta).
Then

    K = a D^2 + b I, a,b real.

Proof: write K=A(theta)D^2+B(theta)D+C(theta). Conjugating by every
rotation translates all coefficients. Equality of differential expressions
forces them constant. Reflection takes D to -D and eliminates B. Symmetry
forces the two remaining constants real. Semiboundedness forces a>=0;
a nonzero second-order kinetic term forces a>0. If K1=0 then b=0.
The closure has domain H2 when a>0; its quadratic form domain is H1.
Hence this declared free class has a unique kinetic shape, not a selected
absolute scale or a selected relative coupling to other sectors.

The corresponding primitive quadratic form is simply

    q(f)=a ||Df||^2.

It uses one derivative, its Hilbert adjoint, and composition. Hilbert space,
measure, periodic sector and the derivative have been supplied, not derived.
In the unit disk, the harmonic response is |D|, as proved in
SIMPLE_TYPED_BRIDGE.md. Physical time, harmonic extension depth and angular
rotation parameter are three different variables.

## Every hypothesis matters

1. Symmetry without derivative-order control does not select this operator:
   D^2+lambda D^4, lambda>0, is positive and invariant under all rotations
   and reflections. Its n=2 to n=1 energy ratio is (4+16lambda)/(1+lambda),
   not 4. Calling it less simple does not prove it absent from TFPT.
2. Fourfold symmetry, locality, reflection, positivity and K1=0 still do not
   suffice. For |epsilon|<1,

       K_epsilon = D (1+epsilon cos(4theta)) D

   has a closed positive form on H1 and is uniformly elliptic. It preserves
   the quarter clock and reflection, but for epsilon!=0 not all rotations.
   On e_n=exp(in theta),

       K_epsilon e_n = n^2 e_n
          +epsilon n(n+4)/2 e_(n+4)
          +epsilon n(n-4)/2 e_(n-4).

   This is a counterexample to uniqueness from these listed assumptions,
   not a proposed new TFPT coupling or a verified full-TFPT countermodel.
3. Other sectors, connections, measures, matrix-valued fields and physical
   reflection lifts require a new analysis. In particular a periodic scalar
   proof cannot settle the antiperiodic fermion or half-charge sector.

## Equivalent operational diagnostic within a diagonal rotor class

For K e_n=h(n)e_n on finite Fourier sums, require

    U* K U + U K U* - 2K = 2a I,

where Ue_n=e_(n+1). This is the recurrence
h(n+1)-2h(n)+h(n-1)=2a. Its complete solution on Z is
h(n)=a n^2+d n+b: subtract a n^2; the remaining first difference is
constant. Reflection sets d=0 and K1=0 sets b=0. This is an all-integer
proof, not a finite numerical fit. It supplies a test of uniform kinetic
response, not a derivation of that extra law. U may fail to preserve the
Gauss sector of an open lattice link; the single-rotor scope is essential.

## What the source audit changes

origin_theory.tex, opening core section, reads dimensions 3 and 5 from the
four-point divisor via topology and meromorphic functions, and explicitly
marks physical identification conditional. Those counts alone do not say
that the four marks must be delta-function energy interactions.
verification/v331_necessity_of_H.py, dtn, does insert such point couplings.
This is an additional modeling step in that inspected construction.
The operator theorem above does not authorize removing punctures or replacing
the marked surface by an unmarked circle: the state/function spaces differ.

There are two distinct symmetry contracts:

- Passive marks: the unmarked kinetic law may retain continuous rotations;
  a measurement or marked description singles out four places.
- Active marks: the dynamics itself depends on those places; only the
  stabilizer symmetry need survive, leaving the freedom demonstrated above.

A third distinction is covariance of the family under joint rotation of
fields AND marks, versus invariance of one operator with marks fixed.
Family covariance does not imply continuous symmetry of that fixed operator.

Next acceptance gate: derive from the actual TFPT source whether marks act
on the kinetic law, the domain, or the observable/readout map. Then justify
(or refute) second-order locality on that actual space. Do not promote
symmetry, chosen minimality, or the free scalar result to a derived vacuum,
interacting Hamiltonian, 3+1D geometry, or any T1--T8 closure.
