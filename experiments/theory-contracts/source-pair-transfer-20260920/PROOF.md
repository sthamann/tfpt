# Exact pair response and its state/time limit

**UR.SOURCE.PAIR_TRANSFER.01 — PARTIAL — 20 September 2026**

## Question, fixed premises and decision

The previous contract identified the native W in the local products of
64 odd composite fields and recovered its dark exterior-square directions
in second-order product coefficients. Does the actual source response now
derive the native attractive interaction, rather than merely resembling
its tensor?

We answer using the complete response, without selecting a new oscillator,
mediator, coupling or energy matrix. The fixed premises are the existing
Gamma=I_(9,1) compact boundary, the F(E8) embedding, its already selected
massless Vaux, the lattice vacuum and inherited cocycle. These are still
conditional boundary data; their origin from P1/P2 or the single-channel
QWZ source has NOT been derived. Full P1 is not reduced to its sign data.

The source time here is the conformal cylinder time of that assigned
Gaussian theory, in the existing dimensionless normalization, with the
previous quarter-charge term retained when indicated. It is not a new
identification of conformal scale, inverse temperature and native clocks.
The vacuum functional is held fixed throughout; no physical vacuum
selection is inferred from this calculation.

The result is constructive: an exact matrix-valued pair response, a
canonical polar state embedding, and a controlled collision limit that
intertwines the SAME assigned real and Euclidean time. But its connected
pair energy is a nonnegative dark-channel penalty, whereas the original
native mediator Hamiltonian has negative bright-channel binding. Dropping
a mandatory pair-energy offset would conceal this distinction.

## 1. Actual source fields and the complete pair state

Keep the notation and simultaneous native basis phases from
UR.SOURCE.DRESSED_NATIVE.01:

    K=diag(1^9,-1), a=(1,1,1,-1,-1,-1,-1,-1),
    e_R=-e9, m=(a,0,3), Vaux=K+2 K m m^T K,
    F(r)=(r-(a.r)a/2,0,-a.r),
    p_i=F(FW_i/2)+e_R, i=1,...,64.

All p_i lie in the positive right-moving E8+Z e_R sublattice at Vaux,
with p_i^2=3. The left-moving spectator is in its vacuum. Thus the
calculation uses a positive chiral Heisenberg Fock space, not an indefinite
chiral VOA of the entire Lorentzian lattice.

Psi_i is the rephased lattice vertex of p_i, of weight3/2. The 2016
native pair labels span E=Lambda^2 C^64 with their ORIGINAL orthonormal
CAR bookkeeping basis. They are not assumed to be source CAR operators.
For real 0<r<1 define an actual source state map

    J_r(e_i wedge e_j)
       = [Psi_i(r)Psi_j(0)-Psi_j(r)Psi_i(0)]|Omega>/2.   (1)

The antisymmetrization is essential for the original G=Spin10 x SU4
action. Each state in (1) has finite norm. The parameter r specifies the
radial separation of these two field insertions in the chosen unit disk;
it is not a fitted coupling or a new physical scale selected by P1.

The vertex expansion, in dual oscillator coordinates, is

    Psi_i(r)Psi_j(0)|Omega>
      = eta_ij r^lambda exp[sum_(n>=1) r^n p_i.a_-n/n]
          |p_i+p_j>,       lambda=p_i.p_j.             (2)

The vacuum oscillator relation [a_n(u),a_-n(v)]=n(u.v) implies

    <exp(E_u(r)) | exp(E_v(s))> = (1-rs)^(-u.v).      (3)

This follows by summing sum_(n>=1)(rs)^n/n=-log(1-rs), not by truncating
the oscillator tower. The underlying lattice OPE and cocycle framework
is standard; see Anagiannis et al., Appendix B,
[arXiv:2009.00186](https://arxiv.org/pdf/2009.00186). The concrete native
weights, phases, response reduction and interpretation are checked here.

## 2. The entire response reduces to I and W^dagger W

Write A=W^dagger W, so A^2=8A, rank A=60. Put v=rs. For pair labels
c=(i,j), d=(k,l) with equal total momentum, their exact Gram entry is

    eta_c eta_d v^lambda/4 * [
      (1-v)^(-p_i.p_k) + (-1)^lambda (1-v)^(-p_i.p_l)
      + (-1)^lambda (1-v)^(-p_j.p_k) + (1-v)^(-p_j.p_l)]. (4)

Different total momenta are orthogonal. The native arrays give 996 momentum
fibers, containing 6816 matrix cells in just nine distinct sign/exponent
types. Substitution in (4), including every nonzero W sign, yields the
FULL rational-function identity

    J_r^dagger J_s = G(rs) = d(rs) I + o(rs) A,

    d(v)=v^2(2-v)/[2(1-v)^3],
    o(v)=(2-v)/[2(1-v)^2].                            (5)

All other matrix cells are zero on both sides by actual momentum
orthogonality. The checker verifies the rational identities for all nine
types and their full census, not a finite sampling of v. This identifies
the native invariant A throughout the response, not only at coincidence.

Let J_r=sum_(n>=0) r^n C_n. Distinct C_n images have cylinder energies
3+n and are orthogonal. From (5),

    C_n^dagger C_n = d_n I + o_n A,
    o_n=(n+2)/2 for n>=0,
    d_0=0, d_n=(n-1)(n+2)/4 for n>=1.                (6)

The coefficient formula follows from differential identities applied to
1/(1-v), proved by the checker. Thus all infinitely many coefficients
are determined analytically. In particular C0^dagger C0=A,
C1^dagger C1=3A/2, and C2^dagger C2=I+2A.

Define Pb=A/8 and Pd=I-Pb. The bright and dark response eigenvalues are

    gb(v)=d(v)+8o(v),       gd(v)=d(v).               (7)

They have positive spectral weights at every grade n>=0 and n>=2,
respectively. This provides the complete positive pair spectral measure
of this particular vacuum response. It does not specify the whole QFT
or a physical many-particle vacuum.

## 3. Finite separation: exact compressed evolution, not a closed Hamiltonian

Set rho=r^2. Since d(rho)>0, G(rho) is positive definite. The polar map

    U_r=J_r G(rho)^(-1/2)                             (8)

is an isometry from the native pair bookkeeping space into the actual
source Hilbert space. This normalization is fixed by the source Gram;
no independent normalization per temporal measurement is performed.
The native reference here is its specified empty-Fock N=2 pair sector.
It is not the interacting native ground state in N=64. No identification
of that true native ground state with the source vacuum is assumed.

For H0=L0 on this right-moving sector, C_n has energy3+n. Therefore

    T_r(tau)=U_r^dagger exp(-tau H0) U_r
      = exp(-3tau) G(rho exp(-tau)) G(rho)^(-1).      (9)

Equations (7),(9) give both response channels for every tau>=0. Real-time
compression follows by tau=it, because rho<1 ensures absolute convergence
of the same spectral series.

At finite r the range of U_r is not H0-invariant. Its initial mean energy
is M_r=3I+rho G'(rho)G(rho)^(-1), with

    h_d=5-rho/(2-rho)+3rho/(1-rho),
    M_r=h_d I-kappa(rho) A,
    kappa(rho)=(2-rho)/(rho^2-8rho+8).                (10)

But exp(-tau M_r) is NOT (9). On each channel, the compression defect at
second order is the strictly positive variance

    T_r''(0)-T_r'(0)^2
      = U_r^dagger H0 (I-U_r U_r^dagger) H0 U_r.      (11)

Strict positivity follows from the multiple positive spectral weights in
(6). At rho=1/2 the dark and bright variances are 50/9 and 10850/2601.
For the concrete tau=log2 control,

    T_b(2tau)-T_b(tau)^2=46131751/20811911904 >0,
    T_d(2tau)-T_d(tau)^2=7999/72013536 >0.

At real time t=pi, the same two normalized amplitudes are -245/1377 and
-5/81, of modulus less than one. The compressed response is not unitary
on E even though its full source evolution is unitary. Treating (10) as
its exact autonomous Hamiltonian would discard the rest of the source.

The measure has infinitely many positive energy poles. A finite native
N=2 bright two-level block cannot reproduce it exactly at finite rho.
This is a spectral-support statement, not a numerical fit failure. It
does not rule out a controlled approximation or an infinite extension.

## 4. A controlled state AND time limit exists

The collision limit of (8) is not obtained by merely throwing away dark
states. Their source normalization diverges as 1/rho and retains C2:

    U_0 = C0 Pb/sqrt8 + C2 Pd,
    U_0^dagger U_0=I.                                (12)

The isometry follows from (6) and orthogonality of grades3 and5. Its range
IS invariant under H0, and

    H0 U_0 = U_0 (3Pb+5Pd),
    H_pair,0 =3Pb+5Pd=5I-A/4.                        (13)

This is a derived state/time map in the existing assigned boundary theory.
It is no longer only a dimension or an operator-tensor match. It is also
not a map preserving creation products or the full native CAR/CCR algebra.
For example the old coincident pair/mediator Gram defect still holds.

The limit has explicit control. The lowest-grade weights in the normalized
spectral measures are

    p_b=8/gb(rho),       p_d=rho^2/d(rho).

For every 0<rho<1,

    1-p_b <=3rho/2,       1-p_d <=5rho/2.             (14)

To verify these bounds without sampling, subtract the left sides from the
right sides. The respective remainders are

    rho^2(4-3rho^2)/[2(2-rho)(rho^2-8rho+8)],
    rho^2(7-4rho)/[2(2-rho)],

both positive on that interval. Summing the remaining positive spectral
weights gives the uniform bounds

    sup_(tau>=0) ||T_r(tau)-exp[-tau(3Pb+5Pd)]|| <=5rho/2,
    sup_(t in R) ||T_r(it)-exp[-it(3Pb+5Pd)]|| <=5rho. (15)

The real-time bound uses |exp(-int)-1|<=2. These are all-time bounds for
the specified pair response, not a claimed bound on the full field theory.
The state maps themselves satisfy
U_r^dagger U_0=sqrt(p_b)Pb+sqrt(p_d)Pd, hence
||U_r-U_0||<=sqrt(5rho). The divergent dark normalization therefore has
a controlled, finite isometric limit.

Retain the prior source quarter-charge term. Each momentum fiber has its
actual q_i+q_j, so Q2 commutes with A and is intertwined by every C_n.
The exact limiting generator becomes

    H_pair = 3I-Q2/4+2Pd.                            (16)

The finite-r response gains the corresponding exp(tau Q2/4) or unitary
exp(itQ2/4) factor. Real-time bound(15) is unchanged. The Euclidean bound
also holds here: bright q<=0 and dark q<=4, so both shifted lowest energies
remain nonnegative. These charge bounds are checked on all native pairs.

## 5. The absolute energy comparison rejects native attractive binding

The SAME source one-field states have energy3/2-q_i/4. Thus the additive
energy of a pair is 3-(q_i+q_j)/4. Subtracting this fixed one-particle
baseline from (16) yields

    V_connected,pair = 2Pd = 2I-A/4 >=0.             (17)

The bright channel has connected energy zero, and the dark channels +2.
At finite r the mean connected energies are positive on both channels;
this follows from the positive spectral weights above their lowest grades.
The term -A/4 in (13) is therefore not a negative binding energy relative
to the actual same-source one-particle states. Its accompanying +2I
in (17) is essential.

This is an effective operator on the reconstructed pair subspace of
composite source fields. It is not a newly generated microscopic
four-fermion interaction in the original Gaussian elementary source.
The distinction between composite response and elementary dynamics from
UR.SOURCE.DYNAMICS_SELECTION.01 is preserved.

The unchanged native Hamiltonian is

    H_nat=Delta N_b+g_c sum_A(b_A^dagger P_A+P_A^dagger b_A),
    P_A=sum_(i<j) W_(A,ij) f_j f_i, with NO mu N.

Using its own fixed vacuum/one-fermion zero, each normalized bright pair
and independent mediator form the exact block

    [[0,sqrt8 g_c],[sqrt8 g_c,Delta]],
    E_-=(Delta-sqrt(Delta^2+32 g_c^2))/2 <0 for g_c!=0. (18)

Its determinant is -8g_c^2. At the original test ratio Delta=1,g_c=1/20,
E_-=(5-3sqrt3)/10. The source value in the bright channel of (17) is zero,
not this negative value. Aligning the separately displayed one-particle
charge/energy baseline does not alter that connected-energy discrepancy.
No change to the native Hamiltonian or its theorem is made here.
This comparison concerns the indicated empty-reference N=2 sector. It
is not a calculation of charged spectra around the true native N=64
ground state, and does not rule out a different demonstrated vacuum/GNS
map. That map has not been supplied by the present construction.

One could make only the N=2 energy GAP look attractive by subtracting
2I from (17). That subtraction is not a permissible global calibration:
an affine shift c+mu N keeping N=0 and N=1 fixed forces c=mu=0. Changing
N=2 alone adds new occupation-dependent dynamics. Consequently (13) does
not derive the native vacuum theorem, a physical attractive interaction,
or many-body mass generation. The prior exact CAR/product obstruction
also remains in force.
More generally, E_ij-E_i-E_j+E_vac is invariant under c+mu N if the same
four reference states are retained. A new mu term that changes which
state is the ground state is a change of dynamics/state selection, not
an innocuous remedy for this comparison.

## 6. Correlation with the sector-reconstruction lane

The new UR.SOURCE.SECTOR_RECONSTRUCTION.01 was read in full and its
32-control algebra checker reproduced byte for byte. It reconstructs
Gamma charged intertwiners with the same assigned H from four explicit
even-lattice sectors and a spin-sensitive trace combination. It does not
select H or the state functional.

Here each odd Psi passes through the odd sector; its pair has even Gamma
parity and its four-field Gram is an even overall response. Retaining the
same intertwiners, vacuum/state preparation and H in both descriptions
preserves (4)--(18). The change of sector description cannot turn zero
connected bright energy into negative binding. A different state or a
different source Hamiltonian would be additional physical input.

The two lanes therefore give compatible constructive advances: one
retains the charged fields and their assigned time; this one determines
their complete pair response and a controlled state/time embedding.
Neither replaces the outstanding derivation of the actual source energy,
charged channels and physical vacuum from the original principles.

## Decision and first remaining source test

The original question has a definite scoped answer. W governs the entire
pair response of this conditional boundary. A same-time finite pair
embedding exists with a quantitative error bound. Its source-connected
energy is NOT the attractive energy of the native Hamiltonian.

Any proposed common physical origin must now supply an actual source
operator/state mechanism that gives the required connected pair energy
while keeping the vacuum, one-particle calibration, charges and field
products consistent. Inserting another mediator, choosing Vaux by hand,
or subtracting a pair-only constant would assume the missing mechanism.
No spectra are optimized after this failed identification.

The source-derived ten channels, Vaux, native full Fock algebra, common
3+1D dynamics, flavor/alpha/gravity transfers and physical vacuum remain
open. No T1-T8 gate, paper, ledger or empirical scorecard is promoted.
Normal and optimized exact checkers agree; no independent agent review
or formal proof-assistant verification is claimed for this contract.
