# Round24: finite scalar AND charge density with an explicit comparison bound

2026-09-07. NON-RH. Work on the actual g=nu=0 common parent (g is the
gravity coupling), odd L>=3, N=L^3, m>0. Keep every integer E8 charge and
all continuous species. Introduce the DECLARED scaling lambda_N=N u,
u>=0. This is a choice of coupling path, not a microscopic TFPT prediction.

## 1. Uniform charge shift and a controlled neutral fluctuation ground state

Fix p=e2, e_p=e(p)=1, and the exact unitary S_p=product_x T_x,p using the
original cocycle. On the neutral fluctuation sector sum_x n_x=0,

    S_p* D_phys S_p = e_p + D, D=(1/N)sum_x e(n_x),
    S_p* H_hop S_p = H_hop.                          (1)

The second identity retains the full projective phases: conjugation of
each on-site shift contributes (-1)^(p^T G r), and the two endpoints of
every neutral hop cancel that sign. Translation also commutes with S_p.
The physical total charge after this unitary is Np, not one dilute root.

In the neutral sector D has a UNIQUE zero vector Omega (all charges zero)
and exact next gap Delta=2/N. Any other neutral profile has at least two
nonzero sites, each of integer energy at least one. A root/negative-root
pair attains the gap. Write H_c=D+48NJ+JK, ||K||<=b=48N, and set

    eps=Jb/Delta=24N^2J<=1/32, J>0.

The same elementary contour argument as Round22 gives a unique analytic
lowest vector chi_J with positive overlap with Omega. It has translation
character zero. If Q=I-|Omega><Omega| and eta=2eps/(1-2eps), then

    ||Q chi_J||<=eta,
    ||E chi_J||<=4eps, E=N D,
    <E>_chi <= 2eps(2eta+eta^2).                     (2)

For the last two estimates use H_tilde=D+JK, its ground eigenvalue
epsilon_0 in [-Jb,0], and <Omega|K|Omega>=0. Thus ||D chi||<=2Jb and
<D>=epsilon_0-J<K><=Jb(2eta+eta^2). This controls the energy mean to
SECOND order, not merely by the first-order graph bound. At eps=1/32,
||E chi||<=1/8 and <E><=31/3600. The L5 endpoint is J=1/12000000.
The physical hopping constant 48NJ and background energy e_p remain.

## 2. Resum the finite background instead of estimating it as a small error

In shifted variables,

    e(n_x+p)=e_p+p^T G n_x+e(n_x),
    a_x=p^T G n_x+e(n_x), sum_x a_x=E.

The scalar part of the original Hamiltonian is EXACTLY

    H_m(m)+u sum_x e(n_x+p)phi_x^2
       =H_m(m_*)+W, m_*^2=m^2+2u e_p,
    W=u sum_x a_x phi_x^2.                          (3)

No normal ordering or vacuum-energy subtraction is made. The finite
mass shift is already in the original interaction on this chosen path.
W is not positive, but the ORIGINAL Hamiltonian and its torus average
are positive with their retained lower bounds. Neither is replaced by W.

Take psi=(S_p chi_J) tensor |M_0;m_*>: M quanta in the scalar zero mode,
with ALL other scalar modes in their physical m_* vacuum. M/N may tend
to any fixed finite density. No Fock truncation is imposed on evolution.
Other free continuous factors remain, without a chosen auxiliary vacuum.
The reference H_ref=H_c,phys+H_m(m_*) has psi as a charge/scalar eigenstate.
The physical charge density is p, and the scalar excitation density is M/N.

## 3. Exact high-mode covariance and a volume-controlled residual

Write phi_x=X_0/sqrt(N)+xi_x. In the stated number state and hard vacuum,

    z=<X_0^2>/N=(2M+1)/(2N m_*),
    w=<X_0^4>/N^2=(6M^2+6M+3)/(4N^2 m_*^2),
    C_H(x,y)=<xi_x xi_y>, c_H=C_H(x,x)<=1/(2m_*).

C_H has precisely the nonzero Fourier modes, is positive, and has norm
at most 1/(2m_*). Parseval gives sum_y C_H(x,y)^2<=1/(4m_*^2).
Wick's rule and the full number-state ladder algebra give, for each REAL
coefficient profile a (its entries may be negative),

    ||sum_x a_x phi_x^2 |M_0,vac_H>||^2
      =(w+2z c_H+c_H^2)(sum a)^2
          +4z a^T C_H a+2 a^T(C_H Hadamard C_H)a.    (4)

This includes the hard vacuum and its pair fluctuations. Define

    A=w+z/m_*+1/(4m_*^2),
    B=2z/m_*+1/(2m_*^2).

The Schur-product covariance in (4) has norm at most 1/(4m_*^2).
Also (p^T G n_x)^2<=4e_p e(n_x), hence
sum a_x^2<=2E^2+8e_p E. Applying (2) fiber by fiber proves

    ||W psi|| <= R_N,
    R_N^2=u^2[(A+2B)(4eps)^2
                  +8e_p B*2eps(2eta+eta^2)].        (5)

At fixed scalar density M/N, A and B are uniformly bounded; R_N=O(u eps),
independent of volume. Replacing <E> by an uncontrolled extensive charge
count, or dropping the hard Gaussian contractions, would lose this result.

## 4. Actual dynamics and positive clock, including arbitrary free spectators

The charge/scalar input is an eigenstate of H_ref and has signed K=0.
The averaged residual therefore acts as E_(K=0) W psi and has norm <=R_N.
The preparation subspace consisting of this one charge/scalar vector
tensored with the ENTIRE free-spectator Hilbert space is invariant under
H_ref. The two residual operators are bounded by R_N on that subspace.
Finite D-graph cutoffs and full oscillator moments supply the interacting
operator domains, as in Round23. No interacting-subspace invariance is used.

Duhamel along the reference orbit yields for every real t

    ||(exp(-itH_original)-exp(-itH_ref)) psi||<=min(2,|t|R_N),
    ||(exp(-itH_original)-exp(-itH_averaged)) psi||<=min(2,2|t|R_N).

These bounds are uniform over normalized free-spectator data. If gamma>0
is a retained common positive lower bound for all three bases, the
restricted square-root resolvent argument of Round23 gives the clock bound

    ||(exp(-i tau sqrt(12H_original))
          -exp(-i tau sqrt(12H_averaged))) psi||
        <=min(2,2|tau|sqrt(3/gamma)R_N).             (6)

It uses the common canonical positive-frequency initial-data chart, not
an identification of old source/Gaussian wavefunction encodings. No
state-dependent energy subtraction is allowed in gamma.

## What this does and does not close

This is a finite-CHARGE-density and finite-SCALAR-density comparison for
a SPECIFIED uniform background/zero-mode number preparation, with finite
mass shift and explicitly bounded full dynamics. The actual hopping is
positive and retained, but its sufficient window still scales as N^-2.
Making eps tend to zero freezes charge fluctuations and leaves a massive
Gaussian scalar reference. That is not a nontrivial interacting TOE limit.
Arbitrary inhomogeneous finite-density states, fixed J in the large-volume
limit, full gravity, chiral matter and local relativistic stress remain open.

The companion [local elimination](../local-gaussian-elimination-round24/PROOF.md)
keeps original spatial locality when eliminating scalar cell interiors;
it is distinct from the nonlocal torus averaging tested in Round23.
No T1-T8/TOE/RH or empirical promotion.
