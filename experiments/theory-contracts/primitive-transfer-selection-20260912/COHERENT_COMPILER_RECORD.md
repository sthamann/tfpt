# Two-sided compiler multiplication gives an exact conditional reconstruction code

2026-09-12. NON-RH. A finite constructive state/operator bridge; no physical
TOE, horizon, matter content or universal dynamics is derived.

## 1. Starting data and explicitly added physical interpretation

The original signed word algebra has sixteen words U_v (v in F2^4) and
U_v U_w=(-1)^c(v,w) U_(v+w). Its four generators g_i are skew-Hermitian,
square to -I and anticommute. `compiler-clifford-bridge/checker.py` already
contains the faithful real sixteen-dimensional left-regular matrices L_i.
The new checker reads those actual functions and the cocycle under the
previously established source pins, and checks eight upstream file hashes.
It does not infer a physical memory from the presence of these functions.

The CONSTRUCTION assumes a complex sixteen-dimensional quantum register R
with orthonormal word basis |v>, a four-dimensional system S carrying U_v,
and the tensor product R tensor S. Complexifying an algebraic label register
and declaring this physical tensor product are additional interpretations.
This is not the previously ruled-out whole-source unital M2 embedding into
the eight-mode seam, nor is it an identification with its physical boundary.

## 2. A closed model can be built, but it is not the Poisson model

Let X_i flip word bit i without a sign, and G_i=X_i tensor g_i. The controlled
decoder D=sum_v |v><v| tensor U_v† obeys the EXACT identity

    D G_i D† = L_i tensor I_S.

It moves every polynomial process in G_i into the record factor while the
decoded logical system is unaffected. This is a finite noiseless-subsystem
construction, a familiar operator-algebra mechanism rather than a new general
theorem; see [Knill–Laflamme–Viola](https://arxiv.org/abs/quant-ph/9908066).

For a stipulated coherent Hamiltonian H=i sum_i k_i G_i, H^2=Omega^2 I,
Omega^2=sum k_i^2. With initial record |0>, tracing R gives

    E_t(rho)=cos^2(Omega t) rho
       +sin^2(Omega t) sum_i (k_i^2/Omega^2) g_i rho g_i†.

The Omega=0 case is identity. This finite coherent model has quadratic
onset and recurrence, not exponential Markov relaxation. Its linear
Hamiltonian has only two energies ±Omega, each with multiplicity 32 on
the 64-dimensional joint space. It is not an interacting physical TOE.
The displayed channel formula follows from the two-term exponential and
orthogonal record labels, not an independently simulated time trace.

## 3. A different, compatible set of signed consistency constraints

Define instead S_i=L_i tensor g_i. These are Hermitian involutions. They
COMMUTE: the anticommutation sign in each factor cancels the other. Thus

    P_code=product_(i=1..4)(I+S_i)/2

is an orthogonal projector. It has rank four and equals W W† for the explicit
isometry

    W |psi>=(1/4)sum_v |v> tensor U_v |psi>.

All four S_i W=W. For arbitrary strictly positive weights w_i,
H_code=sum_i w_i(I-S_i)/2 is positive and has exactly this ground subspace.
Its ground STATE is not unique. At equal weights one, the full spectrum is
0,1,2,3,4 with multiplicities 4,16,24,16,4. The weights and ground-subspace
restriction are additional assumptions, not selected physical quantities.
The formula W is derived as the range of the specified projector; uniform
amplitudes are not simply asserted independently of the constraints.

The previous G_i and these S_i are DIFFERENT operations. In fact W†G_iW=0
for every i: the unsigned recorded primitive moves this code out of itself.
It would be false to identify the coherent model in section 2 with automatic
code-preserving logical dynamics in section 3. The checker explicitly guards
against this tempting conflation.

## 4. Full quantum state recovery from the coherent register alone

Discarding S leaves enough information to recover the complete logical state.
An explicit register-only unitary F has entries

    F_(a,b),v = conjugate((U_v)_(a,b))/2.

Hilbert–Schmidt orthogonality of the sixteen U_v proves F is unitary. Directly,

    (F tensor I_S) W |psi>
      = (1/2)sum_a |a>_(R1) tensor |psi>_(R2) tensor |a>_S.

Thus R decomposes, after F, into R1 tensor R2. The logical state sits on R2;
R1 and S form a fixed maximally entangled pair. Apply F on R and discard R1
to recover |psi>, or any mixed/reference-entangled input by linearity.

The checker also verifies every erasure condition

    W†(I_R tensor |a><b|_S)W = delta_ab I_logical/4.

This is exact state AND operator reconstruction for this specified code.
It is equivalent under an explicit basis change to storing the logical
state in part of R alongside a Bell pair. It is not by itself an emergence
of spatial geometry, gravity, an entropy-area law or a physically identified
horizon. No literal seam-boundary recovery is claimed.

## 5. The logical operations are also already algebraic: right multiplication

Let R_i |v>=(-1)^c(v,e_i)|v+e_i> be RIGHT multiplication by g_i in the word
algebra. Left and right multiplication commute. The exact identity is

    (R_i† tensor I_S) W = W g_i.

So each logical primitive has a representative acting on R alone. Products
and linear combinations preserve this intertwining; adjoints do as well
because the code is invariant under these unitaries and their inverses.
There is no need to infer an operator map just from dimension or spectrum.

For a specified Hermitian polynomial H_logical in g_i, this gives a Hermitian
record representative with H_R W=W H_logical. But it does NOT select that
polynomial or its coefficients. H_code vanishes on the whole logical space;
its constraints protect information, they do not determine its nontrivial
dynamics. Source-derived physical access to right multiplication also remains
unproved. Algebraic availability and an implemented physical operation differ.

## 6. Why this does not contradict the previous classical-record result

Dephasing R in its word basis changes the encoded state to

    (1/16)sum_v |v><v| tensor U_v rho U_v†.

After discarding S, this gives I_R/16 for every input rho. The classical
labels alone contain no input information. The off-diagonal word coherences
are essential for record-only recovery. With a classical record AND S,
conditional correction still works as in [PRIMITIVE_RECORD_RECOVERY.md](PRIMITIVE_RECORD_RECOVERY.md).

This is a precise example of why preserving the signed algebra and its
coherences matters. Merely having sixteen classical labels does not provide
the coherent sixteen-dimensional physical carrier required here.

## 7. Completion boundary and next source obligations

Closed in this finite conditional construction: commuting constraints,
the complete code projector, record-only recovery, and explicit logical
generator reconstruction from source-word right multiplication.

Open: why TFPT realizes the joint register/system tensor product; why its
physical state satisfies S_i=+1; whether all actual source operations preserve
that space; preparation and record access; a selected nontrivial logical
Hamiltonian; relation to the actual seam, spatial locality and a common
continuum. The existence of this code closes none of T1–T8 on its own.

## Verification

`coherent_compiler_record.py` checks the source-pinned regular representation,
four 64-dimensional decoder identities, the commuting stabilizers, the exact
64x4 encoding, all sixteen character-sector dimensions, record-only decoder,
all sixteen erasure matrix units, right-action intertwiners and the separate
two-level Hamiltonian identity. Full upstream physical suites are not rerun.
The normal and Python `-OO` runs each pass 70 exact checks and produce
byte-identical JSON output. These are finite algebraic checks, not a physical
completion certificate.
No paper/status promotion, commit, push or external export is claimed.
