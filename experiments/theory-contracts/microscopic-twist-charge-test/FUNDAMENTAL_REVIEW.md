# Parallel review: simpler structure, criticality, and actual channel count

9 September 2026. A user-requested parallel, read-only review was checked
against the original sources and reproduced by the integrating agent.
No source Hamiltonian, paper, website or T1–T8 status is changed.

## 1. Separate global carry from local field shape

The most useful simplification is not a new geometric ingredient. The
original flux ramp already advances the actual Fourier labels. Continuing
the filled occupations, rather than resetting the sea after each step,
produces the integer carry after two half steps. Its canonical polar
correction transports the complete sea exactly.

This gives a clean division of work: a common global carrier handles the
sector change; the existing endpoint-dependent factor handles the field
profile. Replacing the former leaves every source-side neutral pair
exactly unchanged. [The derivation](PROOF.md) and finite charged-operator
tests implement this route on the original microscopic space.

The simplification is limited: a background-dependent global transporter
is not a local charged field or a derived autonomous dynamics. It avoids
adding a charge counter by hand, but does not itself explain why TFPT
selects the background path. Locality, normalization, and growing-window
energy estimates remain the first operator-level follow-up.

## 2. Fixed-width half charge requires the critical representative

The existing proof is valid at the explicitly fixed m=1,W=8 source; the
parallel review found no hard contradiction to that scoped derivation.
However, this assumption matters much more than the early finite-size
half-charge plateau suggests.

For an explicitly labeled control m=1+epsilon, the original chiral-basis
strip block has

```
D(p)=(m-cos p) I-shift_upper,
det D(0)=epsilon^W.
```

At fixed finite W and m not equal to either 1 or -1, the entire strip is
gapped. Indeed a zero of h requires both sin p=0 and det D(p)=0. The
regional negative-projector density f(p) is then periodic analytic.
The difference between its r=1 and r=3 shifted-grid sums tends to zero:
Fourier aliasing bounds it by exponentially small coefficients times N.
Constants depend on the gap and on W; convergence need not appear at
small circumference.

Reproduced controls with W=8 and the original regional cut:

| Mass | N=64 | N=256 | N=1024 | N=4096 |
|---|---:|---:|---:|---:|
| Original 1.0 | 0.500000 | 0.500000 | 0.500000 | 0.500000 |
| Mutant 1.5 | 0.489780 | 0.408620 | 0.075999 | 0.00001736 |
| Mutant 1.8 | 0.023258 | 0.000000196 | numerical zero | numerical zero |

Entries are full-sea upper-region differences, not fitted charges. The
last floating-point values for mass 1.8 are of order 1e-11, not certified
exact zeros. Mutants are evaluated in a separate function; original
source pins are unchanged.

### An alternative to requiring an exact mass value

For delta=|epsilon| in (0,1), the zero-momentum half gap is the smallest
singular value of D(0), with rigorous elementary bounds

```
(1-delta) delta^W/(1-delta^W)
 <= s_min(D(0))
 <= sqrt((1-delta^2)/(1-delta^(2W))) delta^W.             (1)
```

The lower bound follows by expanding the inverse triangular matrix as a
finite geometric series. The upper bound follows by testing the normalized
geometric edge vector. Thus the relevant rescaled gap is of order
N delta^W. This suggests two distinct routes:

1. Derive why the fixed-width physical source must lie at its critical
   representative. The current construction has not done so.
2. Treat m=1 as a tractable representative of a class, and prove a suitable
   universality limit. A candidate is
   W(N)=ceil((1+nu) log N/|log delta|), nu>0, so N delta^W -> 0.

The second route changes the width limit and must be declared as such.
It is not yet a universality theorem. At momentum p, let rho=m-cos p and
C^2=(1-rho^2)/(1-rho^(2W)). Compression on the two normalized geometric
edge vectors gives exactly

```
[[-sin p, C^2 rho^W], [C^2 rho^W, sin p]].              (2)
```

This compressed space is not exactly invariant. Each vector's residual
outside it has norm C |rho|^W sqrt(1-C^2), for |rho|<1. For the r=1,3
Fourier window |j|<=M_N<=sqrt(N), put

```
tau_N=delta+2 pi^2 (M_N+3/4)^2/N^2.
```

The rescaled residual is at most a constant times N tau_N^W. With the
displayed logarithmic width this vanishes. These are useful spectral
estimates, not the missing complete-sea, Gaussian-filter, adjoint and
local-field estimates for growing W. Those must be proved uniformly
before this route can remove the fixed-mass selection obligation.

## 3. Eight rows must not be counted as eight chiral currents

The present single strip has one geometrically marked branch on each
edge. Its transverse width eight is not eight independent chiral channels.
The older [v367 lattice calculation](../../../verification/v367_seam_s3_lattice.py)
sets N_Maj=2^(g_car-1) and multiplies a one-copy central charge by that
number. This computes a declared multi-copy model; it does not reconstruct
the copies from this strip's microscopic current algebra.

The concrete next test is the central-term/Gram matrix of genuinely
source-defined low-energy currents: derive its rank and marking before
identifying it with the eight-dimensional E8 charge space. If it has rank
one on one boundary, no relabeling of transverse rows supplies rank eight.
An additional source mechanism would have to generate those channels.

This agrees with the existing
[parent-selection audit](../parent-selection-audit/README.md) and
[Origin composition review](../origin-composition-audit/README.md): a
compact principle can conceal strong assumptions. The Origin Story's
word “admissible” already includes several desired physical properties.
They cannot simultaneously be counted as derived consequences of the
slogan. A promising common strategy is to prove a minimal universal
construction with explicit observable and state maps, not merely to make
the list of axioms look shorter.

## Research priority

First pursue the improved operator (4) in PROOF.md through a nonzero,
energy-controlled smeared limit, keeping its exact neutral-pair identity.
In parallel, test the width/mass route against the full sea, not just its
two edge quasimodes. Then require actual current-channel rank and phases
from the same source. These are discriminating next steps; none is a
claim of a completed TOE or a new link to RH.
