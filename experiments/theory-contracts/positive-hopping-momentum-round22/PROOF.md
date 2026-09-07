# Round22: incompatible exact resonances at strictly positive hopping

2026-09-07. NON-RH. Fix L=3, a=1, N=27, m>0, nu=0, total charge p=e2,
and ANY J in 0<J<=1/1119744. Use the original, unaveraged scalar coupling

    H(lambda,J)=H_m+H_c(J)+lambda V_1,
    V_1=(1/N)sum_x e(n_x)phi_x^2.

The exact moving-charge states chi_k(J), cubic energy equalities and
nonzero form factors are those of the [band proof](../positive-hopping-band-round22/PROOF.md).
J is fixed and positive throughout this argument; no differentiability
or prescribed limit of the momentum as J->0 is assumed.

## 1. The precise class tested

Suppose P(lambda)=P_0+lambda P_1+o(lambda) conserves H in differentiable
commutator matrix elements on a common domain containing the states below.
The seed is P_0=P_m,1+P_c, where P_m is the ACTUAL centered scalar momentum,
and P_c is self-adjoint, acts only on charges and strongly commutes with
H_c and all three charge translations. P_1 may be arbitrary and mixed.

Translation covariance of P_c is an explicit additional assumption. The
isolated charge band contains one eigenvector per character, so P_c acts
there as P_c chi_k=w(k)chi_k with real w(k). Spectral isolation prevents
mixing with higher states of the same energy; one-dimensional character
spaces prevent mixing within the band. An unbounded P_c has a bounded
restriction to this finite band if it strongly commutes as stipulated.

First-order conservation requires [H_0,P_1]=-[V_1,P_0]. Between equal-
energy H_0 eigenstates the left side is zero for EVERY admitted P_1.
Thus any nonzero resonant V_1 matrix element requires equal seed momenta.

## 2. Two processes on the SAME charge transition

Use signed momentum labels in {-1,0,1}^3 and write scalar one-quantum
states as |q>. Their exact free frequencies and scalar momentum weights are

    omega_q=sqrt(m^2+3 number_of_nonzero_components(q)),
    f(q)=sin(2pi q_1/3).

The conventions agree with Round21's real-mode oscillator computation.
Let k=(0,-1,0), l=(1,0,0), h=l-k=(1,1,0). A proper quarter-turn maps k
to l, so E_k(J)=E_l(J) exactly. Consider:

| channel | incoming scalar q | outgoing scalar r | omega | f(q)-f(r) |
| --- | --- | --- | --- | --- |
| A | (1,0,0) | (0,-1,0) | sqrt(m^2+3) | sqrt(3)/2 |
| B | (-1,-1,0) | (1,1,0) | sqrt(m^2+6) | -sqrt(3) |

In BOTH channels, q-r=h modulo 3 and omega_q=omega_r. Therefore
|chi_k,q> and |chi_l,r> are genuine equal-energy states of the full
unperturbed charge-plus-scalar H_0 at this positive J.

The exact oscillator identity, with no truncated canonical algebra, is

    <r|phi_x^2|q>=exp(2pi i(q-r).x/3)/(N omega_q), q!=r.

Consequently both exact coupling matrix elements are

    M_A=F_lk(J)/(N^2 sqrt(m^2+3)),
    M_B=F_lk(J)/(N^2 sqrt(m^2+6)),
    F_lk=<chi_l|F_h|chi_k>, |F_lk|>=29/40.             (1)

They cannot vanish by virtual charge dressing or cocycle interference in
the certified interval. The two necessary seed conditions would be

    w(l)-w(k)=sqrt(3)/2,
    w(l)-w(k)=-sqrt(3).                                (2)

No real weights satisfy both. Their mismatch is 3sqrt(3)/2. At least one
seed mismatch has magnitude >=3sqrt(3)/4, independently of P_c. Thus at
least one resonant commutator matrix element has magnitude at least

    87sqrt(3)/(160 N^2 sqrt(m^2+6)) > 0.               (3)

This is a strictly positive-J obstruction to an arbitrary regular mixed
first correction, not merely a charge-only no-go, a J=0 argument, or a
numerical degeneracy inferred from a truncated matrix.

## 3. A broader cubic-vector seed is also tested

Changing sin to an arbitrary real cubic-vector weight in a number-
preserving scalar quadratic seed does not repair this L=3 example.
On this lattice proper-cubic covariance forces its one-quantum vector
weight to be f(q)=alpha_s q on shell s=1,2,3, and f(0)=0: each reference
vector has a stabilizer fixing only its own line. This is a statement
about that class of seeds, not every nonlinear free conserved operator.

For the charge transition k=(-1,0,0)->l=(1,0,0), use scalar transitions
q=(1,b,c)->r=(-1,b,c) with (b,c)=(0,0),(1,0),(1,1).
All have the required common transfer modulo 3 and equal scalar energies;
the same band/form-factor bound applies. They require the SAME charge
weight difference to equal 2alpha_1, 2alpha_2, 2alpha_3. Hence all three
alpha values agree. Channels A,B above simultaneously require
alpha_1=-2alpha_2. Therefore all three vanish. Nonzero standard spectral
or centered cubic-vector scalar weights are both excluded if the original
interaction is retained and the regular additive seed assumptions hold.

## 4. What survives and what can actually change

The original discrete simultaneous translations, hence crystal momentum,
remain exact symmetries. Channel B conserves wave vector MODULO the
reciprocal lattice but changes an unwrapped additive momentum. An exact
logarithm of the JOINT translation is not the additive seed assumed here.
Neither theorem excludes a fundamentally mixed zeroth-order generator,
nonregular dependence on lambda, a different coupling, larger J/nu, a
different total-charge sector or a continuum limit. L=3 scalar modes in
these channels are regulator-scale modes; this is not a no-go for emergent
low-energy Lorentz symmetry at a controlled continuum limit.

The companion [translation completion](../translation-completion-round22/PROOF.md)
constructs an explicit positive CHANGE to the common parent that retains
nontrivial exchange while conserving another continuous global momentum.
It removes the incompatible reciprocal-lattice vertices at the price of
spatial nonlocality and changed first interactions. That change is not
hidden inside a claimed solution of the original Hamiltonian.

The exact checker derives the actual scalar Fourier/oscillator factors,
checks the proper rotation, the two resonances, the inconsistent equations
and the more general cubic-weight test. The infinite-charge nonvanishing
input comes from the preceding resolvent proof. No TOE/T1–T8/RH promotion.
