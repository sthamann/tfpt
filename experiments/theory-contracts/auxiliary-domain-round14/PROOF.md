# Auxiliary momentum domains and an exact, declared quantum reduction

2026-09-06. Round14 NON-RH locally integrated research. No physical gate is promoted.

## Outcome and boundaries first

There is a constructive auxiliary-domain result, with a necessary price:

1. A parameter-dependent metaplectic unitary straightens the actual
   noncommuting quadratic source graph into canonical auxiliary coordinates.
2. It supplies a self-adjoint **completed total Hamiltonian**, an explicit
   domain and exact auxiliary Weyl propagation. Its classical restriction
   at `p_y=0` is the prescribed `H_sa`, and the original source is retained.
   Off that primary surface it contains additional, explicitly defined
   primary-momentum-dependent terms and modified secondary representatives.
3. A separately declared gauge-unfixing removes the secondary quadratic
   term. Abelian group averaging of the retained primary constraints then
   gives exactly the canonical seed Hilbert norm and its seed evolution.
   On the already reduced TT/matter seed, this is precisely the unique
   positive quantum Hamiltonian already proved, with no ordering constant.
4. Both constructions commute with simultaneous gravity dressing in the
   exact unitary sense specified below. They require no unproved covariant
   unreduced propagator.

This is **not** a proof that the unchanged off-shell `H_sa` has acquired
strong constraint covariance, nor a uniqueness theorem for its extensions.
It does not establish equivalence between an unspecified quantize-first
prescription and reduction-then-quantization. The gauge-unfixing prescription
changes the off-shell Hamiltonian and which real constraints are imposed.
The original real second-class constraints have no nonzero simultaneous
annihilation solution, even as distributions on their common polynomial
test space. The full gravitational physical Hamiltonian/inner product still
requires its independent first-class dynamical argument.

## 1. Actual finite input and the exact operator square

Use the retained real nonzero auxiliary space of
`local-positive-auxiliary/SECOND_CLASS.md`. It has `d=28(n-1)` coordinates
and constant invertible symmetric KKT Hessian `K`; its inertia is
`(22(n-1),6(n-1),0)`. Put

\[
 s=gB\tau,\qquad f=-K^{-1}s,\qquad
 H_{\rm sa}=H_b+\tfrac12y^TKy+y^Ts,
 \quad H_{\rm sr}=H_b-\tfrac12s^TK^{-1}s.
 \tag{1}
\]

There are two separately identified choices of seed:

- **Already reduced TT/matter:** `H_b=H_m+H_TT+g q_TT:tau`, and
  `H_sr=H_red,+`. Its quantum closure `A` is the unique positive operator
  in `local-positive-auxiliary/QUANTUM_DOMAIN.md`.
- **Full retained gravity seed:** `H_b=H_f+gW`, as in
  `mixed-constraints-round11`. Here choose a self-adjoint extension `A`
  of the actual Weyl expression `H_sr=H_f+gW+g^2R`. Existence does not
  require its unproved covariance: ordinary original-coordinate complex
  conjugation fixes this real symmetric polynomial expression. It pairs
  its two deficiency spaces, so a self-adjoint extension exists. The
  quartic `R` does not disturb the countable Hermite/Cayley construction
  used in Round12. Neither essential self-adjointness nor a canonical
  extension is asserted for this choice.

The actual unprojected stress is quadratic in matter phase space and can
have nonzero commutators. Nevertheless

\[
 -B^TK^{-1}B=P_{TT}\ell^{-1},\qquad
 \widehat f^{,T}K\widehat f
 =\widehat s^{,T}K^{-1}\widehat s
 =-g^2\sum_\alpha T_\alpha(\phi)^2/r_\alpha^2.
 \tag{2}
\]

These are ordered operator identities on Schwartz space. The constant
matrix contraction can be performed before any source products; it
annihilates the entire common kinetic/mass trace. The remaining TT sources
are configuration-only multiplication quadratics and commute. Hence the
operator square in (2) equals Weyl quantization of the classical square,
with no additional scalar correction. This is special to the actual TT
contraction, not a rule for arbitrary quadratic sources.

Thus the formal test-domain identity is

\[
 \widehat H_{\rm sa}
 =\widehat H_{\rm sr}
   +\tfrac12(y-\widehat f)^TK(y-\widehat f).
 \tag{3}
\]

It is not legitimate to call the entries `y-f` canonical: their mutual
commutators are the generally nonzero `[f_i,f_j]`.

## 2. A globally defined unitary straightening of the source graph

Fourier transform the auxiliaries, with

\[
 p_y=\eta,\qquad y=i\partial_\eta,
 \qquad {\cal H}_{\rm ext}=L^2(\mathbb R^d_\eta;{\cal H}_{\rm seed}).
\]

For each real `eta` the operator
`F(eta)=sum_i eta_i fhat_i` is the Weyl quantization of a real homogeneous
quadratic matter symbol. It is essentially self-adjoint and its finite
time propagator is metaplectic. Define

\[
 V(\eta)=e^{-iF(\eta)},\qquad
 (V\psi)(\eta)=V(\eta)\psi(\eta).
 \tag{4}
\]

No commutativity of the separate `f_i` is needed. The quadratic classical
matrix depends linearly on `eta`; its time-one exponential is smooth.
The metaplectic lift selected by this exponential is strongly continuous,
so (4) is a unitary on the full extended Hilbert space. It commutes with
every bounded function of `eta` and satisfies `V(0)=I`.

Define the self-adjoint operators and their domains by transport,

\[
 Y_i=Vy_iV^*,\qquad \eta_i=V\eta_iV^*.
 \tag{5}
\]

Their full Weyl representation is the canonical auxiliary representation
conjugated by `V`. In particular the `Y_i` strongly commute, and their
canonical Weyl relations with the `eta_i` hold exactly, not just formally.

On compact-`eta`, Schwartz-seed tests one may write

\[
 Y_i=y_i+\mathcal A_i(\eta),\qquad
 \mathcal A_i=iV\partial_iV^*
 =-\int_0^1 e^{-itF}\widehat f_i e^{itF}\,dt.
 \tag{6}
\]

The matrix-valued quadratic connection obeys

\[
 \mathcal A_i(0)=-\widehat f_i,\qquad
 \partial_j\mathcal A_i(0)=\tfrac i2[\widehat f_j,\widehat f_i],
 \quad
 i(\partial_i\mathcal A_j-\partial_j\mathcal A_i)
       +[\mathcal A_i,\mathcal A_j]=0.
 \tag{7}
\]

The last identity, or simply unitary conjugation of commuting `y_i`, proves
that the primary-dependent correction is exactly what cancels the original
nonzero source commutator. Replacing (6) by `y-f` would fail.

**Test-space limit:** `V` preserves
`D0=C_c^infinity(R^d_eta;S(seed))`, because metaplectic actions and parameter
derivatives are bounded in Schwartz seminorms on compact `eta` sets. Their
coefficients can grow exponentially at large `eta`; invariance of the full
joint Schwartz space is not asserted. On the full gravity seed the same
statement uses compact `X,eta` and Schwartz-valued physical tests after
the fixed linear Darboux transform.

The quadratic/metaplectic input is [Combescure–Robert, sections 3–5,
Theorem 4.1 and Remark 4.6](https://arxiv.org/html/math-ph/0509027v1).
The extension criterion used for the unreduced choice of `A` is
[Teschl, Theorems 2.27 and 2.29](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
These inputs do not assume that the interacting seed is itself quadratic.

## 3. A completed total Hamiltonian with an exact auxiliary domain

On the straightened tensor product let

\[
 H_\circ=A\otimes I+I\otimes\tfrac12y^TKy.
 \tag{8}
\]

The auxiliary quadratic is a real multiplication operator in the original
`y` representation. Its joint spectral sum with `A` is self-adjoint, with
domain given by square integrability of `E+q_K(y)`, not automatically just
the intersection of the two separate summand domains. Indefiniteness of
`K` causes no obstruction to this joint spectral construction.

Now declare

\[
 H_T^{\rm comp}=V H_\circ V^*,\qquad
 \operatorname{Dom}H_T^{\rm comp}=V\operatorname{Dom}H_\circ,
 \qquad \widetilde\Phi=KY.
 \tag{9}
\]

This is self-adjoint, and its unitary evolution has exact auxiliary
Heisenberg/Weyl propagation

\[
 Y(t)=Y,\qquad \eta(t)=\eta-tKY.
 \tag{10}
\]

Equivalently, on the invariant expression tests,
`[eta,H_T^comp]=-i K Y` and `[KY,H_T^comp]=0`. Equation (10) is the stronger
domain-independent statement about the corresponding bounded Weyl
operators. It does not claim that all classical scalar source operators
are separately constants of motion.

A core of `H_circle` can be obtained from finite sums of a core of `A`
and `C_c^infinity(eta)`, a core of the constant-coefficient auxiliary
quadratic in the `eta` representation. To verify this even for an
indefinite sum, first truncate both commuting spectral variables to bounded
boxes and then approximate in both individual graph norms. Transporting
this core gives a core of (9). If the chosen unreduced `A` is a proper
extension, its minimal Schwartz tests need not be a core; no such claim is
made. The explicit `D0` is nevertheless contained in the domain and has
the displayed expression, and `V D0=D0`.

### Exactly what agrees with the prescribed Hamiltonian

The formal expression in (9) is

\[
 V\widehat H_{\rm sr}V^*
   +\tfrac12(y+\mathcal A)^TK(y+\mathcal A).
 \tag{11}
\]

Its operator-valued auxiliary Weyl symbol at `eta=0` is precisely (3).
The derivative term coming from the symmetric `y,A` product vanishes:

\[
 \sum_{ij}K_{ij}\partial_i\mathcal A_j(0)
       =\tfrac i2\sum_{ij}K_{ij}[\widehat f_i,\widehat f_j]=0.
 \tag{12}
\]

At that point `V H_sr V*=H_sr`, and (2) removes the only possible quartic
product-ordering constant. Thus neither the actual unprojected source nor
the positive TT completion has been replaced. The secondary expression
also has `tildePhi|_(eta=0)=Ky+s` at this symbol level.

However, (11) is **not the unchanged operator H_sa on its full Schwartz
domain**. Its differences are smooth primary-momentum-dependent terms,
including the finite connection and conjugation corrections. In local
auxiliary Weyl-symbol coordinates those differences vanish at `eta=0`.
Hadamard's formula writes them as `sum_i eta_i mu_i(y,eta,z)`; symmetric
Weyl ordering of each product is the anticommutator with `eta_i/2`.
These define one allowed completed multiplier prescription, with higher
primary-dependent terms. They need not coincide with any independently
chosen quantization of the old off-surface multiplier formula.

The corresponding classical canonical transformation is the **negative
unit-time pullback** `a composed with Phi_F^-1` for the flow generated by
`F=sum eta_i f_i`. This sign agrees with metaplectic covariance at fixed
`eta` on the seed variables. An exact full-space Egorov identity for every
symbol is not asserted: `F` is cubic on the enlarged space, and (9), not
blind Weyl quantization of its classical pullback, specifies the ordering.
Its matter flow is linear at fixed `eta`, the `eta` are
constant, and the auxiliary shifts are finite integrals of quadratics;
it is global at finite parameters. At `eta=0`, it leaves the seed point
fixed and sends `y` to `y-f`, so it maps the original stationary graph to
the straight zero graph. Its completed Hamiltonian agrees with (1) on
the primary surface. On the common constraint surface the physical
evolution and the forced multiplier are therefore those of the original
classical second-class reduction. Off that surface the prescription is
an explicit choice, not a new uniqueness result.

## 4. A rigorous physical norm requires a declared reduction prescription

The real second-class conditions cannot all annihilate a state. Already

\[
 [\eta_i,\widehat\Phi_j]=-iK_{ji}I
 \tag{13}
\]

and invertibility of `K` imply that a simultaneous solution is zero.
This is true on compatible operator domains and also for Schwartz
distributions, since the original operators have polynomial coefficients
and their commutator identity extends to the dual test space. Unitary
transport gives the corresponding statement for the new canonical pair.
There is no common `L2` kernel rescued by (9).

One complete alternative is the following **explicit gauge-unfixing**:
retain only the commuting first-class primaries `eta=0`, regard `Y=0` as
the discarded gauge-fixing partners, and replace (9) by

\[
H_{GU}=V(A\otimes I)V^*
       =H_T^{\rm comp}-\tfrac12Y^TKY.
 \tag{14}
\]

The second equality is a difference in the common transported joint spectral
calculus, or equivalently the closure of the difference on the natural
intersection domain. A naive unbounded-operator subtraction need not have
the full domain of the first, defining expression in (14).

The subtraction is a real change of the off-shell Hamiltonian by a
secondary-constraint quadratic. Classically it agrees with the original
second-class dynamics after restriction. At the quantum level (14) is a
declared prescription, not a consequence of setting noncommuting operators
to zero in an associative operator quotient.

The operator (14) is self-adjoint on the exact transported domain,
strongly commutes with all `eta_i`, and is unitarily equivalent to the
constant seed family `A`. Let the dense averaging tests be

\[
 \psi(\eta)=V(\eta)\sum_{j=1}^N u_j(\eta)v_j,
 \quad u_j\in C_c^\infty(\mathbb R^d),\quad v_j\in{\cal H}_{seed}.
\]

Average the translation group `exp(i t.eta)` using `d^dt/(2pi)^d`.
Fourier evaluation gives the positive form

\[
 \eta_{aux}(\psi,\varphi)
   =\langle\psi(0),\varphi(0)\rangle_{{\cal H}_{seed}}.
 \tag{15}
\]

This is an ordinary absolutely convergent matrix-element group average:
after the pointwise unitary cancellation, repeated integration by parts
of the compactly supported scalar coefficient gives integrable decay in
`t`. The quotient completes to the entire seed Hilbert space, since any
`v` is reached with `u(0)=1`. No source-dependent measure determinant or
extra ordering constant appears. The group-zero kernel in kinematic
`L2(eta)` itself is zero and is not used as the physical space.

Moreover `exp(-it H_GU)` preserves this test class and descends under (15)
to exactly `exp(-itA)`, because `V(0)=I`. This proves domains, the physical
inner product and physical-time unitarity for this auxiliary-reduction
prescription. For the already reduced seed it is the original positive
`H_red,+`, including the massless uniform scalar and its no-ground-state
boundary. For the full retained seed it is the chosen extension `A`, not
an automatically covariant first-class physical Hamiltonian.

The group-averaging convention and its auxiliary-structure dependence are
consistent with [Marolf, Refined Algebraic Quantization](https://arxiv.org/abs/gr-qc/9508015).
The concrete norm and evolution here follow directly from (15), not from
an imported general equivalence theorem for second-class quantization.

## 5. Simultaneous gravity dressing and the remaining open problem

On the full seed let `U_g(X)=exp(-ig X^a J_a)` be the previously established
quadratic dressing. It acts trivially on auxiliaries and commutes with
`eta,y`. Before this dressing, `V` acts only on matter and auxiliaries,
so it strongly commutes with every undressed `c_a`.

Use the single combined unitary `W=U_g V`. Then

\[
 C_a=Wc_aW^*=U_gc_aU_g^*,\quad
 Y_g=WyW^*,\quad \eta=W\eta W^*,
\]
\[
 H_{T,g}^{comp}=W H_\circ W^*,\qquad
 H_{GU,g}=W(A\otimes I)W^*.
 \tag{16}
\]

All stated self-adjoint domains are transported by this same unitary.
The `C_a` strongly commute with the auxiliary canonical constraints, as
they did before transport. The auxiliary Weyl propagation of the completed
total Hamiltonian and the Abelian primary averaging of the gauge-unfixed
Hamiltonian remain exact. Auxiliary reduction identifies the latter with
`U_g A U_g^*`; thus dressing and this declared auxiliary quantization
commute in the exact Hilbert-space/domain sense.

These facts do **not** establish strong propagation of `C_a` under that
Hamiltonian when it was not known for `c_a` under `A`. In particular an
arbitrary self-adjoint eliminated seed extension cannot be advertised as
solving Round13's covariant-domain limit problem. Nor can the unchanged
Round12 `H_sa` be replaced by (9) without reporting its additional
primary-dependent terms. There is no proven quantize-first equivalence
for the original full real second-class operator list.

## 6. Reproduction and evidence typing

`auxiliary_domain_check.py` is an exact finite checker. It reconstructs
the actual `L=2,(pi,pi,0)` real boundary KKT Hessian and actual source,
checks the nonzero full source bracket, computes the TT contraction of
the full Weyl-square correction, and verifies the flat connection's
zeroth-order cancellation. An exact solvable configuration-only model
checks the complete unitary shear, its required `p_y` terms, auxiliary
propagation and the gauge-unfixing subtraction on arbitrary functions.
The model is labelled MODEL; it is not passed off as the unprojected
noncommuting actual source. No finite CCR matrices or spectral cutoff
are used as evidence for an infinite-dimensional domain statement.

The analytic construction above supplies the domain and averaging proofs.
No positive microscopic parent, first-class gravitational covariance,
homogeneous gravity receiver, locality, continuum limit, TFPT inner
product selection, or TOE gate follows from it.
