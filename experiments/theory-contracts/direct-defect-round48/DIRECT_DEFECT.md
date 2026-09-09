# Direct physical-defect control of the executed cubic source

2026-09-08. **NON-RH, conditional same-parent theory experiment.**
This is a new certificate for Round47's ALREADY COMPUTED numerical column.
No new bulk column, additional numerical M layer, complete electric solution,
or T1-T8 solution is claimed. The exact new interval is in `validation.json`.

## 1. Use the actual source as the target

Keep the compact U(1) parent, a=1/12, eta=1/2, beta=1/4, kappa=1/100,
M=4, Vmag=0, and the ambient cubic low onsite term 1/96. No parameter
or initial preparation is selected from TFPT here. The numerical readout
remains n_H,0 at t=1 in uniform bare-low E0 filling.

Round47 actually evaluated the finite ideal source

\[
Z_* = Z_{45}+C_{MEMMM}+C_{MMEMM}+C_{MMMEM}+C_{MEEM},           \tag{1}
\]

up to its separately certified configuration and arithmetic errors.
Its certificate went through the infinite-M target Z46 and then added
an all-later-M evaluation tail. That triangle inequality is valid but
not compulsory. We now certify (1) directly against the physical H.

For a source with the correct initial value define the defect

\[
R(t)=\dot Z_*(t)-i[H,Z_*(t)].
\]

The strong variation-of-constants identity gives

\[
\tau_t(c_{H,0})-Z_*(t)
 =-\int_0^t\tau_{t-s}(R(s))\,ds,
\quad
\|\tau_t(c_{H,0})-Z_*(t)\|
 \le\int_0^{|t|}\|R(s)\|\,ds.                              \tag{2}
\]

The outer propagator is the FULL physical dynamics, not the auxiliary
word tensor evolution. It is norm preserving. Thus all subsequent M
AND E events after a boundary source are enclosed by (2), without an
additional exponential amplification factor. This does not mean that
those later events have been numerically solved or set to zero.

Use the inherited finite-volume strong identities and volume-uniform
bounds; do not differentiate the unbounded electric generator in norm.
The relevant strong-integral framework is discussed by
[Nachtergaele and Sims](https://arxiv.org/html/1410.8174v1).
The branch partition and model-specific bounds below are derived here,
not attributed to that reference. The inherited thermodynamic-limit
assumptions remain conditions of the experiment.

## 2. The exact boundary of the retained branch tree

For each old leaf p in {MEMM, MMEM, MMME, MEE}, retain p and pM.
The complete uncomputed boundary is

\[
\{pE,\ pMM,\ pME\}.                                       \tag{3}
\]

Every later history has a unique first boundary node. In particular,
pE is NOT removed just because pM was calculated. Its full continuation
does not overlap the continuation of pMM or pME. The first-electric
branches after four or more initial M events and the old MEME/MMEE
branches are outside this replacement and remain unchanged.

If D_other denotes D45 minus its four old leaf bounds, the new direct
bound is D_other plus the three boundary bounds in (3) for each family.
This is a replacement of an exact residual decomposition, not deletion
of positive terms from Round47's indirect triangle bound.

## 3. State-independent zero words are safe, initial null words are not

A literal CAR monomial is identically zero precisely when its repeated
actions on some mode demand inconsistent occupations. Reading right to
left, the first encounter fixes that mode's required initial occupancy;
each legal creation/annihilation toggles it. A later inconsistent demand
kills every Fock matrix element. If all demands are consistent, choose
the required input occupation for each encountered mode: the result is
a nonzero signed basis vector. This proves necessity and sufficiency.

If O=0 as an operator, then F O=0, F[V,O]=0 and [V,F]O=0. Both M and E
branches vanish identically, as does their free propagation. Such a SEED
can therefore be removed from an envelope before further M propagation.
No numerical source or predecessor file needs to be changed: its exact
whole-operator contributions already cancel.

This is NOT a quotient by the chosen initial state. For example, two
different annihilators at one site can annihilate every exactly-one/site
input and still form a NONZERO whole-Fock operator. The checker retains
such words. Tests compare the decision against exhaustive complete Fock
action and compare the all-M edge result before/after only this safe rule.

The full raw census is still collected and must equal Round45/47 exactly.
Only then is the independently identified whole-operator-zero subset
excluded from the new boundary moments. No tensor-l2/CAR isometry is used.

## 4. Compute the new moments without enumerating another 95 million paths

Let d=3 or 5 be the literal word arity, k=(d-1)/2 the electric count,
and n=5-k the seed order. Keep Round45's scalar phase moments m_p,b_p,
its prefix currents r_j, and the zero final phase-difference entries.
For each species pattern sigma collect, over NONZERO operator seeds,

\[
a_\sigma=\sum |w_p|m_p,\quad
b_\sigma=\sum |w_p|b_p,\quad
f_\sigma=\sum |w_p|m_p|r_{p,n}|_1.                          \tag{4}
\]

All six first directions enter these moments; raw and retained vectors
of dimensions 8 and 32 are stored separately. There is no spatial cutoff.

Use the positive species matrix and whole-Fock CAR row bounds

\[
W=\begin{pmatrix}53/96&1/4\\1/4&0\end{pmatrix},\quad
C_L=\sqrt{107/2048},\quad C_H=\sqrt{1/96}.
\]

Let W_d be the sum of its actions on all d legs and c_sigma=sum_j C_sigma_j.
Enumerating the already-retained pM row in absolute weight, then grouping
the LAST uncomputed M as a whole CAR commutator, gives

\[
A'_k=aW_dc.                                                \tag{5}
\]

This is the first m=2 moment of Round47's envelope, not its whole infinite
sum. The missing continuation is now in the full-H isometry (2).

For the new electric boundary, appending M with transport u appends a
zero to every old phase-difference vector. Consequently its exact phase
moment is b_p+m_p|r_{p,n}+u|_1. The triangle bound on this final current
is the only relaxation in the following new phase census:

\[
B'_k\le\sum_\sigma\left[
 \lambda_\sigma(b_\sigma+f_\sigma)+\nu_\sigma a_\sigma
\right],                                                  \tag{6}
\]

where lambda_sigma=sum_j sum_t W_sigma_j,t and
nu_sigma=sum_j J_sigma_j, with J_L=41/48 and J_H=1/4.
These are the original absolute and length-weighted hopping rows,
including all nonbacktracking two-step terms and creator reversals.
Independent explicit cubic pM paths check (5) and the upper inequality (6).
No new bulk physical column is generated to evaluate these moments.

Writing B_k=sum_sigma b_sigma, b_force=53/288 and T=|t|, the three
complete boundary contributions are

\[
R_{pE}=\frac{\kappa^{k+1}b_{force}B_k T^7}{7!},\quad
R_{pMM}=\frac{\kappa^k A'_k T^7}{7!},\quad
R_{pME}=\frac{\kappa^{k+1}b_{force}B'_k T^8}{8!}.            \tag{7}
\]

The factorials follow from the same simplex moment formula as Round45:
n+k=5, the retained additional M adds one integral, the final boundary
adds another; an E boundary also adds a phase-gradient moment. Thus

\[
D_{48}=D_{other}+\sum_{k=1,2}(R_{pE}+R_{pMM}+R_{pME}).       \tag{8}
\]

For an original cubic subgraph with z first neighbors, scale the full
cubic boundary census by z/6, as in Round45. This is not a claim that
a finite edge is equivalent to the cubic bulk. The global ideal error
remains sixth order because D_other starts at T6.

## 5. Reuse the exact numerical center and retain all numerical errors

The pinned Round47 rational q and its entire configuration/arithmetic
error epsilon_num are reused unchanged. No new amplitude or center is
claimed. Apply (8) to the finite ideal source that Round47 actually
approximates, and then add epsilon_num:

\[
\epsilon=D_{48}+\epsilon_{num},\qquad
\langle n_{H,0}(t)\rangle\in
[\max(0,\sqrt q-\epsilon)^2,\min(1,(\sqrt q+\epsilon)^2)].    \tag{9}
\]

This reuse is legitimate because the direct certificate targets the
SAME source, not a different resummed source with uncomputed terms.
The Round44 configuration-exit error stays present and can start at T4.
Neither the global ideal error nor the full numerical error is called
seventh- or eighth-order merely because new boundary terms have those orders.

The deterministic record includes a no-zero-quotient control, both full
and retained raw moment censuses, exact error components, old/new intervals,
source hashes, unchanged center and explicit non-execution flags.
Full physical edge dynamics provides independent finite-model controls,
including coherent inputs; these do not create a new bulk Bell result.

## 6. Remaining work and claim boundary

This removes avoidable looseness in the certificate, not physical terms
from H. The older first-electric/MEME/MMEE branches are still open, as
are further numerical source improvements and additional bulk observables.
Parameter/preparation selection, a chiral continuum and universal spin-two
dynamics have not been derived. T1-T8 are not closed by this calculation.

Only local theory-experiment files and catalog/continuation notes change.
There is no empirical claim, public-paper/website/verification/ledger or
scorecard promotion, no proof-assistant or peer-review promotion, and no
commit or push in this round. The earlier expensive bulk calculation is
a real dependency cost; this smaller recertification is not an end-to-end
speedup claim for solving the physical model.
