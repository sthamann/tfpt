# Four-generator noise: exact recovery with a record, not yet a physical origin

2026-09-12. NON-RH. Applies to the explicitly stipulated independent-Poisson
four-generator model, not arbitrary TFPT or arbitrary coherent path histories.

## 1. Source algebra and compression of the event history

The checker reconstructs the original four Clifford generators from the
source-pinned frame used in [FOUR_PRIMITIVE_PROCESS.md](FOUR_PRIMITIVE_PROCESS.md).
For v in {0,1}^4 put U_v=g_1^v1 ... g_4^v4 in that fixed order. The original
ordered cocycle gives

    U_v U_w = (-1)^c(v,w) U_(v xor w).

All 256 products are checked using the source's own cocycle function.
The central sign disappears in conjugation U rho U†. Consequently, for the
CLASSICAL random event histories stipulated here, the four event-count
parities suffice to label the final system operation. The length or detailed
order of the event list is unnecessary for correcting that final operation.

These are the same sixteen binary word labels as the algebraic compiler
register, not a newly invented set of labels. This is not an identification
of that register with a physically accessible memory. The latter remains an
additional realization obligation. For coherently superposed alternative
histories, relative cocycle phases can matter; parity alone is not declared
a sufficient description of arbitrary coherent path amplitudes.

## 2. Exact finite-time channel

For rates r=(c,c,c,e), let z_i=exp(-2 r_i t). Independent Poisson counts have
odd probability (1-z_i)/2, hence

    p_v(t)= product_i [(1+z_i)/2 if v_i=0 else (1-z_i)/2],
    E_t(rho)=sum_v p_v(t) U_v rho U_v†.

The independent Bernoulli parity distribution is a consequence of the
assumed Poisson process, NOT of the Clifford multiplication relations alone.
The checker verifies normalization and the full channel eigenvalue formula
symbolically for four independent z_i, so the comparison is not one fitted time.

For any finite t>0 and c,e>0 every p_v>0. The sixteen U_v are Hilbert–Schmidt
orthogonal: Tr(U_v† U_w)=4 delta_vw. The Choi eigenvalues are therefore 4 p_v,
and its rank is sixteen. A minimal pure-environment Stinespring representation
of THIS channel has dimension sixteen; this is not a general bound on all
possible mixed-environment implementations or the original compiler's size.

## 3. Complete correction with the additional record

Keep the channel output together with the classical label v:

    F_t(rho)=sum_v p_v |v><v| tensor U_v rho U_v†.

Apply U_v† to the system conditionally on v and discard the label. The result
is exactly rho. Linearity makes this identity valid also for inputs entangled
with an arbitrary reference. No postselection or knowledge of rho is needed.

Equivalently, use the fixed-time isometry

    W_t |psi> = sum_v sqrt(p_v) |v> tensor U_v |psi>.

The controlled inverse C=sum_v |v><v| tensor U_v† satisfies

    C W_t |psi> = (sum_v sqrt(p_v)|v>) tensor |psi>.

This is a standard environment-assisted correction mechanism, specialized to
the source words; it is not a new general theorem:
[Gregoratti–Werner, Quantum Lost and Found](https://arxiv.org/abs/quant-ph/0209025).

Each record effect is p_v U_v†U_v=p_v I, so the classical record probabilities
are independent of the input state. The label alone does NOT encode or
reconstruct the quantum message. Output system PLUS label permit correction.
This is not holographic reconstruction of the whole input from the label alone.
The coherent environment may carry additional information in off-diagonal
entries; it must not be confused with its measured classical labels.

No source-derived record carrier, controlled correction, reset process or
access protocol is claimed. Existing algebraic labels do not establish these
physical resources. Four bits describe the sixteen labels at one endpoint;
this does not provide a four-bit autonomous bath for arbitrarily many uses.

## 4. Without the record, invertibility is not physical reversibility

At finite time every channel eigenvalue is nonzero, so E_t has a LINEAR
inverse on the sixteen-dimensional operator space. Its inverse is not in
general a positive quantum operation.

For f=g_1 g_2 g_3, the two states rho_±=(I±f)/4 have orthogonal supports and
trace distance one. The channel gives

    E_t(rho_±)=(I±exp(-2 e t)f)/4,
    D(E_t(rho_+),E_t(rho_-))=exp(-2 e t)<1.

A CPTP recovery on the system alone cannot increase trace distance back to
one. Equivalently, the formal inverse applied to rho_+ has eigenvalues
(1±exp(2 e t))/4 and is not positive. Full operator rank therefore does not
mean a physically executable inverse. The source involution and initial
purity-loss derivative are independently checked.

## 5. Why the fixed-time construction does not yet derive physical time

Suppose a finite environment starts in a fixed state sigma independently of
the arbitrary input rho, and one fixed bounded Hamiltonian H generates the
closed joint dynamics. Differentiating at zero gives

    d/dt Tr_E(exp(-itH)(rho tensor sigma)exp(itH)) at t=0
       = -i[H_eff,rho],
    H_eff=Tr_E[H(I tensor sigma)].

The first-order reduced evolution is Hamiltonian; its purity derivative is
zero for every rho by cyclicity of trace. Our unit-rate four-generator
candidate instead has d/dt Tr(E_t(rho_+)^2) at zero equal to -1.
For general e the value is -e. This rules out that particular exact finite,
fixed-Hamiltonian, product-initial-state realization for all times.

This does NOT rule out a dilation at each fixed time, collision models with
fresh environments, approximations, time-dependent singular couplings,
infinite reservoirs or restricted preparations. Each changes the physical
premises and must be derived if used. In W_t the one-event amplitudes begin
as sqrt(r_i t), illustrating why writing down W_t is not already a regular
autonomous microscopic Hamiltonian.

## 6. What has advanced

The candidate now has a complete forward channel, an exact record-assisted
inverse, an explicit no-record obstruction and a microscopic-onset test.
The disappearance of system information need not mean its destruction in an
enlarged model. But the enlarged model has physical resource requirements,
and the random process still needs its own origin.

The fundamental question becomes precise: Does the actual compiler supply
a physical carrier of these operation records and a joint dynamical law, or
does it merely supply the word algebra? Adding a record by hand resolves the
conditional information problem, not the source-realization problem.

## Verification

`primitive_record_recovery.py`: 340 exact checks per normal/-OO run,
byte-identical outputs. Pins include the previous source helper
`1c853b49041aaa61e772ad331e22d9e5400c3192c81d69fead873396db6a9109`,
the original frame and its eight upstream file hashes. It checks all word
products, symbolic parity-channel eigenvalues, a 64x4 isometry and controlled
inverse at a rational interior point, rank-sixteen Choi matrix and the source
purity-loss witness. General time and recovery statements follow from the
written formulas, not from a finite sampling claim. No T1–T8 closure, paper
promotion, commit, push or external export.
