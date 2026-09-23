#!/usr/bin/env python3
"""Build the hand-curated, sourced seed ontology and alias lexicon."""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = "rh/paper/rh_program.tex"
LEAN = "rh/lean/RH"
CLASSICAL = "DLMF §25.10"
WEIL = "A. Weil, Commun. Sem. Math. Univ. Lund, Suppl. (1952), pp. 252–265"

nodes: list[dict] = []
edges: list[dict] = []


def node(
    id_: str,
    type_: str,
    name: str,
    aliases: list[str],
    definition: str,
    status: str,
    sources: list[str],
    tags: list[str],
) -> None:
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", id_), id_
    assert len(definition.split()) <= 60, (id_, len(definition.split()))
    nodes.append({
        "id": id_, "type": type_, "name": name, "aliases": aliases,
        "definition": definition, "status": status, "sources": sources,
        "tags": tags, "attempt_count": 0, "alive": status == "CLASSICAL",
    })


def edge(
    src: str,
    dst: str,
    rel: str,
    strength: str,
    source: str,
    note: str = "",
) -> None:
    edges.append({
        "src": src, "dst": dst, "rel": rel, "strength": strength,
        "source": source, "note": note,
    })


# Classification anchors.
for row in [
    ("analytic-object", "Analytic object", "Functions, transforms, measures, and formulas used in analytic number theory."),
    ("positivity-criterion", "Positivity criterion", "A criterion phrased as positivity or nonnegativity of a form, sequence, kernel, or matrix."),
    ("spectral-framework", "Spectral framework", "An operator, trace formula, or spectral model used to organize RH-adjacent questions."),
    ("arithmetic-geometry", "Arithmetic geometry", "Geometric and cohomological structures carrying arithmetic information."),
    ("tfpt-compiler", "TFPT compiler structure", "A project-internal finite structure or bridge, with no implication to RH unless an explicit sourced edge says so."),
    ("obstruction-class", "Obstruction class", "A typed reason that a proposed route is blocked, killed, circular, or incomplete."),
    ("research-question", "Research question", "A currently open, explicitly sourced reduction or missing bridge."),
]:
    node(row[0], "CLASS", row[1], [], row[2], "CLASSICAL", ["rh/catalog/map/README.md:1"], ["class"])

# RH core objects, invariants, methods, and criteria.
core = [
    ("riemann-zeta", "OBJECT", "Riemann zeta function ζ(s)", ["zeta", "ζ(s)"], "The meromorphic continuation of the Dirichlet series Σn⁻ˢ, with Euler product in Re(s)>1.", "CLASSICAL", [CLASSICAL], ["rh-core"]),
    ("riemann-xi", "OBJECT", "Riemann xi function ξ(s)", ["xi", "ξ(s)", "Riemann xi"], "The completed entire zeta function, normalized to satisfy ξ(s)=ξ(1−s).", "CLASSICAL", [CLASSICAL], ["rh-core"]),
    ("riemann-hypothesis", "OPEN_QUESTION", "Riemann Hypothesis", ["RH", "RiemannHypothesis"], "The assertion that every nontrivial zero of ζ has real part one half.", "OPEN", [CLASSICAL], ["rh-core"]),
    ("critical-line", "GEOMETRY", "Critical line", ["Re(s)=1/2", "critical line"], "The vertical line Re(s)=1/2 in the critical strip.", "CLASSICAL", [CLASSICAL], ["rh-core"]),
    ("critical-strip", "GEOMETRY", "Critical strip", ["critical strip"], "The strip 0<Re(s)<1 containing the nontrivial zeta zeros.", "CLASSICAL", [CLASSICAL], ["rh-core"]),
    ("riemann-kernel", "OBJECT", "Riemann kernel Φ(u)", ["Phi(u)", "Φ(u)", "Riemann kernel"], "The classical even rapidly decaying kernel whose Fourier transform gives Ξ on the critical line.", "CLASSICAL", ["Titchmarsh, The Theory of the Riemann Zeta-function, §2.16"], ["fourier"]),
    ("xi-fourier-function", "OBJECT", "Ξ(t)", ["Xi(t)", "Ξ(t)"], "The real even function ξ(1/2+it), represented as a Fourier transform of the Riemann kernel.", "CLASSICAL", ["Titchmarsh, The Theory of the Riemann Zeta-function, §2.16"], ["fourier"]),
    ("fourier-transform", "METHOD", "Fourier transform", ["Fourier", "Fourier pair"], "The integral transform exchanging a function with its frequency representation.", "CLASSICAL", ["DLMF §1.14"], ["transform"]),
    ("mellin-transform", "METHOD", "Mellin transform", ["Mellin", "Mellin transform M"], "The multiplicative transform M[f](s)=∫₀∞f(x)xˢ⁻¹dx.", "CLASSICAL", ["DLMF §2.5"], ["transform"]),
    ("laplace-transform", "METHOD", "Laplace transform", ["Laplace transform"], "The integral transform f↦∫₀∞e⁻ˢᵗf(t)dt.", "CLASSICAL", ["DLMF §1.14"], ["transform"]),
    ("functional-equation", "THEOREM", "Zeta functional equation", ["functional equation", "FE"], "The symmetry relating completed zeta values at s and 1−s.", "CLASSICAL", [CLASSICAL], ["rh-core"]),
    ("explicit-formula", "THEOREM", "Riemann–Weil explicit formula", ["explicit formula", "Weil explicit formula"], "A distributional identity relating sums over zeta zeros to prime-power and archimedean terms.", "CLASSICAL", [WEIL], ["rh-core"]),
    ("von-mangoldt", "OBJECT", "von Mangoldt function Λ(n)", ["von Mangoldt", "Λ(n)", "Lambda(n)"], "The arithmetic weight log p on prime powers pᵏ and zero otherwise.", "CLASSICAL", ["DLMF §27.10"], ["prime"]),
    ("chebyshev-psi", "OBJECT", "Chebyshev ψ(x)", ["Chebyshev psi", "ψ(x)"], "The summatory function Σn≤x Λ(n).", "CLASSICAL", ["DLMF §27.2"], ["prime"]),
    ("prime-counting", "OBJECT", "Prime-counting function π(x)", ["prime counting", "π(x)"], "The number of primes not exceeding x.", "CLASSICAL", ["DLMF §27.2"], ["prime"]),
    ("zero-counting", "INVARIANT", "Zero-counting function N(T)", ["zero counting", "N(T)"], "The number of nontrivial zeta zeros with ordinate between zero and T, counted with multiplicity.", "CLASSICAL", ["Titchmarsh, The Theory of the Riemann Zeta-function, Thm. 9.3"], ["zeros"]),
    ("pair-correlation", "INVARIANT", "Pair correlation of zeta zeros", ["pair correlation"], "The limiting local two-point statistic conjectured for normalized zeta ordinates.", "CONJECTURAL", ["Montgomery, Proc. Symp. Pure Math. 24 (1973)"], ["zeros"]),
    ("gue-statistics", "CLASS", "GUE statistics", ["GUE", "Gaussian unitary ensemble"], "The local eigenvalue statistics of large random Hermitian matrices in the unitary symmetry class.", "CLASSICAL", ["Mehta, Random Matrices, 3rd ed."], ["random-matrix"]),
    ("montgomery-conjecture", "OPEN_QUESTION", "Montgomery pair-correlation conjecture", ["Montgomery conjecture"], "The conjecture that normalized zeta-zero pair correlation agrees with the GUE sine-kernel law.", "OPEN", ["Montgomery, Proc. Symp. Pure Math. 24 (1973)"], ["zeros"]),
    ("weil-quadratic-form", "OBJECT", "Weil quadratic form Q(f)", ["Weil form", "Q(f)", "Weil quadratic form"], "The explicit-formula quadratic functional whose positivity on the admissible test class is equivalent to RH.", "CLASSICAL", [WEIL], ["weil"]),
    ("weil-arch-term", "OBJECT", "Weil archimedean term", ["arch term", "archimedean term", "ARCH"], "The gamma-factor contribution to the Weil explicit-formula quadratic form.", "CLASSICAL", [WEIL], ["weil"]),
    ("weil-prime-term", "OBJECT", "Weil prime term", ["prime term", "PRIME"], "The prime-power contribution, weighted by the von Mangoldt function, in the Weil form.", "CLASSICAL", [WEIL], ["weil"]),
    ("weil-pole-term", "OBJECT", "Weil pole term", ["pole term", "POLE"], "The contribution of the pole and trivial normalization terms in the Weil form.", "CLASSICAL", [WEIL], ["weil"]),
    ("weil-positivity", "CRITERION", "Weil positivity criterion", ["Weil positivity", "Weil criterion"], "Nonnegativity of the Weil quadratic form on the full admissible test class.", "CLASSICAL", [WEIL], ["rh-equivalent", "weil"]),
    ("gabor-zero-side", "OBJECT", "Gabor zero side", ["gaborZeroSide", "Gabor zero-side"], "The zero-side functional evaluated on the corpus pure-Gabor two-parameter test family.", "FORMALIZED_LEAN", [f"{LEAN}/GaborSeparation.lean:1998"], ["gabor"]),
    ("pure-gabor-family", "CLASS", "Pure Gabor test family", ["pureGaborTest", "pure Gabor"], "The two-parameter Gaussian wavepacket family indexed by a>0 and frequency ω.", "FORMALIZED_LEAN", [f"{LEAN}/GaborCountableCriterion.lean:526"], ["gabor"]),
    ("gabor-pure-criterion", "CRITERION", "Pure-Gabor zero-side criterion", ["gabor pure criterion", "gabor_zeroSide_pure_criterion_iff_rh_unconditional"], "Nonnegativity of the Gabor zero side for every pure-Gabor packet.", "FORMALIZED_LEAN", [f"{LEAN}/GaborExposedOrbit.lean:1718"], ["rh-equivalent", "gabor"]),
    ("gabor-rational-criterion", "CRITERION", "Rational pure-Gabor criterion", ["gabor rational criterion", "gabor_zeroSide_rational_criterion_iff_rh_unconditional"], "Nonnegativity of the pure-Gabor zero side on positive rational scales and rational frequencies.", "FORMALIZED_LEAN", [f"{LEAN}/GaborCountableCriterion.lean:540"], ["rh-equivalent", "gabor"]),
    ("gabor-prime-side-criterion", "CRITERION", "Gabor prime-side rational criterion", ["gabor prime-side criterion", "gabor_primeSide_rational_criterion_iff_rh"], "The rational pure-Gabor criterion rewritten using the pole, prime-comb, and archimedean sides.", "FORMALIZED_LEAN", [f"{LEAN}/GaborCountableCriterion.lean:550"], ["rh-equivalent", "gabor"]),
    ("li-coefficients", "INVARIANT", "Li coefficients λₙ", ["Li coefficients", "Li lambda", "λ_n"], "Coefficients obtained from derivatives of log ξ at s=1 in Li's criterion.", "CLASSICAL", ["Li, J. Number Theory 65 (1997), DOI:10.1006/jnth.1997.2138"], ["rh-core"]),
    ("li-criterion", "CRITERION", "Li criterion", ["Li's criterion", "Li criterion"], "Nonnegativity of all Li coefficients.", "CLASSICAL", ["Li, J. Number Theory 65 (1997), DOI:10.1006/jnth.1997.2138"], ["rh-equivalent"]),
    ("nyman-beurling-space", "OBJECT", "Nyman–Beurling closure space", ["Nyman-Beurling space"], "The closed span in L²(0,1) of fractional-part combinations satisfying the Nyman–Beurling constraint.", "CLASSICAL", ["Nyman, Ark. Mat. 1 (1950); Beurling, Proc. Nat. Acad. Sci. 41 (1955)"], ["hilbert-space"]),
    ("nyman-beurling-criterion", "CRITERION", "Nyman–Beurling criterion", ["Nyman-Beurling", "Nyman–Beurling"], "The closure criterion for approximating the constant function in L²(0,1).", "CLASSICAL", ["Beurling, Proc. Nat. Acad. Sci. 41 (1955)"], ["rh-equivalent"]),
    ("baez-duarte-criterion", "CRITERION", "Báez-Duarte criterion", ["Baez-Duarte", "Báez-Duarte"], "A discrete Nyman–Beurling approximation criterion equivalent to RH.", "CLASSICAL", ["Báez-Duarte, Adv. Math. 178 (2003), DOI:10.1016/S0001-8708(02)00041-5"], ["rh-equivalent"]),
    ("hardy-space-h2", "OBJECT", "Hardy space H²", ["Hardy H2", "H²"], "The Hilbert space of analytic functions with square-integrable boundary values in the relevant half-plane or disk model.", "CLASSICAL", ["Duren, Theory of Hᵖ Spaces"], ["hilbert-space"]),
    ("debruijn-newman-constant", "INVARIANT", "de Bruijn–Newman constant Λ", ["de Bruijn-Newman Lambda", "Newman constant"], "The threshold heat-flow parameter above which the deformed Riemann Fourier transform has only real zeros.", "CLASSICAL", ["Rodgers–Tao, Forum Math. Pi 8 (2020), arXiv:1801.05914"], ["zeros"]),
    ("rodgers-tao-theorem", "THEOREM", "Rodgers–Tao theorem Λ≥0", ["Lambda >= 0", "Rodgers-Tao"], "The theorem that the de Bruijn–Newman constant is nonnegative.", "CLASSICAL", ["Rodgers–Tao, Forum Math. Pi 8 (2020), arXiv:1801.05914"], ["zeros"]),
    ("newman-criterion", "CRITERION", "Newman heat-flow criterion", ["Newman's criterion"], "The criterion identifying RH with the equality Λ=0, given the classical upper implication and Λ≥0.", "CLASSICAL", ["Rodgers–Tao, Forum Math. Pi 8 (2020), arXiv:1801.05914"], ["rh-equivalent"]),
    ("laguerre-polya-class", "CLASS", "Laguerre–Pólya class", ["Laguerre-Polya", "LP class"], "The class of real entire functions locally approximable by real-rooted polynomials.", "CLASSICAL", ["Levin, Distribution of Zeros of Entire Functions, Ch. VIII"], ["entire"]),
    ("hermite-biehler-class", "CLASS", "Hermite–Biehler class", ["Hermite-Biehler", "HB class"], "Entire functions E satisfying |E(z)|>|E*(z)| in the upper half-plane.", "CLASSICAL", ["de Branges, Hilbert Spaces of Entire Functions"], ["entire"]),
    ("debranges-space", "OBJECT", "de Branges space", ["de Branges space"], "A Hilbert space of entire functions generated by a Hermite–Biehler function.", "CLASSICAL", ["de Branges, Hilbert Spaces of Entire Functions"], ["operator"]),
    ("lee-yang-property", "CRITERION", "Lee–Yang property", ["Lee-Yang", "Lee–Yang"], "A zero-location property placing partition-function zeros on a prescribed circle or line after normalization.", "CLASSICAL", ["Lee–Yang, Phys. Rev. 87 (1952), DOI:10.1103/PhysRev.87.410"], ["zeros"]),
    ("kps-theorem", "THEOREM", "KPS van Dantzig theorem", ["KPS theorem", "van Dantzig pair"], "A sourced theorem connecting specified characteristic-function pairs and Lee–Yang-type zero geometry; the map records only the corpus-used formulation.", "CLASSICAL", [f"{PAPER}:4130"], ["lee-yang"]),
    ("van-dantzig-pair", "OBJECT", "van Dantzig pair", ["van Dantzig pairs"], "A pair of characteristic functions related by reciprocal analytic continuation in the van Dantzig problem.", "CLASSICAL", [f"{PAPER}:4130"], ["probability"]),
    ("polya-frequency-function", "CLASS", "Pólya frequency function", ["PF function", "Polya frequency"], "A function whose translation kernel is totally positive of all orders.", "CLASSICAL", ["Karlin, Total Positivity, Vol. I"], ["positivity"]),
    ("toeplitz-positivity", "CRITERION", "Toeplitz positivity", ["Toeplitz minors", "Toeplitz positivity"], "Positive semidefiniteness or total positivity conditions on Toeplitz matrices formed from a coefficient sequence.", "CLASSICAL", ["Karlin, Total Positivity, Vol. I"], ["matrix"]),
    ("hankel-positivity", "CRITERION", "Hankel moment positivity", ["Hankel positivity", "Hankel minors"], "Positive semidefiniteness of Hankel matrices built from a moment or coefficient sequence.", "CLASSICAL", ["Akhiezer, The Classical Moment Problem"], ["matrix"]),
    ("jensen-polynomials", "OBJECT", "Jensen polynomials", ["Jensen polynomial"], "Polynomials built from consecutive Taylor coefficients of an entire function.", "CLASSICAL", ["Griffin–Ono–Rolen–Zagier, PNAS 116 (2019), DOI:10.1073/pnas.1902572116"], ["polynomial"]),
    ("jensen-hyperbolicity", "CRITERION", "Jensen polynomial hyperbolicity", ["Jensen hyperbolicity"], "Real-rootedness of every Jensen polynomial in the degree and shift range specified by the criterion.", "CLASSICAL", ["Pólya–Schur, J. Reine Angew. Math. 144 (1914)"], ["rh-equivalent"]),
    ("gorz-theorem", "THEOREM", "GORZ Jensen-polynomial theorem", ["Griffin-Ono-Rolen-Zagier", "GORZ"], "The theorem that fixed-degree Jensen polynomials associated with ξ are eventually hyperbolic with Hermite asymptotics.", "CLASSICAL", ["Griffin–Ono–Rolen–Zagier, PNAS 116 (2019), DOI:10.1073/pnas.1902572116"], ["polynomial"]),
]
for row in core:
    node(*row)

# Spectral, geometric, analytic, and corpus methods.
more = [
    ("hilbert-polya-operator", "OPERATOR", "Hilbert–Pólya operator", ["Hilbert-Polya", "Hilbert–Pólya"], "A conjectural self-adjoint operator whose spectrum would encode nontrivial zeta ordinates.", "CONJECTURAL", ["Pólya correspondence, 1912–1914; Hilbert reported by Conrey (2003)"], ["spectral"]),
    ("berry-keating-xp", "OPERATOR", "Berry–Keating xp Hamiltonian", ["Berry-Keating", "xp Hamiltonian"], "A semiclassical dilation Hamiltonian proposed as a model for the average zeta-zero counting law.", "CONJECTURAL", ["Berry–Keating, SIAM Review 41 (1999), DOI:10.1137/S0036144598347497"], ["spectral"]),
    ("connes-trace-formula", "METHOD", "Connes trace formula", ["Connes trace formula"], "A noncommutative-geometric trace-formula approach representing zeta zeros through an absorption spectrum.", "CONJECTURAL", ["Connes, Selecta Math. 5 (1999), DOI:10.1007/s000290050054"], ["spectral"]),
    ("adele-class-space", "GEOMETRY", "Adele class space", ["adele class space"], "The quotient of the adele ring by the multiplicative action of the global field.", "CLASSICAL", ["Connes, Selecta Math. 5 (1999), DOI:10.1007/s000290050054"], ["adelic"]),
    ("scaling-site", "GEOMETRY", "Connes–Consani scaling site", ["scaling site"], "A characteristic-one geometric framework carrying scaling and arithmetic-site structures.", "CLASSICAL", ["Connes–Consani, arXiv:1507.05818"], ["adelic"]),
    ("selberg-trace-formula", "THEOREM", "Selberg trace formula", ["Selberg trace formula"], "An identity relating spectral data of a hyperbolic quotient to lengths of closed geodesics.", "CLASSICAL", ["Selberg, J. Indian Math. Soc. 20 (1956)"], ["trace"]),
    ("modular-surface", "GEOMETRY", "Modular surface", ["PSL2Z quotient", "modular surface"], "The finite-area hyperbolic orbifold PSL₂(Z)\\H.", "CLASSICAL", ["Iwaniec, Spectral Methods of Automorphic Forms"], ["automorphic"]),
    ("eisenstein-series", "OBJECT", "Eisenstein series", ["Eisenstein series"], "A noncuspidal automorphic eigenfunction formed by summing a height function over a parabolic quotient.", "CLASSICAL", ["Iwaniec, Spectral Methods of Automorphic Forms"], ["automorphic"]),
    ("eisenstein-constant-term", "OBJECT", "Eisenstein constant term", ["constant term", "scattering term"], "The two-term Fourier coefficient encoding the scattering coefficient of an Eisenstein series.", "CLASSICAL", ["Iwaniec, Spectral Methods of Automorphic Forms, Ch. 3"], ["automorphic"]),
    ("epstein-zeta", "OBJECT", "Epstein zeta function", ["Epstein zeta"], "The zeta function obtained by summing powers of a positive quadratic form over nonzero lattice vectors.", "CLASSICAL", ["DLMF §25.11"], ["automorphic"]),
    ("hecke-operator", "OPERATOR", "Hecke operator", ["Hecke operators"], "A commuting arithmetic correspondence acting on automorphic forms.", "CLASSICAL", ["Miyake, Modular Forms, Ch. 4"], ["automorphic"]),
    ("hecke-correspondence", "GEOMETRY", "Hecke correspondence", ["Hecke correspondences"], "An algebraic or adelic correspondence whose induced action gives a Hecke operator.", "CLASSICAL", ["Miyake, Modular Forms, Ch. 4"], ["automorphic"]),
    ("bruhat-tits-tree", "GEOMETRY", "Bruhat–Tits tree of PGL₂(Qₚ)", ["Bruhat-Tits tree", "PGL2(Qp) tree"], "The regular tree of homothety classes of rank-two Zₚ-lattices.", "CLASSICAL", ["Serre, Trees, Ch. II"], ["padic"]),
    ("bost-connes-system", "OBJECT", "Bost–Connes system", ["Bost-Connes", "BC system"], "A quantum statistical mechanical system whose partition function is ζ and whose symmetries encode class-field data.", "CLASSICAL", ["Bost–Connes, Selecta Math. 1 (1995), DOI:10.1007/BF01589495"], ["operator-algebra"]),
    ("arakelov-intersection", "GEOMETRY", "Arakelov intersection theory", ["Arakelov"], "Intersection theory on arithmetic varieties combining finite-place and archimedean contributions.", "CLASSICAL", ["Gillet–Soulé, Publ. Math. IHÉS 72 (1990)"], ["arithmetic-geometry"]),
    ("arithmetic-hodge-index", "THEOREM", "Arithmetic Hodge index theorem", ["arithmetic Hodge index", "Yuan-Zhang"], "A negativity theorem for arithmetic intersections orthogonal to a polarization, in the hypotheses of Yuan–Zhang.", "CLASSICAL", ["Yuan–Zhang, Math. Ann. 367 (2017), DOI:10.1007/s00208-016-1391-8"], ["arithmetic-geometry"]),
    ("deninger-cohomology", "METHOD", "Deninger cohomological program", ["Deninger cohomology"], "A conjectural cohomological and dynamical framework intended to model arithmetic zeta functions by regularized determinants.", "CONJECTURAL", ["Deninger, Proc. ICM Berlin 1998, Doc. Math. Extra Vol. I"], ["cohomology"]),
    ("weil-conjectures", "THEOREM", "Weil conjectures over finite fields", ["Weil conjectures"], "The rationality, functional equation, Betti-number interpretation, and Riemann-hypothesis bounds for zeta functions of smooth projective varieties over finite fields.", "CLASSICAL", ["Deligne, Publ. Math. IHÉS 43 (1974)"], ["function-field"]),
    ("deligne-rh", "THEOREM", "Deligne's function-field RH theorem", ["Deligne theorem"], "The weight theorem proving the Riemann-hypothesis part of the Weil conjectures.", "CLASSICAL", ["Deligne, Publ. Math. IHÉS 43 (1974)"], ["function-field"]),
    ("pick-function", "CLASS", "Pick function", ["Pick", "Nevanlinna function"], "A holomorphic function mapping the upper half-plane into itself.", "CLASSICAL", ["Donoghue, Monotone Matrix Functions and Analytic Continuation"], ["complex-analysis"]),
    ("herglotz-function", "CLASS", "Herglotz function", ["Herglotz", "Herglotz-Nevanlinna"], "A Pick function represented by a positive measure through the Herglotz formula.", "CLASSICAL", ["Donoghue, Monotone Matrix Functions and Analytic Continuation"], ["complex-analysis"]),
    ("bernstein-function", "CLASS", "Bernstein function", ["Bernstein function"], "A nonnegative smooth function whose derivative is completely monotone.", "CLASSICAL", ["Schilling–Song–Vondraček, Bernstein Functions, 2nd ed."], ["positivity"]),
    ("completely-monotone", "CLASS", "Completely monotone function", ["complete monotonicity"], "A smooth function f on (0,∞) satisfying (−1)ⁿf⁽ⁿ⁾≥0 for every n.", "CLASSICAL", ["Widder, The Laplace Transform"], ["positivity"]),
    ("stieltjes-function", "CLASS", "Stieltjes function", ["Stieltjes function"], "A function representable as a nonnegative constant plus an integral of 1/(x+t) against a positive measure.", "CLASSICAL", ["Schilling–Song–Vondraček, Bernstein Functions, Ch. 7"], ["positivity"]),
    ("carlson-theorem", "THEOREM", "Carlson uniqueness theorem", ["Carlson's theorem"], "A uniqueness theorem for entire functions of restricted exponential type from values on the nonnegative integers.", "CLASSICAL", ["Titchmarsh, Theory of Functions, §5.81"], ["complex-analysis"]),
    ("saddle-point-method", "METHOD", "Saddle-point method", ["saddle point", "steepest descent"], "An asymptotic method based on deforming an integral through critical points of its phase.", "CLASSICAL", ["DLMF §2.4"], ["asymptotic"]),
    ("lambert-w", "OBJECT", "Lambert W function", ["Lambert-W", "Lambert W"], "The multivalued inverse of w↦weʷ.", "CLASSICAL", ["DLMF §4.13"], ["asymptotic"]),
    ("prolate-operator", "OPERATOR", "Prolate spheroidal concentration operator", ["prolate", "PSWF"], "The time–band limiting integral operator whose eigenvalues quantify simultaneous concentration.", "CLASSICAL", ["Slepian–Pollak, Bell Syst. Tech. J. 40 (1961)"], ["spectral"]),
    ("landau-widom-asymptotics", "THEOREM", "Landau–Widom concentration asymptotics", ["Landau-Widom"], "Asymptotics for the transition region of eigenvalues of time–frequency concentration operators.", "CLASSICAL", ["Landau–Widom, J. Math. Anal. Appl. 77 (1980), DOI:10.1016/0022-247X(80)90269-9"], ["spectral"]),
    ("prime-torus", "GEOMETRY", "Prime torus", ["prime polytorus", "Bohr torus"], "The infinite product torus whose coordinates encode prime phases in the Bohr lift of Dirichlet series.", "CLASSICAL", ["Hedenmalm–Lindqvist–Seip, Duke Math. J. 86 (1997)"], ["dirichlet"]),
    ("bohr-lift", "METHOD", "Bohr lift", ["Bohr transform"], "The correspondence sending a Dirichlet series to a power series on a polytorus by prime factorization.", "CLASSICAL", ["Hedenmalm–Lindqvist–Seip, Duke Math. J. 86 (1997)"], ["dirichlet"]),
    ("dirichlet-series-polytorus", "OBJECT", "Dirichlet series on the polytorus", ["Dirichlet polytorus"], "The analytic function on an infinite polydisk obtained from a Dirichlet series through the Bohr lift.", "CLASSICAL", ["Hedenmalm–Lindqvist–Seip, Duke Math. J. 86 (1997)"], ["dirichlet"]),
    ("hypercontractivity", "THEOREM", "Hypercontractivity on the prime torus", ["hypercontractivity"], "Norm-improving estimates for the prime-torus semigroup acting on Bohr lifts.", "CLASSICAL", ["Weissler, J. Funct. Anal. 32 (1979)"], ["dirichlet"]),
    ("beurling-deny-criterion", "CRITERION", "Beurling–Deny criterion", ["Beurling-Deny"], "A criterion characterizing Dirichlet forms by Markovian contraction properties.", "CLASSICAL", ["Fukushima–Oshima–Takeda, Dirichlet Forms, Thm. 1.4.1"], ["semigroup"]),
    ("positivity-semigroup", "OPERATOR", "Positivity-preserving semigroup", ["Markov semigroup"], "A semigroup of operators preserving the positive cone.", "CLASSICAL", ["Fukushima–Oshima–Takeda, Dirichlet Forms"], ["semigroup"]),
    ("cuntz-system", "OPERATOR", "Cuntz system", ["Cuntz algebra", "Cuntz system"], "Isometries with orthogonal ranges summing to the identity, generating a Cuntz algebra.", "CLASSICAL", ["Cuntz, Comm. Math. Phys. 57 (1977)"], ["operator-algebra"]),
    ("ucp-map", "OPERATOR", "Unital completely positive map", ["UCP", "UCP map"], "A unital linear map whose matrix amplifications preserve positivity.", "CLASSICAL", ["Paulsen, Completely Bounded Maps and Operator Algebras"], ["operator-algebra"]),
    ("groupoid", "GEOMETRY", "Measured groupoid", ["groupoid"], "A groupoid equipped with measure-class data suitable for convolution and operator-algebra constructions.", "CLASSICAL", ["Renault, A Groupoid Approach to C*-algebras"], ["groupoid"]),
    ("groupoid-modular-function", "INVARIANT", "Groupoid modular function", ["modular function"], "The Radon–Nikodym cocycle comparing left and right measures on a measured groupoid.", "CLASSICAL", ["Renault, A Groupoid Approach to C*-algebras"], ["groupoid"]),
    ("half-density", "OBJECT", "Groupoid half-density", ["half-density", "halfdensity"], "A square-root density used to define intrinsic convolution without choosing a unimodular measure.", "CLASSICAL", ["Connes, Noncommutative Geometry, Ch. II"], ["groupoid"]),
    ("additive-adeles", "GEOMETRY", "Additive adeles", ["additive adeles", "A_Q"], "The restricted product of all completions of Q under addition.", "CLASSICAL", ["Tate, Thesis, 1950"], ["adelic"]),
    ("self-dual-measure", "OBJECT", "Self-dual Haar measure", ["self-dual measure"], "The Haar measure normalized so Fourier inversion is self-dual for a chosen additive character.", "CLASSICAL", ["Tate, Thesis, 1950"], ["adelic"]),
    ("relative-determinant", "INVARIANT", "Relative determinant", ["relative determinant"], "A regularized determinant comparing two operators when their resolvent difference has suitable trace class.", "CLASSICAL", ["Müller, Comm. Math. Phys. 192 (1998)"], ["spectral"]),
    ("spectral-shift", "INVARIANT", "Krein spectral shift function", ["spectral shift", "Krein"], "A function encoding trace differences f(A)−f(B) for suitable self-adjoint operator pairs.", "CLASSICAL", ["Krein, Mat. Sb. 33 (1953)"], ["spectral"]),
    ("vitali-montel", "THEOREM", "Vitali–Montel normal-family principle", ["Vitali", "Montel", "normal family"], "Local boundedness plus convergence on a uniqueness set yields compactness and analytic convergence in standard normal-family formulations.", "CLASSICAL", ["Conway, Functions of One Complex Variable I, Ch. VII"], ["complex-analysis"]),
    ("euler-gross-entropy-gap", "INVARIANT", "Euler–Gross entropy gap", ["Euler-Gross entropy"], "A corpus diagnostic comparing arithmetic Euler structure with Gaussian or control-world entropy.", "PROVED_HERE", [f"{PAPER}:4040"], ["corpus"]),
    ("ising-lee-yang-compiler", "METHOD", "Ising/Lee–Yang compiler", ["Ising compiler"], "A corpus route translating finite interaction data into a Lee–Yang polynomial test.", "OPEN", [f"{PAPER}:4130"], ["corpus"]),
    ("cusp-surgery", "METHOD", "Cusp surgery", ["cusp surgery"], "A geometric degeneration method relating determinant data before and after cutting or truncating a cusp.", "CLASSICAL", ["Efrat, Comm. Math. Phys. 119 (1988)"], ["spectral"]),
    ("efrat-determinant", "THEOREM", "Efrat determinant formula", ["Efrat determinant"], "A determinant identity for hyperbolic surfaces with cusps in the cited formulation.", "CLASSICAL", ["Efrat, Comm. Math. Phys. 119 (1988)"], ["spectral"]),
    ("regulator-jump", "INVARIANT", "Regulator jump", ["regulator jump"], "A measured discontinuity or large change in a regulator-like quantity used by the corpus factoring geometry.", "OPEN", ["experiments/tfpt-discovery/regulator_jump_probe.py:1"], ["unrelated-rh"]),
    ("murru-salvatori", "METHOD", "Murru–Salvatori regulator method", ["Murru-Salvatori"], "The external regulator/factorization proposal audited by the corpus; it is not an RH mechanism.", "OPEN", ["experiments/tfpt-discovery/regulator_relation_result.json"], ["external", "unrelated-rh"]),
    ("openai-long-prime-gaps", "METHOD", "OpenAI 2026 long-prime-gap work", ["long prime gaps", "OpenAI prime gaps"], "An external long-prime-gap result tracked by the corpus and explicitly classified as unrelated to RH.", "OPEN", ["rh/catalog/fragments/part_8.json"], ["external", "unrelated-rh"]),
    ("chuk-window-certificate", "CRITERION", "Chuk compact-window certificate at L=0.8", ["Chuk", "L=0.8 certificate"], "The compact-window positivity certificate reproduced by the corpus at L=0.8; it is finite-window evidence, not an RH claim.", "PROVED_HERE", ["experiments/tfpt-discovery/weil_window_certificate_result.json"], ["external", "finite"]),
    ("cubic-wedges", "METHOD", "Cubic wedges of arXiv:2607.16795", ["2607.16795", "cubic wedges"], "The external cubic-wedge construction audited by the corpus without promotion to an RH implication.", "OPEN", ["arXiv:2607.16795"], ["external"]),
]
for row in more:
    node(*row)

# TFPT structures and project-internal reductions.
tfpt = [
    ("tfpt-c3", "TFPT_STRUCTURE", "TFPT axiom c3=1/(8π)", ["c3", "1/(8π)"], "The project compiler's declared c3 normalization.", "PROVED_HERE", ["tfpt_1_architecture_e8.tex:1"], ["tfpt"]),
    ("tfpt-gcar", "TFPT_STRUCTURE", "TFPT axiom g_car=5", ["g_car", "gcar"], "The project compiler's declared carrier count.", "PROVED_HERE", ["tfpt_1_architecture_e8.tex:1"], ["tfpt"]),
    ("tfpt-e8-compiler", "TFPT_STRUCTURE", "D5⊕A3+μ4⇒E8 compiler", ["D5+A3", "mu4 E8"], "The project-internal finite compiler from D5, A3, and μ4 data to E8.", "PROVED_HERE", ["tfpt_1_architecture_e8.tex:1"], ["tfpt"]),
    ("tfpt-e8-lattice", "TFPT_STRUCTURE", "E8 lattice", ["E8 lattice", "E8"], "The even unimodular rank-eight lattice as used by the TFPT compiler.", "CLASSICAL", ["Conway–Sloane, Sphere Packings, Lattices and Groups"], ["tfpt", "lattice"]),
    ("e8-theta-series", "OBJECT", "E8 theta series", ["E8 theta", "Theta_E8"], "The theta series of the E8 lattice, equal to the weight-four Eisenstein series E4.", "CLASSICAL", ["Serre, A Course in Arithmetic, Ch. VII"], ["lattice"]),
    ("e8-cascade", "TFPT_STRUCTURE", "E8 cascade", ["E8 cascade"], "The project-internal cascade of finite E8 readouts.", "PROVED_HERE", [f"{PAPER}:4094"], ["tfpt"]),
    ("cm-seam", "TFPT_STRUCTURE", "CM seam τ=i", ["tau=i", "CM seam", "Gaussian seam"], "The Gaussian complex-multiplication seam used by TFPT arithmetic constructions.", "PROVED_HERE", ["note_e8_gaussian_code.tex:1"], ["tfpt", "cm"]),
    ("gaussian-e8-module", "TFPT_STRUCTURE", "Gaussian E8 module", ["Gaussian E8", "v714"], "The Gaussian E8 module and Hecke-groupoid data audited in verification v714.", "PROVED_HERE", ["verification/v714_e8_gaussian_hecke_groupoid.py:1"], ["tfpt"]),
    ("main-world", "CLASS", "MAIN world control", ["MAIN"], "The corpus arithmetic data world against which smooth and scrambled controls are compared.", "PROVED_HERE", [f"{PAPER}:940"], ["control"]),
    ("smooth-world", "CLASS", "SMOOTH world control", ["SMOOTH"], "A smoothed control world used to test arithmetic specificity.", "PROVED_HERE", [f"{PAPER}:940"], ["control"]),
    ("scrarith-world", "CLASS", "SCRARITH world control", ["SCRARITH"], "A scrambled-arithmetic control preserving selected marginals while destroying arithmetic organization.", "PROVED_HERE", [f"{PAPER}:940"], ["control"]),
    ("seam-geodesic", "TFPT_STRUCTURE", "Seam geodesic", ["seam geodesic"], "A project geometric factoring route along the Gaussian seam; classified as unrelated to RH.", "OPEN", ["experiments/tfpt-discovery/seam_geodesic_infrastructure_result.json"], ["tfpt", "unrelated-rh"]),
    ("gate-zero", "TFPT_STRUCTURE", "Gate 0", ["Gate 0"], "The corpus name for the initial adelic/groupoid compatibility gate.", "OPEN", [f"{PAPER}:3644"], ["tfpt", "adelic"]),
    ("plastic-number-threshold", "INVARIANT", "Plastic-number threshold", ["plastic number", "plastic threshold"], "A corpus finite threshold involving the real root of x³=x+1.", "PROVED_HERE", [f"{PAPER}:1210"], ["tfpt"]),
    ("terminal-statement", "OPEN_QUESTION", "Terminal cross-ratio statement", ["terminal q", "q_N<1", "terminal inequality"], "The open cofinal terminal inequality q_N<1 in the corpus reduction.", "OPEN", [f"{PAPER}:3535"], ["tfpt", "open"]),
    ("lstar-statement", "OPEN_QUESTION", "L* subordination statement", ["L*", "Lstar", "lemma L*"], "The canonical open subordination inequality for the corpus free-window reduction.", "OPEN", [f"{PAPER}:774"], ["tfpt", "open"]),
    ("lambda-star-ladder", "INVARIANT", "λ*(L) ladder", ["lambda*", "λ*", "lambda-star"], "The scale-indexed minimum-margin ladder measured in compact Weil-window experiments.", "OPEN", [f"{PAPER}:3293"], ["tfpt", "finite"]),
    ("quadrep", "TFPT_STRUCTURE", "Quadrep", ["quadrep"], "The project finite quadratic representation bridge tracked by the RH corpus.", "PROVED_HERE", ["rh/problem/verify_quadrep.py:1"], ["tfpt"]),
    ("inner-bridges", "TFPT_STRUCTURE", "Inner bridges", ["inner bridges"], "The corpus family of finite bridges internal to the compiler representation.", "PROVED_HERE", ["rh/problem/verify_inner_bridges.py:1"], ["tfpt"]),
    ("outer-bridges", "TFPT_STRUCTURE", "Outer bridges", ["outer bridges"], "The corpus family of finite bridges from compiler data toward external analytic objects.", "OPEN", ["rh/problem/verify_outer_bridges.py:1"], ["tfpt"]),
    ("relay-lead-law", "TFPT_STRUCTURE", "Relay lead law", ["relay lead law", "relay"], "A measured prime-event-log relation in the corpus; no RH implication is asserted.", "OPEN", ["experiments/tfpt-discovery/relay_lead_law_result.json"], ["tfpt", "prime"]),
    ("narrowband-weil", "METHOD", "Narrowband Weil probe", ["narrowband Weil"], "A finite-window Weil-form experiment restricted to narrow frequency bands.", "OPEN", ["experiments/tfpt-discovery/narrowband_weil_probe.py:1"], ["tfpt", "finite"]),
    ("arch-rate", "THEOREM", "Archimedean rate identity", ["arch rate"], "The corpus-isolated archimedean identity and selected-tent O(δ²) rate.", "PROVED_HERE", ["rh/problem/arch_rate.tex:1"], ["tfpt", "identity"]),
    ("extraction-joint", "OPEN_QUESTION", "Extraction joint", ["extraction joint"], "The missing joint transferring finite selected-window positivity to the full Weil test class.", "OPEN", [f"{PAPER}:1997"], ["tfpt", "open"]),
    ("finite-weil-window", "OBJECT", "Finite Weil window", ["compact Weil window", "window form"], "A finite-dimensional compression of the localized Weil form to a specified window and basis.", "PROVED_HERE", [f"{PAPER}:97"], ["tfpt", "finite"]),
    ("selected-window-family", "CLASS", "Selected-window family", ["selected windows"], "The project family of finite test windows used in the formalized extraction chain.", "FORMALIZED_LEAN", [f"{LEAN}/Selected.lean:444"], ["tfpt", "finite"]),
]
for row in tfpt:
    node(*row)

# Barriers and open questions.
barriers = [
    ("barrier-circularity", "Renamed RH-equivalent / circularity", ["circular", "renamed RH"], "A route assumes RH or a known equivalent under another name.", ["rh/catalog/taxonomy.json:46"]),
    ("barrier-prime-phase-coherence", "Prime-phase coherence", ["prime phase coherence"], "The missing control of correlated prime phases needed by several finite-to-global routes.", [f"{PAPER}:955"]),
    ("barrier-p2-defect", "p=2 defect", ["2-adic defect", "p=2 defect"], "A structural obstruction in the first 2-adic Weil channel.", [f"{PAPER}:3644"]),
    ("barrier-pole-mode", "Pole mode uncontrolled", ["pole mode"], "Failure to control the pole contribution uniformly in the proposed positivity transfer.", [f"{PAPER}:1925"]),
    ("barrier-arch-compensation", "Archimedean compensation", ["arch compensation"], "A mismatch where the archimedean channel compensates or reverses a prime-side sign.", [f"{PAPER}:1925"]),
    ("barrier-unimodularity", "Unimodularity / no half-density", ["unimodularity", "no half-density"], "The groupoid construction lacks the half-density or modular correction needed for intrinsic convolution.", ["experiments/tfpt-discovery/groupoid_halfdensity_result.json"]),
    ("barrier-zero-denominator", "Zero-bearing denominator", ["zero-bearing denominator"], "A proposed quotient places zeta zeros in its denominator, creating poles or circular sign information.", ["experiments/tfpt-discovery/mellin_cofactor_nonreal_zero_result.json"]),
    ("barrier-finite-window-ceiling", "Finite-window ceiling / Landau–Widom decay", ["finite-window ceiling", "Landau-Widom decay"], "Concentration eigenvalue decay prevents a fixed compact window from controlling the full test class.", [f"{PAPER}:2865"]),
    ("barrier-pick-sign", "Pick-sign violation", ["Pick sign violation"], "The candidate continuation violates the upper-half-plane sign required of a Pick function.", ["experiments/tfpt-discovery/mellin_pick_zero_residue_result.json"]),
    ("barrier-nonreal-cofactor-zeros", "Non-real cofactor zeros", ["non-real cofactor zeros"], "A Mellin cofactor has non-real zeros incompatible with the proposed Lee–Yang or Pick class.", ["experiments/tfpt-discovery/mellin_cofactor_nonreal_zero_result.json"]),
    ("barrier-world-blind", "World blindness", ["world blind", "WORLD_BLIND"], "The route does not distinguish arithmetic MAIN data from control worlds.", ["rh/catalog/taxonomy.json:47"]),
    ("barrier-lossy-constant", "Lossy constant", ["lossy constant"], "An inequality loses the quantitative margin required by the next reduction.", ["rh/catalog/taxonomy.json:48"]),
    ("barrier-structural-mismatch", "Structural mismatch", ["structural mismatch"], "The route identifies objects that are not mathematically the same object.", ["rh/catalog/taxonomy.json:49"]),
    ("barrier-no-bridge", "No bridge", ["NO_BRIDGE", "no bridge"], "The construction has no sourced dictionary to an RH-adjacent criterion.", ["rh/catalog/taxonomy.json:53"]),
]
for id_, name, aliases, definition, sources in barriers:
    node(id_, "BARRIER", name, aliases, definition, "KILLED_HERE", sources, ["barrier"])

questions = [
    ("open-gabor-window-positivity", "Gabor positivity for the specific window class", ["Gabor positivity open"], "Does the corpus pure-Gabor zero-side remain nonnegative on the stated two-parameter window family?", [f"{PAPER}:4603"]),
    ("open-global-all-place-intersection", "Global all-place intersection identity", ["all-place intersection"], "Can finite-place and archimedean geometric contributions be assembled into the exact global identity required by the route?", ["rh/catalog/analysis/paths_report.json"]),
    ("open-relative-determinant-identity", "Exact relative determinant identity", ["relative determinant identity"], "Can the proposed relative determinant be identified exactly with the target explicit-formula object?", ["rh/catalog/analysis/paths_report.json"]),
    ("open-independent-positivity-source", "Independent positivity source", ["positivity source"], "Is there a positivity mechanism independent of merely rewriting the explicit formula or an RH-equivalent criterion?", [f"{PAPER}:3657"]),
    ("open-lambda-star-scale-law", "Scale law of λ*(L)", ["lambda scale law"], "What is the rigorous scale dependence of the compact-window margin λ*(L)?", ["experiments/tfpt-discovery/lambdastar03_probe.py"]),
    ("open-prime-phase-control", "Prime-phase coherence control", ["prime phase control"], "Can the correlated prime phases be controlled with a non-world-blind estimate?", [f"{PAPER}:955"]),
    ("open-half-density-geometry", "Half-density from geometry", ["geometric half-density", "half-density from geometry", "half-density-from-geometry"], "Does the proposed groupoid geometry canonically supply the required half-density and modular correction?", ["experiments/tfpt-discovery/groupoid_halfdensity_probe.py"]),
]
for id_, name, aliases, definition, sources in questions:
    node(id_, "OPEN_QUESTION", name, aliases, definition, "OPEN", sources, ["open"])

# Mechanism-anatomy, cone, event-log, judge, and missing-fundamental seeds.
PRIME_STORY = "rh/catalog/analysis/prime_story.md"
EVENTLOG = "rh/catalog/analysis/event_log_function.md"
added = [
    ("static-prime-event-log", "OBJECT", "Static prime event log", ["prime checksum", "arithmetic census", "static prime event log"], "The family of static coefficient sequences in the corpus: E8 shell counts, Gaussian signed census, Hecke coefficients, and the von Mangoldt comb. It is not an autonomous dynamics.", "PROVED_HERE", ["tfpt_prime_front.tex:716-751", "tfpt_prime_front.tex:795-807"], ["prime", "event-log", "census"]),
    ("finite-clock-commensurability", "BARRIER", "Finite-clock commensurability", ["prime-period no-go", "finite-clock eventlog barrier", "finite-clock commensurability"], "Finite-order clocks have commensurable periods and therefore cannot realize more than one primitive period proportional to log p.", "PROVED_HERE", ["tfpt_prime_front.tex:921-951"], ["dynamics", "clock", "prime", "barrier"]),
    ("open-autonomous-prime-generator", "OPEN_QUESTION", "Autonomous prime generator", ["dynamic event-log mechanism"], "Whether a source-only non-periodic TFPT evolution derived from the compiler emits support log(p^k) and von Mangoldt amplitudes without sieve, prime table, or fitted event locations.", "OPEN", ["tfpt_prime_front.tex:937-968"], ["dynamics", "firewall", "prime"]),
    ("weight4-gl1-transport", "OPEN_QUESTION", "Weight-4 to GL(1) transport", ["ZETA.CENSUS.TO.GL1", "weight-4 GL(1) transport"], "The open canonical transport from the E4/f8 lattice-Hecke world to the GL(1) xi/Weil world, including the archimedean place.", "OPEN", ["tfpt_prime_front.tex:684-693", "verification/v535_hecke_from_geometry.py:41-48"], ["hecke", "gl1", "bridge"]),
    ("waldspurger-squares", "METHOD", "Waldspurger square positivity", ["waldspurger-square-positivity", "half-integral period squares", "Waldspurger squares"], "Positivity of central f8 twist values represented by squares of half-integral Fourier coefficients, independent of the zeta explicit formula.", "CLASSICAL", ["verification/v537_halfintegral_bridge.py:33-54"], ["positivity", "waldspurger", "f8"]),
    ("siegel-weil-carrier", "OBJECT", "Siegel–Weil positive linear carrier", ["siegel-weil-linear-carrier", "siegel-weil-theta-pairing", "Theta linear carrier", "Siegel-Weil carrier"], "The positive measure Theta(d)|d|^{-a} whose prime side is a plus combination of shifted zeta forms; certified only in the Euler region.", "PROVED_HERE", ["verification/v540_amplitude_linear_carrier.py:14-45", "verification/v540_amplitude_linear_carrier.py:70-87"], ["positivity", "siegel-weil", "theta"]),
    ("eisenstein-rh-neutrality", "THEOREM", "E8 Eisenstein RH-neutrality", ["Eisenstein bridge no-new-information theorem"], "The E8 theta L-function is zeta(s)zeta(s-3), so its nontrivial zeros are exactly the zeta zeros and their translate; the bridge renames rather than locates them.", "PROVED_HERE", ["tfpt_prime_front.tex:851-890"], ["e8", "eisenstein", "barrier"]),
    ("positive-cone-blindness", "BARRIER", "Positive-cone blindness", ["nu-scaling blindness", "positive-measure source barrier", "positive cone blindness"], "A certificate whose premises retain only the positive measure, negative support, window degree, and nonnegative source terms is invariant under scaling the negative mass, so it cannot certify a signed moment inequality; a metric comparison is necessary.", "PROVED_HERE", ["experiments/tfpt-discovery/positive_cone_blindness_probe.py", "experiments/tfpt-discovery/positive_cone_blindness_result.json", "verification/v963_lstar_reduction_dictionary.py:1908-1941"], ["barrier", "moment-cone", "signed-measure", "lstar"]),
    ("rankin-selberg-norm-square", "METHOD", "Rankin–Selberg norm-square", ["Rankin-Selberg norm square", "GNS norm-square"], "The Rankin–Selberg diagonal GNS/norm-square positivity on automorphic forms; it does not by itself control the signed Weil defect.", "CLASSICAL", ["verification/v539_weil_structure_family.py:6-10"], ["positivity", "automorphic"]),
    ("cohen-seeds", "OBJECT", "Cohen positive seeds L(E4⊗χ_d,2)", ["cohen-positive-seeds", "Cohen-Eisenstein seeds", "L(E4⊗χ_d,2)"], "Cohen–Eisenstein edge values L(E4⊗χ_d,2) and L(−1,χ_d) used as positive seeds; a centre version is GRH(χ_d).", "CLASSICAL", ["verification/v540_amplitude_linear_carrier.py:20-23"], ["positivity", "l-values"]),
    ("sos-pontryagin-language", "METHOD", "SOS / Pontryagin language", ["SOS Pontryagin", "sum-of-squares Pontryagin"], "The sum-of-squares / Pontryagin-split language for the signed moment form; it exists exactly when the negative register is empty.", "PROVED_HERE", ["verification/v963_lstar_reduction_dictionary.py:515-523"], ["positivity", "language"]),
    ("kasteleyn-orientation-language", "METHOD", "Kasteleyn orientation language", ["Kasteleyn orientation", "value-preserving orientation"], "Value-preserving Kasteleyn/orientation language on the Cauchy–Binet configuration space, available exactly in the positive-measure class.", "PROVED_HERE", ["verification/v963_lstar_reduction_dictionary.py:524-579"], ["positivity", "language"]),
    ("hamiltonian-psd-language", "METHOD", "Hamiltonian PSD language", ["canonical Hamiltonian positivity"], "Canonical Hamiltonian positivity as a signed-moment pivot condition, not an independent positivity source.", "PROVED_HERE", ["verification/v963_lstar_reduction_dictionary.py:581-597"], ["positivity", "language"]),
    ("dual-pair-language", "METHOD", "Dual-pair product language", ["dual pair language", "exact product law"], "The exact dual-pair product law that synchronizes signs and contributes no second positivity condition.", "PROVED_HERE", ["verification/v963_lstar_reduction_dictionary.py:599-614"], ["positivity", "language"]),
    ("connes-adele-scaling-flow", "METHOD", "Connes–Meyer adele-class scaling flow", ["Connes-Meyer", "adele-class flow", "Connes-Meyer scaling"], "The idele-class scaling representation in which prime powers contribute periodic-orbit terms of length log p to an explicit-formula trace.", "CLASSICAL", ["Connes, Selecta Math. 5 (1999)", "Meyer, 2005"], ["adelic", "event-log"]),
    ("bost-connes-kms-system", "OBJECT", "Bost–Connes KMS system", ["Bost-Connes KMS", "BC KMS system"], "An arithmetic C*-dynamical system whose partition function is zeta(beta), with a phase transition at beta=1 and Hecke-semigroup prime generators.", "CLASSICAL", ["Bost–Connes, Selecta Math. 1 (1995)"], ["operator-algebra", "event-log"]),
    ("primon-riemann-gas", "OBJECT", "Primon or Riemann gas", ["primon gas", "Riemann gas", "Julia Spector gas"], "A quantum gas with one-particle energies log p, so the bosonic partition function is zeta(beta); the prime spectrum is input rather than derived.", "CLASSICAL", ["Julia, 1990", "Spector"], ["event-log", "statistical"]),
    ("berry-keating-dilation", "METHOD", "Berry–Keating dilation Hamiltonian", ["Berry-Keating dilation", "xp dilation"], "The xp dilation generator with semiclassical zero-count asymptotics; a canonical self-adjoint boundary condition encoding prime oscillations remains missing.", "CONJECTURAL", ["Berry–Keating, SIAM Review 41 (1999)"], ["spectral", "event-log"]),
    ("deninger-foliated-dynamics", "METHOD", "Deninger foliated dynamics", ["Deninger flow", "Deninger foliated dynamics"], "A conjectural arithmetic flow whose closed prime orbits and Lefschetz trace model the explicit formula, with a Hodge-type positivity requirement.", "CONJECTURAL", ["Deninger, Proc. ICM Berlin 1998", "experiments/tfpt-discovery/cohomspec_probe.py:122-132"], ["cohomology", "event-log"]),
    ("knauf-arithmetic-statistical-system", "OBJECT", "Knauf arithmetic quantum statistical system", ["Knauf system", "BC-Marcolli", "Connes-Marcolli statistical"], "A family of spin-chain and arithmetic statistical systems encoding factorisation through Hamiltonians, partition functions, KMS phases, and entropy.", "CLASSICAL", ["Knauf, 1990", "Connes–Marcolli"], ["event-log", "statistical"]),
    ("event-log-function", "OPEN_QUESTION", "Event-log function", ["event-log dynamical function", "dynamical function of the prime event log", "event log function"], "Whether a canonical TFPT evolution derives the prime event log as an energy spectrum, primitive-orbit length spectrum, or scale-flow trace without importing arithmetic.", "OPEN", [f"{EVENTLOG}:139-161"], ["event-log", "open"]),
    ("unitarity-of-emergent-time", "OPEN_QUESTION", "Unitarity of emergent TFPT time", ["unitarity of emergent time", "emergent time unitarity", "emergent-time-unitarity"], "Whether emergent TFPT time has a canonical positive Hilbert metric and self-adjoint generator that can be transported to an arithmetic scale flow; no such general axiom was found.", "OPEN", ["tfpt_4_frontier.tex:457-471", "tfpt_4_frontier.tex:809-824", f"{EVENTLOG}:53-59"], ["event-log", "open"]),
    ("edge-l-values", "METHOD", "Edge L-values", ["edge L-values", "Euler-region L-values"], "L-values on the edge of the Euler/absolute-convergence region, as opposed to central critical values.", "CLASSICAL", ["verification/v540_amplitude_linear_carrier.py:70-82"], ["l-values"]),
    ("edge-nonvanishing-method", "METHOD", "Edge nonvanishing method", ["edge nonvanishing", "zeta(1+it) nonzero", "ζ(1+it)≠0"], "Classical nonvanishing methods such as ζ(1+it)≠0 used as comparison templates, without an RH implication.", "CLASSICAL", [PRIME_STORY], ["nonvanishing"]),
    ("quarter-shift-to-centre", "BARRIER", "Quarter-shift to centre", ["quarter-shift to centre", "quarter shift to centre", "Weil criterion quarter-shift"], "The plus-balance of the Siegel–Weil carrier sits off the critical line by a quarter-shift, so Euler-region positivity is not the Weil criterion at the centre.", "PROVED_HERE", ["verification/v540_amplitude_linear_carrier.py:55-68"], ["barrier", "weil"]),
    ("farkas-witness-n-mod-8", "BARRIER", "Farkas witness n≡6 mod 8", ["farkas-witness n≡6 mod 8", "Farkas witness n=6 mod 8", "C_L3 n==6 mod 8"], "A Farkas/LP witness on atoms n≡6 mod 8 showing the residual λ* gap of the theta-library hull is not removed by a finite deterministic-sign family.", "PROVED_HERE", ["verification/v540_amplitude_linear_carrier.py:83-90"], ["barrier", "farkas"]),
    ("metric-by-operator-positivity", "METHOD", "Metric-by-operator positivity", ["metric-by-operator positivity", "operator positivity template"], "A template in which positivity is an output of a self-adjoint or trace-class operator rather than a signed-measure comparison.", "CLASSICAL", [PRIME_STORY], ["positivity", "operator"]),
    ("rhp-iiks-toda-tau", "METHOD", "RHP/IIKS/Toda tau framework", ["RHP/IIKS/Toda tau framework", "IIKS/Toda", "Toda tau", "RHP IIKS Toda", "tau iiks toda", "IIKS Fredholm tau"], "The Riemann–Hilbert / IIKS / Toda-tau dictionary for the finite wall determinant, certified in v955–v963 as finite identities with cofinal no-pole still open.", "PROVED_HERE", ["verification/v955_tau_iiks_toda_dictionary.py:1", "verification/v963_lstar_reduction_dictionary.py:1"], ["rhp", "iiks", "toda"]),
    ("suzuki-screw-canonical-systems", "CLASS", "Suzuki screw functions / canonical systems", ["Suzuki screw functions", "canonical systems", "Suzuki screw", "screw function", "W1 Suzuki"], "Suzuki screw functions and the associated canonical/de Branges systems used as a W1 identification of the TFPT atom measure.", "CLASSICAL", ["notes/arxiv_w1_note/note_w1_suzuki_identification.tex", "verification/v630_suzuki_contact.py:1"], ["suzuki", "screw"]),
    ("quillen-bfk-seam-determinants", "OBJECT", "Quillen/BFK seam determinants", ["Quillen/BFK seam determinants", "Quillen metric", "BFK determinant", "Burghelea-Friedlander-Kappeler", "Quillen/BFK"], "Quillen metrics and Burghelea–Friedlander–Kappeler gluing determinants for elliptic operators on seamed or cut manifolds.", "CLASSICAL", ["experiments/tfpt-discovery/seam_bfk_conical_det_probe.py"], ["quillen", "bfk"]),
    ("i5-transport-ledger-criterion", "CRITERION", "I5 transport-ledger criterion", ["I5 transport-ledger criterion", "I5 criterion", "transport ledger", "I5 inequality"], "The coupled prime–archimedean inequality I5 left after the transport ledger closes; typed as equivalent to Weil positivity, not as a reduction.", "PROVED_HERE", ["verification/v541_matching_lemma_ledger.py:1", "tfpt_prime_front.tex:136-138"], ["i5", "ledger", "rh-equivalent"]),
    ("r-dagger-kernel-loewner-stack", "METHOD", "R† kernel–Loewner positivity stack", ["R† kernel–Loewner positivity stack", "kernel-Loewner", "kernel Loewner positivity", "RDAGGER", "R dagger kernel"], "The R† kernel–Loewner positivity stack at compact windows, certified numerically in v1017 with a float64 floor, not an interval [E] certificate.", "PROVED_HERE", ["verification/v1017_kernel_loewner_positivity.py:1"], ["loewner", "kernel"]),
]
for row in added:
    node(*row)

# Compiler, pi, QSM, positivity, and bridge-2 seeds.
# Duplicate ids remapped to canonical seeds: event-log-function,
# unitarity-of-emergent-time, finite-clock-commensurability,
# positive-cone-blindness, weil-positivity, lstar-statement,
# hilbert-polya-operator, explicit-formula, functional-equation,
# adele-class-space, self-dual-measure. Edge strength CLASSICAL is
# not in the schema; use THEOREM plus a note.
COMPILER_NOTE = "rh/catalog/analysis/compiler_necessity.md"
PI_NOTE = "rh/catalog/analysis/pi_prime_correlations.md"
POS_NOTE = "rh/catalog/analysis/positivity_origin_search.md"
BRIDGE2 = "rh/catalog/analysis/bridge2_direct_search.md"
HECKE_NOTE = "rh/catalog/analysis/hecke_index_theorem.md"
BRIDGE2_OBJ = "rh/catalog/analysis/bridge2_object_search.md"
LEAN_ARCH = f"{LEAN}/SelectedArchErrorQuadraticRateClassical.lean"
ARCH_PACK = "/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Formal_2026-09-05"
GEOM_NOTE = "rh/catalog/analysis/geometry_audit.md"
TATE_NOTE = "rh/catalog/analysis/all_place_tate_audit.md"
HEAT_NB = "rh/catalog/analysis/external_proposals_heat_nb.md"
round_additions = [
    ("multiplicative-composition-law", "THEOREM", "Multiplicative composition necessity", ["multiplicative composition", "log-n information law"], "A monotone additive information function on multiplicatively composed positive-integer labels is c log n; primes are the free monoid's irreducible generators.", "CLASSICAL", [f"{COMPILER_NOTE}:A1"], ["prime", "information"]),
    ("census-qsm", "OBJECT", "E8 census quantum statistical system", ["E8 census QSM", "census quantum statistical system"], "The arithmetic state census with partition function sum sigma_3(n)n^-beta=zeta(beta)zeta(beta-3) and Hecke norm-labelled generators.", "OPEN", ["verification/v1018_e8_directed_readout.py:21-34", "verification/v535_hecke_from_geometry.py:6-29"], ["qsm", "census"]),
    ("modular-clock", "OPERATOR", "Seam modular clock", ["seam modular clock", "free modular Hamiltonian"], "The free modular Hamiltonian K=log((1-C)C^-1) reconstructed from a reflection-positive seam covariance.", "PROVED_HERE", ["verification/v446_seam_clock_invariance.py:31-38", "verification/v446_seam_clock_invariance.py:123-139"], ["clock", "modular"]),
    ("resummed-clock-tower", "OBJECT", "Resummed clock tower", ["resummed clock tower", "clock combination spectrum"], "The family of spectra 6 log(N/(N-n)); its all-N union is 6 log of the positive rational numbers with noncanonical label multiplicity.", "KILLED_HERE", ["verification/v124_resummed_clock.py:10-37", "experiments/tfpt-discovery/clock_combination_spectrum_result.json"], ["clock", "killed"]),
    ("koide-mobius-flow", "OBJECT", "Koide Möbius flow", ["Koide Mobius flow", "Koide Riccati flow"], "The autonomous Riccati flow with fixed points 2 and 5 and time-one multipliers 64/729 and 729/64.", "PROVED_HERE", ["verification/v723_phys_modular_clock.py:111-139", "tfpt_4_frontier.tex:463-472"], ["clock", "koide"]),
    ("4d-lattice-contract", "OBJECT", "Four-dimensional lattice dynamics contract", ["four-dimensional lattice contract", "4d lattice dynamics"], "A local Hermitian Hamiltonian family with transfer exp(-aH), quasilocal thermodynamic dynamics, and a Lieb-Robinson bound.", "OPEN", ["tfpt_4_frontier.tex:809-824", "verification/v1013_thermodynamic_dynamics.py:11-36"], ["lattice", "dynamics"]),
    ("qca-dilation", "OBJECT", "QCA unitary dilation", ["QCA dilation", "collision-band dilation"], "The strictly local collision-band unitary dilation whose reduced diagonal dynamics is the seam Markov transfer B^n.", "PROVED_HERE", ["origin_theory.tex:793-796", "verification/v984_markov_qca_dilation.py:37-43"], ["qca", "dilation"]),
    ("no-canonical-integer-label", "BARRIER", "No canonical integer state label", ["no canonical integer label", "missing log-integer spectrum"], "The physical clock and lattice constructions do not derive a multiplicative positive-integer label whose norm supplies a log-integer spectrum.", "PROVED_HERE", ["experiments/tfpt-discovery/clock_combination_spectrum_result.json", f"{COMPILER_NOTE}:B"], ["barrier", "clock"]),
    ("archimedean-place", "OBJECT", "Archimedean place of Q", ["real place", "infinite place", "Gamma factor and log pi"], "The real completion whose local zeta integral supplies the Gamma factor and log pi; for exp(2 pi i x), exp(-pi x^2) and Lebesgue measure are Fourier self-dual.", "CLASSICAL", ["Tate, Thesis, 1950", WEIL], ["adelic", "explicit-formula", "archimedean"]),
    ("class-number-formula-q-i", "THEOREM", "Class-number formula for Q(i)", ["L(1,chi_-4)=pi/4", "Gaussian class-number formula"], "For Q(i), the Dirichlet class-number formula gives L(1,chi_-4)=2 pi h/(w sqrt(|d|))=pi/4 because h=1, d=-4 and w=|mu4|=4.", "CLASSICAL", ["Dirichlet class-number formula", "Neukirch, Algebraic Number Theory, Chapter VII"], ["dirichlet-l", "gaussian-integers", "mu4"]),
    ("finite-infinite-place-balance", "THEOREM", "Finite-infinite place balance", ["explicit-formula place balance", "prime-real-place identity"], "The Guinand-Weil explicit formula is an identity balancing von Mangoldt prime-power data at finite places against the real-place Gamma, log pi and pole terms.", "CLASSICAL", ["Guinand, Proc. London Math. Soc. 50 (1948)", WEIL], ["explicit-formula", "finite-places", "archimedean"]),
    ("archimedean-dominance", "CRITERION", "Archimedean dominance criterion", ["reality conformity", "archimedean-prime metric dominance"], "Nonnegativity of the full Weil form: the archimedean-plus-pole contribution dominates the prime contribution for every admissible test function; equivalent to RH on the full class.", "CLASSICAL", [WEIL, f"{PAPER}:733-791"], ["weil", "criterion", "metric"]),
    ("pi-numerology-c3", "BARRIER", "c3 and L(1,chi_-4) numerology", ["c3=1/(32 L(1,chi_-4))", "pi numerology c3"], "The algebraic rewrite c3=1/(8 pi)=1/(32 L(1,chi_-4)) has no corpus derivation connecting P1 to the Gaussian class-number formula and is firewall-flagged as coincidence.", "OPEN", [f"{PI_NOTE}:A3", "tfpt_5_redteam.tex:662-689"], ["numerology", "p1", "firewall"]),
    ("mu4-mark", "TFPT_STRUCTURE", "TFPT mu4 mark", ["four-mark boundary datum", "mu4 mark"], "The four-element mark/unit structure carried by the TFPT boundary and E8 glue.", "PROVED_HERE", ["tfpt_1_architecture_e8.tex:150-171", "verification/v53_compiler_core.py:1-29"], ["tfpt", "mu4", "mark"]),
    ("chi-minus-4-census", "INVARIANT", "chi-minus-4 signed census", ["chi_-4 census", "Gaussian split-inert census"], "The corpus exact finite split of prime residue classes by the real character chi_-4; it does not itself evaluate the Euler product at s=1.", "PROVED_HERE", ["verification/v786_prime_packet480.py:394-404", "verification/v786_prime_packet480.py:555"], ["chi-minus-4", "prime-census", "gaussian"]),
    ("census-qsm-normflow", "OBJECT", "Census QSM norm flow", ["census QSM normflow", "Gaussian submodule QSM"], "The single-module rank-four Gaussian submodule QSM with endomorphism-semigroup isometries, index Hamiltonian, and classical Solomon-zeta partition function; it constructs bridge 1 only.", "PROVED_HERE", ["experiments/tfpt-discovery/census_qsm_normflow_probe.py", "experiments/tfpt-discovery/census_qsm_normflow_result.json"], ["qsm", "normflow"]),
    ("connes-marcolli-gln-system", "OBJECT", "Connes–Marcolli GLn arithmetic QSM", ["Connes-Marcolli GLn", "higher-rank arithmetic QSM"], "The classical higher-rank arithmetic quantum statistical system built from commensurability classes, determinant-norm time evolution, and KMS states.", "CLASSICAL", ["Connes-Marcolli, Noncommutative Geometry, Quantum Fields and Motives"], ["qsm", "adelic"]),
    ("index-flow-time", "OPERATOR", "Index-flow time evolution", ["index-flow time", "norm-index Hamiltonian"], "The dynamics sigma_t(mu_A)=Norm(det A)^(it)mu_A generated by the logarithm of submodule index on the canonical submodule Hilbert space.", "PROVED_HERE", ["experiments/tfpt-discovery/census_qsm_normflow_probe.py"], ["qsm", "dynamics"]),
    ("p1-gauss-bonnet-positive-normalization", "THEOREM", "P1 Gauss–Bonnet positive normalization", ["P1 Gauss-Bonnet", "c3 curvature integral"], "The exact positive scalar c3=1/(8pi) obtained from the one-sided S2 curvature integral; this is a coefficient, not a positive arithmetic quadratic form.", "PROVED_HERE", ["origin_theory.tex:1188-1196"], ["p1", "positivity"]),
    ("e8-positive-lattice-norm", "OBJECT", "E8 positive lattice norm", ["E8 Gram form", "positive E8 norm"], "The positive-definite even unimodular E8 Gram form whose shell counts are 240 sigma_3(n).", "PROVED_HERE", ["tfpt_1_architecture_e8.tex:440-450", "verification/v1018_e8_directed_readout.py:27-46"], ["lattice", "positivity"]),
    ("seam-os-positive-transfer", "OPERATOR", "Seam OS positive transfer", ["seam OS transfer", "Lambda=e^{-h}"], "The reflection-positive Gaussian reconstruction Lambda=e^{-h}, a positive contraction on the seam GNS space.", "PROVED_HERE", ["verification/v446_seam_clock_invariance.py:20-39"], ["seam", "os"]),
    ("seam-modular-generator", "OPERATOR", "Seam modular generator", ["seam modular Hamiltonian", "K=log((1-C)C^{-1})"], "The self-adjoint free modular Hamiltonian K=log((1-C)C^{-1}) commuting with the mu4 seam clock for invariant covariance.", "PROVED_HERE", ["verification/v446_seam_clock_invariance.py:31-43"], ["seam", "modular"]),
    ("markov-qca-unitary-dilation", "OPERATOR", "Markov QCA unitary dilation", ["Markov QCA dilation", "Stinespring collision dilation"], "The exact Stinespring collision dilation on a qutrit system and record-qutrit stream whose reduced populations follow the TFPT Markov transfer.", "PROVED_HERE", ["verification/v984_markov_qca_dilation.py:1-43"], ["qca", "markov"]),
    ("quasilocal-hamiltonian-dynamics", "OPERATOR", "Quasilocal Hamiltonian dynamics", ["quasilocal Hamiltonian", "Lieb-Robinson dynamics"], "Hamiltonian-class thermodynamic dynamics with Hermitian local H, positive Euclidean transfer, unitary tau_t, and a Lieb-Robinson bound.", "PROVED_HERE", ["verification/v1013_thermodynamic_dynamics.py:11-37"], ["dynamics", "hamiltonian"]),
    ("e8-theta-heat-operator", "OPERATOR", "E8 theta heat operator", ["E8 heat semigroup", "theta heat operator"], "The positive heat semigroup on L2(R8/E8), whose trace is E4 and whose spectral zeta is 240(8pi^2)^(-s)zeta(s)zeta(s-3).", "CLASSICAL", ["verification/v1018_e8_directed_readout.py:27-46", f"{POS_NOTE}:P2-P3"], ["lattice", "heat"]),
    ("hodge-riemann-positivity-candidate", "OBJECT", "Hodge and Riemann-bilinear positivity candidate", ["Hodge Riemann bilinear", "mu3-cover positivity"], "Finite Hodge data and a conditional Riemann-bilinear route on the mu3-cover; no Kahler positivity theorem is established specifically at the tau=i E8 seam.", "OPEN", ["tfpt_1_architecture_e8.tex:278-290", "tfpt_1_architecture_e8.tex:5488-5493"], ["hodge", "positivity"]),
    ("perron-fixed-point-transport", "OPERATOR", "Perron fixed-point transport", ["Perron transport", "primitive stochastic transport"], "The finite primitive stochastic transport with unique positive attractor and spectrum {1,(2/3)^6,(1/3)^6}.", "PROVED_HERE", ["origin_theory.tex:669-767"], ["perron", "transport"]),
    ("seam-kms-gibbs-positivity", "OBJECT", "Seam KMS and Gibbs positivity", ["seam KMS", "Gibbs positivity"], "Positive thermal states and Boltzmann weights on seam and Hamiltonian-class algebras.", "PROVED_HERE", ["origin_theory.tex:800-817", "verification/v1013_thermodynamic_dynamics.py:20-27"], ["kms", "gibbs"]),
    ("heat-zeta-regularization", "OPERATOR", "Heat and spectral-zeta regularization", ["heat zeta regularization", "Seeley-DeWitt"], "Positive heat semigroups on compact models together with meromorphically continued spectral zeta determinants and Seeley-DeWitt coefficients.", "CLASSICAL", ["tfpt_1_architecture_e8.tex:3870-3913"], ["heat", "zeta"]),
    ("horizon-replica-positivity", "THEOREM", "Horizon replica and area-law positivity", ["horizon replica", "area-law positivity"], "Finite Gaussian, determinant, entropy, and gapped area-law structures used to pin local horizon coefficients.", "PROVED_HERE", ["origin_theory.tex:1250-1267", "tfpt_horizon_readouts.tex:560-620"], ["horizon", "replica"]),
    ("seam-rp-blind-selector", "THEOREM", "Seam RP blindness and straddle selector", ["seam RP blindness", "straddle selector"], "Free RP and kinematic forms are side-blind, while a fenced interacting toy selects one seam-bit member with positive coupling and OS/GNS form.", "PROVED_HERE", ["introduction.tex:226-244", "tfpt_1_architecture_e8.tex:246-251"], ["seam", "rp"]),
    ("admissible-os-positive-measure", "OPERATOR", "Admissible OS positive measure", ["admissible OS measure", "H_OS=-log T"], "The admissible-sector PSD transfer, tight measure family, and many-body Hamiltonian H_OS=-log T with inherited finite-model gap.", "PROVED_HERE", ["origin_theory.tex:1813-1818", "origin_theory.tex:1901-1907"], ["os", "measure"]),
    ("finite-weil-gns-metric", "OBJECT", "Finite Weil GNS family metric", ["finite Weil GNS", "character-family GNS"], "Finite character-family GNS forms combining prime and archimedean channels but not identified with the global central-line Weil form.", "OPEN", ["tfpt_1_architecture_e8.tex:2116-2149", "verification/v539_weil_structure_family.py:6-10"], ["weil", "gns"]),
    ("matching-ledger-positivity", "THEOREM", "Matching-ledger per-term positivity", ["matching-ledger positivity", "per-term Weil ledger"], "Finite-window decomposition of the Weil ledger into certified, archimedean, and correction terms; global positivity remains open.", "PROVED_HERE", ["tfpt_1_architecture_e8.tex:2207-2246", "verification/v541_matching_lemma_ledger.py"], ["ledger", "weil"]),
    ("discrete-spectrum-neutrality", "BARRIER", "Discrete-spectrum neutrality", ["discrete-spectrum zeros", "spectral-zeta continuation"], "For compact finite-type operators, arithmetic L-functions arise as spectral zeta functions; their analytically continued zeros are not eigenvalues of the positive operator.", "PROVED_HERE", [f"{POS_NOTE}:P3"], ["barrier", "spectrum"]),
    ("no-archimedean-prime-joint-space", "BARRIER", "No archimedean-prime joint space", ["no joint archimedean-prime space", "no arithmetic scaling action"], "TFPT has archimedean positive operator spaces and static prime/Hecke spaces, but no canonical Hilbert space carrying both a multiplicative arithmetic action and the physical self-adjoint flow.", "OPEN", [f"{EVENTLOG}:71-77", f"{COMPILER_NOTE}:69-82"], ["barrier", "adelic"]),
    ("finite-family-target-mismatch", "BARRIER", "Finite-family target mismatch", ["finite-family mismatch", "sampled-character mismatch"], "A positive metric on sampled character families does not transfer to the global zeta Weil form without an independently proved representation and limit theorem.", "OPEN", ["tfpt_1_architecture_e8.tex:2116-2149", f"{POS_NOTE}:P1"], ["barrier", "finite"]),
    ("kneser-groupoid", "OBJECT", "Marked Kneser neighbour groupoid", ["Kneser groupoid", "marked Kneser groupoid"], "The marked Kneser-neighbour groupoid of mu4 glue states; fibre ratios were identically one, so no half-density amplitude.", "KILLED_HERE", ["experiments/tfpt-discovery/kneser_groupoid_halfdensity_probe.py", "experiments/tfpt-discovery/kneser_groupoid_halfdensity_result.json"], ["groupoid", "killed"]),
    ("hnf-groupoid", "OBJECT", "HNF submodule correspondence groupoid", ["HNF groupoid", "Gaussian HNF groupoid"], "The degree-graded HNF submodule correspondence groupoid of the rank-4 Gaussian module; source and target HNF fibres agree, so Delta is identically one.", "KILLED_HERE", ["experiments/tfpt-discovery/groupoid_halfdensity_probe.py", "experiments/tfpt-discovery/groupoid_halfdensity_result.json"], ["groupoid", "killed"]),
    ("euler-side-blindness", "BARRIER", "Euler-side blindness", ["Euler-side positivity blindness", "compact-torus blindness"], "Every positivity built on a compact torus, finite-type module, or discrete spectrum is the Euler side of a would-be reflection-positive scale model; per-term positive implies blind, and the critical side is the criterion.", "PROVED_HERE", [BRIDGE2, "experiments/tfpt-discovery/positive_cone_blindness_probe.py", "experiments/tfpt-discovery/census_qsm_normflow_probe.py"], ["barrier", "euler", "positivity"]),
    ("stochastic-scale-semigroup-on-connes-cokernel", "OPEN_QUESTION", "Stochastic scale semigroup on Connes cokernel", ["stochastic scale semigroup", "Connes-cokernel Markov semigroup"], "The only admissible shape of bridge 2: a manifestly positive Markov semigroup in log-scale on the adele class space modulo the Fourier-invariant part whose generator carries the zeros.", "OPEN", [BRIDGE2], ["bridge-2", "adelic", "open"]),
    ("rh-as-reflection-positivity", "THEOREM", "RH as reflection positivity", ["RH reflection positivity", "Bochner-OS-Hilbert-Polya"], "RH is equivalent to Bochner positivity of the Weil kernel, to OS reflection positivity of the Wick-rotated kernel under the functional-equation reflection, and to Hilbert–Pólya.", "CLASSICAL", [WEIL, "Widder, The Laplace Transform; Bernstein theorem", "Osterwalder–Schrader, Comm. Math. Phys. 31 (1973)"], ["weil", "os", "rh-equivalent"]),
    ("e8-sublattice-rg-semigroup", "OBJECT", "E8 sublattice RG semigroup", ["E8 RG semigroup", "superlattice conditional expectation"], "Conditional expectations onto superlattice-periodic functions on R^8/E8, with RG time the log index, reflection L to L-star, and Solomon scale two-point function zeta(s) through zeta(s-7).", "CLASSICAL", [BRIDGE2, "Solomon, Adv. Math. 26 (1977)"], ["lattice", "rg", "semigroup"]),
    # Index / modular (proposed_additions_index.json). No remaps; equality-hunt
    # is the T4 hunt used as the BLOCKED_BY source and was missing as a node.
    ("hecke-index-theorem", "THEOREM", "Hecke covering-index theorem", ["Hecke covering-index", "covering index theorem"], "For an injective integral endomorphism A of the E8 torus, pullback on C(R^8/E8) has finite covering index |det A| and multiplicative composition. Proved here exactly, but mathematically classical and only an arithmetic-side stand-in.", "PROVED_HERE", ["experiments/tfpt-discovery/hecke_index_theorem_probe.py", "experiments/tfpt-discovery/hecke_index_theorem_result.json"], ["index", "hecke", "torus"]),
    ("pimsner-popa-entropy", "THEOREM", "Pimsner-Popa index entropy", ["Pimsner-Popa entropy", "index entropy"], "For a finite covering conditional expectation, log Ind is the additive logarithmic index quantity; this does not by itself make log Ind a physical modular Hamiltonian.", "CLASSICAL", ["Pimsner-Popa, Entropy and index for subfactors, Ann. Sci. ENS 19 (1986)", "Watatani, Index for C*-subalgebras, Memoirs AMS 83 (1990)"], ["index", "entropy"]),
    ("cuntz-laca-semigroup-algebra", "OBJECT", "Cuntz-Laca semigroup algebra", ["Cuntz-Laca algebra", "semigroup crossed product"], "A classical semigroup crossed-product arithmetic QSM in which isometries carry a norm-defined time evolution. It realizes the desired algebra only after the index dynamics is specified, not derived from TFPT physics.", "CLASSICAL", ["Laca-Raeburn, J. London Math. Soc. 59 (1999), DOI:10.1112/S0024610798006620", "Arledge-Laca-Raeburn, Doc. Math. 2 (1997), 115-138"], ["qsm", "operator-algebra"]),
    ("connes-trace-formula-dichotomy", "BARRIER", "Connes trace-formula dichotomy", ["Connes cutoff dichotomy", "cutoff dichotomy"], "Cutoff positivity before quotienting is vacuous because of a divergent positive boundary term; the Fourier-invariant cokernel version is criterion-bearing. Compact-torus counting diverges as Lambda^8, not as the adelic log Lambda term.", "CLASSICAL", ["Connes, Selecta Math. 5 (1999), 29-106", "experiments/tfpt-discovery/hecke_index_theorem_result.json"], ["barrier", "adelic", "cutoff"]),
    ("index-modular-state", "OPEN_QUESTION", "Physical index-modular state", ["physical index-modular state", "index modular Hamiltonian"], "Does the physical 4D OS sector algebra admit a state whose own modular flow acts on lattice-endomorphism sectors with modular Hamiltonian log index, rather than assuming the index dynamics?", "OPEN", ["experiments/tfpt-discovery/hecke_index_theorem_probe.py", f"{COMPILER_NOTE}:A2"], ["index", "modular", "open"]),
    ("equality-hunt", "OPEN_QUESTION", "Torus-cutoff equality hunt", ["cutoff equality hunt"], "The search for a compact-torus or heat-kernel identification of the Weil Arch-Prime-Pole remainder; compact-torus traces diverge as Lambda^8, not as the adelic log Lambda term.", "OPEN", [f"{HECKE_NOTE}:150-205"], ["index", "cutoff", "open"]),
    # Bridge-2 objects (proposed_additions_bridge2.json). hilbert-polya remapped
    # to hilbert-polya-operator; lstar remapped to lstar-statement.
    ("screw-function-criterion", "CRITERION", "Suzuki screw-function criterion", ["zeta screw kernel", "Krein-Langer criterion"], "For Suzuki's explicit g, positivity of K_g(t,u)=g(t-u)-g(t)-g(-u)+g(0) on the real line is equivalent to Weil positivity and RH.", "CLASSICAL", ["Suzuki, arXiv:2206.03682, Theorem 1.2", "doi:10.1112/jlms.12785"], ["bridge-2", "metric", "criterion"]),
    ("canonical-system-hamiltonian", "OPERATOR", "Zeta canonical-system Hamiltonian", ["positive Hamiltonian H(t)", "Krein canonical system"], "The positive Hamiltonian produced abstractly when the zeta screw kernel is positive; constructing it globally and independently from the prime/archimedean data is the forward problem.", "OPEN", ["Suzuki, arXiv:2206.03682", "Suzuki, arXiv:2606.09096"], ["bridge-2", "operator", "canonical-system"]),
    ("schoenberg-helical-embedding", "THEOREM", "Schoenberg-Krein helical embedding", ["screw line", "stationary-increment embedding"], "A positive screw kernel is the Gram kernel of stationary increments x(t)-x(0), with squared norm -2g(t); conversely such an embedding gives kernel positivity.", "CLASSICAL", ["Suzuki, arXiv:2209.04658", "Suzuki, arXiv:2206.03682"], ["metric", "schoenberg", "helical"]),
    ("de-branges-positivity", "CRITERION", "de Branges shift positivity", ["de Branges operator positivity"], "The shift-form condition Re<F,F(.+i)> > 0 is sufficient for critical-line zeros, but Conrey-Li prove that it fails for the natural xi-associated de Branges space; it is strictly stronger than RH.", "KILLED_HERE", ["Conrey-Li, arXiv:math/9812166", "doi:10.1155/S1073792800000489"], ["criterion", "strictly-stronger", "barrier"]),
    ("conductor-operator-burnol", "OPERATOR", "Burnol conductor operator", ["log-position plus log-momentum operator"], "The local Fourier-invariant operator log|x|+F^-1 log|y| F explaining local explicit-formula terms; its self-adjoint structure does not make the global zeta zeros its point spectrum.", "CLASSICAL", ["Burnol, arXiv:math/9902080", "Burnol, arXiv:math/0101068", "doi:10.1515/FORUM.2004.16.6.789"], ["operator", "explicit-formula", "local"]),
    ("verified-zeros-height", "INVARIANT", "Rigorous verified-zero height", ["Platt-Trudgian height"], "Every nontrivial zeta zero with 0 < gamma <= 3000175332800 lies on the critical line.", "CLASSICAL", ["Platt-Trudgian, arXiv:2004.09765", "doi:10.1112/blms.12460"], ["zeros", "finite-height", "rigorous-computation"]),
    ("compact-window-certificate-mechanism", "BARRIER", "Compact-window finite-height barrier", ["Paley-Wiener tail barrier"], "Compact log-support makes the Fourier transform entire rather than height-supported, so zeros verified through any finite H do not by themselves imply positivity on the whole compact-support function class; a uniform tail/operator bound is additionally required.", "CLASSICAL", ["Paley-Wiener theorem", f"{BRIDGE2_OBJ}:S3(iv)", "Platt-Trudgian, arXiv:2004.09765"], ["barrier", "compact-window", "verified-zeros"]),
    ("w2-form-density", "OPEN_QUESTION", "W2 form-density and limit bridge", ["W2 form density"], "Establish the required form-density, Mosco/norm-resolvent and pointwise frame estimates connecting nested TFPT Galerkin spaces to Suzuki's localized form domain.", "OPEN", ["notes/arxiv_w1_note/note_w1_suzuki_identification.tex:421-456", "notes/arxiv_w3_note/note_w3_detector_structure.tex:574-583"], ["W2", "form-density", "operator-limit"]),
    ("w3-uniform-window-positivity", "OPEN_QUESTION", "W3 uniform window positivity", ["W3 uniform positivity", "no-ladder wall"], "Prove positivity uniformly over all windows/scales; finite deployed windows are off-line-zero detectors, while the uniform statement is the conjectural wall.", "OPEN", ["notes/arxiv_w3_note/note_w3_detector_structure.tex:584-591", "verification/v677_w3_structure_theorem.py"], ["W3", "window", "positivity"]),
    ("w4-global-positivity-transfer", "OPEN_QUESTION", "W4 global Weil-positivity transfer", ["W4 global transfer"], "Transfer finite Galerkin/window positivity to the full Weil test-function class using domain density, scale control and uniform estimates.", "OPEN", ["notes/arxiv_w1_note/note_w1_suzuki_identification.tex:432-436"], ["W4", "global-transfer", "weil"]),
    # Lean r475-repair (part_18) and FREQ/grid outer bridges.
    ("selected-arch-error-quadratic-rate", "THEOREM", "Refuted prescribed archRateConst bound", ["SelectedArchErrorQuadraticRate", "archRateConst bound"], "The old prescribed archRateConst formula is too small in the endpoint-kink regime and remains refuted. This is distinct from the corrected test-dependent existential rate, now separately proved in the external ARCH package.", "KILLED_HERE", [LEAN_ARCH, "rh/catalog/fragments/part_18.json"], ["arch", "rate", "killed"]),
    ("selected-arch-weighted-interpolation-estimate", "THEOREM", "Selected arch weighted interpolation estimate", ["SelectedArchWeightedInterpolationEstimate"], "Exact productionArchLag near/far transcription and weighted interpolation estimate, proved without hypotheses for every fixed native GridElement. The eventual constant may depend on that test; no support-uniform constant or global positivity follows.", "FORMALIZED_LEAN", [f"{ARCH_PACK}/ArchRateClosure.lean:33", LEAN_ARCH], ["arch", "interpolation", "lean"]),
    ("selected-arch-error-rate-exists", "THEOREM", "Corrected existential ARCH quadratic rate", ["SelectedArchErrorQuadraticRateExists", "selectedArchErrorQuadraticRateExists_holds"], "For every fixed native GridElement f there exists C_f such that eventually selectedArchError(k,f) is at most C_f times selectedDelta(k) squared. C_f is independent of k, not of f. This does not restore the refuted archRateConst formula.", "FORMALIZED_LEAN", [f"{ARCH_PACK}/ArchRateClosure.lean:44"], ["arch", "rate", "lean"]),
    ("selected-arch-error-convergence", "THEOREM", "Selected ARCH error tends to zero", ["selectedArchError_tendsto_zero"], "The actual native selectedArchError(k,f) tends to zero for every fixed GridElement f. This is archimedean quadrature convergence, not uniform convergence over all tests, FREQ, or Weil positivity.", "FORMALIZED_LEAN", [f"{ARCH_PACK}/ArchRateClosure.lean:49"], ["arch", "convergence", "lean"]),
    ("eventual-selected-read-lower-bound", "OPEN_QUESTION", "Eventual native read lower bound", ["EventuallySelectedReadLowerBound"], "Eventually, for each fixed native test, the selected read is bounded below by minus its archimedean error. Under FREQ and the now proved ARCH convergence this is equivalent to native GridElement Weil nonnegativity; neither side is established.", "OPEN", [f"{ARCH_PACK}/FrontierClosure.lean:8", f"{ARCH_PACK}/SeparatedTail.lean"], ["native", "read", "open"]),
    ("native-grid-weil-positivity", "OPEN_QUESTION", "Native GridElement Weil positivity", ["native_grid_weil_nonnegative"], "Nonnegativity of RH.weilForm on every native GridElement. This must not be silently identified with the classical full Weil or rational Gabor criterion; a precise domain, normalization and transfer theorem is a separate obligation.", "OPEN", [f"{ARCH_PACK}/FrontierClosure.lean:8"], ["native", "positivity", "open"]),
    ("frequently-selected-aug-dual-resolvent", "OPEN_QUESTION", "FREQ cone theorem", ["frequently_selected_augDualResolvent_ge_half", "FREQ cone"], "The FREQ cone theorem: for arbitrarily large K there exist k>=K and a faithful mu-orthonormal transcription of the selected real window with R-dagger(W_k^R)-I/2 positive semidefinite.", "OPEN", [f"{LEAN}/FrequentlySelected.lean:294", "rh/catalog/analysis/evolve_props_report.md"], ["freq", "cone", "open"]),
    ("selected-polynomial-approximates-grid", "OPEN_QUESTION", "Selected polynomial approximates grid", ["SelectedPolynomialApproximatesGrid"], "Named outer bridge: a coefficient vector z exists so the fullRead versus A_cap quadratic form differs by at most the archimedean error. Contains the channel-positivity bridge; r473 NO_BRIDGE.", "OPEN", [f"{LEAN}/InnerBridges.lean:366", "rh/catalog/fragments/part_4.json"], ["grid", "polynomial", "no-bridge"]),
    # Geometry audit (proposed_additions_geometry.json). USED_BY dest must be
    # an attempt path: rigid-calabi-yau-f8 → mu4-mark remapped to the cusp probe.
    ("fourier-quasicrystal-geometry", "GEOMETRY", "Fourier-quasicrystal geometry", ["crystalline measure", "Fourier quasicrystal"], "Discrete tempered measures with discrete Fourier spectrum; positivity is an additional property, and the standard zeta explicit-formula distribution includes an archimedean continuous term.", "CLASSICAL", ["doi:10.1007/s00222-014-0542-z", "doi:10.1063/5.0012286"], ["geometry", "quasicrystal", "bridge-2"]),
    ("dyson-fourier-quasicrystal-criterion", "THEOREM", "Renormalized Dyson Fourier-quasicrystal criterion", ["Dyson quasicrystal criterion", "zeta zero crystalline criterion"], "After the required archimedean density subtraction, real support/temperedness of the zero distribution and its prime-power Fourier partner is equivalent to RH; the unrenormalized zero measure is not a standard Fourier quasicrystal.", "CLASSICAL", ["Dyson, Notices AMS 56 (2009), 212-223", "arXiv:2402.10604", "doi:10.1063/5.0012286"], ["criterion", "restatement", "quasicrystal"]),
    ("infinite-rank-prime-fourier-module", "INVARIANT", "Infinite-rank prime Fourier module", ["Z-span of log primes", "prime frequency module"], "Unique factorization makes the set of log primes Q-linearly independent, so its integer span has infinite rank and cannot arise from one finite-variable Lee-Yang restriction.", "CLASSICAL", ["Fundamental theorem of arithmetic", "arXiv:2303.03201"], ["quasicrystal", "prime", "rank"]),
    ("quantum-metric-graph", "GEOMETRY", "Quantum metric graph", ["quantum graph", "metric graph Laplacian"], "A metric graph with self-adjoint vertex conditions whose spectral trace is an exact sum over closed graph walks and their repetitions.", "CLASSICAL", ["Berkolaiko-Kuchment, Introduction to Quantum Graphs, 2013", "arXiv:1307.6055"], ["spectral", "periodic-orbit", "bridge-2"]),
    ("no-composite-orbits", "BARRIER", "No-composite-orbits barrier", ["mixed prime-orbit barrier", "log-pq orbit barrier"], "The Riemann explicit formula has primitive prime labels and prime-power repetitions but no independent mixed log(pq) primitive orbit; a connected graph flow normally creates such mixed closed walks, so an exact realization needs product-over-places components or proved cancellations.", "CLASSICAL", ["arXiv:1307.6055, Section 2", "Berry-Keating, SIAM Review 41 (1999)", f"{GEOM_NOTE}:B2"], ["barrier", "prime-orbits", "adelic"]),
    ("quantum-graph-decoupling-lemma", "THEOREM", "Conditional quantum-graph decoupling lemma", ["prime-sector decoupling"], "For Q-independent log-prime lengths, exact prime-power trace support and no cancellation imply that every recurrent closed walk lies in one prime sector, so the recurrent scattering matrix is block diagonal.", "CLASSICAL", [f"{GEOM_NOTE}:B2", "arXiv:1307.6055"], ["conditional", "quantum-graph", "barrier"]),
    ("rigid-calabi-yau-f8", "OBJECT", "Rigid Calabi-Yau realization of f8", ["level-8 rigid CY3", "eta(2tau)^4 eta(4tau)^4 Calabi-Yau"], "Rigid Calabi-Yau threefolds whose middle-cohomology L-function is the weight-4 level-8 newform f8=eta(2tau)^4 eta(4tau)^4.", "CLASSICAL", ["LMFDB:8.4.a.a", "arXiv:math/0504070"], ["calabi-yau", "f8", "mu4", "neutral"]),
    ("tate-trace-projector", "THEOREM", "Scalar Tate trace projector", ["Tate projector", "End(V) scalar projector"], "For a two-dimensional representation V, e_T(A)=Tr(A)I/2 is an equivariant self-adjoint idempotent whose image is the scalar Tate line Q(0).", "PROVED_HERE", ["verification/v1021_all_place_tate_rank_audit.py", TATE_NOTE], ["tate", "calabi-yau", "exact"]),
    ("tate-information-loss", "BARRIER", "Tate projection information loss", ["Tate information loss", "universal scalar-line barrier"], "The scalar Q(0) image contains no level, Hecke, Calabi-Yau or E8/H8 data. Projective representation data surviving in End(V) lie in Ad0(V), while scalar-twist, sign and realization data may be lost altogether.", "PROVED_HERE", ["verification/v1021_all_place_tate_rank_audit.py", TATE_NOTE], ["tate", "barrier", "positivity"]),
    ("fixed-finite-carrier-rank-obstruction", "BARRIER", "Fixed finite-carrier rank-nullity lemma", ["finite carrier no-go", "finite-rank pullback obstruction"], "A linear map from a source with dimension larger than one fixed finite carrier has a kernel; the exact pullback of any bilinear carrier form vanishes on that kernel.", "PROVED_HERE", ["verification/v1021_all_place_tate_rank_audit.py", TATE_NOTE], ["rank", "barrier", "finite", "linear"]),
    ("strict-weil-window-floor-zhu", "CRITERION", "Zhu v2 strict Weil-window floor (external)", ["external strict-window premise", "Zhu compact-window floor"], "An external v2 preprint reports a certified positive lower bound for the Weil form on a compact window. The repository does not re-prove or independently certify this premise.", "CONJECTURAL", ["arXiv:2608.24827v2", TATE_NOTE], ["external", "preprint", "weil", "window"]),
    ("all-place-tate-weil-realization", "OPEN_QUESTION", "All-place Tate--Weil realization", ["Tate-Weil realization theorem", "all-place correspondence compiler"], "Construct a zero-independent infinite-dimensional or compatible direct-limit family of arithmetic correspondences whose complete finite, archimedean and pole intersection pairing is exactly the polarized Weil form.", "OPEN", [TATE_NOTE], ["all-place", "tate", "arakelov", "open"]),
    ("absolute-twistor-line", "GEOMETRY", "Absolute twistor line", ["absolute curve with twistor infinity", "compactified Spec Z twistor line"], "The Connes--Consani preprint's absolute curve candidate joining finite prime places to an archimedean F_1^2 twistor component; no required global intersection pairing or Hodge-index theorem is supplied.", "CONJECTURAL", ["arXiv:2609.00299", TATE_NOTE], ["absolute-geometry", "twistor", "preprint", "all-place"]),
    ("rankin-mean-pointwise-exponent-drop", "BARRIER", "Rankin mean-to-pointwise exponent drop", ["q to q-1+epsilon inference", "T49 exponent drop"], "The inference A(X)=O(X^q) with nonnegative coefficients implies b_n=O(n^(q-1+epsilon)) is false; a sparse exact counterexample preserves both the leading mean and pole.", "KILLED_HERE", ["verification/v1021_all_place_tate_rank_audit.py", "DOI:10.1017/S0305004100021101", TATE_NOTE], ["rankin", "counterexample", "killed"]),
    ("petz-watatani-tate-network", "OPEN_QUESTION", "Petz--Watatani--Tate network", ["all-place UCP Tate network", "compatible conditional-expectation network"], "Can compatible Hecke-equivariant conditional expectations converge normally to an infinite all-place carrier whose pullback is the complete signed Weil form rather than a finite positive proxy?", "OPEN", [TATE_NOTE, "verification/v801_prime_cp_intertwiner.py"], ["quantum", "ucp", "all-place", "open"]),
    ("arithmetic-topology-prime-knots", "GEOMETRY", "Arithmetic topology of primes and knots", ["primes as knots", "Morishita arithmetic topology"], "The analogy between primes in Spec Z and knots in a three-manifold, with residue symbols represented by linking invariants.", "CLASSICAL", ["Morishita, Knots and Primes, 2012", "Mazur, Notes on etale cohomology of number fields, 1973"], ["topology", "prime", "analogy"]),
    ("hyperbolic-ruelle-dynamics", "GEOMETRY", "Hyperbolic Ruelle-Selberg dynamics", ["Ruelle zeta geometry", "hyperbolic geodesic flow"], "Hyperbolic geodesic flows whose dynamical zeta zeros and poles have spectral or cohomological interpretations and whose trace formulas use the manifold's primitive length spectrum.", "CLASSICAL", ["Fried, Invent. Math. 84 (1986)", "Patterson-Perry, Duke Math. J. 106 (2001)"], ["dynamics", "hyperbolic", "length-spectrum"]),
    ("k3-hodge-lattice", "OBJECT", "K3 Hodge lattice", ["K3 lattice", "3U plus 2E8(-1)"], "The even unimodular lattice H2(K3,Z)=3U plus 2E8(-1), of signature (3,19), with Neron-Severi signature (1,rho-1) in the projective case.", "CLASSICAL", ["arXiv:1501.04049"], ["k3", "hodge", "e8"]),
    ("rosati-positive-geometry", "THEOREM", "Rosati positivity mechanism", ["positive Rosati involution", "Weil finite-field positivity"], "A polarization makes the Rosati trace pairing on an abelian variety positive; together with Frobenius adjunction it yields the finite-field Riemann-hypothesis bound.", "CLASSICAL", ["arXiv:1509.00797", "doi:10.4310/ICCM.2016.v4.n2.a4"], ["finite-field", "positivity", "local"]),
    ("mobius-scale-group", "METHOD", "Möbius/metaplectic scale-line geometry", ["PSL2 scale geometry", "metaplectic scale action"], "Translations, dilations, inversion and Fourier/metaplectic duality on the scale line; for zeta these are the Tate, Berry-Keating and Connes ingredients.", "CLASSICAL", ["Tate, Thesis, 1950", "Berry-Keating, SIAM Review 41 (1999)", "doi:10.1007/s000290050042"], ["mobius", "scale", "covered"]),
    ("mobius-strip-topology", "GEOMETRY", "Möbius-strip topology", ["nonorientable strip"], "A nonorientable surface that can impose twisted boundary conditions but supplies no canonical multiplicative all-place arithmetic action.", "CLASSICAL", ["Classical topology", f"{GEOM_NOTE}:B5"], ["topology", "shape-irrelevant"]),
    ("finite-spectral-triple-zero-approximants", "OPERATOR", "Finite spectral-triple zero approximants", ["finite self-adjoint zeta perturbations"], "Finite self-adjoint perturbations of the logarithmic scaling spectral triple whose low spectra numerically track zeta ordinates; convergence to the global zeta object is open.", "OPEN", ["arXiv:2511.22755", "arXiv:2511.23257"], ["noncommutative", "spectral-triple", "operator-limit"]),
    ("quantum-torus-geometry", "GEOMETRY", "Quantum-torus and quantum-group geometry", ["quantum torus", "quantum group geometry"], "Noncommutative deformation geometries with canonical representations but no known all-place arithmetic action whose generator carries the Riemann zero ordinates.", "CLASSICAL", ["Connes, Noncommutative Geometry, 1994", f"{GEOM_NOTE}:B6"], ["quantum-geometry", "shape-irrelevant"]),
    ("lapidus-maier-fractal-string-criterion", "THEOREM", "Lapidus-Maier fractal-string criterion", ["inverse spectral problem for fractal strings"], "For fixed D in (0,1), the inverse Minkowski-measurability spectral problem is affirmative exactly when zeta has no zero on Re(s)=D; its affirmative answer for all D not equal to 1/2 is equivalent to RH.", "CLASSICAL", ["doi:10.1112/jlms/52.1.15"], ["fractal-string", "criterion", "restatement"]),
    ("berkovich-bruhat-tits-geometry", "GEOMETRY", "Berkovich and Bruhat-Tits local geometry", ["p-adic analytic geometry", "Bruhat-Tits geometry"], "Local nonarchimedean spaces carrying p-adic group and Hecke actions; by themselves they omit the global archimedean-prime joint state space.", "CLASSICAL", ["Berkovich, Spectral Theory and Analytic Geometry over Non-Archimedean Fields, 1990", "Serre, Trees, 1980"], ["padic", "local", "geometry"]),
    ("causal-spin-network-geometry", "GEOMETRY", "Causal-set and spin-network geometry", ["causal sets", "loop quantum geometry", "spin networks"], "Discrete Lorentzian or loop-quantum geometric state spaces with no accepted canonical zeta all-place action or Riemann-zero generator.", "CLASSICAL", ["Bombelli et al., Phys. Rev. Lett. 59 (1987)", "Rovelli-Smolin, Phys. Rev. D 52 (1995)", f"{GEOM_NOTE}:B6"], ["quantum-geometry", "shape-irrelevant"]),
    # External proposals 5.9. (proposed_additions_nb.json). Existing
    # nyman-beurling-criterion / baez-duarte-criterion / nyman-beurling-space
    # reused; no nyman-beurling-baez-duarte duplicate.
    ("burnol-lower-bound", "THEOREM", "Burnol lower bound", ["Burnol NB lower bound", "multiplicity-squared NB bound"], "Unconditionally, liminf E_N log N is at least the sum of m(rho)^2/|rho|^2 over distinct zeta zeros on the critical line.", "CLASSICAL", ["Burnol, Advances in Mathematics 170 (2002), 56-70, DOI:10.1006/aima.2001.2066"], ["nyman-beurling", "lower-bound", "zeros"]),
    ("baez-duarte-rate-conjecture", "OPEN_QUESTION", "Báez-Duarte rate conjecture", ["E_N asymptotic", "C_BD over log N"], "The expected asymptotic E_N sim C/log N, with C given by the multiplicity-weighted zero sum and by 2+gamma-log(4pi) under RH and simple zeros.", "CONJECTURAL", ["Bettin-Conrey-Farmer, Proc. Steklov Inst. Math. 280 (2013), S30-S36", "Burnol, Advances in Mathematics 170 (2002)"], ["nyman-beurling", "baez-duarte", "rate"]),
    ("dyadic-block-capture-eta", "OPEN_QUESTION", "Dyadic block capture eta", ["eta_k capture conjecture", "binary NB block capture"], "Whether the residualized span of u_n=2r_2n-r_n for N/2<n<=N captures eta_k at least c/k of the Nyman-Beurling residual for one c>0.", "OPEN", ["experiments/tfpt-discovery/nb_dyadic_capture_probe.py", HEAT_NB], ["nyman-beurling", "dyadic", "schur-complement", "positive-geometry"]),
    ("gaussian-smoothed-zero-density", "OBJECT", "Gaussian-smoothed transformed zero density", ["heat-normalized Gabor zero density", "H(a,omega)"], "The distribution pi sqrt(2pi) times the heat-kernel convolution of the real part of the transformed zeta-zero measure.", "CLASSICAL", ["experiments/tfpt-discovery/heat_gabor_restatement_probe.py", f"{LEAN}/GaborCountableCriterion.lean"], ["weil", "gabor", "heat-kernel", "explicit-formula"]),
    ("negative-explosion-criterion-a", "CRITERION", "Negative-explosion criterion A", ["dyadic heat-grid lower bound", "criterion A"], "A dyadic-grid lower bound on the heat-normalized Gabor zero side whose violation under an off-line exposed orbit grows like exp(sigma^2/(2a)).", "PROVED_HERE", [f"{LEAN}/GaborExposedOrbit.lean", "experiments/tfpt-discovery/heat_gabor_restatement_probe.py"], ["weil", "gabor", "equivalent-strength", "restatement"]),
    ("vasyunin-gram-matrix", "OBJECT", "Vasyunin Nyman-Beurling Gram matrix", ["Vasyunin cotangent Gram", "NB Gram matrix"], "The explicit Gram matrix of fractional-part dilations, expressible through periodic digamma sums or Vasyunin cotangent sums.", "CLASSICAL", ["Vasyunin, Algebra i Analiz 7 (1995), 118-135", "Landreau-Richard, Experimental Mathematics 11 (2002), 349-360"], ["nyman-beurling", "gram-matrix", "cotangent-sum"]),
]
for row in round_additions:
    node(*row)

# Every node is explicitly classified. The source is the node's own provenance.
type_class = {
    "CRITERION": "positivity-criterion", "THEOREM": "analytic-object",
    "OBJECT": "analytic-object", "INVARIANT": "analytic-object",
    "METHOD": "spectral-framework", "OPERATOR": "spectral-framework",
    "GEOMETRY": "arithmetic-geometry", "TFPT_STRUCTURE": "tfpt-compiler",
    "BARRIER": "obstruction-class", "OPEN_QUESTION": "research-question",
}
for n in nodes:
    if n["type"] in type_class:
        edge(n["id"], type_class[n["type"]], "INSTANCE_OF", "HEURISTIC", n["sources"][0], "Ontology classification.")

# Classical theorem-strength relations.
T = "THEOREM"
C = "CONDITIONAL"
H = "HEURISTIC"
edge("riemann-zeta", "riemann-xi", "REQUIRES", T, CLASSICAL, "ξ is built from ζ and gamma factors.")
edge("riemann-xi", "functional-equation", "REQUIRES", T, CLASSICAL)
edge("riemann-kernel", "xi-fourier-function", "TRANSFORM_OF", T, "Titchmarsh, §2.16")
edge("xi-fourier-function", "riemann-kernel", "TRANSFORM_OF", T, "Titchmarsh, §2.16")
edge("riemann-kernel", "fourier-transform", "REQUIRES", T, "Titchmarsh, §2.16")
edge("critical-line", "critical-strip", "SPECIAL_CASE_OF", T, CLASSICAL)
edge("riemann-hypothesis", "critical-line", "REQUIRES", T, CLASSICAL)
edge("explicit-formula", "riemann-zeta", "REQUIRES", T, WEIL)
edge("explicit-formula", "von-mangoldt", "REQUIRES", T, WEIL)
edge("chebyshev-psi", "von-mangoldt", "REQUIRES", T, "DLMF §27.2")
edge("prime-counting", "chebyshev-psi", "REQUIRES", T, "DLMF §27.2")
edge("zero-counting", "riemann-zeta", "REQUIRES", T, "Titchmarsh, Thm. 9.3")
edge("montgomery-conjecture", "pair-correlation", "EQUIVALENT_TO", C, "Montgomery (1973)", "This node names the conjectured pair-correlation law.")
edge("pair-correlation", "gue-statistics", "EQUIVALENT_TO", C, "Montgomery (1973)", "Conjectured local-statistics identification.")
edge("weil-quadratic-form", "explicit-formula", "REQUIRES", T, WEIL)
for part in ["weil-arch-term", "weil-prime-term", "weil-pole-term"]:
    edge("weil-quadratic-form", part, "REQUIRES", T, WEIL)
edge("weil-prime-term", "von-mangoldt", "REQUIRES", T, WEIL)
edge("weil-positivity", "weil-quadratic-form", "REQUIRES", T, WEIL)
edge("weil-positivity", "riemann-hypothesis", "EQUIVALENT_TO", T, WEIL)
edge("riemann-hypothesis", "weil-positivity", "EQUIVALENT_TO", T, WEIL)
edge("li-criterion", "li-coefficients", "REQUIRES", T, "Li (1997)")
edge("li-criterion", "riemann-hypothesis", "EQUIVALENT_TO", T, "Li (1997)")
edge("riemann-hypothesis", "li-criterion", "EQUIVALENT_TO", T, "Li (1997)")
edge("nyman-beurling-criterion", "nyman-beurling-space", "REQUIRES", T, "Beurling (1955)")
edge("nyman-beurling-criterion", "hardy-space-h2", "DUAL_TO", T, "Beurling (1955)", "Equivalent Hilbert-space formulations use Hardy-space models.")
edge("nyman-beurling-criterion", "riemann-hypothesis", "EQUIVALENT_TO", T, "Beurling (1955)")
edge("riemann-hypothesis", "nyman-beurling-criterion", "EQUIVALENT_TO", T, "Beurling (1955)")
edge("baez-duarte-criterion", "nyman-beurling-criterion", "SPECIAL_CASE_OF", T, "Báez-Duarte (2003)")
edge("baez-duarte-criterion", "riemann-hypothesis", "EQUIVALENT_TO", T, "Báez-Duarte (2003)")
edge("riemann-hypothesis", "baez-duarte-criterion", "EQUIVALENT_TO", T, "Báez-Duarte (2003)")
edge("rodgers-tao-theorem", "debruijn-newman-constant", "IMPLIES", T, "arXiv:1801.05914", "Proves Λ≥0.")
edge("newman-criterion", "debruijn-newman-constant", "REQUIRES", T, "arXiv:1801.05914")
edge("newman-criterion", "riemann-hypothesis", "EQUIVALENT_TO", T, "arXiv:1801.05914")
edge("riemann-hypothesis", "newman-criterion", "EQUIVALENT_TO", T, "arXiv:1801.05914")
edge("xi-fourier-function", "laguerre-polya-class", "INSTANCE_OF", C, "Pólya heat-flow framework", "Membership is equivalent to all zeros being real.")
edge("jensen-polynomials", "riemann-xi", "REQUIRES", T, "GORZ (2019)")
edge("jensen-hyperbolicity", "laguerre-polya-class", "EQUIVALENT_TO", T, "Pólya–Schur (1914)")
edge("jensen-hyperbolicity", "riemann-hypothesis", "EQUIVALENT_TO", T, "Pólya–Schur (1914)", "For the ξ coefficient sequence.")
edge("riemann-hypothesis", "jensen-hyperbolicity", "EQUIVALENT_TO", T, "Pólya–Schur (1914)", "For the ξ coefficient sequence.")
edge("gorz-theorem", "jensen-polynomials", "IMPLIES", T, "GORZ (2019)", "Fixed degrees are eventually hyperbolic.")
edge("debranges-space", "hermite-biehler-class", "REQUIRES", T, "de Branges (1968)")
edge("lee-yang-property", "laguerre-polya-class", "REQUIRES", C, "Lee–Yang (1952)", "After the relevant normalization and limiting hypotheses.")
edge("kps-theorem", "van-dantzig-pair", "REQUIRES", T, f"{PAPER}:4130")
edge("kps-theorem", "lee-yang-property", "IMPLIES", T, f"{PAPER}:4130", "Only the cited KPS hypotheses.")
edge("polya-frequency-function", "toeplitz-positivity", "EQUIVALENT_TO", T, "Karlin, Total Positivity")
edge("hankel-positivity", "stieltjes-function", "REQUIRES", T, "Akhiezer, Moment Problem")
edge("pick-function", "herglotz-function", "EQUIVALENT_TO", T, "Donoghue (1974)")
edge("stieltjes-function", "pick-function", "SPECIAL_CASE_OF", T, "Schilling–Song–Vondraček, Ch. 7")
edge("stieltjes-function", "completely-monotone", "SPECIAL_CASE_OF", T, "Schilling–Song–Vondraček, Ch. 7")
edge("bernstein-function", "completely-monotone", "REQUIRES", T, "Schilling–Song–Vondraček", "Its derivative is completely monotone.")
edge("completely-monotone", "laplace-transform", "TRANSFORM_OF", T, "Bernstein–Widder theorem")
edge("lambert-w", "saddle-point-method", "REQUIRES", H, "DLMF §4.13", "Lambert W often solves saddle equations in Mellin asymptotics.")
edge("prolate-operator", "landau-widom-asymptotics", "REQUIRES", T, "Landau–Widom (1980)")
edge("bohr-lift", "prime-torus", "REQUIRES", T, "Hedenmalm–Lindqvist–Seip (1997)")
edge("dirichlet-series-polytorus", "bohr-lift", "TRANSFORM_OF", T, "Hedenmalm–Lindqvist–Seip (1997)")
edge("hypercontractivity", "prime-torus", "REQUIRES", T, "Weissler (1979)")
edge("beurling-deny-criterion", "positivity-semigroup", "EQUIVALENT_TO", T, "Fukushima–Oshima–Takeda")
edge("ucp-map", "cuntz-system", "REQUIRES", T, "Paulsen, Completely Bounded Maps", "Cuntz families furnish standard UCP constructions.")
edge("half-density", "groupoid", "REQUIRES", T, "Connes, Noncommutative Geometry")
edge("groupoid-modular-function", "groupoid", "REQUIRES", T, "Renault (1980)")
edge("self-dual-measure", "additive-adeles", "REQUIRES", T, "Tate thesis")
edge("additive-adeles", "fourier-transform", "DUAL_TO", T, "Tate thesis")
edge("spectral-shift", "relative-determinant", "REQUIRES", T, "Krein (1953); Müller (1998)")
edge("selberg-trace-formula", "modular-surface", "REQUIRES", T, "Selberg (1956)")
edge("selberg-trace-formula", "eisenstein-series", "REQUIRES", T, "Iwaniec, Spectral Methods")
edge("eisenstein-series", "eisenstein-constant-term", "REQUIRES", T, "Iwaniec, Spectral Methods")
edge("hecke-operator", "hecke-correspondence", "REALIZES", T, "Miyake, Modular Forms")
edge("e8-theta-series", "epstein-zeta", "TRANSFORM_OF", T, "Mellin transform of theta series")
edge("arakelov-intersection", "arithmetic-hodge-index", "REQUIRES", T, "Yuan–Zhang (2017)")
edge("deligne-rh", "weil-conjectures", "IMPLIES", T, "Deligne (1974)")
edge("weil-conjectures", "riemann-hypothesis", "SPECIAL_CASE_OF", H, "Deligne (1974)", "Function-field analogue, not an implication for ζ.")
edge("bost-connes-system", "riemann-zeta", "REALIZES", T, "Bost–Connes (1995)", "Its partition function is ζ.")
edge("connes-trace-formula", "adele-class-space", "REQUIRES", C, "Connes (1999)")
edge("scaling-site", "adele-class-space", "GENERALIZES", C, "Connes–Consani, arXiv:1507.05818")
edge("hilbert-polya-operator", "riemann-hypothesis", "WOULD_CLOSE", C, "Hilbert–Pólya program")
edge("berry-keating-xp", "hilbert-polya-operator", "SPECIAL_CASE_OF", H, "Berry–Keating (1999)", "Semiclassical model, not an established realization.")
edge("deninger-cohomology", "hilbert-polya-operator", "WOULD_CLOSE", C, "Deninger, ICM 1998", "A suitable positive cohomological realization would supply a spectral route.")

# Lean-established Gabor equivalences; these are logical equivalences, not positivity proofs.
edge("gabor-pure-criterion", "gabor-zero-side", "REQUIRES", T, f"{LEAN}/GaborExposedOrbit.lean:1718")
edge("gabor-pure-criterion", "riemann-hypothesis", "EQUIVALENT_TO", T, f"{LEAN}/GaborExposedOrbit.lean:1718")
edge("riemann-hypothesis", "gabor-pure-criterion", "EQUIVALENT_TO", T, f"{LEAN}/GaborExposedOrbit.lean:1718")
edge("gabor-rational-criterion", "gabor-pure-criterion", "EQUIVALENT_TO", T, f"{LEAN}/GaborCountableCriterion.lean:540")
edge("gabor-rational-criterion", "riemann-hypothesis", "EQUIVALENT_TO", T, f"{LEAN}/GaborCountableCriterion.lean:540")
edge("riemann-hypothesis", "gabor-rational-criterion", "EQUIVALENT_TO", T, f"{LEAN}/GaborCountableCriterion.lean:540")
edge("gabor-prime-side-criterion", "gabor-rational-criterion", "EQUIVALENT_TO", T, f"{LEAN}/GaborCountableCriterion.lean:550")
edge("gabor-prime-side-criterion", "riemann-hypothesis", "EQUIVALENT_TO", T, f"{LEAN}/GaborCountableCriterion.lean:550")
edge("riemann-hypothesis", "gabor-prime-side-criterion", "EQUIVALENT_TO", T, f"{LEAN}/GaborCountableCriterion.lean:550")
edge("gabor-prime-side-criterion", "explicit-formula", "REQUIRES", T, f"{PAPER}:4612")
edge("gabor-pure-criterion", "rh/lean/RH/GaborExposedOrbit.lean", "USED_BY", T, f"{LEAN}/GaborExposedOrbit.lean:1718", "Lean attempt record containing the theorem-strength equivalence.")
edge("gabor-rational-criterion", "rh/lean/RH/GaborCountableCriterion.lean", "USED_BY", T, f"{LEAN}/GaborCountableCriterion.lean:540", "Lean attempt record containing the theorem-strength equivalence.")
edge("gabor-prime-side-criterion", "rh/lean/RH/GaborCountableCriterion.lean", "USED_BY", T, f"{LEAN}/GaborCountableCriterion.lean:550", "Lean attempt record containing the theorem-strength equivalence.")
edge("open-gabor-window-positivity", "gabor-pure-criterion", "WOULD_CLOSE", C, f"{PAPER}:4603")
edge("open-gabor-window-positivity", "barrier-finite-window-ceiling", "BLOCKED_BY", C, f"{PAPER}:2865")

# Internal TFPT structure and strictly typed conditional reductions.
edge("tfpt-c3", "tfpt-e8-compiler", "REQUIRES", C, "tfpt_1_architecture_e8.tex:1")
edge("tfpt-gcar", "tfpt-e8-compiler", "REQUIRES", C, "tfpt_1_architecture_e8.tex:1")
edge("tfpt-e8-compiler", "tfpt-e8-lattice", "REALIZES", C, "tfpt_1_architecture_e8.tex:1")
edge("tfpt-e8-lattice", "e8-theta-series", "REALIZES", T, "Serre, A Course in Arithmetic")
edge("e8-theta-series", "riemann-zeta", "TRANSFORM_OF", T, "Serre, A Course in Arithmetic, Ch. VII", "The Mellin L-series of E4 factors as ζ(s)ζ(s−3); this is RH-neutral.")
edge("e8-cascade", "tfpt-e8-lattice", "REQUIRES", C, f"{PAPER}:4094")
edge("gaussian-e8-module", "cm-seam", "REQUIRES", C, "verification/v714_e8_gaussian_hecke_groupoid.py:1")
edge("gaussian-e8-module", "tfpt-e8-lattice", "REQUIRES", C, "verification/v714_e8_gaussian_hecke_groupoid.py:1")
edge("gaussian-e8-module", "hecke-correspondence", "REQUIRES", C, "verification/v714_e8_gaussian_hecke_groupoid.py:1")
edge("main-world", "smooth-world", "DUAL_TO", H, f"{PAPER}:940", "Control comparison.")
edge("main-world", "scrarith-world", "DUAL_TO", H, f"{PAPER}:940", "Control comparison.")
edge("seam-geodesic", "cm-seam", "REQUIRES", C, "experiments/tfpt-discovery/seam_geodesic_infrastructure_result.json")
edge("gate-zero", "groupoid", "REQUIRES", C, f"{PAPER}:3644")
edge("gate-zero", "half-density", "REQUIRES", C, "experiments/tfpt-discovery/groupoid_halfdensity_result.json")
edge("finite-weil-window", "weil-quadratic-form", "SPECIAL_CASE_OF", C, f"{PAPER}:97")
edge("narrowband-weil", "finite-weil-window", "SPECIAL_CASE_OF", C, "experiments/tfpt-discovery/narrowband_weil_probe.py:1")
edge("chuk-window-certificate", "finite-weil-window", "SPECIAL_CASE_OF", C, "experiments/tfpt-discovery/weil_window_certificate_result.json")
edge("chuk-window-certificate", "weil-positivity", "IMPLIED_BY", C, "experiments/tfpt-discovery/weil_window_certificate_result.json", "Finite-window certificate only.")
edge("lambda-star-ladder", "finite-weil-window", "REQUIRES", C, f"{PAPER}:3293")
edge("selected-window-family", "finite-weil-window", "INSTANCE_OF", C, f"{LEAN}/Selected.lean:444")
edge("quadrep", "inner-bridges", "REQUIRES", C, "rh/problem/verify_inner_bridges.py:1")
edge("inner-bridges", "outer-bridges", "REQUIRES", C, "rh/problem/verify_outer_bridges.py:1")
edge("outer-bridges", "selected-window-family", "REDUCES_TO", C, f"{LEAN}/Selected.lean:444")
edge("terminal-statement", "finite-weil-window", "WOULD_CLOSE", C, f"{PAPER}:3535")
edge("lstar-statement", "finite-weil-window", "WOULD_CLOSE", C, f"{PAPER}:774")
edge("terminal-statement", "lstar-statement", "REQUIRES", C, f"{PAPER}:1991", "Both are inputs to the finite master statement.")
edge("extraction-joint", "weil-positivity", "WOULD_CLOSE", C, f"{PAPER}:1997")
edge("extraction-joint", "selected-window-family", "REQUIRES", C, f"{PAPER}:1997")
edge("extraction-joint", "barrier-finite-window-ceiling", "BLOCKED_BY", C, f"{PAPER}:1997")
edge("relay-lead-law", "von-mangoldt", "REQUIRES", H, "experiments/tfpt-discovery/relay_lead_law_result.json")
edge("arch-rate", "weil-arch-term", "REDUCES_TO", C, "rh/problem/arch_rate.tex:1")
edge("euler-gross-entropy-gap", "main-world", "REQUIRES", H, f"{PAPER}:4040")
edge("ising-lee-yang-compiler", "lee-yang-property", "REDUCES_TO", C, f"{PAPER}:4130")
edge("cusp-surgery", "efrat-determinant", "REQUIRES", T, "Efrat (1988)")
edge("openai-long-prime-gaps", "riemann-hypothesis", "BLOCKED_BY", H, "rh/catalog/fragments/part_8.json", "Catalog classification: relevance none; no RH bridge.")
edge("murru-salvatori", "regulator-jump", "REQUIRES", H, "experiments/tfpt-discovery/regulator_relation_result.json")
edge("cubic-wedges", "riemann-hypothesis", "BLOCKED_BY", H, "arXiv:2607.16795", "External route remains unpromoted.")

# Open-question settlement targets and barriers.
for src, dst, source in [
    ("open-global-all-place-intersection", "arakelov-intersection", "rh/catalog/analysis/paths_report.json"),
    ("open-global-all-place-intersection", "additive-adeles", "rh/catalog/analysis/paths_report.json"),
    ("open-global-all-place-intersection", "weil-quadratic-form", "rh/catalog/analysis/paths_report.json"),
    ("open-relative-determinant-identity", "relative-determinant", "rh/catalog/analysis/paths_report.json"),
    ("open-relative-determinant-identity", "explicit-formula", "rh/catalog/analysis/paths_report.json"),
    ("open-independent-positivity-source", "weil-positivity", f"{PAPER}:3657"),
    ("open-independent-positivity-source", "positivity-semigroup", f"{PAPER}:3657"),
    ("open-lambda-star-scale-law", "lambda-star-ladder", "experiments/tfpt-discovery/lambdastar03_probe.py"),
    ("open-prime-phase-control", "weil-prime-term", f"{PAPER}:955"),
    ("open-half-density-geometry", "half-density", "experiments/tfpt-discovery/groupoid_halfdensity_probe.py"),
    ("open-half-density-geometry", "gate-zero", "experiments/tfpt-discovery/groupoid_halfdensity_probe.py"),
]:
    edge(src, dst, "WOULD_CLOSE", C, source)
for src, dst, source in [
    ("open-global-all-place-intersection", "barrier-arch-compensation", "rh/catalog/analysis/paths_report.json"),
    ("open-relative-determinant-identity", "barrier-structural-mismatch", "rh/catalog/analysis/paths_report.json"),
    ("open-independent-positivity-source", "barrier-circularity", f"{PAPER}:3657"),
    ("open-lambda-star-scale-law", "barrier-finite-window-ceiling", "experiments/tfpt-discovery/lambdastar03_probe.py"),
    ("open-prime-phase-control", "barrier-prime-phase-coherence", f"{PAPER}:955"),
    ("open-prime-phase-control", "barrier-world-blind", f"{PAPER}:955"),
    ("open-half-density-geometry", "barrier-unimodularity", "experiments/tfpt-discovery/groupoid_halfdensity_result.json"),
    ("terminal-statement", "barrier-lossy-constant", f"{PAPER}:3535"),
    ("lstar-statement", "barrier-prime-phase-coherence", f"{PAPER}:955"),
    ("gate-zero", "barrier-p2-defect", f"{PAPER}:3644"),
    ("finite-weil-window", "barrier-finite-window-ceiling", f"{PAPER}:2865"),
    ("pick-function", "barrier-pick-sign", "experiments/tfpt-discovery/mellin_pick_zero_residue_result.json"),
    ("stieltjes-function", "barrier-nonreal-cofactor-zeros", "experiments/tfpt-discovery/mellin_cofactor_nonreal_zero_result.json"),
]:
    edge(src, dst, "BLOCKED_BY", C, source)

# Additional sourced structural links provide useful traversal without asserting RH.
for src, dst, rel, source in [
    ("mellin-transform", "fourier-transform", "TRANSFORM_OF", "DLMF §2.5"),
    ("laplace-transform", "mellin-transform", "TRANSFORM_OF", "DLMF §2.5"),
    ("riemann-xi", "riemann-zeta", "TRANSFORM_OF", CLASSICAL),
    ("epstein-zeta", "mellin-transform", "REQUIRES", "DLMF §25.11"),
    ("e8-theta-series", "hecke-operator", "REQUIRES", "Serre, A Course in Arithmetic"),
    ("modular-surface", "eisenstein-series", "REALIZES", "Iwaniec, Spectral Methods"),
    ("bruhat-tits-tree", "hecke-correspondence", "REALIZES", "Serre, Trees"),
    ("bost-connes-system", "adele-class-space", "REQUIRES", "Bost–Connes (1995)"),
    ("adele-class-space", "additive-adeles", "REQUIRES", "Connes (1999)"),
    ("carlson-theorem", "vitali-montel", "REQUIRES", "Titchmarsh, Theory of Functions"),
    ("relative-determinant", "cusp-surgery", "REQUIRES", "Müller (1998)"),
    ("spectral-shift", "hilbert-polya-operator", "REQUIRES", "Krein (1953)"),
    ("hermite-biehler-class", "hilbert-polya-operator", "REQUIRES", "de Branges (1968)"),
    ("debranges-space", "hilbert-polya-operator", "REQUIRES", "de Branges (1968)"),
    ("toeplitz-positivity", "polya-frequency-function", "REQUIRES", "Karlin, Total Positivity"),
    ("hankel-positivity", "stieltjes-function", "REQUIRES", "Akhiezer, Moment Problem"),
    ("jensen-polynomials", "toeplitz-positivity", "REQUIRES", "Pólya–Schur (1914)"),
    ("pick-function", "mellin-transform", "REQUIRES", f"{PAPER}:4130"),
    ("saddle-point-method", "mellin-transform", "REQUIRES", "DLMF §2.5"),
    ("lambert-w", "mellin-transform", "REQUIRES", "DLMF §4.13"),
    ("prolate-operator", "fourier-transform", "REQUIRES", "Slepian–Pollak (1961)"),
    ("prime-torus", "von-mangoldt", "REQUIRES", "Hedenmalm–Lindqvist–Seip (1997)"),
    ("positivity-semigroup", "beurling-deny-criterion", "REQUIRES", "Fukushima–Oshima–Takeda"),
    ("groupoid", "ucp-map", "REQUIRES", "Renault (1980)"),
    ("self-dual-measure", "half-density", "DUAL_TO", "Connes, Noncommutative Geometry"),
    ("scaling-site", "bost-connes-system", "REQUIRES", "Connes–Consani, arXiv:1507.05818"),
    ("deninger-cohomology", "weil-conjectures", "GENERALIZES", "Deninger, ICM 1998"),
    ("arithmetic-hodge-index", "weil-conjectures", "REQUIRES", "Yuan–Zhang (2017)"),
]:
    edge(src, dst, rel, C, source)

# Mechanism-anatomy relations.
edge("e8-theta-series", "static-prime-event-log", "REALIZES", T, "tfpt_prime_front.tex:716-732", "E8 shell coefficients give the sigma_3 ledger.")
edge("static-prime-event-log", "riemann-zeta", "TRANSFORM_OF", T, "tfpt_prime_front.tex:716-732", "Its shell Dirichlet series is 240 zeta(s)zeta(s-3).")
edge("e8-theta-series", "eisenstein-rh-neutrality", "REALIZES", T, "tfpt_prime_front.tex:851-890", "The exact factorization fixes the zero set.")
edge("eisenstein-rh-neutrality", "weight4-gl1-transport", "REQUIRES", T, "verification/v535_hecke_from_geometry.py:41-48", "Any non-neutral use needs information not supplied by the Eisenstein identity.")
edge("open-autonomous-prime-generator", "finite-clock-commensurability", "BLOCKED_BY", T, "tfpt_prime_front.tex:921-951", "A successful generator must be non-periodic with infinitely many Q-independent primitive periods.")
edge("e8-cascade", "finite-clock-commensurability", "BLOCKED_BY", T, "tfpt_prime_front.tex:937-951", "Finite Coxeter/E8 timing cannot realize the prime orbit spectrum.")
edge("relay-lead-law", "static-prime-event-log", "REQUIRES", "STATISTICAL", "experiments/tfpt-discovery/support_relay_census_probe.py:3-7", "The relay analyzes supplied prime-power support events.")
edge("waldspurger-squares", "weight4-gl1-transport", "BLOCKED_BY", C, "verification/v537_halfintegral_bridge.py:33-54", "The square positivity remains on the f8 GL(2) twist family.")
edge("siegel-weil-carrier", "open-lambda-star-scale-law", "BLOCKED_BY", C, "verification/v540_amplitude_linear_carrier.py:70-87", "Euler-region positivity does not remove the lambda-star Farkas gap.")
edge("siegel-weil-carrier", "waldspurger-squares", "CO_OCCURS", T, "verification/v540_amplitude_linear_carrier.py:1-23", "They are the Eisenstein and cusp positivity candidates in the same half-integral family.")
edge("self-dual-measure", "siegel-weil-carrier", "CO_OCCURS", H, "verification/v540_amplitude_linear_carrier.py:46-87", "Proposed all-place normalization test; no bridge is claimed.")
edge("open-autonomous-prime-generator", "static-prime-event-log", "WOULD_CLOSE", C, "tfpt_prime_front.tex:937-968", "A source-only dynamics would upgrade the static ledger metaphor to a generation mechanism.")

# Positive-cone blindness: BLIND sources and surviving templates.
CONE_PROBE = "experiments/tfpt-discovery/positive_cone_blindness_probe.py"
for src, source, note in [
    ("waldspurger-squares", "verification/v537_halfintegral_bridge.py:557-617", "Coefficient-square positivity does not compare the prime-channel mass with the positive channel."),
    ("siegel-weil-carrier", "verification/v540_amplitude_linear_carrier.py:13-21", "Positive lattice counts and the pure Eisenstein pairing are invariant under negative-mass scaling."),
    ("rankin-selberg-norm-square", "verification/v539_weil_structure_family.py:6-10", "The positive diagonal GNS metric does not control the signed Weil defect."),
    ("cohen-seeds", "verification/v540_amplitude_linear_carrier.py:20-23", "Positive edge-value seeds retain no metric ratio between the two moment measures."),
    ("sos-pontryagin-language", "verification/v963_lstar_reduction_dictionary.py:515-523", "The SOS language exists exactly for an empty negative register; the surviving comparison restates positivity."),
    ("kasteleyn-orientation-language", "verification/v963_lstar_reduction_dictionary.py:524-579", "Value-preserving orientation is available exactly in the positive-measure class."),
    ("hamiltonian-psd-language", "verification/v963_lstar_reduction_dictionary.py:581-597", "Canonical Hamiltonian positivity is the existing signed-moment pivot condition, not an independent source."),
    ("dual-pair-language", "verification/v963_lstar_reduction_dictionary.py:599-614", "The exact product law synchronizes signs and contributes no second positivity condition."),
]:
    edge(src, "positive-cone-blindness", "BLOCKED_BY", C, source, note)
    edge(src, "positive-cone-blindness", "BLOCKED_BY", C, CONE_PROBE, "LEMMA_PROVED: positive-cone source is cone-blind.")
edge("open-independent-positivity-source", "lstar-statement", "WOULD_CLOSE", C, CONE_PROBE, "One surviving target is a representation-theoretic proof of the metric moment-cone comparison nu <= mu.")
edge("open-independent-positivity-source", "hilbert-polya-operator", "WOULD_CLOSE", C, CONE_PROBE, "The alternative surviving template is operator positivity with a proved explicit-formula bridge.")
edge("open-independent-positivity-source", "metric-by-operator-positivity", "WOULD_CLOSE", C, CONE_PROBE, "Would close to metric comparison/L* and operator positivity.")

# Event-log templates and barriers.
for src, strength, source in [
    ("connes-adele-scaling-flow", C, "Connes 1999"),
    ("bost-connes-kms-system", H, "Bost-Connes 1995"),
    ("primon-riemann-gas", H, "Julia 1990"),
    ("berry-keating-dilation", H, "Berry-Keating 1999"),
    ("deninger-foliated-dynamics", C, "Deninger 1998"),
    ("knauf-arithmetic-statistical-system", H, "Knauf 1990"),
]:
    edge(src, "event-log-function", "WOULD_CLOSE", strength, source)
edge("event-log-function", "finite-clock-commensurability", "BLOCKED_BY", T, "tfpt_prime_front.tex:921-951")
edge("event-log-function", "unitarity-of-emergent-time", "REQUIRES", C, f"{EVENTLOG}:146-161")
edge("unitarity-of-emergent-time", "weil-positivity", "WOULD_CLOSE", C, f"{EVENTLOG}:150-161")
edge("connes-adele-scaling-flow", "adele-class-space", "REQUIRES", C, "Connes 1999")
edge("connes-adele-scaling-flow", "connes-trace-formula", "SPECIAL_CASE_OF", C, "Connes 1999")
edge("bost-connes-kms-system", "bost-connes-system", "SPECIAL_CASE_OF", T, "Bost-Connes 1995")
edge("berry-keating-dilation", "berry-keating-xp", "SPECIAL_CASE_OF", H, "Berry-Keating 1999")
edge("deninger-foliated-dynamics", "deninger-cohomology", "SPECIAL_CASE_OF", C, "Deninger 1998")

# Judge findings (prime_story.md).
edge("waldspurger-squares", "positive-cone-blindness", "BLOCKED_BY", T, PRIME_STORY, "positive-measure source; direct-sum census: cusp summand carries no inequality for the Eisenstein summand")
edge("cohen-seeds", "edge-l-values", "SPECIAL_CASE_OF", T, PRIME_STORY, "reflected Euler-region datum; centre version = GRH(χ_d)")
edge("rankin-selberg-norm-square", "edge-nonvanishing-method", "INSTANCE_OF", T, PRIME_STORY, "ζ(1+it)≠0; CLASSICAL_NEUTRAL")
edge("siegel-weil-carrier", "quarter-shift-to-centre", "BLOCKED_BY", T, "verification/v540_amplitude_linear_carrier.py:55-68")
edge("siegel-weil-carrier", "farkas-witness-n-mod-8", "BLOCKED_BY", T, "verification/v540_amplitude_linear_carrier.py:83-90")
edge("additive-adeles", "explicit-formula", "REDUCES_TO", T, PRIME_STORY, "Tate/Connes–Meyer restatement of additive-adeles × Siegel–Weil.")
edge("siegel-weil-carrier", "explicit-formula", "REDUCES_TO", T, PRIME_STORY, "Tate/Connes–Meyer restatement of additive-adeles × Siegel–Weil.")
edge("selberg-trace-formula", "metric-by-operator-positivity", "INSTANCE_OF", T, PRIME_STORY, "The only template where positivity is an operator output.")
edge("hilbert-polya-operator", "unitarity-of-emergent-time", "REQUIRES", C, PRIME_STORY)

# Missing-fundamental typing.
edge("i5-transport-ledger-criterion", "weil-positivity", "EQUIVALENT_TO", T, "tfpt_prime_front.tex:136-138", "Corpus typing: I5 is equivalent to Weil positivity, not a reduction.")
edge("weil-positivity", "i5-transport-ledger-criterion", "EQUIVALENT_TO", T, "tfpt_prime_front.tex:136-138", "Corpus typing: I5 is equivalent to Weil positivity, not a reduction.")

# Today's kills and cone lemma evidence.
edge("open-half-density-geometry", "experiments/tfpt-discovery/kneser_groupoid_halfdensity_probe.py", "KILLED_BY", C, "experiments/tfpt-discovery/kneser_groupoid_halfdensity_probe.py", "K1 Δ≡1")
edge("open-half-density-geometry", "experiments/tfpt-discovery/parabolic_detline2_probe.py", "KILLED_BY", C, "experiments/tfpt-discovery/parabolic_detline2_probe.py", "K2 odd-power resummation ≠ Weil weights")

# Compiler necessity (proposed_additions_compiler.json).
edge("census-qsm", "multiplicative-composition-law", "REQUIRES", T, f"{COMPILER_NOTE}:A1")
edge("census-qsm", "event-log-function", "WOULD_CLOSE", C, f"{COMPILER_NOTE}:C")
edge("census-qsm", "no-canonical-integer-label", "BLOCKED_BY", C, f"{COMPILER_NOTE}:A2")
edge("modular-clock", "census-qsm", "WOULD_CLOSE", C, f"{COMPILER_NOTE}:B3")
edge("modular-clock", "no-canonical-integer-label", "BLOCKED_BY", H, "experiments/tfpt-discovery/clock_combination_spectrum_result.json")
edge("resummed-clock-tower", "no-canonical-integer-label", "BLOCKED_BY", T, "experiments/tfpt-discovery/clock_combination_spectrum_probe.py")
edge("resummed-clock-tower", "event-log-function", "WOULD_CLOSE", H, f"{COMPILER_NOTE}:B")
edge("koide-mobius-flow", "finite-clock-commensurability", "BLOCKED_BY", T, "verification/v723_phys_modular_clock.py:111-139")
edge("koide-mobius-flow", "no-canonical-integer-label", "BLOCKED_BY", T, "experiments/tfpt-discovery/clock_combination_spectrum_result.json")
edge("4d-lattice-contract", "event-log-function", "WOULD_CLOSE", C, f"{COMPILER_NOTE}:B4")
edge("4d-lattice-contract", "no-canonical-integer-label", "BLOCKED_BY", C, f"{COMPILER_NOTE}:B4")
edge("4d-lattice-contract", "qca-dilation", "REQUIRES", C, "verification/v984_markov_qca_dilation.py:37-43")
edge("qca-dilation", "no-canonical-integer-label", "BLOCKED_BY", C, f"{COMPILER_NOTE}:B4")
edge("event-log-function", "finite-clock-commensurability", "BLOCKED_BY", T, "tfpt_prime_front.tex:921-951")
edge("event-log-function", "no-canonical-integer-label", "BLOCKED_BY", C, f"{COMPILER_NOTE}:D")

# Pi / archimedean place (proposed_additions_pi.json).
edge("finite-infinite-place-balance", "archimedean-place", "REQUIRES", T, "Tate thesis; Weil 1952", "USED_BY remapped: dest must be an attempt path; the real local factor supplies Gamma and log pi.")
edge("finite-infinite-place-balance", "weil-positivity", "REQUIRES", T, "Weil 1952", "Positivity is imposed on the quadratic form defined by the explicit-formula identity.")
edge("archimedean-dominance", "weil-positivity", "EQUIVALENT_TO", T, "Weil 1952", "This is a naming of full-class Weil positivity, not a new criterion.")
edge("archimedean-dominance", "lstar-statement", "REDUCES_TO", C, f"{PAPER}:733-791,1964-2004", "L* is the finite free-window metric reduction; global extraction remains open.")
edge("mu4-mark", "class-number-formula-q-i", "INSTANCE_OF", T, "Dirichlet class-number formula; tfpt_1_architecture_e8.tex:150-171", "The shared abstract group is the four-element unit group; this does not derive P1.")
edge("chi-minus-4-census", "class-number-formula-q-i", "TRANSFORM_OF", C, "verification/v786_prime_packet480.py:394-404,555; Euler product for L(s,chi_-4)", "The finite census supplies the character signs; passing to the convergent/continued value at s=1 is classical analysis not computed by that census.")
edge("event-log-function", "archimedean-place", "REQUIRES", C, f"{EVENTLOG}:139-161; Tate thesis", "An all-place event-log interpretation must include the real local factor, not only prime events.")
edge("pi-numerology-c3", "class-number-formula-q-i", "BLOCKED_BY", H, f"{PI_NOTE}:A3", "Equality as numbers is exact; the claimed mechanism is blocked by absence of a derivation.")

# Census QSM normflow (proposed_additions_qsm.json).
edge("census-qsm-normflow", "connes-marcolli-gln-system", "INSTANCE_OF", T, "experiments/tfpt-discovery/census_qsm_normflow_result.json")
edge("census-qsm-normflow", "multiplicative-composition-law", "REALIZES", T, "experiments/tfpt-discovery/census_qsm_normflow_probe.py")
edge("census-qsm-normflow", "event-log-function", "WOULD_CLOSE", C, "experiments/tfpt-discovery/census_qsm_normflow_result.json#bridge-1-only")
edge("census-qsm-normflow", "positive-cone-blindness", "BLOCKED_BY", T, "experiments/tfpt-discovery/positive_cone_blindness_probe.py#bridge-2")

# Positivity origins (proposed_additions_positivity.json).
# positive-cone-blindness node skipped (canonical seed already present).
# hilbert-polya remapped to hilbert-polya-operator.
edge("p1-gauss-bonnet-positive-normalization", "positive-cone-blindness", "BLOCKED_BY", T, f"{POS_NOTE}:P1")
edge("e8-positive-lattice-norm", "positive-cone-blindness", "BLOCKED_BY", T, "experiments/tfpt-discovery/positive_cone_blindness_result.json")
edge("seam-os-positive-transfer", "no-archimedean-prime-joint-space", "BLOCKED_BY", C, f"{POS_NOTE}:P1")
edge("seam-modular-generator", "no-archimedean-prime-joint-space", "BLOCKED_BY", C, f"{EVENTLOG}:53-77")
edge("markov-qca-unitary-dilation", "no-archimedean-prime-joint-space", "BLOCKED_BY", T, "verification/v984_markov_qca_dilation.py:35-43")
edge("quasilocal-hamiltonian-dynamics", "no-archimedean-prime-joint-space", "BLOCKED_BY", C, f"{COMPILER_NOTE}:145-154")
edge("e8-theta-heat-operator", "discrete-spectrum-neutrality", "BLOCKED_BY", T, f"{POS_NOTE}:P3")
edge("hilbert-polya-operator", "no-archimedean-prime-joint-space", "REQUIRES", C, f"{POS_NOTE}:P4")
edge("hilbert-polya-operator", "seam-modular-generator", "REQUIRES", H, f"{POS_NOTE}:P4")
edge("hilbert-polya-operator", "e8-theta-heat-operator", "REQUIRES", H, f"{POS_NOTE}:P2-P4")
edge("hodge-riemann-positivity-candidate", "no-archimedean-prime-joint-space", "BLOCKED_BY", C, f"{POS_NOTE}:P1")
edge("perron-fixed-point-transport", "no-archimedean-prime-joint-space", "BLOCKED_BY", T, "origin_theory.tex:669-767")
edge("seam-kms-gibbs-positivity", "positive-cone-blindness", "BLOCKED_BY", T, f"{COMPILER_NOTE}:100-107")
edge("heat-zeta-regularization", "discrete-spectrum-neutrality", "BLOCKED_BY", T, f"{POS_NOTE}:P3")
edge("horizon-replica-positivity", "positive-cone-blindness", "BLOCKED_BY", C, f"{POS_NOTE}:P1")
edge("seam-rp-blind-selector", "positive-cone-blindness", "BLOCKED_BY", T, "introduction.tex:226-244")
edge("admissible-os-positive-measure", "no-archimedean-prime-joint-space", "BLOCKED_BY", C, "origin_theory.tex:1901-1907")
edge("finite-weil-gns-metric", "finite-family-target-mismatch", "BLOCKED_BY", C, "tfpt_1_architecture_e8.tex:2116-2149")
edge("matching-ledger-positivity", "positive-cone-blindness", "BLOCKED_BY", T, "experiments/tfpt-discovery/positive_cone_blindness_result.json")
edge("hilbert-polya-operator", "finite-weil-gns-metric", "REQUIRES", H, f"{POS_NOTE}:P4")

# Bridge 2 anatomy (bridge2_direct_search.md).
edge("e8-sublattice-rg-semigroup", "euler-side-blindness", "INSTANCE_OF", C, BRIDGE2, "Euler-side instance of the would-be reflection-positive scale model.")
edge("e8-sublattice-rg-semigroup", "euler-side-blindness", "BLOCKED_BY", C, BRIDGE2, "Per-term Solomon coefficients are cone-blind; the critical side is the criterion.")
edge("e8-sublattice-rg-semigroup", "census-qsm-normflow", "REALIZES", C, BRIDGE2, "The corpus realises the classical RG semigroup via the census-qsm-normflow probe.")
edge("e8-sublattice-rg-semigroup", "functional-equation", "DUAL_TO", T, BRIDGE2, "Poisson self-duality L↔L* and θ_E8(1/t)=t^4 θ_E8(t) induce the functional-equation reflection.")
edge("rh-as-reflection-positivity", "weil-positivity", "EQUIVALENT_TO", T, WEIL, "Bochner positivity of the Weil kernel is Weil positivity.")
edge("rh-as-reflection-positivity", "riemann-hypothesis", "EQUIVALENT_TO", T, WEIL)
edge("rh-as-reflection-positivity", "hilbert-polya-operator", "EQUIVALENT_TO", T, "Osterwalder–Schrader; Hilbert–Pólya program", "OS reconstruction yields a self-adjoint scale Hamiltonian.")
edge("rh-as-reflection-positivity", "functional-equation", "REQUIRES", T, WEIL, "The OS reflection is the functional-equation involution.")
for src in [
    "waldspurger-squares",
    "siegel-weil-carrier",
    "cohen-seeds",
    "census-qsm-normflow",
    "kneser-groupoid",
    "hnf-groupoid",
    "e8-theta-series",
    "e8-theta-heat-operator",
    "census-qsm",
]:
    edge(src, "euler-side-blindness", "BLOCKED_BY", C, BRIDGE2, "KILLED_HERE/BLIND Euler-side source: per-term positive, critical side is the criterion.")
edge("kneser-groupoid", "experiments/tfpt-discovery/kneser_groupoid_halfdensity_probe.py", "KILLED_BY", C, "experiments/tfpt-discovery/kneser_groupoid_halfdensity_probe.py", "K1 Δ≡1")
edge("hnf-groupoid", "experiments/tfpt-discovery/groupoid_halfdensity_probe.py", "KILLED_BY", C, "experiments/tfpt-discovery/groupoid_halfdensity_probe.py", "unimodular HNF fibres")
edge("stochastic-scale-semigroup-on-connes-cokernel", "hilbert-polya-operator", "WOULD_CLOSE", C, BRIDGE2)
edge("stochastic-scale-semigroup-on-connes-cokernel", "rh-as-reflection-positivity", "WOULD_CLOSE", C, BRIDGE2)
edge("stochastic-scale-semigroup-on-connes-cokernel", "adele-class-space", "REQUIRES", C, BRIDGE2)
edge("stochastic-scale-semigroup-on-connes-cokernel", "self-dual-measure", "REQUIRES", C, BRIDGE2)
edge("stochastic-scale-semigroup-on-connes-cokernel", "unitarity-of-emergent-time", "REQUIRES", C, BRIDGE2, "Needs a positive Hilbert metric and self-adjoint generator transportable to an arithmetic scale flow.")
edge("stochastic-scale-semigroup-on-connes-cokernel", "no-archimedean-prime-joint-space", "BLOCKED_BY", C, BRIDGE2, "Absence of a joint arithmetic scaling action.")
edge("stochastic-scale-semigroup-on-connes-cokernel", "no-canonical-integer-label", "BLOCKED_BY", C, BRIDGE2)
edge("stochastic-scale-semigroup-on-connes-cokernel", "finite-clock-commensurability", "BLOCKED_BY", C, BRIDGE2)

# Index / modular (proposed_additions_index.json).
edge("hecke-index-theorem", "multiplicative-composition-law", "REALIZES", T, "experiments/tfpt-discovery/hecke_index_theorem_result.json")
edge("index-modular-state", "event-log-function", "WOULD_CLOSE", C, "experiments/tfpt-discovery/hecke_index_theorem_result.json#T3_modular")
edge("equality-hunt", "connes-trace-formula-dichotomy", "BLOCKED_BY", T, "Connes, Selecta Math. 5 (1999), 29-106")
edge("connes-trace-formula-dichotomy", "lstar-statement", "REDUCES_TO", C, f"{PAPER}:733-791")

# Bridge-2 objects (proposed_additions_bridge2.json).
# hilbert-polya remapped to hilbert-polya-operator; USED_BY dest must be an
# attempt path, so that proposed edge becomes REQUIRES.
# lstar remapped to lstar-statement.
edge("screw-function-criterion", "weil-positivity", "EQUIVALENT_TO", T, "Suzuki, arXiv:2206.03682, Theorem 1.2", "Criterion equivalence, not a positivity construction.")
edge("schoenberg-helical-embedding", "screw-function-criterion", "EQUIVALENT_TO", T, "Suzuki, arXiv:2209.04658", "The embedding is available precisely when the full screw kernel is positive.")
edge("canonical-system-hamiltonian", "screw-function-criterion", "REQUIRES", C, "Suzuki, arXiv:2206.03682", "A global positive Hamiltonian from the zeta data is the forward problem.")
edge("de-branges-positivity", "weil-positivity", "IMPLIES", T, "Conrey-Li, arXiv:math/9812166", "The implication is sufficient but too strong; Conrey–Li show the premise fails for the natural xi space.")
edge("conductor-operator-burnol", "hilbert-polya-operator", "REQUIRES", H, "Burnol, doi:10.1515/FORUM.2004.16.6.789", "USED_BY remapped: dest must be an attempt path; local operator ingredients do not yield a global zeta point spectrum.")
edge("verified-zeros-height", "compact-window-certificate-mechanism", "BLOCKED_BY", T, "Paley-Wiener theorem; rh/catalog/analysis/bridge2_object_search.md:S3(iv)", "Finite height is not a hard cutoff for compactly supported tests.")
edge("finite-weil-window", "compact-window-certificate-mechanism", "BLOCKED_BY", T, f"{BRIDGE2_OBJ}:S3(iv)", "A whole-window result needs an independent geometric-side certificate or a uniform zero-side tail theorem.")
edge("w4-global-positivity-transfer", "w2-form-density", "REQUIRES", C, "notes/arxiv_w1_note/note_w1_suzuki_identification.tex:421-436", "Domain and operator convergence are prerequisites.")
edge("w4-global-positivity-transfer", "w3-uniform-window-positivity", "REQUIRES", C, "notes/arxiv_w1_note/note_w1_suzuki_identification.tex:428-436", "Finite measurements do not replace uniform positivity.")
edge("w4-global-positivity-transfer", "weil-positivity", "WOULD_CLOSE", C, "notes/arxiv_w1_note/note_w1_suzuki_identification.tex:432-436", "This is the intended global transfer.")
edge("lstar-statement", "finite-weil-window", "EQUIVALENT_TO", T, "verification/v963_lstar_reduction_dictionary.py", "Finite half-filling metric reduction only.")
edge("lstar-statement", "w3-uniform-window-positivity", "WOULD_CLOSE", C, f"{PAPER}:773-790", "A uniform family theorem would provide the finite metric leg; global transfer still requires W2/W4.")

# Lean r475-repair (part_18) and FREQ/grid outer bridges.
# Catalog attempt path is the Lean file itself (part_18.path).
edge("selected-arch-weighted-interpolation-estimate", "selected-arch-error-rate-exists", "IMPLIES", T, f"{ARCH_PACK}/ArchRateClosure.lean:44", "The corrected existential rate, not the refuted prescribed constant.")
edge("selected-arch-error-rate-exists", "selected-arch-error-convergence", "IMPLIES", T, f"{ARCH_PACK}/ArchRateClosure.lean:49", "For each fixed native test; no uniform all-test positivity inference.")
edge("selected-arch-error-quadratic-rate", LEAN_ARCH, "USED_BY", C, LEAN_ARCH, "The original prescribed constant remains refuted; the corrected existential rate is a separate theorem.")
edge("selected-arch-weighted-interpolation-estimate", f"{ARCH_PACK}/ArchRateClosure.lean", "USED_BY", T, f"{ARCH_PACK}/ArchRateClosure.lean:33", "Unconditional source theorem, freshly checked with standard Lean axioms only.")
edge("eventual-selected-read-lower-bound", "native-grid-weil-positivity", "EQUIVALENT_TO", T, f"{ARCH_PACK}/FrontierClosure.lean:8", "CONDITIONAL on FREQ. The AND-premise is explicit in proof_search; neither positivity nor the bound is proved.")
edge("native-grid-weil-positivity", "frequently-selected-aug-dual-resolvent", "REQUIRES", C, f"{ARCH_PACK}/FrontierClosure.lean:8", "This particular read-bound route requires FREQ; not a necessity theorem for every conceivable proof.")
edge("frequently-selected-aug-dual-resolvent", "lstar-statement", "REQUIRES", C, f"{LEAN}/FrequentlySelected.lean:294", "Metric FREQ cone, not Euler-side; requires the L* finite free-window comparison.")
edge("selected-polynomial-approximates-grid", "weil-positivity", "REQUIRES", C, f"{LEAN}/InnerBridges.lean:366", "Contains the channel-positivity bridge; r473 NO_BRIDGE.")

# Geometry audit (proposed_additions_geometry.json).
# USED_BY dest must be an attempt path, so rigid-calabi-yau-f8 → mu4-mark
# becomes USED_BY of the cusp-channel probe.
edge("dyson-fourier-quasicrystal-criterion", "weil-positivity", "EQUIVALENT_TO", T, "arXiv:2402.10604; Weil criterion", "Only after the required renormalization; not the naive positive zero measure.")
edge("dyson-fourier-quasicrystal-criterion", "fourier-quasicrystal-geometry", "REQUIRES", C, "Dyson 2009; arXiv:2402.10604", "Distributional formulation rather than a standard uncorrected Fourier quasicrystal.")
edge("fourier-quasicrystal-geometry", "infinite-rank-prime-fourier-module", "BLOCKED_BY", T, "Fundamental theorem of arithmetic; arXiv:2303.03201", "A single finite-variable Lee-Yang restriction has finite frequency rank.")
edge("infinite-rank-prime-fourier-module", "prime-torus", "REALIZES", T, "Hedenmalm-Lindqvist-Seip, Duke Math. J. 86 (1997)", "The Bohr prime torus carries all independent prime phases, but not the zero generator.")
edge("quantum-metric-graph", "no-composite-orbits", "BLOCKED_BY", C, f"arXiv:1307.6055; {GEOM_NOTE}:B2", "Unconditional only under exact support and no-cancellation hypotheses.")
edge("quantum-graph-decoupling-lemma", "no-composite-orbits", "REDUCES_TO", T, f"{GEOM_NOTE}:B2", "The theorem is explicitly conditional on no cancellation.")
edge("no-composite-orbits", "adele-class-space", "REQUIRES", C, f"Connes 1999; {GEOM_NOTE}:C", "Product-over-places components are the known structural way to isolate primitive primes.")
edge("rigid-calabi-yau-f8", "weight4-gl1-transport", "INSTANCE_OF", T, "LMFDB:8.4.a.a; arXiv:math/0504070", "The f8 cusp channel is a weight-4 motivic L-function, not Riemann zeta.")
edge("rigid-calabi-yau-f8", "experiments/tfpt-discovery/cuspidal_bridge_probe.py", "USED_BY", H, f"{GEOM_NOTE}:B3; experiments/tfpt-discovery/cuspidal_bridge_probe.py:111", "TFPT corpus contact; no RH implication.")
edge("rigid-calabi-yau-f8", "tate-trace-projector", "REQUIRES", T, TATE_NOTE, "The endomorphism motive contains a canonical scalar Tate summand.")
edge("tate-trace-projector", "riemann-zeta", "REALIZES", T, TATE_NOTE, "The scalar line contributes one zeta factor, including the inertia-fixed identity at p=2.")
edge("tate-trace-projector", "tate-information-loss", "BLOCKED_BY", T, TATE_NOTE, "The projector is universal and retains no level-8-specific positivity data.")
edge("tate-information-loss", "verification/v1021_all_place_tate_rank_audit.py", "USED_BY", T, TATE_NOTE, "Exact correction and claim fence.")
edge("fixed-finite-carrier-rank-obstruction", "strict-weil-window-floor-zhu", "REQUIRES", C, "arXiv:2608.24827v2; " + TATE_NOTE, "The abstract rank-nullity lemma is internal; its application to the Weil window is conditional on the external preprint floor.")
edge("all-place-tate-weil-realization", "fixed-finite-carrier-rank-obstruction", "BLOCKED_BY", C, TATE_NOTE, "For an exact linear pullback on the full strict window, one fixed finite carrier is excluded; nonlinear methods, growing discretizations and direct limits are not.")
edge("fixed-finite-carrier-rank-obstruction", "verification/v1021_all_place_tate_rank_audit.py", "USED_BY", T, TATE_NOTE, "The rank-nullity lemma is exact; the Weil-window application is separately conditional.")
edge("all-place-tate-weil-realization", "open-global-all-place-intersection", "REQUIRES", C, TATE_NOTE)
edge("all-place-tate-weil-realization", "arakelov-intersection", "REQUIRES", C, TATE_NOTE)
edge("all-place-tate-weil-realization", "arithmetic-hodge-index", "REQUIRES", C, TATE_NOTE, "The required absolute-square theorem is not supplied by the existing line-bundle theorem.")
edge("all-place-tate-weil-realization", "weil-quadratic-form", "WOULD_CLOSE", C, TATE_NOTE, "Exact pullback plus independent Hodge-index positivity would imply Weil positivity.")
edge("absolute-twistor-line", "all-place-tate-weil-realization", "REQUIRES", H, "arXiv:2609.00299; " + TATE_NOTE, "To serve as an RH route, this candidate carrier still needs the square, correspondence compiler and intersection theorem.")
edge("petz-watatani-tate-network", "all-place-tate-weil-realization", "REDUCES_TO", C, TATE_NOTE, "The normal compatible limit and signed Weil identification are the same open all-place bridge.")
edge("petz-watatani-tate-network", "no-archimedean-prime-joint-space", "BLOCKED_BY", C, TATE_NOTE)
edge("rankin-mean-pointwise-exponent-drop", "experiments/tfpt-discovery/rankin_positivity_miniature_probe.py", "KILLED_BY", T, "verification/v1021_all_place_tate_rank_audit.py", "The historical finite identities survive; the exponent-extraction route does not.")
edge("arithmetic-topology-prime-knots", "deninger-foliated-dynamics", "REQUIRES", H, "Morishita 2012; arXiv:2301.11643", "USED_BY remapped: dest must be an attempt path; topological analogy motivates, but does not construct, the analytic flow.")
edge("hyperbolic-ruelle-dynamics", "no-composite-orbits", "BLOCKED_BY", H, f"Fried 1986; Patterson-Perry 2001; {GEOM_NOTE}:B4", "Known primitive length spectra and archimedean factors do not match Riemann zeta; no universal impossibility theorem is asserted.")
edge("deninger-foliated-dynamics", "stochastic-scale-semigroup-on-connes-cokernel", "REDUCES_TO", C, f"Deninger ICM 1998; {BRIDGE2}", "Both require the same unconstructed arithmetic all-place flow and positive generator.")
edge("k3-hodge-lattice", "hodge-riemann-positivity-candidate", "INSTANCE_OF", T, "arXiv:1501.04049", "Geometric polarization without the global prime scale action.")
edge("rosati-positive-geometry", "positive-cone-blindness", "BLOCKED_BY", C, "arXiv:1509.00797; experiments/tfpt-discovery/positive_cone_blindness_probe.py", "The local theorem is valid; the barrier concerns assembling independent local positivity into global zeta positivity.")
edge("mobius-scale-group", "connes-adele-scaling-flow", "REDUCES_TO", T, "Tate thesis; Berry-Keating 1999; Connes 1999", "The arithmetic Möbius-scale ingredients are already present in the adelic scaling framework.")
edge("mobius-strip-topology", "no-archimedean-prime-joint-space", "BLOCKED_BY", H, f"{GEOM_NOTE}:B5", "Nonorientability alone creates no arithmetic joint space.")
edge("finite-spectral-triple-zero-approximants", "hilbert-polya-operator", "WOULD_CLOSE", C, "arXiv:2511.22755; arXiv:2511.23257", "Requires proved global spectral or determinant convergence.")
edge("finite-spectral-triple-zero-approximants", "w2-form-density", "REQUIRES", C, BRIDGE2_OBJ, "Operator-domain and limit control are the analogous open step.")
edge("quantum-torus-geometry", "no-archimedean-prime-joint-space", "BLOCKED_BY", H, f"{GEOM_NOTE}:B6", "No canonical zeta all-place action is known.")
edge("lapidus-maier-fractal-string-criterion", "weil-positivity", "EQUIVALENT_TO", T, "doi:10.1112/jlms/52.1.15; Weil criterion", "Both are RH-equivalent criteria; this edge does not assert a direct proof between their native formulations.")
edge("berkovich-bruhat-tits-geometry", "scaling-site", "SPECIAL_CASE_OF", H, "arXiv:1507.05818", "Local nonarchimedean geometry must be assembled in the global tropical/adelic site.")
edge("causal-spin-network-geometry", "no-archimedean-prime-joint-space", "BLOCKED_BY", H, f"{GEOM_NOTE}:B6", "No accepted arithmetic all-place bridge was found.")
edge("stochastic-scale-semigroup-on-connes-cokernel", "no-composite-orbits", "REQUIRES", C, f"{GEOM_NOTE}:C", "Its orbit trace must derive, rather than assume, the prime-only primitive decomposition.")

# External proposals 5.9. (proposed_additions_nb.json).
# nyman-beurling-criterion / baez-duarte-criterion reused, not duplicated.
edge("burnol-lower-bound", "baez-duarte-rate-conjecture", "REQUIRES", T, "Burnol 2002; Bettin-Conrey-Farmer 2013", "Any proposed asymptotic constant must respect Burnol's multiplicity-squared liminf floor.")
edge("baez-duarte-rate-conjecture", "baez-duarte-criterion", "IMPLIES", T, "Báez-Duarte 2003; E_N sim C/log N", "The conjectured positive rate forces E_N to zero.")
edge("dyadic-block-capture-eta", "baez-duarte-rate-conjecture", "REQUIRES", C, "experiments/tfpt-discovery/nb_dyadic_capture_probe.py", "The block statement is stronger structural information than the bare rate because it specifies where dyadic improvement lies.")
edge("dyadic-block-capture-eta", "riemann-hypothesis", "WOULD_CLOSE", C, "E_2N <= (1-eta_k)E_N and Báez-Duarte criterion", "A bound eta_k>=c/k implies E_(2^k)->0. The converse is not known, so this is deliberately not typed EQUIVALENT_TO.")
edge("dyadic-block-capture-eta", "vasyunin-gram-matrix", "REQUIRES", T, "experiments/tfpt-discovery/nb_dyadic_capture_probe.py", "Eta is a residual Schur-complement projection computed from this Gram structure.")
edge("vasyunin-gram-matrix", "nyman-beurling-space", "REALIZES", T, "Vasyunin 1995; Landreau-Richard 2002", "The matrix records the Hilbert geometry of the fractional-part dilation family.")
edge("gaussian-smoothed-zero-density", "weil-quadratic-form", "TRANSFORM_OF", T, "experiments/tfpt-discovery/heat_gabor_restatement_probe.py", "The cross-term-free heat object is an exact linear transform of the pure Gabor Weil form.")
edge("negative-explosion-criterion-a", "weil-positivity", "EQUIVALENT_TO", C, f"{LEAN}/GaborExposedOrbit.lean; heat_gabor_restatement_probe.py", "Equivalence uses the exposed-orbit assembly and grid-continuity passage; it is a same-hardness restatement.")
edge("negative-explosion-criterion-a", "gaussian-smoothed-zero-density", "REQUIRES", T, "experiments/tfpt-discovery/heat_gabor_restatement_probe.py", "Criterion A is stated directly on this heat-normalized object.")
edge("dyadic-block-capture-eta", "experiments/tfpt-discovery/nb_dyadic_capture_probe.py", "USED_BY", C, HEAT_NB, "Finite ladder through N=512; eta_k>=c/k remains open.")
edge("negative-explosion-criterion-a", "experiments/tfpt-discovery/heat_gabor_restatement_probe.py", "USED_BY", C, HEAT_NB, "Same-hardness restatement; prime budget e^{1/(8a)} vs slack e^{1/sqrt(a)}.")
edge("gaussian-smoothed-zero-density", "experiments/tfpt-discovery/heat_gabor_restatement_probe.py", "USED_BY", T, HEAT_NB, "Heat-kernel identity and convolution normalization.")

from research_seeds_20260909 import extend as extend_late_research
extend_late_research(node, edge)

# Source-pinned paper claims. These are scope annotations, not Lean rules.
import sys
sys.path.insert(0, str(HERE.parent))
from paper_knowledge import graph_rows
paper_nodes, paper_edges = graph_rows()
for row in paper_nodes:
    node(row['id'], row['type'], row['name'], row['aliases'], row['definition'],
         row['status'], row['sources'], row['tags'])
for row in paper_edges:
    edge(*row)

# Deduplicate stable edge identities.
ids = {n["id"] for n in nodes}
dedup: dict[tuple, dict] = {}
for e in edges:
    assert e["src"] in ids, e
    if e["rel"] not in {"USED_BY", "KILLED_BY"}:
        assert e["dst"] in ids, e
    dedup[(e["src"], e["dst"], e["rel"], e["source"])] = e
edges = list(dedup.values())
assert len(nodes) >= 120, len(nodes)
assert len(edges) >= 250, len(edges)

lexicon = {}
extract_stop = {
    "ARCH", "E8", "FE", "Fourier", "GUE", "Krein", "MAIN", "Mellin",
    "Montel", "Pick", "POLE", "PRIME", "RH", "SCRARITH", "SMOOTH",
    "UCP", "Vitali", "relay", "xi", "zeta", "λ*", "L*",
}
for n in nodes:
    terms = [
        n["name"], n["id"].replace("-", " "), n["id"].replace("-", "_"),
        *n["aliases"],
    ]
    terms = sorted(
        {
            t.strip() for t in terms
            if len(t.strip()) >= 3 and t.strip() not in extract_stop
        },
        key=lambda x: (-len(x), x.lower()),
    )
    lexicon[n["id"]] = terms

(HERE / "seed_nodes.json").write_text(json.dumps(nodes, ensure_ascii=False, indent=2) + "\n")
(HERE / "seed_edges.json").write_text(json.dumps(edges, ensure_ascii=False, indent=2) + "\n")
(HERE / "lexicon.json").write_text(json.dumps(lexicon, ensure_ascii=False, indent=2) + "\n")
print(f"seed nodes={len(nodes)} edges={len(edges)} aliases={sum(map(len, lexicon.values()))}")
