# Round23: an exact locality test of the Round22 translation completion

2026-09-07. NON-RH. The target is the actual changed full parent X_av
of [Round22](../translation-completion-round22/PROOF.md), not every
possible TFPT Hamiltonian. Fix odd L>=5, N=L^3, a=1 unless restored below,
m>0 and lambda>0. All integer charges and all 35 continuous species remain.

## 1. Local neutral measurements and a free translation orbit

Put h=(L-1)/2, x=(0,0,0), y=(0,h,0), p=e2 with e(p)=e(-p)=1.
Let n have p at x, -p at y and zero elsewhere, and n'=T_c,1 n.
The N spatial translates of n are distinct (the location of +p fixes
the translation). Their span is an invariant subspace of translations
and diagonal charge energies, NOT of the full hopping Hamiltonian.
Using it for matrix elements does not truncate the physical model.

Let A_x and B_y be the ON-SITE spectral projectors onto n_x=p and
n_y=-p. They are bounded norm-one, neutral under all total charges, and
belong to the original local observable net. Both are one on n and zero
on n'. For any operator O on the common finite-charge/Schwartz core,

    <n'|[[O,A_x],B_y]|n>=<n'|O|n>.                  (1)

The supports are separated by h lattice steps. For the original X the
double commutator is ZERO: the diagonal charge terms commute with both
projectors, continuous-only terms do too, and no nearest-neighbor hop
contains both sites. This statement uses the full hopping inventory.

## 2. The conserved global momentum has no uniformly local density

The charge component in Round22 is the signed logarithm of translation.
For z=exp(2pi i/L), its one-axis group-algebra coefficients are

    K_c,1=sum_(r=1)^(L-1) c_r T_c,1^r,
    c_r=(1/L)sum_(k=-h)^h k z^(kr)
        =z^(-hr)/(z^r-1)
        =-i(-1)^r/[2 sin(pi r/L)].                 (2)

The identity follows by shifting the finite geometric sum; c_0=0 and
c_(L-r)=conjugate(c_r). No numerical logarithm or branch fitting is used.
Equation (1) applied to P_1=2pi(K_cont,1+K_c,1)/(La) gives

    |<n'|[[P_1,A_x],B_y]|n>|=pi/[La sin(pi/L)]>=1/a. (3)

The continuous part commutes with the charge projectors. Thus the fixed
conserved momentum cannot be a sum of densities of volume-independent
finite support diameter. More generally it cannot have a local-density
representation whose double-commutator tails vanish uniformly with this
separation. This is a statement about this generator and the original net;
it is not a classification of all possible conserved momenta.

## 3. The Hamiltonian itself also has a nonlocal term

This is stronger than finding a nonlocal symmetry generator. Take scalar
one-quantum states q=(1,0,0), r=(0,0,0), with

    omega_q=sqrt(m^2+4 sin(pi/L)^2), omega_r=m.

The exact untruncated oscillator matrix element of the original coupling is

    <r|V_1|q>=F_1/[N^2 sqrt(omega_q omega_r)],
    F_1=sum_s exp(2pi i s_1/L)e(n_s).                (4)

On the full translation orbit above, F_1|v>=2 z^(v_1)|v>.
In its N-character basis F_1 sends |k> to 2|k+e1 mod L>.
The Round22 torus average retains the scalar transition q->r only if
the charge increment is the SIGNED +e1. It therefore removes exactly
the wrap k_1=h -> l_1=-h, retaining all other k_1 and all k_2,k_3:

    F_1,av=F_1-2 sum_(k_2,k_3)|-h,k_2,k_3><h,k_2,k_3|.

The original F_1 is diagonal in position configurations. Transforming the
removed plane back to that basis gives the exact off-diagonal coefficient

    <n'|F_1,av|n>=-(2/L)z^(-h).                    (5)

Neither a finite scalar Hilbert space nor omission of other charge
configurations is used. Consequently, with any common normalized Schwartz
state in the other continuous factors,

    |<n',r|[[X_av,A_x],B_y]|n,q>|
        =2 lambda/[L N^2 sqrt(omega_q m)] > 0.       (6)

All other contributions vanish in this double commutator: D and hopping
are unchanged by averaging; the remaining averaged parent terms act only
on continuous fields. In particular this witness is not cancelled by the
gravity/auxiliary squares, by a cocycle or by the retained 48NJ constant.

These vectors and their A/B images belong to the new operator's domain:
they lie in the invariant polynomial/finite-charge core, on which the
finite sum-of-squares expression represents its Friedrichs realization.
Thus the corresponding matrix element of [exp(itX_av)A_x exp(-itX_av),B_y]
has the nonzero first derivative i times (6). This is an actual weak
dynamical locality failure, not only a rewritten vertex.

## 4. Precisely which propagation claim fails

At fixed a=1, lambda,m>0, (6) is bounded below by

    2 lambda/[L^7 sqrt(m sqrt(m^2+4))].              (7)

No C,v,mu>0 independent of L can therefore give the usual exponential
bound C exp(-mu d)(exp(v|t|)-1) for these norm-one local observables:
differentiate its matrix-element consequence at t=0 and use d=h.
An inverse seventh power cannot be bounded by a fixed exponential in h
for all odd L. In particular X_av has no uniformly finite-range
interaction representation on the original local net.

The claim excluded here is that SPECIFIC volume-uniform, small-time
exponential locality estimate. Power-law bounds, state-dependent bounds,
different observable nets and a renormalized continuum are not ruled out.
The finite-regulator failure is not by itself a theorem about relativistic
continuum causality. See the [low-momentum/dynamics contract](../soft-sector-round23/PROOF.md)
for a restricted positive comparison bound rather than such an inference.

For background, [Nachtergaele-Sims-Young](https://arxiv.org/abs/1810.02428)
discuss quasi-locality including unbounded on-site terms;
[Wilming-Werner](https://arxiv.org/abs/2006.10062) give a converse for their
k-body setting. Their hypotheses are not silently transferred to X_av.
Our conclusion follows directly from (6), not from invoking that converse
for an unbounded, volume-global Hamiltonian.

## Scope

The finite translation representation, full E8 energy, exact oscillator
coefficient and double commutator are checked algebraically. General-L
statements follow from the displayed geometric sum, support and domain
arguments, not from the finite test list. Round22 positivity and global
conservation remain valid; its local relativistic stress interpretation
is now explicitly excluded on the stated net. No T1-T8/TOE/RH promotion.
