# Can positive reflection weights repair ternary reassociation?

12 September 2026. NON-RH finite follow-up. Executable: `weights.py`.

## Answer

**No, not with the same ternary encoding Z and the same five-site
nearest-neighbor Bell interaction family.** One can repair the mean-energy
mismatch by making the two outer links half as strong as the two inner
links. At precisely that ratio, however, the energy variances differ.
Consequently no Hamiltonian-commuting unitary can identify the left and
middle encodings. This is an exact obstruction for every d>1 and every
strictly positive pair of reflection-symmetric weights, not a numerical
search that merely failed to find a repair.

This does not prohibit a different embedding, an enlarged parent, an
explicitly dynamical reassociation map or an approximate effective theory.
Those would change the hypotheses and require their own tests.

## 1. What remains unchanged

Use the precise ternary ground isometry from the previous conditional
three-factor Bell model,

    Z=(V+W)/sqrt(2(1+1/d)).

The left and middle five-factor embeddings L,M are exactly those of
`refinement/ternary.py`: the inner application is inserted in the first
or middle factor of Z, with conjugation on the dual middle factor.
No reoptimization, new encoding, or change of logical basis is made.

The pinned source is `refinement/ternary.py`, SHA-256
`9fbafd5778fc630883046f492f2a86d6693a04ac2a077d93b5ab0738b2db5b31`.
Its original composition-code and note pins are also verified.

The only altered hypothesis is the local energy weighting:

    H(a,b)=a[(I-P12)+(I-P45)]+b[(I-P23)+(I-P34)],
    a>0, b>0.

This retains the chosen open graph, its reflection and the same Bell
projectors. Full active mixed-unitary symmetry, the graph, physical
interpretation and actual origin of these weights remain conditional.

## 2. Exact first moments and the unique energy fit

The five original noncrossing contraction diagrams give a closed
five-dimensional multiplicity-space representation of H(a,b). Their Gram
matrix and L,M coefficient vectors are inherited unchanged from the
source. Their full logical compressions are scalar multiples of I_d:

    L*H L = E_L I_d,
    M*H M = E_M I_d,

    E_L=(d-1)[4ad+4a+5bd+6b]/[4d(d+1)],
    E_M=(d-1)[3ad+4a+2bd+2b]/[2d(d+1)].

Subtracting gives

    E_M-E_L=(2a-b)(d-1)(d+2)/[4d(d+1)].

For every d>1, matching means therefore forces the single ratio

    a/b=1/2.

Thus equal means can indeed be obtained by a simple positive local
reweighting. Stopping at that observation would wrongly credit an energy
fit with repairing physical dynamics.

## 3. Second moment excludes every positive matching choice

At a=b/2 the complete scalar difference of second moments is

    M*H^2 M - L*H^2 L
      = -b^2(d-1)/[8d^2(d+1)] I_d.

It is strictly negative for d>1 and b>0. Since the first moments now
agree, this is also the difference of energy variances for every normalized
logical input. It persists for all nonzero input vectors and is unchanged
by any scalar energy offset H -> H+cI.

At d=4 and b=1, a=1/2:

    E_L=E_M=27/20,
    Var_L(H)=243/3200,
    Var_M(H)=57/800,
    Var_M(H)-Var_L(H)=-3/640.

This gives an ordinary operational witness: the mean energy is identical,
but repeated energy measurements have different fluctuations. No factor,
spectral peak, or physical TFPT apparatus is assumed to be available by
the finite algebraic statement itself.

## 4. Why the moment mismatch rules out an H-preserving repair

If a physical-space unitary U commuted with H and satisfied U L=M, then
for every nonnegative integer k,

    L*H^k L = L*U*H^k U L = M*H^k M.

The first moment forces a=b/2, and the second then contradicts this
necessary equality. Hence no such U exists anywhere in the stated strictly
positive two-parameter family. The same obstruction applies to
U L=M R with an arbitrary logical unitary R, because all these compressed
moments are scalar matrices and therefore invariant under R conjugation.

The claim concerns commuting with the SAME fixed H. It does not address
transforming the Hamiltonian, observable algebra and preparation together,
which would describe a different notion of equivalence.

The full higher-moment checks requested in this audit agree with this
conclusion. At the energy-matching ratio, define Delta_k=M*H^k M-L*H^k L.
Their scalar coefficients are

| k | Delta_k / I_d |
| --- | --- |
| 0 | 0 |
| 1 | 0 |
| 2 | -b^2(d-1)/(8d^2(d+1)) |
| 3 | -11b^3(d-1)/(16d^2(d+1)) |
| 4 | -b^4(d-1)(81d^2+4)/(32d^4(d+1)) |
| 5 | -b^5(d-1)(499d^2+72)/(64d^4(d+1)) |

At d=4,b=1, k=2,3,4,5 give respectively

    -3/640, -33/1280, -195/2048, -3021/10240.

The second moment already proves impossibility; the additional moments
are independent consistency checks, not additional physical gate closures.

## 5. Independent finite representation check

Besides symbolic five-diagram contraction, the checker constructs all
five original diagram embeddings as sparse 1024-by-4 matrices at d=4.
It applies the actual adjacent Bell projectors in tensor coordinates,
not just the five-dimensional matrix, and verifies their weighted action
on every diagram. Then it checks L*H^k L and M*H^k M on the full logical
4-by-4 matrices for k=0,...,5, including off-diagonal logical entries.

The unchanged cross-overlap L*M=(17/20)I4 is retained explicitly. This
guards against silently replacing either branch by an energy-adapted
isometry. No 1024-by-1024 Hamiltonian diagonalization or approximate
floating-point equality is used.

## 6. Scope for the simplicity search

This closes a specific tempting repair: adjusting reflection-symmetric
positive edge strengths to fit a previously unequal mean energy cannot
make the unchanged left/middle encodings equivalent under the same
Hamiltonian. The obstruction is dynamical, not merely a normalization
or scale discrepancy.

It does not establish a universal no-go for simple models. In particular,
it does not exclude a different ternary tensor, an enlarged invariant
interaction family, an explicitly time-dependent recoupling, physical
endpoint relabeling where appropriate, or a controlled approximate
low-energy description. No such extension is constructed here.
Physical origin, common parent, continuum and all T1-T8 remain open.

## Executed verification

Normal and optimized `-OO` runs each pass **33 exact checks**, with
byte-identical JSON confirmed by subprocess comparison. `git diff --check`
passes for the directory. Only the new `weights.py` and `weights.md` were
created; no previous research file, source, paper, website or ledger changed.
