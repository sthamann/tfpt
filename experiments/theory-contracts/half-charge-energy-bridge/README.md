# Half-charge energy bridge after publication

9 September 2026, **local follow-up after published commit `66b91e40`**.
This is an exact conditional target calculation connected to the newly
proved source charge energies. It does not construct eight microscopic
channels, a half-charge field, a selected Hamiltonian, or close T1–T8.

## Result

The source holonomy need not be erased in order to use conformal energy
bounds. On the stated E8 target its shifted generator and the standard
conformal generator have the **same polynomial energy domains**. This is a
useful positive bridge for the next smeared-field construction. They are
nevertheless different Hamiltonians: copying the same quarter-holonomy to
all eight channels produces **two** ground states after the spinor extension.
A mere relabeling as the usual conformal generator would be incorrect.

## 1. Separate the proved source from the extension hypothesis

The pinned source in `microscopic-charged-car-limit/checker.py` gives

    E_top(q) = q²/2 − q/4, q an integer.

It explicitly rejects half-integer q. Extending this to eight bosonized
channels and to the E8 lattice is an additional hypothesis, not an output
of that checker. The target lattice already fixed by `half-twist-grade-carry`
is `L=D8 ∪ (D8+s)`, `s=(1/2)^8`, where D8 has even integer coordinate sum.
On the target oscillator/charge basis introduce, explicitly conditionally,

    L0 = N_osc + |q|²/2,
    H_sigma = L0 − lambda_sigma·q,
    lambda_sigma = (sigma_1,...,sigma_8)/4, sigma_i in {−1,+1}.

The uniform choice sigma=(+1)^8 retains the known source offset in every
channel. Other sign patterns are comparison hypotheses; neither the eight
copies nor their relative signs have been selected by TFPT. Changing a
holonomy sign must not silently be identified with changing edge chirality.

## 2. Positivity and the exact ground-space distinction, on all charges

Every nonzero E8 lattice charge has `|q|²/2 >= 1`, and the latter is an
integer. Also `|lambda_sigma|²=1/2`. Therefore Cauchy–Schwarz gives

    |lambda_sigma·q| <= sqrt(|q|²/2),
    H_sigma >= N_osc + |q|²/2 − sqrt(|q|²/2) >= 0.

This proves positivity on the complete target charge/oscillator space,
not just the enumerated root shell. A zero-energy state must have
`N_osc=0`, and either q=0 or equality in both inequalities. For nonzero q,
equality forces `|q|²/2=1` and `q=2 lambda_sigma=sigma/2`.

Thus the kernel has dimension two exactly when sigma has an **even**
number of minus signs, because then sigma/2 belongs to L. For odd sign
parity, the kernel is the single charge vacuum q=0. For even parity the
affine charge reflection `q -> sigma/2−q` preserves both L and H_sigma,
and exchanges the two ground charges. This is a target symmetry, not a
microscopic deck or a selected physical vacuum.

In the uniform case the two charges are 0 and s. The standard L0 has
only one ground state, so no unitary conjugation plus positive rescaling
and vacuum-energy normalization identifies these two generators.
Restricting to charge-zero observables can change the physical question;
it does not prove equivalence of the full charged conformal structures.

## 3. Exact low-energy census and genuine charge carry

For even sign parity the 240 root-charge energies have multiplicities:

| H_sigma | 0 | 1/2 | 1 | 3/2 | 2 |
|---|---:|---:|---:|---:|---:|
| Root states | 1 | 56 | 126 | 56 | 1 |

For odd sign parity:

| H_sigma | 1/4 | 1/2 | 3/4 | 1 | 5/4 | 3/2 | 7/4 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Root states | 8 | 28 | 56 | 56 | 56 | 28 | 8 |

These are root-charge states, **not** the entire oscillator spectrum.
For norm level at least two, the lower bound is at least `2−sqrt(2)>1/2`.
Oscillators cost positive integers. Consequently the full target's first
positive energy is 1/2 in the even case and 1/4 in the odd case. These
are conditional target spectral gaps, not gaps of the microscopic TFPT
parent or the separate rotor model and not particle-mass predictions.

In particular the illustrative sign split `(+1)^5(−1)^3` has a unique
target ground state but is not thereby selected: the original s has
energy 3/4, not 1. No nonzero linear charge shift leaves all 240 root
weights equal to one, since the roots span R8.

The existing cocycle need not change. For the genuine lattice shift U_alpha,

    [H_sigma,U_alpha]
       = U_alpha(alpha·P + |alpha|²/2 − lambda_sigma·alpha).

For uniform signs the s ladder has energies `n²−n`: `0,0,2,6,12` at
n=0,...,4. The fourth step is still U_(4s), with energy 12 from the vacuum,
not a return to a four-state register. This preserves the distinction
between finite glue grade and unbounded charge carry.

## 4. Positive result: retain the offset and transfer energy domains

For every joint basis vector set x=L0>=0. The previous estimate implies
`|H_sigma−L0| <= sqrt(x)`, and `sqrt(x) <= (x+1)/2` gives

    1+L0 <= 2(1+H_sigma),
    1+H_sigma <= (3/2)(1+L0).

Both generators are diagonal in the same complete basis, so for every
real p>=0 these scalar bounds can be raised to p and summed in the
Hilbert norm. Hence

    D((1+L0)^p) = D((1+H_sigma)^p),
    ||(1+L0)^p psi|| <= 2^p ||(1+H_sigma)^p psi||,
    ||(1+H_sigma)^p psi|| <= (3/2)^p ||(1+L0)^p psi||.

The finite charge/oscillator span is a common core. In particular the
smooth energy domains coincide. A field bound
`||V_alpha(f) psi|| <= C ||f||_r ||(1+L0)^p psi||`
therefore becomes the same H_sigma bound with constant `2^p C`, without
deleting the source holonomy. The same applies separately to its adjoint.
This implication is conditional on having the stated target field and
the microscopic comparison maps; it does not create those maps.

Published target theory supports this route: Carpi–Tomassini prove energy
bounds for even positive lattice VOAs (Proposition 4.2) and for suitable
extensions with the same conformal vector (Theorem 4.6). Those results
cannot be used to assume the missing microscopic extension. See
[Energy bounds for vertex operator algebra extensions](https://link.springer.com/article/10.1007/s11005-023-01682-y).

## 5. Do not confuse an energy comparison with a new conformal structure

There are two different operations: keeping the ordinary unitary E8 VOA
and evolving by the charge-shifted H_sigma, or declaring H_sigma to be
the zero mode of a shifted Virasoro field. Dong–Mason's construction has
`L_lambda(n)=L(n)−(n+1)lambda·J(n)` and central charge
`c_lambda=8−12|lambda|²=2`, not 8. For real lambda, with the original
adjoints, `L_lambda(n)^*−L_lambda(−n)=−2n lambda·J(−n)` is nonzero.
Thus that direct improvement does not preserve the original unitary
c=8 conformal structure. This is not a claim that every spectral-flow
or background-connection construction is forbidden. Source:
[Dong–Mason, Section 3, equations 3.4, 3.8–3.9](https://arxiv.org/html/math/0411526#S3).

## Next acceptance test

Construct the renormalized half-charge inter-sector field with the
source holonomy retained and use the domain comparison above in its
energy estimates. Derive the relative channel holonomies and physical
charge sector from the actual marked source; do not select them because
one produces a preferred vacuum multiplicity. Then check source Ward
identities, adjoints, local smearing and charge/cocycle carry together.
The new calculation removes a possible energy-domain mismatch in the
**conditional target**, not the missing microscopic half-charge field.

`checker.py` and `test_checker.py` use exact fractions and pinned upstream
sources. The complete positivity/kernel/domain arguments are the written
all-charge proof above; finite tests are regression controls, not its
substitute. No publication paper, website, source pin or TOE marker is changed
by this post-publication branch.
