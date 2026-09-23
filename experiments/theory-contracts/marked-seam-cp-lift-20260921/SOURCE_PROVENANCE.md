# q*-marked compiler versus seam transfer: source audit

Date: 2026-09-21  
Scope: bounded provenance/novelty audit; no new physical model and no TFPT source edits.

## Verdict

No such combination was found in the checked repository sources or the current theory-graph search scope: the actual q*-marked Pauli/Clifford process decomposition

\[
M_4(\mathbb C)=P_0\oplus P_5\oplus P_{10}
\]

with the seam one-leg eigenvalues \(1,2/3,1/3\) (or their six-leg powers) as one completely positive operator transfer. The two sides exist separately:

1. The q*-marked source gives exact word orbits \(O_5,O_{10}\), a Pauli-diagonal operator channel class, exact Choi eigenvalues, and the complete two-rate CPTP semigroup cone in that class.
2. The seam clock gives a separate three-level cusp/Z2-pair transfer with one-leg spectrum \(1,2/3,1/3\) and six-leg spectrum \(1,(2/3)^6,(1/3)^6\).
3. No checked prior source supplies an intertwiner that assigns the two cusp modes to the q*-word orbits. Existing work explicitly keeps the physical execution law and the raw-seam operator identity open.

Under the **additional, conditional orbit-scalar identification** that the two seam modes are exactly the scalar eigenmodes on \(P_5,P_{10}\), complete positivity selects one discrete one-leg assignment:

\[
T_1=P_0+\frac13P_5+\frac23P_{10}.
\]

It is the random-unitary Pauli channel

\[
T_1=\frac7{12}\operatorname{id}
    +\frac1{12}\sum_{v\in O_5}\operatorname{Ad}_{P_v},
\]

with zero \(O_{10}\)-jump weight. Its sixth power has exactly

\[
T_1^6=P_0+(1/3)^6P_5+(2/3)^6P_{10}.
\]

This exact \(7/12,1/12,0\) channel was not found in the checked repository or theory-graph searches. Within that bounded search, it is a new algebraic composition of old ingredients, conditional on the new orbit assignment. The audit also identifies an explicit conditional trine readout on the original fixed-plane words; it intertwines the channel with the original three-state transfer matrix exactly. This strengthens the result from a spectral match to an operator-system readout, but it does not derive a physical charged-field transfer.

Neither assignment is continuously embeddable in the existing q*-marked orbit-scalar CPTP semigroup class. Thus the conditional result is a **discrete six-leg CP channel**, not a derived continuous Lindblad evolution.

## Existing marked operator theorem

The original marked source defines

\[
q_*(v)=\operatorname{wt}(\iota(v))/2\pmod 2,
\quad O_5=\{q_*=0\}\setminus\{0\},\quad O_{10}=\{q_*=1\}.
\]

The exact checker constructs rank-\(1,5,10\) process projectors and the generator

\[
L=\gamma_5\sum_{v\in O_5}(\operatorname{Ad}_{P_v}-I)
 +\gamma_{10}\sum_{v\in O_{10}}(\operatorname{Ad}_{P_v}-I),
\quad \gamma_5,\gamma_{10}\ge0.
\]

Its decay rates are

\[
r_5=8(\gamma_5+\gamma_{10}),\qquad
r_{10}=4\gamma_5+12\gamma_{10}.
\]

For an orbit-scalar map

\[
T=P_0+aP_5+bP_{10},
\]

the normalized Choi eigenvalues, equivalently the per-word Pauli mixture weights, are

\[
p_0=\frac{1+5a+10b}{16},\quad
p_5=\frac{1-3a+2b}{16},\quad
p_{10}=\frac{1+a-2b}{16}.
\]

Complete positivity is exactly \(p_0,p_5,p_{10}\ge0\). For a norm-continuous orbit-scalar semigroup with \(a(t)=e^{-r_5t}\), \(b(t)=e^{-r_{10}t}\), infinitesimal CP is equivalent to

\[
\frac12r_5\le r_{10}\le\frac32r_5.
\]

Original sources:

- `experiments/theory-contracts/compiler-kernel-foundation-20260914/redteam/TWO_RATE_ADDENDUM.md:15-59,95-119`
- `experiments/theory-contracts/compiler-kernel-foundation-20260914/redteam/two_rate.py:45-80,127-169`
- The source itself says the family is not physically selected: `TWO_RATE_ADDENDUM.md:3-5,91-93` and `two_rate.py:168-169`.

## Existing seam one-leg and six-leg theorem

The seam-side source reads the frozen three-level spectrum as

\[
\lambda_n=(1-n/3)^6,\qquad n=0,1,2,
\]

and explicitly marks the semiclassical derivation as still open. The original three-state one-leg root is

\[
B=\frac1{18}
\begin{pmatrix}
13&1&4\\
1&13&4\\
4&4&10
\end{pmatrix}
=\frac J3+\frac23P_2+\frac13P_3,
\]

where \(J\) is the all-ones matrix, \(P_2\) projects onto \((1,-1,0)\), and \(P_3\) projects onto \((1,1,-2)\). Its sixth power is the actual v221 transfer bit-exactly. Separately, v486 realizes the same two decaying eigenvalues with the symmetric Z2-pair survival block

\[
B_{\rm pair}=\begin{pmatrix}1/2&1/6\\1/6&1/2\end{pmatrix},
\quad \operatorname{spec}B_{\rm pair}=\{2/3,1/3\},
\]

so its two non-unit eigenvalues are \(2/3,1/3\). This block must not be confused with the full \(3\times3\) matrix \(B\), which is stochastic and has spectrum \(\{1,2/3,1/3\}\). These are classical transfers, not by themselves the q*-marked Pauli channel.

Original sources:

- `verification/v124_resummed_clock.py:1-18,27-35` — exact frozen-spectrum identity; semiclassical derivation open.
- `verification/v486_transfer_full_rule.py:1-43,86-127` — spectrum-to-rule reconstruction; direction is explicitly spectrum \(\to\) rates.
- `verification/v814_k5_sixstep_transport.py:1-40,55-71` — the full \(3\times3\) root and bit-exact identity \(B^6=T_{v221}\).
- `verification/v221_seam_qecc.py:1-24,39-62` — the actual three-state six-step transfer in the fixed deviation basis.
- `verification/v977_transfer_unistochastic_wilson.py:93,278-283,339-349` — exact \(B\) and its projector decomposition.
- `experiments/theory-contracts/lazy01_clock_rung_forcing.py:10-38,103-126` — even/odd Z2-pair assignment in the three-level walk.
- `experiments/theory-contracts/born01_deck_envariance.py:27-35,150-189` — per-substep 2:1 counting interpretation and sixfold composition.

The stronger seam/operator bridge is still conditional. `verification/v162_seam_transport_identification.py:1-37,140-155` requires the seam RG generator to be admissible and mu4-equivariant and retains the raw physical identification as an input. The authoritative ledger keeps `QGEO.KERNEL.01` open: raw seam Calderon operator equality is not established merely by the spectral list.

## New exact conditional calculation

There are two possible assignments of the one-leg seam values to \((a,b)=(\lambda_5,\lambda_{10})\).

| Assignment | \((a,b)\) | \((p_0,p_5,p_{10})\) | One-leg CP? |
|---|---:|---:|---:|
| direct | \((2/3,1/3)\) | \((23/48,-1/48,1/16)\) | no |
| swapped | \((1/3,2/3)\) | \((7/12,1/12,0)\) | yes |

Therefore CP alone, **after** assuming an orbit-scalar common transfer, selects

\[
O_5\longleftrightarrow 1/3,\qquad O_{10}\longleftrightarrow 2/3.
\]

If only the six-leg macro spectrum is imposed, both assignments are CP:

| Macro assignment | \((a,b)\) | \((p_0,p_5,p_{10})\) |
|---|---:|---:|
| direct | \((64/729,1/729)\) | \((353/3888,539/11664,791/11664)\) |
| swapped | \((1/729,64/729)\) | \((229/1944,427/5832,301/5832)\) |

Hence the selector comes specifically from requiring a CP **one-leg sixth root on the same q*-orbit projectors**, not from macro-time CP alone.

## New exact fixed-plane trine readout

The compiler bridge already fixes the plane

\[
\{0,A_{\rm BIT},F_{\rm SIG},A_{\rm BIT}+F_{\rm SIG}\},
\qquad q(A_{\rm BIT})=1,\quad q(F_{\rm SIG})=0,
\]

and its inherited bilinear form has \(h_b(A_{\rm BIT},F_{\rm SIG})=1\). With the source phase convention

\[
A=i\,\mathrm{word}(A_{\rm BIT}),\qquad F=\mathrm{word}(F_{\rm SIG}),
\]

the two matrices are Hermitian involutions and anticommute. The selected Pauli channel acts as

\[
\Phi(A)=\frac23 A,\qquad \Phi(F)=\frac13 F.
\]

Define three effects

\[
E_1=\frac{I+(\sqrt3/2)A+(1/2)F}{3},\qquad
E_2=\frac{I-(\sqrt3/2)A+(1/2)F}{3},\qquad
E_3=\frac{I-F}{3}.
\]

Because \(A^2=F^2=I\) and \(AF=-FA\), each \(E_i\) has eigenvalues \(0,2/3\), the effects are positive, and \(E_1+E_2+E_3=I\). Direct substitution gives the full matrix identity

\[
\Phi(E_i)=\sum_j B_{ij}E_j,
\qquad
B=\frac1{18}
\begin{pmatrix}
13&1&4\\
1&13&4\\
4&4&10
\end{pmatrix},
\]

and hence \(\Phi^6\) induces the actual v221 transfer \(B^6\). This is stronger than matching eigenvalue lists: it is an explicit positive operator-system readout using the original fixed-plane words.

The checked corpus and theory-graph searches did not locate this particular trine construction or this exact intertwining identity. That is a bounded novelty finding, not an exhaustive literature claim. Its limitations are algebraically visible:

- \(E_i^2=(2/3)E_i\), so the map from the three classical labels to effects is not multiplicative and is not a \(*\)-algebra embedding.
- For a state \(\rho\), \(p_i=\operatorname{tr}(\rho E_i)\le2/3\), and the attainable probability vectors satisfy \(\sum_i(p_i-1/3)^2\le1/6\). The image is a proper disk in the classical simplex, not the full simplex.
- The source fixes the plane and its Clifford relations, but it does not select this POVM, its sharpness \(2/3\), an instrument realizing it, or a record/update rule. Those remain extra readout choices.

Indeed, the same one-step identity holds for the family

\[
E_1(u,v)=\frac{I+uA+vF}{3},\quad
E_2(u,v)=\frac{I-uA+vF}{3},\quad
E_3(u,v)=\frac{I-2vF}{3},
\]

whenever \(u^2+v^2\le1\) and \(|2v|\le1\), which are exactly the positivity bounds. The displayed trine is the maximal equal-sharpness choice \((u,v)=(\sqrt3/2,1/2)\); the transfer identity does not select it.

Original fixed-plane sources:

- `experiments/theory-contracts/compiler-clifford-bridge/checker.py:66-96,120-137` — q-selection, fixed plane, cocycle word matrices, and split Clifford algebra.
- `experiments/theory-contracts/compiler-clifford-bridge/README.md:93-106` — the same algebra and the explicit warning that it is not automatically a physical charged-seam assignment.

## Continuous embedding verdict

For the direct assignment,

\[
\frac{r_{10}}{r_5}=\frac{\log 3}{\log(3/2)}>\frac32.
\]

For the swapped assignment,

\[
\frac{r_{10}}{r_5}=\frac{\log(3/2)}{\log 3}<\frac12.
\]

Both violate the exact marked-semigroup cone. Multiplying both rates by six leaves the ratio unchanged, so the same obstruction applies to the macro eigenvalues.

For the CP-swapped discrete root, the forced positive square root already fails CP:

\[
a_{1/2}=1/\sqrt3,\qquad b_{1/2}=\sqrt{2/3},
\]

\[
p_{10}(T_{1/2})=
\frac{1+1/\sqrt3-2\sqrt{2/3}}{16}<0.
\]

This rules out a norm-continuous CPTP embedding that remains orbit-scalar on the same \(P_0,P_5,P_{10}\) decomposition. It does not rule out every larger non-diagonal dilation or a transfer that abandons the marked covariance at intermediate times.

## Why this is not yet a charged-source derivation

The extra premise is load-bearing:

> The seam Z2-pair eigenmodes are the same operator modes as the q*-marked \(O_5,O_{10}\) process sectors, with the same one-leg composition law.

No current source proves it. The compiler bridge explicitly warns that its quadratic/cocycle representative is not automatically the full charged seam cocycle or a physical operator assignment (`experiments/theory-contracts/compiler-clifford-bridge/README.md:93-97`). It also warns that equal dimensions are not identification maps (`README.md:40-43`). The earlier common-source process audit found that the uniform original root instrument is depolarizing and cannot injectively carry the nonzero \(2/3,1/3\) seam modes (`compiler-process-reconstruction-20260918/checker.py:87-114`; `README.md:3-15`).

The five \(\Gamma_j\) in the marked Pauli proof are the five Hermitian q*=0 Pauli words. They are not the unrelated lattice/current `Gamma` objects in later source contracts. No SU(4), six-environment-leg, electric-charge, or physical-spin identification follows from the counts 5, 10, or 6.

There is also no charged-time law hidden in the fixed-plane CAR notation. If

\[
c=\frac{F+iA}{2},
\]

then \(c\) satisfies the one-mode CAR, but

\[
\Phi(c)=\frac12c-\frac16c^\dagger,
\qquad
\Phi(c)^2=-\frac1{12}I.
\]

Thus \(\Phi\) does not preserve the CAR product and is not a \(*\)-automorphism or a derived physical charged evolution. A reduced CP channel may admit a larger CAR dilation, but neither that dilation nor its P1 source selection is supplied here.

The accompanying independent checker (`work/marked_source_transfer_20260921/checker.py`) imports the pinned original v814/v221 transfer and the original bridge labels \(A_{\rm BIT},F_{\rm SIG}\). It passes 56 exact conditions, including the Choi weights, random-unitary identity, one- and six-step readout intertwiners, CAR mixing, unique maximally mixed fixed state, and the non-unique \((u,v)\) readout family. Four targeted mutants fail as intended: reverse assignment CP, continuous marked interpolation CP, projection-valued readout, and charge preservation. This validates the conditional algebra; its trace correlations remain formal channel iterates, not a process tensor or full multitime insertion functional.

## Novelty and decisive next test

**Prior:** exact q*-marked CPTP semigroup family and CP cone; exact separate seam one-leg/six-leg rule; fixed-plane Clifford words; no located common operator-system readout.  
**New conditional result in the checked scope:** the exact discrete channel \((p_0,p_5,p_{10})=(7/12,1/12,0)\), CP selection of the swapped orbit assignment, non-embeddability in the marked orbit-scalar continuous semigroup class, and the exact trine identity \(\Phi(E_i)=\sum_jB_{ij}E_j\).  
**Still open:** source derivation of the orbit assignment, the trine POVM/instrument and its state/record semantics, and any physical charged interpretation.

The algebraic intertwiner now exists on the trine operator system, so the next decisive source test is narrower: derive from P1/the original source rule, without inserting the target matrix, the trine POVM and an instrument whose outcome updates reproduce \(B\) in multi-time probabilities. It must also explain why \(A\) carries the \(2/3\) mode and \(F\) the \(1/3\) mode. A one-step equality of effect expectations is insufficient because the effect map is nonmultiplicative.

Equivalently, the still-missing physical map must extend the present positive readout

\[
J:\text{three classical labels}\longrightarrow
\operatorname{span}\{I,A,F\}\subset M_4(\mathbb C)
\]

to a source-selected instrument/record process preserving the actual deck/family action and the observed one-leg/multi-leg composition law. Failure of that test leaves the \(7/12,1/12,0\) channel and trine readout as clean conditional candidates rather than a TFPT-derived charged transfer.
