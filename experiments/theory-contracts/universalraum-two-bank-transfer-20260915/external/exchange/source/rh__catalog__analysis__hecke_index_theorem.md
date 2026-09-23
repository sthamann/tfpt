# TFPT Hecke Index Theorem: index, modular flow, and the cutoff barrier

Claim boundary: experiment-only structural analysis; no claim for or against RH.

Contract: `TFPT.HECKE.INDEX.01`. Machine record:
`experiments/tfpt-discovery/hecke_index_theorem_probe.py` (7/7 exact/numeric
checks) and `hecke_index_theorem_result.json`.

Tags: `[T]` classical theorem · `[E]` exact probe result · `[I]` inference.

## T1. Physical Hilbert/GNS/OS candidates actually present

The final column distinguishes an actual E8/Hecke action from the stronger
contract: canonical all-\(n\) finite-index endomorphisms on the **physical 4D
OS space**.

| Space | Algebra and state | Time / symmetry | Arithmetic action and contract status |
|---|---|---|---|
| 4D Hamiltonian lattice | Gauge-invariant quasilocal \(\mathcal A^G\); ground/KMS states exist | Thermodynamic-limit \(\tau_t\), gauge symmetry, LR cone | None: `v1013_thermodynamic_dynamics.py:11-35`; `tfpt_4_frontier.tex:809-814`. |
| Finite seam OS + modular GNS | \(B(\mathbb C^N)\), Gaussian/OU covariance and free CAR state | \(\Lambda=e^{-h}\), \(K=\log((1-C)C^{-1})\), \(\mu_4\) | Clock commutation only: `v446_seam_clock_invariance.py:16-42,123-139`. |
| Five-slot Fock/code | \(\Lambda^\bullet(\mathbb C^5)\), \(16\)-state \(S^+\), vacuum | Quadratic Clifford transport, sheet parity | Carrier only: `tfpt_1_architecture_e8.tex:1570-1589`. |
| Collision QCA | \(M_3\) plus qutrit ancillas; density/population state | \(\Phi^n=B^n\), \(Z_3\) adder | No E8 action; continuous OS leg open: `v984_markov_qca_dilation.py:11-42`. |
| Weak-collision HP/GNS | Finite matrix algebra; uniform Hilbert–Schmidt GNS | GKSL \(Q=\log B\), local flow | No E8 action: `v999_weak_collision_hp.py:6-22,518-551`. |
| 16-Majorana Fock and \((E_8)_1\) net | Clifford/CAR and simple-current net extension; quasi-free vacuum | \(Z_4/Z_8\), modular rotation | **E8 net action and index-4 CAR expectation exist**, but no all-\(n\) physical \(\rho_n\): `v506_seam_clock_rigidity.py:43-60,716-729`; `tfpt_1_architecture_e8.tex:1615-1635,1850-1889`. |
| Flat \(\tau=i\) pillowcase | Laplacian/DtN; OS quasi-free vacuum is hypothesis \(H\) | Twisted heat traces, \(\mu_4\) deck | E8 character/heat readout, no endomorphism sectors: `origin_theory.tex:340-346,710-714,1793-1810`. |
| RTF arithmetic GNS carrier | \(\ell^2(d,b^2/|d|)\) character fibres | Hecke \(T(p^2)\), amplitude Dirac | **Hecke-equivariant action exists**, but this is an arithmetic/compiler carrier, not physical 4D OS: `tfpt_1_architecture_e8.tex:2026-2036,2117-2189`. |
| OS-reconstructed seam vacuum | RP transfer/projective-limit state | \(H_{\rm OS}=-\log T\), gap \(6\log(3/2)\) | No lattice action: `origin_theory.tex:1903-1908`. |
| Relative boundary QFT | \((\mathcal A_\Sigma,\omega_\Sigma,\Delta_\Sigma,\rho,A_F,H_F,D_F,J,\gamma,S_{\rm rel})\) | Seam KMS/modular cutoff | E8 is a K3 facet, not an all-\(n\) action: `origin_theory.tex:1885-1898`. |

[I] E8 and Hecke actions do exist in the corpus, contrary to the overbroad
initial absence statement. The narrower precondition remains absent: no
**physical 4D OS space** carries canonical \(\rho_n\) for every \(n\), with
index \(n\). The scale lattice (`tfpt_1_architecture_e8.tex:4165-4190`) is
metrology, not a Hilbert space. The existing Hecke action is arithmetic and the
net action has only the index-\(4\) slice, so neither meets the frozen
“physical, not rebuilt arithmetic” clause. We therefore use
\[
\mathcal H_{\rm tor}=L^2(\mathbb R^8/E_8),\qquad
\mathcal A_{\rm tor}=C(\mathbb R^8/E_8),
\]
with Haar state, character basis, heat semigroup, and Weyl lattice isometries.
This is an **arithmetic-side stand-in, not the 4D OS space**.

## T2. L1 index theorem on the stand-in

Choose an integral basis of \(E_8\). Every \(A\in M_8(\mathbb Z)\) with
\(\det A\ne0\) induces
\[
\rho_A(f)=f\circ A,\qquad \rho_A(e_v)=e_{A^{\mathsf T}v}.
\]
Character addition and \(e_v^*=e_{-v}\) prove the unital
\(*\)-endomorphism law. Since \(A^{\mathsf T}\) is injective on the character
lattice, \(\rho_A\) is injective. Its range is the
\(\ker(A:\mathbb T^8\to\mathbb T^8)\)-invariant algebra and
\[
E_Af(x)=\frac1{|\det A|}\sum_{y\in\ker A}f(x+y).
\]
The free finite-group action gives Watatani/Pimsner–Popa index
\(\operatorname{Ind}(\rho_A)=|\det A|\), the covering degree [T].

The probe formed random unimodular conjugates of
\(\operatorname{diag}(d,1,\ldots,1)\) and counted every fibre exactly:

| \(|\det A|\) | 2 | 3 | 5 | 6 | 7 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| fibres / index | 2 | 3 | 5 | 6 | 7 | 9 | 10 |

Also,
\[
\operatorname{Ind}(\rho_A\rho_B)=|\det(BA)|
=|\det A|\,|\det B|.
\]
For the commuting canonical family
\(A_n=\operatorname{diag}(n,1,\ldots,1)\),
\(\rho_m\rho_n=\rho_{mn}\). Every prime \(p\le50\) (15/15) occurs, and
primes are precisely the primitive non-unit indices.

For the Gaussian rank-four module the same proof gives
\(\operatorname{Ind}(\rho_A)=N_{\mathbb Q(i)/\mathbb Q}(\det A)\).

| Gaussian prime type | index \(p\)? | first scalar index |
|---|---:|---:|
| \(p=2\), ramified | yes | \(2\) |
| \(p\equiv1\pmod4\), split | yes | \(p\) |
| \(p\equiv3\pmod4\), inert | no | \(p^2\) |

Thus L1 is proved on the torus algebra, but it is the classical finite-cover
index / sublattice RG of `bridge2_direct_search.md` §§2–3. The \(\mu_4\)
mark changes the arithmetic to \(\mathbb Q(i)\) and the Euler factors toward
\(\zeta_{\mathbb Q(i)}=\zeta L(\chi_{-4})\); it does not create the missing
physical representation.

## T3. L2 modular test

### Haar and all commutative torus states

\(\mathcal A_{\rm tor}\) is commutative, so **every** state on it is tracial.
For a faithful GNS state its Tomita modular operator is
\(\Delta=1\), hence \(H=\log\Delta=0\). In particular Haar does not give
\(\Delta_{\rho_p}=p\). L2 fails exactly for the trace.

This also corrects a tempting misstatement: a classical Gaussian free-field
measure on a commutative field algebra has trivial Tomita flow. Its heat or
Laplacian evolution is a Markov/transfer flow, not automatically modular flow.

### Heat density on the noncommutative mode algebra

On \(B(\ell^2(E_8^*))\), take a type-I heat density with
\(K_t=4\pi^2t(-\Delta)\). For \(A=\operatorname{diag}(2,1,\ldots,1)\),
\[
K_t(A^{\mathsf T}v)-K_t(v)
=4\pi^2t\bigl(|A^{\mathsf T}v|^2-|v|^2\bigr).
\]
The truncated character test found exact quadratic differences
\(\{0,3,12,27\}\), rather than one value \(\log2\). Therefore \(v_A\) is not
a modular eigenoperator with determinant-only eigenvalue.

The v446 state does not help: its modular \(K=h\) is a generic seeded
\(\mu_4\)-block matrix; it commutes with the clock but has no index labelling
(`compiler_necessity.md` §B3).

### Arithmetic semigroup algebra

In Bost–Connes/Laca–Raeburn-type semigroup crossed products,
\(\sigma_t(v_A)=|\det A|^{it}v_A\) is **defined** as the arithmetic dynamics;
it is not derived from Haar or the TFPT OS state. See Arledge–Laca–Raeburn,
*Doc. Math.* 2 (1997), 115–138, and Laca–Raeburn,
*J. London Math. Soc.* 59 (1999), DOI `10.1112/S0024610798006620`.

The sublattice Gibbs representation has
\[
Z_8(\beta)=\prod_{j=0}^{7}\zeta(\beta-j),\qquad \beta>8.
\]
The probe independently matched all 30 coefficients by HNF recursion:
\[
a_8(1..10)=
1,255,3280,43435,97656,836400,960800,6347715,8069620,24902280.
\]
This is the classical subgroup zeta function of \(\mathbb Z^8\). “Solomon
zeta” is broader terminology for lattice/module zeta functions; the displayed
free-abelian formula should not be attributed to a special new E8 theorem.

K2 therefore fires: no corpus state realizes index flow as **its own** modular
flow. A physical state would have to satisfy sector weights
\(w_A\propto\operatorname{Ind}(A)^{-1}\), equivalently the \(\beta=1\) KMS
condition for the index dynamics. But that KMS statement already presupposes
the dynamics it was meant to derive; moreover \(Z_8(1)\) is outside the
\(\beta>8\) trace-class region.

## T4. Equality hunt and cutoff

Let \(T_n=\sum_{[E_8:L]=n}E_L\), where the sum is over sublattices modulo
basis change, not over infinitely many matrices \(A\) of determinant \(n\).
For the constant invariant vacuum \(\Omega\),
\[
\langle\Omega,T_n\Omega\rangle=a_8(n),\qquad
F(s)=\prod_{j=0}^{7}\zeta(s-j).
\]
For a finite-\(t\) normalized heat-kernel vector,
\[
\langle\Omega_t,T_n\Omega_t\rangle
=\sum_{[E_8:L]=n}\|E_L\Omega_t\|^2,
\]
a geometry-dependent theta sum. It is **not** \(a_8(n)\); only the
\(t\to\infty\) constant-vacuum limit gives the subgroup-zeta series.

The Euler-side logarithmic derivative is exactly
\[
-\frac{Z_8'}{Z_8}(s)
=\sum_{p}\sum_{k\ge1}
\bigl(1+p^k+\cdots+p^{7k}\bigr)(\log p)\,p^{-ks}.
\]
Every displayed weight is positive. This is not the Weil
\(\operatorname{Arch}(h)-\operatorname{Prime}(h)+\operatorname{Pole}(h)\)
form: the negative sign and \(n^{-1/2}\) central normalization arise after
logarithmic differentiation and the adelic/\(\mathbb Q^*\) quotient, not
from a positive sublattice sum.

There is also a decisive cutoff mismatch. For torus modes
\(|v|\le\Lambda\),
\[
\operatorname{Tr}P_\Lambda
\sim \operatorname{Vol}(B_8)\Lambda^8
=\frac{\pi^4}{24}\Lambda^8,
\]
and for a cube cutoff it is exactly \((2L+1)^8\). The trace itself therefore
does **not** contain an \(h(0)\log\Lambda\) leading term; only
\(\log\operatorname{Tr}P_\Lambda=8\log\Lambda+O(1)\).

Connes’ \(2h(1)\log\Lambda\) term is a property of the adelic quotient trace
formula, not compact-torus mode counting (Connes, *Selecta Math.* 5 (1999),
29–106). Consequently the torus gives no finite
Arch–Prime–Pole remainder to identify. Its positive polynomial divergence is
vacuous; the criterion-bearing step is passage to the Fourier-invariant
cokernel/adele-class quotient.

If the three corpus scales
\(\{\alpha^{-1},L_0,\log(8\pi)\}\) bound log-scale
(`tfpt_1_architecture_e8.tex:4165-4190`), one may only write
\[
\operatorname{Weil}(h)+B(h)\ge0.
\]
Proving \(B\) subordinate is precisely an L*-type metric inequality, not a
consequence of finite scale volume (`rh_program.tex:733-791`; terminal
ratio discussion `rh_program.tex:313-340`).

## T5. Verdict (Kurzfassung)

**Verdikt:** `L1_PROVED_CLASSICAL + L2_KILLED(K2) +
EQUALITY_HUNT=CONNES_DICHOTOMY`.

Bewiesen ist L1 nur auf dem arithmetischen Torus:
\(\operatorname{Ind}(\rho_A)=|\det A|\) ist der klassische
Überlagerungsgrad, multiplikativ; Primzahlen sind primitive Indizes. Die
Gaussianische \(\mu_4\)-Marke ersetzt \(\mathbb Z\) durch \(\mathbb Z[i]\):
\(p=2\) und \(p\equiv1\pmod4\) treten bei Index \(p\) auf,
\(p\equiv3\pmod4\) erst bei \(p^2\).

Gescheitert ist die physikalische Aussage. Kein im Korpus konstruierter
4D-OS/GNS-Raum trägt diese Endomorphismen. Auf \(C(T^8)\) ist
\(\Delta=1\); auf der Heat-Mode-Algebra hängt der modulare Energieunterschied
von \(v\), nicht nur von \(\det A\), ab. Die gewünschte Dynamik ist in
arithmetischen Semigruppen-Systemen definiert, nicht aus TFPT hergeleitet.

Auch der Equality Hunt schließt nichts: die Torusspur hat positive
Eisenstein/Untergittergewichte und divergiert wie \(\Lambda^8\), nicht wie
\(\log\Lambda\). Erst Connes’ Quotient erzeugt die kriterientragende
Arch–Prime–Pole-Struktur.

TFPT müsste daher zweierlei liefern: (1) einen Zustand auf dem
physikalischen 4D-OS-Sektoralgebra, dessen eigener modularer Hamiltonian auf
Lattice-Endomorphismen \(\log\operatorname{Ind}\) ist — also einen
\(\beta=1\)-KMS-Zustand der Indexdynamik, ohne diese Dynamik vorauszusetzen;
und (2) ein endliches Skalenvolumen mit beweisbar subordinierter Randform
\(B\), genau die offene L*-Anforderung. Kein RH-Claim.
