# Source sectors 1 and 3: half-shift, opposite-edge compensation and carry

9 September 2026. Local research after publication `66b91e40`.

**Result:** the two actual QWZ backgrounds linked by the proposed half
twist have compatible charged scaling spaces and exactly matching energy
origins. In a stated common point-split reference convention, their top
charges differ by +1/2 and their bottom charges by -1/2. This supplies a
source-specific sector dictionary, not a microscopic local half-charge
field, eight selected copies, an E8 projection, or T1–T8 closure.

The previous `half-charge-energy-bridge` result remains valid. Its two
ground charges are not an algebraic inconsistency: here they can be
matched to two distinct, already present source backgrounds. It would
still be wrong to identify their direct sum with a single-vacuum conformal
representation or to infer that TFPT selects that direct sum physically.

## 1. Same source, two backgrounds, both boundaries

Use the pinned `verification/v1033_charged_disorder.py` source with width 8,
mass 1 and circumference N; no source coefficient is edited. For r=1,3 set

    h_(N,r) = QWZ(N,8,1,r), P_(N,r)=1_(h_(N,r)<0),
    H_(N,r)=dGamma(N h_(N,r)/(2 pi)) - N Tr(P_(N,r)h_(N,r))/(2 pi),
    Q_N = dGamma(I)-8N.

The top modes have momentum p=2 pi(j-r/4)/N and limiting energy
epsilon_top=r/4-j. The bottom energy is its negative. Consequently top
occupancy is j>=1 and bottom occupancy j<=0 in both backgrounds. There
is no zero mode in either background. These are two Hamiltonians for the
same finite CAR algebra, not two new species.

### The vacuum energies agree before normal ordering

Let R reverse the eight transverse rows and Z=diag(1,-1). The actual
strip symbol satisfies, exactly,

    M h(p) M* = h(-p), M=R tensor Z,

because Z sigma_x Z=-sigma_x, Z sigma_z Z=sigma_z and Z TY* Z=TY.
Also p_(3,j)=-p_(1,1-j), modulo 2 pi. Fourier block decomposition
therefore gives identical full finite-cylinder spectra for r=1 and r=3.
In particular their filled sea energies agree exactly. There is no
unknown relative Casimir constant being silently discarded in this pair.
M exchanges the two edges: this equality does NOT identify the top
charged fields or construct a local intersector operator.

### Extension of the existing source CAR estimates

Choose M_N=min(floor(N/12),floor(sqrt(N))) for N>=16. Then throughout
|j|<=M_N, r=1,3, rho=1-cos(p)<1/2. This narrower common window avoids
incorrectly reusing the old r=1 endpoint bound at r=3.

For the top use q_y proportional to rho^(7-y)(1,1); for the bottom use
rho^y(1,-1). The source identities give, on either edge,

    ||(h(p)-epsilon_edge(p)) q|| <= rho^8,
    epsilon_top(p)=-sin(p), epsilon_bottom(p)=sin(p),
    ||P_wrong q|| <= rho^8/|sin(p)|,
    ||q-row_spinor|| <= 2 rho.

Project q into its correct actual spectral sign and normalize it to j_r.
The retention is at least 1-1/49152, and ||j_r-row_spinor||<=4 rho.
Opposite edges at the same momentum lie in opposite spectral signs and
are exactly orthogonal after projection. Distinct Fourier momenta are
orthogonal as well. This gives polarized isometries for both edges and
both actual filled seas. No massive occupied modes are deleted.

The same particle/hole exterior-power construction as in the pinned CAR
proof now applies to each r, simultaneously to both edges. Its projected
generator residual per mode is bounded by

    N/(2 pi) [2 rho^8 + |p|^3/6].

On any fixed finite-energy space this is O(N^-2), with at most floor(4E)
excitations; it is not multiplied by the 8N sea rank. The local raw-row
field estimate and smooth Fourier l1 alias tails work with j-r/4 in
place of j-1/4. Thus the sectorwise local CAR fields, their adjoints and
finite-energy generator comparisons extend to r=3. This argument gives
sectorwise field limits, NOT convergence of an operator changing r.

## 2. Charge energies fix a compatible half-sector dictionary

Filling the nearest available modes gives, for every integer q,

    E_top,r(q) = q^2/2 + (r/4-1/2)q,
    E_bottom,r(q) = q^2/2 - (r/4-1/2)q.

At fixed edge charge, any finite excitation has this minimum plus a
nonnegative integer oscillator level. This follows directly by moving
particles/holes away from the nearest filling, or from the usual charged
partition description; a fixed-charge change of mode occupation cancels
the fractional part of every energy. These are limiting edge minima,
not a statement about finite-cylinder global charge-sector minima.

Write b=(r-1)/2 in {0,1}. The common-reference charges

    p_top=q_top+b/2, p_bottom=q_bottom-b/2

then give, without an additive sector-dependent energy shift,

    H = N_osc + p_top^2/2-p_top/4
              + p_bottom^2/2+p_bottom/4.

In particular E_top,3(q)=E_top,1(q+1/2), with the right-hand side the
polynomial extension, NOT a half-integer call to the old source checker.
The latter correctly continues to accept only integer source charges.
The bottom relation uses q-1/2. Total charge is unchanged:

    p_top+p_bottom=q_top+q_bottom in Z.

This dictionary is unique among affine shifts with unit charge spacing,
the stated r=1 reference and the fixed quadratic energy coefficient.
Energy matching alone would not make these shifted labels observable
charges. The following local-reference calculation independently checks
their vacuum subtraction and records its precise regularization boundary.

## 3. Independent check: point-split covariance subtraction

Use the original Fourier phases in a common local trivialization of the
circle and write t=2 pi(x-y), a=r/4. The limiting top covariance is the
Abel boundary value of

    K_top,a(t;z) = e^(-iat) sum_(j>=1) z^j e^(ijt), 0<z<1.

For t nonzero modulo 2 pi its z->1 value is
e^(i(1-a)t)/(1-e^(it)). The bottom similarly has
K_bottom,a(t)=e^(-iat)/(1-e^(-it)), summing j<=0.
Their differences between a=3/4 and a=1/4 simplify on an arc around zero:

    K_top,3/4-K_top,1/4 = 1/[2 cos(t/4)],
    K_bottom,3/4-K_bottom,1/4 = -1/[2 cos(t/4)].

They have smooth diagonal limits +1/2 and -1/2. Thus Wick subtraction
relative to the r=1 covariance gives exactly the shifts in Section 2.
The singular covariance parts cancel. This is a local statement: a
single common trivialization around the whole twisted circle was not
assumed. It uses the charged CAR scaling covariances, not a new vacuum.

There is an explicit regulated source comparison: restrict the raw-row
Fourier covariance to |j|<=M_N and weight mode j by z^|j|. Denote its
actual spectral occupancy by nu_(N,r,j). The polarization estimate gives
|nu_(N,r,j)-nu_(r,j)|<=9 rho_j^2 on either edge. At fixed 0<z<1,

    |K_(N,r)(t;z)-K_r(t;z)|
      <= 9 sum_(|j|<=M_N) z^|j| rho_j^2 + z^(M_N+1)/(1-z) -> 0.

The bound is uniform in real t at that fixed z. The finite sum is O(N^-4)
since rho_j^2<=p_j^4/4 and the weighted fourth moment is finite. This
connects the Abel covariances to the full source's raw-row polarizations;
it is not a bound uniform as z->1. The separate cutoff-removal and
point-splitting steps must not be collapsed into a finite-density claim.

**Order and convention matter.** Set t=0 before removing the Abel cutoff
and both differences are zero. The statement is the smooth diagonal
restriction AFTER taking the covariance boundary values. It does not
assert convergence of the unsmeared finite-N density, uniform convergence
at coincident cutoff points, or a regulator-independent global charge.
Introducing a background-dependent Wilson-line subtraction changes the
comparison convention. A physical gauge/Clock Ward dictionary still has
to select and justify the current prescription. The exact finite Q_N
remains integral and both finite source seas have Q_N=0.

Background-dependent charge and spin-structure bookkeeping is standard,
not a newly discovered phenomenon. Yao–Fukusumi discuss background flux,
bosonization and the need to keep global sector information in
[Bosonization with a background U(1) gauge field, Sections IV.1–IV.3](https://arxiv.org/html/1902.06584).
Our source-specific equations above do not import their theory as a
proof of the missing microscopic field or of a TFPT physical selection.

## 4. The second half step must carry actual integer edge excitations

On the charge-vacuum span of the two limiting source sectors define the
energy-compatible abstract transfer (phases chosen to be +1 here):

    S |0;q_top,q_bottom> = |1;q_top,q_bottom>,
    S |1;q_top,q_bottom> = |0;q_top+1,q_bottom-1>.

This is a bijection of the actual limiting charge-vacuum basis. Its
adjoint is the inverse. It raises p_top by 1/2 and lowers p_bottom by
1/2, preserving total charge. Its square transfers one integer unit
between the edges; it is NOT the identity. From the reference vacuum,

    energy(S^n Omega) = n(n-1)/4: 0,0,1/2,3/2,3,...
    [H,S]=S(p_top-p_bottom)/2

on that span. A pure two-state flip fails the charge Ward identity on its
second leg. In the CAR mode language the integer second step shifts
both filled edge sets j->j-1; the top gains a particle and the bottom
loses one. This is the required direction of compensation, not an
arbitrary reset of a cyclic register.

The abstract S is not claimed to equal the microscopic Gaussian string,
nor is it local, a smeared operator-valued distribution, an adiabatic
pump, or the E8 cocycle. Its chosen phases do not replace the previously
pinned lattice cocycle. Superposing these background sectors also remains
a physical choice. With a bottom vacuum fixed in the shifted reference,
the r=3 top-half sector cannot simply be retained while its compensating
bottom half sector is deleted.

## 5. What this advances and the next acceptance test

The next half-charge construction can now use BOTH source-derived
sectorwise Fock embeddings, matching energy origins, and an explicit
charge-reference/carry dictionary. It need not postulate an unrelated
half-charge Hilbert register just to obtain the right spectrum.

The remaining test is stronger: construct an actual intersector
operator sequence, control its determinant phase/normalization and its
adjoint after smearing on the common energy core, and obtain the stated
current Ward identities from the same sequence. Its opposite-edge
compensation must either be retained or removed by a proved local
factorization. The known non-Hilbert–Schmidt sharp twist and the failure
of a bare bottom identity to preserve the other vacuum remain in force.
No eight-channel selection, D8 parity restriction, E8 cocycle locality,
common 3+1D parent or TOE status is promoted.

## Reproduction

`checker.py` pins the published source and preceding local energy note.
`test_checker.py` checks exact rational energy/carry identities, independent
covariance algebra, source hopping symmetry, the full 16N-dimensional
filled sea, both edges and sectors, the common projection window and
wrong-reference/wrong-carry controls. Floating finite diagnostics are not
interval certificates or substitutes for the all-mode arguments above.

From this directory:

```sh
../../tfpt-discovery/.venv/bin/python -B -m unittest -v test_checker
../../tfpt-discovery/.venv/bin/python -B -OO -m unittest -v test_checker
../../tfpt-discovery/.venv/bin/python -B checker.py
```
