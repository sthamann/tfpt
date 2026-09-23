# Native half-loop transport and background-aware energy matching

## 1. Fixed source and full physical Hilbert space

Use exactly the native square and all terms of Round37, as pinned and
executed in the previous common-engine experiment. There are eight complex
fermion modes. On the neutral Gauss sector the occupation number is four.
Write m for an eight-bit occupation mask with popcount four, and w for an
arbitrary integer. There are 70 such masks, not 140 or an added coin space.

For `q_x=n_Lx+n_Hx-1`, set

```
r(q)=(q2,-q0-q2,-q0-q1-q2,0),
z=(1,-1,-1,1),
E(m,w)=r(q(m))+z*w.
```

Then `B E=-q`, and every original integer Gauss state is uniquely of this
form. The physical space is thus a coordinate presentation of
`direct_sum_(70 masks) l2(Z)`. The Wilson loop W shifts w by one and leaves
m unchanged. No finite cyclic rotor is used.

## 2. Matter-assisted root on the existing space

Let `mbar=255 xor m`, so `q(mbar)=-q(m)`. Select the existing occupation
bit `b(m)=n_H3`, which satisfies `b(mbar)=1-b(m)`. Define

```
S |m,w> = |mbar,w+b(m)>,
S*|m,w> = |mbar,w-(1-b(m))>.
```

Both are inverse permutations of the same complete orthonormal basis.
Thus S is unitary and `S²|m,w>=|m,w+1>=W|m,w>`. Also `[S,W]=0`.
The actual flux change is

```
Delta E = -2 r(q(m)) + b(m) z
```

for S, with the analogous inverse expression for S*. It is integral and
`B Delta E=2q`, which cancels the matter charge change `Delta q=-2q`.
Hence each direction preserves Gauss.

The implementation checks the identities on all 70 masks with symbolic
integer w. Large positive and negative integer samples separately compare
against the original source action. Such samples are corroboration, not
the reason the identities extend to every integer.

### Realization in the existing operator algebra

On the N=4 sector, a product annihilating the four occupied source modes
and creating the four complementary modes is the matrix unit
`|mbar><m|`, with an explicitly checked CAR ordering sign. Multiplying
each matrix unit by the integer link shifts `U^(Delta E(m))` implements S.
This is a finite sum of existing matter and link operators, supported on
this square; no auxiliary field is required. It is an eight-fermion
observable, not an added eight-fermion Hamiltonian term and not a
single-particle field.

The construction selects a bit, a charge-chart pairing and matrix-unit
phases. Eight tested bit choices give distinct roots. Nothing here proves
their equivalence under the actual Clock or selects one dynamically.
This finite open-square result is not a local-net construction on the
infinite lattice; exterior transport and continuum identification remain
separate obligations.

## 3. Common energy domain and adjoints

An exact census over all masks and both signs gives
`||Delta E||² <= 44`, uniformly in w (also for the eight tested pivots).
Put `H_E=kappa ||E||²/2`, with original `kappa=1/100`. Pointwise,

```
H_E(S^eps state) <= 2 H_E(state) + 44 kappa,  eps=+1,-1.
```

Because S is a basis permutation, the inequality proves

```
||H_E S^eps psi|| <= 2 ||H_E psi|| + 44 kappa ||psi||.
```

Write `H=H_E+V`, with all original onsite and hopping terms in V. On this
fixed finite graph, V is bounded. The unchanged source term groups give

```
||V|| <= 4M + 24 beta a² + sum(source group bounds)
       = 2407/144 =: B0.
```

This deliberately loose bound retains both high and low species and every
two-link path. Bounded perturbation gives `D(H)=D(H_E)`. Therefore

```
||H S^eps psi|| <= 2 ||H psi|| + (3B0+44 kappa)||psi||
                = 2 ||H psi|| + (60703/1200)||psi||.
```

The same argument in the quadratic form norm proves preservation of finite
expected electric energy. Both S and S* map the full Hamiltonian domain
onto itself, not merely a special finite cutoff core. Consequently
`S(t)=exp(itH) S exp(-itH)` is a well-defined bounded operator with the
same domain property; its strong time derivative on D(H) is controlled
by the corresponding commutator.

Numerically the sequence `evolve(2), S, evolve(2)` was executed at cutoff
10. The tiny measured loss from projecting S's output is recorded rather
than normalized away. This finite diagnostic is not an interval-certified
infinite-volume calculation. Domain control comes from the argument above,
not the small numerical loss.

## 4. Why the scalar spectral root is not an energy-regular replacement

For a fixed q=0 matter mask, pass to the loop-angle representation on
`-pi<theta<pi`. W is multiplication by `exp(i theta)`. Its branch root
`R=exp(i theta/2)` is a bounded unitary with R²=W, but is discontinuous
as a periodic function. On the constant loop vector its coefficients are

```
r_n = (1/2pi) integral_-pi^pi exp(i(1/2-n)theta) dtheta
    = 2(-1)^n / [pi(1-2n)].
```

Their squares sum to one by Parseval. Electric energy on this charge
fiber is `2 kappa n²`. Thus the graph-norm series has terms asymptotic to
`const*|n|^(4s-2)`, proving

```
R Omega in D(H_E^s) iff 0 <= s < 1/4.
```

In particular expected electric energy diverges. The symmetric partial
sum of that energy grows as `4 kappa N/pi² + O(1)`.

Nor can another scalar branch `f(W)` with `f²=exp(i theta)` map this
vacuum to finite electric energy: that would require periodic f in H1,
hence a continuous representative. The chain rule gives `f'/f=i/2`,
forcing a sign change around the circle, contrary to periodicity. This
argument is specifically about scalar functional-calculus roots. The
matter-assisted matrix root above is a counterexample to extending it to
all roots. It also says nothing against a time-smeared field whose square
is not the same bare unitary loop.

## 5. Actual dynamical mismatch, not hidden by a new charge label

The diagonal quantity `P=w+b(m)/2` satisfies `[P,S]=S/2`. It is therefore
a half-step label for this chosen operator. But `[P,H]` is nonzero. On the
actual preceding experiment's initial state `(m,w)=(105,0)`, a native term
with amplitude 1/12 reaches `(101,-1)` and changes P by -1.

In addition `[H,S]|105,0>` has components outside `S|105,0>`. Thus the
candidate is not a bare zero-mode carry intertwining the unchanged
nonzero-mode dynamics. This does not assert that every full charged field
must have a scalar commutator with H; full fields also create descendants.

A uniform half-electric translation is also not what was constructed:
the E3 increment is 0 or 1, never uniformly 1/2. Such a unitary translation
on the integer E3 spectrum would contradict `exp(2pi i E3)=1`.

### All occupation/flux-diagonal conserved quantities in this patch

The native off-diagonal Hamiltonian terms define a graph on 70 occupation
masks, with each edge carrying its integer winding change. All 640 directed
transitions and their amplitudes are extracted from the original H action.
They do not depend on the input winding. The graph on masks is connected.
There is an explicit nonzero-H path

```
(15,0) -> (27,0) -> (23,-1) -> (54,-1)
       -> (30,-1) -> (27,-1) -> (15,-1).
```

Hence every integer winding at the base mask is connected to every other;
paths on masks then connect the entire 70-times-Z basis. Equivalently the
cycle winding gcd is one. If a diagonal operator F commuting with H has
the finite-support basis in its commutator domain, every nonzero matrix
element forces `F(state)=F(target)`. Connectivity makes F constant.

This strengthens the affine-charge check, whose four-dimensional kernel
consists precisely of the Gauss generators and is scalar on physical
states. It does not exclude non-diagonal conserved operators, different
spatial models, or emergent charges in an independently justified limit.
Assigning arbitrary labels to energy eigenvectors would not establish a
local, physically marked charge algebra either.

## 6. Background-aware target-energy criterion

The previous common-engine energy test explicitly used the quadratic
target energy. Applying raw equal-energy conditions to the source would
ignore its inherited quarter-holonomy. For an affine quadratic energy,

```
E(q)=q^T G q/2 + ell.q + c,
[E(q0+alpha)+E(q0-alpha)-2E(q0)]/2 = alpha^T G alpha/2.
```

Expansion proves this identity for any common reference q0. It cancels
the fixed linear background and reference offset without redefining H,
changing a conformal stress tensor or fitting a chemical potential.

The original `half-charge-energy-bridge` functions are pinned and reused.
For uniform signs its half root has energies `(0,2)`; for the original
5+3 sign option they are `(3/4,5/4)`. Both centered pairs give 1. All 240
root pairs for both options agree. This is still that source-informed
conditional eight-channel target, not eight identified microscopic fields.

The criterion uses comparable charge-sector zero-mode energies or known
descendant levels. An arbitrary smeared field state generally has an
oscillator contribution, so its raw expected energy cannot simply be
inserted into this formula and called a zero-mode measurement.

## 7. Full invariant quadratic family, not a hidden diagonal ansatz

Require `J^T G J=G` and `sigma^T G sigma=G` for the ACTUAL inherited target
maps and G real symmetric. This requirement concerns the quadratic part;
the background linear term need not preserve the same symmetries. Exact
linear algebra leaves six real parameters. In the paired complex coordinates
`z_j=x_(2j)+i x_(2j+1)`, their Hermitian matrix is

```
K = [[a,    c+i*d,c-i*d,u+i*v],
     [c-i*d,a,    c+i*d,u+i*v],
     [c+i*d,c-i*d,a,    u+i*v],
     [u-i*v,u-i*v,u-i*v,b    ]].
```

The real G represents `z* K z`; energy is half this quadratic form.
Choose the six actual target roots, in zero-based real coordinates,

```
alpha0=e0+e1, alpha1=e0+e2, alpha2=e0+e3,
alpha3=e0+e6, alpha4=e0+e7, alpha5=s=(1/2)^8.
```

Their five centered-pair energy differences relative to alpha0 are

```
c,  -d,  u+(b-a)/2,  -v+(b-a)/2,  3c/2+3u/2+(b-a)/4.
```

Vanishing forces c=d=0, then u=(a-b)/2, v=(b-a)/2, and finally a=b.
Thus u=v=0 and `G=a I`. Positivity makes a>0. These five independent
linear comparisons are minimal within the six-dimensional family: fewer
independent linear conditions cannot isolate its one-dimensional scale
line. For each omitted comparison the checker constructs a strictly
positive, symmetry-preserving metric satisfying the other four but not
the omitted one. Positivity is independently bounded by strict diagonal
dominance.

This is an acceptance criterion for a future correctly normalized source
current system. It does not prove that any microscopic candidate already
has these six charge fields, energies or currents. In particular the
matter-assisted S from Section 2 fails the conserved-charge test before
such an identification can be asserted.

## 8. Relation to the external QCA construction

The operator comparison was informed by the half-twist relations in
[Jones–Sopenko–Thorngren, section 7.3](https://arxiv.org/html/2608.26456v1).
Their local conformal-net construction has much stronger field and
locality premises than the single loop relation tested here. We do not
import its conclusion from S²=W, nor claim to have reproduced its QCA.
T1–T8 and the actual microscopic E8 half-charge field remain open.
