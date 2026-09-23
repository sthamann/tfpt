# Frame, anchor, positive comparison, and time: the exact missing bridge

NON-RH source audit. Conditional finite algebra, no physical-signature selection,
no TOE completion. This note adds no dynamics and changes no previous files.

## The source-specific answer

The original Clifford construction does **not** identify the anchor with time.
In `compiler-clifford-bridge/checker.py:128`, with the actual source generators,

    a=g4, f=g1g2g3, ui=(g1g2,g2g3,g3g1),
    Lorentz: γ0=f, γi=a f ui,
    Euclidean: Γ0=f, Γi=a ui.

The two frames have signatures(+---) and(++++), respectively. Both are
equivariant under the same family cycle. The source explicitly reports
`unique_physical_signature_selected: False` at lines190–193.

Moreover, the exact source identities give

    a=γ0γ1γ2γ3,       χ=i a,

so the anchor supplies an oriented volume/chirality element in this Lorentz
chart; the candidate time gamma is the **family volume f**, not a. Consequently
the primitive weights J for g1,g2,g3 and K for g4 are not automatically spatial
versus temporal energy weights. That reading would need another explicit map.

The underlying original marking is visible in
`verification/v774_arf_spinor_compiler.py:427–437`: anchor bit(0,0,0,1), family
sum(1,1,1,0), and sigma cycling the first three coordinates while fixing the
fourth. `verification/v975_dimension_selector_4d.py:1–65` independently states
that its four-dimensional physics assumptions are not derived from compiler
primitives. It also distinguishes Euclidean real self-duality from Lorentzian
complex self-duality. Neither result supplies a physical clock/update rule.

## A narrow obstruction: no fixed positive Lorentz-vector norm

Let G be a real symmetric matrix defining q(x)=xᵀGx on the real Lorentz-vector
representation. Require invariance under all spatial rotations and boosts,

    ΛᵀGΛ=G.

Spatial rotation invariance forces G=diag(a,b,b,b). For a boost in the01-plane,
the off-diagonal invariance equation is (a+b) cosh(t)sinh(t)=0. Any nonzero
rapidity therefore requires b=−a, so G=a diag(1,−1,−1,−1). If G is positive
semidefinite, a≥0 and−a≥0 imply **G=0**.

An even shorter positive-definite obstruction uses one nontrivial boost. It
has a real eigenvector v with eigenvalue e^t≠1. Invariance would imply

    vᵀGv=(Λv)ᵀG(Λv)=e^(2t) vᵀGv,

contradicting positive definiteness. A single boost can leave a positive
semidefinite form supported on transverse directions invariant; the stronger
zero statement above uses the whole Lorentz group.

**Scope:** this prohibits a nonzero fixed positive-semidefinite quadratic norm
of a Lorentz four-vector. It does not prohibit positive physical energies,
Lorentz-covariant quantum field theories, unitary representations on their full
state spaces, or observer-dependent positive forms. Nor does it prove that the
four primitive comparison operators form a physical Lorentz four-vector.

For a concrete rational example, take

    B=[[5/4,3/4,0,0],[3/4,5/4,0,0],[0,0,1,0],[0,0,0,1]].

Then BᵀηB=η but (BᵀB)00=17/8 rather than1. Thus replacing a compact Euclidean
frame symmetry by physical Lorentz covariance cannot justify retaining the
same positive isotropic four-vector cost with a fixed inner product.

## The actual source matrices show why chirality cannot choose a rest frame

Let α=γ0γ1 from the source frame. It is Hermitian and α²=I. Define

    S=(3I−α)/(2 sqrt2),       S⁻¹=(3I+α)/(2 sqrt2).

Exact evaluation in the source four-dimensional representation gives

    S γ0 S⁻¹=(5/4)γ0+(3/4)γ1,
    S γ1 S⁻¹=(3/4)γ0+(5/4)γ1,
    S†γ0S=γ0,
    S†S=(5I−3α)/4 ≠ I,
    S a S⁻¹=a.

The ordinary positive spinor norm changes, with S†S eigenvalues1/2 and2,
each twice. The indefinite Dirac form and the anchor/chirality are preserved,
while the candidate time gamma changes. Hence **the anchor alone does not
remove boost freedom or pick a positive-energy time direction**. The full
marked source also contains f, but recognizing it as a matrix is not yet a
proof that it is a physical unit timelike field or the generator of evolution.

The finite spinor boost is nonunitary in its ordinary four-component norm.
This is not a violation of physical quantum unitarity: the full physical state
space, spacetime/momentum transformation, and appropriate adjoint/inner product
have not been constructed by this finite matrix calculation.

## A simple positive repair exists, but it explicitly needs an observer

There is no need for an elaborate algebraic workaround. Supply a unit timelike
vector u with uᵀηu=1 and define

    Q_u(x)=2(uᵀηx)²−xᵀηx,
    G_u=2ηu uᵀη−η.

In the rest frame u=(1,0,0,0), G_u=I, so this is a positive isotropic comparison
norm. Under simultaneous transformation of x and u,

    Q_(Λu)(Λx)=Q_u(x).

Thus positivity and covariance coexist for an **observer-indexed family**, not
as the same fixed Lorentz-scalar norm of x alone. For the rational B above,

    G_(Bu)=[[17/8,−15/8,0,0],[−15/8,17/8,0,0],
            [0,0,1,0],[0,0,0,1]],
    BᵀG_(Bu)B=I.

All these identities were checked exactly. The quadratic identity is useful
even without interpreting x as an existing TFPT field. If such a physical
interpretation is later supplied, energy similarly requires a time/observer
projection of four-momentum; positivity of the energy spectrum is not the same
requirement as a positive Lorentz-invariant quadratic four-vector norm.

**This is a conditional construction, not a selected TFPT solution.** The source
must still identify u (or an equivalent clock/state/foliation), the physical
vector/operator whose comparison is being measured, and their common update
law. Treating f as that u without a source-defined realization would just move
the missing implication into notation. The construction also does not prove
primitive J=K: the primitive anchor/family register is not this spacetime frame.

## Exact next acceptance gate

A proposed time mechanism must provide an operational identification of the
source f or another source object with u, specify how both comparison operators
and u transform, and show that the same dynamics preserves the resulting
positive inner product/energy conditions. Three things cannot substitute for
that test: chirality alone, compact internal Spin(4) isotropy, or the existence
of formal Lorentz gamma matrices. Equally, failure of a fixed Euclidean norm to
be Lorentz invariant is not grounds to reject an observer-indexed construction.

## Evidence and reproducibility boundary

The following original file hashes were verified in the preceding source audit;
the bridge hash was rechecked before evaluating its actual `generators` and
`frame` functions for this note:

    compiler-clifford-bridge/checker.py
      bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d
    verification/v774_arf_spinor_compiler.py
      3ef92c17d9f0de62212bab940ac2c017be866645d8a5b276bdcf2d92128bae8c
    verification/v975_dimension_selector_4d.py
      e9e31593b4a2eb4c15384f83a936aeee1474fcce5f2702a6df37147800407673

An ephemeral exact SymPy evaluation executed the source frame guards plus the
boost and observer identities:53 successful guards in total. This note is the
only new file for this subtask, not an additional persisted checker or an
integrated runner receipt. Its finite identities are explicit above; no
continuum or physical dynamical construction was tested.
