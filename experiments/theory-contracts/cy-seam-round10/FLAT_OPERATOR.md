# A constructive local boundary operator, and its exact spectral limitation

Status: unpromoted mathematical research, 2026-09-06. This constructs a
specific elliptic **boundary** operator on the proposed geometry; it is not
the microscopic TFPT operator and not a physical 3+1D completion. The metric
area and operator choice below are new declared data, not TFPT outputs.

## 1. Local operator and its domain

Let F=C/(Z+iZ) carry ds²=A(dx²+dy²), A>0. A nontrivial degree-zero
holomorphic line has its compatible unitary flat connection, unique up to
unitary gauge after a Hermitian normalization. Write the holonomy angles as
(a/4,b/4), (a,b) in (Z/4)². In the universal-cover description sections obey

    f(x+1,y)=exp(2 pi i a/4) f(x,y),
    f(x,y+1)=exp(2 pi i b/4) f(x,y).

The local connection Laplacian is Delta_L=-(partial_x²+partial_y²)/A.
Multiplication by exp(2 pi i(ax+by)/4) identifies its Hilbert space with
periodic L², and the Fourier basis has exact eigenvalues

    lambda_nm = (4 pi²/A)[(n+a/4)²+(m+b/4)²], n,m in Z.

Define its self-adjoint domain by sum lambda_nm² |c_nm|²<infinity.
The diagonal real nonnegative Fourier multiplier is self-adjoint, has
compact resolvent and smooth eigenbasis; integration by parts gives the
local differential expression. Finite Fourier sums form an operator core.
This is an explicit construction, not merely an existence claim or a
numerical spectrum extrapolation.

## 2. Coherent rank-four completion

For r(z)=iz+T, T=2P, form E=direct_sum_{j=0}^3 (r^j)^*L_P, with the pulled-back
metrics/connections. The canonical cyclic pullback identification defines a
unitary U on sections. Since r^4=id, functorial pullback gives U^4=I (no arbitrary
closing edge). The direct-sum Laplacian Delta_E commutes with U. This supplies
a local, positive, self-adjoint **chosen** boundary operator with the desired
order-four action.

Explicitly on a frequency w/4, pullback by r gives phase
exp(2 pi i (w/4).T) and frequency R^T w/4. Across four applications the
translation phases multiply to one because I+R^T+(R^T)²+(R^T)³=0.
The operator remains local on E even though the symmetry U moves base points.

Fix the principal-polarization convention explicitly: the divisor point
P=(b-ia)/4 corresponds to holonomies (a,b)/4. One sees this by taking
theta(z-P)/theta(z) and multiplying by exp(-2 pi i Im(P) z); the resulting
multipliers are exp(-2 pi i Im(P)) and exp(2 pi i Re(P)), up to the inverse
bundle convention. Accordingly T=2P has representative
((b mod 2)/2,(a mod 2)/2), **not** ((a mod 2)/2,(b mod 2)/2).
The inverse convention changes both signs and gives the same two-torsion
translation. These rotations/signs preserve both spectral orbit types;
no numerical physical CP label is assigned.

## 3. All four character restrictions are unitarily isospectral

This follows from a general lemma, not from finite spectral samples. Let
H=direct_sum_{j=0}^3 H_j, U H_j=H_{j+1}, U^4=I, and let self-adjoint D be
block diagonal with UDU^-1=D including domains. For k=0,1,2,3 define

    W_k v = (1/2) sum_{j=0}^3 i^(-kj) U^j v, v in H_0.

The four summands are orthogonal, so W_k is an isometry. Its image is exactly
ker(U-i^k): the eigenvalue equation determines every component from the
zeroth. Furthermore D W_k=W_k D_0, including domains. Therefore every
character restriction is unitarily equivalent to D_0. Apply this to
Delta_E. All heat traces, spectra with multiplicities and spectral zeta
determinants of these positive character restrictions coincide.

For successful CM points, 2P is nonfixed by i. In E[4] this is precisely
opposite coordinate parity. The eight possibilities form two rotation orbits
represented by (1,0) and (1,2). Hence the exact gaps are respectively

    gap = pi²/(4A),       gap = 5 pi²/(4A).

There are two admissible marked geometries, not a geometrically selected
unique value. Their gap ratio is five **for this chosen Laplacian**, not a
predicted particle mass ratio. Within either geometry every clock character
has the same gap and full spectrum. Acyclicity of the four nontrivial
degree-zero lines also gives H^0(F,E)=H^1(F,E)=0. Thus this completion alone
provides neither chiral zero modes nor character-dependent mass splitting.

The statement is stronger than a Laplacian calculation: it holds for any
block-preserving equivariant self-adjoint operator. Constant character twists
of U relabel the four identical spectra; they cannot split them.

## 4. Exact limits and counterexamples

Symmetry **alone** does not force isospectrality. On a single four-cycle,
I+epsilon(U+U*) commutes with U but has character eigenvalues
1+2 epsilon cos(pi k/2). As a torus operator this uses finite rotations of
base points, so it is not a local bundle endomorphism. More general local
off-diagonal smooth bundle maps can exist if new, nonparallel coefficient
sections are supplied. They are not excluded here. In contrast, global
holomorphic off-diagonal maps between our distinct degree-zero line bundles
vanish, as do parallel maps. An actual local splitting mechanism must specify
additional data and leave the audited block-preserving class.

Likewise a unitary cyclic operator with closing edge -I satisfies U^4=-I,
not I; exact coherence is essential. The checker tests both negative controls.

Equality of scalar Laplacian spectra at a point is **not** equality of chiral
determinant lines with connection over a configuration family. We do not
identify a scalar spectral determinant with the open TFPT chiral measure.
No global lift of the CM clock to the rational elliptic surface is supplied.

## 5. Reproduction and source boundary

Run `python flat_orbit_operator.py` with SymPy installed. The checker tests
complete bounded spectral shells, exact affine phases and character
projectors, plus the negative controls. The all-mode and domain statements
are proved above, not established by counting finite checks.

The Fourier proof is elementary and explicit. For the broader mathematical
setting, see [Gordon, Guerini, Kappeler and Webb, *Inverse spectral results on
even dimensional tori*](https://www.numdam.org/item/AIF_2008__58_7_2445_0/).
That paper is not invoked as a TFPT identification theorem. Determinant
connections require additional information; see [Freed, *Determinant Line
Bundles Revisited*](https://arxiv.org/abs/dg-ga/9505002).

T1-T8, the shared microscopic parent, the chiral measure, continuum dynamics,
coupling selection, universal gravity and initial-state selection stay open.
