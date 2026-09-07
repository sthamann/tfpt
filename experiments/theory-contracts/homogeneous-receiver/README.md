# Round 9 — homogeneous trace clock: conditional receiver and sharp global obstruction

## Verdict

There is a **regular conditional receiver for positive total energy on each
non-vacuum time-orientation branch**, but there is **no regular smooth
internal-clock deparameterization through the vacuum for this constraint
ansatz**, and the construction does not
receive nonzero total momentum.

The conditional construction restores only the homogeneous trace canonical
pair.  Its negative kinetic sign is then used in a postulated global Hamiltonian
constraint.  After fixing the trace coordinate as time and selecting one
orientation, the negative direction is absent from the reduced phase space and
the physical Hamiltonian is positive.  This is the standard mechanism suggested
by minisuperspace, and it needs no external clock.

However, the current TFPT target supplies neither the global constraint nor its
coupling to the complete rest energy.  More sharply, the intrinsic-time gauge
has zero Faddeev--Popov bracket at the vacuum, the two energy branches meet
there and the constraint description is irregular there. For the quadratic
free rest Hamiltonian, the reduced square root is not differentiable there;
this last claim does not hold for every smooth nonnegative function A.  No other smooth internal clock can
repair that point because the Hamiltonian vector field of the constraint itself
vanishes at the vacuum.  An added canonical clock with a momentum entering
linearly would evade this obstruction, but it would be an external assumption,
not a TFPT-derived repair.

This is an unpromoted theory contract in the repository research area. It
does not enter the verification suite or ledger, and makes no TOE or RH claim.

## Fixed input from the current target

At repository commit `a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`, the
homogeneous fibre has

\[
 K_q(0)=0,
 \qquad K_p(0)=I-\frac12tt^T,
 \qquad t=(1,1,1,0,0,0)^T.
\]

For canonical six-component variables \((q,p)\), define

\[
 Q=\frac13t^Tq,\qquad P=t^Tp,
 \qquad p_\perp=p-\frac P3t.
\]

Then \(\{Q,P\}=1\), \(t^Tp_\perp=0\), and exact matrix algebra gives

\[
 \frac12p^TK_pp
 =\frac12\lVert p_\perp\rVert^2-\frac1{12}P^2.       \tag{1}
\]

Thus the trace pair has one negative kinetic direction.  The other five
homogeneous directions have positive kinetic coefficient but no \(K_q\)
potential; the preceding construction removed the complete block rather than
calling it gauge.

The minimal candidate considered here restores only \((Q,P)\).  Keeping the
other five zero-frequency pairs is unnecessary for the energy-receiver test and
would add unstabilized moduli without changing any conclusion below.

## Additional assumptions — not outputs of the target

Let \(z\) denote every retained non-clock degree of freedom and let
\(A(z)\geq0\) be its complete positive Hamiltonian.  For the narrow matter
test one may take \(A=gE_m\), where \(g>0\) and
\(E_m=\sum_x\rho_x\) is the conserved Round-8 free-scalar energy.  The
candidate requires all of the following new assumptions:

1. restore the trace pair \((Q,P)\);
2. introduce a global lapse and postulate the constraint
   \[
      C=-\frac1{12}P^2+A(z)=0;                    \tag{2}
   \]
3. couple the complete rest energy through \(A\), not merely a prescribed
   source term;
4. choose one time-orientation branch;
5. restrict the compact periodic theory to vanishing total momentum.

No cosmological constant, trace potential, or external clock is assumed.
Equation (2) is motivated by the exact coefficient in (1), but it is **not
derived** from the present linear constraints.  Indeed, the existing scalar
constraint \(-s(k)^Tq(k)\) tends to zero with \(k\), while (2) is a new
quadratic global constraint.  The operation is therefore not a continuous
extension of the known nonzero-momentum constraint.

## Theorem 1 — regular branch reduction and positivity

Assume (2), \(\{Q,P\}=1\), and that \(A\) is independent of \(Q,P\).
On the open region \(A>0\), the constraint surface has two disjoint sheets

\[
 P_\sigma=\sigma\sqrt{12A},\qquad \sigma=\pm1.    \tag{3}
\]

Choose the intrinsic-time gauge

\[
 \chi=Q-\tau=0.
\]

Its exact gauge bracket is

\[
 \{\chi,C\}=-\frac P6,                            \tag{4}
\]

which is nonzero on either sheet.  Starting from the canonical action

\[
 S=\int d\lambda\,[P\dot Q+\theta_z-NC],
\]

substitution of \(Q=\tau\) and (3) gives

\[
 S_{\rm red}=\int d\tau\,[\theta_z-H_{\rm phys}^{(\sigma)}],
 \qquad H_{\rm phys}^{(\sigma)}=-P_\sigma
 =-\sigma\sqrt{12A}.                              \tag{5}
\]

Selecting the contracting-momentum sheet \(P<0\) (equivalently fixing the
orientation of \(Q\)) yields

\[
 \boxed{H_{\rm phys}=\sqrt{12A}\geq0}.            \tag{6}
\]

The trace pair has been eliminated, so no negative-energy or negative-norm
degree remains in the reduced variables.  In lapse \(N=1\),

\[
 \dot Q=-\frac P6,\qquad \dot Q^2=\frac A3.       \tag{7}
\]

Thus total positive energy is received as the magnitude of the homogeneous
trace velocity.  Gauge preservation fixes \(N=-6/P\), which is positive on
the selected \(P<0\) sheet.

If \(\widehat A\) is a nonnegative self-adjoint operator, the spectral
calculus makes

\[
 \widehat H_{\rm phys}=(12\widehat A)^{1/2}
\]

positive and self-adjoint on \(D(\widehat A^{1/2})\).  In the \(Q\)
representation the unreduced constraint is

\[
 \left(\partial_Q^2+12\widehat A\right)\Psi=0.    \tag{8}
\]

The selected sheet is exactly the positive-Hamiltonian first-order equation

\[
 i\partial_Q\Psi=\sqrt{12\widehat A}\,\Psi,
 \qquad \widehat P\Psi=-\sqrt{12\widehat A}\,\Psi. \tag{9}
\]

This proves conditional positivity and unitary \(Q\)-evolution.  It does not
derive \(\widehat A\), an ordering, a physical inner product for both sheets,
or the global constraint from TFPT.

## Theorem 2 — no smooth continuation of this reduction through vacuum

Let \(z_0\) be a smooth vacuum of the rest system with
\(A(z_0)=0\).  Because a smooth nonnegative function has vanishing derivative
at an interior minimum, \(dA(z_0)=0\).  At the full vacuum
\((P,z)=(0,z_0)\),

\[
 dC=-\frac P6dP+dA=0.                             \tag{10}
\]

Three consequences follow.

* The displayed constraint has zero differential and is not a regular
  constraint description at the vacuum. A singular level set is established
  explicitly for the quadratic oscillator below, not for every possible
  nonnegative \(A\).
* The intrinsic-time determinant (4) vanishes.  The lapse required by this
  gauge diverges as \(P\to0\).
* The Hamiltonian vector field \(X_C\) vanishes at the vacuum.  Hence for
  **every** smooth candidate internal clock \(T\),
  \(\{T,C\}=dT(X_C)=0\) there.  This rules out merely changing the smooth
  internal clock coordinate.

The failure is visible in the smallest exact counterexample.  Take one
positive canonical oscillator,

\[
 A(x,y)=\frac12(x^2+y^2).
\]

Then

\[
 C=-\frac1{12}P^2+\frac12(x^2+y^2)=0
\]

is a double cone with singular apex, while

\[
 H_{\rm phys}=\sqrt6\sqrt{x^2+y^2}
\]

has opposite one-sided derivatives \(\pm\sqrt6\) along \(y=0\).  It is
continuous but not differentiable at the vacuum, so its classical Hamiltonian
flow has no smooth extension there.  Choosing \(P\) itself as time also fails:
since (2) is independent of \(Q\), \(\{P,C\}=0\) everywhere.

At the operator level \((12\widehat A)^{1/2}\) can still be a perfectly good
self-adjoint operator including zero in its spectrum.  What fails at zero is
the claimed equivalence to a regular classical gauge reduction and a
nondegenerate positive-frequency split, not the spectral theorem.

The non-differentiability assertion is specific to a rest Hamiltonian with a
nonzero positive quadratic direction at its zero. For example `A=x^4` gives
the smooth reduced expression `sqrt(12)*x^2`, although `dC=0` and the
unreduced clock-gauge obstruction persist at zero. The checker explicitly
guards this distinction. No universal non-differentiability theorem for all
smooth nonnegative functions is claimed.

## Theorem 3 — total momentum remains an independent obstruction

On the periodic lattice the homogeneous vector constraints remain

\[
 \Psi_i(0)=-gJ_i,\qquad J_i=\sum_xj_i(x).          \tag{11}
\]

Restoring the scalar trace pair changes neither equation: \(B(0)=0\) for the
entire homogeneous metric block, so no homogeneous metric momentum appears in
(11).  The exact Round-8 Ward identity gives \(\dot J_i=0\).  Consequently the
combined conditional system is preserved on the sector

\[
 J_1=J_2=J_3=0,                                   \tag{12}
\]

but it does not accept a state with nonzero total momentum.

For the free scalar this preservation and the global constraint brackets can
also be seen without summing the local Ward identity.  Let \(S_i\) be the
periodic shift and

\[
 D_i^c=\frac{S_i-S_i^{-1}}{2a},\qquad
 J_i=-\pi^TD_i^c\phi,
\]

and write

\[
 E_m=\frac12\pi^T\pi+\frac12\phi^T\Omega^2\phi,
 \qquad
 \Omega^2=m^2I+\sum_i\frac{2I-S_i-S_i^{-1}}{a^2}.
\]

The \(D_i^c\) are antisymmetric and mutually commuting, and each commutes
with the symmetric \(\Omega^2\).  Direct canonical differentiation therefore
gives

\[
 \{E_m,J_i\}=0,\qquad \{J_i,J_j\}=0.             \tag{13}
\]

Thus, for \(A=gE_m\), \(\{C,J_i\}=0\); the postulated scalar constraint and
the three zero-momentum conditions are first class within this free global
algebra.  This is consistency of the restricted sector, not a mechanism that
solves (11) when \(J_i\ne0\).

Two exact periodic examples separate energy reception from momentum reception.

* A spatially constant scalar with constant \(\pi\) has \(E_m>0\) and
  \(J_i=0\).  Equation (3) gives a nonzero trace momentum and consistently
  receives its energy on either non-vacuum sheet.
* On a four-site periodic row with \(a=1,m=0\), choose
  \(\phi=(0,1,0,-1)\) and \(\pi=(1,0,-1,0)\).  The exact free energy is
  \(E_m=3\) and the centred total current is \(J=-2\).  With \(g=1\), the
  energy constraint has the real solutions \(P=\pm6\), but the vector
  constraint is \(-J=2\ne0\).  The trace receiver therefore does not solve
  the global momentum problem.

## Exact boundary of the result

The strongest supported statement is:

> Reintroducing the homogeneous trace pair and **postulating** the global
> constraint (2) yields a ghost-free, positive, self-adjoint reduced theory on
> either regular \(A>0\), fixed-orientation, zero-total-momentum sector.

The stronger desired statement is ruled out for this ansatz:

> It is not a smooth global TFPT-derived receiver covering the vacuum, and it
> is not a receiver for nonzero total momentum.

To promote the candidate, a future construction must derive the global lapse
constraint and its normalization from the TFPT parent, show how it joins the
nonzero-momentum constraints, provide a regular treatment of the vacuum, and
close the compact global momentum constraints.  A linear spectator-clock term
would only replace the problem by an unproved external degree of freedom.

## Executable certificate

Run only the standalone exact checker:

```text
python experiments/theory-contracts/homogeneous-receiver/homogeneous_receiver_checker.py
```

It uses SymPy exact integers and rationals.  It checks the matrix signature and
canonical decomposition, both constraint branches, the gauge bracket and
reduced sign, the Wheeler--DeWitt factorization, the vacuum singularity and
non-differentiability counterexample, and the two periodic matter examples.
Finite matrix entries in the self-adjointness smoke check are illustrative;
the general self-adjointness statement rests on spectral calculus, not on that
sample.

The repository re-run passes **52/52 exact checks**, including the additional
guard that `A=x^4` has a smooth square root even though the constraint
differential still vanishes at its vacuum. This prevents confusing the
general clock obstruction with the more specific quadratic-energy cusp.

## Primary context (not imported as proof)

The canonical role of lapse/shift constraints is the setting of the original
[ADM formulation](https://arxiv.org/abs/gr-qc/0405109).  Solving a Bianchi-I
Hamiltonian constraint for the momentum conjugate to a chosen intrinsic time,
and the resulting square-root Hamiltonian issue, is exhibited directly by
[Vakili and Sepangi](https://arxiv.org/abs/0709.2988).  A distinct vacuum
Bianchi-I quantization also illustrates that internal-time evolution can be
branch/sector dependent rather than a global crossing
[Martin-Benito, Mena Marugan, and Pawlowski](https://arxiv.org/abs/0804.3157).
These references motivate the question only; equations (1)--(13) and the
counterexamples above are self-contained consequences of the fixed target and
the explicitly marked new assumptions.
