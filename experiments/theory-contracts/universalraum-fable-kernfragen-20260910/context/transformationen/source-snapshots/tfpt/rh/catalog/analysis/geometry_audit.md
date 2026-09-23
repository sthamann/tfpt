# Geometry audit against the fixed Bridge-2 shape

**As of:** 2026-09-04. **Claim boundary:** literature/corpus synthesis only; no claim for or against RH.

## Target and audit rule

The target is a manifestly positive Markov/OS semigroup in log scale whose reflection is
\(s\mapsto1-s\) and whose **self-adjoint generator itself** carries the ordinates of the
nontrivial zeta zeros. It needs: **I1** noncompact scale space/dilations; **I2** a
multiplicative all-place action with primitive orbit labels \(p\) and repetitions
\(p^k\), but no independent \(\log(pq)\) orbit; **I3** canonical Hilbert structure;
**I4** the zeros as generator spectrum, not zeros of a continued spectral zeta; **I5**
the archimedean \(\Gamma,\pi\), Gaussian/Fourier place on the same space.

The filters are `positive-cone-blindness`, `discrete-spectrum-neutrality`, and the
Conrey–Li warning that a natural operator positivity may be strictly stronger than RH.
The fixed shape and filters are from `bridge2_direct_search.md` and
`bridge2_object_search.md`.

## A. Map re-examination

`python3 rh/catalog/map/rhmap.py gaps --json` returned **182 G1 zero-attempt nodes**.
“Zero-attempt” is map metadata, not evidence that the corpus or literature never touched
the object. Every G1 `GEOMETRY`, `OBJECT`, or `METHOD` was classified in the companion
JSON. The main collapses are:

- compact lattices, tori, modular surfaces, finite modules, theta/Hecke and spectral-zeta
  objects → `discrete-spectrum-neutrality` or `euler-side-blindness`;
- positive measures, heat kernels, Gibbs/KMS, squares and conditional expectations →
  `positive-cone-blindness`;
- Mellin/Pick/Lee–Yang/de Branges/Hankel languages → a known criterion, RESTATEMENT, or
  Conrey–Li's stronger-than-RH obstruction;
- local \(p\)-adic trees, K3/Hodge and Rosati geometry → per-place geometry without the
  global archimedean–prime joint space;
- Berry–Keating, Connes, scaling-site and Deninger nodes → already covered forms of the
  global scaling/dynamical program.

### G1(b): genuinely unexamined and shape-relevant

- `adele-class-space` — global state-space candidate for I1/I2/I5; the Markov generator
  required for I4 is unconstructed.
- `additive-adeles` — canonical self-dual Fourier space and all-place carrier, but its
  present map route reduces to the explicit formula rather than a zero generator.
- `arakelov-intersection` — joins finite and archimedean places and could supply I2/I5;
  no noncompact OS generator is known.
- `connes-adele-scaling-flow` — supplies the canonical global dilation action; its
  established action is unitary, not the required stochastic semigroup.
- `deninger-cohomology` / `deninger-foliated-dynamics` — conjectural I1–I5 template;
  the arithmetic host and polarization are not constructed.

These are genuinely unprobed **map components**, but not overlooked finished frameworks.
They collapse to the already-recorded open node
`stochastic-scale-semigroup-on-connes-cokernel` or the equivalent
all-place Deninger/Arakelov realization. `ising-lee-yang-compiler` remains in (a), because
its map edge already reduces it to the Lee–Yang criterion rather than supplying I4.

G2 adds no unused escape: screw/Lee–Yang/Li/Jensen/Newman are criteria; de Branges
positivity is too strong; Hankel and archimedean dominance do not create I2/I4.
G5's shortest TFPT paths reach the explicit formula/finite Weil windows, while
`cm-seam`, `mu4-mark`, `seam-geodesic`, `tfpt-c3`, and `tfpt-gcar` have no live path.
The live G6 closers are W3/W4/L*, the all-place intersection, and the stochastic Connes
cokernel; all are already named open walls.

## B. Framework audit

### B1. Quasicrystals

Dyson called a pure-point distribution with pure-point Fourier spectrum a
one-dimensional quasicrystal and observed that RH would put the zero atoms on a line,
with prime-power frequencies suggested by the explicit formula [Dyson 2009].
The slogan needs a correction. In a standard normalization the explicit formula contains
both prime-power atoms and an archimedean continuous/background distribution; it is not
simply
\[
\widehat{\sum_\rho\delta_{\gamma_\rho}}
=-\sum_{p,k\ge1}(\log p)p^{-k/2}
(\delta_{k\log p}+\delta_{-k\log p}).
\]
Kurasov–Sarnak explicitly note that Guinand's prime explicit-formula example is **not**
a Fourier quasicrystal in their sense, even assuming RH. A 2024 proposal instead uses a
renormalized tempered distribution (zero atoms minus the Riemann–von Mangoldt density);
its temperedness/real support criterion is another explicit-formula reformulation
[arXiv:2402.10604].

A crystalline measure may be complex: it is a discrete tempered Radon measure whose
distributional Fourier transform is a discrete Radon measure. A Fourier quasicrystal
also requires tempered total variations. Positivity is extra, not definitional
[Lev–Olevskii, DOI `10.1007/s00222-014-0542-z`; Favorov,
DOI `10.1007/s10476-024-00031-y`]. Kurasov–Sarnak construct positive examples from
finite-variable stable/Lee–Yang polynomials [DOI `10.1063/5.0012286`]. Alon–Cohen–
Vinzant characterize **\(\mathbb N\)-valued one-dimensional Fourier quasicrystals** by
finite-variable Lee–Yang restrictions, not arbitrary complex crystalline measures
[arXiv:2303.03201].

The frequencies \(\{\log p\}\) are \(\mathbb Q\)-linearly independent by unique
factorization, hence have infinite rank. This excludes any one fixed finite-variable
Lee–Yang/Kurasov–Sarnak realization. The Bohr lift on \(\mathbb T^\infty\) accommodates
the rank but is compact, gives Euler-side Hardy/hypercontractive structure, and supplies
neither I4 nor the archimedean correction. Focused corpus contact
(`quasicrystal|Lee-Yang|Meyer set`): **10 files / 22 lines**; best hits are
`recursive_crystal.py:6`, `fractal_selfsimilarity_hunt.py:4`, and
`tfpt_decagonal.py:3`; `Meyer set` has no hit. Map contacts are
`ising-lee-yang-compiler`, `prime-torus`, and `bohr-lift`.
**Supplies:** I2 partially, I3. **Cannot supply:** I1,
I4, I5 without importing the explicit formula. **Verdict: NEUTRAL
(restatement/definition mismatch).**

### B2. Quantum graphs

A metric graph Laplacian with self-adjoint vertex conditions has a unitary bond-scattering
matrix and secular equation \(\det(I-S(k)e^{ikL})=0\); its exact trace formula sums
closed walks and repetitions [Kottos–Smilansky; Berkolaiko–Kuchment]. If edges/cycles
of lengths \(\log p\) and \(\log q\) communicate, concatenated closed walks have length
\(\log(pq)\). This is the “composite orbit” difficulty stated explicitly by Kuipers,
Hummel and Richter [arXiv:1307.6055; DOI `10.1103/PhysRevLett.112.070406`].

**Conditional support lemma.** Assume edge lengths \(\{\log p\}\) are
\(\mathbb Q\)-independent; require the periodic-orbit distribution to have support only
at \(k\log p\); and forbid cancellation between distinct walks of equal metric length.
Then every nonzero closed walk uses one prime edge only. Consequently the directed
support of \(S\) has no cycle visiting two prime sectors, so after removing transient
arcs its recurrent part is block diagonal. The secular determinant factors into
single-prime determinants. This proves decoupling under the stated no-cancellation
hypothesis; it is **not** an unconditional published theorem against engineered
cancellations.

Indeed arXiv:1307.6055 builds a *swarm* of butterfly graphs whose combined oscillatory
density mimics prime terms and repairs repetition signs by interference. It does not
produce one canonical finite-length graph, match the Riemann–von Mangoldt mean density,
or prove that its generator spectrum equals the zeta zeros. A 2026 “prime bouquet”
deposit (DOI `10.5281/zenodo.19589662`) is an unrefereed formal resonance construction.
Exner's DOI `10.1088/1751-8113/43/9/095204` is a narrower no-go for
Berry–Keating operators on compact graphs, not the general decoupling claim.
Corpus direct count: **0**. **Supplies:** I3 and formal I4 for a genuine graph spectrum;
I2 only by hand. **Cannot supply:** exact I1/I5 and the all-place prime-power trace
without decoupling or unproved infinite cancellation. **Verdict: NO-GO for connected
noncancelling metric graphs; NEUTRAL/OPEN for cancellation-engineered infinite swarms.**

### B3. Calabi–Yau geometry

LMFDB `8.4.a.a` is the unique normalized weight-4, level-8 newform
\[
f_8(\tau)=\eta(2\tau)^4\eta(4\tau)^4.
\]
It occurs as the \(H^3\) L-function of several rigid Calabi–Yau threefolds, including
resolutions of self-fibre products of level-8 elliptic modular surfaces
[Meyer–Cynk, arXiv:math/0504070; LMFDB 8.4.a.a]. An explicit anchor is the
Verrill/Fermi \(T_{70}\) threefold, birational to the \(W_0(8)\) self-fibre product;
see Verrill, DOI `10.1006/jnth.1999.2449`. Thus the TFPT \(\mu_4\) cusp channel
has a genuine rigid-CY3 arithmetic realization. This does **not** transfer RH for
\(\zeta\): GRH for \(L(f_8,s)\) is a separate conjecture.

Mirror symmetry and finite-field zeta functions relate periods to local Frobenius data
[Candelas–de la Ossa–Rodriguez-Villegas, arXiv:hep-th/0012233]. They supply local I2,
not a noncompact global scale generator. Corpus: 3 literal `Calabi` hits; many `f8`
hits, e.g. `cuspidal_bridge_probe.py:111`. **Supplies:** local I2, canonical cohomological
I3, local archimedean factor. **Cannot supply:** I1 and I4 for Riemann zeros.
**Verdict: COVERED / NEUTRAL.**

### B4. Other-dimensional topologies

- **Arithmetic topology.** Mazur/Morishita's primes↔knots, linking↔residue-symbol
  dictionary is structural analogy, not a constructed scale flow [Morishita,
  *Knots and Primes*, 2012]. It lacks I3–I5. **NEUTRAL.**
- **Deninger 3-flows.** Closed orbits model primes and reduced leafwise cohomology models
  the explicit formula. Determinant/trace theorems exist for actual foliated systems,
  but the arithmetic system and polarization do not [Deninger, arXiv:2301.11643;
  arXiv:2410.20758]. This can supply I1–I5 *if constructed*. **COVERED,
  UNEXAMINED-WORTH-A-CONTRACT only in its arithmetic realization.**
- **Hyperbolic/Ruelle/Selberg.** For an actual hyperbolic manifold, zeros/poles of
  dynamical zetas have spectral/cohomological meanings [Fried; Patterson–Perry], but
  its primitive length spectrum and gamma/topological factors are geometric, not the
  completed Riemann data. There is no theorem known here saying that *every* hyperbolic
  length spectrum cannot equal \(\{\log p\}\); claiming such rigidity would overstate
  the literature. The exact mismatch is that no known manifold realizes that prescribed
  prime length spectrum and the Riemann archimedean term simultaneously. **NO-GO for
  known manifolds / OPEN as Deninger's conjectural arithmetic flow.**
- **K3.** \(H^2(K3,\mathbb Z)\cong3U\oplus2E_8(-1)\), signature \((3,19)\);
  \(\mathrm{NS}\) has signature \((1,\rho-1)\) [arXiv:1501.04049]. This gives a Hodge
  polarization but no prime scale action or zeta generator. **NEUTRAL.**
- **Abelian varieties/Rosati.** Positive Rosati trace pairing proves the finite-field
  RH mechanism and \(F^\dagger F=[q]\) [arXiv:1509.00797]. It is per variety/per place;
  applying it independently cannot create global prime interference. **NO-GO by
  positive-cone/all-place blindness, not by failure of Rosati positivity.**

### B5. Möbius

Möbius inversion and the primon fermionic partition function \(1/\zeta\) merely invert
the Euler product; zeros become poles and I4 is unchanged. On the scale line,
translations/dilations/inversion sit in the affine/Möbius and metaplectic/Weil
frameworks; Tate Fourier duality supplies the functional equation, Berry–Keating
\(xp\) supplies dilation, and Connes supplies the adelic quotient/cokernel. What remains
is precisely the global boundary/trace positivity or stochastic generator. A Möbius
strip adds only non-orientable boundary conditions; no published arithmetic mechanism
creates I2/I5 or forces the zeta spectrum.

Corpus broad count: 393, overwhelmingly arithmetic Möbius sieves/metaplectic probes;
best structural contacts are `mobius_crossratio_firewall_probe.py`,
`seam_cover_forcing_probe.py`, and `koide-mobius-flow`, the latter blocked by finite
clock commensurability/no canonical integer label. **Supplies:** (ii) I1–I3 and part of
I5 through Tate/Connes; (i)/(iii) none beyond notation/topology. **Cannot supply:** I4
without the Connes global step. **Verdict: COVERED; Möbius-scale geometry REDUCES TO
Connes/Berry–Keating, strip geometry is shape-irrelevant.**

### B6. Quantum geometries

- **Noncommutative geometry / spectral triples:** Connes' adele class space supplies
  I1–I3/I5. Finite self-adjoint perturbations in Connes–Consani–Moscovici
  (arXiv:2511.22755) numerically track low zeros, but spectral/determinant convergence
  is open. **COVERED.**
- **Bost–Connes/QSM:** canonical KMS positivity and \(H=\log N\), but zeta is the
  partition function; zeros are continuation artifacts. **NEUTRAL.**
- **Quantum tori/groups:** useful deformation/representation geometry, but no known
  canonical all-place action whose generator has zeta zeros. **UNEXAMINED but
  shape-irrelevant absent I2/I5.**
- **Fractal strings:** for fixed \(D\in(0,1)\), the Lapidus–Maier inverse spectral
  problem is affirmative iff \(\zeta\) has no zero on \(\Re s=D\); hence affirmative
  for every \(D\ne1/2\) iff RH [DOI `10.1112/jlms/52.1.15`]. This is an exact geometric
  criterion, not a generator construction. Corpus direct terms `fractal string`/
  `Lapidus` are absent, but `fractal_selfsimilarity_hunt.py` and
  `rh_program.tex:4047` use complex dimensions. **NEUTRAL (RESTATEMENT).**
- **Tropical/Berkovich/\(p\)-adic:** the Connes–Consani scaling site is already a
  tropical curve \([0,\infty)\rtimes\mathbb N^\times\), with prime circles of length
  \(\log p\) [arXiv:1507.05818; DOI `10.1016/j.crma.2015.09.027`]. Local
  Bruhat–Tits/Berkovich geometry lacks the global I4 step. **COVERED under CC.**
- **Causal/Lorentzian and loop/spin networks:** no accepted direct zeta/RH mechanism;
  the TFPT 4D layer has no all-place arithmetic action. **Shape-irrelevant.**

### B7. Remaining map candidates

Arakelov intersection is the only additional geometric language that natively combines
finite and archimedean places. It can supply I2/I5 and a Hodge-index form, but no known
noncompact Markov generator with zero spectrum; `open-global-all-place-intersection`
already records this gap. Bruhat–Tits trees, modular surfaces, E8 tori, prime tori and
finite Weil-GNS metrics are respectively local, compact, or criterion-level and are
subsumed by the filters above.

### Frozen contract (the sole surviving shape, not a newly discovered framework)

1. State space: an adelic/Arakelov quotient with self-dual Haar measure.
2. Scale action: a conservative Markov semigroup \(P_t\), \(t=\log r\).
3. Orbit trace: primitive components \(p\), repetitions \(p^k\), no mixed primitive orbit.
4. Reflection: OS involution realizes \(s\leftrightarrow1-s\), including the real place.
5. Generator: canonical self-adjoint \(A\), independently of zeta continuation.
6. Prove a trace/resolvent identity identifying \(\operatorname{spec}(A)\) with zero ordinates.

## C. Synthesis

Die Prüfung findet keine vergessene fertige Geometrie. Quasikristalle (in einer
renormalisierten/distributionellen Fassung) und Lapidus–Maier-Fraktalsaiten sind präzise
geometrische **Umformulierungen**; sie erzeugen die fehlende Positivität nicht.
Calabi–Yau-Geometrie identifiziert \(f_8\) tatsächlich als rigid-CY3-L-Funktion, bleibt
aber für \(\zeta\) GRH-neutral. K3/Hodge und Rosati liefern echte geometrische
Positivität nur pro Objekt bzw. pro Stelle. Möbius-Geometrie auf der Skalenachse ist
bereits Tate/Berry–Keating/Connes; das Möbiusband trägt keinen zusätzlichen
arithmetischen Mechanismus.

Der Quantum-Graph-Einwand ist stark, aber nur unter expliziter
Nicht-Auslöschungsannahme ein No-Go: ein verbundener Graph erzeugt gemischte
\(\log(pq)\)-Bahnen; Auslöschungskonstruktionen existieren, liefern bisher jedoch weder
einen kanonischen globalen Graphen noch das volle Spektrum. Ebenso gibt es kein
allgemeines publiziertes Starrheitstheorem, das jedes hyperbolische
\(\{\log p\}\)-Längenspektrum ausschließt; bekannte Mannigfaltigkeiten passen nicht,
und Deningers postuliertes arithmetisches Flusssystem ist genau die offene Ausnahme.

Der gemeinsame Strukturpunkt ist daher nicht Dimension, Orientierbarkeit oder
„Quantengeometrie“, sondern das **Produkt über alle Stellen**. Nur ein adelischer
Raum macht Primorbit \(p\), Wiederholungen \(p^k\), archimedischen Faktor und
Skalenreflexion zu Teilen desselben Objekts. Der einzige vertragsfähige Rest ist der
oben eingefrorene stochastische Skalenhalbgruppe auf dem Connes-Kokern bzw. eine
äquivalente Deninger/Arakelov-Realisierung; das ist bereits die bekannte Bridge-2-Lücke,
keine neu entdeckte Lösung.

## Primary references

Dyson, *Notices AMS* 56 (2009), 212–223; Arias de Reyna,
arXiv:2402.10604; Kurasov–Sarnak,
DOI `10.1063/5.0012286`; Lev–Olevskii, DOI `10.1007/s00222-014-0542-z`;
Alon–Cohen–Vinzant, arXiv:2303.03201; Kuipers–Hummel–Richter,
arXiv:1307.6055, DOI `10.1103/PhysRevLett.112.070406`; Berry–Keating,
DOI `10.1137/S0036144598347497`;
Meyer–Cynk, arXiv:math/0504070; Verrill, DOI `10.1006/jnth.1999.2449`;
Candelas–de la Ossa–Rodriguez-Villegas,
arXiv:hep-th/0012233; Deninger, arXiv:2301.11643; Álvarez López et al.,
arXiv:2410.20758; Connes, DOI `10.1007/s000290050042`; Connes–Consani,
arXiv:1507.05818; Lapidus–Maier, DOI `10.1112/jlms/52.1.15`;
Milne, arXiv:1509.00797; Harder–Thompson, arXiv:1501.04049.
