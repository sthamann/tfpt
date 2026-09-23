# A rigorously improved finite-correlation dimer ansatz

For the declared uniform primitive source chain, a very small correlated
dimer ansatz has exact energy density **5023/5476 < 1**, improving the
uncorrelated Bell-dimer value 1. This is a variational upper bound on the
ground energy density, not an exact ground state or a lower bound.

## 1. State and transfer normalization

Start from a periodic alternating chain with Bell pairs (12)(34)... and
apply disjoint local filters F(t)=I-t h4 on the intervening bonds (23),
(45),... . Take each filtered bond as a two-register cell. The bond-four
matrix-product tensors are

    A^{st}_{ab}=F(t)_{st,ab}/2.

No blocking truncation is performed. At t=0 these tensors describe the
original product of Bell links between the chosen cells. The actual
source h4 is real, so the alternating bond orientations give the same
matrix in this computation; the checker verifies this explicitly.

For E(X)=sum_st A^{st} X A^{st}*, both fixed matrices are the identity:

    E(I)=pI, E*(I)=pI, p=1-4t+5t^2=Tr(F^2)/16.

In the complete sixteen-word Clifford basis its eigenvalues are

| Clifford degree | Multiplicity | Unnormalized transfer eigenvalue |
| --- | --- | --- |
| 0 | 1 | p |
| 1 | 4 | r1=t-2t^2 |
| 2 | 6 | r2=t^2/2 |
| 3 or 4 | 5 | 0 |

The Perron eigenvalue is strictly dominant for every real t. Indeed
p>0, p-r1>0, p+r1>0 and p-r2>0, as witnessed by

    p    =5(t-2/5)^2+1/5,
    p-r1 =7(t-5/14)^2+3/28,
    p+r1 =3(t-1/2)^2+1/4,
    p-r2 =(9/2)(t-4/9)^2+1/9.

Thus E/p converges to X -> Tr(X)I/4 and is primitive: sufficiently high
powers send every nonzero positive matrix to a positive definite one.
One can see this directly from convergence uniformly on trace-one
positive matrices. On 0<=t<1/4 the filter itself is positive definite
and invertible, since h4 has eigenvalues 0,1,2,3,4. Outside that interval
transfer primitivity must not be confused with positivity of the filter.

For L cells the periodic norm contraction is

    Tr(E^L)=p^L+4r1^L+6r2^L, L>=1.

Strict spectral dominance justifies the limiting local expectations
below. They are exact transfer limits, not finite-size extrapolations.

## 2. The two bond energies

The filtered intracell bond has density matrix F^2/(16p), hence

    e_inside(t)=Tr(h4 F^2)/(16p)=(2-10t+14t^2)/p.

The links between cells were initially Bell pairs. Their energy cannot
be discarded after filtering. Direct physical-observable insertions in
the transfer network give a boundary numerator

    b(t)=1-4t+(7/2)t^2.

For each original primitive synchronization direction the two-cell
expectation is (b/p)^2. Equivalently, the left and right insertion
matrices each equal b times the appropriate original source generator;
contracting them with the Perron fixed matrices yields this ratio.
Therefore

    e_between(t)=2-2(b/p)^2.

Both insertion maps are independently evaluated in the checker, so this
does not replace the energy of a link with a one-cell guess. The two
bond types together give the exact energy per physical register:

    e(t)=[e_inside(t)+e_between(t)]/2
        =(2-10t+14t^2)/(2p)+1-(b/p)^2
        =(4-36t+140t^2-260t^3+191t^4)/(4p^2).

At t=0, e_inside=2, e_between=0 and e=1. The exact derivative e'(0)=-1
proves that small positive filters improve the product-dimer energy,
despite the induced positive cost on the initially perfect Bell links.

## 3. An explicit rational improved state

Choose t=1/8. Then

    p=37/64,
    e_inside=62/37,
    e_between=435/2738,
    e=5023/5476 = approximately 0.9172754.

The reduction from the dimer baseline is 453/5476, approximately 8.27%.
The normalized nonzero subleading transfer eigenvalues are 6/37 and
1/74, both strictly below one. The resulting state has finite
correlation length in cells, and F has eigenvalues 1,7/8,3/4,5/8,1/2,
all positive. This proves the ansatz is well-defined and improves the
energy for the infinite uniform chain within the conditional model.
At this chosen value the sixteen Kraus matrices span all M4 because
F is invertible, so the transfer is even strictly positive in one step.
The stated e(t) is the thermodynamic fixed-point expectation; a finite
periodic chain retains the subleading transfer terms in its norm and
observable contractions and need not have exactly this energy density.

## 4. Scope and useful continuation

Unlike treating disconnected dimers as an exact uniform-chain ground,
this ansatz explicitly includes the cost and benefit of changing their
neighboring correlations. Its small transfer matrix supplies an analytic
variational benchmark for further computations.

It does not establish the exact ground state, a many-body spectral gap,
or an exact renormalization fixed point. A variational state having
finite correlation length does not prove that the Hamiltonian is gapped.
One may optimize the single parameter or enlarge the variational family;
neither step by itself closes the exact ground-energy or uniform-gap
problem. The Hamiltonian and register graph remain declared inputs, and
no physical parent or T1-T8 closure is selected by the calculation.

## 5. Executed verification

The checker passed 56 exact checks under normal Python and Python -OO,
with byte-identical JSON output. The scoped whitespace check passed.
Tests include source/dependency pins, both Perron matrices, all sixteen
transfer word eigenvectors, strict spectral dominance identities,
independent left/right physical insertions, both bond energies, the
exact rational improvement and full Kraus span at t=1/8. No numerical
ground-state diagonalization, tolerance or fit is used.
