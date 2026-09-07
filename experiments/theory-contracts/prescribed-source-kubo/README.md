# Prescribed-source quantum Kubo closure for the zero-mean tensor target

## Result

For the already-constructed **free, zero-mean, finite-volume tensor Fock
target**, a prescribed conserved c-number source produces an exact coherent
displacement of the two TT oscillators at every nonzero momentum.  The Kubo
commutator has the retarded sign and normalization

\[
 \delta E_{\rm TT}(t,k)
 =-g\int_{t_0}^{t}{\sin r(t-t')\over r}\,
       r^2P_{\rm TT}(k)\tau(t',k)\,dt'.                 \tag{R1}
\]

This is only the radiative part of the sourced curvature.  The full sourced
curvature also contains the non-radiative affine c-number

\[
 E_{\rm aff}(t,k)=-{g\over 2r^2}s(k)\rho(t,k),\qquad
 F_{\rm aff}(t,k)=-{g\over 2r^2}s(k)\dot\rho(t,k),      \tag{R2}
\]

where (s=v-r^2t), (t=(1,1,1,0,0,0)^T), and (r=|\kappa|>0).
It obeys

\[
 BE_{\rm aff}=0,\qquad t^TE_{\rm aff}=g\rho,
 \qquad t^TF_{\rm aff}=g\dot\rho.                     \tag{R3}
\]

Thus the exact quantum answer is **TT Weyl/Kubo displacement plus an affine
scalar curvature lift**.  The TT commutator by itself is not the full sourced
curvature response.

This artifact is standalone.  It changes no repository paper, verification
module, suite, or ledger.

## Fixed conventions

At one nonzero staggered Fourier momentum, use the inherited real matrices

\[
 (Bh)_i=h_{ij}\kappa_j,\quad v=B^T\kappa,\quad
 s=v-r^2t,
\]

\[
 K_p=I-\frac12tt^T,\qquad
 K_q=r^2(I-tt^T)-2B^TB+tv^T+vt^T.                  \tag{1}
\]

The prescribed source is real after pairing (k) with (-k) and satisfies
the physical-position Fourier Ward equations

\[
 \dot\rho=-i\kappa^Tj,\qquad \dot j=-iB\tau.       \tag{2}
\]

The sourced Hamiltonian and affine constraints are

\[
 H_g=H_0+g\langle q,\tau\rangle,\qquad
 \Psi_0=-s^Tq+g\rho,\qquad
 \boldsymbol\Psi=iBp-gj.                           \tag{3}
\]

The local curvature pair and drive are

\[
 E=K_qq,\qquad F=K_qK_pp,\qquad
 \mathcal J=K_qK_p\tau+\frac12s\rho.              \tag{4}
\]

The inherited exact identities used below are

\[
 K_qB^T=0,\quad K_ps=B^T\kappa,\quad K_qt=s,
 \quad K_qK_pK_q=r^4P_{\rm TT}.                    \tag{5}
\]

All formulas below use a real orthonormal basis of the finite-dimensional
physical mode space after imposing Fourier reality and Bloch gluing.  In that
basis the common Fourier-volume factor is already part of the inner product,
so

\[
 [q_\alpha,p_\beta]=i\delta_{\alpha\beta},\qquad
 H_0=\frac12\sum_\alpha(p_\alpha^2+r_\alpha^2q_\alpha^2). \tag{6}
\]

There are (2(V-1)) real oscillators.  No finite-dimensional matrix
approximation to the CCR is used.

## Theorem: exact finite-volume Weyl and Kubo response

Let the homogeneous gravitational block be absent.  Let the paired source be
real, obey (2), and suppose on every compact time interval that its physical
TT force coefficients are integrable.  For pointwise affine formulas assume
(\rho\in C^2) and (j\in C^1); weaker distributional sources require a
separate domain statement.

Define

\[
 \tau_{\rm TT}=P_{\rm TT}\tau,
 \qquad \eta_\alpha(t)=\langle e_\alpha,\tau_{\rm TT}(t)\rangle, \tag{7}
\]

where (e_\alpha) are real normalized TT modes.  On the free Fock space, the
reduced prescribed-source Hamiltonian is

\[
 H_{\rm red}(t)=H_0+g\sum_\alpha\eta_\alpha(t)q_\alpha+c(t)I. \tag{8}
\]

The scalar (c(t)) may include the value of the source vertex on a chosen
affine constraint lift; it affects only the overall phase.  Then:

1. The interaction-picture propagator exists and is a phase times a Weyl
   displacement,

   \[
   U_I(t,t_0)=e^{i\phi(t,t_0)}\prod_\alpha D(\alpha_\alpha(t,t_0)), \tag{9}
   \]

   \[
   \alpha_\alpha(t,t_0)=
   -{ig\over\sqrt{2r_\alpha}}
   \int_{t_0}^{t}\eta_\alpha(u)e^{ir_\alpha u}\,du,             \tag{10}
   \]

   \[
   \phi={g^2\over2}\sum_\alpha\int_{t_0}^{t}du
        \int_{t_0}^{u}dv\,
        {\eta_\alpha(u)\eta_\alpha(v)\over r_\alpha}
        \sin r_\alpha(u-v),                                    \tag{11}
   \]

   up to the additional phase (-\int c).  Here
   (D(\alpha)=\exp(\alpha a^\dagger-\bar\alpha a)).

2. Starting from the zero-mean Fock vacuum at (t_0), the TT curvature mean
   is exactly (R1), not merely its first perturbative approximation.  The
   corresponding (F_{\rm TT}) response is its time derivative.

3. The full curvature operators on the affine sourced constraint surface are

   \[
   E_g=E_{{\rm TT},g}-{g\over2r^2}s\rho,\qquad
   F_g=F_{{\rm TT},g}-{g\over2r^2}s\dot\rho.        \tag{12}
   \]

   With constraint-compatible initial data they satisfy

   \[
   \ddot E_g+r^2E_g=-g\mathcal J,\qquad
   BE_g=0,\quad t^TE_g=g\rho,\quad t^TF_g=g\dot\rho. \tag{13}
   \]

4. The affine terms are c-numbers, so all connected fluctuation covariances
   and all commutators remain those of the free TT field.  The driven vacuum
   is coherent; it is not a new interacting vacuum.

### Proof

On TT modes, (5) gives (K_q=r^2I), (K_p=I), and therefore

\[
 E_\alpha=r_\alpha^2q_\alpha,\qquad
 F_\alpha=r_\alpha^2p_\alpha.                    \tag{14}
\]

Free evolution from (t') to (t), with (Delta=t-t'>0), is

\[
 q(t)=q(t')\cos(r\Delta)+{p(t')\over r}\sin(r\Delta).
\]

Using ([q,p]=i), in this order,

\[
 [q(t),q(t')]=-{i\over r}\sin(r\Delta),\qquad
 [E(t),q(t')]=-ir\sin(r\Delta).                  \tag{15}
\]

For the plus-sign perturbation (H_{\rm int}=+g\eta q), expansion of
(U_I^\dagger E_IU_I) gives

\[
 \delta\langle E(t)\rangle
 =-i\int_{t_0}^{t}
   \langle[E_I(t),H_{\rm int}(t')]\rangle_0dt'.  \tag{16}
\]

Substituting (15) yields

\[
 (-i)g\eta(t')[-ir\sin(r\Delta)]
 =-gr\sin(r\Delta)\eta(t'),                     \tag{17}
\]

which is precisely (R1).  Equivalently, in basis-independent tensor form the
free commutator is

\[
 [E(t),E(t')]=-iC{\sin(r\Delta)\over r},
 \qquad C=r^4P_{\rm TT},                         \tag{18}
\]

and (q_{\rm TT}=r^{-2}E_{\rm TT}); insertion in (16) again gives
(-g(\sin r\Delta/r)r^2P_{\rm TT}\tau).  This fixes both the sign and all
powers of (r).

For (9), write

\[
 q_{\alpha,I}(u)=
 {a_\alpha e^{-ir_\alpha u}+a_\alpha^\dagger e^{ir_\alpha u}
  \over\sqrt{2r_\alpha}}.                        \tag{19}
\]

The first Magnus term (-i\int H_{\rm int}) is exactly
(\sum_\alpha(\alpha_\alpha a_\alpha^\dagger-
\bar\alpha_\alpha a_\alpha)) with (10).  The commutator

\[
 [H_I(u),H_I(v)]
 =-{ig^2}\sum_\alpha {\eta_\alpha(u)\eta_\alpha(v)\over r_\alpha}
                    \sin r_\alpha(u-v)\,I        \tag{20}
\]

is central.  All nested commutators of depth at least three vanish, so Magnus
terminates and its second term is (i\phi), proving (9)--(11).  Since
(D(\alpha)^\dagger aD(\alpha)=a+\alpha), (10) gives

\[
 \langle q_\alpha(t)\rangle
 =-{g\over r_\alpha}\int_{t_0}^{t}
       \sin r_\alpha(t-u)\eta_\alpha(u)du.        \tag{21}
\]

Multiplication by (r_\alpha^2) proves (R1) exactly.  Higher Kubo terms for
a linear field mean vanish because the first commutator is a c-number.

It remains to restore the sourced scalar constraint.  The Ward equations
imply

\[
 \ddot\rho=-\kappa^TB\tau.                       \tag{22}
\]

The drive is transverse and its trace is

\[
 B\mathcal J=0,\qquad
 t^T\mathcal J=-(\ddot\rho+r^2\rho).             \tag{23}
\]

Every transverse symmetric tensor splits into its TT part and its transverse
trace direction (s=-r^2P).  Hence, exactly,

\[
 \boxed{\quad
 \mathcal J=r^2P_{\rm TT}\tau
       +{s\over2r^2}(\ddot\rho+r^2\rho).\quad}    \tag{24}
\]

The first term is the force generated by (8) on the reduced Fock space.  The
second cannot occur in a TT commutator.  But (R2) obeys

\[
 (\partial_t^2+r^2)E_{\rm aff}
 =-g{s\over2r^2}(\ddot\rho+r^2\rho),             \tag{25}
\]

as well as (R3).  Adding (21) and (25) proves (12)--(13).

An explicit unreduced affine lift is

\[
 q_{\rm aff}=-{g\over2r^2}t\rho,\qquad
 p_{\rm aff}={g\over r^2}t\dot\rho              \tag{26}
\]

for the longitudinal-current part.  Indeed (K_qq_{\rm aff}=E_{\rm aff}),
(-s^Tq_{\rm aff}+g\rho=0), (K_pp_{\rm aff}=\dot q_{\rm aff}), and
(iBp_{\rm aff}-gj_L=0), using
(j_L=i\kappa\dot\rho/r^2).  Transverse components of (j) fix gauge
directions but do not alter (E) or (F).

Finally, the affine additions commute with everything.  A Weyl displacement
changes means but not connected covariances or CCR, proving the last claim.
\(\square\)

## Initial data and the meaning of “retarded”

The formula with lower limit (t_0) has radiative initial conditions

\[
 \delta E_{\rm TT}(t_0)=\delta F_{\rm TT}(t_0)=0. \tag{27}
\]

The **full** compatible initial data are instead

\[
 E_g(t_0)=E_{\rm TT}(t_0)-{g s\rho(t_0)\over2r^2},\qquad
 F_g(t_0)=F_{\rm TT}(t_0)-{g s\dot\rho(t_0)\over2r^2}. \tag{28}
\]

Writing the lower limit as (-\infty) is justified only when the source has
vanishing past data (or when a separately stated switching prescription makes
the integrals converge).  If (\rho(t_0)=\dot\rho(t_0)=0), convolution of the
second term in (24) gives (R2) directly.  For nonzero past source data one must
retain (28); silently setting the full curvature to zero would violate the
constraints.

## A non-TT conserved source that rejects a TT-only answer

Take (\kappa=(0,0,r)) and any twice differentiable (\rho(t)).  Set

\[
 j=(0,0,i\dot\rho/r),\qquad
 \tau_{33}=-\ddot\rho/r^2,\qquad
 \tau_{ij}=0\ \text{otherwise}.                 \tag{29}
\]

Then both Ward equations hold.  Moreover

\[
 P_{\rm TT}\tau=0,\qquad
 P_{\rm TT}\mathcal J=0.                         \tag{30}
\]

Thus its Weyl displacement and TT Kubo response vanish.  Nevertheless

\[
 E_g=E_{\rm aff}={g\rho\over2}\,
       \operatorname{diag}(1,1,0),\qquad t^TE_g=g\rho, \tag{31}
\]

which is nonzero whenever (\rho\ne0).  This one source makes the boundary
unambiguous: reporting “zero response” from TT Kubo alone would erase the
sourced scalar curvature.

## Finite-volume versus infinite-volume implementability

At finite (L) there are finitely many positive-frequency oscillators.
For (\eta_\alpha\in L^1_{\rm loc}(dt)), every amplitude (10) is finite on a
compact time interval, (D(\alpha)) is unitary, and (9) gives the propagator
constructively.

After the spatial thermodynamic limit, a single Fock-space implementer exists
at time (t) exactly when the coherent displacement is a one-particle vector:

\[
 \boxed{\quad
 \|\alpha_t\|_1^2=
 {g^2\over2}\sum_{\lambda=1}^{2}
 \int_{\mathrm{BZ}_a}{d^3k\over(2\pi)^3\,r_a(k)}
 \left|\int_{t_0}^{t}
 \tau_{{\rm TT},\lambda}(u,k)e^{ir_a(k)u}du\right|^2<\infty.
 \quad}                                                        \tag{32}
\]

At fixed lattice spacing the Brillouin zone is compact.  A spatially
Schwartz, compact-time source is bounded near (k=0); in three dimensions the
infrared measure behaves as (r^2dr/r=r\,dr), so (32) is finite.  In the
continuum limit, spacetime Schwartz decay also controls the ultraviolet.

Condition (32), not conservation by itself, is the implementability
hypothesis.  Spatially non-decaying sources, singular infrared profiles, or
eternal forcing can violate it.  In that case the induced shift may still be
describable as an algebraic affine automorphism on a suitable local Weyl
algebra, but this artifact does **not** claim a unitary on the original global
Fock space.

The affine scalar term (R2) is not part of (\alpha_t): it is a prescribed
c-number translation of the observable/constraint embedding.  It therefore
does not repair or spoil (32).

## Executable certificate

Run:

```bash
python experiments/theory-contracts/prescribed-source-kubo/kubo_source_checker.py
```

The checker independently executes:

- the polynomial projector and source decomposition (24);
- transversality and sourced trace identities;
- the CCR commutator, Kubo sign, and Weyl displacement normalization;
- termination of the Magnus series at second order;
- the explicit non-TT conserved source (29), including its affine canonical
  lift and the failure of a TT-only result;
- a retarded Green-function regression with compatible initial data; and
- an explicit finite coherent-norm integral in three dimensions.

The expected summary is `exact 24/24; floating regressions 2/2`.

## Exact claim boundary

Closed here:

- prescribed c-number forcing of the existing nonzero-mode free TT Fock
  target;
- finite-volume unitary Weyl implementation;
- exact retarded Kubo response of the TT curvature mean;
- correct affine scalar completion of the full sourced curvature;
- explicit hypotheses for global infinite-volume implementability.

Not closed here:

- the omitted homogeneous (k=0) sector or coupling to total source energy;
- a source generated by dynamical quantum matter;
- an interacting constraint algebra beyond the prescribed c-number affine
  shifts;
- nonlinear gravity, backreaction, renormalized composite stress, or a
  microscopic TFPT parent;
- interacting Lorentz invariance or reconstruction of a complete sourced
  four-dimensional Riemann/Weyl tensor;
- any TOE milestone T1--T8;
- any RH statement.

**NO RH CLAIM.  T1--T8 remain open.**
