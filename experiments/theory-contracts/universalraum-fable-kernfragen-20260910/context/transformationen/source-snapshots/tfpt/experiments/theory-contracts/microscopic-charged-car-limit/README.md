# A microscopic integer-charged CAR field from the same QWZ source

2026-09-09. NON-RH. Written constructive proof for one chiral complex CAR
field on the original width-8, mass-1, r=1 cylinder and its actual filled
negative-energy sea. This is **not** the E8 half-charge vertex lambda,
an eight-channel identification, or a common 3+1D parent. All T1--T8 stay open.

## 1. What is new and what is not

The neutral two/four-point results concern exponentials of filtered densities.
Their endpoint charges are not by themselves physical fermion-number shifts.
Here the operators are instead the original microscopic CAR annihilators
and creators, smeared on one boundary row. Charge, adjoints, the true vacuum,
locality, positive excitation energy and time evolution are controlled
together. No finite charge register or independent charge Hilbert factor is
appended. The lower boundary and every bulk mode remain in the source vacuum.

Free chiral edge fermions in QWZ-type models are not a new discovery; see
[Qi--Wu--Zhang's original work](https://arxiv.org/abs/cond-mat/0505308).
The contribution here is the explicit source-specific field/state/domain
dictionary, with quantitative errors, needed before the more difficult E8
spinor extension can be attempted. This does not replace that extension.

Use the actual source loaded through `microscopic-energy-linearization`.
That adapter validates the existing source chain; no source parameters or
old checkers are changed. Let

```
h_N = actual QWZ cylinder(N, width=8, mass=1, sector=1),
P_N = 1_(h_N<0), rank P_N = 8N,
Omega_N = its filled Slater vacuum,
D_N = N h_N/(2 pi),
Hcal_N = dGamma(D_N) - Tr(P_N D_N),
Q_N = dGamma(I) - 8N.
```

The full source has no zero level in this sector and Hcal_N >= 0 on its
entire finite Fock space, including charged sectors. This assertion belongs
to this free source, not to the separate interacting rotor parent.

## 2. Exactly local operators and an exact charged Ward identity

Write chi_+=(1,1)/sqrt(2), and let r be chi_+ on transverse row y=7 and zero
on the other seven rows. For smooth periodic g and x=0,...,N-1, define

```
R_N g(x,y) = N^(-1/2) exp(-i pi x/(2N)) g(x/N) delta_(y,7) chi_+,
Psi_N(g) = a_N(R_N g).
```

Creation a^*(v) is linear in v, annihilation a(v) is antilinear. The twist
factor is the original r=1 holonomy, not a fitted conformal offset. If g
is supported in a proper open arc I, Psi_N(g) is supported **exactly** on
the top-row sites x/N in I. For disjoint arcs the equal-time fields obey
graded CAR locality. This is fermionic locality, not commuting odd fields.

On the whole microscopic Fock space, exactly,

```
[Q_N,Psi_N(g)] = -Psi_N(g),
[Q_N,Psi_N(g)^*] = +Psi_N(g)^*,
{Psi_N(f),Psi_N(g)^*} = <R_N f,R_N g> I.
```

The scalar product converges to the circle L2 scalar product by Riemann
sums. The adjoint is the actual microscopic adjoint; no separate ansatz
is selected. These are integer total CAR charges, not yet E8 root charges,
hypercharge, or Gauss-invariant charged operators of the rotor theory.

## 3. A particularly simple source identity controls dynamics

For Fourier mode j, put

```
k_j=j-1/4, p_j=2 pi k_j/N, epsilon_j=-k_j,
r_Nj=N^(-1/2) exp(i p_j x) r,
rho_j=1-cos(p_j).
```

Direct multiplication of the ORIGINAL transverse hopping blocks gives

```
h(p) r = -sin(p) r + rho chi_- at the same top row,
||h(p) r|| = 2 |sin(p/2)|.
```

At p=0 the row vector is an exact edge zero mode; its transverse hopping
vanishes. Therefore no ultraviolet/bulk norm proportional to N occurs in
the following commutator. For every integer j, even beyond an unaliased
Fourier window,

```
||D_N r_Nj|| <= |k_j|,
||(D_N-epsilon_j)r_Nj||
 <= pi k_j^2/N + (2 pi^2/3)|k_j|^3/N^2 =: b_Nj.       (1)
```

The second estimate uses 1-cos p <= p^2/2 and |p-sin p| <= |p|^3/6.
For g=sum_j f_j exp(2 pi i j x), define S_m(g)=sum_j |k_j|^m |f_j|.
All these sums are finite for smooth g. Absolute convergence handles
sampling aliases without pretending that infinitely many discrete Fourier
vectors are orthogonal. Equation (1) gives

```
||R_N g|| <= S_0(g),
||[Hcal_N,Psi_N(g)^*]|| = ||a^*(D_N R_N g)|| <= S_1(g),
||exp(it D_N) R_N g - R_N g_t||
 <= |t|[pi S_2(g)/N + (2 pi^2/3)S_3(g)/N^2],         (2)
g_t(x)=exp(it/4) g(x-t/(2 pi)).
```

The annihilation/adjoint bounds are identical with the appropriate conjugate
phase. Equation (2) is unitary Duhamel applied mode by mode, not an expansion
of a large extensive Fock Hamiltonian. It gives uniform convergence on
compact time intervals and the same bound in CAR operator norm. The local
field has a single chiral translation in this scaling; no claim of 3+1D
Lorentz symmetry follows.

## 4. The vacuum is the actual filled sea

For |j|<=M_N=min(floor(N/8),floor(sqrt(N))) use the existing source quasimode

```
q_j(y) = rho_j^(7-y) chi_+ / sqrt(sum_(a=0)^7 rho_j^(2a)),
||(h(p_j)+sin(p_j))q_j|| <= rho_j^8,
j_j = P_sign q_j / ||P_sign q_j||,
P_sign=P_N on j>=1, and I-P_N on j<=0.
```

The strip spectral inventory gives |eigenvalue|>=|sin p_j|. Hence
the wrong-sign part of q_j has norm at most

```
rho_j^8/|sin p_j| = rho_j^(15/2)/sqrt(2-rho_j).
```

There is no p_j=0 in this sector. Throughout the declared window rho<1/2,
and the already proved retention floor is 1-1/49152. Moreover
||q_j-r|| <= rho_j/sqrt(1-rho_j^2) <= 2 rho_j. Thus

```
||P_wrong r|| <= 3 rho_j,
||j_j-r|| <= 4 rho_j,
|<r,P_N r>-1_(j>=1)| <= 9 rho_j^2.                    (3)
```

These are O(N^-2), O(N^-2), O(N^-4), respectively, at fixed j. Distinct
Fourier labels remain orthogonal, including after spectral projection.
Let J_N map e_j to the full Fourier column built from j_j. Then

```
J_N^*J_N=I, P_N J_N=J_N P_cur, P_cur(j)=1_(j>=1).     (4)
```

The raw field is a local representative of this exactly polarized embedding:

```
||R_N g-J_N Pi_(M_N) f||
 <= 4 rho_star ||Pi_(M_N) f||_2 + sum_(|j|>M_N)|f_j| -> 0.    (5)
```

Here rho_star=O(N^-1). The tail bound is l1 because it includes sampling
aliases. No filled massive mode is removed to get (3)--(5).

## 5. Many-body isometries, both adjoints, and a common energy core

Define the limiting CAR representation by particle annihilators b_j for
j<=0 and hole annihilators d_j for j>=1:

```
a_j=b_j (j<=0), a_j=d_j^* (j>=1),
Omega=empty excitation vacuum,
Hcal=sum_(j<=0)(1/4-j)b_j^*b_j
     +sum_(j>=1)(j-1/4)d_j^*d_j,
Q=sum b_j^*b_j-sum d_j^*d_j.
```

This excitation representation is obtained from (4), not installed as an
unrelated physical tensor factor. Send its vacuum to Omega_N, particles to
a_N^*(J_N e_j)Omega_N, holes to a_N(J_N e_j)Omega_N, and ordered excitation
products to their ordered microscopic products. Exact CAR and (4) make this
an isometry I_N on the full finite-window excitation Fock space. It intertwines
the truncated a_j, their adjoints and relative charge exactly. The rest of
the physical source is in its original occupied/empty configuration.

To compare all Hilbert spaces, use the contraction V_N=I_N Gamma(Pi_M),
where Gamma(Pi_M) projects onto excitation vectors with all modes in the
window. It is an isometry on every fixed finite-energy space for sufficiently
large N. Its discarded tail tends strongly to zero. Equations (4)--(5)
then imply on every finite-excitation vector psi, for smooth g,

```
||Psi_N(g) V_N psi - V_N a(f) psi|| -> 0,
||Psi_N(g)^* V_N psi - V_N a(f)^* psi|| -> 0.          (6)
```

There is no hidden mismatch of charge sectors: [Q,a_j]=-a_j and each hole
has charge -1, exactly as in the microscopic construction. The limit fields
are bounded by ||f||_2. Source bounds S_0(g) and (6) give convergence of all
fixed finite words on the core, and hence their full complex vacuum moments.
Using (2) gives the same conclusion at finitely many times. Wick's rule is
a corroborating way to calculate these moments, not a replacement vacuum.

The generator limit also holds on a common dense core. Commutation of h with
P_sign and the retention floor imply

```
||(D_N-epsilon_j) J_N e_j||
 <= N/(2 pi)[2 rho_j^8+|p_j|^3/6] =: b'_Nj.          (7)
```

It is O(N^-2) for each fixed j. The residual columns at different momenta
are orthogonal. In the particle/hole excitation representation, second
quantization on k excitations therefore gives an error <=k max b'_Nj,
not a factor equal to the 8N filled vacuum particles. Hcal_N Omega_N=0
exactly. On the spectral space Hcal<=E there are at most floor(4E)
excitations and only |j-1/4|<=E can occur. Thus (7) proves

```
||(Hcal_N V_N-V_N Hcal) 1_(Hcal<=E)|| -> 0.          (8)
```

The union of these finite-dimensional energy spaces is a dense invariant
core for Hcal and Q. Smooth fields preserve D(Hcal) because their commutators
are bounded, with ||[Hcal,a(f)]||=||epsilon f||_2; the source has the uniform
bound (2). This is a field/domain result, not merely a one-particle test.

## 6. Integer charge vacua are supplied by source excitations

For q>=0 occupy the top-edge particle modes j=0,-1,...,1-q; for q=-m<0
create the holes j=1,...,m. These actual source excitation vectors converge
under the same isometries. Their limiting top-edge energies are

```
E_top(q)=q^2/2-q/4, q in Z.                           (9)
```

They minimize energy **within the limiting top-edge CAR representation at
that charge**: filling any more distant particle/hole costs more, and adding
a neutral pair costs positive energy. They are not proved to minimize energy
over the whole finite cylinder, whose other edge remains present.

Thus an unbounded integer-charge ladder, not a cyclic charge register, is
obtained from microscopic particle/hole operators. The linear term in (9)
is the actual r=1 holonomy offset and must not silently be dropped to match
a desired q^2/2 target. As abstract matrix elements on the charge-vacuum span,
E_top(q+1)-E_top(q)=q+1/4. This is not a construction of a local unitary
charge-shift field or of the full boson/fermion correspondence.

## 7. Why this does not close T2 or the other TOE gates

- The field here has unit fermion-number charge. The sourced lambda needs
  the simultaneous eight-channel half twist, lattice cocycle, intersector
  charge carry and the correct weight-one vertex. It is not this field.
- The bare CAR algebra allows odd fermion fields. If TFPT selects only an
  even observable algebra, charged fields belong to an extension; that
  physical choice has not been derived here.
- One QWZ copy was already in the source. This proof does not select eight
  copies, derive D8/E8 charge assignments, or identify the 12-real-dimensional
  compiler readout with a boundary field multiplet.
- No new coupling, spatial spin action, anomaly cancellation, mirror removal,
  rotor Gauss dictionary, universal 3+1D continuum or graviton is supplied.
- The vacuum is the specified source's spectral vacuum, not a uniquely
  selected cosmological state. Bottom modes have not disappeared.

The next direct T2 gate is now sharper: construct the sourced half-charge
intertwiner **between representations of this same microscopic CAR algebra**,
with charge carry, both adjoints, local support and finite-energy estimates.
The previously proved sharp half-string obstruction still matters: its
intersector crossed Hilbert--Schmidt sum diverges, so no unrenormalized Fock
unitary can simply be used as that field. A renormalized smeared spinor field
and its multi-channel E8 extension remain to be proved.

## 8. Verification boundary

`checker.py` validates upstream hashes and evaluates the explicit strip
identities, bounds and original full-cylinder covariance at N=8,16,32.
`test_checker.py` adds independent finite CAR/charge tests, nonzero charged
vacuum vectors, local support, time/adjoint tests, source/phase negative
controls, charge energies and fixed-core many-body residual checks.
Numerical values are floating diagnostics, not interval proofs; the
all-N statements rest on sections 2--6. No external review or proof-assistant
certificate is claimed. Frozen inputs, paper, website and ledger are unchanged.
