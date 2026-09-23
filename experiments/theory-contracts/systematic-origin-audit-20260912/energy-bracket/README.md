# Exact energy bracket and the state-symmetry boundary

12 September 2026. NON-RH. Same stipulated uniform primitive Hamiltonian
as the preceding work; no physical graph, time, or T1-T8 closure is selected.

## 1. Updated result

For the thermodynamic ground-energy density of the original chain,

    3249/4000 <= e_ground <= 254850665/279993289,

or approximately

    0.812250000 <= e_ground <= 0.910202762.

The previous bracket was (4-sqrt(6))/2 through5023/5476. Both ends have
improved, by independent methods. The lower bound is an exact whole-cluster
positivity certificate, not a variational estimate. The upper bound is an
exactly evaluated trial state, not a solution of the original ground state.
Neither inequality states a physical energy in measured units.

## 2. A complete five-site certificate gives the lower bound

The exact source-to-occupation basis yields two commuting Pauli triples.
In the minus-exchange gauge a nearest-neighbor bond is

    h=2I-(1/2)[tau_x tau_x'+tau_y tau_y'
                +tau_z tau_z'(sigma_x sigma_x'+sigma_y sigma_y')].

Consequently total tau and sigma occupations are conserved. For five sites,
the36 sectors (n_tau,n_sigma), each between0 and5, have dimensions
C(5,n_tau)C(5,n_sigma). They sum to1024 and the largest dimension is100.
The checker establishes the hopping rule from the pinned source on BOTH
alternating bond orientations and checks all two-site block/off-block entries.
Tensoring that exact local identity proves the many-site sector construction.
No alleged lowest sector is selected in advance.

In each sector s form the integer, real-symmetric matrix

    B_s=1000 H_(5,s)-3249 I.

The checker computes every coefficient of det(xI+B_s) in exact integer
arithmetic and verifies that all coefficients are strictly positive. This
polynomial is positive for every x>=0. If B_s had a nonpositive eigenvalue,
the polynomial would vanish at its negative, a contradiction. Thus B_s is
positive definite in every sector, proving

    H_5 >= (3249/1000) I.

For an even periodic physical chain of length N>=6, sum this inequality
over allN consecutive five-site windows. Every primitive bond appears four
times, so

    4 H_N >= N (3249/1000) I.

Dividing by4N proves the lower bound at these finite lengths and in the
thermodynamic limit. Open and periodic ground energies differ by a bounded
end bond, so they have the same limiting density. This is an all-length
operator argument, not extrapolation of five-site numerical eigenvalues.

`cluster_bound.py --explore` is a separate optional numerical guide used to
choose the rational test value. The accepted proof does not call NumPy or
use a floating-point eigenvalue. Sector determinants and coefficient hashes
are recorded; the exact checker recomputes all coefficients.

### Negative control and a useful stopping condition

The nearby false proposal H5 >=13/4 I is rejected exactly: in the (2,2)
sector, det(4H5-13I) is negative. There is therefore an eigenvalue below13/4.
This also shows that a lower bound obtained solely from identical unweighted
five-site windows cannot reach13/16=0.8125 per bond.

That is a ceiling of THIS LOWER-BOUND METHOD, **not** an upper bound on the
true infinite-chain energy. Merely computing the five-site minimum to more
decimal places cannot close the remaining bracket. Larger windows or extra
overlap/consistency constraints are needed for a material improvement.

## 3. Better correlations without larger matrix-product bond dimension

The previous trial applied F=I-t h4 on alternate bonds between Bell dimers.
First extend it to

    F=I-t h4+u h4^2.

The positive rational choice t=8/33,u=1/33 has the simple form

    F=((h4-4I)^2+17I)/33.

It gives e=53950/59177, approximately0.911671764. The full earlier linear
family is recovered at u=0 as an exact regression.
[Quadratic construction](polynomial_filter.md).

The complete spectral-filter family is still very small. Since h4 has only
the five eigenvalues0,1,2,3,4, write F=f(h4) using five real values f0,...,f4.
An overall scale cancels from normalized expectations. Define

    p=(1/16)sum_k C(4,k) f_k^2,
    q=(1/16)sum_k k C(4,k) f_k^2,
    b=(f0 f3+3 f1 f2+f1 f4+3 f2 f3)/8.

The exact source contractions reduce the thermodynamic energy to

    e_f=1+q/(2p)-(b/p)^2.

One way to understand the b formula is to conjugate by one primitive
generator: this preserves its own constraint bit and flips the other three.
Counting those16 constraint syndromes gives the displayed products. The
physical left/right insertions and all16 transfer directions are checked
independently, rather than inferred from an energy fit.

The transparent positive choice (f0,...,f4)=(16,11,9,8,7) already gives
2134375/2343961, approximately0.910584690. The somewhat finer rational
witness

    (f0,...,f4)=(52,36,30,27,23)

gives the reported upper bound254850665/279993289. These integers are
chosen trial parameters, not derived constants of nature or a claim of
global optimality. All five values are positive; F is invertible. The
sixteen reshaped matrix-product cell tensors span M4, establishing a
strictly positive transfer map and a well-defined unique transfer limit.
The bond dimension is still four, not an increasing chain-sized object.

For this witness the normalized transfer eigenvalues by Clifford degree are

    (1,3309/16733,1433/16733,1041/16733,533/16733),

with multiplicities1,4,6,4,1. The bond costs are respectively
26848/16733 and60453746/279993289, both included in the reported mean.
The Hamiltonian has not been changed. Finite-ring contractions keep the
subleading transfer terms; the simple formula is a thermodynamic expectation.
[Five-value source construction](spectral_filter.md).

## 4. Internal symmetry is not the absence of spatial order

The independent [state audit](state_symmetry.md) examines the earlier
t=1/8 branch quantitatively. Primitive/family and continuous internal
Spin(4) symmetry are retained. Individual registers are already maximally
mixed, I4/4. Nevertheless, the two alternating bond energies differ by
Delta=4153/2738. The selected branch is therefore not one-site translation
invariant. The same internal-covariance argument extends to every polynomial
F(h4); the numerical contrast and plateau quoted here refer specifically
to the audited linear-filter branch, not automatically to every new filter.

Mixing equally with the one-site translate makes the mean energy the same
on every bond but leaves a connected long-range covariance Delta^2/4 on
equal-parity bonds. Averaging hides the local alternation; it does not
erase the branch information from correlations. The symmetric finite cat
state has interference terms, but its local thermodynamic limit has the
same mixture behavior. This is shown from the clustering of the two branches.

Nor can an exact Hamiltonian tailored to the MPS replace the one under
investigation. Standard parent-Hamiltonian theorems concern that newly
constructed operator, under their injectivity and interaction-range premises;
they do not identify it with our fixed nearest-neighbor Hamiltonian.
[Parent-Hamiltonian reference, sections4.1-4.2](https://arxiv.org/html/quant-ph/0608197).

## 5. Next decisive work, with explicit stop conditions

1. Strengthen the lower bound through larger odd windows or verified overlap
   constraints. Do not spend further effort expecting precision alone in
   the unweighted five-site minimum to pass0.8125.
2. Optimize or enlarge the correlation family, retaining exact/rational
   witnesses. A local numerical optimizer is parameter discovery, not a
   proof of optimality even inside this family.
3. Test residuals and state observables, not energy alone. A short-range
   trial state and a restored average do not prove a unique, symmetric,
   gapped ground state of the original Hamiltonian.
4. Keep the independent TFPT source obligation explicit: derive adjacency,
   couplings and the time/update interpretation, rather than identifying
   an internally covariant conditional spin model with physical spacetime.

The gap between the two energy bounds, the exact original ground state,
its spectral gap and the physical-source implications remain unresolved.
No T1-T8, RH, factorization, P-versus-NP or Hylæan capability closure is claimed.

### A concrete overlap-consistency certificate to seek next

Rather than merely diagonalizing a larger matrix, one can keep a five-site
window and seek a Hermitian four-site operator Y and rational lambda with

    H5/4 + I4 tensor Y - Y tensor I4 >= lambda I.

Summing its translations around a periodic chain makes the Y terms telescope
to zero, while the H5/4 terms sum to H_N. Therefore this one local positive
certificate would prove e_ground>=lambda without changing the Hamiltonian.
It can be stronger than the uncorrected five-site minimum: the added terms
penalize locally favorable choices that cannot be consistently shared by
neighboring windows. This is the dual form of requiring their four-site
overlap marginals to agree. No improving Y has yet been certified here;
Y=0 reproduces the present bound. The displayed cancellation is exact,
while finding a stronger positive witness is the next concrete search.

## 6. Reproduction and provenance

Run `python3 -B run_checks.py`. All four lanes execute normally and under
`-OO`, with byte-identical results and hash-stable local source. The nearby
false lower bound and inherited linear-filter regression are retained.
`verification.json` stores the actual replay output. The original generators
are pinned; numerical searches are not used as acceptance certificates.
An independent read-only reviewer checked the lower-bound logic and the
general five-value energy contractions.
