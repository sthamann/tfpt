# Primitive block iteration and source symmetry

12 September 2026. NON-RH. Continuation of the exact source-selection audit.
No physical source selection, T1–T8 closure, or continuum limit is asserted.

## 1. What the iteration actually preserves

Use the exact three-site primitive ground isometry G from
`../source-selection/primitive_chain.py`, and W=G tensor conjugate(G).
Its two factors describe two alternating three-site blocks. For the link h
between those blocks, exact boundary contractions give

    W* h W = (3/8) H_sync + (5/4) I.

Thus the primitive coupling reproduces its **first-order compressed shape**.
The factor 3/8 is the square of the source-generator attenuation sqrt(6)/4.
This is not an exact all-time intertwining statement.

For S_i=g_i tensor conjugate(g_i) and K=sum_(i<j)S_i S_j, the discarded
amplitude has exact Gram operator

    W* h^2 W - (W* h W)^2 = (55/64) I + (115/1152) K.

Its smallest eigenvalue is 95/144>0. There is no nonzero logical input whose
bare block encoding remains unaffected by excitation outside that encoding.
Even the logical Bell state has nonzero leakage. This is an amplitude-squared
coefficient, not a finite-time escape probability.

See [the exact block-link proof](block_link.md). The calculation uses only
64-by-4 boundary contractions, not a dense 4096-by-4096 Hamiltonian.

## 2. The controlled question beyond bare compression

Consider the explicitly chosen weak-link family

    H(epsilon)=H0+epsilon h,
    H0=H3 tensor I + I tensor conjugate(H3).

The unperturbed ground energy is E0=8-2sqrt(6), the ground dimension is 16,
and its separation from the next band is Delta=sqrt(6)-2. Centering the
link as h-2I leaves its norm at 2 and does not affect eigenvectors. Weyl's
eigenvalue bounds give a separated lowest 16-dimensional band whenever

    abs(epsilon)<Delta/4,
    gap_(16,17)(H(epsilon)) >= Delta-4abs(epsilon).

This is a sufficient finite-system bound, not a sharp critical coupling
or a uniform many-block claim. An adjusted, or dressed, low-energy subspace
can exist despite the strictly positive bare leakage above.

In canonical degenerate perturbation theory,

    H_eff = E0 I + epsilon K1 + epsilon^2 K2 + O(epsilon^3),
    K1 = W* h W,
    K2 = -W* h Q (H0-E0)^(-1) Q h W,

where Q=I-WW*. All excited bands enter the reduced inverse. Replacing their
denominators by a single gap is not an exact second-order calculation.
The exact finite spectral-response calculation is in `second_order.py`.

The standard direct-rotation and perturbative framework is
[Bravyi, DiVincenzo and Loss, §§3.1–3.4](https://arxiv.org/pdf/1105.0675).
Their conservative absolute Taylor convergence guarantee gives
abs(epsilon)<Delta/32 here after centering, since the unperturbed ground
interval has zero width. This is distinct from the larger real-coupling
band-separation bound. Neither estimate controls a unit-strength link here.

## 3. Exact second order: the one-coupling iteration does not close

The complete finite calculation gives

    K2 = -A I - B K,
    K = sum_(i<j) S_i S_j,
    A = 927307 sqrt(6) / 6167040  = approximately 0.368317537248,
    B = 34101 sqrt(6) / 822272   = approximately 0.101584451032 >0.

These are exact algebraic coefficients. All seven block-energy bands were
included, with exact spectral responses on every primitive source direction.
The highest band's contribution was proved zero, not discarded from a
numerical tolerance. Reflection symmetry proves equality of left and right
responses, as required for neighboring conjugate blocks.

For the Hermitian a_i=i g_i, define

    G* A_i P_E A_j G = d_E I  if i=j,
                       b_E a_i a_j  if i!=j,

where A_i acts at one end of the physical block. The exact response table is

| block energy E | d_E | b_E |
|---|---|---|
| 4-sqrt(6) | 3/8 | 3/8 |
| 2 | 3/32 | 3/32 |
| 4-sqrt(2) | 1/8-sqrt(3)/16 | -1/24+sqrt(3)/48 |
| 4 | 3/16 | 5/48 |
| 4+sqrt(2) | 1/8+sqrt(3)/16 | -1/24-sqrt(3)/48 |
| 6 | 3/32 | 3/32 |
| 4+sqrt(6) | 0 | 0 |

With the ground-ground pair omitted, factorization gives

    A = sum'_(E,F) d_E d_F / (E+F-2e0),
    B = (1/2) sum'_(E,F) b_E b_F / (E+F-2e0),
    e0 = 4-sqrt(6).

The checker verifies the sixteen-term tensor-product contraction fixing
these normalization factors. Negative b_E values in some bands are retained.
The final shift is strictly negative: its three eigenvalues are
-(A+6B), -A, -(A-2B), with multiplicities 2,8,6.

The coefficient of any S_i S_j, i!=j, is orthogonal to both I and H_sync.
A nonzero trace Tr(K2 S_i S_j)/16 therefore cannot be absorbed into an
energy shift or a rescaling of the primitive coupling. Moreover S_i S_j
commutes with K1, so that trace is unchanged by a near-identity logical
gauge change, whose second-order effect is a commutator with K1.

This is a stronger test than bare leakage: leakage alone allows the second
order still to lie in span{I,H_sync}. Conversely, failure of this narrow
closure would not exclude a larger finite interaction family or the dressed
low-energy model. Connecting three blocks can also generate multi-block
terms; pair closure must never be promoted to closure of an entire chain.

An independent numerical 64-dimensional eigenprojector calculation
corroborated A and B, the full factorized 16-dimensional coefficient, and
left/right response equality (residuals below 3e-15). This was a separate
diagnostic, not the source of the exact coefficients or proof.

## 4. Source selection, not extra symmetry by notation

The original source audit and its independently checked counterexamples
are documented in [frame_audit.md](frame_audit.md). An orthonormal Clifford
frame is algebraically available, but a quadratic energy form can still
distinguish the marked anchor. Passive changes of coordinates do not force
isotropy: the coefficients transform with the frame. An additional active
symmetry or operational energy axiom must select the form.

The original carrier also has larger algebraic automorphism groups. The
question is not whether such automorphisms exist, but which must preserve
physical dynamics and which source markings must stay fixed. Different
answers define different candidates; their common Bell kernel does not
make their excitation energies identical.

### The generated interaction has an original-source interpretation

The original Arf form's ten-word q*=1 orbit consists of the four primitive
words and six two-generator words. Its uniform comparison parent satisfies

    H10 = H4 + sum_(i<j)(I-S_i S_j)/2 = 5H4-H4^2,
    spectrum(H10) = 0 (once), 4 (five times), 6 (ten times).

Here H4=H_sync. The orbit belongs to an S5 carrier symmetry already present
in the original sources; it was not invented by fitting the perturbation.
Substituting the polynomial relation into the exact K2 gives

    K2 = 2B H10 - 2B H4 - (A+6B)I.

Thus through second order, up to scalar shifts,

    H_eff = [(3/8)epsilon-2B epsilon^2]H4
            + 2B epsilon^2 H10 + O(epsilon^3).

This is the concrete positive connection: virtual excitations of the
chosen primitive model generate a positive coefficient of the source's
ten-word completion. The coefficient is derived, not a new fitted constant.
It does not show that this is the unique physical source energy, that an
iteration approaches the S5-symmetric parent, or that S5 symmetry is restored.
The H4 coefficient remains nonzero near zero coupling, so the effective
interaction is not itself the pure S5-symmetric H10 model.

### A small pair-interaction space, not yet a closed many-body theory

Define K_r=sum_(|v|=r) product_i S_i^v_i, with K_0=I, for r=0,...,4.
These five independent operators form the degree-symmetric pair space.
For the fixed G used here, the previously checked complete word boundary
map immediately gives

    W* K_r(physical boundary) W = lambda_r^2 K_r(logical pair),
    lambda_r^2 = 1, 3/8, 49/144, 3/8, 1/4.

So failure of the one-coupling ansatz does not require an arbitrary large
pair interaction: a five-dimensional coefficient space contains these
terms and is closed under this specified bare pair compression. This is
an algebraic consequence of the exact sixteen-word map, not a claim about
the newly dressed block ground state or shared-link corrections. Recomputing
G for changed interactions and retaining connected multi-block terms remain
necessary before any self-consistent renormalization claim.

### Two shared links already extend the effective range

The next connected term has also been calculated. Take three alternating
blocks V,conjugate(V),V, with weak links epsilon_L h12 and epsilon_R h23.
In a cross term of the second-order reduced resolvent, only the middle
block can be excited: the other link cannot remove an outer-block excitation.
The outside boundary factors each contribute lambda_1=sqrt(6)/4.

The reflection operator exchanging the ends fixes G and commutes with H3.
On the response columns P_E A_i G, its signs in increasing band order are
1,-1,1,-1,1,-1; the highest band's response is exactly zero. These are
verified response-column parities, not a classification of entire bands.
The cross-end d_E and b_E are therefore the table in section 3 multiplied
by those signs. Exact summation gives

    sum_(E>e0) d_E^(LR)/(E-e0) = -3sqrt(6)/32.

Because a_i a_j is anti-Hermitian for i!=j and the response coefficients
are real, those terms cancel between the two link orderings. The remaining
canonical effective cross term is

    epsilon_L epsilon_R C sum_i a_i tensor I tensor a_i,
    C = -(lambda_1^2/2) sum_(E>e0) d_E^(LR)/(E-e0)
      = 9sqrt(6)/512 >0.

The outside factors here are **same-copy** factors; replacing one by its
conjugate would change the operator. This is a next-neighbor pair mediated
by the middle block, not an additional three-body operator at this order.
Its nonzero traceless outer factors make it linearly independent of
nearest-neighbor terms in the fixed tensor-factor description. This does
not exclude other choices of effective logical gauge, with corresponding
changes in effective observables.

For equal link strengths epsilon, a sufficient finite three-block band
separation bound is abs(epsilon)<Delta/8: the centered sum of two links
has norm at most 4, giving gap>=Delta-8abs(epsilon). The same conservative
Taylor theorem gives abs(epsilon)<Delta/64. No nine-site physical matrix
was allocated; response factorization proves the displayed coefficient.

Thus extending the pair coefficient space alone does not close the
nearest-neighbor ansatz for a chain. The exact algebra remains small at
this order, but the effective interaction range has grown. This is a
controlled finite expansion, not a proof of unbounded proliferation or
of a uniform infinite-chain error estimate.

## 5. Scope and next acceptance

Keep three separate obligations:

1. Derive which source operations are physical symmetries of the interaction.
2. Retain the interaction terms actually generated by controlled elimination
   of excited states, with their error regime stated.
3. Establish any repeated or many-block closure separately, including shared
   links, locality, and the growth of effective interactions.

The chosen graph, physical factors, time scale, and actual TFPT state are
still inputs. This work concerns an exact finite compiler-based model and
its controlled weak-link expansion, not a universal object that solves RH,
factoring, P versus NP, Hylæan, or the remaining physical TOE requirements.

## 6. Reproduction and checker integrity

Run `python3 -B run_checks.py`. Each of the three new checkers is replayed
normally and under `-OO`; all mathematical conditions use exception guards,
not disabled assertions. The receipt binds exact outputs to checker hashes.
Original sources and the preceding exact ground checker are pinned where
used. Analytic perturbation bounds are not claimed as machine-proved by the
finite matrix tests.

The final three-checker replay passes 448 explicit guards per mode, with
byte-identical normal and optimized outputs in all six executions. The
previous source-selection suite also passed in six executions and is
recorded in `previous_source_verification.json`. These are finite checks,
not a count of independent physical predictions or closed TOE obligations.

The first spectral-response run exposed a SymPy structural-equality issue:
I(-1/24+sqrt(3)/48) and -I/24+I sqrt(3)/48 compared structurally unequal.
The reported difference simplified exactly to zero. Following the
systematic-debugging procedure, the checker now compares the exact
simplified residual and includes this regression plus a nonzero 10^-20
counterexample. No numerical tolerance or expected physical result was
substituted. Repeated immutable scalar simplifications are cached only to
reduce runtime.
