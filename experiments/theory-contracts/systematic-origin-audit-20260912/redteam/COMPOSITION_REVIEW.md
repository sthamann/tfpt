# Peer review of overlapping Bell-block composition

12 September 2026. NON-RH, finite conditional construction.

## Independently derived identities

Let `V=|Phi_d>_12 tensor I_3`, `W=I_1 tensor |Phi_d>_23`.
Both are isometries and direct index contraction gives `V*W=I/d`.
For `H=2I−VV*−WW*`,

    H(V+W) = (1−1/d)(V+W),
    H(V−W) = (1+1/d)(V−W).

The normalized ground isometry is

    A = (V+W)/sqrt(2(1+1/d)).

The two d-dimensional ranges are orthogonal; the orthogonal complement has
energy 2. Therefore at d=4 the ground energy is 3/4, its multiplicity is 4,
the first excitation energy is 5/4, and the gap is 1/2.

For an arbitrary operator O on the left endpoint, the four contractions are

    V*(O tensor I tensor I)V = tr(O) I/d,
    W*(O tensor I tensor I)W = O,
    V*(O tensor I tensor I)W = O/d,
    W*(O tensor I tensor I)V = O/d.

The same holds for the right endpoint after interchanging V and W. Thus

    A* O_endpoint A = ((d+2)O + tr(O)I)/(2(d+1)).

Writing this as `D(O)=aO+(1−a)tr(O)I/d` gives
`a=(d+2)/(2(d+1))`, hence `a=3/5` at d=4.

Two conjugate blocks, with a physical Bell projector C across their adjacent
endpoints and B their product ground embedding, therefore give

    Q = B* C B = a² P + (1−a²)I/d² = (I+9P)/25,

where P is the logical Bell projector at d=4. Because C is a projector,

    [(I−BB*)CB]* [(I−BB*)CB] = Q−Q²
                             = (24I+126P)/625.

Its eigenvalues are 6/25 (multiplicity 1) and 24/625 (multiplicity 15), both
strictly positive. Thus every nonzero encoded logical state has a nonzero
component leaving the bare product-block subspace under the linking term.

`composition_direct.py` independently checks this by constructing B as a
4096-by-16 sparse matrix and applying the physical middle Bell projector by
six-site index contractions. It does not import the interaction checker,
expand Bell projectors in the source-word basis, or assume the boundary map.

## Exact scope of the effective coupling statement

The identity

    B*(I−C)B = (9/25)(I−P) + (3/5)I

is an exact static compression. For a Hamiltonian with weak interblock
coupling lambda and uncoupled block Hamiltonians, it is also the first-order
degenerate effective Hamiltonian. Calling the compressed value an exact
closed renormalization flow of the full dynamics would be incorrect:
the original bare embedding is not invariant, and higher-order effects are
not controlled by the compression identity alone.

However, the converse overclaim must also be avoided. Leakage does **not**
exclude every exact dressed low-energy effective Hamiltonian. For exactly
two conjugate blocks, with exact full U(4) symmetry and a sufficiently weak
link so that the original 16-dimensional band remains isolated, a
symmetry-respecting dressed identification carries `4 tensor conjugate(4)
= 1 direct-sum 15`. Each irrep occurs once. Schur's lemma then restricts any
such effective invariant Hamiltonian to a scalar plus a logical Bell
projector, potentially to all orders but with different coefficients.
This conditional observation does not establish a local many-block RG:
larger chains have multiplicities and can generate additional interactions,
while dressing and observables must be tracked explicitly.

The accurate conclusion is:

> The bare block projection preserves the Bell interaction's form, but it
> does not supply an invariant microscopic subspace or exact closed
> many-block dynamics. Dressed two-block reductions are a distinct question.

No physical graph, tensor factorization, full active U(4) symmetry,
weak-coupling scale or TFPT source realization is derived by these identities.
