# A minimal covariant collision completion of the actual D3/7 decode

2026-09-14. Positive construction with explicit resource assumptions; no
native tensor product, interaction, measurement, reset or physical time is
derived. The largest quantum Hilbert space used in the check is64D.

## Positive result and its exact scope

The actual sixty-ray transition has quantum decode

    D(rho)=(3/7)rho+(4/7)I4/4

for normalized rho. This is not inferred from a proposed new noise channel:
the probe replays the source construction through its exact16x60 decode
intertwiner in `compiler-origin-audit-20260913/context_instrument.py:129-138`,
including the original v783 root/context prefix.

Assume a system S=C4, an environmental collision factor E=C4 initially in
I4/4, and permission to implement a unitary commuting with every g tensor g.
Then the full covariant unitary class is

    U=e^(i phi)[cos(theta) I+i sin(theta) Swap].

The source contrast fixes cos²(theta)=3/7. Up to global phase and theta modulo
pi, exactly two choices remain:

    U+ = sqrt(3/7) I+i sqrt(4/7) Swap,
    U- = U+†.

Thus there is a particularly small exact common unitary completion of the
one-time **quantum decode**. This does not reconstruct the complete original
sixty-label instrument or select its context/record history from that decode.

## Why the covariance statement is exact

For full SU(4), the symmetric10 and antisymmetric6 sectors give the commutant
span{I,Swap}. The same commutant already follows for the actual full
projective two-qubit Clifford group. The independent finite check uses its
four collective Pauli generators, whose sixteen joint eigenspaces have rank1,
and the actual H1,H2,S1,S2,CNOT action. It is transitive on the fifteen
nonidentity Pauli tensor operators. Since

    sum_Pauli P tensor P = 4 Swap,

the full commutant reduces exactly to I and Swap. Every unitary in it has one
phase on Sym10 and one on Anti6, giving the form above. The group symmetry is
a covariance requirement, not evidence that the particular partial-SWAP is
an executable original Clifford word.

The partial-trace identity is

    tr_E[U(rho tensor sigma)U†]
      = cos²(theta)rho+sin²(theta)sigma
        +i cos(theta)sin(theta)[sigma,rho]

for normalized inputs. At sigma=I4/4 the commutator vanishes. The channel is
therefore D_(cos²theta), and neither the sign of theta nor phi is identified
by any one-time system preparation/readout experiment.

## Canonical purification and minimal Stinespring rank

Purify the trace environment as

    |Phi4>_(E,A)=(1/2)sum_j |j>_E |bar j>_A,
    V|psi>=(U_SE tensor I_A)(|psi>_S tensor |Phi4>_(E,A)).

The auxiliary factor carries the **conjugate** representation4bar. Thus
E tensor A is the neutral16D representation4 tensor4bar=End(C4), and

    Vg=(g_S tensor g_E tensor bar(g)_A)V.

This was checked on the actual Clifford generators and on all fifteen
infinitesimal SU(4) generators, as well as the central iI4. The total purified
space is4*4*4=64D.

The normalized channel Choi matrix is

    J=(3/7)|Phi4><Phi4|+I16/28.

Its eigenvalues are13/28 once and1/28 fifteen times. Consequently its Choi
rank, and the minimum dimension of a **pure-state Stinespring environment**,
is exactly16. The construction achieves that minimum. A mixed4D collision
bath does not contradict this: its purification introduces the additional
4bar factor.

If one instead demanded a nonzero linear intertwiner C4->C4 tensor C4 with
both output factors fundamental and no purifier, the central element iI4
would impose iV=-V, impossible for nonzero V. This is a statement about that
specific representation-typed pure isometry, not a prohibition of mixed4D
baths, other record representations or ordinary channels. The64D construction
is mathematical purification, not a newly derived physical TFPT cell.

Even with the canonical purification, the two signs are related as one-time
minimal dilations by an explicit environment-only unitary. Writing
P=|Phi4><Phi4| on E tensor A,

    W=[(11-4i sqrt3)/13]P-(I-P),
    V-=(I_S tensor W)V+.

This unitary commutes with the neutral environment representation. One-time
Stinespring uniqueness therefore does not choose a sign or the way this
environment is subsequently accessed. In general W does not preserve an
independently designated active E versus passive A factor.

## Two contacts: fresh versus reused environment

With no intermediate intervention, two fresh trace environments give

    D_lambda composed D_lambda = D_(lambda²), lambda²=9/49.

Reusing the same environment and the same unitary gives instead

    U_theta²=U_(2theta),
    D_reuse=D_(cos²(2theta))=D_(1/49).

For any original pure source ray prepared and tested again, the complete raw
return probabilities are

| Execution | Return probability |
|---|---:|
| One contact | 4/7 |
| Two contacts, fresh environment | 19/49 |
| Two contacts, reused environment | 13/49 |

The difference is6/49. Both signs give the same values in this unfiltered
test. The same fixed unitary and same initial trace environment have been
used; the missing extra choice is whether its memory is kept or discarded.
The fresh calculation explicitly traces out/replaces the environment; it
does not treat reset or supply of fresh states as a free physical operation.
The reused result was additionally checked as one full64D purified execution.

## Existing ray boundaries can distinguish the angle signs at two times

Use three actual original Gaussian/stabilizer rays, verified against the
source sixty-ray set:

    input |z>=|00>,
    intermediate selected ray |x>=|+0>,
    final tested ray |y>=|+i,0>.

Apply one contact, record the rank-one intermediate filter P_x, then apply a
second contact and test P_y. The environment begins in the same trace state
as before. The filter is an explicit additional instrument/access premise;
the source ray's existence alone does not implement it.

The intermediate flag has raw probability5/14 for either sign. With the same
environment retained, the **joint**, unrenormalized flag-and-final-event
probability is

    p_joint(U+) = 29/196-2sqrt3/49,
    p_joint(U-) = 29/196+2sqrt3/49.

Their difference is4sqrt3/49. Dividing by the recorded5/14 would give the
conditional values29/70 minus/plus4sqrt3/35, but the probe computes the raw
joint weights first and never normalizes hidden histories independently.
With a fresh environment at the second contact the joint probability is
25/196 for both signs.

Therefore the angle sign is markable by fixed existing boundary directions
plus an intermediate record contract. It is not fixed by the one-time decode
or by the simple unfiltered return test. An arbitrary overall unitary phase
still requires interference against a separately controlled alternative;
ordinary channel measurements do not expose it.

## What the one-time source data leave open

The positive construction requires separately specified system/environment
tensor factors, the active versus passive environmental representation,
implementation of the partial-SWAP, allowed intermediate instruments, and
reset/reuse rules. The measured lambda fixes a mixing angle within this
covariant ansatz, not a physical duration or Hamiltonian strength. Matching
the quantum decode does not fix a sixty-label record instrument, its loss of
context information, or any larger physical theory.

## Verification

`probe.py` performs158 own exact guards and2014 inherited source/decode-prefix
guards, with no floating-point norm claims. `replay.py` requires normal/-OO
byte-identical JSON and rejects three mutants: replacing reuse by fresh
composition, declaring the sign invisible despite intermediate records, and
identifying the mixed4D bath with a pure4D minimal environment.

Source hashes, the actual boundary-ray indices and exact counts are preserved
in `verification.json` and `replay.json`. All writes are confined to this new
collision directory.
