# The shared T6/T8 residual parity and an existing candidate order parameter

2026-09-07. NON-RH, unpromoted research. This is a selection-rule theorem
for the **actual** projective family lift already present in v1024/v1028,
not a derived neutrino mass matrix. No observed mass or mixing target is
loaded. The theorem identifies a concrete missing symmetry-breaking
ingredient and its compatibility condition with state selection.

## 1. Use the fermion lift, not its even-pair quotient

There are six existing gauge-singlet nu^c modes, two spin components in
each family r=1,2,3. In the occupation basis the inherited family operator is

    C_f=exp[-i pi (N_1+2N_2+3N_3)/4].

Its fourth power is

    K=C_f^4=(-1)^(N_1+N_3), K^2=1.                    (1)

This is **not** total fermion parity: a single family-two fermion is K
even and fermion odd. The ordinary four-state seam rotation C_s obeys
C_s^4=1, so (C_s tensor C_f)^4=I tensor K.

On the three one-fermion family labels, K is P=diag(-1,+1,-1). Its
complete six-mode Fock space has 32 K-even and 32 K-odd basis vectors.
All powers/products and arbitrary operators of the ordinary seam factor
commute with I tensor K. Enlarging a polynomial in ordinary seam
operators therefore cannot supply a K-odd coefficient. This conclusion
does not assume that the state preserves the full seam rotation.

## 2. Exact rotation selection, including what it does not establish

Put zeta=exp(i pi/4). A family-r **creation** operator transforms under
C_f with phase zeta^(-r). A seam coefficient of grade k has phase
zeta^(2k). A Majorana pair-creation term with a seam coefficient can be
rotation invariant only if

    2k-i-j=0 mod8.                                    (2)

The six unordered family pairs consequently give

| Pair | Required ordinary seam grade k |
|---|---|
| (1,1) | 1 |
| (1,2) | none |
| (1,3) | 2 |
| (2,2) | 2 |
| (2,3) | none |
| (3,3) | 3 |

This is the **rotation** test only. The full projective reflection,
spin structure, dynamical coefficients and expectation values must also
be satisfied; the four permitted cells are not claimed to have acquired
nonzero masses. With a scalar constant and unbroken C_f, v1028's stronger
zero-matrix conclusion still holds.

The new all-coefficient consequence is that any K-preserving effective
Majorana mass has

    P M P=M,
    M=[ m11  0   m13;
         0  m22   0 ;
        m13  0   m33 ].                                (3)

For a K-invariant state and K-invariant Hamiltonian, an off-block
anomalous two-point function vanishes at all times: insert K^2 in the
trace, commute K through the state and evolution, and obtain minus
the same correlator. The same change of variables in any finite
invariant integral gives the rule for its exact effective action.
Equivalently a Feshbach/Schur reduction through K-invariant projections
commutes with K wherever its resolvent exists. It cannot fill the two
forbidden entries. This covers arbitrary ordinary-seam insertions and
K-preserving interactions, not merely a few trial mass matrices.

The claim is about this nu^c Majorana block. It does not by itself rule
out physical PMNS mixing: that additionally requires the charged-lepton
and Dirac Yukawa sectors and their transformations to be specified. If
those sectors share the same unbroken family parity, their corresponding
off-block mixings inherit the same obstruction. Changing their family
action is additional model input, not covered by (3).

## 3. A minimal K-odd boson already exists in the given Fock space

One need not introduce a new elementary scalar just to obtain the right
quantum numbers. The existing cross-family spin-singlet pair

    B12=nu_(1,up) nu_(2,down)-nu_(1,down) nu_(2,up)

is gauge neutral (both nu^c fields are gauge singlets), fermion even,
and satisfies K B12 K=-B12. B23 is the other adjacent-family example.
Under C_f, the annihilation pair B12 carries zeta^3, while B23 carries
zeta^5. These are precisely odd Z8 charges unavailable in the ordinary
Z4 seam factor. Reflection exchanges their families with the inherited
fermionic signs; a complete candidate interaction must keep that full
orbit rather than choose one component by fiat.

The checker constructs B12 from all six exact CAR matrices. Acting on
the vacuum, its adjoint has squared norm two, and its coherent vacuum/
pair order parameter is explicitly K odd. This is an available composite
operator, **not** evidence that it condenses or has the required mass scale.

For example, B12^* B12 is invariant under the rotation and K, but a
coefficient multiplying it is still a coupling to be derived. Even an
attractive invariant four-fermion interaction does not by itself prove
condensation, full flavor mixing, a positive continuum measure, or the
needed neutrino hierarchy. No such coefficient is fitted here.

## 4. The T8 compatibility condition is unavoidable

Let a finite-volume H commute with K and have a unique ground ray Omega.
Then K Omega is a ground vector, so uniqueness makes it a scalar multiple
of Omega. Since K^2=1 the scalar is +1 or -1. Every K-odd B therefore has

    <Omega,B Omega>=-<Omega,B Omega>=0.                 (4)

The conclusion also holds for any invariant density matrix, including
the finite-volume Gibbs state at every beta. It does not depend on a
gap estimate, on a chosen entropy functional, or on ordinary D4 versus
its projective lift. In particular a unique symmetric internal cap
cannot also supply a nonzero B12 order parameter.

This does **not** forbid spontaneous symmetry breaking in infinite
volume. The constructive candidate route is now precise:

1. Derive a K-invariant interaction involving the existing K-odd pair
   orbit from the same microscopic parent, with no tuned mass target.
2. Establish an infinite-volume ordered phase or an explicitly derived
   boundary/state prescription. A finite symmetric vacuum is insufficient.
3. Derive which branch the state preparation selects, rather than
   replacing it by a fitted K-odd source.
4. Compute the complete Majorana, Dirac and charged-lepton readouts from
   that same state and action, with scale and error bounds.

If an infinitesimal source is used to define a branch, the order of
limits matters: first volume to infinity at nonzero source, then source
to zero. Existence, nonzero limiting order and source-independent physical
selection have **not** been proved here. A K-breaking Euclidean cap would
also be extra data unless independently derived.

Thus T6 and T8 cannot be solved independently by combining a symmetry-
preserving finite state selector with an assumed odd condensate. The
specific missing ingredient is a controlled physical K-breaking state
or mechanism, not a longer scan over ordinary seam polynomials. The
new composite gives a concrete operator to test, but none of the
numerical neutrino texture, cosmological state or full T6/T8 gates closes.
