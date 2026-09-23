# Process, state and Clock tests of the compiler cone

9 September 2026. Source-scoped mathematical audit, not a physical
reconstruction or T1–T8 closure. The algebraic cone construction and its
integral-order qualifications are treated in [ORDER_PROOF](ORDER_PROOF.md);
the marked representation comparison is treated in
[MARKED_BRIDGE](MARKED_BRIDGE.md). The conclusions below distinguish an
available algebraic operation, a conditional quantum protocol, and an
operation actually selected by the existing source.

## 1. A whole-source Clock normalizer is excluded under the matched-center hypothesis

The unchanged sixteen-real-mode source has

\[
J=A_0=I_8\otimes\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad D=uJ+tB,\qquad [O,J]=[B,J]=[O,B]=0.
\]

Thus its Clock is complex-linear on the eight-complex-mode space defined
by \(J\). The exact source gives

\[
\chi_{O_8}(x)=(x-1)^5(x+1)(x^2+x+1),\qquad
\chi_{O_8^2}(x)=(x-1)^6(x^2+x+1).
\]

These matrices are constructed in the original
[source, lines 586–627](../../tfpt-discovery/seam_state_derivation_probe.py#L586)
and exposed, with source pins, by
[the Clock adapter](../clock-bilinear-response/checker.py#L28).
In that adapter, `O8=O[::2,::2]`, because \(O=O_8\otimes I_2\).

**Theorem.** There is no unital star embedding of \(M_2(\mathbb C)\) into
this \(M_8(\mathbb C)\), matching its internal central complex structure
to \(J\) or \(-J\), whose image is normalized by the actual \(O\) or \(O^2\).

Every such representation is unitarily equivalent to

\[
M_2(\mathbb C)\otimes I_4.
\]

A normalizing unitary must be \(V_2\otimes W_4\): its induced complex star
automorphism of \(M_2\) is inner, and removing that implementer leaves an
operator in the commutant \(I_2\otimes M_4\). If \(V_2\) has distinct
eigenvalues \(v_1,v_2\), the multiplicity of any eigenvalue \(\lambda\) is

\[
m_{W}(\lambda/v_1)+m_{W}(\lambda/v_2)\leq4,
\]

since these are distinct eigenspaces of the same four-dimensional \(W\).
If \(V_2\) is scalar, all multiplicities are even. The source polynomials
violate both alternatives: multiplicity five or six exceeds four, while
the nonreal eigenvalues are simple. This proves the stated exclusion,
independently of coordinate relabeling.

The hypotheses matter. This does not exclude nonunital corners, the
256-dimensional Fock space, larger representations, or a different
source-derived identification of the complex center. It is not a no-go
for every possible fundamental object.

## 2. One M₂ cannot carry both actual slow Clock frequencies

An autonomous unitary star-automorphism flow of \(M_2(\mathbb C)\) is

\[
X(t)=e^{-itH_2}Xe^{itH_2}.
\]

Its derivation has spectrum \(0,0,+\omega,-\omega\): at most one distinct
positive Bohr frequency. The actual primitive, number-neutral source
operators have two nonzero frequency magnitudes, for \(t\ne0\),

\[
(\sqrt3-1)|t|,\qquad(\sqrt3+1)|t|.
\]

Consequently both cannot be placed faithfully inside one closed \(M_2\)
algebra while intertwining their source dynamics. Their ratio \(2+\sqrt3\)
does not identify this Hamiltonian flow with a Pell boost. Operators in
modules outside \(M_2\), open dynamics and larger algebras are different
proposals, not excluded by this argument.

## 3. A constructive same-source alternative: the active M₃ corner

Let \(\eta=e^{-2\pi i/3}\) and define orthonormal vectors in the source
eight-mode space:

\[
f_0=(e_4-e_5)/\sqrt2,\qquad
f_+=(1,\eta,\eta^2,0,\ldots,0)^T/\sqrt3,\qquad
f_-=\overline{f_+}.
\]

Their span is invariant under the unchanged source Hamiltonian and Clock:

\[
h_{\rm active}=\operatorname{diag}(u-t,u+\sqrt3t,u-\sqrt3t),
\]
\[
O_{\rm active}=\operatorname{diag}(-1,\eta,\bar\eta),\qquad
O^2_{\rm active}=\operatorname{diag}(1,\bar\eta,\eta).
\]

Each corner \(\operatorname{span}(f_0,f_\pm)\) carries an \(M_2\) and one
slow frequency. Its identity is its corner projector, not \(I_8\).
Retaining both transfers \(E_{0+},E_{0-}\), their adjoints and composition
generates every matrix unit on the active three-mode space; in particular

\[
E_{+0}E_{0-}=E_{+-}.
\]

The resulting closed one-body algebra is \(M_3(\mathbb C)\), with a
nine-real-dimensional selfadjoint part. This is a concrete alternative
to identifying the single four-dimensional Lorentz cone with the entire
active observable algebra. It is not a universal uniqueness theorem for
\(M_3\).

At the source point \(u=1,t=1/8\), all three energies are positive.
Number-preserving transfers annihilate the empty ground state. The active
space is also orthogonal to the existing Boundary-generated Clock-fixed
space; its even primitive transfers commute with that Boundary algebra.
The corner construction therefore does not supply either the missing
access or an occupied preparation. See the source-specific
[Clock marking audit](../clock-marking-audit/README.md) and
[response calculation](../clock-bilinear-response/checker.py#L99).

## 4. A valid instrument and coherent protocol, with explicit extra premises

Write \(S=\alpha_1+\alpha_2+\alpha_3\), so \(S^2=3I\). Since

\[
T_j^\dagger T_j=3I+2\alpha_j,
\]

the following four effects form a positive, normalized instrument:

\[
K_j=T_j/\sqrt{13},\quad E_j=K_j^\dagger K_j
 ={3I+2\alpha_j\over13},\qquad
K_0=\sqrt{E_0},\quad E_0={4I-2S\over13}.
\]

Indeed \(4-2\sqrt3>0\) and \(\sum_{j=0}^3E_j=I\). These effects span the
four-real-dimensional Hermitian space: an informationally complete
qubit instrument. The normalization 13 is a convenient choice, not a
predicted constant. The family cycles \(K_1,K_2,K_3\) and fixes \(K_0\).
For the stipulated preparation \(\rho_0=I/2\),

\[
p_j=3/13,\quad p_0=4/13,\qquad
\rho_j={1\over2}(I+{2\over3}\alpha_j).
\]

Coherent addition needs more than forgetting the branch label. The
operator \(T=a+\sum_j\alpha_j+\sum_j a\alpha_j\) is a sum of seven
existing signed unitary monomials. A seven-path ancilla, equal-amplitude
preparation, controlled execution of those words and postselection onto
the same ancilla state realize the Kraus operator \(K=T/7\) exactly. On
\(I/2\), its success probability is \(1/7\). This is a conditional
linear-combination-of-unitaries protocol, not a process derived from the
closed source. Incoherently mixing word channels deletes the cross terms
responsible for the norm-37 calculation.

## 5. State selection and the three different notions of time

Family symmetry alone leaves the continuum of normalized states

\[
\rho_r={1\over2}(I+rS/\sqrt3),\qquad -1\leq r\leq1.
\]

They are faithful for \(|r|<1\). Thus symmetry does not uniquely select
\(I/2\), a temperature, or a readable source state. Trace normalization
also removes the radial degree of freedom of the four-dimensional cone;
retaining intensity requires an additional operational record.

For a successful filter \(K=A/c\), let

\[
p=\operatorname{Tr}(K\rho K^\dagger),\qquad
\rho'=K\rho K^\dagger/p,\qquad
\tau(\rho)=\tfrac12\log\det\rho.
\]

For faithful states and invertible \(A\),

\[
\tau(\rho')-\tau(\rho)
=\tfrac12\log\nu(A)-2\log c-\log p.
\]

The success probability is state-dependent. For \(T/7\) on \(I/2\), the
normalized determinant ratio is \(37/49\), not 37. Neither the raw norm
nor its logarithm is automatically the time of the actual source.

There is a sharper order test. Requiring

\[
AXA^\dagger\geq X\quad\hbox{for every }X\geq0
\]

forces \(A=\lambda I\), \(|\lambda|\geq1\). Apply the requirement to every
rank-one \(X=|v\rangle\langle v|\). Positivity of the difference forces
\(v\) to lie in the one-dimensional support spanned by \(Av\); hence every
line is an eigenline of \(A\), so \(A\) is scalar. This excludes interpreting
a nonscalar boost as a future-directed increment for every cone event.
It does not exclude cone-order-preserving transformations or a monotone
trajectory for a specifically selected state.

## 6. The finite cone algebra is not an invertible half-charge translator

In finite dimension an invertible \(F\) cannot satisfy
\([Q,F]=qF\) with \(q\ne0\): \(F^{-1}QF=Q+qI\) contradicts the trace.
In particular \(\zeta^{12}=I\) cannot be an exact half-charge translation;
its twelfth power would otherwise carry charge six. A nilpotent qubit
raising operator can have a half-charge commutator, but its square is
zero, unlike the nonzero integer carry of the two forward microscopic
transports.

An infinite or explicitly intersector representation can evade this
finite-dimensional obstruction. It must then match the distinct charge
operators, adjoints, energy and carry of the
[actual source transport](../microscopic-twist-charge-test/PROOF.md).
Finite spinor phases or equal dimension counts do not supply that map.

The next constructive gate is therefore a source-allowed preparation and
access protocol for the active Clock corners, preserving coherent
composition and the success record. The present analysis validates
conditional operations and isolates incompatible identifications; it
does not validate a unique universal physical object.
