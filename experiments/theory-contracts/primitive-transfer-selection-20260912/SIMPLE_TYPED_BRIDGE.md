# Simpler bridge: response, generator, and operations

2026-09-12. NON-RH, unpromoted. Independent parallel audit plus direct proofs.
This corrects the research priority, not the valid scoped domain obstructions.

## 1. The free identification needs no added coupling

On l2(Z), E|n>=n|n>, U|n>=|n+1>. The Fourier unitary F|n>=exp(in theta)
to L2(S1,dtheta/2pi) gives FEF*=D=-i d/dtheta and FUF*=multiplication by
exp(i theta). It preserves the quarter rotation exp(i pi E/2) exactly.
Set K=D^2. Harmonic extension into the unit disk is

    u(r,theta)=sum_n f_n r^|n| exp(in theta).
    Lambda f = partial_r u(1,theta) = |D|f = sqrt(K)f.

The identity is spectral, for every mode, with operator domains H1 for
Lambda and H2 for K; their form domains are H^(1/2) and H1 respectively.
For a declared electric Hamiltonian cE^2, Lambda=c^(-1/2)sqrt(F H_el F*).
This does NOT derive c or identify the extension coordinate with physical time.
The disk geometry and units are explicit hypotheses, not a derived TFPT bulk.

Classical reference: Girouard--Polterovich, *Spectral geometry of the Steklov
problem*, sections 1.2--1.3, https://arxiv.org/html/1411.6567 . Finite cylinders
have length/boundary-condition dependent responses; the disk formula is not
automatically the response of the actual TFPT collar.

## 2. The lost sign can be recovered from operations, not eigenvalues alone

On trigonometric polynomials, with the specified oriented shift U,

    U* K U - K = 2D + I,
    D = (U* K U - K - I)/2.

Proof: both sides act on exp(in theta) by (n+1)^2-n^2=2n+1.
The difference on this core has the unique self-adjoint closure 2D+I.
Thus the pair (Lambda,U), with K=Lambda^2, recovers signed D; Lambda alone
cannot distinguish +n from -n. Replacing U by U* changes the orientation.
This does not derive a preferred orientation, but shows why discarding the
operation algebra and retaining only a spectrum creates an artificial loss.
No new state space or adjustable coupling is required for this identity.
U is a single-rotor operation; on a constrained lattice an open-link shift
need not preserve Gauss. A gauge-physical dictionary still has to be supplied.

## 3. Why smoothing is not a physical identification

At depth s=-log r>0, P_s=exp(-s|D|) sends L2 into every Hm, since
sup_n |n|^m exp(-s|n|) is finite. It is nonunitary and

    (P_s U-U P_s)e_n=(exp(-s|n+1|)-exp(-s|n|))e_(n+1).

Consequently smoothing a rough collar vector does not furnish an
operation-preserving physical map. Indeed an isometry J preserving E and U
between these simple rotor/circle representations satisfies J|n>=a_n e_n,
|a_n|=1 and a_(n+1)=a_n: it is F up to one global phase.

The infinite E^2 expectation in ELECTRIC_DOMAIN.md therefore remains true
for the renormalized vector under that literal state map. It does not prove
that a boundary response must itself be the physical Hamiltonian, or that
every boundary datum must be an admissible finite-electric-energy state.

## 4. Source audit and minimal next gate

- verification/v331_necessity_of_H.py, dtn: inserts |D| plus four point-mark
  Fourier couplings. The function does not construct a bulk elliptic problem
  proving that the full expression is its actual Dirichlet-to-Neumann map.
- experiments/theory-contracts/parent-selection-audit/README.md, section 1:
  dynamical compact rotors and electric coefficients are declared extensions,
  not a derived seam-to-4D dictionary.
- The native parent contains matter and multiple links. The free one-rotor
  square-root identity is not an identity for that full interacting parent.

Do not silently square |D| plus a singular point term: its raw form was shown
nonclosable in COLLAR_LIMIT.md. A renormalized self-adjoint operator can be
squared by spectral calculus, but that does not establish the native local
Hamiltonian or physical state selection.

Priority: derive a concrete TFPT elliptic boundary problem and the marked
operation U (or gauge-physical replacement), then compute its response and
test the operator dictionary. First decide whether four marks are observation
labels, boundary conditions, or actual interactions. These are different
models. Do not add another free repair parameter before this distinction.

Scope: an exact free-sector structural relation and a clearer missing premise.
No unique interacting parent, selected vacuum, 3+1D emergence or T1--T8 closure.
No RH, factoring, P versus NP, or Hylæan capability implication follows.
