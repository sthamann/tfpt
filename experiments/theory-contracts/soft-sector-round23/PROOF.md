# Round23: exact soft compression, controlled dynamics and a hard-mode witness

2026-09-07. NON-RH. Compare the actual original common parent X with its
explicitly changed Round22 torus average X_av. Exact compression is first
proved for the whole polynomial parent. The time bounds and explicit
leakage witness then use the declared g=0, nu=0 scalar/charge slice, with
the other continuous species retained as decoupled free factors.

## 1. An exact no-alias compression theorem

Choose positive reference frequencies equal on each real cosine/sine pair.
For the scalar choose its ACTUAL free frequency omega_q, not frequency
one. This does not change Round22's translation group: the pair generator
q_c p_s-q_s p_c is independent of that common reference frequency. A
unit-frequency vacuum would generally differ from the physical vacuum.

For odd L and an integer cutoff kappa>=0 with 4 kappa<L, let P_soft:

- retain the charge translation characters with every |k_i|<=kappa,
  without restricting any integer charge magnitude or energy;
- put continuous oscillator modes with any |q_i|>kappa in their
  reference vacuum, for ALL 35 species, allowing arbitrary occupation
  in the remaining modes.

This is a kinematic Fourier projection, NOT an energy cutoff and not
an invariant interacting subspace. It commutes with the torus action.
On its projected finite-charge/Schwartz core one has the EXACT form identity

    q_X(P_soft psi,P_soft phi)=q_Xav(P_soft psi,P_soft phi). (1)

To prove it, normal order the actual polynomial factors before taking
the hard-mode vacuum expectation. Hard-mode contractions carry zero signed
momentum; they do not create a reciprocal-lattice defect. Pure continuous
terms have degree at most four. Charge-scalar terms contain a charge
character difference (at most 2 kappa per component) and two continuous
legs (at most 2 kappa). Hence every remaining frequency component has
absolute value at most 4 kappa. Original discrete translation invariance
requires that component to be a multiple of L. The STRICT inequality
4 kappa<L leaves only zero, which is exactly what the torus average keeps.
D and hopping already commute with the torus action and remain unchanged.

The closures of these common compressed-core forms agree as well. This
does not assert equality of unexamined maximal restriction domains or of
P_soft exp(-itX)P_soft and P_soft exp(-itX_av)P_soft. Projecting an operator
does not integrate out the omitted modes. The first useful case is L=5,
kappa=1, not L=3 with all its nonzero modes called soft. Boundary equality
4 kappa=L is unsafe: a nonzero reciprocal-lattice frequency can then occur.

## 2. A genuine all-time comparison on a specified finite-particle sector

Now set g=nu=0, m>0 and use the original full positive hopping. Write

    H_0=H_m+H_c(J), H_lambda=H_0+lambda V_1,
    H_av,lambda=H_0+lambda V_1,av, lambda>=0.

Independent free continuous factors can be tensored throughout. The
physical energy constants are not removed. For total root charge p=e2,
let P_band be Round22's EXACT lowest N-state charge spectral projection,
on the infinite charge carrier, at

    eps=48 N^2 J<=1/32, J>0.

Bounded perturbation gives the operator norm estimate

    ||D P_band|| <= (1+2eps)/N =: d_N.                (2)

Indeed H_c-48NJ=D+JK has spectrum within 1/N +/- Jb on the band,
b=48N, and ||JK||<=Jb. Let P_M retain at most M free scalar quanta in
ALL momentum modes. This is a preparation class, not a replacement of
the canonical algebra. For each site, writing phi_x=a(f_x)+a*(f_x),

    ||f_x||^2=(1/(2N))sum_q 1/omega_q<=1/(2m),
    ||phi_x^2 P_M|| <= 2 sqrt((M+1)(M+2))/m =: C_M. (3)

The second estimate follows by applying the full ladder operators twice;
the intermediate state can have M+1 quanta and the output M+2. On each
charge configuration, all e(n_x) are nonnegative. The triangle inequality
in that fiber, followed by the charge norm, therefore gives

    ||V_1 (P_band tensor P_M)||<= C_M d_N.           (4)

The same bound holds for V_1,av, since the preparation projection is
torus-invariant. H_0 preserves this projection. Duhamel's identity along
the FREE orbit is therefore legitimate on its domain and extends by
density to the preparation space. The interacting orbit need NOT remain
in that space. For every real t,

    ||(exp(-itH_lambda)-exp(-itH_av,lambda))
                    (P_band tensor P_M)||
       <=min(2, 4 lambda |t| sqrt((M+1)(M+2))
                              (1+2eps)/(m N)).       (5)

This is a true operator-norm dynamical comparison, not just (1) or a
formal perturbation series. It keeps the full unbounded interactions.
For any normalized prepared state and bounded observable A, twice this
state-norm bound times ||A|| also bounds the difference of expectations.
Unbounded stress/energy observables need additional graph-norm control.
The Duhamel argument compares each dynamics with H_0, so the price of
its simple bound is that both interactions are weak on this preparation.

For the dynamical soft-mode test below, P_soft,sc means the charge and
SCALAR factors of P_soft tensored with the IDENTITY on the other continuous
species. No common stationary auxiliary reference vacuum is assumed.
Identity (1) also holds for this projection in the g=0 slice: the other
free factors are unchanged by averaging and commute with the projection.

For a scalar vacuum initial state, Wick's exact fourth moment sharpens
||phi_x^2 vac|| to sqrt(3)/(2m). The same reasoning improves (5) to

    error <=min(2, sqrt(3) lambda |t| (1+2eps)/(m N)). (6)

For fixed M,lambda,m,t and J satisfying the stated N-dependent window,
these bounds tend to zero with N. This is a dilute, weakly coupled
comparison: J is forced to scale at most as N^(-2). It is NOT a nontrivial
relativistic continuum limit, a finite-density result (M proportional to
N need not give a vanishing bound), or a bound at arbitrary fixed J.

## 3. The same control for the positive-frequency clock

Let gamma>0 be a retained common lower bound for H_0, H_lambda and
H_av,lambda, and S=sqrt(12H). No physical energy constant is subtracted
to manufacture gamma. On P=P_band tensor P_M, the resolvent identity and

    sqrt(A)-sqrt(B)=(1/pi) integral_0^infinity
        s^(1/2)(A+s)^(-1)(A-B)(B+s)^(-1) ds,
    (1/pi) integral_0^infinity sqrt(s)/(gamma+s)^2 ds
        =1/(2sqrt(gamma))

give ||(S_lambda-S_0)P||<=sqrt(3/gamma) lambda C_M d_N,
and the same bound for S_av-S_0. The identity is used as a convergent
operator-norm integral AFTER restriction to P: the right free resolvent
preserves P and (A-B)P is bounded by (4). It is not an assertion that
A-B is bounded on the full Hilbert space. The resolvent equation is
justified on these vectors by their common H_0/interacting operator domain;
the resulting integral supplies the square-root domain estimate.

Applying Duhamel along the free S_0 orbit therefore gives

    ||(exp(-i tau S_lambda)-exp(-i tau S_av,lambda))P||
       <=min(2, sqrt(3/gamma) * 4 lambda |tau|
                  sqrt((M+1)(M+2))(1+2eps)/(mN)).    (6a)

The scalar-vacuum improvement multiplies the uncapped right side of (6)
by sqrt(3/gamma), then caps the result at two. This compares positive-
frequency data in their common canonical initial-data Hilbert chart.
It does not identify original model-dependent weighted wavefunctions,
Gaussian encoding or source/observable maps. Vanishing clock error also
requires that the chosen positive gap not degenerate too quickly with N.

## 4. Exact low-mode compression nevertheless misses a real transition

Take odd L>=5, kappa=1, chi_0(J) from the exact charge band, and the
scalar vacuum. The initial state psi=chi_0 tensor vac is in P_soft,sc and
has total signed K=0. Here the dynamical projection is P_soft,sc as defined
above, not the all-species projection in Section 1. Spectator factors may
be chosen in a K=0 Schwartz
state and do not affect the argument. Put q=(h,0,0), h=(L-1)/2.
The state f=chi_e1 tensor |2_q> contains two quanta of that SAME hard mode.
It lies outside P_soft,sc, and its signed total momentum is

    e1+2q=L e1 !=0, but equals zero MODULO L.

The exact Bose normalization gives

    <2_q|phi_x^2|vac>=sqrt(2) exp(-4pi i q.x/L)/(2N omega_q),
    <f|V_1|psi>=F_e1,0(J)/[sqrt(2) N^2 omega_q],
    |F_e1,0(J)|>=29/40.                              (7)

The last bound is Round22's full-carrier result, valid for this odd L.
The original transition is nonzero even at fixed positive J in its window;
the average deletes it exactly, since its unwrapped momentum is L e1.
For L=5, N=125 the certified J endpoint is 1/24000000 and
omega_q^2=m^2+(5+sqrt(5))/2. No oscillator or charge cutoff is used.

## 5. Its observable short-time consequence, without analytic perturbation claims

Let Q=I-P_soft,sc. Then QH_0 psi=0. Both Hamiltonians have psi in their
operator domains: finite charge-energy cutoffs converge in the D graph
norm, (4) controls V on the finite-particle vectors, and the averaged
interaction is the bounded K=0 projection of V psi. This approximates
psi and its operator image from the specified common core.

Strong differentiability at t=0 requires only Dom H, not Dom H^2, and gives

    ||Q exp(-itH_lambda)psi||^2
       =lambda^2 t^2 ||Q V_1 psi||^2+o(t^2),

and the analogous expression with V_1,av. Since Q commutes with K and
V_1,av psi=E_(K=0)V_1 psi, the difference of the two leading coefficients is

    D_leak=||(I-E_(K=0))Q V_1 psi||^2,
    (29/40)^2/[2 N^4 omega_q^2] <= D_leak
       <=3(1+2eps)^2/[4m^2 N^2].                    (8)

Thus the escape probabilities differ by lambda^2 t^2 D_leak+o(t^2),
with a strictly positive, explicitly bounded coefficient. This is
consistent with the all-time upper bound (6), not a contradiction.
It proves that identical directly compressed forms do not imply identical
reduced dynamics. No convergent lambda power series, Feshbach analytic
expansion or uniform bound on the little-o remainder is assumed.

## What is solved and what remains

The no-alias compressed form, an all-time norm comparison for a declared
low-band/few-quanta preparation, and the leading difference in hard-mode
escape are established with explicit domains and constants. These are
three different assertions. The preparation projections do not change
the Hamiltonians or supply a new microscopic selection principle.

A local relativistic effective theory still requires nontrivial scaling,
finite-density/energy control, virtual-mode contributions, local observable
identification and full gravity. Those do not follow from (1) or (5).
No T1-T8/TOE/RH or empirical promotion.
