# Full five-value source filter: a sharper certified upper bound

Keeping the same matrix-product bond dimension four, a positive spectral
filter with five small integer weights yields the thermodynamic
variational upper bound

    e_ground <= 254850665/279993289 = approximately 0.9102027620.

This improves the quadratic-filter bound 53950/59177, approximately
0.9116717644. It is not the exact ground energy or a claim of global
optimality within the trial-state family.

## 1. Source filter with no change of Hamiltonian

The original h4 has eigenvalues k=0,...,4 and projectors P_k of ranks
binomial(4,k). Build them directly, without an eigensolver, as

    P_k=product_(j!=k)(h4-jI)/(k-j),
    F=sum_k f_k P_k.

Every such filter is a polynomial in the unchanged source h4 of degree
at most four. It acts on the intervening bonds in the same Bell-dimer
construction, with cell tensors A^{st}_{ab}=F_{st,ab}/2. Common scaling
of all f_k does not change the normalized trial state; below f0=1.

For real values f0,...,f4 define

    p=(f0^2+4f1^2+6f2^2+4f3^2+f4^2)/16,
    q=(4f1^2+12f2^2+12f3^2+4f4^2)/16,
    b=(f0 f3+3f1 f2+f1 f4+3f2 f3)/8.

The exact two bond energies and thermodynamic energy density are

    e_inside=q/p,
    e_between=2-2(b/p)^2,
    e=1+q/(2p)-(b/p)^2.

The checker verifies the five-value b formula using full physical
left/right insertions in the original source matrices, not merely a
formula copied from an optimization. It also checks reduction to the
previous quadratic-filter family.

## 2. Transfer and positivity

The full transfer remains diagonal in the sixteen Clifford words, with
degree-r eigenvalue

    d_r=(1/16)sum_k f_k^2
        sum_(j=0)^r (-1)^j binomial(r,j)binomial(4-r,k-j),

of multiplicity binomial(4,r). Its left and right Perron matrices are I,
with d0=p. These statements are checked with symbolic real f_k before
specializing to either witness.

For each positive witness below F is invertible. The sixteen Kraus
matrices therefore span M4, giving strict one-step positivity and a
primitive transfer. All subleading normalized rates are also checked
explicitly to have absolute value less than one.

## 3. Two transparent rational witnesses

The small integer weights [16,11,9,8,7], divided by 16, already give

    e=2134375/2343961 = approximately 0.9105846898.

The slightly larger weights [52,36,30,27,23], divided by 52, improve it
further to

    e=254850665/279993289 = approximately 0.9102027620.

Both are exact source-matrix contractions with both bond costs included.
The weights were selected using a numerical search as a guide. A local
numerical value near 0.910194615 appeared for approximately
[1,0.691407,0.577183,0.519737,0.437978]; neither its exact attainment nor
its global optimality is claimed. The acceptance consists of the
rational positive witnesses and their exact contractions instead.

## 4. Thermodynamic and physical scope

The finite periodic norm remains Tr(E^L)=sum_r binomial(4,r)d_r^L.
Finite-ring observable contractions have corresponding subleading
terms. The stated energy density is the thermodynamic fixed-point
limit justified by strict transfer dominance, not an exact energy
assigned to every finite ring.

These trial states provide upper bounds for the specified uniform
source Hamiltonian. They do not give a lower bound, prove a spectral
gap, select the physical parent, or close T1-T8. A numerical preference
within this small variational family is not a theory-selection rule.

## 5. Executed verification

The checker passed 63 exact checks under normal Python and Python -OO
with byte-identical JSON output. The scoped whitespace check passed.
It reconstructs the five projectors from original source matrices,
verifies their ranks and completeness, proves the general symbolic
transfer and both physical boundary formulas, then checks both positive
rational witnesses, their full normalized transfer spectra and exact
energy improvements. Numerical optimization is excluded from acceptance.
