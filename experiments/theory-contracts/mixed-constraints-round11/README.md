# Finite mixed first-/second-class constraint completion

Date: 2026-09-06. Bounded mathematical construction and independent algebra
checks. This combines the chosen positive reduced completion with the
canonical gravity dressing and the saddle auxiliary construction. It does
not construct a local first-class microscopic parent, restore homogeneous
gravity, select the completion from TFPT, or close any TOE gate.

## 1. Hypotheses and the result

Use the finite real Darboux chart of
`experiments/theory-contracts/constraint-dressing/README.md`, sections 7–10,
and the constant auxiliary Hessian of
`experiments/theory-contracts/local-positive-auxiliary/SECOND_CLASS.md`.
The original theorem below uses retained nonzero gravity modes. Any separate
zero-mode auxiliary extension is covered only after its Hessian has been
proved invertible; no homogeneous gravity variables are thereby supplied.

Write the original phase space as `(X,c,z)`, with
`{X^a,c_b}=delta^a_b` and independent canonical TT/matter variables `z`.
All other brackets among `X,c` vanish. Fix real `g` and suppose:

1. `H_f=H_0+H_m` and `{c_a,H_f}=A_a^b c_b`, with constant real `A`.
   Here `H_0` is gravity-only and `H_m` matter-only.
2. The matter currents `J_a(z)` commute with `X,c`. Put
   `S=-X^a J_a`, `D f={f,S}`, and `T_g=exp(gD)`. Thus `D c_a=J_a`.
3. The exact first Ward identity holds for the prescribed `V_1`. Equivalently
   `W=V_1-DH_f` satisfies `{c_a,W}=0` strongly. The equality is off-shell.
4. The auxiliary variables `y in R^d,p_y in R^d` are independent canonical
   pairs. `K=K^T` is a fixed invertible real matrix and
   `s(g,z)=g B tau(z)`, where the real source `tau` is matter-only. Hence
   `{c,s}=0` and `{X,s}=0`. For the local tensor construction, `B` inserts
   the six stress components into the multiplier slot of `y=(E,u,lambda)`.
5. The auxiliary inverse gives
   `-B^T K^{-1} B=P ell^{-1}` on retained modes, so
   `R=-s^T K^{-1}s/(2g^2)=tau^T P ell^{-1}tau/2`.
6. On the undressed section `X=c=0`, the free gravity TT block decouples
   from the gauge/constraint block and its first derivatives there vanish.
   Consequently `H_f` reduces to the positive free TT/matter Hamiltonian
   and `W` reduces to `sum_alpha Q_alpha tau_alpha`. This is the verified
   free-matrix property in the earlier contract, not a consequence of the
   Ward identity alone.

The mixed classical Hamiltonian is

\[
 H_{\mathrm{sa}}(g)=H_f+gW+\frac12y^TKy+y^Ts(g,z),\qquad
 \mathcal H_g=T_g H_{\mathrm{sa}}(g).
 \tag{1}
\]

Here `sa` labels seed plus auxiliaries, not self-adjointness. Extend `T_g`
trivially on both `y` and `p_y`. The resulting complete mixed classical
system has the original number of first-class gravity constraints, exactly
`2d` second-class auxiliary constraints, unchanged seed Dirac brackets,
fixed auxiliary preservation multipliers, and the positive physical
Hamiltonian of the chosen completion after both reductions.

For finite homogeneous quadratic matter currents the dressing is defined
for every real `g`: `X` is constant along its flow, matter follows a linear
ODE, and `c` integrates a finite quadratic function on every bounded
parameter interval. This is completeness in the *dressing parameter*, not
automatically physical-time completeness of an unreduced gauge choice.

## 2. The undressed mixed bracket is block diagonal

Let `H_b=H_f+gW` and order the auxiliary constraints as

\[
 \chi=(p_y,\Phi),\qquad \Phi=Ky+s,\qquad F_{ij}=\{s_i,s_j\}.
\]

Every `c_a` commutes strongly with every component of `chi`, while
`{c,H_sa}=Ac`. The auxiliary bracket and inverse are

\[
 \Delta=\begin{pmatrix}0&-K\\K&F\end{pmatrix},\qquad
 \Delta^{-1}=\begin{pmatrix}
 K^{-1}FK^{-1}&K^{-1}\\-K^{-1}&0
 \end{pmatrix}.
 \tag{2}
\]

Both inverse products are the identity for arbitrary antisymmetric `F`.
The full bracket of `(c,chi)` is `0` direct-sum `Delta`; its null directions
are precisely the first-class gravity constraints, not an auxiliary rank
defect. No commutativity assumption on the unprojected stresses is needed.

For **all** seed functions `f(X,c,z),h(X,c,z)`, not merely already reduced
physical observables, the brackets with `p_y` vanish. The lower-right zero
block of (2) therefore proves

\[
 \{f,h\}_{D,\chi}=\{f,h\}_{\mathrm{seed}}.
 \tag{3}
\]

The unique auxiliary graph and eliminated Hamiltonian are

\[
 y_*=-K^{-1}s,\quad p_y=0,\qquad
 H_{\mathrm{sr}}=H_b-\frac12s^TK^{-1}s=H_f+gW+g^2R.
 \tag{4}
\]

The canonical one-form restricts to the original seed one because
`p_y dy=0`, even when `y_*` depends on seed momenta. In particular the
first-class gravity brackets and propagation remain exactly those of
`H_sr`: `{c,H_sr}=Ac`. Each `d` auxiliary pairs are removed by exactly
`2d` second-class constraints. For the retained nonzero tensor block,
`d=28` per real Fourier component.

## 3. Stabilization, including arbitrary first-class multipliers

Take `H_T=H_sa+mu^T p_y+v^a c_a`, with `v` arbitrary. Primary preservation
gives `dot p_y=-Phi` modulo primary constraints. Write

\[
 a_i=\{s_i,H_b\},\qquad
 \dot\Phi\approx a+Fy+K\mu.
\]

The term involving `v^a{Phi,c_a}` is zero. If `v` is phase-space dependent,
the additional `{Phi,v^a}c_a` is weakly zero. Similarly derivatives of `mu`
multiply the primary constraints. Thus every auxiliary multiplier is fixed:

\[
 \mu_*=-K^{-1}(a+Fy_*),\qquad
 \{y_*,H_{\mathrm{sr}}\}=\mu_*.
 \tag{5}
\]

There are no tertiary conditions and no restrictions on the gravity
multipliers. The original first-class constraints obey
`dot c approx Ac`. For a source with momentum dependence, the `F y_*`
term must not be omitted. The actual unprojected scalar source has such
nonzero brackets, as checked in the preceding auxiliary experiment.

## 4. Canonical dressing commutes with the auxiliary reduction

Set

\[
 C=T_gc,\qquad s_g=T_gs,\qquad
 \chi_g=(p_y,\Phi_g),\quad \Phi_g=Ky+s_g.
 \tag{6}
\]

Because the extension of `T_g` is symplectic, it preserves every Poisson
bracket, including the mixed ones. Therefore

\[
 \{C_a,C_b\}=0,\quad \{C_a,\chi_g\}=0,\quad
 \{C,\mathcal H_g\}=AC.
 \tag{7}
\]

The second-class matrix is still (2), with `F_g=T_gF={s_g,s_g}`. Its
inverse still has a zero lower-right block; all seed functions continue
to have their original Dirac bracket. The stationary graph is
`y_{*,g}=-K^{-1}s_g=T_g y_*`, and

\[
 \left.\mathcal H_g\right|_{\chi_g=0}
 =T_g\left(H_f+gW+g^2R\right).
 \tag{8}
\]

The preservation multipliers are simply `T_g mu_*`, with the same weak
qualification for phase-space-dependent multipliers. Equivalently, for
arbitrary extended functions,
`{T_g f,T_g h}_{D,chi_g}=T_g{f,h}_{D,chi}`. This follows by substituting
the transformed brackets and inverse into the Dirac formula. It does
not require the transformation to preserve locality, which it does not.

The first-class gauge section also transports correctly. Since `T_g X=X`,
the dressed section is `X=0,C=0`. At `X=0`,

\[
 C=c+gJ,\qquad c=-gJ.
 \tag{9}
\]

It is incorrect to set the bare `c=0` in the dressed Hamiltonian. If the
phase-space flow is denoted by `phi_g`, so `T_g f=f composed with phi_g`,
then `phi_g` sends (9) to the seed section `X=c=0`: the dressed constraint
surface is the inverse image of the seed surface under that flow.
The physical matter and TT coordinates agree on these two corresponding
sections because their dressing flow is the identity at `X=0`.

Furthermore `{X,chi_g}=0`: the source flow depends on `X,z`, not on `c`.
Thus imposing the gauge conditions `X=0` gives the block bracket matrix

\[
 \{(X,C,\chi_g),(X,C,\chi_g)\}
 =\begin{pmatrix}0&I\\-I&0\end{pmatrix}\oplus\Delta_g.
 \tag{10}
\]

For functions only of the TT/matter coordinates, both reductions leave the
canonical bracket unchanged. The fully reduced Hamiltonian is exactly

\[
 H_{\mathrm{red},+}=H_m+\frac12\sum_\alpha
 \left[P_\alpha^2+r_\alpha^2
 \left(Q_\alpha+g\tau_\alpha/r_\alpha^2\right)^2\right]\ge0.
 \tag{11}
\]

Also `det Delta_g=(det K)^2`, independently of source brackets. Integrating
`delta(p_y)delta(Ky+s_g)sqrt(det Delta_g)` gives one. The gauge block has
unit determinant. On the slice `X=0`, `delta(C)=delta(c+gJ)` has unit
Jacobian in `c`. The fully reduced **finite classical** measure is therefore
the canonical TT/matter Liouville measure. No path-integral quantization
theorem follows from this identity.

## 5. Exact first vertex: before and after elimination are different

Equation (1) matches the prescribed original vertex only in the eliminated
original-variable Hamiltonian. Off the auxiliary constraint surface,

\[
 \mathcal H_0=H_f+\frac12y^TKy,\qquad
 [g]\mathcal H_g=DH_f+W+y^TB\tau
                 =V_1+\lambda^T\tau.
 \tag{12}
\]

There is a genuine additional first-order auxiliary–matter vertex. It is
zero on the `g=0` auxiliary graph `y=0`, and on the full graph `y_*=O(g)`
its contribution begins at order `g^2`. After elimination, (8) gives

\[
 [g]H_{\mathrm{match},+}=V_1,\qquad
 [g^2]H_{\mathrm{match},+}
   =DV_1-\frac12D^2H_f+R.
 \tag{13}
\]

Thus a demand for *literally no new first-order vertex on the extended
off-shell space* is not satisfied by this construction. Dropping
`lambda^T tau` would also drop the desired source in the auxiliary
secondary equations and lose the chosen `+R` completion.

Positivity belongs to the fully reduced Hamiltonian (11), not to the
unconstrained extended function (1). The tensor Hessian has six negative
directions per nonzero real component, and the original gravity gauge
sector is not assumed positive. Canonical conjugation preserves these
off-surface energy values; it cannot turn an indefinite extended function
into a nonnegative one. On the earlier TT-reduced constrained electric
form, positivity may be displayed as a square, but that is a restriction
to its constraints, not a positive unconstrained Hessian.

## 6. A rigorous finite quantum mixed-constraint statement

Assume now that every `J_a` and every component of the actual unprojected
`tau` is the Weyl quantization of a real homogeneous quadratic matter
polynomial. Let

\[
 \mathscr H_{\mathrm{kin}}
 =L^2(\mathbb R^M_X)\otimes L^2(\mathbb R^n_\phi)
   \otimes\mathscr H_{\mathrm{TT}}\otimes L^2(\mathbb R^d_y),
 \quad c_a=-i\partial_{X^a},\quad p_{y,i}=-i\partial_{y_i},
\]
\[
 (U_g\psi)(X)=\exp[-ig X^a\widehat J_a]\psi(X).
 \tag{14}
\]

Use the identity on the TT and auxiliary factors. The finite-quadratic
unitary theorem of the original constraint-dressing experiment makes
`U_g` a strongly continuous unitary group for all real `g`, preserving

\[
 \mathscr D=C_c^\infty\!\left(\mathbb R^M_X;
 \mathcal S(\mathbb R^n_\phi\times\mathbb R^{N_{TT}}_Q
                          \times\mathbb R^d_y)\right).
 \tag{15}
\]

These are smooth compactly supported **Schwartz-valued** functions, not
only separated finite sums. The metaplectic propagator and all its
`X` derivatives act continuously in Schwartz seminorms, uniformly on
compact `X,g` sets. The finite quadratic/metaplectic analytic input is
[Combescure–Robert, *Quadratic Quantum Hamiltonians revisited*, Theorem 4.1,
Remark 4.6 and section 5](https://arxiv.org/html/math-ph/0509027v1).

For each fixed component define the seed operator

\[
 \widehat\Phi_i=(Ky)_i+g(B\widehat\tau)_i.
\]

The two summands act on separate tensor factors and strongly commute;
their joint spectral sum is self-adjoint. The quadratic matter summand
is essentially self-adjoint on Schwartz space. Spectral cutoffs of the
two strongly commuting summands and their tensor-product cores show that
Schwartz space is a core for the joint sum. It follows that (15) is a
common invariant core for all seed `c_a,p_{y,i},Phi_i`.

Now define **by simultaneous unitary conjugation**

\[
 \widehat C_a=U_gc_aU_g^*,\quad
 \widehat\Phi_{g,i}=U_g\widehat\Phi_iU_g^*,\quad
 U_gp_{y,i}U_g^*=p_{y,i}.
 \tag{16}
\]

Every displayed operator is self-adjoint on its conjugated domain and
has the common invariant core (15). The `C_a` strongly commute with one
another, and each `C_a` strongly commutes with every `p_y` and every
`Phi_g`. This is a statement about commuting spectral projections:
before conjugation `c_a` acts on a separate factor, and simultaneous
unitary conjugation preserves that property. It is stronger than a
vanishing formal commutator. It does **not** say that the second-class
operators commute with one another.

On (15) their exact mixed algebra is

\[
 [\widehat C_a,\widehat C_b]=0,\qquad
 [\widehat C_a,p_{y,i}]=[\widehat C_a,\widehat\Phi_{g,i}]=0,
\]
\[
 [p_{y,i},\widehat\Phi_{g,j}]=-iK_{ji}I,\qquad
 [\widehat\Phi_{g,i},\widehat\Phi_{g,j}]
      =i\,U_g\operatorname{Op}_W(F_{ij})U_g^*.
 \tag{17}
\]

For quadratic source symbols the Weyl commutator equals `i` times their
Poisson bracket exactly. At fixed `X`, metaplectic covariance also
identifies the transformed source with its transformed quadratic symbol;
no derivatives in `c` occur in it. The source need not commute with the
undressed matter current `J`: simultaneous transformation in (16) is
essential to the mixed zero brackets.

These facts do not supply a quantum Dirac-bracket prescription for
arbitrary operator-valued observables. A formal inverse of an
operator-valued bracket matrix is not, by itself, a proof of a quantum
Jacobi identity, compatible domains, or equivalence of quantization
before and after reduction. In particular one cannot impose
`p_y psi=Phi_g psi=0` as simultaneous annihilation conditions: (17) and
invertibility of `K` exclude every nonzero common solution on a domain
where the commutators make sense.

## 7. Reduced quantization is complete; unreduced Hamiltonian domains are not

Classical reduction above canonically identifies the physical phase space
with the earlier TT/matter phase space. **Define** its quantization on
`L^2(R^(N_TT+n),dQ dphi)` by (11) with the operator-square prescription.
For the actual finite free-scalar source,
`tau_alpha=T_alpha(phi)` is a gradient-only quadratic multiplication
operator, because TT smearing cancels every common trace momentum/mass
term. Thus

\[
 \widehat H_{\mathrm{red},+}
 =-\tfrac12\Delta_{Q,\phi}+V_g(Q,\phi),\qquad V_g\ge0
\]

is the smooth nonnegative polynomial Schrödinger operator proved
essentially self-adjoint on `C_c^infinity` in the preceding
`local-positive-auxiliary/QUANTUM_DOMAIN.md`. Its closure has a Schwartz
operator core and agrees with the positive closed-form construction.
This gives unique unitary physical-time evolution for this explicitly
chosen reduced quantization at every fixed finite lattice and real `g`.
The earlier mass-dependent ground-state results are unchanged.

This definition need not invent an `L^2` kernel of the first-class
constraints either: `c_a` has continuous spectrum, and simultaneous
`c_a=0` means wavefunctions constant in `X`, not normalizable in
`L^2(R^M_X)`. Reduced quantization bypasses that distributional issue;
it does not assert a TFPT-derived rigging map or physical inner product.

What is **not** established is a self-adjoint realization of the full
off-constraint interacting `H_sa` in (1), or its transformed counterpart,
with all the prescribed off-shell vertices and the requisite invariant
domains. Its mixed gauge/auxiliary polynomial is not the nonnegative
Schrödinger operator just used. Algebraic stabilization and simultaneous
self-adjointness of the constraints do not imply self-adjointness of a
different, interacting Hamiltonian. Unitary conjugation would transport
an independently supplied self-adjoint seed Hamiltonian and all proved
domain relations; it cannot provide missing seed-domain hypotheses.
No no-go against every such realization is proved here.

For general momentum-dependent reduced stresses even the quartic ordering
must be specified: operator squares and Weyl quantization of classical
squares can differ by constants. The actual configuration-only TT source
avoids that particular ambiguity, but this does not justify blindly
Weyl-quantizing the full nonlinear dressed extended Hamiltonian.

## 8. Independent exact witness and scope

Run `python3 mixed_constraint_checker.py` from this directory with SymPy.
The final run passes **53/53 exact checks**, with no floating-point checks.
It imports no TFPT implementation. It uses one gauge pair, nonzero scalar
propagation `A=a`, two physical TT oscillator pairs, and one matter pair:

\[
 H_f=-aXc+\tfrac12c^2+\tfrac12(u^2+p^2)
       +\tfrac12\sum_{j=0}^1(Q_j^2+P_j^2),
 \quad J=u^2/2,\quad S=-Xu^2/2,
\]
\[
 \tau=(u^2/2,up),\quad W=Q^T\tau,\quad V_1=DH_f+W,
 \quad
 K=\begin{pmatrix}I_2&-I_2\\-I_2&0\end{pmatrix}.
\]

The exact canonical flow is polynomial:
`X -> X, c -> c+g u^2/2, u -> u, p -> p+gXu`; auxiliaries are unchanged.
This witness has a genuinely nonzero source bracket
`{tau_0,tau_1}=u^2`, so the nontrivial lower-right `F` block and its
preservation contribution are exercised. It is an algebra witness, not
the actual scalar stress or a substitute for the all-mode argument.

The `c^2/2` term supplies a non-vacuous mutant for the incorrect dressed
section `X=c=0`: it leaves an unwanted `g^2 J^2/2` contribution.
The checker tests canonical flow, Ward matching, the complete mixed
constraint matrix/inverse, multiplier preservation, exact elimination,
gauge fixing and physical symplectic reduction, the classical measure,
the additional off-shell auxiliary vertex, and the all-order reduced
positive squares. Differential-operator checks on an arbitrary smooth
function verify the unitary intertwining and the cancellation in the
mixed quantum commutator. Mutants which fail to dress the auxiliary
source, omit the `F y_*` multiplier term, use the wrong gauge section,
or erase the extra extended vertex are explicitly rejected.

The proof gives the finite mixed-class compatibility theorem. The witness
checks signs and non-vacuity, not continuum locality, microscopic origin,
relativistic causality, or a full interacting quantum gravity parent.
