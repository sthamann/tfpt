# Carrier-module conjugation and the remaining microscopic choice

2026-09-08. Exact lattice/cocycle result plus a conditional source-symmetry
test. No T1–T8, TOE or RH status promotion.

## 1. The 5+3 marking can be recovered from norm and charge grade

Let L be the existing E8 lattice in physical coordinates and retain the
existing character

\[
 k(q)=2\sum_{i=1}^5q_i\pmod4,\qquad L_0=\ker k=D_5\oplus D_3.
\]

This character is input from the preceding carrier construction; its
microscopic origin is not newly derived here.
Among the norm-two roots, the neutral roots are precisely the 40 D5 roots
and 12 D3 roots. Their second moment is

\[
 M_0=\sum_{\alpha\in L_0,\ \|\alpha\|^2=2}\alpha\alpha^T
    =16P_5+8P_3,\qquad
 P_5={M_0-8I\over8},\quad P_3=I-P_5.
\]

Proof: the roots of D_m are all ±e_i±e_j. Their off-diagonal moments
cancel and every diagonal entry is 4(m-1). Thus the two marked real
subspaces are intrinsic to the norm together with this one Z4 character.
There is no need for an *additional* arbitrary coordinate projector once
these data have been specified.

## 2. A carrier-preserving symmetry missed by the earlier pair reflection

The preceding [origin audit](../origin-composition-audit/README.md) used
a pair-swap reflection R. It interchanges the two unoriented Clifford
choices but does not preserve k. That negative result concerned R, not
every possible symmetry.

Instead take

\[
 K(q_1,\ldots,q_8)=(q_1,-q_2,q_3,-q_4,q_5,-q_6,q_7,-q_8).
\]

Then:

- K is an E8 lattice isometry, K^2=I and det K=+1.
- It flips two coordinates in each of the 5- and 3-dimensional blocks,
  so K belongs to W(D5) x W(D3).
- k(Kq)-k(q)=-4(q_2+q_4), an integer multiple of 4 on all of E8.
- K commutes with the existing family action sigma.
- KJK^(-1)=-J: it reverses the chosen Gaussian complex orientation.

The compiler quotient V=L/(1+J)L is fixed pointwise. Indeed, in the
existing coordinate convention,

\[
 (1+J)^{-1}(K-I)q
 =(-q_2,-q_2,-q_4,-q_4,-q_6,-q_6,-q_8,-q_8)\in L.
\]

For integer q this has even coordinate sum; for half-integer q it remains
in the half-integer E8 coset with even sum. Therefore the change is zero
in V. On the four existing finite compiler sections, K acts by
[2,3,0,1], exchanging the two pairs related by the Gaussian deck action.
The checker verifies the lattice generators, metric, full character,
family action and every finite quotient element.

Consequently the two choices are equivalent under a symmetry preserving
the *carrier module and unoriented J*. This does not prove equivalence
when oriented J is held fixed. Real orientation is preserved, so the
result must not be relabelled as a physical parity or CP theorem.

## 3. The charged lift preserves the actual neutral carry

Use the pinned lattice cocycle epsilon(q,p)=(-1)^c(q,p). In the existing
integer lattice basis the columns of K modulo 2 are

    (1, 3, 5, 9, 17, 33, 65, 230).

Its lift is not merely a permutation of basis states. Construct the
quadratic phase p_K by polarizing

\[
 p_K(x)+p_K(y)+p_K(x+y)=c(Kx,Ky)+c(x,y)\pmod2.
\]

All 65,536 cells of this identity are checked. The existing coherent
Gaussian/family lifts admit the four additional character choices
[0,126,128,254]; here the zero character is used. This choice obeys the
involution, family-commutation and J-reversal coherence equations.

On the finite-support core of ell^2(L), let

\[
 V_K|q\rangle=(-1)^{p_K(q)}|Kq\rangle,\qquad
 U_s|q\rangle=(-1)^{c(s,q)}|q+s\rangle.
\]

Both extend as unitaries. The polarization identity gives
V_K U_s V_K^(-1)=(-1)^{p_K(s)}U_(Ks) on the whole integer lattice,
not just on its reduction modulo 2. The permutation also commutes with
H_0|q>=||q||^2|q>/2, including the self-adjoint domain of this diagonal
operator.

For the existing positive charge representative s=(1/2)^8,

\[
 Ks=s+\delta,\qquad
 \delta=(0,-1,0,-1,0,-1,0,-1)\in L_0.
\]

Here p_K(s)=c(delta,s)=0, so the exact result is

\[
 \boxed{V_K U_s V_K^{-1}=U_\delta U_s.}
\]

Thus K preserves s+L0, not the individual vector s. This is precisely
carrier-module equivalence, with a genuine neutral charge shift.
It does not erase the earlier fourth-power carry:
U_(Ks)^4=U_(4Ks), not the identity. Integer-charge tests include charges
of size one million, while the proof itself follows from the full
lattice identities.

This closes the particular algebraic ambiguity between the two
unoriented compiler choices at the carrier-module level. It is not yet
a symmetry on microscopic charged field operators, nor a selection of
an oriented complex structure or a preferred positive generator.

## 4. What the actual QWZ source says about a possible microscopic lift

There is a concrete candidate to investigate: reversing a charge by a
particle-hole transformation in the four channels with negative signs.
This identification with K is conditional, not already established.

For the unchanged v988/v1033 QWZ one-particle matrix H_r, set
X=I tensor sigma_x. Its on-site and directed-hopping matrices obey

\[
 -\sigma_x M^*\sigma_x=M,\quad
 -\sigma_x T_x^*\sigma_x=T_x,\quad
 -\sigma_x T_y^*\sigma_x=T_y.
\]

The seam factor i^r is conjugated. Hence the actual number-conserving
Hamiltonian under this particle-hole transformation has one-particle matrix

\[
 -(X^T H_r X)^T=H_{-r}.
\]

The hopping identities are checked symbolically. Full source matrices
at N=8 and N=16 verify the identity for every r=0,1,2,3.
For even r the transformed one-particle matrix is the same; for odd r,
||H_(-r)-H_r||=2 in these finite source checks.

A partial transformation in four of eight channels sends a uniform
holonomy (r,r,...,r) to alternating r,-r. Within the currently declared
uniform-flux family this closes only for r=0 or r=2. The neutral-current
numerics use r=1 and are not silently moved to a different sector.
Channel-dependent backgrounds or additional gauge identifications might
alter this conclusion, but have not been supplied by the source contract.

## 5. Exact zero modes make the r=0 preparation a real obligation

For the checked even circumferences the r=0 source has two exact p=0
edge zero modes. They are also explicit for the source formula: at p=0
the top and bottom profiles are supported at their respective boundary
rows, with orbital spinors chi_+ and chi_-. In their real orthonormal
top/bottom basis, X acts as diag(1,-1). The checker evaluates both
zero-mode residuals directly.

Within the **half-filled, number-conserving quasifree** zero-mode sector,
write its covariance as

\[
 C_0=\begin{pmatrix}a&z\\\bar z&1-a\end{pmatrix},\qquad X_0=\mathrm{diag}(1,-1).
\]

Particle-hole invariance requires
C_0=I-X_0 C_0^T X_0, hence a=1/2 and z is real.
Purity of this quasifree covariance is C_0^2=C_0, equivalently
det C_0=1/4-z^2=0. There are therefore two pure choices,

\[
 C_0^\pm={1\over2}\begin{pmatrix}1&\pm1\\\pm1&1\end{pmatrix}.
\]

Both correlate the two edges. The edge-diagonal invariant choice is I/2,
which is mixed rather than a pure Slater projector. This is a classification
in the stated covariance class, not a no-go for all states or preparations.
Outside the quasifree class, the covariance I/2 alone does not determine
the density matrix: a fixed-one-particle mixture and a quasifree mixture
on the full two-mode Fock space can share this covariance.
Neither pure choice, nor the mixed choice, has been inserted into the
source calculation. Filling by E<0 alone does not settle these zero modes.

The r=2 source has no zero modes at the checked even circumferences,
but choosing that sector alone is not a derivation of the full charged
transition and its adjoint between sectors.

## 6. Next gate and relation to simplicity

The useful simplification is now explicit: norm plus one character
recovers the marking; one elementary Weyl symmetry removes the
unoriented module-level doubling. No new geometry, arbitrary projector
or extra phase fitting was introduced.

The remaining choice is sharper: establish the microscopic field
implementation of K with the allowed holonomies and specify a
zero-mode/vacuum preparation selected by the parent construction.
That implementation must also preserve the oscillator/zero-mode
composition, domains, adjoint and neutral carry. It cannot be inferred
from the abstract lattice unitary alone.

See the complementary [normalization and determinant analysis](../neutral-current-limit/README.md).
These are requirements on a common construction, not independent toy
models whose positive checks can be added into a TOE-completion claim.

## Reproduction

    python3 experiments/theory-contracts/carrier-module-conjugation/checker.py --output experiments/theory-contracts/carrier-module-conjugation/validation.json
    python3 -m unittest discover -s experiments/theory-contracts/carrier-module-conjugation -p test_checker.py
    python3 -OO -m unittest discover -s experiments/theory-contracts/carrier-module-conjugation -p test_checker.py

Nine tests cover source-pin rejection, the reconstructed projector, full
integer charged transport and carry, energy preservation, source holonomy,
pure-versus-mixed zero-mode covariances, and the saved result's explicit
microscopic no-promotion boundary. See the [combined verification record](../neutral-current-limit/TEST_RESULTS.md).
