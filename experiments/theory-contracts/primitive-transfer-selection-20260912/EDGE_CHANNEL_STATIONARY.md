# Transport does not select the state: exact fixed-algebra countercheck

12 September 2026. Continuation of COVARIANT_EDGE_CHANNEL.md.

Use its six neutral edge generators K_k on eight complex modes and the
unchanged source h. At pulse angle pi/2, U_k=I-K_k^2-iK_k, and
Phi(X)=sum_k U_k X U_k*/6. One possible continuous event model would be

    L(X)=-i[h,X]+r(Phi(X)-X), r>0.

This is an explicitly added Poisson-event model, not a TFPT derivation.
It is a valid finite quantum Markov generator: event-only evolution is
exp(-rt) sum_n (rt)^n Phi^n/n!, and including h follows by the finite
Trotter product. No fundamental event rate is selected.

For any matrix X the real Hilbert--Schmidt quadratic form of the event
part is -sum_k ||[U_k,X]||_HS^2/12. The Hamiltonian commutator contributes
zero to its real part. Thus stationarity for L implies commutation with
every U_k and then with h. Conversely these commutations imply stationarity.
The three distinct eigenvalues of U_k corresponding to K_k=0,+1,-1
mean that commuting with U_k is equivalent to commuting with K_k.

Exact commutant equations give complex dimensions 10 for the edges alone
and 5 for the edges together with h. The latter algebra is

    C I_6 direct_sum M_2(C).

The two-dimensional subspace of boundary modes 5,6,7 whose coefficients
sum to zero is untouched by all edges and has h=I. Let R be its rank-two
orthogonal projector. Then R/2 and (I-R)/6 are two distinct, positive,
normalized stationary states with orthogonal supports. Operators on R
give four fixed directions; the complement identity gives the fifth.
The exact dimension calculation excludes further fixed directions.

Therefore the channel can transmit the previously exhibited population
signal while failing to select a unique one-particle state. On full Fock
space number conservation adds further selection obstructions. The
vacuum is still not excited by these neutral operations.

Finally the 64-dimensional superoperator Phi is NOT selfadjoint in the
Hilbert--Schmidt inner product. It cannot simply be substituted for a
strictly positive selfadjoint state-space transfer T in
H=-log(T/lambda_0)/tau. A completely positive channel and a positive
Hilbert-space operator are different types of objects; a positive Choi
matrix does not remove that distinction. This does not exclude a different
source-derived positive transfer or a different detailed-balance metric.

Verification: edge_channel_stationary.py, 15 exact checks normal and -OO.
Includes source pin, three commutant ranks, explicit stationary witnesses
and failure of Hilbert--Schmidt selfadjointness. No source modification or
T1-T8 promotion.
