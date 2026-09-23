# Composing the same simple Bell glue: exact obstruction and a surviving block rule

12 September 2026. NON-RH. Companion check: `composition.py`.
This continues the conditional conjugate-pair result in `RESULTS.md` without
changing the original compiler, the existing rotor parent, or any TOE gate.

## Ergebnis in einfachen Worten

**Der einfachste Bell-Baustein lässt sich nicht naiv aneinanderstecken:**
Ein einzelnes vierdimensionales System kann nicht gleichzeitig mit seinem
linken und seinem rechten Nachbarn jeweils in einem reinen Bell-Zustand
sein. Drei solche Faktoren besitzen daher keinen Zustand, der beide
Kopplungsbedingungen perfekt erfüllt.

Aber es bleibt eine überraschend einfache Struktur erhalten: Der beste
gemeinsame Zustandsraum ist wieder vierdimensional und trägt dieselbe
unitäre Darstellung wie ein ursprünglicher Faktor. Komprimiert man die
Randkopplung zweier solcher Blöcke auf diese Zustandsräume, erhält man
**wieder eine Bell-Kopplung**, mit Faktor 9/25 und einem unwirksamen
Energie-Offset. Das ist eine konkrete selbstähnliche Rechenregel.

Die wichtige Grenze wurde ebenfalls exakt bestimmt: Die reale Randkopplung
verlässt diese Block-Zustandsräume. Die komprimierte Regel ist daher kein
exakt abgeschlossener universeller Motor. Sie ist ein kontrollierbar zu
entwickelnder Kandidat für eine effektive Beschreibung, zunächst in erster
Störungsordnung und unter den ausdrücklich hinzugefügten Voraussetzungen.

## 1. Hypotheses and three-factor model

Choose d-dimensional factors A,B,C, d>=2, with global active symmetry
U tensor conjugate(U) tensor U. Adjoining physical factors, choosing this
duality, imposing full U(d), identifying neighbors and interpreting H as
physical time evolution are hypotheses, not outputs of the compiler audit.

Set phi=(1/sqrt(d)) sum_a |a,a> and

    P = |phi><phi|_AB tensor I_C,
    Q = I_A tensor |phi><phi|_BC,
    H = (I-P)+(I-Q) = 2I-P-Q.

Both terms are exactly the conditional unique pair glue already selected
under full dual-unitary symmetry and a unique pair ground state. No new
term, factor-specific correction or compensating counterterm is added.

## 2. General exact proof of compatibility and complete spectrum

Define isometries V,W:C^d -> (C^d)^tensor3 by

    V psi = phi_AB tensor psi_C,
    W psi = psi_A tensor phi_BC.

Index contraction gives V*W=W*V=I/d, while V*V=W*W=I. Hence

    P=VV*, Q=WW*, P Q P = P/d^2, Q P Q = Q/d^2.

If P psi=Q psi=psi, the first identity gives psi=psi/d^2. For d>1 this
forces psi=0. Thus the two Bell constraints have NO common nonzero state.
This is an exact finite-dimensional overlap obstruction, not a numerical
failure or a claim that interacting many-body states cannot exist.

Moreover,

    (P+Q)(V+W)=(1+1/d)(V+W),
    (P+Q)(V-W)=(1-1/d)(V-W),
    (V+W)*(V-W)=0,
    (V+-W)*(V+-W)=2(1+-1/d)I.

Both maps have rank d for d>1. The ranges of P,Q together have dimension
2d; their orthogonal complement has dimension d^3-2d and P+Q=0 there.
This proves the COMPLETE spectrum, not merely candidate eigenvalues:

| Energy of H | Multiplicity |
| --- | --- |
| 1-1/d | d |
| 1+1/d | d |
| 2 | d^3-2d |

At d=4 these are **3/4 (fourfold), 5/4 (fourfold), 2 (56-fold)**.
The three-factor spectral gap above the ground multiplet is 1/2.
No unique global ground follows from unique pair grounds. The positive
ground energy means frustration relative to the two pair-zero conventions;
subtracting that scalar does not make both original constraints satisfied.

Let Z=(V+W)/sqrt(2(1+1/d)). Then Z is the ground isometry. It obeys

    (U tensor conjugate(U) tensor U) Z = Z U.

Thus the surviving d-dimensional ground degree of freedom has exactly the
original fundamental representation, not a newly inferred spatial dimension.
Both edge Bell fidelities are fixed throughout the ground space:

    Z*P Z = Z*Q Z = (1+1/d)I/2.

For d=4 each is 5/8, not one. The checker verifies these identities for
d=2,3,4 and verifies the representation intertwiners on all sixteen actual
Hermitian d=4 compiler words. General validity follows from the identities
above; it is not inferred from those three finite cases.

## 3. Varying positive weights cannot restore compatibility

For J,K>0, let H_JK=J(I-P)+K(I-Q). On the independent, nonorthogonal
coordinates (V,W), its matrix is

    [[K,-J/d],[-K/d,J]].

It has the two eigenvalues

    E_minus/plus=(J+K -/+ sqrt((J-K)^2+4JK/d^2))/2,

each with multiplicity d; the complementary energy is J+K, multiplicity
d^3-2d. Since

    (J+K)^2 - ((J-K)^2+4JK/d^2) = 4JK(1-1/d^2)>0,

the ground energy remains strictly positive for d>1 and both weights
positive. Ground multiplicity remains d. Setting a weight to zero removes
one constraint rather than solving its compatibility. These statements
do not address arbitrary additional Hamiltonians.

## 4. Positive continuation: the exact boundary compression rule

For an arbitrary dxd boundary observable O, direct contraction gives

    V*(O_A)V = Tr(O)I/d,       W*(O_A)W = O,
    V*(O_A)W = W*(O_A)V = O/d.

Consequently the ground encoding has the same boundary channel on A and C:

    Z*(O_A)Z = Z*(O_C)Z
       = a O + Tr(O)I/[2(d+1)],
    a = (d+2)/[2(d+1)].

This is a unital depolarizing map on observables. It is a compression
identity, not an assumption about stochastic motion. At d=4, a=3/5.
The checker tests the complete source-word basis, so the statement covers
every complex linear combination, not selected diagonal measurements.

### Established quantum-information identification, not a TFPT fingerprint

Tracing out the middle factor gives exactly

    Tr_B(Z rho Z*) = [2/(d+1)] P_sym (rho tensor I) P_sym,
    P_sym=(I+F_swap)/2.

This is the standard symmetric 1-to-2 universal cloning channel, not a newly
unique TFPT primitive. The formula specializes equation (3.3) of
[R. F. Werner, Optimal Cloning of Pure States](https://arxiv.org/html/quant-ph/9804001v1),
with N=1 and M=2. The checker independently compares all sixteen d=4 matrix
units after the actual middle-factor trace, including off-diagonal units.
The outputs are approximate clones with contracted marginals, not forbidden
perfect copies of an unknown quantum state. The useful new audit result is
the exact identification in this conditional compiler construction and its
interaction/composition limits, not discovery of universal quantum cloning.

Now choose two CONJUGATE three-factor blocks, with encoding
A_block=Z tensor conjugate(Z). Their selected neighboring boundary factors
transform as U and conjugate(U). Let B be the physical Bell projector on
those two boundary factors (identity on the other four factors). Writing
the Bell projector in a Hilbert-Schmidt orthogonal Hermitian word basis
and applying the two boundary channels gives the exact compressed link

    R=A_block* B A_block
      = a^2 P_logical + (1-a^2) I/d^2.

At d=4 this is

    R=(I+9 P_logical)/25,
    A_block*(I-B)A_block
      =(9/25)(I-P_logical)+(3/5)I.

Thus a pair of effective d=4 ground factors inherits the SAME Bell
coupling form, with coefficient multiplied by 9/25, plus scalar energy.
This is an exact algebraic compression and a natural FIRST-ORDER
effective interaction when a weak interblock link is added to strong
intrinsic block Hamiltonians. It is not by itself an exact renormalization
transformation or a proof of iteration to a continuum fixed point.

## 5. Exact leakage: why compression is not invariant dynamics

Because B is an orthogonal projector and A_block is an isometry, the
off-code transition operator

    L=(I-A_block A_block*) B A_block

has Gram matrix

    L*L=R-R^2.

No 4096-dimensional dense diagonalization is required: this follows
algebraically from B^2=B and the independently established full boundary
compression. At d=4 the exact result is

    L*L=(24 I+126 P_logical)/625.

Its eigenvalues are **6/25 (multiplicity one)** and **24/625 (multiplicity
fifteen)**. Thus every nonzero logical input has nonzero coupling leakage.
There is no hidden exact invariant subspace inside the whole two-block
BARE product-ground code for this boundary projector. The complementary interaction
I-B has the same leakage norm.

This does NOT rule out an exact dressed low-energy spectral subspace of
the coupled finite system. Such a subspace changes the encoding. In a
preserved isolated 1-plus-adjoint band, full dual symmetry could again
restrict a dressed effective Hamiltonian to a scalar plus Bell projector,
with corrected coefficients. Neither that isolated-band construction nor
its extension to many blocks is supplied by the bare compression identity.

For a fixed finite system and a link multiplied by epsilon, leakage starts
quadratically in time, epsilon^2 t^2 <L*L>, while the compressed interaction
is the first-order degenerate-perturbation term. A complete effective
theory would still need higher-order terms and quantitative error control
for the chosen coupling, number of blocks and times. No such convergence
or large-network control is asserted here. The bare block gap 1/2 is known,
but a gap by itself does not certify arbitrary iterative truncations.

## 6. Independent virtual legs are a different construction

One can avoid the overlap obstruction by replacing the shared B factor
with B_left tensor B_right, each of dimension d. Then the two Bell terms
act on disjoint pairs A-B_left and B_right-C and commute. Their unique
zero-energy state is the product of two Bell pairs. This has total space
dimension d^4 instead of d^3 and central dimension d^2 instead of d.

The central marginal of that pure state is I_(d^2)/d^2. Its rank d^2
prevents a lossless isometric identification with the original d-dimensional
central factor. At d=4 the center has rank16, verified explicitly. The
virtual-leg spectrum follows by adding two pair spectra: 0 (multiplicity1),
1 (multiplicity2(d^2-1)), 2 (multiplicity(d^2-1)^2).

A subsequent projection from virtual legs to a smaller physical factor
would change the construction and generally the constraints. Such a map,
its physical reason and the resulting parent would need separate proof.
This is not a prohibition on tensor-network approaches; it prevents an
unannounced increase of local degrees of freedom from being called a
solution of the original shared-factor problem.

## 7. What is and is not newly established

Established within the explicit finite conditional model:

- exact pair-glue composition spectrum and incompatibility;
- a surviving fundamental ground representation;
- a fully derived boundary map and self-similar compressed Bell coupling;
- strict leakage from that compressed subspace;
- the extra local dimension needed by the disjoint-virtual-leg workaround.

Not established: physical pairing, origin selection of full active U(4),
an actual TFPT spatial graph, the compact-rotor/compiler identification,
exact many-block closure, selected energy scales, continuum, or any T1-T8
completion. The positive compression law is a concrete research advance
without changing these proof boundaries.

## Verification and debug provenance

`composition.py` uses the same pinned actual four-generator source and
verifies all eight inherited hashes. All checks use explicit exceptions,
exact rational/symbolic arithmetic, and no optimization-removable asserts.

An initial weighted-polynomial check failed because it compared an expanded
expression to a factored expression structurally. The systematic-debugging
procedure isolated that formatting issue: their symbolic difference was
exactly zero, while a deliberately shifted negative control was -1. The
fix compares the simplified difference to zero; no mathematical acceptance
criterion or expected spectrum was weakened.

Final executed receipt: **123 exact checks** in both normal and `-OO`
execution; subprocess comparison confirms byte-identical JSON. The initial
interaction checker was not changed during this continuation. Only the
new `composition.py` and this `COMPOSITION.md` were created/edited.
