# Appending Bell pairs does not intertwine an active connected chain

12 September 2026. NON-RH finite/analytic audit. Companion: `append.py`.

## Main outcome

**Appending a normalized Bell pair gives an exact isometric embedding and
changes compressed energy only by a scalar. It nevertheless fails to
preserve the connected dynamics on EVERY nonzero old state.** Subtracting
the scalar energy does not remove the orthogonal transition out of the
appended subspace. Repeating the operation increases its squared leakage
linearly with the number of new active bridges.

There is a constructive positive refinement: for the FIRST extension from
one to three factors, switching on the bridge has an explicitly gapped
ground-state path that deforms the bare append into the previous ternary
ground encoding. This changes the embedding. It is not proof of a uniform
gap or a usable growth protocol for arbitrary chain length.

## 1. Exact scope and notation

Let d>=2 and

    H_n=sum_(j=1)^(n-1) (I-P_(j,j+1)),
    W_n psi=psi tensor Phi,
    Phi=(1/sqrt(d)) sum_a |a,a>.

P is the normalized rank-one Bell projector. For the alternating active
symmetry U,bar(U),U,... choose odd n, so the appended factors transform
as bar(U),U. The following algebraic contraction identities hold for any
n; oddness fixes the stated duality pattern.

Physical factorization, the open graph, full active unitary symmetry,
Hamiltonian interpretation, pair preparation and clock remain conditional.
The source `interaction/composition.py` is pinned at SHA-256
`c28ddc0b2a21a3d796d4770d0ad015858b4348967a4b1692989a9bedb8f42192`;
its original Clifford-source hash is independently checked. No original
source, previous experiment, paper or physical gate is modified.

## 2. The bridge is the entire intertwining defect

Write B=I-P_(n,n+1), where the bridge connects the old endpoint to the
first newly appended factor. The new pair term annihilates Phi, and the
old Hamiltonian acts only on old factors. Therefore

    D:=H_(n+2) W_n-W_n H_n = B W_n.

The one-half Bell marginal is I/d. Consequently

    W_n* P_(n,n+1) W_n = I/d^2,
    W_n* B W_n = c I,          c=1-1/d^2.

This proves

    W_n* H_(n+2) W_n = H_n+cI.

However B is itself a projector, so

    D*D=W_n* B^2 W_n=cI.

The exact intertwining error is not scalar motion within the range of W_n.
Its optimal scalar subtraction is

    L=D-c W_n,
    W_n* L=0,
    L*L=c(1-c)I=(d^2-1)I/d^4.

It is strictly positive for every d>1, independently of n. At d=4:

    compressed energy shift=15/16,
    squared orthogonal leakage=15/256,
    leakage operator norm=sqrt(15)/16.

For any other scalar t,

    (D-tW_n)*(D-tW_n)=[c(1-c)+(t-c)^2]I

when t is real. Thus c is the best energy-origin correction, but none
restores exact dynamics. Because the Gram is a positive scalar identity,
no special old state, subcode, or entanglement with an external reference
can make this bare-append defect disappear.

The second moment makes the difference operational:

    W_n* H_(n+2)^2 W_n=(H_n+cI)^2+c(1-c)I.

For any normalized old state, the connected energy variance increases by
c(1-c). Equal compressed generators up to a scalar do not imply equal
spectral measures or time evolution when the subspace is not invariant.

## 3. Repeated bare append with all new bridges active

Append k independent Bell pairs:

    W_(n,k) psi=psi tensor Phi^tensor k.

The k bridge projectors lie on the edges between the old chain and the
first pair and between successive pairs. For any subset S of these
bridges, their joint compression is exactly

    W_(n,k)* product_(j in S) P_bridge,j W_(n,k)
        = d^(-2|S|) I.

Proof: peel the rightmost selected bridge. Its right new Bell pair has
no selected bridge farther right; contracting that pair replaces the
projector with I/d^2 on the remaining left factor. Repeat. Unselected
Bell pairs contribute normalized identities. This proof applies to all
k and to arbitrary states of the old chain.

Writing B_total=sum_j (I-P_bridge,j), it follows that

    W*B_total W=kcI,
    W*B_total^2 W=[(kc)^2+k c(1-c)]I.

The same original/new-pair cancellation as above yields

    H_(n+2k) W-W H_n = B_total W,
    W*H_(n+2k)W=H_n+kcI,
    L_k*L_k=k c(1-c)I=k(d^2-1)I/d^4,
    L_k=(I-WW*)B_total W.

Thus squared leakage accumulates linearly, and its norm grows as sqrt(k).
For d=4, two appended pairs give squared leakage 15/128.
The independent Bernoulli contraction describes the bridge projectors in
this product-append preparation. It does NOT make the FULL connected
Hamiltonian a commuting Bernoulli model: the internal pair terms do not
commute with bridge terms after evolution begins.

## 4. Inactive bridges give an exact but disconnected construction

If all new bridge couplings are zero, the remaining Hamiltonian is

    H_disconnected=H_n+sum_(new pairs) (I-P_pair).

Then H_disconnected W=W H_n exactly, with no offset or leakage. Repeated
append consequently works as a compatible product extension of an old
chain plus isolated Bell dimers. It does not build the connected chain
H_(n+2k). Calling this a connected inductive dynamics would omit the very
terms responsible for interaction between the old and new pieces.

For a single bridge multiplied by lambda, the scalar shift is lambda c
and the squared bare leakage is lambda^2 c(1-c). Making lambda small
reduces the error; it does not make it zero at nonzero lambda.

## 5. Positive finite alternative: a gapped first-append dressing path

For n=1 the old Hamiltonian is zero. Let

    V psi=Phi_12 tensor psi_3,
    W psi=psi_1 tensor Phi_23,
    H(lambda)=lambda(I-P12)+(I-P23),      0<=lambda<=1.

The independent V,W coordinates have overlap V*W=I/d. On their 2d-
dimensional span the exact Hamiltonian matrix is

    [[1,-lambda/d],[-1/d,lambda]],

with eigenvalues

    E_minus/plus(lambda)=(1+lambda -/+ Delta(lambda))/2,
    Delta(lambda)=sqrt((1-lambda)^2+4lambda/d^2),

each repeated d times. The remaining energy is 1+lambda with multiplicity
d^3-2d. For lambda>=0, 1+lambda>=Delta(lambda), so the actual spectral
gap above the d-dimensional ground band is Delta(lambda).

Completing a square gives

    Delta(lambda)^2
      =[lambda-(1-2/d^2)]^2+4(d^2-1)/d^4.

Therefore along the entire interval,

    min Delta=2sqrt(d^2-1)/d^2>0.

At d=4 this minimum is sqrt(15)/8. In particular, the first switching
path does not merely assume the gap required for dressing.

A normalized ground isometry is explicitly

    G_lambda=(r_lambda V+W)/sqrt(r_lambda^2+1+2r_lambda/d),
    r_lambda=lambda/[d(1-E_minus(lambda))].

It starts at G_0=W, the bare Bell append, and ends at
G_1=(V+W)/sqrt(2(1+1/d))=Z, the original ternary ground embedding.
The map is smooth on [0,1]. Exact finite checks use d=2,3,4 and
lambda=0,1/2,1; the full interval proof follows from the formulas.

This proves existence of a finite gapped ground-band deformation, not
instantaneous exact evolution of the bare appended state. An adiabatic
implementation additionally requires a chosen time schedule and quantified
transition error; a finite-time exact counterdiabatic implementation
would require additional controls. Neither protocol nor its physical
origin is derived here. For general old-chain n, no uniform many-chain
gap, compatible dressed embeddings or controlled infinite extension has
been proved by this first-append calculation.

## 6. Verification and status

The checker performs direct sparse Bell-projector action for d=2,3,4,
n=1 and3, and checks two appended pairs for n=1 at all three dimensions.
It verifies full logical matrix identities, not selected basis-state
expectations. It also checks the first-append switching eigenmaps and
the dimension-independent gap polynomial. No dense large Hamiltonian,
floating tolerance or optimization-removable assertion is used.

No claim is made that TFPT selects these factors, Bell preparation,
graph, switching schedule or physical dynamics. All T1-T8 remain open.

The negative result concerns exact intertwining by these particular BARE
Hilbert-state embeddings. It is not a prohibition on a connected-chain
quasilocal observable limit or a thermodynamic dynamics constructed by
other methods. A finite-volume boundary perturbation can recede from any
fixed local observable; convergence of that observable dynamics is a
different question with different bounds. Neither its impossibility nor
its full construction is inferred from the nonzero append leakage.

Executed receipt: normal and `-OO` each pass **124 exact checks**, and
subprocess comparison confirms byte-identical JSON. Directory diff check
passes. Only `append.py` and this note were created; no earlier experiment,
source, paper, website or ledger was edited. An initial unmatched closing
parenthesis in the new endpoint check was corrected before execution;
the mathematical check and expected endpoint were unchanged.
