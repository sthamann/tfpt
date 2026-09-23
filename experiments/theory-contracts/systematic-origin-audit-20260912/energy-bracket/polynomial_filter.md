# Improved exact variational upper bound with the same bond dimension

A quadratic positive filter lowers the certified uniform-chain energy
density upper bound from 5023/5476 to **53950/59177**, approximately
**0.9116717644**. The matrix-product bond dimension remains four. The
Hamiltonian is unchanged; only the trial state's local correlation
filter has been enlarged.

## 1. Source-based general quadratic family

Keep the actual primitive pair h=h4, with eigenvalue k of multiplicity
binomial(4,k), and use F=I-t h+u h^2 on the intervening bonds of the
Bell-dimer construction. Its five spectral values are

    f_k=1-t k+u k^2, k=0,...,4.

For S_i=a_i tensor conjugate(a_i), source algebra gives

    F=c0 I+c1 sum_i S_i+c2 sum_(i<j)S_i S_j,
    c0=1-2t+5u, c1=t/2-2u, c2=u/2.

The two-register-cell tensors remain A^{st}_{ab}=F_{st,ab}/2. Define

    p=(1/16)sum_k binomial(4,k) f_k^2
     =c0^2+4c1^2+6c2^2,
    w=(1/16)sum_k binomial(4,k) k f_k^2,
    b=c0^2-2c1^2.

Both transfer fixed matrices are I with eigenvalue p. Independent
physical left/right insertions give the boundary numerator b for each
primitive direction. The bivector contribution to that numerator
cancels, rather than being silently omitted: conjugating a fixed
primitive generator by the six bivectors gives three plus and three
minus signs.

Whenever the normalized transfer is primitive, the exact thermodynamic
bond and energy-density contractions are therefore

    e_inside=w/p,
    e_between=2-2(b/p)^2,
    e(t,u)=w/(2p)+1-(b/p)^2.

Setting u=0 reproduces the whole previous linear-filter energy formula,
not just its value at one selected point.

## 2. Transfer spectrum and justified normalization

The complete Clifford-word transfer basis remains diagonal. A word of
degree r has unnormalized eigenvalue

    d_r=(1/16)sum_(k=0)^4 f_k^2
        sum_(j=0)^r (-1)^j binomial(r,j) binomial(4-r,k-j).

As usual, out-of-range binomial coefficients vanish. The five degree
multiplicities are 1,4,6,4,1. This is the exact Fourier decomposition of
F^2 on the four commuting source constraints; all sixteen physical
transfer eigenvector identities are independently checked.

No generic primitivity region for every pair t,u is claimed here. The
explicit parameter choice below has a positive invertible filter and
strict transfer positivity, sufficient for all reported energy values.

## 3. Simple rational certified improvement

A small numerical two-parameter search found a local value near
t=0.2429807,u=0.0304552, with energy about 0.9116715879. This was only
parameter discovery, not an acceptance proof or a global optimum claim.
The exact rational choice

    t=8/33, u=1/33,
    F=((h-4I)^2+17I)/33

is nearly as good and has a particularly simple positive-square form.
Its eigenvalues, in k order, are

    1,26/33,7/11,6/11,17/33.

All are strictly positive. Thus the sixteen Kraus matrices span all M4
and the transfer sends each nonzero positive matrix to a positive
definite matrix in one step. Its normalization and rates are

    p=1003/2178,
    (d0,d1,d2,d3,d4)/p=(1,188/1003,62/1003,12/1003,3/1003).

This proves a well-defined finite-correlation thermodynamic trial state.
The exact boundary transmission is b/p=56/59. Consequently

    e_inside=1630/1003,
    e_between=690/3481,
    e=53950/59177 < 5023/5476,
    previous_bound-e=1815871/324053252 > 0.

The between-cell cost is included. It would be incorrect to use only
the improved energy of a filtered pair and ignore its changed Bell
links to neighboring cells.

## 4. Finite periodic chains versus the thermodynamic bound

For L cells the exact periodic norm is

    Tr(E^L)=sum_(r=0)^4 binomial(4,r)d_r^L.

Finite periodic observable contractions retain subleading transfer
terms. The quoted energy is their thermodynamic fixed-point limit, not
an asserted exact energy for every finite ring. Strict spectral
dominance makes that limiting contraction rigorous. By the variational
principle it bounds the original uniform Hamiltonian's thermodynamic
ground energy density from above.

## 5. Scope

This is an improvement of a controlled trial state with unchanged local
source and unchanged bond dimension, not the exact ground state and
not a lower bound. The numerical search does not establish that this
is optimal even in the quadratic-filter family. Finite correlation
length of a trial state does not prove a Hamiltonian spectral gap.
The physical graph and parent selection, all-scale closure and T1-T8
remain outside this calculation.

## 6. Executed verification

The checker passed 56 exact checks under normal Python and Python -OO
with byte-identical JSON output. The checks include original/dependency
pins, the entire earlier linear family as a regression, all sixteen
transfer directions, independent physical boundary insertions, the
positive rational filter spectrum and Kraus span, both bond costs and
the strict rational improvement. Numerical optimization is not part
of these acceptance checks.
