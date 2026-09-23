# The filtered dimer state: internal symmetry without restored clustering

NON-RH. This audits the pinned `uniform-chain/dimer_filter.py` state at t=1/8,
not a newly selected physical model. The companion `state_symmetry.py` verifies
the original matrices, covariance generators, local contractions and finite
translation controls. T1–T8 remain open.

## 1. Exact internal symmetry

The ansatz starts from a product of Bell pairs and applies F=I−h4/8 on the
alternating intervening bonds. Write ai=i gi for the actual original Hermitian
Clifford generators and

    h4=2I−(1/2)Σ_i ai⊗bar(ai).

Each Bell vector is fixed by U⊗bar(U). The filter commutes with that action
for each actual source gi and for the family lift w. Consequently the whole
normalized finite-chain state, and its thermodynamic limit, preserve these
global primitive/family symmetries.

There is also continuous **internal Spin(4)** symmetry. For every i<j, put
kij=ai aj. The six kij are anti-Hermitian bivector generators, and exact
matrix calculation gives

    [h4,kij⊗I+I⊗bar(kij)]=0.

Exponentiating gives the continuous symmetry of the filter and therefore of
the filtered Bell state. This is compact internal frame symmetry, not a proof
of physical Lorentz covariance, a selected spacetime, or time evolution.

It is not full U4 invariance: the infinitesimal direction k=i a1 has a nonzero
commutator with F and with the actual cell density matrix below. The distinction
is checked, rather than inferred only from terminology.

## 2. The state is spatially dimerized

Use each filtered bond as a two-register cell. The chosen branch is invariant
under a two-site shift. The one-site shift exchanges this branch with another
branch of the same uniform-Hamiltonian variational energy.

At t=1/8, the exact thermodynamic bond energies are

    e_inside=62/37,
    e_between=435/2738,
    Delta=e_inside−e_between=4153/2738 > 0.

This nonzero local bond contrast proves that the branch is not invariant under
a one-site shift. A separate exact four-site periodic control verifies two-site
invariance and linear independence of the one-site-translated branch; its
finite-size energies are not substituted for these thermodynamic values.

There is **no alternating single-register population**. Both single-register
reduced densities are exactly I4/4, obtained by tracing

    rho_cell=F²/(16p),       p=37/64.

The order parameter is a two-register bond observable, not an onsite density.
This distinction is important when saying that an averaged state “looks
uniform”: its individual registers already look uniform before averaging.

Typing qualification: the one-site shift T is the cyclic permutation in the
fixed common computational chart; it exchanges fundamental and conjugate site
types. T² preserves the types. The actual h4 is real and has the same matrix
on either alternating edge. Thus T is a symmetry of the declared uniform-chain
matrix, but promoting it to a source-geometric symmetry still requires the
type identification. Nothing in this state calculation derives spatial sites
from the internal family cycle.

## 3. Equal mixture: uniform local energies, long-range dimer information

Let omega_A be the chosen infinite branch and omega_B its one-site translate.
Both are clustering in two-site cells, because their normalized transfer
eigenvalues are1,6/37,1/74,0, with a unique leading eigenvalue. Define

    omega_mix=(omega_A+omega_B)/2.

This is one-site translation invariant. Every bond now has expectation

    ebar=(e_inside+e_between)/2=5023/5476.

The averaging does not improve the variational energy density. More importantly,
it does not remove the branch label from correlations. For widely separated
bonds of the same parity, clustering inside each branch gives

    lim Cov_mix(h_i,h_j)
      =(e_inside²+e_between²)/2−ebar²
      =Delta²/4
      =17247409/29986576 > 0.

For opposite parity the limit is the negative of this number. Equivalently,
the staggered bond observable has positive long-range order. Thus the mixture
restores the alternating local expectation while retaining nondecaying
correlations. It is not a single clustering branch.

A mixture of two distinct states cannot establish a unique pure ground state.
If a finite positive Hamiltonian has such a mixture supported in its ground
space, positivity implies that both components belong to that space. This
observation does not determine the gap above a degenerate ground space.

## 4. A coherent cat does not automatically solve the issue

For an even periodic chain, let psi_B=T psi_A with T² psi_A=psi_A. The normalized
plus-cat proportional to psi_A+psi_B is exactly T-invariant whenever nonzero.
The checker verifies this independently for four physical sites. At finite
size its local values include cross-branch interference and are not exactly
those of the classical mixture.

In the thermodynamic limit, the two clustering branches are macroscopically
distinguishable by averaging one fixed bond parity: their means differ by
Delta, while each branch's variance of that average tends to zero. This also
shows why the cat's fixed-support interference vanishes. Choose an averaged
bond operator A_N far from the support of a bounded local O. Then [A_N,O]=0,
and, writing m_A and m_B for its branch means,

    |m_A−m_B| |<psi_A|O|psi_B>|
      <= ||O|| (sqrt(Var_A A_N)+sqrt(Var_B A_N)) -> 0.

The same estimate with O=I makes the branch overlap vanish. Summable cell
correlations supplied by the transfer spectrum give the required vanishing
variances. Consequently the plus-cat has the same local thermodynamic limit
as omega_mix, including its nonzero staggered covariance plateau. This is
not a claim that the finite cat and finite mixture are identical, nor a claim
that arbitrary global/nonlocal observables fail to distinguish them.

## 5. What an MPS parent can and cannot establish

At the selected t, F is invertible and the16 cell matrices span M4. The branch
is therefore injective in **two-site cells**. Standard injective-MPS parent
construction yields a different finite-range Hamiltonian for which this branch
is an exact ground state; with the stated injectivity/range hypotheses it gives
uniqueness on periodic cell chains and a uniform gap. A canonical multi-branch
parent instead retains the distinct sector ground states rather than selecting
a unique cat. These are parent-Hamiltonian results, not results about a
Hamiltonian chosen in advance. See Pérez-García et al., sections4.1–4.2 of
[Matrix Product State Representations](https://arxiv.org/html/quant-ph/0608197).

In particular, none of that establishes that the supplied uniform nearest-
neighbor primitive H4 chain has this exact ground state, is gapped, or has a
unique one-site-symmetric ground state. A parent tailored to the two-site
branch also retains the chosen cell structure. Symmetrizing its state or
enlarging its local kernel to include both branches does not silently preserve
uniqueness. An explicit operator comparison to the original chain, together
with a quantitative spectral/state bound, would be required for transfer of
such conclusions. The transfer decay rate is not itself that comparison.

## Verification and scope

The checker pins the original bridge and dimer-filter implementation, recomputes
both bond energies through the local cell and independent intercell insertions,
checks the complete word transfer spectrum, all six Spin4 generators, actual
primitive/family operations, maximal mixing of individual registers, a non-U4
negative control, the exact covariance plateau and finite translation/cat
controls. It makes no many-body ground-state or gap assertion. Run normally
and with `python -OO`; all guards are explicit, not `assert` statements.

Original bridge SHA256:
`bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d`.

Pinned dimer-filter SHA256:
`53792526398ae08559169493b48a833a05623aa8efc6b3d7747b7a6c7f10aa80`.
