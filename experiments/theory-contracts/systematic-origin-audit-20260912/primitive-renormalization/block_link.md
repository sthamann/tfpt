# Primitive compiler block link: exact self-reproduction and its limit

This is a finite NON-RH result conditional on the equal-weight primitive
synchronization parent and the chosen open three-factor blocking. The four
original source matrices, not arbitrary full-U4 replacements, are used.
Source and previous exact checker are SHA256-pinned in `block_link.py`;
the original source's eight dependency pins are also verified.

## 1. Objects and first-order closure

Write S_i=g_i tensor conjugate(g_i), S=sum_i S_i, and

    h=H_sync=2I-S/2.

The S_i are commuting Hermitian involutions. On each three-factor block
let G be the exact four-dimensional ground isometry constructed in
`source-selection/primitive_chain.py`, with energy E0=4-sqrt(6).
Two adjacent blocks alternate representations: their encoding is
W=G tensor conjugate(G). The physical link couples the last factor of
the first block to the first factor of the second block. These factors
are distinct physical registers; there is no identification of independent
virtual legs or inference of physical space/time from tensor notation.

The checked boundary channel B obeys

    B(g_i)=a g_i, a=sqrt(6)/4,
    B(g_i g_j)=b g_i g_j, b=7/12 (i != j).

Since W is a product-block isometry, compression of the boundary link
factors into the two boundary channels. Therefore

    Q=W* h_link W=2I-(a^2/2)S
     =(3/8)h+(5/4)I.

This is a positive self-reproduction result: to first order in a weak
inter-block coupling, the same primitive compiler interaction reappears,
with coefficient 3/8 and an additive constant. No isotropic full-U4
depolarizing assumption is needed. It is not the old flat Bell coefficient
9/25, and it does not assert closure at higher perturbative orders.

## 2. Exact leakage, without a dense six-factor matrix

Let K=sum_(i<j) S_i S_j. The involutions commute, so

    h^2=5I-2S+K/2,
    W* h_link^2 W=5I-2a^2 S+(b^2/2)K.

In contrast, squaring the compression gives

    Q^2=(4+a^4)I-2a^2 S+(a^4/2)K.

With L=(I-WW*)h_link W, the exact leakage Gram is therefore

    L*L=W* h_link^2 W-Q^2
       =(1-a^4)I+(b^2-a^4)K/2
       =(55/64)I+(115/1152)K
       =(35/24)I-(115/144)h+(115/576)h^2.

The calculation uses independently recomputed 64-by-4 boundary
contractions for all four generators and six bivectors. It does not
confuse compression of a product with the product of compressions.

If k of the four primitive constraints are violated, S=4-2k and
K=((4-2k)^2-4)/2. This proves the full leakage spectrum:

| Logical syndrome k | Multiplicity | Eigenvalue of L*L |
| --- | --- | --- |
| 0 or 4 | 2 total | 35/24 |
| 1 or 3 | 8 total | 55/64 |
| 2 | 6 | 95/144 |

Thus L*L >= (95/144)I is strictly positive on every logical state,
including the logical Bell state. No logical subspace has zero leakage.
Subtracting a scalar zero-point energy does not alter L. The checker
also rejects the tempting false replacement b^2=a^4, which would miss
the nonconstant leakage term.

## 3. What follows for dynamics

For the two-block Hamiltonian H0+epsilon h_link, with H0 the sum of the
two internal three-factor parents, H0 W=2E0 W exactly. Consequently

    W*(H0+epsilon h_link)W=2E0 I+epsilon Q,
    (I-WW*)(H0+epsilon h_link)W=epsilon L.

For every nonzero epsilon the bare product-block embedding is not an
invariant dynamical subspace. The failure cannot be fixed by choosing a
special logical input or by removing the additive constant. At short
physical evolution parameter t, leakage probability has leading term
epsilon^2 t^2 times the expectation of L*L (units hbar=1).

Nevertheless the decoupled blocks have a finite gap sqrt(6)-2 and the
link is bounded (norm 4). The compressed Q is the first-order operator
in ordinary finite-dimensional degenerate perturbation theory near
epsilon=0. Exact or perturbative *dressed* low-energy subspaces are NOT
excluded by the bare leakage. Second-order terms require the excited
block resolvent, not merely the positive leakage Gram computed here.
No infinite-chain uniform gap, exact renormalization fixed point, physical
time assignment or T1-T8 closure is claimed.

## 4. Research meaning

The primitive parent retains something simpler and more constructive
than mere symmetry resemblance: its own interaction reproduces at first
order under its own exact ground encoding. At the same time, the
strictly positive and nonconstant leakage identifies the exact point
where a claimed all-time recursion would exceed the calculation.
The discriminating next operation is the excited-block-resolvent weighted
second-order correction, to determine whether it only renormalizes h
or generates independent logical operators. This remains a finite model
test, not a selection of the physical parent from TFPT's origin alone.

## 5. Executed verification

The checker passed 37 exact acceptance checks under normal Python and
Python -OO with byte-identical JSON output. The scoped diff whitespace
check passed. No numerical eigensolver, tolerance, dense 4096-dimensional
operator or promotion of a physical acceptance gate was used.
