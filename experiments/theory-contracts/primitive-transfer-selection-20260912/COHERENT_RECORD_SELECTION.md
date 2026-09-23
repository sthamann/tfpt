# Coherent record: exact selection boundary and a discrete-step alternative

NON-RH, 12 September 2026. No physical completion or status promotion.
Companion: [coherent_compiler_record.py](coherent_compiler_record.py).
New reproducible audit: [coherent_record_selection.py](coherent_record_selection.py).

## 1. What is source-derived and what was added

The pinned source supplies four skew-Hermitian Clifford generators on C^4,
their sixteen signed words U_v, and left-regular multiplication L_i.
It also supplies the quaternion frame and its family-cycle element.
Interpreting sixteen algebraic labels as a physical C^16 register R,
adjoining an independent C^4 system S, and imposing L_i tensor g_i = +1
are additional premises of this particular code construction. Source pins
and exact matrices do not turn these premises into physical conclusions.
This audit neither inventories all other physical TFPT candidates nor
identifies the family cycle with the actual seam Clock.

## 2. The apparent holographic encoding is a general finite construction

For ANY Hilbert-Schmidt orthogonal unitary basis {U_v}_{v=1}^{d^2} of M_d(C),
define W psi = (1/d) sum_v |v> tensor U_v psi and
F_{(a,b),v} = conjugate((U_v)_{ab})/sqrt(d).
Completeness of the orthogonal operator basis gives

    sum_v conjugate((U_v)_{ab}) (U_v)_{sc}
       = d delta_{as} delta_{bc}.

Therefore F is unitary and

    (F tensor I) W psi
       = (1/sqrt(d)) sum_a |a>_R1 tensor |psi>_R2 tensor |a>_S.

The reconstruction is thus an explicit basis change exposing a fixed Bell
pair and the logical input. It is not, by itself, a TFPT-specific selection,
a compression below the input dimension, or a spatial holographic law.
The checker includes a non-TFPT d=2 Pauli-basis positive control.

This is consistent with established unitary-error-basis mathematics;
see R. F. Werner, [All Teleportation and Dense Coding Schemes](https://arxiv.org/abs/quant-ph/0003070).
The elementary identity above is supplied here directly, rather than treating
that reference as a proof of the additional TFPT physical assumptions.

### Conditional optimality, not a universal dimension selector

In our d=4 code the erased S is I_4/4 for every logical input, and erasure
is exactly correctable from R. For a maximally entangled logical input and
four-dimensional external reference E, the marginal ES is I_16/16:
the erased channel is completely depolarizing, also on matrix units.
The pure global encoding requires R to purify a rank-16 state, hence

    dim R >= 16.

The construction attains this lower bound. This is a lower bound for a pure
isometric encoding with this full-rank erased marginal, not for every
possible physical encoding. A fixed pure erased subsystem would instead
allow dim R = 4. Mixed extra environments change the bookkeeping.

## 3. Every logical Hamiltonian survives the four constraints

In the record-only F coordinates,

    F L_i F* = conjugate(g_i) tensor I_4.

The constraints consequently act only on R1 and S. For EVERY Hermitian
4x4 matrix h the record operator

    h_R = F* (I_4 tensor h) F

commutes, after adjoining I_S, with all four constraints and obeys

    (h_R tensor I_S) W = W h.

The Hermitian source words span all sixteen real Hermitian directions.
Removing the scalar energy offset leaves fifteen unconstrained logical
Hamiltonian parameters. This establishes the complete freedom of the
logical restriction, not merely a few alternative examples. There may be
further unconstrained off-code choices, which are not needed for the result.

### Positive, unique-ground, isospectral counterexample

Take h_A = diag(0,1,2,3), q = Hadamard tensor I_2, h_B = q h_A q*.
Append either record lift to the SAME positive constraint parent
H_c = sum_i (I-S_i)/2. In decoded syndrome coordinates H_c has energies
0,1,2,3,4 with multiplicities 1,4,6,4,1, tensored with a logical identity.
Both full parents H_c + h_{A/B,R} tensor I_S thus have energies

| Energy | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Multiplicity | 1 | 5 | 11 | 15 | 15 | 11 | 5 | 1 |

Both are positive, have a unique ground state and gap one, preserve the
same code, and have the same entire spectrum. Yet from logical |00> at
t=pi/2, the probability of returning to |00> is 1 for A and 0 for B.
Preparation and measurement are held fixed: these are not compared after
silently relabeling the apparatus. Their physical availability is conditional
on the code/register model, not an experimental TFPT prediction.
The energy unit and time units here are illustrative inputs.

## 4. Full invariance is not a remedy; an assigned automorphism is different

Requiring [h,g_i]=0 for every logical generator leaves only h=cI: the
commutator map has rank 15 on the 16-dimensional Hermitian space. Thus this
EXTRA fixed-frame invariance condition removes nontrivial isolated logical
motion. It is not a prohibition on symmetry-invariant interacting field
theories, relational evolution, or dynamics on a larger system.

There is a more constructive, weaker alternative. Set

    u=(g1 g2, g2 g3, g3 g1),  w=(I+u1+u2+u3)/2.

Then w is unitary, w^3=-I, and conjugation cycles g1->g2->g3->g1 while
fixing g4. If a unitary v implements EXACTLY this ordered generator action,
w* v commutes with all four generators. Consequently v=e^(i theta) w.
The ASSIGNED generator automorphism uniquely determines a unitary step
modulo global phase. This is an exact discrete operational determination;
it does not require guessing a Hamiltonian first.

However, promoting this algebraic family permutation to a physical update
is an added premise. Its channel has period three. It supplies neither
an elapsed physical time nor propagation between spatially localized sites.

### Continuous interpolation is still nonunique, even with positivity

Let N=i(u1+u2+u3)/sqrt(3), N^2=I, P_+=(I+N)/2, P_-=(I-N)/2.
Both projectors have rank two. With an assigned unit time and hbar=1,

    h_1 = (pi/3) P_+ + (5pi/3) P_-,
    h_2 = (7pi/3) P_+ + (5pi/3) P_-

are positive and satisfy exp(-i h_1)=exp(-i h_2)=w. At half time their
relative unitary is P_- - P_+, not a scalar. An equal superposition of one
unit vector from each eigenspace gives orthogonal half-time outputs.
Thus all integer updates can agree while intermediate predictions differ.
This explicit branch ambiguity is enough to refute uniqueness; no claim
to classify all Hamiltonian logarithms is needed.

## 5. Focused continuation criteria

1. Locate a source-defined preparation/access map for an actual register;
   the mere existence of a regular representation is insufficient.
2. Ask whether the family automorphism is explicitly an operational update,
   not a symmetry relabeling or a matrix-assembly loop. If not, do not call it time.
3. If it is an update, test the resulting discrete process first. Its period
   three alone cannot supply general physical dynamics. A source-derived
   composition/interaction rule, not an arbitrary extra Hamiltonian, is needed.
4. Derive a continuous interpolation or show why only discrete predictions
   are physical. Positivity and a unique matrix logarithm convention are not
   an origin derivation. Record access, locality and a common continuum remain open.

These results remove an unjustified uniqueness inference and identify an
exact finite discrete-step question. They close none of T1-T8.

## Verification

The new checker verifies pinned source identities, complete Hermitian span,
all sixteen record lifts, the fixed-frame invariance rank, the family-cycle
intertwining, two distinct positive logarithms, the isospectral parent pair,
the rank-16 purification bound in this construction and the d=2 control.
It uses explicit exceptions, not optimization-removable assertions.
Normal and Python `-OO` execution each pass 83 exact checks; a subprocess
comparison confirms byte-identical JSON results. `git diff --check` passes.
No commit, push, paper rebuild, external export or physical-suite rerun.
